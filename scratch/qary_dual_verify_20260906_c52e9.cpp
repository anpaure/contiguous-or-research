// Exact all-chain-pair dual certificates on [3]^6 and [4]^6.
#include <algorithm>
#include <array>
#include <cassert>
#include <functional>
#include <iostream>
#include <map>
#include <vector>

using Point = std::vector<int>;
using Census = std::array<int, 4>;

std::vector<Point> grid(int q, int d) {
    int n=1;
    for (int i=0;i<d;++i) n*=q;
    std::vector<Point> points(n,Point(d));
    for (int i=0;i<n;++i) {
        int x=i;
        for (int j=d-1;j>=0;--j) { points[i][j]=x%q; x/=q; }
    }
    return points;
}

void verify(int q) {
    std::map<Census,int> weight;
    if (q==3) {
        weight={{{0,5,1,0},4},{{0,6,0,0},24},{{1,3,2,0},8},
                {{1,4,1,0},16},{{2,1,3,0},12},{{2,2,2,0},8}};
    } else {
        weight={{{0,2,4,0},12},{{0,3,1,2},6},{{0,3,2,1},10},{{0,3,3,0},6},
                {{0,4,0,2},4},{{0,4,1,1},5},{{0,5,0,1},13},{{1,1,2,2},6},
                {{1,1,3,1},11},{{1,2,0,3},12},{{1,2,1,2},5},{{1,2,2,1},4},
                {{1,3,0,2},3},{{2,0,1,3},12},{{2,0,2,2},6},{{2,1,1,2},2}};
    }
    auto value=[&](const Point& x,const Point& y) {
        Census count{};
        for (int z:x) ++count[z];
        for (int z:y) ++count[z];
        Census reversed=count;
        std::reverse(reversed.begin(),reversed.begin()+q);
        auto it=weight.find(std::min(count,reversed));
        return it==weight.end()?0:it->second;
    };
    long long objective=0;
    for (const Point& point:grid(q,6)) objective+=value(point,{});
    assert(objective==12*(q==3?306:1248));
    for (int r=1;r<=3;++r) {
        auto left=grid(q,r), right=grid(q,6-r);
        int a=int(left.size()), b=int(right.size());
        std::vector<std::vector<int>> successors(a), predecessors(b);
        for (int i=0;i<a;++i) for (int j=i+1;j<a;++j) {
            bool valid=true;
            for (int t=0;t<r;++t) valid &= left[i][t]<=left[j][t];
            if (valid) successors[i].push_back(j);
        }
        for (int j=0;j<b;++j) {
            int stride=1;
            for (int t=5-r;t>=0;--t) {
                if (right[j][t]) predecessors[j].push_back(j-stride);
                stride*=q;
            }
        }
        std::vector<std::vector<int>> table(a,std::vector<int>(b));
        for (int i=0;i<a;++i) for (int j=0;j<b;++j) table[i][j]=value(left[i],right[j]);
        std::vector<int> sums(b), best(b);
        long long count=0;
        std::function<void(int,int)> extend=[&](int i,int length) {
            for (int j=0;j<b;++j) sums[j]+=table[i][j];
            for (int j=0;j<b;++j) {
                int previous=0;
                for (int p:predecessors[j]) previous=std::max(previous,best[p]);
                best[j]=previous+std::max(0,sums[j]-12);
            }
            assert(best.back()<=12*length);
            ++count;
            for (int j:successors[i]) extend(j,length+1);
            for (int j=0;j<b;++j) sums[j]-=table[i][j];
        };
        for (int i=0;i<a;++i) extend(i,1);
        const long long counts3[]={7,103,3271}, counts4[]={15,1007,257295};
        assert(count==(q==3?counts3[r-1]:counts4[r-1]));
        std::cout<<"q="<<q<<" split="<<r<<"+"<<6-r<<": "<<count<<" left chains; all right chains verified\n";
    }
    std::cout<<"PASS exact fractional-cover lower bound "<<objective<<"/12="<<objective/12<<"\n";
}

int main() { verify(3); verify(4); }
