#include <array>
#include <bit>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

using namespace std;

namespace q369_projection {

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

static int pc(Mask value) { return popcount(static_cast<unsigned>(value)); }

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
    for (int p = 0; p < N; ++p) result.push_back({p, p});
    for (int p = 0; p + 1 < N; ++p) result.push_back({p, p + 1});
    for (int p = SIGMA; p + 2 < N; ++p) result.push_back({p, p + 2});
    if (result.size() != 1023) throw runtime_error("bad lower-cell count");
    return result;
}

static int choose(int n, int r) {
    if (r < 0 || r > n) return 0;
    int value = 1;
    for (int i = 1; i <= r; ++i) value = value * (n - r + i) / i;
    return value;
}

static int lower_masks_avoiding(int forbidden_bits) {
    const int available = K - forbidden_bits;
    int result = 0;
    for (int rank = 1; rank <= 5; ++rank) result += choose(available, rank);
    return result;
}

static string variable(int track, int position) {
    return "x" + to_string(track) + "_" + to_string(position);
}

static string or_expression(int track, Interval interval) {
    if (interval.left == interval.right) return variable(track, interval.left);
    string result = "(or";
    for (int p = interval.left; p <= interval.right; ++p)
        result += " " + variable(track, p);
    result += ")";
    return result;
}

}  // namespace q369_projection

int main(int argc, char** argv) {
    using namespace q369_projection;
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    try {
        if (argc < 4) {
            cerr << "usage: k11_q369_multibit_projection_smt ROW OUTPUT "
                    "[--core|--model] BIT [BIT ...]\n";
            return 2;
        }
        const vector<Mask> row = read_row(argv[1]);
        int first_bit = 3;
        bool core = false, model = false;
        while (first_bit < argc && string(argv[first_bit]).rfind("--", 0) == 0) {
            const string option = argv[first_bit++];
            if (option == "--core") core = true;
            else if (option == "--model") model = true;
            else throw runtime_error("unknown option " + option);
        }
        if (core && model) throw runtime_error("--core and --model are mutually exclusive");
        vector<int> bits;
        array<uint8_t, K> used{};
        for (int arg = first_bit; arg < argc; ++arg) {
            const int bit = stoi(argv[arg]);
            if (bit < 0 || bit >= K || used[bit]++)
                throw runtime_error("bits must be distinct values in 0..10");
            bits.push_back(bit);
        }
        if (bits.empty() || bits.size() > 11)
            throw runtime_error("one through eleven projected bits supported");

        ofstream output(argv[2]);
        if (!output) throw runtime_error("cannot open output");
        output << "(set-logic QF_LIA)\n";
        if (core) output << "(set-option :produce-unsat-cores true)\n"
                         << "(set-option :smt.core.minimize true)\n";
        for (int track = 0; track < static_cast<int>(bits.size()); ++track)
            for (int p = 0; p < N; ++p)
                output << "(declare-fun " << variable(track, p) << " () Bool)\n";

        for (int track = 0; track < static_cast<int>(bits.size()); ++track) {
            const Mask flag = static_cast<Mask>(1u << bits[track]);
            for (int i = 0; i < M; ++i) {
                const string value = or_expression(track, CENTRAL[i]);
                output << "(assert " << ((row[i] & flag) ? value : "(not " + value + ")")
                       << ")\n";
            }
        }

        const vector<Interval> cells = lower_cells();
        const int sublimit = 1 << bits.size();
        for (int subset = 1; subset < sublimit; ++subset) {
            output << "(assert ";
            if (core) output << "(! ";
            output << "(= (+";
            for (Interval interval : cells) {
                output << " (ite (and";
                for (int track = 0; track < static_cast<int>(bits.size()); ++track)
                    if (subset & (1 << track))
                        output << " (not " << or_expression(track, interval) << ")";
                output << ") 1 0)";
            }
            output << ") " << lower_masks_avoiding(popcount(static_cast<unsigned>(subset)))
                   << ")";
            if (core) output << " :named c" << subset << ")";
            output << ")\n";
        }
        output << "(check-sat)\n";
        if (core) output << "(get-unsat-core)\n";
        if (model) {
            output << "(get-value (";
            for (int track = 0; track < static_cast<int>(bits.size()); ++track)
                for (int p = 0; p < N; ++p)
                    output << ' ' << variable(track, p);
            output << "))\n";
        }
        return 0;
    } catch (const exception& error) {
        cerr << "error: " << error.what() << '\n';
        return 2;
    }
}
