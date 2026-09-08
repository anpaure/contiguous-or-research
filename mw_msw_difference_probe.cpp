#include <algorithm>
#include <bit>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

using U64 = std::uint64_t;
using Path = std::vector<U64>;
using Family = std::vector<Path>;

struct Edge {
    U64 a, b;
    Edge(U64 x = 0, U64 y = 0) : a(std::min(x,y)), b(std::max(x,y)) {}
    bool operator<(const Edge& o) const { return std::pair(a,b) < std::pair(o.a,o.b); }
    bool operator==(const Edge& o) const { return a == o.a && b == o.b; }
};

// Edmonds' blossom algorithm, used only for the small endpoint-metric audit.
struct BlossomMatching {
    int n;
    std::vector<std::vector<int>> g;
    std::vector<int> match,p,base,q;
    std::vector<char> used,blossom;
    explicit BlossomMatching(int n_):n(n_),g(n_),match(n_,-1),p(n_),base(n_),q(n_),used(n_),blossom(n_){}
    void add_edge(int a,int b){g[a].push_back(b);g[b].push_back(a);}
    int lca(int a,int b){
        std::vector<char> seen(n,0);
        while(true){a=base[a];seen[a]=1;if(match[a]<0)break;a=p[match[a]];}
        while(true){b=base[b];if(seen[b])return b;b=p[match[b]];}
    }
    void mark_path(int v,int b,int child){
        while(base[v]!=b){blossom[base[v]]=blossom[base[match[v]]]=1;p[v]=child;child=match[v];v=p[match[v]];}
    }
    int find_path(int root){
        std::fill(used.begin(),used.end(),0);std::fill(p.begin(),p.end(),-1);
        std::iota(base.begin(),base.end(),0);int qh=0,qt=0;q[qt++]=root;used[root]=1;
        while(qh<qt){int v=q[qh++];for(int u:g[v]){
            if(base[v]==base[u]||match[v]==u)continue;
            if(u==root||(match[u]>=0&&p[match[u]]>=0)){
                int cur=lca(v,u);std::fill(blossom.begin(),blossom.end(),0);
                mark_path(v,cur,u);mark_path(u,cur,v);
                for(int i=0;i<n;++i)if(blossom[base[i]]){base[i]=cur;if(!used[i]){used[i]=1;q[qt++]=i;}}
            }else if(p[u]<0){p[u]=v;if(match[u]<0)return u;u=match[u];used[u]=1;q[qt++]=u;}
        }}return -1;
    }
    int solve(){
        for(int i=0;i<n;++i)if(match[i]<0){int v=find_path(i);if(v<0)continue;while(v>=0){int pv=p[v],nv=pv<0?-1:match[pv];if(pv>=0)match[v]=pv;if(pv>=0)match[pv]=v;v=nv;}}
        int z=0;for(int x:match)z+=x>=0;return z/2;
    }
};

static U64 mask_n(int n) { return n == 64 ? ~U64{0} : ((U64{1} << n) - 1); }

// Words are stored in reading order from low to high bit.  Appending a bit
// therefore places it at position n.
static U64 append_bits(U64 x, int old_n, int tag, int cnt) {
    return x | (U64(tag) << old_n);
}

static U64 rev_bits(U64 x, int n) {
    U64 y = 0;
    for (int i = 0; i < n; ++i) if ((x >> i) & 1U) y |= U64{1} << (n-1-i);
    return y;
}

static U64 mw_f0(U64 x, int n) { return mask_n(n) ^ rev_bits(x,n); }

static Path tagged(const Path& p, int old_n, int tag, int cnt) {
    Path q;
    q.reserve(p.size());
    for (U64 x : p) q.push_back(append_bits(x, old_n, tag, cnt));
    return q;
}

static Path transformed_tagged(const Path& p, int old_n, int tag) {
    Path q;
    q.reserve(p.size());
    for (U64 x : p) q.push_back(mw_f0(x,old_n) | (U64(tag) << old_n));
    return q;
}

