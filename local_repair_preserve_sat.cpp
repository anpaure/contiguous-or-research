#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif
#include <cadical.hpp>
#include <algorithm>
#include <bit>
#include <cstdint>
#include <iostream>
#include <random>
#include <vector>
using namespace std;
struct Interval{int fixed_or=0,original_or=0;vector<int>vars;};
int main(int argc,char**argv){if(argc<5)return 2;int k=stoi(argv[1]),limit=1<<k,choice=stoi(argv[2]),top=stoi(argv[3]);vector<int>positions;for(int i=4;i<argc;++i)positions.push_back(stoi(argv[i]));sort(positions.begin(),positions.end());vector<int>a;for(int x;cin>>x;)a.push_back(x);vector<int>vi(a.size(),-1);for(int i=0;i<(int)positions.size();++i)vi[positions[i]]=i;
 vector<Interval>ints;ints.reserve((long long)a.size()*(a.size()+1)/2);vector<uint8_t>fixed(limit),all(limit);for(int l=0;l<(int)a.size();++l){int fo=0,oo=0;vector<int>vs;for(int r=l;r<(int)a.size();++r){oo|=a[r];if(vi[r]<0)fo|=a[r];else vs.push_back(vi[r]);ints.push_back({fo,oo,vs});all[oo]=1;if(vs.empty())fixed[fo]=1;}}
 CaDiCaL::Solver s;s.set("quiet",1);s.declare_more_variables((int)positions.size()*k+limit*top);int vc=0;auto var=[&](){return++vc;};auto clause=[&](const vector<int>&c){for(int x:c)s.add(x);s.add(0);};vector<vector<int>>x(positions.size(),vector<int>(k));for(int i=0;i<(int)positions.size();++i){for(int b=0;b<k;++b){x[i][b]=var();s.phase(a[positions[i]]&(1<<b)?x[i][b]:-x[i][b]);}clause(x[i]);}
 auto enforce=[&](const Interval&I,int target,int select){for(int b=0;b<k;++b){if(!(target&(1<<b))){for(int j:I.vars)clause(select?vector<int>{-select,-x[j][b]}:vector<int>{-x[j][b]});}else if(!(I.fixed_or&(1<<b))){vector<int>c;if(select)c.push_back(-select);for(int j:I.vars)c.push_back(x[j][b]);clause(c);}}};
 int preserved=0,missing=0;long long selectors=0;mt19937_64 rng(choice);for(int target=1;target<limit;++target){if(fixed[target])continue;if(all[target]){vector<const Interval*>cand;for(const auto&I:ints)if(I.original_or==target&&!I.vars.empty())cand.push_back(&I);if(cand.empty())return 3;sort(cand.begin(),cand.end(),[](auto*A,auto*B){return A->vars.size()<B->vars.size();});int pool=min<int>(max(1,top),cand.size()),want=min(4,pool);vector<int>chosen;while((int)chosen.size()<want){int index=(choice+target+rng())%pool;if(find(chosen.begin(),chosen.end(),index)==chosen.end())chosen.push_back(index);}if(chosen.size()==1){enforce(*cand[chosen[0]],target,0);}else{vector<int>w;for(int index:chosen){int sel=var();w.push_back(sel);enforce(*cand[index],target,sel);++selectors;}clause(w);}++preserved;}else{++missing;vector<pair<int,const Interval*>>cand;for(const auto&I:ints){if(I.fixed_or&~target)continue;int need=target&~I.fixed_or;if(need&&I.vars.empty())continue;int original=I.original_or,cost=32*popcount((unsigned)(original^target))+I.vars.size();cand.push_back({cost,&I});}sort(cand.begin(),cand.end(),[](auto&a,auto&b){return a.first<b.first;});vector<int>w;for(int z=0;z<min<int>(top,cand.size());++z){int sel=var();w.push_back(sel);enforce(*cand[z].second,target,sel);++selectors;}if(w.empty())return 4;clause(w);}}
 cerr<<"positions="<<positions.size()<<" preserved="<<preserved<<" missing="<<missing<<" selectors="<<selectors<<" variables="<<vc<<'\n';int result=s.solve();if(result!=10){cerr<<"UNSAT\n";return 1;}for(int i=0;i<(int)positions.size();++i){int v=0;for(int b=0;b<k;++b)if(s.val(x[i][b])>0)v|=1<<b;a[positions[i]]=v;}cerr<<"SAT\n";for(int v:a)cout<<v<<' ';cout<<'\n';}
