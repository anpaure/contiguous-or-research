#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <tuple>
#include <unordered_map>
#include <utility>
#include <vector>

// H100-only audit of universal parent ports per inverse highest-valley packet.

using U = std::uint64_t;
enum Packet { P01 = 0, P001 = 1, P011 = 2, P0011 = 3 };
static const char* names[] = {"01", "001", "011", "0011"};

static std::pair<U,int> g(U x,int m){
    std::vector<int> before(2*m); int h=0,d0=0;
    for(int i=0;i<2*m;++i){before[i]=h;if(!((x>>i)&1U)&&h==0)++d0;h+=(x>>i)&1U?1:-1;}
    int seen=0;for(int i=0;i<2*m;++i)if(!((x>>i)&1U)&&(before[i]==0||before[i]==1)&&++seen==d0+1)return{x|(U{1}<<i),i};
    assert(false);return{};
}
static std::pair<U,int> hmap(U y,int m){
    std::vector<int> before(2*m);int h=0,u1=0;
    for(int i=0;i<2*m;++i){before[i]=h;if(((y>>i)&1U)&&h==1)++u1;h+=(y>>i)&1U?1:-1;}
    int seen=0;for(int i=0;i<2*m;++i)if(((y>>i)&1U)&&(before[i]==0||before[i]==1)&&++seen==u1)return{y&~(U{1}<<i),i};
    assert(false);return{};
}
static std::vector<int> tight_order(U root,int m){
    U x=root;int n=2*m+1;std::vector<int> rho;
    for(int e=0;e<m;++e){auto a=g(x,m);auto b=hmap(a.first,m);rho.push_back(a.second);rho.push_back(b.second);x=b.first;}
    rho.push_back(2*m);std::vector<int> out(n);for(int j=0;j<n;++j)out[j]=rho[(2*j)%n];return out;
}
using Rail=std::pair<int,int>;using Signature=std::vector<Rail>;
static std::array<std::vector<Signature>,2> signatures(U root,int m,int d){
    std::array<std::vector<Signature>,2> out;auto row=tight_order(root,m);int n=2*m+1,s=m+1-d;
    for(int orientation=0;orientation<2;++orientation){
        out[orientation].assign(n,Signature(d));
        for(int a=0;a<n;++a)for(int j=0;j<d;++j){int x=row[(a+j)%n],y=row[(a+s-1+j)%n];if(x>y)std::swap(x,y);out[orientation][a][j]={x,y};}
        std::reverse(row.begin(),row.end());
    }
    return out;
}
static int cyclic_distance(int a,int b,int n){int x=std::abs(a-b);return std::min(x,n-x);}
static std::string bit_word(U x,int m){std::string s;for(int i=0;i<2*m;++i)s.push_back((x>>i)&1U?'1':'0');return s;}

