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
    if (argc != 2) return 2;
    const int old_k = stoi(argv[1]);
    const int high = 1 << old_k;
    vector<int> a;
    for (int value; cin >> value;) a.push_back(value);
    if (a.size() < 3) return 2;
    vector<int> p(a.size() - 1), q(a.size() - 2);
    for (int i = 0; i + 1 < static_cast<int>(a.size()); ++i)
        p[i] = a[i] | a[i + 1];
    for (int i = 0; i + 1 < static_cast<int>(p.size()); ++i)
        q[i] = p[i] | p[i + 1];

    vector<int> result;
    int exceptions = 0;
    for (int i = 0; i < static_cast<int>(p.size()); ++i) {
        if (popcount(static_cast<unsigned>(p[i])) == old_k / 2) {
            result.push_back(high | p[i]);
        } else {
            ++exceptions;
        }
        if (i < static_cast<int>(q.size())) result.push_back(q[i]);
    }
    cerr << "P=" << p.size() << " Q=" << q.size()
         << " exceptions=" << exceptions << " result=" << result.size() << '\n';
    for (int value : result) cout << value << ' ';
    cout << '\n';
}
