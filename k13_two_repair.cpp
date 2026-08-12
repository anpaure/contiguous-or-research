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
#include <tuple>
#include <vector>
using namespace std;
struct Result{int score;bool has_a,has_b;};
struct Eval{vector<uint32_t>s=vector<uint32_t>(8192);uint32_t g=0;Result run(const vector<int>&a,int p1,int v1,int p2=-1,int v2=0){if(++g==0)fill(s.begin(),s.end(),0),++g;array<int,24>p{},q{};int pn=0;for(int j=0;j<(int)a.size();++j){int x=j==p1?v1:(j==p2?v2:a[j]),qn=0;q[qn++]=x;for(int i=0;i<pn;++i){int v=p[i]|x;if(v!=q[qn-1])q[qn++]=v;}for(int i=0;i<qn;++i)s[q[i]]=g;p.swap(q);pn=qn;}int c=0;for(int x=1;x<8192;++x)c+=s[x]==g;return{c,s[5712]==g,s[5972]==g};}};
int main(int argc,char**argv){if(argc<3)return 2;ifstream in(argv[1]);vector<int>a;for(int x;in>>x;)a.push_back(x);if(a.size()!=1851)return 2;vector<pair<int,int>>firsts;Eval e;for(int z=0;z<4096;++z){if((z|1876)!=1876)continue;int v=4096|z;for(int p=927;p<(int)a.size();++p){Result r=e.run(a,p,v);if(r.score==8190&&r.has_a&&!r.has_b)firsts.push_back({p,v});}}cerr<<"first_states="<<firsts.size()<<'\n';long long tested=0;for(auto [p1,v1]:firsts){for(int z=0;z<4096;++z){if((z|1876)!=1876)continue;int v2=4096|z;for(int p2=927;p2<(int)a.size();++p2){if(p2==p1)continue;++tested;Result r=e.run(a,p1,v1,p2,v2);if(r.score==8191){ofstream out(argv[2]);for(int j=0;j<(int)a.size();++j)out<<(j==p1?v1:(j==p2?v2:a[j]))<<' ';out<<'\n';cout<<"FOUND p1="<<p1<<" v1="<<v1<<" p2="<<p2<<" v2="<<v2<<" tested="<<tested<<'\n';return 0;}}}cerr<<"done_first p="<<p1<<" v="<<v1<<" tested="<<tested<<'\n';}cout<<"NONE states="<<firsts.size()<<" tested="<<tested<<'\n';return 1;}
