#include <algorithm>
#include <bit>
#include <cstdint>
#include <iostream>
#include <queue>
#include <set>
#include <vector>

using Mask = std::uint32_t;
using Chain = std::vector<Mask>;

static std::vector<Chain> scd(int k) {
    std::vector<Chain> chains(1, Chain{0});
    for (int b = 0; b < k; ++b) {
        const Mask z = Mask{1} << b;
        std::vector<Chain> next;
        next.reserve(chains.size() * 2);
        for (const Chain &c : chains) {
            Chain long_chain = c;
            long_chain.push_back(c.back() | z);
            next.push_back(std::move(long_chain));
            if (c.size() >= 2) {
                Chain short_chain;
                short_chain.reserve(c.size() - 1);
                for (std::size_t i = 0; i + 1 < c.size(); ++i)
                    short_chain.push_back(c[i] | z);
                next.push_back(std::move(short_chain));
            }
        }
        chains.swap(next);
    }
    return chains;
}

struct Digraph {
    std::vector<std::vector<int>> adj;
    std::set<std::pair<int,int>> edge_set;
    explicit Digraph(int n) : adj(n) {}
    void add(int u, int v) {
        if (u == v) return;
        if (edge_set.emplace(u,v).second) adj[u].push_back(v);
    }
};

static std::vector<std::vector<int>> sccs(const Digraph &g) {
    const int n = (int)g.adj.size();
    std::vector<std::vector<int>> radj(n);
    for (int u=0;u<n;++u) for(int v:g.adj[u]) radj[v].push_back(u);
    std::vector<char> seen(n);
    std::vector<int> order;
    auto dfs1 = [&](auto &&self,int u)->void {
        seen[u]=1;
        for(int v:g.adj[u]) if(!seen[v]) self(self,v);
        order.push_back(u);
    };
    for(int u=0;u<n;++u) if(!seen[u]) dfs1(dfs1,u);
    std::fill(seen.begin(),seen.end(),0);
    std::vector<std::vector<int>> out;
    auto dfs2 = [&](auto &&self,int u,std::vector<int>& c)->void {
        seen[u]=1;c.push_back(u);
        for(int v:radj[u]) if(!seen[v]) self(self,v,c);
    };
    std::reverse(order.begin(),order.end());
    for(int u:order) if(!seen[u]) { out.emplace_back(); dfs2(dfs2,u,out.back()); }
    return out;
}

