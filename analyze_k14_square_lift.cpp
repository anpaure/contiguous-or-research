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
#include <numeric>
#include <queue>
#include <unordered_set>
#include <vector>
using namespace std;

int main() {
    constexpr int old_bits = 12, bits = 14;
    constexpr int xbit = 1 << 12, ybit = 1 << 13;
    constexpr int limit = 1 << bits;
    vector<int> path;
    for (int value; cin >> value;) path.push_back(value);
    if (path.size() != 924) return 2;
    vector<int> lower(path.size() - 1), upper(path.size() - 1);
    for (int i = 0; i + 1 < static_cast<int>(path.size()); ++i) {
        if (popcount(static_cast<unsigned>(path[i] ^ path[i + 1])) != 2) return 3;
        lower[i] = path[i] & path[i + 1];
        upper[i] = path[i] | path[i + 1];
    }

    vector<char> vertex(limit), lower_color(limit), upper_color(limit);
    unordered_set<uint32_t> edge_keys;
    vector<pair<int, int>> edges;
    auto add_edge = [&](int a, int b) {
        if (a == b) return;
        if (popcount(static_cast<unsigned>(a)) != 7 ||
            popcount(static_cast<unsigned>(b)) != 7 ||
            popcount(static_cast<unsigned>(a ^ b)) != 2) {
            cerr << "invalid edge " << a << ' ' << b << '\n';
            exit(4);
        }
        if (a > b) swap(a, b);
        const uint32_t key = (static_cast<uint32_t>(a) << bits) | b;
        if (!edge_keys.insert(key).second) return;
        edges.push_back({a, b});
        vertex[a] = vertex[b] = true;
        lower_color[a & b] = true;
        upper_color[a | b] = true;
    };

    for (int i = 0; i < static_cast<int>(lower.size()); ++i) {
        const int a = upper[i];
        const int b = xbit | path[i];
        const int c = xbit | ybit | lower[i];
        const int d = ybit | path[i + 1];
        add_edge(a, b); add_edge(b, c); add_edge(c, d); add_edge(d, a);
    }
    // Horizontal traces.  The exact k=12 path makes lower and upper derived
    // rows into Johnson walks (allowing equality only in the upper row).
    for (int i = 0; i + 1 < static_cast<int>(path.size()); ++i) {
        add_edge(xbit | path[i], xbit | path[i + 1]);
        add_edge(ybit | path[i], ybit | path[i + 1]);
    }
    for (int i = 0; i + 1 < static_cast<int>(lower.size()); ++i) {
        add_edge(xbit | ybit | lower[i], xbit | ybit | lower[i + 1]);
        if (upper[i] != upper[i + 1]) add_edge(upper[i], upper[i + 1]);
    }

    int vertices = 0, wanted_vertices = 0, lower_colors = 0, upper_colors = 0;
    for (int mask = 0; mask < limit; ++mask) {
        const int rank = popcount(static_cast<unsigned>(mask));
        vertices += vertex[mask];
        wanted_vertices += rank == 7;
        lower_colors += rank == 6 && lower_color[mask];
        upper_colors += rank == 8 && upper_color[mask];
    }
    vector<vector<int>> adjacency(limit);
    for (auto [a, b] : edges) {
        adjacency[a].push_back(b);
        adjacency[b].push_back(a);
    }
    int components = 0;
    vector<char> reached(limit);
    array<int, 64> degree_histogram{};
    for (int mask = 0; mask < limit; ++mask) if (vertex[mask]) {
        ++degree_histogram[adjacency[mask].size()];
        if (reached[mask]) continue;
        ++components;
        queue<int> pending;
        pending.push(mask); reached[mask] = true;
        while (!pending.empty()) {
            const int here = pending.front(); pending.pop();
            for (int next : adjacency[here]) if (!reached[next]) {
                reached[next] = true; pending.push(next);
            }
        }
    }
    cout << "vertices=" << vertices << '/' << wanted_vertices
         << " edges=" << edges.size() << " components=" << components
         << " lower_colors=" << lower_colors << "/3003"
         << " upper_colors=" << upper_colors << "/3003\n";
    cout << "degrees";
    for (int degree = 0; degree < static_cast<int>(degree_histogram.size()); ++degree)
        if (degree_histogram[degree]) cout << ' ' << degree << ':' << degree_histogram[degree];
    cout << '\n';

    array<int, 4> lower_classes{}, upper_classes{};
    for (int mask = 0; mask < limit; ++mask) {
        const int new_bits = ((mask & xbit) != 0) + ((mask & ybit) != 0);
        if (popcount(static_cast<unsigned>(mask)) == 6 && lower_color[mask])
            ++lower_classes[new_bits];
        if (popcount(static_cast<unsigned>(mask)) == 8 && upper_color[mask])
            ++upper_classes[new_bits];
    }
    cout << "lower_classes";
    for (int i = 0; i <= 2; ++i) cout << ' ' << i << ':' << lower_classes[i];
    cout << " upper_classes";
    for (int i = 0; i <= 2; ++i) cout << ' ' << i << ':' << upper_classes[i];
    cout << '\n';
}
