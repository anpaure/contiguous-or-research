// Enumerate every unordered full 5+5 prefix row modulo the half-swap involution.
#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <string>
using namespace std;
int involution(int mask){return ((mask&31)<<5)|(mask>>5);}
int main(int argc,char**argv){
    ios::sync_with_stdio(false);cin.tie(nullptr);
    bool all=argc>1&&string(argv[1])=="--all";
    int count;if(!(cin>>count))return 2;array<bool,1024> core{};
    for(int i=0;i<count;++i){int mask;cin>>mask;core[mask]=true;}
    array<int,10> p{0,1,2,3,4,5,6,7,8,9};array<int,1024> seen{};int stamp=0;
    long long canonical=0,fixed_count=0,valid_fixed=0,valid_pairs=0,emitted=0;
    do{
        if(p[0]>p[5])continue;
        array<int,10> q;for(int i=0;i<10;++i)q[i]=(p[i]+5)%10;
        if(q[0]>q[5])for(int i=0;i<5;++i)swap(q[i],q[i+5]);
        if(q<p)continue;++canonical;bool fixed=q==p;if(fixed)++fixed_count;
        array<int,6> a{},b{};for(int i=0;i<5;++i){a[i+1]=a[i]|1<<p[i];b[i+1]=b[i]|1<<p[5+i];}
        bool valid=true,compatible=true;++stamp;
        for(int i=0;i<=5&&valid;++i)for(int j=0;j<=5;++j){
            int rank=i+j;if(rank<4||rank>6)continue;
            int mask=a[i]|b[j],partner=involution(mask),key=min(mask,partner);
            if(!fixed&&(mask==partner||seen[key]==stamp)){valid=false;break;}
            seen[key]=stamp;if(core[mask]||core[partner])compatible=false;
        }
        if(!valid)continue;if(fixed)++valid_fixed;else ++valid_pairs;
        if(!all&&(fixed||!compatible))continue;
        uint64_t packed=0;for(int i=0;i<10;++i)packed|=uint64_t(p[i])<<(4*i);
        cout<<(fixed?1:2)<<' '<<packed<<'\n';++emitted;
    }while(next_permutation(p.begin(),p.end()));
    cerr<<"CATALOGUE canonical="<<canonical<<" fixed="<<fixed_count
        <<" valid_fixed="<<valid_fixed<<" valid_pairs="<<valid_pairs<<" emitted="<<emitted<<'\n';
    if(canonical!=908160||fixed_count!=1920||valid_fixed!=1920)return 3;
}
