#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <functional>
#include <iostream>
#include <string>
#include <tuple>
#include <unordered_map>
#include <utility>
#include <vector>

// Emit the exact oriented highest-valley separated-port CSP.
// By default both orientations are included; an optional final argument
// "canonical" restricts both endpoints to orientation zero.
// Run only on H100.  Each option is
// (child,parent,child_orientation,child_port,parent_orientation,parent_port).

using U = std::uint64_t;

static std::pair<U, int> g(U x, int m) {
    std::vector<int> before(2 * m);
    int h = 0, d0 = 0;
    for (int i = 0; i < 2 * m; ++i) {
        before[i] = h;
        if (((x >> i) & 1U) == 0 && h == 0) ++d0;
        h += (x >> i) & 1U ? 1 : -1;
    }
    int seen = 0;
    for (int i = 0; i < 2 * m; ++i)
        if (((x >> i) & 1U) == 0 &&
            (before[i] == 0 || before[i] == 1) && ++seen == d0 + 1)
            return {x | (U{1} << i), i};
    assert(false); return {};
}

static std::pair<U, int> hmap(U y, int m) {
    std::vector<int> before(2 * m);
    int h = 0, u1 = 0;
    for (int i = 0; i < 2 * m; ++i) {
        before[i] = h;
        if (((y >> i) & 1U) != 0 && h == 1) ++u1;
        h += (y >> i) & 1U ? 1 : -1;
    }
    int seen = 0;
    for (int i = 0; i < 2 * m; ++i)
        if (((y >> i) & 1U) != 0 &&
            (before[i] == 0 || before[i] == 1) && ++seen == u1)
            return {y & ~(U{1} << i), i};
    assert(false); return {};
}

static std::vector<int> tight_order(U root, int m) {
    U x = root;
    const int n = 2 * m + 1;
    std::vector<int> rho;
    for (int e = 0; e < m; ++e) {
        auto a = g(x, m); auto b = hmap(a.first, m);
        rho.push_back(a.second); rho.push_back(b.second); x = b.first;
    }
    rho.push_back(2 * m);
    std::vector<int> tight(n);
    for (int j = 0; j < n; ++j) tight[j] = rho[(2 * j) % n];
    return tight;
}

static std::vector<U> signatures(const std::vector<int>& row, int d, int s) {
    const int n = static_cast<int>(row.size());
    assert(10 * d <= 64);
    std::vector<U> answer(n);
    for (int a = 0; a < n; ++a) {
        U word = 0;
        for (int j = 0; j < d; ++j) {
            int x = row[(a + j) % n], y = row[(a + s - 1 + j) % n];
            if (x > y) std::swap(x, y);
            word |= U(32 * x + y) << (10 * j);
        }
        answer[a] = word;
    }
    return answer;
}

static std::array<std::vector<U>,2> oriented_signatures(
    std::vector<int> row,int d,int s) {
    std::array<std::vector<U>,2> out;
    out[0]=signatures(row,d,s);
    std::reverse(row.begin(),row.end());
    out[1]=signatures(row,d,s);
    return out;
}

int main(int argc, char** argv) {
    assert(argc >= 4);
    const int m = std::stoi(argv[1]), d = std::stoi(argv[2]);
    const std::string output = argv[3];
    const bool canonical_only = argc > 4 && std::string(argv[4]) == "canonical";
    const int n = 2 * m + 1, s = m + 1 - d;
    // The packed signature uses one ten-bit field 32*x+y per rail.
    assert(n <= 32 && 10 * d <= 64);

    std::vector<U> roots;
    std::function<void(int,int,int,U)> gen = [&](int pos,int up,int down,U x) {
        if (pos == 2 * m) { roots.push_back(x); return; }
        if (up < m) gen(pos+1,up+1,down,x|(U{1}<<pos));
        if (down < up) gen(pos+1,up,down+1,x);
    };
    gen(0,0,0,0);
    std::unordered_map<U,int> index;
    index.reserve(2*roots.size());
    for (int i=0;i<(int)roots.size();++i) index[roots[i]]=i;

    std::vector<std::array<std::vector<U>,2>> sig(roots.size());
    for (int i=0;i<(int)roots.size();++i)
        sig[i]=oriented_signatures(tight_order(roots[i],m),d,s);

    using Option=std::tuple<int,int,int,int,int,int>;
    std::vector<Option> options;
    const int root_id=index.at((U{1}<<m)-1);
    for (int child=0;child<(int)roots.size();++child) {
        if (child==root_id) continue;
        U x=roots[child]; int height=0, maximum=-1;
        std::vector<int> valleys;
        for (int v=0;v+1<2*m;++v) {
            if (((x>>v)&3U)==2U) {
                if (height>maximum) { maximum=height; valleys.clear(); }
                if (height==maximum) valleys.push_back(v);
            }
            height+=(x>>v)&1U?1:-1;
        }
        assert(!valleys.empty());
        std::vector<std::pair<int,int>> moves;
        for (int valley : valleys) {
            moves.push_back({valley,valley+1});
            bool left=valley>0 && ((x>>(valley-1))&1U)==0;
            bool right=valley+2<2*m && ((x>>(valley+2))&1U)!=0;
            if(left)moves.push_back({valley-1,valley+1});
            if(right)moves.push_back({valley,valley+2});
            if(left&&right)moves.push_back({valley-1,valley+2});
        }
        for(auto [p,q]:moves) {
            int parent=index.at(x^(U{1}<<p)^(U{1}<<q));
            for(int oc=0;oc<(canonical_only?1:2);++oc)
            for(int op=0;op<(canonical_only?1:2);++op)
            for(int a=0;a<n;++a)for(int b=0;b<n;++b)
                if(sig[child][oc][a]==sig[parent][op][b])
                    options.emplace_back(child,parent,oc,a,op,b);
        }
    }
    std::sort(options.begin(),options.end());
    options.erase(std::unique(options.begin(),options.end()),options.end());
    std::ofstream out(output);
    out<<"H "<<m<<' '<<d<<' '<<n<<' '<<roots.size()<<' '<<root_id<<' '
       <<options.size()<<'\n';
    for(auto [c,p,oc,a,op,b]:options)
        out<<"O "<<c<<' '<<p<<' '<<oc<<' '<<a<<' '<<op<<' '<<b<<'\n';
    out.close();
    std::cout<<"m="<<m<<" d="<<d<<" roots="<<roots.size()
             <<" root="<<root_id<<" options="<<options.size()<<'\n';
}
