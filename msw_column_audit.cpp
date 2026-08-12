#include <algorithm>
#include <bit>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <vector>

using U64 = std::uint64_t;

static int start_height(U64 x, int pos) {
    int h = 0;
    for (int i = 0; i < pos; ++i) h += ((x >> i) & 1U) ? 1 : -1;
    return h;
}

static bool is_dyck(U64 x, int n) {
    int h = 0;
    for (int i = 0; i < n; ++i) {
        h += ((x >> i) & 1U) ? 1 : -1;
        if (h < 0) return false;
    }
    return h == 0;
}

// MSW's g: flip the (d_0(x)+1)-st down-step touching height 0.
static U64 g(U64 x, int n) {
    int d0 = 0;
    for (int i = 0; i < n; ++i)
        if (((x >> i) & 1U) == 0 && start_height(x, i) == 0) ++d0;

    int seen = 0;
    for (int i = 0; i < n; ++i) {
        if ((x >> i) & 1U) continue;
        const int h = start_height(x, i);
        if (h == 0 || h == 1) {
            if (++seen == d0 + 1) return x | (U64{1} << i);
        }
    }
    assert(false);
    return 0;
}

// MSW's h: flip the u_1(y)-th up-step touching height 1.
static U64 hmap(U64 y, int n) {
    int u1 = 0;
    for (int i = 0; i < n; ++i)
        if (((y >> i) & 1U) != 0 && start_height(y, i) == 1) ++u1;

    int seen = 0;
    for (int i = 0; i < n; ++i) {
        if (((y >> i) & 1U) == 0) continue;
        const int h = start_height(y, i);
        if (h == 0 || h == 1) {
            if (++seen == u1) return y & ~(U64{1} << i);
        }
    }
    assert(false);
    return 0;
}

static U64 f(U64 x, int n) { return hmap(g(x, n), n); }

int main(int argc, char** argv) {
    const int max_m = argc > 1 ? std::stoi(argv[1]) : 10;
    for (int m = 1; m <= max_m; ++m) {
        const int n = 2 * m;
        const U64 lim = U64{1} << n;
        std::vector<std::vector<unsigned char>> lower(m + 1,
            std::vector<unsigned char>(lim));
        std::vector<std::vector<unsigned char>> upper(m + 1,
            std::vector<unsigned char>(lim));
        std::uint64_t columns = 0;

        for (U64 x0 = 0; x0 < lim; ++x0) {
            if (std::popcount(x0) != m || !is_dyck(x0, n)) continue;
            ++columns;
            std::vector<U64> x(m + 1);
            x[0] = x0;
            for (int i = 0; i < m; ++i) x[i + 1] = f(x[i], n);
            assert(x[m] == ((lim - 1) ^ x[0]));

            for (int q = 0; q <= m; ++q) {
                for (int i = 0; i + q <= m; ++i) {
                    U64 lo = lim - 1, hi = 0;
                    for (int j = i; j <= i + q; ++j) {
                        lo &= x[j];
                        hi |= x[j];
                    }
                    assert(std::popcount(lo) == m - q);
                    assert(std::popcount(hi) == m + q);
                    lower[q][lo] = 1;
                    upper[q][hi] = 1;
                }
            }
        }

        bool all_ok = true;
        std::cout << "m=" << m << " columns=" << columns;
        for (int q = 0; q <= m; ++q) {
            std::uint64_t got_lo = 0, got_hi = 0, need = 0;
            for (U64 x = 0; x < lim; ++x) {
                got_lo += lower[q][x];
                got_hi += upper[q][x];
                need += std::popcount(x) == m - q;
            }
            const bool ok = got_lo == need && got_hi == need;
            all_ok &= ok;
            std::cout << " q" << q << "=" << got_lo << "/" << need
                      << "," << got_hi << "/" << need;
        }
        std::cout << " all=" << (all_ok ? "yes" : "no") << '\n';
    }
}
