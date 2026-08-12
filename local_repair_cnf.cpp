#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#endif

#include <algorithm>
#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

struct Interval {
    int fixed_or = 0;
    vector<int> variables;
};

int main(int argc, char** argv) {
    if (argc < 4) return 2;
    const int k = stoi(argv[1]);
    const int limit = 1 << k;
    const string output_path = argv[2];
    vector<int> positions;
    int maximum_flips = -1;
    for (int i = 3; i < argc; ++i) {
        const string argument = argv[i];
        if (argument.rfind("f=", 0) == 0) maximum_flips = stoi(argument.substr(2));
        else positions.push_back(stoi(argument));
    }
    sort(positions.begin(), positions.end());
    positions.erase(unique(positions.begin(), positions.end()), positions.end());
    vector<int> a;
    for (int value; cin >> value;) a.push_back(value);
    if (a.empty() || positions.empty() || positions.back() >= static_cast<int>(a.size()))
        return 2;
    vector<int> variable_index(a.size(), -1);
    for (int i = 0; i < static_cast<int>(positions.size()); ++i)
        variable_index[positions[i]] = i;

    int variable_count = positions.size() * k;
    vector<vector<int>> clauses;
    vector<vector<int>> x(positions.size(), vector<int>(k));
    for (int i = 0; i < static_cast<int>(positions.size()); ++i) {
        for (int bit = 0; bit < k; ++bit) {
            const int raw = i * k + bit + 1;
            // The semantic literal "this entry contains bit" is inverted
            // when the seed contains that bit.  Thus raw=false reproduces the
            // entire seed and gives Kissat a useful default phase.
            x[i][bit] = a[positions[i]] & (1 << bit) ? -raw : raw;
        }
        clauses.push_back(x[i]);
    }
    vector<Interval> intervals;
    vector<uint8_t> fixed_seen(limit);
    for (int left = 0; left < static_cast<int>(a.size()); ++left) {
        int fixed_or = 0;
        vector<int> contained;
        for (int right = left; right < static_cast<int>(a.size()); ++right) {
            const int index = variable_index[right];
            if (index < 0) fixed_or |= a[right];
            else contained.push_back(index);
            intervals.push_back({fixed_or, contained});
            if (contained.empty()) fixed_seen[fixed_or] = 1;
        }
    }
    int constrained_targets = 0;
    long long selectors = 0;
    for (int target = 1; target < limit; ++target) {
        if (fixed_seen[target]) continue;
        ++constrained_targets;
        vector<int> witnesses;
        for (const Interval& interval : intervals) {
            if (interval.fixed_or & ~target) continue;
            if ((target & ~interval.fixed_or) && interval.variables.empty()) continue;
            const int select = ++variable_count;
            witnesses.push_back(select);
            ++selectors;
            for (int bit = 0; bit < k; ++bit) {
                if (!(target & (1 << bit))) {
                    for (int index : interval.variables)
                        clauses.push_back({-select, -x[index][bit]});
                } else if (!(interval.fixed_or & (1 << bit))) {
                    vector<int> cover{-select};
                    for (int index : interval.variables) cover.push_back(x[index][bit]);
                    clauses.push_back(move(cover));
                }
            }
        }
        if (witnesses.empty()) {
            cerr << "structural UNSAT target=" << target << '\n';
            return 1;
        }
        clauses.push_back(move(witnesses));
    }
    if (maximum_flips >= 0 && maximum_flips < static_cast<int>(positions.size()) * k) {
        if (maximum_flips == 0) {
            for (int raw = 1; raw <= static_cast<int>(positions.size()) * k; ++raw)
                clauses.push_back({-raw});
        } else {
        vector<int> previous;
        const int raw_count = positions.size() * k;
        for (int raw = 1; raw <= raw_count; ++raw) {
            vector<int> current(maximum_flips);
            for (int& value : current) value = ++variable_count;
            clauses.push_back({-raw, current[0]});
            for (int j = 0; j < static_cast<int>(previous.size()); ++j)
                clauses.push_back({-previous[j], current[j]});
            for (int j = 0; j + 1 < static_cast<int>(previous.size()) &&
                            j + 1 < maximum_flips; ++j)
                clauses.push_back({-raw, -previous[j], current[j + 1]});
            if (static_cast<int>(previous.size()) == maximum_flips)
                clauses.push_back({-raw, -previous[maximum_flips - 1]});
            previous.swap(current);
        }
        }
    }
    ofstream output(output_path);
    output << "p cnf " << variable_count << ' ' << clauses.size() << '\n';
    for (const vector<int>& clause : clauses) {
        for (int literal : clause) output << literal << ' ';
        output << "0\n";
    }
    cerr << "positions=" << positions.size()
         << " constrained=" << constrained_targets
         << " selectors=" << selectors
         << " variables=" << variable_count
         << " clauses=" << clauses.size()
         << " max_flips=" << maximum_flips << '\n';
}
