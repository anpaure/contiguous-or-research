#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <cadical.hpp>

#include <algorithm>
#include <bit>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <vector>
using namespace std;

int main(int argc, char** argv) {
    if (argc < 4 || argc > 5) {
        cerr << "usage: pinnable_factor_sat K D OUTPUT_ARRAY [SEED_FACTOR] "
                "< CENTRAL_ROW\n";
        return 2;
    }
    const int k = stoi(argv[1]), d = stoi(argv[2]);
    const int limit = 1 << k, full = limit - 1;
    vector<int> central;
    for (int x; cin >> x;) central.push_back(x);
    if (central.empty()) return 3;
    const int rank = popcount(static_cast<unsigned>(central.front()));
    for (int x : central)
        if (popcount(static_cast<unsigned>(x)) != rank) return 4;
    const int m = central.size(), n = m + d;
    vector<int> seed_factor;
    if (argc == 5) {
        ifstream seed_input(argv[4]);
        for (int value; seed_input >> value;) seed_factor.push_back(value);
        if (seed_factor.size() != static_cast<size_t>(n)) return 10;
    }
    vector<int> envelope(n, full);
    for (int position = 0; position < n; ++position)
        for (int i = max(0, position - d); i <= min(m - 1, position); ++i)
            envelope[position] &= central[i];

    CaDiCaL::Solver solver;
    solver.set("quiet", 1);
    solver.set("seed", k * 1009 + d * 9176);
    int variables = n * k;
    solver.declare_more_variables(2000000);
    long long clauses = 0, selectors = 0;
    const bool core_mode = getenv("PIN_CORE") != nullptr;
    vector<int> target_assumption(limit);
    auto x = [&](int position, int bit) { return position * k + bit + 1; };
    auto clause = [&](const vector<int>& values) {
        for (int literal : values) solver.add(literal);
        solver.add(0);
        ++clauses;
    };
    auto variable = [&]() { return ++variables; };

    // Envelope exclusions, nonzero factor labels, and exact central coverage.
    for (int position = 0; position < n; ++position) {
        vector<int> nonzero;
        for (int bit = 0; bit < k; ++bit) {
            if (envelope[position] & (1 << bit)) {
                nonzero.push_back(x(position, bit));
                solver.phase(seed_factor.empty() ||
                             (seed_factor[position] & (1 << bit))
                                 ? x(position, bit) : -x(position, bit));
            } else clause({-x(position, bit)});
        }
        if (nonzero.empty()) {
            cerr << "empty envelope position=" << position << '\n';
            return 5;
        }
        clause(nonzero);
    }
    for (int i = 0; i < m; ++i)
        for (int bit = 0; bit < k; ++bit) if (central[i] & (1 << bit)) {
            vector<int> hit;
            for (int position = i; position <= i + d; ++position)
                if (envelope[position] & (1 << bit))
                    hit.push_back(x(position, bit));
            clause(hit);
        }

    // Enumerate only envelope-compatible short witnesses.  Inverting the
    // enumeration (interval first, then submasks of its small envelope union)
    // reduces k=14 from about 44 million selectors to a few hundred thousand.
    vector<vector<int>> target_witnesses(limit);
    for (int length = 1; length <= d; ++length)
        for (int left = 0; left + length <= n; ++left) {
            int union_envelope = 0;
            for (int p = left; p < left + length; ++p)
                union_envelope |= envelope[p];
            for (int target = union_envelope; target;
                 target = (target - 1) & union_envelope) {
                if (popcount(static_cast<unsigned>(target)) >= rank) continue;
                bool every_label_can_be_nonzero = true;
                for (int p = left; p < left + length; ++p)
                    every_label_can_be_nonzero &= (target & envelope[p]) != 0;
                if (!every_label_can_be_nonzero) continue;
                const int select = variable();
                ++selectors;
                solver.phase(-select);
                target_witnesses[target].push_back(select);
                for (int p = left; p < left + length; ++p) {
                    int forbidden = envelope[p] & ~target;
                    while (forbidden) {
                        const int bit = countr_zero(static_cast<unsigned>(forbidden));
                        clause({-select, -x(p, bit)});
                        forbidden &= forbidden - 1;
                    }
                }
                int required = target;
                while (required) {
                    const int bit = countr_zero(static_cast<unsigned>(required));
                    vector<int> hit{-select};
                    for (int p = left; p < left + length; ++p)
                        if (envelope[p] & (1 << bit)) hit.push_back(x(p, bit));
                    clause(hit);
                    required &= required - 1;
                }
            }
        }
    for (int target = 1; target < limit; ++target)
        if (popcount(static_cast<unsigned>(target)) < rank) {
            if (target_witnesses[target].empty()) {
                cerr << "no witness candidate target=" << target << '\n';
                return 6;
            }
            if (core_mode) {
                target_assumption[target] = variable();
                vector<int> gated{-target_assumption[target]};
                gated.insert(gated.end(), target_witnesses[target].begin(),
                             target_witnesses[target].end());
                clause(gated);
            } else clause(target_witnesses[target]);
        }

    cerr << "k=" << k << " d=" << d << " central=" << m << " n=" << n
         << " selectors=" << selectors << " variables=" << variables
         << " clauses=" << clauses << '\n';
    if (core_mode)
        for (int target = 1; target < limit; ++target)
            if (target_assumption[target]) solver.assume(target_assumption[target]);
    const int result = solver.solve();
    if (result != 10) {
        cerr << (result == 20 ? "UNSAT" : "UNKNOWN") << '\n';
        if (result == 20 && core_mode) {
            int core_size = 0;
            cerr << "failed_targets";
            for (int target = 1; target < limit; ++target)
                if (target_assumption[target] && solver.failed(target_assumption[target])) {
                    cerr << ' ' << target;
                    ++core_size;
                }
            cerr << "\nfailed_target_count=" << core_size << '\n';
        }
        return result == 20 ? 1 : 7;
    }
    vector<int> factor(n);
    for (int position = 0; position < n; ++position)
        for (int bit = 0; bit < k; ++bit)
            if (solver.val(x(position, bit)) > 0) factor[position] |= 1 << bit;

    // Independent internal audit of the returned factor and all lower masks.
    vector<uint8_t> seen(limit);
    for (int left = 0; left < n; ++left) {
        int value = 0;
        for (int right = left; right < n; ++right) {
            value |= factor[right];
            seen[value] = 1;
            if (right - left + 1 >= d && value == full) break;
        }
    }
    for (int i = 0; i < m; ++i) {
        int value = 0;
        for (int p = i; p <= i + d; ++p) value |= factor[p];
        if (value != central[i]) return 8;
    }
    for (int target = 1; target < limit; ++target)
        if (popcount(static_cast<unsigned>(target)) < rank && !seen[target])
            return 9;

    ofstream out(argv[3]);
    for (int value : factor) out << value << ' ';
    out << '\n';
    int covered = 0;
    for (int x = 1; x < limit; ++x) covered += seen[x];
    cerr << "SAT covered_all_intervals=" << covered << '/' << limit - 1 << '\n';
}
