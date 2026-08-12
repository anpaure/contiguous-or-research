#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <algorithm>
#include <bit>
#include <fstream>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>
using namespace std;

static vector<int> read_path(const string& filename) {
    ifstream in(filename);
    vector<int> result;
    for (int x; in >> x;) result.push_back(x);
    return result;
}

static bool adjacent(int a, int b) {
    return popcount(static_cast<unsigned>(a ^ b)) == 2;
}

static int lower_coverage(const vector<int>& path, int rank, int bits) {
    vector<unsigned char> seen(1 << bits);
    for (int i = 0; i + 1 < static_cast<int>(path.size()); ++i) {
        if (!adjacent(path[i], path[i + 1])) return -1;
        const int value = path[i] & path[i + 1];
        if (popcount(static_cast<unsigned>(value)) == rank - 1) seen[value] = 1;
    }
    int result = 0;
    for (int x = 0; x < (1 << bits); ++x)
        if (popcount(static_cast<unsigned>(x)) == rank - 1 && seen[x]) ++result;
    return result;
}

static vector<int> materialize(const vector<int>& path,
                               const vector<pair<int, int>>& pieces) {
    vector<int> result;
    result.reserve(path.size());
    for (auto [first, last] : pieces) {
        const int step = first <= last ? 1 : -1;
        for (int i = first;; i += step) {
            result.push_back(path[i]);
            if (i == last) break;
        }
    }
    return result;
}

static bool joins_are_valid(const vector<int>& path,
                            const vector<pair<int, int>>& pieces) {
    for (int i = 0; i + 1 < static_cast<int>(pieces.size()); ++i)
        if (!adjacent(path[pieces[i].second], path[pieces[i + 1].first]))
            return false;
    return true;
}

