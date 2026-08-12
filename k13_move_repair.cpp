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
struct Eval{vector<uint32_t>s=vector<uint32_t>(8192);uint32_t g=0;int operator()(const vector<int>&a){if(++g==0)fill(s.begin(),s.end(),0),++g;array<int,24>p{},q{};int pn=0;for(int x:a){int qn=0;q[qn++]=x;for(int i=0;i<pn;++i){int v=p[i]|x;if(v!=q[qn-1])q[qn++]=v;}for(int i=0;i<qn;++i)s[q[i]]=g;p.swap(q);pn=qn;}int c=0;for(int x=1;x<8192;++x)c+=s[x]==g;return c;}};
int main(int argc,char**argv){if(argc<3)return 2;ifstream in(argv[1]);vector<int>a;for(int x;in>>x;)a.push_back(x);if(a.size()!=1851)return 2;Eval e;int best=e(a);cerr<<"initial="<<best<<"/8191\n";const int first=927,n=a.size();for(int from=first;from<n;++from){for(int to=first;to<n;++to){if(from==to)continue;vector<int>b=a;int x=b[from];b.erase(b.begin()+from);int gap=to;if(to>from)--gap;b.insert(b.begin()+gap,x);int score=e(b);if(score>best){best=score;cerr<<"BEST move="<<from<<"->"<<to<<" score="<<score<<"/8191\n";}if(score==8191){ofstream out(argv[2]);for(int x:b)out<<x<<' ';out<<'\n';cout<<"FOUND move="<<from<<"->"<<to<<'\n';return 0;}}}cerr<<"moves_done best="<<best<<'\n';for(int l=first;l<n;++l){for(int r=l+1;r<n;++r){vector<int>b=a;reverse(b.begin()+l,b.begin()+r+1);int score=e(b);if(score>best){best=score;cerr<<"BEST reverse="<<l<<','<<r<<" score="<<score<<"/8191\n";}if(score==8191){ofstream out(argv[2]);for(int x:b)out<<x<<' ';out<<'\n';cout<<"FOUND reverse="<<l<<','<<r<<'\n';return 0;}}}cerr<<"reversals_done best="<<best<<'\n';for(int i=first;i<n;++i){for(int j=i+1;j<n;++j){vector<int>b=a;swap(b[i],b[j]);int score=e(b);if(score>best){best=score;cerr<<"BEST swap="<<i<<','<<j<<" score="<<score<<"/8191\n";}if(score==8191){ofstream out(argv[2]);for(int x:b)out<<x<<' ';out<<'\n';cout<<"FOUND swap="<<i<<','<<j<<'\n';return 0;}}}cout<<"NONE best="<<best<<"/8191\n";return 1;}
