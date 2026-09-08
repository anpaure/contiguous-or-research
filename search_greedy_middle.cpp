#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#elif defined(__clang__)
#pragma clang optimize on
#endif

#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <iostream>
#include <random>
#include <vector>

using namespace std;

struct State {
    array<uint64_t, 4> seen{};
    array<uint64_t, 2> visited{};
    array<uint16_t, 20> blocks{};
    uint8_t block_count = 0;
    uint16_t present = 0;
    uint16_t last_target = 0;
    int score = 0;
    vector<int> output;
};

static bool get(const array<uint64_t, 4>& bits, int x) {
    return bits[x >> 6] >> (x & 63) & 1;
}

static void add_seen(State& s, int x) {
    if (!get(s.seen, x)) {
        s.seen[x >> 6] |= 1ULL << (x & 63);
        ++s.score;
    }
}

static State start_state(int target, int recent) {
    State s;
    const int old = target ^ recent;
    s.output = {old, recent};
    s.blocks[0] = recent;
    s.blocks[1] = old;
    s.block_count = 2;
    s.present = target;
    s.last_target = target;
    add_seen(s, old);
    add_seen(s, recent);
    add_seen(s, target);
    return s;
}

static State transition(const State& s, int target) {
    State t = s;
    int request = target & ~s.present;
    bool barrier = false;
    for (int i = 0; i < s.block_count; ++i) {
        const int block = s.blocks[i];
        if (block & ~target) barrier = true;
        if (barrier) request |= block & target;
    }
    if (!request) request = target;
    t.output.push_back(request);
    t.last_target = target;
    t.present |= request;
    t.block_count = 1;
    t.blocks[0] = request;
    for (int i = 0; i < s.block_count; ++i) {
        const int block = s.blocks[i] & ~request;
        if (block) t.blocks[t.block_count++] = block;
    }
    int value = 0;
    for (int i = 0; i < t.block_count; ++i) {
        value |= t.blocks[i];
        add_seen(t, value);
    }
    return t;
}

static int heuristic(const State& s, int k) {
    int h = s.score * 1000 + s.block_count * 3;
    // Scarce low/high ranks matter more than another easy middle-rank hit.
    for (int mask = 1; mask < (1 << k); ++mask) if (get(s.seen, mask)) {
        const int rank = popcount(static_cast<unsigned>(mask));
        if (rank == 1 || rank == k - 1) h += 9;
        else if (rank == 2 || rank == k - 2) h += 3;
    }
    return h;
}

int main(int argc, char** argv) {
    const int k = argc > 1 ? stoi(argv[1]) : 8;
    const uint64_t restarts = argc > 2 ? stoull(argv[2]) : 1000000;
    const uint64_t seed = argc > 3 ? stoull(argv[3]) : 0x13198a2e03707344ULL;
    const int r = k / 2;
    vector<int> middle;
    array<int, 1 << 8> index{};
    index.fill(-1);
    for (int mask = 1; mask < (1 << k); ++mask)
        if (popcount(static_cast<unsigned>(mask)) == r) {
            index[mask] = middle.size();
            middle.push_back(mask);
        }

    mt19937_64 rng(seed);
    int global_best = 0;
    for (uint64_t restart = 0; restart < restarts; ++restart) {
        const int first = middle[rng() % middle.size()];
        int recent = rng() & first;
        if (!recent || recent == first) recent = first & -first;
        State state = start_state(first, recent);
        state.visited[index[first] >> 6] |= 1ULL << (index[first] & 63);

        while (state.output.size() < middle.size() + 1) {
            struct Candidate { int h, target; State state; };
            array<Candidate, 8> top;
            int top_count = 0;
            for (int target : middle) {
                const int id = index[target];
                if (state.visited[id >> 6] >> (id & 63) & 1) continue;
                if (popcount(static_cast<unsigned>(target ^ state.last_target)) != 2)
                    continue;
                State next = transition(state, target);
                int h = heuristic(next, k);
                // Prefer Johnson steps and small refresh requests.
                const int request = next.output.back();
                const int old_middle = state.output.size() >= 2 ? 0 : 0;
                (void)old_middle;
                h -= 8 * max(0, popcount(static_cast<unsigned>(request)) - 1);
                h += int(rng() & 31);
                Candidate c{h, target, std::move(next)};
                int p = top_count;
                if (p < static_cast<int>(top.size())) ++top_count;
                else if (h <= top[top_count - 1].h) continue;
                else p = top_count - 1;
                while (p > 0 && top[p - 1].h < h) {
                    if (p < static_cast<int>(top.size())) top[p] = std::move(top[p - 1]);
                    --p;
                }
                top[p] = std::move(c);
            }
            if (!top_count) break;
            const int choose = (rng() % 100 < 82) ? 0 : rng() % min(4, top_count);
            const int target = top[choose].target;
            state = std::move(top[choose].state);
            const int id = index[target];
            state.visited[id >> 6] |= 1ULL << (id & 63);
        }

        if (state.score > global_best) {
            global_best = state.score;
            cerr << "score " << global_best << '/' << ((1 << k) - 1)
                 << " restart " << restart << ':';
            for (int x : state.output) cerr << ' ' << x;
            cerr << '\n';
            if (global_best == (1 << k) - 1) return 0;
        }
    }
    return 1;
}
