#include <algorithm>
#include <array>
#include <bit>
#include <fstream>
#include <iostream>
#include <set>
#include <string>
#include <tuple>
#include <vector>

using namespace std;

static int wt(int x) { return popcount(static_cast<unsigned>(x)); }

static vector<int> read_all(const string& name) {
    ifstream in(name);
    if (!in) throw runtime_error("cannot open " + name);
    vector<int> result;
    for (int x; in >> x;) result.push_back(x);
    return result;
}

struct Score {
    int deficit = 0;
    int violations = 0;
    vector<array<int, 5>> detail;  // bit, first, last, length, required
};

static Score score(const vector<int>& row, int short_count) {
    Score result;
    for (int bit = 0; bit < 11; ++bit) {
        int at = 0;
        while (at < static_cast<int>(row.size())) {
            if (!(row[at] & (1 << bit))) {
                ++at;
                continue;
            }
            const int first = at;
            while (at < static_cast<int>(row.size()) &&
                   (row[at] & (1 << bit)))
                ++at;
            if (first == 0 || at == static_cast<int>(row.size())) continue;
            // One-based run starts <= short_count+1 need length three;
            // later starts need length four.
            const int required = first <= short_count ? 3 : 4;
            const int length = at - first;
            if (length < required) {
                result.deficit += required - length;
                ++result.violations;
                result.detail.push_back(
                    {bit, first + 1, at, length, required});
            }
        }
    }
    return result;
}

static vector<int> upper_row(const vector<int>& cycle, int start, int direction) {
    vector<int> result;
    int at = start;
    while (result.size() < 462) {
        if (wt(cycle[at]) == 6) result.push_back(cycle[at]);
        at = (at + direction + cycle.size()) % cycle.size();
    }
    return result;
}

int main(int argc, char** argv) {
    if (argc != 3) {
        cerr << "usage: ml11_mixed_cut_analyze PATH CYCLE\n";
        return 2;
    }
    vector<int> path, cycle;
    try {
        path = read_all(argv[1]);
        cycle = read_all(argv[2]);
    } catch (const exception& e) {
        cerr << e.what() << '\n';
        return 2;
    }
    if (path.size() != 37 || cycle.size() != 924) return 2;
    vector<int> prescribed;
    for (int x : path) if (wt(x) == 6) prescribed.push_back(x);
    const set<int> prescribed_set(prescribed.begin(), prescribed.end());

    int valid = 0, factorable = 0;
    tuple<int, int, int, int> best{1 << 20, 1 << 20, 0, 0};
    vector<int> best_row;
    vector<tuple<int, int, Score>> prefix_schedules;
    for (int direction : {-1, 1}) {
        for (int start = 0; start < static_cast<int>(cycle.size()); ++start) {
            if (wt(cycle[start]) != 6) continue;
            vector<int> row = upper_row(cycle, start, direction);
            bool q_disjoint = true;
            for (int i = 369; i < 462; ++i)
                if (prescribed_set.count(row[i])) q_disjoint = false;
            if (!q_disjoint) continue;
            ++valid;
            const Score value = score(row, 369);
            if (!value.deficit) ++factorable;
            const auto key = tuple{value.deficit, value.violations,
                                   cycle[start], direction};
            if (key < best) {
                best = key;
                best_row = row;
            }
            if (equal(prescribed.begin(), prescribed.end(), row.begin()))
                prefix_schedules.push_back({direction, 0, value});
            vector<int> reversed = prescribed;
            reverse(reversed.begin(), reversed.end());
            if (equal(reversed.begin(), reversed.end(), row.begin()))
                prefix_schedules.push_back({direction, 1, value});
        }
    }

    const auto [best_deficit, best_violations, best_start, best_direction] = best;
    cout << "valid_q_arcs=" << valid << " factorable=" << factorable << '\n';
    cout << "best deficit=" << best_deficit
         << " violations=" << best_violations
         << " start_mask=" << best_start
         << " direction=" << best_direction << '\n';
    cout << "best_P_first=" << best_row.front()
         << " best_P_last=" << best_row[368]
         << " best_Q_first=" << best_row[369]
         << " best_Q_last=" << best_row.back() << '\n';
    for (const auto& [direction, reversed, value] : prefix_schedules)
        cout << "prefix_at_P_start direction=" << direction
             << " reversed=" << reversed
             << " deficit=" << value.deficit
             << " violations=" << value.violations << '\n';

    // The orientation that retains the certified prefix order also admits a
    // q=19 schedule.  Report its exact run score and the fixed-boundary test
    // from Theorem 5.1 of K11_PORTAL_EMBEDDING_MATH_NEXT.md.
    for (int start = 0; start < static_cast<int>(cycle.size()); ++start)
        for (int direction : {-1, 1}) {
            if (wt(cycle[start]) != 6) continue;
            vector<int> row = upper_row(cycle, start, direction);
            if (!equal(prescribed.begin(), prescribed.end(), row.begin()))
                continue;
            const Score value = score(row, 19);
            const vector<int> d(row.begin() + 19, row.end());
            const bool containment = !(550 & ~d[0]) && !(546 & ~d[1]) &&
                                     !(514 & ~d[2]);
            const bool initial_runs = !((d[0] & ~d[1]) & ~4) &&
                !(((d[0] & d[1]) & ~d[2]) & ~32) &&
                !(((d[0] & d[1] & d[2]) & ~d[3]) & ~514);
            cout << "q19_prefix_order deficit=" << value.deficit
                 << " violations=" << value.violations
                 << " fixed_boundary_containment=" << containment
                 << " fixed_boundary_initial_runs=" << initial_runs
                 << " D_first=" << d[0] << ',' << d[1] << ',' << d[2]
                 << ',' << d[3] << '\n';
        }
}
