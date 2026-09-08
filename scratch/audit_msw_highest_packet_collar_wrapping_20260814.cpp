#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <string>
#include <tuple>
#include <unordered_map>
#include <utility>
#include <vector>
#ifdef _OPENMP
#include <omp.h>
#endif

// H100-only targeted audit of highest-valley packets under a collar profile.
// For every nonmountain root, test whether at least one highest-valley packet
// has a collar witness and continues to have one after H primitive wrappings.

using U = std::uint64_t;
constexpr int MAX_FIELDS = 32;

static std::pair<U,int> g(U x,int m){std::vector<int>b(2*m);int h=0,z=0;for(int i=0;i<2*m;++i){b[i]=h;if(!((x>>i)&1U)&&h==0)++z;h+=(x>>i)&1U?1:-1;}int s=0;for(int i=0;i<2*m;++i)if(!((x>>i)&1U)&&(b[i]==0||b[i]==1)&&++s==z+1)return{x|(U{1}<<i),i};assert(false);return{};}
static std::pair<U,int> hmap(U x,int m){std::vector<int>b(2*m);int h=0,o=0;for(int i=0;i<2*m;++i){b[i]=h;if(((x>>i)&1U)&&h==1)++o;h+=(x>>i)&1U?1:-1;}int s=0;for(int i=0;i<2*m;++i)if(((x>>i)&1U)&&(b[i]==0||b[i]==1)&&++s==o)return{x&~(U{1}<<i),i};assert(false);return{};}
static std::vector<int> order(U root,int m){U x=root;int n=2*m+1;std::vector<int>rho;rho.reserve(n);for(int e=0;e<m;++e){auto a=g(x,m);auto b=hmap(a.first,m);rho.push_back(a.second);rho.push_back(b.second);x=b.first;}rho.push_back(2*m);std::vector<int>r(n);for(int i=0;i<n;++i)r[i]=rho[(2*i)%n];return r;}
static U wrap(U x){return U{1}|(x<<1);}

struct Entry {std::array<U,MAX_FIELDS> forced{},maximal{};int fields=0,orientation=0,start=0;};
struct Key {std::array<U,MAX_FIELDS> values{};int fields=0;bool operator==(Key const&o)const{return fields==o.fields&&values==o.values;}};
struct KeyHash {std::size_t operator()(Key const&k)const{std::size_t h=k.fields;for(int i=0;i<k.fields;++i)h^=std::hash<U>{}(k.values[i]+0x9e3779b97f4a7c15ULL+(h<<6)+(h>>2));return h;}};

static std::vector<Entry> entries(U root,int m,int d,int t){assert(d+t<16);int n=2*m+1;auto row=order(root,m);std::vector<Entry>out;out.reserve(2*n);for(int orientation=0;orientation<2;++orientation){for(int start=0;start<n;++start){Entry e;e.orientation=orientation;e.start=start;for(int q=d;q<=d+t;++q){int s=m+1-q;for(int offset=0;offset<q;++offset){assert(e.fields<MAX_FIELDS);U maximal=0;for(int step=0;step<s;++step)maximal|=U{1}<<row[(start+offset+step)%n];U forced=(U{1}<<row[(start+offset)%n])|(U{1}<<row[(start+offset+s-1)%n]);e.forced[e.fields]=forced;e.maximal[e.fields]=maximal;++e.fields;}}out.push_back(e);}std::reverse(row.begin(),row.end());}return out;}

static int equality_fields(int d,int t,bool contain){if(!contain||t==0){int count=0;for(int q=d;q<=d+t;++q)count+=q;return count;}int count=0;for(int q=d;q<d+t;++q)count+=q;return count;}
static Key key(Entry const&e,int count){Key k;k.fields=count;for(int i=0;i<count;++i)k.values[i]=e.forced[i];return k;}
static bool compatible(U a,U b,int m,int d,int t,bool contain){auto left=entries(a,m,d,t),right=entries(b,m,d,t);int equal=equality_fields(d,t,contain);std::unordered_multimap<Key,int,KeyHash>table;table.reserve(2*right.size());for(int j=0;j<(int)right.size();++j)table.emplace(key(right[j],equal),j);for(auto const&x:left){auto range=table.equal_range(key(x,equal));for(auto it=range.first;it!=range.second;++it){auto const&y=right[it->second];bool okay=true;for(int f=equal;f<x.fields;++f)okay&=((x.forced[f]|y.forced[f])&~(x.maximal[f]&y.maximal[f]))==0;if(okay)return true;}}return false;}

