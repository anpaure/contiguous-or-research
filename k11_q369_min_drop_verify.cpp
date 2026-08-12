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

using Mask = uint16_t;
constexpr int K = 11;
constexpr int LIMIT = 1 << K;
constexpr int M = 462;
constexpr int SIGMA = 369;
constexpr int N = 465;

static int pc(Mask value) {
    return popcount(static_cast<unsigned>(value));
}

static vector<Mask> read_masks(const string& path, int wanted) {
    ifstream input(path);
    if (!input) throw runtime_error("cannot open " + path);
    vector<long long> raw;
    for (long long value; input >> value;) raw.push_back(value);
    if (!input.eof()) throw runtime_error("invalid token in " + path);
    if (raw.size() == static_cast<size_t>(wanted + 1) && raw.front() == wanted)
        raw.erase(raw.begin());
    if (raw.size() != static_cast<size_t>(wanted))
        throw runtime_error(path + " must contain " + to_string(wanted) + " masks");
    vector<Mask> result;
    for (long long value : raw) {
        if (value <= 0 || value >= LIMIT) throw runtime_error("mask out of range");
        result.push_back(static_cast<Mask>(value));
    }
    return result;
}

int main(int argc, char** argv) {
    try {
        if (argc < 3) {
            cerr << "usage: k11_q369_min_drop_verify ROW FACTOR [EXPECTED_MISSING ...]\n";
            return 2;
        }
        const vector<Mask> row = read_masks(argv[1], M);
        const vector<Mask> factor = read_masks(argv[2], N);

        array<uint8_t, LIMIT> row_count{};
        for (Mask mask : row) {
            if (pc(mask) != 6 || ++row_count[mask] != 1)
                throw runtime_error("row is not a rank-six permutation");
        }
        for (int mask = 1; mask < LIMIT; ++mask)
            if (pc(static_cast<Mask>(mask)) == 6 && row_count[mask] != 1)
                throw runtime_error("row omits a rank-six mask");

        for (int i = 0; i < M; ++i) {
            Mask value = 0;
            const int right = i + (i < SIGMA ? 2 : 3);
            for (int p = i; p <= right; ++p) value |= factor[p];
            if (value != row[i])
                throw runtime_error("central mismatch at row " + to_string(i + 1));
        }

        array<uint8_t, LIMIT> covered{};
        vector<Mask> suffixes, next;
        for (Mask entry : factor) {
            next.clear();
            next.push_back(entry);
            for (Mask old : suffixes) next.push_back(static_cast<Mask>(old | entry));
            sort(next.begin(), next.end());
            next.erase(unique(next.begin(), next.end()), next.end());
            for (Mask value : next) covered[value] = 1;
            suffixes.swap(next);
        }

        vector<Mask> missing;
        for (int mask = 1; mask < LIMIT; ++mask)
            if (pc(static_cast<Mask>(mask)) <= 5 && !covered[mask])
                missing.push_back(static_cast<Mask>(mask));

        vector<Mask> expected;
        for (int i = 3; i < argc; ++i) {
            const long long value = stoll(argv[i]);
            if (value <= 0 || value >= LIMIT)
                throw runtime_error("expected missing mask out of range");
            expected.push_back(static_cast<Mask>(value));
        }
        sort(expected.begin(), expected.end());
        expected.erase(unique(expected.begin(), expected.end()), expected.end());
        if (missing != expected) {
            cerr << "actual_missing";
            for (Mask mask : missing) cerr << ' ' << static_cast<int>(mask);
            cerr << '\n';
            throw runtime_error("missing-mask list differs from expectation");
        }

        int upper_missing = 0;
        for (int mask = 1; mask < LIMIT; ++mask)
            if (pc(static_cast<Mask>(mask)) >= 7 && !covered[mask]) ++upper_missing;
        cout << "PASS q369 central=462 lower_missing=" << missing.size()
             << " upper_missing=" << upper_missing << " masks";
        for (Mask mask : missing) cout << ' ' << static_cast<int>(mask);
        cout << '\n';
        return 0;
    } catch (const exception& error) {
        cerr << "error: " << error.what() << '\n';
        return 1;
    }
}
