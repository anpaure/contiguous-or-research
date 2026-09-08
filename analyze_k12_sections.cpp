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
#include <set>
#include <string>
#include <vector>

using namespace std;

static int erase_bit(int x, int bit) {
    return (x & ((1 << bit) - 1)) | ((x >> (bit + 1)) << bit);
}

struct Score {
    int invalid_edges = 0;
    int short_runs = 0;
    int run_deficit = 0;
    vector<int> missing;
};

static Score score_rank6(const vector<int>& path) {
    constexpr int k = 11, rank = 6, delay = 3, full = (1 << k) - 1;
    vector<vector<unsigned char>> seen(k + 1, vector<unsigned char>(1 << k));
    Score score;
    for (int x : path) seen[rank][x] = 1;
    for (int i = 0; i + 1 < static_cast<int>(path.size()); ++i)
        score.invalid_edges += popcount(static_cast<unsigned>(path[i] ^ path[i + 1])) != 2;
    for (int bit = 0; bit < k; ++bit) {
        int i = 0;
        while (i < static_cast<int>(path.size())) {
            if (!(path[i] & (1 << bit))) { ++i; continue; }
            const int first = i;
            while (i < static_cast<int>(path.size()) && (path[i] & (1 << bit))) ++i;
            if (first && i < static_cast<int>(path.size()) && i - first < delay + 1) {
                ++score.short_runs;
                score.run_deficit += delay + 1 - (i - first);
            }
        }
    }
    for (int length = 2; length <= delay + 1; ++length) {
        const int wanted = rank - length + 1;
        for (int left = 0; left + length <= static_cast<int>(path.size()); ++left) {
            int x = full;
            for (int j = 0; j < length; ++j) x &= path[left + j];
            if (popcount(static_cast<unsigned>(x)) == wanted) seen[wanted][x] = 1;
        }
    }
    for (int length = 2; rank + length - 1 <= k; ++length) {
        const int wanted = rank + length - 1;
        for (int left = 0; left + length <= static_cast<int>(path.size()); ++left) {
            int x = 0;
            for (int j = 0; j < length; ++j) x |= path[left + j];
            if (popcount(static_cast<unsigned>(x)) == wanted) seen[wanted][x] = 1;
        }
    }
    score.missing.assign(k + 1, 0);
    for (int x = 1; x <= full; ++x) {
        int r = popcount(static_cast<unsigned>(x));
        if (r >= rank - delay && !seen[r][x]) ++score.missing[r];
    }
    return score;
}

static void print_score(const Score& s) {
    cout << "bad=" << s.invalid_edges << " runs=" << s.short_runs
         << '/' << s.run_deficit << " miss=";
    for (int r = 3; r <= 11; ++r) cout << r << ':' << s.missing[r] << ',';
}

int main(int argc, char** argv) {
    if (argc < 2) return 2;
    ifstream in(argv[1]);
    vector<int> q;
    for (int x; in >> x;) q.push_back(x);
    if (q.size() != 924) {
        cerr << "expected 924 central masks, got " << q.size() << '\n';
        return 2;
    }
    for (int z = 0; z < 12; ++z) {
        vector<int> zero, one, zero_run_lengths, one_run_lengths;
        int mixed_edges = 0;
        for (int i = 0; i < static_cast<int>(q.size());) {
            bool value = q[i] & (1 << z);
            int j = i + 1;
            while (j < static_cast<int>(q.size()) && bool(q[j] & (1 << z)) == value) ++j;
            (value ? one_run_lengths : zero_run_lengths).push_back(j - i);
            i = j;
        }
        for (int i = 0; i + 1 < static_cast<int>(q.size()); ++i)
            mixed_edges += bool(q[i] & (1 << z)) != bool(q[i + 1] & (1 << z));
        for (int x : q) {
            if (x & (1 << z)) one.push_back(erase_bit(x, z));
            else zero.push_back(erase_bit(x, z));
        }
        vector<int> dual;
        dual.reserve(one.size());
        for (int x : one) dual.push_back(((1 << 11) - 1) ^ x);

        Score zs = score_rank6(zero), ds = score_rank6(dual);
        cout << "z=" << z << " mixed=" << mixed_edges
             << " zruns=" << zero_run_lengths.size() << " oruns=" << one_run_lengths.size()
             << " zrange=" << *min_element(zero_run_lengths.begin(), zero_run_lengths.end())
             << '-' << *max_element(zero_run_lengths.begin(), zero_run_lengths.end())
             << " orange=" << *min_element(one_run_lengths.begin(), one_run_lengths.end())
             << '-' << *max_element(one_run_lengths.begin(), one_run_lengths.end()) << "\n  zero ";
        print_score(zs);
        cout << "\n  dual ";
        print_score(ds);

        // Exact inverse-braid signature.  In a standard braid one section is
        // a single block P and the other section, after erasing z, is the set
        // of P's adjacent intersections plus the omitted colour.  We report
        // how many residual one-section consecutive pairs have the required
        // local relation even when the section-convex condition fails.
        set<int> zero_intersections;
        int zero_valid_edges = 0;
        for (int i = 0; i + 1 < static_cast<int>(zero.size()); ++i) {
            if (popcount(static_cast<unsigned>(zero[i] ^ zero[i + 1])) == 2) {
                ++zero_valid_edges;
                zero_intersections.insert(zero[i] & zero[i + 1]);
            }
        }
        int one_valid_edges = 0;
        set<int> one_unions;
        for (int i = 0; i + 1 < static_cast<int>(one.size()); ++i) {
            if (popcount(static_cast<unsigned>(one[i] ^ one[i + 1])) == 2) {
                ++one_valid_edges;
                one_unions.insert(one[i] | one[i + 1]);
            }
        }
        cout << "\n  valid-section edges zero=" << zero_valid_edges
             << " distinct-I=" << zero_intersections.size()
             << " one=" << one_valid_edges << " distinct-U=" << one_unions.size() << '\n';

        if (argc > 2 && z == stoi(argv[2])) {
            string prefix = argc > 3 ? argv[3] : "k11_k12_section";
            ofstream oz(prefix + "_zero.txt"), od(prefix + "_dual_one.txt");
            for (int x : zero) oz << x << ' ';
            for (int x : dual) od << x << ' ';
            oz << '\n'; od << '\n';
        }
    }
}
