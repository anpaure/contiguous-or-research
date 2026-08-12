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
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <string>
#include <tuple>
#include <vector>
using namespace std;

namespace {
constexpr int k = 14, limit = 1 << k;
bool adjacent(int a, int b) {
    return __builtin_popcount(static_cast<unsigned>(a ^ b)) == 2;
}
template<class Callback>
void for_neighbors(int mask, Callback callback) {
    for (int remove = 0; remove < k; ++remove) if (mask & (1 << remove))
        for (int add = 0; add < k; ++add) if (!(mask & (1 << add)))
            callback(mask ^ (1 << remove) ^ (1 << add));
}
bool preserves_colors(const vector<int>& path, const vector<int>& lower,
                      const vector<int>& upper, int left, int right,
                      int edge, bool reversed) {
    const int p = path[left - 1], q = path[right + 1];
    const int x = path[edge], y = path[edge + 1];
    const int first = reversed ? path[right] : path[left];
    const int last = reversed ? path[left] : path[right];
    array<int, 6> lm{}, um{}, ld{}, ud{};
    int ln = 0, un = 0;
    auto change = [](auto& masks, auto& deltas, int& used, int value, int delta) {
        for (int i = 0; i < used; ++i) if (masks[i] == value) {
            deltas[i] += delta; return;
        }
        masks[used] = value; deltas[used] = delta; ++used;
    };
    auto edge_change = [&](int a, int b, int delta) {
        change(lm, ld, ln, a & b, delta);
        change(um, ud, un, a | b, delta);
    };
    edge_change(p, path[left], -1);
    edge_change(path[right], q, -1);
    edge_change(x, y, -1);
    edge_change(p, q, +1);
    edge_change(x, first, +1);
    edge_change(last, y, +1);
    for (int i = 0; i < ln; ++i) if (lower[lm[i]] + ld[i] <= 0) return false;
    for (int i = 0; i < un; ++i) if (upper[um[i]] + ud[i] <= 0) return false;
    return true;
}
vector<int> relocate(const vector<int>& path, int left, int right,
                     int edge, bool reversed) {
    vector<int> result;
    result.reserve(path.size());
    auto append_block = [&]() {
        if (!reversed)
            result.insert(result.end(), path.begin() + left, path.begin() + right + 1);
        else
            for (int i = right; i >= left; --i) result.push_back(path[i]);
    };
    if (edge < left - 1) {
        result.insert(result.end(), path.begin(), path.begin() + edge + 1);
        append_block();
        result.insert(result.end(), path.begin() + edge + 1, path.begin() + left);
        result.insert(result.end(), path.begin() + right + 1, path.end());
    } else {
        result.insert(result.end(), path.begin(), path.begin() + left);
        result.insert(result.end(), path.begin() + right + 1, path.begin() + edge + 1);
        append_block();
        result.insert(result.end(), path.begin() + edge + 1, path.end());
    }
    return result;
}
struct Eval { int deficit = 0, target = 0, rank5 = 0, upper_missing = 0; };
bool has_union_target(const vector<int>& path, int target) {
    for (int left = 0; left < static_cast<int>(path.size()); ++left) {
        if (path[left] & ~target) continue;
        int value = 0;
        for (int right = left; right < static_cast<int>(path.size()) &&
             !(path[right] & ~target); ++right) {
            value |= path[right];
            if (value == target) return true;
        }
    }
    return false;
}
Eval evaluate(const vector<int>& path, int target, bool full_upper) {
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
    array<uint8_t, limit> seen5{}, seen_union{};
    for (int i = 0; i + 2 < static_cast<int>(path.size()); ++i) {
        const int value = path[i] & path[i + 1] & path[i + 2];
        if (__builtin_popcount(static_cast<unsigned>(value)) == 5) seen5[value] = 1;
    }
    if (full_upper)
        for (int left = 0; left < static_cast<int>(path.size()); ++left) {
            int value = 0;
            for (int right = left; right < static_cast<int>(path.size()); ++right) {
                value |= path[right]; seen_union[value] = 1;
                if (value == limit - 1) break;
            }
        }
    for (int mask = 0; mask < limit; ++mask) {
        const int rank = __builtin_popcount(static_cast<unsigned>(mask));
        if (rank == 5) result.rank5 += seen5[mask];
        if (full_upper && 9 <= rank && rank <= 11) result.upper_missing += !seen_union[mask];
    }
    const bool upper_target = __builtin_popcount(static_cast<unsigned>(target)) >= 9;
    result.target = upper_target ?
        (full_upper ? seen_union[target] : has_union_target(path, target)) :
        seen5[target];
    return result;
}
} // namespace

