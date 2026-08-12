#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <algorithm>
#include <bit>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;

struct Eval {
    int deficit = 0;
    int covered = 0;
    vector<int> ranks;
};

static Eval evaluate(const vector<int>& path, int k, int rank, int d) {
    Eval result;
    result.ranks.assign(k + 1, 0);
    for (int bit = 0; bit < k; ++bit) {
        int i = 0;
        while (i < static_cast<int>(path.size())) {
            if (!(path[i] & (1 << bit))) { ++i; continue; }
            const int first = i;
            while (i < static_cast<int>(path.size()) && (path[i] & (1 << bit))) ++i;
            if (first && i < static_cast<int>(path.size()))
                result.deficit += max(0, d + 1 - (i - first));
        }
    }
    vector<uint8_t> seen(1 << k);
    auto record = [&] (int value, int wanted) {
        if (popcount(static_cast<unsigned>(value)) != wanted || seen[value]) return;
        seen[value] = 1;
        ++result.covered;
        ++result.ranks[wanted];
    };
    for (int value : path) record(value, rank);
    for (int length = 2; length <= d + 1; ++length) {
        for (int left = 0; left + length <= static_cast<int>(path.size()); ++left) {
            int value = (1 << k) - 1;
            for (int j = left; j < left + length; ++j) value &= path[j];
            record(value, rank - length + 1);
        }
    }
    for (int length = 2; rank + length - 1 <= k; ++length) {
        for (int left = 0; left + length <= static_cast<int>(path.size()); ++left) {
            int value = 0;
            for (int j = left; j < left + length; ++j) value |= path[j];
            record(value, rank + length - 1);
        }
    }
    return result;
}

int main(int argc, char** argv) {
    const int k = argc > 1 ? stoi(argv[1]) : 11;
    const int lower = argc > 2 ? stoi(argv[2]) : k / 2;
    const int d = argc > 3 ? stoi(argv[3]) : 3;
    const int forced_omitted = argc > 4 ? stoi(argv[4]) : -1;
    vector<int> cycle;
    for (int value; cin >> value;) cycle.push_back(value);
    if (cycle.empty()) return 2;
    for (int i = 0; i < static_cast<int>(cycle.size()); ++i)
        if (popcount(static_cast<unsigned>(cycle[i] ^
                cycle[(i + 1) % cycle.size()])) != 1) return 3;
    Eval best;
    best.deficit = 1e9;
    int best_omitted = -1;
    vector<int> best_path;
    for (int omitted = 0; omitted < static_cast<int>(cycle.size()); ++omitted) {
        if (popcount(static_cast<unsigned>(cycle[omitted])) != lower) continue;
        if (forced_omitted >= 0 && cycle[omitted] != forced_omitted) continue;
        vector<int> path;
        for (int step = 1; step < static_cast<int>(cycle.size()); ++step) {
            const int value = cycle[(omitted + step) % cycle.size()];
            if (popcount(static_cast<unsigned>(value)) == lower + 1)
                path.push_back(value);
        }
        Eval current = evaluate(path, k, lower + 1, d);
        if (current.deficit < best.deficit ||
            (current.deficit == best.deficit && current.covered > best.covered)) {
            best = current;
            best_omitted = cycle[omitted];
            best_path = move(path);
        }
    }
    if (best_path.empty()) return 4;
    cerr << "omitted=" << best_omitted << " deficit=" << best.deficit
         << " covered=" << best.covered << " ranks";
    for (int r = 0; r <= k; ++r) if (best.ranks[r])
        cerr << ' ' << r << ':' << best.ranks[r];
    cerr << '\n';
    for (int value : best_path) cout << value << ' ';
    cout << '\n';
}
