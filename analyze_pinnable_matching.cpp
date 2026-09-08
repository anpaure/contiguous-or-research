#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <algorithm>
#include <bit>
#include <iostream>
#include <queue>
#include <array>
#include <limits>
#include <tuple>
#include <vector>
using namespace std;

int main(int argc, char** argv) {
    if (argc != 3) return 2;
    const int k = stoi(argv[1]), d = stoi(argv[2]);
    const int limit = 1 << k, full = limit - 1;
    vector<int> central;
    for (int x; cin >> x;) central.push_back(x);
    if (central.empty()) return 3;
    const int rank = popcount(static_cast<unsigned>(central.front()));
    const int n = central.size() + d;
    vector<int> envelope(n, full);
    for (int p = 0; p < n; ++p)
        for (int i = max(0, p - d); i <= min<int>(central.size() - 1, p); ++i)
            envelope[p] &= central[i];

    vector<int> targets, target_index(limit, -1);
    for (int x = 1; x < limit; ++x)
        if (popcount(static_cast<unsigned>(x)) < rank) {
            target_index[x] = targets.size();
            targets.push_back(x);
        }
    struct Interval { int left, length; };
    vector<Interval> intervals;
    for (int length = 1; length <= d; ++length)
        for (int left = 0; left + length <= n; ++left)
            intervals.push_back({left, length});
    vector<vector<int>> adjacency(targets.size());
    vector<int> candidates_by_rank_min(rank, 1 << 30), candidates_by_rank_max(rank);
    for (int id = 0; id < static_cast<int>(intervals.size()); ++id) {
        const auto [left, length] = intervals[id];
        int allowed = 0;
        for (int p = left; p < left + length; ++p) allowed |= envelope[p];
        for (int target = allowed; target; target = (target - 1) & allowed) {
            const int ti = target_index[target];
            if (ti < 0) continue;
            bool nonzero = true;
            for (int p = left; p < left + length; ++p)
                nonzero &= (target & envelope[p]) != 0;
            if (nonzero) adjacency[ti].push_back(id);
        }
    }
    for (int i = 0; i < static_cast<int>(targets.size()); ++i) {
        const int r = popcount(static_cast<unsigned>(targets[i]));
        candidates_by_rank_min[r] = min<int>(candidates_by_rank_min[r], adjacency[i].size());
        candidates_by_rank_max[r] = max<int>(candidates_by_rank_max[r], adjacency[i].size());
    }

    // Hopcroft--Karp: lower targets on the left, physical short intervals on
    // the right.  This tests the ordinary injective-assignment Hall condition
    // before any coordinate pin-survival interactions are imposed.
    vector<int> left_match(targets.size(), -1), right_match(intervals.size(), -1), distance(targets.size());
    auto bfs = [&]() {
        queue<int> q;
        bool augmenting = false;
        for (int u = 0; u < static_cast<int>(targets.size()); ++u) {
            if (left_match[u] < 0) distance[u] = 0, q.push(u);
            else distance[u] = -1;
        }
        while (!q.empty()) {
            const int u = q.front(); q.pop();
            for (int v : adjacency[u]) {
                const int next = right_match[v];
                if (next < 0) augmenting = true;
                else if (distance[next] < 0) distance[next] = distance[u] + 1, q.push(next);
            }
        }
        return augmenting;
    };
    auto dfs = [&](auto&& self, int u) -> bool {
        for (int v : adjacency[u]) {
            const int next = right_match[v];
            if (next < 0 || (distance[next] == distance[u] + 1 && self(self, next))) {
                left_match[u] = v;
                right_match[v] = u;
                return true;
            }
        }
        distance[u] = -1;
        return false;
    };
    int matching = 0;
    while (bfs())
        for (int u = 0; u < static_cast<int>(targets.size()); ++u)
            if (left_match[u] < 0 && dfs(dfs, u)) ++matching;

    // The alternating-reachability set from all unmatched left vertices is an
    // explicit Hall witness.  Let U be the reachable targets and N(U) the
    // reachable intervals.  Every unmatched edge is traversed left-to-right
    // and every matched edge right-to-left, so N(U) is exactly the displayed
    // right set and |U|-|N(U)| is the matching deficiency.
    vector<char> hall_left(targets.size()), hall_right(intervals.size());
    queue<int> hall_queue;
    for (int u = 0; u < static_cast<int>(targets.size()); ++u)
        if (left_match[u] < 0) hall_left[u] = true, hall_queue.push(u);
    while (!hall_queue.empty()) {
        const int u = hall_queue.front(); hall_queue.pop();
        for (int v : adjacency[u]) {
            if (left_match[u] == v || hall_right[v]) continue;
            hall_right[v] = true;
            const int next = right_match[v];
            if (next >= 0 && !hall_left[next]) {
                hall_left[next] = true;
                hall_queue.push(next);
            }
        }
    }

    cout << "targets=" << targets.size() << " intervals=" << intervals.size()
         << " candidate_edges=";
    long long edges = 0;
    for (const auto& list : adjacency) edges += list.size();
    cout << edges << " matching=" << matching << " deficiency="
         << targets.size() - matching << '\n';
    for (int r = 1; r < rank; ++r)
        cout << "rank=" << r << " candidates_min=" << candidates_by_rank_min[r]
             << " max=" << candidates_by_rank_max[r] << '\n';
    array<int, 32> hall_rank{};
    array<int, 32> hall_length{};
    int hall_left_count = 0, hall_right_count = 0;
    for (int u = 0; u < static_cast<int>(targets.size()); ++u)
        if (hall_left[u]) {
            ++hall_left_count;
            ++hall_rank[popcount(static_cast<unsigned>(targets[u]))];
        }
    for (int v = 0; v < static_cast<int>(intervals.size()); ++v)
        if (hall_right[v]) {
            ++hall_right_count;
            ++hall_length[intervals[v].length];
        }
    cout << "hall_targets=" << hall_left_count
         << " hall_neighbors=" << hall_right_count
         << " hall_deficiency=" << hall_left_count - hall_right_count << '\n';
    cout << "hall_target_ranks";
    for (int r = 1; r < rank; ++r) cout << ' ' << r << ':' << hall_rank[r];
    cout << '\n';
    cout << "hall_interval_lengths";
    for (int length = 1; length <= d; ++length)
        cout << ' ' << length << ':' << hall_length[length];
    cout << '\n';

    struct HallComponent {
        int left = 0, right = 0, min_position = 0, max_position = 0;
        int common_mask = 0, union_mask = 0;
        array<int, 32> ranks{};
    };
    vector<vector<int>> reverse_adjacency(intervals.size());
    for (int u = 0; u < static_cast<int>(targets.size()); ++u)
        if (hall_left[u])
            for (int v : adjacency[u])
                if (hall_right[v]) reverse_adjacency[v].push_back(u);
    vector<char> component_left(targets.size()), component_right(intervals.size());
    vector<HallComponent> components;
    for (int root = 0; root < static_cast<int>(targets.size()); ++root) {
        if (!hall_left[root] || component_left[root]) continue;
        HallComponent component;
        component.min_position = numeric_limits<int>::max();
        component.max_position = -1;
        component.common_mask = full;
        queue<pair<int, int>> pending; // side 0 = target, side 1 = interval
        component_left[root] = true;
        pending.push({0, root});
        while (!pending.empty()) {
            auto [side, id] = pending.front(); pending.pop();
            if (side == 0) {
                ++component.left;
                component.common_mask &= targets[id];
                component.union_mask |= targets[id];
                ++component.ranks[popcount(static_cast<unsigned>(targets[id]))];
                for (int v : adjacency[id])
                    if (hall_right[v] && !component_right[v]) {
                        component_right[v] = true;
                        pending.push({1, v});
                    }
            } else {
                ++component.right;
                component.min_position = min(component.min_position, intervals[id].left);
                component.max_position = max(component.max_position,
                                             intervals[id].left + intervals[id].length - 1);
                for (int u : reverse_adjacency[id])
                    if (!component_left[u]) {
                        component_left[u] = true;
                        pending.push({0, u});
                    }
            }
        }
        components.push_back(component);
    }
    sort(components.begin(), components.end(), [](const auto& a, const auto& b) {
        const int deficiency_a = a.left - a.right;
        const int deficiency_b = b.left - b.right;
        if (deficiency_a != deficiency_b) return deficiency_a > deficiency_b;
        return a.left > b.left;
    });
    cout << "hall_components=" << components.size() << '\n';
    for (int i = 0; i < min<int>(20, components.size()); ++i) {
        const auto& component = components[i];
        cout << "component=" << i
             << " targets=" << component.left
             << " neighbors=" << component.right
             << " deficiency=" << component.left - component.right
             << " positions=[" << component.min_position << ',' << component.max_position << ']'
             << " common=" << component.common_mask
             << " union=" << component.union_mask
             << " ranks";
        for (int r = 1; r < rank; ++r)
            if (component.ranks[r]) cout << ' ' << r << ':' << component.ranks[r];
        cout << '\n';
    }
    int shown = 0;
    cout << "unmatched";
    for (int i = 0; i < static_cast<int>(targets.size()) && shown < 50; ++i)
        if (left_match[i] < 0) cout << ' ' << targets[i], ++shown;
    cout << '\n';
}
