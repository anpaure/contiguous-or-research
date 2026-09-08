#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char** argv) {
    if (argc != 3) return 2;
    const int k = stoi(argv[1]);
    const int d = stoi(argv[2]);
    vector<int> central;
    for (int value; cin >> value;) central.push_back(value);
    if (central.empty()) return 2;
    const int n = central.size() + d;
    for (int position = 0; position < n; ++position) {
        int value = (1 << k) - 1;
        for (int i = max(0, position - d);
             i <= min(static_cast<int>(central.size()) - 1, position); ++i)
            value &= central[i];
        cout << value << (position + 1 == n ? '\n' : ' ');
    }
}
