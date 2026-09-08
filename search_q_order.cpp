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
#include <random>
#include <string>
#include <unordered_set>
#include <vector>

using namespace std;

struct Evaluation {
    int score;
    int violations;
    int lower_labels;
    int upper_labels;
    int high_labels;
    int johnson_edges;
};

static Evaluation evaluate(const vector<int>& q, int k, int q_rank) {
    int violations = 0;
    for (int bit = 0; bit < k; ++bit) {
        int start = 0;
        while (start < static_cast<int>(q.size())) {
            if (!(q[start] & (1 << bit))) { ++start; continue; }
            int end = start;
            while (end < static_cast<int>(q.size()) && (q[end] & (1 << bit))) ++end;
            if (start != 0 && end != static_cast<int>(q.size()) && end - start < 3)
                violations += 3 - (end - start);
            start = end;
        }
    }

    vector<uint8_t> lower(1 << k), upper(1 << k);
    int lower_count = 0, upper_count = 0, johnson = 0;
    for (int i = 0; i + 1 < static_cast<int>(q.size()); ++i) {
        const int intersection = q[i] & q[i + 1];
        const int union_value = q[i] | q[i + 1];
        if (popcount(static_cast<unsigned>(q[i] ^ q[i + 1])) == 2) ++johnson;
        if (popcount(static_cast<unsigned>(intersection)) == q_rank - 1 &&
            !lower[intersection]) lower[intersection] = 1, ++lower_count;
        if (popcount(static_cast<unsigned>(union_value)) == q_rank + 1 &&
            !upper[union_value]) upper[union_value] = 1, ++upper_count;
    }
    vector<uint8_t> high(1 << k);
    int high_count = 0;
    for (int left = 0; left < static_cast<int>(q.size()); ++left) {
        int value = 0;
        for (int right = left; right < static_cast<int>(q.size()); ++right) {
            value |= q[right];
            if (popcount(static_cast<unsigned>(value)) >= q_rank && !high[value])
                high[value] = 1, ++high_count;
            if (value == (1 << k) - 1) break;
        }
    }
    const bool noncentral_rank = q_rank != (k + 1) / 2;
    const int high_weight = (k >= 10 || noncentral_rank) ? 300 : 30;
    const int score = -100 * violations + high_weight * high_count +
        5 * lower_count + johnson;
    return {score, violations, lower_count, upper_count, high_count, johnson};
}

static bool construct_root(const vector<int>& q, int k, vector<int>& a) {
    const int n = q.size() + 2;
    a.assign(n, 0);
    for (int bit = 0; bit < k; ++bit) {
        array<uint8_t, 4> possible{1, 1, 1, 1};
        struct Parent { int8_t state = -1, value = -1; };
        vector<array<Parent, 4>> parent(q.size() + 1);
        for (int i = 0; i < static_cast<int>(q.size()); ++i) {
            array<uint8_t, 4> next{};
            for (int state = 0; state < 4; ++state) if (possible[state]) {
                for (int value = 0; value < 2; ++value) {
                    const bool window = (state >> 1) | (state & 1) | value;
                    if (window != static_cast<bool>(q[i] & (1 << bit))) continue;
                    const int next_state = ((state & 1) << 1) | value;
                    if (!next[next_state]) {
                        next[next_state] = 1;
                        parent[i + 1][next_state] = {
                            static_cast<int8_t>(state), static_cast<int8_t>(value)};
                    }
                }
            }
            possible = next;
        }
        int state = -1;
        for (int s = 0; s < 4; ++s) if (possible[s]) { state = s; break; }
        if (state < 0) return false;
        vector<int> bits(n);
        for (int i = q.size(); i > 0; --i) {
            const Parent p = parent[i][state];
            bits[i + 1] = p.value;
            state = p.state;
        }
        bits[0] = state >> 1;
        bits[1] = state & 1;
        for (int i = 0; i < n; ++i) if (bits[i]) a[i] |= 1 << bit;
    }
    return true;
}

