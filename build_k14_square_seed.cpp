#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <algorithm>
#include <bit>
#include <fstream>
#include <iostream>
#include <limits>
#include <string>
#include <tuple>
#include <vector>

using namespace std;

static vector<int> reflected_gray(int n, int choose) {
    if (choose == 0) return {0};
    if (choose == n) return {(1 << n) - 1};
    vector<int> first = reflected_gray(n - 1, choose);
    vector<int> second = reflected_gray(n - 1, choose - 1);
    reverse(second.begin(), second.end());
    for (int& x : second) x |= 1 << (n - 1);
    first.insert(first.end(), second.begin(), second.end());
    return first;
}

static bool adjacent(int x, int y) {
    return popcount(static_cast<unsigned>(x ^ y)) == 2;
}

// Rotate a cyclic Gray ordering so target is the requested endpoint.
static vector<int> rotate_cycle(vector<int> path, int target, bool target_first) {
    if (!adjacent(path.front(), path.back())) {
        cerr << "reflected ordering is not cyclic\n";
        exit(3);
    }
    const int at = find(path.begin(), path.end(), target) - path.begin();
    rotate(path.begin(), path.begin() + at, path.end());
    if (!target_first) {
        // target first -> reverse makes it last while preserving all edges.
        reverse(path.begin(), path.end());
    }
    return path;
}

struct Eval {
    int deficit = 0;
    int missing = 0;
    vector<int> by_rank;
};

static Eval evaluate(const vector<int>& path) {
    constexpr int k = 14, rank = 7, d = 2, limit = 1 << k;
    Eval e;
    e.by_rank.assign(k + 1, 0);
    for (int bit = 0; bit < k; ++bit) {
        int i = 0;
        while (i < static_cast<int>(path.size())) {
            if (!(path[i] & (1 << bit))) { ++i; continue; }
            const int left = i;
            while (i < static_cast<int>(path.size()) && (path[i] & (1 << bit))) ++i;
            if (left && i < static_cast<int>(path.size()))
                e.deficit += max(0, d + 1 - (i - left));
        }
    }
    vector<vector<uint8_t>> seen(k + 1, vector<uint8_t>(limit));
    for (int x : path) seen[rank][x] = 1;
    for (int length = 2; length <= d + 1; ++length) {
        const int wanted = rank - length + 1;
        for (int left = 0; left + length <= static_cast<int>(path.size()); ++left) {
            int x = limit - 1;
            for (int j = left; j < left + length; ++j) x &= path[j];
            if (popcount(static_cast<unsigned>(x)) == wanted) seen[wanted][x] = 1;
        }
    }
    for (int length = 2; rank + length - 1 <= k; ++length) {
        const int wanted = rank + length - 1;
        for (int left = 0; left + length <= static_cast<int>(path.size()); ++left) {
            int x = 0;
            for (int j = left; j < left + length; ++j) x |= path[j];
            if (popcount(static_cast<unsigned>(x)) == wanted) seen[wanted][x] = 1;
        }
    }
    for (int r = rank - d; r <= k; ++r) {
        int miss = 0;
        for (int x = 1; x < limit; ++x)
            if (popcount(static_cast<unsigned>(x)) == r && !seen[r][x]) ++miss;
        e.by_rank[r] = miss;
        e.missing += miss;
    }
    return e;
}

int main(int argc, char** argv) {
    if (argc < 2) return 2;
    ifstream input(argv[1]);
    vector<int> t;
    for (int x; input >> x;) t.push_back(x);
    if (t.size() != 924) return 2;

    const int new_a = 1 << 12;
    const int new_b = 1 << 13;
    vector<int> gray7 = reflected_gray(12, 7);
    vector<int> gray5 = reflected_gray(12, 5);

    tuple<int, int> best_key{numeric_limits<int>::max(), numeric_limits<int>::max()};
    vector<int> best;
    Eval best_eval;
    string best_description;

    for (int reverse_t = 0; reverse_t < 2; ++reverse_t) {
        vector<int> q = t;
        if (reverse_t) reverse(q.begin(), q.end());
        const int endpoint = q.front();
        for (int add = 0; add < 12; ++add) {
            if (endpoint & (1 << add)) continue;
            const int seven = endpoint | (1 << add);
            vector<int> p7 = rotate_cycle(gray7, seven, false);
            for (int drop = 0; drop < 12; ++drop) {
                if (!(endpoint & (1 << drop))) continue;
                const int five = endpoint ^ (1 << drop);
                vector<int> p5 = rotate_cycle(gray5, five, true);
                for (int reverse_p7 = 0; reverse_p7 < 2; ++reverse_p7) {
                    // Reversing and then re-rotating keeps the chosen junction endpoint.
                    vector<int> left = p7;
                    if (reverse_p7) {
                        reverse(left.begin(), left.end());
                        left = rotate_cycle(left, seven, false);
                    }
                    for (int reverse_p5 = 0; reverse_p5 < 2; ++reverse_p5) {
                        vector<int> right = p5;
                        if (reverse_p5) {
                            reverse(right.begin(), right.end());
                            right = rotate_cycle(right, five, true);
                        }
                        vector<int> path;
                        path.reserve(3432);
                        path.insert(path.end(), left.begin(), left.end());
                        for (int x : q) path.push_back(new_a | x);
                        for (auto it = q.rbegin(); it != q.rend(); ++it)
                            path.push_back(new_b | *it);
                        for (int x : right) path.push_back(new_a | new_b | x);
                        for (int i = 0; i + 1 < static_cast<int>(path.size()); ++i)
                            if (!adjacent(path[i], path[i + 1])) return 4;
                        Eval e = evaluate(path);
                        const tuple<int, int> key{e.deficit, e.missing};
                        if (key < best_key) {
                            best_key = key;
                            best = move(path);
                            best_eval = e;
                            best_description = "reverse_t=" + to_string(reverse_t) +
                                " add=" + to_string(add) + " drop=" + to_string(drop) +
                                " rp7=" + to_string(reverse_p7) +
                                " rp5=" + to_string(reverse_p5);
                            cerr << "BEST " << best_description << " deficit=" << e.deficit
                                 << " missing=" << e.missing << " by_rank";
                            for (int r = 5; r <= 14; ++r) cerr << ' ' << r << ':' << e.by_rank[r];
                            cerr << '\n';
                        }
                    }
                }
            }
        }
    }
    ofstream out(argc > 2 ? argv[2] : "k14_square_seed.txt");
    for (int x : best) out << x << ' ';
    out << '\n';
    cout << best_description << " deficit=" << best_eval.deficit
         << " missing=" << best_eval.missing << '\n';
}
