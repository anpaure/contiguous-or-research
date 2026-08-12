#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <algorithm>
#include <bit>
#include <climits>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <limits>
#include <string>
#include <tuple>
#include <vector>

using namespace std;

static vector<int> gray(int n, int choose) {
    if (!choose) return {0};
    if (choose == n) return {(1 << n) - 1};
    vector<int> a = gray(n - 1, choose), b = gray(n - 1, choose - 1);
    reverse(b.begin(), b.end());
    for (int& x : b) x |= 1 << (n - 1);
    a.insert(a.end(), b.begin(), b.end());
    return a;
}
static bool adjacent(int x, int y) { return popcount(static_cast<unsigned>(x ^ y)) == 2; }
static vector<int> end_at(vector<int> cycle, int target) {
    if (!adjacent(cycle.front(), cycle.back())) exit(3);
    auto it = find(cycle.begin(), cycle.end(), target);
    rotate(cycle.begin(), it, cycle.end());
    reverse(cycle.begin(), cycle.end());
    return cycle;
}

struct Eval { int deficit = 0, missing = 0; vector<int> by_rank; };
static Eval evaluate(const vector<int>& p) {
    constexpr int k=13, r=7, d=3, limit=1<<k;
    Eval e; e.by_rank.assign(k+1,0);
    for(int bit=0;bit<k;++bit){
        int i=0;
        while(i<(int)p.size()){
            if(!(p[i]&(1<<bit))){++i;continue;}
            int l=i; while(i<(int)p.size()&&(p[i]&(1<<bit)))++i;
            if(l&&i<(int)p.size()) e.deficit+=max(0,d+1-(i-l));
        }
    }
    vector<vector<uint8_t>> seen(k+1,vector<uint8_t>(limit));
    for(int x:p)seen[r][x]=1;
    for(int len=2;len<=d+1;++len){int want=r-len+1;for(int l=0;l+len<=(int)p.size();++l){int x=limit-1;for(int j=l;j<l+len;++j)x&=p[j];if(popcount((unsigned)x)==want)seen[want][x]=1;}}
    for(int len=2;r+len-1<=k;++len){int want=r+len-1;for(int l=0;l+len<=(int)p.size();++l){int x=0;for(int j=l;j<l+len;++j)x|=p[j];if(popcount((unsigned)x)==want)seen[want][x]=1;}}
    for(int rank=r-d;rank<=k;++rank){for(int x=1;x<limit;++x)if(popcount((unsigned)x)==rank&&!seen[rank][x])++e.by_rank[rank],++e.missing;}
    return e;
}

int main(int argc,char**argv){
    if(argc<2)return 2; ifstream in(argv[1]); vector<int> t; for(int x;in>>x;)t.push_back(x); if(t.size()!=924)return 2;
    vector<int> g=gray(12,7),best; Eval be; tuple<int,int> bk{INT_MAX,INT_MAX}; string bd;
    for(int rt=0;rt<2;++rt){vector<int> q=t;if(rt)reverse(q.begin(),q.end());int endpoint=q.front();
        for(int add=0;add<12;++add)if(!(endpoint&(1<<add))){int s=endpoint|(1<<add);for(int rg=0;rg<2;++rg){vector<int> cyc=g;if(rg)reverse(cyc.begin(),cyc.end());vector<int> low=end_at(cyc,s),p=low;for(int x:q)p.push_back((1<<12)|x);for(int i=0;i+1<(int)p.size();++i)if(!adjacent(p[i],p[i+1]))return 4;Eval e=evaluate(p);auto key=tuple{e.deficit,e.missing};if(key<bk){bk=key;best=move(p);be=e;bd="rt="+to_string(rt)+" add="+to_string(add)+" rg="+to_string(rg);cerr<<"BEST "<<bd<<" deficit="<<e.deficit<<" missing="<<e.missing<<" by_rank";for(int r=4;r<=13;++r)cerr<<' '<<r<<':'<<e.by_rank[r];cerr<<'\n';}}}}
    ofstream out(argc>2?argv[2]:"k13_lift_seed.txt");for(int x:best)out<<x<<' ';out<<'\n';cout<<bd<<" deficit="<<be.deficit<<" missing="<<be.missing<<'\n';
}
