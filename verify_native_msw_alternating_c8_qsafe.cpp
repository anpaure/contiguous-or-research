#include <algorithm>
#include <bit>
#include <cassert>
#include <cstdint>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <sstream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

using U = std::uint32_t;

static std::pair<U, int> g(U x, int m) {
    std::vector<int> before(2 * m);
    int height = 0, d0 = 0;
    for (int i = 0; i < 2 * m; ++i) {
        before[i] = height;
        if (((x >> i) & 1U) == 0 && height == 0) ++d0;
        height += ((x >> i) & 1U) ? 1 : -1;
    }
    int seen = 0;
    for (int i = 0; i < 2 * m; ++i) {
        if (((x >> i) & 1U) == 0 &&
            (before[i] == 0 || before[i] == 1) && ++seen == d0 + 1)
            return {x | (U{1} << i), i};
    }
    assert(false);
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
    for (int i = 0; i < 2 * m; ++i) {
        if (((y >> i) & 1U) != 0 &&
            (before[i] == 0 || before[i] == 1) && ++seen == u1)
            return {y & ~(U{1} << i), i};
    }
    assert(false);
}

static long long choose(int n, int r) {
    if (r < 0 || r > n) return 0;
    long long z = 1;
    for (int i = 1; i <= r; ++i) z = z * (n - r + i) / i;
    return z;
}

static std::uint64_t ikey(U owner, U lower) {
    return (std::uint64_t(owner) << 32) | lower;
}

struct Port { U owner, lower; };

