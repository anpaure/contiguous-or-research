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
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

using namespace std;

struct Cnf {
    int variables = 0;
    vector<vector<int>> clauses;
    int var() { return ++variables; }
    void add(vector<int> c) { clauses.push_back(move(c)); }
    template<class... T> void add(T... x) { clauses.push_back({static_cast<int>(x)...}); }
    void at_most_one(const vector<int>& xs) {
        if (xs.size() <= 1) return;
        vector<int> s(xs.size() - 1);
        for (int& x : s) x = var();
        add(-xs[0], s[0]);
        for (int i = 1; i + 1 < static_cast<int>(xs.size()); ++i) {
            add(-xs[i], s[i]);
            add(-s[i - 1], s[i]);
            add(-xs[i], -s[i - 1]);
        }
        add(-xs.back(), -s.back());
    }
    void exactly_one(const vector<int>& xs) {
        add(xs);
        at_most_one(xs);
    }
    void write(const string& path) const {
        ofstream out(path);
        out << "p cnf " << variables << ' ' << clauses.size() << '\n';
        for (const auto& c : clauses) {
            for (int x : c) out << x << ' ';
            out << "0\n";
        }
    }
};

struct Encoding {
    int k, n, q_rank;
    Cnf cnf;
    vector<vector<int>> x;

    explicit Encoding(const vector<int>& q, int bits, const string& high_mode)
        : k(bits), n(q.size() + 2), q_rank((bits + 1) / 2),
          x(n, vector<int>(k)) {
        if (q.empty()) throw invalid_argument("Q must be nonempty");
        for (int value : q)
            if (value <= 0 || value >= (1 << k) ||
                popcount(static_cast<unsigned>(value)) != q_rank)
                throw invalid_argument("Q entries have the wrong rank");
        for (auto& row : x) for (int& v : row) v = cnf.var();
        for (int i = 0; i < n; ++i) cnf.add(x[i]);

        // Fix OR(A_i,A_{i+1},A_{i+2})=Q_i directly.
        for (int i = 0; i < static_cast<int>(q.size()); ++i)
            for (int bit = 0; bit < k; ++bit) {
            if (q[i] & (1 << bit))
                cnf.add(x[i][bit], x[i + 1][bit], x[i + 2][bit]);
            else {
                cnf.add(-x[i][bit]);
                cnf.add(-x[i + 1][bit]);
                cnf.add(-x[i + 2][bit]);
            }
        }

        // Q-search has already certified every rank >= q_rank.  Ask SAT for a
        // triple root covering all lower masks in intervals of length at most 2.
        vector<vector<int>> by_short_interval(2 * n - 1);
        int low_target_count = 0;
        for (int target = 1; target < (1 << k); ++target) {
            const int rank = popcount(static_cast<unsigned>(target));
            vector<int> lengths;
            if (rank < q_rank) {
                ++low_target_count;
                if (k == 8) lengths = rank <= 2 ? vector<int>{1} : vector<int>{2};
                else lengths = {1, 2};
            }
            else if (rank >= 6 && high_mode == "full") lengths = {rank - 1};
            else if (rank == 6 && high_mode == "rank6")
                for (int length = 1; length <= 45; ++length) lengths.push_back(length);
            else continue;
            vector<int> witnesses;
            for (int length : lengths) {
                for (int left = 0; left + length <= n; ++left) {
                    const int select = cnf.var();
                    witnesses.push_back(select);
                    if (rank < q_rank && length <= 2)
                        by_short_interval[length == 1 ? left : n + left].push_back(select);
                    for (int bit = 0; bit < k; ++bit) {
                        if (target & (1 << bit)) {
                            vector<int> clause{-select};
                            for (int p = left; p < left + length; ++p)
                                clause.push_back(x[p][bit]);
                            cnf.add(move(clause));
                        } else {
                            for (int p = left; p < left + length; ++p)
                                cnf.add(-select, -x[p][bit]);
                        }
                    }
                }
            }
            cnf.exactly_one(witnesses);
        }

        const bool perfect_short_bijection = low_target_count == 2 * n - 1;
        for (const auto& group : by_short_interval) {
            if (perfect_short_bijection) cnf.exactly_one(group);
            else cnf.at_most_one(group);
        }

        // Q already fixes bit names, so no bit-permutation symmetry breaker is
        // imposed here; a labeled Q-order need not have canonical singleton order.
    }
};

static vector<int> read_values(const string& line) {
    istringstream in(line);
    vector<int> result;
    int x;
    while (in >> x) result.push_back(x);
    return result;
}

int main(int argc, char** argv) {
    if (argc < 3) {
        cerr << "usage: fixed_q_sat generate output.cnf < q-line\n"
             << "   or: fixed_q_sat decode solver.model < q-line\n";
        return 2;
    }
    string line;
    getline(cin, line);
    const string high_mode = argc > 3 ? argv[3] : "low";
    const int k = argc > 4 ? stoi(argv[4]) : 8;
    Encoding encoding(read_values(line), k, high_mode);
    const string mode = argv[1];
    if (mode == "generate") {
        encoding.cnf.write(argv[2]);
        cerr << "variables=" << encoding.cnf.variables
             << " clauses=" << encoding.cnf.clauses.size() << '\n';
        return 0;
    }
    if (mode == "decode") {
        ifstream model(argv[2]);
        vector<uint8_t> truth(encoding.cnf.variables + 1);
        bool sat = false;
        while (getline(model, line)) {
            if (line.rfind("s SATISFIABLE", 0) == 0) sat = true;
            if (line.empty() || line[0] != 'v') continue;
            istringstream values(line.substr(1));
            int literal;
            while (values >> literal)
                if (literal > 0 && literal < static_cast<int>(truth.size())) truth[literal] = 1;
        }
        if (!sat) return 1;
        vector<int> a(encoding.n);
        for (int p = 0; p < encoding.n; ++p)
            for (int bit = 0; bit < encoding.k; ++bit)
                if (truth[encoding.x[p][bit]]) a[p] |= 1 << bit;
        for (int value : a) cout << value << ' ';
        cout << '\n';
        return 0;
    }
    return 2;
}
