#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <cadical.hpp>

#include <algorithm>
#include <bit>
#include <cstdlib>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

struct Interval {
    int fixed_or = 0;
    vector<int> variables;
};

int main(int argc, char** argv) {
    if (argc < 3) return 2;
    const int k = stoi(argv[1]);
    const int limit = 1 << k;
    int first_position_argument = 2;
    int top_witnesses = 0;
    const string option = argv[2];
    if (option.rfind("top=", 0) == 0) {
        top_witnesses = stoi(option.substr(4));
        first_position_argument = 3;
    }
    vector<int> positions;
    for (int i = first_position_argument; i < argc; ++i)
        positions.push_back(stoi(argv[i]));
    sort(positions.begin(), positions.end());
    positions.erase(unique(positions.begin(), positions.end()), positions.end());
    vector<int> a;
    for (int value; cin >> value;) a.push_back(value);
    if (a.empty() || positions.back() >= static_cast<int>(a.size())) return 2;

    vector<int> variable_index(a.size(), -1);
    for (int i = 0; i < static_cast<int>(positions.size()); ++i)
        variable_index[positions[i]] = i;

    vector<Interval> intervals;
    intervals.reserve(a.size() * (a.size() + 1) / 2);
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
    long long selector_bound = 0;
    for (int target = 1; target < limit; ++target) {
        if (fixed_seen[target]) continue;
        for (const Interval& interval : intervals) {
            if (interval.fixed_or & ~target) continue;
            const int missing_bits = target & ~interval.fixed_or;
            if (missing_bits && interval.variables.empty()) continue;
            ++selector_bound;
        }
    }
    // With top-witness pruning, at most `top_witnesses` selectors survive for
    // each target.  Using the unpruned selector count here needlessly rejects
    // larger repair regions before the pruning below is applied.
    const long long declared = static_cast<long long>(positions.size()) * k +
        (top_witnesses > 0
             ? static_cast<long long>(limit - 1) * top_witnesses
             : selector_bound);
    if (declared > 2000000000LL) return 2;

    CaDiCaL::Solver solver;
    solver.set("quiet", 1);
    solver.declare_more_variables(static_cast<int>(declared));
    vector<int8_t> preferred_phase(static_cast<size_t>(declared) + 1, 1);
    int variable_count = 0;
    auto variable = [&] { return ++variable_count; };
    const char* dimacs_path = getenv("LOCAL_REPAIR_DIMACS");
    vector<vector<int>> stored_clauses;
    auto clause = [&] (const vector<int>& values) {
        if (dimacs_path) stored_clauses.push_back(values);
        for (int value : values) solver.add(value);
        solver.add(0);
    };
    vector<vector<int>> x(positions.size(), vector<int>(k));
    for (int i = 0; i < static_cast<int>(positions.size()); ++i) {
        for (int bit = 0; bit < k; ++bit) {
            x[i][bit] = variable();
            const bool originally_set = a[positions[i]] & (1 << bit);
            preferred_phase[x[i][bit]] = originally_set ? 1 : -1;
            solver.phase(originally_set ? x[i][bit] : -x[i][bit]);
        }
        clause(x[i]);
    }

    int constrained_targets = 0;
    long long selector_count = 0;
    for (int target = 1; target < limit; ++target) {
        if (fixed_seen[target]) continue;
        ++constrained_targets;
        vector<int> witnesses;
        int best_interval = -1;
        int best_cost = 1000000000;
        vector<pair<int,int>> ranked_intervals;
        for (int interval_index = 0;
             interval_index < static_cast<int>(intervals.size());
             ++interval_index) {
            const Interval& interval = intervals[interval_index];
            if (interval.fixed_or & ~target) continue;
            const int missing_bits = target & ~interval.fixed_or;
            if (missing_bits && interval.variables.empty()) continue;
            int original_or = interval.fixed_or;
            for (int index : interval.variables)
                original_or |= a[positions[index]];
            const int cost = 32 * popcount(static_cast<unsigned>(original_or ^ target)) +
                             static_cast<int>(interval.variables.size());
            ranked_intervals.push_back({cost,interval_index});
            if (cost < best_cost) {
                best_cost = cost;
                best_interval = interval_index;
            }
        }
        sort(ranked_intervals.begin(),ranked_intervals.end());
        vector<uint8_t> retained(intervals.size(),top_witnesses==0);
        if(top_witnesses>0)
            for(int i=0;i<min<int>(top_witnesses,ranked_intervals.size());++i)
                retained[ranked_intervals[i].second]=1;
        for (int interval_index = 0;
             interval_index < static_cast<int>(intervals.size());
             ++interval_index) {
            const Interval& interval = intervals[interval_index];
            if(!retained[interval_index])continue;
            if (interval.fixed_or & ~target) continue;
            const int missing_bits = target & ~interval.fixed_or;
            if (missing_bits && interval.variables.empty()) continue;
            const int select = variable();
            const bool preferred = interval_index == best_interval;
            preferred_phase[select] = preferred ? 1 : -1;
            solver.phase(preferred ? select : -select);
            witnesses.push_back(select);
            ++selector_count;
            for (int bit = 0; bit < k; ++bit) {
                if (!(target & (1 << bit))) {
                    for (int index : interval.variables)
                        clause({-select, -x[index][bit]});
                } else if (!(interval.fixed_or & (1 << bit))) {
                    vector<int> cover{-select};
                    for (int index : interval.variables) cover.push_back(x[index][bit]);
                    clause(cover);
                }
            }
        }
        if (witnesses.empty()) {
            cerr << "UNSAT structurally target=" << target << '\n';
            return 1;
        }
        clause(witnesses);
    }
    cerr << "positions=" << positions.size()
         << " constrained_targets=" << constrained_targets
         << " selectors=" << selector_count
         << " variables=" << variable_count << '\n';

    if (dimacs_path) {
        ofstream dimacs(dimacs_path);
        dimacs << "p cnf " << variable_count << ' ' << stored_clauses.size() << '\n';
        for (const vector<int>& values : stored_clauses) {
            for (int value : values) {
                const int transformed = preferred_phase[abs(value)] > 0
                    ? value : -value;
                dimacs << transformed << ' ';
            }
            dimacs << "0\n";
        }
        cerr << "DIMACS " << dimacs_path << " clauses=" << stored_clauses.size() << '\n';
        return 0;
    }

    if (solver.solve() != 10) {
        cerr << "UNSAT\n";
        return 1;
    }
    for (int i = 0; i < static_cast<int>(positions.size()); ++i) {
        int value = 0;
        for (int bit = 0; bit < k; ++bit)
            if (solver.val(x[i][bit]) > 0) value |= 1 << bit;
        a[positions[i]] = value;
    }
    cerr << "SAT\n";
    for (int value : a) cout << value << ' ';
    cout << '\n';
}
