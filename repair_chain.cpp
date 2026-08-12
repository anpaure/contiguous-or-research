#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <array>
#include <cstdint>
#include <deque>
#include <iostream>
#include <unordered_set>
#include <vector>

using namespace std;

struct State {
    vector<int> a;
    vector<int> missing;
    int depth = 0;
};

static vector<int> missing_masks(const vector<int>& a, int k) {
    vector<uint8_t> seen(1 << k);
    array<int, 32> previous{}, current{};
    int previous_size = 0;
    for (int value : a) {
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
    vector<int> result;
    for (int mask = 1; mask < (1 << k); ++mask) if (!seen[mask]) result.push_back(mask);
    return result;
}

static uint64_t hash_array(const vector<int>& a) {
    uint64_t hash = 0xcbf29ce484222325ULL;
    for (int value : a) hash = (hash ^ static_cast<unsigned>(value)) * 0x100000001b3ULL;
    return hash;
}

int main(int argc, char** argv) {
    const int k = argc > 1 ? stoi(argv[1]) : 10;
    const uint64_t state_limit = argc > 2 ? stoull(argv[2]) : 1000000;
    const int maximum_missing = argc > 3 ? stoi(argv[3]) : 2;
    const int root_shard = argc > 4 ? stoi(argv[4]) : 0;
    const int root_shards = argc > 5 ? stoi(argv[5]) : 1;
    State initial;
    for (int value; cin >> value;) initial.a.push_back(value);
    initial.missing = missing_masks(initial.a, k);
    if (initial.missing.empty() ||
        initial.missing.size() > static_cast<size_t>(maximum_missing)) return 2;
    deque<State> queue;
    queue.push_back(move(initial));
    unordered_set<uint64_t> visited;
    visited.insert(hash_array(queue.front().a));
    uint64_t expanded = 0;
    int deepest = 0;
    while (!queue.empty() && visited.size() < state_limit) {
        State state = move(queue.front());
        queue.pop_front();
        ++expanded;
        if (expanded <= 100)
        {
            cerr << "state depth=" << state.depth << " missing:";
            for (int mask : state.missing) cerr << ' ' << mask;
            cerr << '\n';
        }
        if (state.depth > deepest) {
            deepest = state.depth;
            cerr << "depth=" << deepest << " expanded=" << expanded
                 << " visited=" << visited.size() << " queue=" << queue.size() << '\n';
        }
        for (int target : state.missing) {
        for (int position = 0; position < static_cast<int>(state.a.size()); ++position) {
            if (state.depth == 0 && position % root_shards != root_shard) continue;
            if (state.a[position] == target) continue;
            State next = state;
            next.a[position] = target;
            vector<int> missing = missing_masks(next.a, k);
            if (missing.empty()) {
                cerr << "FOUND depth=" << state.depth + 1 << " expanded=" << expanded
                     << " visited=" << visited.size() << '\n';
                for (int value : next.a) cout << value << ' ';
                cout << '\n';
                return 0;
            }
            if (missing.size() > static_cast<size_t>(maximum_missing)) continue;
            next.missing = move(missing);
            next.depth = state.depth + 1;
            const uint64_t hash = hash_array(next.a);
            if (visited.insert(hash).second) queue.push_back(move(next));
        }
        }
    }
    cerr << "NONE expanded=" << expanded << " visited=" << visited.size()
         << " queue=" << queue.size() << '\n';
    return 1;
}
