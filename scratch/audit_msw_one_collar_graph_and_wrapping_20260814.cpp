#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <set>
#include <string>
#include <tuple>
#include <unordered_map>
#include <utility>
#include <vector>

// H100-only audit of context-stable collar candidates.
// A witness is one orientation/cut pair on each endpoint.  It must have
// equality of forced rails at widths d,...,d+t.  In "contain" mode the last
// level d+t may instead satisfy the full forced-union/maximal-intersection
// criterion.  Wrapping transports cuts by the exact old-position embedding
// in the wrapped tight order and rechecks the same witness.

using U = std::uint64_t;

static std::pair<U,int> g(U x,int m){std::vector<int>b(2*m);int h=0,z=0;for(int i=0;i<2*m;++i){b[i]=h;if(!((x>>i)&1U)&&h==0)++z;h+=(x>>i)&1U?1:-1;}int s=0;for(int i=0;i<2*m;++i)if(!((x>>i)&1U)&&(b[i]==0||b[i]==1)&&++s==z+1)return{x|(U{1}<<i),i};assert(false);return{};}
static std::pair<U,int> hmap(U x,int m){std::vector<int>b(2*m);int h=0,o=0;for(int i=0;i<2*m;++i){b[i]=h;if(((x>>i)&1U)&&h==1)++o;h+=(x>>i)&1U?1:-1;}int s=0;for(int i=0;i<2*m;++i)if(((x>>i)&1U)&&(b[i]==0||b[i]==1)&&++s==o)return{x&~(U{1}<<i),i};assert(false);return{};}
static std::vector<int> order(U root,int m){U x=root;int n=2*m+1;std::vector<int>rho;for(int e=0;e<m;++e){auto a=g(x,m);auto b=hmap(a.first,m);rho.push_back(a.second);rho.push_back(b.second);x=b.first;}rho.push_back(2*m);std::vector<int>r(n);for(int i=0;i<n;++i)r[i]=rho[(2*i)%n];return r;}
static std::string word(U x,int m){std::string s;for(int i=0;i<2*m;++i)s.push_back((x>>i)&1U?'1':'0');return s;}
static U wrap(U x,int m){return U{1}|(x<<1);}

struct Level {
    std::array<U,16> forced{};
    std::array<U,16> maximal{};
};
using Profile=std::vector<std::vector<std::vector<Level>>>; // orientation,start,depth q

static Profile profiles(U root,int m,int maximum_q){
    assert(maximum_q<16);int n=2*m+1;auto row=order(root,m);Profile out(2,std::vector<std::vector<Level>>(n,std::vector<Level>(maximum_q+1)));
    for(int orientation=0;orientation<2;++orientation){
        for(int start=0;start<n;++start)for(int q=1;q<=maximum_q;++q){int s=m+1-q;if(s<=0)continue;for(int offset=0;offset<q;++offset){U maximal=0;for(int step=0;step<s;++step)maximal|=U{1}<<row[(start+offset+step)%n];U forced=(U{1}<<row[(start+offset)%n])|(U{1}<<row[(start+offset+s-1)%n]);out[orientation][start][q].forced[offset]=forced;out[orientation][start][q].maximal[offset]=maximal;}}
        std::reverse(row.begin(),row.end());
    }return out;
}

struct Witness {int ou,a,ov,b;};

static std::vector<Witness> witnesses(Profile const&u,Profile const&v,int n,int d,int t,bool contain_last){
    std::vector<Witness> out;for(int ou=0;ou<2;++ou)for(int ov=0;ov<2;++ov)for(int a=0;a<n;++a)for(int b=0;b<n;++b){bool okay=true;for(int q=d;q<=d+t;++q){auto const&x=u[ou][a][q];auto const&y=v[ov][b][q];for(int offset=0;offset<q;++offset){if(contain_last&&q==d+t&&t>0)okay&=(((x.forced[offset]|y.forced[offset])&~(x.maximal[offset]&y.maximal[offset]))==0);else okay&=x.forced[offset]==y.forced[offset];}}if(okay)out.push_back({ou,a,ov,b});}return out;
}

static int wrapped_start(std::vector<int> const&old_order,std::vector<int> const&new_order,int orientation,int start){
    int old_n=old_order.size(),new_n=new_order.size();std::vector<int>oriented_old=old_order,oriented_new=new_order;if(orientation){std::reverse(oriented_old.begin(),oriented_old.end());std::reverse(oriented_new.begin(),oriented_new.end());}
    int label=oriented_old[start]+1;auto it=std::find(oriented_new.begin(),oriented_new.end(),label);assert(it!=oriented_new.end());return it-oriented_new.begin();
}

