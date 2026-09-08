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
    if (argc != 3 && argc != 4) return 2;
    const int k = stoi(argv[1]);
    const int rank = stoi(argv[2]);
    const bool lower_mode = argc == 3 || string(argv[3]) == "lower";
    if (k != 2 * rank - 1) return 2;
    const int limit = 1 << k;
    vector<int> path;
    for (int value; cin >> value;) path.push_back(value);
    vector<unsigned char> used(limit);
    for (int value : path)
        if (popcount(static_cast<unsigned>(value)) != rank || used[value]++) return 3;
    for (int i = 0; i + 1 < static_cast<int>(path.size()); ++i) {
        if (popcount(static_cast<unsigned>(path[i] ^ path[i + 1])) != 2) return 4;
        const int color = path[i] & path[i + 1];
        if (popcount(static_cast<unsigned>(color)) != rank - 1 || used[color]++) return 5;
    }
    int missing = -1;
    for (int mask = 0; mask < limit; ++mask)
        if (popcount(static_cast<unsigned>(mask)) == rank - 1 && !used[mask]) {
            if (missing >= 0) return 6;
            missing = mask;
        }
    if (missing < 0) return 6;
    if (lower_mode) {
        if ((missing & ~path.back()) != 0) {
            if ((missing & ~path.front()) != 0) return 7;
            reverse(path.begin(), path.end());
        }
    } else if ((missing & ~path.front()) != 0) {
        if ((missing & ~path.back()) != 0) return 7;
        reverse(path.begin(), path.end());
    }
    const int high = 1 << k;
    vector<int> colors;
    for (int i = 0; i + 1 < static_cast<int>(path.size()); ++i)
        colors.push_back(path[i] & path[i + 1]);
    reverse(colors.begin(), colors.end());
    if (lower_mode) colors.insert(colors.begin(), missing);
    else colors.push_back(missing);

    vector<int> result;
    result.reserve(2 * path.size());
    result.insert(result.end(), path.begin(), path.end());
    for (int color : colors) result.push_back(high | color);
    for (int i = 0; i + 1 < static_cast<int>(result.size()); ++i)
        if (popcount(static_cast<unsigned>(result[i] ^ result[i + 1])) != 2)
            return 8;
    cerr << "old=" << path.size() << " missing=" << missing
         << " new=" << result.size() << '\n';
    for (int value : result) cout << value << ' ';
    cout << '\n';
}
