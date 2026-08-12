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
#include <iostream>
#include <unordered_set>
#include <vector>

using namespace std;

struct State {
    vector<int> a;
    vector<int> missing;
    int score = 0;
};

static void evaluate(State& state, int k) {
    vector<uint8_t> seen(1 << k);
    array<int, 32> previous{}, current{};
    int previous_size = 0;
    for (int value : state.a) {
        int current_size = 0;
        current[current_size++] = value;
        for (int i = 0; i < previous_size; ++i) {
            const int next = previous[i] | value;
            if (next != current[current_size - 1]) current[current_size++] = next;
        }
        for (int i = 0; i < current_size; ++i) seen[current[i]] = 1;
        previous.swap(current);
        previous_size = current_size;
    }
    state.score = 0;
    state.missing.clear();
    for (int mask = 1; mask < (1 << k); ++mask) {
        const int rank = popcount(static_cast<unsigned>(mask));
        const int weight = 1 + 100 * (rank == k / 2) +
            8 * (rank == k / 2 - 1 || rank == k / 2 + 1);
        if (seen[mask]) state.score += weight;
        else state.missing.push_back(mask);
    }
}

static uint64_t hash_array(const vector<int>& a) {
    uint64_t hash = 0xcbf29ce484222325ULL;
    for (int value : a) hash = (hash ^ static_cast<unsigned>(value)) * 0x100000001b3ULL;
    return hash;
}

int main(int argc, char** argv) {
    const int k = argc > 1 ? stoi(argv[1]) : 10;
    const int width = argc > 2 ? stoi(argv[2]) : 200;
    const int depth_limit = argc > 3 ? stoi(argv[3]) : 12;
    State initial;
    for (int value; cin >> value;) initial.a.push_back(value);
    evaluate(initial, k);
    vector<State> beam{move(initial)};
    for (int depth = 0; depth <= depth_limit; ++depth) {
        cerr << "depth=" << depth << " score=" << beam.front().score
             << " missing=" << beam.front().missing.size() << ':';
        for (int mask : beam.front().missing) cerr << ' ' << mask;
        cerr << '\n';
        if (beam.front().missing.empty()) {
            for (int value : beam.front().a) cout << value << ' ';
            cout << '\n';
            return 0;
        }
        vector<State> next;
        unordered_set<uint64_t> hashes;
        for (const State& state : beam) {
            // Focus on no more than the 24 currently missing targets with the
            // highest lattice-layer weights.
            vector<int> targets = state.missing;
            stable_sort(targets.begin(), targets.end(), [k] (int lhs, int rhs) {
                auto weight = [k] (int mask) {
                    const int rank = popcount(static_cast<unsigned>(mask));
                    return 1 + 100 * (rank == k / 2) +
                        8 * (rank == k / 2 - 1 || rank == k / 2 + 1);
                };
                return weight(lhs) > weight(rhs);
            });
            if (targets.size() > 24) targets.resize(24);
            for (int position = 0; position < static_cast<int>(state.a.size()); ++position) {
                for (int target : targets) {
                    if (state.a[position] == target) continue;
                    State candidate = state;
                    candidate.a[position] = target;
                    evaluate(candidate, k);
                    if (candidate.missing.empty()) {
                        for (int value : candidate.a) cout << value << ' ';
                        cout << '\n';
                        return 0;
                    }
                    const uint64_t hash = hash_array(candidate.a);
                    if (hashes.insert(hash).second) next.push_back(move(candidate));
                }
            }
            // A missing low-rank mask can also be made by bringing two
            // existing submask entries next to each other, preserving the
            // multiset of entries and therefore all literal witnesses.
            for (int target : targets) {
                for (int first = 0; first < static_cast<int>(state.a.size()); ++first) {
                    if ((state.a[first] | target) != target) continue;
                    for (int second = 0; second < static_cast<int>(state.a.size()); ++second) {
                        if (first == second || (state.a[second] | target) != target ||
                            (state.a[first] | state.a[second]) != target)
                            continue;
                        State candidate = state;
                        const int value = candidate.a[second];
                        candidate.a.erase(candidate.a.begin() + second);
                        int destination = first + (second > first ? 1 : 0);
                        candidate.a.insert(candidate.a.begin() + destination, value);
                        evaluate(candidate, k);
                        if (candidate.missing.empty()) {
                            for (int entry : candidate.a) cout << entry << ' ';
                            cout << '\n';
                            return 0;
                        }
                        const uint64_t hash = hash_array(candidate.a);
                        if (hashes.insert(hash).second) next.push_back(move(candidate));
                    }
                }
            }
        }
        if (next.empty()) break;
        const int keep = min(width, static_cast<int>(next.size()));
        nth_element(next.begin(), next.begin() + keep - 1, next.end(),
            [] (const State& lhs, const State& rhs) { return lhs.score > rhs.score; });
        next.resize(keep);
        sort(next.begin(), next.end(),
            [] (const State& lhs, const State& rhs) { return lhs.score > rhs.score; });
        beam.swap(next);
    }
    if (!beam.empty()) {
        for (int value : beam.front().a) cout << value << ' ';
        cout << '\n';
    }
    return 1;
}
