#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <functional>
#include <iostream>
#include <set>
#include <string>
#include <tuple>
#include <unordered_map>
#include <utility>
#include <vector>

// H100-only audit of coalescing nonidentical forced histories at one
// parent start.  For every inverse highest-valley packet fibre, choose a
// parent start and arbitrary child orientations/starts.  Test whether one
// literal word H can serve every incidence, coordinatewise:
//       union(all forced sets) subset intersection(all maximal sets).

using U = std::uint64_t;
enum Packet { P01 = 0, P001 = 1, P011 = 2, P0011 = 3 };
static const char* packet_name[] = {"01", "001", "011", "0011"};

static std::pair<U, int> g(U word, int m) {
    std::vector<int> before(2 * m);
    int height = 0, down_zero = 0;
    for (int i = 0; i < 2 * m; ++i) {
        before[i] = height;
        if (((word >> i) & 1U) == 0 && height == 0) ++down_zero;
        height += (word >> i) & 1U ? 1 : -1;
    }
    int seen = 0;
    for (int i = 0; i < 2 * m; ++i) {
        if (((word >> i) & 1U) == 0 &&
            (before[i] == 0 || before[i] == 1) && ++seen == down_zero + 1) {
            return {word | (U{1} << i), i};
        }
    }
    assert(false); return {};
}

static std::pair<U, int> hmap(U word, int m) {
    std::vector<int> before(2 * m);
    int height = 0, up_one = 0;
    for (int i = 0; i < 2 * m; ++i) {
        before[i] = height;
        if (((word >> i) & 1U) != 0 && height == 1) ++up_one;
        height += (word >> i) & 1U ? 1 : -1;
    }
    int seen = 0;
    for (int i = 0; i < 2 * m; ++i) {
        if (((word >> i) & 1U) != 0 &&
            (before[i] == 0 || before[i] == 1) && ++seen == up_one) {
            return {word & ~(U{1} << i), i};
        }
    }
    assert(false); return {};
}

static std::vector<int> tight_order(U root, int m) {
    U word = root;
    const int n = 2 * m + 1;
    std::vector<int> rho;
    rho.reserve(n);
    for (int edge = 0; edge < m; ++edge) {
        auto first = g(word, m);
        auto second = hmap(first.first, m);
        rho.push_back(first.second);
        rho.push_back(second.second);
        word = second.first;
    }
    rho.push_back(2 * m);
    std::vector<int> order(n);
    for (int i = 0; i < n; ++i) order[i] = rho[(2 * i) % n];
    return order;
}

struct Port {
    std::array<U, 6> forced{};
    std::array<U, 6> maximal{};

    bool operator<(Port const& other) const {
        return std::tie(forced, maximal) < std::tie(other.forced, other.maximal);
    }
};

static std::string bit_word(U word, int m) {
    std::string answer;
    for (int i = 0; i < 2 * m; ++i) answer.push_back((word >> i) & 1U ? '1' : '0');
    return answer;
}

