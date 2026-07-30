#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <numeric>
#include <set>
#include <stdexcept>
#include <string>
#include <vector>

using std::array;
using std::pair;
using std::string;
using std::vector;

namespace {
constexpr int K = 16;
constexpr int R = 8;
constexpr int W = 12870;
constexpr int H = 3;
constexpr int L = W + H;
constexpr uint16_t FULL = 0xffffu;
constexpr uint16_t PIN = 0x8000u;
constexpr int PIN_POSITION = 6389;
constexpr array<int,H> X = {12870,12871,12872};
constexpr array<int,H> Y = {0,1,6388};
constexpr const char* EXPECTED_SHA =
  "c7beccc38489ad0ce4f203fa11e348a9fb04a18418cdc8ac9dce038ddde06906";

struct Cell { int start, length; bool omitted; };
struct Edge { uint16_t target; int cell; int var; };

int pc(uint16_t x) { return std::popcount(x); }
bool in3(const array<int,H>& a,int p){return std::find(a.begin(),a.end(),p)!=a.end();}

vector<uint16_t> load(const string& path){
  std::ifstream in(path); vector<uint16_t> out; unsigned value;
  while(in>>value)out.push_back(static_cast<uint16_t>(value));
  if(static_cast<int>(out.size())!=W)throw std::runtime_error("bad target length");
  if(std::set<uint16_t>(out.begin(),out.end()).size()!=W)
    throw std::runtime_error("targets are not distinct");
  for(auto x:out)if(pc(x)!=R)throw std::runtime_error("non-middle target");
  return out;
}

long long amo_clauses(size_t n){return n<2?0:(n==2?2:3LL*n-4);}

struct Writer {
  std::ofstream out;
  long long clauses=0;
  vector<char> buffer;
  explicit Writer(const string& path):out(path),buffer(1<<20){
    out.rdbuf()->pubsetbuf(buffer.data(),buffer.size());
    if(!out)throw std::runtime_error("cannot open CNF");
  }
  void lit(int x){out<<x<<' ';}
  void end(){out<<"0\n";++clauses;}
};

void emit_amo(Writer& w,const vector<int>& xs,int aux0){
  const int n=static_cast<int>(xs.size());
  if(n<2)return;
  // Sinz sequential at-most-one; auxiliary s_i has id aux0+i, i=0..n-2.
  w.lit(-xs[0]);w.lit(aux0);w.end();
  for(int i=1;i<n-1;++i){
    int prev=aux0+i-1,cur=aux0+i;
    w.lit(-xs[i]);w.lit(cur);w.end();
    w.lit(-prev);w.lit(cur);w.end();
    w.lit(-xs[i]);w.lit(-prev);w.end();
  }
  w.lit(-xs[n-1]);w.lit(-(aux0+n-2));w.end();
}

} // namespace

