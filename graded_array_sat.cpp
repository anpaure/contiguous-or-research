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
#include <fstream>
#include <iostream>
#include <numeric>
#include <random>
#include <stdexcept>
#include <vector>

using namespace std;

class Encoding {
    CaDiCaL::Solver solver;
    int variables = 0;
    int k, n, middle, middle_count, slack, central_length, maximum_length;
    vector<vector<int>> x;
    // window[length][left][bit], for the only lengths used by the model.
    vector<vector<vector<int>>> window;

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
    static int binomial(int n, int r) {
        if (r < 0 || r > n) return 0;
        r = min(r, n - r);
        int result = 1;
        for (int i = 1; i <= r; ++i) result = result * (n - r + i) / i;
        return result;
    }

    template<class Emit>
    static void combinations(const vector<int>& values, int choose, Emit emit) {
        if (choose < 0 || choose > static_cast<int>(values.size())) return;
        vector<int> selected;
        auto recurse = [&] (auto&& self, int next) -> void {
            if (static_cast<int>(selected.size()) == choose) {
                emit(selected);
                return;
            }
            const int needed = choose - selected.size();
            for (int i = next; i + needed <= static_cast<int>(values.size()); ++i) {
                selected.push_back(values[i]);
                self(self, i + 1);
                selected.pop_back();
            }
        };
        recurse(recurse, 0);
    }

