#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <numeric>
#include <random>
#include <string>
#include <vector>

using namespace std;

static bool universal(const vector<int>& a, int bits, int* count_out = nullptr) {
    vector<uint8_t> seen(1 << bits);
    array<int, 32> previous{}, current{};
    int previous_size = 0;
    for (int x : a) {
        int current_size = 0;
        current[current_size++] = x;
        for (int i = 0; i < previous_size; ++i) {
            const int value = previous[i] | x;
            if (value != current[current_size - 1]) current[current_size++] = value;
        }
        for (int i = 0; i < current_size; ++i) seen[current[i]] = 1;
        previous.swap(current);
        previous_size = current_size;
    }
    int count = 0;
    for (int x = 1; x < (1 << bits); ++x) count += seen[x];
    if (count_out) *count_out = count;
    return count == (1 << bits) - 1;
}

static int delete_coordinate(int x, int bit) {
    const int low = x & ((1 << bit) - 1);
    const int high = x >> (bit + 1);
    return low | (high << bit);
}

static vector<int> filter_coordinate(const vector<int>& source, int bit) {
    vector<int> result;
    result.reserve(source.size());
    for (int x : source) {
        if ((x & (1 << bit)) == 0) result.push_back(delete_coordinate(x, bit));
    }
    return result;
}

static vector<int> greedy_prune(vector<int> a, mt19937_64& rng) {
    vector<int> order(a.size());
    iota(order.begin(), order.end(), 0);
    shuffle(order.begin(), order.end(), rng);

    vector<uint8_t> alive(a.size(), 1);
    vector<int> candidate;
    candidate.reserve(a.size());
    for (int chosen : order) {
        if (!alive[chosen]) continue;
        candidate.clear();
        for (int i = 0; i < static_cast<int>(a.size()); ++i)
            if (alive[i] && i != chosen) candidate.push_back(a[i]);
        if (universal(candidate, 11)) alive[chosen] = 0;
    }
    candidate.clear();
    for (int i = 0; i < static_cast<int>(a.size()); ++i)
        if (alive[i]) candidate.push_back(a[i]);
    return candidate;
}

static void write_array(const string& path, const vector<int>& a) {
    ofstream out(path);
    for (int x : a) out << x << ' ';
    out << '\n';
}

int main(int argc, char** argv) {
    if (argc < 2) {
        cerr << "usage: reduce_k12_to_k11 ARRAY [ROUNDS] [SEED] [PREFIX]\n";
        return 2;
    }
    const int rounds = argc > 2 ? stoi(argv[2]) : 200;
    const uint64_t seed = argc > 3 ? stoull(argv[3]) : 120011ULL;
    const string prefix = argc > 4 ? argv[4] : "k11_from_k12";

    ifstream input(argv[1]);
    vector<int> source;
    for (int x; input >> x;) source.push_back(x);
    if (source.empty() || !universal(source, 12)) {
        cerr << "input is not a universal 12-bit array\n";
        return 2;
    }

    vector<vector<int>> filtered(12);
    int best_bit = -1;
    vector<int> best;
    for (int bit = 0; bit < 12; ++bit) {
        filtered[bit] = filter_coordinate(source, bit);
        int covered = 0;
        const bool ok = universal(filtered[bit], 11, &covered);
        cerr << "bit=" << bit << " filtered_length=" << filtered[bit].size()
             << " covered=" << covered << "/2047 ok=" << ok << '\n';
        if (!ok) return 3;
        if (best_bit < 0 || filtered[bit].size() < best.size()) {
            best_bit = bit;
            best = filtered[bit];
        }
    }
    write_array(prefix + "_filtered_best.txt", best);
    cerr << "best filtered bit=" << best_bit << " length=" << best.size() << '\n';

    mt19937_64 rng(seed);
    // Mix all coordinates into the restart pool: a longer filtered seed can
    // still prune to a shorter irredundant subsequence.
    for (int round = 0; round < rounds; ++round) {
        const int bit = round % 12;
        vector<int> candidate = greedy_prune(filtered[bit], rng);
        if (candidate.size() < best.size()) {
            best = move(candidate);
            write_array(prefix + "_pruned_best.txt", best);
            cerr << "NEW_BEST round=" << round << " source_bit=" << bit
                 << " length=" << best.size() << '\n';
        }
        if ((round + 1) % 10 == 0)
            cerr << "progress=" << (round + 1) << '/' << rounds
                 << " best=" << best.size() << '\n';
    }

    int covered = 0;
    const bool ok = universal(best, 11, &covered);
    write_array(prefix + "_best.txt", best);
    cout << "best_length=" << best.size() << " covered=" << covered
         << "/2047 universal=" << ok << '\n';
    return ok ? 0 : 4;
}
