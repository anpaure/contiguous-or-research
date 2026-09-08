#include <algorithm>
#include <array>
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <limits>
#include <vector>

#ifdef _OPENMP
#include <omp.h>
#endif

// Exact finite diagnostic for the reverse star-forest peeling reduction.
// For every nontrivial T it computes
//
//   min_{A in T} deg(T)/deg(T-A) * r^{h_T(A)},
//
// where h_T(A) is the number of boundary endpoints unique to A.  It then
// maximizes this best peel over T, stratified by |T|.  The computation is
// evidence only; the asymptotic peeling inequality is not inferred from it.

static std::uint64_t factorial(int n) {
    std::uint64_t z = 1;
    for (int i = 2; i <= n; ++i) z *= static_cast<std::uint64_t>(i);
    return z;
}

int main(int argc, char** argv) {
    const int r = argc > 1 ? std::atoi(argv[1]) : 5;
    const int b = 2 * r + 1;
    const int rank = 4 * r;
    if (rank > 20 || b > 20) return 2;

    const int target_universe = 1 << b;
    std::vector<int> middle(target_universe, -1), lower(target_universe, -1);
    std::vector<std::uint32_t> endpoints(rank, 0);
    int next = 0;
    for (int layer = 0; layer < 2; ++layer) {
        const int length = layer == 0 ? r : r - 1;
        auto& table = layer == 0 ? middle : lower;
        for (int start = 1; start < b; ++start) {
            int target = 0;
            for (int j = 0; j < length; ++j) target |= 1 << ((start + j) % b);
            table[target] = next;
            endpoints[next] = (std::uint32_t{1} << start) |
                              (std::uint32_t{1} << ((start + length) % b));
            ++next;
        }
    }

    const std::size_t count = std::size_t{1} << rank;
    std::vector<std::uint64_t> exact(count, 0);
#pragma omp parallel for schedule(dynamic, 1)
    for (int code = 0; code < b * (b - 1); ++code) {
        const int first = code / (b - 1);
        const int second_slot = code % (b - 1);
        const int second = second_slot >= first ? second_slot + 1 : second_slot;
        std::vector<int> tail;
        for (int x = 0; x < b; ++x) if (x != first && x != second) tail.push_back(x);
        do {
            std::vector<int> word(b);
            word[0] = first;
            word[1] = second;
            for (int i = 2; i < b; ++i) word[i] = tail[i - 2];
            std::size_t hit = 0;
            for (int layer = 0; layer < 2; ++layer) {
                const int length = layer == 0 ? r : r - 1;
                const auto& table = layer == 0 ? middle : lower;
                int target = 0;
                for (int j = 0; j < length; ++j) target |= 1 << word[(1 + j) % b];
                for (int start = 1; start < b; ++start) {
                    if (table[target] >= 0) hit |= std::size_t{1} << table[target];
                    target ^= 1 << word[start % b];
                    target ^= 1 << word[(start + length) % b];
                }
            }
#pragma omp atomic update
            ++exact[hit];
        } while (std::next_permutation(tail.begin(), tail.end()));
    }

    std::vector<std::uint64_t> degree = exact;
    for (int bit = 0; bit < rank; ++bit) {
        const std::size_t flag = std::size_t{1} << bit;
        for (std::size_t mask = 0; mask < count; ++mask) {
            if ((mask & flag) == 0) degree[mask] += degree[mask | flag];
        }
    }

    std::vector<long double> worst(rank + 1, 0.0L);
    std::vector<std::size_t> witness(rank + 1, 0);
    for (std::size_t mask = 1; mask < count; ++mask) {
        const int size = __builtin_popcountll(static_cast<unsigned long long>(mask));
        if (size < 2 || degree[mask] == 0) continue;
        long double best = std::numeric_limits<long double>::infinity();
        for (int removed = 0; removed < rank; ++removed) {
            const std::size_t flag = std::size_t{1} << removed;
            if ((mask & flag) == 0) continue;
            const std::size_t base = mask ^ flag;
            std::uint32_t old_endpoints = 0;
            std::size_t work = base;
            while (work) {
                const int bit = __builtin_ctzll(static_cast<unsigned long long>(work));
                old_endpoints |= endpoints[bit];
                work &= work - 1;
            }
            const int h = __builtin_popcount(endpoints[removed] & ~old_endpoints);
            const long double priced =
                static_cast<long double>(degree[mask]) /
                static_cast<long double>(degree[base]) *
                std::pow(static_cast<long double>(r), h);
            best = std::min(best, priced);
        }
        if (best > worst[size]) {
            worst[size] = best;
            witness[size] = mask;
        }
    }

    long double overall = 0.0L;
    for (int size = 2; size <= rank; ++size) overall = std::max(overall, worst[size]);
    std::cout << std::setprecision(12)
              << "BOUNDARY_STAR_PEELING_DIAGNOSTIC r=" << r
              << " words=" << factorial(b)
              << " worst_best_peel=" << overall << '\n';
    for (int size = 2; size <= rank; ++size) {
        std::cout << "size=" << size << " value=" << worst[size]
                  << " mask=" << witness[size] << '\n';
    }
    return 0;
}