struct DSU{std::vector<int>p;DSU(int n):p(n){std::iota(p.begin(),p.end(),0);}int f(int x){return p[x]==x?x:p[x]=f(p[x]);}void u(int a,int b){a=f(a);b=f(b);if(a!=b)p[a]=b;}};

int main(int argc,char**argv){assert(argc==5);int m=std::stoi(argv[1]),d=std::stoi(argv[2]),t=std::stoi(argv[3]);bool contain=std::string(argv[4])=="contain";int n=2*m+1;
    std::vector<U>roots;auto gen=[&](auto&&self,int pos,int up,int down,U x)->void{if(pos==2*m){roots.push_back(x);return;}if(up<m)self(self,pos+1,up+1,down,x|(U{1}<<pos));if(down<up)self(self,pos+1,up,down+1,x);};gen(gen,0,0,0,0);std::unordered_map<U,int>root_index;root_index.reserve(2*roots.size());for(int i=0;i<(int)roots.size();++i)root_index[roots[i]]=i;
    std::vector<Profile>prof;prof.reserve(roots.size());for(U x:roots)prof.push_back(profiles(x,m,d+t));std::vector<std::vector<int>>ord;for(U x:roots)ord.push_back(order(x,m));
    std::vector<Profile>wprof;std::vector<std::vector<int>>worder;wprof.reserve(roots.size());worder.reserve(roots.size());for(U x:roots){wprof.push_back(profiles(wrap(x,m),m+1,d+t));worder.push_back(order(wrap(x,m),m+1));}
    DSU dsu(roots.size());long long trans=0,edges=0,witness_count=0,mapped_edges_survive=0,mapped_witness_survive=0,existential_edges_survive=0;std::vector<std::tuple<int,int,std::vector<Witness>>> failures;
    for(int i=0;i<(int)roots.size();++i){U zero=(~roots[i])&((U{1}<<(2*m))-1),one=roots[i];for(int p=0;p<2*m;++p)if((zero>>p)&1U)for(int q=0;q<2*m;++q)if((one>>q)&1U){U mate=roots[i]^(U{1}<<p)^(U{1}<<q);auto it=root_index.find(mate);if(it==root_index.end()||it->second<=i)continue;int j=it->second;++trans;auto ws=witnesses(prof[i],prof[j],n,d,t,contain);if(ws.empty())continue;++edges;witness_count+=ws.size();dsu.u(i,j);bool edge_survives=false;for(auto w:ws){int a=wrapped_start(ord[i],worder[i],w.ou,w.a),b=wrapped_start(ord[j],worder[j],w.ov,w.b);bool okay=true;for(int qdepth=d;qdepth<=d+t;++qdepth){auto const&x=wprof[i][w.ou][a][qdepth];auto const&y=wprof[j][w.ov][b][qdepth];for(int offset=0;offset<qdepth;++offset){if(contain&&qdepth==d+t&&t>0)okay&=(((x.forced[offset]|y.forced[offset])&~(x.maximal[offset]&y.maximal[offset]))==0);else okay&=x.forced[offset]==y.forced[offset];}}if(okay){edge_survives=true;++mapped_witness_survive;}}
        if(edge_survives)++mapped_edges_survive;
        auto wrapped_ws=witnesses(wprof[i],wprof[j],n+2,d,t,contain);
        if(!wrapped_ws.empty())++existential_edges_survive;
        else if(failures.size()<10)failures.push_back({i,j,ws});}}
    std::set<int>components;for(int i=0;i<(int)roots.size();++i)components.insert(dsu.f(i));
    std::cout<<"SUMMARY m="<<m<<" d="<<d<<" t="<<t<<" mode="<<(contain?"contain":"equal")<<" roots="<<roots.size()<<" transposition_edges="<<trans<<" collar_edges="<<edges<<" components="<<components.size()<<" witnesses="<<witness_count<<" wrapped_existential_survivors="<<existential_edges_survive<<" wrapped_existential_failures="<<edges-existential_edges_survive<<" wrapped_mapped_cut_survivors="<<mapped_edges_survive<<" wrapped_mapped_witness_survivors="<<mapped_witness_survive<<'\n';
    for(auto const&[i,j,ws]:failures)std::cout<<"FAIL "<<word(roots[i],m)<<' '<<word(roots[j],m)<<" witnesses="<<ws.size()<<'\n';
}
