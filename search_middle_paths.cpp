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
#include <queue>
#include <random>
#include <vector>

using namespace std;

struct Edge { int lower, upper, variable; };

static void add_clause(CaDiCaL::Solver& solver, const vector<int>& clause) {
    for (int literal : clause) solver.add(literal);
    solver.add(0);
}

static void exactly_two(CaDiCaL::Solver& solver, const vector<int>& variables) {
    // At least two: after omitting any one literal, at least one remains true.
    for (int omitted = 0; omitted < static_cast<int>(variables.size()); ++omitted) {
        vector<int> clause;
        clause.reserve(variables.size() - 1);
        for (int i = 0; i < static_cast<int>(variables.size()); ++i)
            if (i != omitted) clause.push_back(variables[i]);
        add_clause(solver, clause);
    }
    // At most two.
    for (int i = 0; i < static_cast<int>(variables.size()); ++i)
        for (int j = i + 1; j < static_cast<int>(variables.size()); ++j)
            for (int l = j + 1; l < static_cast<int>(variables.size()); ++l)
                add_clause(solver, {-variables[i], -variables[j], -variables[l]});
}

static bool pair_rootable(const vector<int>& p, int k) {
    for (int bit = 0; bit < k; ++bit) {
        int start = 0;
        while (start < static_cast<int>(p.size())) {
            if (!(p[start] & (1 << bit))) { ++start; continue; }
            int end = start + 1;
            while (end < static_cast<int>(p.size()) && (p[end] & (1 << bit))) ++end;
            if (start > 0 && end < static_cast<int>(p.size()) && end - start == 1)
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

static int lower_coverage(const vector<int>& p, int k, int rank) {
    vector<uint8_t> seen(1 << k);
    int count = 0;
    for (int i = 0; i + 1 < static_cast<int>(p.size()); ++i) {
        const int value = p[i] & p[i + 1];
        if (popcount(static_cast<unsigned>(value)) == rank && !seen[value])
            seen[value] = 1, ++count;
    }
    return count;
}

int main(int argc, char** argv) {
    const int k = argc > 1 ? stoi(argv[1]) : 9;
    const int rank = (k - 1) / 2;
    const int wanted_paths = argc > 2 ? stoi(argv[2]) : 10000;
    const int seed = argc > 3 ? stoi(argv[3]) : 1;
    const int exception_rank = argc > 4 ? stoi(argv[4]) : 3;
    const int high_threshold = argc > 5 ? stoi(argv[5]) : (1 << (k - 1));
    const int lower_threshold = argc > 6 ? stoi(argv[6]) : 0;
    const bool force_rank_six = argc > 7 ? stoi(argv[7]) != 0 : true;
    const bool force_rank_three = argc > 8 ? stoi(argv[8]) != 0 : true;
    if (k != 9 || (exception_rank != 2 && exception_rank != 3)) return 2;

    const int exception = (1 << exception_rank) - 1;
    vector<int> lower, upper;
    for (int mask = 1; mask < (1 << k); ++mask) {
        const int weight = popcount(static_cast<unsigned>(mask));
        if (weight == rank) lower.push_back(mask);
        if (weight == rank + 1) upper.push_back(mask);
    }
    mt19937_64 randomizer(static_cast<uint64_t>(seed) * 0x9e3779b97f4a7c15ULL);
    shuffle(lower.begin(), lower.end(), randomizer);
    shuffle(upper.begin(), upper.end(), randomizer);
    lower.push_back(exception);
    upper.push_back(-1);  // Auxiliary vertex: deleting it opens a Hamilton path.
    const int side = lower.size();
    const int exception_index = side - 1, auxiliary_index = side - 1;

    CaDiCaL::Solver solver;
    solver.set("quiet", 1);
    solver.set("seed", seed);
    vector<Edge> edges;
    vector<vector<int>> edge_variable(side, vector<int>(side));
    vector<vector<int>> incident(2 * side);
    vector<int> lower_index(1 << k, -1), upper_index(1 << k, -1);
    for (int i = 0; i < side; ++i)
        if (lower[i] >= 0) lower_index[lower[i]] = i;
    for (int i = 0; i < side - 1; ++i) upper_index[upper[i]] = i;
    int variable = 0;
    for (int i = 0; i < side; ++i) {
        for (int j = 0; j < side; ++j) {
            const bool adjacent = j == auxiliary_index ||
                (lower[i] != upper[j] && (lower[i] & upper[j]) == lower[i]);
            if (!adjacent) continue;
            edge_variable[i][j] = ++variable;
            edges.push_back({i, j, variable});
            incident[i].push_back(variable);
            incident[side + j].push_back(variable);
        }
    }

    // If Q is adjacent to E and a rank-4 mask P, their union must be Q.
    for (int q = 0; q < side - 1; ++q) {
        const int eq = edge_variable[exception_index][q];
        if (!eq) continue;
        for (int p = 0; p < side - 1; ++p) {
            const int pq = edge_variable[p][q];
            if (pq && (lower[p] | exception) != upper[q])
                add_clause(solver, {-eq, -pq});
        }
    }

    for (const vector<int>& list : incident) exactly_two(solver, list);

    // Force each rank-(r+2) mask to occur as the union of two consecutive
    // rank-(r+1) masks.  Around a rank-r vertex L contained in S, the two
    // relevant upper neighbors are L plus each of the two bits in S\L.
    if (force_rank_six) {
        for (int target = 1; target < (1 << k); ++target) {
            if (popcount(static_cast<unsigned>(target)) != rank + 2) continue;
            vector<int> witnesses;
            for (int l = 0; l < side - 1; ++l) {
                if ((lower[l] & target) != lower[l]) continue;
                const int difference = target & ~lower[l];
                if (popcount(static_cast<unsigned>(difference)) != 2) continue;
                const int first_bit = difference & -difference;
                const int second_bit = difference ^ first_bit;
                const int q1 = upper_index[lower[l] | first_bit];
                const int q2 = upper_index[lower[l] | second_bit];
                const int e1 = edge_variable[l][q1], e2 = edge_variable[l][q2];
                const int witness = ++variable;
                witnesses.push_back(witness);
                add_clause(solver, {-witness, e1});
                add_clause(solver, {-witness, e2});
            }
            add_clause(solver, witnesses);
        }
    }

    // Dually, force every rank-(r-1) mask to occur as the intersection of
    // two consecutive rank-r masks.  If Q=T+{a,b}, its two required lower
    // faces are T+a and T+b.
    if (force_rank_three) {
        for (int target = 1; target < (1 << k); ++target) {
            if (popcount(static_cast<unsigned>(target)) != rank - 1) continue;
            vector<int> witnesses;
            for (int q = 0; q < side - 1; ++q) {
                if ((target & upper[q]) != target) continue;
                const int difference = upper[q] & ~target;
                if (popcount(static_cast<unsigned>(difference)) != 2) continue;
                const int first_bit = difference & -difference;
                const int second_bit = difference ^ first_bit;
                const int p1 = lower_index[target | first_bit];
                const int p2 = lower_index[target | second_bit];
                const int e1 = edge_variable[p1][q], e2 = edge_variable[p2][q];
                const int witness = ++variable;
                witnesses.push_back(witness);
                add_clause(solver, {-witness, e1});
                add_clause(solver, {-witness, e2});
            }
            add_clause(solver, witnesses);
        }
    }

    // Forbid a one-position internal run of any bit in the lower-mask path.
    // A transition event L-Q-M exits bit b when L contains b and M does not.
    for (int l = 0; l < side; ++l) {
        for (int bit = 0; bit < k; ++bit) {
            if (!(lower[l] & (1 << bit))) continue;
            struct Event { int q, first, second; };
            vector<Event> exits;
            for (int q = 0; q < side - 1; ++q) {
                const int lq = edge_variable[l][q];
                if (!lq) continue;
                for (int m = 0; m < side; ++m) {
                    const int mq = edge_variable[m][q];
                    if (!mq || (lower[m] & (1 << bit))) continue;
                    if ((l == exception_index || m == exception_index) &&
                        (lower[l] | lower[m]) != upper[q]) continue;
                    exits.push_back({q, lq, mq});
                }
            }
            for (int a = 0; a < static_cast<int>(exits.size()); ++a)
                for (int b = a + 1; b < static_cast<int>(exits.size()); ++b) {
                    if (exits[a].q == exits[b].q) continue;
                    add_clause(solver, {-exits[a].first, -exits[a].second,
                                        -exits[b].first, -exits[b].second});
                }
        }
    }

    uint64_t factors = 0, paths = 0, rootable = 0, emitted = 0;
    int best_high = 0, best_lower = 0, best_joint_lower = 0;
    while (paths < static_cast<uint64_t>(wanted_paths) && solver.solve() == 10) {
        ++factors;
        vector<vector<pair<int, int>>> chosen(2 * side);
        vector<int> selected;
        for (int e = 0; e < static_cast<int>(edges.size()); ++e) {
            if (solver.val(edges[e].variable) <= 0) continue;
            const int u = edges[e].lower, v = side + edges[e].upper;
            chosen[u].push_back({v, e});
            chosen[v].push_back({u, e});
            selected.push_back(e);
        }
        vector<int> component(2 * side, -1);
        int components = 0;
        for (int start = 0; start < 2 * side; ++start) {
            if (component[start] >= 0) continue;
            queue<int> pending;
            pending.push(start);
            component[start] = components;
            while (!pending.empty()) {
                const int u = pending.front(); pending.pop();
                for (auto [v, edge] : chosen[u]) {
                    (void) edge;
                    if (component[v] < 0) component[v] = components, pending.push(v);
                }
            }
            ++components;
        }
        if (components > 1) {
            for (int c = 0; c < components; ++c) {
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
        ++paths;

        // Walk away from the auxiliary upper vertex; omitting it opens the cycle.
        vector<int> p, q;
        int previous = side + auxiliary_index;
        int current = chosen[previous][0].first;
        while (current != side + auxiliary_index) {
            if (current < side) p.push_back(lower[current]);
            else q.push_back(upper[current - side]);
            const auto& nexts = chosen[current];
            const int next = nexts[0].first == previous ? nexts[1].first : nexts[0].first;
            previous = current;
            current = next;
        }
        if (p.size() != static_cast<size_t>(side) || q.size() != static_cast<size_t>(side - 1))
            return 3;
        if (!pair_rootable(p, k)) return 4;
        ++rootable;
        const int low = lower_coverage(p, k, rank - 1);
        const int high = high_coverage(p, k, rank + 1);
        best_lower = max(best_lower, low);
        best_high = max(best_high, high);
        if (high == (1 << (k - 1))) best_joint_lower = max(best_joint_lower, low);
        if (high >= high_threshold && low >= lower_threshold) {
            ++emitted;
            for (int i = 0; i + 1 < static_cast<int>(p.size()); ++i)
                cout << (p[i] | p[i + 1]) << ' ';
            cout << '\n' << flush;
        }

        vector<int> block;
        for (int edge : selected) block.push_back(-edges[edge].variable);
        add_clause(solver, block);
        if (paths % 100 == 0)
            cerr << "factors=" << factors << " paths=" << paths
                 << " emitted=" << emitted << " best_high=" << best_high
                 << " best_lower=" << best_lower
                 << " high_lower=" << best_joint_lower << '\n';
    }
    cerr << "done factors=" << factors << " paths=" << paths
         << " emitted=" << emitted << " best_high=" << best_high
         << " best_lower=" << best_lower
         << " high_lower=" << best_joint_lower << '\n';
    return 0;
}
