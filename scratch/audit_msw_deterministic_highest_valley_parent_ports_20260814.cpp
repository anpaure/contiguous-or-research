#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <string>
#include <tuple>
#include <unordered_map>
#include <utility>
#include <vector>

// H100-only audit of a deterministic all-m candidate:
// leftmost highest valley, residue-table packet, and least canonical common cut.

using U = std::uint64_t;

enum Packet { P01 = 0, P001 = 1, P011 = 2, P0011 = 3 };

static const char* packet_name(Packet packet) {
    static const char* names[] = {"01", "001", "011", "0011"};
    return names[packet];
}

static std::pair<U, int> g(U x, int m) {
    std::vector<int> before(2 * m);
    int height = 0, down_zero = 0;
    for (int i = 0; i < 2 * m; ++i) {
        before[i] = height;
        if (((x >> i) & 1U) == 0 && height == 0) ++down_zero;
        height += (x >> i) & 1U ? 1 : -1;
    }
    int seen = 0;
    for (int i = 0; i < 2 * m; ++i) {
        if (((x >> i) & 1U) == 0 &&
            (before[i] == 0 || before[i] == 1) && ++seen == down_zero + 1) {
            return {x | (U{1} << i), i};
        }
    }
    assert(false); return {};
}

static std::pair<U, int> hmap(U y, int m) {
    std::vector<int> before(2 * m);
    int height = 0, up_one = 0;
    for (int i = 0; i < 2 * m; ++i) {
        before[i] = height;
        if (((y >> i) & 1U) != 0 && height == 1) ++up_one;
        height += (y >> i) & 1U ? 1 : -1;
    }
    int seen = 0;
    for (int i = 0; i < 2 * m; ++i) {
        if (((y >> i) & 1U) != 0 &&
            (before[i] == 0 || before[i] == 1) && ++seen == up_one) {
            return {y & ~(U{1} << i), i};
        }
    }
    assert(false); return {};
}

static std::vector<int> tight_order(U root, int m) {
    U x = root;
    const int n = 2 * m + 1;
    std::vector<int> rho;
    rho.reserve(n);
    for (int edge = 0; edge < m; ++edge) {
        auto first = g(x, m);
        auto second = hmap(first.first, m);
        rho.push_back(first.second);
        rho.push_back(second.second);
        x = second.first;
    }
    rho.push_back(2 * m);
    std::vector<int> answer(n);
    for (int index = 0; index < n; ++index) answer[index] = rho[(2 * index) % n];
    return answer;
}

using Rail = std::pair<int,int>;
using Signature = std::vector<Rail>;

static std::vector<Signature> signatures(U root, int m, int d) {
    std::vector<int> order = tight_order(root, m);
    const int n = 2 * m + 1, shift = m + 1 - d;
    std::vector<Signature> answer(n, Signature(d));
    for (int start = 0; start < n; ++start) {
        for (int offset = 0; offset < d; ++offset) {
            int x = order[(start + offset) % n];
            int y = order[(start + shift - 1 + offset) % n];
            if (x > y) std::swap(x, y);
            answer[start][offset] = {x, y};
        }
    }
    return answer;
}

struct Choice {
    U parent;
    Packet packet;
    int valley;
    int L, Q, O;
};

