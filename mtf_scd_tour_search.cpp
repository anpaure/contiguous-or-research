#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#endif

#include <algorithm>
#include <bit>
#include <cstdint>
#include <iostream>
#include <unordered_set>
#include <vector>

using namespace std;
using State = vector<uint16_t>;

static int k, full, width;
static vector<State> path_states;
static vector<vector<int>> path_chains;
static vector<int> path_updates;
static uint64_t all_sets;

static State mtf(const State &p, int x) {
    State q{(uint16_t)x};
    for (int b : p) {
        b &= ~x;
        if (b) q.push_back((uint16_t)b);
    }
    return q;
}

static vector<vector<int>> exposed_symmetric_chains(const State &p) {
    vector<int> at_rank(k + 1, -1);
    at_rank[0] = 0;
    int s = 0;
    for (int b : p) {
        s |= b;
        at_rank[popcount((unsigned)s)] = s;
    }
    vector<vector<int>> ans;
    for (int r = 0; r <= k / 2; ++r) {
        vector<int> c;
        bool ok = true;
        for (int q = r; q <= k - r; ++q) {
            if (at_rank[q] < 0) { ok = false; break; }
            c.push_back(at_rank[q]);
        }
        if (ok) ans.push_back(move(c));
    }
    return ans;
}

static uint64_t chain_bits(const vector<int> &c) {
    uint64_t z = 0;
    for (int s : c) z |= 1ULL << s;
    return z;
}

static string key(const State &p, uint64_t used, int depth) {
    string s;
    s.resize(2 * p.size() + 16);
    int at = 0;
    for (uint16_t x : p) {
        s[at++] = char(x & 255);
        s[at++] = char(x >> 8);
    }
    for (int i = 0; i < 8; ++i) s[at++] = char(used >> (8 * i));
    s[at++] = char(depth);
    s.resize(at);
    return s;
}

static unordered_set<string> dead;

static bool dfs(const State &state, uint64_t used, int depth) {
    if (depth == width) return used == all_sets;
    string memo = key(state, used, depth);
    if (dead.count(memo)) return false;

    vector<pair<int, State>> nexts;
    for (int x = 1; x <= full; ++x) nexts.push_back({x, mtf(state, x)});
    sort(nexts.begin(), nexts.end(), [](auto &a, auto &b) {
        return a.second.size() > b.second.size();
    });
    nexts.erase(unique(nexts.begin(), nexts.end(), [](auto &a, auto &b) {
        return a.second == b.second;
    }), nexts.end());

    for (auto &[x, q] : nexts) {
        auto cs = exposed_symmetric_chains(q);
        sort(cs.begin(), cs.end(), [](auto &a, auto &b) { return a.size() > b.size(); });
        for (auto &c : cs) {
            uint64_t cb = chain_bits(c);
            if (cb & used) continue;
            path_updates.push_back(x);
            path_states.push_back(q);
            path_chains.push_back(c);
            if (dfs(q, used | cb, depth + 1)) return true;
            path_chains.pop_back();
            path_states.pop_back();
            path_updates.pop_back();
        }
    }
    dead.insert(move(memo));
    return false;
}

int main(int argc, char **argv) {
    k = argc > 1 ? stoi(argv[1]) : 4;
    if (k > 6) return 2;
    full = (1 << k) - 1;
    width = 1;
    for (int i = 1; i <= k / 2; ++i) width = width * (k - i + 1) / i;
    all_sets = k == 6 ? ~0ULL : (1ULL << (1 << k)) - 1;

    State first;
    for (int i = 0; i < k; ++i) first.push_back(1u << i);
    vector<int> first_chain;
    int s = 0;
    first_chain.push_back(0);
    for (int b : first) { s |= b; first_chain.push_back(s); }
    path_states = {first};
    path_chains = {first_chain};
    uint64_t used = chain_bits(first_chain);
    if (!dfs(first, used, 1)) {
        cout << "NO TOUR FOUND\n";
        return 1;
    }
    cout << "k=" << k << " states=" << path_states.size() << "\n";
    for (int i = 0; i < width; ++i) {
        cout << i + 1 << " P=";
        for (int x : path_states[i]) cout << x << ',';
        cout << " C=";
        for (int x : path_chains[i]) cout << x << ',';
        if (i + 1 < width) cout << " nextX=" << path_updates[i];
        cout << '\n';
    }
}