int main(int argc, char** argv) {
    const int min_m = argc > 2 ? std::stoi(argv[1]) : 3;
    const int max_m = argc > 2 ? std::stoi(argv[2])
                               : (argc > 1 ? std::stoi(argv[1]) : 9);
    for (int m = min_m; m <= max_m; ++m) {
        const int R = m + 1, n = 2 * m + 1;
        assert(n < 31);

        std::vector<std::vector<int>> rows;
        std::vector<U> roots;
        std::vector<int> root_heights;
        std::function<void(int, int, int, U)> gen = [&](int pos, int up,
                                                        int down, U mask) {
            if (pos == 2 * m) {
                U x = mask;
                std::vector<int> omitted;
                for (int e = 0; e < m; ++e) {
                    auto a = g(x, m);
                    auto b = hmap(a.first, m);
                    omitted.push_back(a.second);
                    omitted.push_back(b.second);
                    x = b.first;
                }
                omitted.push_back(2 * m);
                std::vector<int> tight(n);
                for (int j = 0; j < n; ++j) tight[j] = omitted[(2 * j) % n];
                rows.push_back(std::move(tight));
                roots.push_back(mask);
                int height = 0, maximum = 0;
                for (int j = 0; j < 2 * m; ++j) {
                    height += ((mask >> j) & 1U) ? 1 : -1;
                    maximum = std::max(maximum, height);
                }
                root_heights.push_back(maximum);
                return;
            }
            if (up < m) gen(pos + 1, up + 1, down,
                            mask | (U{1} << pos));
            if (down < up) gen(pos + 1, up, down + 1, mask);
        };
        gen(0, 0, 0, 0);

        const long long W = choose(n, R);
        std::unordered_set<std::uint64_t> factor_incidence;
        std::unordered_map<U, std::pair<U, U>> factor_neighbours;
        std::unordered_map<U, std::pair<U, U>> factor_lowers;
        std::unordered_map<U, int> owner_component;
        std::vector<Port> ports;
        factor_incidence.reserve(4 * W);
        factor_neighbours.reserve(2 * W);
        factor_lowers.reserve(2 * W);
        owner_component.reserve(2 * W);
        ports.reserve(2 * W);

        for (int component = 0; component < static_cast<int>(rows.size());
             ++component) {
            std::vector<U> owners(n);
            for (int i = 0; i < n; ++i) {
                for (int j = 0; j < R; ++j)
                    owners[i] |= U{1} << rows[component][(i + j) % n];
                owner_component[owners[i]] = component;
            }
            for (int i = 0; i < n; ++i) {
                U a = owners[i], b = owners[(i + 1) % n], lower = a & b;
                factor_neighbours[lower] = {a, b};
                auto add_lower = [&](U owner) {
                    auto [it, inserted] = factor_lowers.try_emplace(
                        owner, std::pair<U, U>{lower, lower});
                    if (!inserted) {
                        assert(it->second.first == it->second.second);
                        it->second.second = lower;
                    }
                };
                add_lower(a); add_lower(b);
                factor_incidence.insert(ikey(a, lower));
                factor_incidence.insert(ikey(b, lower));
                ports.push_back({a, lower});
                ports.push_back({b, lower});
            }
        }
        assert(static_cast<long long>(owner_component.size()) == W);
        assert(static_cast<long long>(factor_neighbours.size()) == W);

        auto is_factor = [&](U owner, U lower) {
            return factor_incidence.count(ikey(owner, lower)) != 0;
        };
        auto next_lower = [&](U owner, U previous) {
            auto options = factor_lowers.at(owner);
            assert(options.first != options.second);
            return options.first == previous ? options.second : options.first;
        };

        const long long lambda = 1LL << (n - 1);
        int d = 0;
        while (d * W + 1LL * d * (d + 1) / 2 < lambda) ++d;
        const int target_q = d + 1;

        long long alternating = 0;
        std::map<int, long long> component_count_hist;
        std::map<std::pair<int, int>, long long> outcome_hist;
        std::vector<std::vector<long long>> safe_by_old_components(
            5, std::vector<long long>(m + 1));
        std::vector<std::vector<long long>> useful_safe_by_old_components(
            5, std::vector<long long>(m + 1));
        std::vector<long long> min_gap_hist(4 * n + 1);
        std::vector<long long> target_component_degree(rows.size());
        std::vector<std::vector<int>> target_component_graph(rows.size());
        std::map<std::vector<int>, long long> target_tuple_hist;
        std::map<std::vector<int>, long long> target_height_hist;
        std::unordered_map<std::uint64_t, long long> target_resource_load;
        std::vector<std::vector<std::uint64_t>> target_resources;
        std::vector<std::string> widest_examples;
        int widest_gap = 0;

        auto nonfactor_supersets = [&](U lower, auto&& callback) {
            for (int x = 0; x < n; ++x) if (((lower >> x) & 1U) == 0) {
                U owner = lower | (U{1} << x);
                if (!is_factor(owner, lower)) callback(owner);
            }
        };

        for (const Port& p0 : ports) {
            const U O0 = p0.owner, L0 = p0.lower;
            nonfactor_supersets(L0, [&](U O1) {
                if (O1 == O0) return;
                auto lower_pair1 = factor_lowers.at(O1);
                U lower_options1[2] = {lower_pair1.first, lower_pair1.second};
                for (U L1 : lower_options1) {
                    if (L1 == L0) continue;
                    nonfactor_supersets(L1, [&](U O2) {
                        if (O2 == O0 || O2 == O1) return;
                        auto lower_pair2 = factor_lowers.at(O2);
                        U lower_options2[2] = {lower_pair2.first, lower_pair2.second};
                        for (U L2 : lower_options2) {
                            if (L2 == L0 || L2 == L1) continue;
                            if (std::popcount(L2 & O0) != R - 2) continue;
                            U missing_from_L2 = O0 & ~L2;
                            assert(std::popcount(missing_from_L2) == 2);
                            for (int x = 0; x < n; ++x)
                                if ((missing_from_L2 >> x) & 1U) {
                                    U L3 = O0 & ~(U{1} << x);
                                    if (L3 == L0 || L3 == L1 || L3 == L2) continue;
                                    U O3 = L2 | L3;
                                    if (std::popcount(O3) != R || O3 == O0 ||
                                        O3 == O1 || O3 == O2) continue;
                                    if (!is_factor(O3, L3) || is_factor(O3, L2) ||
                                        is_factor(O0, L3)) continue;

                                    std::pair<U, U> old_ports[4] = {
                                        {O0,L0},{O1,L1},{O2,L2},{O3,L3}};
                                    auto minimum = *std::min_element(
                                        old_ports, old_ports + 4);
                                    if (old_ports[0] != minimum) continue;
                                    ++alternating;

                                    U owner[4] = {O0,O1,O2,O3};
                                    U lower[4] = {L0,L1,L2,L3};
                                    std::vector<int> components;
                                    for (U O : owner)
                                        components.push_back(owner_component.at(O));
                                    std::sort(components.begin(), components.end());
                                    int distinct = std::unique(components.begin(),
                                                               components.end()) - components.begin();
                                    ++component_count_hist[distinct];
                                    components.resize(distinct);

                                    std::pair<U,U> saved_neighbours[4], saved_lowers[4];
                                    for (int i = 0; i < 4; ++i) {
                                        saved_neighbours[i] = factor_neighbours[lower[i]];
                                        auto& pair = factor_neighbours[lower[i]];
                                        U replacement = owner[(i + 1) % 4];
                                        if (pair.first == owner[i]) pair.first = replacement;
                                        else {
                                            assert(pair.second == owner[i]);
                                            pair.second = replacement;
                                        }
                                    }
                                    for (int i = 0; i < 4; ++i) {
                                        saved_lowers[i] = factor_lowers[owner[i]];
                                        U added = lower[(i + 3) % 4];
                                        auto& pair = factor_lowers[owner[i]];
                                        if (pair.first == lower[i]) pair.first = added;
                                        else {
                                            assert(pair.second == lower[i]);
                                            pair.second = added;
                                        }
                                    }

                                    std::vector<std::vector<U>> cycle_supports;
                                    std::unordered_set<U> seen_owners;
                                    int traversed_supports = 0;
                                    for (U seed : owner) {
                                        if (seen_owners.count(seed)) continue;
                                        std::vector<U> supports;
                                        U start = seed, current = start, previous_lower = 0;
                                        do {
                                            assert(seen_owners.insert(current).second);
                                            U lower_next = next_lower(current, previous_lower);
                                            auto pair = factor_neighbours.at(lower_next);
                                            U next = pair.first == current ? pair.second : pair.first;
                                            supports.push_back(current ^ next);
                                            previous_lower = lower_next;
                                            current = next;
                                        } while (current != start);
                                        traversed_supports += supports.size();
                                        cycle_supports.push_back(std::move(supports));
                                    }
                                    assert(traversed_supports == distinct * n);

                                    for (int i = 0; i < 4; ++i) {
                                        factor_neighbours[lower[i]] = saved_neighbours[i];
                                        factor_lowers[owner[i]] = saved_lowers[i];
                                    }

                                    const int after_cycles = cycle_supports.size();
                                    ++outcome_hist[{distinct, after_cycles}];
                                    int min_gap = 4 * n;
                                    for (const auto& supports : cycle_supports) {
                                        int cycle_gap = supports.size();
                                        for (int coordinate = 0; coordinate < n; ++coordinate) {
                                            std::vector<int> positions;
                                            for (int j = 0; j < static_cast<int>(supports.size()); ++j)
                                                if ((supports[j] >> coordinate) & 1U)
                                                    positions.push_back(j);
                                            assert(positions.size() >= 2);
                                            for (int j = 0; j < static_cast<int>(positions.size()); ++j) {
                                                int next = positions[(j + 1) % positions.size()];
                                                if (j + 1 == static_cast<int>(positions.size()))
                                                    next += supports.size();
                                                cycle_gap = std::min(cycle_gap,
                                                                     next - positions[j]);
                                            }
                                        }
                                        min_gap = std::min(min_gap, cycle_gap);
                                    }
                                    ++min_gap_hist[min_gap];
                                    for (int q = 1; q <= m; ++q)
                                        if (min_gap >= q) {
                                            ++safe_by_old_components[distinct][q];
                                            if (after_cycles == 1)
                                                ++useful_safe_by_old_components[distinct][q];
                                        }

                                    if (min_gap > widest_gap) {
                                        widest_gap = min_gap;
                                        widest_examples.clear();
                                    }
                                    if (min_gap == widest_gap && widest_examples.size() < 6) {
                                        std::ostringstream out;
                                        out << "owners=" << O0 << ',' << O1 << ',' << O2 << ',' << O3
                                            << " components=";
                                        for (int i = 0; i < 4; ++i) {
                                            if (i) out << ',';
                                            int component = owner_component.at(owner[i]);
                                            out << component << "(root=" << roots[component]
                                                << ",h=" << root_heights[component] << ')';
                                        }
                                        widest_examples.push_back(out.str());
                                    }

                                    if (min_gap >= target_q && after_cycles == 1) {
                                        ++target_tuple_hist[components];
                                        std::vector<int> heights;
                                        for (int component : components) {
                                            ++target_component_degree[component];
                                            heights.push_back(root_heights[component]);
                                        }
                                        std::sort(heights.begin(), heights.end());
                                        ++target_height_hist[heights];
                                        for (int i = 0; i < distinct; ++i)
                                            for (int j = i + 1; j < distinct; ++j) {
                                                target_component_graph[components[i]].push_back(components[j]);
                                                target_component_graph[components[j]].push_back(components[i]);
                                            }
                                        std::vector<std::uint64_t> resources;
                                        for (U O : owner)
                                            resources.push_back((std::uint64_t{1} << 63) | O);
                                        for (U L : lower) resources.push_back(L);
                                        for (auto resource : resources)
                                            ++target_resource_load[resource];
                                        target_resources.push_back(std::move(resources));
                                    }
                                }
                        }
                    });
                }
            });
        }

        long long active = 0, degree_min = -1, degree_max = 0;
        for (long long degree : target_component_degree) if (degree) {
            ++active;
            degree_min = degree_min < 0 ? degree : std::min(degree_min, degree);
            degree_max = std::max(degree_max, degree);
        }
        std::vector<int> seen(rows.size());
        int graph_components = 0;
        for (int source = 0; source < static_cast<int>(rows.size()); ++source) {
            if (!target_component_degree[source] || seen[source]) continue;
            ++graph_components;
            std::vector<int> stack{source}; seen[source] = 1;
            while (!stack.empty()) {
                int x = stack.back(); stack.pop_back();
                for (int y : target_component_graph[x]) if (!seen[y]) {
                    seen[y] = 1; stack.push_back(y);
                }
            }
        }
        long long tuple_min = -1, tuple_max = 0;
        for (const auto& [tuple, count] : target_tuple_hist) {
            tuple_min = tuple_min < 0 ? count : std::min(tuple_min, count);
            tuple_max = std::max(tuple_max, count);
        }
        long long resource_max = 0, conflict_upper_max = 0;
        for (const auto& [resource, load] : target_resource_load)
            resource_max = std::max(resource_max, load);
        for (const auto& resources : target_resources) {
            long long bound = 0;
            for (auto resource : resources)
                bound += target_resource_load[resource] - 1;
            conflict_upper_max = std::max(conflict_upper_max, bound);
        }

        std::cout << "m=" << m << " R=" << R << " q=" << target_q
                  << " components=" << rows.size()
                  << " alternating_c8=" << alternating
                  << " old_component_count=";
        bool first = true;
        for (const auto& [count, number] : component_count_hist) {
            if (!first) std::cout << ',';
            first = false;
            std::cout << count << ':' << number;
        }
        std::cout << " outcomes=";
        first = true;
        for (const auto& [outcome, number] : outcome_hist) {
            if (!first) std::cout << ',';
            first = false;
            std::cout << outcome.first << "->" << outcome.second << ':' << number;
        }
        std::cout << " safe_by_q_and_old_components=";
        first = true;
        for (int count = 2; count <= 4; ++count)
            for (int q = 1; q <= m; ++q)
                if (safe_by_old_components[count][q]) {
                    if (!first) std::cout << ',';
                    first = false;
                    std::cout << count << '@' << q << ':'
                              << safe_by_old_components[count][q];
                }
        std::cout << " useful_safe_by_q_and_old_components=";
        first = true;
        for (int count = 2; count <= 4; ++count)
            for (int q = 1; q <= m; ++q)
                if (useful_safe_by_old_components[count][q]) {
                    if (!first) std::cout << ',';
                    first = false;
                    std::cout << count << '@' << q << ':'
                              << useful_safe_by_old_components[count][q];
        }
        std::cout << " min_gap_hist=";
        first = true;
        for (int gap = 1; gap <= 4 * n; ++gap) if (min_gap_hist[gap]) {
            if (!first) std::cout << ',';
            first = false;
            std::cout << gap << ':' << min_gap_hist[gap];
        }
        std::cout << " target_2section={active:" << active
                  << ",components:" << graph_components
                  << ",degree_min:" << degree_min
                  << ",degree_max:" << degree_max
                  << ",tuples:" << target_tuple_hist.size()
                  << ",multiplicity_min:" << tuple_min
                  << ",multiplicity_max:" << tuple_max << "}"
                  << " resource_load_max=" << resource_max
                  << " conflict_degree_upper_max=" << conflict_upper_max
                  << " widest_gap=" << widest_gap << '\n';
        std::cout << "widest_examples:";
        for (const auto& example : widest_examples) std::cout << " [" << example << ']';
        std::cout << '\n';
        if (!target_height_hist.empty()) {
            std::cout << "target_height_signatures:";
            for (const auto& [signature, count] : target_height_hist) {
                std::cout << " [";
                for (int i = 0; i < static_cast<int>(signature.size()); ++i) {
                    if (i) std::cout << ',';
                    std::cout << signature[i];
                }
                std::cout << ':' << count << ']';
            }
            std::cout << '\n';
        }
    }
}
