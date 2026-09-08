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
#include <utility>
#include <vector>

using namespace std;

namespace {

struct UpperConstraint {
    int mask = 0;
    vector<pair<int, int>> edges;
};

struct SingletonUpper {
    int mask = 0;
    int base_vertex = -1;
    int missing_bits = 0;
};

vector<char> covered_masks(const vector<int>& word, int limit) {
    vector<char> seen(limit, false);
    vector<int> previous, current;
    previous.reserve(32);
    current.reserve(32);
    for (int x : word) {
        current.clear();
        current.push_back(x);
        for (int old : previous) current.push_back(old | x);
        sort(current.begin(), current.end());
        current.erase(unique(current.begin(), current.end()), current.end());
        for (int value : current) seen[value] = true;
        previous.swap(current);
    }
    return seen;
}

bool connected(int source, int target, const vector<vector<int>>& graph) {
    vector<int> stack{source};
    vector<char> seen(graph.size(), false);
    seen[source] = true;
    while (!stack.empty()) {
        int vertex = stack.back();
        stack.pop_back();
        if (vertex == target) return true;
        for (int next : graph[vertex]) {
            if (seen[next]) continue;
            seen[next] = true;
            stack.push_back(next);
        }
    }
    return false;
}

bool choose_forest(int depth, const vector<UpperConstraint>& constraints,
                   vector<vector<int>>& graph, vector<int>& degree,
                   vector<pair<int, int>>& chosen) {
    if (depth == static_cast<int>(constraints.size())) return true;

    vector<pair<int, int>> candidates = constraints[depth].edges;
    stable_sort(candidates.begin(), candidates.end(), [&](auto a, auto b) {
        int score_a = degree[a.first] + degree[a.second];
        int score_b = degree[b.first] + degree[b.second];
        return score_a < score_b;
    });

    for (auto [u, v] : candidates) {
        if (degree[u] == 2 || degree[v] == 2) continue;
        if (connected(u, v, graph)) continue;
        graph[u].push_back(v);
        graph[v].push_back(u);
        ++degree[u];
        ++degree[v];
        chosen[depth] = {u, v};
        if (choose_forest(depth + 1, constraints, graph, degree, chosen))
            return true;
        --degree[u];
        --degree[v];
        graph[u].pop_back();
        graph[v].pop_back();
    }
    return false;
}

void enumerate_matchings(int first, const vector<vector<char>>& compatible,
                         vector<char>& used, vector<pair<int, int>>& current,
                         vector<vector<pair<int, int>>>& result) {
    const int n = static_cast<int>(used.size());
    while (first < n && used[first]) ++first;
    if (first == n) {
        result.push_back(current);
        return;
    }
    used[first] = true;
    enumerate_matchings(first + 1, compatible, used, current, result);
    for (int other = first + 1; other < n; ++other) {
        if (used[other] || !compatible[first][other]) continue;
        used[other] = true;
        current.push_back({first, other});
        enumerate_matchings(first + 1, compatible, used, current, result);
        current.pop_back();
        used[other] = false;
    }
    used[first] = false;
}

vector<int> linearize_forest(const vector<vector<int>>& graph) {
    const int n = static_cast<int>(graph.size());
    vector<char> used(n, false);
    vector<int> order;
    order.reserve(n);
    for (int start = 0; start < n; ++start) {
        if (used[start] || graph[start].size() == 2) continue;
        int previous = -1;
        int current = start;
        while (current >= 0 && !used[current]) {
            used[current] = true;
            order.push_back(current);
            int next = -1;
            for (int candidate : graph[current])
                if (candidate != previous) {
                    next = candidate;
                    break;
                }
            previous = current;
            current = next;
        }
    }
    return order;
}

void write_word(const string& path, const vector<int>& word) {
    ofstream output(path);
    if (!output) throw runtime_error("could not open output " + path);
    for (int value : word) output << value << '\n';
}

}  // namespace