int main(int argc, char** argv) {
    const int target = argc > 1 ? stoi(argv[1]) : 3209;
    vector<int> path;
    for (int value; cin >> value;) path.push_back(value);
    const int n = path.size();
    if (n != 3432) return 2;
    vector<int> position(limit, -1), lower(limit), upper(limit);
    for (int i = 0; i < n; ++i) position[path[i]] = i;
    for (int i = 0; i + 1 < n; ++i) {
        if (!adjacent(path[i], path[i + 1])) return 3;
        ++lower[path[i] & path[i + 1]];
        ++upper[path[i] | path[i + 1]];
    }
    for (int mask = 0; mask < limit; ++mask) {
        const int rank = __builtin_popcount(static_cast<unsigned>(mask));
        if (rank == 6 && !lower[mask]) return 4;
        if (rank == 8 && !upper[mask]) return 5;
    }
    const Eval original = evaluate(path, target, true);
    Eval best = original;
    vector<int> best_path = path;
    int best_left = -1, best_right = -1, best_edge = -1;
    bool best_reversed = false;
    long long closed_segments = 0, splice_candidates = 0, color_valid = 0,
              run_valid = 0, target_valid = 0;
    struct Saved {
        Eval score;
        vector<int> path;
        int left, right, edge;
        bool reversed;
    };
    vector<Saved> saved;
    const char* dump_prefix = getenv("DUMP_PREFIX");
    const int top_k = getenv("TOP_K") ? max(1, stoi(getenv("TOP_K"))) : 64;
    auto better_score = [](const Eval& a, const Eval& b) {
        return tuple{a.upper_missing, -a.rank5} <
               tuple{b.upper_missing, -b.rank5};
    };
    auto save_candidate = [&](const Eval& score, const vector<int>& candidate,
                              int left, int right, int edge, bool reversed) {
        if (!dump_prefix) return;
        Saved value{score, candidate, left, right, edge, reversed};
        if (static_cast<int>(saved.size()) < top_k) {
            saved.push_back(std::move(value));
            return;
        }
        int worst = 0;
        for (int i = 1; i < static_cast<int>(saved.size()); ++i)
            if (better_score(saved[worst].score, saved[i].score)) worst = i;
        if (better_score(score, saved[worst].score)) saved[worst] = std::move(value);
    };

    for (int left = 1; left + 1 < n; ++left) {
        const int p = path[left - 1];
        for_neighbors(p, [&](int qmask) {
            const int qpos = position[qmask];
            const int right = qpos - 1;
            if (right < left || right + 1 >= n) return;
            ++closed_segments;
            for (int reverse_flag = 0; reverse_flag < 2; ++reverse_flag) {
                const bool reversed = reverse_flag;
                const int first = reversed ? path[right] : path[left];
                const int last = reversed ? path[left] : path[right];
                for_neighbors(first, [&](int xmask) {
                    const int edge = position[xmask];
                    if (edge < 0 || edge + 1 >= n) return;
                    if (!(edge < left - 1 || edge > right)) return;
                    if (!adjacent(last, path[edge + 1])) return;
                    ++splice_candidates;
                    if (!preserves_colors(path, lower, upper, left, right,
                                          edge, reversed)) return;
                    ++color_valid;
                    vector<int> candidate = relocate(path, left, right, edge, reversed);
                    const Eval quick = evaluate(candidate, target, false);
                    if (quick.deficit) return;
                    ++run_valid;
                    if (!quick.target) return;
                    ++target_valid;
                    const Eval current = evaluate(candidate, target, true);
                    save_candidate(current, candidate, left, right, edge, reversed);
                    if (current.upper_missing < best.upper_missing ||
                        (!best.target && current.target) ||
                        (current.upper_missing == best.upper_missing &&
                         current.rank5 > best.rank5)) {
                        best = current; best_path.swap(candidate);
                        best_left = left; best_right = right; best_edge = edge;
                        best_reversed = reversed;
                    }
                });
            }
        });
    }
    cerr << "original=" << original.deficit << ',' << original.target << ','
         << original.rank5 << ',' << original.upper_missing
         << " best=" << best.deficit << ',' << best.target << ',' << best.rank5 << ','
         << best.upper_missing << " relocation=[" << best_left << ',' << best_right
         << "]@" << best_edge << " reversed=" << best_reversed
         << " closed_segments=" << closed_segments
         << " splice_candidates=" << splice_candidates
         << " color_valid=" << color_valid << " run_valid=" << run_valid
         << " target_valid=" << target_valid << '\n';
    if (dump_prefix) {
        sort(saved.begin(), saved.end(), [&](const Saved& a, const Saved& b) {
            return better_score(a.score, b.score);
        });
        for (int i = 0; i < static_cast<int>(saved.size()); ++i) {
            const string filename = string(dump_prefix) + to_string(i) + ".txt";
            ofstream output(filename);
            for (int value : saved[i].path) output << value << ' ';
            output << '\n';
            cerr << "saved=" << i << " score=" << saved[i].score.upper_missing
                 << ',' << saved[i].score.rank5 << " move=[" << saved[i].left
                 << ',' << saved[i].right << "]@" << saved[i].edge
                 << "r" << saved[i].reversed << " file=" << filename << '\n';
        }
    }
    for (int value : best_path) cout << value << ' ';
    cout << '\n';
}