int main(int argc, char** argv) {
    const int k = argc > 1 ? stoi(argv[1]) : 8;
    const uint64_t iterations = argc > 2 ? stoull(argv[2]) : 500000000ULL;
    const uint64_t seed = argc > 3 ? stoull(argv[3]) : 0x3c6ef372fe94f82bULL;
    const int wanted_candidates = argc > 4 ? stoi(argv[4]) : 100;
    vector<int> a;
    int value;
    while (cin >> value) a.push_back(value);
    if (a.size() < 3) return 2;
    vector<int> q;
    if (argc > 5 && string(argv[5]) == "q") {
        q = a;
    } else {
        for (int i = 0; i + 2 < static_cast<int>(a.size()); ++i)
            q.push_back(a[i] | a[i + 1] | a[i + 2]);
    }
    const int mutable_start = argc > 6 ? stoi(argv[6]) : 0;
    if (mutable_start < 0 || mutable_start >= static_cast<int>(q.size())) return 2;
    const int q_rank = argc > 7 ? stoi(argv[7]) : (k + 1) / 2;
    for (int mask : q)
        if (popcount(static_cast<unsigned>(mask)) != q_rank) return 2;

    mt19937_64 rng(seed);
    uniform_real_distribution<double> real(0.0, 1.0);
    Evaluation current = evaluate(q, k, q_rank), best = current;
    vector<int> best_q = q;
    unordered_set<uint64_t> emitted;
    int wanted_high = 0;
    for (int mask = 1; mask < (1 << k); ++mask)
        wanted_high += popcount(static_cast<unsigned>(mask)) >= q_rank;
    const int minimum_lower = k == 8 ? 54 : 0;
    cerr << "initial score=" << current.score << " violations=" << current.violations
         << " lower=" << current.lower_labels << " upper=" << current.upper_labels
         << " high=" << current.high_labels << " johnson=" << current.johnson_edges << '\n';

    for (uint64_t it = 0; it < iterations; ++it) {
        int i = mutable_start + rng() % (q.size() - mutable_start);
        int j = mutable_start + rng() % (q.size() - mutable_start);
        if (i > j) swap(i, j);
        const int operation = rng() & 7;
        if (operation < 3) swap(q[i], q[j]);
        else if (operation < 7) reverse(q.begin() + i, q.begin() + j + 1);
        else {
            if (i == j) continue;
            rotate(q.begin() + i, q.begin() + i + 1, q.begin() + j + 1);
        }

        const Evaluation next = evaluate(q, k, q_rank);
        const double phase = double(it % 300000) / 300000.0;
        const bool noncentral_rank = q_rank != (k + 1) / 2;
        const double maximum_temperature = (k >= 10 || noncentral_rank) ? 500.0 : 35.0;
        const double temperature = maximum_temperature * (1.0 - phase) + 0.05;
        if (next.score >= current.score ||
            real(rng) < exp(double(next.score - current.score) / temperature)) {
            current = next;
        } else {
            if (operation < 3) swap(q[i], q[j]);
            else if (operation < 7) reverse(q.begin() + i, q.begin() + j + 1);
            else rotate(q.begin() + i, q.begin() + j, q.begin() + j + 1);
        }

        if (!current.violations && current.high_labels == wanted_high &&
            current.lower_labels >= minimum_lower) {
            uint64_t hash = 0xcbf29ce484222325ULL;
            for (int x : q) hash = (hash ^ static_cast<unsigned>(x)) * 0x100000001b3ULL;
            if (emitted.insert(hash).second) {
                for (int x : q) cout << x << ' ';
                cout << '\n' << flush;
                if (static_cast<int>(emitted.size()) >= wanted_candidates) return 0;
            }
        }

        if (current.score > best.score) {
            best = current;
            best_q = q;
            cerr << "score=" << best.score << " violations=" << best.violations
                 << " lower=" << best.lower_labels << " upper=" << best.upper_labels
                 << " high=" << best.high_labels << " johnson=" << best.johnson_edges
                 << " at=" << it << " Q:";
            for (int x : best_q) cerr << ' ' << x;
            cerr << '\n';
        }
    }
    return 1;
}
