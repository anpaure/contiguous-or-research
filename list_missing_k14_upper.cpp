#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <array>
#include <cstdint>
#include <iostream>
#include <vector>

using namespace std;

int main() {
    constexpr int k = 14;
    constexpr int limit = 1 << k;
    vector<int> path;
    for (int value; cin >> value;) path.push_back(value);

    array<uint8_t, limit> seen{};
    vector<int> previous, current;
    for (int value : path) {
        current.clear();
        current.push_back(value);
        for (int old : previous) {
            const int joined = old | value;
            if (joined != current.back()) current.push_back(joined);
        }
        for (int joined : current) seen[joined] = 1;
        previous.swap(current);
    }

    for (int rank = 11; rank >= 9; --rank)
        for (int mask = 1; mask < limit; ++mask)
            if (__builtin_popcount(static_cast<unsigned>(mask)) == rank && !seen[mask])
                cout << mask << '\n';
}
