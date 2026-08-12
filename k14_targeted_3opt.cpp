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
struct Eval { int deficit = 0, rank5 = 0, upper8 = 0; };
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
vector<int> bad_edges(const vector<int>& path) {
    vector<int> result;
    for (int bit = 0; bit < k; ++bit) {
        int i = 0;
        while (i < static_cast<int>(path.size())) {
            if (!(path[i] & (1 << bit))) { ++i; continue; }
            const int first = i;
            while (i < static_cast<int>(path.size()) && (path[i] & (1 << bit))) ++i;
            if (!first || i == static_cast<int>(path.size()) || i - first >= 3) continue;
            for (int edge = first - 1; edge <= i - 1; ++edge) result.push_back(edge);
        }
    }
    sort(result.begin(), result.end());
    result.erase(unique(result.begin(), result.end()), result.end());
    return result;
}
struct Segment { int first, last; bool reverse; };
int front(const vector<int>& path, const Segment& segment) {
    return path[segment.reverse ? segment.last : segment.first];
}
int back(const vector<int>& path, const Segment& segment) {
    return path[segment.reverse ? segment.first : segment.last];
}
void append_segment(vector<int>& output, const vector<int>& path, const Segment& segment) {
    if (!segment.reverse)
        output.insert(output.end(), path.begin() + segment.first, path.begin() + segment.last + 1);
    else
        for (int i = segment.last; i >= segment.first; --i) output.push_back(path[i]);
}
} // namespace

int main(int argc, char** argv) {
    const int minimum_rank5 = argc > 1 ? stoi(argv[1]) : 1998;
    vector<int> path;
    for (int value; cin >> value;) path.push_back(value);
    const int n = path.size(), edge_count = n - 1;
    if (n != 3432) return 2;
    vector<int> colors(limit);
    for (int edge = 0; edge < edge_count; ++edge) {
        if (!adjacent(path[edge], path[edge + 1])) return 3;
        ++colors[path[edge] & path[edge + 1]];
    }
    int covered = 0;
    for (int mask = 0; mask < limit; ++mask)
        covered += popcount(static_cast<unsigned>(mask)) == 6 && colors[mask];
    if (covered != 3003) return 4;
    const vector<int> bad = bad_edges(path);
    const Eval initial = evaluate(path);
    Eval best = initial;
    vector<int> best_path = path;
    array<int, 3> best_cuts{-1, -1, -1};
    int best_order = -1, best_directions = -1;
    long long cut_triples = 0, johnson_valid = 0, color_valid = 0;
    for (int forced : bad)
        for (int other1 = 0; other1 < edge_count; ++other1)
            for (int other2 = other1 + 1; other2 < edge_count; ++other2) {
                if (forced == other1 || forced == other2) continue;
                array<int, 3> cuts{forced, other1, other2};
                sort(cuts.begin(), cuts.end());
                bool assigned_to_earlier_bad = false;
                for (int bad_edge : bad)
                    if (bad_edge < forced && binary_search(cuts.begin(), cuts.end(), bad_edge))
                        assigned_to_earlier_bad = true;
                if (assigned_to_earlier_bad) continue;
                ++cut_triples;
                const int a = cuts[0], b = cuts[1], c = cuts[2];
                const Segment A{0, a, false}, B{a + 1, b, false},
                              C{b + 1, c, false}, D{c + 1, n - 1, false};
                for (int order = 0; order < 2; ++order)
                    for (int directions = 0; directions < 4; ++directions) {
                        Segment first = order ? C : B;
                        Segment second = order ? B : C;
                        first.reverse = directions & 1;
                        second.reverse = directions & 2;
                        if (!order && !directions) continue; // original path
                        array<pair<int, int>, 3> joins{{
                            {back(path, A), front(path, first)},
                            {back(path, first), front(path, second)},
                            {back(path, second), front(path, D)}
                        }};
                        bool valid = true;
                        for (auto [u, v] : joins) valid &= adjacent(u, v);
                        if (!valid) continue;
                        ++johnson_valid;
                        array<int, 6> masks{};
                        array<int, 6> deltas{};
                        int used = 0;
                        auto change = [&](int mask, int delta) {
                            for (int i = 0; i < used; ++i) if (masks[i] == mask) {
                                deltas[i] += delta; return;
                            }
                            masks[used] = mask; deltas[used] = delta; ++used;
                        };
                        for (int cut : cuts) change(path[cut] & path[cut + 1], -1);
                        for (auto [u, v] : joins) change(u & v, +1);
                        for (int i = 0; i < used; ++i)
                            if (colors[masks[i]] + deltas[i] <= 0) valid = false;
                        if (!valid) continue;
                        ++color_valid;
                        vector<int> candidate;
                        candidate.reserve(n);
                        append_segment(candidate, path, A);
                        append_segment(candidate, path, first);
                        append_segment(candidate, path, second);
                        append_segment(candidate, path, D);
                        const Eval current = evaluate(candidate);
                        if (current.rank5 >= minimum_rank5 && better(current, best)) {
                            best = current;
                            best_path.swap(candidate);
                            best_cuts = cuts;
                            best_order = order;
                            best_directions = directions;
                        }
                    }
            }
    cerr << "initial=" << initial.deficit << ',' << initial.rank5 << ',' << initial.upper8
         << " best=" << best.deficit << ',' << best.rank5 << ',' << best.upper8
         << " bad_edges=" << bad.size()
         << " cuts=[" << best_cuts[0] << ',' << best_cuts[1] << ',' << best_cuts[2] << ']'
         << " order=" << best_order << " directions=" << best_directions
         << " cut_triples=" << cut_triples << " johnson_valid=" << johnson_valid
         << " color_valid=" << color_valid << '\n';
    for (int value : best_path) cout << value << ' ';
    cout << '\n';
}
