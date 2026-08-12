#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <tuple>
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

struct Occurrence { int side, order, start; };

int main() {
    constexpr int n = 9;
    std::array<std::vector<int>, 8> cycles;
    for (int i = 0; i < 4; ++i) cycles[i] = interval_cycle(negative[i]);
    for (int i = 0; i < 4; ++i) cycles[4+i] = interval_cycle(positive[i]);

    std::map<Mask,std::vector<Occurrence>> by_middle;
    for (int v = 0; v < 8; ++v)
        for (int s = 0; s < n; ++s)
            by_middle[interval(cycles[v],s,4)].push_back(
                Occurrence{v >= 4,v,s});

    std::array<std::vector<std::pair<int,int>>,8> graph;
    int malformed = 0;
    for (const auto& [target, occ] : by_middle) {
        (void)target;
        if (occ.size() != 2 || occ[0].side == occ[1].side) {
            ++malformed;
            continue;
        }
        Occurrence a=occ[0], b=occ[1];
        if (a.side) std::swap(a,b);
        const int voltage = (b.start-a.start+n)%n;
        graph[a.order].push_back({b.order,voltage});
        graph[b.order].push_back({a.order,(n-voltage)%n});
    }
    assert(malformed == 0);

    std::array<int,8> potential;
    potential.fill(-1);
    int components=0, bad_edges=0;
    for (int source=0;source<8;++source) if (potential[source]<0) {
        ++components;
        potential[source]=0;
        std::queue<int> q;
        q.push(source);
        while(!q.empty()) {
            int u=q.front(); q.pop();
            for(auto [v,gamma]:graph[u]) {
                int want=(potential[u]+gamma)%n;
                if(potential[v]<0){potential[v]=want;q.push(v);}
                else bad_edges += potential[v]!=want;
            }
        }
    }

    std::map<Mask,std::array<std::map<int,int>,2>> lower_hist;
    for (int v=0;v<8;++v)
        for(int s=0;s<n;++s) {
            const Mask target=interval(cycles[v],s,3);
            const int offset=(potential[v]-s+n)%n;
            ++lower_hist[target][v>=4][offset];
        }
    int bad_targets=0, l1=0;
    for(const auto& [target,h]:lower_hist) {
        (void)target;
        if(h[0]!=h[1]) ++bad_targets;
        std::map<int,int> delta=h[0];
        for(auto [x,c]:h[1]) delta[x]-=c;
        for(auto [x,c]:delta){(void)x;l1+=std::abs(c);}
    }

    std::cout << "middle_targets=" << by_middle.size()
              << " components=" << components
              << " inconsistent_directed_edges=" << bad_edges
              << " lower_bad_targets=" << bad_targets
              << " lower_hist_l1=" << l1
              << " potentials=";
    for(int x:potential) std::cout << x << ',';
    std::cout << '\n';
    return 0;
}
