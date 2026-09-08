#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <string>
#include <utility>
#include <vector>

using Pt=std::array<int,3>; using Lab=std::pair<int,int>;
static int rk(Pt p){return p[0]+p[1]+p[2];}
static Lab ll(Pt p,int m){int i=std::min(p[1],m-p[0]),t=p[0]+p[1]-i,j=std::min(t,m-p[2]);return{i,j};}
static Lab rr(Pt p,int m){int i=std::min(p[2],m-p[0]),t=p[0]+p[2]-i,j=std::min(t,m-p[1]);return{i,j};}
struct Chain{std::string s;std::vector<Pt> a;};

static std::vector<Chain> raw(bool left,int m){
 std::map<Lab,std::vector<Pt>> f;for(int x=0;x<=m;x++)for(int y=0;y<=m;y++)for(int z=0;z<=m;z++){Pt p{x,y,z};f[left?ll(p,m):rr(p,m)].push_back(p);}
 std::vector<Chain> c;for(auto&[q,a]:f){std::sort(a.begin(),a.end(),[](Pt x,Pt y){return rk(x)<rk(y);});c.push_back({(left?"L":"R")+std::to_string(q.first)+","+std::to_string(q.second),a});}return c;
}
static std::vector<Chain> rechainedR(int m){
 auto R=raw(false,m);std::map<Lab,std::vector<Pt>> r;for(auto&c:R){Lab q=rr(c.a[0],m);r[q]=c.a;}
 std::map<Lab,std::vector<Pt>> p,s;for(auto&[q,a]:r)if(q.first+q.second<=m){Pt u{q.second,q.first,q.first};for(Pt v:a)(rk(v)<=rk(u)?p[q]:s[q]).push_back(v);}
 std::set<Lab> up,us;std::vector<Chain> out;
 for(int i=0;i<=m-2;i++)for(int j=0;j<=m-i-1;j++){std::vector<Pt>a=p[{i,j}];a.insert(a.end(),s[{i+1,j}].begin(),s[{i+1,j}].end());out.push_back({"Q"+std::to_string(i)+","+std::to_string(j),a});up.insert({i,j});us.insert({i+1,j});}
 out.push_back({"B",r[{0,m}]});up.insert({0,m});us.insert({0,m});
 for(auto&[q,a]:r){int i=q.first,j=q.second;if(i+j<=m){if(!up.count(q)&&!p[q].empty())out.push_back({"P"+std::to_string(i)+","+std::to_string(j),p[q]});if(!us.count(q)&&!s[q].empty())out.push_back({"S"+std::to_string(i)+","+std::to_string(j),s[q]});}else out.push_back({"U"+std::to_string(i)+","+std::to_string(j),a});}
 return out;
}
static std::vector<Chain> rechainedRdiag(int m){
 auto R=raw(false,m);std::map<Lab,std::vector<Pt>>r;for(auto&c:R){Lab q=rr(c.a[0],m);r[q]=c.a;}
 std::map<Lab,std::vector<Pt>>p,s;for(auto&[q,a]:r)if(q.first+q.second<=m){Pt u{q.second,q.first,q.first};for(Pt v:a)(rk(v)<=rk(u)?p[q]:s[q]).push_back(v);}
 std::set<Lab>up,us;std::vector<Chain>out;
 for(int a=1;a<=m-1;a++)for(int j=0;j<=m-a-1;j++){std::vector<Pt>x=p[{a-1,j}];x.insert(x.end(),s[{a,j}].begin(),s[{a,j}].end());out.push_back({"Q"+std::to_string(a-1)+","+std::to_string(j),x});up.insert({a-1,j});us.insert({a,j});}
 for(int a=0;a<=m-1;a++){int j=m-a;out.push_back({"D"+std::to_string(a)+","+std::to_string(j),r[{a,j}]});up.insert({a,j});us.insert({a,j});}
 for(auto&[q,a]:r){int i=q.first,j=q.second;if(i+j<=m){if(!up.count(q)&&!p[q].empty())out.push_back({"P"+std::to_string(i)+","+std::to_string(j),p[q]});if(!us.count(q)&&!s[q].empty())out.push_back({"S"+std::to_string(i)+","+std::to_string(j),s[q]});}else out.push_back({"U"+std::to_string(i)+","+std::to_string(j),a});}
 return out;
}
static std::vector<Chain> splitG(std::vector<Chain> R,int m){
 std::vector<Chain> out;
 for(auto&c:R){int a=-1;if(c.s=="S0,"+std::to_string(m-1))a=0;for(int z=1;z<m;z++)if(c.s=="Q"+std::to_string(z-1)+","+std::to_string(m-z-1))a=z;
  if(a<0){out.push_back(c);continue;}int cut=-1;for(int z=0;z+1<(int)c.a.size();z++){Lab x=ll(c.a[z],m),y=ll(c.a[z+1],m);if((x==Lab{a,m-a}&&y==Lab{a+1,m-a-1})||(y==Lab{a,m-a}&&x==Lab{a+1,m-a-1}))cut=z;}
  assert(cut>=0);out.push_back({c.s+"a",{c.a.begin(),c.a.begin()+cut+1}});out.push_back({c.s+"b",{c.a.begin()+cut+1,c.a.end()}});
 }
 return out;
}
static bool topo(const std::vector<std::set<int>>&g,std::vector<int>*ord=nullptr){std::vector<int>d(g.size());for(auto&s:g)for(int v:s)d[v]++;std::set<int>q;for(int i=0;i<(int)d.size();i++)if(!d[i])q.insert(i);std::vector<int>o;while(!q.empty()){int u=*q.begin();q.erase(q.begin());o.push_back(u);for(int v:g[u])if(!--d[v])q.insert(v);}if(ord)*ord=o;return o.size()==g.size();}
static std::vector<int> onecycle(const std::vector<std::set<int>>&g){std::vector<int>co(g.size()),st,cy;auto dfs=[&](auto&&self,int u)->bool{co[u]=1;st.push_back(u);for(int v:g[u]){if(!co[v]){if(self(self,v))return true;}else if(co[v]==1){auto it=std::find(st.begin(),st.end(),v);cy.assign(it,st.end());return true;}}st.pop_back();co[u]=2;return false;};for(int i=0;i<(int)g.size();i++)if(!co[i]&&dfs(dfs,i))break;return cy;}
static std::pair<std::vector<std::set<int>>,std::vector<std::set<int>>> prec(const std::vector<Chain>&L,const std::vector<Chain>&R,int m){
 std::map<Pt,int> li,ri;for(int i=0;i<(int)L.size();i++)for(Pt p:L[i].a)li[p]=i;for(int i=0;i<(int)R.size();i++)for(Pt p:R[i].a)ri[p]=i;assert(li.size()==ri.size());
 std::vector<std::set<int>> pgR(R.size()),pgL(L.size());
 for(auto&c:L){std::vector<int>s;for(Pt p:c.a){int x=ri[p];if(s.empty()||x!=s.back())s.push_back(x);}for(int i=1;i<(int)s.size();i++)if(s[i]!=s[i-1])pgR[s[i-1]].insert(s[i]);}
 for(auto&c:R){std::vector<int>s;for(Pt p:c.a){int x=li[p];if(s.empty()||x!=s.back())s.push_back(x);}for(int i=1;i<(int)s.size();i++)if(s[i]!=s[i-1])pgL[s[i]].insert(s[i-1]);}
 return{pgL,pgR};
}
static int excess(const std::vector<Chain>&L,const std::vector<Chain>&R,const std::vector<int>&ord){std::map<Pt,int>ri;for(int i=0;i<(int)R.size();i++)for(Pt p:R[i].a)ri[p]=i;std::set<int>N;int best=0,s=0;for(auto it=ord.rbegin();it!=ord.rend();++it){s++;for(Pt p:L[*it].a)N.insert(ri[p]);best=std::max(best,(int)N.size()-s);}return best;}
static int linear_excess(const std::vector<Chain>&L,const std::vector<Chain>&R,int m){int best=1e9;for(int A=-12;A<=12;A++)for(int B=-12;B<=12;B++)if(A||B)for(int ti=0;ti<2;ti++){std::vector<int>o(L.size());std::iota(o.begin(),o.end(),0);std::sort(o.begin(),o.end(),[&](int x,int y){auto p=ll(L[x].a[0],m),q=ll(L[y].a[0],m);auto k1=std::tuple{A*p.first+B*p.second,ti?p.first:-p.first,p.second},k2=std::tuple{A*q.first+B*q.second,ti?q.first:-q.first,q.second};return k1<k2;});best=std::min(best,excess(L,R,o));}return best;}
static int greedy_excess(const std::vector<Chain>&L,const std::vector<Chain>&R){std::map<Pt,int>ri;for(int i=0;i<(int)R.size();i++)for(Pt p:R[i].a)ri[p]=i;std::vector<std::set<int>>n(L.size());for(int i=0;i<(int)L.size();i++)for(Pt p:L[i].a)n[i].insert(ri[p]);int bestAll=1e9;for(int seed=0;seed<8;seed++){std::set<int>N;std::vector<char>use(L.size());int best=0;for(int s=0;s<(int)L.size();s++){int pick=-1,score=1e9;for(int i=0;i<(int)L.size();i++)if(!use[i]){int add=0;for(int v:n[i])add+=!N.count(v);int q=add*100000+(int)n[i].size()*100+int((i*1103515245u+seed*12345u)&63);if(q<score){score=q;pick=i;}}use[pick]=1;for(int v:n[pick])N.insert(v);best=std::max(best,(int)N.size()-(s+1));}bestAll=std::min(bestAll,best);}return bestAll;}
static std::vector<Chain> splitQjoins(std::vector<Chain>R,int m){std::vector<Chain>o;for(auto&c:R){if(c.s.empty()||c.s[0]!='Q'){o.push_back(c);continue;}int comma=c.s.find(','),i=std::stoi(c.s.substr(1,comma-1));int cut=i;assert(cut+1<(int)c.a.size());o.push_back({c.s+"p",{c.a.begin(),c.a.begin()+cut+1}});o.push_back({c.s+"s",{c.a.begin()+cut+1,c.a.end()}});}return o;}
static std::vector<Chain> splitCaps(std::vector<Chain>R,int m,bool joins=true){std::vector<Chain>o;for(auto&c:R){std::set<int>cut;if(joins&&!c.s.empty()&&c.s[0]=='Q'){int comma=c.s.find(','),i=std::stoi(c.s.substr(1,comma-1));cut.insert(i);}int a=-1;if(c.s.rfind("S0,",0)==0)a=0;else if(!c.s.empty()&&c.s[0]=='Q'){int comma=c.s.find(','),i=std::stoi(c.s.substr(1,comma-1));a=i+1;}if(a>=0)for(int z=0;z+1<(int)c.a.size();z++){Lab x=ll(c.a[z],m),y=ll(c.a[z+1],m);if((x==Lab{a,m-a}&&y.first>a)||(y==Lab{a,m-a}&&x.first>a))cut.insert(z);}int lo=0,id=0;for(int z:cut){o.push_back({c.s+char('a'+id++),{c.a.begin()+lo,c.a.begin()+z+1}});lo=z+1;}o.push_back({c.s+char('a'+id),{c.a.begin()+lo,c.a.end()}});}return o;}
static std::vector<Chain> splitLAtP(std::vector<Chain>L,const std::vector<Chain>&R){std::set<Pt>p;for(auto&c:R)if(!c.s.empty()&&c.s[0]=='P')for(Pt x:c.a)p.insert(x);std::vector<Chain>o;for(auto&c:L){std::set<int>cut;for(int z=0;z<(int)c.a.size();z++)if(p.count(c.a[z])){if(z)cut.insert(z-1);if(z+1<(int)c.a.size())cut.insert(z);}int lo=0,id=0;for(int z:cut){o.push_back({c.s+char('a'+id++),{c.a.begin()+lo,c.a.begin()+z+1}});lo=z+1;}o.push_back({c.s+char('a'+id),{c.a.begin()+lo,c.a.end()}});}return o;}
static std::vector<Chain> splitRP(std::vector<Chain>R){std::vector<Chain>o;for(auto&c:R)if(!c.s.empty()&&c.s[0]=='P')for(int z=0;z<(int)c.a.size();z++)o.push_back({c.s+std::to_string(z),{c.a[z]}});else o.push_back(c);return o;}
int main(int argc,char**argv){int lo=1,hi=40;if(argc>1)lo=hi=std::stoi(argv[1]);for(int m=lo;m<=hi;m++){auto L=raw(true,m),R=rechainedR(m);std::string mode=argc>2?argv[2]:"g";if(mode=="b"){std::cout<<m<<" linear_excess="<<linear_excess(L,R,m)<<" imbalance="<<R.size()-L.size()<<"\n";continue;}auto Rg=mode=="q"?splitQjoins(R,m):mode=="c"?splitCaps(R,m,true):mode=="k"?splitCaps(R,m,false):splitG(R,m);if(mode=="p"){Rg=R;L=splitLAtP(L,R);}auto [pl,pr]=prec(L,Rg,m);std::vector<int>ol,orr;bool al=topo(pl,&ol),ar=topo(pr,&orr);std::cout<<m<<" L="<<L.size()<<" R="<<R.size()<<" Rg="<<Rg.size()<<" PL="<<al<<" PR="<<ar;if(al)std::cout<<" excess="<<excess(L,Rg,ol)<<" imbalance="<<Rg.size()-L.size();std::cout<<"\n";if(argc>1){auto a=onecycle(pl),b=onecycle(pr);std::cout<<"PLcycle";for(int x:a)std::cout<<" "<<L[x].s;std::cout<<"\nPRcycle";for(int x:b)std::cout<<" "<<Rg[x].s;std::cout<<"\n";if(argc>3){std::cout<<"PLorder";for(int x:ol)std::cout<<" "<<L[x].s;std::cout<<"\nPRorder";for(int x:orr)std::cout<<" "<<Rg[x].s;std::cout<<"\n";if(argc>4)for(int z=0;z<(int)orr.size();z++){auto&c=Rg[orr[z]];std::cout<<z<<" "<<c.s<<" ranks="<<rk(c.a.front())<<".."<<rk(c.a.back())<<" L=";for(Pt p:c.a){auto q=ll(p,m);std::cout<<q.first<<","<<q.second<<";";}std::cout<<"\n";}}}}}
