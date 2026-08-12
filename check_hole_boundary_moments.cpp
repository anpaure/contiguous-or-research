#include <algorithm>
#include <cstdint>
#include <iostream>
#include <limits>
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
    const long long middle = choose(k, rank);
    long long lower = 0;
    for (int s = 1; s < rank; ++s) lower += choose(k, s);
    for (long long d = 0;; ++d)
        if (lower <= d * middle + d * (d + 1) / 2) return d;
}

static long long bound(int k) {
    if (!k) return 0;
    long long result = 0;
    for (int rank = 1; rank <= k; ++rank)
        result = max(result, choose(k, rank) + delay(k, rank));
    return result;
}

static string print128(i128 value) {
    if (!value) return "0";
    bool negative = value < 0;
    if (negative) value = -value;
    string result;
    while (value) {
        result.push_back('0' + value % 10);
        value /= 10;
    }
    if (negative) result.push_back('-');
    reverse(result.begin(), result.end());
    return result;
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
            const long long tau = delay(k, rank);
            if (M + tau != n) continue;
            const long long d = n - M;
            if (!d) continue;
            long long lower = 0;
            for (int s = 1; s < rank; ++s) lower += choose(k, s);
            const long long sigma = d * M + d * (d + 1) / 2 - lower;
            const long long band_edges = (d - 1) * (2 * n - d);
            const long long selected_edges = max(0LL, band_edges - 4 * sigma);
            i128 minimum_margin = numeric_limits<long long>::max();
            int worst_q = -1;
            for (int q = 1; q <= k; ++q) {
                long long projected_lower = 0;
                for (int s = 1; s < rank; ++s) projected_lower += choose(k - q, s);
                const i128 lhs4 = static_cast<i128>(4) * d * choose(k, q) * (n - B[q]);
                const i128 rhs4 = static_cast<i128>(4) * choose(k, q) * projected_lower
                    + static_cast<i128>(d) * selected_edges * choose(k - rank + 1, q - 1);
                const i128 margin = lhs4 - rhs4;
                if (q < k && margin < minimum_margin)
                    minimum_margin = margin, worst_q = q;
                if (margin < 0) {
                    ++violations;
                    cout << "VIOLATION k=" << k << " rank=" << rank << " q=" << q
                         << " B=" << n << " d=" << d << " sigma=" << sigma
                         << " margin4=" << print128(margin) << '\n';
                }
            }
            cout << "k=" << k << " rank=" << rank << " B=" << n << " d=" << d
                 << " sigma=" << sigma << " selected_edge_lb=" << selected_edges
                 << " worst_q=" << worst_q
                 << " minimum_margin4=" << print128(minimum_margin) << '\n';
        }
    }
    cout << "checked_through=" << maximum << " violations=" << violations << '\n';
    return violations ? 1 : 0;
}