static void add_path_edges(std::map<U64,std::vector<U64>>& adj, const Path& p) {
    for (std::size_t i=1;i<p.size();++i) {
        adj[p[i-1]].push_back(p[i]);
        adj[p[i]].push_back(p[i-1]);
    }
}

// Reconstruct the all-zero M\u00fctze--Weber dangling families P_{2n}(k,k+1).
// Return vector indexed by k; only k=n,...,2n-1 are populated.
static std::vector<Family> mw_allzero(int n) {
    if (n == 1) {
        std::vector<Family> f(2);
        f[1] = {Path{1,3,2}}; // words 10,11,01 in reading-order bit convention
        return f;
    }
    const int old_m = n-1;
    const int old_n = 2*old_m;
    auto old = mw_allzero(old_m);
    std::vector<Family> out(2*n);

    // Upper systems: equation (ind-step1-P).
    for (int k=n+1;k<=2*n-1;++k) {
        auto copy = [&](int oldk, int tag) {
            if (oldk < 0 || oldk >= (int)old.size()) return;
            for (const Path& p : old[oldk]) out[k].push_back(tagged(p,old_n,tag,2));
        };
        copy(k,0);       // 00
        copy(k-1,1);     // 10
        copy(k-1,2);     // 01
        copy(k-2,3);     // 11
    }

    const Family& P = old[old_m];

    // C_{2m+1}=P\circ0 union f_0(P)\circ1 union endpoint matching.
    std::map<U64,std::vector<U64>> adj;
    for (const Path& p : P) {
        add_path_edges(adj,tagged(p,old_n,0,1));
        add_path_edges(adj,transformed_tagged(p,old_n,1));
    }
    std::set<U64> FL;
    for (const Path& p : P) { FL.insert(p.front()); FL.insert(p.back()); }
    for (U64 v : FL) {
        U64 a=v, b=v|(U64{1}<<old_n);
        adj[a].push_back(b); adj[b].push_back(a);
    }

    // Delete (F(P),S(P))\circ0 from every old central path.
    auto erase_edge = [&](U64 a,U64 b) {
        auto& aa=adj[a]; aa.erase(std::find(aa.begin(),aa.end(),b));
        auto& bb=adj[b]; bb.erase(std::find(bb.begin(),bb.end(),a));
    };
    for (const Path& p : P) erase_edge(p[0],p[1]);

    // Each start S(P)\circ0 now starts one component of C^-.
    std::set<U64> used;
    Family mixed;
    for (const Path& p : P) {
        U64 start=p[1];
        assert(adj[start].size()==1);
        Path comp;
        U64 prev=~U64{0}, cur=start;
        while (true) {
            assert(!used.contains(cur));
            used.insert(cur); comp.push_back(cur);
            U64 nxt=~U64{0};
            for (U64 z:adj[cur]) if (z!=prev) { nxt=z; break; }
            if (nxt==~U64{0}) break;
            prev=cur; cur=nxt;
        }
        assert(std::popcount(comp.front())==old_m+1);
        assert(std::popcount(comp.back())==old_m);

        // M^S then C^-\circ1, with new bits in order (old 2m-bit, first, second).
        Path np;
        np.reserve(comp.size()+1);
        np.push_back(start); // start\circ00
        for (U64 z:comp) np.push_back(z | (U64{1} << (old_n+1)));
        mixed.push_back(std::move(np));
    }

    // Equation (ind-step2-P): upper-old\circ00, central-old\circ10, mixed.
    if (old_m+1 < (int)old.size())
        for (const Path& p:old[old_m+1]) out[n].push_back(tagged(p,old_n,0,2));
    for (const Path& p:P) out[n].push_back(tagged(p,old_n,1,2));
    out[n].insert(out[n].end(),mixed.begin(),mixed.end());
    return out;
}

