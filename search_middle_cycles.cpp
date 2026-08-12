#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <cadical.hpp>

#include <algorithm>
#include <bit>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <queue>
#include <random>
#include <vector>

using namespace std;

struct Edge {
    int lower;
    int upper;
    int variable;
};

static void add_clause(CaDiCaL::Solver& solver, const vector<int>& clause) {
    for (int literal : clause) solver.add(literal);
    solver.add(0);
}

static void exactly_two_of_five(CaDiCaL::Solver& solver,
                                const vector<int>& variables) {
    // At least two: every four variables cannot all be false.
    for (int omitted = 0; omitted < 5; ++omitted) {
        vector<int> clause;
        for (int i = 0; i < 5; ++i)
            if (i != omitted) clause.push_back(variables[i]);
        add_clause(solver, clause);
    }
    // At most two: no three variables can all be true.
    for (int i = 0; i < 5; ++i)
        for (int j = i + 1; j < 5; ++j)
            for (int l = j + 1; l < 5; ++l)
                add_clause(solver, {-variables[i], -variables[j], -variables[l]});
}

static bool pair_rootable(const vector<int>& p, int k) {
    for (int bit = 0; bit < k; ++bit) {
        int start = 0;
        while (start < static_cast<int>(p.size())) {
            if (!(p[start] & (1 << bit))) {
                ++start;
                continue;
            }
            int end = start + 1;
            while (end < static_cast<int>(p.size()) && (p[end] & (1 << bit))) ++end;
            if (start > 0 && end < static_cast<int>(p.size()) && end - start == 1)
                return false;
            start = end;
        }
    }
    return true;
}

static bool triple_rootable(const vector<int>& p, int k) {
    for (int bit = 0; bit < k; ++bit) {
        int start = 0;
        while (start < static_cast<int>(p.size())) {
            if (!(p[start] & (1 << bit))) { ++start; continue; }
            int end = start + 1;
            while (end < static_cast<int>(p.size()) && (p[end] & (1 << bit))) ++end;
            if (start > 0 && end < static_cast<int>(p.size()) && end - start < 3)
                return false;
            start = end;
        }
    }
    return true;
}

static int high_coverage(const vector<int>& p, int k, int minimum_rank) {
    vector<uint8_t> seen(1 << k);
    int count = 0;
    for (int left = 0; left < static_cast<int>(p.size()); ++left) {
        int value = 0;
        for (int right = left; right < static_cast<int>(p.size()); ++right) {
            value |= p[right];
            if (popcount(static_cast<unsigned>(value)) >= minimum_rank && !seen[value]) {
                seen[value] = 1;
                ++count;
            }
            if (value == (1 << k) - 1) break;
        }
    }
    return count;
}

static int lower_intersection_coverage(const vector<int>& p, int k, int rank) {
    vector<uint8_t> seen(1 << k);
    int count = 0;
    for (int i = 0; i + 1 < static_cast<int>(p.size()); ++i) {
        const int value = p[i] & p[i + 1];
        if (popcount(static_cast<unsigned>(value)) == rank && !seen[value]) {
            seen[value] = 1;
            ++count;
        }
    }
    return count;
}