struct Move{int p,q,type;};
static std::vector<Move> highest_moves(U root,int m){std::vector<int>height(2*m+1);for(int i=0;i<2*m;++i)height[i+1]=height[i]+((root>>i)&1U?1:-1);int maximum=-1;for(int v=0;v+1<2*m;++v)if(((root>>v)&3U)==2U)maximum=std::max(maximum,height[v]);std::vector<Move>moves;for(int v=0;v+1<2*m;++v)if(((root>>v)&3U)==2U&&height[v]==maximum){moves.push_back({v,v+1,0});bool left=v>0&&!((root>>(v-1))&1U),right=v+2<2*m&&((root>>(v+2))&1U);if(left)moves.push_back({v-1,v+1,1});if(right)moves.push_back({v,v+2,2});if(left&&right)moves.push_back({v-1,v+2,3});}return moves;}

int main(int argc,char**argv){assert(argc==6);int m=std::stoi(argv[1]),d=std::stoi(argv[2]),t=std::stoi(argv[3]),H=std::stoi(argv[4]);bool contain=std::string(argv[5])=="contain";assert(2*(m+H)+1<63);
    std::vector<U>roots;auto gen=[&](auto&&self,int pos,int up,int down,U x)->void{if(pos==2*m){roots.push_back(x);return;}if(up<m)self(self,pos+1,up+1,down,x|(U{1}<<pos));if(down<up)self(self,pos+1,up,down+1,x);};gen(gen,0,0,0,0);U mountain=(U{1}<<m)-1;
    std::uint64_t nonmountain=0,source_good=0,stable_good=0;std::array<std::uint64_t,4>chosen{};std::vector<std::string>examples;
    #pragma omp parallel for schedule(dynamic,64) reduction(+:nonmountain,source_good,stable_good)
    for(std::int64_t index=0;index<(std::int64_t)roots.size();++index){
        U root=roots[index];if(root==mountain)continue;++nonmountain;
        bool any_source=false,any_stable=false;int stable_type=-1;
        for(auto move:highest_moves(root,m)){
            U mate=root^(U{1}<<move.p)^(U{1}<<move.q);
            if(!compatible(root,mate,m,d,t,contain))continue;
            any_source=true;U a=root,b=mate;bool survives=true;
            for(int h=1;h<=H;++h){a=wrap(a);b=wrap(b);survives&=compatible(a,b,m+h,d,t,contain);}
            if(survives){any_stable=true;stable_type=move.type;break;}
        }
        source_good+=any_source;stable_good+=any_stable;
        if(any_stable){
            #pragma omp atomic update
            chosen[stable_type]++;
        }else{
            #pragma omp critical
            {
                if(examples.size()<20){std::string s;for(int i=0;i<2*m;++i)s.push_back((root>>i)&1U?'1':'0');examples.push_back(s);}
            }
        }
    }
    std::cout<<"SUMMARY m="<<m<<" d="<<d<<" t="<<t<<" H="<<H<<" mode="<<(contain?"contain":"equal")<<" roots="<<roots.size()<<" nonmountain="<<nonmountain<<" source_good="<<source_good<<" source_bad="<<nonmountain-source_good<<" stable_good="<<stable_good<<" stable_bad="<<nonmountain-stable_good<<" chosen_01="<<chosen[0]<<" chosen_001="<<chosen[1]<<" chosen_011="<<chosen[2]<<" chosen_0011="<<chosen[3]<<'\n';for(auto const&s:examples)std::cout<<"BAD "<<s<<'\n';
}
