#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

static int coverage(const vector<int>& a, int k) {
    vector<uint8_t> seen(1 << k);
    vector<int> previous, current;
    for (int x : a) {
        current.clear();
        current.push_back(x);
        for (int old : previous) {
            const int value = old | x;
            if (current.back() != value) current.push_back(value);
        }
        for (int value : current) seen[value] = 1;
        previous.swap(current);
    }
    int result = 0;
    for (int mask = 1; mask < (1 << k); ++mask) result += seen[mask];
    return result;
}

int main(int argc, char** argv) {
    if (argc != 2) return 2;
    const int k = stoi(argv[1]);
    vector<int> input;
    for (int value; cin >> value;) input.push_back(value);
    if (input.size() < 2) return 2;
    const int extra = input.back();
    input.pop_back();
    int best = -1, best_gap = -1;
    vector<int> best_array;
    vector<pair<int, int>> scores;
    for (int gap = 0; gap <= static_cast<int>(input.size()); ++gap) {
        vector<int> candidate = input;
        candidate.insert(candidate.begin() + gap, extra);
        const int score = coverage(candidate, k);
        scores.push_back({score, gap});
        if (score > best) {
            best = score;
            best_gap = gap;
            best_array.swap(candidate);
        }
    }
    sort(scores.begin(), scores.end(), greater<>());
    cerr << "best=" << best << " gap=" << best_gap << " extra=" << extra << '\n';
    cerr << "top";
    for (int i = 0; i < min(30, static_cast<int>(scores.size())); ++i)
        cerr << ' ' << scores[i].second << ':' << scores[i].first;
    cerr << '\n';
    for (int value : best_array) cout << value << ' ';
    cout << '\n';
}