int main(int argc,char**argv) {
    int maxk=argc>1?std::stoi(argv[1]):12;
    for(int k=1;k<=maxk;++k) {
        auto C=scd(k);
        const int W=(int)C.size(), N=1<<k;
        const Mask full=N-1;
        std::vector<int> owner(N,-1);
        for(int i=0;i<W;++i) for(Mask x:C[i]) owner[x]=i;
        Digraph right_order(W), left_order(W);
        std::vector<int> rmin(W),rmout(W);
        int bad_pairs=0, max_pair=0;
        std::vector<int> pair_count(W*W);
        for(int x=1;x<N;++x) {
            int l=owner[x], r=owner[full^Mask(x)];
            max_pair=std::max(max_pair,++pair_count[l*W+r]);
        }
        for(int z:pair_count) if(z>1) ++bad_pairs;
        // Along each punctured left chain, right-chain indices increase with rank.
        for(const Chain& c:C) {
            int prev=-1;
            for(Mask x:c) if(x) {
                int r=owner[full^x];
                if(prev>=0) { right_order.add(prev,r); ++rmout[prev]; ++rmin[r]; }
                prev=r;
            }
        }
        // Along each punctured right chain, left-chain indices decrease with rank.
        // An ascending right chain is complements of an original chain in reverse.
        for(const Chain& c:C) {
            int prev=-1; // low rank to high rank in right chain
            for(auto it=c.rbegin();it!=c.rend();++it) {
                Mask x=full^*it;
                if(!x) continue;
                int l=owner[x];
                if(prev>=0) left_order.add(l,prev); // current high-rank left < previous low-rank left
                prev=l;
            }
        }
        auto rs=sccs(right_order), ls=sccs(left_order);
        int rcyc=0,rmax=0,lcyc=0,lmax=0;
        for(auto&s:rs) if(s.size()>1){++rcyc;rmax=std::max(rmax,(int)s.size());}
        for(auto&s:ls) if(s.size()>1){++lcyc;lmax=std::max(lmax,(int)s.size());}
        int mutualR=0, mutualL=0;
        bool rbalanced=true,lbalanced=true;
        bool rmultibal=true; int mindeg=1000000;
        for(int u=0;u<W;++u){rmultibal&=rmin[u]==rmout[u];mindeg=std::min(mindeg,std::min(rmin[u],rmout[u]));}
        for(int u=0;u<W;++u){
            int ro=0,ri=0,lo=0,li=0;
            for(int v:right_order.adj[u]) (void)v,++ro;
            for(int v=0;v<W;++v) for(int w:right_order.adj[v]) if(w==u) ++ri;
            for(int v:left_order.adj[u]) (void)v,++lo;
            for(int v=0;v<W;++v) for(int w:left_order.adj[v]) if(w==u) ++li;
            rbalanced &= ro==ri; lbalanced &= lo==li;
        }
        for(auto [u,v]:right_order.edge_set) if(u<v && right_order.edge_set.count({v,u})) ++mutualR;
        for(auto [u,v]:left_order.edge_set) if(u<v && left_order.edge_set.count({v,u})) ++mutualL;
        std::cout<<"k="<<k<<" W="<<W
                 <<" maxpair="<<max_pair<<" badpairs="<<bad_pairs
                 <<" Rarcs="<<right_order.edge_set.size()<<" Rscc="<<rcyc<<" Rmax="<<rmax<<" R2="<<mutualR
                 <<" Rbal="<<rbalanced<<" Rmultibal="<<rmultibal<<" mindeg="<<mindeg
                 <<" Larcs="<<left_order.edge_set.size()<<" Lscc="<<lcyc<<" Lmax="<<lmax<<" L2="<<mutualL
                 <<" Lbal="<<lbalanced<<"\n";
        if(k<=5) {
            std::cout<<"  R mutual:";
            for(auto [u,v]:right_order.edge_set) if(u<v&&right_order.edge_set.count({v,u})) std::cout<<" "<<u<<"<->"<<v;
            std::cout<<"\n";
            if(k<=4){
              for(int i=0;i<W;++i){
                std::cout<<"  C"<<i<<":";
                for(Mask x:C[i]) std::cout<<" "<<x;
                std::cout<<" | out";
                for(int v:right_order.adj[i]) std::cout<<" "<<v;
                std::cout<<"\n";
              }
            }
        }
        if(k%2==0) {
            const int m=k/2;
            std::vector<Mask> center_of_chain(W);
            std::vector<int> center_index(N,-1);
            for(int c=0;c<W;++c) for(Mask x:C[c]) if(__builtin_popcount(x)==m) {
                center_of_chain[c]=x; center_index[x]=c;
            }
            std::vector<int> nxt(W,-1), indeg(W), upper_nxt(W,-1);
            int lower_edges=0,upper_edges=0;
            for(int x=1;x<N;++x) {
                int wt=__builtin_popcount((Mask)x);
                if(wt!=m-1 && wt!=m+1) continue;
                Mask lc=center_of_chain[owner[x]];
                int rc_owner=owner[full^Mask(x)];
                Mask rc=full^center_of_chain[rc_owner];
                int u=center_index[lc], v=center_index[rc];
                if(wt==m-1){nxt[u]=v;++indeg[v];++lower_edges;}
                else {upper_nxt[u]=v;++upper_edges;}
            }
            int cycles=0,cycverts=0,components=W-lower_edges;
            std::vector<char> state(W);
            for(int s=0;s<W;++s) if(!state[s]) {
                int u=s;
                while(u>=0 && state[u]==0){state[u]=1;u=nxt[u];}
                if(u>=0 && state[u]==1){++cycles;int v=u;do{++cycverts;v=nxt[v];}while(v!=u);}
                u=s; while(u>=0&&state[u]==1){state[u]=2;u=nxt[u];}
            }
            int paired_reverse=0;
            int sum_up=0,sum_down=0,lex_up=0,lex_down=0;
            auto pos_sum=[&](Mask x){int s=0;for(int b=0;b<k;++b)if(x>>b&1)s+=b+1;return s;};
            for(int u=0;u<W;++u) if(nxt[u]>=0 && upper_nxt[nxt[u]]==u) ++paired_reverse;
            for(int u=0;u<W;++u) if(nxt[u]>=0){
              int a=pos_sum(center_of_chain[u]),b=pos_sum(center_of_chain[nxt[u]]);
              (b>a?sum_up:sum_down)++;
              (center_of_chain[nxt[u]]>center_of_chain[u]?lex_up:lex_down)++;
            }
            std::cout<<"  middle lower_edges="<<lower_edges<<" cycles="<<cycles<<" cycverts="<<cycverts
                     <<" path_components_if_forest="<<components
                     <<" upper_edges="<<upper_edges<<" exact_reverse="<<paired_reverse<<"/"<<lower_edges<<"\n";
            Digraph central_prec(W);
            for(int u=0;u<W;++u){
              if(nxt[u]>=0) central_prec.add(nxt[u],u); // lower: right center before left center
              if(upper_nxt[u]>=0) central_prec.add(u,upper_nxt[u]);
            }
            auto cs=sccs(central_prec); int cc=0,cv=0,cm=0;
            for(auto&s:cs)if(s.size()>1){++cc;cv+=s.size();cm=std::max(cm,(int)s.size());}
            std::cout<<"  combined_central_prec sccs="<<cc<<" cycverts="<<cv<<" max="<<cm<<" arcs="<<central_prec.edge_set.size()<<"\n";
            if(k<=10 && cc){
              std::vector<int> best;
              for(int s=0;s<W;++s){
                std::vector<int> dist(W,-1),par(W,-1);std::queue<int>qq;dist[s]=0;qq.push(s);
                while(!qq.empty()){
                  int u=qq.front();qq.pop();
                  for(int v:central_prec.adj[u]){
                    if(v==s){
                      std::vector<int> cyc;int x=u;cyc.push_back(s);
                      std::vector<int> rev;while(x!=s){rev.push_back(x);x=par[x];}
                      std::reverse(rev.begin(),rev.end());cyc.insert(cyc.end(),rev.begin(),rev.end());
                      if(best.empty()||cyc.size()<best.size())best=cyc;
                    } else if(dist[v]<0){dist[v]=dist[u]+1;par[v]=u;qq.push(v);}
                  }
                }
              }
              std::cout<<"  shortest central cycle:";
              for(std::size_t z=0;z<best.size();++z){
                int u=best[z],v=best[(z+1)%best.size()];
                char typ=upper_nxt[u]==v?'U':(nxt[v]==u?'L':'?');
                std::cout<<" "<<center_of_chain[u]<<"-"<<typ;
              }
              std::cout<<"\n";
            }
            std::cout<<"  potentials sum_up/down="<<sum_up<<"/"<<sum_down<<" numeric_up/down="<<lex_up<<"/"<<lex_down<<"\n";
            if(k<=6){
              std::cout<<"  lower:";
              for(int u=0;u<W;++u) if(nxt[u]>=0)
                std::cout<<" "<<center_of_chain[u]<<"->"<<center_of_chain[nxt[u]];
              std::cout<<"\n  upper:";
              for(int u=0;u<W;++u) if(upper_nxt[u]>=0)
                std::cout<<" "<<center_of_chain[u]<<"->"<<center_of_chain[upper_nxt[u]];
              std::cout<<"\n";
              std::cout<<"  paths:";
              for(int u=0;u<W;++u) if(indeg[u]==0){
                std::cout<<" [";
                for(int v=u;v>=0;v=nxt[v]) std::cout<<center_of_chain[v]<<"(r"<<__builtin_popcount(C[v].front())<<"),";
                std::cout<<"]";
              }
              std::cout<<"\n";
            }
        }
    }
}
