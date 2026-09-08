#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <algorithm>
#include <array>
#include <bit>
#include <iostream>
#include <map>
#include <vector>
using namespace std;

int main(int argc, char** argv) {
    if (argc != 2) return 2;
    const int k = stoi(argv[1]);
    const int full = (1 << k) - 1;
    vector<int> masks;
    for (int value; cin >> value;) masks.push_back(value);
    if (masks.empty()) return 3;
    int common = full, united = 0;
    map<int, int> ranks;
    vector<int> frequency(k);
    for (int mask : masks) {
        common &= mask; united |= mask;
        ++ranks[popcount(static_cast<unsigned>(mask))];
        for (int bit = 0; bit < k; ++bit) frequency[bit] += !!(mask & (1 << bit));
    }
    cout << "count=" << masks.size() << " common=" << common << " union=" << united
         << " ranks";
    for (auto [rank, count] : ranks) cout << ' ' << rank << ':' << count;
    cout << "\nbit_frequency";
    for (int bit = 0; bit < k; ++bit) cout << ' ' << bit << ':' << frequency[bit];
    cout << '\n';
    vector<int> minimal, maximal;
    for (int mask : masks) {
        bool has_smaller = false, has_larger = false;
        for (int other : masks) if (other != mask) {
            has_smaller |= (other & ~mask) == 0;
            has_larger |= (mask & ~other) == 0;
        }
        if (!has_smaller) minimal.push_back(mask);
        if (!has_larger) maximal.push_back(mask);
    }
    cout << "minimal"; for (int mask : minimal) cout << ' ' << mask; cout << '\n';
    cout << "maximal"; for (int mask : maximal) cout << ' ' << mask; cout << '\n';
    sort(masks.begin(), masks.end(), [](int a, int b) {
        const int ra = popcount(static_cast<unsigned>(a));
        const int rb = popcount(static_cast<unsigned>(b));
        return ra != rb ? ra < rb : a < b;
    });
    for (int mask : masks) {
        cout << mask << " rank=" << popcount(static_cast<unsigned>(mask)) << " bits=";
        bool first = true;
        for (int bit = 0; bit < k; ++bit) if (mask & (1 << bit)) {
            if (!first) cout << ',';
            cout << bit; first = false;
        }
        cout << '\n';
    }
}
