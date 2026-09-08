#include <algorithm>
#include <bit>
#include <cassert>
#include <cstdint>
#include <functional>
#include <iostream>
#include <queue>
#include <set>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

// Enumerate canonical MSW incidence C6 switches on the even 2r-coordinate
// path factor and search the single-hole q2 relay graph.  Heavy runs belong
// on h100 only.

using U = std::uint32_t;

static std::pair<U,int> g(U x,int r){
  std::vector<int> before(2*r); int h=0,d0=0;
  for(int i=0;i<2*r;++i){before[i]=h;if(!((x>>i)&1U)&&h==0)++d0;h+=((x>>i)&1U)?1:-1;}
  int seen=0;
  for(int i=0;i<2*r;++i) if(!((x>>i)&1U)&&(before[i]==0||before[i]==1)&&++seen==d0+1)
    return {x|(U{1}<<i),i};
  assert(false);return {};
}
static std::pair<U,int> hmap(U y,int r){
  std::vector<int> before(2*r); int h=0,u1=0;
  for(int i=0;i<2*r;++i){before[i]=h;if(((y>>i)&1U)&&h==1)++u1;h+=((y>>i)&1U)?1:-1;}
  int seen=0;
  for(int i=0;i<2*r;++i) if(((y>>i)&1U)&&(before[i]==0||before[i]==1)&&++seen==u1)
    return {y&~(U{1}<<i),i};
  assert(false);return {};
}

static std::string word(U x,int n){std::string s;for(int i=0;i<n;++i)s.push_back((x>>i&1U)?'1':'0');return s;}

struct Arc { int from,to; U owner,colour,other; };
struct Hex { U core; int a,b,c; std::vector<std::pair<U,int>> delta; U relay_from=0,relay_to=0; int unique_neg=0; };
struct ExtraTrade { std::vector<U> owners; std::vector<std::pair<U,int>> delta; std::string desc; };

static std::string state_key(const std::vector<U>& h){
  std::string s(reinterpret_cast<const char*>(h.data()),h.size()*sizeof(U));
  return s;
}

