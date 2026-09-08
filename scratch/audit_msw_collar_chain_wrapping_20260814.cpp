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

// H100-only exact collar-chain census.  For every transposition edge in D_m,
// test equality of the complete forced profiles at depths d,...,d+t, with an
// optional full-compatibility relaxation at only the final depth.  Then wrap
// both roots repeatedly by u -> 1u0, reselecting cuts at each level, and test
// survival for h=1,...,H.  The graph components are those at the source m.

using U = std::uint64_t;
static std::pair<U,int> g(U x,int m){std::vector<int>b(2*m);int h=0,z=0;for(int i=0;i<2*m;++i){b[i]=h;if(!((x>>i)&1U)&&h==0)++z;h+=(x>>i)&1U?1:-1;}int s=0;for(int i=0;i<2*m;++i)if(!((x>>i)&1U)&&(b[i]==0||b[i]==1)&&++s==z+1)return{x|(U{1}<<i),i};assert(false);return{};}
static std::pair<U,int> hmap(U x,int m){std::vector<int>b(2*m);int h=0,o=0;for(int i=0;i<2*m;++i){b[i]=h;if(((x>>i)&1U)&&h==1)++o;h+=(x>>i)&1U?1:-1;}int s=0;for(int i=0;i<2*m;++i)if(((x>>i)&1U)&&(b[i]==0||b[i]==1)&&++s==o)return{x&~(U{1}<<i),i};assert(false);return{};}
static std::vector<int> order(U root,int m){U x=root;int n=2*m+1;std::vector<int>rho;for(int e=0;e<m;++e){auto a=g(x,m);auto b=hmap(a.first,m);rho.push_back(a.second);rho.push_back(b.second);x=b.first;}rho.push_back(2*m);std::vector<int>r(n);for(int i=0;i<n;++i)r[i]=rho[(2*i)%n];return r;}
static U wrap(U x){return U{1}|(x<<1);}

// Store a full profile compactly outside the fixed struct: [orientation][start][q][offset].
using Full=std::vector<std::vector<std::vector<std::vector<std::pair<U,U>>>>>;
static Full full_profiles(U root,int m,int maximum_q){int n=2*m+1;auto row=order(root,m);Full out(2,std::vector<std::vector<std::vector<std::pair<U,U>>>>(n,std::vector<std::vector<std::pair<U,U>>>(maximum_q+1)));
    for(int orientation=0;orientation<2;++orientation){for(int start=0;start<n;++start)for(int q=1;q<=maximum_q;++q){int s=m+1-q;if(s<=0)continue;out[orientation][start][q].resize(q);for(int offset=0;offset<q;++offset){U maximal=0;for(int step=0;step<s;++step)maximal|=U{1}<<row[(start+offset+step)%n];U forced=(U{1}<<row[(start+offset)%n])|(U{1}<<row[(start+offset+s-1)%n]);out[orientation][start][q][offset]={forced,maximal};}}std::reverse(row.begin(),row.end());}return out;}

static bool adjacent(Full const&a,Full const&b,int n,int d,int t,bool contain){for(int oa=0;oa<2;++oa)for(int ob=0;ob<2;++ob)for(int x=0;x<n;++x)for(int y=0;y<n;++y){bool okay=true;for(int q=d;q<=d+t&&okay;++q)for(int offset=0;offset<q;++offset){auto [af,am]=a[oa][x][q][offset];auto [bf,bm]=b[ob][y][q][offset];if(contain&&t>0&&q==d+t)okay&=((af|bf)&~(am&bm))==0;else okay&=af==bf;}if(okay)return true;}return false;}

struct DSU{std::vector<int>p;DSU(int n):p(n){std::iota(p.begin(),p.end(),0);}int f(int x){return p[x]==x?x:p[x]=f(p[x]);}void u(int a,int b){a=f(a);b=f(b);if(a!=b)p[a]=b;}};

int main(int argc,char**argv){assert(argc==6);int m=std::stoi(argv[1]),d=std::stoi(argv[2]),t=std::stoi(argv[3]),H=std::stoi(argv[4]);bool contain=std::string(argv[5])=="contain";assert(2*(m+H)+1<63&&d+t<m+1);
    std::vector<U>roots;auto gen=[&](auto&&self,int pos,int up,int down,U x)->void{if(pos==2*m){roots.push_back(x);return;}if(up<m)self(self,pos+1,up+1,down,x|(U{1}<<pos));if(down<up)self(self,pos+1,up,down+1,x);};gen(gen,0,0,0,0);std::unordered_map<U,int>idx;idx.reserve(2*roots.size());for(int i=0;i<(int)roots.size();++i)idx[roots[i]]=i;
    std::vector<Full>base;base.reserve(roots.size());for(U x:roots)base.push_back(full_profiles(x,m,d+t));DSU dsu(roots.size());long long trans=0,edges=0;std::vector<long long>survive(H+1);std::vector<std::pair<int,int>>current;
    for(int i=0;i<(int)roots.size();++i){U zeros=(~roots[i])&((U{1}<<(2*m))-1);for(int p=0;p<2*m;++p)if((zeros>>p)&1U)for(int q=0;q<2*m;++q)if((roots[i]>>q)&1U){U mate=roots[i]^(U{1}<<p)^(U{1}<<q);auto it=idx.find(mate);if(it==idx.end()||it->second<=i)continue;int j=it->second;++trans;if(adjacent(base[i],base[j],2*m+1,d,t,contain)){++edges;dsu.u(i,j);current.push_back({i,j});}}}
    survive[0]=edges;
    std::vector<U>wrapped=roots;
    for(int h=1;h<=H;++h){for(U&x:wrapped)x=wrap(x);std::vector<std::pair<int,int>>next;next.reserve(current.size());int mm=m+h;for(auto[i,j]:current){auto a=full_profiles(wrapped[i],mm,d+t),b=full_profiles(wrapped[j],mm,d+t);if(adjacent(a,b,2*mm+1,d,t,contain))next.push_back({i,j});}current.swap(next);survive[h]=current.size();}
    std::set<int>components;for(int i=0;i<(int)roots.size();++i)components.insert(dsu.f(i));
    std::cout<<"SUMMARY m="<<m<<" d="<<d<<" t="<<t<<" mode="<<(contain?"contain":"equal")<<" roots="<<roots.size()<<" transposition_edges="<<trans<<" collar_edges="<<edges<<" components="<<components.size()<<" survival=";for(int h=0;h<=H;++h)std::cout<<h<<':'<<survive[h]<<',';std::cout<<'\n';
}
