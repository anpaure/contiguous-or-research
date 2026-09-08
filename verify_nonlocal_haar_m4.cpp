#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <vector>

using Order = std::array<int,9>;
using Mask = std::uint16_t;

static const std::array<Order,4> negative = {{
    {1,8,6,7,4,5,3,9,2},
    {1,9,8,6,7,4,5,2,3},
    {1,5,3,9,8,6,7,2,4},
    {1,7,3,9,4,5,8,2,6},
}};

static const std::array<Order,4> positive = {{
    {1,9,3,5,4,7,6,8,2},
    {1,5,4,7,6,8,9,2,3},
    {1,7,6,8,9,3,5,2,4},
    {1,8,5,4,9,3,7,2,6},
}};

static const std::array<Order,10> common = {{
    {1,4,6,9,7,8,5,3,2},
    {1,6,5,7,3,9,8,4,2},
    {1,3,8,6,7,5,9,4,2},
    {1,4,6,2,8,9,5,7,3},
    {1,4,6,5,2,9,7,8,3},
    {1,5,4,2,6,9,7,8,3},
    {1,8,6,7,5,9,2,3,4},
    {1,8,7,9,4,2,5,3,6},
    {1,7,2,3,5,9,8,4,6},
    {1,8,7,9,2,3,4,5,6},
}};

static Mask interval(const Order& q, int start, int rank) {
    Mask s = 0;
    for (int j=0;j<rank;++j)
        s |= Mask{1} << (q[(start+2*j)%9]-1);
    return s;
}

static std::map<Mask,int> effect(int rank) {
    std::map<Mask,int> d;
    for (const auto& q: positive)
        for (int i=0;i<9;++i) ++d[interval(q,i,rank)];
    for (const auto& q: negative)
        for (int i=0;i<9;++i) --d[interval(q,i,rank)];
    for (auto it=d.begin();it!=d.end();)
        if (it->second==0) it=d.erase(it); else ++it;
    return d;
}

template<class Side> static void check_partial(const Side& side) {
    std::set<Mask> seen;
    for (const auto& q: side)
        for (int i=0;i<9;++i)
            assert(seen.insert(interval(q,i,4)).second);
}

template<class Changed> static void check_exact(const Changed& changed) {
    std::set<Mask> seen;
    for (const auto& q: common)
        for (int i=0;i<9;++i)
            assert(seen.insert(interval(q,i,4)).second);
    for (const auto& q: changed)
        for (int i=0;i<9;++i)
            assert(seen.insert(interval(q,i,4)).second);
    assert(seen.size()==126);
}

int main() {
    check_partial(negative);
    check_partial(positive);
    check_exact(negative);
    check_exact(positive);
    assert(effect(4).empty());
    assert(effect(3).empty());
    assert(!effect(2).empty());
    for (int r=1;r<=4;++r) {
        auto d=effect(r);
        std::cout << "rank " << r << " support " << d.size() << ':';
        for (auto [s,c]:d) {
            std::cout << (c>0?" +{":" -{");
            for (int b=0;b<9;++b) if ((s>>b)&1) std::cout << b+1 << '.';
            std::cout << '}';
        }
        std::cout << '\n';
    }
}
