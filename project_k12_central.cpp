#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <algorithm>
#include <bit>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

static int delete_coordinate(int x, int bit) {
    const int low = x & ((1 << bit) - 1);
    return low | ((x >> (bit + 1)) << bit);
}

struct Score {
    int invalid_edges = 0;
    int short_runs = 0;
    int run_deficit = 0;
    vector<int> missing;
    int total_missing = 0;
};

static Score analyze(const vector<int>& path, int k, int rank, int d) {
    const int limit = 1 << k;
    vector<vector<uint8_t>> seen(k + 1, vector<uint8_t>(limit));
    Score score;
    for (int x : path) seen[rank][x] = 1;

    for (int i = 0; i + 1 < static_cast<int>(path.size()); ++i)
        score.invalid_edges += popcount(static_cast<unsigned>(path[i] ^ path[i + 1])) != 2;

    for (int bit = 0; bit < k; ++bit) {
        int i = 0;
        while (i < static_cast<int>(path.size())) {
            if (!(path[i] & (1 << bit))) { ++i; continue; }
            const int left = i;
            while (i < static_cast<int>(path.size()) && (path[i] & (1 << bit))) ++i;
            const int length = i - left;
            if (left > 0 && i < static_cast<int>(path.size()) && length < d + 1) {
                ++score.short_runs;
                score.run_deficit += d + 1 - length;
            }
        }
    }

    for (int length = 2; length <= d + 1; ++length) {
        const int wanted = rank - length + 1;
        for (int left = 0; left + length <= static_cast<int>(path.size()); ++left) {
            int value = limit - 1;
            for (int j = left; j < left + length; ++j) value &= path[j];
            if (popcount(static_cast<unsigned>(value)) == wanted) seen[wanted][value] = 1;
        }
    }
    for (int length = 2; rank + length - 1 <= k; ++length) {
        const int wanted = rank + length - 1;
        for (int left = 0; left + length <= static_cast<int>(path.size()); ++left) {
            int value = 0;
            for (int j = left; j < left + length; ++j) value |= path[j];
            if (popcount(static_cast<unsigned>(value)) == wanted) seen[wanted][value] = 1;
        }
    }
    for (int r = rank - d; r <= k; ++r) {
        int missing = 0;
        for (int x = 1; x < limit; ++x)
            if (popcount(static_cast<unsigned>(x)) == r && !seen[r][x]) ++missing;
        score.missing.push_back(missing);
        score.total_missing += missing;
    }
    return score;
}

int main(int argc, char** argv) {
    if (argc < 2) return 2;
    ifstream input(argv[1]);
    vector<int> source;
    for (int x; input >> x;) source.push_back(x);
    if (source.size() != 924) {
        cerr << "expected 924 rank-6 masks, got " << source.size() << '\n';
        return 2;
    }

    int best_bit = -1;
    Score best_score;
    vector<int> best_path;
    for (int bit = 0; bit < 12; ++bit) {
        vector<int> path;
        for (int x : source)
            if (!(x & (1 << bit))) path.push_back(delete_coordinate(x, bit));
        if (path.size() != 462) return 3;
        Score score = analyze(path, 11, 6, 3);
        cout << "bit=" << bit << " invalid_edges=" << score.invalid_edges
             << " short_runs=" << score.short_runs
             << " run_deficit=" << score.run_deficit << " missing_by_rank=";
        for (int x : score.missing) cout << x << ',';
        cout << " total_missing=" << score.total_missing << '\n';
        const auto key = pair(score.run_deficit, score.total_missing);
        const auto best_key = pair(best_score.run_deficit, best_score.total_missing);
        if (best_bit < 0 || key < best_key) {
            best_bit = bit;
            best_score = score;
            best_path = move(path);
        }
    }
    ofstream out(argc > 2 ? argv[2] : "k11_projected_central_best.txt");
    for (int x : best_path) out << x << ' ';
    out << '\n';
    cout << "best_bit=" << best_bit << " run_deficit=" << best_score.run_deficit
         << " total_missing=" << best_score.total_missing << '\n';
}
