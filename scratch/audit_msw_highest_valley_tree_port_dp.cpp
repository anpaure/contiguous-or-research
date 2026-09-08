#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <functional>
#include <iostream>
#include <numeric>
#include <unordered_map>
#include <utility>
#include <vector>

// Exact H100-only verifier for the coupled separated-port problem on a
// highest-valley monotone same-forced parent tree.

using U = std::uint64_t;

static std::pair<U, int> g(U x, int m) {
    std::vector<int> before(2 * m);
    int height = 0, d0 = 0;
    for (int i = 0; i < 2 * m; ++i) {
        before[i] = height;
        if (((x >> i) & 1U) == 0 && height == 0) ++d0;
        height += ((x >> i) & 1U) ? 1 : -1;
    }
    int seen = 0;
    for (int i = 0; i < 2 * m; ++i)
        if (((x >> i) & 1U) == 0 &&
            (before[i] == 0 || before[i] == 1) && ++seen == d0 + 1)
            return {x | (U{1} << i), i};
    assert(false);
    return {};
}

static std::pair<U, int> hmap(U y, int m) {
    std::vector<int> before(2 * m);
    int height = 0, u1 = 0;
    for (int i = 0; i < 2 * m; ++i) {
        before[i] = height;
        if (((y >> i) & 1U) != 0 && height == 1) ++u1;
        height += ((y >> i) & 1U) ? 1 : -1;
    }
    int seen = 0;
    for (int i = 0; i < 2 * m; ++i)
        if (((y >> i) & 1U) != 0 &&
            (before[i] == 0 || before[i] == 1) && ++seen == u1)
            return {y & ~(U{1} << i), i};
    assert(false);
    return {};
}

static std::vector<int> tight_order(U root, int m) {
    U x = root;
    const int n = 2 * m + 1;
    std::vector<int> rho;
    rho.reserve(n);
    for (int e = 0; e < m; ++e) {
        auto a = g(x, m);
        auto b = hmap(a.first, m);
        rho.push_back(a.second);
        rho.push_back(b.second);
        x = b.first;
    }
    rho.push_back(2 * m);
    std::vector<int> tight(n);
    for (int j = 0; j < n; ++j) tight[j] = rho[(2 * j) % n];
    return tight;
}

static int area(U root, int m) {
    int height = 0, answer = 0;
    for (int i = 0; i < 2 * m; ++i) {
        height += (root >> i) & 1U ? 1 : -1;
        answer += height;
    }
    return answer;
}

static std::vector<U> signatures(const std::vector<int>& row, int d, int s) {
    const int n = static_cast<int>(row.size());
    assert(10 * d <= 64);
    std::vector<U> answer(n);
    for (int start = 0; start < n; ++start) {
        U signature = 0;
        for (int j = 0; j < d; ++j) {
            int a = row[(start + j) % n];
            int b = row[(start + s - 1 + j) % n];
            if (a > b) std::swap(a, b);
            signature |= U(32 * a + b) << (10 * j);
        }
        answer[start] = signature;
    }
    return answer;
}

static std::array<std::vector<U>, 2> oriented_signatures(
    std::vector<int> row, int d, int s) {
    std::array<std::vector<U>, 2> answer;
    answer[0] = signatures(row, d, s);
    std::reverse(row.begin(), row.end());
    answer[1] = signatures(row, d, s);
    return answer;
}

static U relation_mask(const std::vector<U>& child,
                       const std::vector<U>& parent,
                       U feasible_child) {
    const int n = static_cast<int>(child.size());
    U answer = 0;
    for (int b = 0; b < n; ++b)
        for (int a = 0; a < n; ++a)
            if (((feasible_child >> a) & 1U) && child[a] == parent[b]) {
                answer |= U{1} << b;
                break;
            }
    return answer;
}

static bool choose_separated(std::vector<U> masks, U compatible,
                             const std::vector<U>& separated) {
    if (masks.empty()) return true;
    std::sort(masks.begin(), masks.end(), [](U a, U b) {
        return __builtin_popcountll(a) < __builtin_popcountll(b);
    });
    std::function<bool(int, U)> search = [&](int index, U current) {
        if (index == static_cast<int>(masks.size())) return true;
        U options = masks[index] & current;
        while (options) {
            int bit = __builtin_ctzll(options);
            options &= options - 1;
            if (search(index + 1, current & separated[bit])) return true;
        }
        return false;
    };
    return search(0, compatible);
}

