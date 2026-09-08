#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <string>
#include <utility>
#include <vector>
#ifdef _OPENMP
#include <omp.h>
#endif

// H100-only end-to-end audit of the thirteen universal-port theorem.
// Reconstruct actual canonical MSW tight orders and the case-selected
// leftmost-highest parent for every Dyck root at the requested (m,d).

using U = std::uint64_t;
constexpr int MAX_N = 63;

static std::pair<U,int> g(U x,int m){std::array<int,MAX_N>b{};int h=0,z=0;for(int i=0;i<2*m;++i){b[i]=h;if(!((x>>i)&1U)&&h==0)++z;h+=(x>>i)&1U?1:-1;}int seen=0;for(int i=0;i<2*m;++i)if(!((x>>i)&1U)&&(b[i]==0||b[i]==1)&&++seen==z+1)return{x|(U{1}<<i),i};assert(false);return{};}
static std::pair<U,int> hmap(U x,int m){std::array<int,MAX_N>b{};int h=0,o=0;for(int i=0;i<2*m;++i){b[i]=h;if(((x>>i)&1U)&&h==1)++o;h+=(x>>i)&1U?1:-1;}int seen=0;for(int i=0;i<2*m;++i)if(((x>>i)&1U)&&(b[i]==0||b[i]==1)&&++seen==o)return{x&~(U{1}<<i),i};assert(false);return{};}
struct Orders{std::array<unsigned char,MAX_N> flip{},tight{};};
static Orders canonical_orders(U root,int m){U x=root;int n=2*m+1;Orders out;int length=0;for(int e=0;e<m;++e){auto a=g(x,m);auto b=hmap(a.first,m);out.flip[length++]=a.second;out.flip[length++]=b.second;x=b.first;}out.flip[length++]=2*m;assert(length==n);for(int i=0;i<n;++i)out.tight[i]=out.flip[(2*i)%n];return out;}

struct Choice{U parent;int type;};
static Choice choose(U word,int m){std::array<int,MAX_N>height{},mate{},stack{};mate.fill(-1);int top=0;for(int i=0;i<2*m;++i){height[i+1]=height[i]+((word>>i)&1U?1:-1);if((word>>i)&1U)stack[top++]=i;else{assert(top);int opening=stack[--top];mate[i]=opening;mate[opening]=i;}}assert(top==0);int maximum=-1,valley=-1;for(int i=0;i+1<2*m;++i)if(((word>>i)&3U)==2U&&height[i]>maximum){maximum=height[i];valley=i;}assert(valley>=0);int L=(valley-mate[valley]-1)/2,Q=(mate[valley+1]-valley-2)/2;int p,q,type;if(L==0&&Q==0){p=valley;q=valley+1;type=0;}else if(L>0&&Q==0){p=valley-1;q=valley+1;type=1;}else if(L==0&&Q>0){p=valley;q=valley+2;type=2;}else{p=valley-1;q=valley+2;type=3;}assert(!((word>>p)&1U)&&((word>>q)&1U));return{word^(U{1}<<p)^(U{1}<<q),type};}

int main(int argc,char**argv){assert(argc==3||argc==4);int m=std::stoi(argv[1]),d=std::stoi(argv[2]),n=2*m+1,s=m+1-d;std::uint64_t root_limit=argc==4?std::stoull(argv[3]):~std::uint64_t{0};assert(n<MAX_N&&n>=13*(d+1));std::vector<U>roots;auto gen=[&](auto&&self,int pos,int up,int down,U x)->void{if(roots.size()>=root_limit)return;if(pos==2*m){roots.push_back(x);return;}if(up<m)self(self,pos+1,up+1,down,x|(U{1}<<pos));if(down<up)self(self,pos+1,up,down+1,x);};gen(gen,0,0,0,0);U mountain=(U{1}<<m)-1;
    std::uint64_t checked=0,failed=0,indexing_failures=0;std::array<std::uint64_t,4>types{};std::array<std::uint64_t,13>chosen{};int maximum_support=0,maximum_bad=0;std::vector<std::string>examples;
    #pragma omp parallel for schedule(dynamic,128) reduction(+:checked,failed,indexing_failures) reduction(max:maximum_support,maximum_bad)
    for(std::int64_t index=0;index<(std::int64_t)roots.size();++index){
        U root=roots[index];if(root==mountain)continue;++checked;
        Choice choice=choose(root,m);auto old_orders=canonical_orders(root,m),next_orders=canonical_orders(choice.parent,m);auto const&old=old_orders.tight;auto const&next=next_orders.tight;
        std::array<int,MAX_N>position{},flip_position{},map{},pi{};for(int i=0;i<n;++i){position[old[i]]=i;flip_position[old_orders.flip[i]]=i;}
        for(int i=0;i<n;++i)pi[i]=flip_position[next_orders.flip[i]];
        std::array<char,MAX_N>bad{};int support=0;
        for(int i=0;i<n;++i){map[i]=position[next[i]];if(map[i]!=i){++support;bad[i]=1;bad[(i-(s-1)+n)%n]=1;}}
        bool indexing_valid=true;int flip_support=0,inv2=m+1;for(int r=0;r<n;++r)flip_support+=pi[r]!=r;for(int j=0;j<n;++j)indexing_valid&=map[j]==(inv2*pi[(2*j)%n])%n;indexing_valid&=flip_support==support;if(!indexing_valid)++indexing_failures;
        int bad_count=std::count(bad.begin(),bad.begin()+n,1);maximum_support=std::max(maximum_support,support);maximum_bad=std::max(maximum_bad,bad_count);
        int selected=-1;for(int t=0;t<13&&selected<0;++t){int a=t*(d+1);bool okay=true;for(int j=0;j<d;++j)okay&=!bad[(a+j)%n];if(okay)selected=t;}
        bool valid=indexing_valid&&selected>=0&&support<=6&&bad_count<=12;
        if(valid){int a=selected*(d+1);for(int j=0;j<d;++j){valid&=old[(a+j)%n]==next[(a+j)%n];valid&=old[(a+s-1+j)%n]==next[(a+s-1+j)%n];}}
        if(!valid){
            ++failed;
            #pragma omp critical
            {if(examples.size()<20){std::string x;for(int i=0;i<2*m;++i)x.push_back((root>>i)&1U?'1':'0');examples.push_back(x);}}
        }else{
            #pragma omp atomic update
            types[choice.type]++;
            #pragma omp atomic update
            chosen[selected]++;
        }
    }
    std::cout<<"SUMMARY m="<<m<<" d="<<d<<" n="<<n<<" roots="<<roots.size()<<" checked_edges="<<checked<<" failures="<<failed<<" iota_indexing_failures="<<indexing_failures<<" maximum_support="<<maximum_support<<" maximum_bad_set="<<maximum_bad<<" packet_hist=";for(int i=0;i<4;++i)std::cout<<i<<':'<<types[i]<<',';std::cout<<" chosen_port_hist=";for(int i=0;i<13;++i)std::cout<<i<<':'<<chosen[i]<<',';std::cout<<'\n';for(auto const&x:examples)std::cout<<"FAIL "<<x<<'\n';
}