static int start_height(U64 x,int pos) {
    int h=0; for(int i=0;i<pos;++i) h += ((x>>i)&1U)?1:-1; return h;
}
static bool is_dyck(U64 x,int n) {
    int h=0; for(int i=0;i<n;++i){ h += ((x>>i)&1U)?1:-1; if(h<0)return false;} return h==0;
}
static U64 g_map(U64 x,int n) {
    int d0=0;
    for(int i=0;i<n;++i) if(!((x>>i)&1U) && start_height(x,i)==0) ++d0;
    int seen=0;
    for(int i=0;i<n;++i) if(!((x>>i)&1U)) {
        int h=start_height(x,i); if(h==0||h==1) if(++seen==d0+1) return x|(U64{1}<<i);
    }
    assert(false); return 0;
}
static U64 h_map(U64 y,int n) {
    int u1=0;
    for(int i=0;i<n;++i) if((y>>i)&1U) if(start_height(y,i)==1) ++u1;
    int seen=0;
    for(int i=0;i<n;++i) if((y>>i)&1U) {
        int h=start_height(y,i); if(h==0||h==1) if(++seen==u1) return y&~(U64{1}<<i);
    }
    assert(false); return 0;
}
static U64 f_msw(U64 x,int n){return h_map(g_map(x,n),n);}

static Family msw_factor(int half) {
    int n=2*half; U64 lim=U64{1}<<n; Family fam;
    for(U64 x=0;x<lim;++x) if(std::popcount(x)==half && is_dyck(x,n)) {
        Path p; p.push_back(x);
        for(int i=0;i<half;++i) {
            U64 y=g_map(p.back(),n); p.push_back(y); p.push_back(h_map(y,n));
        }
        assert(p.back()==(mask_n(n)^x)); fam.push_back(std::move(p));
    }
    return fam;
}

static std::set<Edge> edges(const Family& f) {
    std::set<Edge> e; for(const auto&p:f) for(std::size_t i=1;i<p.size();++i) {
        bool ok=e.insert(Edge(p[i-1],p[i])).second; assert(ok);
    } return e;
}
static std::set<U64> endpoints(const Family& f) {
    std::set<U64> s; for(const auto&p:f){s.insert(p.front());s.insert(p.back());} return s;
}
static std::uint64_t choose(int n,int k){if(k<0||k>n)return 0;k=std::min(k,n-k);std::uint64_t z=1;for(int i=1;i<=k;++i)z=z*(n-k+i)/i;return z;}
static std::uint64_t cat(int n){return choose(2*n,n)/(n+1);}

static std::string mu_word(std::string s) {
    std::reverse(s.begin(),s.end()); for(char&c:s)c=(c=='1'?'0':'1'); return s;
}
static int predicted_R_step(const std::string& w) {
    assert(!w.empty() && w.front()=='1');
    int h=0, ret=-1;
    for(int i=0;i<(int)w.size();++i){h+=(w[i]=='1'?1:-1);if(h==0){ret=i;break;}}
    assert(ret>=1);
    std::string u=w.substr(1,ret-1);
    if(u.empty()) return 1;
    return 1+predicted_R_step(mu_word(u));
}
static int predicted_K_step(const std::string& w) {
    if (w=="10") return 2; // formal seed; no second K-edge in dimension two
    int h=0,ret=-1;
    for(int i=0;i<(int)w.size();++i){h+=(w[i]=='1'?1:-1);if(h==0){ret=i;break;}}
    std::string u=w.substr(1,ret-1),v=w.substr(ret+1);
    if(!u.empty()) return 1+predicted_K_step(mu_word(u));
    assert(!v.empty());
    return 2+predicted_R_step(v);
}

// Lexicographic matching LM_{N}(half,half+1), then reverse all coordinates.
static std::set<Edge> reversed_lex_matching(int N,int half) {
    std::set<Edge> ans; U64 lim=U64{1}<<N;
    for(U64 x=0;x<lim;++x) if(std::popcount(x)==half) {
        std::vector<int> st; std::vector<char> matched(N,0);
        // Match 0-opening with 1-closing, left to right.
        for(int i=0;i<N;++i) {
            if(!((x>>i)&1U)) st.push_back(i);
            else if(!st.empty()) { matched[st.back()]=matched[i]=1; st.pop_back(); }
        }
        int j=-1; for(int i=0;i<N;++i) if(!matched[i]&&!((x>>i)&1U)){j=i;break;}
        if(j<0) continue;
        U64 y=x|(U64{1}<<j);
        ans.insert(Edge(rev_bits(x,N),rev_bits(y,N)));
    }
    return ans;
}

