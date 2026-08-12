#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <unordered_map>
#include <vector>

using namespace std;

static int popcount(uint32_t x) { return __builtin_popcount(x); }

static bool is_dyck(uint32_t x, int m) {
    int h = 0;
    for (int i = 0; i < 2 * m; ++i) {
        h += ((x >> i) & 1U) ? 1 : -1;
        if (h < 0) return false;
    }
    return h == 0;
}

// Mütze--Standke--Wiechert's g: flip the (d_0(x)+1)-st down-step
// touching height 0, where d_0 counts down-steps starting at height 0.
static pair<uint32_t, int> apply_g(uint32_t x, int m) {
    vector<int> before(2 * m);
    int h = 0, d0 = 0;
    for (int i = 0; i < 2 * m; ++i) {
        before[i] = h;
        if (((x >> i) & 1U) == 0 && h == 0) ++d0;
        h += ((x >> i) & 1U) ? 1 : -1;
    }
    int ordinal = 0;
    for (int i = 0; i < 2 * m; ++i) {
        if (((x >> i) & 1U) == 0 && (before[i] == 0 || before[i] == 1)) {
            if (++ordinal == d0 + 1) return {x | (1U << i), i};
        }
    }
    assert(false);
    return {};
}

// MSW's h: flip the u_1(y)-th up-step touching height 1, where u_1
// counts up-steps starting at height 1.
static pair<uint32_t, int> apply_h(uint32_t y, int m) {
    vector<int> before(2 * m);
    int h = 0, u1 = 0;
    for (int i = 0; i < 2 * m; ++i) {
        before[i] = h;
        if (((y >> i) & 1U) && h == 1) ++u1;
        h += ((y >> i) & 1U) ? 1 : -1;
    }
    int ordinal = 0;
    for (int i = 0; i < 2 * m; ++i) {
        if (((y >> i) & 1U) && (before[i] == 0 || before[i] == 1)) {
            if (++ordinal == u1) return {y & ~(1U << i), i};
        }
    }
    assert(false);
    return {};
}

static long long binom(int n, int k) {
    if (k < 0 || k > n) return 0;
    long long z = 1;
    for (int i = 1; i <= k; ++i) z = z * (n - k + i) / i;
    return z;
}

int main(int argc, char** argv) {
    int max_m = argc > 1 ? stoi(argv[1]) : 9;
    bool all_depths = false, details = false;
    for (int i = 2; i < argc; ++i) {
        all_depths |= string(argv[i]) == "--all-depths";
        details |= string(argv[i]) == "--details";
    }
    for (int m = 1; m <= max_m; ++m) {
        const int n = 2 * m + 1;
        const uint32_t full_old = (1U << (2 * m)) - 1;
        map<uint32_t, int> middle_mult, lower_mult;
        vector<unordered_map<uint32_t, int>> depth_mult;
        if (all_depths) depth_mult.resize(m + 1);
        int cycles = 0;

        for (uint32_t x0 = 0; x0 <= full_old; ++x0) {
            if (popcount(x0) != m || !is_dyck(x0, m)) continue;
            ++cycles;
            uint32_t x = x0;
            vector<int> omitted;
            omitted.reserve(n);
            for (int e = 0; e < m; ++e) {
                auto [y, a] = apply_g(x, m);
                auto [next, b] = apply_h(y, m);
                omitted.push_back(a);
                omitted.push_back(b);
                x = next;
            }
            assert(x == (full_old ^ x0));
            omitted.push_back(2 * m);
            vector<int> sorted = omitted;
            sort(sorted.begin(), sorted.end());
            for (int i = 0; i < n; ++i) assert(sorted[i] == i);
            if (details && m == max_m) {
                cerr << "dyck=";
                for (int i = 0; i < 2*m; ++i) cerr << (((x0 >> i) & 1U) ? '1' : '0');
                cerr << " pi=";
                for (int i = 0; i < 2*m; ++i) cerr << omitted[i] + 1 << (i+1==2*m?'\n':',');
            }

            for (int i = 0; i < n; ++i) {
                uint32_t mid = 0, low = 0;
                for (int t = 0; t < m; ++t)
                    mid |= 1U << omitted[(i + 1 + 2 * t) % n];
                for (int t = 0; t < m - 1; ++t)
                    low |= 1U << omitted[(i + 1 + 2 * t) % n];
                ++middle_mult[mid];
                ++lower_mult[low];
                if (all_depths) {
                    for (int d = 0; d <= m; ++d) {
                        uint32_t value = 0;
                        for (int t = 0; t < m - d; ++t)
                            value |= 1U << omitted[(i + 1 + 2*t) % n];
                        ++depth_mult[d][value];
                    }
                }
            }
        }

        int missing_middle = 0, missing_lower = 0, max_lower_mult = 0;
        int missing_lower_without_z = 0, missing_lower_with_z = 0;
        map<int, int> histogram, histogram_without_z, histogram_with_z;
        for (uint32_t s = 0; s < (1U << n); ++s) {
            if (popcount(s) == m && !middle_mult.count(s)) ++missing_middle;
            if (popcount(s) == m - 1) {
                int z = lower_mult[s];
                if (!z) {
                    ++missing_lower;
                    if ((s >> (2*m)) & 1U) ++missing_lower_with_z;
                    else ++missing_lower_without_z;
                    if (details && m == max_m) {
                        cerr << "missing m=" << m << " set=";
                        for (int b = 0; b < n; ++b) if ((s >> b) & 1U) cerr << (b+1) << ',';
                        cerr << '\n';
                    }
                }
                max_lower_mult = max(max_lower_mult, z);
                ++histogram[z];
                if ((s >> (2*m)) & 1U) ++histogram_with_z[z];
                else ++histogram_without_z[z];
            }
        }
        cout << "m=" << m
             << " cycles=" << cycles << '/' << binom(2*m,m)/(m+1)
             << " middle_missing=" << missing_middle
             << " lower_missing=" << missing_lower << '/' << binom(n,m-1)
             << " (noz=" << missing_lower_without_z
             << ",z=" << missing_lower_with_z << ')'
             << " lower_max_mult=" << max_lower_mult << " hist=";
        for (auto [mult, count] : histogram) cout << mult << ':' << count << ',';
        cout << " noz_hist=";
        for (auto [mult, count] : histogram_without_z) cout << mult << ':' << count << ',';
        cout << " z_hist=";
        for (auto [mult, count] : histogram_with_z) cout << mult << ':' << count << ',';
        cout << '\n';
        if (all_depths) {
            for (int d = 0; d <= m; ++d) {
                long long target = binom(n, m-d);
                long long distinct = depth_mult[d].size();
                cout << "  depth=" << d << " rank=" << (m-d)
                     << " distinct=" << distinct << '/' << target
                     << " missing=" << (target-distinct) << '\n';
            }
        }
    }
}