static Choice choose_parent(U word, int m, int d) {
    std::vector<int> height(2 * m + 1);
    for (int i = 0; i < 2 * m; ++i)
        height[i + 1] = height[i] + ((word >> i) & 1U ? 1 : -1);
    int maximum = -1, valley = -1;
    for (int i = 0; i + 1 < 2 * m; ++i) {
        if (((word >> i) & 3U) == 2U && height[i] > maximum) {
            maximum = height[i];
            valley = i;
        }
    }
    assert(valley >= 0);

    std::vector<int> stack, mate(2 * m, -1);
    for (int i = 0; i < 2 * m; ++i) {
        if ((word >> i) & 1U) stack.push_back(i);
        else {
            assert(!stack.empty());
            int opening = stack.back(); stack.pop_back();
            mate[i] = opening; mate[opening] = i;
        }
    }
    assert(stack.empty());
    int L = (valley - mate[valley] - 1) / 2;
    int Q = (mate[valley + 1] - valley - 2) / 2;
    int O = m - L - Q - 2;
    assert(L >= 0 && Q >= 0 && O >= 0);

    int first, second;
    Packet packet;
    if (L == 0 && Q == 0) {
        packet = P01; first = valley; second = valley + 1;
    } else if (L > 0 && Q == 0) {
        packet = P001; first = valley - 1; second = valley + 1;
    } else if (L == 0 && Q > 0) {
        packet = P011; first = valley; second = valley + 2;
    } else if (L == d && Q == d && O == d - 1) {
        // Fixed exceptional choice requested in the analytic lead.
        packet = P001; first = valley - 1; second = valley + 1;
    } else {
        packet = P0011; first = valley - 1; second = valley + 2;
    }
    assert(first >= 0 && second < 2 * m && first < second);
    assert(((word >> first) & 1U) == 0 && ((word >> second) & 1U) != 0);
    return {word ^ (U{1} << first) ^ (U{1} << second), packet, valley, L, Q, O};
}

static int cyclic_distance(int a, int b, int n) {
    int delta = std::abs(a - b);
    return std::min(delta, n - delta);
}

static std::string bit_word(U word, int m) {
    std::string answer;
    for (int i = 0; i < 2 * m; ++i) answer.push_back((word >> i) & 1U ? '1' : '0');
    return answer;
}

