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
#include <iostream>
#include <tuple>
#include <vector>
using namespace std;

namespace {
constexpr int k = 14, limit = 1 << k;
bool adjacent(int a, int b) {
    return popcount(static_cast<unsigned>(a ^ b)) == 2;
}
struct Eval {
    int deficit = 0, target = 0, rank5 = 0;
    int upper_missing = 0, rank9 = 0, rank10 = 0, rank11 = 0;
};
Eval evaluate(const vector<int>& path, int target) {
    Eval result;
    for (int bit = 0; bit < k; ++bit) {
        int i = 0;
        while (i < static_cast<int>(path.size())) {
            if (!(path[i] & (1 << bit))) { ++i; continue; }
            const int first = i;
            while (i < static_cast<int>(path.size()) && (path[i] & (1 << bit))) ++i;
            if (first && i < static_cast<int>(path.size()) && i - first < 3)
                result.deficit += 3 - (i - first);
        }
    }
    array<uint8_t, limit> seen_intersection{}, seen_union{};
    for (int i = 0; i + 2 < static_cast<int>(path.size()); ++i) {
        const int value = path[i] & path[i + 1] & path[i + 2];
        if (popcount(static_cast<unsigned>(value)) == 5) seen_intersection[value] = 1;
    }
    for (int left = 0; left < static_cast<int>(path.size()); ++left) {
        int value = 0;
        for (int right = left; right < static_cast<int>(path.size()); ++right) {
            value |= path[right];
            seen_union[value] = 1;
            if (value == limit - 1) break;
        }
    }
    for (int mask = 0; mask < limit; ++mask) {
        const int rank = popcount(static_cast<unsigned>(mask));
        if (rank == 5) result.rank5 += seen_intersection[mask];
        if (rank == 9) result.rank9 += seen_union[mask];
        if (rank == 10) result.rank10 += seen_union[mask];
        if (rank == 11) result.rank11 += seen_union[mask];
    }
    result.target = seen_intersection[target];
    result.upper_missing = (2002 - result.rank9) + (1001 - result.rank10) +
                           (364 - result.rank11);
    return result;
}
bool better(const Eval& a, const Eval& b) {
    return tie(a.deficit, b.target, a.upper_missing, b.rank5) <
           tie(b.deficit, a.target, b.upper_missing, a.rank5);
}
bool preserves(const vector<int>& path, const vector<int>& lower,
               const vector<int>& upper, int left, int right) {
    array<int, 4> lower_mask{}, upper_mask{}, lower_delta{}, upper_delta{};
    int lower_used = 0, upper_used = 0;
    auto change = [](auto& masks, auto& deltas, int& used, int mask, int delta) {
        for (int i = 0; i < used; ++i) if (masks[i] == mask) {
            deltas[i] += delta; return;
        }
        masks[used] = mask; deltas[used] = delta; ++used;
    };
    auto edge_change = [&](int a, int b, int delta) {
        change(lower_mask, lower_delta, lower_used, a & b, delta);
        change(upper_mask, upper_delta, upper_used, a | b, delta);
    };
    if (left) {
        edge_change(path[left - 1], path[left], -1);
        edge_change(path[left - 1], path[right], +1);
    }
    if (right + 1 < static_cast<int>(path.size())) {
        edge_change(path[right], path[right + 1], -1);
        edge_change(path[left], path[right + 1], +1);
    }
    for (int i = 0; i < lower_used; ++i)
        if (lower[lower_mask[i]] + lower_delta[i] <= 0) return false;
    for (int i = 0; i < upper_used; ++i)
        if (upper[upper_mask[i]] + upper_delta[i] <= 0) return false;
    return true;
}
} // namespace

int main(int argc, char** argv) {
    const int target = argc > 1 ? stoi(argv[1]) : 3209;
    vector<int> path;
    for (int value; cin >> value;) path.push_back(value);
    if (path.size() != 3432) return 2;
    vector<int> lower(limit), upper(limit);
    for (int i = 0; i + 1 < static_cast<int>(path.size()); ++i) {
        if (!adjacent(path[i], path[i + 1])) return 3;
        ++lower[path[i] & path[i + 1]];
        ++upper[path[i] | path[i + 1]];
    }
    for (int mask = 0; mask < limit; ++mask) {
        const int rank = popcount(static_cast<unsigned>(mask));
        if (rank == 6 && !lower[mask]) return 4;
        if (rank == 8 && !upper[mask]) return 5;
    }
    const Eval original = evaluate(path, target);
    Eval best = original;
    vector<int> best_path = path;
    int best_left = -1, best_right = -1;
    long long valid = 0, color_valid = 0, run_valid = 0;
    const int n = path.size();
    for (int left = 0; left < n; ++left)
        for (int right = left + 2; right < n; ++right) {
            if (left && !adjacent(path[left - 1], path[right])) continue;
            if (right + 1 < n && !adjacent(path[left], path[right + 1])) continue;
            ++valid;
            if (!preserves(path, lower, upper, left, right)) continue;
            ++color_valid;
            reverse(path.begin() + left, path.begin() + right + 1);
            const Eval current = evaluate(path, target);
            if (!current.deficit) ++run_valid;
            if (better(current, best)) {
                best = current; best_path = path;
                best_left = left; best_right = right;
            }
            reverse(path.begin() + left, path.begin() + right + 1);
        }
    cerr << "original=" << original.deficit << ',' << original.target << ','
         << original.rank5 << ',' << original.upper_missing
         << " best=" << best.deficit << ',' << best.target << ',' << best.rank5 << ','
         << best.upper_missing << " move=[" << best_left << ',' << best_right << ']'
         << " valid=" << valid << " color_valid=" << color_valid
         << " run_valid=" << run_valid << '\n';
    for (int value : best_path) cout << value << ' ';
    cout << '\n';
}
