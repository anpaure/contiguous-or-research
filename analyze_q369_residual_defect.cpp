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
constexpr int N = 465;
constexpr int SIGMA = 369;

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
        if (argc != 3) {
            cerr << "usage: analyze_q369_residual_defect ROW FACTOR\n";
            return 2;
        }
        const vector<Mask> row = read_masks(argv[1], M);
        const vector<Mask> factor = read_masks(argv[2], N);
        array<Mask, N> envelope;
        envelope.fill(static_cast<Mask>(LIMIT - 1));
        for (int i = 0; i < M; ++i) {
            const int right = i + (i < SIGMA ? 2 : 3);
            for (int p = i; p <= right; ++p) envelope[p] &= row[i];
        }
        for (int i = 0; i < M; ++i) {
            Mask value = 0;
            const int right = i + (i < SIGMA ? 2 : 3);
            for (int p = i; p <= right; ++p) value |= factor[p];
            if (value != row[i])
                throw runtime_error("central mismatch at row " + to_string(i + 1));
        }

        array<int, LIMIT> count{};
        array<vector<pair<int, int>>, LIMIT> occurrences;
        auto add = [&](int left, int right) {
            Mask value = 0;
            for (int p = left; p <= right; ++p) value |= factor[p];
            ++count[value];
            occurrences[value].push_back({left, right});
        };
        for (int p = 0; p < N; ++p) add(p, p);
        for (int p = 0; p + 1 < N; ++p) add(p, p + 1);
        for (int p = SIGMA; p + 2 < N; ++p) add(p, p + 2);

        int missing = 0, excess = 0;
        array<int, K + 1> cells_by_rank{}, excess_by_rank{};
        cout << "missing";
        for (int mask = 1; mask < LIMIT; ++mask) {
            if (pc(static_cast<Mask>(mask)) <= 5 && !count[mask]) {
                ++missing;
                cout << ' ' << mask << "(r" << pc(static_cast<Mask>(mask)) << ')';
            }
        }
        cout << '\n';
        cout << "excess";
        for (int mask = 0; mask < LIMIT; ++mask) {
            const int wanted = mask && pc(static_cast<Mask>(mask)) <= 5 ? 1 : 0;
            if (count[mask] > wanted) {
                const int amount = count[mask] - wanted;
                excess += amount;
                excess_by_rank[pc(static_cast<Mask>(mask))] += amount;
                cout << ' ' << mask << "(r" << pc(static_cast<Mask>(mask))
                     << ",x" << amount << ",at";
                for (const auto [left, right] : occurrences[mask]) {
                    Mask maximum = 0, forced = 0;
                    for (int p = left; p <= right; ++p) maximum |= envelope[p];
                    for (int i = 0; i < M; ++i) {
                        const int central_right = i + (i < SIGMA ? 2 : 3);
                        for (int bit = 0; bit < K; ++bit) {
                            if (!(row[i] & (1u << bit))) continue;
                            bool has_legal = false, all_inside = true;
                            for (int p = i; p <= central_right; ++p) {
                                if (!(envelope[p] & (1u << bit))) continue;
                                has_legal = true;
                                if (p < left || p > right) all_inside = false;
                            }
                            if (has_legal && all_inside) forced |= static_cast<Mask>(1u << bit);
                        }
                    }
                    cout << '[' << left + 1 << ',' << right + 1 << ']'
                         << "{max=" << static_cast<int>(maximum)
                         << ",forced=" << static_cast<int>(forced) << '}';
                }
                cout << ')';
            }
            cells_by_rank[pc(static_cast<Mask>(mask))] += count[mask];
        }
        cout << '\n';
        cout << "summary missing=" << missing << " excess=" << excess
             << " cells=1023\ncell_ranks";
        for (int rank = 0; rank <= K; ++rank)
            if (cells_by_rank[rank]) cout << ' ' << rank << ':' << cells_by_rank[rank];
        cout << "\nexcess_ranks";
        for (int rank = 0; rank <= K; ++rank)
            if (excess_by_rank[rank]) cout << ' ' << rank << ':' << excess_by_rank[rank];
        cout << '\n';
        return missing == excess ? 0 : 1;
    } catch (const exception& error) {
        cerr << "error: " << error.what() << '\n';
        return 2;
    }
}
