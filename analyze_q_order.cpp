#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <bit>
#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char** argv) {
    if (argc < 2) return 2;
    const int k = stoi(argv[1]), middle = (k + 1) / 2;
    vector<int> q;
    for (int value; cin >> value;) q.push_back(value);
    int violations = 0;
    for (int bit = 0; bit < k; ++bit) {
        cout << "bit " << bit << " short-runs:";
        int start = 0;
        while (start < static_cast<int>(q.size())) {
            if (!(q[start] & (1 << bit))) { ++start; continue; }
            int end = start + 1;
            while (end < static_cast<int>(q.size()) && (q[end] & (1 << bit))) ++end;
            if (start > 0 && end < static_cast<int>(q.size()) && end - start < 3) {
                cout << " [" << start << ',' << end - 1 << "]";
                violations += 3 - (end - start);
            }
            start = end;
        }
        cout << '\n';
    }
    vector<unsigned char> seen(1 << k);
    for (int left = 0; left < static_cast<int>(q.size()); ++left) {
        int value = 0;
        for (int right = left; right < static_cast<int>(q.size()); ++right) {
            value |= q[right];
            if (__builtin_popcount(static_cast<unsigned>(value)) >= middle) seen[value] = 1;
            if (value == (1 << k) - 1) break;
        }
    }
    int covered = 0;
    cout << "missing high:";
    for (int mask = 1; mask < (1 << k); ++mask) {
        if (__builtin_popcount(static_cast<unsigned>(mask)) < middle) continue;
        if (seen[mask]) ++covered;
        else cout << ' ' << mask;
    }
    cout << "\ncovered=" << covered << " violations=" << violations << '\n';
}
