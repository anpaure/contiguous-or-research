#define main msw_factor_fibre_bfs_main
#include "msw_factor_fibre_bfs.cpp"
#undef main
#include <iostream>
int main(int argc,char**argv){int m=argc>1?std::stoi(argv[1]):2,n=2*m+1;std::vector<U64>f;
 std::function<void(int,int,int,U32)>gen=[&](int p,int u,int d,U32 mask){if(p==2*m){U32 x=mask;std::vector<int>q;for(int e=0;e<m;++e){auto a=g(x,m);auto b=hfun(a.first,m);q.push_back(a.second);q.push_back(b.second);x=b.first;}q.push_back(2*m);f.push_back(canon(q));return;}if(u<m)gen(p+1,u+1,d,mask|(U32{1}<<p));if(d<u)gen(p+1,u,d+1,mask);};gen(0,0,0,0);for(auto q:f){for(int x:unpack(q,n))std::cout<<x+1<<' ';std::cout<<'\n';}}
