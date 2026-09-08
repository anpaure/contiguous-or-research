#include <algorithm>
#include <bit>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

static string bits(int x, int k) {
    string s;
    for (int b = 0; b < k; ++b) if (x & (1 << b)) s += char('1' + b);
    return s.empty() ? "0" : s;
}

int main(int argc, char** argv) {
    if (argc < 3) return 2;
    const int k = stoi(argv[1]);
    vector<int> a;
    for (int i = 2; i < argc; ++i) a.push_back(stoi(argv[i]));
    vector<char> seen(1 << k);
    vector<int> previous;
    int total = 0;
    for (int j = 0; j < static_cast<int>(a.size()); ++j) {
        vector<int> current{a[j]};
        for (int x : previous) {
            x |= a[j];
            if (x != current.back()) current.push_back(x);
        }
        cout << j + 1 << " A=" << bits(a[j], k) << " chain:";
        for (int x : current) cout << ' ' << bits(x, k);
        cout << " new:";
        for (int x : current) if (!seen[x]) {
            seen[x] = 1;
            ++total;
            cout << ' ' << bits(x, k);
        }
        cout << " total=" << total << '\n';
        previous.swap(current);
    }
    cout << "missing:";
    for (int x = 1; x < (1 << k); ++x) if (!seen[x]) cout << ' ' << bits(x, k);
    cout << '\n';
}