    void weight_between(const vector<int>& bits, int minimum, int maximum) {
        // At most maximum: every maximum+1 variables cannot all be true.
        combinations(bits, maximum + 1, [&] (const vector<int>& subset) {
            vector<int> clause;
            for (int value : subset) clause.push_back(-value);
            add(clause);
        });
        // At least minimum: every k-minimum+1 variables cannot all be false.
        combinations(bits, static_cast<int>(bits.size()) - minimum + 1,
            [&] (const vector<int>& subset) { add(subset); });
    }

public:
    Encoding(int bits, int length, int seed, vector<int> phase_seed = {})
        : k(bits), n(length), middle((bits + 1) / 2),
          middle_count(binomial(bits, (bits + 1) / 2)),
          slack(length - middle_count), central_length(slack + 1),
          maximum_length(slack + 1 + bits - (bits + 1) / 2),
          x(n, vector<int>(k)), window(maximum_length + 1) {
        if (slack < 1 || maximum_length > n)
            throw invalid_argument("length is outside the graded-model range");
        solver.set("quiet", 1);
        solver.set("seed", seed);
        // Some CaDiCaL builds enable strict external-variable checking and
        // require the complete user-variable range to be declared before the
        // first clause.  The supported k<=11 structured models use fewer
        // than three million variables.
        solver.declare_more_variables(4000000);
        for (auto& row : x) for (int& value : row) value = var();
        if (phase_seed.size() == static_cast<size_t>(n + 1))
            phase_seed.erase(phase_seed.begin() + seed % phase_seed.size());
        if (phase_seed.size() == static_cast<size_t>(n))
            for (int position = 0; position < n; ++position)
                for (int bit = 0; bit < k; ++bit)
                    solver.phase(phase_seed[position] & (1 << bit)
                        ? x[position][bit] : -x[position][bit]);
        for (const auto& row : x) add(row);  // nonzero entries

        vector<int> lengths;
        for (int length_used = 1; length_used <= slack; ++length_used)
            lengths.push_back(length_used);
        for (int rank = middle; rank <= k; ++rank)
            lengths.push_back(central_length + rank - middle);
        sort(lengths.begin(), lengths.end());
        lengths.erase(unique(lengths.begin(), lengths.end()), lengths.end());
        for (int length_used : lengths) {
            window[length_used].assign(n - length_used + 1, vector<int>(k));
            for (int left = 0; left + length_used <= n; ++left) {
                for (int bit = 0; bit < k; ++bit) {
                    const int out = var();
                    window[length_used][left][bit] = out;
                    vector<int> reverse{-out};
                    for (int p = left; p < left + length_used; ++p) {
                        add({-x[p][bit], out});
                        reverse.push_back(x[p][bit]);
                    }
                    add(reverse);
                }
            }
        }

        const bool structured_central =
            (6 <= k && k <= 10) || (k == 11 && n == 465);
        if (structured_central) {
            // This is a deliberately structured sufficient ansatz.  Its
            // central row T=D^slack A is the complete middle layer, and T is
            // a Johnson-graph path.  The supported exact-bound targets are
            // (k,n,d)=(10,254,2),(10,255,3),(11,465,3).
            //
            // Bit-label symmetry normalizes the first adjacent central pair.
            const int first_central = (1 << middle) - 1;
            const int second_central =
                (first_central ^ (1 << (middle - 1))) | (1 << middle);
            for (int bit = 0; bit < k; ++bit) {
                add({(first_central & (1 << bit))
                    ? window[central_length][0][bit]
                    : -window[central_length][0][bit]});
                add({(second_central & (1 << bit))
                    ? window[central_length][1][bit]
                    : -window[central_length][1][bit]});
            }

            for (const vector<int>& bits : window[central_length])
                weight_between(bits, middle, middle);

            // Consecutive central sets differ by one exchange, so their union
            // (an A-window one position longer) has rank exactly six.
            for (const vector<int>& bits : window[central_length + 1])
                weight_between(bits, middle + 1, middle + 1);

            // A union of q+1 consecutive central sets contains an adjacent
            // union (rank >=6) and has rank at most 5+q.
            for (int length_used = central_length + 2;
                 length_used <= maximum_length; ++length_used) {
                const int maximum_weight = min(
                    k, middle + length_used - central_length);
                for (const vector<int>& bits : window[length_used]) {
                    weight_between(bits, middle + 1, maximum_weight);
                }
            }
        }

        vector<vector<vector<int>>> by_interval(maximum_length + 1);
        for (int length_used : lengths)
            by_interval[length_used].resize(n - length_used + 1);

        vector<int> targets((1 << k) - 1);
        iota(targets.begin(), targets.end(), 1);
        mt19937_64 rng(static_cast<uint64_t>(seed) * 0x9e3779b97f4a7c15ULL);
        shuffle(targets.begin(), targets.end(), rng);
        for (int target : targets) {
            const int rank = popcount(static_cast<unsigned>(target));
            vector<int> allowed_lengths;
            if (rank == 1) allowed_lengths = {1};
            else if (rank < middle) {
                if (structured_central) {
                    // Strict two-sided grading.  For a Johnson central path,
                    // the maximal factor has internal row-q rank
                    // middle-slack+q.  Seek each lower target in its natural
                    // row (smaller ranks can all be literal entries here).
                    const int bottom_rank = middle - slack;
                    allowed_lengths = {
                        rank <= bottom_rank ? 1 : rank - bottom_rank + 1
                    };
                } else {
                    for (int length_used = 1; length_used <= slack; ++length_used)
                        allowed_lengths.push_back(length_used);
                }
            }
            else allowed_lengths = {central_length + rank - middle};
            vector<int> witnesses;
            for (int length_used : allowed_lengths) {
                for (int left = 0; left + length_used <= n; ++left) {
                    const int select = var();
                    witnesses.push_back(select);
                    by_interval[length_used][left].push_back(select);
                    for (int bit = 0; bit < k; ++bit) {
                        const int value = window[length_used][left][bit];
                        add({-select, target & (1 << bit) ? value : -value});
                    }
                }
            }
            exactly_one(witnesses);
        }
        for (int length_used : lengths) {
            for (const vector<int>& witnesses : by_interval[length_used])
                at_most_one(witnesses);
        }

        // There are n-central_length+1=C(k,middle) central windows and the
        // same number of middle-layer targets, hence this row is bijective.
        for (const vector<int>& witnesses : by_interval[central_length])
            add(witnesses);

        cerr << "middle=" << middle << " slack=" << slack
             << " central_length=" << central_length
             << " variables=" << variables << '\n';
    }

    bool solve() { return solver.solve() == 10; }
    vector<int> model() {
        vector<int> result(n);
        for (int position = 0; position < n; ++position)
            for (int bit = 0; bit < k; ++bit)
                if (solver.val(x[position][bit]) > 0) result[position] |= 1 << bit;
        return result;
    }
};

int main(int argc, char** argv) {
    const int k = argc > 1 ? stoi(argv[1]) : 10;
    const int n = argc > 2 ? stoi(argv[2]) : 254;
    const int seed = argc > 3 ? stoi(argv[3]) : 1;
    vector<int> phase_seed;
    if (argc > 4) {
        ifstream input(argv[4]);
        for (int value; input >> value;) phase_seed.push_back(value);
    }
    Encoding encoding(k, n, seed, move(phase_seed));
    if (!encoding.solve()) {
        cerr << "UNSAT\n";
        return 1;
    }
    cerr << "SAT\n";
    for (int value : encoding.model()) cout << value << ' ';
    cout << '\n';
}
