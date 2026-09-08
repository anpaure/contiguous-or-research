// PREPARED FOR REVIEW ONLY. One fixed graph; no word or assignment search.
#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stdexcept>
#include <string>
#include <unordered_set>
#include <vector>
#include <sys/resource.h>
#include <unistd.h>

using M=uint32_t;
constexpr int K=21, WIDTH=352716, N=353297;
constexpr M FULL=(1u<<K)-1;
const std::array<int,3> PERIODS={352548,105,63};
std::string OUT;
void need(bool ok,const std::string& msg){if(!ok)throw std::runtime_error(msg);}
int pop(M x){return __builtin_popcount(x);}
M rot(M x){return ((x<<1)&FULL)|(x>>(K-1));}
double cpu(){rusage u{};getrusage(RUSAGE_SELF,&u);return u.ru_utime.tv_sec+u.ru_utime.tv_usec*1e-6+u.ru_stime.tv_sec+u.ru_stime.tv_usec*1e-6;}
M phi(M x){int h=0,m=0,p=-1;for(int j=0;j<K;j++){h+=(x>>j&1)?1:-1;if(h<m){m=h;p=j;}}need(h==-1&&p>=0,"Phi domain");need(!(x&(1u<<p)),"Phi adds absent bit");return x|(1u<<p);}
std::ofstream output(const std::string& name,bool binary=false){std::ofstream f(OUT+"/"+name,binary?std::ios::binary:std::ios::out);need(bool(f),"open output "+name);return f;}
std::ifstream input(const std::string& name,bool binary=false){std::ifstream f(OUT+"/"+name,binary?std::ios::binary:std::ios::in);need(bool(f),"open replay "+name);return f;}
void put32(std::ostream& f,uint32_t x){for(int j=0;j<4;j++)f.put(char((x>>(8*j))&255));}
void put64(std::ostream& f,uint64_t x){for(int j=0;j<8;j++)f.put(char((x>>(8*j))&255));}
uint32_t get32(std::istream& f){uint32_t x=0;for(int j=0;j<4;j++){int c=f.get();need(c!=EOF,"truncated graph");x|=uint32_t(c)<<(8*j);}return x;}
uint64_t get64(std::istream& f){uint64_t x=0;for(int j=0;j<8;j++){int c=f.get();need(c!=EOF,"truncated graph");x|=uint64_t(c)<<(8*j);}return x;}

struct Cycle{std::vector<M>A,R,U,E;};
struct Target{M representative;int weight,rank;};
struct Cell{int cycle,pos,length;M representative,forced,available,e0,e1;std::vector<int> targets,flow_edges;};
M at(const std::vector<M>& v,int i){int n=int(v.size());i%=n;if(i<0)i+=n;return v[i];}

std::pair<M,M> cell_bounds(const Cycle& c,int pos,int len){
  M forced=0,available=0;
  for(int d=0;d<len;d++)available|=at(c.E,pos+d);
  for(int start=-2;start<len;start++){
    M outside=0;
    for(int d=start;d<start+3;d++)if(d<0||d>=len)outside|=at(c.E,pos+d);
    forced|=at(c.R,pos+start)&~outside;
  }
  need(!(forced&~available),"forced deficit outside available cap");
  return {forced,available};
}

// Every candidate is generated from exact deficits. Replaying each accepted
// maximal cap on every affected native triple checks the constructive direction.
template<class F> void candidates(const Cycle& c,const Cell& cell,F accept,bool replay){
  M free=cell.available&~cell.forced;
  for(M sub=free;;sub=(sub-1)&free){
    M s=cell.forced|sub;
    if(s&&pop(s)<=9&&(s&cell.e0)&&(cell.length==1||(s&cell.e1))){
      if(replay){
        M exact_or=0;for(int d=0;d<cell.length;d++)exact_or|=at(c.E,cell.pos+d)&s;
        need(exact_or==s,"candidate target OR");
        for(int start=-2;start<cell.length;start++){
          M actual=0;
          for(int d=start;d<start+3;d++){
            M letter=at(c.E,cell.pos+d);
            if(0<=d&&d<cell.length)letter&=s;
            need(letter!=0,"candidate nonempty affected letter");actual|=letter;
          }
          need(actual==at(c.R,cell.pos+start),"candidate affected triple replay");
        }
      }
      accept(s);
    }
    if(sub==0)break;
  }
}

