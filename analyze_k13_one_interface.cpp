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
int main(int argc,char**argv){if(argc<5)return 2;ifstream in(argv[1]);vector<int>b;for(int x;in>>x;)b.push_back(x);if(stoi(argv[2]))reverse(b.begin(),b.end());int a=stoi(argv[3]),c=stoi(argv[4]);vector<int>residue=b;if(argc>7)residue[stoi(argv[6])]=stoi(argv[7]);vector<int>full=b;full.push_back(1<<12);for(int i=0;i<(int)residue.size();++i)if(i!=a&&i!=c)full.push_back((1<<12)|residue[i]);vector<uint8_t>seen(8192);array<int,20>p{},q{};int pn=0;for(int x:full){int qn=0;q[qn++]=x;for(int i=0;i<pn;++i){int v=p[i]|x;if(v!=q[qn-1])q[qn++]=v;}for(int i=0;i<qn;++i)seen[q[i]]=1;p.swap(q);pn=qn;}cout<<"length="<<full.size()<<" missing";for(int x=1;x<8192;++x)if(!seen[x])cout<<' '<<x;cout<<'\n';if(argc>5){ofstream out(argv[5]);for(int x:full)out<<x<<' ';out<<'\n';}}
