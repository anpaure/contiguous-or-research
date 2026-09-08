#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <vector>

using namespace std;

static int pc(uint32_t x) { return __builtin_popcount(x); }

static bool dyck(uint32_t x, int m) {
    int h = 0;
    for (int i = 0; i < 2 * m; ++i) {
        h += (x >> i & 1U) ? 1 : -1;
        if (h < 0) return false;
    }
    return h == 0;
}

static uint32_t g(uint32_t x, int m) {
    vector<int> before(2 * m);
    int h = 0, d0 = 0;
    for (int i = 0; i < 2 * m; ++i) {
        before[i] = h;
        if (!(x >> i & 1U) && h == 0) ++d0;
        h += (x >> i & 1U) ? 1 : -1;
    }
    int ord = 0;
    for (int i = 0; i < 2 * m; ++i) {
        if (!(x >> i & 1U) && (before[i] == 0 || before[i] == 1) &&
            ++ord == d0 + 1)
            return x | (1U << i);
    }
    assert(false);
    return 0;
}

static uint32_t hmap(uint32_t y, int m) {
    vector<int> before(2 * m);
    int h = 0, u1 = 0;
    for (int i = 0; i < 2 * m; ++i) {
        before[i] = h;
        if ((y >> i & 1U) && h == 1) ++u1;
        h += (y >> i & 1U) ? 1 : -1;
    }
    int ord = 0;
    for (int i = 0; i < 2 * m; ++i) {
        if ((y >> i & 1U) && (before[i] == 0 || before[i] == 1) &&
            ++ord == u1)
            return y & ~(1U << i);
    }
    assert(false);
    return 0;
}

static long long binom(int n, int k) {
    if (k < 0 || k > n) return 0;
    long long z = 1;
    for (int i = 1; i <= k; ++i) z = z * (n - k + i) / i;
    return z;
}

int main(int argc, char **argv) {
    const int max_m = argc > 1 ? stoi(argv[1]) : 10;
    for (int m = 2; m <= max_m; ++m) {
        const uint32_t lim = 1U << (2 * m);
        map<uint32_t, int> mult;
        long long slots = 0, columns = 0;
        for (uint32_t x0 = 0; x0 < lim; ++x0) {
            if (pc(x0) != m || !dyck(x0, m)) continue;
            ++columns;
            vector<uint32_t> ys;
            uint32_t x = x0;
            for (int i = 0; i < m; ++i) {
                uint32_t y = g(x, m);
                ys.push_back(y);
                x = hmap(y, m);
            }
            for (int i = 1; i < m; ++i) {
                ++mult[ys[i - 1] | ys[i]];
                ++slots;
            }
        }
        long long target = binom(2 * m, m + 2), missing = 0, repeated = 0;
        vector<uint32_t> first_missing;
        map<int, long long> hist;
        for (uint32_t z = 0; z < lim; ++z) {
            if (pc(z) != m + 2) continue;
            int c = mult[z];
            ++hist[c];
            if (!c) {
                ++missing;
                if (first_missing.size() < 6) first_missing.push_back(z);
            }
            if (c > 1) repeated += c - 1;
        }
        cout << "m=" << m << " C=" << columns << " slots=" << slots
             << " target=" << target << " missing=" << missing
             << " repeated_excess=" << repeated << " hist=";
        for (auto [c, n] : hist) cout << c << ':' << n << ',';
        cout << " first_missing=";
        for (uint32_t z : first_missing) {
            cout << '{';
            for (int i = 0; i < 2 * m; ++i)
                if (z >> i & 1U) cout << i + 1 << ',';
            cout << "},";
        }
        cout << '\n';
    }
}