struct Dinic{
  struct Edge{int to,next,cap;};
  std::vector<int> head,level,ptr,q;std::vector<Edge> e;
  explicit Dinic(int n,size_t reserve):head(n,-1),level(n),ptr(n),q(n){e.reserve(reserve);}
  int add(int a,int b,int cap){int id=int(e.size());e.push_back({b,head[a],cap});head[a]=id;e.push_back({a,head[b],0});head[b]=id+1;return id;}
  bool bfs(int s,int t){std::fill(level.begin(),level.end(),-1);int a=0,b=0;q[b++]=s;level[s]=0;while(a<b){int v=q[a++];for(int id=head[v];id!=-1;id=e[id].next)if(e[id].cap&&level[e[id].to]<0){level[e[id].to]=level[v]+1;q[b++]=e[id].to;}}return level[t]>=0;}
  int dfs(int v,int t,int amount){if(v==t)return amount;for(int& id=ptr[v];id!=-1;id=e[id].next){auto& z=e[id];if(z.cap&&level[z.to]==level[v]+1){int got=dfs(z.to,t,std::min(amount,z.cap));if(got){z.cap-=got;e[id^1].cap+=got;return got;}}}return 0;}
  int solve(int s,int t){int total=0;while(bfs(s,t)){ptr=head;while(int f=dfs(s,t,1000000000))total+=f;}return total;}
  std::vector<char> reachable(int s){std::vector<char>seen(head.size());std::queue<int>q0;q0.push(s);seen[s]=1;while(!q0.empty()){int v=q0.front();q0.pop();for(int id=head[v];id!=-1;id=e[id].next)if(e[id].cap&&!seen[e[id].to]){seen[e[id].to]=1;q0.push(e[id].to);}}return seen;}
};