int main(int argc, char** argv) {
    if (argc != 4) {
        cerr << "usage: build_k14_two_block_seed LOWER_RAINBOW_R7 "
                "UPPER_COMPLETE_R7 OUTPUT\n";
        return 2;
    }
    constexpr int old_bits = 13;
    constexpr int full = (1 << old_bits) - 1;
    constexpr int high = 1 << old_bits;
    vector<int> lower = read_path(argv[1]);
    vector<int> upper = read_path(argv[2]);
    if (lower.size() != 1716 || upper.size() != 1716) return 3;

    vector<unsigned char> lower_colors(1 << old_bits);
    for (int i = 0; i + 1 < static_cast<int>(lower.size()); ++i) {
        if (!adjacent(lower[i], lower[i + 1])) return 4;
        lower_colors[lower[i] & lower[i + 1]] = 1;
    }
    int omitted = -1, omitted_count = 0;
    for (int x = 0; x <= full; ++x)
        if (popcount(static_cast<unsigned>(x)) == 6 && !lower_colors[x]) {
            omitted = x;
            ++omitted_count;
        }
    if (omitted_count != 1 || (lower.back() & omitted) != omitted) {
        cerr << "lower path has omitted_count=" << omitted_count
             << " omitted=" << omitted << " endpoint=" << lower.back() << '\n';
        return 5;
    }

    // Complementing the upper-complete rank-7 path gives a rank-6 path whose
    // adjacent intersections cover all rank-5 masks.  We need the omitted
    // rank-6 color of the first block as its first endpoint.  Reassemble at
    // most three contiguous pieces of the known path and retain full color
    // coverage.
    vector<int> base(upper.size());
    transform(upper.begin(), upper.end(), base.begin(),
              [](int x) { return full ^ x; });
    if (lower_coverage(base, 6, old_bits) != 1287) return 6;
    const auto found = find(base.begin(), base.end(), omitted);
    if (found == base.end()) return 7;
    const int target = found - base.begin();

    vector<int> repaired;
    const int n = base.size();
    auto test = [&](const vector<pair<int, int>>& pieces) {
        if (!repaired.empty() || pieces.empty() ||
            base[pieces.front().first] != omitted ||
            !joins_are_valid(base, pieces)) return;
        vector<int> candidate = materialize(base, pieces);
        if (static_cast<int>(candidate.size()) != n) return;
        vector<unsigned char> used(1 << old_bits);
        for (int x : candidate) {
            if (popcount(static_cast<unsigned>(x)) != 6 || used[x]) return;
            used[x] = 1;
        }
        if (lower_coverage(candidate, 6, old_bits) == 1287)
            repaired.swap(candidate);
    };

    // Two remaining pieces: the portions on either side of the target.
    vector<pair<int, int>> left, right;
    if (target > 0) left.push_back({0, target - 1});
    if (target + 1 < n) right.push_back({target + 1, n - 1});
    vector<vector<pair<int, int>>> sides;
    if (!left.empty() && !right.empty()) {
        for (int swap_order = 0; swap_order < 2; ++swap_order)
            for (int reverse_left = 0; reverse_left < 2; ++reverse_left)
                for (int reverse_right = 0; reverse_right < 2; ++reverse_right) {
                    auto a = left[0], b = right[0];
                    if (reverse_left) swap(a.first, a.second);
                    if (reverse_right) swap(b.first, b.second);
                    vector<pair<int, int>> pieces{{target, target}};
                    if (swap_order) pieces.insert(pieces.end(), {b, a});
                    else pieces.insert(pieces.end(), {a, b});
                    test(pieces);
                }
    }

    // If two pieces are insufficient, add one extra cut in either side and
    // enumerate all permutations and orientations of the three residual
    // pieces.  This is only O(n) configurations up to a constant factor.
    for (int cut = 0; repaired.empty() && cut + 1 < n; ++cut) {
        if (cut == target || cut + 1 == target) continue;
        vector<pair<int, int>> segments;
        int begin = 0;
        for (int boundary : vector<int>{min(cut, target - 1),
                                        max(cut, target - 1)}) {
            if (boundary >= begin && boundary < n - 1) {
                segments.push_back({begin, boundary});
                begin = boundary + 1;
            }
        }
        if (begin < n) segments.push_back({begin, n - 1});
        // Remove the singleton target from its containing segment, producing
        // up to three nonempty residual intervals.
        vector<pair<int, int>> residual;
        for (auto [a, b] : segments) {
            if (target < a || target > b) residual.push_back({a, b});
            else {
                if (a < target) residual.push_back({a, target - 1});
                if (target < b) residual.push_back({target + 1, b});
            }
        }
        if (residual.size() != 3) continue;
        vector<int> permutation{0, 1, 2};
        do {
            for (int directions = 0; directions < 8; ++directions) {
                vector<pair<int, int>> pieces{{target, target}};
                for (int j = 0; j < 3; ++j) {
                    auto piece = residual[permutation[j]];
                    if (directions & (1 << j)) swap(piece.first, piece.second);
                    pieces.push_back(piece);
                }
                test(pieces);
            }
        } while (next_permutation(permutation.begin(), permutation.end()));
    }

    if (repaired.empty()) {
        cerr << "no <=3-piece endpoint repair; omitted=" << omitted
             << " target_position=" << target << '\n';
        return 8;
    }

    vector<int> result = lower;
    for (int x : repaired) result.push_back(high | x);
    if (result.size() != 3432) return 9;
    vector<unsigned char> seen_vertex(1 << 14), seen_color(1 << 14);
    for (int x : result) {
        if (popcount(static_cast<unsigned>(x)) != 7 || seen_vertex[x]) return 10;
        seen_vertex[x] = 1;
    }
    for (int i = 0; i + 1 < static_cast<int>(result.size()); ++i) {
        if (!adjacent(result[i], result[i + 1])) return 11;
        seen_color[result[i] & result[i + 1]] = 1;
    }
    int colors = 0;
    for (int x = 0; x < (1 << 14); ++x)
        if (popcount(static_cast<unsigned>(x)) == 6 && seen_color[x]) ++colors;
    if (colors != 3003) return 12;

    ofstream out(argv[3]);
    for (int x : result) out << x << ' ';
    out << '\n';
    cerr << "success omitted=" << omitted << " repaired_start=" << repaired.front()
         << " rank6_colors=" << colors << '\n';
}
