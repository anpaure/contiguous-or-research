#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <algorithm>
#include <bit>
#include <iostream>
#include <set>
#include <vector>

using namespace std;

struct Eval {
    int deficit;
    int covered;
};

static bool adjacent(int x, int y) {
    return popcount(static_cast<unsigned>(x ^ y)) == 2;
}

static Eval evaluate(const vector<int>& path, int k, int rank, int d) {
    int deficit = 0;
    for (int bit = 0; bit < k; ++bit) {
        int i = 0;
        while (i < static_cast<int>(path.size())) {
            if (!(path[i] & (1 << bit))) { ++i; continue; }
            const int first = i;
            while (i < static_cast<int>(path.size()) && (path[i] & (1 << bit))) ++i;
            if (first && i < static_cast<int>(path.size()))
                deficit += max(0, d + 1 - (i - first));
        }
    }
    vector<uint8_t> seen(1 << k);
    int covered = 0;
    auto record = [&] (int value, int wanted) {
        if (popcount(static_cast<unsigned>(value)) == wanted && !seen[value]) {
            seen[value] = 1;
            ++covered;
        }
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
    return {deficit, covered};
}

int main(int argc, char** argv) {
    if (argc != 4) return 2;
    const int k = stoi(argv[1]);
    const int rank = stoi(argv[2]);
    const int d = stoi(argv[3]);
    vector<int> path;
    for (int value; cin >> value;) path.push_back(value);
    const Eval original = evaluate(path, k, rank, d);
    Eval best = original;
    vector<int> best_path = path;
    int valid = 0, preserving = 0, improving = 0;
    for (int left = 0; left < static_cast<int>(path.size()); ++left) {
        for (int right = left + 2; right < static_cast<int>(path.size()); ++right) {
            if (left && !adjacent(path[left - 1], path[right])) continue;
            if (right + 1 < static_cast<int>(path.size()) &&
                !adjacent(path[left], path[right + 1])) continue;
            ++valid;
            reverse(path.begin() + left, path.begin() + right + 1);
            const Eval next = evaluate(path, k, rank, d);
            preserving += next.deficit == 0;
            improving += next.deficit == 0 && next.covered > original.covered;
            if (next.deficit < best.deficit ||
                (next.deficit == best.deficit && next.covered > best.covered)) {
                best = next;
                best_path = path;
            }
            reverse(path.begin() + left, path.begin() + right + 1);
        }
    }
    cerr << "original=" << original.deficit << ',' << original.covered
         << " best=" << best.deficit << ',' << best.covered
         << " valid=" << valid << " preserving=" << preserving
         << " improving=" << improving << '\n';
    for (int value : best_path) cout << value << ' ';
    cout << '\n';
}