int main(int argc, char** argv) {
    assert(argc == 3);
    const int m = std::stoi(argv[1]), d = std::stoi(argv[2]);
    const int n = 2 * m + 1, s = m + 1 - d;
    assert(m >= 3 * d + 1 && n < 63 && 1 <= d && d <= 6);

    std::vector<U> roots;
    auto generate = [&](auto&& self, int position, int up, int down, U word) -> void {
        if (position == 2 * m) { roots.push_back(word); return; }
        if (up < m) self(self, position + 1, up + 1, down, word | (U{1} << position));
        if (down < up) self(self, position + 1, up, down + 1, word);
    };
    generate(generate, 0, 0, 0, 0);
    std::unordered_map<U, int> index;
    index.reserve(2 * roots.size());
    for (int i = 0; i < static_cast<int>(roots.size()); ++i) index[roots[i]] = i;
    const int root = index.at((U{1} << m) - 1);

    // Flatten [row][orientation][start].
    std::vector<Port> ports(roots.size() * 2 * n);
    auto port_at = [&](int row, int orientation, int start) -> Port& {
        return ports[(static_cast<std::size_t>(row) * 2 + orientation) * n + start];
    };
    for (int row_index = 0; row_index < static_cast<int>(roots.size()); ++row_index) {
        auto order = tight_order(roots[row_index], m);
        for (int orientation = 0; orientation < 2; ++orientation) {
            for (int start = 0; start < n; ++start) {
                Port& port = port_at(row_index, orientation, start);
                for (int offset = 0; offset < d; ++offset) {
                    U maximal = 0;
                    for (int step = 0; step < s; ++step)
                        maximal |= U{1} << order[(start + offset + step) % n];
                    int first = order[(start + offset) % n];
                    int last = order[(start + offset + s - 1) % n];
                    port.forced[offset] = (U{1} << first) | (U{1} << last);
                    port.maximal[offset] = maximal;
                }
            }
            std::reverse(order.begin(), order.end());
        }
    }

    // Structural inverse highest-valley packet fibres.
    std::vector<std::array<std::vector<int>, 4>> children(roots.size());
    for (int child = 0; child < static_cast<int>(roots.size()); ++child) {
        if (child == root) continue;
        U word = roots[child];
        int height = 0, maximum = -1;
        std::vector<int> valleys;
        for (int valley = 0; valley + 1 < 2 * m; ++valley) {
            if (((word >> valley) & 3U) == 2U) {
                if (height > maximum) { maximum = height; valleys.clear(); }
                if (height == maximum) valleys.push_back(valley);
            }
            height += (word >> valley) & 1U ? 1 : -1;
        }
        for (int valley : valleys) {
            std::vector<std::tuple<int, int, Packet>> moves{{valley, valley + 1, P01}};
            bool left = valley > 0 && ((word >> (valley - 1)) & 1U) == 0;
            bool right = valley + 2 < 2 * m && ((word >> (valley + 2)) & 1U) != 0;
            if (left) moves.push_back({valley - 1, valley + 1, P001});
            if (right) moves.push_back({valley, valley + 2, P011});
            if (left && right) moves.push_back({valley - 1, valley + 2, P0011});
            for (auto [first, second, packet] : moves) {
                int parent = index.at(word ^ (U{1} << first) ^ (U{1} << second));
                children[parent][packet].push_back(child);
            }
        }
    }
    for (auto& row : children) for (auto& list : row) {
        std::sort(list.begin(), list.end());
        list.erase(std::unique(list.begin(), list.end()), list.end());
    }

    for (int parent_orientation = 0; parent_orientation < 2; ++parent_orientation) {
        long long fibres = 0, strict_fail = 0, relaxed_success = 0, relaxed_fail = 0;
        long long strict_success = 0, recovered = 0;
        std::array<long long, 4> packet_fibres{}, packet_strict_fail{},
                                 packet_recovered{}, packet_relaxed_fail{};
        int maximum_fibre = 0, printed_recovered = 0, printed_failure = 0;

        for (int parent = 0; parent < static_cast<int>(roots.size()); ++parent) {
            for (int packet = 0; packet < 4; ++packet) {
                auto const& fibre_children = children[parent][packet];
                if (fibre_children.empty()) continue;
                ++fibres; ++packet_fibres[packet];
                maximum_fibre = std::max(maximum_fibre,
                                         static_cast<int>(fibre_children.size()));

                bool has_strict = false, has_relaxed = false;
                int relaxed_parent_start = -1;
                std::array<U, 6> relaxed_history{};

                for (int parent_start = 0; parent_start < n && !has_strict; ++parent_start) {
                    Port const& parent_port = port_at(parent, parent_orientation, parent_start);
                    bool works = true;
                    for (int child : fibre_children) {
                        bool child_works = false;
                        for (int orientation = 0; orientation < 2 && !child_works; ++orientation)
                            for (int start = 0; start < n && !child_works; ++start) {
                                Port const& child_port = port_at(child, orientation, start);
                                child_works = true;
                                for (int offset = 0; offset < d; ++offset)
                                    child_works &= child_port.forced[offset] ==
                                                   parent_port.forced[offset];
                            }
                        if (!child_works) { works = false; break; }
                    }
                    has_strict = works;
                }

                for (int parent_start = 0; parent_start < n && !has_relaxed; ++parent_start) {
                    Port const& parent_port = port_at(parent, parent_orientation, parent_start);
                    std::vector<std::vector<Port>> candidates;
                    bool individually_possible = true;
                    for (int child : fibre_children) {
                        std::set<Port> unique;
                        for (int orientation = 0; orientation < 2; ++orientation)
                            for (int start = 0; start < n; ++start) {
                                Port const& candidate = port_at(child, orientation, start);
                                bool okay = true;
                                for (int offset = 0; offset < d; ++offset) {
                                    U joined_forced = parent_port.forced[offset] |
                                                      candidate.forced[offset];
                                    U common_maximal = parent_port.maximal[offset] &
                                                       candidate.maximal[offset];
                                    okay &= (joined_forced & ~common_maximal) == 0;
                                }
                                if (okay) unique.insert(candidate);
                            }
                        if (unique.empty()) { individually_possible = false; break; }
                        candidates.emplace_back(unique.begin(), unique.end());
                    }
                    if (!individually_possible) continue;
                    std::sort(candidates.begin(), candidates.end(),
                              [](auto const& first, auto const& second) {
                                  return first.size() < second.size();
                              });

                    std::array<U, 6> initial_union = parent_port.forced;
                    std::array<U, 6> initial_intersection = parent_port.maximal;
                    std::function<bool(int, std::array<U, 6> const&,
                                           std::array<U, 6> const&)> search;
                    search = [&](int position, std::array<U, 6> const& joined,
                                 std::array<U, 6> const& common) -> bool {
                        if (position == static_cast<int>(candidates.size())) {
                            relaxed_history = joined;
                            return true;
                        }
                        for (Port const& candidate : candidates[position]) {
                            auto next_joined = joined;
                            auto next_common = common;
                            bool okay = true;
                            for (int offset = 0; offset < d; ++offset) {
                                next_joined[offset] |= candidate.forced[offset];
                                next_common[offset] &= candidate.maximal[offset];
                                okay &= (next_joined[offset] & ~next_common[offset]) == 0;
                            }
                            if (okay && search(position + 1, next_joined, next_common)) return true;
                        }
                        return false;
                    };
                    if (search(0, initial_union, initial_intersection)) {
                        has_relaxed = true;
                        relaxed_parent_start = parent_start;
                    }
                }

                if (has_strict) { ++strict_success; assert(has_relaxed); }
                else {
                    ++strict_fail; ++packet_strict_fail[packet];
                    if (has_relaxed) {
                        ++recovered; ++packet_recovered[packet];
                        if (printed_recovered < 10) {
                            std::cout << "RECOVERED parent_orientation=" << parent_orientation
                                      << " parent=" << parent << " packet="
                                      << packet_name[packet] << " multiplicity="
                                      << fibre_children.size() << " parent_start="
                                      << relaxed_parent_start << " history_sizes=";
                            for (int offset = 0; offset < d; ++offset)
                                std::cout << __builtin_popcountll(relaxed_history[offset]) << ',';
                            std::cout << " parent_word=" << bit_word(roots[parent], m) << '\n';
                            ++printed_recovered;
                        }
                    }
                }
                if (has_relaxed) ++relaxed_success;
                else {
                    ++relaxed_fail; ++packet_relaxed_fail[packet];
                    if (printed_failure < 10) {
                        std::cout << "RELAXED_FAIL parent_orientation=" << parent_orientation
                                  << " parent=" << parent << " packet="
                                  << packet_name[packet] << " multiplicity="
                                  << fibre_children.size() << " parent_word="
                                  << bit_word(roots[parent], m) << " children=";
                        for (int child : fibre_children)
                            std::cout << bit_word(roots[child], m) << ',';
                        std::cout << '\n';
                        ++printed_failure;
                    }
                }
            }
        }
        std::cout << "SUMMARY m=" << m << " d=" << d
                  << " parent_orientation=" << parent_orientation
                  << " roots=" << roots.size() << " fibres=" << fibres
                  << " maximum_fibre=" << maximum_fibre
                  << " strict_success=" << strict_success
                  << " strict_fail=" << strict_fail
                  << " recovered_strict_fail=" << recovered
                  << " relaxed_success=" << relaxed_success
                  << " relaxed_fail=" << relaxed_fail << " packet_fibres=";
        for (int packet = 0; packet < 4; ++packet)
            std::cout << packet_name[packet] << ':' << packet_fibres[packet] << ',';
        std::cout << " packet_strict_fail=";
        for (int packet = 0; packet < 4; ++packet)
            std::cout << packet_name[packet] << ':' << packet_strict_fail[packet] << ',';
        std::cout << " packet_recovered=";
        for (int packet = 0; packet < 4; ++packet)
            std::cout << packet_name[packet] << ':' << packet_recovered[packet] << ',';
        std::cout << " packet_relaxed_fail=";
        for (int packet = 0; packet < 4; ++packet)
            std::cout << packet_name[packet] << ':' << packet_relaxed_fail[packet] << ',';
        std::cout << '\n';
    }
}
