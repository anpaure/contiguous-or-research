#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#endif

#include <algorithm>
#include <bit>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <set>
#include <string>
#include <vector>

using namespace std;

using State = vector<int>;
using Chain = vector<int>;

static State mtf(State p, int x) {
    State q{x};
    for (int b : p) {
        b &= ~x;
        if (b) q.push_back(b);
    }
    return q;
}

static vector<int> prefixes(const State &p) {
    vector<int> out;
    int x = 0;
    for (int b : p) {
        x |= b;
        out.push_back(x);
    }
    return out;
}

static bool valid_state(const State &p, int k) {
    int u = 0;
    for (int b : p) {
        if (!b || (u & b)) return false;
        u |= b;
    }
    return u == (1 << k) - 1;
}

static bool verify_tour(int k, const vector<State> &states,
                        const vector<Chain> &chains,
                        const vector<int> &updates, bool cyclic) {
    if (states.size() != chains.size()) return false;
    if (updates.size() != states.size() - 1 + int(cyclic)) return false;
    const int full = (1 << k) - 1;
    vector<int> owner(1 << k, -1);
    for (int i = 0; i < (int)states.size(); ++i) {
        if (!valid_state(states[i], k)) return false;
        auto pref = prefixes(states[i]);
        for (int j = 0; j < (int)chains[i].size(); ++j) {
            int s = chains[i][j];
            if (s && find(pref.begin(), pref.end(), s) == pref.end()) return false;
            if (j && ((chains[i][j - 1] & ~s) ||
                      popcount((unsigned)(s ^ chains[i][j - 1])) != 1)) return false;
            if (owner[s] != -1) return false;
            owner[s] = i;
        }
        if (!chains[i].empty()) {
            int lo = popcount((unsigned)chains[i].front());
            int hi = popcount((unsigned)chains[i].back());
            if (lo + hi != k) return false;
        }
    }
    if (find(owner.begin(), owner.end(), -1) != owner.end()) return false;
    for (int i = 0; i + 1 < (int)states.size(); ++i)
        if (mtf(states[i], updates[i]) != states[i + 1]) return false;
    if (cyclic && mtf(states.back(), updates.back()) != states.front()) return false;
    return true;
}

static bool verify_word(int k, const vector<int> &a) {
    vector<char> seen(1 << k);
    vector<int> old, now;
    for (int x : a) {
        now = {x};
        for (int y : old) {
            int z = x | y;
            if (z != now.back()) now.push_back(z);
        }
        for (int z : now) seen[z] = true;
        old.swap(now);
    }
    return all_of(seen.begin() + 1, seen.end(), [](char x) { return x; });
}

int main() {
    const vector<State> k3_states = {
        {1, 2, 4}, {4, 1, 2}, {2, 4, 1},
    };
    const vector<Chain> k3_chains = {
        {0, 1, 3, 7}, {4, 5}, {2, 6},
    };
    const vector<int> k3_updates = {4, 2, 1};
    assert(verify_tour(3, k3_states, k3_chains, k3_updates, true));

    const vector<State> k4_states = {
        {1, 2, 4, 8},
        {8, 1, 2, 4},
        {4, 8, 1, 2},
        {2, 4, 8, 1},
        {8, 2, 4, 1},
        {5, 8, 2},
    };
    const vector<Chain> k4_chains = {
        {0, 1, 3, 7, 15},
        {8, 9, 11},
        {4, 12, 13},
        {2, 6, 14},
        {10},
        {5},
    };
    const vector<int> k4_updates = {8, 4, 2, 8, 5};
    assert(verify_tour(4, k4_states, k4_chains, k4_updates, false));

    const vector<State> k5_states = {
        {4, 2, 1, 16, 8},
        {8, 4, 2, 1, 16},
        {16, 8, 4, 2, 1},
        {1, 16, 8, 4, 2},
        {2, 1, 16, 8, 4},
        {8, 2, 1, 16, 4},
        {18, 8, 1, 4},
        {20, 2, 8, 1},
        {5, 16, 2, 8},
        {9, 4, 16, 2},
    };
    const vector<Chain> k5_chains = {
        {0, 4, 6, 7, 23, 31},
        {8, 12, 14, 15},
        {16, 24, 28, 30},
        {1, 17, 25, 29},
        {2, 3, 19, 27},
        {10, 11},
        {18, 26},
        {20, 22},
        {5, 21},
        {9, 13},
    };
    const vector<int> k5_updates = {8, 16, 1, 2, 8, 18, 20, 5, 9};
    assert(verify_tour(5, k5_states, k5_chains, k5_updates, false));

    vector<int> word;
    for (auto it = k5_states[0].rbegin(); it != k5_states[0].rend(); ++it)
        word.push_back(*it);
    word.insert(word.end(), k5_updates.begin(), k5_updates.end());
    assert(word == vector<int>({8, 16, 1, 2, 4, 8, 16, 1, 2, 8, 18, 20, 5, 9}));
    assert(verify_word(5, word));

    cout << "k=3 cyclic MTF-SCD certificate: PASS\n";
    cout << "k=4 MTF-SCD path certificate: PASS\n";
    cout << "k=5 MTF-SCD path certificate: PASS\n";
    cout << "k=5 induced OR word length 14: PASS\n";
}