int main(int argc,char**argv){
    int max_m=argc>1?std::stoi(argv[1]):6;
    std::map<std::string,int> bdict;
    for(int m=0;m<=max_m;++m){
        int half=m+1,n=2*half;
        auto all=mw_allzero(half); const Family&H0=all[half];
        Family HMSW=msw_factor(half);
        auto e0=edges(H0), e1=edges(HMSW); auto t0=endpoints(H0),t1=endpoints(HMSW);
        auto rlm=reversed_lex_matching(n,half);
        std::vector<U64> singleton_ep;
        for (U64 v : t0) if (!t0.contains(mask_n(n)^v)) singleton_ep.push_back(v);
        std::vector<U64> deleted_ep,added_ep;
        for(U64 v:t0)if(!t1.contains(v))deleted_ep.push_back(v);
        for(U64 v:t1)if(!t0.contains(v))added_ep.push_back(v);
        std::map<int,std::size_t> nearest_antipodal_hist;
        std::map<int,std::uint64_t> endpoint_pair_count;
        for (std::size_t i=0;i<singleton_ep.size();++i) {
            int best=n+1;
            for (std::size_t j=0;j<singleton_ep.size();++j) if(i!=j) {
                int cost=std::popcount(singleton_ep[i]&singleton_ep[j]);
                best=std::min(best,cost);
                ++endpoint_pair_count[cost];
            }
            ++nearest_antipodal_hist[best];
        }
        std::vector<std::size_t> max_matching_by_cost;
        for (int threshold=1;threshold<=3;++threshold) {
            BlossomMatching g(singleton_ep.size());
            for(std::size_t i=0;i<singleton_ep.size();++i)
                for(std::size_t j=i+1;j<singleton_ep.size();++j)
                    if(std::popcount(singleton_ep[i]&singleton_ep[j])<=threshold)
                        g.add_edge(i,j);
            max_matching_by_cost.push_back(g.solve());
        }
        std::vector<int> canonical_bipartite_matching;
        std::vector<int> canonical_dist3_mt;
        for(int threshold=1;threshold<=4;++threshold){
            std::vector<int> mt(added_ep.size(),-1);
            auto aug=[&](auto&&self,int v,std::vector<char>&seen)->bool{
                for(int j=0;j<(int)added_ep.size();++j)if(!seen[j]&&
                    half-std::popcount(deleted_ep[v]&added_ep[j])<=threshold){
                    seen[j]=1;if(mt[j]<0||self(self,mt[j],seen)){mt[j]=v;return true;}
                }return false;
            };
            int got=0;for(int i=0;i<(int)deleted_ep.size();++i){std::vector<char>seen(added_ep.size());got+=aug(aug,i,seen);}
            canonical_bipartite_matching.push_back(got);
            if(threshold==3)canonical_dist3_mt=mt;
        }
        std::size_t common=0;for(const auto&e:e0)common+=e1.contains(e);
        std::size_t tcommon=0;for(U64 v:t0)tcommon+=t1.contains(v);
        std::map<std::string,std::size_t> bytag;
        std::map<std::string,std::size_t> common_tag;
        std::map<int,std::size_t> common_step;
        std::map<Edge,int> msw_step;
        std::map<Edge,char> msw_kind;
        std::map<Edge,U64> msw_root;
        for (const auto& p:HMSW) for(std::size_t i=1;i<p.size();++i)
        {
            Edge ee(p[i-1],p[i]);
            msw_step.emplace(ee,int(i-1));
            msw_kind.emplace(ee, ((i-1)%2==0)?'g':'h');
            msw_root.emplace(ee,p.front());
        }
        std::map<char,std::size_t> common_kind;
        std::map<U64,int> common_at_upper;
        for(const auto&e:e0) if(e1.contains(e)) {
            int ta=(e.a>>(n-2))&3, tb=(e.b>>(n-2))&3;
            if(ta>tb)std::swap(ta,tb);
            common_tag[std::to_string(ta)+"-"+std::to_string(tb)]++;
            common_step[msw_step.at(e)]++;
            common_kind[msw_kind.at(e)]++;
            U64 up = std::popcount(e.a)==half+1 ? e.a : e.b;
            ++common_at_upper[up];
        }
        for(const auto&e:e0) if(!e1.contains(e)) {
            int ta=(e.a>>(n-2))&3, tb=(e.b>>(n-2))&3;
            if(ta>tb)std::swap(ta,tb);
            bytag[std::to_string(ta)+"-"+std::to_string(tb)]++;
        }
        std::cout<<"m="<<m<<" n="<<n<<" C_m="<<cat(m)<<" C_next="<<cat(m+1)
                 <<" paths="<<H0.size()<<" edges="<<e0.size()
                 <<" common="<<common<<" diff_each="<<(e0.size()-common)
                 <<" symdiff="<<2*(e0.size()-common)
                 <<" endpoints_common="<<tcommon<<" endpoint_symdiff="<<2*(t0.size()-tcommon)
                 <<" ratio/Cm="<<(m?double(2*(e0.size()-common))/cat(m):0.0)<<"\n";
        std::cout<<"  old-only tags:";for(auto&[x,c]:bytag)std::cout<<' '<<x<<'='<<c;std::cout<<"\n";
        std::cout<<"  common tags:";for(auto&[x,c]:common_tag)std::cout<<' '<<x<<'='<<c;std::cout<<"\n";
        std::cout<<"  common MSW steps:";for(auto&[x,c]:common_step)std::cout<<' '<<x<<'='<<c;std::cout<<"\n";
        std::cout<<"  common kinds:";for(auto&[x,c]:common_kind)std::cout<<' '<<x<<'='<<c;std::cout<<"\n";
        std::map<int,std::size_t> hist; for(auto [u,c]:common_at_upper)++hist[c];
        std::size_t upper_total=choose(n,half+1); hist[0]=upper_total-common_at_upper.size();
        std::cout<<"  upper common-degree:";for(auto&[x,c]:hist)std::cout<<' '<<x<<'='<<c;std::cout<<"\n";
        std::map<U64,int> perroot; for(const auto&e:e0)if(e1.contains(e))++perroot[msw_root.at(e)];
        std::map<int,std::size_t> rhist;for(auto [x,c]:perroot)++rhist[c];
        std::cout<<"  path common-edge hist:";for(auto&[x,c]:rhist)std::cout<<' '<<x<<'='<<c;std::cout<<"\n";
        std::size_t common_rlm=0, rlm_msw=0;
        std::map<char,std::size_t> rlm_kind, k_kind;
        for(const auto&e:rlm){common_rlm+=e0.contains(e)&&e1.contains(e);rlm_msw+=e1.contains(e);}
        for(const auto&e:e0) if(e1.contains(e)) {
            if(rlm.contains(e)) ++rlm_kind[msw_kind.at(e)];
            else ++k_kind[msw_kind.at(e)];
        }
        std::cout<<"  revLM="<<rlm.size()<<" contained_H0=";
        std::size_t rlm_h0=0;for(const auto&e:rlm)rlm_h0+=e0.contains(e);
        std::cout<<rlm_h0<<" intersects_MSW="<<rlm_msw<<" triple="<<common_rlm<<"\n";
        std::cout<<"  matrix R/K x g/h: Rg="<<rlm_kind['g']<<" Rh="<<rlm_kind['h']
                 <<" Kg="<<k_kind['g']<<" Kh="<<k_kind['h']<<"\n";
        bool rpred_ok=true;
        bool kpred_ok=true;
        std::map<std::string,int> current_b;
        for(const auto&p:HMSW){
            std::string w;for(int i=0;i<n;++i)w+=((p.front()>>i)&1U)?'1':'0';
            int got=-1,cnt=0;
            for(std::size_t i=1;i<p.size();++i)if(rlm.contains(Edge(p[i-1],p[i]))){got=i-1;++cnt;}
            rpred_ok &= cnt==1 && got==predicted_R_step(w);
            int kb=-1,kcnt=0;
            for(std::size_t i=2;i<p.size();++i) {
                Edge ee(p[i-1],p[i]);
                if(e0.contains(ee)&&!rlm.contains(ee)){kb=i-1;++kcnt;}
            }
            if(half>=2) assert(kcnt==1);
            if(half>=2) kpred_ok &= kb==predicted_K_step(w);
            current_b[w]=kb;
        }
        std::cout<<"  R-crossing recurrence="<<(rpred_ok?"OK":"FAIL")<<"\n";
        std::cout<<"  K-crossing recurrence="<<(kpred_ok?"OK":"FAIL")<<"\n";
        std::cout<<"  singleton endpoints="<<singleton_ep.size()<<" nearest complement-move cost:";
        for(auto [d,c]:nearest_antipodal_hist)std::cout<<' '<<d<<'='<<c;
        std::cout<<"\n  ordered singleton-pair costs:";
        for(auto [d,c]:endpoint_pair_count)std::cout<<' '<<d<<'='<<c;
        std::cout<<"\n  maximum endpoint pair matching (cost<=1,2,3):";
        for(auto c:max_matching_by_cost)std::cout<<' '<<c;
        std::cout<<" of "<<singleton_ep.size()/2<<"\n";
        std::cout<<"  H0->MSW endpoint matching (Johnson dist<=1..4):";
        for(auto c:canonical_bipartite_matching)std::cout<<' '<<c;
        std::cout<<" of "<<deleted_ep.size()<<"\n";
        if(m<=3&&m>=1){
            std::cout<<"  dist3 endpoint pairs (deleted -> added):\n";
            for(int j=0;j<(int)canonical_dist3_mt.size();++j)if(canonical_dist3_mt[j]>=0){
                auto printword=[&](U64 z){for(int i=0;i<n;++i)std::cout<<((z>>i)&1U);};
                std::cout<<"    ";printword(deleted_ep[canonical_dist3_mt[j]]);std::cout<<" -> ";printword(added_ep[j]);
                std::cout<<" d="<<half-std::popcount(deleted_ep[canonical_dist3_mt[j]]&added_ep[j])<<"\n";
            }
        }
        if (half==4) {
            for(auto [w,b]:current_b){
                int h=0,ret=-1;for(int i=0;i<(int)w.size();++i){h+=(w[i]=='1'?1:-1);if(!h){ret=i;break;}}
                std::string u=w.substr(1,ret-1),v=w.substr(ret+1);
                auto val=[&](const std::string&s)->int{auto it=bdict.find(s);return it==bdict.end()?-9:it->second;};
                std::cout<<"    KREC w="<<w<<" u="<<u<<" v="<<v<<" b="<<b
                         <<" bmu="<<val(mu_word(u))<<" bv="<<val(v)
                         <<" amu="<<(u.empty()?-1:predicted_R_step(mu_word(u)))
                         <<" av="<<(v.empty()?-1:predicted_R_step(v))<<"\n";
            }
        }
        bdict.insert(current_b.begin(),current_b.end());
        if (m==1 || m==2 || m==3) {
            for (const auto& p:HMSW) {
                std::cout << "    root=";
                for(int i=0;i<n;++i) std::cout<<((p.front()>>i)&1U);
                std::cout << " steps=";
                for(std::size_t i=1;i<p.size();++i) if(e0.contains(Edge(p[i-1],p[i])))
                {
                    U64 d=p[i-1]^p[i];
                    Edge ee(p[i-1],p[i]);
                    std::cout << (i-1) << '@' << std::countr_zero(d)+1
                              << (rlm.contains(ee)?'R':'K') << ',';
                }
                std::cout << '\n';
            }
        }
    }
}
