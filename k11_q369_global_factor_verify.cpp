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

namespace {
using Mask = uint16_t;
constexpr int K = 11;
constexpr int LIMIT = 1 << K;
constexpr int M = 462;
constexpr int SIGMA = 369;
constexpr int N = 465;

struct Interval { int left, right; };

int pc(Mask value) { return popcount(static_cast<unsigned>(value)); }

vector<Mask> read_values(const string& path, int wanted) {
    ifstream input(path);
    if (!input) throw runtime_error("cannot open " + path);
    vector<long long> raw;
    for (long long value; input >> value;) raw.push_back(value);
    if (!input.eof()) throw runtime_error("invalid token in " + path);
    if (raw.size() == static_cast<size_t>(wanted + 1) && raw.front() == wanted)
        raw.erase(raw.begin());
    if (raw.size() != static_cast<size_t>(wanted))
        throw runtime_error(path + " must contain " + to_string(wanted) + " values");
    vector<Mask> result;
    for (long long value : raw) {
        if (value < 0 || value >= LIMIT) throw runtime_error("mask out of range");
        result.push_back(static_cast<Mask>(value));
    }
    return result;
}

Mask range_or(const vector<Mask>& values, Interval interval) {
    Mask result = 0;
    for (int p = interval.left; p <= interval.right; ++p) result |= values[p];
    return result;
}

[[noreturn]] void fail(const string& message) { throw runtime_error(message); }
}  // namespace

int main(int argc, char** argv) {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    try {
        if (argc < 3 || argc > 4) {
            cerr << "usage: k11_q369_global_factor_verify ROW FACTOR [--universal]\n";
            return 2;
        }
        const bool universal = argc == 4 && string(argv[3]) == "--universal";
        if (argc == 4 && !universal) fail("unknown option");
        const vector<Mask> row = read_values(argv[1], M);
        const vector<Mask> factor = read_values(argv[2], N);

        array<uint8_t, LIMIT> row_count{};
        for (Mask value : row) {
            if (pc(value) != 6 || ++row_count[value] != 1)
                fail("row is not a rank-six permutation");
        }
        for (int value = 1; value < LIMIT; ++value)
            if (pc(static_cast<Mask>(value)) == 6 && !row_count[value])
                fail("row omits a rank-six mask");
        for (Mask value : factor)
            if (!value) fail("factor contains zero");

        array<Interval, M> central{};
        for (int i = 0; i < M; ++i) {
            central[i] = {i, i + (i < SIGMA ? 2 : 3)};
            const Mask value = range_or(factor, central[i]);
            if (value != row[i])
                fail("central mismatch at one-based index " + to_string(i + 1));
        }

        array<uint8_t, LIMIT> exhaustive{}, short_seen{}, suffix{};
        long long intervals = 0;
        for (int left = 0; left < N; ++left) {
            Mask value = 0;
            for (int right = left; right < N; ++right) {
                value |= factor[right];
                exhaustive[value] = 1;
                if (right - left + 1 <= 3) short_seen[value] = 1;
                ++intervals;
            }
        }
        if (intervals != 108345) fail("wrong physical interval count");

        vector<Mask> previous, current;
        for (Mask x : factor) {
            current.clear();
            current.push_back(x);
            for (Mask old : previous) current.push_back(static_cast<Mask>(old | x));
            sort(current.begin(), current.end());
            current.erase(unique(current.begin(), current.end()), current.end());
            for (Mask value : current) suffix[value] = 1;
            previous.swap(current);
        }

        int covered = 0, covered_lower = 0, covered_upper = 0;
        array<int, K + 1> missing_by_rank{};
        for (int value = 1; value < LIMIT; ++value) {
            const Mask mask = static_cast<Mask>(value);
            const int rank = pc(mask);
            if (exhaustive[mask] != suffix[mask]) fail("independent verifier disagreement");
            if (exhaustive[mask]) {
                ++covered;
                if (rank <= 5) ++covered_lower;
                if (rank >= 7) ++covered_upper;
            } else {
                ++missing_by_rank[rank];
            }
            if (rank <= 5 && !short_seen[mask])
                fail("missing short lower target " + to_string(value));
            if (universal && !exhaustive[mask])
                fail("missing universal target " + to_string(value));
        }
        if (covered_lower != 1023) fail("lower coverage count mismatch");
        cout << "PASS k=11 q369 factor_length=465 lower=1023/1023"
             << " covered=" << covered << "/2047 upper=" << covered_upper << "/562"
             << " intervals=" << intervals;
        for (int rank = 7; rank <= 11; ++rank)
            cout << " missing_r" << rank << '=' << missing_by_rank[rank];
        cout << " mode=" << (universal ? "universal" : "lower") << '\n';
        return 0;
    } catch (const exception& e) {
        cerr << "FAIL " << e.what() << '\n';
        return 1;
    }
}