int main(int argc, char** argv) {
    const int k = argc > 1 ? stoi(argv[1]) : 9;
    const int rank = (k - 1) / 2;
    const int wanted_cycles = argc > 2 ? stoi(argv[2]) : 10000;
    const int seed = argc > 3 ? stoi(argv[3]) : 1;
    const int output_threshold = argc > 4 ? stoi(argv[4]) : (1 << (k - 1));
    const int lower_threshold = argc > 5 ? stoi(argv[5]) : 0;
    const bool plain_lower_order = argc > 6 && string(argv[6]) == "plain";
    vector<int> lower, upper;
    for (int mask = 1; mask < (1 << k); ++mask) {
        const int weight = popcount(static_cast<unsigned>(mask));
        if (weight == rank) lower.push_back(mask);
        if (weight == rank + 1) upper.push_back(mask);
    }
    if (lower.size() != upper.size()) return 2;
    mt19937_64 randomizer(static_cast<uint64_t>(seed) * 0x9e3779b97f4a7c15ULL);
    shuffle(lower.begin(), lower.end(), randomizer);
    shuffle(upper.begin(), upper.end(), randomizer);
    const int side = lower.size();

    CaDiCaL::Solver solver;
    solver.set("quiet", 1);
    solver.set("seed", seed);
    vector<Edge> edges;
    vector<vector<int>> incident(2 * side);
    vector<vector<int>> edge_variable(side, vector<int>(side));
    vector<int> lower_index(1 << k, -1), upper_index(1 << k, -1);
    for (int i = 0; i < side; ++i) lower_index[lower[i]] = i;
    for (int i = 0; i < side; ++i) upper_index[upper[i]] = i;
    int variable = 0;
    for (int i = 0; i < side; ++i) {
        for (int j = 0; j < side; ++j) {
            if ((lower[i] & upper[j]) != lower[i]) continue;
            edges.push_back({i, j, ++variable});
            edge_variable[i][j] = variable;
            incident[i].push_back(variable);
            incident[side + j].push_back(variable);
        }
    }
    for (const vector<int>& list : incident) {
        if (list.size() != static_cast<size_t>(rank + 1)) return 2;
        if (rank + 1 != 5) return 2;
        exactly_two_of_five(solver, list);
    }

    // In plain-lower-order mode, force every rank-(r+2) mask to be the union
    // of the two upper neighbors around some rank-r vertex.  In the resulting
    // lower order this is a length-three window, and after adjoining a new bit
    // it supplies the next graded layer of the k+1 construction.
    if (plain_lower_order) {
        for (int target = 1; target < (1 << k); ++target) {
            if (popcount(static_cast<unsigned>(target)) != rank + 2) continue;
            vector<int> witnesses;
            for (int l = 0; l < side; ++l) {
                if ((lower[l] & target) != lower[l]) continue;
                const int difference = target & ~lower[l];
                if (popcount(static_cast<unsigned>(difference)) != 2) continue;
                const int first_bit = difference & -difference;
                const int second_bit = difference ^ first_bit;
                const int q1 = upper_index[lower[l] | first_bit];
                const int q2 = upper_index[lower[l] | second_bit];
                const int witness = ++variable;
                witnesses.push_back(witness);
                add_clause(solver, {-witness, edge_variable[l][q1]});
                add_clause(solver, {-witness, edge_variable[l][q2]});
            }
            add_clause(solver, witnesses);
        }
    }

    // In the cyclic order of rank-r vertices, forbid a bit from occurring at
    // exactly one vertex of an internal run.  If S contains b and U=S+u is an
    // adjacent upper vertex, crossing U from S to U-b is precisely an exit
    // from b.  Two such exits on the two sides of S would make {S} a singleton
    // b-run, which cannot be the pairwise-OR image of any binary root.
    for (int s = 0; s < side; ++s) {
        vector<int> supersets;
        for (int u = 0; u < side; ++u)
            if (edge_variable[s][u]) supersets.push_back(u);
        for (int bit = 0; bit < k; ++bit) {
            if (!(lower[s] & (1 << bit))) continue;
            for (int a = 0; a < static_cast<int>(supersets.size()); ++a) {
                const int u = supersets[a];
                const int across_u = lower_index[upper[u] & ~(1 << bit)];
                for (int c = a + 1; c < static_cast<int>(supersets.size()); ++c) {
                    const int v = supersets[c];
                    const int across_v = lower_index[upper[v] & ~(1 << bit)];
                    add_clause(solver, {
                        -edge_variable[s][u], -edge_variable[across_u][u],
                        -edge_variable[s][v], -edge_variable[across_v][v]});
                }
            }
        }
    }


    // Also forbid cyclic runs of length two.  Such a run is a lower-vertex
    // path L0-L1-L2-L3 whose middle two masks contain b and whose endpoints do
    // not.  Each transition has a unique intervening upper union.
    for (int bit = 0; bit < k; ++bit) {
        for (int l1 = 0; l1 < side; ++l1) {
            if (!(lower[l1] & (1 << bit))) continue;
            for (int l2 = 0; l2 < side; ++l2) {
                if (!(lower[l2] & (1 << bit)) ||
                    popcount(static_cast<unsigned>(lower[l1] ^ lower[l2])) != 2)
                    continue;
                const int q12 = upper_index[lower[l1] | lower[l2]];
                for (int enter = 0; enter < k; ++enter) {
                    if (lower[l1] & (1 << enter)) continue;
                    const int l0 = lower_index[(lower[l1] & ~(1 << bit)) | (1 << enter)];
                    const int q01 = upper_index[lower[l0] | lower[l1]];
                    for (int leave = 0; leave < k; ++leave) {
                        if (lower[l2] & (1 << leave)) continue;
                        const int l3 = lower_index[(lower[l2] & ~(1 << bit)) | (1 << leave)];
                        const int q23 = upper_index[lower[l2] | lower[l3]];
                        add_clause(solver, {
                            -edge_variable[l0][q01], -edge_variable[l1][q01],
                            -edge_variable[l1][q12], -edge_variable[l2][q12],
                            -edge_variable[l2][q23], -edge_variable[l3][q23]});
                    }
                }
            }
        }
    }

    uint64_t two_factors = 0, cycles = 0, cuts = 0, rootable = 0, high_complete = 0;
    int best_high = 0, best_lower = 0, best_lower_when_high = 0;
    while (cycles < static_cast<uint64_t>(wanted_cycles) && solver.solve() == 10) {
        ++two_factors;
        vector<vector<pair<int, int>>> chosen(2 * side);
        vector<int> selected;
        for (int e = 0; e < static_cast<int>(edges.size()); ++e) {
            if (solver.val(edges[e].variable) <= 0) continue;
            const int u = edges[e].lower;
            const int v = side + edges[e].upper;
            chosen[u].push_back({v, e});
            chosen[v].push_back({u, e});
            selected.push_back(e);
        }

        vector<int> component(2 * side, -1);
        int component_count = 0;
        for (int start = 0; start < 2 * side; ++start) {
            if (component[start] >= 0) continue;
            queue<int> pending;
            component[start] = component_count;
            pending.push(start);
            while (!pending.empty()) {
                const int u = pending.front();
                pending.pop();
                for (auto [v, edge] : chosen[u]) {
                    (void) edge;
                    if (component[v] >= 0) continue;
                    component[v] = component_count;
                    pending.push(v);
                }
            }
            ++component_count;
        }
        if (component_count > 1) {
            for (int c = 0; c < component_count; ++c) {
                vector<int> crossing;
                for (const Edge& edge : edges) {
                    const int u = edge.lower, v = side + edge.upper;
                    if ((component[u] == c) != (component[v] == c))
                        crossing.push_back(edge.variable);
                }
                add_clause(solver, crossing);
            }
            continue;
        }

        ++cycles;
        // Recover the cyclic alternating order, beginning at a lower vertex.
        vector<int> walk;
        walk.reserve(2 * side);
        int previous = -1, current = 0;
        do {
            walk.push_back(current);
            const auto& nexts = chosen[current];
            const int next = nexts[0].first == previous ? nexts[1].first : nexts[0].first;
            previous = current;
            current = next;
        } while (current != walk[0]);
        if (walk.size() != static_cast<size_t>(2 * side)) return 3;

        // Every deleted upper-lower edge gives a Hamilton path.  Append a
        // rank-2 or rank-3 exceptional pair mask E at its upper endpoint.
        for (int direction : {1, -1}) {
            for (int offset = 0; offset < 2 * side; offset += 2) {
                ++cuts;
                vector<int> p;
                p.reserve(side + 1);
                vector<int> q;
                q.reserve(side);
                for (int step = 0; step < 2 * side; ++step) {
                    int position = (offset + direction * step) % (2 * side);
                    if (position < 0) position += 2 * side;
                    const int vertex = walk[position];
                    if (vertex < side) p.push_back(lower[vertex]);
                    else q.push_back(upper[vertex - side]);
                }
                if (p.size() != static_cast<size_t>(side) ||
                    q.size() != static_cast<size_t>(side)) return 3;
                if (plain_lower_order) {
                    if (!triple_rootable(p, k)) return 4;
                    const int high = high_coverage(p, k, rank);
                    best_high = max(best_high, high);
                    if (high >= output_threshold) {
                        ++high_complete;
                        for (int value : p) cout << value << ' ';
                        cout << '\n' << flush;
                    }
                    continue;
                }
                const int last_p = p.back(), last_q = q.back();
                const int new_bit = last_q & ~last_p;
                vector<int> old_bits;
                for (int bit = 0; bit < k; ++bit)
                    if (last_p & (1 << bit)) old_bits.push_back(1 << bit);
                vector<int> exceptions;
                for (int bit : old_bits) exceptions.push_back(new_bit | bit);
                for (int i = 0; i < static_cast<int>(old_bits.size()); ++i)
                    for (int j = i + 1; j < static_cast<int>(old_bits.size()); ++j)
                        exceptions.push_back(new_bit | old_bits[i] | old_bits[j]);
                for (int exception : exceptions) {
                    p.push_back(exception);
                    if (!pair_rootable(p, k)) {
                        p.pop_back();
                        continue;
                    }
                    ++rootable;
                    const int lower_count = lower_intersection_coverage(p, k, rank - 1);
                    best_lower = max(best_lower, lower_count);
                    const int high = high_coverage(p, k, rank + 1);
                    best_high = max(best_high, high);
                    if (high == (1 << (k - 1)))
                        best_lower_when_high = max(best_lower_when_high, lower_count);
                    if (high < output_threshold || lower_count < lower_threshold) {
                        p.pop_back();
                        continue;
                    }
                    if (high == (1 << (k - 1))) ++high_complete;
                    // Recompute Q from P to make orientation unambiguous.
                    for (int i = 0; i + 1 < static_cast<int>(p.size()); ++i)
                        cout << (p[i] | p[i + 1]) << ' ';
                    cout << '\n' << flush;
                    p.pop_back();
                }
            }
        }

        // Block this 2-factor, forcing the next model to change an edge.
        vector<int> block;
        block.reserve(selected.size());
        for (int edge : selected) block.push_back(-edges[edge].variable);
        add_clause(solver, block);
        if (cycles % 100 == 0)
            cerr << "two_factors=" << two_factors << " cycles=" << cycles
                 << " cuts=" << cuts << " rootable=" << rootable
                 << " high=" << high_complete << " best_high=" << best_high
                 << " best_lower=" << best_lower
                 << " high_lower=" << best_lower_when_high << '\n';
    }
    cerr << "done two_factors=" << two_factors << " cycles=" << cycles
         << " cuts=" << cuts << " rootable=" << rootable
         << " high=" << high_complete << " best_high=" << best_high
         << " best_lower=" << best_lower
         << " high_lower=" << best_lower_when_high << '\n';
    return 0;
}
