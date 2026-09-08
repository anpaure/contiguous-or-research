#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <cadical.hpp>

#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <queue>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
using namespace std;

struct Edge { int a, b, variable; };

int main(int argc, char** argv) {
    if (argc < 3 || argc > 4) {
        cerr << "usage: k14_square_path_sat SEED OUTPUT [plain|colors|runs|both] "
                "< K12_CENTRAL_PATH\n";
        return 2;
    }
    const string mode = argc == 4 ? argv[3] : "both";
    const bool enforce_colors = mode == "colors" || mode == "both";
    const bool enforce_runs = mode == "runs" || mode == "both";
    if (mode != "plain" && mode != "colors" && mode != "runs" && mode != "both")
        return 2;
    constexpr int bits = 14, limit = 1 << bits;
    constexpr int xbit = 1 << 12, ybit = 1 << 13;
    vector<int> base;
    for (int value; cin >> value;) base.push_back(value);
    if (base.size() != 924) return 3;
    vector<int> lower(base.size() - 1), upper(base.size() - 1);
    for (int i = 0; i + 1 < static_cast<int>(base.size()); ++i) {
        if (popcount(static_cast<unsigned>(base[i] ^ base[i + 1])) != 2) return 4;
        lower[i] = base[i] & base[i + 1];
        upper[i] = base[i] | base[i + 1];
    }

    vector<Edge> edges;
    vector<vector<int>> incident_mask(limit);
    vector<char> is_vertex(limit);
    unordered_set<uint32_t> edge_keys;
    auto add_edge = [&](int a, int b) {
        if (a == b) return;
        if (popcount(static_cast<unsigned>(a)) != 7 ||
            popcount(static_cast<unsigned>(b)) != 7 ||
            popcount(static_cast<unsigned>(a ^ b)) != 2) exit(5);
        if (a > b) swap(a, b);
        const uint32_t key = (static_cast<uint32_t>(a) << bits) | b;
        if (!edge_keys.insert(key).second) return;
        const int id = edges.size();
        edges.push_back({a, b, id + 1});
        incident_mask[a].push_back(id);
        incident_mask[b].push_back(id);
        is_vertex[a] = is_vertex[b] = true;
    };
    for (int i = 0; i < static_cast<int>(lower.size()); ++i) {
        const int a = upper[i];
        const int b = xbit | base[i];
        const int c = xbit | ybit | lower[i];
        const int d = ybit | base[i + 1];
        add_edge(a, b); add_edge(b, c); add_edge(c, d); add_edge(d, a);
    }
    for (int i = 0; i + 1 < static_cast<int>(base.size()); ++i) {
        add_edge(xbit | base[i], xbit | base[i + 1]);
        add_edge(ybit | base[i], ybit | base[i + 1]);
    }
    for (int i = 0; i + 1 < static_cast<int>(lower.size()); ++i) {
        add_edge(xbit | ybit | lower[i], xbit | ybit | lower[i + 1]);
        if (upper[i] != upper[i + 1]) add_edge(upper[i], upper[i + 1]);
    }
    vector<int> forced_endpoint;
    for (int mask = 0; mask < limit; ++mask)
        if (is_vertex[mask] && incident_mask[mask].size() == 1)
            forced_endpoint.push_back(mask);
    if (forced_endpoint.size() != 2) return 6;
    if (const char* extra_path_file = getenv("K14_EXTRA_PATH")) {
        ifstream input(extra_path_file);
        vector<int> extra;
        for (int value; input >> value;) extra.push_back(value);
        if (extra.size() != 3432) return 15;
        for (int i = 0; i + 1 < static_cast<int>(extra.size()); ++i)
            add_edge(extra[i], extra[i + 1]);
    }

    vector<int> vertices, endpoint = forced_endpoint;
    for (int mask = 0; mask < limit; ++mask) if (is_vertex[mask]) {
        vertices.push_back(mask);
    }
    if (vertices.size() != 3432) return 6;

    CaDiCaL::Solver solver;
    solver.set("quiet", 1);
    solver.set("seed", stoi(argv[1]));
    solver.declare_more_variables(200000);
    long long clauses = 0;
    auto clause = [&](const vector<int>& values) {
        for (int literal : values) solver.add(literal);
        solver.add(0); ++clauses;
    };

    // Forced endpoint-to-endpoint spanning path degree constraints.
    for (int vertex : vertices) {
        vector<int> literals;
        for (int id : incident_mask[vertex]) literals.push_back(edges[id].variable);
        const int wanted = find(endpoint.begin(), endpoint.end(), vertex) != endpoint.end() ? 1 : 2;
        clause(literals); // at least one
        if (wanted == 1) {
            for (int i = 0; i < static_cast<int>(literals.size()); ++i)
                for (int j = i + 1; j < static_cast<int>(literals.size()); ++j)
                    clause({-literals[i], -literals[j]});
        } else {
            // At least two: after omitting any one incident edge, some other
            // edge must be selected.  At most two uses direct triples because
            // the square-lift graph has maximum degree 12.
            for (int omitted = 0; omitted < static_cast<int>(literals.size()); ++omitted) {
                vector<int> rest;
                for (int i = 0; i < static_cast<int>(literals.size()); ++i)
                    if (i != omitted) rest.push_back(literals[i]);
                clause(rest);
            }
            for (int i = 0; i < static_cast<int>(literals.size()); ++i)
                for (int j = i + 1; j < static_cast<int>(literals.size()); ++j)
                    for (int h = j + 1; h < static_cast<int>(literals.size()); ++h)
                        clause({-literals[i], -literals[j], -literals[h]});
        }
    }

    // Both edge-color projections must be surjective.
    vector<vector<int>> lower_witness(limit), upper_witness(limit);
    for (const Edge& edge : edges) {
        lower_witness[edge.a & edge.b].push_back(edge.variable);
        upper_witness[edge.a | edge.b].push_back(edge.variable);
    }
    if (enforce_colors)
        for (int mask = 0; mask < limit; ++mask) {
            const int rank = popcount(static_cast<unsigned>(mask));
            if (rank == 6) clause(lower_witness[mask]);
            if (rank == 8) clause(upper_witness[mask]);
        }

    // For d=2, factorability is exactly the absence of internal coordinate
    // 1-runs of lengths one and two.  These are local selected-edge patterns.
    vector<char> is_endpoint(limit);
    for (int value : endpoint) is_endpoint[value] = true;
    if (enforce_runs) for (int bit = 0; bit < bits; ++bit) {
        const int flag = 1 << bit;
        for (int vertex : vertices) if ((vertex & flag) && !is_endpoint[vertex]) {
            vector<int> exits;
            for (int id : incident_mask[vertex]) {
                const Edge& edge = edges[id];
                const int other = edge.a ^ edge.b ^ vertex;
                if (!(other & flag)) exits.push_back(edge.variable);
            }
            for (int i = 0; i < static_cast<int>(exits.size()); ++i)
                for (int j = i + 1; j < static_cast<int>(exits.size()); ++j)
                    clause({-exits[i], -exits[j]});
        }
        for (const Edge& middle : edges) {
            if (!(middle.a & flag) || !(middle.b & flag)) continue;
            vector<int> left_exits, right_exits;
            for (int id : incident_mask[middle.a]) if (id != middle.variable - 1) {
                const Edge& edge = edges[id];
                const int other = edge.a ^ edge.b ^ middle.a;
                if (!(other & flag)) left_exits.push_back(edge.variable);
            }
            for (int id : incident_mask[middle.b]) if (id != middle.variable - 1) {
                const Edge& edge = edges[id];
                const int other = edge.a ^ edge.b ^ middle.b;
                if (!(other & flag)) right_exits.push_back(edge.variable);
            }
            for (int left : left_exits) for (int right : right_exits)
                clause({-middle.variable, -left, -right});
        }
    }

    cerr << "vertices=" << vertices.size() << " edges=" << edges.size()
         << " clauses=" << clauses << " endpoints=" << endpoint[0] << ',' << endpoint[1]
         << '\n';
    int rounds = 0;
    vector<char> selected(edges.size());
    while (true) {
        const int result = solver.solve();
        if (result != 10) {
            cerr << (result == 20 ? "UNSAT" : "UNKNOWN") << " rounds=" << rounds << '\n';
            return result == 20 ? 1 : 7;
        }
        for (int id = 0; id < static_cast<int>(edges.size()); ++id)
            selected[id] = solver.val(edges[id].variable) > 0;
        vector<char> reached(limit);
        vector<int> component_of(limit, -1);
        vector<vector<int>> components;
        for (int root : vertices) if (!reached[root]) {
            const int component = components.size();
            components.push_back({});
            queue<int> pending;
            pending.push(root); reached[root] = true;
            while (!pending.empty()) {
                const int here = pending.front(); pending.pop();
                component_of[here] = component;
                components.back().push_back(here);
                for (int id : incident_mask[here]) if (selected[id]) {
                    const Edge& edge = edges[id];
                    const int next = edge.a ^ edge.b ^ here;
                    if (!reached[next]) reached[next] = true, pending.push(next);
                }
            }
        }
        cerr << "round=" << rounds << " components=" << components.size();
        for (int i = 0; i < min<int>(8, components.size()); ++i)
            cerr << ' ' << components[i].size();
        cerr << '\n';
        if (components.size() == 1) break;
        const int path_component = component_of[endpoint[0]];
        for (int component = 0; component < static_cast<int>(components.size()); ++component) {
            if (component == path_component) continue;
            vector<int> crossing;
            for (const Edge& edge : edges)
                if ((component_of[edge.a] == component) !=
                    (component_of[edge.b] == component))
                    crossing.push_back(edge.variable);
            if (crossing.empty()) return 8;
            clause(crossing);
        }
        ++rounds;
    }

    vector<int> path;
    path.reserve(vertices.size());
    int previous = -1, current = endpoint[0];
    while (true) {
        path.push_back(current);
        int next = -1;
        for (int id : incident_mask[current]) if (selected[id]) {
            const Edge& edge = edges[id];
            const int candidate = edge.a ^ edge.b ^ current;
            if (candidate != previous) { next = candidate; break; }
        }
        if (next < 0) break;
        previous = current; current = next;
    }
    if (path.size() != vertices.size() || path.back() != endpoint[1]) return 9;

    // Independent structural audit.
    vector<char> seen_vertex(limit), seen_lower(limit), seen_upper(limit);
    for (int value : path) {
        if (seen_vertex[value] || popcount(static_cast<unsigned>(value)) != 7) return 10;
        seen_vertex[value] = true;
    }
    for (int i = 0; i + 1 < static_cast<int>(path.size()); ++i) {
        if (popcount(static_cast<unsigned>(path[i] ^ path[i + 1])) != 2) return 11;
        seen_lower[path[i] & path[i + 1]] = true;
        seen_upper[path[i] | path[i + 1]] = true;
    }
    if (enforce_colors)
        for (int mask = 0; mask < limit; ++mask) {
            const int rank = popcount(static_cast<unsigned>(mask));
            if (rank == 6 && !seen_lower[mask]) return 12;
            if (rank == 8 && !seen_upper[mask]) return 13;
        }
    if (enforce_runs) for (int bit = 0; bit < bits; ++bit) {
        int i = 0;
        while (i < static_cast<int>(path.size())) {
            if (!(path[i] & (1 << bit))) { ++i; continue; }
            const int first = i;
            while (i < static_cast<int>(path.size()) && (path[i] & (1 << bit))) ++i;
            if (first && i < static_cast<int>(path.size()) && i - first < 3) return 14;
        }
    }
    ofstream out(argv[2]);
    for (int value : path) out << value << ' ';
    out << '\n';
    cerr << "SAT path=" << path.size() << " rounds=" << rounds << '\n';
}
