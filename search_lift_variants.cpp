#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <random>
#include <vector>

using namespace std;

static bool verify(const vector<int>& a, int remove_a, int remove_b) {
    vector<uint8_t> seen(1 << 10);
    array<int, 32> previous{}, current{};
    int previous_size = 0;
    for (int position = 0; position < static_cast<int>(a.size()); ++position) {
        if (position == remove_a || position == remove_b) continue;
        int current_size = 0;
        current[current_size++] = a[position];
        for (int i = 0; i < previous_size; ++i) {
            const int next = previous[i] | a[position];
            if (next != current[current_size - 1]) current[current_size++] = next;
        }
        for (int i = 0; i < current_size; ++i) seen[current[i]] = 1;
        previous.swap(current);
        previous_size = current_size;
    }
    for (int mask = 1; mask < 1024; ++mask) if (!seen[mask]) return false;
    return true;
}

int main(int argc, char** argv) {
    const int trials = argc > 1 ? stoi(argv[1]) : 20;
    const uint64_t seed = argc > 2 ? stoull(argv[2]) : 1;
    vector<int> base;
    for (int value; cin >> value;) base.push_back(value);
    if (base.size() != 128) return 2;
    mt19937_64 rng(seed);
    uint64_t tested = 0;
    for (int trial = 0; trial < trials; ++trial) {
        vector<int> permutation(9);
        iota(permutation.begin(), permutation.end(), 0);
        shuffle(permutation.begin(), permutation.end(), rng);
        vector<int> old = base, transformed = base;
        if (rng() & 1) reverse(old.begin(), old.end());
        if (rng() & 1) reverse(transformed.begin(), transformed.end());
        vector<int> lifted = old;
        lifted.push_back(512);
        for (int mask : transformed) {
            int permuted = 0;
            for (int bit = 0; bit < 9; ++bit)
                if (mask & (1 << bit)) permuted |= 1 << permutation[bit];
            lifted.push_back(512 | permuted);
        }
        for (int first = 0; first < 257; ++first)
            for (int second = first + 1; second < 257; ++second) {
                ++tested;
                if (!verify(lifted, first, second)) continue;
                cerr << "FOUND trial=" << trial << " removed=" << first << ',' << second
                     << " tested=" << tested << '\n';
                for (int position = 0; position < 257; ++position)
                    if (position != first && position != second)
                        cout << lifted[position] << ' ';
                cout << '\n';
                return 0;
            }
    }
    cerr << "NONE trials=" << trials << " tested=" << tested << '\n';
    return 1;
}
