#include <algorithm>
#include <cstdint>
#include <iostream>
#include <limits>
#include <string>
#include <tuple>
#include <vector>

using namespace std;
using i128 = __int128_t;

static long long choose(int n, int r) {
    if (r < 0 || r > n) return 0;
    r = min(r, n - r);
    long long value = 1;
    for (int i = 1; i <= r; ++i) value = value * (n - r + i) / i;
    return value;
}

static long long delay(int k, int rank) {
    const long long M = choose(k, rank);
    long long L = 0;
    for (int s = 1; s < rank; ++s) L += choose(k, s);
    long long lo = 0, hi = 1;
    while (hi * M + hi * (hi + 1) / 2 < L) hi *= 2;
    while (lo < hi) {
        const long long mid = (lo + hi) / 2;
        if (mid * M + mid * (mid + 1) / 2 >= L)
            hi = mid;
        else
            lo = mid + 1;
    }
    return lo;
}

static long long bound(int k) {
    if (!k) return 0;
    long long result = 0;
    for (int r = 1; r <= k; ++r)
        result = max(result, choose(k, r) + delay(k, r));
    return result;
}

static string print128(i128 value) {
    if (!value) return "0";
    const bool negative = value < 0;
    if (negative) value = -value;
    string out;
    while (value) {
        out.push_back('0' + value % 10);
        value /= 10;
    }
    if (negative) out.push_back('-');
    reverse(out.begin(), out.end());
    return out;
}

int main(int argc, char** argv) {
    const int maximum = argc == 2 ? stoi(argv[1]) : 19;
    vector<long long> B(maximum + 1);
    for (int k = 0; k <= maximum; ++k) B[k] = bound(k);
    int violations = 0;
    for (int k = 1; k <= maximum; ++k) {
        const long long n = B[k];
        for (int rank = 1; rank <= k; ++rank) {
            const long long M = choose(k, rank);
            const long long d = n - M;
            if (choose(k, rank) + delay(k, rank) != n || d <= 0) continue;
            long long L = 0;
            for (int s = 1; s < rank; ++s) L += choose(k, s);
            const long long sigma = d * M + d * (d + 1) / 2 - L;
            const long long E = (d - 1) * (2 * n - d);
            i128 minimum_margin = 0;
            bool have_margin = false;
            int worst_q = -1;
            long long worst_h = -1;
            for (int q = 1; q < k; ++q) {
                long long projected = 0;
                for (int s = 1; s < rank; ++s)
                    projected += choose(k - q, s);
                const long long a = choose(k - rank + 1, q);
                const long long b = choose(k - rank + 1, q - 1);

                // The objective is linear while E-2 sigma-2h is positive
                // and linear after it reaches zero, so endpoints and the
                // one breakpoint suffice.
                vector<long long> candidates{0, sigma};
                const long long crossing = (E - 2 * sigma) / 2;
                for (long long h = crossing - 2; h <= crossing + 2; ++h)
                    if (0 <= h && h <= sigma) candidates.push_back(h);
                i128 best_extra4 = -1;
                long long best_h = -1;
                for (long long h : candidates) {
                    const long long edges = max(0LL, E - 2 * sigma - 2 * h);
                    const i128 extra4 = static_cast<i128>(4) * h * a
                        + static_cast<i128>(d) * edges * b;
                    if (best_extra4 < 0 || extra4 < best_extra4)
                        best_extra4 = extra4, best_h = h;
                }
                const i128 lhs4 = static_cast<i128>(4) * d * choose(k, q)
                    * (n - B[q]);
                const i128 rhs4 = static_cast<i128>(4) * choose(k, q)
                    * projected + best_extra4;
                const i128 margin = lhs4 - rhs4;
                if (!have_margin || margin < minimum_margin) {
                    minimum_margin = margin;
                    worst_q = q;
                    worst_h = best_h;
                    have_margin = true;
                }
                if (margin < 0) {
                    ++violations;
                    cout << "VIOLATION k=" << k << " rank=" << rank
                         << " q=" << q << " h=" << best_h
                         << " margin4=" << print128(margin) << '\n';
                }
            }
            cout << "k=" << k << " rank=" << rank << " B=" << n
                 << " d=" << d << " sigma=" << sigma << " E=" << E
                 << " worst_q=" << worst_q << " worst_h=" << worst_h
                 << " minimum_margin4=" << print128(minimum_margin) << '\n';
        }
    }
    cout << "checked_through=" << maximum << " violations=" << violations
         << '\n';
    return violations ? 1 : 0;
}
