#include <algorithm>
#include <bit>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <set>
#include <vector>

using Mask = std::uint64_t;

static int flaw_count(Mask x, int n) {
    int height = 0;
    int flaws = 0;
    for (int i = 0; i < n; ++i) {
        if ((x >> i) & 1ULL) {
            ++height;
        } else {
            --height;
            if (height < 0) ++flaws;
        }
    }
    return flaws;
}

// Mütze--Standke--Wiechert's maps g and h.  A 1-bit is an up-step.
static Mask g_map(Mask x, int n) {
    int height = 0;
    int d0 = 0;
    for (int i = 0; i < n; ++i) {
        if ((x >> i) & 1ULL) {
            ++height;
        } else {
            if (height == 0) ++d0;
            --height;
        }
    }

    height = 0;
    int touching = 0;
    for (int i = 0; i < n; ++i) {
        if ((x >> i) & 1ULL) {
            ++height;
        } else {
            const int next = height - 1;
            if (height == 0 || next == 0) {
                ++touching;
                if (touching == d0 + 1) return x | (Mask{1} << i);
            }
            height = next;
        }
    }
    assert(false);
    return 0;
}

static Mask h_map(Mask x, int n) {
    int height = 0;
    int u1 = 0;
    for (int i = 0; i < n; ++i) {
        if ((x >> i) & 1ULL) {
            if (height == 1) ++u1;
            ++height;
        } else {
            --height;
        }
    }

    height = 0;
    int touching = 0;
    for (int i = 0; i < n; ++i) {
        if ((x >> i) & 1ULL) {
            const int next = height + 1;
            if (height == 1 || next == 1) {
                ++touching;
                if (touching == u1) return x & ~(Mask{1} << i);
            }
            height = next;
        } else {
            --height;
        }
    }
    assert(false);
    return 0;
}

static Mask f_map(Mask x, int n) { return h_map(g_map(x, n), n); }

static std::uint64_t choose(int n, int k) {
    if (k < 0 || k > n) return 0;
    k = std::min(k, n - k);
    std::uint64_t ans = 1;
    for (int i = 1; i <= k; ++i) ans = ans * (n - k + i) / i;
    return ans;
}

int main(int argc, char** argv) {
    const int m_max = argc > 1 ? std::stoi(argv[1]) : 9;
    for (int m = 1; m <= m_max; ++m) {
        const int n = 2 * m;
        std::vector<std::set<Mask>> lower(m + 1), upper(m + 1);
        std::vector<std::set<Mask>> wreath(2 * m + 2);
        std::vector<std::uint64_t> windows(m + 1, 0);
        std::uint64_t roots = 0;

        for (Mask x = 0; x < (Mask{1} << n); ++x) {
            if (std::popcount(x) != m || flaw_count(x, n) != 0) continue;
            ++roots;
            std::vector<Mask> col(m + 1);
            std::vector<int> omitted;
            col[0] = x;
            for (int e = 0; e < m; ++e) {
                col[e + 1] = f_map(col[e], n);
                const Mask arrived = col[e + 1] & ~col[e];
                const Mask departed = col[e] & ~col[e + 1];
                assert(std::popcount(arrived) == 1);
                assert(std::popcount(departed) == 1);
                omitted.push_back(std::countr_zero(arrived));
                omitted.push_back(std::countr_zero(departed));
                assert(flaw_count(col[e + 1], n) == e + 1);
            }
            assert(col[m] == (((Mask{1} << n) - 1) ^ x));

            // The omitted-edge labels, followed by the new coordinate n,
            // determine the literal wreath order by taking step +2.
            omitted.push_back(n);
            const int odd_n = n + 1;
            std::vector<int> order(odd_n);
            for (int j = 0; j < odd_n; ++j) order[j] = omitted[(2 * j) % odd_n];
            for (int len = 0; len <= odd_n; ++len) {
                for (int start = 0; start < odd_n; ++start) {
                    Mask z = 0;
                    for (int j = 0; j < len; ++j) z |= Mask{1} << order[(start + j) % odd_n];
                    wreath[len].insert(z);
                }
            }

            for (int q = 0; q <= m; ++q) {
                for (int e = 0; e + q <= m; ++e) {
                    Mask lo = (Mask{1} << n) - 1;
                    Mask hi = 0;
                    for (int j = 0; j <= q; ++j) {
                        lo &= col[e + j];
                        hi |= col[e + j];
                    }
                    assert(std::popcount(lo) == m - q);
                    assert(std::popcount(hi) == m + q);
                    lower[q].insert(lo);
                    upper[q].insert(hi);
                    ++windows[q];
                }
            }
        }

        std::cout << "m=" << m << " roots=" << roots;
        bool ok = true;
        for (int q = 0; q <= m; ++q) {
            const auto want = choose(n, m - q);
            const bool here = lower[q].size() == want && upper[q].size() == want;
            ok &= here;
            std::cout << " q" << q << "=" << lower[q].size() << "/"
                      << upper[q].size() << "/" << want
                      << "[" << windows[q] << "]";
        }
        std::cout << " " << (ok ? "COMPLETE" : "MISSING") << '\n';
        bool wreath_ok = true;
        std::cout << "  wreath:";
        for (int r = 0; r <= n + 1; ++r) {
            const auto want = choose(n + 1, r);
            wreath_ok &= wreath[r].size() == want;
            std::cout << " r" << r << "=" << wreath[r].size() << "/" << want;
        }
        std::cout << " " << (wreath_ok ? "COMPLETE" : "MISSING") << '\n';
        if (m == 4) {
            const int r = m - 1;
            std::cout << "  missing wreath rank " << r << ':';
            for (Mask s = 0; s < (Mask{1} << (n + 1)); ++s) {
                if (std::popcount(s) == r && !wreath[r].contains(s)) {
                    std::cout << ' ';
                    for (int i = 0; i <= n; ++i) if ((s >> i) & 1ULL) std::cout << i + 1 << ',';
                }
            }
            std::cout << '\n';
        }
        if (m <= 5 && lower[1].size() != choose(n, m - 1)) {
            std::cout << "  missing lower q=1:";
            for (Mask s = 0; s < (Mask{1} << n); ++s) {
                if (std::popcount(s) == m - 1 && !lower[1].contains(s)) {
                    std::cout << ' ';
                    for (int i = 0; i < n; ++i) if ((s >> i) & 1ULL) std::cout << i + 1 << ',';
                }
            }
            std::cout << '\n';
        }
    }
}
