// Exact feasibility reduction for two replacement rectangles with free splits.
// No chain catalogue and no optimization solver are used here.
#include <algorithm>
#include <array>
#include <cstdint>
#include <functional>
#include <iostream>
#include <map>
#include <set>
#include <vector>
using namespace std;
using Bits=array<uint64_t,4>;
struct Pair {int i,j;uint32_t bad;};

bool bipartite(const vector<Bits>& a,const vector<Bits>& b,int n,vector<int>* odd=nullptr) {
    array<Bits,2> colors{};Bits used{}; vector<int> color(n,-1),parent(n,-1),queue;
    for(int root=0;root<n;++root) if(color[root]<0) {
        queue.clear();queue.push_back(root);color[root]=0;
        colors[0][root/64]|=1ULL<<(root%64);used[root/64]|=1ULL<<(root%64);
        for(size_t at=0;at<queue.size();++at) {
            int v=queue[at],c=color[v];
            for(int z=0;z<4;++z) {
                uint64_t e=a[v][z]&b[v][z];
                if(e&colors[c][z]) {
                    if(odd) {
                        int w=64*z+__builtin_ctzll(e&colors[c][z]);
                        vector<int> position(n,-1),first,second;
                        for(int x=v;x>=0;x=parent[x]){position[x]=first.size();first.push_back(x);}
                        int x=w;while(position[x]<0){second.push_back(x);x=parent[x];}
                        first.resize(position[x]+1);reverse(second.begin(),second.end());
                        first.insert(first.end(),second.begin(),second.end());*odd=first;
                    }
                    return false;
                }
                uint64_t fresh=e&~used[z];
                while(fresh) {
                    int bit=__builtin_ctzll(fresh),w=64*z+bit;fresh&=fresh-1;
                    color[w]=1-c;parent[w]=v;queue.push_back(w);
                    used[z]|=1ULL<<bit;colors[1-c][z]|=1ULL<<bit;
                }
            }
        }
    }
    return true;
}

vector<int> solve2sat(const vector<Pair>& pairs,int s,int t,int n,
                     vector<int>* path0=nullptr,vector<int>* path1=nullptr) {
    vector<vector<int>> g(2*n),back(2*n);
    auto edge=[&](int a,int b){g[a].push_back(b);back[b].push_back(a);};
    for(auto p:pairs) {
        if(p.bad&(1U<<s)){edge(2*p.i+1,2*p.j);edge(2*p.j+1,2*p.i);}
        if(p.bad&(1U<<t)){edge(2*p.i,2*p.j+1);edge(2*p.j,2*p.i+1);}
    }
    vector<int> seen(2*n),order,component(2*n,-1);
    function<void(int)> dfs=[&](int v){seen[v]=1;for(int w:g[v])if(!seen[w])dfs(w);order.push_back(v);};
    for(int v=0;v<2*n;++v)if(!seen[v])dfs(v);
    function<void(int,int)> rev=[&](int v,int c){component[v]=c;for(int w:back[v])if(component[w]<0)rev(w,c);};
    int c=0;for(auto it=order.rbegin();it!=order.rend();++it)if(component[*it]<0)rev(*it,c++);
    vector<int> assignment(n);
    auto path=[&](int source,int target) {
        vector<int> parent(2*n,-1),queue{source};parent[source]=source;
        for(size_t at=0;at<queue.size()&&parent[target]<0;++at)
            for(int w:g[queue[at]])if(parent[w]<0){parent[w]=queue[at];queue.push_back(w);}
        if(parent[target]<0)abort();vector<int> result;
        for(int v=target;;v=parent[v]){result.push_back(v);if(v==source)break;}
        reverse(result.begin(),result.end());return result;
    };
    for(int i=0;i<n;++i){if(component[2*i]==component[2*i+1]){
        if(path0)*path0=path(2*i,2*i+1);if(path1)*path1=path(2*i+1,2*i);return {};
    }assignment[i]=component[2*i+1]>component[2*i];}
    for(auto p:pairs) {
        if((p.bad&(1U<<s))&&assignment[p.i]&&assignment[p.j])abort();
        if((p.bad&(1U<<t))&&!assignment[p.i]&&!assignment[p.j])abort();
    }
    return assignment;
}

