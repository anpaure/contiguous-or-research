#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#endif

#include <algorithm>
#include <bit>
#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char** argv) {
    if (argc < 4 || argc > 6) return 2;
    const int k = stoi(argv[1]);
    const int d = stoi(argv[2]);
    const string output_path = argv[3];
    const int maximum_target_rank = argc > 4 ? stoi(argv[4]) : k;
    const int minimum_target_rank = argc > 5 ? stoi(argv[5]) : 1;
    vector<int> central;
    for (int value; cin >> value;) central.push_back(value);
    if (central.empty()) return 2;
    const int central_rank = popcount(static_cast<unsigned>(central.front()));
    if (central_rank <= d) return 2;
    const int n = central.size() + d;
    const int limit = 1 << k;
    vector<int> envelope(n, limit - 1);
    for (int position = 0; position < n; ++position)
        for (int i = max(0, position - d);
             i <= min(static_cast<int>(central.size()) - 1, position); ++i)
            envelope[position] &= central[i];

    int variable_count = n * k;
    auto x = [&] (int position, int bit) { return position * k + bit + 1; };
    vector<vector<int>> clauses;
    for (int position = 0; position < n; ++position) {
        vector<int> nonzero;
        for (int bit = 0; bit < k; ++bit) {
            if (envelope[position] & (1 << bit)) nonzero.push_back(x(position, bit));
            else clauses.push_back({-x(position, bit)});
        }
        clauses.push_back(move(nonzero));
    }
    for (int start = 0; start < static_cast<int>(central.size()); ++start) {
        for (int bit = 0; bit < k; ++bit) {
            if (!(central[start] & (1 << bit))) continue;
            vector<int> cover;
            for (int position = start; position <= start + d; ++position)
                cover.push_back(x(position, bit));
            clauses.push_back(move(cover));
        }
    }

    long long selectors = 0;
    for (int target = 1; target < limit; ++target) {
        const int rank = popcount(static_cast<unsigned>(target));
        if (rank >= central_rank || rank > maximum_target_rank ||
            rank < minimum_target_rank) continue;
        vector<int> witnesses;
        // Any lower-rank witness has length at most d, because a length-(d+1)
        // interval contains a prescribed central window.  For the supported
        // d<=3 searches, min(d,rank) retains the needed boundary flexibility
        // while avoiding vacuous long singleton witnesses.  This remains a
        // sufficient structured labeling ansatz, not a general normal form.
        const int maximum_length = min(d, rank);
#ifdef NATURAL_GRADING
        const int minimum_length = rank <= central_rank - d ? 1
            : rank - (central_rank - d) + 1;
        const int last_length = minimum_length;
#else
        const int minimum_length = 1;
        const int last_length = maximum_length;
#endif
        for (int length = minimum_length; length <= last_length; ++length) {
            for (int left = 0; left + length <= n; ++left) {
                const int select = ++variable_count;
                ++selectors;
                witnesses.push_back(select);
                for (int bit = 0; bit < k; ++bit) {
                    if (!(target & (1 << bit))) {
                        for (int position = left; position < left + length; ++position)
                            clauses.push_back({-select, -x(position, bit)});
                    } else {
                        vector<int> cover{-select};
                        for (int position = left; position < left + length; ++position)
                            cover.push_back(x(position, bit));
                        clauses.push_back(move(cover));
                    }
                }
            }
        }
        clauses.push_back(move(witnesses));
    }

    ofstream output(output_path);
    output << "p cnf " << variable_count << ' ' << clauses.size() << '\n';
    for (const vector<int>& clause : clauses) {
        for (int literal : clause) output << literal << ' ';
        output << "0\n";
    }
    cerr << "n=" << n << " selectors=" << selectors
         << " variables=" << variable_count
         << " clauses=" << clauses.size() << '\n';
}
