#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <deque>
#include <functional>
#include <iostream>
#include <numeric>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

using U32=std::uint32_t; using U64=std::uint64_t;
struct DSU{std::vector<int>p;DSU(int n):p(n){std::iota(p.begin(),p.end(),0);}int f(int x){return p[x]==x?x:p[x]=f(p[x]);}void u(int a,int b){a=f(a);b=f(b);if(a!=b)p[b]=a;}};
static std::pair<U32,int> g(U32 x,int m){std::vector<int>b(2*m);int h=0,d=0;for(int i=0;i<2*m;++i){b[i]=h;if(!((x>>i)&1U)&&h==0)++d;h+=((x>>i)&1U)?1:-1;}int o=0;for(int i=0;i<2*m;++i)if(!((x>>i)&1U)&&(b[i]==0||b[i]==1))if(++o==d+1)return{x|(U32{1}<<i),i};assert(false);return{};}
static std::pair<U32,int> hfun(U32 y,int m){std::vector<int>b(2*m);int h=0,u=0;for(int i=0;i<2*m;++i){b[i]=h;if(((y>>i)&1U)&&h==1)++u;h+=((y>>i)&1U)?1:-1;}int o=0;for(int i=0;i<2*m;++i)if(((y>>i)&1U)&&(b[i]==0||b[i]==1))if(++o==u)return{y&~(U32{1}<<i),i};assert(false);return{};}
static long long C(int n,int k){long long z=1;if(k<0||k>n)return 0;for(int i=1;i<=k;++i)z=z*(n-k+i)/i;return z;}
static U64 pack(const std::vector<int>&q){U64 z=0;for(size_t i=0;i<q.size();++i)z|=U64(q[i])<<(4*i);return z;}
static std::vector<int> unpack(U64 z,int n){std::vector<int>q(n);for(int i=0;i<n;++i)q[i]=(z>>(4*i))&15;return q;}
static U64 canon(std::vector<int>q){int n=q.size(),at=std::find(q.begin(),q.end(),0)-q.begin();std::rotate(q.begin(),q.begin()+at,q.end());std::vector<int>r(n);r[0]=0;for(int i=1;i<n;++i)r[i]=q[n-i];return std::min(pack(q),pack(r));}
static U64 swap_labels(U64 z,int n,int a,int b){auto q=unpack(z,n);for(int&x:q){if(x==a)x=b;else if(x==b)x=a;}return canon(q);}
static std::vector<U32> intervals(U64 z,int n,int r){auto q=unpack(z,n);std::vector<U32>v(n);for(int i=0;i<n;++i)for(int t=0;t<r;++t)v[i]|=U32{1}<<q[(i+2*t)%n];return v;}
static std::string state_key(const std::vector<U64>&s){return std::string(reinterpret_cast<const char*>(s.data()),s.size()*sizeof(U64));}
static std::string shadow_key(const std::vector<U64>&s,int n,int r){std::vector<unsigned char>c(U32{1}<<n);for(U64 z:s)for(U32 x:intervals(z,n,r)){assert(c[x]<255);++c[x];}std::string k;for(U32 x=0;x<(U32{1}<<n);++x)if(__builtin_popcount(x)==r)k.push_back(char(c[x]));return k;}

