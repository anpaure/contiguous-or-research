#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <algorithm>
#include <cstdint>
#include <iostream>
#include <limits>
using namespace std;

static long long choose(int n, int r) {
    if (r < 0 || r > n) return 0;
    r = min(r, n - r);
    long long value = 1;
    for (int i = 1; i <= r; ++i) value = value * (n - r + i) / i;
    return value;
}
static long long width(int n) { return choose(n, n / 2); }

static long long complement_bridge(int p, int q) {
    const long long cp1 = width(p - 1), cq = width(q);
    return cq * ((1LL << (p - 1)) + 2 * cp1 - 2) +
           cp1 * ((1LL << q) + cq - 2) + (q & 1);
}

static long long antipodal_even(int s, int t) {
    const long long p = width(s), q = width(t);
    const long long delta = min(((1LL << s) + p - 2) / p,
                                ((1LL << t) + q - 2) / q);
    return (1LL << (s - 1)) * q + (1LL << (t - 1)) * p +
           min(p * q - p - q, p + q - 2) + delta;
}

int main() {
    long long lifted = 1;
    for (int k = 1; k < 20; ++k) {
        if (k <= 10) {
            static const long long exact[] =
                {0,1,2,4,7,12,21,37,72,128,254};
            lifted = exact[k];
        } else lifted *= 2;
        long long bridge = numeric_limits<long long>::max();
        int bridge_p = -1;
        for (int p = 1; p < k; ++p) {
            const long long value = complement_bridge(p, k - p);
            if (value < bridge) bridge = value, bridge_p = p;
        }
        long long antipodal = numeric_limits<long long>::max();
        int antipodal_s = -1;
        if (!(k & 1)) {
            for (int s = 2; s <= k - 2; s += 2) {
                const long long value = antipodal_even(s, k - s);
                if (value < antipodal) antipodal = value, antipodal_s = s;
            }
        } else if (k >= 5) {
            for (int s = 2; s <= k - 3; s += 2) {
                const long long value = 2 * antipodal_even(s, k - 1 - s);
                if (value < antipodal) antipodal = value, antipodal_s = s;
            }
        }
        cout << "k=" << k << " lift=" << lifted
             << " bridge=" << bridge << "(" << bridge_p << '+' << k-bridge_p << ')';
        if (antipodal != numeric_limits<long long>::max())
            cout << " antipodal=" << antipodal << '(' << antipodal_s << '+'
                 << (k - (k&1) - antipodal_s) << "+lift" << (k&1) << ')';
        cout << '\n';
    }
}
