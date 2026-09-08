#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char** argv) {
    if (argc != 2) return 2;
    const int k = stoi(argv[1]);
    const int limit = 1 << k;
    vector<int> word;
    for (int x; cin >> x;) word.push_back(x);
    for (int skip = 0; skip < static_cast<int>(word.size()); ++skip) {
        vector<uint8_t> seen(limit, false);
        array<int, 32> previous{}, current{};
        int previous_size = 0;
        for (int position = 0; position < static_cast<int>(word.size()); ++position) {
            if (position == skip) continue;
            int current_size = 0;
            current[current_size++] = word[position];
            for (int i = 0; i < previous_size; ++i) {
                int value = previous[i] | word[position];
                if (value != current[current_size - 1]) current[current_size++] = value;
            }
            for (int i = 0; i < current_size; ++i) seen[current[i]] = true;
            previous.swap(current);
            previous_size = current_size;
        }
        vector<int> by_rank(k + 1, 0);
        int missing = 0;
        for (int mask = 1; mask < limit; ++mask)
            if (!seen[mask]) {
                ++missing;
                ++by_rank[popcount(static_cast<unsigned>(mask))];
            }
        if (by_rank[7] <= 12) {
            cout << "skip=" << skip << " value=" << word[skip]
                 << " missing=" << missing << " ranks=";
            for (int rank = 1; rank <= k; ++rank)
                if (by_rank[rank]) cout << rank << ':' << by_rank[rank] << ',';
            cout << '\n';
        }
    }
}
