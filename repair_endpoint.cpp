#include <algorithm>
#include <bit>
#include <iostream>
#include <vector>
using namespace std;

static int K, D, MIN_COLORS;

static bool valid(const vector<int>& path) {
    vector<uint8_t> colors(1 << K);
    int distinct = 0;
    for (int i = 0; i + 1 < static_cast<int>(path.size()); ++i) {
        if (popcount(static_cast<unsigned>(path[i] ^ path[i + 1])) != 2) return false;
        const int color = path[i] & path[i + 1];
        if (!colors[color]) colors[color] = 1, ++distinct;
    }
    if (distinct < MIN_COLORS) return false;
    for (int bit = 0; bit < K; ++bit) {
        int i = 0;
        while (i < static_cast<int>(path.size())) {
            if (!(path[i] & (1 << bit))) { ++i; continue; }
            const int first = i;
            while (i < static_cast<int>(path.size()) && (path[i] & (1 << bit))) ++i;
            if (first && i < static_cast<int>(path.size()) && i - first < D + 1)
                return false;
        }
    }
    return true;
}

int main(int argc, char** argv) {
    if (argc != 5) return 2;
    K = stoi(argv[1]); D = stoi(argv[2]); MIN_COLORS = stoi(argv[3]);
    const int target = stoi(argv[4]);
    vector<int> path;
    for (int value; cin >> value;) path.push_back(value);
    if (!valid(path)) return 3;
    const int n = path.size();
    for (int position = 0; position < n; ++position) {
        if (target & ~path[position]) continue;
        for (int length = 1; length <= 16; ++length) {
            for (int left = max(0, position - length + 1);
                 left <= position && left + length <= n; ++left) {
                const int right = left + length;
                vector<int> block(path.begin() + left, path.begin() + right);
                vector<int> reduced;
                reduced.insert(reduced.end(), path.begin(), path.begin() + left);
                reduced.insert(reduced.end(), path.begin() + right, path.end());
                for (int reverse_flag = 0; reverse_flag < 2; ++reverse_flag) {
                    if (reverse_flag) reverse(block.begin(), block.end());
                    for (int at_end = 0; at_end < 2; ++at_end) {
                        vector<int> candidate = reduced;
                        const int gap = at_end ? candidate.size() : 0;
                        candidate.insert(candidate.begin() + gap, block.begin(), block.end());
                        if ((target & ~(at_end ? candidate.back() : candidate.front())) ||
                            !valid(candidate)) continue;
                        cerr << "FOUND position=" << position << " block=[" << left
                             << ',' << right - 1 << "] reverse=" << reverse_flag
                             << " end=" << at_end << '\n';
                        for (int value : candidate) cout << value << ' ';
                        cout << '\n';
                        return 0;
                    }
                    if (reverse_flag) reverse(block.begin(), block.end());
                }
            }
        }
    }
    cerr << "NONE\n";
    return 1;
}
