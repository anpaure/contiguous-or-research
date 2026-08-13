#define main msw_factor_fibre_bfs_main
#include "msw_factor_fibre_bfs.cpp"
#undef main

#include <cmath>
#include <iostream>
#include <random>

struct ShadowScore {
    int holes;
    int collisions;
};

static ShadowScore shadow_score(const std::vector<U64>& state, int n, int r) {
    std::vector<unsigned char> count(U32{1} << n);
    for (U64 row : state) {
        for (U32 target : intervals(row, n, r)) ++count[target];
    }
    int holes = 0;
    int collisions = 0;
    for (U32 target = 0; target < (U32{1} << n); ++target) {
        if (__builtin_popcount(target) != r) continue;
        if (count[target] == 0) ++holes;
        collisions += count[target] * (count[target] - 1) / 2;
    }
    return {holes, collisions};
}

static std::vector<std::vector<U64>> component_neighbors(
        const std::vector<U64>& cur, int n, int a, int b) {
    std::vector<U64> rhs(cur.size());
    std::vector<int> old_owner(U32{1} << n, -1), new_owner(U32{1} << n, -1);
    for (int i = 0; i < static_cast<int>(cur.size()); ++i) {
        for (U32 owner : intervals(cur[i], n, (n - 1) / 2)) old_owner[owner] = i;
        rhs[i] = swap_labels(cur[i], n, a, b);
        for (U32 owner : intervals(rhs[i], n, (n - 1) / 2)) new_owner[owner] = i;
    }
    DSU dsu(2 * cur.size());
    for (U32 owner = 0; owner < (U32{1} << n); ++owner) {
        if (old_owner[owner] >= 0) dsu.u(old_owner[owner], cur.size() + new_owner[owner]);
    }
    std::unordered_map<int, std::pair<std::vector<int>, std::vector<int>>> components;
    for (int i = 0; i < static_cast<int>(cur.size()); ++i) {
        components[dsu.f(i)].first.push_back(i);
        components[dsu.f(cur.size() + i)].second.push_back(i);
    }
    std::vector<std::vector<U64>> result;
    for (const auto& [_, shores] : components) {
        std::vector<char> remove(cur.size());
        for (int i : shores.first) remove[i] = true;
        std::vector<U64> next;
        for (int i = 0; i < static_cast<int>(cur.size()); ++i) {
            if (!remove[i]) next.push_back(cur[i]);
        }
        for (int i : shores.second) next.push_back(rhs[i]);
        std::sort(next.begin(), next.end());
        if (next != cur) result.push_back(std::move(next));
    }
    return result;
}

static std::vector<U64> canonical_msw_factor(int m) {
    std::vector<U64> start;
    std::function<void(int, int, int, U32)> generate = [&](int p, int up, int down, U32 mask) {
        if (p == 2 * m) {
            U32 x = mask;
            std::vector<int> omitted;
            for (int e = 0; e < m; ++e) {
                auto arrived = g(x, m);
                auto departed = hfun(arrived.first, m);
                omitted.push_back(arrived.second);
                omitted.push_back(departed.second);
                x = departed.first;
            }
            omitted.push_back(2 * m);
            start.push_back(canon(omitted));
            return;
        }
        if (up < m) generate(p + 1, up + 1, down, mask | (U32{1} << p));
        if (down < up) generate(p + 1, up, down + 1, mask);
    };
    generate(0, 0, 0, 0);
    std::sort(start.begin(), start.end());
    return start;
}

int main(int argc, char** argv) {
    const int m = argc > 1 ? std::stoi(argv[1]) : 5;
    const long long iterations = argc > 2 ? std::stoll(argv[2]) : 2000000;
    const std::uint64_t seed = argc > 3 ? std::stoull(argv[3]) : 1;
    const int n = 2 * m + 1;
    if (n > 15) {
        std::cerr << "Packed representation supports n <= 15\n";
        return 2;
    }
    std::mt19937_64 rng(seed);
    auto current = canonical_msw_factor(m);
    ShadowScore score = shadow_score(current, n, m - 1);
    auto best = current;
    ShadowScore best_score = score;
    std::cerr << "initial holes=" << score.holes << " collisions=" << score.collisions
              << " rows=" << current.size() << '\n';

    for (long long iteration = 1; iteration <= iterations && best_score.holes; ++iteration) {
        int a = rng() % n;
        int b = rng() % (n - 1);
        if (b >= a) ++b;
        if (a > b) std::swap(a, b);
        auto neighbors = component_neighbors(current, n, a, b);
        if (neighbors.empty()) continue;
        auto candidate = std::move(neighbors[rng() % neighbors.size()]);
        const int jump = (rng() % 8 == 0) ? 2 + rng() % 7 : 1;
        for (int step = 1; step < jump; ++step) {
            int c = rng() % n;
            int d = rng() % (n - 1);
            if (d >= c) ++d;
            if (c > d) std::swap(c, d);
            auto more = component_neighbors(candidate, n, c, d);
            if (!more.empty()) candidate = std::move(more[rng() % more.size()]);
        }
        ShadowScore candidate_score = shadow_score(candidate, n, m - 1);
        const double phase = double(iteration % 200000) / 200000.0;
        const double temperature = std::max(0.08, 2.5 * (1.0 - phase));
        const bool accept = candidate_score.collisions <= score.collisions ||
            std::generate_canonical<double, 53>(rng) <
                std::exp((score.collisions - candidate_score.collisions) / temperature);
        if (accept) {
            current = std::move(candidate);
            score = candidate_score;
        }
        if (score.holes < best_score.holes ||
                (score.holes == best_score.holes && score.collisions < best_score.collisions)) {
            best = current;
            best_score = score;
            std::cerr << "iteration=" << iteration << " best holes=" << best_score.holes
                      << " collisions=" << best_score.collisions << '\n';
        }
    }

    std::cout << "BEST m=" << m << " holes=" << best_score.holes
              << " collisions=" << best_score.collisions << "\n";
    for (U64 row : best) {
        for (int x : unpack(row, n)) std::cout << x + 1 << ' ';
        std::cout << '\n';
    }
    return best_score.holes == 0 ? 0 : 1;
}
