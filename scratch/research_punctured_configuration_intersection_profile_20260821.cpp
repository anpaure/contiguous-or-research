#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <map>
#include <tuple>
#include <vector>

#ifdef _OPENMP
#include <omp.h>
#endif

static std::uint64_t factorial(int n) {
    std::uint64_t z = 1;
    for (int i = 2; i <= n; ++i) z *= static_cast<std::uint64_t>(i);
    return z;
}

int main(int argc, char** argv) {
    const int r = argc > 1 ? std::atoi(argv[1]) : 5;
    const int b = 2 * r + 1;
    if (b > 20) return 2;
    const int rank = 4 * r;
    const int universe = 1 << b;
    std::vector<int> is_middle(universe, -1), is_lower(universe, -1);
    std::vector<std::pair<int, int>> base_vertices;
    auto mark_base = [&](int k, int layer, std::vector<int>& table) {
        for (int start = 1; start < b; ++start) {
            int mask = 0;
            for (int j = 0; j < k; ++j) mask |= 1 << ((start + j) % b);
            table[mask] = static_cast<int>(base_vertices.size());
            base_vertices.push_back({layer, mask});
        }
    };
    mark_base(r, 0, is_middle);
    mark_base(r - 1, 1, is_lower);

    const int thread_cap = 256;
    std::vector<std::array<std::uint64_t, 81>> local_hist(thread_cap);
    std::vector<std::uint64_t> local_pair(thread_cap, 0), local_count(thread_cap, 0);
    std::vector<std::vector<std::uint64_t>> local_matrix(
        thread_cap, std::vector<std::uint64_t>(rank * rank, 0));
    const bool collect_all_codegrees = rank <= 20;
    std::vector<std::uint64_t> exact_intersection_masks(
        collect_all_codegrees ? (std::size_t{1} << rank) : 0, 0);
    for (auto& a : local_hist) a.fill(0);

#pragma omp parallel for schedule(dynamic, 1)
    for (int code = 0; code < b * (b - 1); ++code) {
        const int first = code / (b - 1);
        int second_index = code % (b - 1);
        const int second = second_index >= first ? second_index + 1 : second_index;
#ifdef _OPENMP
        const int tid = omp_get_thread_num();
#else
        const int tid = 0;
#endif
        std::vector<int> tail;
        for (int x = 0; x < b; ++x) if (x != first && x != second) tail.push_back(x);
        do {
            std::vector<int> w(b);
            w[0] = first;
            w[1] = second;
            for (int i = 2; i < b; ++i) w[i] = tail[i - 2];
            int overlap = 0;
            std::array<int, 80> hit{};
            int hit_count = 0;
            for (int which = 0; which < 2; ++which) {
                const int k = which == 0 ? r : r - 1;
                const auto& table = which == 0 ? is_middle : is_lower;
                int mask = 0;
                for (int j = 0; j < k; ++j) mask |= 1 << w[(1 + j) % b];
                for (int start = 1; start < b; ++start) {
                    if (table[mask] >= 0) hit[hit_count++] = table[mask];
                    const int leaving = w[start % b];
                    const int entering = w[(start + k) % b];
                    mask ^= 1 << leaving;
                    mask ^= 1 << entering;
                }
            }
            overlap = hit_count;
            std::sort(hit.begin(), hit.begin() + hit_count);
            hit_count = static_cast<int>(std::unique(hit.begin(), hit.begin() + hit_count) - hit.begin());
            if (hit_count != overlap) std::abort();
            if (collect_all_codegrees) {
                std::size_t hit_mask = 0;
                for (int i = 0; i < hit_count; ++i) hit_mask |= std::size_t{1} << hit[i];
#pragma omp atomic update
                ++exact_intersection_masks[hit_mask];
            }
            for (int i = 0; i < hit_count; ++i) {
                for (int j = i + 1; j < hit_count; ++j) {
                    ++local_matrix[tid][hit[i] * rank + hit[j]];
                }
            }
            ++local_hist[tid][overlap];
            local_pair[tid] += static_cast<std::uint64_t>(overlap) * (overlap - 1) / 2;
            ++local_count[tid];
        } while (std::next_permutation(tail.begin(), tail.end()));
    }

    std::array<std::uint64_t, 81> hist{};
    std::uint64_t pair_sum = 0, count = 0;
    std::vector<std::uint64_t> matrix(rank * rank, 0);
    for (int t = 0; t < thread_cap; ++t) {
        pair_sum += local_pair[t];
        count += local_count[t];
        for (int j = 0; j <= rank; ++j) hist[j] += local_hist[t][j];
        for (int j = 0; j < rank * rank; ++j) matrix[j] += local_matrix[t][j];
    }
    if (count != factorial(b)) return 3;
    long double d_middle = 2.0L * r * factorial(r) * factorial(r + 1);
    std::cout << "PUNCTURED_CONFIG_INTERSECTION_CPP r=" << r
              << " b=" << b << " count=" << count
              << " pair_sum=" << pair_sum
              << " S_over_Dmiddle=" << static_cast<long double>(pair_sum) / d_middle
              << " S_over_rank_Dmiddle=" << static_cast<long double>(pair_sum) / (rank * d_middle)
              << " hist=";
    for (int j = 0; j <= rank; ++j) if (hist[j]) std::cout << j << ':' << hist[j] << ',';
    std::cout << '\n';
    std::map<std::tuple<int, int, int>, std::vector<std::uint64_t>> categories;
    for (int i = 0; i < rank; ++i) {
        for (int j = i + 1; j < rank; ++j) {
            const auto [li, mi] = base_vertices[i];
            const auto [lj, mj] = base_vertices[j];
            const int a = std::min(li, lj), c = std::max(li, lj);
            const int inter = __builtin_popcount(static_cast<unsigned>(mi & mj));
            categories[{a, c, inter}].push_back(matrix[i * rank + j]);
        }
    }
    for (const auto& [key, values] : categories) {
        auto [a, c, inter] = key;
        auto [lo, hi] = std::minmax_element(values.begin(), values.end());
        std::uint64_t sum = 0;
        for (auto value : values) sum += value;
        std::cout << "PAIR_CATEGORY layers=" << a << c << " inter=" << inter
                  << " count=" << values.size() << " min=" << *lo << " max=" << *hi
                  << " sum=" << sum << '\n';
    }
    if (collect_all_codegrees) {
        auto codegrees = exact_intersection_masks;
        for (int bit = 0; bit < rank; ++bit) {
            const std::size_t flag = std::size_t{1} << bit;
            for (std::size_t mask = 0; mask < codegrees.size(); ++mask) {
                if ((mask & flag) == 0) codegrees[mask] += codegrees[mask | flag];
            }
        }
        std::vector<std::uint64_t> max_codegree(rank + 1, 0), max_count(rank + 1, 0);
        for (std::size_t mask = 1; mask < codegrees.size(); ++mask) {
            const int t = __builtin_popcountll(static_cast<unsigned long long>(mask));
            if (codegrees[mask] > max_codegree[t]) {
                max_codegree[t] = codegrees[mask];
                max_count[t] = 1;
            } else if (codegrees[mask] == max_codegree[t]) {
                ++max_count[t];
            }
        }
        std::cout << "MAX_T_CODEGREES";
        for (int t = 1; t <= rank; ++t) {
            std::cout << ' ' << t << ':' << max_codegree[t] << 'x' << max_count[t];
        }
        std::cout << '\n';
    }
    return 0;
}
