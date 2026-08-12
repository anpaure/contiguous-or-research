#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

using namespace std;

namespace q369_projection_cnf {
using Mask = uint16_t;
constexpr int K = 11;
constexpr int LIMIT = 1 << K;
constexpr int M = 462;
constexpr int N = 465;
constexpr int SIGMA = 369;
constexpr int LOWER_CELLS = 1023;

struct Interval { int left, right; };

struct Cnf {
    int variables = 0;
    vector<vector<int>> clauses;

    int variable() { return ++variables; }
    void add(vector<int> clause) { clauses.push_back(move(clause)); }
    template<class... Ints>
    void add(Ints... literals) { clauses.push_back({static_cast<int>(literals)...}); }

    void at_most_one(const vector<int>& xs) {
        if (xs.size() <= 1) return;
        vector<int> prefix(xs.size() - 1);
        for (int& value : prefix) value = variable();
        add(-xs[0], prefix[0]);
        for (int i = 1; i + 1 < static_cast<int>(xs.size()); ++i) {
            add(-xs[i], prefix[i]);
            add(-prefix[i - 1], prefix[i]);
            add(-xs[i], -prefix[i - 1]);
        }
        add(-xs.back(), -prefix.back());
    }

    void exactly_one(const vector<int>& xs) {
        if (xs.empty()) add();
        else add(xs);
        at_most_one(xs);
    }

    // Monotone unary counter: no more than k inputs may be true.
    void at_most_k(const vector<int>& xs, int k) {
        if (k < 0) throw invalid_argument("negative cardinality");
        if (k >= static_cast<int>(xs.size())) return;
        if (k == 0) {
            for (int x : xs) add(-x);
            return;
        }
        vector<int> previous;
        for (int x : xs) {
            vector<int> current(k);
            for (int& value : current) value = variable();
            add(-x, current[0]);
            for (int j = 0; j < static_cast<int>(previous.size()); ++j)
                add(-previous[j], current[j]);
            for (int j = 0; j + 1 < static_cast<int>(previous.size()) && j + 1 < k; ++j)
                add(-x, -previous[j], current[j + 1]);
            if (static_cast<int>(previous.size()) == k)
                add(-x, -previous[k - 1]);
            previous.swap(current);
        }
    }

    void write(const string& path) const {
        ofstream output(path);
        if (!output) throw runtime_error("cannot open output CNF");
        output << "p cnf " << variables << ' ' << clauses.size() << '\n';
        for (const auto& clause : clauses) {
            for (int literal : clause) output << literal << ' ';
            output << "0\n";
        }
    }
};

static vector<Mask> read_row(const string& path) {
    ifstream input(path);
    if (!input) throw runtime_error("cannot open " + path);
    vector<unsigned> raw;
    for (unsigned value; input >> value;) raw.push_back(value);
    if (!input.eof()) throw runtime_error("invalid row token");
    if (raw.size() == M + 1 && raw.front() == M) raw.erase(raw.begin());
    if (raw.size() != M) throw runtime_error("row must contain 462 masks");
    array<uint8_t, LIMIT> seen{};
    vector<Mask> row;
    for (unsigned value : raw) {
        const Mask mask = static_cast<Mask>(value);
        if (value >= LIMIT || popcount(static_cast<unsigned>(mask)) != 6 ||
            ++seen[mask] != 1)
            throw runtime_error("row is not a rank-six permutation");
        row.push_back(mask);
    }
    return row;
}

static vector<Interval> lower_cells() {
    vector<Interval> result;
    for (int p = 0; p < N; ++p) result.push_back({p, p});
    for (int p = 0; p + 1 < N; ++p) result.push_back({p, p + 1});
    for (int p = SIGMA; p + 2 < N; ++p) result.push_back({p, p + 2});
    if (result.size() != LOWER_CELLS) throw runtime_error("bad lower-cell count");
    return result;
}
}  // namespace q369_projection_cnf

