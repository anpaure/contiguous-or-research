#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#elif defined(__clang__)
#pragma clang optimize on
#endif

#include <algorithm>
#include <array>
#include <bit>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <random>
#include <vector>

using namespace std;

struct Result {
    int score = 0;
    int covered = 0;
    vector<int> array;
};

static int weight(int rank, int k) {
    const int distance = min(rank, k - rank);
    if (distance == 1) return 100;
    if (distance == 2) return 24;
    if (distance == 3) return 6;
    return 1;
}

// Turn an ordering of the middle layer into requests.  The state is the
// ordered partition of coordinates by equal last-occurrence time.  To make T
// a suffix union, request exactly the elements of T that are not strictly
// before the first block containing an element outside T.
static Result evaluate(int k, const vector<int>& order, int first_block) {
    const int universe = (1 << k) - 1;
    vector<int> blocks;
    vector<int> a;
    const int first = order.front();
    first_block &= first;
    if (first_block == 0 || first_block == first) return {};
    a.push_back(first ^ first_block);
    a.push_back(first_block);
    blocks.push_back(first_block);
    blocks.push_back(first ^ first_block);

    int present = first;
    for (int oi = 1; oi < static_cast<int>(order.size()); ++oi) {
        const int target = order[oi];
        int request = target & ~present;
        bool barrier = false;
        for (int block : blocks) {
            if (block & ~target) barrier = true;
            if (barrier) request |= block & target;
        }
        if (request == 0) request = target;
        a.push_back(request);

        vector<int> next{request};
        for (int block : blocks) {
            block &= ~request;
            if (block) next.push_back(block);
        }
        blocks.swap(next);
        present |= request;
    }

    vector<uint8_t> seen(1 << k);
    vector<int> previous;
    int covered = 0;
    for (int value : a) {
        vector<int> current{value};
        for (int suffix : previous) {
            suffix |= value;
            if (suffix != current.back()) current.push_back(suffix);
        }
        for (int mask : current) if (!seen[mask]) {
            seen[mask] = 1;
            ++covered;
        }
        previous.swap(current);
    }
    int score = 0;
    for (int mask = 1; mask < (1 << k); ++mask)
        if (seen[mask]) score += weight(popcount(static_cast<unsigned>(mask)), k);
    return {score, covered, move(a)};
}

static vector<int> reflected_combinations(int n, int r) {
    if (r == 0) return {0};
    if (r == n) return {(1 << n) - 1};
    vector<int> left = reflected_combinations(n - 1, r);
    vector<int> right = reflected_combinations(n - 1, r - 1);
    reverse(right.begin(), right.end());
    for (int& x : right) x |= 1 << (n - 1);
    left.insert(left.end(), right.begin(), right.end());
    return left;
}

int main(int argc, char** argv) {
    const int k = argc > 1 ? stoi(argv[1]) : 8;
    const uint64_t iterations = argc > 2 ? stoull(argv[2]) : 100000000ULL;
    const uint64_t seed = argc > 3 ? stoull(argv[3]) : 0x243f6a8885a308d3ULL;
    const int r = k / 2;
    vector<int> order = reflected_combinations(k, r);
    mt19937_64 rng(seed);
    if (seed & 1) reverse(order.begin(), order.end());
    rotate(order.begin(), order.begin() + seed % order.size(), order.end());
    uniform_real_distribution<double> real(0.0, 1.0);

    int first_block = order[0] & -order[0];
    Result current = evaluate(k, order, first_block);
    Result best = current;
    vector<int> best_order = order;
    int maximum = 0;
    for (int mask = 1; mask < (1 << k); ++mask)
        maximum += weight(popcount(static_cast<unsigned>(mask)), k);
    cerr << "initial objective=" << best.score << '/' << maximum
         << " covered=" << best.covered << '/' << ((1 << k) - 1) << ':';
    for (int x : best.array) cerr << ' ' << x;
    cerr << '\n';

    for (uint64_t it = 0; it < iterations; ++it) {
        const int operation = rng() & 7;
        int i = rng() % order.size();
        int j = rng() % order.size();
        if (i > j) swap(i, j);
        if (operation < 5) swap(order[i], order[j]);
        else reverse(order.begin() + i, order.begin() + j + 1);

        int proposed_block = first_block;
        if ((rng() & 31) == 0) {
            const int first = order.front();
            proposed_block = rng() & first;
            if (proposed_block == 0 || proposed_block == first)
                proposed_block = first & -first;
        }
        Result next = evaluate(k, order, proposed_block);
        const double phase = double(it % 200000) / 200000.0;
        const double temperature = 14.0 * (1.0 - phase) + 0.05;
        if (next.score >= current.score ||
            real(rng) < exp(double(next.score - current.score) / temperature)) {
            current = move(next);
            first_block = proposed_block;
        } else {
            if (operation < 5) swap(order[i], order[j]);
            else reverse(order.begin() + i, order.begin() + j + 1);
        }

        if (current.score > best.score) {
            best = current;
            best_order = order;
            cerr << "objective=" << best.score << '/' << maximum
                 << " covered=" << best.covered << '/' << ((1 << k) - 1)
                 << " at " << it << ":";
            for (int x : best.array) cerr << ' ' << x;
            cerr << " | order:";
            for (int x : best_order) cerr << ' ' << x;
            cerr << '\n';
            if (best.covered == (1 << k) - 1) return 0;
        }
    }
    return 1;
}
