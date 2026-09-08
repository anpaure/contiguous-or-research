#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <cadical.hpp>

#include <algorithm>
#include <bit>
#include <fstream>
#include <iostream>
#include <numeric>
#include <queue>
#include <random>
#include <vector>

using namespace std;

struct Edge { int u, v, variable; };

int main(int argc, char** argv) {
    const int k = argc > 1 ? stoi(argv[1]) : 11;
    const int lower_rank = argc > 2 ? stoi(argv[2]) : k / 2;
    const int seed = argc > 3 ? stoi(argv[3]) : 1;
    const string requested = argc > 4 ? argv[4] : "";
    const bool distinguished_cut = requested == "twosidedcut";
    const bool cover_next_rank = requested == "cover7" ||
        requested == "cover7runs" || requested == "cover8runs" ||
        requested == "twosidedruns" || distinguished_cut;
    const bool enforce_long_runs = requested == "cover7runs" ||
        requested == "cover8runs" || requested == "twosidedruns" ||
        distinguished_cut;
    const bool cover_second_next_rank = requested == "cover8runs" ||
        requested == "twosidedruns" || distinguished_cut;
    const bool cover_second_lower_rank = requested == "twosidedruns" ||
        distinguished_cut;
    const int cut_lower = (1 << lower_rank) - 1;
    if (k != 2 * lower_rank + 1) return 2;
    const int limit = 1 << k;
    vector<int> masks;
    vector<int> index(limit, -1);
    for (int mask = 0; mask < limit; ++mask) {
        const int rank = popcount(static_cast<unsigned>(mask));
        if (rank == lower_rank || rank == lower_rank + 1) {
            index[mask] = masks.size();
            masks.push_back(mask);
        }
    }
    vector<Edge> edges;
    vector<vector<int>> incident(masks.size());
    vector<vector<int>> edge_variable(limit, vector<int>(k));
    int variable = 0;
    for (int mask = 0; mask < limit; ++mask) {
        if (popcount(static_cast<unsigned>(mask)) != lower_rank) continue;
        const int u = index[mask];
        for (int bit = 0; bit < k; ++bit) if (!(mask & (1 << bit))) {
            const int v = index[mask | (1 << bit)];
            const int edge_index = edges.size();
            edges.push_back({u, v, ++variable});
            edge_variable[mask][bit] = variable;
            incident[u].push_back(edge_index);
            incident[v].push_back(edge_index);
        }
    }

    CaDiCaL::Solver solver;
    solver.set("quiet", 1);
    solver.set("seed", seed);
    // Covers edge variables plus all local shadow witnesses for k=11.
    // This is needed by CaDiCaL builds with strict variable declaration.
    solver.declare_more_variables(500000);
    mt19937_64 random(seed);
    vector<uint8_t> phase_selected(variable + 1);
    bool has_phase_cycle = false;
    if (argc > 5) {
        ifstream phase_input(argv[5]);
        vector<int> phase_cycle;
        for (int value; phase_input >> value;) phase_cycle.push_back(value);
        if (phase_cycle.size() == masks.size()) {
            has_phase_cycle = true;
            for (int i = 0; i < static_cast<int>(phase_cycle.size()); ++i) {
                int a = phase_cycle[i];
                int b = phase_cycle[(i + 1) % phase_cycle.size()];
                if (popcount(static_cast<unsigned>(a)) >
                    popcount(static_cast<unsigned>(b))) swap(a, b);
                if (popcount(static_cast<unsigned>(a)) != lower_rank ||
                    popcount(static_cast<unsigned>(b)) != lower_rank + 1 ||
                    popcount(static_cast<unsigned>(a ^ b)) != 1) return 5;
                const int bit = countr_zero(static_cast<unsigned>(a ^ b));
                phase_selected[edge_variable[a][bit]] = 1;
            }
        }
    }
    for (const Edge& edge : edges)
        solver.phase(has_phase_cycle
            ? (phase_selected[edge.variable] ? edge.variable : -edge.variable)
            : ((random() & 1) ? edge.variable : -edge.variable));
    auto add_clause = [&] (const vector<int>& clause) {
        for (int literal : clause) solver.add(literal);
        solver.add(0);
    };
    // Every vertex has degree exactly two in the selected subgraph.
    for (const vector<int>& list : incident) {
        // At least two of six: every five-element subfamily contains a chosen edge.
        for (int omitted = 0; omitted < static_cast<int>(list.size()); ++omitted) {
            vector<int> clause;
            for (int i = 0; i < static_cast<int>(list.size()); ++i)
                if (i != omitted) clause.push_back(edges[list[i]].variable);
            add_clause(clause);
        }
        // At most two: no triple may be chosen.
        for (int i = 0; i < static_cast<int>(list.size()); ++i)
            for (int j = i + 1; j < static_cast<int>(list.size()); ++j)
                for (int h = j + 1; h < static_cast<int>(list.size()); ++h)
                    add_clause({-edges[list[i]].variable,
                                -edges[list[j]].variable,
                                -edges[list[h]].variable});
    }

    // Optional exact prescribed-path extension branch.  The input is a
    // whitespace-separated alternating path in the middle-levels graph.
    // Forcing its edges is sufficient: the degree-two constraints above
    // prevent an internal prescribed vertex from acquiring any other edge,
    // while the lazy component cuts below require the completed 2-factor to
    // be one Hamilton cycle.  This option deliberately imposes no OR-shadow
    // or factorability assumptions.
    if (const char* raw_path = getenv("MIDDLE_FORCE_PATH")) {
        ifstream path_input(raw_path);
        if (!path_input) return 6;
        vector<int> path;
        for (int value; path_input >> value;) path.push_back(value);
        if (path.size() < 2) return 6;
        vector<uint8_t> used(masks.size());
        for (int value : path) {
            if (value < 0 || value >= limit || index[value] < 0 ||
                used[index[value]])
                return 6;
            used[index[value]] = 1;
        }
        for (int i = 0; i + 1 < static_cast<int>(path.size()); ++i) {
            int lower = path[i], upper = path[i + 1];
            if (popcount(static_cast<unsigned>(lower)) >
                popcount(static_cast<unsigned>(upper)))
                swap(lower, upper);
            if (popcount(static_cast<unsigned>(lower)) != lower_rank ||
                popcount(static_cast<unsigned>(upper)) != lower_rank + 1 ||
                (lower & upper) != lower ||
                popcount(static_cast<unsigned>(lower ^ upper)) != 1)
                return 6;
            const int bit = countr_zero(static_cast<unsigned>(lower ^ upper));
            const int edge = edge_variable[lower][bit];
            if (!edge) return 6;
            add_clause({edge});
        }
        cerr << "forced_path_vertices=" << path.size()
             << " forced_path_edges=" << path.size() - 1 << '\n';
    }

    if (distinguished_cut) {
        // After fixing the cut to {0,...,lower_rank-1}, its stabilizer acts
        // transitively on unordered pairs of outside coordinates.  Normalize
        // the two selected incident edges to the first two outside bits.
        for (int bit = lower_rank; bit < k; ++bit)
            add_clause({bit < lower_rank + 2
                ? edge_variable[cut_lower][bit]
                : -edge_variable[cut_lower][bit]});
    }

    if (cover_next_rank) {
        // At a lower-layer vertex C, the selected 2-factor uses exactly two
        // incident edges C--(C+x) and C--(C+y).  The two corresponding
        // consecutive upper-layer vertices have union C+{x,y}.  Requiring
        // one such selected pair for every (lower_rank+2)-set therefore
        // forces the first upper union-shadow to be complete.
        for (int target = 0; target < limit; ++target) {
            if (popcount(static_cast<unsigned>(target)) != lower_rank + 2)
                continue;
            vector<int> witnesses;
            for (int first = 0; first < k; ++first) {
                if (!(target & (1 << first))) continue;
                for (int second = first + 1; second < k; ++second) {
                    if (!(target & (1 << second))) continue;
                    const int lower = target ^ (1 << first) ^ (1 << second);
                    if (distinguished_cut && lower == cut_lower) continue;
                    const int e1 = edge_variable[lower][first];
                    const int e2 = edge_variable[lower][second];
                    if (!e1 || !e2) return 4;
                    const int witness = ++variable;
                    witnesses.push_back(witness);
                    add_clause({-witness, e1});
                    add_clause({-witness, e2});
                }
            }
            add_clause(witnesses);
        }
    }

    if (enforce_long_runs) {
        // The upper-layer vertices of the alternating cycle will be the
        // prescribed central row T.  For D^3-factorability, every cyclic run
        // of a coordinate in T must have length at least four.  A run of
        // length one is already impossible in a middle-levels cycle: both
        // boundary transitions would have to use the same lower vertex
        // U\{b}.  Explicitly forbid runs of lengths two and three.
        auto transition_edges = [&] (int upper_a, int upper_b) {
            const int lower = upper_a & upper_b;
            const int bit_a = countr_zero(static_cast<unsigned>(upper_a ^ lower));
            const int bit_b = countr_zero(static_cast<unsigned>(upper_b ^ lower));
            return pair<int,int>{edge_variable[lower][bit_a],
                                 edge_variable[lower][bit_b]};
        };
        vector<int> uppers;
        for (int mask = 0; mask < limit; ++mask)
            if (popcount(static_cast<unsigned>(mask)) == lower_rank + 1)
                uppers.push_back(mask);
        long long forbidden = 0;
        for (int bit = 0; bit < k; ++bit) {
            for (int first : uppers) {
                if (!(first & (1 << bit))) continue;
                const int left_boundary = edge_variable[first ^ (1 << bit)][bit];
                for (int removed1 = 0; removed1 < k; ++removed1) {
                    if (removed1 == bit || !(first & (1 << removed1))) continue;
                    for (int added1 = 0; added1 < k; ++added1) {
                        if (first & (1 << added1)) continue;
                        const int second = first ^ (1 << removed1) ^ (1 << added1);
                        const auto [e12a, e12b] = transition_edges(first, second);
                        const int right2 = edge_variable[second ^ (1 << bit)][bit];
                        const int lower12 = first & second;
                        if (first < second &&
                            (!distinguished_cut || lower12 != cut_lower)) {
                            add_clause({-left_boundary, -e12a, -e12b, -right2});
                            ++forbidden;
                        }
                        for (int removed2 = 0; removed2 < k; ++removed2) {
                            if (removed2 == bit || !(second & (1 << removed2))) continue;
                            for (int added2 = 0; added2 < k; ++added2) {
                                if (second & (1 << added2)) continue;
                                const int third = second ^ (1 << removed2) ^ (1 << added2);
                                if (third == first || first > third) continue;
                                const int lower23 = second & third;
                                if (lower12 == lower23) continue;
                                if (distinguished_cut &&
                                    (lower12 == cut_lower || lower23 == cut_lower))
                                    continue;
                                const auto [e23a, e23b] = transition_edges(second, third);
                                const int right3 = edge_variable[third ^ (1 << bit)][bit];
                                add_clause({-left_boundary, -e12a, -e12b,
                                            -e23a, -e23b, -right3});
                                ++forbidden;
                            }
                        }
                    }
                }
            }
        }
        cerr << "forbidden_short_runs=" << forbidden << '\n';
    }
    if (cover_second_next_rank) {
        // Three consecutive upper-layer vertices form a selected alternating
        // path U1-C12-U2-C23-U3.  Enumerate exactly those paths whose union is
        // a prescribed (lower_rank+3)-set, and require one for every target.
        // Reversal gives the same window, so retain only U1<U3.
        long long witnesses_created = 0;
        for (int target = 0; target < limit; ++target) {
            if (popcount(static_cast<unsigned>(target)) != lower_rank + 3)
                continue;
            vector<int> witnesses;
            for (int middle = target; ; middle = (middle - 1) & target) {
                if (popcount(static_cast<unsigned>(middle)) == lower_rank + 1) {
                    vector<int> neighbors;
                    for (int removed = 0; removed < k; ++removed) {
                        if (!(middle & (1 << removed))) continue;
                        for (int added = 0; added < k; ++added) {
                            if (!(target & (1 << added)) || (middle & (1 << added)))
                                continue;
                            neighbors.push_back(middle ^ (1 << removed) ^ (1 << added));
                        }
                    }
                    for (int first : neighbors) for (int third : neighbors) {
                        if (first >= third || (first | middle | third) != target)
                            continue;
                        const int lower12 = first & middle;
                        const int lower23 = middle & third;
                        if (lower12 == lower23) continue;
                        if (distinguished_cut &&
                            (lower12 == cut_lower || lower23 == cut_lower))
                            continue;
                        const int first_added = countr_zero(
                            static_cast<unsigned>(first ^ lower12));
                        const int middle_added12 = countr_zero(
                            static_cast<unsigned>(middle ^ lower12));
                        const int middle_added23 = countr_zero(
                            static_cast<unsigned>(middle ^ lower23));
                        const int third_added = countr_zero(
                            static_cast<unsigned>(third ^ lower23));
                        const int witness = ++variable;
                        witnesses.push_back(witness);
                        add_clause({-witness, edge_variable[lower12][first_added]});
                        add_clause({-witness, edge_variable[lower12][middle_added12]});
                        add_clause({-witness, edge_variable[lower23][middle_added23]});
                        add_clause({-witness, edge_variable[lower23][third_added]});
                        ++witnesses_created;
                    }
                }
                if (!middle) break;
            }
            add_clause(witnesses);
        }
        cerr << "rank8_path_witnesses=" << witnesses_created << '\n';
    }
    if (cover_second_lower_rank) {
        // Dually, require every (lower_rank-1)-set to be the intersection of
        // three consecutive upper vertices.  This is the decisive lower-row
        // condition for the d=3 factor: the maximal realization then covers
        // the complete rank-4 layer in its length-two row.
        long long witnesses_created = 0;
        for (int target = 0; target < limit; ++target) {
            if (popcount(static_cast<unsigned>(target)) != lower_rank - 1)
                continue;
            vector<int> witnesses;
            // Enumerate rank-6 supersets through two-element subsets of the
            // complement of the prescribed rank-4 intersection.
            const int available = (limit - 1) ^ target;
            for (int extras = available; ; extras = (extras - 1) & available) {
                if (popcount(static_cast<unsigned>(extras)) == 2) {
                    const int middle = target | extras;
                    vector<int> neighbors;
                    for (int removed = 0; removed < k; ++removed) {
                        if (!(extras & (1 << removed))) continue;
                        for (int added = 0; added < k; ++added) {
                            if (!(available & (1 << added)) || (extras & (1 << added)))
                                continue;
                            neighbors.push_back(middle ^ (1 << removed) ^ (1 << added));
                        }
                    }
                    for (int first : neighbors) for (int third : neighbors) {
                        if (first >= third || (first & middle & third) != target)
                            continue;
                        const int lower12 = first & middle;
                        const int lower23 = middle & third;
                        if (lower12 == lower23) continue;
                        if (distinguished_cut &&
                            (lower12 == cut_lower || lower23 == cut_lower))
                            continue;
                        const int first_added = countr_zero(
                            static_cast<unsigned>(first ^ lower12));
                        const int middle_added12 = countr_zero(
                            static_cast<unsigned>(middle ^ lower12));
                        const int middle_added23 = countr_zero(
                            static_cast<unsigned>(middle ^ lower23));
                        const int third_added = countr_zero(
                            static_cast<unsigned>(third ^ lower23));
                        const int witness = ++variable;
                        witnesses.push_back(witness);
                        add_clause({-witness, edge_variable[lower12][first_added]});
                        add_clause({-witness, edge_variable[lower12][middle_added12]});
                        add_clause({-witness, edge_variable[lower23][middle_added23]});
                        add_clause({-witness, edge_variable[lower23][third_added]});
                        ++witnesses_created;
                    }
                }
                if (!extras) break;
            }
            add_clause(witnesses);
        }
        cerr << "rank4_path_witnesses=" << witnesses_created << '\n';
    }

    for (int round = 0; ; ++round) {
        if (solver.solve() != 10) {
            cerr << "UNSAT after cuts round=" << round << '\n';
            return 1;
        }
        vector<vector<int>> selected(masks.size());
        for (const Edge& edge : edges) if (solver.val(edge.variable) > 0) {
            selected[edge.u].push_back(edge.v);
            selected[edge.v].push_back(edge.u);
        }
        vector<int> component(masks.size(), -1);
        vector<vector<int>> components;
        for (int start = 0; start < static_cast<int>(masks.size()); ++start) {
            if (component[start] >= 0) continue;
            const int id = components.size();
            components.push_back({});
            queue<int> queue;
            queue.push(start);
            component[start] = id;
            while (!queue.empty()) {
                const int u = queue.front(); queue.pop();
                components.back().push_back(u);
                for (int v : selected[u]) if (component[v] < 0) {
                    component[v] = id;
                    queue.push(v);
                }
            }
        }
        cerr << "round=" << round << " cycles=" << components.size();
        for (const auto& value : components) cerr << ' ' << value.size();
        cerr << '\n';
        if (components.size() == 1) {
            vector<int> cycle;
            cycle.reserve(masks.size());
            int previous = -1, current = 0;
            do {
                cycle.push_back(current);
                const int next = selected[current][0] == previous
                    ? selected[current][1] : selected[current][0];
                previous = current;
                current = next;
            } while (current != cycle.front());
            if (cycle.size() != masks.size()) return 3;
            for (int node : cycle) cout << masks[node] << ' ';
            cout << '\n';
            return 0;
        }
        // A degree-two spanning subgraph is one cycle iff it has no proper
        // component.  Require at least one graph edge to leave every current
        // component; degree parity will force crossing edges in pairs.
        for (const vector<int>& vertices : components) {
            if (vertices.size() == masks.size()) continue;
            vector<uint8_t> inside(masks.size());
            for (int u : vertices) inside[u] = 1;
            vector<int> cut;
            for (const Edge& edge : edges)
                if (inside[edge.u] != inside[edge.v]) cut.push_back(edge.variable);
            add_clause(cut);
        }
    }
}