int main(int argc,char**argv){
  auto begun=std::chrono::steady_clock::now();double begun_cpu=cpu();
  try{
    need(argc==3,"arguments: input word, fresh wrapper-created output directory");OUT=argv[2];
    char host[256]{};need(gethostname(host,sizeof(host))==0,"hostname");need(std::string(host).substr(0,std::string(host).find('.'))=="arboghast","h100 only");
    std::ifstream in(argv[1]);need(bool(in),"input word");std::vector<M>word;std::string tok;
    while(in>>tok){need(!tok.empty()&&std::all_of(tok.begin(),tok.end(),[](unsigned char c){return c>='0'&&c<='9';}),"decimal word token");unsigned long long x=std::stoull(tok);need(x>0&&x<=FULL,"word mask range");word.push_back(M(x));}
    need(word.size()==N,"fixed literal length");
    std::vector<Cycle>cycles;int offset=0;std::map<int,int>ehist,pairhist;
    for(int period:PERIODS){
      Cycle c;c.A.assign(word.begin()+offset,word.begin()+offset+period);
      for(int j=0;j<3;j++)need(word[offset+period+j]==c.A[j],"literal prefix-three collar");offset+=period+3;
      c.R.resize(period);c.U.resize(period);c.E.resize(period);
      for(int i=0;i<period;i++){c.R[i]=at(c.A,i)|at(c.A,i+1)|at(c.A,i+2);c.U[i]=c.R[i]|at(c.A,i+3);need(pop(c.R[i])==10&&pop(c.U[i])==11,"middle ranks");need(phi(c.R[i])==c.U[i],"canonical outgoing Phi");}
      for(int i=0;i<period;i++){c.E[i]=at(c.U,i-3)&at(c.U,i-2)&at(c.U,i-1)&c.U[i];need(c.E[i]&&!(c.A[i]&~c.E[i]),"literal below maximal antecedent");ehist[pop(c.E[i])]++;}
      for(int i=0;i<period;i++){
        need((c.R[i]|at(c.R,i+1))==c.U[i],"owner union phase");need((at(c.U,i-1)&c.U[i])==c.R[i],"owner intersection phase");
        need((c.E[i]|at(c.E,i+1)|at(c.E,i+2))==c.R[i],"maximal triple identity");need((c.E[i]|at(c.E,i+1)|at(c.E,i+2)|at(c.E,i+3))==c.U[i],"maximal four identity");pairhist[pop(c.E[i]|at(c.E,i+1))]++;
      }cycles.push_back(std::move(c));
    }
    need(offset==WIDTH+9&&int(word.size())-offset==572,"exact three-cycle-plus-repair layout");
    std::vector<int>where(FULL+1,-1),location_cycle,location_pos;location_cycle.reserve(WIDTH);location_pos.reserve(WIDTH);std::vector<char>seen_upper(FULL+1);
    for(int ci=0;ci<3;ci++)for(int i=0;i<int(cycles[ci].R.size());i++){
      M r=cycles[ci].R[i],u=cycles[ci].U[i];need(where[r]<0&&!seen_upper[u],"globally unique middle owners");where[r]=int(location_cycle.size());location_cycle.push_back(ci);location_pos.push_back(i);seen_upper[u]=1;
    }need(location_cycle.size()==WIDTH,"complete middle deck size");
    int all10=0,all11=0;for(M s=1;s<=FULL;s++){if(pop(s)==10){need(where[s]>=0,"every rank10 owner");all10++;}if(pop(s)==11){need(seen_upper[s],"every rank11 owner");all11++;}}need(all10==WIDTH&&all11==WIDTH,"middle counts");
    std::vector<int>representatives;
    for(int z=0;z<WIDTH;z++){
      int ci=location_cycle[z],i=location_pos[z];const auto&c=cycles[ci];M r=c.R[i];int zi=where[rot(r)];need(zi>=0,"rotated owner exists");int cj=location_cycle[zi],j=location_pos[zi];const auto&d=cycles[cj];
      need(ci==cj&&rot(at(c.R,i+1))==at(d.R,j+1)&&rot(c.U[i])==d.U[j]&&rot(c.E[i])==d.E[j],"carrier and cap rotation equivariance");
      M smallest=r,x=rot(r);int orbit=1;while(x!=r){smallest=std::min(smallest,x);x=rot(x);orbit++;need(orbit<=21,"middle orbit closes");}need(orbit==21,"full middle rotation orbit");if(smallest==r)representatives.push_back(z);
    }need(representatives.size()*21==WIDTH,"all physical cells in full orbits");

    std::vector<int>target_id(FULL+1,-1);std::vector<Target>targets;int demand=0;
    for(M s=1;s<=FULL;s++)if(pop(s)<=9&&target_id[s]<0){int id=int(targets.size()),size=0;M x=s;do{need(target_id[x]<0,"target orbit disjointness");target_id[x]=id;size++;x=rot(x);need(size<=21,"target orbit closes");}while(x!=s);need(size==3||size==7||size==21,"actual nonempty small-rank orbit size");targets.push_back({s,size,pop(s)});demand+=size;}
    int actual_low=0;for(M s=1;s<=FULL;s++)if(pop(s)<=9){need(target_id[s]>=0,"every lower target in orbit inventory");actual_low++;}need(demand==actual_low,"weighted target count");
    {auto f=output("target_orbits.tsv");for(int t=0;t<int(targets.size());t++)f<<t<<'\t'<<targets[t].representative<<'\t'<<targets[t].weight<<'\t'<<targets[t].rank<<'\n';need(bool(f),"target mapping write");}
    std::vector<Cell>cells;cells.reserve(representatives.size()*2);uint64_t candidate_count=0,edges=0;
    for(int z:representatives)for(int len=1;len<=2;len++){
      int ci=location_cycle[z],pos=location_pos[z];const auto&c=cycles[ci];auto bounds=cell_bounds(c,pos,len);
      Cell cell{ci,pos,len,c.R[pos],bounds.first,bounds.second,c.E[pos],len==2?at(c.E,pos+1):0,{},{}};
      candidates(c,cell,[&](M s){int t=target_id[s];need(t>=0,"candidate target orbit");cell.targets.push_back(t);candidate_count++;},true);
      std::sort(cell.targets.begin(),cell.targets.end());cell.targets.erase(std::unique(cell.targets.begin(),cell.targets.end()),cell.targets.end());edges+=cell.targets.size();cells.push_back(std::move(cell));
    }
    {auto f=output("cell_orbits.tsv");for(int c=0;c<int(cells.size());c++){const auto&v=cells[c];f<<c<<'\t'<<v.length<<'\t'<<v.cycle<<'\t'<<v.pos<<'\t'<<v.representative<<'\t'<<v.forced<<'\t'<<v.available<<'\t'<<v.e0<<'\t'<<v.e1<<'\t'<<v.targets.size()<<'\n';}need(bool(f),"cell mapping write");}
    {auto f=output("graph_rows.bin",true);f.write("H21ROW01",8);put32(f,targets.size());put32(f,cells.size());put64(f,edges);for(const auto&c:cells){put32(f,c.targets.size());for(int t:c.targets)put32(f,t);}need(bool(f),"complete graph write");}
    std::cout<<"GRAPH_READY targets="<<targets.size()<<" demand="<<demand<<" cells="<<cells.size()<<" edges="<<edges<<" candidates="<<candidate_count<<std::endl;

    int nt=int(targets.size()),nc=int(cells.size()),source=nt+nc,sink=source+1,INF=demand+1;
    need(edges+nt+nc<1000000000ULL,"integer edge-index range");Dinic network(sink+1,2*(edges+nt+nc));
    for(int t=0;t<nt;t++)network.add(source,t,targets[t].weight);
    for(int c=0;c<nc;c++){network.add(nt+c,sink,21);for(int t:cells[c].targets)cells[c].flow_edges.push_back(network.add(t,nt+c,INF));}
    int flow=network.solve(source,sink);auto reachable=network.reachable(source);need(!reachable[sink],"terminal residual cut");
    {auto f=output("positive_flow.tsv");for(int c=0;c<nc;c++)for(size_t j=0;j<cells[c].targets.size();j++){int amount=network.e[cells[c].flow_edges[j]^1].cap;if(amount)f<<cells[c].targets[j]<<'\t'<<c<<'\t'<<amount<<'\n';}need(bool(f),"flow write");}
    {auto f=output("cut_target_orbits.txt");for(int t=0;t<nt;t++)if(reachable[t])f<<t<<'\n';}
    {auto f=output("cut_cell_orbits.txt");for(int c=0;c<nc;c++)if(reachable[nt+c])f<<c<<'\n';}

    // Certificate replay: reread persisted graph/flow/cut. It does not use
    // Dinic residual capacities, source/sink arcs, or its claimed conservation.
    std::vector<std::vector<int>>saved_rows(nc);uint64_t replay_edges=0;
    {auto f=input("graph_rows.bin",true);char magic[8];f.read(magic,8);need(std::string(magic,8)=="H21ROW01","graph header");need(get32(f)==uint32_t(nt)&&get32(f)==uint32_t(nc)&&get64(f)==edges,"graph sizes");for(int c=0;c<nc;c++){uint32_t degree=get32(f);need(degree<=uint32_t(nt),"deduplicated graph degree");auto&row=saved_rows[c];row.resize(degree);for(int& t:row){t=get32(f);need(0<=t&&t<nt,"saved target index");}need(std::is_sorted(row.begin(),row.end())&&std::adjacent_find(row.begin(),row.end())==row.end(),"saved row sorted unique");need(row==cells[c].targets,"persisted complete graph matches generator");replay_edges+=degree;}need(f.get()==EOF&&replay_edges==edges,"graph exact end");}
    std::vector<int>target_load(nt),cell_load(nc);std::unordered_set<uint64_t>used_edges;uint64_t positive_records=0;long long replay_flow=0;
    {auto f=input("positive_flow.tsv");std::string line;while(std::getline(f,line)){std::istringstream row(line);int t,c,a;std::string extra;need(bool(row>>t>>c>>a)&&!(row>>extra),"complete three-field flow row");need(0<=t&&t<nt&&0<=c&&c<nc&&a>0&&a<=21,"flow record range");need(std::binary_search(saved_rows[c].begin(),saved_rows[c].end(),t),"flow edge belongs to complete graph");uint64_t key=uint64_t(t)*nc+c;need(used_edges.insert(key).second,"one positive record per edge");target_load[t]+=a;cell_load[c]+=a;need(target_load[t]<=targets[t].weight&&cell_load[c]<=21,"replayed source/target and cell/sink capacities");replay_flow+=a;positive_records++;}need(f.eof(),"flow parse complete");}
    need(replay_flow==flow&&std::accumulate(target_load.begin(),target_load.end(),0LL)==replay_flow&&std::accumulate(cell_load.begin(),cell_load.end(),0LL)==replay_flow,"replayed flow conservation and value");
    std::vector<char>F(nt),saved_neighbors(nc),neighbors(nc);int countF=0,countN=0;long long demandF=0;
    {auto f=input("cut_target_orbits.txt");int t;while(f>>t){need(0<=t&&t<nt&&!F[t],"cut target range and uniqueness");F[t]=1;countF++;demandF+=targets[t].weight;}need(f.eof(),"target cut parse");}
    {auto f=input("cut_cell_orbits.txt");int c;while(f>>c){need(0<=c&&c<nc&&!saved_neighbors[c],"cut cell range and uniqueness");saved_neighbors[c]=1;}need(f.eof(),"cell cut parse");}
    uint64_t neighbor_candidate_replay=0;
    for(int c=0;c<nc;c++){
      bool row_neighbor=false;for(int t:saved_rows[c])if(F[t]){row_neighbor=true;break;}
      // Regenerate the ENTIRE local menu from native owner deficits. This
      // checks the full Hall-neighbor union independently of exported rows.
      auto b=cell_bounds(cycles[cells[c].cycle],cells[c].pos,cells[c].length);need(b.first==cells[c].forced&&b.second==cells[c].available,"Hall deficit regeneration");
      bool direct_neighbor=false;candidates(cycles[cells[c].cycle],cells[c],[&](M s){neighbor_candidate_replay++;if(F[target_id[s]])direct_neighbor=true;},false);
      need(row_neighbor==direct_neighbor&&saved_neighbors[c]==direct_neighbor,"full direct Hall neighborhood replay");neighbors[c]=direct_neighbor;if(direct_neighbor)countN++;
    }
    long long capacityN=21LL*countN,deficit=demandF-capacityN;
    need(deficit==demand-replay_flow&&deficit>=0,"feasible-flow / Hall-upper-bound equality certifies optimum");
    {auto f=output("hall_physical_target_masks.txt");for(M s=1;s<=FULL;s++)if(pop(s)<=9&&F[target_id[s]])f<<s<<'\n';need(bool(f),"physical Hall target export");}
    {auto f=output("hall_physical_neighbor_cells.tsv");long long physical=0;for(int c=0;c<nc;c++)if(neighbors[c]){M x=cells[c].representative;for(int j=0;j<21;j++){int z=where[x];need(z>=0,"Hall physical cell rotation");f<<location_cycle[z]<<'\t'<<location_pos[z]<<'\t'<<cells[c].length<<'\t'<<c<<'\n';physical++;x=rot(x);}need(x==cells[c].representative,"Hall cell orbit closes");}need(physical==capacityN&&bool(f),"full physical Hall neighbor export");}
    auto elapsed=std::chrono::duration<double>(std::chrono::steady_clock::now()-begun).count();
    auto report=output("candidate_hall_certificate.json");
    report<<"{\n  \"status\": \"PASS_FIXED_GRAPH_AND_INDEPENDENT_CERTIFICATE_REPLAY\",\n"
      <<"  \"physical_positions\": "<<WIDTH<<",\n  \"target_orbits\": "<<nt<<",\n  \"target_weight\": "<<demand<<",\n  \"cell_orbits\": "<<nc<<",\n  \"cell_orbit_capacity\": 21,\n"
      <<"  \"graph_edges\": "<<edges<<",\n  \"accepted_local_masks_before_orbit_deduplication\": "<<candidate_count<<",\n  \"maximum_weighted_flow\": "<<flow<<",\n  \"physical_hall_deficiency\": "<<deficit<<",\n"
      <<"  \"cut_target_orbits\": "<<countF<<",\n  \"cut_physical_target_weight\": "<<demandF<<",\n  \"full_neighbor_cell_orbits\": "<<countN<<",\n  \"full_neighbor_physical_capacity\": "<<capacityN<<",\n"
      <<"  \"positive_flow_records_replayed\": "<<positive_records<<",\n  \"local_masks_regenerated_for_full_neighbor_replay\": "<<neighbor_candidate_replay<<",\n"
      <<"  \"claimed_edges\": 1997177,\n  \"claimed_flow\": 695397,\n  \"claimed_deficiency\": 462,\n"
      <<"  \"claimed_edge_count_matches\": "<<(edges==1997177?"true":"false")<<",\n  \"claimed_flow_matches\": "<<(flow==695397?"true":"false")<<",\n  \"claimed_deficiency_matches\": "<<(deficit==462?"true":"false")<<",\n"
      <<"  \"cpu_seconds\": "<<cpu()-begun_cpu<<",\n  \"wall_seconds\": "<<elapsed<<",\n"
      <<"  \"checks\": {\"all_middle_owners\":true,\"canonical_phi\":true,\"rotation_equivariance\":true,\"maximal_antecedents\":true,\"every_accepted_cap_replayed\":true,\"saved_flow_feasible\":true,\"full_Hall_neighbor_set_regenerated\":true,\"max_flow_min_cut_value_equality\":true},\n"
      <<"  \"scope\": \"One fixed three-cycle maximal-cap candidate graph. No word search, alternate cuts, reassignment solver, or simultaneous-cap construction. The claimed counts were comparisons, not premises.\"\n}\n";
    need(bool(report),"final report write");report.close();
    std::cout<<"PASS_FIXED_GRAPH flow="<<flow<<" deficiency="<<deficit<<" Hall_weight="<<demandF<<" neighbor_capacity="<<capacityN<<" cpu="<<cpu()-begun_cpu<<" wall="<<elapsed<<std::endl;
    return 0;
  }catch(const std::bad_alloc&){if(!OUT.empty()){auto f=output("failure.json");f<<"{\"status\":\"INCONCLUSIVE_MEMORY_LIMIT\"}\n";}std::cerr<<"Memory limit\n";return 3;}
  catch(const std::exception& e){if(!OUT.empty()){auto f=output("failure.json");f<<"{\"status\":\"ERROR_NOT_CERTIFIED\"}\n";}std::cerr<<"ERROR: "<<e.what()<<'\n';return 2;}
}
