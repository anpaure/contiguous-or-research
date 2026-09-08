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
#include <iostream>
#include <vector>
using namespace std;

static int choose(int n, int r) {
    if (r < 0 || r > n) return 0;
    r = min(r, n - r);
    int64_t result = 1;
    for (int i = 1; i <= r; ++i) result = result * (n - r + i) / i;
    return static_cast<int>(result);
}

// Rank-slack lower bound from the interval-antichain argument.
static int lower_bound_length(int k) {
    int answer = 0;
    for (int r = 1; r <= k; ++r) {
        const int middle_count = choose(k, r);
        int lower_count = 0;
        for (int s = 1; s < r; ++s) lower_count += choose(k, s);
        int slack = 0;
        while (slack * middle_count + slack * (slack + 1) / 2 < lower_count)
            ++slack;
        answer = max(answer, middle_count + slack);
    }
    return answer;
}

// Every target of this rank has a witness no longer than this in any
// length-n solution.  This is the same interval-antichain argument, now used
// as a sound SAT pruning rule.
static int maximum_witness_length(int k, int n, int rank) {
    int result = n - choose(k, rank) + 1;
    for (int higher = rank + 1; higher <= k; ++higher)
        result = min(result, n - choose(k, higher));
    return result;
}

static bool verify(int k, const vector<int>& a) {
    vector<uint8_t> seen(1 << k);
    vector<int> previous, current;
    for (int x : a) {
        current.clear();
        current.push_back(x);
        for (int old : previous) {
            const int value = old | x;
            if (value != current.back()) current.push_back(value);
        }
        for (int value : current) seen[value] = 1;
        previous.swap(current);
    }
    return all_of(seen.begin() + 1, seen.end(), [](uint8_t x) { return x; });
}

static vector<int> solve_length(int k, int n) {
    const int masks = 1 << k;
    int selector_count = 0;
    for (int target = 1; target < masks; ++target) {
        const int rank = popcount(static_cast<unsigned>(target));
        const int maximum = maximum_witness_length(k, n, rank);
        if (maximum < 1) return {};
        selector_count += maximum * (n + 1) - maximum * (maximum + 1) / 2;
    }

    CaDiCaL::Solver sat;
    sat.set("quiet", 1);
    sat.set("seed", 1);
    const int entry_variables = n * k;
    const int singleton_variables = n * k;
    sat.declare_more_variables(entry_variables + singleton_variables + selector_count);
    int next_variable = entry_variables + singleton_variables;
    auto x = [k](int position, int bit) { return position * k + bit + 1; };
    auto singleton = [=](int position, int bit) {
        return entry_variables + position * k + bit + 1;
    };
    auto add = [&](const vector<int>& clause) {
        for (int literal : clause) sat.add(literal);
        sat.add(0);
    };

    // A shortest nonzero construction can be taken to have no zero entries.
    for (int position = 0; position < n; ++position) {
        vector<int> clause;
        for (int bit = 0; bit < k; ++bit) clause.push_back(x(position, bit));
        add(clause);
    }

    // Break the k! bit-renaming symmetry by ordering the first literal
    // singleton occurrences 1,2,4,... .
    for (int bit = 0; bit < k; ++bit) {
        vector<int> occurs;
        for (int position = 0; position < n; ++position) {
            const int flag = singleton(position, bit);
            occurs.push_back(flag);
            add({-flag, x(position, bit)});
            vector<int> reverse{flag, -x(position, bit)};
            for (int other = 0; other < k; ++other) if (other != bit) {
                add({-flag, -x(position, other)});
                reverse.push_back(x(position, other));
            }
            add(reverse);
            if (bit) {
                vector<int> ordered{-flag};
                for (int earlier = 0; earlier < position; ++earlier)
                    ordered.push_back(singleton(earlier, bit - 1));
                add(ordered);
            }
        }
        add(occurs);
    }

    // For each nonzero target S, choose an interval and state directly that
    // every bit of S occurs there and no bit outside S occurs there.
    for (int target = 1; target < masks; ++target) {
        const int rank = popcount(static_cast<unsigned>(target));
        const int maximum = maximum_witness_length(k, n, rank);
        vector<int> witnesses;
        for (int length = 1; length <= maximum; ++length) {
            for (int left = 0; left + length <= n; ++left) {
                const int select = ++next_variable;
                witnesses.push_back(select);
                for (int bit = 0; bit < k; ++bit) {
                    if (target & (1 << bit)) {
                        vector<int> clause{-select};
                        for (int p = left; p < left + length; ++p)
                            clause.push_back(x(p, bit));
                        add(clause);
                    } else {
                        for (int p = left; p < left + length; ++p)
                            add({-select, -x(p, bit)});
                    }
                }
            }
        }
        add(witnesses);
    }

    cerr << "k=" << k << " n=" << n << " variables=" << next_variable << '\n';
    if (sat.solve() != 10) return {};
    vector<int> answer(n);
    for (int position = 0; position < n; ++position)
        for (int bit = 0; bit < k; ++bit)
            if (sat.val(x(position, bit)) > 0) answer[position] |= 1 << bit;
    return answer;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int k;
    if (!(cin >> k) || k < 0 || k > 10) return 2;
    if (!k) {
        cout << "1\n0\n";
        return 0;
    }
    for (int n = lower_bound_length(k);; ++n) {
        vector<int> answer = solve_length(k, n);
        if (answer.empty()) continue;
        if (!verify(k, answer)) return 3;
        cout << answer.size() + 1 << "\n0";
        for (int x : answer) cout << ' ' << x;
        cout << '\n';
        return 0;
    }
}
