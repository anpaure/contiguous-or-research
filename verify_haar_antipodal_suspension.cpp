#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <vector>

using Mask = std::uint16_t;
using OldOrder = std::array<int, 9>;

static const std::array<OldOrder, 4> negative = {{
    {1,8,6,7,4,5,3,9,2},
    {1,9,8,6,7,4,5,2,3},
    {1,5,3,9,8,6,7,2,4},
    {1,7,3,9,4,5,8,2,6},
}};

static const std::array<OldOrder, 4> positive = {{
    {1,9,3,5,4,7,6,8,2},
    {1,5,4,7,6,8,9,2,3},
    {1,7,6,8,9,3,5,2,4},
    {1,8,5,4,9,3,7,2,6},
}};

static std::vector<int> interval_cycle(const OldOrder& q) {
    std::vector<int> c(q.size());
    for (int i = 0; i < static_cast<int>(q.size()); ++i)
        c[i] = q[(2 * i) % q.size()];
    return c;
}

static Mask interval(const std::vector<int>& c, int start, int rank) {
    Mask out = 0;
    for (int j = 0; j < rank; ++j)
        out |= Mask{1} << (c[(start + j) % c.size()] - 1);
    return out;
}

static std::vector<std::vector<int>> antipodal_extensions(
        const std::vector<int>& c) {
    const int n = c.size();
    const int m = (n - 1) / 2;
    std::vector<std::vector<int>> out;
    for (int point = 0; point < n; ++point) {
        const int other = (point + m) % n;
        std::vector<int> q;
        for (int i = 0; i < n; ++i) {
            q.push_back(c[i]);
            if (i == point) q.push_back(n + 1);
            if (i == other) q.push_back(n + 2);
        }
        out.push_back(std::move(q));
    }
    return out;
}

template<class Side>
static std::map<Mask, int> old_effect(int rank, const Side& plus,
                                     const Side& minus) {
    std::map<Mask, int> out;
    for (const auto& q : plus) {
        auto c = interval_cycle(q);
        for (int i = 0; i < 9; ++i) ++out[interval(c, i, rank)];
    }
    for (const auto& q : minus) {
        auto c = interval_cycle(q);
        for (int i = 0; i < 9; ++i) --out[interval(c, i, rank)];
    }
    for (auto it = out.begin(); it != out.end();)
        if (it->second == 0) it = out.erase(it); else ++it;
    return out;
}

template<class Side>
static std::map<Mask, int> lifted_effect(int rank, const Side& plus,
                                        const Side& minus) {
    std::map<Mask, int> out;
    for (const auto& q : plus)
        for (const auto& e : antipodal_extensions(interval_cycle(q)))
            for (int i = 0; i < 11; ++i) ++out[interval(e, i, rank)];
    for (const auto& q : minus)
        for (const auto& e : antipodal_extensions(interval_cycle(q)))
            for (int i = 0; i < 11; ++i) --out[interval(e, i, rank)];
    for (auto it = out.begin(); it != out.end();)
        if (it->second == 0) it = out.erase(it); else ++it;
    return out;
}

int main() {
    const auto old4 = old_effect(4, positive, negative);
    const auto old3 = old_effect(3, positive, negative);
    const auto old2 = old_effect(2, positive, negative);
    assert(old4.empty() && old3.empty() && !old2.empty());

    assert(lifted_effect(5, positive, negative).empty());
    assert(lifted_effect(4, positive, negative).empty());
    const auto lifted3 = lifted_effect(3, positive, negative);

    std::map<Mask, int> expected;
    for (auto [u, coefficient] : old2) {
        expected[u | (Mask{1} << 9)] = 3 * coefficient;
        expected[u | (Mask{1} << 10)] = 3 * coefficient;
    }
    assert(lifted3 == expected);

    // The linear suspension is not a packing: for one old middle interval,
    // each one-new middle target occurs m+1=5 times over all pointings.
    const auto c = interval_cycle(negative.front());
    const Mask s = interval(c, 0, 4);
    int multiplicity_x = 0, multiplicity_y = 0;
    for (const auto& e : antipodal_extensions(c)) {
        for (int i = 0; i < 11; ++i) {
            const Mask z = interval(e, i, 5);
            multiplicity_x += z == (s | (Mask{1} << 9));
            multiplicity_y += z == (s | (Mask{1} << 10));
        }
    }
    assert(multiplicity_x == 5 && multiplicity_y == 5);

    std::cout << "old_B2_support=" << old2.size()
              << " lifted_B3_support=" << lifted3.size()
              << " middle_multiplicity=" << multiplicity_x
              << " verified\n";
}
