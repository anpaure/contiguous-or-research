#include <array>
#include <cstdint>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

static constexpr int M = 4;
static constexpr int N = 2 * M + 1;
static constexpr int NN = N + 2;
using OldOrder = array<int, N>;
using NewOrder = array<int, NN>;

static OldOrder ordinary(const OldOrder &q) {
    OldOrder c{};
    for (int i = 0; i < N; ++i) c[i] = q[(2 * i) % N];
    return c;
}

static NewOrder extend(const OldOrder &c, int a) {
    NewOrder out{};
    int at = 0;
    for (int i = 0; i < N; ++i) {
        out[at++] = c[i];
        if (i == a) out[at++] = 10;
        if (i == (a + M) % N) out[at++] = 11;
    }
    if (at != NN) __builtin_trap();
    return out;
}

static int interval_mask(const NewOrder &c, int start, int len) {
    int mask = 0;
    for (int j = 0; j < len; ++j) mask |= 1 << (c[(start + j) % NN] - 1);
    return mask;
}

static string signature(const array<OldOrder, 4> &side,
                        const array<int, 4> &pointing,
                        int low_rank = 4) {
    string s(1 << NN, '\0');
    for (int z = 0; z < 4; ++z) {
        NewOrder c = extend(side[z], pointing[z]);
        for (int i = 0; i < NN; ++i) {
            ++s[interval_mask(c, i, M + 1)];
            if (low_rank) ++s[interval_mask(c, i, low_rank)];
        }
    }
    return s;
}

static vector<int> shadow(const array<OldOrder, 4> &side,
                          const array<int, 4> &pointing, int rank) {
    vector<int> v(1 << NN);
    for (int z = 0; z < 4; ++z) {
        NewOrder c = extend(side[z], pointing[z]);
        for (int i = 0; i < NN; ++i) ++v[interval_mask(c, i, rank)];
    }
    return v;
}

static uint32_t code(const array<int, 4> &a) {
    uint32_t x = 0;
    for (int i = 3; i >= 0; --i) x = N * x + a[i];
    return x;
}

static array<int, 4> decode(uint32_t x) {
    array<int, 4> a{};
    for (int i = 0; i < 4; ++i) {
        a[i] = x % N;
        x /= N;
    }
    return a;
}

int main() {
    const array<OldOrder, 4> nq{{
        {1, 8, 6, 7, 4, 5, 3, 9, 2},
        {1, 9, 8, 6, 7, 4, 5, 2, 3},
        {1, 5, 3, 9, 8, 6, 7, 2, 4},
        {1, 7, 3, 9, 4, 5, 8, 2, 6},
    }};
    const array<OldOrder, 4> pq{{
        {1, 9, 3, 5, 4, 7, 6, 8, 2},
        {1, 5, 4, 7, 6, 8, 9, 2, 3},
        {1, 7, 6, 8, 9, 3, 5, 2, 4},
        {1, 8, 5, 4, 9, 3, 7, 2, 6},
    }};

    array<OldOrder, 4> neg{}, pos{};
    for (int i = 0; i < 4; ++i) {
        neg[i] = ordinary(nq[i]);
        pos[i] = ordinary(pq[i]);
    }

    unordered_multimap<string, uint32_t> table, top_table;
    table.reserve(7000);
    top_table.reserve(7000);
    for (uint32_t z = 0; z < N * N * N * N; ++z) {
        auto a = decode(z);
        table.emplace(signature(neg, a), z);
        top_table.emplace(signature(neg, a, 0), z);
    }

    uint64_t equal_top = 0, nonzero_deep = 0, equal_middle = 0;
    bool showed_middle = false;
    for (uint32_t z = 0; z < N * N * N * N; ++z) {
        auto b = decode(z);
        auto top_range = top_table.equal_range(signature(pos, b, 0));
        for (auto jt = top_range.first; jt != top_range.second; ++jt) {
            ++equal_middle;
            if (!showed_middle) {
                auto a = decode(jt->second);
                cerr << "first equal-middle pointings N:";
                for (int x : a) cerr << ' ' << x;
                cerr << " P:";
                for (int x : b) cerr << ' ' << x;
                cerr << '\n';
                showed_middle = true;
            }
        }
        string sig = signature(pos, b);
        auto [it, end] = table.equal_range(sig);
        for (; it != end; ++it) {
            ++equal_top;
            auto a = decode(it->second);
            auto bn = shadow(neg, a, M - 1);
            auto bp = shadow(pos, b, M - 1);
            if (bn == bp) continue;
            ++nonzero_deep;
            cout << "FOUND\nnegative pointings:";
            for (int x : a) cout << ' ' << x;
            cout << "\npositive pointings:";
            for (int x : b) cout << ' ' << x;
            cout << "\nrank3 effect:";
            for (int mask = 0; mask < (1 << NN); ++mask) {
                int d = bp[mask] - bn[mask];
                if (d) cout << ' ' << mask << ':' << d;
            }
            cout << "\n";
            return 0;
        }
    }
    cout << "equal_middle=" << equal_middle << " equal_top=" << equal_top
         << " nonzero_deep=" << nonzero_deep << "\n";
}
