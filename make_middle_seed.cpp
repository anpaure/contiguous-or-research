#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <bit>
#include <iostream>
#include <unordered_set>
#include <vector>

using namespace std;

int main(int argc, char** argv) {
    if (argc < 2) return 2;
    const int k = stoi(argv[1]);
    vector<int> a;
    for (int value; cin >> value;) a.push_back(value);
    const int middle = (k + 1) / 2;
    vector<int> q, p;
    unordered_set<int> seen_q, seen_p;
    for (int i = 0; i + 2 < static_cast<int>(a.size()); ++i) {
        const int value = a[i] | a[i + 1] | a[i + 2];
        if (popcount(static_cast<unsigned>(value)) == middle && seen_q.insert(value).second)
            q.push_back(value);
    }
    for (int i = 0; i + 1 < static_cast<int>(a.size()); ++i) {
        const int value = a[i] | a[i + 1];
        if (popcount(static_cast<unsigned>(value)) == middle - 1 &&
            seen_p.insert(value).second) p.push_back(value);
    }
    cerr << "triple_middle=" << q.size() << " pair_lower=" << p.size() << '\n';
    for (int value : q) cout << value << ' ';
    const int high = 1 << k;
    for (int value : p) cout << (high | value) << ' ';
    cout << '\n';
}
