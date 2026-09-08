#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <algorithm>
#include <bit>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;

static vector<int> next_suffixes(const vector<int>& previous, int value) {
    vector<int> result{value};
    for (int old : previous) result.push_back(old | value);
    sort(result.begin(), result.end());
    result.erase(unique(result.begin(), result.end()), result.end());
    return result;
}

int main(int argc, char** argv) {
    if (argc < 2 || argc > 3) return 2;
    const int k = stoi(argv[1]);
    const int maximum_added = argc == 3 ? stoi(argv[2]) : (1 << k);
    const int limit = 1 << k;
    vector<int> array;
    for (int value; cin >> value;) {
        if (value <= 0 || value >= limit) return 3;
        array.push_back(value);
    }
    vector<uint8_t> seen(limit);
    vector<int> suffixes;
    int covered = 0;
    for (int value : array) {
        suffixes = next_suffixes(suffixes, value);
        for (int current : suffixes) if (!seen[current]) {
            seen[current] = 1; ++covered;
        }
    }
    for (int step = 0; step < maximum_added && covered < limit - 1; ++step) {
        int best_value = -1, best_gain = -1, best_suffix_count = 0;
        vector<int> best_suffixes;
        for (int value = 1; value < limit; ++value) {
            vector<int> candidate = next_suffixes(suffixes, value);
            int gain = 0;
            for (int current : candidate) gain += !seen[current];
            // Prefer a richer suffix chain after equal immediate gain; it
            // retains more options for subsequent cross-boundary intervals.
            if (gain > best_gain ||
                (gain == best_gain && static_cast<int>(candidate.size()) > best_suffix_count) ||
                (gain == best_gain && static_cast<int>(candidate.size()) == best_suffix_count &&
                 popcount(static_cast<unsigned>(value)) <
                 popcount(static_cast<unsigned>(best_value)))) {
                best_gain = gain;
                best_value = value;
                best_suffix_count = candidate.size();
                best_suffixes.swap(candidate);
            }
        }
        if (best_value < 0 || best_gain <= 0) return 4;
        array.push_back(best_value);
        suffixes.swap(best_suffixes);
        for (int current : suffixes) if (!seen[current]) {
            seen[current] = 1; ++covered;
        }
        cerr << "step=" << step + 1 << " value=" << best_value
             << " gain=" << best_gain << " suffixes=" << suffixes.size()
             << " covered=" << covered << '/' << limit - 1 << '\n';
    }
    cerr << "final_length=" << array.size() << " covered=" << covered
         << '/' << limit - 1 << '\n';
    for (int value : array) cout << value << ' ';
    cout << '\n';
    return covered == limit - 1 ? 0 : 1;
}
