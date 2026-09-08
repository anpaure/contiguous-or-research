// Necessary 4-clique cuts for covering old private cores by three products.
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <vector>
using namespace std;
using Bits=array<uint64_t,2>;
bool four_clique(const vector<Bits>& a,const vector<Bits>& b,const vector<Bits>& c,int n) {
    vector<Bits> g(n);for(int i=0;i<n;++i)for(int z=0;z<2;++z)g[i][z]=a[i][z]&b[i][z]&c[i][z];
    for(int u=0;u<n;++u)for(int z=u/64;z<2;++z) {
        uint64_t neighbors=g[u][z];if(z==u/64)neighbors&=~0ULL<<(u%64);neighbors&=~(z==u/64?1ULL<<(u%64):0ULL);
        while(neighbors) {
            int v=64*z+__builtin_ctzll(neighbors);neighbors&=neighbors-1;
            Bits common{};for(int k=0;k<2;++k)common[k]=g[u][k]&g[v][k];
            for(int k=0;k<2;++k){if(k<v/64)common[k]=0;else if(k==v/64){common[k]&=~0ULL<<(v%64);common[k]&=~(1ULL<<(v%64));}}
            for(int k=0;k<2;++k) {
                uint64_t candidates=common[k];while(candidates){int w=64*k+__builtin_ctzll(candidates);candidates&=candidates-1;
                    if((g[w][0]&common[0])||(g[w][1]&common[1]))return true;
                }
            }
        }
    }
    return false;
}
int main(){
    ios::sync_with_stdio(false);cin.tie(nullptr);
    int nr;if(!(cin>>nr))return 2;vector<int> cost(nr),old(nr),weights(4096),mult(4096);for(int&w:weights)cin>>w;
    vector<set<int>> supports(nr);for(int i=0;i<nr;++i){int n;cin>>cost[i]>>old[i]>>n;while(n--){int p;cin>>p;supports[i].insert(p);++mult[p];}}
    vector<int> splits;for(int m=1;m<63;m+=2)splits.push_back(m);
    vector<array<int,3>> triples;for(int s=0;s<31;++s)for(int t=s;t<31;++t)for(int u=t;u<31;++u)triples.push_back({s,t,u});
    int nw=(triples.size()+63)/64;vector<vector<uint64_t>> possible(nr,vector<uint64_t>(nw));
    map<int,int> survivors_hist;long long tests=0,blocked=0;
    for(int row=0;row<nr;++row) {
        vector<int> p;for(int x:supports[row])if(mult[x]==1)p.push_back(x);int n=p.size();if(n>128)abort();
        vector<vector<Bits>> graph(31,vector<Bits>(n));
        for(int i=0;i<n;++i)for(int j=i+1;j<n;++j){int up=0,down=0;for(int a=0;a<6;++a){int x=(p[i]>>(2*a))&3,y=(p[j]>>(2*a))&3;if(x<y)up|=1<<a;if(x>y)down|=1<<a;}
            if(!up||!down)continue;for(int s=0;s<31;++s){int m=splits[s];bool ok=((up&m)==up&&!(down&m))||((down&m)==down&&!(up&m));if(!ok){graph[s][i][j/64]|=1ULL<<(j%64);graph[s][j][i/64]|=1ULL<<(i%64);}}
        }
        int survivors=0;
        for(int z=0;z<(int)triples.size();++z){auto [s,t,u]=triples[z];bool contains=splits[s]==old[row]||splits[t]==old[row]||splits[u]==old[row];
            bool fail=false;if(!contains){++tests;fail=four_clique(graph[s],graph[t],graph[u],n);if(fail)++blocked;else ++survivors;}
            if(!fail)possible[row][z/64]|=1ULL<<(z%64);
        }
        ++survivors_hist[survivors];
    }
    long long row_triples=0,forced=0,alt_count=0;int min_alt=100000,max_alt=0;
    for(int i=0;i<nr;++i)for(int j=i+1;j<nr;++j)for(int k=j+1;k<nr;++k){
        ++row_triples;int count=0;array<int,3> original{old[i],old[j],old[k]};sort(original.begin(),original.end());
        for(int z=0;z<nw;++z){uint64_t v=possible[i][z]&possible[j][z]&possible[k][z];while(v){int id=64*z+__builtin_ctzll(v);v&=v-1;if(id>=(int)triples.size())abort();auto [s,t,u]=triples[id];array<int,3> now{splits[s],splits[t],splits[u]};if(now!=original)++count;}}
        if(!count)++forced;alt_count+=count;min_alt=min(min_alt,count);max_alt=max(max_alt,count);
    }
    cout<<"PRIVATE_CUT tests="<<tests<<" blocked="<<blocked<<" survivors="<<tests-blocked<<'\n';
    cout<<"PER_ROW_OMITTING_OLD_SURVIVORS";for(auto[n,count]:survivors_hist)cout<<' '<<n<<':'<<count;cout<<'\n';
    cout<<"THREE_ROW necessary_cases="<<row_triples<<" no_alternative_after_cuts="<<forced<<" alternative_support_instances="<<alt_count<<" min="<<min_alt<<" max="<<max_alt<<'\n';
}
