// Complete tight-shape census quotient; used only as a necessary relaxation.
#include <algorithm>
#include <array>
#include <cassert>
#include <fstream>
#include <iostream>
#include <map>
#include <vector>

using Census=std::array<int,4>;

int main(int argc,char** argv) {
    assert(argc==3);
    std::map<Census,int> population,indices;
    auto census=[](int x,int r) {
        Census c{};
        for (int i=0;i<r;++i) { ++c[x%4]; x/=4; }
        return c;
    };
    auto canonical=[](Census c) {
        auto rev=c;
        std::reverse(rev.begin(),rev.end());
        return std::min(c,rev);
    };
    for (int x=0;x<4096;++x) ++population[canonical(census(x,6))];
    int index=0;
    for (auto [c,n]:population) indices[c]=index++;
    std::map<std::vector<int>,std::pair<int,int>> columns;
    std::ifstream input(argv[1]);
    std::ofstream output(argv[2]);
    assert(input.good() && output.good());
    int r,n,m,row=0;
    while (input>>r>>n) {
        ++row;
        std::vector<int> c(n);
        for (int& x:c) input>>x;
        input>>m;
        std::vector<int> d(m);
        for (int& x:d) input>>x;
        std::vector<int> counts(index);
        for (int x:c) for (int y:d) {
            auto a=census(x,r),b=census(y,6-r);
            for (int j=0;j<4;++j) a[j]+=b[j];
            ++counts[indices.at(canonical(a))];
        }
        auto it=columns.find(counts);
        if (it==columns.end() || it->second.first>n+m) columns[counts]={n+m,row};
    }
    output<<index<<' '<<columns.size()<<'\n';
    for (auto [c,n]:population) {
        for (int x:c) output<<x<<' ';
        output<<n<<'\n';
    }
    for (const auto& [counts,record]:columns) {
        output<<record.first<<' '<<record.second;
        for (int n:counts) output<<' '<<n;
        output<<'\n';
    }
    std::cout<<"all shapes="<<row<<" distinct census columns="<<columns.size()<<" orbits="<<index<<'\n';
}
