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
#include <utility>
#include <vector>
using namespace std;

namespace {
constexpr int k = 14;
constexpr int central_rank = 7;
constexpr int target = 440;
constexpr int limit = 1 << k;

bool adjacent(int a, int b) {
    return popcount(static_cast<unsigned>(a ^ b)) == 2;
}

struct Eval {
    int deficit = 0;
    int critical = 0;
    int rank5 = 0;
    int upper8 = 0;
};

Eval evaluate(const vector<int>& path) {
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
    array<uint8_t, limit> seen5{}, seen8{};
    for (int i = 0; i + 1 < static_cast<int>(path.size()); ++i)
        seen8[path[i] | path[i + 1]] = 1;
    for (int i = 0; i + 2 < static_cast<int>(path.size()); ++i)
        seen5[path[i] & path[i + 1] & path[i + 2]] = 1;
    for (int mask = 0; mask < limit; ++mask) {
        const int rank = popcount(static_cast<unsigned>(mask));
        if (rank == 5) result.rank5 += seen5[mask];
        if (rank == 8) result.upper8 += seen8[mask];
    }
    result.critical = seen5[target];
    return result;
}

bool better(const Eval& a, const Eval& b) {
    return tie(a.critical, b.deficit, a.rank5, a.upper8) >
           tie(b.critical, a.deficit, b.rank5, b.upper8);
}

vector<pair<int, int>> valid_reversals(const vector<int>& path) {
    const int n = path.size();
    array<int, limit> position;
    position.fill(-1);
    for (int i = 0; i < n; ++i) position[path[i]] = i;
    vector<pair<int, int>> moves;

    // Prefix reversals: only the right seam must remain a Johnson edge.
    for (int remove = 0; remove < k; ++remove) if (path[0] & (1 << remove))
        for (int add = 0; add < k; ++add) if (!(path[0] & (1 << add))) {
            const int neighbor = path[0] ^ (1 << remove) ^ (1 << add);
            const int next_position = position[neighbor];
            const int right = next_position - 1;
            if (right >= 2 && right + 1 < n) moves.push_back({0, right});
        }

    for (int left = 1; left < n; ++left) {
        const int before = path[left - 1];
        for (int remove = 0; remove < k; ++remove) if (before & (1 << remove))
            for (int add = 0; add < k; ++add) if (!(before & (1 << add))) {
                const int neighbor = before ^ (1 << remove) ^ (1 << add);
                const int right = position[neighbor];
                if (right < left + 2) continue;
                if (right + 1 < n && !adjacent(path[left], path[right + 1])) continue;
                moves.push_back({left, right});
            }
    }
    sort(moves.begin(), moves.end());
    moves.erase(unique(moves.begin(), moves.end()), moves.end());
    return moves;
}

bool preserves_all_colors(const vector<int>& path, const vector<int>& counts,
                          int left, int right) {
    array<int, 4> masks{};
    array<int, 4> deltas{};
    int used = 0;
    auto change = [&](int color, int delta) {
        for (int i = 0; i < used; ++i) if (masks[i] == color) {
            deltas[i] += delta;
            return;
        }
        masks[used] = color;
        deltas[used] = delta;
        ++used;
    };
    if (left) {
        change(path[left - 1] & path[left], -1);
        change(path[left - 1] & path[right], +1);
    }
    if (right + 1 < static_cast<int>(path.size())) {
        change(path[right] & path[right + 1], -1);
        change(path[left] & path[right + 1], +1);
    }
    for (int i = 0; i < used; ++i)
        if (counts[masks[i]] + deltas[i] <= 0) return false;
    return true;
}

bool has_target(const vector<int>& path) {
    for (int i = 0; i + 2 < static_cast<int>(path.size()); ++i)
        if ((path[i] & path[i + 1] & path[i + 2]) == target) return true;
    return false;
}

bool reversal_creates_target(const vector<int>& path, int left, int right) {
    const int n = path.size();
    auto after = [&](int position) {
        return left <= position && position <= right
            ? path[left + right - position] : path[position];
    };
    array<int, 4> starts{left - 2, left - 1, right - 1, right};
    for (int start : starts)
        if (start >= 0 && start + 2 < n &&
            (after(start) & after(start + 1) & after(start + 2)) == target)
            return true;
    return false;
}
} // namespace

int main() {
    vector<int> original;
    for (int value; cin >> value;) original.push_back(value);
    if (original.size() != 3432 || has_target(original)) return 2;
    vector<int> original_counts(limit);
    for (int i = 0; i + 1 < static_cast<int>(original.size()); ++i)
        ++original_counts[original[i] & original[i + 1]];

    const Eval initial = evaluate(original);
    Eval best = initial;
    vector<int> best_path = original;
    pair<int, int> best_first{-1, -1}, best_second{-1, -1};
    long long first_hard = 0, second_valid = 0, second_hard = 0, target_moves = 0;

    const auto first_moves = valid_reversals(original);
    for (auto [first_left, first_right] : first_moves) {
        if (!preserves_all_colors(original, original_counts, first_left, first_right)) continue;
        ++first_hard;
        vector<int> path = original;
        reverse(path.begin() + first_left, path.begin() + first_right + 1);
        if (has_target(path)) {
            const Eval current = evaluate(path);
            if (better(current, best)) {
                best = current; best_path = path;
                best_first = {first_left, first_right}; best_second = {-1, -1};
            }
            continue;
        }
        vector<int> counts(limit);
        for (int i = 0; i + 1 < static_cast<int>(path.size()); ++i)
            ++counts[path[i] & path[i + 1]];
        for (auto [left, right] : valid_reversals(path)) {
            ++second_valid;
            if (!reversal_creates_target(path, left, right)) continue;
            ++target_moves;
            if (!preserves_all_colors(path, counts, left, right)) continue;
            ++second_hard;
            reverse(path.begin() + left, path.begin() + right + 1);
            const Eval current = evaluate(path);
            if (better(current, best)) {
                best = current; best_path = path;
                best_first = {first_left, first_right}; best_second = {left, right};
            }
            reverse(path.begin() + left, path.begin() + right + 1);
        }
    }

    cerr << "initial=" << initial.deficit << ',' << initial.critical << ','
         << initial.rank5 << ',' << initial.upper8
         << " best=" << best.deficit << ',' << best.critical << ','
         << best.rank5 << ',' << best.upper8
         << " first=[" << best_first.first << ',' << best_first.second << ']'
         << " second=[" << best_second.first << ',' << best_second.second << ']'
         << " first_valid=" << first_moves.size() << " first_hard=" << first_hard
         << " second_valid=" << second_valid << " target_moves=" << target_moves
         << " second_hard=" << second_hard << '\n';
    for (int value : best_path) cout << value << ' ';
    cout << '\n';
}
