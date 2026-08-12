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
#include <vector>
using namespace std;
struct Eval{vector<uint32_t>s=vector<uint32_t>(8192);uint32_t g=0;int operator()(const vector<int>&a,int pos,int value,vector<int>*missing=nullptr){if(++g==0)fill(s.begin(),s.end(),0),++g;array<int,24>p{},q{};int pn=0;for(int j=0;j<(int)a.size();++j){int x=j==pos?value:a[j],qn=0;q[qn++]=x;for(int i=0;i<pn;++i){int v=p[i]|x;if(v!=q[qn-1])q[qn++]=v;}for(int i=0;i<qn;++i)s[q[i]]=g;p.swap(q);pn=qn;}int c=0;for(int x=1;x<8192;++x)if(s[x]==g)++c;else if(missing)missing->push_back(x);return c;}};
int main(int argc,char**argv){if(argc<3)return 2;ifstream in(argv[1]);vector<int>a;for(int x;in>>x;)a.push_back(x);if(a.size()!=1851)return 2;string outpath=argv[2];Eval ev;int best=0,bp=-1,bv=-1;const int oldtarget=1876;for(int z=0;z<4096;++z){if((z|oldtarget)!=oldtarget)continue;for(int p=927;p<(int)a.size();++p){int value=(1<<12)|z,score=ev(a,p,value);if(score>best){best=score;bp=p;bv=value;vector<int>miss;ev(a,p,value,&miss);cerr<<"BEST score="<<score<<"/8191 pos="<<p<<" old="<<a[p]<<" new="<<value<<" missing";for(int x:miss)cerr<<' '<<x;cerr<<'\n';}if(score==8191){ofstream out(outpath);for(int j=0;j<(int)a.size();++j)out<<(j==p?value:a[j])<<' ';out<<'\n';cout<<"FOUND pos="<<p<<" value="<<value<<'\n';return 0;}}}cout<<"NONE best="<<best<<" pos="<<bp<<" value="<<bv<<'\n';return 1;}
