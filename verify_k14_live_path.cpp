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
#include <vector>

using namespace std;

namespace {
constexpr int k = 14;
constexpr int limit = 1 << k;

int choose(int n, int r) {
    if (r < 0 || r > n) return 0;
    r = min(r, n - r);
    int result = 1;
    for (int i = 1; i <= r; ++i) result = result * (n - r + i) / i;
    return result;
}
}  // namespace

int main() {
    vector<int> path;
    for (int value; cin >> value;) path.push_back(value);

    array<uint8_t, limit> vertices{}, lower{}, upper{}, triples{}, unions{};
    bool values_ok = true;
    for (int value : path) {
        values_ok &= 0 <= value && value < limit;
        if (0 <= value && value < limit) ++vertices[value];
        values_ok &= __builtin_popcount(static_cast<unsigned>(value)) == 7;
    }

    bool johnson = true;
    for (int i = 0; i + 1 < static_cast<int>(path.size()); ++i) {
        const int intersection = path[i] & path[i + 1];
        const int set_union = path[i] | path[i + 1];
        johnson &= __builtin_popcount(static_cast<unsigned>(path[i] ^ path[i + 1])) == 2;
        lower[intersection] = 1;
        upper[set_union] = 1;
    }
    for (int i = 0; i + 2 < static_cast<int>(path.size()); ++i) {
        const int value = path[i] & path[i + 1] & path[i + 2];
        if (__builtin_popcount(static_cast<unsigned>(value)) == 5) triples[value] = 1;
    }

    int forbidden_runs = 0;
    for (int bit = 0; bit < k; ++bit) {
        int i = 0;
        while (i < static_cast<int>(path.size())) {
            if (!(path[i] & (1 << bit))) {
                ++i;
                continue;
            }
            const int left = i;
            while (i < static_cast<int>(path.size()) && (path[i] & (1 << bit))) ++i;
            const int right = i - 1;
            if (left > 0 && right + 1 < static_cast<int>(path.size()) && right - left + 1 < 3)
                ++forbidden_runs;
        }
    }

    vector<int> previous, current;
    for (int value : path) {
        current.clear();
        current.push_back(value);
        for (int old : previous) {
            const int joined = old | value;
            if (joined != current.back()) current.push_back(joined);
        }
        for (int joined : current) unions[joined] = 1;
        previous.swap(current);
    }

    auto count_rank = [](const auto& seen, int rank) {
        int count = 0;
        for (int value = 0; value < limit; ++value)
            if (__builtin_popcount(static_cast<unsigned>(value)) == rank)
                count += !!seen[value];
        return count;
    };

    int distinct_vertices = 0;
    bool unique_vertices = true;
    for (int value = 0; value < limit; ++value) {
        distinct_vertices += vertices[value] != 0;
        unique_vertices &= vertices[value] <= 1;
    }
    cout << "length=" << path.size()
         << " distinct_rank7=" << distinct_vertices << '/' << choose(14, 7)
         << " unique=" << unique_vertices
         << " values_ok=" << values_ok
         << " johnson=" << johnson
         << " rank6_colors=" << count_rank(lower, 6) << '/' << choose(14, 6)
         << " rank8_colors=" << count_rank(upper, 8) << '/' << choose(14, 8)
         << " rank5_triples=" << count_rank(triples, 5) << '/' << choose(14, 5)
         << " forbidden_runs=" << forbidden_runs << '\n';
    for (int rank = 7; rank <= 14; ++rank)
        cout << "union_rank=" << rank << " covered=" << count_rank(unions, rank)
             << '/' << choose(14, rank) << '\n';

    const bool structural_ok = path.size() == static_cast<size_t>(choose(14, 7)) &&
        distinct_vertices == choose(14, 7) && unique_vertices && values_ok && johnson &&
        count_rank(lower, 6) == choose(14, 6) &&
        count_rank(upper, 8) == choose(14, 8) && forbidden_runs == 0;
    return structural_ok ? 0 : 1;
}
