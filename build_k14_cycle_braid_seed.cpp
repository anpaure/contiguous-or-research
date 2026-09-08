#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>
using namespace std;

static vector<int> read_values(const string& file) {
    ifstream in(file);
    vector<int> values;
    for (int x; in >> x;) values.push_back(x);
    return values;
}

static bool adjacent(int a, int b) {
    return popcount(static_cast<unsigned>(a ^ b)) == 2;
}

static int coverage(const vector<int>& path, int wanted_rank, int bits) {
    vector<uint8_t> seen(1 << bits);
    for (int i = 0; i + 1 < static_cast<int>(path.size()); ++i) {
        if (!adjacent(path[i], path[i + 1])) return -1;
        const int color = path[i] & path[i + 1];
        if (popcount(static_cast<unsigned>(color)) == wanted_rank) seen[color] = 1;
    }
    int count = 0;
    for (int x = 0; x < (1 << bits); ++x)
        count += seen[x] && popcount(static_cast<unsigned>(x)) == wanted_rank;
    return count;
}

static vector<int> piece_path(const vector<int>& base, int target,
                              int order, int directions) {
    vector<pair<int, int>> pieces;
    const pair<int, int> left{0, target - 1};
    const pair<int, int> right{target + 1, static_cast<int>(base.size()) - 1};
    array<pair<int, int>, 2> selected{left, right};
    if (order) swap(selected[0], selected[1]);
    vector<int> result{base[target]};
    for (int p = 0; p < 2; ++p) {
        auto [a, b] = selected[p];
        if (a > b) continue;
        if (directions & (1 << p)) swap(a, b);
        if (!adjacent(result.back(), base[a])) return {};
        const int step = a <= b ? 1 : -1;
        for (int i = a;; i += step) {
            result.push_back(base[i]);
            if (i == b) break;
        }
    }
    return result.size() == base.size() ? result : vector<int>{};
}

struct Eval {
    int deficit = 0;
    int rank5 = 0;
    int upper = 0;
    int total = 0;
};

static Eval evaluate(const vector<int>& path) {
    constexpr int k = 14, rank = 7, d = 2;
    Eval result;
    for (int bit = 0; bit < k; ++bit) {
        int i = 0;
        while (i < static_cast<int>(path.size())) {
            if (!(path[i] & (1 << bit))) { ++i; continue; }
            const int first = i;
            while (i < static_cast<int>(path.size()) && (path[i] & (1 << bit))) ++i;
            if (first && i < static_cast<int>(path.size()))
                result.deficit += max(0, d + 1 - (i - first));
        }
    }
    vector<uint8_t> seen(1 << k);
    for (int x : path) seen[x] = 1;
    for (int length = 2; length <= 3; ++length)
        for (int left = 0; left + length <= static_cast<int>(path.size()); ++left) {
            int x = (1 << k) - 1;
            for (int i = 0; i < length; ++i) x &= path[left + i];
            if (popcount(static_cast<unsigned>(x)) == rank - length + 1) seen[x] = 1;
        }
    for (int length = 2; rank + length - 1 <= k; ++length)
        for (int left = 0; left + length <= static_cast<int>(path.size()); ++left) {
            int x = 0;
            for (int i = 0; i < length; ++i) x |= path[left + i];
            if (popcount(static_cast<unsigned>(x)) == rank + length - 1) seen[x] = 1;
        }
    for (int x = 1; x < (1 << k); ++x) if (seen[x]) {
        ++result.total;
        const int r = popcount(static_cast<unsigned>(x));
        if (r == 5) ++result.rank5;
        if (r > rank) ++result.upper;
    }
    return result;
}

static bool better(const Eval& a, const Eval& b) {
    if (a.deficit != b.deficit) return a.deficit < b.deficit;
    if (a.rank5 != b.rank5) return a.rank5 > b.rank5;
    if (a.upper != b.upper) return a.upper > b.upper;
    return a.total > b.total;
}

int main(int argc, char** argv) {
    if (argc != 4) return 2;
    constexpr int old_bits = 13, old_full = (1 << old_bits) - 1;
    constexpr int high = 1 << old_bits;
    const vector<int> cycle = read_values(argv[1]);
    const vector<int> upper = read_values(argv[2]);
    if (cycle.size() != 3432 || upper.size() != 1716) return 3;
    for (int i = 0; i < static_cast<int>(cycle.size()); ++i)
        if (popcount(static_cast<unsigned>(cycle[i] ^ cycle[(i + 1) % cycle.size()])) != 1)
            return 4;
    vector<int> base(upper.size());
    transform(upper.begin(), upper.end(), base.begin(),
              [](int x) { return old_full ^ x; });
    if (coverage(base, 5, old_bits) != 1287) return 5;
    vector<int> position(1 << old_bits, -1);
    for (int i = 0; i < static_cast<int>(base.size()); ++i) position[base[i]] = i;

    Eval best;
    best.deficit = 1 << 30;
    vector<int> best_path;
    int best_omitted = -1, feasible_endpoint_repairs = 0;
    for (int omitted_position = 0;
         omitted_position < static_cast<int>(cycle.size()); ++omitted_position) {
        const int omitted = cycle[omitted_position];
        if (popcount(static_cast<unsigned>(omitted)) != 6) continue;
        const int target = position[omitted];
        if (target <= 0 || target + 1 >= static_cast<int>(base.size())) continue;
        vector<int> lower;
        lower.reserve(1716);
        for (int step = 1; step < static_cast<int>(cycle.size()); ++step) {
            const int x = cycle[(omitted_position + step) % cycle.size()];
            if (popcount(static_cast<unsigned>(x)) == 7) lower.push_back(x);
        }
        if (lower.size() != 1716 || (lower.back() & omitted) != omitted) return 6;
        for (int order = 0; order < 2; ++order)
            for (int directions = 0; directions < 4; ++directions) {
                vector<int> right = piece_path(base, target, order, directions);
                if (right.empty() || coverage(right, 5, old_bits) != 1287) continue;
                ++feasible_endpoint_repairs;
                for (int reverse_lower = 0; reverse_lower < 2; ++reverse_lower) {
                    if (reverse_lower) reverse(lower.begin(), lower.end());
                    vector<int> combined = lower;
                    for (int x : right) combined.push_back(high | x);
                    if (!adjacent(combined[1715], combined[1716])) return 7;
                    if (coverage(combined, 6, 14) != 3003) return 8;
                    Eval current = evaluate(combined);
                    if (better(current, best)) {
                        best = current;
                        best_path.swap(combined);
                        best_omitted = omitted;
                        cerr << "best omitted=" << omitted
                             << " endpoint_repairs=" << feasible_endpoint_repairs
                             << " deficit=" << best.deficit
                             << " rank5=" << best.rank5 << "/2002"
                             << " upper=" << best.upper << "/6478"
                             << " total=" << best.total << '\n';
                    }
                    if (reverse_lower) reverse(lower.begin(), lower.end());
                }
            }
    }
    if (best_path.empty()) {
        cerr << "no two-piece endpoint repair\n";
        return 9;
    }
    ofstream out(argv[3]);
    for (int x : best_path) out << x << ' ';
    out << '\n';
    cerr << "done feasible_endpoint_repairs=" << feasible_endpoint_repairs
         << " best_omitted=" << best_omitted
         << " deficit=" << best.deficit << " rank5=" << best.rank5
         << " upper=" << best.upper << " total=" << best.total << '\n';
}
