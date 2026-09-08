#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;

static long long choose(int n, int r) {
    if (r < 0 || r > n) return 0;
    r = min(r, n - r);
    long long x = 1;
    for (int i = 1; i <= r; ++i) x = x * (n - r + i) / i;
    return x;
}

int main(int argc, char** argv) {
    if (argc != 3) return 2;
    const int k = stoi(argv[1]), rank = stoi(argv[2]);
    vector<int> path;
    for (int x; cin >> x;) path.push_back(x);
    vector<uint8_t> seen(1 << k);
    vector<pair<int, int>> previous, current;
    for (int x : path) {
        current.clear();
        current.push_back({x, 1});
        for (auto [value, length] : previous) {
            value |= x;
            if (value == current.back().first) continue;
            current.push_back({value, length + 1});
        }
        for (auto [value, length] : current) seen[value] = 1;
        previous.swap(current);
    }
    for (int r = rank; r <= k; ++r) {
        int covered = 0;
        vector<int> missing;
        for (int x = 1; x < (1 << k); ++x)
            if (__builtin_popcount(static_cast<unsigned>(x)) == r) {
                covered += seen[x];
                if (!seen[x] && missing.size() < 20) missing.push_back(x);
            }
        cout << "rank=" << r << " covered=" << covered << '/' << choose(k, r)
             << " first_missing";
        for (int x : missing) cout << ' ' << x;
        cout << '\n';
    }
}
