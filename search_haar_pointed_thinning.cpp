#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
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

static std::vector<int> extend(const std::vector<int>& c, int point,
                               int distance = 4) {
    const int n = static_cast<int>(c.size());
    const int other = (point + distance) % n;
    std::vector<int> out;
    for (int i = 0; i < n; ++i) {
        out.push_back(c[i]);
        if (i == point) out.push_back(10);
        if (i == other) out.push_back(11);
    }
    return out;
}

static Mask interval(const std::vector<int>& c, int start, int rank) {
    Mask out = 0;
    for (int j = 0; j < rank; ++j)
        out |= Mask{1} << (c[(start + j) % c.size()] - 1);
    return out;
}

struct Lift {
    std::array<std::array<std::vector<Mask>,18>,4> rows;
};

static Lift make_lift(const std::array<OldOrder,4>& side) {
    Lift out;
    for (int i = 0; i < 4; ++i) {
        const auto old = interval_cycle(side[i]);
        for (int choice = 0; choice < 18; ++choice) {
            const int p=choice%9, distance=choice<9?4:5;
            const auto e = extend(old,p,distance);
            auto& flat = out.rows[i][choice];
            for (int rank : {5,4,3})
                for (int s = 0; s < 11; ++s)
                    flat.push_back(interval(e,s,rank));
        }
    }
    return out;
}

using Key = std::vector<Mask>;

static bool signature(const Lift& lift, const std::array<int,4>& points,
                      Key& key, std::vector<Mask>* rank3 = nullptr) {
    std::vector<Mask> middle, lower, deep;
    for (int i = 0; i < 4; ++i) {
        const auto& row = lift.rows[i][points[i]];
        middle.insert(middle.end(),row.begin(),row.begin()+11);
        lower.insert(lower.end(),row.begin()+11,row.begin()+22);
        deep.insert(deep.end(),row.begin()+22,row.end());
    }
    std::sort(middle.begin(),middle.end());
    if (std::adjacent_find(middle.begin(),middle.end()) != middle.end())
        return false;
    std::sort(lower.begin(),lower.end());
    key=middle;
    for(Mask x:lower) key.push_back(Mask(x | (Mask{1}<<12)));
    if(rank3){std::sort(deep.begin(),deep.end());*rank3=std::move(deep);}
    return true;
}

static std::array<int,4> decode(int code, int radix) {
    std::array<int,4> out{};
    for(int i=0;i<4;++i){out[i]=code%radix;code/=radix;}
    return out;
}

int main() {
    const Lift nl=make_lift(negative), pl=make_lift(positive);
    {
        const auto c=interval_cycle(negative[0]);
        const Mask s=interval(c,0,4);
        std::cout << "local_middle_signature=";
        for(int p=0;p<9;++p){
            const auto e=extend(c,p,4);
            bool has_x=false,has_y=false;
            for(int i=0;i<11;++i){
                Mask z=interval(e,i,5);
                has_x |= z==Mask(s|(Mask{1}<<9));
                has_y |= z==Mask(s|(Mask{1}<<10));
            }
            std::cout << p << ':' << has_x << has_y << ',';
        }
        std::cout << '\n';
    }
    std::map<Key,int> negative_keys;
    int negative_packings=0, positive_packings=0, matches=0, deep_nonzero=0;
    constexpr int radix=18;
    constexpr int combinations=radix*radix*radix*radix;
    for(int code=0;code<combinations;++code){
        auto p=decode(code,radix); Key key;
        if(!signature(nl,p,key)) continue;
        ++negative_packings;
        negative_keys.try_emplace(std::move(key),code);
    }
    for(int code=0;code<combinations;++code){
        auto pp=decode(code,radix); Key key; std::vector<Mask> pd;
        if(!signature(pl,pp,key,&pd)) continue;
        ++positive_packings;
        auto found=negative_keys.find(key);
        if(found==negative_keys.end()) continue;
        ++matches;
        auto np=decode(found->second,radix); Key ignored; std::vector<Mask> nd;
        assert(signature(nl,np,ignored,&nd));
        if(nd==pd) continue;
        ++deep_nonzero;
        std::cout << "FOUND negative=";
        for(int x:np)std::cout<<x<<',';
        std::cout<<" positive=";
        for(int x:pp)std::cout<<x<<',';
        std::cout<<" deep_equal=0\n";
        break;
    }
    std::cout << "negative_packings=" << negative_packings
              << " negative_signatures=" << negative_keys.size()
              << " positive_packings=" << positive_packings
              << " top_matches=" << matches
              << " deep_nonzero=" << deep_nonzero << '\n';
}
