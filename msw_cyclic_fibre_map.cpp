#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>

using U32 = std::uint32_t;

static std::pair<U32, int> apply_g(U32 x, int m) {
    std::vector<int> before(2 * m);
    int height = 0, down_zero = 0;
    for (int i = 0; i < 2 * m; ++i) {
        before[i] = height;
        if (((x >> i) & 1U) == 0 && height == 0) ++down_zero;
        height += ((x >> i) & 1U) ? 1 : -1;
    }
    int ordinal = 0;
    for (int i = 0; i < 2 * m; ++i)
        if (((x >> i) & 1U) == 0 && (before[i] == 0 || before[i] == 1))
            if (++ordinal == down_zero + 1) return {x | (U32{1} << i), i};
    assert(false);
    return {};
}

static std::pair<U32, int> apply_h(U32 y, int m) {
    std::vector<int> before(2 * m);
    int height = 0, up_one = 0;
    for (int i = 0; i < 2 * m; ++i) {
        before[i] = height;
        if (((y >> i) & 1U) && height == 1) ++up_one;
        height += ((y >> i) & 1U) ? 1 : -1;
    }
    int ordinal = 0;
    for (int i = 0; i < 2 * m; ++i)
        if (((y >> i) & 1U) && (before[i] == 0 || before[i] == 1))
            if (++ordinal == up_one) return {y & ~(U32{1} << i), i};
    assert(false);
    return {};
}

static std::string bits(U32 x, int length) {
    std::string out;
    for (int i = 0; i < length; ++i)
        out.push_back(((x >> i) & 1U) ? '1' : '0');
    return out;
}

struct Factor {
    int m;
    std::vector<int> owner;
    std::vector<U32> roots;

    explicit Factor(int dimension)
        : m(dimension), owner(U32{1} << (2 * m), -1) {
        generate(0, 0, 0, 0);
    }

    void add(U32 root) {
        int id = static_cast<int>(roots.size());
        roots.push_back(root);
        U32 x = root;
        assert(owner[x] < 0);
        owner[x] = id;
        for (int i = 0; i < m; ++i) {
            x = apply_g(x, m).first;
            assert(owner[x] < 0);
            owner[x] = id;
            x = apply_h(x, m).first;
            assert(owner[x] < 0);
            owner[x] = id;
        }
    }

    void generate(int position, int up, int down, U32 mask) {
        if (position == 2 * m) {
            add(mask);
            return;
        }
        if (up < m)
            generate(position + 1, up + 1, down,
                     mask | (U32{1} << position));
        if (down < up)
            generate(position + 1, up, down + 1, mask);
    }
};

int main(int argc, char** argv) {
    const int s = argc > 1 ? std::stoi(argv[1]) : 3;
    Factor small(s);
    Factor factor(s + 1);
    std::map<int, std::set<int>> image;
    std::map<int, std::set<int>> reverse_image;
    std::vector<std::set<int>> left_support(factor.roots.size());
    std::vector<std::set<int>> right_support(factor.roots.size());
    std::vector<std::map<int, int>> left_count(factor.roots.size());
    std::vector<std::map<int, int>> right_count(factor.roots.size());
    for (U32 z = 0; z < (U32{1} << (2 * s)); ++z) {
        int w = __builtin_popcount(z);
        if (w != s && w != s + 1) continue;
        U32 left = U32{1} | (z << 2);                 // 10z
        U32 right = z | (U32{1} << (2 * s + 1));     // z01
        image[factor.owner[left]].insert(factor.owner[right]);
        U32 reversed_z = 0;
        for (int i = 0; i < 2 * s; ++i)
            if ((z >> i) & 1U) reversed_z |= U32{1} << (2 * s - 1 - i);
        U32 left_reversed = U32{1} | (reversed_z << 2);
        reverse_image[factor.owner[left]].insert(factor.owner[left_reversed]);
        left_support[factor.owner[left]].insert(small.owner[z]);
        right_support[factor.owner[right]].insert(small.owner[z]);
        ++left_count[factor.owner[left]][small.owner[z]];
        ++right_count[factor.owner[right]][small.owner[z]];
    }
    int bad = 0;
    for (auto const& [source, targets] : image) {
        if (targets.size() != 1) ++bad;
        std::cout << " root=" << bits(factor.roots[source], 2 * (s + 1))
                  << " images=";
        for (int target : targets)
            std::cout << bits(factor.roots[target], 2 * (s + 1)) << ',';
        std::cout << '\n';
    }
    std::cout << "SUMMARY s=" << s << " bad=" << bad << '/' << image.size()
              << '\n';
    int reverse_bad = 0;
    for (auto const& [source, targets] : reverse_image)
        reverse_bad += targets.size() != 1;
    std::cout << "REVERSE_FIBRE bad=" << reverse_bad << '/'
              << reverse_image.size() << '\n';

    std::set<std::pair<int, int>> left_edges, right_edges;
    auto add_edges = [](std::set<std::pair<int, int>>& edges,
                        std::vector<std::set<int>> const& supports) {
        for (auto const& support : supports)
            for (int x : support) for (int y : support)
                if (x < y) edges.emplace(x, y);
    };
    add_edges(left_edges, left_support);
    add_edges(right_edges, right_support);
    int left_only = 0, right_only = 0;
    for (auto e : left_edges) left_only += !right_edges.count(e);
    for (auto e : right_edges) right_only += !left_edges.count(e);
    std::cout << "EDGE_COMPARE left=" << left_edges.size()
              << " right=" << right_edges.size()
              << " left_only=" << left_only
              << " right_only=" << right_only << '\n';
    std::map<std::pair<int, int>, int> left_gram, right_gram;
    auto add_gram = [](auto& gram, auto const& rows) {
        for (auto const& row : rows)
            for (auto const& [x, cx] : row)
                for (auto const& [y, cy] : row)
                    gram[{x, y}] += cx * cy;
    };
    add_gram(left_gram, left_count);
    add_gram(right_gram, right_count);
    int gram_diff = 0;
    for (auto const& [key, value] : left_gram)
        gram_diff += right_gram[key] != value;
    for (auto const& [key, value] : right_gram)
        gram_diff += !left_gram.count(key);
    std::cout << "GRAM_COMPARE diff=" << gram_diff
              << " entries=" << left_gram.size() << ',' << right_gram.size()
              << '\n';
    auto row_signature = [](std::map<int, int> const& row) {
        std::string out;
        for (auto const& [x, count] : row)
            out += std::to_string(x) + ':' + std::to_string(count) + ',';
        return out;
    };
    std::multiset<std::string> left_rows, right_rows;
    for (auto const& row : left_count) left_rows.insert(row_signature(row));
    for (auto const& row : right_count) right_rows.insert(row_signature(row));
    std::cout << "ROW_MULTISET equal=" << (left_rows == right_rows) << '\n';
    return bad != 0;
}
