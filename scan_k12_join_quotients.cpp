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

static int erase_bit(int x, int bit) {
    return (x & ((1 << bit) - 1)) | ((x >> (bit + 1)) << bit);
}

static vector<int> quotient(const vector<int>& a, int erased, int image) {
    vector<int> result;
    result.reserve(a.size());
    for (int x : a) {
        int y = erase_bit(x, erased);
        if (x & (1 << erased)) y |= image;
        if (!y) continue;
        if (result.empty() || result.back() != y) result.push_back(y);
    }
    return result;
}

static bool universal_without(const vector<int>& a, int skipped) {
    vector<unsigned char> seen(1 << 11);
    array<int, 32> previous{}, current{};
    int pn = 0;
    for (int position = 0; position < static_cast<int>(a.size()); ++position) {
        if (position == skipped) continue;
        int cn = 0;
        current[cn++] = a[position];
        for (int i = 0; i < pn; ++i) {
            int x = previous[i] | a[position];
            if (x != current[cn - 1]) current[cn++] = x;
        }
        for (int i = 0; i < cn; ++i) seen[current[i]] = 1;
        previous.swap(current); pn = cn;
    }
    for (int x = 1; x < (1 << 11); ++x) if (!seen[x]) return false;
    return true;
}

static vector<int> prune(vector<int> a, mt19937_64& rng) {
    vector<int> order(a.size());
    iota(order.begin(), order.end(), 0);
    shuffle(order.begin(), order.end(), rng);
    vector<unsigned char> alive(a.size(), 1);
    for (int chosen : order) {
        if (!alive[chosen]) continue;
        vector<int> candidate;
        candidate.reserve(a.size() - 1);
        for (int i = 0; i < static_cast<int>(a.size()); ++i)
            if (alive[i] && i != chosen) candidate.push_back(a[i]);
        if (universal_without(candidate, -1)) alive[chosen] = 0;
    }
    vector<int> result;
    for (int i = 0; i < static_cast<int>(a.size()); ++i) if (alive[i]) result.push_back(a[i]);
    return result;
}

int main(int argc, char** argv) {
    if (argc < 2) return 2;
    ifstream in(argv[1]);
    vector<int> a;
    for (int x; in >> x;) a.push_back(x);
    if (a.size() != 926) return 2;
    int best_length = 1e9, best_erased = -1, best_image = -1;
    vector<int> best;
    vector<int> histogram(a.size() + 1);
    for (int erased = 0; erased < 12; ++erased) {
        int local_length = 1e9, local_image = -1;
        for (int image = 0; image < (1 << 11); ++image) {
            vector<int> q = quotient(a, erased, image);
            ++histogram[q.size()];
            if (static_cast<int>(q.size()) < local_length) {
                local_length = q.size(); local_image = image;
            }
            if (static_cast<int>(q.size()) < best_length) {
                best_length = q.size(); best_erased = erased;
                best_image = image; best = move(q);
            }
        }
        cout << "erased=" << erased << " best_compressed_length=" << local_length
             << " image=" << local_image << '\n';
    }
    cout << "global_best length=" << best_length << " erased=" << best_erased
         << " image=" << best_image << '\n';
    cout << "histogram";
    for (int n = 0; n < static_cast<int>(histogram.size()); ++n)
        if (histogram[n]) cout << ' ' << n << ':' << histogram[n];
    cout << '\n';
    if (argc > 2) {
        ofstream out(argv[2]);
        for (int x : best) out << x << ' ';
        out << '\n';
    }
    if (argc > 3) {
        const int rounds = stoi(argv[3]);
        mt19937_64 rng(argc > 4 ? stoull(argv[4]) : 120011ULL);
        vector<int> pruned_best = best;
        for (int round = 0; round < rounds; ++round) {
            vector<int> candidate = prune(best, rng);
            if (candidate.size() < pruned_best.size()) {
                pruned_best = move(candidate);
                cout << "pruned_best round=" << round << " length=" << pruned_best.size() << '\n';
            }
        }
        if (argc > 5) {
            ofstream out(argv[5]);
            for (int x : pruned_best) out << x << ' ';
            out << '\n';
        }
    }
}
