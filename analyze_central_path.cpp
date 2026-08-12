#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <algorithm>
#include <bit>
#include <iostream>
#include <map>
#include <vector>

using namespace std;

int main(int argc, char** argv) {
    if (argc != 4) return 2;
    const int k = stoi(argv[1]);
    const int rank = stoi(argv[2]);
    const int d = stoi(argv[3]);
    const int limit = 1 << k;
    vector<int> path;
    for (int value; cin >> value;) path.push_back(value);
    vector<int> witness_count(limit);
    vector<vector<pair<int, int>>> witnesses(limit);

    auto add = [&] (int value, int wanted_rank, int left, int length) {
        if (popcount(static_cast<unsigned>(value)) != wanted_rank) return;
        ++witness_count[value];
        witnesses[value].push_back({left, length});
    };
    for (int i = 0; i < static_cast<int>(path.size()); ++i)
        add(path[i], rank, i, 1);
    for (int length = 2; length <= d + 1; ++length) {
        const int wanted_rank = rank - length + 1;
        for (int left = 0; left + length <= static_cast<int>(path.size()); ++left) {
            int value = limit - 1;
            for (int j = left; j < left + length; ++j) value &= path[j];
            add(value, wanted_rank, left, length);
        }
    }
    for (int length = 2; rank + length - 1 <= k; ++length) {
        const int wanted_rank = rank + length - 1;
        for (int left = 0; left + length <= static_cast<int>(path.size()); ++left) {
            int value = 0;
            for (int j = left; j < left + length; ++j) value |= path[j];
            add(value, wanted_rank, left, length);
        }
    }

    int total_missing = 0;
    for (int r = rank - d; r <= k; ++r) {
        vector<int> missing;
        map<int, int> multiplicities;
        for (int mask = 1; mask < limit; ++mask) {
            if (popcount(static_cast<unsigned>(mask)) != r) continue;
            if (!witness_count[mask]) missing.push_back(mask);
            else ++multiplicities[witness_count[mask]];
        }
        total_missing += missing.size();
        cout << "rank " << r << " missing=" << missing.size() << " values";
        for (int mask : missing) cout << ' ' << mask;
        cout << " multiplicities";
        for (auto [count, masks] : multiplicities) cout << ' ' << count << ':' << masks;
        cout << '\n';
    }

    vector<int> fragile(path.size());
    for (int mask = 1; mask < limit; ++mask) {
        if (witness_count[mask] != 1) continue;
        for (auto [left, length] : witnesses[mask])
            for (int i = left; i < left + length; ++i) ++fragile[i];
    }
    vector<int> positions(path.size());
    for (int i = 0; i < static_cast<int>(positions.size()); ++i) positions[i] = i;
    sort(positions.begin(), positions.end(), [&] (int x, int y) {
        return fragile[x] < fragile[y];
    });
    cout << "total_missing=" << total_missing << " least_fragile";
    for (int i = 0; i < min(30, static_cast<int>(positions.size())); ++i)
        cout << ' ' << positions[i] << ':' << fragile[positions[i]];
    cout << '\n';
}
