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
#include <vector>

using namespace std;

class GradedScorer {
    int k_;
    vector<uint32_t> seen_;
    uint32_t epoch_ = 0;

    int weight(int rank) const {
        const int middle = k_ / 2;
        const int distance = abs(rank - middle);
        if (distance == 0) return 1000;
        if (distance == 1) return 120;
        if (distance == 2) return 24;
        if (distance == 3) return 6;
        return 1;
    }

public:
    explicit GradedScorer(int k) : k_(k), seen_(1U << k) {}

    pair<int, int> operator()(const vector<int>& a, vector<int>* missing = nullptr) {
        if (++epoch_ == 0) fill(seen_.begin(), seen_.end(), 0), ++epoch_;
        int objective = 0, covered = 0;
        for (int length = 1; length < k_; ++length) {
            const int wanted_rank = length == 1 ? -1 : length + 1;
            int value = 0;
            for (int i = 0; i < length; ++i) value |= a[i];
            auto consider = [&] (int mask) {
                const int rank = popcount(static_cast<unsigned>(mask));
                const bool wanted = length == 1 ? rank <= 2 : rank == wanted_rank;
                if (wanted && seen_[mask] != epoch_) {
                    seen_[mask] = epoch_;
                    objective += weight(rank);
                    ++covered;
                }
            };
            consider(value);
            for (int left = 1; left + length <= static_cast<int>(a.size()); ++left) {
                value = 0;
                for (int j = left; j < left + length; ++j) value |= a[j];
                consider(value);
            }
        }
        if (missing) {
            missing->clear();
            for (int mask = 1; mask < (1 << k_); ++mask)
                if (seen_[mask] != epoch_) missing->push_back(mask);
        }
        return {objective, covered};
    }

    int maximum() const {
        int result = 0;
        for (int mask = 1; mask < (1 << k_); ++mask)
            result += weight(popcount(static_cast<unsigned>(mask)));
        return result;
    }
};

int main(int argc, char** argv) {
    const int k = argc > 1 ? stoi(argv[1]) : 8;
    const int n = argc > 2 ? stoi(argv[2]) : 72;
    const uint64_t iterations = argc > 3 ? stoull(argv[3]) : 500000000ULL;
    const uint64_t seed = argc > 4 ? stoull(argv[4]) : 0x6a09e667f3bcc909ULL;
    mt19937_64 rng(seed);
    uniform_real_distribution<double> real(0.0, 1.0);
    GradedScorer scorer(k);
    const int maximum = scorer.maximum();

    vector<int> required;
    for (int mask = 1; mask < (1 << k); ++mask)
        if (popcount(static_cast<unsigned>(mask)) <= 2) required.push_back(mask);
    if (static_cast<int>(required.size()) > n) return 2;

    int global_best = -1;
    for (uint64_t restart = 0, done = 0; done < iterations; ++restart) {
        vector<int> a;
        if (restart == 0 && argc >= 5 + n) {
            for (int i = 0; i < n; ++i) a.push_back(stoi(argv[5 + i]));
        } else {
            a = required;
            while (static_cast<int>(a.size()) < n) {
                int value = 0;
                const int rank = 1 + rng() % 3;
                while (popcount(static_cast<unsigned>(value)) < rank)
                    value |= 1 << (rng() % k);
                a.push_back(value);
            }
            shuffle(a.begin(), a.end(), rng);
        }

        vector<int> required_count(1 << k);
        for (int value : a)
            if (popcount(static_cast<unsigned>(value)) <= 2) ++required_count[value];

        auto [current, current_covered] = scorer(a);
        const uint64_t block = min<uint64_t>(300000, iterations - done);
        for (uint64_t it = 0; it < block; ++it, ++done) {
            const int operation = rng() % 16;
            int left = rng() % n, right = rng() % n;
            if (left > right) swap(left, right);
            const int old = a[left];
            int old_required = -1, new_required = -1;

            if (operation < 7) {
                swap(a[left], a[right]);
            } else if (operation < 10) {
                reverse(a.begin() + left, a.begin() + right + 1);
            } else {
                int proposal = old;
                if (operation < 13) proposal ^= 1 << (rng() % k);
                else {
                    proposal = 0;
                    const int rank = 1 + rng() % 3;
                    while (popcount(static_cast<unsigned>(proposal)) < rank)
                        proposal |= 1 << (rng() % k);
                }
                if (!proposal || popcount(static_cast<unsigned>(proposal)) > 4)
                    proposal = 1 << (rng() % k);
                if (popcount(static_cast<unsigned>(old)) <= 2) {
                    old_required = old;
                    --required_count[old];
                }
                if (popcount(static_cast<unsigned>(proposal)) <= 2) {
                    new_required = proposal;
                    ++required_count[proposal];
                }
                a[left] = proposal;
                if (old_required >= 0 && required_count[old_required] == 0) {
                    if (new_required >= 0) --required_count[new_required];
                    ++required_count[old_required];
                    a[left] = old;
                    continue;
                }
            }

            const auto [next, next_covered] = scorer(a);
            const double phase = double(it) / block;
            const double temperature = 160.0 * (1.0 - phase) + 0.05;
            if (next >= current || real(rng) < exp(double(next - current) / temperature)) {
                current = next;
                current_covered = next_covered;
            } else {
                if (operation < 7) swap(a[left], a[right]);
                else if (operation < 10) reverse(a.begin() + left, a.begin() + right + 1);
                else {
                    if (new_required >= 0) --required_count[new_required];
                    if (old_required >= 0) ++required_count[old_required];
                    a[left] = old;
                }
            }

            if (current > global_best) {
                global_best = current;
                vector<int> missing;
                scorer(a, &missing);
                cerr << "objective=" << current << '/' << maximum
                     << " covered=" << current_covered << '/' << ((1 << k) - 1)
                     << " at=" << done << " array:";
                for (int value : a) cerr << ' ' << value;
                cerr << " | missing:";
                for (int value : missing) cerr << ' ' << value;
                cerr << '\n';
                if (current == maximum) return 0;
            }
        }
    }
    return 1;
}
