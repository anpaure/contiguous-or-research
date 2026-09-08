#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

using namespace std;

using Mask = uint16_t;
constexpr int K = 11;
constexpr int LIMIT = 1 << K;
constexpr int FULL = LIMIT - 1;
constexpr int VERTICES = 462;

static int pc(Mask value) {
    return popcount(static_cast<unsigned>(value));
}

static int choose(int n, int r) {
    if (r < 0 || r > n) return 0;
    int result = 1;
    for (int i = 1; i <= r; ++i) result = result * (n - r + i) / i;
    return result;
}

static vector<Mask> read_cycle(const string& path) {
    ifstream input(path);
    if (!input) throw runtime_error("cannot open " + path);
    vector<unsigned> raw;
    for (unsigned value; input >> value;) raw.push_back(value);
    if (!input.eof()) throw runtime_error("invalid token");
    if (raw.size() == VERTICES + 1 && raw.front() == VERTICES) raw.erase(raw.begin());
    if (raw.size() != VERTICES) throw runtime_error("expected 462 masks");
    array<uint8_t, LIMIT> seen{};
    vector<Mask> result;
    for (unsigned value : raw) {
        if (value >= LIMIT || pc(static_cast<Mask>(value)) != 5 || ++seen[value] != 1)
            throw runtime_error("not a rank-five permutation");
        result.push_back(static_cast<Mask>(value));
    }
    return result;
}

int main(int argc, char** argv) {
    try {
        if (argc < 2 || argc > 3) {
            cerr << "usage: verify_o6_cycle CYCLE.txt [--require-deep]\n";
            return 2;
        }
        const bool require_deep = argc == 3 && string(argv[2]) == "--require-deep";
        if (argc == 3 && !require_deep) throw runtime_error("unknown option");
        const vector<Mask> cycle = read_cycle(argv[1]);
        int disjoint_edges = 0;
        array<uint8_t, LIMIT> transition_seen{};
        int transition_distinct = 0;
        for (int i = 0; i < VERTICES; ++i) {
            if (!(cycle[i] & cycle[(i + 1) % VERTICES])) ++disjoint_edges;
            const Mask value = static_cast<Mask>(
                cycle[(i + VERTICES - 1) % VERTICES] & cycle[(i + 1) % VERTICES]);
            if (pc(value) == 4 && !transition_seen[value]++) ++transition_distinct;
        }
        if (disjoint_edges != VERTICES)
            throw runtime_error("not a Hamilton cycle in KG(11,5)");

        // Taking complements on either parity class converts the O6 cycle
        // into two 231-vertex Johnson cycles on the rank-six layer.
        array<vector<Mask>, 2> parity;
        for (int parity_class = 0; parity_class < 2; ++parity_class)
            for (int i = parity_class; i < VERTICES; i += 2)
                parity[parity_class].push_back(static_cast<Mask>(FULL ^ cycle[i]));

        array<uint8_t, LIMIT> rank6_seen{}, edge_color_seen{};
        int rank6_distinct = 0, johnson_edges = 0, edge_colors = 0;
        for (const auto& component : parity) {
            for (Mask value : component)
                if (!rank6_seen[value]++) ++rank6_distinct;
            for (int i = 0; i < static_cast<int>(component.size()); ++i) {
                const Mask a = component[i];
                const Mask b = component[(i + 1) % component.size()];
                if (pc(static_cast<Mask>(a ^ b)) == 2) ++johnson_edges;
                const Mask color = static_cast<Mask>(a & b);
                if (pc(color) == 5 && !edge_color_seen[color]++) ++edge_colors;
            }
        }

        cout << "PASS O6 vertices=462 edges=" << disjoint_edges
             << " transition_rank4=" << transition_distinct << "/330\n";
        cout << "parity_lift rank6=" << rank6_distinct << "/462"
             << " johnson_edges=" << johnson_edges << "/462"
             << " rank5_colors=" << edge_colors << "/462\n";
        array<int, 7> deep_counts{};
        for (int length = 3; length <= 6; ++length) {
            const int rank = 7 - length;
            array<uint8_t, LIMIT> seen{};
            int distinct = 0;
            for (const auto& component : parity) {
                for (int start = 0; start < static_cast<int>(component.size()); ++start) {
                    Mask value = static_cast<Mask>(FULL);
                    for (int step = 0; step < length; ++step)
                        value &= component[(start + step) % component.size()];
                    if (pc(value) == rank && !seen[value]++) ++distinct;
                }
            }
            cout << "intersection_length=" << length << " rank=" << rank
                 << " distinct=" << distinct << '/' << choose(K, rank) << '\n';
            deep_counts[length] = distinct;
        }
        if (transition_distinct != 330 || rank6_distinct != 462 ||
            johnson_edges != 462 || edge_colors != 462)
            return 1;
        if (require_deep)
            for (int length = 3; length <= 6; ++length)
                if (deep_counts[length] != choose(K, 7 - length)) return 1;
        return 0;
    } catch (const exception& error) {
        cerr << "error: " << error.what() << '\n';
        return 2;
    }
}
