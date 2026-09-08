// Enumerate all zero-reduced-cost chain-pair shapes for the exact c52e9 dual.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <functional>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>

using Point = std::vector<int>;
using Chain = std::vector<int>;
using Census = std::array<int, 4>;

std::vector<Point> grid(int d) {
    std::vector<Point> out(1 << (2*d), Point(d));
    for (int i=0; i<int(out.size()); ++i) {
        int x=i;
        for (int j=d-1; j>=0; --j) { out[i][j]=x%4; x/=4; }
    }
    return out;
}

std::vector<std::vector<int>> transforms(int d) {
    auto points=grid(d);
    Point p(d);
    for (int i=0; i<d; ++i) p[i]=i;
    std::vector<std::vector<int>> maps;
    do {
        std::vector<int> map(points.size());
        for (int i=0; i<int(points.size()); ++i) {
            int x=0;
            for (int j:p) x=4*x+points[i][j];
            map[i]=x;
        }
        maps.push_back(map);
    } while (std::next_permutation(p.begin(),p.end()));
    return maps;
}

Chain canonical(const Chain& c, const std::vector<std::vector<int>>& maps, bool reflection) {
    Chain best=c;
    for (const auto& map:maps) {
        Chain cc;
        for (int i:c) cc.push_back(map[i]);
        best=std::min(best,cc);
        if (reflection) {
            std::reverse(cc.begin(),cc.end());
            for (int& i:cc) i=int(map.size())-1-i;
            best=std::min(best,cc);
        }
    }
    return best;
}

int main(int argc, char** argv) {
    assert(argc==2);
    std::ofstream out(argv[1]);
    assert(out.good());
    std::map<Census,int> weights={
        {{0,2,4,0},12},{{0,3,1,2},6},{{0,3,2,1},10},{{0,3,3,0},6},
        {{0,4,0,2},4},{{0,4,1,1},5},{{0,5,0,1},13},{{1,1,2,2},6},
        {{1,1,3,1},11},{{1,2,0,3},12},{{1,2,1,2},5},{{1,2,2,1},4},
        {{1,3,0,2},3},{{2,0,1,3},12},{{2,0,2,2},6},{{2,1,1,2},2}};
    auto value=[&](const Point& x,const Point& y) {
        Census count{};
        for (int z:x) ++count[z];
        for (int z:y) ++count[z];
        auto rev=count;
        std::reverse(rev.begin(),rev.end());
        auto it=weights.find(std::min(count,rev));
        return it==weights.end()?0:it->second;
    };
    long long objective=0;
    for (const Point& p:grid(6)) objective+=value(p,{});
    assert(objective==12*1248);
    std::set<std::vector<int>> shapes;
    std::map<std::array<int,3>,long long> inventory;
    for (int r=1; r<=3; ++r) {
        auto left=grid(r), right=grid(6-r);
        const int a=int(left.size()), b=int(right.size());
        auto lm=transforms(r), rm=transforms(6-r);
        auto successors=[](const std::vector<Point>& points) {
            std::vector<std::vector<int>> result(points.size());
            for (int i=0; i<int(points.size()); ++i)
                for (int j=i+1; j<int(points.size()); ++j) {
                    bool ok=true;
                    for (int k=0; k<int(points[i].size()); ++k) ok &= points[i][k]<=points[j][k];
                    if (ok) result[i].push_back(j);
                }
            return result;
        };
        auto ls=successors(left), rs=successors(right);
        std::vector<std::vector<int>> table(a,std::vector<int>(b));
        for (int i=0;i<a;++i) for (int j=0;j<b;++j) table[i][j]=value(left[i],right[j]);
        std::vector<int> sums(b), best(b);
        std::vector<uint64_t> counts(b);
        Chain c, d;
        long long total=0, representatives=0, tightleft=0;
        uint64_t pairs=0;
        auto emit=[&]() {
            Chain cc=canonical(c,lm,false), dd=canonical(d,rm,false);
            Chain cr=c, dr=d;
            std::reverse(cr.begin(),cr.end());
            std::reverse(dr.begin(),dr.end());
            for (int& x:cr) x=a-1-x;
            for (int& x:dr) x=b-1-x;
            cr=canonical(cr,lm,false); dr=canonical(dr,rm,false);
            auto pair=std::make_pair(cc,dd), refl=std::make_pair(cr,dr);
            if (r==3) {
                pair=std::min(pair,std::make_pair(dd,cc));
                refl=std::min(refl,std::make_pair(dr,cr));
            }
            pair=std::min(pair,refl);
            cc=pair.first; dd=pair.second;
            std::vector<int> key{r,int(cc.size())};
            key.insert(key.end(),cc.begin(),cc.end());
            key.push_back(int(dd.size()));
            key.insert(key.end(),dd.begin(),dd.end());
            if (!shapes.insert(key).second) return;
            ++inventory[{r,int(cc.size()),int(dd.size())}];
            out << r << ' ' << cc.size();
            for (int x:cc) out << ' ' << x;
            out << ' ' << dd.size();
            for (int x:dd) out << ' ' << x;
            out << '\n';
        };
        std::function<void(int,int)> walkright=[&](int j,int required) {
            assert(sums[j]>=12 && best[j]==required);
            d.push_back(j);
            required-=sums[j]-12;
            if (required==0) emit();
            for (int k:rs[j]) if (sums[k]>=12 && best[k]==required) walkright(k,required);
            d.pop_back();
        };
        std::function<void(int)> extend=[&](int i) {
            c.push_back(i); ++total;
            for (int j=0;j<b;++j) sums[j]+=table[i][j];
            if (canonical(c,lm,true)==c) {
                ++representatives;
                int optimum=0;
                for (int j=b-1;j>=0;--j) {
                    best[j]=-100000; counts[j]=0;
                    if (sums[j]<12) continue;
                    int following=0;
                    for (int k:rs[j]) following=std::max(following,best[k]);
                    best[j]=sums[j]-12+following;
                    counts[j]=following==0;
                    for (int k:rs[j]) if (best[k]==following) counts[j]+=counts[k];
                    optimum=std::max(optimum,best[j]);
                }
                assert(optimum<=12*int(c.size()));
                if (optimum==12*int(c.size())) {
                    ++tightleft;
                    for (int j=0;j<b;++j) if (best[j]==optimum) {
                        pairs+=counts[j];
                        walkright(j,optimum);
                    }
                }
            }
            for (int j:ls[i]) extend(j);
            for (int j=0;j<b;++j) sums[j]-=table[i][j];
            c.pop_back();
        };
        for (int i=0;i<a;++i) extend(i);
        std::cout << "split=" << r << '+' << 6-r << " all_left=" << total
                  << " canonical_left=" << representatives << " tight_left=" << tightleft
                  << " tight_pairs_before_right_quotient=" << pairs
                  << " cumulative_shapes=" << shapes.size() << std::endl;
    }
    for (const auto& [shape,count]:inventory)
        std::cout << "shape " << shape[0] << ' ' << shape[1] << ' ' << shape[2] << " : " << count << '\n';
    std::cout << "PASS exact tight-shape enumeration, shapes=" << shapes.size() << std::endl;
}
