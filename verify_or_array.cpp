#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <algorithm>
#include <bit>
#include <iostream>
#include <limits>
#include <map>
#include <vector>

using namespace std;

int main(int argc, char** argv) {
    if (argc < 2) return 2;
    const int k = stoi(argv[1]);
    const int limit = 1 << k;
    vector<int> a;
    for (int value; cin >> value;) a.push_back(value);
    vector<int> shortest(limit, numeric_limits<int>::max());
    for (int left = 0; left < static_cast<int>(a.size()); ++left) {
        int value = 0;
        for (int right = left; right < static_cast<int>(a.size()); ++right) {
            value |= a[right];
            shortest[value] = min(shortest[value], right - left + 1);
        }
    }
    int covered = 0;
    vector<int> missing;
    vector<map<int, int>> distribution(k + 1);
    for (int mask = 1; mask < limit; ++mask) {
        if (shortest[mask] == numeric_limits<int>::max()) {
            missing.push_back(mask);
            continue;
        }
        ++covered;
        distribution[popcount(static_cast<unsigned>(mask))][shortest[mask]]++;
    }
    cout << "length=" << a.size() << " covered=" << covered
         << " required=" << limit - 1 << '\n';
    for (int rank = 1; rank <= k; ++rank) {
        cout << "rank " << rank << ':';
        for (auto [length, count] : distribution[rank])
            cout << " length" << length << '=' << count;
        cout << '\n';
    }
    if (missing.size() <= 64) {
        cout << "missing:";
        for (int mask : missing) cout << ' ' << mask;
        cout << '\n';
    }
    for (int length = 1; length <= min(k, static_cast<int>(a.size())); ++length) {
        vector<uint8_t> seen(limit);
        vector<int> by_rank(k + 1);
        for (int left = 0; left + length <= static_cast<int>(a.size()); ++left) {
            int value = 0;
            for (int position = left; position < left + length; ++position)
                value |= a[position];
            if (!seen[value]) {
                seen[value] = 1;
                ++by_rank[popcount(static_cast<unsigned>(value))];
            }
        }
        cout << "windows " << length << ':';
        for (int rank = 1; rank <= k; ++rank)
            if (by_rank[rank]) cout << " rank" << rank << '=' << by_rank[rank];
        cout << '\n';
    }
    return covered == limit - 1 ? 0 : 1;
}
