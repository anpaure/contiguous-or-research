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
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>
using namespace std;

namespace {
constexpr int k = 14, limit = 1 << k;

bool adjacent(int a, int b) {
    return popcount(static_cast<unsigned>(a ^ b)) == 2;
}

uint32_t edge_key(int a, int b) {
    if (a > b) swap(a, b);
    return (static_cast<uint32_t>(a) << k) | b;
}

struct Eval { int deficit = 0, rank5 = 0, upper8 = 0; };
struct Candidate {
    Eval eval;
    vector<int> path;
    pair<int, int> first, second;
    int missing = 0;
    uint64_t signature = 0;
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
    return result;
}

bool better(const Eval& a, const Eval& b) {
    return tie(a.deficit, b.rank5, b.upper8) < tie(b.deficit, a.rank5, a.upper8);
}

vector<pair<int, int>> valid_reversals(const vector<int>& path) {
    const int n = path.size();
    array<int, limit> position;
    position.fill(-1);
    for (int i = 0; i < n; ++i) position[path[i]] = i;
    vector<pair<int, int>> moves;
    for (int remove = 0; remove < k; ++remove) if (path[0] & (1 << remove))
        for (int add = 0; add < k; ++add) if (!(path[0] & (1 << add))) {
            const int neighbor = path[0] ^ (1 << remove) ^ (1 << add);
            const int right = position[neighbor] - 1;
            if (right >= 2 && right + 1 < n) moves.push_back({0, right});
        }
    for (int left = 1; left < n; ++left) {
        const int before = path[left - 1];
        for (int remove = 0; remove < k; ++remove) if (before & (1 << remove))
            for (int add = 0; add < k; ++add) if (!(before & (1 << add))) {
                const int right = position[before ^ (1 << remove) ^ (1 << add)];
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
    array<int, 4> masks{}, deltas{};
    int used = 0;
    auto change = [&](int color, int delta) {
        for (int i = 0; i < used; ++i) if (masks[i] == color) {
            deltas[i] += delta; return;
        }
        masks[used] = color; deltas[used] = delta; ++used;
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

int missing_colors_after(const vector<int>& path, const vector<int>& counts,
                         int current_missing, int left, int right) {
    array<int, 4> masks{}, deltas{};
    int used = 0;
    auto change = [&](int color, int delta) {
        for (int i = 0; i < used; ++i) if (masks[i] == color) {
            deltas[i] += delta; return;
        }
        masks[used] = color; deltas[used] = delta; ++used;
    };
    if (left) {
        change(path[left - 1] & path[left], -1);
        change(path[left - 1] & path[right], +1);
    }
    if (right + 1 < static_cast<int>(path.size())) {
        change(path[right] & path[right + 1], -1);
        change(path[left] & path[right + 1], +1);
    }
    int missing = current_missing;
    for (int i = 0; i < used; ++i) {
        const bool before = counts[masks[i]] > 0;
        const bool after = counts[masks[i]] + deltas[i] > 0;
        missing += before - after;
    }
    return missing;
}

unordered_set<uint32_t> bad_run_edges(const vector<int>& path) {
    unordered_set<uint32_t> result;
    const int n = path.size();
    for (int bit = 0; bit < k; ++bit) {
        int i = 0;
        while (i < n) {
            if (!(path[i] & (1 << bit))) { ++i; continue; }
            const int first = i;
            while (i < n && (path[i] & (1 << bit))) ++i;
            if (!first || i == n || i - first >= 3) continue;
            for (int edge = first - 1; edge <= i - 1; ++edge)
                result.insert(edge_key(path[edge], path[edge + 1]));
        }
    }
    return result;
}

uint64_t bad_signature(const vector<int>& path) {
    const auto bad = bad_run_edges(path);
    vector<uint32_t> keys(bad.begin(), bad.end());
    sort(keys.begin(), keys.end());
    uint64_t hash = 1469598103934665603ULL;
    for (uint32_t key : keys) {
        hash ^= key;
        hash *= 1099511628211ULL;
    }
    return hash;
}

bool removes_bad_edge(const vector<int>& path, int left, int right,
                      const unordered_set<uint32_t>& bad) {
    if (left && bad.count(edge_key(path[left - 1], path[left]))) return true;
    return right + 1 < static_cast<int>(path.size()) &&
           bad.count(edge_key(path[right], path[right + 1]));
}
} // namespace

int main(int argc, char** argv) {
    const int minimum_rank5 = argc > 1 ? stoi(argv[1]) : 1995;
    const int keep = argc > 2 ? stoi(argv[2]) : 0;
    const int intermediate_color_slack = argc > 3 ? stoi(argv[3]) : 0;
    vector<int> original;
    for (int value; cin >> value;) original.push_back(value);
    if (original.size() != 3432) return 2;
    vector<int> original_counts(limit);
    for (int i = 0; i + 1 < static_cast<int>(original.size()); ++i) {
        if (!adjacent(original[i], original[i + 1])) return 3;
        ++original_counts[original[i] & original[i + 1]];
    }
    int colors = 0;
    for (int mask = 0; mask < limit; ++mask)
        colors += popcount(static_cast<unsigned>(mask)) == 6 && original_counts[mask];
    if (colors != 3003) return 4;

    const Eval initial = evaluate(original);
    Eval best = initial;
    vector<int> best_path = original;
    pair<int, int> best_first{-1, -1}, best_second{-1, -1};
    pair<int, int> best_third{-1, -1};
    vector<Candidate> frontier;
    long long first_hard = 0, second_considered = 0, second_hard = 0,
              third_considered = 0, third_hard = 0;
    for (auto [first_left, first_right] : valid_reversals(original)) {
        const int first_missing = missing_colors_after(original, original_counts, 0,
                                                       first_left, first_right);
        if (first_missing > intermediate_color_slack) continue;
        ++first_hard;
        vector<int> path = original;
        reverse(path.begin() + first_left, path.begin() + first_right + 1);
        const Eval first_eval = evaluate(path);
        if (keep && first_eval.rank5 >= minimum_rank5 &&
            first_eval.deficit <= initial.deficit + 2)
            frontier.push_back({first_eval, path, {first_left, first_right},
                                {-1, -1}, first_missing, bad_signature(path)});
        if (!first_missing && first_eval.rank5 >= minimum_rank5 && better(first_eval, best)) {
            best = first_eval; best_path = path;
            best_first = {first_left, first_right}; best_second = {-1, -1};
        }
        const auto bad = bad_run_edges(path);
        if (bad.empty()) continue;
        vector<int> counts(limit);
        for (int i = 0; i + 1 < static_cast<int>(path.size()); ++i)
            ++counts[path[i] & path[i + 1]];
        int current_missing = 0;
        for (int mask = 0; mask < limit; ++mask)
            current_missing += popcount(static_cast<unsigned>(mask)) == 6 && !counts[mask];
        for (auto [left, right] : valid_reversals(path)) {
            if (!removes_bad_edge(path, left, right, bad)) continue;
            ++second_considered;
            const int second_missing =
                missing_colors_after(path, counts, current_missing, left, right);
            if (second_missing > intermediate_color_slack) continue;
            ++second_hard;
            reverse(path.begin() + left, path.begin() + right + 1);
            const Eval current = evaluate(path);
            if (keep && current.rank5 >= minimum_rank5 &&
                current.deficit <= initial.deficit + 2)
                frontier.push_back({current, path, {first_left, first_right},
                                    {left, right}, second_missing, bad_signature(path)});
            if (!second_missing && current.rank5 >= minimum_rank5 && better(current, best)) {
                best = current; best_path = path;
                best_first = {first_left, first_right}; best_second = {left, right};
            }
            reverse(path.begin() + left, path.begin() + right + 1);
        }
    }
    if (keep) {
        sort(frontier.begin(), frontier.end(), [](const Candidate& a, const Candidate& b) {
            if (better(a.eval, b.eval)) return true;
            if (better(b.eval, a.eval)) return false;
            if (a.missing != b.missing) return a.missing < b.missing;
            return a.signature < b.signature;
        });
        vector<Candidate> selected;
        unordered_map<uint64_t, int> per_signature;
        const int quota = max(1, keep / 100);
        for (Candidate& candidate : frontier) {
            if (static_cast<int>(selected.size()) >= keep) break;
            if (per_signature[candidate.signature] >= quota) continue;
            ++per_signature[candidate.signature];
            selected.push_back(move(candidate));
        }
        // Fill unused capacity after guaranteeing signature diversity.
        if (static_cast<int>(selected.size()) < keep)
            for (Candidate& candidate : frontier) {
                if (candidate.path.empty()) continue;
                selected.push_back(move(candidate));
                if (static_cast<int>(selected.size()) >= keep) break;
            }
        frontier.clear();
        for (Candidate& candidate : selected) {
            vector<int>& path = candidate.path;
            const auto bad = bad_run_edges(path);
            if (bad.empty()) continue;
            vector<int> counts(limit);
            for (int i = 0; i + 1 < static_cast<int>(path.size()); ++i)
                ++counts[path[i] & path[i + 1]];
            int current_missing = 0;
            for (int mask = 0; mask < limit; ++mask)
                current_missing += popcount(static_cast<unsigned>(mask)) == 6 && !counts[mask];
            for (auto [left, right] : valid_reversals(path)) {
                if (!removes_bad_edge(path, left, right, bad)) continue;
                ++third_considered;
                if (missing_colors_after(path, counts, current_missing, left, right) != 0)
                    continue;
                ++third_hard;
                reverse(path.begin() + left, path.begin() + right + 1);
                const Eval current = evaluate(path);
                if (current.rank5 >= minimum_rank5 && better(current, best)) {
                    best = current;
                    best_path = path;
                    best_first = candidate.first;
                    best_second = candidate.second;
                    best_third = {left, right};
                }
                reverse(path.begin() + left, path.begin() + right + 1);
            }
        }
    }
    cerr << "initial=" << initial.deficit << ',' << initial.rank5 << ',' << initial.upper8
         << " best=" << best.deficit << ',' << best.rank5 << ',' << best.upper8
         << " first=[" << best_first.first << ',' << best_first.second << ']'
         << " second=[" << best_second.first << ',' << best_second.second << ']'
         << " third=[" << best_third.first << ',' << best_third.second << ']'
         << " first_hard=" << first_hard << " second_considered=" << second_considered
         << " second_hard=" << second_hard
         << " frontier=" << frontier.size()
         << " third_considered=" << third_considered
         << " third_hard=" << third_hard << '\n';
    for (int value : best_path) cout << value << ' ';
    cout << '\n';
}
