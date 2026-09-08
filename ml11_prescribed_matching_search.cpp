#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <algorithm>
#include <array>
#include <bit>
#include <chrono>
#include <fstream>
#include <functional>
#include <iostream>
#include <limits>
#include <numeric>
#include <queue>
#include <random>
#include <set>
#include <string>
#include <vector>

using namespace std;

static int wt(int x) { return popcount(static_cast<unsigned>(x)); }

struct MatchingInstance {
    static constexpr int side = 462;
    vector<int> lower, upper;
    vector<int> lower_index, upper_index;
    vector<array<int, 6>> neighbor;
    vector<int> forced_left, forced_right;

    explicit MatchingInstance(const vector<int>& path, int parity)
        : lower_index(1 << 11, -1), upper_index(1 << 11, -1),
          forced_left(side, -1), forced_right(side, -1) {
        for (int x = 0; x < (1 << 11); ++x) {
            if (wt(x) == 5) {
                lower_index[x] = lower.size();
                lower.push_back(x);
            } else if (wt(x) == 6) {
                upper_index[x] = upper.size();
                upper.push_back(x);
            }
        }
        neighbor.resize(side);
        for (int l = 0; l < side; ++l) {
            int at = 0;
            for (int bit = 0; bit < 11; ++bit)
                if (!(lower[l] & (1 << bit)))
                    neighbor[l][at++] = upper_index[lower[l] | (1 << bit)];
            if (at != 6) throw runtime_error("bad degree");
        }
        for (int i = parity; i + 1 < static_cast<int>(path.size()); i += 2) {
            int a = path[i], b = path[i + 1];
            if (wt(a) > wt(b)) swap(a, b);
            const int l = lower_index[a], u = upper_index[b];
            if (l < 0 || u < 0 || (a & b) != a || wt(a ^ b) != 1 ||
                (forced_left[l] >= 0 && forced_left[l] != u) ||
                (forced_right[u] >= 0 && forced_right[u] != l))
                throw runtime_error("invalid forced matching");
            forced_left[l] = u;
            forced_right[u] = l;
        }
    }
};

static bool random_matching(const MatchingInstance& graph,
                            const vector<int>& forbidden,
                            mt19937_64& rng,
                            vector<int>& match_left) {
    constexpr int n = MatchingInstance::side;
    match_left.assign(n, -1);
    vector<int> match_right(n, -1), fixed_left(n), fixed_right(n);
    for (int l = 0; l < n; ++l) if (graph.forced_left[l] >= 0) {
        const int u = graph.forced_left[l];
        if ((!forbidden.empty() && forbidden[l] == u) || match_right[u] >= 0)
            return false;
        match_left[l] = u;
        match_right[u] = l;
        fixed_left[l] = fixed_right[u] = 1;
    }
    vector<int> order(n);
    iota(order.begin(), order.end(), 0);
    shuffle(order.begin(), order.end(), rng);
    vector<int> seen(n), left_seen(n);
    int stamp = 0;
    function<bool(int)> augment = [&](int l) {
        if (left_seen[l] == stamp) return false;
        left_seen[l] = stamp;
        array<int, 6> adjacency = graph.neighbor[l];
        shuffle(adjacency.begin(), adjacency.end(), rng);
        for (int u : adjacency) {
            if ((!forbidden.empty() && forbidden[l] == u) ||
                seen[u] == stamp || fixed_right[u])
                continue;
            seen[u] = stamp;
            const int old = match_right[u];
            if (old < 0 || (!fixed_left[old] && augment(old))) {
                match_left[l] = u;
                match_right[u] = l;
                return true;
            }
        }
        return false;
    };
    for (int l : order) if (match_left[l] < 0) {
        ++stamp;
        if (!augment(l)) return false;
    }
    return true;
}

static vector<vector<int>> cycle_components(const vector<int>& first,
                                             const vector<int>& second) {
    constexpr int n = MatchingInstance::side;
    vector<int> right_first(n), right_second(n);
    for (int l = 0; l < n; ++l) {
        right_first[first[l]] = l;
        right_second[second[l]] = l;
    }
    vector<int> seen(n);
    vector<vector<int>> result;
    for (int start = 0; start < n; ++start) if (!seen[start]) {
        result.push_back({});
        int l = start;
        do {
            seen[l] = 1;
            result.back().push_back(l);
            l = right_second[first[l]];
        } while (l != start);
    }
    return result;
}

static vector<int> make_cycle(const MatchingInstance& graph,
                              const vector<int>& first,
                              const vector<int>& second) {
    constexpr int n = MatchingInstance::side;
    vector<int> right_second(n);
    for (int l = 0; l < n; ++l) right_second[second[l]] = l;
    vector<int> result;
    result.reserve(2 * n);
    int l = 0;
    for (int step = 0; step < n; ++step) {
        result.push_back(graph.lower[l]);
        result.push_back(graph.upper[first[l]]);
        l = right_second[first[l]];
    }
    return result;
}

