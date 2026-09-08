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
#include <string>
#include <unordered_set>
#include <vector>

using namespace std;

struct Eval {
    int run_deficit = 0;
    int covered = 0;
    int adjacent = 0;
    int lower = 0;
    int upper = 0;
    int potential = 0;
    vector<int> missing;
};

static int K = 10, RANK = 5, D = 2, FULL = 1023;
static string MODE = "normal";

struct State {
    vector<uint16_t> path;
    Eval eval;
    uint64_t hash = 0;
};

static bool johnson_adjacent(int x, int y) {
    return popcount(static_cast<unsigned>(x ^ y)) == 2;
}

static uint64_t hash_path(const vector<uint16_t>& path) {
    uint64_t value = 0xcbf29ce484222325ULL;
    for (int x : path) value = (value ^ static_cast<unsigned>(x)) * 0x100000001b3ULL;
    return value;
}

static Eval evaluate(const vector<uint16_t>& path) {
    Eval result;
    for (int bit = 0; bit < K; ++bit) {
        int i = 0;
        while (i < static_cast<int>(path.size())) {
            if (!(path[i] & (1 << bit))) { ++i; continue; }
            const int first = i;
            while (i < static_cast<int>(path.size()) && (path[i] & (1 << bit))) ++i;
            if (first && i < static_cast<int>(path.size()))
                result.run_deficit += max(0, D + 1 - (i - first));
        }
    }
    vector<uint8_t> count(1 << K);
    auto record = [&] (int value, int wanted) {
        if (popcount(static_cast<unsigned>(value)) != wanted) return;
        if (count[value] != 255) ++count[value];
    };
    for (int value : path) record(value, RANK);
    for (int length = 2; length <= D + 1; ++length) {
        for (int left = 0; left + length <= static_cast<int>(path.size()); ++left) {
            int value = FULL;
            for (int j = left; j < left + length; ++j) value &= path[j];
            record(value, RANK - length + 1);
        }
    }
    for (int length = 2; RANK + length - 1 <= K; ++length) {
        for (int left = 0; left + length <= static_cast<int>(path.size()); ++left) {
            int value = 0;
            for (int j = left; j < left + length; ++j) value |= path[j];
            record(value, RANK + length - 1);
        }
    }
    for (int mask = 1; mask <= FULL; ++mask) {
        const int r = popcount(static_cast<unsigned>(mask));
        if (r < RANK - D) continue;
        if (!count[mask]) {
            result.missing.push_back(mask);
            continue;
        }
        ++result.covered;
        if (r < RANK) ++result.lower;
        if (r > RANK) ++result.upper;
        if (r == RANK - 1 || r == RANK + 1) ++result.adjacent;
        int reward = 1024;
        for (int bonus = 256, occurrence = 1;
             bonus && occurrence < count[mask]; bonus >>= 1, ++occurrence)
            reward += bonus;
        result.potential += (r == RANK - 1 || r == RANK + 1 ? 4 : 1) * reward;
    }
    return result;
}

static bool better(const State& a, const State& b) {
    if (MODE == "upper" && a.eval.upper != b.eval.upper)
        return a.eval.upper > b.eval.upper;
    if (MODE == "lower" && a.eval.lower != b.eval.lower)
        return a.eval.lower > b.eval.lower;
    if (a.eval.covered != b.eval.covered) return a.eval.covered > b.eval.covered;
    if (a.eval.adjacent != b.eval.adjacent) return a.eval.adjacent > b.eval.adjacent;
    return a.eval.potential > b.eval.potential;
}

static void save(const State& state, const string& path) {
    ofstream output(path);
    for (int value : state.path) output << value << ' ';
    output << '\n';
}

int main(int argc, char** argv) {
    const string input_path = argc > 1 ? argv[1] : "central_path_966.txt";
    const string output_path = argc > 2 ? argv[2] : "central_path_plateau_best.txt";
    const int beam_size = argc > 3 ? stoi(argv[3]) : 20000;
    const int maximum_depth = argc > 4 ? stoi(argv[4]) : 30;
    K = argc > 5 ? stoi(argv[5]) : 10;
    RANK = argc > 6 ? stoi(argv[6]) : 5;
    D = argc > 7 ? stoi(argv[7]) : 2;
    MODE = argc > 8 ? argv[8] : "normal";
    FULL = (1 << K) - 1;
    ifstream input(input_path);
    State initial;
    for (int value; input >> value;) initial.path.push_back(value);
    if (initial.path.empty()) return 2;
    initial.eval = evaluate(initial.path);
    initial.hash = hash_path(initial.path);
    vector<State> beam{initial};
    State best = initial;
    unordered_set<uint64_t> visited;
    visited.reserve(static_cast<size_t>(beam_size) * maximum_depth * 2);
    visited.insert(initial.hash);

    for (int depth = 1; depth <= maximum_depth; ++depth) {
        vector<State> next;
        next.reserve(static_cast<size_t>(beam.size()) * 40);
        for (const State& state : beam) {
            const int n = state.path.size();
            for (int left = 0; left < n; ++left) {
                for (int right = left + 2; right < n; ++right) {
                    if (left && !johnson_adjacent(state.path[left - 1],
                                                   state.path[right])) continue;
                    if (right + 1 < n && !johnson_adjacent(state.path[left],
                                                            state.path[right + 1])) continue;
                    State candidate;
                    candidate.path = state.path;
                    reverse(candidate.path.begin() + left,
                            candidate.path.begin() + right + 1);
                    candidate.hash = hash_path(candidate.path);
                    if (!visited.insert(candidate.hash).second) continue;
                    candidate.eval = evaluate(candidate.path);
                    if (candidate.eval.run_deficit ||
                        candidate.eval.covered + 30 < initial.eval.covered) continue;
                    if (better(candidate, best)) {
                        best = candidate;
                        cerr << "depth=" << depth << " best=" << best.eval.covered
                             << " lower=" << best.eval.lower
                             << " upper=" << best.eval.upper
                             << " adjacent=" << best.eval.adjacent
                             << " potential=" << best.eval.potential << " missing";
                        for (int x : best.eval.missing) cerr << ' ' << x;
                        cerr << '\n';
                        save(best, output_path);
                        const int desired = 0; // Full completion is detected by no missing masks.
                        (void) desired;
                        if (best.eval.missing.empty()) return 0;
                    }
                    next.push_back(move(candidate));
                }
            }
        }
        if (next.empty()) break;
        if (static_cast<int>(next.size()) > beam_size) {
            nth_element(next.begin(), next.begin() + beam_size, next.end(), better);
            next.resize(beam_size);
        }
        sort(next.begin(), next.end(), better);
        beam.swap(next);
        cerr << "layer=" << depth << " states=" << beam.size()
             << " visited=" << visited.size() << " front=" << beam.front().eval.covered
             << " lower=" << beam.front().eval.lower
             << " upper=" << beam.front().eval.upper << '\n';
    }
    save(best, output_path);
    cerr << "NONE best=" << best.eval.covered << " visited=" << visited.size() << '\n';
    return 1;
}
