#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <algorithm>
#include <bit>
#include <iostream>
#include <vector>
using namespace std;

int main(int argc, char** argv) {
    if (argc != 3) return 2;
    const int k = stoi(argv[1]), rank = stoi(argv[2]);
    const int full = (1 << k) - 1;
    vector<int> path;
    for (int value; cin >> value;) path.push_back(value);
    if (path.size() < 2) return 2;

    vector<int> lower;
    vector<uint8_t> seen(1 << k);
    for (int i = 0; i + 1 < static_cast<int>(path.size()); ++i) {
        if (popcount(static_cast<unsigned>(path[i] ^ path[i + 1])) != 2)
            return 3;
        const int value = path[i] & path[i + 1];
        if (popcount(static_cast<unsigned>(value)) != rank - 1 || seen[value])
            return 4;
        seen[value] = 1;
        lower.push_back(value);
    }
    vector<int> missing;
    for (int mask = 0; mask <= full; ++mask)
        if (popcount(static_cast<unsigned>(mask)) == rank - 1 && !seen[mask])
            missing.push_back(mask);
    if (missing.size() != 1) return 5;
    const int omitted = missing.front();
    if (!(omitted & ~path.front())) lower.insert(lower.begin(), omitted);
    else if (!(omitted & ~path.back())) lower.push_back(omitted);
    else return 6;

    for (int& value : lower) value ^= full;
    for (int i = 0; i + 1 < static_cast<int>(lower.size()); ++i)
        if (popcount(static_cast<unsigned>(lower[i] ^ lower[i + 1])) != 2)
            return 7;
    cerr << "omitted=" << omitted << " length=" << lower.size() << '\n';
    for (int value : lower) cout << value << ' ';
    cout << '\n';
}
