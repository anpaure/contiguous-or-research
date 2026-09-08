#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <numeric>
#include <random>
#include <string>
#include <vector>
using namespace std;

static bool universal_skip(const vector<int>& a, int skip=-1){
    vector<uint8_t> seen(2048); array<int,32> p{},c{}; int pn=0;
    for(int pos=0;pos<(int)a.size();++pos){if(pos==skip||a[pos]==0)continue;int cn=0;c[cn++]=a[pos];for(int i=0;i<pn;++i){int v=p[i]|a[pos];if(v!=c[cn-1])c[cn++]=v;}for(int i=0;i<cn;++i)seen[c[i]]=1;p.swap(c);pn=cn;}
    for(int x=1;x<2048;++x)if(!seen[x])return false;return true;
}

static int erase_bit(int x,int bit){return (x&((1<<bit)-1))|((x>>(bit+1))<<bit);}
static int quotient(int x,int erased,int merged){
    // merged<0: map erased coordinate to zero.  Otherwise identify erased
    // with merged, retaining merged's output coordinate.
    if(merged>=0 && (x&(1<<erased))) x|=1<<merged;
    return erase_bit(x,erased);
}

static vector<int> prune(vector<int>a,mt19937_64&rng){
    a.erase(remove(a.begin(),a.end(),0),a.end());
    vector<uint64_t> key(a.size());for(auto&x:key)x=rng();vector<uint8_t>tested(a.size());
    for(;;){int at=-1;for(int i=0;i<(int)a.size();++i)if(!tested[i]&&(at<0||key[i]<key[at]))at=i;if(at<0)break;
        if(universal_skip(a,at)){a.erase(a.begin()+at);key.erase(key.begin()+at);tested.erase(tested.begin()+at);}else tested[at]=1;
    }return a;
}

int main(int argc,char**argv){
    if(argc<2)return 2;ifstream in(argv[1]);vector<int>base;for(int x;in>>x;)base.push_back(x);if(base.size()!=926)return 2;
    int rounds=argc>2?stoi(argv[2]):10;uint64_t seed=argc>3?stoull(argv[3]):121178;string prefix=argc>4?argv[4]:"k11_quotient";mt19937_64 rng(seed);
    vector<int>best;string desc;
    auto run=[&](int erased,int merged){vector<int>q;q.reserve(base.size());for(int x:base)q.push_back(quotient(x,erased,merged));if(!universal_skip(q)){cerr<<"invalid quotient\n";exit(3);}for(int z=0;z<rounds;++z){vector<int>p=prune(q,rng);if(best.empty()||p.size()<best.size()){best=move(p);desc="erase="+to_string(erased)+" merge="+to_string(merged)+" round="+to_string(z);ofstream out(prefix+"_best.txt");for(int x:best)out<<x<<' ';out<<'\n';cerr<<"BEST "<<desc<<" length="<<best.size()<<'\n';}}};
    for(int erased=0;erased<12;++erased)run(erased,-1);
    for(int a=0;a<12;++a)for(int b=a+1;b<12;++b)run(b,a);
    cout<<desc<<" length="<<best.size()<<" universal="<<universal_skip(best)<<'\n';
}
