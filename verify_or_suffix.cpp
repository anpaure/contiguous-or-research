#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(int argc, char** argv) {
    if (argc != 3) {
        cerr << "usage: verify_or_suffix k array.txt\n";
        return 2;
    }
    const int k = stoi(argv[1]);
    const int limit = 1 << k;
    ifstream input(argv[2]);
    if (!input) return 2;
    vector<char> seen(limit, false);
    vector<int> previous, current;
    int length = 0;
    for (int x; input >> x;) {
        if (x < 0 || x >= limit) return 3;
        ++length;
        current.clear();
        current.push_back(x);
        for (int old : previous) current.push_back(old | x);
        sort(current.begin(), current.end());
        current.erase(unique(current.begin(), current.end()), current.end());
        for (int value : current) seen[value] = true;
        previous.swap(current);
    }
    int covered = 0;
    vector<int> missing;
    for (int mask = 1; mask < limit; ++mask) {
        covered += seen[mask];
        if (!seen[mask]) missing.push_back(mask);
    }
    cout << "length=" << length << " covered=" << covered << '/'
         << limit - 1 << " missing=" << missing.size() << '\n';
    if (missing.size() <= 64) {
        cout << "missing:";
        for (int mask : missing) cout << ' ' << mask;
        cout << '\n';
    }
    return missing.empty() ? 0 : 1;
}