int main(int argc, char** argv) {
    using namespace q369_projection_cnf;
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    try {
        if (argc < 4) {
            cerr << "usage: k11_q369_projection_cnf ROW OUTPUT BIT BIT [BIT ...]\n";
            return 2;
        }
        const auto row = read_row(argv[1]);
        vector<int> bits;
        array<uint8_t, K> used{};
        Mask selected_bits = 0;
        for (int arg = 3; arg < argc; ++arg) {
            const int bit = stoi(argv[arg]);
            if (bit < 0 || bit >= K || used[bit]++)
                throw runtime_error("bits must be distinct values in 0..10");
            bits.push_back(bit);
            selected_bits |= static_cast<Mask>(1u << bit);
        }
        const int h = bits.size();
        if (h < 1 || h > 11) throw runtime_error("one through eleven bits supported");
        const int patterns = 1 << h;

        // Exact multiplicity of each projected pattern among all nonempty
        // masks of full rank at most five.
        vector<int> capacity(patterns);
        for (int full = 1; full < LIMIT; ++full) {
            if (popcount(static_cast<unsigned>(full)) > 5) continue;
            int projected = 0;
            for (int track = 0; track < h; ++track)
                if (full & (1 << bits[track])) projected |= 1 << track;
            ++capacity[projected];
        }
        int capacity_sum = 0;
        for (int value : capacity) capacity_sum += value;
        if (capacity_sum != LOWER_CELLS) throw runtime_error("bad projected capacities");

        Cnf cnf;
        vector<vector<int>> x(N, vector<int>(h));
        for (auto& position : x)
            for (int& variable : position) variable = cnf.variable();

        // Exact projected central OR equations.
        for (int i = 0; i < M; ++i) {
            const int right = i + (i < SIGMA ? 2 : 3);
            for (int track = 0; track < h; ++track) {
                if (row[i] & (1u << bits[track])) {
                    vector<int> clause;
                    for (int p = i; p <= right; ++p) clause.push_back(x[p][track]);
                    cnf.add(move(clause));
                } else {
                    for (int p = i; p <= right; ++p) cnf.add(-x[p][track]);
                }
            }
        }

        // Each residual short cell chooses its exact projected OR pattern.
        // Pattern upper capacities sum to the number of cells, so exact-one
        // per cell plus at-most-capacity per pattern forces every capacity to
        // equality without a second family of lower-bound counters.
        const auto cells = lower_cells();
        vector<vector<int>> by_pattern(patterns);
        long long selectors = 0;
        for (const Interval cell : cells) {
            vector<int> choices;
            Mask possible_full = 0;
            for (int i = max(0, cell.left - 3); i <= min(M - 1, cell.right); ++i) {
                const int central_right = i + (i < SIGMA ? 2 : 3);
                if (i <= cell.right && cell.left <= central_right)
                    possible_full |= row[i];
            }
            int possible = 0;
            for (int track = 0; track < h; ++track)
                if (possible_full & (1u << bits[track])) possible |= 1 << track;

            for (int pattern = 0; pattern < patterns; ++pattern) {
                if (!capacity[pattern] || (pattern & ~possible)) continue;
                const int selector = cnf.variable();
                ++selectors;
                choices.push_back(selector);
                by_pattern[pattern].push_back(selector);
                for (int track = 0; track < h; ++track) {
                    if (pattern & (1 << track)) {
                        vector<int> clause{-selector};
                        for (int p = cell.left; p <= cell.right; ++p)
                            clause.push_back(x[p][track]);
                        cnf.add(move(clause));
                    } else {
                        for (int p = cell.left; p <= cell.right; ++p)
                            cnf.add(-selector, -x[p][track]);
                    }
                }
            }
            cnf.exactly_one(choices);
        }
        for (int pattern = 0; pattern < patterns; ++pattern)
            cnf.at_most_k(by_pattern[pattern], capacity[pattern]);

        cnf.write(argv[2]);
        cerr << "bits=" << h << " factor_variables=" << N * h
             << " selectors=" << selectors
             << " variables=" << cnf.variables
             << " clauses=" << cnf.clauses.size() << '\n';
        return 0;
    } catch (const exception& error) {
        cerr << "error: " << error.what() << '\n';
        return 2;
    }
}
