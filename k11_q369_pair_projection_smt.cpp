#include <array>
#include <bit>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

using namespace std;

namespace q369_pair {

using Mask = uint16_t;
constexpr int K = 11;
constexpr int LIMIT = 1 << K;
constexpr int M = 462;
constexpr int N = 465;
constexpr int SIGMA = 369;

struct Interval { int left, right; };

static array<Interval, M> make_central() {
    array<Interval, M> result{};
    for (int i = 0; i < M; ++i)
        result[i] = {i, i + (i < SIGMA ? 2 : 3)};
    return result;
}

static const array<Interval, M> CENTRAL = make_central();

static int pc(Mask value) {
    return popcount(static_cast<unsigned>(value));
}

static vector<Mask> read_row(const string& path) {
    ifstream input(path);
    if (!input) throw runtime_error("cannot open " + path);
    vector<unsigned> raw;
    for (unsigned value; input >> value;) raw.push_back(value);
    if (!input.eof()) throw runtime_error("invalid token in " + path);
    if (raw.size() == M + 1 && raw.front() == M) raw.erase(raw.begin());
    if (raw.size() != M) throw runtime_error("row must contain 462 masks");
    array<uint8_t, LIMIT> seen{};
    vector<Mask> row;
    row.reserve(M);
    for (unsigned value : raw) {
        if (value >= LIMIT || pc(static_cast<Mask>(value)) != 6 ||
            ++seen[value] != 1)
            throw runtime_error("row is not a rank-six permutation");
        row.push_back(static_cast<Mask>(value));
    }
    return row;
}

static vector<Interval> lower_cells() {
    vector<Interval> result;
    result.reserve(1023);
    for (int p = 0; p < N; ++p) result.push_back({p, p});
    for (int p = 0; p + 1 < N; ++p) result.push_back({p, p + 1});
    for (int p = SIGMA; p + 2 < N; ++p) result.push_back({p, p + 2});
    if (result.size() != 1023) throw runtime_error("bad lower-cell count");
    return result;
}

static string or_expression(char prefix, Interval interval) {
    if (interval.left == interval.right)
        return string(1, prefix) + to_string(interval.left);
    string result = "(or";
    for (int p = interval.left; p <= interval.right; ++p)
        result += " " + string(1, prefix) + to_string(p);
    result += ")";
    return result;
}

static void emit_track_constraints(ostream& output, char prefix,
                                   int bit, const vector<Mask>& row) {
    const Mask flag = static_cast<Mask>(1u << bit);
    for (int i = 0; i < M; ++i) {
        const string value = or_expression(prefix, CENTRAL[i]);
        if (row[i] & flag) output << "(assert " << value << ")\n";
        else output << "(assert (not " << value << "))\n";
    }
}

static void emit_sum(ostream& output, const vector<string>& terms, int wanted) {
    output << "(assert (= (+";
    for (const string& term : terms) output << " (ite " << term << " 1 0)";
    output << ") " << wanted << "))\n";
}

}  // namespace q369_pair

int main(int argc, char** argv) {
    using namespace q369_pair;
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    try {
        if (argc != 5) {
            cerr << "usage: k11_q369_pair_projection_smt ROW BIT_A BIT_B OUTPUT\n";
            return 2;
        }
        const vector<Mask> row = read_row(argv[1]);
        const int bit_a = stoi(argv[2]), bit_b = stoi(argv[3]);
        if (bit_a < 0 || bit_a >= K || bit_b < 0 || bit_b >= K || bit_a == bit_b)
            throw runtime_error("bits must be distinct values in 0..10");
        ofstream output(argv[4]);
        if (!output) throw runtime_error("cannot open output");
        output << "(set-logic QF_LIA)\n";
        for (int p = 0; p < N; ++p)
            output << "(declare-fun x" << p << " () Bool)\n"
                   << "(declare-fun y" << p << " () Bool)\n";
        emit_track_constraints(output, 'x', bit_a, row);
        emit_track_constraints(output, 'y', bit_b, row);

        vector<string> zero_a, zero_b, zero_both;
        for (Interval interval : lower_cells()) {
            const string a = "(not " + or_expression('x', interval) + ")";
            const string b = "(not " + or_expression('y', interval) + ")";
            zero_a.push_back(a);
            zero_b.push_back(b);
            zero_both.push_back("(and " + a + " " + b + ")");
        }
        // The lower masks have pair-intersection histogram
        // (none, only-a, only-b, both)=(381,256,256,130).
        emit_sum(output, zero_a, 637);
        emit_sum(output, zero_b, 637);
        emit_sum(output, zero_both, 381);
        output << "(check-sat)\n";
        return 0;
    } catch (const exception& error) {
        cerr << "error: " << error.what() << '\n';
        return 2;
    }
}
