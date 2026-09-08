#include <algorithm>
#include <bit>
#include <iostream>
#include <vector>
using namespace std;

static int deficit(const vector<int>& path, int k, int d) {
    int result = 0;
    for (int bit = 0; bit < k; ++bit) {
        int i = 0;
        while (i < static_cast<int>(path.size())) {
            if (!(path[i] & (1 << bit))) { ++i; continue; }
            const int first = i;
            while (i < static_cast<int>(path.size()) && (path[i] & (1 << bit))) ++i;
            if (first && i < static_cast<int>(path.size()))
                result += max(0, d + 1 - (i - first));
        }
    }
    return result;
}

int main(int argc, char** argv) {
    if (argc != 3) return 2;
    const int k = stoi(argv[1]), d = stoi(argv[2]);
    vector<int> path;
    for (int value; cin >> value;) path.push_back(value);
    int best = deficit(path, k, d), best_shift = 0;
    const bool cyclic = popcount(static_cast<unsigned>(path.front() ^ path.back())) == 2;
    if (cyclic) {
        vector<int> candidate = path;
        for (int shift = 1; shift < static_cast<int>(path.size()); ++shift) {
            rotate(candidate.begin(), candidate.begin() + 1, candidate.end());
            const int value = deficit(candidate, k, d);
            if (value < best) best = value, best_shift = shift, path = candidate;
        }
    }
    cerr << "cyclic=" << cyclic << " best_deficit=" << best
         << " shift=" << best_shift << '\n';
    for (int value : path) cout << value << ' ';
    cout << '\n';
}