int main(int argc,char**argv){
  if(argc!=3){std::cerr<<"usage: build TARGET.word OUTPUT_PREFIX\n";return 2;}
  const string target_path=argv[1],prefix=argv[2];
  auto targets=load(target_path);

  vector<int> starts,deadlines;
  for(int p=0;p<L;++p){if(!in3(X,p))starts.push_back(p);if(!in3(Y,p))deadlines.push_back(p);}
  if(starts.size()!=W||deadlines.size()!=W)throw std::runtime_error("bad schedule");
  vector<int> depths(W);
  long long area=0;
  for(int i=0;i<W;++i){depths[i]=deadlines[i]-starts[i];if(depths[i]<0||depths[i]>H)throw std::runtime_error("bad depth");area+=depths[i];}
  if(area!=32224)throw std::runtime_error("unexpected area");

  vector<uint16_t> envelope(L,FULL);
  for(int i=0;i<W;++i)for(int p=starts[i];p<=deadlines[i];++p)envelope[p]&=targets[i];
  for(auto x:envelope)if(!x)throw std::runtime_error("zero maximal envelope");
  envelope[PIN_POSITION]=PIN;
  for(int i=0;i<W;++i){uint16_t x=0;for(int p=starts[i];p<=deadlines[i];++p)x|=envelope[p];if(x!=targets[i])throw std::runtime_error("middle replay failed");}

  // Verify the carrier has every middle/upper interval union.
  vector<unsigned char> seen(1<<K,0); vector<uint16_t> ending;
  for(uint16_t x:targets){
    vector<uint16_t> next={x};
    for(uint16_t old:ending){uint16_t value=old|x;if(std::find(next.begin(),next.end(),value)==next.end())next.push_back(value);}
    ending.swap(next);for(uint16_t value:ending)seen[value]=1;
  }
  for(int mask=1;mask<(1<<K);++mask)if(pc(static_cast<uint16_t>(mask))>=R&&!seen[mask])
    throw std::runtime_error("carrier upper replay incomplete");

  vector<Cell> cells; vector<array<int,H+1>> lookup(L);
  for(auto& row:lookup)row.fill(-1);
  for(int i=0;i<W;++i)for(int len=1;len<=depths[i];++len){
    int s=starts[i]; if(lookup[s][len]>=0)throw std::runtime_error("duplicate cell");
    lookup[s][len]=cells.size();cells.push_back({s,len,false});
  }
  for(int s:X)for(int len=1;len<=std::min(H,L-s);++len){
    if(lookup[s][len]>=0)throw std::runtime_error("duplicate omitted cell");
    lookup[s][len]=cells.size();cells.push_back({s,len,true});
  }
  if(cells.size()!=32230)throw std::runtime_error("unexpected physical cell count");
  const int reserved=lookup[PIN_POSITION][1];
  if(reserved<0)throw std::runtime_error("singleton cell absent");

  vector<uint16_t> mandatory(cells.size(),0),allowed(cells.size(),0);
  for(int i=0;i<W;++i){
    for(int bit=0;bit<K;++bit)if(targets[i]&(1u<<bit)){
      int lo=L,hi=-1;
      for(int p=starts[i];p<=deadlines[i];++p)if(envelope[p]&(1u<<bit)){lo=std::min(lo,p);hi=std::max(hi,p);}
      if(hi<0)throw std::runtime_error("lost middle bit");
      for(int len=1;len<=H;++len)for(int s=std::max(0,hi-len+1);s<=lo;++s){
        if(s>=L)continue;int cell=lookup[s][len];if(cell>=0)mandatory[cell]|=(1u<<bit);
      }
    }
  }
  for(size_t c=0;c<cells.size();++c){for(int p=cells[c].start;p<cells[c].start+cells[c].length;++p)allowed[c]|=envelope[p];}

  vector<Edge> edges;
  vector<vector<int>> by_target(1<<K),by_cell(cells.size());
  for(int c=0;c<static_cast<int>(cells.size());++c){
    if(c==reserved)continue;
    uint16_t s=allowed[c];
    while(s){
      if(s!=PIN&&pc(s)<R&&!(mandatory[c]&~s)){
        bool meets=true;for(int p=cells[c].start;p<cells[c].start+cells[c].length;++p)if(!(envelope[p]&s)){meets=false;break;}
        if(meets){int var=edges.size()+1;edges.push_back({s,c,var});by_target[s].push_back(var);by_cell[c].push_back(var);}
      }
      s=(s-1)&allowed[c];
    }
  }
  // The full pinned Hall graph has 347,734 incidences.  This direct model
  // removes the reserved singleton cell and the already-fixed 0x8000 target,
  // leaving the independently audited residual graph of 347,677 incidences.
  if(edges.size()!=347677)throw std::runtime_error("residual incidence count does not match audited graph");
  int lower_count=0;
  for(int s=1;s<(1<<K);++s)if(pc(static_cast<uint16_t>(s))<R&&s!=PIN){
    ++lower_count;if(by_target[s].empty())throw std::runtime_error("zero lower degree");
  }
  if(lower_count!=26331)throw std::runtime_error("bad remaining lower count");

  int next_var=edges.size()+1;
  vector<array<int,K>> avar(L);for(auto&r:avar)r.fill(0);
  vector<pair<int,int>> avec;
  for(int p=0;p<L;++p)for(int bit=0;bit<K;++bit)if(envelope[p]&(1u<<bit)){
    avar[p][bit]=next_var++;avec.push_back({p,bit});
  }
  vector<vector<int>> blockers(avec.size());
  const int a0=edges.size()+1;
  for(const auto&e:edges){const auto&c=cells[e.cell];for(int p=c.start;p<c.start+c.length;++p){
    uint16_t blocked=envelope[p]&~e.target;for(int bit=0;bit<K;++bit)if(blocked&(1u<<bit))blockers[avar[p][bit]-a0].push_back(e.var);
  }}

  vector<int> target_aux(1<<K,-1),cell_aux(cells.size(),-1);
  for(int s=1;s<(1<<K);++s)if(pc(static_cast<uint16_t>(s))<R&&s!=PIN&&by_target[s].size()>=2){target_aux[s]=next_var;next_var+=by_target[s].size()-1;}
  for(size_t c=0;c<cells.size();++c)if(by_cell[c].size()>=2){cell_aux[c]=next_var;next_var+=by_cell[c].size()-1;}
  const int variables=next_var-1;

  long long expected=0;
  for(int s=1;s<(1<<K);++s)if(pc(static_cast<uint16_t>(s))<R&&s!=PIN){expected+=1+amo_clauses(by_target[s].size());}
  for(const auto&g:by_cell)expected+=amo_clauses(g.size());
  for(const auto&b:blockers)expected+=b.size()+1;
  expected+=L;
  for(auto t:targets)expected+=pc(t);
  for(const auto&e:edges)expected+=pc(e.target);

  Writer cnf(prefix+".cnf");cnf.out<<"p cnf "<<variables<<' '<<expected<<"\n";
  // Exactly one cell for every remaining lower target.
  for(int s=1;s<(1<<K);++s)if(pc(static_cast<uint16_t>(s))<R&&s!=PIN){
    for(int v:by_target[s])cnf.lit(v);cnf.end();emit_amo(cnf,by_target[s],target_aux[s]);
  }
  // At most one target per physical cell.
  for(size_t c=0;c<cells.size();++c)emit_amo(cnf,by_cell[c],cell_aux[c]);
  // a_{p,b} iff no selected incidence covering p omits b.
  for(size_t ai=0;ai<avec.size();++ai){int a=a0+ai;for(int y:blockers[ai]){cnf.lit(-a);cnf.lit(-y);cnf.end();}
    cnf.lit(a);for(int y:blockers[ai])cnf.lit(y);cnf.end();
  }
  // Every physical letter is nonempty.
  for(int p=0;p<L;++p){for(int bit=0;bit<K;++bit)if(avar[p][bit])cnf.lit(avar[p][bit]);cnf.end();}
  // Every middle bit is supplied somewhere in its assigned row interval.
  for(int i=0;i<W;++i)for(int bit=0;bit<K;++bit)if(targets[i]&(1u<<bit)){
    for(int p=starts[i];p<=deadlines[i];++p)if(avar[p][bit])cnf.lit(avar[p][bit]);cnf.end();
  }
  // If lower incidence (S,C) is selected, every bit of S appears in C.
  for(const auto&e:edges)for(int bit=0;bit<K;++bit)if(e.target&(1u<<bit)){
    cnf.lit(-e.var);const auto&c=cells[e.cell];for(int p=c.start;p<c.start+c.length;++p)if(avar[p][bit])cnf.lit(avar[p][bit]);cnf.end();
  }
  if(cnf.clauses!=expected)throw std::runtime_error("clause-count mismatch");
  cnf.out.close();

  std::ofstream map(prefix+".map.tsv");
  map<<"kind\tvar\ttarget\tcell\tstart\tlength\tposition\tbit\n";
  for(const auto&e:edges){const auto&c=cells[e.cell];map<<"y\t"<<e.var<<'\t'<<e.target<<'\t'<<e.cell<<'\t'<<c.start<<'\t'<<c.length<<"\t-1\t-1\n";}
  for(size_t ai=0;ai<avec.size();++ai)map<<"a\t"<<a0+ai<<"\t-1\t-1\t-1\t-1\t"<<avec[ai].first<<'\t'<<avec[ai].second<<'\n';
  map.close();

  std::ofstream meta(prefix+".meta.json");
  meta<<"{\n  \"schema\": \"k16.trueff.commoncap-direct-cnf.v1\",\n"
      <<"  \"target\": \""<<target_path<<"\",\n  \"target_sha256\": \""<<EXPECTED_SHA<<"\",\n"
      <<"  \"variables\": "<<variables<<",\n  \"clauses\": "<<expected<<",\n"
      <<"  \"incidence_variables\": "<<edges.size()<<",\n  \"letter_bit_variables\": "<<avec.size()<<",\n"
      <<"  \"remaining_lower_targets\": 26331,\n  \"physical_cells\": "<<cells.size()<<",\n"
      <<"  \"reserved_singleton\": {\"target\": 32768, \"position\": 6389, \"cell\": "<<reserved<<"},\n"
      <<"  \"start_holes\": [12870,12871,12872],\n  \"deadline_holes\": [0,1,6388],\n"
      <<"  \"selected_area\": 32224\n}\n";
  meta.close();

  std::cout<<"variables="<<variables<<" clauses="<<expected<<" y="<<edges.size()
           <<" a="<<avec.size()<<" cells="<<cells.size()<<" blockers=";
  long long bc=0;for(auto&b:blockers)bc+=b.size();std::cout<<bc<<"\n";
}
