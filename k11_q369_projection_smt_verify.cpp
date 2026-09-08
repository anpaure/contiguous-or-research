#include <array>
#include <bit>
#include <cctype>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

using namespace std;

namespace q369_projection_smt_verify {
using Mask = uint16_t;
constexpr int K = 11;
constexpr int LIMIT = 1 << K;
constexpr int M = 462;
constexpr int N = 465;
constexpr int SIGMA = 369;

struct Interval { int left, right; };

static vector<Mask> read_row(const string& path) {
    ifstream input(path);
    if (!input) throw runtime_error("cannot open row " + path);
    vector<unsigned> raw;
    for (unsigned value; input >> value;) raw.push_back(value);
    if (!input.eof()) throw runtime_error("invalid row token");
    if (raw.size() == M + 1 && raw.front() == M) raw.erase(raw.begin());
    if (raw.size() != M) throw runtime_error("row must contain 462 masks");
    array<uint8_t, LIMIT> seen{};
    vector<Mask> row;
    row.reserve(M);
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
    result.reserve(1023);
    for (int p = 0; p < N; ++p) result.push_back({p, p});
    for (int p = 0; p + 1 < N; ++p) result.push_back({p, p + 1});
    for (int p = SIGMA; p + 2 < N; ++p) result.push_back({p, p + 2});
    if (result.size() != 1023) throw runtime_error("bad lower-cell count");
    return result;
}

static pair<int, int> parse_name(const string& name) {
    if (name.empty() || name[0] != 'x') throw runtime_error("bad model symbol " + name);
    const size_t separator = name.find('_', 1);
    if (separator == string::npos || separator + 1 == name.size())
        throw runtime_error("bad model symbol " + name);
    for (size_t i = 1; i < separator; ++i)
        if (!isdigit(static_cast<unsigned char>(name[i])))
            throw runtime_error("bad model symbol " + name);
    for (size_t i = separator + 1; i < name.size(); ++i)
        if (!isdigit(static_cast<unsigned char>(name[i])))
            throw runtime_error("bad model symbol " + name);
    return {stoi(name.substr(1, separator - 1)), stoi(name.substr(separator + 1))};
}

static vector<int> read_model(const string& path, int h) {
    ifstream input(path);
    if (!input) throw runtime_error("cannot open solver output " + path);
    string contents((istreambuf_iterator<char>(input)), istreambuf_iterator<char>());
    for (char& c : contents)
        if (c == '(' || c == ')') c = ' ';

    vector<string> tokens;
    string token;
    for (char c : contents) {
        if (isspace(static_cast<unsigned char>(c))) {
            if (!token.empty()) {
                tokens.push_back(token);
                token.clear();
            }
        } else {
            token += c;
        }
    }
    if (!token.empty()) tokens.push_back(token);

    bool sat = false;
    vector<int8_t> assignment(h * N, -1);
    for (size_t i = 0; i < tokens.size(); ++i) {
        if (tokens[i] == "sat") {
            sat = true;
            continue;
        }
        if (tokens[i].empty() || tokens[i][0] != 'x') continue;
        if (i + 1 == tokens.size() || (tokens[i + 1] != "true" && tokens[i + 1] != "false"))
            throw runtime_error("missing Boolean value after " + tokens[i]);
        const auto [track, position] = parse_name(tokens[i]);
        if (track < 0 || track >= h || position < 0 || position >= N)
            throw runtime_error("out-of-range model symbol " + tokens[i]);
        const int index = track * N + position;
        const int8_t value = tokens[++i] == "true" ? 1 : 0;
        if (assignment[index] != -1 && assignment[index] != value)
            throw runtime_error("inconsistent duplicate model symbol");
        assignment[index] = value;
    }
    if (!sat) throw runtime_error("solver output does not contain sat");
    vector<int> factor(N);
    for (int track = 0; track < h; ++track) {
        for (int p = 0; p < N; ++p) {
            const int8_t value = assignment[track * N + p];
            if (value == -1) throw runtime_error("solver output omits a factor variable");
            if (value) factor[p] |= 1 << track;
        }
    }
    return factor;
}

static void verify(const vector<Mask>& row, const vector<int>& bits,
                   const vector<int>& factor) {
    const int h = bits.size();
    if (factor.size() != N) throw runtime_error("factor must have 465 entries");
    for (int value : factor)
        if (value < 0 || value >= (1 << h)) throw runtime_error("factor entry out of range");

    for (int i = 0; i < M; ++i) {
        int wanted = 0, actual = 0;
        for (int track = 0; track < h; ++track)
            if (row[i] & (1u << bits[track])) wanted |= 1 << track;
        const int right = i + (i < SIGMA ? 2 : 3);
        for (int p = i; p <= right; ++p) actual |= factor[p];
        if (actual != wanted)
            throw runtime_error("central projection mismatch at index " + to_string(i));
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
}
}  // namespace q369_projection_smt_verify

int main(int argc, char** argv) {
    using namespace q369_projection_smt_verify;
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    try {
        if (argc < 4) {
            cerr << "usage: k11_q369_projection_smt_verify ROW Z3_OUTPUT "
                    "[--write FACTOR] BIT [BIT ...]\n";
            return 2;
        }
        const auto row = read_row(argv[1]);
        int first_bit = 3;
        string factor_output;
        if (string(argv[first_bit]) == "--write") {
            if (argc < 6) throw runtime_error("--write requires an output and bits");
            factor_output = argv[first_bit + 1];
            first_bit += 2;
        }
        vector<int> bits;
        array<uint8_t, K> used{};
        for (int arg = first_bit; arg < argc; ++arg) {
            const int bit = stoi(argv[arg]);
            if (bit < 0 || bit >= K || used[bit]++)
                throw runtime_error("bits must be distinct values in 0..10");
            bits.push_back(bit);
        }
        if (bits.empty() || bits.size() > K)
            throw runtime_error("one through eleven projected bits supported");

        const vector<int> factor = read_model(argv[2], bits.size());
        verify(row, bits, factor);
        if (!factor_output.empty()) {
            ofstream output(factor_output);
            if (!output) throw runtime_error("cannot open factor output");
            for (int p = 0; p < N; ++p)
                output << factor[p] << (p + 1 == N ? '\n' : ' ');
        }
        cout << "PASS bits=" << bits.size() << " cells=1023\n";
        return 0;
    } catch (const exception& error) {
        cerr << "error: " << error.what() << '\n';
        return 2;
    }
}
