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

class Scorer {
    int k_;
    vector<uint32_t> seen_;
    uint32_t epoch_ = 0;

public:
    explicit Scorer(int k) : k_(k), seen_(1U << k) {}

    int operator()(const vector<int>& a, vector<int>* missing = nullptr) {
        if (++epoch_ == 0) {
            fill(seen_.begin(), seen_.end(), 0);
            ++epoch_;
        }

        // Distinct ORs of subarrays ending at one position form an inclusion
        // chain, hence there are at most k+1 of them.  Extend that compressed
        // chain instead of enumerating all O(n^2) intervals.
        array<int, 32> previous{}, current{};
        int previous_size = 0;
        int result = 0;
        for (int value : a) {
            int current_size = 0;
            current[current_size++] = value;
            for (int i = 0; i < previous_size; ++i) {
                const int next = previous[i] | value;
                if (next != current[current_size - 1]) current[current_size++] = next;
            }
            for (int i = 0; i < current_size; ++i) {
                const int mask = current[i];
                if (mask != 0 && seen_[mask] != epoch_) {
                    seen_[mask] = epoch_;
                    const int rank = popcount(static_cast<unsigned>(mask));
                    const bool central = rank == k_ / 2 ||
                        ((k_ & 1) && rank == k_ / 2 + 1);
                    const bool near_central = rank == k_ / 2 - 1 ||
                        rank == k_ - k_ / 2 + 1;
                    result += 1 + 100 * central + 8 * near_central;
                }
            }
            swap(previous, current);
            previous_size = current_size;
        }

        if (missing) {
            missing->clear();
            for (int value = 1; value < (1 << k_); ++value) {
                if (seen_[value] != epoch_) missing->push_back(value);
            }
        }
        return result;
    }
};

int main(int argc, char** argv) {
    const int k = argc > 1 ? stoi(argv[1]) : 6;
    const int n = argc > 2 ? stoi(argv[2]) : 21;
    const uint64_t iterations = argc > 3 ? stoull(argv[3]) : 200000000ULL;
    const uint64_t seed = argc > n + 4 ? stoull(argv[n + 4])
                                       : 0x9e3779b97f4a7c15ULL;
    mt19937_64 rng(seed);
    uniform_real_distribution<double> real(0.0, 1.0);
    Scorer score(k);
    vector<int> best;
    int best_score = -1;
    const bool has_seed = argc >= n + 4;
    vector<int> initial_seed;
    if (has_seed) {
        initial_seed.resize(n);
        for (int i = 0; i < n; ++i) initial_seed[i] = stoi(argv[i + 4]);
    }
    for (uint64_t restart = 0, done = 0; done < iterations; ++restart) {
        vector<int> a(n);
        if (has_seed) {
            a = restart == 0 || best.empty() ? initial_seed : best;
        } else {
            for (int i = 0; i < n; ++i) a[i] = 1 + rng() % ((1 << k) - 1);
            // Singleton masks are mandatory; seed every restart with them.
            for (int bit = 0; bit < k; ++bit) a[bit] = 1 << bit;
            shuffle(a.begin(), a.end(), rng);
        }
        array<int, 20> singleton_count{};
        for (int value : a) {
            if (value && (value & (value - 1)) == 0) {
                ++singleton_count[countr_zero(static_cast<unsigned>(value))];
            }
        }
        int current = score(a);
        const uint64_t block = min<uint64_t>(5000000, iterations - done);
        for (uint64_t it = 0; it < block; ++it, ++done) {
            const int pos = rng() % n;
            const int operation = rng() & 15;
            int other = pos;
            const int old = a[pos];
            if (operation == 0) {
                other = rng() % n;
                swap(a[pos], a[other]);
            } else if (operation == 1) {
                other = rng() % n;
                if (other < pos) reverse(a.begin() + other, a.begin() + pos + 1);
                else reverse(a.begin() + pos, a.begin() + other + 1);
            } else {
                int proposal;
                const int move = rng() & 15;
                if (move < 3) proposal = 1 << (rng() % k);
                else if (move < 11) proposal = old ^ (1 << (rng() % k));
                else proposal = 1 + rng() % ((1 << k) - 1);
                if (proposal == 0) proposal = 1 << (rng() % k);
                a[pos] = proposal;
            }
            bool valid = true;
            int old_bit = -1;
            int new_bit = -1;
            if (operation > 1) {
                if (old && (old & (old - 1)) == 0) {
                    old_bit = countr_zero(static_cast<unsigned>(old));
                    --singleton_count[old_bit];
                }
                const int updated = a[pos];
                if (updated && (updated & (updated - 1)) == 0) {
                    new_bit = countr_zero(static_cast<unsigned>(updated));
                    ++singleton_count[new_bit];
                }
                valid = old_bit < 0 || singleton_count[old_bit] != 0;
            }
            if (!valid) {
                if (operation == 0) swap(a[pos], a[other]);
                else if (operation == 1) {
                    if (other < pos) reverse(a.begin() + other, a.begin() + pos + 1);
                    else reverse(a.begin() + pos, a.begin() + other + 1);
                } else {
                    if (new_bit >= 0) --singleton_count[new_bit];
                    if (old_bit >= 0) ++singleton_count[old_bit];
                    a[pos] = old;
                }
                continue;
            }
            const int next = score(a);
            const double temperature = 25.0 * (1.0 - double(it) / block) + 0.08;
            if (next >= current || real(rng) < exp(double(next - current) / temperature)) {
                current = next;
            } else {
                if (operation == 0) swap(a[pos], a[other]);
                else if (operation == 1) {
                    if (other < pos) reverse(a.begin() + other, a.begin() + pos + 1);
                    else reverse(a.begin() + pos, a.begin() + other + 1);
                } else {
                    if (new_bit >= 0) --singleton_count[new_bit];
                    if (old_bit >= 0) ++singleton_count[old_bit];
                    a[pos] = old;
                }
            }
            if (current > best_score) {
                best_score = current;
                best = a;
                vector<int> miss;
                score(best, &miss);
                const int covered = ((1 << k) - 1) - static_cast<int>(miss.size());
                const int middle_count = static_cast<int>([] (int n, int r) {
                        long long x = 1;
                        for (int i = 1; i <= r; ++i) x = x * (n - r + i) / i;
                        return x;
                    }(k, k / 2));
                const int central_layers = (k & 1) ? 2 : 1;
                const int near_rank = k / 2 - 1;
                const int near_count = near_rank >= 1
                    ? static_cast<int>([] (int n, int r) {
                        long long x = 1;
                        for (int i = 1; i <= r; ++i) x = x * (n - r + i) / i;
                        return x;
                    }(k, near_rank)) * 2
                    : 0;
                const int maximum = ((1 << k) - 1) +
                    100 * middle_count * central_layers + 8 * near_count;
                cerr << "objective " << best_score << '/' << maximum
                     << " covered " << covered << '/' << ((1 << k) - 1)
                     << " at " << done << ":";
                for (int x : best) cerr << ' ' << x;
                cerr << " | missing:";
                for (int x : miss) cerr << ' ' << x;
                cerr << '\n';
                if (best_score == maximum) return 0;
            }
        }
    }
    return 1;
}