int main(int argc,char** argv) {
    ios::sync_with_stdio(false);cin.tie(nullptr);
    bool certificate=argc>1&&string(argv[1])=="--certificate";
    int nr;if(!(cin>>nr))return 2;vector<int> costs(nr),oldsplit(nr),weights(4096),multiplicity(4096);
    for(int& w:weights)cin>>w;
    vector<set<int>> supports(nr),privatepoints(nr);
    for(int i=0;i<nr;++i){int n;cin>>costs[i]>>oldsplit[i]>>n;while(n--){int p;cin>>p;supports[i].insert(p);++multiplicity[p];}}
    for(int i=0;i<nr;++i)for(int p:supports[i])if(multiplicity[p]==1)privatepoints[i].insert(p);
    vector<int> splits,projectionmask;
    for(int mask=1;mask<63;mask+=2){splits.push_back(mask);int m=0;for(int i=0;i<6;++i)if(mask>>i&1)m|=3<<(2*i);projectionmask.push_back(m);}
    array<array<uint32_t,64>,64> conflict{};
    for(int up=0;up<64;++up)for(int down=0;down<64;++down)if(up&&down&&!(up&down))
        for(int s=0;s<31;++s){int mask=splits[s];bool ok=((up&mask)==up&&!(down&mask))||((down&mask)==down&&!(up&mask));if(!ok)conflict[up][down]|=1U<<s;}
    array<array<int,6>,4096> digits{};for(int p=0;p<4096;++p)for(int i=0;i<6;++i)digits[p][i]=(p>>(2*i))&3;
    long long dual_pruned=0,tested=0,bip_pass=0,sat=0,original_sat=0,alternative_sat=0;
    long long residuals=0;map<int,long long> potential;
    for(int i=0;i<nr;++i)for(int j=i+1;j<nr;++j) {
        set<int> need=privatepoints[i];need.insert(privatepoints[j].begin(),privatepoints[j].end());
        for(int p:supports[i])if(multiplicity[p]==2&&supports[j].count(p))need.insert(p);
        int lower=0;for(int p:need)lower+=weights[p];lower=(lower+11)/12;
        int old=costs[i]+costs[j];++potential[old-lower];if(lower>=old){++dual_pruned;if(certificate)cout<<"P "<<i<<' '<<j<<'\n';continue;}
        vector<int> points(need.begin(),need.end());int n=points.size();if(n>256)abort();++residuals;
        if(certificate)cout<<"R "<<i<<' '<<j<<' '<<n<<'\n';
        vector<Pair> pairs;vector<vector<Bits>> graph(31,vector<Bits>(n));
        for(int a=0;a<n;++a)for(int b=a+1;b<n;++b) {
            int up=0,down=0;for(int z=0;z<6;++z){if(digits[points[a]][z]<digits[points[b]][z])up|=1<<z;if(digits[points[a]][z]>digits[points[b]][z])down|=1<<z;}
            uint32_t bad=conflict[up][down];if(!bad)continue;pairs.push_back({a,b,bad});
            while(bad){int z=__builtin_ctz(bad);bad&=bad-1;graph[z][a][b/64]|=1ULL<<(b%64);graph[z][b][a/64]|=1ULL<<(a%64);}
        }
        for(int s=0;s<31;++s)for(int t=s;t<31;++t) {
            vector<int> odd,path0,path1;
            ++tested;if(!bipartite(graph[s],graph[t],n,certificate?&odd:nullptr)){
                if(certificate){cout<<"O "<<s<<' '<<t<<' '<<odd.size();for(int v:odd)cout<<' '<<v;cout<<'\n';}continue;
            }++bip_pass;
            auto assignment=solve2sat(pairs,s,t,n,certificate?&path0:nullptr,certificate?&path1:nullptr);
            if(assignment.empty()){
                if(certificate){cout<<"U "<<s<<' '<<t<<' '<<path0.size();for(int v:path0)cout<<' '<<v;cout<<' '<<path1.size();for(int v:path1)cout<<' '<<v;cout<<'\n';}continue;
            }++sat;
            if(certificate){cout<<"S "<<s<<' '<<t<<' ';for(int v:assignment)cout<<v;cout<<'\n';}
            bool original=(splits[s]==oldsplit[i]&&splits[t]==oldsplit[j])||(splits[s]==oldsplit[j]&&splits[t]==oldsplit[i]);
            if(original)++original_sat;else ++alternative_sat;
            array<set<int>,4> projections;
            for(int a=0;a<n;++a){int r=assignment[a]?0:1;int mask=projectionmask[r?t:s];projections[2*r].insert(points[a]&mask);projections[2*r+1].insert(points[a]&(4095^mask));}
            int cost=0;for(auto& p:projections)cost+=p.size();
            if(!original&&!certificate)cout<<"ALT "<<i<<' '<<j<<' '<<splits[s]<<' '<<splits[t]<<' '<<old<<' '<<cost<<' '<<n<<'\n';
            if(cost<old){cout<<"IMPROVE "<<i<<' '<<j<<' '<<splits[s]<<' '<<splits[t]<<' '<<cost<<'\n';for(int a=0;a<n;++a)cout<<points[a]<<':'<<assignment[a]<<' ';cout<<'\n';return 0;}
        }
    }
    cout<<"SUMMARY dual_pruned="<<dual_pruned<<" residuals="<<residuals<<" tested="<<tested<<" bip_pass="<<bip_pass<<" sat="<<sat<<" original_sat="<<original_sat<<" alternative_sat="<<alternative_sat<<'\n';
    cout<<"DUAL_SAVING_LIMITS";for(auto [saving,count]:potential)cout<<' '<<saving<<':'<<count;cout<<'\n';
}