struct Node{std::vector<U64>s;int par=-1,a=-1,b=-1,root=-1;};
int main(int argc,char**argv){int m=argc>1?std::stoi(argv[1]):4;long long cap=argc>2?std::stoll(argv[2]):200000;int n=2*m+1;assert(n<=15);std::vector<U64>start;
 std::function<void(int,int,int,U32)>gen=[&](int p,int u,int d,U32 mask){if(p==2*m){U32 x=mask;std::vector<int>q;for(int e=0;e<m;++e){auto a=g(x,m);auto b=hfun(a.first,m);q.push_back(a.second);q.push_back(b.second);x=b.first;}q.push_back(2*m);start.push_back(canon(q));return;}if(u<m)gen(p+1,u+1,d,mask|(U32{1}<<p));if(d<u)gen(p+1,u,d+1,mask);};gen(0,0,0,0);std::sort(start.begin(),start.end());assert((long long)start.size()==C(2*m,m)/(m+1));
 std::vector<Node>nodes{{start}};std::deque<int>dq{0};std::unordered_map<std::string,int>seen;seen.emplace(state_key(start),0);std::unordered_map<std::string,int>first_shadow;first_shadow.emplace(shadow_key(start,n,m-1),0);
 while(!dq.empty()&&(long long)nodes.size()<cap){int id=dq.front();dq.pop_front();auto cur=nodes[id].s;std::vector<int>own(U32{1}<<n,-1);for(int i=0;i<(int)cur.size();++i)for(U32 x:intervals(cur[i],n,m)){assert(own[x]<0);own[x]=i;}
  for(int a=0;a<n;++a)for(int b=a+1;b<n;++b){std::vector<U64>rhs(cur.size());std::vector<int>rown(U32{1}<<n,-1);for(int i=0;i<(int)cur.size();++i){rhs[i]=swap_labels(cur[i],n,a,b);for(U32 x:intervals(rhs[i],n,m)){assert(rown[x]<0);rown[x]=i;}}DSU d(2*cur.size());for(U32 x=0;x<(U32{1}<<n);++x)if(own[x]>=0)d.u(own[x],cur.size()+rown[x]);std::unordered_map<int,std::pair<std::vector<int>,std::vector<int>>>cs;for(int i=0;i<(int)cur.size();++i){cs[d.f(i)].first.push_back(i);cs[d.f(cur.size()+i)].second.push_back(i);}for(auto &zz:cs){auto L=zz.second.first,R=zz.second.second;std::vector<U64>nx=cur;std::vector<char>del(cur.size());for(int x:L)del[x]=1;nx.clear();for(int i=0;i<(int)cur.size();++i)if(!del[i])nx.push_back(cur[i]);for(int x:R)nx.push_back(rhs[x]);std::sort(nx.begin(),nx.end());auto sk=state_key(nx);if(seen.count(sk))continue;int ni=nodes.size();seen.emplace(sk,ni);nodes.push_back({nx,id,a,b,zz.first});dq.push_back(ni);auto fk=shadow_key(nx,n,m-1);auto it=first_shadow.find(fk);if(it!=first_shadow.end()){int old=it->second;if(shadow_key(nodes[old].s,n,m-2)!=shadow_key(nx,n,m-2)){std::cout<<"FOUND m="<<m<<" states="<<nodes.size()<<" old="<<old<<" new="<<ni<<"\n";auto dump=[&](int x){std::vector<int>path;while(x>0){path.push_back(x);x=nodes[x].par;}std::reverse(path.begin(),path.end());for(int y:path)std::cout<<" step node="<<y<<" swap="<<nodes[y].a+1<<","<<nodes[y].b+1<<" root="<<nodes[y].root<<"\n";};std::cout<<"PATH_OLD\n";dump(old);std::cout<<"PATH_NEW\n";dump(ni);std::cout<<"FACTOR_OLD\n";for(U64 z:nodes[old].s){for(int x:unpack(z,n))std::cout<<x+1<<'.';std::cout<<'\n';}std::cout<<"FACTOR_NEW\n";for(U64 z:nx){for(int x:unpack(z,n))std::cout<<x+1<<'.';std::cout<<'\n';}return 0;}}else first_shadow.emplace(std::move(fk),ni);
  }}if(nodes.size()%1000==0)std::cerr<<"states="<<nodes.size()<<" queue="<<dq.size()<<" shadows="<<first_shadow.size()<<"\n";
 }
 std::cout<<"NONE m="<<m<<" states="<<nodes.size()<<" shadows="<<first_shadow.size()<<"\n";
}
