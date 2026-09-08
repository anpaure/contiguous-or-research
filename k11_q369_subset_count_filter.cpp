#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <array>
#include <bit>
#include <bitset>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

using namespace std;

namespace q369_count {

using Mask = uint16_t;
constexpr int K = 11;
constexpr int LIMIT = 1 << K;
constexpr int FULL = LIMIT - 1;
constexpr int M = 462;
constexpr int N = 465;
constexpr int SIGMA = 369;
constexpr int LOWER_CELLS = 1023;

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
            throw runtime_error("row is not a permutation of the rank-six layer");
        row.push_back(static_cast<Mask>(value));
    }
    return row;
}

static array<Mask, N> envelopes(const vector<Mask>& row) {
    array<Mask, N> result;
    result.fill(static_cast<Mask>(FULL));
    for (int i = 0; i < M; ++i)
        for (int p = CENTRAL[i].left; p <= CENTRAL[i].right; ++p)
            result[p] &= row[i];
    return result;
}

static int choose(int n, int r) {
    if (r < 0 || r > n) return 0;
    int value = 1;
    for (int i = 1; i <= r; ++i) value = value * (n - r + i) / i;
    return value;
}

// The 1023 noncentral short cells enumerate all nonempty masks of ranks <=5.
// If |[11]\\B|=c, exactly sum_{s=1}^5 C(c,s) of those masks avoid B.
static int required_zero_cells(Mask subset) {
    const int complement = K - pc(subset);
    int result = 0;
    for (int rank = 1; rank <= 5; ++rank) result += choose(complement, rank);
    return result;
}

struct Result {
    bool feasible = false;
    int required = 0;
    int nearest = -1;
    int distance = LOWER_CELLS + 1;
};

// Relax the factor to y_p=1 iff A_p meets B.  Every real factor induces such
// a binary word.  The prescribed central ORs give exact length-3/4 window OR
// constraints, and saturation gives an exact count of zero noncentral cells.
static Result test_subset(const vector<Mask>& row,
                          const array<Mask, N>& envelope,
                          Mask subset) {
    array<bitset<LOWER_CELLS + 1>, 8> current{}, next{};
    current[0].set(0);

    for (int p = 0; p < N; ++p) {
        for (auto& values : next) values.reset();
        for (int state = 0; state < 8; ++state) {
            if (current[state].none()) continue;
            for (int value = 0; value <= 1; ++value) {
                if (value && !(envelope[p] & subset)) continue;
                const int new_state = ((state << 1) | value) & 7;

                bool valid = true;
                if (p >= 2 && p - 2 <= 368) {
                    const int central = p - 2;
                    const bool wanted = (row[central] & subset) != 0;
                    valid = (new_state != 0) == wanted;
                }
                if (valid && p >= 372) {
                    const int central = p - 3;
                    const bool wanted = (row[central] & subset) != 0;
                    valid = ((state != 0) || value) == wanted;
                }
                if (!valid) continue;

                int added = 0;
                if (!value) {
                    ++added;  // singleton [p,p]
                    if (p >= 1 && !(state & 1)) ++added;  // pair
                    if (p >= 371 && !(state & 3)) ++added;  // late triple
                }
                next[new_state] |= current[state] << added;
            }
        }
        current.swap(next);
    }

    Result result;
    result.required = required_zero_cells(subset);
    for (int state = 0; state < 8; ++state)
        if (current[state].test(result.required)) result.feasible = true;
    if (result.feasible) {
        result.nearest = result.required;
        result.distance = 0;
        return result;
    }
    for (int count = 0; count <= LOWER_CELLS; ++count) {
        bool reachable = false;
        for (int state = 0; state < 8; ++state)
            reachable |= current[state].test(count);
        if (!reachable) continue;
        const int distance = abs(count - result.required);
        if (distance < result.distance) {
            result.distance = distance;
            result.nearest = count;
        }
    }
    return result;
}

}  // namespace q369_count

int main(int argc, char** argv) {
    using namespace q369_count;
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    try {
        if (argc != 2) {
            cerr << "usage: k11_q369_subset_count_filter ROW\n";
            return 2;
        }
        const vector<Mask> row = read_row(argv[1]);
        const auto envelope = envelopes(row);
        int failed = 0, total_distance = 0, maximum_distance = 0;
        array<int, K + 1> failed_by_size{};
        for (int raw = 1; raw < LIMIT; ++raw) {
            const Mask subset = static_cast<Mask>(raw);
            const Result result = test_subset(row, envelope, subset);
            if (result.feasible) continue;
            ++failed;
            ++failed_by_size[pc(subset)];
            total_distance += result.distance;
            maximum_distance = max(maximum_distance, result.distance);
            cout << "FAIL subset=" << raw << " size=" << pc(subset)
                 << " required=" << result.required
                 << " nearest=" << result.nearest
                 << " distance=" << result.distance << '\n';
        }
        cerr << "subsets=2047 failed=" << failed
             << " total_distance=" << total_distance
             << " maximum_distance=" << maximum_distance
             << " failed_by_size";
        for (int size = 1; size <= K; ++size)
            if (failed_by_size[size]) cerr << ' ' << size << ':' << failed_by_size[size];
        cerr << '\n';
        return failed ? 1 : 0;
    } catch (const exception& error) {
        cerr << "error: " << error.what() << '\n';
        return 2;
    }
}
