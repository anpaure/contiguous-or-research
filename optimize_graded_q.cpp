#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <algorithm>
#include <bit>
#include <cmath>
#include <cstdint>
#include <iostream>
#include <random>
#include <vector>

using namespace std;

struct Evaluation {
    int violations = 0;
    vector<int> counts;
    int total = 0;
};

static Evaluation evaluate(const vector<int>& q, int k, int base_rank) {
    Evaluation result;
    for (int bit = 0; bit < k; ++bit) {
        int start = 0;
        while (start < static_cast<int>(q.size())) {
            if (!(q[start] & (1 << bit))) { ++start; continue; }
            int end = start + 1;
            while (end < static_cast<int>(q.size()) && (q[end] & (1 << bit))) ++end;
            if (start > 0 && end < static_cast<int>(q.size()) && end - start < 3)
                result.violations += 3 - (end - start);
            start = end;
        }
    }
    result.counts.resize(k - base_rank);
    vector<unsigned char> seen(1 << k);
    for (int length = 2; length <= k - base_rank + 1; ++length) {
        fill(seen.begin(), seen.end(), 0);
        const int wanted_rank = base_rank + length - 1;
        int count = 0;
        for (int left = 0; left + length <= static_cast<int>(q.size()); ++left) {
            int value = 0;
            for (int position = left; position < left + length; ++position)
                value |= q[position];
            if (popcount(static_cast<unsigned>(value)) == wanted_rank && !seen[value])
                seen[value] = 1, ++count;
        }
        result.counts[length - 2] = count;
        result.total += count;
    }
    return result;
}

int main(int argc, char** argv) {
    const int k = argc > 1 ? stoi(argv[1]) : 10;
    const uint64_t iterations = argc > 2 ? stoull(argv[2]) : 100000000ULL;
    const uint64_t seed = argc > 3 ? stoull(argv[3]) : 1;
    const int base_rank = argc > 4 ? stoi(argv[4]) : (k + 1) / 2;
    vector<int> q;
    for (int value; cin >> value;) q.push_back(value);
    if (q.empty()) return 2;
    Evaluation current = evaluate(q, k, base_rank), best = current;
    if (current.violations) return 2;
    int wanted_total = 0;
    for (int mask = 1; mask < (1 << k); ++mask)
        wanted_total += popcount(static_cast<unsigned>(mask)) > base_rank;
    mt19937_64 rng(seed);
    uniform_real_distribution<double> real(0.0, 1.0);
    cerr << "initial total=" << current.total << '/' << wanted_total << " counts:";
    for (int count : current.counts) cerr << ' ' << count;
    cerr << '\n';

    for (uint64_t iteration = 0; iteration < iterations; ++iteration) {
        const bool use_reverse = (rng() & 1) == 0;
        int left, middle = -1, right;
        if (use_reverse) {
            left = rng() % q.size(), right = rng() % q.size();
            if (left > right) swap(left, right);
            if (left == right) continue;
            ++right;
            reverse(q.begin() + left, q.begin() + right);
        } else {
            left = rng() % (q.size() + 1);
            middle = rng() % (q.size() + 1);
            right = rng() % (q.size() + 1);
            if (left > middle) swap(left, middle);
            if (middle > right) swap(middle, right);
            if (left > middle) swap(left, middle);
            if (left == middle || middle == right) continue;
            rotate(q.begin() + left, q.begin() + middle, q.begin() + right);
        }
        Evaluation next = evaluate(q, k, base_rank);
        const double phase = double(iteration % 200000) / 200000.0;
        const double temperature = 100.0 * (1.0 - phase) + 0.05;
        const int current_score = 100 * current.total - 20 * current.violations;
        const int next_score = 100 * next.total - 20 * next.violations;
        const bool accept = next_score >= current_score ||
            real(rng) < exp(double(next_score - current_score) / temperature);
        if (accept) current = next;
        else if (use_reverse) reverse(q.begin() + left, q.begin() + right);
        else {
            const int second_length = right - middle;
            rotate(q.begin() + left, q.begin() + left + second_length,
                   q.begin() + right);
        }

        if (!current.violations && current.total > best.total) {
            best = current;
            cerr << "total=" << best.total << '/' << wanted_total << " counts:";
            for (int count : best.counts) cerr << ' ' << count;
            cerr << " at=" << iteration << '\n';
        }
        if (!current.violations && current.total == wanted_total) {
            for (int value : q) cout << value << ' ';
            cout << '\n';
            return 0;
        }
    }
    return 1;
}
