#include <array>
#include <bit>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

using namespace std;

namespace q369_projection_verify {
using Mask = uint16_t;
constexpr int K = 11;
constexpr int LIMIT = 1 << K;
constexpr int M = 462;
constexpr int N = 465;
constexpr int SIGMA = 369;

struct Interval { int left, right; };

static vector<Mask> read_row(const string& path) {
    ifstream input(path);
    if (!input) throw runtime_error("cannot open row");
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

static vector<uint8_t> read_model(const string& path, int variables) {
    ifstream input(path);
    if (!input) throw runtime_error("cannot open model");
    vector<uint8_t> value(variables + 1);
    string line;
    bool sat = false;
    while (getline(input, line)) {
        if (line.rfind("s SATISFIABLE", 0) == 0) sat = true;
        if (line.empty() || line[0] != 'v') continue;
        istringstream parser(line.substr(1));
        for (int literal; parser >> literal;) {
            if (!literal) continue;
            const int variable = abs(literal);
            if (variable <= variables) value[variable] = literal > 0 ? 2 : 1;
        }
    }
    if (!sat) throw runtime_error("model is not SATISFIABLE output");
    for (int variable = 1; variable <= variables; ++variable)
        if (!value[variable]) throw runtime_error("model omits a factor variable");
    return value;
}

static vector<int> read_factor(const string& path, int h) {
    ifstream input(path);
    if (!input) throw runtime_error("cannot open compact factor");
    vector<int> factor;
    for (int value; input >> value;) factor.push_back(value);
    if (!input.eof()) throw runtime_error("invalid compact-factor token");
    if (factor.size() != N) throw runtime_error("compact factor must have 465 entries");
    for (int value : factor)
        if (value < 0 || value >= (1 << h))
            throw runtime_error("compact-factor entry out of projected range");
    return factor;
}

static vector<Interval> lower_cells() {
    vector<Interval> result;
    for (int p = 0; p < N; ++p) result.push_back({p, p});
    for (int p = 0; p + 1 < N; ++p) result.push_back({p, p + 1});
    for (int p = SIGMA; p + 2 < N; ++p) result.push_back({p, p + 2});
    return result;
}
}  // namespace q369_projection_verify

int main(int argc, char** argv) {
    using namespace q369_projection_verify;
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    try {
        if (argc < 4) {
            cerr << "usage: k11_q369_projection_verify ROW MODEL [--write FACTOR] BIT...\n"
                    "   or: k11_q369_projection_verify ROW --factor FACTOR BIT...\n";
            return 2;
        }
        const auto row = read_row(argv[1]);
        bool compact_mode = string(argv[2]) == "--factor";
        string input_path = compact_mode ? argv[3] : argv[2];
        int first_bit = compact_mode ? 4 : 3;
        string factor_output;
        if (!compact_mode && string(argv[3]) == "--write") {
            if (argc < 6) throw runtime_error("--write requires an output and bits");
            factor_output = argv[4];
            first_bit = 5;
        }
        vector<int> bits;
        array<uint8_t, K> used{};
        for (int arg = first_bit; arg < argc; ++arg) {
            const int bit = stoi(argv[arg]);
            if (bit < 0 || bit >= K || used[bit]++)
                throw runtime_error("invalid projected bit list");
            bits.push_back(bit);
        }
        const int h = bits.size();
        if (!h) throw runtime_error("at least one projected bit is required");
        vector<int> factor;
        if (compact_mode) {
            factor = read_factor(input_path, h);
        } else {
            const auto assignment = read_model(input_path, N * h);
            factor.assign(N, 0);
            for (int p = 0; p < N; ++p)
                for (int track = 0; track < h; ++track)
                    if (assignment[p * h + track + 1] == 2) factor[p] |= 1 << track;
        }

        for (int i = 0; i < M; ++i) {
            int wanted = 0, actual = 0;
            for (int track = 0; track < h; ++track)
                if (row[i] & (1u << bits[track])) wanted |= 1 << track;
            const int right = i + (i < SIGMA ? 2 : 3);
            for (int p = i; p <= right; ++p) actual |= factor[p];
            if (actual != wanted) throw runtime_error("central projection mismatch");
        }

        vector<int> wanted(1 << h), actual(1 << h);
        for (int full = 1; full < LIMIT; ++full) {
            if (popcount(static_cast<unsigned>(full)) > 5) continue;
            int projected = 0;
            for (int track = 0; track < h; ++track)
                if (full & (1 << bits[track])) projected |= 1 << track;
            ++wanted[projected];
        }
        for (const Interval cell : lower_cells()) {
            int projected = 0;
            for (int p = cell.left; p <= cell.right; ++p) projected |= factor[p];
            ++actual[projected];
        }
        if (actual != wanted) throw runtime_error("projected lower histogram mismatch");
        if (!factor_output.empty()) {
            ofstream output(factor_output);
            if (!output) throw runtime_error("cannot open factor output");
            for (int p = 0; p < N; ++p)
                output << factor[p] << (p + 1 == N ? '\n' : ' ');
        }
        cout << "PASS bits=" << h << " cells=1023\n";
        return 0;
    } catch (const exception& error) {
        cerr << "error: " << error.what() << '\n';
        return 2;
    }
}