static void emit_cycle(const vector<int>& cycle) {
    for (int i = 0; i < static_cast<int>(cycle.size()); ++i) {
        if (i) cout << ' ';
        cout << cycle[i];
    }
    cout << '\n';
}

static pair<int, int> mixed_run_score(const vector<int>& cycle,
                                      const vector<int>& path,
                                      int short_count) {
    const int n = cycle.size();
    vector<int> row;
    for (int start = 0; start < n; ++start) {
        if (cycle[start] != path.front()) continue;
        for (int direction : {-1, 1}) {
            bool prescribed = true;
            for (int j = 0; j < static_cast<int>(path.size()); ++j)
                if (cycle[(start + direction * j + n * path.size()) % n] !=
                    path[j]) {
                    prescribed = false;
                    break;
                }
            if (!prescribed) continue;
            int at = start;
            while (row.size() < MatchingInstance::side) {
                if (wt(cycle[at]) == 6) row.push_back(cycle[at]);
                at = (at + direction + n) % n;
            }
        }
    }
    if (row.size() != MatchingInstance::side)
        return {numeric_limits<int>::max(), numeric_limits<int>::max()};
    int deficit = 0, violations = 0;
    for (int bit = 0; bit < 11; ++bit) {
        int at = 0;
        while (at < static_cast<int>(row.size())) {
            if (!(row[at] & (1 << bit))) {
                ++at;
                continue;
            }
            const int first = at;
            while (at < static_cast<int>(row.size()) &&
                   (row[at] & (1 << bit)))
                ++at;
            if (!first || at == static_cast<int>(row.size())) continue;
            const int required = first <= short_count ? 3 : 4;
            const int length = at - first;
            if (length < required) {
                deficit += required - length;
                ++violations;
            }
        }
    }
    return {deficit, violations};
}

int main(int argc, char** argv) {
    if (argc < 2 || argc > 5) {
        cerr << "usage: ml11_prescribed_matching_search PATH [TRIALS] [SEED]"
                " [SHORT_COUNT]\n";
        return 2;
    }
    ifstream input(argv[1]);
    if (!input) return 2;
    vector<int> path;
    for (;;) {
        int x;
        if (input >> x) {
            path.push_back(x);
            continue;
        }
        if (input.eof()) break;
        return 2;
    }
    if (path.size() != 37 || set<int>(path.begin(), path.end()).size() != 37)
        return 2;
    const long long trials = argc >= 3 ? stoll(argv[2]) : 100000;
    const uint64_t seed = argc >= 4 ? stoull(argv[3]) : 1;
    const int short_count = argc >= 5 ? stoi(argv[4]) : -1;
    if (short_count > MatchingInstance::side || short_count == 0 ||
        short_count < -1)
        return 2;
    MatchingInstance first_graph(path, 0), second_graph(path, 1);
    mt19937_64 rng(seed);
    vector<int> first, second;
    int best = MatchingInstance::side;
    pair<int, int> best_score{numeric_limits<int>::max(),
                              numeric_limits<int>::max()};
    vector<int> best_cycle;
    const auto started = chrono::steady_clock::now();
    for (long long trial = 1; trial <= trials; ++trial) {
        if (!random_matching(first_graph, {}, rng, first)) continue;
        if (!random_matching(second_graph, first, rng, second)) continue;
        const auto components = cycle_components(first, second);
        if (static_cast<int>(components.size()) < best) {
            best = components.size();
            cerr << "trial=" << trial << " cycles=" << best;
            for (const auto& cycle : components) cerr << ' ' << 2 * cycle.size();
            cerr << '\n';
        }
        if (components.size() == 1) {
            vector<int> cycle = make_cycle(first_graph, first, second);
            if (short_count < 0) {
                emit_cycle(cycle);
                const double seconds = chrono::duration<double>(
                    chrono::steady_clock::now() - started).count();
                cerr << "SAT trial=" << trial << " seconds=" << seconds << '\n';
                return 0;
            }
            const auto value = mixed_run_score(cycle, path, short_count);
            if (value < best_score) {
                best_score = value;
                best_cycle = move(cycle);
                cerr << "score trial=" << trial
                     << " deficit=" << value.first
                     << " violations=" << value.second << '\n';
            }
        }
    }
    const double seconds = chrono::duration<double>(
        chrono::steady_clock::now() - started).count();
    if (!best_cycle.empty()) {
        emit_cycle(best_cycle);
        cerr << "BEST trials=" << trials << " deficit=" << best_score.first
             << " violations=" << best_score.second
             << " seconds=" << seconds << '\n';
        return best_score.first == 0 ? 0 : 1;
    }
    cerr << "NO CERTIFICATE trials=" << trials << " best_cycles=" << best
         << " seconds=" << seconds << '\n';
    return 1;
}
