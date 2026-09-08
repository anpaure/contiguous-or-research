#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#endif

#include <bit>
#include <fstream>
#include <iostream>
#include <limits>
#include <string>
#include <vector>

using namespace std;

int main(int argc, char** argv) {
    if (argc != 5) {
        cerr << "usage: completion_witness_certificate k prefix_length "
                "array.txt targets.txt\n";
        return 2;
    }
    const int k = stoi(argv[1]);
    const int prefix_length = stoi(argv[2]);
    const int limit = 1 << k;
    vector<int> word, targets;
    {
        ifstream input(argv[3]);
        for (int x; input >> x;) word.push_back(x);
    }
    {
        ifstream input(argv[4]);
        for (string line; getline(input, line);) {
            if (line.empty()) continue;
            targets.push_back(stoi(line));
        }
    }
    for (int target : targets) {
        int best_left = -1, best_right = -1;
        int best_length = numeric_limits<int>::max();
        for (int left = 0; left < static_cast<int>(word.size()); ++left) {
            int value = 0;
            for (int right = left; right < static_cast<int>(word.size()); ++right) {
                value |= word[right];
                if (value == target && right - left + 1 < best_length) {
                    best_left = left;
                    best_right = right;
                    best_length = right - left + 1;
                }
                if (value & ~target) break;
            }
        }
        if (best_left < 0) {
            cerr << "missing target " << target << '\n';
            return 1;
        }
        cout << "target=" << target
             << " rank=" << popcount(static_cast<unsigned>(target))
             << " interval=[" << best_left << ',' << best_right << ']'
             << " length=" << best_length
             << " mode="
             << (best_left < prefix_length ? "cross-seam" : "append-only")
             << '\n';
    }
    return 0;
}
