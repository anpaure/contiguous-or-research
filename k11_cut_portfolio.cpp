#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <algorithm>
#include <bit>
#include <iostream>
#include <limits>
#include <tuple>
#include <vector>

using namespace std;

struct Score {
    int cut = 0;
    int direction = 1;
    int run_deficit = 0;
    int lower_missing = 0;
    int upper_missing = 0;
    vector<int> missing;
};

static vector<int> linearize(const vector<int>& cycle, int cut, int direction) {
    const int n = cycle.size();
    vector<int> path;
    path.reserve(n);
    for (int offset = 0; offset < n; ++offset) {
        int index = (cut + direction * offset) % n;
        if (index < 0) index += n;
        path.push_back(cycle[index]);
    }
    return path;
}

static Score evaluate(const vector<int>& cycle, int cut, int direction,
                      int k, int rank, int delay) {
    const int full = (1 << k) - 1;
    const vector<int> path = linearize(cycle, cut, direction);
    Score score;
    score.cut = cut;
    score.direction = direction;

    for (int bit = 0; bit < k; ++bit) {
        int i = 0;
        while (i < static_cast<int>(path.size())) {
            if (!(path[i] & (1 << bit))) {
                ++i;
                continue;
            }
            const int first = i;
            while (i < static_cast<int>(path.size()) &&
                   (path[i] & (1 << bit))) ++i;
            if (first && i < static_cast<int>(path.size()))
                score.run_deficit += max(0, delay + 1 - (i - first));
        }
    }

    vector<unsigned char> seen(1 << k);
    for (int value : path) seen[value] = 1;
    for (int length = 2; length <= delay + 1; ++length) {
        int value = full;
        for (int i = 0; i < length; ++i) value &= path[i];
        seen[value] = 1;
        for (int left = 1; left + length <= static_cast<int>(path.size()); ++left) {
            value = full;
            for (int i = left; i < left + length; ++i) value &= path[i];
            seen[value] = 1;
        }
    }
    for (int length = 2; rank + length - 1 <= k; ++length) {
        for (int left = 0; left + length <= static_cast<int>(path.size()); ++left) {
            int value = 0;
            for (int i = left; i < left + length; ++i) value |= path[i];
            seen[value] = 1;
        }
    }

    // The omitted adjacent-intersection colour is represented at the cut
    // boundary in any factorization, so do not count it as a lower omission.
    const int previous = (cut - direction + static_cast<int>(cycle.size())) %
                         static_cast<int>(cycle.size());
    seen[cycle[previous] & cycle[cut]] = 1;

    for (int mask = 1; mask <= full; ++mask) {
        const int mask_rank = popcount(static_cast<unsigned>(mask));
        if (mask_rank < rank - delay || seen[mask]) continue;
        score.missing.push_back(mask);
        if (mask_rank < rank) ++score.lower_missing;
        if (mask_rank > rank) ++score.upper_missing;
    }
    return score;
}

int main(int argc, char** argv) {
    if (argc != 4) return 2;
    const int k = stoi(argv[1]);
    const int rank = stoi(argv[2]);
    const int delay = stoi(argv[3]);
    vector<int> cycle;
    for (int value; cin >> value;) cycle.push_back(value);
    if (cycle.empty()) return 2;
    if (popcount(static_cast<unsigned>(cycle.front() ^ cycle.back())) != 2) {
        cerr << "endpoints do not close to a Johnson cycle\n";
        return 1;
    }

    vector<Score> scores;
    for (int direction : {-1, 1})
        for (int cut = 0; cut < static_cast<int>(cycle.size()); ++cut)
            scores.push_back(evaluate(cycle, cut, direction, k, rank, delay));
    sort(scores.begin(), scores.end(), [](const Score& a, const Score& b) {
        return tie(a.run_deficit, a.lower_missing, a.upper_missing) <
               tie(b.run_deficit, b.lower_missing, b.upper_missing);
    });
    for (int i = 0; i < min(30, static_cast<int>(scores.size())); ++i) {
        const Score& s = scores[i];
        cout << "cut=" << s.cut << " dir=" << s.direction
             << " run=" << s.run_deficit
             << " lower=" << s.lower_missing
             << " upper=" << s.upper_missing << " missing";
        for (int value : s.missing) cout << ' ' << value;
        cout << '\n';
    }
}
