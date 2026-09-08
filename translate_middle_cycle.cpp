#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#elif defined(__clang__)
#pragma clang optimize on
#endif

#include <algorithm>
#include <bit>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>

using namespace std;

static vector<int> translate(const vector<int>& lower, int first_upper,
                             const vector<int>& startup) {
    const int first_lower = lower.front();
    vector<int> result{first_upper ^ first_lower};
    result.insert(result.end(), startup.begin(), startup.end());
    vector<int> blocks(startup.rbegin(), startup.rend());
    blocks.push_back(first_upper ^ first_lower);
    for (int i = 1; i < static_cast<int>(lower.size()); ++i) {
        const int old_lower = lower[i - 1], next_lower = lower[i];
        const int removed = old_lower & ~next_lower;
        int request = next_lower & ~old_lower;
        bool at_removed = false;
        for (int block : blocks) {
            if (block & removed) at_removed = true;
            if (at_removed) request |= block & next_lower;
        }
        result.push_back(request);
        vector<int> next{request};
        for (int block : blocks) if ((block &= ~request)) next.push_back(block);
        blocks.swap(next);
    }
    return result;
}

static int score(int k, const vector<int>& a) {
    vector<uint8_t> seen(1 << k);
    vector<int> previous;
    int result = 0;
    for (int value : a) {
        vector<int> current{value};
        for (int x : previous) {
            x |= value;
            if (x != current.back()) current.push_back(x);
        }
        for (int x : current) if (!seen[x]) seen[x] = 1, ++result;
        previous.swap(current);
    }
    return result;
}

int main(int argc, char** argv) {
    if (argc < 2) return 2;
    const int k = stoi(argv[1]);
    const int m = (k - 1) / 2;
    vector<int> lower;
    string line;
    while (cin >> line) {
        if (static_cast<int>(line.size()) != k ||
            line.find_first_not_of("01") != string::npos) continue;
        int mask = 0;
        for (int i = 0; i < k; ++i) if (line[i] == '1') mask |= 1 << i;
        if (popcount(static_cast<unsigned>(mask)) == m) lower.push_back(mask);
    }
    if (lower.empty()) return 3;

    int best_score = 0;
    vector<int> best;
    for (int direction = 0; direction < 2; ++direction) {
        for (int shift = 0; shift < static_cast<int>(lower.size()); ++shift) {
            rotate(lower.begin(), lower.begin() + 1, lower.end());
            const int first_upper = lower.back() | lower.front();
            vector<int> startup;
            for (int x = lower.front(); x; x &= x - 1) startup.push_back(x & -x);
            do {
                vector<int> a = translate(lower, first_upper, startup);
                int s = score(k, a);
                if (s > best_score) {
                    best_score = s;
                    best = std::move(a);
                    cerr << "score " << best_score << '/' << ((1 << k) - 1)
                         << " shift " << shift << " direction " << direction << '\n';
                }
            } while (next_permutation(startup.begin(), startup.end()));
        }
        reverse(lower.begin(), lower.end());
    }
    cout << best.size();
    for (int x : best) cout << ' ' << x;
    cout << '\n';
    return best_score == (1 << k) - 1 ? 0 : 1;
}
