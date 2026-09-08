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
    const int k = stoi(argv[1]), target = stoi(argv[2]);
    const int limit = 1 << k;
    vector<int> path;
    for (int value; cin >> value;) path.push_back(value);
    vector<vector<int>> edge_positions(limit);
    for (int i = 0; i + 1 < static_cast<int>(path.size()); ++i)
        edge_positions[path[i] & path[i + 1]].push_back(i);

    cout << "target=" << target << " rank="
         << popcount(static_cast<unsigned>(target)) << '\n';
    for (int bit = 0; bit < k; ++bit) if (!(target & (1 << bit))) {
        const int color = target | (1 << bit);
        cout << "super bit=" << bit << " color=" << color
             << " multiplicity=" << edge_positions[color].size();
        for (int edge : edge_positions[color])
            cout << " e" << edge << "=(" << path[edge] << ',' << path[edge + 1]
                 << ") upper=" << (path[edge] | path[edge + 1]);
        cout << '\n';
    }

    cout << "vertices_containing_target\n";
    for (int i = 0; i < static_cast<int>(path.size()); ++i)
        if ((path[i] & target) == target) {
            cout << "  i=" << i << " v=" << path[i];
            if (i) cout << " lc=" << (path[i - 1] & path[i]);
            if (i + 1 < static_cast<int>(path.size()))
                cout << " rc=" << (path[i] & path[i + 1]);
            if (i && i + 1 < static_cast<int>(path.size()))
                cout << " triple=" << (path[i - 1] & path[i] & path[i + 1]);
            cout << '\n';
        }
}
