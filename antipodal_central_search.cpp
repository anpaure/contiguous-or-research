#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <algorithm>
#include <bit>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <numeric>
#include <random>
#include <vector>

using namespace std;

struct Audit {
    int run_deficit = 0;
    int covered = 0;
    int lower = 0;
    int upper = 0;
    int potential = 0;
    vector<int> by_rank;
};

struct Search {
    int k = 10;
    int rank = 5;
    int d = 2;
    int full = (1 << 10) - 1;
    vector<int> representatives;
    vector<vector<int8_t>> parity;
    mt19937_64 random;
    chrono::steady_clock::time_point deadline;
    string output_path;
    string input_path;

    explicit Search(uint64_t seed, string output, string input)
        : random(seed), output_path(move(output)), input_path(move(input)) {
        for (int x = 0; x <= full; ++x) {
            if (popcount(static_cast<unsigned>(x)) != rank) continue;
            if (x < (full ^ x)) representatives.push_back(x);
        }
        const int n = representatives.size();
        parity.assign(n, vector<int8_t>(n, -1));
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if (popcount(static_cast<unsigned>(representatives[i] ^
                                                   representatives[j])) == 2)
                    parity[i][j] = parity[j][i] = 0;
                else if (popcount(static_cast<unsigned>(representatives[i] ^
                                                        (full ^ representatives[j]))) == 2)
                    parity[i][j] = parity[j][i] = 1;
            }
        }
    }

    bool odd_cycle(const vector<int>& cycle) const {
        int sum = 0;
        for (int i = 0; i < static_cast<int>(cycle.size()); ++i) {
            const int value = parity[cycle[i]][cycle[(i + 1) % cycle.size()]];
            if (value < 0) return false;
            sum ^= value;
        }
        return sum == 1;
    }

    vector<int> expand(const vector<int>& cycle) const {
        const int n = cycle.size();
        vector<int> first(n);
        int orientation = 0;
        first[0] = representatives[cycle[0]];
        for (int i = 1; i < n; ++i) {
            orientation ^= parity[cycle[i - 1]][cycle[i]];
            first[i] = representatives[cycle[i]] ^ (orientation ? full : 0);
        }
        vector<int> path = first;
        for (int value : first) path.push_back(full ^ value);
        return path;
    }

    Audit evaluate_cycle(const vector<int>& cycle) const {
        Audit result;
        result.by_rank.assign(k + 1, 0);
        if (!odd_cycle(cycle)) {
            result.run_deficit = 1000000;
            return result;
        }
        const vector<int> path = expand(cycle);
        for (int bit = 0; bit < k; ++bit) {
            int i = 0;
            while (i < static_cast<int>(path.size())) {
                if (!(path[i] & (1 << bit))) { ++i; continue; }
                const int begin = i;
                while (i < static_cast<int>(path.size()) &&
                       (path[i] & (1 << bit))) ++i;
                if (begin && i < static_cast<int>(path.size()))
                    result.run_deficit += max(0, d + 1 - (i - begin));
            }
        }

        vector<uint8_t> count(1 << k);
        auto record = [&] (int value, int wanted_rank) {
            if (popcount(static_cast<unsigned>(value)) != wanted_rank) return;
            if (!count[value]) {
                ++result.covered;
                ++result.by_rank[wanted_rank];
                if (wanted_rank < rank) ++result.lower;
                if (wanted_rank > rank) ++result.upper;
            }
            if (count[value] != 255) ++count[value];
        };
        for (int value : path) record(value, rank);
        for (int length = 2; length <= d + 1; ++length) {
            for (int left = 0; left + length <= static_cast<int>(path.size()); ++left) {
                int value = full;
                for (int j = left; j < left + length; ++j) value &= path[j];
                record(value, rank - length + 1);
            }
        }
        for (int length = 2; rank + length - 1 <= k; ++length) {
            for (int left = 0; left + length <= static_cast<int>(path.size()); ++left) {
                int value = 0;
                for (int j = left; j < left + length; ++j) value |= path[j];
                record(value, rank + length - 1);
            }
        }
        for (int mask = 1; mask <= full; ++mask) {
            const int mask_rank = popcount(static_cast<unsigned>(mask));
            if (mask_rank < rank - d || mask_rank < 3) continue;
            if (!count[mask]) continue;
            int reward = 1024;
            for (int bonus = 256, occurrence = 1;
                 bonus && occurrence < count[mask]; bonus >>= 1, ++occurrence)
                reward += bonus;
            result.potential += reward;
        }
        return result;
    }

    static long long score(const Audit& value) {
        return -1000000000000LL * value.run_deficit
             + 1000000000LL * value.covered + value.potential;
    }

    void print(const Audit& value) const {
        cerr << "run=" << value.run_deficit << " covered=" << value.covered
             << "/968 lower=" << value.lower << " upper=" << value.upper
             << " potential=" << value.potential << " ranks";
        for (int r = 0; r <= k; ++r)
            if (value.by_rank[r]) cerr << ' ' << r << ':' << value.by_rank[r];
        cerr << '\n';
    }

    void save(const vector<int>& cycle) const {
        ofstream output(output_path);
        for (int value : expand(cycle)) output << value << ' ';
        output << '\n';
    }

    bool make_initial(vector<int>& cycle) {
        const int n = representatives.size();
        vector<int> path{0};
        vector<uint8_t> used(n);
        used[0] = 1;
        vector<int> next_index(n, 0);
        vector<vector<int>> choices(n);
        long long nodes = 0;
        while (!path.empty()) {
            if (++nodes % 2000000 == 0 && chrono::steady_clock::now() >= deadline)
                return false;
            const int depth = path.size();
            if (depth == n) {
                if (odd_cycle(path)) { cycle = path; return true; }
                used[path.back()] = 0;
                path.pop_back();
                continue;
            }
            if (choices[depth].empty()) {
                const int last = path.back();
                for (int candidate = 0; candidate < n; ++candidate)
                    if (!used[candidate] && parity[last][candidate] >= 0)
                        choices[depth].push_back(candidate);
                shuffle(choices[depth].begin(), choices[depth].end(), random);
                stable_sort(choices[depth].begin(), choices[depth].end(),
                    [&] (int a, int b) {
                        int da = 0, db = 0;
                        for (int x = 0; x < n; ++x) if (!used[x]) {
                            da += parity[a][x] >= 0;
                            db += parity[b][x] >= 0;
                        }
                        return da < db;
                    });
                next_index[depth] = 0;
            }
            if (next_index[depth] == static_cast<int>(choices[depth].size())) {
                choices[depth].clear();
                next_index[depth] = 0;
                if (path.size() == 1) break;
                used[path.back()] = 0;
                path.pop_back();
                continue;
            }
            const int candidate = choices[depth][next_index[depth]++];
            if (used[candidate]) continue;
            if (depth + 1 == n && parity[candidate][path[0]] < 0) continue;
            used[candidate] = 1;
            path.push_back(candidate);
        }
        return false;
    }

    bool reverse_move(vector<int>& cycle) {
        const int n = cycle.size();
        for (int attempt = 0; attempt < 300; ++attempt) {
            int left = random() % n;
            int right = random() % n;
            if (left > right) swap(left, right);
            if (right - left < 2 || (left == 0 && right + 1 == n)) continue;
            const int before = cycle[(left + n - 1) % n];
            const int after = cycle[(right + 1) % n];
            if (parity[before][cycle[right]] < 0 ||
                parity[cycle[left]][after] < 0) continue;
            reverse(cycle.begin() + left, cycle.begin() + right + 1);
            if (odd_cycle(cycle)) return true;
            reverse(cycle.begin() + left, cycle.begin() + right + 1);
        }
        return false;
    }

    bool relocate_move(vector<int>& cycle) {
        const int n = cycle.size();
        for (int attempt = 0; attempt < 300; ++attempt) {
            const int length = 1 + random() % 8;
            const int left = random() % (n - length + 1);
            const int right = left + length;
            // Keep the chosen linear cut fixed; cyclic rotations are supplied
            // naturally by later two-opt moves.
            if (left == 0 || right == n) continue;
            if (parity[cycle[left - 1]][cycle[right]] < 0) continue;
            vector<int> block(cycle.begin() + left, cycle.begin() + right);
            vector<int> reduced;
            reduced.reserve(n - length);
            reduced.insert(reduced.end(), cycle.begin(), cycle.begin() + left);
            reduced.insert(reduced.end(), cycle.begin() + right, cycle.end());
            if (random() & 1) reverse(block.begin(), block.end());
            for (int gap_attempt = 0; gap_attempt < 100; ++gap_attempt) {
                const int gap = 1 + random() % (reduced.size() - 1);
                if (gap == left) continue;
                if (parity[reduced[gap - 1]][block.front()] < 0 ||
                    parity[block.back()][reduced[gap]] < 0) continue;
                vector<int> candidate = reduced;
                candidate.insert(candidate.begin() + gap, block.begin(), block.end());
                if (!odd_cycle(candidate)) continue;
                cycle.swap(candidate);
                return true;
            }
        }
        return false;
    }

    bool mutate(vector<int>& cycle) {
        const int type = random() % 100;
        if (type < 55) return reverse_move(cycle);
        if (type < 90) return relocate_move(cycle);
        const int shift = 1 + random() % (cycle.size() - 1);
        rotate(cycle.begin(), cycle.begin() + shift, cycle.end());
        return true;
    }

    void run(double seconds) {
        deadline = chrono::steady_clock::now() +
            chrono::milliseconds(static_cast<long long>(seconds * 1000));
        vector<int> cycle;
        if (!input_path.empty()) {
            ifstream input(input_path);
            vector<int> path;
            for (int value; input >> value;) path.push_back(value);
            if (path.size() == 252) {
                vector<int> index(1 << k, -1);
                for (int i = 0; i < static_cast<int>(representatives.size()); ++i)
                    index[representatives[i]] = i;
                vector<uint8_t> used(representatives.size());
                for (int i = 0; i < 126; ++i) {
                    const int representative = min(path[i], full ^ path[i]);
                    const int q = index[representative];
                    if (q < 0 || used[q]) { cycle.clear(); break; }
                    used[q] = 1;
                    cycle.push_back(q);
                }
                if (cycle.size() != 126 || !odd_cycle(cycle)) cycle.clear();
            }
        }
        if (cycle.empty() && !make_initial(cycle)) {
            cerr << "failed to find an odd quotient Hamilton cycle\n";
            return;
        }
        Audit current = evaluate_cycle(cycle);
        Audit best = current;
        vector<int> best_cycle = cycle;
        print(best);
        save(best_cycle);
        uniform_real_distribution<double> uniform(0.0, 1.0);
        long long iteration = 0;
        while (chrono::steady_clock::now() < deadline) {
            vector<int> candidate = cycle;
            if (!mutate(candidate)) continue;
            Audit next = evaluate_cycle(candidate);
            const long long current_score = score(current);
            const long long next_score = score(next);
            const double phase = (iteration++ % 10000) / 10000.0;
            const double temperature = 5e10 * pow(1e-6, phase) + 1.0;
            if (next_score >= current_score ||
                uniform(random) < exp((next_score - current_score) / temperature)) {
                cycle.swap(candidate);
                current = move(next);
            }
            if (score(current) > score(best)) {
                best = current;
                best_cycle = cycle;
                print(best);
                save(best_cycle);
                if (!best.run_deficit && best.covered == 968) break;
            }
        }
        save(best_cycle);
    }
};

int main(int argc, char** argv) {
    const double seconds = argc > 1 ? stod(argv[1]) : 60.0;
    const uint64_t seed = argc > 2 ? stoull(argv[2]) : 1;
    const string output = argc > 3 ? argv[3] : "antipodal_central.txt";
    const string input = argc > 4 ? argv[4] : "";
    Search search(seed, output, input);
    search.run(seconds);
}
