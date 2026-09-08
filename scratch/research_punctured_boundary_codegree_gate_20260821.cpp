#include <algorithm>
#include <array>
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <limits>
#include <numeric>
#include <vector>

#ifdef _OPENMP
#include <omp.h>
#endif

static std::uint64_t factorial(int n) {
    std::uint64_t z = 1;
    for (int i = 2; i <= n; ++i) z *= static_cast<std::uint64_t>(i);
    return z;
}

static int find_root(std::array<int, 32>& parent, int x) {
    if (parent[x] != x) parent[x] = find_root(parent, parent[x]);
    return parent[x];
}

int main(int argc, char** argv) {
    const int r = argc > 1 ? std::atoi(argv[1]) : 5;
    const int b = 2 * r + 1;
    const int rank = 4 * r;
    if (rank > 20 || b > 20) return 2;
    const int label_universe = 1 << b;
    std::vector<int> is_middle(label_universe, -1), is_lower(label_universe, -1);
    std::vector<int> lengths, starts;
    auto mark_base = [&](int length, std::vector<int>& table) {
        for (int start = 1; start < b; ++start) {
            int mask = 0;
            for (int j = 0; j < length; ++j) mask |= 1 << ((start + j) % b);
            table[mask] = static_cast<int>(lengths.size());
            lengths.push_back(length);
            starts.push_back(start);
        }
    };
    mark_base(r, is_middle);
    mark_base(r - 1, is_lower);

    std::vector<std::uint64_t> exact(std::size_t{1} << rank, 0);
#pragma omp parallel for schedule(dynamic, 1)
    for (int code = 0; code < b * (b - 1); ++code) {
        const int first = code / (b - 1);
        const int second_index = code % (b - 1);
        const int second = second_index >= first ? second_index + 1 : second_index;
        std::vector<int> tail;
        for (int x = 0; x < b; ++x) if (x != first && x != second) tail.push_back(x);
        do {
            std::vector<int> word(b);
            word[0] = first;
            word[1] = second;
            for (int i = 2; i < b; ++i) word[i] = tail[i - 2];
            std::size_t hit_mask = 0;
            for (int which = 0; which < 2; ++which) {
                const int length = which == 0 ? r : r - 1;
                const auto& table = which == 0 ? is_middle : is_lower;
                int mask = 0;
                for (int j = 0; j < length; ++j) mask |= 1 << word[(1 + j) % b];
                for (int start = 1; start < b; ++start) {
                    if (table[mask] >= 0) hit_mask |= std::size_t{1} << table[mask];
                    mask ^= 1 << word[start % b];
                    mask ^= 1 << word[(start + length) % b];
                }
            }
#pragma omp atomic update
            ++exact[hit_mask];
        } while (std::next_permutation(tail.begin(), tail.end()));
    }

    auto codegrees = exact;
    for (int bit = 0; bit < rank; ++bit) {
        const std::size_t flag = std::size_t{1} << bit;
        for (std::size_t mask = 0; mask < codegrees.size(); ++mask) {
            if ((mask & flag) == 0) codegrees[mask] += codegrees[mask | flag];
        }
    }

    const long double degree = static_cast<long double>(2 * r) * factorial(r) * factorial(r + 1);
    struct Row {
        long double root = 0;
        std::uint64_t degree = 0;
        std::size_t mask = 0;
        int q = 0;
        int c = 0;
    };
    std::vector<Row> best(rank + 1);
    long double global_root = 0;
    for (std::size_t mask = 1; mask < codegrees.size(); ++mask) {
        const int t = __builtin_popcountll(static_cast<unsigned long long>(mask));
        if (t < 2 || codegrees[mask] == 0) continue;
        std::array<bool, 32> used{};
        std::array<int, 32> parent{};
        std::iota(parent.begin(), parent.end(), 0);
        for (int index = 0; index < rank; ++index) if (mask & (std::size_t{1} << index)) {
            const int left = starts[index];
            const int right = (left + lengths[index]) % b;
            used[left] = used[right] = true;
            int a = find_root(parent, left), c = find_root(parent, right);
            if (a != c) parent[c] = a;
        }
        int q = 0;
        std::array<bool, 32> roots{};
        for (int x = 0; x < b; ++x) if (used[x]) {
            ++q;
            roots[find_root(parent, x)] = true;
        }
        int components = std::count(roots.begin(), roots.end(), true);
        const long double scaled = static_cast<long double>(codegrees[mask]) / degree
                                 * std::pow(static_cast<long double>(r), q - 2);
        const long double root = std::pow(scaled, 1.0L / t);
        if (root > best[t].root) best[t] = {root, codegrees[mask], mask, q, components};
        global_root = std::max(global_root, root);
    }

    std::cout << std::setprecision(12)
              << "BC_GATE_CENSUS r=" << r << " b=" << b
              << " permutations=" << factorial(b)
              << " global_required_C=" << global_root << '\n';
    for (int t = 2; t <= rank; ++t) if (best[t].mask) {
        std::cout << "t=" << t << " q=" << best[t].q << " c=" << best[t].c
                  << " degree=" << best[t].degree << " required_C=" << best[t].root
                  << " targets=";
        for (int index = 0; index < rank; ++index) if (best[t].mask & (std::size_t{1} << index)) {
            std::cout << (lengths[index] == r ? 'M' : 'L') << starts[index] << ',';
        }
        std::cout << '\n';
    }
    return 0;
}
