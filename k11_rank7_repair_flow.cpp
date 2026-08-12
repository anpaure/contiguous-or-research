#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#endif

#include <algorithm>
#include <bit>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

struct Edge {
    int to;
    int reverse;
    int capacity;
};

struct Dinic {
    vector<vector<Edge>> graph;
    vector<int> level;
    vector<int> next;

    explicit Dinic(int n) : graph(n), level(n), next(n) {}

    void add_edge(int from, int to, int capacity) {
        Edge a{to, static_cast<int>(graph[to].size()), capacity};
        Edge b{from, static_cast<int>(graph[from].size()), 0};
        graph[from].push_back(a);
        graph[to].push_back(b);
    }

    bool bfs(int source, int sink) {
        fill(level.begin(), level.end(), -1);
        queue<int> q;
        level[source] = 0;
        q.push(source);
        while (!q.empty()) {
            const int from = q.front();
            q.pop();
            for (const Edge& edge : graph[from])
                if (edge.capacity && level[edge.to] < 0) {
                    level[edge.to] = level[from] + 1;
                    q.push(edge.to);
                }
        }
        return level[sink] >= 0;
    }

    int dfs(int from, int sink, int pushed) {
        if (from == sink) return pushed;
        for (int& index = next[from]; index < static_cast<int>(graph[from].size()); ++index) {
            Edge& edge = graph[from][index];
            if (!edge.capacity || level[edge.to] != level[from] + 1) continue;
            const int value = dfs(edge.to, sink, min(pushed, edge.capacity));
            if (!value) continue;
            edge.capacity -= value;
            graph[edge.to][edge.reverse].capacity += value;
            return value;
        }
        return 0;
    }

    int max_flow(int source, int sink) {
        int result = 0;
        while (bfs(source, sink)) {
            fill(next.begin(), next.end(), 0);
            while (const int value = dfs(source, sink, 1'000'000)) result += value;
        }
        return result;
    }
};

int main(int argc, char** argv) {
    if (argc != 3) return 2;
    const int k = stoi(argv[1]);
    const int rank = stoi(argv[2]);
    const int limit = 1 << k;
    vector<int> path;
    for (int value; cin >> value;) path.push_back(value);
    if (path.size() < 2) return 2;

    vector<int> current_upper(limit, -1);
    vector<int> upper_multiplicity(limit);
    vector<int> lower_present(limit);
    for (int i = 0; i + 1 < static_cast<int>(path.size()); ++i) {
        const int lower = path[i] & path[i + 1];
        const int upper = path[i] | path[i + 1];
        if (popcount(static_cast<unsigned>(lower)) != rank - 1 ||
            popcount(static_cast<unsigned>(upper)) != rank + 1) return 3;
        if (current_upper[lower] >= 0) return 4;
        current_upper[lower] = upper;
        lower_present[lower] = 1;
        ++upper_multiplicity[upper];
    }

    vector<int> missing;
    vector<int> lowers;
    vector<int> uppers;
    for (int mask = 0; mask < limit; ++mask) {
        const int weight = popcount(static_cast<unsigned>(mask));
        if (weight == rank - 1 && lower_present[mask]) lowers.push_back(mask);
        if (weight == rank + 1) {
            uppers.push_back(mask);
            if (!upper_multiplicity[mask]) missing.push_back(mask);
        }
    }

    const int source = 0;
    const int missing_offset = 1;
    const int lower_offset = missing_offset + missing.size();
    const int upper_offset = lower_offset + lowers.size();
    const int sink = upper_offset + uppers.size();
    Dinic flow(sink + 1);
    vector<int> upper_node(limit, -1);
    for (int i = 0; i < static_cast<int>(uppers.size()); ++i) {
        upper_node[uppers[i]] = upper_offset + i;
        flow.add_edge(upper_offset + i, sink, max(0, upper_multiplicity[uppers[i]] - 1));
    }
    for (int i = 0; i < static_cast<int>(missing.size()); ++i) {
        const int node = missing_offset + i;
        flow.add_edge(source, node, 1);
        for (int j = 0; j < static_cast<int>(lowers.size()); ++j) {
            const int lower = lowers[j];
            if ((lower & missing[i]) != lower) continue;
            if (upper_multiplicity[current_upper[lower]] < 2) continue;
            flow.add_edge(node, lower_offset + j, 1);
        }
    }
    for (int j = 0; j < static_cast<int>(lowers.size()); ++j) {
        const int lower = lowers[j];
        flow.add_edge(lower_offset + j, upper_node[current_upper[lower]], 1);
    }

    const int value = flow.max_flow(source, sink);
    cout << "missing_rank" << rank + 1 << '=' << missing.size()
         << " maximum_safe_reassignments=" << value << '\n';
    for (int i = 0; i < static_cast<int>(missing.size()); ++i) {
        const int node = missing_offset + i;
        for (const Edge& edge : flow.graph[node]) {
            if (edge.to < lower_offset || edge.to >= upper_offset) continue;
            // Unit forward edge was used exactly when its residual capacity is zero.
            if (edge.capacity) continue;
            const int lower = lowers[edge.to - lower_offset];
            cout << "target=" << missing[i] << " donor_lower=" << lower
                 << " displaced_upper=" << current_upper[lower]
                 << " displaced_multiplicity="
                 << upper_multiplicity[current_upper[lower]] << '\n';
        }
    }
    return value == static_cast<int>(missing.size()) ? 0 : 1;
}