int main(int argc, char** argv) {
    assert(argc == 3);
    const int m = std::stoi(argv[1]), d = std::stoi(argv[2]);
    assert(m >= 3 * d + 1 && 2 * m + 1 < 63);
    const int n = 2 * m + 1;

    std::vector<U> roots;
    auto generate = [&](auto&& self, int position, int up, int down, U word) -> void {
        if (position == 2 * m) { roots.push_back(word); return; }
        if (up < m) self(self, position + 1, up + 1, down, word | (U{1} << position));
        if (down < up) self(self, position + 1, up, down + 1, word);
    };
    generate(generate, 0, 0, 0, 0);
    std::unordered_map<U,int> index;
    index.reserve(2 * roots.size());
    for (int i = 0; i < static_cast<int>(roots.size()); ++i) index[roots[i]] = i;
    const U mountain = (U{1} << m) - 1;
    const int root = index.at(mountain);

    std::vector<int> parent(roots.size(), -1), parent_port(roots.size(), -1);
    std::vector<Packet> parent_packet(roots.size(), P01);
    std::vector<std::vector<int>> children(roots.size());
    std::vector<std::vector<int>> incident_ports(roots.size());
    std::map<std::tuple<int,int>,std::vector<int>> fibre;
    std::map<Packet,long long> packet_hist;
    long long direct_edges = 0, crossed_edges = 0;
    int missing = 0;

    for (int child = 0; child < static_cast<int>(roots.size()); ++child) {
        if (child == root) continue;
        Choice choice = choose_parent(roots[child], m, d);
        int par = index.at(choice.parent);
        parent[child] = par;
        parent_packet[child] = choice.packet;
        children[par].push_back(child);
        ++packet_hist[choice.packet];
        fibre[{par, static_cast<int>(choice.packet)}].push_back(child);

        auto child_signatures = signatures(roots[child], m, d);
        auto parent_signatures = signatures(roots[par], m, d);
        int child_start = -1, par_start = -1;
        if (!(choice.L == d && choice.Q == d && choice.O == d - 1)) {
            for (int start = 0; start < n; ++start) {
                if (child_signatures[start] == parent_signatures[start]) {
                    child_start = par_start = start;
                    break;
                }
            }
            if (child_start >= 0) ++direct_edges;
        } else {
            for (int first = 0; first < n && child_start < 0; ++first) {
                for (int second = 0; second < n; ++second) {
                    if (child_signatures[first] == parent_signatures[second]) {
                        child_start = first; par_start = second; break;
                    }
                }
            }
            if (child_start >= 0) ++crossed_edges;
        }
        if (child_start < 0) {
            ++missing;
            if (missing <= 20) {
                std::cout << "MISSING child=" << child << " packet="
                          << packet_name(choice.packet) << " triple=" << choice.L
                          << ',' << choice.Q << ',' << choice.O << '\n';
            }
            continue;
        }
        parent_port[child] = par_start;
        incident_ports[child].push_back(child_start);
        incident_ports[par].push_back(par_start);
    }

    int max_fibre = 0, bad_fibres = 0;
    for (auto const& [key, members] : fibre) {
        int count = static_cast<int>(members.size());
        max_fibre = std::max(max_fibre, count);
        if (count > 1) {
            ++bad_fibres;
            if (bad_fibres <= 20) {
                std::cout << "NONINJECTIVE parent=" << std::get<0>(key)
                          << " packet=" << packet_name(static_cast<Packet>(std::get<1>(key)))
                          << " multiplicity=" << count
                          << " parent_word=" << bit_word(roots[std::get<0>(key)], m)
                          << " child_words=";
                for (int child : members) {
                    Choice choice = choose_parent(roots[child], m, d);
                    std::cout << bit_word(roots[child], m) << '[' << choice.L << ','
                              << choice.Q << ',' << choice.O << "]" << ',';
                }
                std::cout << '\n';
            }
        }
    }

    int max_children = 0, max_distinct = 0, bad_vertices = 0;
    for (int vertex = 0; vertex < static_cast<int>(roots.size()); ++vertex) {
        max_children = std::max(max_children, static_cast<int>(children[vertex].size()));
        auto ports = incident_ports[vertex];
        std::sort(ports.begin(), ports.end());
        ports.erase(std::unique(ports.begin(), ports.end()), ports.end());
        max_distinct = std::max(max_distinct, static_cast<int>(ports.size()));
        bool bad = false;
        for (int i = 0; i < static_cast<int>(ports.size()); ++i) {
            for (int j = i + 1; j < static_cast<int>(ports.size()); ++j) {
                if (cyclic_distance(ports[i], ports[j], n) < d + 1) bad = true;
            }
        }
        if (bad) {
            ++bad_vertices;
            if (bad_vertices <= 20) {
                std::cout << "PORT_COLLISION vertex=" << vertex << " ports=";
                for (int port : ports) std::cout << port << ',';
                std::cout << " children=" << children[vertex].size()
                          << " word=" << bit_word(roots[vertex], m)
                          << " parent_port=" << parent_port[vertex] << " child_data=";
                for (int child : children[vertex]) {
                    Choice choice = choose_parent(roots[child], m, d);
                    std::cout << bit_word(roots[child], m) << ':'
                              << packet_name(choice.packet) << ':' << parent_port[child]
                              << '[' << choice.L << ',' << choice.Q << ',' << choice.O
                              << "],";
                }
                std::cout << '\n';
            }
        }
    }

    std::cout << "SUMMARY m=" << m << " d=" << d << " roots=" << roots.size()
              << " direct=" << direct_edges << " crossed=" << crossed_edges
              << " missing=" << missing << " max_fibre=" << max_fibre
              << " noninjective_fibres=" << bad_fibres
              << " max_children=" << max_children
              << " max_distinct_ports=" << max_distinct
              << " port_collision_vertices=" << bad_vertices << '\n';
    std::cout << "PACKETS";
    for (auto const& [packet, count] : packet_hist)
        std::cout << ' ' << packet_name(packet) << '=' << count;
    std::cout << '\n';
}
