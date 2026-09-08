#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <algorithm>
#include <bit>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

static bool johnson_adjacent(int a, int b) {
    return a == b || popcount(static_cast<unsigned>(a ^ b)) == 2;
}

static void report(const string& name, const vector<int>& raw, int bits, int rank) {
    const int limit = 1 << bits;
    vector<int> compressed;
    for (int value : raw)
        if (compressed.empty() || compressed.back() != value) compressed.push_back(value);
    vector<char> seen(limit);
    int distinct = 0, invalid = 0;
    for (int value : raw) if (!seen[value]) seen[value] = true, ++distinct;
    for (int i = 0; i + 1 < static_cast<int>(compressed.size()); ++i)
        invalid += !johnson_adjacent(compressed[i], compressed[i + 1]);

    // Chronological loop erasure of the derived Johnson walk.
    vector<int> loop_erased;
    vector<int> position(limit, -1);
    for (int value : compressed) {
        if (position[value] < 0) {
            position[value] = loop_erased.size();
            loop_erased.push_back(value);
        } else {
            const int keep = position[value] + 1;
            while (static_cast<int>(loop_erased.size()) > keep) {
                position[loop_erased.back()] = -1;
                loop_erased.pop_back();
            }
        }
    }

    // Greedy first occurrences are not generally a walk; record how close.
    vector<int> first;
    fill(seen.begin(), seen.end(), false);
    for (int value : compressed)
        if (!seen[value]) seen[value] = true, first.push_back(value);
    int first_bad = 0;
    for (int i = 0; i + 1 < static_cast<int>(first.size()); ++i)
        first_bad += !johnson_adjacent(first[i], first[i + 1]);

    int expected = 0;
    for (int value = 0; value < limit; ++value)
        expected += popcount(static_cast<unsigned>(value)) == rank;
    cout << name << " raw=" << raw.size() << " compressed=" << compressed.size()
         << " distinct=" << distinct << '/' << expected
         << " compressed_bad_edges=" << invalid
         << " loop_erased=" << loop_erased.size()
         << " first_occurrence_bad_edges=" << first_bad << '\n';
}

int main(int argc, char** argv) {
    if (argc != 3) return 2;
    const int bits = stoi(argv[1]);
    const int rank = stoi(argv[2]);
    vector<int> path;
    for (int value; cin >> value;) path.push_back(value);
    vector<int> lower, upper;
    for (int i = 0; i + 1 < static_cast<int>(path.size()); ++i) {
        lower.push_back(path[i] & path[i + 1]);
        upper.push_back(path[i] | path[i + 1]);
    }
    report("lower", lower, bits, rank - 1);
    report("upper", upper, bits, rank + 1);
}
