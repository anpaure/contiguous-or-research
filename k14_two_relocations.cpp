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
#include <sstream>
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

struct Move { int left, right, edge; bool reversed; };

vector<int> relocate(const vector<int>& path, const Move& move) {
    const auto [left, right, edge, reversed] = move;
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

bool preserves_colors(const vector<int>& path, const vector<int>& lower,
                      const vector<int>& upper, const Move& move) {
    const auto [left, right, edge, reversed] = move;
    const int p = path[left - 1], q = path[right + 1];
    const int x = path[edge], y = path[edge + 1];
    const int first = reversed ? path[right] : path[left];
    const int last = reversed ? path[left] : path[right];
    array<int, 6> lm{}, um{}, ld{}, ud{};
    int ln = 0, un = 0;
    auto change = [](auto& masks, auto& deltas, int& used, int value, int delta) {
        for (int i = 0; i < used; ++i) if (masks[i] == value) {
            deltas[i] += delta;
            return;
        }
        masks[used] = value;
        deltas[used] = delta;
        ++used;
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

bool run_free(const vector<int>& path) {
    for (int bit = 0; bit < k; ++bit) {
        int i = 0;
        while (i < static_cast<int>(path.size())) {
            if (!(path[i] & (1 << bit))) { ++i; continue; }
            const int first = i;
            while (i < static_cast<int>(path.size()) && (path[i] & (1 << bit))) ++i;
            if (first && i < static_cast<int>(path.size()) && i - first < 3)
                return false;
        }
    }
    return true;
}

bool has_triple(const vector<int>& path, int target) {
    for (int i = 0; i + 2 < static_cast<int>(path.size()); ++i)
        if ((path[i] & path[i + 1] & path[i + 2]) == target) return true;
    return false;
}

// Since relocation preserves every internal triple (even when the moved block
// is reversed), a new triple can only straddle one of the three new joins.
bool relocation_creates_target(const vector<int>& path, const Move& move,
                               int target) {
    struct Block { int first, last, step; };
    const auto [left, right, edge, reversed] = move;
    vector<Block> blocks;
    auto moved = [&]() -> Block {
        return reversed ? Block{right, left, -1} : Block{left, right, 1};
    };
    if (edge < left - 1) {
        blocks = {{0, edge, 1}, moved(), {edge + 1, left - 1, 1},
                  {right + 1, static_cast<int>(path.size()) - 1, 1}};
    } else {
        blocks = {{0, left - 1, 1}, {right + 1, edge, 1}, moved(),
                  {edge + 1, static_cast<int>(path.size()) - 1, 1}};
    }
    auto block_size = [](const Block& b) { return (b.last - b.first) / b.step + 1; };
    auto at = [&](const Block& b, int offset) { return path[b.first + offset * b.step]; };
    for (int join = 0; join + 1 < static_cast<int>(blocks.size()); ++join) {
        const Block& a = blocks[join];
        const Block& b = blocks[join + 1];
        const int as = block_size(a), bs = block_size(b);
        if (as >= 2 && (at(a, as - 2) & at(a, as - 1) & at(b, 0)) == target)
            return true;
        if (bs >= 2 && (at(a, as - 1) & at(b, 0) & at(b, 1)) == target)
            return true;
    }
    return false;
}

struct Eval { int rank5 = 0, upper_missing = 0, target_multiplicity = 0; };
Eval evaluate(const vector<int>& path, int target) {
    array<uint8_t, limit> seen5{}, seen_union{};
    Eval result;
    for (int i = 0; i + 2 < static_cast<int>(path.size()); ++i) {
        const int value = path[i] & path[i + 1] & path[i + 2];
        if (__builtin_popcount(static_cast<unsigned>(value)) == 5) seen5[value] = 1;
        result.target_multiplicity += value == target;
    }
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
        if (9 <= rank && rank <= 11) result.upper_missing += !seen_union[mask];
    }
    return result;
}

template<class Callback>
void enumerate_moves(const vector<int>& path, Callback callback) {
    const int n = path.size();
    vector<int> position(limit, -1);
    for (int i = 0; i < n; ++i) position[path[i]] = i;
    for (int left = 1; left + 1 < n; ++left) {
        const int p = path[left - 1];
        for_neighbors(p, [&](int qmask) {
            const int right = position[qmask] - 1;
            if (right < left || right + 1 >= n) return;
            for (int reverse_flag = 0; reverse_flag < 2; ++reverse_flag) {
                const bool reversed = reverse_flag;
                const int first = reversed ? path[right] : path[left];
                const int last = reversed ? path[left] : path[right];
                for_neighbors(first, [&](int xmask) {
                    const int edge = position[xmask];
                    if (edge < 0 || edge + 1 >= n) return;
                    if (!(edge < left - 1 || edge > right)) return;
                    if (!adjacent(last, path[edge + 1])) return;
                    callback(Move{left, right, edge, reversed});
                });
            }
        });
    }
}

void color_counts(const vector<int>& path, vector<int>& lower, vector<int>& upper) {
    lower.assign(limit, 0); upper.assign(limit, 0);
    for (int i = 0; i + 1 < static_cast<int>(path.size()); ++i) {
        ++lower[path[i] & path[i + 1]];
        ++upper[path[i] | path[i + 1]];
    }
}
} // namespace

int main(int argc, char** argv) {
    if (argc < 2) return 2;
    const int target = stoi(argv[1]);
    vector<int> preserved;
    for (int i = 2; i < argc; ++i) preserved.push_back(stoi(argv[i]));
    auto preserves_triples = [&](const vector<int>& path) {
        for (int value : preserved) if (!has_triple(path, value)) return false;
        return true;
    };
    auto missing_preserved_triples = [&](const vector<int>& path) {
        int missing = 0;
        for (int value : preserved) missing += !has_triple(path, value);
        return missing;
    };
    vector<int> original;
    for (int value; cin >> value;) original.push_back(value);
    if (original.size() != 3432 || has_triple(original, target)) return 3;

    vector<int> original_lower, original_upper;
    color_counts(original, original_lower, original_upper);
    const bool allow_first_bad_run = getenv("ALLOW_FIRST_BAD_RUN") != nullptr;
    vector<pair<vector<int>, Move>> first_paths;
    long long first_moves = 0, first_color = 0, first_run = 0;
    enumerate_moves(original, [&](const Move& move) {
        ++first_moves;
        if (!preserves_colors(original, original_lower, original_upper, move)) return;
        ++first_color;
        vector<int> path = relocate(original, move);
        const bool first_is_run_free = run_free(path);
        first_run += first_is_run_free;
        if (!allow_first_bad_run && !first_is_run_free) return;
        if (!preserves_triples(path)) return;
        first_paths.push_back({std::move(path), move});
    });

    Eval best_eval{0, 1 << 30};
    vector<int> best_path;
    Move best_first{-1, -1, -1, false}, best_second{-1, -1, -1, false};
    Move best_third{-1, -1, -1, false};
    long long second_moves = 0, second_target = 0, second_color = 0,
              second_run = 0, final_preserved = 0;
    const char* dump_prefix = getenv("DUMP_PREFIX");
    const bool third_repair = getenv("THIRD_REPAIR") != nullptr;
    const bool fourth_repair = getenv("FOURTH_REPAIR") != nullptr;
    const bool fifth_repair = getenv("FIFTH_REPAIR") != nullptr;
    const bool allow_defect_swap = getenv("ALLOW_DEFECT_SWAP") != nullptr;
    vector<int> protected_masks;
    if (const char* raw = getenv("PROTECTED_MASKS")) {
        istringstream input(raw);
        for (int value; input >> value;) protected_masks.push_back(value);
    }
    const int beam_width = getenv("BEAM_WIDTH") ?
        max(1, stoi(getenv("BEAM_WIDTH"))) : 128;
    const bool rank5_first = getenv("RANK5_FIRST") != nullptr;
    const bool ignore_secondary = getenv("IGNORE_SECONDARY") != nullptr;
    const bool target_multiplicity_second =
        getenv("TARGET_MULTIPLICITY_SECOND") != nullptr;
    const bool target_multiplicity_first =
        getenv("TARGET_MULTIPLICITY_FIRST") != nullptr;
    const uint64_t tie_seed = getenv("TIE_SEED") ?
        stoull(getenv("TIE_SEED")) : 0;
    auto is_better = [&](const Eval& candidate, const Eval& incumbent) {
        if (rank5_first) {
            if (target_multiplicity_first)
                return tuple{-candidate.target_multiplicity, -candidate.rank5,
                             candidate.upper_missing} <
                       tuple{-incumbent.target_multiplicity, -incumbent.rank5,
                             incumbent.upper_missing};
            if (target_multiplicity_second)
                return tuple{-candidate.rank5, -candidate.target_multiplicity,
                             candidate.upper_missing} <
                       tuple{-incumbent.rank5, -incumbent.target_multiplicity,
                             incumbent.upper_missing};
            if (ignore_secondary)
                return candidate.rank5 > incumbent.rank5;
            return tuple{-candidate.rank5, candidate.upper_missing} <
                   tuple{-incumbent.rank5, incumbent.upper_missing};
        }
        if (ignore_secondary)
            return candidate.upper_missing < incumbent.upper_missing;
        return tuple{candidate.upper_missing, -candidate.rank5} <
               tuple{incumbent.upper_missing, -incumbent.rank5};
    };
    auto path_hash = [&](const vector<int>& path) {
        uint64_t h = tie_seed ^ 0x9e3779b97f4a7c15ULL;
        for (int value : path) {
            h ^= static_cast<uint64_t>(value) + 0x9e3779b97f4a7c15ULL +
                 (h << 6) + (h >> 2);
            h *= 0xbf58476d1ce4e5b9ULL;
        }
        return h;
    };
    auto score_equal = [&](const Eval& a, const Eval& b) {
        return !is_better(a, b) && !is_better(b, a);
    };
    uint64_t best_path_hash = UINT64_MAX;
    int best_swap_defect = 1 << 30;
    Eval best_swap_eval{0, 1 << 30};
    vector<int> best_swap_path;
    uint64_t best_swap_hash = UINT64_MAX;
    auto consider_defect_swap = [&](const vector<int>& candidate, int defect) {
        if (!allow_defect_swap || defect <= 0 ||
            !has_triple(candidate, target)) return;
        for (int value : protected_masks)
            if (!has_triple(candidate, value)) return;
        const Eval score = evaluate(candidate, target);
        const bool primary_better = defect < best_swap_defect ||
            (defect == best_swap_defect && is_better(score, best_swap_eval));
        const bool tied = defect == best_swap_defect &&
            score_equal(score, best_swap_eval);
        const uint64_t hash = tie_seed && (primary_better || tied) ?
            path_hash(candidate) : UINT64_MAX;
        if (primary_better || (tie_seed && tied && hash < best_swap_hash)) {
            best_swap_defect = defect;
            best_swap_eval = score;
            best_swap_path = candidate;
            best_swap_hash = hash;
        }
    };
    struct Intermediate { vector<int> path; Move first, second; };
    vector<Intermediate> bad_run_paths;
    for (const auto& [path, first_move] : first_paths) {
        vector<int> lower, upper;
        color_counts(path, lower, upper);
        enumerate_moves(path, [&](const Move& move) {
            ++second_moves;
            if (!relocation_creates_target(path, move, target)) return;
            ++second_target;
            if (!preserves_colors(path, lower, upper, move)) return;
            ++second_color;
            vector<int> candidate = relocate(path, move);
            const bool candidate_run_free = run_free(candidate);
            const bool candidate_preserves = preserves_triples(candidate);
            if (third_repair && has_triple(candidate, target) &&
                (!candidate_run_free || !candidate_preserves)) {
                bad_run_paths.push_back({candidate, first_move, move});
            }
            if (!candidate_run_free) return;
            ++second_run;
            if (!candidate_preserves) return;
            ++final_preserved;
            const Eval score = evaluate(candidate, target);
            if (dump_prefix) {
                const string filename = string(dump_prefix) +
                    to_string(final_preserved) + ".txt";
                ofstream output(filename);
                for (int value : candidate) output << value << ' ';
                output << '\n';
                cerr << "candidate=" << final_preserved
                     << " rank5=" << score.rank5
                     << " upper_missing=" << score.upper_missing
                     << " file=" << filename << '\n';
            }
            const bool primary_better = is_better(score, best_eval);
            const bool tied = score_equal(score, best_eval);
            const uint64_t hash = tie_seed && (primary_better || tied) ?
                path_hash(candidate) : UINT64_MAX;
            if (primary_better || (tie_seed && tied && hash < best_path_hash)) {
                best_eval = score;
                best_path.swap(candidate);
                best_path_hash = hash;
                best_first = first_move;
                best_second = move;
            }
        });
    }

    long long third_moves = 0, third_color = 0, third_run = 0,
              third_preserved = 0;
    struct FourthIntermediate {
        vector<int> path;
        Move first, second, third;
    };
    vector<FourthIntermediate> fourth_paths;
    int fourth_seed_missing = 1 << 30;
    const int max_fourth_seeds = beam_width;
    for (const Intermediate& intermediate : bad_run_paths) {
        vector<int> lower, upper;
        color_counts(intermediate.path, lower, upper);
        enumerate_moves(intermediate.path, [&](const Move& move) {
            ++third_moves;
            if (!preserves_colors(intermediate.path, lower, upper, move)) return;
            ++third_color;
            vector<int> candidate = relocate(intermediate.path, move);
            if (!run_free(candidate)) return;
            ++third_run;
            const int missing = missing_preserved_triples(candidate);
            consider_defect_swap(candidate, missing);
            const int defect = missing + !has_triple(candidate, target);
            if (fourth_repair && defect > 0) {
                if (defect < fourth_seed_missing) {
                    fourth_seed_missing = defect;
                    fourth_paths.clear();
                }
                if (defect == fourth_seed_missing &&
                    static_cast<int>(fourth_paths.size()) < max_fourth_seeds) {
                    fourth_paths.push_back(
                        {candidate, intermediate.first, intermediate.second, move});
                }
            }
            if (defect != 0) return;
            ++third_preserved;
            const Eval score = evaluate(candidate, target);
            if (dump_prefix) {
                const string filename = string(dump_prefix) + "third_" +
                    to_string(third_preserved) + ".txt";
                ofstream output(filename);
                for (int value : candidate) output << value << ' ';
                output << '\n';
                cerr << "third_candidate=" << third_preserved
                     << " rank5=" << score.rank5
                     << " upper_missing=" << score.upper_missing
                     << " file=" << filename << '\n';
            }
            const bool primary_better = is_better(score, best_eval);
            const bool tied = score_equal(score, best_eval);
            const uint64_t hash = tie_seed && (primary_better || tied) ?
                path_hash(candidate) : UINT64_MAX;
            if (primary_better || (tie_seed && tied && hash < best_path_hash)) {
                best_eval = score;
                best_path.swap(candidate);
                best_path_hash = hash;
                best_first = intermediate.first;
                best_second = intermediate.second;
                best_third = move;
            }
        });
    }

    long long fourth_moves = 0, fourth_color = 0, fourth_run = 0,
              fourth_preserved = 0;
    struct FifthIntermediate {
        vector<int> path;
        Move first, second, third, fourth;
    };
    vector<FifthIntermediate> fifth_paths;
    int fifth_seed_defect = 1 << 30;
    const int max_fifth_seeds = beam_width;
    Move best_fourth{-1, -1, -1, false};
    for (const FourthIntermediate& intermediate : fourth_paths) {
        vector<int> lower, upper;
        color_counts(intermediate.path, lower, upper);
        enumerate_moves(intermediate.path, [&](const Move& move) {
            ++fourth_moves;
            if (!preserves_colors(intermediate.path, lower, upper, move)) return;
            ++fourth_color;
            vector<int> candidate = relocate(intermediate.path, move);
            if (!run_free(candidate)) return;
            ++fourth_run;
            const int defect = missing_preserved_triples(candidate) +
                               !has_triple(candidate, target);
            consider_defect_swap(candidate,
                missing_preserved_triples(candidate));
            if (fifth_repair && defect > 0) {
                if (defect < fifth_seed_defect) {
                    fifth_seed_defect = defect;
                    fifth_paths.clear();
                }
                if (defect == fifth_seed_defect &&
                    static_cast<int>(fifth_paths.size()) < max_fifth_seeds) {
                    fifth_paths.push_back({candidate, intermediate.first,
                        intermediate.second, intermediate.third, move});
                }
            }
            if (defect != 0) return;
            ++fourth_preserved;
            const Eval score = evaluate(candidate, target);
            const bool primary_better = is_better(score, best_eval);
            const bool tied = score_equal(score, best_eval);
            const uint64_t hash = tie_seed && (primary_better || tied) ?
                path_hash(candidate) : UINT64_MAX;
            if (primary_better || (tie_seed && tied && hash < best_path_hash)) {
                best_eval = score;
                best_path.swap(candidate);
                best_path_hash = hash;
                best_first = intermediate.first;
                best_second = intermediate.second;
                best_third = intermediate.third;
                best_fourth = move;
            }
        });
    }

    long long fifth_moves = 0, fifth_color = 0, fifth_run = 0,
              fifth_preserved = 0;
    Move best_fifth{-1, -1, -1, false};
    for (const FifthIntermediate& intermediate : fifth_paths) {
        vector<int> lower, upper;
        color_counts(intermediate.path, lower, upper);
        enumerate_moves(intermediate.path, [&](const Move& move) {
            ++fifth_moves;
            if (!preserves_colors(intermediate.path, lower, upper, move)) return;
            ++fifth_color;
            vector<int> candidate = relocate(intermediate.path, move);
            if (!run_free(candidate)) return;
            ++fifth_run;
            consider_defect_swap(candidate,
                missing_preserved_triples(candidate));
            if (!has_triple(candidate, target) || !preserves_triples(candidate)) return;
            ++fifth_preserved;
            const Eval score = evaluate(candidate, target);
            const bool primary_better = is_better(score, best_eval);
            const bool tied = score_equal(score, best_eval);
            const uint64_t hash = tie_seed && (primary_better || tied) ?
                path_hash(candidate) : UINT64_MAX;
            if (primary_better || (tie_seed && tied && hash < best_path_hash)) {
                best_eval = score;
                best_path.swap(candidate);
                best_path_hash = hash;
                best_first = intermediate.first;
                best_second = intermediate.second;
                best_third = intermediate.third;
                best_fourth = intermediate.fourth;
                best_fifth = move;
            }
        });
    }

    bool used_defect_swap = false;
    if (best_path.empty() && allow_defect_swap && !best_swap_path.empty()) {
        best_path.swap(best_swap_path);
        best_eval = best_swap_eval;
        used_defect_swap = true;
    }

    cerr << "first_moves=" << first_moves << " first_color=" << first_color
         << " first_run=" << first_run << " retained=" << first_paths.size()
         << " allow_first_bad_run=" << allow_first_bad_run
         << " third_repair=" << third_repair
         << " fourth_repair=" << fourth_repair
         << " fifth_repair=" << fifth_repair
         << " allow_defect_swap=" << allow_defect_swap
         << " protected_count=" << protected_masks.size()
         << " rank5_first=" << rank5_first
         << " ignore_secondary=" << ignore_secondary
         << " target_multiplicity_second=" << target_multiplicity_second
         << " target_multiplicity_first=" << target_multiplicity_first
         << " tie_seed=" << tie_seed
         << " second_moves=" << second_moves << " second_target=" << second_target
         << " second_color=" << second_color << " second_run=" << second_run
         << " final_preserved=" << final_preserved
         << " best_rank5=" << best_eval.rank5
         << " best_upper_missing=" << best_eval.upper_missing
         << " best_target_multiplicity=" << best_eval.target_multiplicity
         << " first=[" << best_first.left << ',' << best_first.right << "]@"
         << best_first.edge << "r" << best_first.reversed
         << " second=[" << best_second.left << ',' << best_second.right << "]@"
         << best_second.edge << "r" << best_second.reversed
         << " bad_run_paths=" << bad_run_paths.size()
         << " third_moves=" << third_moves << " third_color=" << third_color
         << " third_run=" << third_run << " third_preserved=" << third_preserved
         << " third=[" << best_third.left << ',' << best_third.right << "]@"
         << best_third.edge << "r" << best_third.reversed
         << " fourth_seed_missing=" << fourth_seed_missing
         << " fourth_seeds=" << fourth_paths.size()
         << " fourth_moves=" << fourth_moves
         << " fourth_color=" << fourth_color
         << " fourth_run=" << fourth_run
         << " fourth_preserved=" << fourth_preserved
         << " fourth=[" << best_fourth.left << ',' << best_fourth.right << "]@"
         << best_fourth.edge << "r" << best_fourth.reversed
         << " fifth_seed_defect=" << fifth_seed_defect
         << " fifth_seeds=" << fifth_paths.size()
         << " fifth_moves=" << fifth_moves
         << " fifth_color=" << fifth_color
         << " fifth_run=" << fifth_run
         << " fifth_preserved=" << fifth_preserved
         << " fifth=[" << best_fifth.left << ',' << best_fifth.right << "]@"
         << best_fifth.edge << "r" << best_fifth.reversed
         << " used_defect_swap=" << used_defect_swap
         << " swap_defect=" << best_swap_defect << '\n';
    if (best_path.empty()) best_path = original;
    for (int value : best_path) cout << value << ' ';
    cout << '\n';
}
