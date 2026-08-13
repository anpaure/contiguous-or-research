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

struct Incidence {
    int component;
};

static std::string bits(U x, int n) {
    std::string s;
    s.reserve(n);
    for (int i = 0; i < n; ++i) s.push_back(((x >> i) & 1U) ? '1' : '0');
    return s;
}

int main(int argc, char** argv) {
    const int min_m = argc > 2 ? std::stoi(argv[1]) : 3;
    const int max_m = argc > 2 ? std::stoi(argv[2])
                               : (argc > 1 ? std::stoi(argv[1]) : 9);
    for (int m = min_m; m <= max_m; ++m) {
        const int R = m + 1, n = 2 * m + 1;
        assert(n < 31);
        const U all = (U{1} << n) - 1;

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
            if (up < m) gen(pos + 1, up + 1, down, mask | (U{1} << pos));
            if (down < up) gen(pos + 1, up, down + 1, mask);
        };
        gen(0, 0, 0, 0);

        std::unordered_map<std::uint64_t, Incidence> factor_incidence;
        std::unordered_map<U, std::pair<U, U>> factor_neighbours;
        std::unordered_map<U, std::pair<U, U>> factor_lowers;
        std::unordered_map<U, int> owner_component;
        for (int c = 0; c < static_cast<int>(rows.size()); ++c) {
            std::vector<U> owners(n);
            for (int i = 0; i < n; ++i) {
                for (int j = 0; j < R; ++j)
                    owners[i] |= U{1} << rows[c][(i + j) % n];
                owner_component[owners[i]] = c;
            }
            for (int i = 0; i < n; ++i) {
                U a = owners[i], b = owners[(i + 1) % n], lower = a & b;
                factor_neighbours[lower] = {a, b};
                auto add_lower = [&](U owner) {
                    auto [it, inserted] = factor_lowers.try_emplace(owner,
                                                                    std::pair<U, U>{lower, lower});
                    if (!inserted) {
                        assert(it->second.first == it->second.second);
                        it->second.second = lower;
                    }
                };
                add_lower(a);
                add_lower(b);
                factor_incidence[ikey(a, lower)] = {c};
                factor_incidence[ikey(b, lower)] = {c};
            }
        }
        assert(static_cast<long long>(owner_component.size()) == choose(n, R));
        assert(static_cast<long long>(factor_neighbours.size()) == choose(n, R - 1));

        auto next_lower = [&](U owner, U previous) {
            auto options = factor_lowers.at(owner);
            assert(options.first != options.second);
            return options.first == previous ? options.second : options.first;
        };

        long long W = choose(n, R), lambda = 1LL << (n - 1);
        int d = 0;
        while (1LL * d * W + 1LL * d * (d + 1) / 2 < lambda) ++d;
        const int target_q = d + 1;
        const int selected_q = argc > 3 ? std::stoi(argv[3]) : target_q;
        std::vector<long long> safe_count(m + 1), min_gap_hist(3 * n + 1);
        long long alternating = 0, three_component = 0;
        std::map<std::vector<int>, long long> height_signature_hist;
        std::map<std::vector<int>, long long> target_height_signature_hist;
        std::map<std::vector<int>, long long> component_triple_hist;
        std::vector<long long> target_component_degree(rows.size());
        std::vector<std::vector<int>> target_component_graph(rows.size());
        std::vector<std::string> widest_examples;
        std::vector<std::string> target_examples;
        int widest_gap = 0;

        for (U core = 0; core <= all; ++core) {
            if (std::popcount(core) != R - 2) continue;
            std::vector<int> outside;
            for (int x = 0; x < n; ++x) if (((core >> x) & 1U) == 0)
                outside.push_back(x);
            for (int ia = 0; ia < static_cast<int>(outside.size()); ++ia)
            for (int ib = ia + 1; ib < static_cast<int>(outside.size()); ++ib)
            for (int ic = ib + 1; ic < static_cast<int>(outside.size()); ++ic) {
                int a = outside[ia], b = outside[ib], c = outside[ic];
                U owner[3] = {
                    core | (U{1} << a) | (U{1} << b),
                    core | (U{1} << b) | (U{1} << c),
                    core | (U{1} << c) | (U{1} << a)};
                U lower[3] = {
                    core | (U{1} << b),
                    core | (U{1} << c),
                    core | (U{1} << a)};
                for (int phase = 0; phase < 2; ++phase) {
                    U old_owner[3], new_owner[3];
                    bool is_alternating = true;
                    for (int i = 0; i < 3; ++i) {
                        old_owner[i] = phase == 0 ? owner[i] : owner[(i + 1) % 3];
                        new_owner[i] = phase == 0 ? owner[(i + 1) % 3] : owner[i];
                        if (!factor_incidence.count(ikey(old_owner[i], lower[i])) ||
                             factor_incidence.count(ikey(new_owner[i], lower[i]))) {
                            is_alternating = false;
                            break;
                        }
                    }
                    if (!is_alternating) continue;
                    ++alternating;
                    std::unordered_set<int> components;
                    for (int i = 0; i < 3; ++i)
                        components.insert(owner_component.at(old_owner[i]));
                    if (components.size() != 3) continue;
                    ++three_component;

                    std::pair<U, U> saved_pair[3];
                    std::pair<U, U> saved_lowers[3];
                    for (int i = 0; i < 3; ++i) {
                        auto& pair = factor_neighbours[lower[i]];
                        saved_pair[i] = pair;
                        if (pair.first == old_owner[i]) pair.first = new_owner[i];
                        else {
                            assert(pair.second == old_owner[i]);
                            pair.second = new_owner[i];
                        }
                    }
                    for (int j = 0; j < 3; ++j) {
                        saved_lowers[j] = factor_lowers[owner[j]];
                        U removed = 0, added = 0;
                        for (int i = 0; i < 3; ++i) {
                            if (old_owner[i] == owner[j]) removed = lower[i];
                            if (new_owner[i] == owner[j]) added = lower[i];
                        }
                        assert(removed && added && removed != added);
                        auto& pair = factor_lowers[owner[j]];
                        if (pair.first == removed) pair.first = added;
                        else {
                            assert(pair.second == removed);
                            pair.second = added;
                        }
                    }

                    // Traverse only the merged cycle, which has 3n projected edges.
                    std::vector<U> supports;
                    U start = owner[0], current = start, previous_lower = 0;
                    do {
                        U lower_next = next_lower(current, previous_lower);
                        auto pair = factor_neighbours.at(lower_next);
                        U next = pair.first == current ? pair.second : pair.first;
                        supports.push_back(current ^ next);
                        previous_lower = lower_next;
                        current = next;
                    } while (current != start);
                    assert(static_cast<int>(supports.size()) == 3 * n);

                    for (int i = 0; i < 3; ++i)
                        factor_neighbours[lower[i]] = saved_pair[i];
                    for (int i = 0; i < 3; ++i)
                        factor_lowers[owner[i]] = saved_lowers[i];

                    int min_gap = static_cast<int>(supports.size());
                    for (int x = 0; x < n; ++x) {
                        std::vector<int> positions;
                        for (int j = 0; j < static_cast<int>(supports.size()); ++j)
                            if ((supports[j] >> x) & 1U) positions.push_back(j);
                        assert(positions.size() >= 2);
                        for (int j = 0; j < static_cast<int>(positions.size()); ++j) {
                            int next = positions[(j + 1) % positions.size()];
                            if (j + 1 == static_cast<int>(positions.size()))
                                next += supports.size();
                            min_gap = std::min(min_gap, next - positions[j]);
                        }
                    }
                    ++min_gap_hist[min_gap];
                    for (int q = 1; q <= m; ++q)
                        if (min_gap >= q) ++safe_count[q];

                    std::vector<int> component_vec(components.begin(), components.end());
                    std::sort(component_vec.begin(), component_vec.end());
                    std::vector<int> heights;
                    for (int component : component_vec)
                        heights.push_back(root_heights[component]);
                    std::sort(heights.begin(), heights.end());
                    ++height_signature_hist[heights];

                    if (min_gap > widest_gap) {
                        widest_gap = min_gap;
                        widest_examples.clear();
                    }

                    if (min_gap >= selected_q && target_examples.size() < 32) {
                        std::ostringstream out;
                        out << "core=" << bits(core, n) << " active=" << a << ',' << b
                            << ',' << c << " phase=" << phase << " roots=";
                        for (int j = 0; j < 3; ++j) {
                            if (j) out << ',';
                            out << bits(roots[component_vec[j]], 2 * m);
                        }
                        out << " supports=";
                        for (int j = 0; j < static_cast<int>(supports.size()); ++j) {
                            U support = supports[j];
                            int x = std::countr_zero(support);
                            int y = std::countr_zero(support & ~(U{1} << x));
                            if (j) out << ';';
                            out << x << '-' << y;
                        }
                        target_examples.push_back(out.str());
                    }
                    if (min_gap == widest_gap && widest_examples.size() < 8) {
                        std::ostringstream out;
                        out << "core=" << core << " active=" << a << ',' << b << ',' << c
                            << " phase=" << phase << " components=";
                        for (int j = 0; j < 3; ++j) {
                            if (j) out << ',';
                            out << component_vec[j] << "(root=" << roots[component_vec[j]]
                                << ",h=" << root_heights[component_vec[j]] << ')';
                        }
                        widest_examples.push_back(out.str());
                    }

                    if (min_gap >= selected_q) {
                        ++target_height_signature_hist[heights];
                        ++component_triple_hist[component_vec];
                        for (int component : component_vec)
                            ++target_component_degree[component];
                        for (int x = 0; x < 3; ++x)
                            for (int y = x + 1; y < 3; ++y) {
                                target_component_graph[component_vec[x]].push_back(component_vec[y]);
                                target_component_graph[component_vec[y]].push_back(component_vec[x]);
                            }
                    }
                }
            }
        }

        std::cout << "m=" << m << " R=" << R << " q=" << target_q
                  << " selected_q=" << selected_q
                  << " components=" << rows.size()
                  << " alternating_hex=" << alternating
                  << " three_component=" << three_component
                  << " safe_by_q=";
        for (int q = 1; q <= m; ++q) {
            if (q > 1) std::cout << ',';
            std::cout << q << ':' << safe_count[q];
        }
        std::cout << " min_gap_hist=";
        bool first = true;
        for (int gap = 1; gap <= 3 * n; ++gap) if (min_gap_hist[gap]) {
            if (!first) std::cout << ',';
            first = false;
            std::cout << gap << ':' << min_gap_hist[gap];
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
        long long triple_min = -1, triple_max = 0;
        for (const auto& [triple, count] : component_triple_hist) {
            triple_min = triple_min < 0 ? count : std::min(triple_min, count);
            triple_max = std::max(triple_max, count);
        }
        std::cout << " target_2section={active:" << active
                  << ",components:" << graph_components
                  << ",degree_min:" << degree_min
                  << ",degree_max:" << degree_max
                  << ",triples:" << component_triple_hist.size()
                  << ",multiplicity_min:" << triple_min
                  << ",multiplicity_max:" << triple_max << "}";
        std::cout << " widest_gap=" << widest_gap << '\n';
        std::cout << "widest_examples:";
        for (const auto& example : widest_examples) std::cout << " [" << example << ']';
        std::cout << '\n';
        if (!target_height_signature_hist.empty()) {
            std::cout << "target_height_signatures:";
            for (const auto& [signature, count] : target_height_signature_hist) {
                std::cout << " [";
                for (int i = 0; i < static_cast<int>(signature.size()); ++i) {
                    if (i) std::cout << ',';
                    std::cout << signature[i];
                }
                std::cout << ':' << count << ']';
            }
            std::cout << '\n';
        }
        if (!target_examples.empty()) {
            std::cout << "target_examples:\n";
            for (const auto& example : target_examples)
                std::cout << example << '\n';
        }
    }
}
