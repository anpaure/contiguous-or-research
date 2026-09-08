#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif
#include <algorithm>
#include <array>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <random>
#include <string>
#include <vector>
using namespace std;
struct Eval{vector<uint32_t>s=vector<uint32_t>(8192);uint32_t g=0;int operator()(const vector<int>&a){if(++g==0)fill(s.begin(),s.end(),0),++g;array<int,24>p{},q{};int pn=0;for(int x:a){int qn=0;q[qn++]=x;for(int i=0;i<pn;++i){int v=p[i]|x;if(v!=q[qn-1])q[qn++]=v;}for(int i=0;i<qn;++i)s[q[i]]=g;p.swap(q);pn=qn;}int c=0;for(int x=1;x<8192;++x)c+=s[x]==g;return c;}};
static void save(const string&path,const vector<int>&a){ofstream o(path);for(int x:a)o<<x<<' ';o<<'\n';}
int main(int argc,char**argv){if(argc<5)return 2;ifstream in(argv[1]);vector<int>seed;for(int x;in>>x;)seed.push_back(x);if(seed.size()!=1851)return 2;string out=argv[2];double seconds=stod(argv[3]);uint64_t rs=stoull(argv[4]);mt19937_64 rng(rs);uniform_real_distribution<double>u(0,1);Eval eval;int global=eval(seed);vector<int>best=seed;cerr<<"initial="<<global<<"/8191\n";auto deadline=chrono::steady_clock::now()+chrono::milliseconds((long long)(1000*seconds));long long iterations=0;const int first=927,n=seed.size();while(chrono::steady_clock::now()<deadline){vector<int>a=best;int cur=global;for(int step=0;step<20000&&chrono::steady_clock::now()<deadline;++step,++iterations){vector<int>b=a;int type=rng()%3;if(type==0){int i=first+rng()%(n-first),j=first+rng()%(n-first);swap(b[i],b[j]);}else if(type==1){int l=first+rng()%(n-first),r=first+rng()%(n-first);if(l>r)swap(l,r);reverse(b.begin()+l,b.begin()+r+1);}else{int from=first+rng()%(n-first),to=first+rng()%(n-first);int x=b[from];b.erase(b.begin()+from);if(to>from)--to;b.insert(b.begin()+to,x);}int sc=eval(b);double phase=(step%2000)/2000.0,temp=4.0*pow(1e-3,phase)+0.02;if(sc>=cur||u(rng)<exp((sc-cur)/temp)){a.swap(b);cur=sc;}if(cur>global){global=cur;best=a;save(out,best);cerr<<"BEST iteration="<<iterations<<" score="<<global<<"/8191\n";if(global==8191){cout<<"FOUND iterations="<<iterations<<'\n';return 0;}}}}cout<<"NONE iterations="<<iterations<<" best="<<global<<"/8191\n";return 1;}