int main(int argc, char** argv) {
    if (argc != 7) {
        cerr << "usage: partial_completion_forest k lower_rank partial.txt "
                "completion.txt completed.txt missing.txt\n";
        return 2;
    }
    const int k = stoi(argv[1]);
    const int lower_rank = stoi(argv[2]);
    const int limit = 1 << k;
    vector<int> partial;
    {
        ifstream input(argv[3]);
        if (!input) {
            cerr << "could not open partial word\n";
            return 2;
        }
        for (int value; input >> value;) {
            if (value <= 0 || value >= limit) {
                cerr << "entry outside nonzero k-bit range\n";
                return 2;
            }
            partial.push_back(value);
        }
    }

    const vector<char> partial_seen = covered_masks(partial, limit);
    vector<int> lower, upper;
    {
        ofstream missing_output(argv[6]);
        for (int mask = 1; mask < limit; ++mask) {
            if (partial_seen[mask]) continue;
            int rank = popcount(static_cast<unsigned>(mask));
            missing_output << mask << ' ' << rank << '\n';
            if (rank == lower_rank)
                lower.push_back(mask);
            else if (rank == lower_rank + 1)
                upper.push_back(mask);
            else {
                cerr << "unexpected missing rank " << rank << " mask "
                     << mask << '\n';
                return 3;
            }
        }
    }

    vector<UpperConstraint> constraints;
    vector<SingletonUpper> singleton_upper;
    vector<int> literal_upper;
    for (int target : upper) {
        UpperConstraint constraint;
        constraint.mask = target;
        vector<int> contained;
        for (int i = 0; i < static_cast<int>(lower.size()); ++i)
            if ((lower[i] | target) == target) contained.push_back(i);
        for (int i = 0; i < static_cast<int>(contained.size()); ++i)
            for (int j = i + 1; j < static_cast<int>(contained.size()); ++j) {
                int u = contained[i], v = contained[j];
                if ((lower[u] | lower[v]) == target)
                    constraint.edges.push_back({u, v});
            }
        cout << "upper=" << target << " contained_lower=" << contained.size()
             << " pair_edges=" << constraint.edges.size() << " lowers=";
        for (int vertex : contained) cout << lower[vertex] << ',';
        cout << '\n';
        if (!constraint.edges.empty()) {
            constraints.push_back(std::move(constraint));
        } else if (contained.size() == 1) {
            const int base = contained[0];
            singleton_upper.push_back(
                {target, base, target & ~lower[base]});
        } else {
            literal_upper.push_back(target);
        }
    }
    sort(constraints.begin(), constraints.end(), [](const auto& a, const auto& b) {
        return a.edges.size() < b.edges.size();
    });

    vector<vector<char>> compatible(singleton_upper.size(),
                                    vector<char>(singleton_upper.size(), false));
    for (int i = 0; i < static_cast<int>(singleton_upper.size()); ++i)
        for (int j = i + 1; j < static_cast<int>(singleton_upper.size()); ++j) {
            int x = singleton_upper[i].missing_bits |
                    singleton_upper[j].missing_bits;
            compatible[i][j] = compatible[j][i] =
                (x | singleton_upper[i].mask) == singleton_upper[i].mask &&
                (x | singleton_upper[j].mask) == singleton_upper[j].mask;
        }
    vector<vector<pair<int, int>>> matchings;
    vector<pair<int, int>> current_matching;
    vector<char> matching_used(singleton_upper.size(), false);
    enumerate_matchings(0, compatible, matching_used, current_matching, matchings);
    stable_sort(matchings.begin(), matchings.end(), [](const auto& a, const auto& b) {
        return a.size() > b.size();
    });

    vector<vector<int>> graph;
    vector<int> vertex_value;
    vector<pair<int, int>> selected_matching;
    bool solved = false;
    for (const auto& matching : matchings) {
        graph.assign(lower.size() + matching.size(), {});
        vector<int> degree(graph.size(), 0);
        vertex_value = lower;
        vector<char> used_singleton(singleton_upper.size(), false);
        bool valid = true;
        for (int edge_index = 0; edge_index < static_cast<int>(matching.size());
             ++edge_index) {
            auto [i, j] = matching[edge_index];
            used_singleton[i] = used_singleton[j] = true;
            int auxiliary = singleton_upper[i].missing_bits |
                            singleton_upper[j].missing_bits;
            int a = singleton_upper[i].base_vertex;
            int b = singleton_upper[j].base_vertex;
            int x = static_cast<int>(lower.size()) + edge_index;
            vertex_value.push_back(auxiliary);
            for (auto [u, v] : {pair<int, int>{a, x}, {x, b}}) {
                if (u == v || degree[u] == 2 || degree[v] == 2 ||
                    connected(u, v, graph)) {
                    valid = false;
                    break;
                }
                graph[u].push_back(v);
                graph[v].push_back(u);
                ++degree[u];
                ++degree[v];
            }
            if (!valid) break;
        }
        if (!valid) continue;
        vector<pair<int, int>> chosen(constraints.size());
        if (!choose_forest(0, constraints, graph, degree, chosen)) continue;
        selected_matching = matching;
        vector<char> matched(singleton_upper.size(), false);
        for (auto [i, j] : matching) matched[i] = matched[j] = true;
        for (int i = 0; i < static_cast<int>(singleton_upper.size()); ++i)
            if (!matched[i]) literal_upper.push_back(singleton_upper[i].mask);
        solved = true;
        break;
    }
    if (!solved) {
        cerr << "no simultaneous augmented linear forest exists\n";
        return 4;
    }

    vector<int> vertex_order = linearize_forest(graph);
    if (vertex_order.size() != graph.size()) {
        cerr << "selected graph did not linearize all lower targets\n";
        return 4;
    }
    vector<int> completion;
    completion.reserve(vertex_value.size() + literal_upper.size());
    for (int vertex : vertex_order) completion.push_back(vertex_value[vertex]);
    completion.insert(completion.end(), literal_upper.begin(), literal_upper.end());

    for (const auto& constraint : constraints) {
        bool found = false;
        for (int i = 0; i + 1 < static_cast<int>(vertex_order.size()); ++i)
            if ((completion[i] | completion[i + 1]) == constraint.mask) {
                found = true;
                break;
            }
        if (!found) {
            cerr << "lost selected upper target " << constraint.mask << '\n';
            return 4;
        }
    }

    vector<int> completed = partial;
    completed.insert(completed.end(), completion.begin(), completion.end());
    const vector<char> completed_seen = covered_masks(completed, limit);
    int covered = 0;
    for (int mask = 1; mask < limit; ++mask) covered += completed_seen[mask];
    if (covered != limit - 1) {
        cerr << "completed word covers only " << covered << '/' << limit - 1
             << '\n';
        return 5;
    }

    write_word(argv[4], completion);
    write_word(argv[5], completed);
    for (auto [i, j] : selected_matching) {
        int auxiliary = singleton_upper[i].missing_bits |
                        singleton_upper[j].missing_bits;
        cout << "shared_auxiliary=" << auxiliary
             << " upper_a=" << singleton_upper[i].mask
             << " base_a=" << lower[singleton_upper[i].base_vertex]
             << " upper_b=" << singleton_upper[j].mask
             << " base_b=" << lower[singleton_upper[j].base_vertex] << '\n';
    }
    cout << "partial_length=" << partial.size()
         << " missing_lower=" << lower.size()
         << " missing_upper=" << upper.size()
         << " paired_upper=" << constraints.size()
         << " shared_auxiliary_pairs=" << selected_matching.size()
         << " literal_upper=" << literal_upper.size()
         << " completion_length=" << completion.size()
         << " completed_length=" << completed.size()
         << " covered=" << covered << '/' << limit - 1 << '\n';
    return 0;
}
