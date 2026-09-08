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
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

using namespace std;

class Encoding {
    CaDiCaL::Solver solver;
    int variables = 0;
    int k;
    int n;
    int q_rank;
    vector<vector<int>> x;
    vector<vector<int>> qbit;

    int var() { return ++variables; }

    void add(const vector<int>& clause) {
        for (int literal : clause) solver.add(literal);
        solver.add(0);
    }

    void add(initializer_list<int> clause) {
        for (int literal : clause) solver.add(literal);
        solver.add(0);
    }

    void at_most_one(const vector<int>& literals) {
        if (literals.size() <= 1) return;
        vector<int> prefix(literals.size() - 1);
        for (int& value : prefix) value = var();
        add({-literals[0], prefix[0]});
        for (int i = 1; i + 1 < static_cast<int>(literals.size()); ++i) {
            add({-literals[i], prefix[i]});
            add({-prefix[i - 1], prefix[i]});
            add({-literals[i], -prefix[i - 1]});
        }
        add({-literals.back(), -prefix.back()});
    }

    void exactly_one(const vector<int>& literals) {
        add(literals);
        at_most_one(literals);
    }

public:
    Encoding(int bits, int length) : k(bits), n(length), q_rank((bits + 1) / 2),
        x(n, vector<int>(k)), qbit(n - 2, vector<int>(k)) {
        solver.set("quiet", 1);
        for (auto& row : x) for (int& value : row) value = var();
        for (auto& row : qbit) for (int& value : row) value = var();
        for (const auto& row : x) add(row);

        // qbit[i][b] is exactly x[i][b] OR x[i+1][b] OR x[i+2][b].
        for (int i = 0; i + 2 < n; ++i) {
            for (int bit = 0; bit < k; ++bit) {
                const int q = qbit[i][bit];
                add({-x[i][bit], q});
                add({-x[i + 1][bit], q});
                add({-x[i + 2][bit], q});
                add({-q, x[i][bit], x[i + 1][bit], x[i + 2][bit]});
            }
        }

        // There are exactly 2n-1 intervals of lengths one and two, and at the
        // k=9 lower-bound equality n=128 this equals the number of masks below
        // rank five.  Assign every such mask to exactly one short interval and
        // every short interval to exactly one mask.
        vector<vector<int>> by_interval(2 * n - 1);
        int target_count = 0;
        for (int target = 1; target < (1 << k); ++target) {
            if (popcount(static_cast<unsigned>(target)) >= q_rank) continue;
            ++target_count;
            vector<int> witnesses;
            witnesses.reserve(2 * n - 1);
            for (int length = 1; length <= 2; ++length) {
                for (int left = 0; left + length <= n; ++left) {
                    const int select = var();
                    witnesses.push_back(select);
                    const int interval_id = length == 1 ? left : n + left;
                    by_interval[interval_id].push_back(select);
                    for (int bit = 0; bit < k; ++bit) {
                        if (target & (1 << bit)) {
                            vector<int> clause{-select};
                            for (int p = left; p < left + length; ++p)
                                clause.push_back(x[p][bit]);
                            add(clause);
                        } else {
                            for (int p = left; p < left + length; ++p)
                                add({-select, -x[p][bit]});
                        }
                    }
                }
            }
            exactly_one(witnesses);
        }
        const bool perfect_bijection = target_count == 2 * n - 1;
        for (const vector<int>& witnesses : by_interval) {
            if (perfect_bijection) exactly_one(witnesses);
            else at_most_one(witnesses);
        }

        cerr << "base variables=" << variables
             << " candidates use " << (n - 2) * k << " assumptions\n";
    }

    bool solve(const vector<int>& q) {
        if (static_cast<int>(q.size()) != n - 2) return false;
        for (int i = 0; i + 2 < n; ++i) {
            if (q[i] <= 0 || q[i] >= (1 << k) ||
                popcount(static_cast<unsigned>(q[i])) != q_rank) return false;
            for (int bit = 0; bit < k; ++bit)
                solver.assume((q[i] & (1 << bit)) ? qbit[i][bit] : -qbit[i][bit]);
        }
        return solver.solve() == 10;
    }

    vector<int> model() {
        vector<int> result(n);
        for (int i = 0; i < n; ++i)
            for (int bit = 0; bit < k; ++bit)
                if (solver.val(x[i][bit]) > 0) result[i] |= 1 << bit;
        return result;
    }
};

static vector<int> parse_line(const string& line) {
    istringstream input(line);
    vector<int> result;
    int value;
    while (input >> value) result.push_back(value);
    return result;
}

int main(int argc, char** argv) {
    const int k = argc > 1 ? stoi(argv[1]) : 9;
    const int n = argc > 2 ? stoi(argv[2]) : 128;
    Encoding encoding(k, n);
    string line;
    uint64_t tested = 0;
    while (getline(cin, line)) {
        vector<int> q = parse_line(line);
        if (q.empty()) continue;
        ++tested;
        if (encoding.solve(q)) {
            cerr << "SAT after " << tested << " candidates\nQ ";
            for (int value : q) cerr << value << ' ';
            cerr << "\nA ";
            for (int value : encoding.model()) cerr << value << ' ';
            cerr << '\n';
            return 0;
        }
        if (tested % 100 == 0) cerr << "tested=" << tested << '\n';
    }
    cerr << "UNSAT candidates=" << tested << '\n';
    return 1;
}
