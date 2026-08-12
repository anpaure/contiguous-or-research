#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#endif

#include <algorithm>
#include <bit>
#include <fstream>
#include <iostream>
#include <queue>
#include <set>
#include <tuple>
#include <vector>
using namespace std;

struct Edge { int to, reverse, capacity; };
struct Dinic {
    vector<vector<Edge>> g; vector<int> level,next;
    explicit Dinic(int n):g(n),level(n),next(n){}
    void add(int a,int b,int c){Edge x{b,(int)g[b].size(),c},y{a,(int)g[a].size(),0};g[a].push_back(x);g[b].push_back(y);}
    bool bfs(int s,int t){fill(level.begin(),level.end(),-1);queue<int>q;q.push(s);level[s]=0;while(!q.empty()){int a=q.front();q.pop();for(auto&e:g[a])if(e.capacity&&level[e.to]<0)level[e.to]=level[a]+1,q.push(e.to);}return level[t]>=0;}
    int dfs(int a,int t,int f){if(a==t)return f;for(int&i=next[a];i<(int)g[a].size();++i){Edge&e=g[a][i];if(!e.capacity||level[e.to]!=level[a]+1)continue;int z=dfs(e.to,t,min(f,e.capacity));if(z){e.capacity-=z;g[e.to][e.reverse].capacity+=z;return z;}}return 0;}
    int flow(int s,int t){int z=0;while(bfs(s,t)){fill(next.begin(),next.end(),0);while(int f=dfs(s,t,1e9))z+=f;}return z;}
};

static vector<int> read(const char* name){ifstream in(name);vector<int>a;for(int x;in>>x;)a.push_back(x);return a;}

int main(int argc,char**argv){
    if(argc!=3)return 2;vector<int> seed=read(argv[1]),aux=read(argv[2]);if(seed.size()!=462||aux.size()!=462)return 2;
    constexpr int limit=1<<11;
    vector<int> seed_upper(limit,-1), upper_count(limit), lower_present(limit);
    set<pair<int,int>> auxiliary_pairs;
    for(int i=0;i+1<(int)seed.size();++i){int c=seed[i]&seed[i+1],u=seed[i]|seed[i+1];seed_upper[c]=u;lower_present[c]=1;++upper_count[u];}
    for(int i=0;i+1<(int)aux.size();++i)auxiliary_pairs.insert({aux[i]&aux[i+1],aux[i]|aux[i+1]});
    vector<int> missing,lowers,uppers;
    for(int x=0;x<limit;++x){int r=popcount((unsigned)x);if(r==5&&lower_present[x])lowers.push_back(x);if(r==7){uppers.push_back(x);if(!upper_count[x])missing.push_back(x);}}
    int S=0,mo=1,lo=mo+missing.size(),uo=lo+lowers.size(),T=uo+uppers.size();Dinic f(T+1);vector<int> un(limit,-1);
    for(int i=0;i<(int)uppers.size();++i){un[uppers[i]]=uo+i;f.add(uo+i,T,max(0,upper_count[uppers[i]]-1));}
    for(int i=0;i<(int)missing.size();++i){f.add(S,mo+i,1);for(int j=0;j<(int)lowers.size();++j){int c=lowers[j];if(auxiliary_pairs.count({c,missing[i]})&&upper_count[seed_upper[c]]>=2)f.add(mo+i,lo+j,1);}}
    for(int j=0;j<(int)lowers.size();++j)f.add(lo+j,un[seed_upper[lowers[j]]],1);
    int value=f.flow(S,T);cerr<<"missing="<<missing.size()<<" assigned="<<value<<'\n';
    for(int i=0;i<(int)missing.size();++i)for(auto&e:f.g[mo+i])if(e.to>=lo&&e.to<uo&&!e.capacity)cout<<lowers[e.to-lo]<<' '<<missing[i]<<'\n';
    return value==(int)missing.size()?0:1;
}