int main(int argc,char**argv){
  int r=argc>1?std::stoi(argv[1]):6, n=2*r;
  std::string explicit_target=argc>2?argv[2]:"";
  bool dump_creators=argc>3&&std::string(argv[3])=="--dump-creators";
  assert(n<31);
  std::unordered_map<U,std::vector<U>> owner_cols;
  std::unordered_map<U,std::vector<U>> colour_owners;
  std::unordered_map<U,int> q2load;
  std::vector<U> roots;
  std::function<void(int,int,int,U)> gen=[&](int pos,int up,int down,U x){
    if(pos==n){roots.push_back(x);return;}
    if(up<r)gen(pos+1,up+1,down,x|(U{1}<<pos));
    if(down<up)gen(pos+1,up,down+1,x);
  }; gen(0,0,0,0);
  for(U root:roots){
    U x=root;
    std::vector<U> owners{x},cols;
    for(int j=0;j<r;++j){auto a=g(x,r);cols.push_back(a.first);auto b=hmap(a.first,r);x=b.first;owners.push_back(x);}
    for(int j=0;j<r;++j){owner_cols[owners[j]].push_back(cols[j]);owner_cols[owners[j+1]].push_back(cols[j]);
      colour_owners[cols[j]].push_back(owners[j]);colour_owners[cols[j]].push_back(owners[j+1]);}
    for(int j=1;j<r;++j)++q2load[cols[j-1]|cols[j]];
  }
  std::unordered_map<U,std::vector<Arc>> bycore;
  for(auto &[o,cs]:owner_cols){
    assert(cs.size()==1||cs.size()==2);
    for(int z=0;z<(int)cs.size();++z){U q=cs[z],other=cs.size()==2?cs[1-z]:0;U ins=q&~o;assert(std::popcount(ins)==1);int to=std::countr_zero(ins);
      U bits=o;while(bits){int from=std::countr_zero(bits);bits&=bits-1;U core=o&~(U{1}<<from);bycore[core].push_back({from,to,o,q,other});}}
  }
  std::vector<Hex> hexes;
  for(auto &[core,arcs]:bycore){
    std::unordered_map<int,int> idx;
    for(int i=0;i<(int)arcs.size();++i)idx[(arcs[i].from<<6)|arcs[i].to]=i;
    for(const Arc &ab:arcs)for(const Arc &bc:arcs){
      if(ab.to!=bc.from)continue;int a=ab.from,b=ab.to,c=bc.to;
      if(a>=b||a==c||b==c)continue; // one cyclic representative: a is smallest
      auto it=idx.find((c<<6)|a);if(it==idx.end())continue;const Arc&ca=arcs[it->second];
      // New incidences a->c, b->a, c->b must be unselected.
      if(idx.count((a<<6)|c)||idx.count((b<<6)|a)||idx.count((c<<6)|b))continue;
      std::unordered_map<U,int> dm;
      auto turn=[&](const Arc&old,int predecessor){if(!old.other)return;U nq=core|(U{1}<<old.from)|(U{1}<<predecessor);--dm[old.other|old.colour];++dm[old.other|nq];};
      turn(ab,c);turn(bc,a);turn(ca,b);
      Hex H{core,a,b,c,{}};
      for(auto [t,v]:dm)if(v)H.delta.push_back({t,v});
      std::sort(H.delta.begin(),H.delta.end());
      hexes.push_back(std::move(H));
    }
  }
  std::cerr<<"r="<<r<<" roots="<<roots.size()<<" owners="<<owner_cols.size()<<" cores="<<bycore.size()<<" hexes="<<hexes.size()<<"\n";
  const auto base_load=[&](U t){auto it=q2load.find(t);return it==q2load.end()?0:it->second;};

  // Build simple relay arcs: a hex which creates a canonical hole H and
  // deletes exactly one canonical singleton B gives H -> B; if it deletes
  // no singleton it gives H -> 0 (closed).
  std::unordered_map<U,std::vector<std::pair<U,int>>> relay;
  for(int hi=0;hi<(int)hexes.size();++hi){
    std::vector<U> holes,unique_neg;
    for(auto [t,v]:hexes[hi].delta){int load=q2load.count(t)?q2load[t]:0;
      if(v>0&&load==0)holes.push_back(t);
      if(v<0&&load==1)unique_neg.push_back(t);
    }
    if(unique_neg.size()<=1)for(U h:holes)relay[h].push_back({unique_neg.empty()?0:unique_neg[0],hi});
  }

  std::vector<U> targets;
  // Slice T_(a,b)=(1100)^a 111 (10)^b 1, where r=2a+b+2.
  for(int a=2;a<=r;++a){int b=r-2*a-2;if(b<0)continue;std::string s;
    for(int z=0;z<a;++z)s+="1100";s+="111";for(int z=0;z<b;++z)s+="10";s+="1";
    assert((int)s.size()==n);U t=0;for(int i=0;i<n;++i)if(s[i]=='1')t|=U{1}<<i;
    if(!q2load.count(t))targets.push_back(t);
  }
  // Also the minimal T0 followed by a Dyck suffix is handled elsewhere;
  // include literal T0 when r=6.
  if(r==6){std::string s="110011001111";U t=0;for(int i=0;i<n;++i)if(s[i]=='1')t|=U{1}<<i;targets.push_back(t);}
  if(!explicit_target.empty()){
    assert((int)explicit_target.size()==n);U t=0;for(int i=0;i<n;++i)if(explicit_target[i]=='1')t|=U{1}<<i;
    targets.clear();targets.push_back(t);
  }

  for(U start:targets){
    // Targeted native alternating C8 creators.  A cycle is written
    // O0-Q0-O1-Q1-O2-Q2-O3-Q3-O0 with Oi-Qi new and
    // Qi-O(i+1) selected (indices mod 4).
    long long c8creators=0,c8safe=0;std::vector<std::string> c8examples;std::vector<ExtraTrade> c8trades;
    auto selected=[&](U o,U q){auto it=owner_cols.find(o);return it!=owner_cols.end()&&std::find(it->second.begin(),it->second.end(),q)!=it->second.end();};
    auto other_colour=[&](U o,U removed)->U{auto &cs=owner_cols.at(o);if(cs.size()!=2)return 0;return cs[0]==removed?cs[1]:(cs[1]==removed?cs[0]:0);};
    for(auto &[O0,cs0]:owner_cols)if(cs0.size()==2)for(int keep=0;keep<2;++keep){U E0=cs0[keep],Q3=cs0[1-keep];
      U absent=((U{1}<<n)-1)^O0;while(absent){int z0=std::countr_zero(absent);absent&=absent-1;U Q0=O0|(U{1}<<z0);if(selected(O0,Q0)||((E0|Q0)!=start))continue;
        for(U O1:colour_owners[Q0]){if(O1==O0||owner_cols[O1].size()!=2)continue;U E1=other_colour(O1,Q0);if(!E1)continue;
          U a1=((U{1}<<n)-1)^O1;while(a1){int z1=std::countr_zero(a1);a1&=a1-1;U Q1=O1|(U{1}<<z1);if(selected(O1,Q1)||Q1==Q0||Q1==Q3)continue;
            for(U O2:colour_owners[Q1]){if(O2==O0||O2==O1||owner_cols[O2].size()!=2)continue;U E2=other_colour(O2,Q1);if(!E2)continue;
              U a2=((U{1}<<n)-1)^O2;while(a2){int z2=std::countr_zero(a2);a2&=a2-1;U Q2=O2|(U{1}<<z2);if(selected(O2,Q2)||Q2==Q0||Q2==Q1||Q2==Q3)continue;
                for(U O3:colour_owners[Q2]){if(O3==O0||O3==O1||O3==O2||owner_cols[O3].size()!=2||selected(O3,Q3)||((O3&Q3)!=O3))continue;U E3=other_colour(O3,Q2);if(!E3)continue;
                  std::unordered_map<U,int> dm;auto upd=[&](U E,U oldq,U newq){--dm[E|oldq];++dm[E|newq];};upd(E0,Q3,Q0);upd(E1,Q0,Q1);upd(E2,Q1,Q2);upd(E3,Q2,Q3);
                  if(dm[start]<=0)continue;++c8creators;bool safe=true;std::vector<std::pair<U,int>> dv;for(auto[t,v]:dm)if(v){dv.push_back({t,v});if(base_load(t)+v<=0)safe=false;}std::sort(dv.begin(),dv.end());if(safe)++c8safe;
                  std::string ex="safe="+std::to_string(safe)+" owners="+word(O0,n)+","+word(O1,n)+","+word(O2,n)+","+word(O3,n)+" colours="+word(Q0,n)+","+word(Q1,n)+","+word(Q2,n)+","+word(Q3,n)+" delta=";for(auto[t,v]:dv)ex+=(v>0?"+":"")+std::to_string(v)+":"+word(t,n)+",";
                  c8trades.push_back({{O0,O1,O2,O3},dv,ex});if(c8examples.size()<3)c8examples.push_back(ex);
                }
              }
            }
          }
        }
      }
    }
    std::cout<<"target_c8="<<word(start,n)<<" creators="<<c8creators<<" support_safe="<<c8safe<<"\n";for(auto&s:c8examples)std::cout<<"  c8 "<<s<<"\n";
    if(dump_creators){
      int nc=0;
      for(const Hex&H:hexes){bool creates=false;for(auto[t,v]:H.delta)if(t==start&&v>0)creates=true;if(!creates)continue;
        std::cout<<"creator["<<nc++<<"] core="<<word(H.core,n)<<" active="<<H.a+1<<","<<H.b+1<<","<<H.c+1<<" delta=";
        for(auto[t,v]:H.delta)std::cout<<(v>0?"+":"")<<v<<":"<<word(t,n)<<"(load="<<(q2load.count(t)?q2load[t]:0)<<"),";std::cout<<"\n";
      }

      // Search alternating cycles longer than C6 which create the target.
      // An owner arc O->O' is an unselected incidence OQ followed by a
      // selected incidence QO'.  A directed owner cycle is exactly an
      // alternating incidence cycle.
      auto selected_at=[&](U o,U q){auto it=owner_cols.find(o);if(it==owner_cols.end())return false;
        return std::find(it->second.begin(),it->second.end(),q)!=it->second.end();};
      int found_cycles=0,shortest=0;
      std::vector<U> tbits;for(U z=start;z;z&=z-1)tbits.push_back(U{1}<<std::countr_zero(z));
      for(int maxowners=3;maxowners<=8&&found_cycles==0;++maxowners){
        for(int ii=0;ii<(int)tbits.size()&&found_cycles<12;++ii)for(int jj=ii+1;jj<(int)tbits.size()&&found_cycles<12;++jj){
          U o0=start&~tbits[ii]&~tbits[jj];auto oit=owner_cols.find(o0);if(oit==owner_cols.end()||oit->second.size()!=2)continue;
          for(int ez=0;ez<2&&found_cycles<12;++ez){U mate=oit->second[ez],qminus=oit->second[1-ez];if((mate&start)!=mate)continue;
            U qplus=o0|(start&~mate);if(std::popcount(qplus)!=r+1||selected_at(o0,qplus))continue;
            auto cit=colour_owners.find(qplus);if(cit==colour_owners.end())continue;
            for(U o1:cit->second){if(o1==o0)continue;
              std::vector<U> os{o0,o1},qs{qplus};
              std::function<void()> dfs=[&](){
                U u=os.back();
                for(int x=0;x<n&&found_cycles<12;++x){if((u>>x)&1U)continue;U q=u|(U{1}<<x);if(selected_at(u,q))continue;
                  auto jt=colour_owners.find(q);if(jt==colour_owners.end())continue;
                  for(U v:jt->second){
                    if(v==o0){if(q!=qminus||os.size()!=size_t(maxowners))continue;
                      qs.push_back(q);std::unordered_map<U,int> dm;
                      for(int k=0;k<(int)os.size();++k){U oo=os[k],qin=k?qs[k-1]:qminus,qout=qs[k];auto &cs=owner_cols[oo];
                        if(cs.size()!=2)continue;U other=cs[0]==qin?cs[1]:(cs[1]==qin?cs[0]:0);if(!other){std::cerr<<"bad incoming\n";std::abort();}
                        --dm[other|qin];++dm[other|qout];}
                      bool creates=dm[start]>0,safe=true;for(auto[t,vv]:dm)if((q2load.count(t)?q2load[t]:0)+vv<1)safe=false;
                      if(creates){if(!shortest)shortest=2*maxowners;++found_cycles;
                        std::cout<<"cycle_creator["<<found_cycles-1<<"] C"<<2*maxowners<<" final_safe="<<safe<<" owners=";
                        for(U oo:os)std::cout<<word(oo,n)<<",";std::cout<<" colours=";for(U qq:qs)std::cout<<word(qq,n)<<",";
                        std::cout<<" delta=";std::vector<std::pair<U,int>> dv(dm.begin(),dm.end());std::sort(dv.begin(),dv.end());
                        for(auto[t,vv]:dv)if(vv)std::cout<<(vv>0?"+":"")<<vv<<":"<<word(t,n)<<"(load="<<(q2load.count(t)?q2load[t]:0)<<"),";std::cout<<"\n";}
                      qs.pop_back();continue;}
                    if(os.size()>=size_t(maxowners)||std::find(os.begin(),os.end(),v)!=os.end()||std::find(qs.begin(),qs.end(),q)!=qs.end())continue;
                    os.push_back(v);qs.push_back(q);dfs();qs.pop_back();os.pop_back();
                  }
                }
              };dfs();
            }
          }
        }
      }
      std::cout<<"short_alternating_cycle_creator="<<(found_cycles?std::to_string(shortest):std::string("NONE_THROUGH_C16"))<<" count_printed="<<found_cycles<<"\n";
    }
    std::unordered_map<U,std::pair<U,int>> prev;std::queue<U>qq;prev[start]={start,-1};qq.push(start);U finish=~U{0};
    while(!qq.empty()&&finish==~U{0}){U cur=qq.front();qq.pop();auto it=relay.find(cur);if(it==relay.end())continue;
      for(auto [nx,hi]:it->second){if(nx==0){prev[0]={cur,hi};finish=0;break;}if(!prev.count(nx)){prev[nx]={cur,hi};qq.push(nx);}}
    }
    std::cout<<"target="<<word(start,n)<<" relay_degree="<<relay[start].size();
    if(finish!=0)std::cout<<" status=NO_SIMPLE_RELAY visited="<<prev.size()<<"\n";
    else {
      std::vector<std::pair<U,int>> path;for(U cur=0;cur!=start;){auto [p,h]=prev[cur];path.push_back({cur,h});cur=p;}std::reverse(path.begin(),path.end());
      std::cout<<" status=CLOSED steps="<<path.size()<<"\n";U cur=start;
      for(auto [nx,hi]:path){const Hex&H=hexes[hi];std::cout<<"  "<<word(cur,n)<<" -> "<<(nx?word(nx,n):std::string("CLOSED"))
        <<" core="<<word(H.core,n)<<" active="<<H.a+1<<","<<H.b+1<<","<<H.c+1<<" delta=";
        for(auto[t,v]:H.delta)std::cout<<(v>0?"+":"")<<v<<":"<<word(t,n)<<"(load="<<(q2load.count(t)?q2load[t]:0)<<"),";std::cout<<"\n";cur=nx;}
    }

    // Multi-hole relay BFS (diagnostic): track only deleted canonical
    // singleton targets.  This is a necessary/support model; a returned
    // path is rechecked below for exact loads and owner-disjointness.
    std::unordered_map<U,std::vector<int>> gains;
    for(int hi=0;hi<(int)hexes.size();++hi)for(auto[t,v]:hexes[hi].delta){
      if(v>0)gains[t].push_back(hi);
    }
    for(int ei=0;ei<(int)c8trades.size();++ei)for(auto[t,v]:c8trades[ei].delta)if(v>0)gains[t].push_back((int)hexes.size()+ei);
    const auto& trade_delta=[&](int ti)->const std::vector<std::pair<U,int>>&{return ti<(int)hexes.size()?hexes[ti].delta:c8trades[ti-hexes.size()].delta;};
    const auto trade_owners=[&](int ti){std::vector<U> out;if(ti<(int)hexes.size()){U acts=(U{1}<<hexes[ti].a)|(U{1}<<hexes[ti].b)|(U{1}<<hexes[ti].c);while(acts){int x=std::countr_zero(acts);acts&=acts-1;out.push_back(hexes[ti].core|(U{1}<<x));}}else out=c8trades[ti-hexes.size()].owners;return out;};
    struct Node{std::vector<U> holes;std::vector<std::pair<U,int>> delta;std::vector<U> owners;int parent=-1,hex=-1;};
    std::vector<Node> nodes{{{start},{},{},-1,-1}};std::queue<int>bq;bq.push(0);
    auto node_key=[&](const std::vector<U>& holes,const std::vector<std::pair<U,int>>&delta,const std::vector<U>&owners){
      std::string s=state_key(holes);s.append(reinterpret_cast<const char*>(delta.data()),delta.size()*sizeof(delta[0]));s.append(reinterpret_cast<const char*>(owners.data()),owners.size()*sizeof(U));return s;};
    std::unordered_set<std::string> seen_states{node_key(nodes[0].holes,nodes[0].delta,nodes[0].owners)};int goal=-1,maxdepth=8;
    std::vector<int> depth{0};
    while(!bq.empty()&&goal<0){int ni=bq.front();bq.pop();if(depth[ni]>=maxdepth)continue;
      std::unordered_set<int> cand;for(U h:nodes[ni].holes)for(int hi:gains[h])cand.insert(hi);
      for(int hi:cand){
        std::vector<U> own=nodes[ni].owners;bool collide=false;for(U o:trade_owners(hi)){if(std::find(own.begin(),own.end(),o)!=own.end()){collide=true;break;}own.push_back(o);}if(collide)continue;std::sort(own.begin(),own.end());
        std::unordered_map<U,int> dd;for(auto[t,v]:nodes[ni].delta)dd[t]=v;for(auto[t,v]:trade_delta(hi))dd[t]+=v;
        std::vector<std::pair<U,int>> dv;std::vector<U> hv;
        for(auto[t,v]:dd)if(v){dv.push_back({t,v});if(base_load(t)+v<=0)hv.push_back(t);}
        if(std::find(hv.begin(),hv.end(),start)!=hv.end() && dd[start]<=0){}
        std::sort(dv.begin(),dv.end());std::sort(hv.begin(),hv.end());
        if(hv.size()>8)continue;std::string key=node_key(hv,dv,own);if(!seen_states.insert(key).second)continue;
        int nj=nodes.size();nodes.push_back({hv,dv,own,ni,hi});depth.push_back(depth[ni]+1);
        if(hv.empty()){goal=nj;break;}bq.push(nj);
      }
    }
    std::cout<<"  multihole_bfs="<<(goal>=0?"CLOSED":"OPEN")<<" visited="<<nodes.size();
    if(goal>=0){std::vector<int> hs;for(int z=goal;nodes[z].parent>=0;z=nodes[z].parent)hs.push_back(nodes[z].hex);std::reverse(hs.begin(),hs.end());
      std::unordered_map<U,int> loads=q2load;std::unordered_set<U> usedowners;bool exact=true;
      for(int hi:hs){for(U o:trade_owners(hi))if(!usedowners.insert(o).second)exact=false;
        for(auto[t,v]:trade_delta(hi))loads[t]+=v;
      }
      for(auto[t,v]:loads)if(v<1)exact=false;
      std::cout<<" steps="<<hs.size()<<" exact_owner_disjoint_support="<<exact<<"\n";
      for(int hi:hs){if(hi<(int)hexes.size()){const Hex&H=hexes[hi];std::cout<<"    C6 core="<<word(H.core,n)<<" active="<<H.a+1<<","<<H.b+1<<","<<H.c+1<<" delta=";for(auto[t,v]:H.delta)std::cout<<(v>0?"+":"")<<v<<":"<<word(t,n)<<"(load="<<base_load(t)<<"),";std::cout<<"\n";}else std::cout<<"    C8 "<<c8trades[hi-hexes.size()].desc<<"\n";}
    } else std::cout<<"\n";
  }
}
