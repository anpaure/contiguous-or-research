#include <algorithm>
#include <array>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
using P=std::array<int,3>;using L=std::pair<int,int>;
static L base(P p,int m){int i=std::min(p[1],m-p[0]),t=p[0]+p[1]-i,j=std::min(t,m-p[2]);return{i,j};}
static std::map<L,std::vector<P>> part(int m,std::array<int,3> perm,bool comp){std::map<L,std::vector<P>>f;for(int x=0;x<=m;x++)for(int y=0;y<=m;y++)for(int z=0;z<=m;z++){P p{x,y,z},q;for(int a=0;a<3;a++)q[a]=p[perm[a]];if(comp)for(int&a:q)a=m-a;f[base(q,m)].push_back(p);}return f;}
int main(){std::vector<std::array<int,3>>ps;std::array<int,3>p{0,1,2};do{ps.push_back(p);}while(std::next_permutation(p.begin(),p.end()));for(int m=2;m<=12;m++){std::cout<<"m="<<m<<"\n";for(int a=0;a<12;a++)for(int b=a+1;b<12;b++){auto A=part(m,ps[a%6],a>=6),B=part(m,ps[b%6],b>=6);int mx=0,dbl=0,extra=0;for(auto&[x,u]:A)for(auto&[y,v]:B){int z=0;std::set<P>s(u.begin(),u.end());for(P w:v)z+=s.count(w);mx=std::max(mx,z);if(z>=2)dbl++;extra+=std::max(0,z-1);}if(mx<=2&&extra<=m+2)std::cout<<a<<","<<b<<" mx="<<mx<<" dbl="<<dbl<<" extra="<<extra<<"\n";}break;}}
