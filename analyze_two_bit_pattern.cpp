#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <algorithm>
#include <array>
#include <bit>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <string>
#include <vector>
using namespace std;

int main(int argc, char** argv) {
    if (argc != 3) return 2;
    const int k = stoi(argv[1]);
    const int rank = k / 2;
    ifstream in(argv[2]);
    vector<int> path;
    for (int x; in >> x;) path.push_back(x);
    const int low_mask = (1 << (k - 2)) - 1;
    auto type = [&](int x) { return x >> (k - 2); };
    array<int, 4> type_count{};
    array<array<int, 4>, 4> transitions{};
    map<pair<int, int>, int> run_histogram;
    vector<int> run_sequence;
    for (int x : path) ++type_count[type(x)];
    for (int i = 0; i + 1 < static_cast<int>(path.size()); ++i)
        ++transitions[type(path[i])][type(path[i + 1])];
    for (int i = 0; i < static_cast<int>(path.size());) {
        int j = i + 1;
        while (j < static_cast<int>(path.size()) && type(path[j]) == type(path[i])) ++j;
        ++run_histogram[{type(path[i]), j - i}];
        run_sequence.push_back(type(path[i]));
        i = j;
    }
    cout << "vertices=" << path.size() << " type_counts";
    for (int t = 0; t < 4; ++t) cout << ' ' << t << ':' << type_count[t];
    cout << " runs=" << run_sequence.size() << '\n';
    cout << "transition_matrix\n";
    for (int a = 0; a < 4; ++a) {
        for (int b = 0; b < 4; ++b) cout << transitions[a][b] << (b == 3 ? '\n' : ' ');
    }
    cout << "run_histogram";
    for (auto [key, count] : run_histogram)
        cout << " type" << key.first << "x" << key.second << ':' << count;
    cout << '\n';
    cout << "run_sequence";
    for (int i = 0; i < min<int>(run_sequence.size(), 200); ++i)
        cout << ' ' << run_sequence[i];
    if (run_sequence.size() > 200) cout << " ...";
    cout << '\n';

    // Analyze the four projected subsequences, both after filtering and only
    // across edges that remain inside one two-bit type block.
    for (int t = 0; t < 4; ++t) {
        vector<int> projected;
        for (int x : path) if (type(x) == t) projected.push_back(x & low_mask);
        int filtered_johnson = 0, internal_edges = 0, internal_johnson = 0;
        for (int i = 0; i + 1 < static_cast<int>(projected.size()); ++i)
            filtered_johnson += popcount(static_cast<unsigned>(projected[i] ^ projected[i + 1])) == 2;
        vector<unsigned char> meet(1 << (k - 2)), join(1 << (k - 2));
        for (int i = 0; i + 1 < static_cast<int>(path.size()); ++i) if (type(path[i]) == t && type(path[i + 1]) == t) {
            ++internal_edges;
            int a = path[i] & low_mask, b = path[i + 1] & low_mask;
            internal_johnson += popcount(static_cast<unsigned>(a ^ b)) == 2;
            meet[a & b] = 1;
            join[a | b] = 1;
        }
        int meets = accumulate(meet.begin(), meet.end(), 0);
        int joins = accumulate(join.begin(), join.end(), 0);
        cout << "type=" << t << " old_rank=" << rank - popcount(static_cast<unsigned>(t))
             << " filtered_edges=" << projected.size() - 1
             << " filtered_johnson=" << filtered_johnson
             << " internal_edges=" << internal_edges
             << " internal_johnson=" << internal_johnson
             << " distinct_meets=" << meets << " distinct_joins=" << joins << '\n';
    }

    // How the complete lower two rows are distributed among two-bit types.
    for (int length = 2; length <= 3; ++length) {
        array<int, 4> windows{};
        vector<unsigned char> seen(1 << k);
        for (int i = 0; i + length <= static_cast<int>(path.size()); ++i) {
            int value = (1 << k) - 1;
            for (int j = 0; j < length; ++j) value &= path[i + j];
            if (popcount(static_cast<unsigned>(value)) == rank - length + 1) {
                seen[value] = 1;
                ++windows[type(value)];
            }
        }
        array<int, 4> colors{};
        for (int x = 0; x < (1 << k); ++x) if (seen[x]) ++colors[type(x)];
        cout << "lower_length=" << length << " windows_by_type";
        for (int t = 0; t < 4; ++t) cout << ' ' << t << ':' << windows[t];
        cout << " colors_by_type";
        for (int t = 0; t < 4; ++t) cout << ' ' << t << ':' << colors[t];
        cout << '\n';
    }
}