int main(int argc,char**argv){
    assert(argc==3);int m=std::stoi(argv[1]),d=std::stoi(argv[2]),n=2*m+1;assert(m>=3*d+1&&n<63);
    std::vector<U> roots;auto gen=[&](auto&&self,int pos,int up,int down,U x)->void{if(pos==2*m){roots.push_back(x);return;}if(up<m)self(self,pos+1,up+1,down,x|(U{1}<<pos));if(down<up)self(self,pos+1,up,down+1,x);};gen(gen,0,0,0,0);
    std::unordered_map<U,int> index;index.reserve(2*roots.size());for(int i=0;i<(int)roots.size();++i)index[roots[i]]=i;
    int root=index.at((U{1}<<m)-1);
    std::vector<std::array<std::vector<Signature>,2>> sig;sig.reserve(roots.size());for(U x:roots)sig.push_back(signatures(x,m,d));

    // children[parent][packet] contains every child obtained by that packet at
    // any highest valley. Duplicates are removed.
    std::vector<std::array<std::vector<int>,4>> children(roots.size());
    for(int child=0;child<(int)roots.size();++child){if(child==root)continue;U x=roots[child];int h=0,maximum=-1;std::vector<int> valleys;
        for(int v=0;v+1<2*m;++v){if(((x>>v)&3U)==2U){if(h>maximum){maximum=h;valleys.clear();}if(h==maximum)valleys.push_back(v);}h+=(x>>v)&1U?1:-1;}
        for(int v:valleys){std::vector<std::tuple<int,int,Packet>> moves={{v,v+1,P01}};bool left=v>0&&!((x>>(v-1))&1U);bool right=v+2<2*m&&((x>>(v+2))&1U);if(left)moves.push_back({v-1,v+1,P001});if(right)moves.push_back({v,v+2,P011});if(left&&right)moves.push_back({v-1,v+2,P0011});
            for(auto[p,q,packet]:moves){int par=index.at(x^(U{1}<<p)^(U{1}<<q));children[par][packet].push_back(child);}}
    }
    for(auto& row:children)for(auto& list:row){std::sort(list.begin(),list.end());list.erase(std::unique(list.begin(),list.end()),list.end());}

    for(int orientation=0;orientation<2;++orientation){
        long long nonempty_fibres=0,empty_intersections=0,parents_with_types=0,parents_packable=0,parents_universal_failure=0;
        int max_fibre=0,max_types=0;std::array<long long,4> type_nonempty{},type_fail{};int printed=0;
        for(int parent=0;parent<(int)roots.size();++parent){
            std::array<std::vector<int>,4> universal;std::vector<int> types;
            for(int packet=0;packet<4;++packet){auto const& list=children[parent][packet];if(list.empty())continue;++nonempty_fibres;++type_nonempty[packet];types.push_back(packet);max_fibre=std::max(max_fibre,(int)list.size());
                std::vector<char> common(n,1);
                for(int child:list){std::vector<char> admitted(n,0);for(int b=0;b<n;++b)for(int a=0;a<n;++a)if(sig[parent][orientation][b]==sig[child][orientation][a]){admitted[b]=1;break;}for(int b=0;b<n;++b)common[b]&=admitted[b];}
                for(int b=0;b<n;++b)if(common[b])universal[packet].push_back(b);
                if(universal[packet].empty()){++empty_intersections;++type_fail[packet];if(printed<12){std::cout<<"EMPTY orientation="<<orientation<<" parent="<<parent<<" packet="<<names[packet]<<" multiplicity="<<list.size()<<" word="<<bit_word(roots[parent],m)<<" children=";for(int c:list)std::cout<<bit_word(roots[c],m)<<',';std::cout<<'\n';++printed;}}
            }
            if(types.empty())continue;++parents_with_types;max_types=std::max(max_types,(int)types.size());bool all_nonempty=true;for(int packet:types)all_nonempty&=!universal[packet].empty();if(!all_nonempty){++parents_universal_failure;continue;}
            bool feasible=false;std::vector<int> chosen;
            auto search=[&](auto&&self,int k)->void{if(feasible)return;if(k==(int)types.size()){feasible=true;return;}for(int port:universal[types[k]]){bool okay=true;for(int old:chosen)if(port!=old&&cyclic_distance(port,old,n)<d+1){okay=false;break;}if(!okay)continue;chosen.push_back(port);self(self,k+1);chosen.pop_back();}};search(search,0);if(feasible)++parents_packable;else if(printed<20){std::cout<<"UNPACKABLE orientation="<<orientation<<" parent="<<parent<<" word="<<bit_word(roots[parent],m)<<" sets=";for(int packet:types){std::cout<<names[packet]<<'[';for(int port:universal[packet])std::cout<<port<<',';std::cout<<']';}std::cout<<'\n';++printed;}
        }
        std::cout<<"SUMMARY m="<<m<<" d="<<d<<" orientation="<<orientation<<" roots="<<roots.size()<<" nonempty_fibres="<<nonempty_fibres<<" empty_intersections="<<empty_intersections<<" max_fibre="<<max_fibre<<" parents_with_types="<<parents_with_types<<" max_types="<<max_types<<" parents_universal_failure="<<parents_universal_failure<<" parents_packable="<<parents_packable<<" type_nonempty=";for(int p=0;p<4;++p)std::cout<<names[p]<<':'<<type_nonempty[p]<<',';std::cout<<" type_fail=";for(int p=0;p<4;++p)std::cout<<names[p]<<':'<<type_fail[p]<<',';std::cout<<'\n';
    }
}