int main(int argc, char** argv) {
    const int m = argc > 1 ? std::stoi(argv[1]) : 13;
    const int d = argc > 2 ? std::stoi(argv[2]) : 4;
    const int n = 2 * m + 1, R = m + 1, s = R - d;
    assert(n < 63 && 10 * d <= 64);
    const U all_starts = (U{1} << n) - 1;

    std::vector<U> roots;
    std::function<void(int, int, int, U)> generate =
        [&](int pos, int up, int down, U root) {
            if (pos == 2 * m) {
                roots.push_back(root);
                return;
            }
            if (up < m) generate(pos + 1, up + 1, down, root | (U{1} << pos));
            if (down < up) generate(pos + 1, up, down + 1, root);
        };
    generate(0, 0, 0, 0);

    std::unordered_map<U, int> index;
    index.reserve(2 * roots.size());
    for (int i = 0; i < static_cast<int>(roots.size()); ++i) index[roots[i]] = i;

    std::vector<std::array<std::vector<U>, 2>> sig(roots.size());
    std::vector<int> areas(roots.size());
    for (int i = 0; i < static_cast<int>(roots.size()); ++i) {
        sig[i] = oriented_signatures(tight_order(roots[i], m), d, s);
        areas[i] = area(roots[i], m);
    }

    const U mountain = (U{1} << m) - 1;
    const int root_id = index.at(mountain);
    std::vector<std::vector<int>> candidates(roots.size());
    std::uint64_t no_candidate = 0;
    for (int id = 0; id < static_cast<int>(roots.size()); ++id) {
        if (id == root_id) continue;
        U x = roots[id];
        int height = 0, maximum = -1, highest_left = -1;
        for (int v = 0; v + 1 < 2 * m; ++v) {
            if (((x >> v) & 3U) == 2U && height > maximum) {
                maximum = height;
                highest_left = v;
            }
            height += (x >> v) & 1U ? 1 : -1;
        }
        assert(highest_left >= 0);
        const int v = highest_left;
        std::vector<std::pair<int, int>> moves{{v, v + 1}};
        const bool left = v > 0 && ((x >> (v - 1)) & 1U) == 0;
        const bool right = v + 2 < 2 * m && ((x >> (v + 2)) & 1U) != 0;
        if (left) moves.push_back({v - 1, v + 1});
        if (right) moves.push_back({v, v + 2});
        if (left && right) moves.push_back({v - 1, v + 2});
        for (auto [p, q] : moves) {
            U y = x ^ (U{1} << p) ^ (U{1} << q);
            int parent = index.at(y);
            assert(areas[parent] > areas[id]);
            U relation = 0;
            for (int child_orientation = 0; child_orientation < 2;
                 ++child_orientation)
                for (int parent_orientation = 0; parent_orientation < 2;
                     ++parent_orientation)
                    relation |= relation_mask(sig[id][child_orientation],
                                              sig[parent][parent_orientation],
                                              all_starts);
            if (relation)
                candidates[id].push_back(parent);
        }
        std::sort(candidates[id].begin(), candidates[id].end());
        candidates[id].erase(std::unique(candidates[id].begin(),
                                         candidates[id].end()),
                             candidates[id].end());
        if (candidates[id].empty()) ++no_candidate;
    }

    std::vector<int> order(roots.size());
    std::iota(order.begin(), order.end(), 0);
    std::sort(order.begin(), order.end(), [&](int a, int b) {
        if (areas[a] != areas[b]) return areas[a] > areas[b];
        return roots[a] < roots[b];
    });

    std::vector<int> parent(roots.size(), -1), child_load(roots.size());
    for (int id : order) {
        if (id == root_id || candidates[id].empty()) continue;
        int best = candidates[id][0];
        for (int p : candidates[id])
            if (child_load[p] < child_load[best] ||
                (child_load[p] == child_load[best] && p < best))
                best = p;
        parent[id] = best;
        ++child_load[best];
    }
    const int maximum_children = *std::max_element(child_load.begin(),
                                                    child_load.end());
    std::vector<std::vector<int>> children(roots.size());
    for (int id = 0; id < static_cast<int>(roots.size()); ++id)
        if (parent[id] >= 0) children[parent[id]].push_back(id);

    std::vector<U> separated(n);
    for (int a = 0; a < n; ++a)
        for (int b = 0; b < n; ++b) {
            int delta = std::abs(a - b);
            delta = std::min(delta, n - delta);
            if (delta >= d + 1) separated[a] |= U{1} << b;
        }

    std::sort(order.begin(), order.end(), [&](int a, int b) {
        if (areas[a] != areas[b]) return areas[a] < areas[b];
        return roots[a] < roots[b];
    });
    std::vector<std::array<U, 2>> feasible(roots.size());
    std::uint64_t empty_feasible = 0;
    std::vector<std::uint64_t> feasible_size_hist(n + 1);
    bool root_ok = false;
    for (int id : order) {
        for (int orientation = 0; orientation < 2; ++orientation) {
            std::vector<U> child_masks;
            for (int child : children[id]) {
                U mask = 0;
                for (int child_orientation = 0; child_orientation < 2;
                     ++child_orientation)
                    mask |= relation_mask(sig[child][child_orientation],
                                          sig[id][orientation],
                                          feasible[child][child_orientation]);
                child_masks.push_back(mask);
            }
            if (id == root_id) {
                const bool orientation_ok =
                    choose_separated(child_masks, all_starts, separated);
                root_ok |= orientation_ok;
                feasible[id][orientation] = orientation_ok ? all_starts : 0;
            } else {
                U mask = 0;
                for (int port = 0; port < n; ++port)
                    if (choose_separated(child_masks, separated[port], separated))
                        mask |= U{1} << port;
                feasible[id][orientation] = mask;
            }
        }
        if (!feasible[id][0] && !feasible[id][1]) ++empty_feasible;
        ++feasible_size_hist[std::max(__builtin_popcountll(feasible[id][0]),
                                     __builtin_popcountll(feasible[id][1]))];
    }

    std::cout << "m=" << m << " d=" << d << " n=" << n
              << " roots=" << roots.size()
              << " no_candidate=" << no_candidate
              << " maximum_children=" << maximum_children
              << " empty_feasible=" << empty_feasible
              << " root_ok=" << root_ok
              << " root_children=" << children[root_id].size() << '\n';
    std::cout << "feasible_size_hist=";
    for (int z = 0; z <= n; ++z)
        if (feasible_size_hist[z]) std::cout << z << ':' << feasible_size_hist[z] << ',';
    std::cout << '\n';
}
