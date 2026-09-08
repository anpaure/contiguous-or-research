#include <algorithm>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <numeric>
#include <random>
#include <vector>

static std::uint64_t choose_u64(int n, int k) {
    if (k < 0 || k > n) return 0;
    if (k > n - k) k = n - k;
    std::uint64_t z = 1;
    for (int i = 1; i <= k; ++i) z = z * static_cast<std::uint64_t>(n - k + i) / i;
    return z;
}

int main(int argc, char** argv) {
    const int r = argc > 1 ? std::atoi(argv[1]) : 8;
    const std::uint64_t seed = argc > 2 ? std::strtoull(argv[2], nullptr, 10) : 1;
    const std::uint64_t failure_cap = argc > 3 ? std::strtoull(argv[3], nullptr, 10) : 10000000ULL;
    const int b = 2 * r + 1;
    if (b > 25) return 2;
    const std::uint64_t middle_count = choose_u64(b, r);
    const std::uint64_t lower_count = choose_u64(b, r - 1);
    const std::uint64_t capacity = lower_count / (2 * r);
    std::vector<unsigned char> used_middle(std::size_t{1} << b, 0);
    std::vector<unsigned char> used_lower(std::size_t{1} << b, 0);
    std::vector<int> word(b);
    std::iota(word.begin(), word.end(), 0);
    std::mt19937_64 rng(seed);
    std::uint64_t accepted = 0, failures = 0, attempts = 0;
    while (failures < failure_cap && accepted < capacity) {
        std::shuffle(word.begin(), word.end(), rng);
        ++attempts;
        bool ok = true;
        std::vector<int> mm, ll;
        mm.reserve(2 * r);
        ll.reserve(2 * r);
        for (int start = 1; start < b && ok; ++start) {
            int m = 0, l = 0;
            for (int j = 0; j < r; ++j) {
                const int bit = 1 << word[(start + j) % b];
                m |= bit;
                if (j < r - 1) l |= bit;
            }
            if (used_middle[m] || used_lower[l]) ok = false;
            mm.push_back(m);
            ll.push_back(l);
        }
        if (!ok) {
            ++failures;
            continue;
        }
        for (int x : mm) used_middle[x] = 1;
        for (int x : ll) used_lower[x] = 1;
        ++accepted;
        failures = 0;
    }
    const long double lower_covered = static_cast<long double>(2 * r) * accepted / lower_count;
    const long double middle_covered = static_cast<long double>(2 * r) * accepted / middle_count;
    std::cout << "RANDOM_GREEDY_PUNCTURED_CONFIG r=" << r << " b=" << b
              << " seed=" << seed << " attempts=" << attempts
              << " accepted=" << accepted << " capacity_floor=" << capacity
              << " lower_covered=" << lower_covered
              << " middle_covered=" << middle_covered
              << " terminal_failures=" << failures << '\n';
    return 0;
}
