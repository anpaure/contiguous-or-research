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
#include <set>
#include <stdexcept>
#include <string>
#include <vector>

using namespace std;

namespace {

using Mask = uint16_t;
constexpr int K = 11;
constexpr int LIMIT = 1 << K;
constexpr int FULL = LIMIT - 1;
constexpr int M = 462;
constexpr int SIGMA = 369;
constexpr int N = 465;
constexpr int BULK = 1011;

struct Interval { int left, right; };
struct Core { int first, last; Interval physical; };

int pc(Mask x) { return popcount(static_cast<unsigned>(x)); }

vector<Mask> read_vector(ifstream& input) {
    int length = -1;
    if (!(input >> length) || length < 0) throw runtime_error("invalid vector length");
    vector<Mask> result(length);
    for (int i = 0; i < length; ++i) {
        int value = -1;
        if (!(input >> value) || value < 0 || value >= LIMIT)
            throw runtime_error("invalid/truncated vector value");
        result[i] = static_cast<Mask>(value);
    }
    return result;
}

Mask range_or(const vector<Mask>& values, Interval interval) {
    Mask result = 0;
    for (int i = interval.left; i <= interval.right; ++i) result |= values[i];
    return result;
}

[[noreturn]] void fail(const string& message) { throw runtime_error(message); }

}  // namespace

int main(int argc, char** argv) {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    try {
        if (argc != 2) {
            cerr << "usage: k11_boundary_reservoir_verify CERTIFICATE\n";
            return 2;
        }
        ifstream input(argv[1]);
        if (!input) fail("cannot open certificate");
        const vector<Mask> row = read_vector(input);
        const vector<Mask> labels = read_vector(input);
        const vector<Mask> values = read_vector(input);
        string trailing;
        if (input >> trailing) fail("trailing certificate data");
        if (row.size() != M || labels.size() != 12 || values.size() != N)
            fail("wrong certificate dimensions");

        array<Interval, M> central{};
        vector<Core> cores;
        for (int i = 0; i < M; ++i) {
            central[i] = {i, i + (i < SIGMA ? 2 : 3)};
            for (int q = i + 1; q <= min(M - 1, central[i].right); ++q)
                cores.push_back({i, q, {q, central[i].right}});
        }
        if (cores.size() != BULK) fail("internal core count");
        const array<Interval, 12> reservoir{
            Interval{0, 0}, Interval{0, 1}, Interval{1, 1},
            Interval{369, 371}, Interval{370, 371}, Interval{371, 371},
            Interval{462, 462}, Interval{462, 463}, Interval{462, 464},
            Interval{463, 463}, Interval{463, 464}, Interval{464, 464},
        };

        array<uint8_t, LIMIT> row_seen{};
        for (Mask value : row) {
            if (!value || pc(value) != 6) fail("row is not rank six");
            if (++row_seen[value] != 1) fail("duplicate row value");
        }
        for (int value = 1; value < LIMIT; ++value)
            if (pc(static_cast<Mask>(value)) == 6 && !row_seen[value])
                fail("missing rank-six row value");

        for (int bit = 0; bit < K; ++bit) {
            const Mask flag = static_cast<Mask>(1u << bit);
            int i = 0;
            while (i < M) {
                if (!(row[i] & flag)) { ++i; continue; }
                const int first = i;
                while (i < M && (row[i] & flag)) ++i;
                if (first == 0 || i == M) continue;
                const int required = first <= 369 ? 3 : 4;
                if (i - first < required) fail("mixed run condition failed");
            }
        }

        vector<Mask> meet_values;
        meet_values.reserve(BULK);
        array<uint8_t, LIMIT> meet_seen{};
        for (const Core& core : cores) {
            Mask value = static_cast<Mask>(FULL);
            for (int i = core.first; i <= core.last; ++i) value &= row[i];
            if (!value || pc(value) > 5) fail("invalid bulk meet");
            if (meet_seen[value]) fail("bulk meet collision");
            meet_seen[value] = 1;
            meet_values.push_back(value);
        }

        vector<Mask> missing;
        for (int value = 1; value < LIMIT; ++value) {
            Mask mask = static_cast<Mask>(value);
            if (pc(mask) <= 5 && !meet_seen[mask]) missing.push_back(mask);
        }
        if (missing.size() != 12) fail("lower complement is not twelve masks");
        vector<Mask> sorted_labels = labels;
        sort(sorted_labels.begin(), sorted_labels.end());
        if (adjacent_find(sorted_labels.begin(), sorted_labels.end()) != sorted_labels.end())
            fail("duplicate reservoir label");
        vector<Mask> sorted_missing = missing;
        sort(sorted_missing.begin(), sorted_missing.end());
        if (sorted_labels != sorted_missing) fail("reservoir labels are not lower complement");

        array<Mask, N> expected;
        expected.fill(static_cast<Mask>(FULL));
        for (int i = 0; i < M; ++i)
            for (int j = central[i].left; j <= central[i].right; ++j)
                expected[j] &= row[i];
        for (int a = 0; a < 12; ++a)
            for (int j = reservoir[a].left; j <= reservoir[a].right; ++j)
                expected[j] &= labels[a];
        for (int j = 0; j < N; ++j) {
            if (!values[j]) fail("zero array entry");
            if (values[j] != expected[j]) fail("array differs from maximal legal reconstruction");
        }

        for (int i = 0; i < M; ++i)
            if (range_or(values, central[i]) != row[i]) fail("central witness mismatch");
        for (int e = 0; e < BULK; ++e)
            if (range_or(values, cores[e].physical) != meet_values[e])
                fail("bulk witness mismatch");
        for (int a = 0; a < 12; ++a)
            if (range_or(values, reservoir[a]) != labels[a])
                fail("reservoir witness mismatch");

        array<uint8_t, LIMIT> row_unions{};
        vector<Mask> previous, current;
        for (Mask x : row) {
            current.clear();
            current.push_back(x);
            for (Mask old : previous) current.push_back(static_cast<Mask>(old | x));
            sort(current.begin(), current.end());
            current.erase(unique(current.begin(), current.end()), current.end());
            for (Mask value : current) row_unions[value] = 1;
            previous.swap(current);
        }
        for (int value = 1; value < LIMIT; ++value)
            if (pc(static_cast<Mask>(value)) >= 7 && !row_unions[value])
                fail("missing upper central-row union");

        array<uint8_t, LIMIT> exhaustive{}, suffix{};
        long long interval_count = 0;
        for (int left = 0; left < N; ++left) {
            Mask value = 0;
            for (int right = left; right < N; ++right) {
                value |= values[right];
                exhaustive[value] = 1;
                ++interval_count;
            }
        }
        previous.clear();
        for (Mask x : values) {
            current.clear();
            current.push_back(x);
            for (Mask old : previous) current.push_back(static_cast<Mask>(old | x));
            sort(current.begin(), current.end());
            current.erase(unique(current.begin(), current.end()), current.end());
            for (Mask value : current) suffix[value] = 1;
            previous.swap(current);
        }
        int covered = 0;
        for (int value = 1; value < LIMIT; ++value) {
            if (!exhaustive[value] || !suffix[value] || exhaustive[value] != suffix[value])
                fail("coverage failure at mask " + to_string(value));
            ++covered;
        }
        if (interval_count != 108345) fail("wrong interval count");
        cout << "PASS k=11 nonzero_length=465 row=462 bulk=1011 reservoir=12"
             << " covered=" << covered << "/2047 intervals=" << interval_count << '\n';
        return 0;
    } catch (const exception& e) {
        cerr << "FAIL " << e.what() << '\n';
        return 1;
    }
}
