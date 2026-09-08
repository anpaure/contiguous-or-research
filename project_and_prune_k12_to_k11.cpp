#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <algorithm>
#include <bit>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <numeric>
#include <random>
#include <string>
#include <vector>
using namespace std;

static bool covers_all_nonzero(const vector<int>& a, int k) {
    vector<unsigned char> seen(1 << k, 0);
    vector<int> previous, current;
    previous.reserve(k + 1);
    current.reserve(k + 1);
    for (int x : a) {
        current.clear();
        current.push_back(x);
        for (int y : previous) {
            const int z = x | y;
            if (z != current.back()) current.push_back(z);
        }
        // `previous` is an inclusion chain in its natural generation order;
        // equal adjacent OR values are the only duplicates.
        for (int y : current) seen[y] = 1;
        previous.swap(current);
    }
    for (int x = 1; x < (1 << k); ++x)
        if (!seen[x]) return false;
    return true;
}

static int erase_bit(int x, int bit) {
    const int low = x & ((1 << bit) - 1);
    const int high = x >> (bit + 1);
    return low | (high << bit);
}

static vector<int> project_by_deletion(const vector<int>& source, int bit) {
    vector<int> result;
    result.reserve(source.size());
    for (int x : source)
        if (!(x & (1 << bit))) result.push_back(erase_bit(x, bit));
    return result;
}

static vector<int> greedy_prune(vector<int> a, uint64_t seed, bool reverse_scan) {
    mt19937_64 rng(seed);
    bool changed = true;
    while (changed) {
        changed = false;
        vector<int> order(a.size());
        iota(order.begin(), order.end(), 0);
        if (seed) shuffle(order.begin(), order.end(), rng);
        else if (reverse_scan) reverse(order.begin(), order.end());

        vector<unsigned char> removed(a.size(), 0);
        for (int original_index : order) {
            int current_index = original_index;
            for (int j = 0; j < original_index; ++j)
                current_index -= removed[j];
            if (current_index < 0 || current_index >= (int)a.size()) continue;

            const int saved = a[current_index];
            a.erase(a.begin() + current_index);
            if (covers_all_nonzero(a, 11)) {
                removed[original_index] = 1;
                changed = true;
            } else {
                a.insert(a.begin() + current_index, saved);
            }
        }
    }
    return a;
}

int main(int argc, char** argv) {
    if (argc < 2) {
        cerr << "usage: project_and_prune_k12_to_k11 ARRAY [random_restarts]\n";
        return 2;
    }
    ifstream in(argv[1]);
    vector<int> source;
    for (int x; in >> x;) source.push_back(x);
    if (source.empty()) return 3;
    const int restarts = argc >= 3 ? stoi(argv[2]) : 0;

    vector<int> best;
    int best_bit = -1;
    for (int bit = 0; bit < 12; ++bit) {
        vector<int> projected = project_by_deletion(source, bit);
        if (!covers_all_nonzero(projected, 11)) {
            cerr << "projection theorem failed for bit " << bit << '\n';
            return 4;
        }
        cout << "bit=" << bit << " projected=" << projected.size();

        vector<int> candidate = greedy_prune(projected, 0, false);
        vector<int> reverse_candidate = greedy_prune(projected, 0, true);
        if (reverse_candidate.size() < candidate.size())
            candidate.swap(reverse_candidate);
        for (int run = 0; run < restarts; ++run) {
            vector<int> random_candidate =
                greedy_prune(projected, 0x9e3779b97f4a7c15ULL *
                              (1 + run + 131 * bit), false);
            if (random_candidate.size() < candidate.size())
                candidate.swap(random_candidate);
        }
        cout << " pruned=" << candidate.size() << '\n';
        if (best.empty() || candidate.size() < best.size()) {
            best = move(candidate);
            best_bit = bit;
        }
    }
    if (!covers_all_nonzero(best, 11)) return 5;
    cout << "best_bit=" << best_bit << " best_length=" << best.size() << '\n';
    for (int x : best) cout << x << ' ';
    cout << '\n';
}
