// Exhaustive intrinsic-multiparent transfer census for the five canonical
// k=15 parents, relative to P0.
//
// The selected successor is Q=P0 o p.  A transfer p is intrinsic
// multiparent when no one nonbase parent supplies every changed successor
// arc.  For support at most eight, parity leaves exactly these derangement
// types:
//   3, 2+2, 5, 3+3, 4+2, 7, 3+2+2,
//   6+2, 5+3, 4+4, 2+2+2+2.
// Every candidate is tested for exact Hamilton monodromy, exact linear
// depth-three residence, and literal upper coverage q=1,...,7.  Every
// locally legal path is emitted for the independent Hall/DM auditor.
//
// Build:
//   c++ -O3 -march=native -DNDEBUG -std=c++20 \
//     scratch/enumerate_k15_intrinsic_multiparent_support3_7.cpp \
//     -o scratch/enumerate_k15_intrinsic_multiparent_support3_7
//
// Run:
//   ./scratch/enumerate_k15_intrinsic_multiparent_support3_7 \
//     P0 P1 P2 P3 P4 OUTPUT_DIR

#include <algorithm>
#include <array>
#include <bit>
#include <cctype>
#include <cstdint>
#include <filesystem>
#include <fstream>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <stdexcept>
#include <string>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

namespace {

constexpr int K = 15;
constexpr int R = 8;
constexpr int W = 6435;
constexpr int N = W + 1;
constexpr int DUMMY = W;
constexpr int PARENTS = 5;

std::string read_file(const std::string& path) {
  std::ifstream input(path, std::ios::binary);
  if (!input) throw std::runtime_error("cannot open " + path);
  std::ostringstream out;
  out << input.rdbuf();
  return out.str();
}

size_t skip_space(const std::string& text, size_t p) {
  while (p < text.size() &&
         std::isspace(static_cast<unsigned char>(text[p]))) ++p;
  return p;
}

std::vector<int> parse_array_at(const std::string& text, size_t p) {
  p = text.find('[', p);
  if (p == std::string::npos) return {};
  ++p;
  int nesting = 1;
  std::vector<int> result;
  while (p < text.size() && nesting) {
    p = skip_space(text, p);
    if (p >= text.size()) break;
    if (text[p] == '[') {
      ++nesting;
      ++p;
    } else if (text[p] == ']') {
      --nesting;
      ++p;
    } else if (text[p] == '-' ||
               std::isdigit(static_cast<unsigned char>(text[p]))) {
      bool negative = text[p] == '-';
      if (negative) ++p;
      int value = 0;
      while (p < text.size() &&
             std::isdigit(static_cast<unsigned char>(text[p]))) {
        value = 10 * value + (text[p++] - '0');
      }
      if (nesting == 1) result.push_back(negative ? -value : value);
    } else {
      ++p;
    }
  }
  return result;
}

std::vector<int> extract_middle(const std::string& path) {
  std::string text = read_file(path);
  for (const std::string key : {"middle_path", "middle_cycle"}) {
    size_t p = text.find("\"" + key + "\"");
    if (p != std::string::npos) {
      auto row = parse_array_at(text, p + key.size() + 2);
      if (!row.empty()) return row;
    }
  }
  throw std::runtime_error(path + ": no middle path");
}

int choose(int n, int r) {
  if (r < 0 || r > n) return 0;
  long long value = 1;
  for (int i = 1; i <= r; ++i) value = value * (n-r+i) / i;
  return static_cast<int>(value);
}

struct Cycle {
  std::vector<int> v;
  uint8_t common = 0;
};

struct Transposition {
  int a = -1;
  int b = -1;
  uint8_t common = 0;
};

struct TypeCount {
  uint64_t total = 0;
  uint64_t disjoint = 0;
  uint64_t parent_pure = 0;
  uint64_t intrinsic = 0;
  uint64_t hamilton = 0;
  uint64_t residence_safe = 0;
  uint64_t upper_safe = 0;
  uint64_t emitted = 0;
};

struct ResidenceClauseResult {
  bool impossible = false;
  std::vector<std::vector<int>> clauses;
};

struct PairKernel {
  int first_edge = -1;
  int second_edge = -1;
  std::array<int,4> support{};  // increasing frozen H29 position
  std::vector<std::vector<int>> clauses;
};

struct FourChordPattern {
  std::array<int,8> partner{};
  std::array<int,4> a_ranks{};
  std::array<int,4> b_ranks{};
};

struct FourChordCount {
  uint64_t raw_four_edge_subsets = 0;
  uint64_t abstract_matchings = 0;
  uint64_t abstract_one_cycle = 0;
  uint64_t abstract_three_cycle = 0;
  uint64_t abstract_five_cycle = 0;
  uint64_t crossing_pair_kernels = 0;
  uint64_t impossible_pair_kernels = 0;
  uint64_t indexed_pair_kernels = 0;
  uint64_t clean_pair_kernels = 0;
  uint64_t rescue_queries = 0;
  uint64_t range_queries = 0;
  uint64_t postings_scanned = 0;
  uint64_t box_candidates = 0;
  uint64_t mutual_rescue_candidates = 0;
  uint64_t intrinsic_candidates = 0;
  uint64_t parent_pure_candidates = 0;
  uint64_t intrinsic_residence_safe = 0;
  uint64_t parent_pure_residence_safe = 0;
  uint64_t intrinsic_upper_safe = 0;
  uint64_t parent_pure_upper_safe = 0;
  uint64_t intrinsic_emitted = 0;
  uint64_t parent_pure_emitted = 0;
};

class Census {
 public:
  explicit Census(const std::array<std::string,PARENTS>& source,
                  const std::filesystem::path& output,
                  int min_support,
                  int max_support,
                  bool include_parent_pure)
      : source_(source), output_(output), min_support_(min_support),
        max_support_(max_support),
        include_parent_pure_(include_parent_pure) {
    std::filesystem::create_directories(output_);
    load();
    enumerate_cycles();
  }

  void run() {
    if(min_support_<=3&&max_support_>=3)
      for (const Cycle& c : cycles_[3]) test("3", {c});

    if(min_support_<=4&&max_support_>=4) for (size_t i=0; i<trans_.size(); ++i) {
      for (size_t j=i+1; j<trans_.size(); ++j) {
        ++counts_["2+2"].total;
        if (!disjoint(trans_[i], trans_[j])) continue;
        ++counts_["2+2"].disjoint;
        test("2+2", {as_cycle(trans_[i]), as_cycle(trans_[j])});
      }
    }

    if(min_support_<=5&&max_support_>=5)
      for (const Cycle& c : cycles_[5]) test("5", {c});

    if(min_support_<=6&&max_support_>=6) for (size_t i=0; i<cycles_[3].size(); ++i) {
      for (size_t j=i+1; j<cycles_[3].size(); ++j) {
        ++counts_["3+3"].total;
        if (!disjoint(cycles_[3][i], cycles_[3][j])) continue;
        ++counts_["3+3"].disjoint;
        test("3+3", {cycles_[3][i],cycles_[3][j]});
      }
    }

    if(min_support_<=6&&max_support_>=6) for (const Cycle& c : cycles_[4]) {
      for (const Transposition& t : trans_) {
        ++counts_["4+2"].total;
        if (!disjoint(c,t)) continue;
        ++counts_["4+2"].disjoint;
        test("4+2", {c,as_cycle(t)});
      }
    }

    if(min_support_<=7&&max_support_>=7)
      for (const Cycle& c : cycles_[7]) test("7", {c});

    // The largest loop is about 1.35e8 tiny iterations and belongs on the
    // H100 CPU host.  No relaxation or random sampling is used.
    if(min_support_<=7&&max_support_>=7) counts_["3+2+2"].total =
        static_cast<uint64_t>(cycles_[3].size()) * trans_.size() *
        (trans_.size()-1) / 2;
    if(min_support_<=7&&max_support_>=7) for (const Cycle& c : cycles_[3]) {
      for (size_t i=0; i<trans_.size(); ++i) {
        if (!disjoint(c,trans_[i])) continue;
        for (size_t j=i+1; j<trans_.size(); ++j) {
          if (!disjoint(c,trans_[j]) || !disjoint(trans_[i],trans_[j]))
            continue;
          ++counts_["3+2+2"].disjoint;
          test("3+2+2", {c,as_cycle(trans_[i]),as_cycle(trans_[j])});
        }
      }
    }
    if(min_support_<=8&&max_support_>=8) {
      for(const Cycle&c:cycles_[6]) for(const Transposition&t:trans_) {
        ++counts_["6+2"].total;
        if(!disjoint(c,t))continue;
        ++counts_["6+2"].disjoint;
        test("6+2",{c,as_cycle(t)});
      }
      for(const Cycle&a:cycles_[5]) for(const Cycle&b:cycles_[3]) {
        ++counts_["5+3"].total;
        if(!disjoint(a,b))continue;
        ++counts_["5+3"].disjoint;
        test("5+3",{a,b});
      }
      for(size_t i=0;i<cycles_[4].size();++i)
        for(size_t j=i+1;j<cycles_[4].size();++j) {
          ++counts_["4+4"].total;
          if(!disjoint(cycles_[4][i],cycles_[4][j]))continue;
          ++counts_["4+4"].disjoint;
          test("4+4",{cycles_[4][i],cycles_[4][j]});
        }
      run_indexed_four_chords();
    }
    write_summary();
  }

 private:
  std::array<std::string,PARENTS> source_;
  std::filesystem::path output_;
  std::array<std::vector<int>,PARENTS> path_;
  std::array<std::vector<int>,PARENTS> succ_;
  std::vector<int> masks_, pos_, inv0_;
  std::vector<std::unordered_map<int,uint8_t>> transfer_;
  std::array<std::vector<Cycle>,9> cycles_;
  std::vector<Transposition> trans_;
  std::array<std::vector<int>,8> base_upper_;
  std::vector<int> pmap_, pinvmap_;
  std::map<std::string,TypeCount> counts_;
  std::map<std::string,TypeCount> pure_counts_;
  std::vector<std::vector<int>> incident_trans_;
  std::vector<PairKernel> pair_kernels_;
  std::vector<std::vector<int>> pair_by_vertex_;
  std::array<std::vector<int>,4> pair_coordinate_index_;
  std::vector<FourChordPattern> four_patterns_;
  FourChordCount four_count_;
  std::vector<uint32_t> pair_stamp_;
  uint32_t current_stamp_ = 0;
  uint64_t output_id_ = 0;
  int min_support_=3;
  int max_support_=7;
  bool include_parent_pure_=false;

  void load() {
    for (int a=0; a<PARENTS; ++a) {
      path_[a] = extract_middle(source_[a]);
      if (path_[a].size()!=W ||
          std::set<int>(path_[a].begin(),path_[a].end()).size()!=W)
        throw std::runtime_error(source_[a] + ": invalid path");
    }
    masks_=path_[0];
    std::sort(masks_.begin(),masks_.end());
    masks_.push_back(-1);
    std::unordered_map<int,int> node;
    for (int i=0;i<W;++i) node[masks_[i]]=i;
    for (int a=0;a<PARENTS;++a) {
      std::vector<int> order;
      for (int m:path_[a]) order.push_back(node.at(m));
      path_[a]=order;
      succ_[a].assign(N,-1);
      for (int i=0;i+1<W;++i) succ_[a][order[i]]=order[i+1];
      succ_[a][order.back()]=DUMMY;
      succ_[a][DUMMY]=order.front();
    }
    inv0_.assign(N,-1);
    for (int x=0;x<N;++x) inv0_[succ_[0][x]]=x;
    pos_.assign(N,-1);
    for (int i=0;i<W;++i) pos_[path_[0][i]]=i;
    pos_[DUMMY]=W;
    transfer_.resize(N);
    pmap_.assign(N,-1);
    pinvmap_.assign(N,-1);
    for (int x=0;x<N;++x) {
      for (int a=1;a<PARENTS;++a) {
        int y=inv0_[succ_[a][x]];
        if (y!=x) transfer_[x][y] |= static_cast<uint8_t>(1u<<a);
      }
    }
    for (int q=1;q<R;++q) {
      base_upper_[q].assign(1<<K,0);
      for (int i=0;i+q<W;++i) {
        int value=0;
        for (int j=0;j<=q;++j) value |= masks_[path_[0][i+j]];
        if (std::popcount(static_cast<unsigned>(value))==R+q)
          ++base_upper_[q][value];
      }
    }
  }

  static bool vector_less_rotation(const std::vector<int>& row, int shift) {
    for (int i=0;i<static_cast<int>(row.size());++i) {
      int a=row[(i+shift)%row.size()], b=row[i];
      if (a!=b) return a<b;
    }
    return false;
  }

  void cycle_dfs(int start,int length,std::vector<int>& row) {
    int x=row.back();
    if (static_cast<int>(row.size())==length) {
      auto it=transfer_[x].find(start);
      if (it==transfer_[x].end()) return;
      // Keep exactly the rotation beginning with the smallest node id.
      if (start!=*std::min_element(row.begin(),row.end())) return;
      uint8_t common=31;
      for (int i=0;i<length;++i)
        common &= transfer_[row[i]].at(row[(i+1)%length]);
      cycles_[length].push_back({row,common});
      return;
    }
    for (const auto& [y,mask]:transfer_[x]) {
      (void)mask;
      if (std::find(row.begin(),row.end(),y)!=row.end()) continue;
      row.push_back(y);
      cycle_dfs(start,length,row);
      row.pop_back();
    }
  }

  void enumerate_cycles() {
    for (int length:{3,4,5,6,7}) {
      for (int start=0;start<N;++start) {
        std::vector<int> row{start};
        cycle_dfs(start,length,row);
      }
      std::sort(cycles_[length].begin(),cycles_[length].end(),
                [](const Cycle&a,const Cycle&b){return a.v<b.v;});
    }
    for (int a=0;a<N;++a) {
      for (const auto& [b,mab]:transfer_[a]) {
        if (b<=a) continue;
        auto it=transfer_[b].find(a);
        if (it!=transfer_[b].end())
          trans_.push_back({a,b,static_cast<uint8_t>(mab&it->second)});
      }
    }
    std::sort(trans_.begin(),trans_.end(),[](const Transposition&x,
                                             const Transposition&y) {
      return std::tie(x.a,x.b)<std::tie(y.a,y.b);
    });
    incident_trans_.assign(N,{});
    for(int edge=0;edge<static_cast<int>(trans_.size());++edge) {
      incident_trans_[trans_[edge].a].push_back(edge);
      incident_trans_[trans_[edge].b].push_back(edge);
    }
  }

  static Cycle as_cycle(const Transposition&t) {
    return {{t.a,t.b},t.common};
  }
  static bool disjoint(const Cycle&a,const Cycle&b) {
    for(int x:a.v) for(int y:b.v) if(x==y) return false;
    return true;
  }
  static bool disjoint(const Cycle&a,const Transposition&b) {
    return std::find(a.v.begin(),a.v.end(),b.a)==a.v.end() &&
           std::find(a.v.begin(),a.v.end(),b.b)==a.v.end();
  }
  static bool disjoint(const Transposition&a,const Transposition&b) {
    return a.a!=b.a&&a.a!=b.b&&a.b!=b.a&&a.b!=b.b;
  }

  struct Permutation {
    std::vector<int> support;
  };

  Permutation make_p(const std::vector<Cycle>& parts) {
    Permutation result;
    result.support.reserve(8);
    for (const Cycle& c:parts) {
      for (int i=0;i<static_cast<int>(c.v.size());++i) {
        int x=c.v[i],y=c.v[(i+1)%c.v.size()];
        result.support.push_back(x);
        pmap_[x]=y;
        pinvmap_[y]=x;
      }
    }
    return result;
  }

  bool hamilton_monodromy(const Permutation& p) const {
    std::vector<int> order=p.support;
    std::sort(order.begin(),order.end(),[&](int a,int b){return pos_[a]<pos_[b];});
    std::array<int,8> g{};
    const int s=static_cast<int>(order.size());
    for(int i=0;i<s;++i) {
      int destination=pmap_[order[(i+1)%s]];
      g[i]=static_cast<int>(std::find(order.begin(),order.end(),destination)-order.begin());
      if(g[i]>=s) throw std::runtime_error("transfer leaves support");
    }
    std::array<char,8> seen{};
    int cycles=0;
    for(int x=0;x<s;++x) if(!seen[x]) {
      ++cycles;
      for(int y=x;!seen[y];y=g[y]) seen[y]=1;
    }
    return cycles==1;
  }

  int next(int x,const Permutation&p) const {
    (void)p;
    return succ_[0][pmap_[x]<0?x:pmap_[x]];
  }
  int previous(int x,const Permutation&p) const {
    (void)p;
    int y=inv0_[x];
    return pinvmap_[y]<0?y:pinvmap_[y];
  }

  void clear_p(const Permutation&p) {
    for(int x:p.support){pmap_[x]=-1;pinvmap_[x]=-1;}
  }

  bool residence_safe_local(const Permutation&p) const {
    std::set<int> starts;
    for(int edge:p.support) {
      int x=edge;
      for(int back=0;back<=3;++back) {
        starts.insert(x);
        x=previous(x,p);
      }
    }
    for(int start:starts) {
      if(start==DUMMY) continue;
      int following=next(start,p);
      if(following==DUMMY) continue;
      int inserted=masks_[following]&~masks_[start];
      int at=following;
      for(int delay=1;delay<=3;++delay) {
        int after=next(at,p);
        if(after==DUMMY) break;
        if((masks_[at]&~masks_[after])&inserted) return false;
        at=after;
      }
    }
    return true;
  }

  ResidenceClauseResult residence_clauses(const Permutation&p) const {
    ResidenceClauseResult result;
    std::vector<int> starts;
    starts.reserve(4*p.support.size());
    for(int edge:p.support) {
      int x=edge;
      for(int back=0;back<=3;++back) {
        if(std::find(starts.begin(),starts.end(),x)==starts.end())
          starts.push_back(x);
        x=previous(x,p);
      }
    }
    auto in_partial_support=[&](int x) {
      return std::find(p.support.begin(),p.support.end(),x)!=p.support.end();
    };
    for(int start:starts) {
      if(start==DUMMY)continue;
      int following=next(start,p);
      if(following==DUMMY)continue;
      int inserted=masks_[following]&~masks_[start];
      int at=following;
      std::vector<int> word_tails{start};
      for(int delay=1;delay<=3;++delay) {
        int after=next(at,p);
        if(after==DUMMY)break;
        word_tails.push_back(at);
        if((masks_[at]&~masks_[after])&inserted) {
          std::vector<int> clause;
          for(int tail:word_tails) {
            if(in_partial_support(tail)||tail==DUMMY||
               incident_trans_[tail].empty())continue;
            clause.push_back(tail);
          }
          std::sort(clause.begin(),clause.end());
          clause.erase(std::unique(clause.begin(),clause.end()),clause.end());
          if(clause.empty()) {
            result.impossible=true;
            result.clauses.clear();
            return result;
          }
          result.clauses.push_back(std::move(clause));
          break;
        }
        at=after;
      }
    }
    std::sort(result.clauses.begin(),result.clauses.end());
    result.clauses.erase(
        std::unique(result.clauses.begin(),result.clauses.end()),
        result.clauses.end());
    // If C is contained in D, hitting C automatically hits D, so D is
    // redundant.  Keeping only inclusion-minimal clauses also minimizes the
    // indexed completion query without weakening it.
    std::vector<std::vector<int>> minimal;
    for(size_t i=0;i<result.clauses.size();++i) {
      const auto& clause=result.clauses[i];
      bool redundant=false;
      for(size_t j=0;j<result.clauses.size();++j) if(i!=j) {
        const auto& other=result.clauses[j];
        if(other.size()<=clause.size()&&
           std::includes(clause.begin(),clause.end(),
                         other.begin(),other.end())) {
          redundant=true;
          break;
        }
      }
      if(!redundant)minimal.push_back(clause);
    }
    result.clauses=std::move(minimal);
    return result;
  }

  std::vector<int> materialize(const Permutation&p) const {
    std::vector<int> row;
    std::vector<char> seen(N,0);
    int x=next(DUMMY,p);
    while(x!=DUMMY&&!seen[x]) {
      seen[x]=1;
      row.push_back(x);
      x=next(x,p);
    }
    if(x!=DUMMY||row.size()!=W) return {};
    return row;
  }

  bool residence_safe_direct(const std::vector<int>& row) const {
    for(int i=0;i+1<W;++i) {
      int inserted=masks_[row[i+1]]&~masks_[row[i]];
      if(std::popcount(static_cast<unsigned>(inserted))!=1) return false;
      for(int delay=1;delay<=3&&i+delay+1<W;++delay) {
        if((masks_[row[i+delay]]&~masks_[row[i+delay+1]])&inserted)
          return false;
      }
    }
    return true;
  }

  bool upper_safe_direct(const std::vector<int>& row) const {
    for(int q=1;q<R;++q) {
      std::vector<char> hit(1<<K,0);
      int distinct=0;
      for(int i=0;i+q<W;++i) {
        int value=0;
        for(int j=0;j<=q;++j) value|=masks_[row[i+j]];
        if(std::popcount(static_cast<unsigned>(value))==R+q&&!hit[value]) {
          hit[value]=1;
          ++distinct;
        }
      }
      if(distinct!=choose(K,R+q)) return false;
    }
    return true;
  }

  bool upper_safe_local(const Permutation& p) const {
    // The base is upper-complete.  A changed non-wrapping q-window must
    // contain one of the changed successor edges, so these start sets are
    // the complete signed symmetric-difference ledger.
    for (int q=1;q<R;++q) {
      std::unordered_map<int,int> delta;
      std::set<int> starts;
      for (int edge:p.support) {
        int x=edge;
        for (int back=0;back<q;++back) {
          starts.insert(x);
          x=inv0_[x];
        }
      }
      for (int start:starts) {
        if (start==DUMMY) continue;
        int value=masks_[start],x=start;
        bool valid=true;
        for (int step=0;step<q;++step) {
          x=succ_[0][x];
          if (x==DUMMY) {valid=false;break;}
          value|=masks_[x];
        }
        if (valid&&std::popcount(static_cast<unsigned>(value))==R+q)
          --delta[value];
      }
      starts.clear();
      for (int edge:p.support) {
        int x=edge;
        for (int back=0;back<q;++back) {
          starts.insert(x);
          x=previous(x,p);
        }
      }
      for (int start:starts) {
        if (start==DUMMY) continue;
        int value=masks_[start],x=start;
        bool valid=true;
        for (int step=0;step<q;++step) {
          x=next(x,p);
          if (x==DUMMY) {valid=false;break;}
          value|=masks_[x];
        }
        if (valid&&std::popcount(static_cast<unsigned>(value))==R+q)
          ++delta[value];
      }
      for (const auto&[target,change]:delta)
        if (base_upper_[q][target]+change<=0) return false;
    }
    return true;
  }

  static bool crossing(std::pair<int,int> x,std::pair<int,int> y) {
    if(x.first>x.second)std::swap(x.first,x.second);
    if(y.first>y.second)std::swap(y.first,y.second);
    return (x.first<y.first&&y.first<x.second&&x.second<y.second)||
           (y.first<x.first&&x.first<y.second&&y.second<x.second);
  }

  bool physical_crossing(const Transposition&a,const Transposition&b) const {
    return crossing({pos_[a.a],pos_[a.b]},{pos_[b.a],pos_[b.b]});
  }

  void build_four_patterns() {
    if(!four_patterns_.empty())return;
    std::array<int,8> partner;
    partner.fill(-1);
    std::function<void()> generate=[&]() {
      int first=0;
      while(first<8&&partner[first]>=0)++first;
      if(first==8) {
        ++four_count_.abstract_matchings;
        std::array<char,8> seen{};
        int component_count=0;
        for(int x=0;x<8;++x)if(!seen[x]) {
          ++component_count;
          for(int y=x;!seen[y];y=partner[(y+1)%8])seen[y]=1;
        }
        if(component_count==1)++four_count_.abstract_one_cycle;
        else if(component_count==3)++four_count_.abstract_three_cycle;
        else if(component_count==5)++four_count_.abstract_five_cycle;
        else throw std::runtime_error("unexpected four-chord component count");
        if(component_count!=1)return;

        std::array<std::pair<int,int>,4> edges;
        int edge_count=0;
        for(int i=0;i<8;++i)if(i<partner[i])
          edges[edge_count++]={i,partner[i]};
        if(edge_count!=4)throw std::runtime_error("bad abstract matching");
        std::sort(edges.begin(),edges.end());

        // The interlace Pfaffian of a one-face four-chord diagram is one,
        // so at least one of the three 2+2 splits has crossing pairs on both
        // shores.  Choose the first split containing the lexicographically
        // first abstract chord; this makes the physical join duplicate-free.
        FourChordPattern pattern;
        pattern.partner=partner;
        bool found=false;
        for(int mate=1;mate<4&&!found;++mate) {
          std::array<int,2> ai{0,mate};
          std::array<int,2> bi{};
          int at=0;
          for(int e=1;e<4;++e)if(e!=mate)bi[at++]=e;
          if(!crossing(edges[ai[0]],edges[ai[1]])||
             !crossing(edges[bi[0]],edges[bi[1]]))continue;
          std::array<int,4> ar{
              edges[ai[0]].first,edges[ai[0]].second,
              edges[ai[1]].first,edges[ai[1]].second};
          std::array<int,4> br{
              edges[bi[0]].first,edges[bi[0]].second,
              edges[bi[1]].first,edges[bi[1]].second};
          std::sort(ar.begin(),ar.end());
          std::sort(br.begin(),br.end());
          pattern.a_ranks=ar;
          pattern.b_ranks=br;
          found=true;
        }
        if(!found)throw std::runtime_error("one-face pattern has no crossing split");
        four_patterns_.push_back(pattern);
        return;
      }
      for(int second=first+1;second<8;++second)if(partner[second]<0) {
        partner[first]=second;
        partner[second]=first;
        generate();
        partner[first]=partner[second]=-1;
      }
    };
    generate();
    if(four_count_.abstract_matchings!=105||
       four_count_.abstract_one_cycle!=21||
       four_count_.abstract_three_cycle!=70||
       four_count_.abstract_five_cycle!=14||four_patterns_.size()!=21)
      throw std::runtime_error("four-chord 105/21/70/14 audit failed");
    std::sort(four_patterns_.begin(),four_patterns_.end(),
              [](const FourChordPattern&a,const FourChordPattern&b) {
      return a.partner<b.partner;
    });
    std::ofstream out(output_/"support8_2222_patterns.tsv");
    out<<"pattern_id\tedges\ta_ranks\tb_ranks\n";
    for(size_t id=0;id<four_patterns_.size();++id) {
      const auto&p=four_patterns_[id];
      out<<id;
      for(int i=0;i<8;++i)if(i<p.partner[i])
        out<<'\t'<<i<<p.partner[i];
      out<<'\t';
      for(int i=0;i<4;++i){if(i)out<<',';out<<p.a_ranks[i];}
      out<<'\t';
      for(int i=0;i<4;++i){if(i)out<<',';out<<p.b_ranks[i];}
      out<<'\n';
    }
  }

  void build_crossing_pair_kernels() {
    if(!pair_kernels_.empty())return;
    const uint64_t edge_count=trans_.size();
    four_count_.raw_four_edge_subsets=
        edge_count*(edge_count-1)*(edge_count-2)*(edge_count-3)/24;
    for(int i=0;i<static_cast<int>(trans_.size());++i) {
      for(int j=i+1;j<static_cast<int>(trans_.size());++j) {
        if(!disjoint(trans_[i],trans_[j])||
           !physical_crossing(trans_[i],trans_[j]))continue;
        ++four_count_.crossing_pair_kernels;
        std::vector<Cycle> parts{as_cycle(trans_[i]),as_cycle(trans_[j])};
        Permutation p=make_p(parts);
        if(!hamilton_monodromy(p))
          throw std::runtime_error("crossing pair failed support-four monodromy");
        ResidenceClauseResult defects=residence_clauses(p);
        const bool locally_safe=residence_safe_local(p);
        if(locally_safe!=( !defects.impossible&&defects.clauses.empty()))
          throw std::runtime_error("residence clause ledger mismatch");
        if(locally_safe) {
          std::vector<int> row=materialize(p);
          if(row.empty()||!residence_safe_direct(row))
            throw std::runtime_error("clean pair failed direct residence replay");
          ++four_count_.clean_pair_kernels;
        }
        if(defects.impossible) {
          ++four_count_.impossible_pair_kernels;
          clear_p(p);
          continue;
        }
        PairKernel kernel;
        kernel.first_edge=i;
        kernel.second_edge=j;
        kernel.support={trans_[i].a,trans_[i].b,
                        trans_[j].a,trans_[j].b};
        std::sort(kernel.support.begin(),kernel.support.end(),
                  [&](int x,int y){return pos_[x]<pos_[y];});
        kernel.clauses=std::move(defects.clauses);
        pair_kernels_.push_back(std::move(kernel));
        clear_p(p);
      }
    }
    four_count_.indexed_pair_kernels=pair_kernels_.size();
    pair_by_vertex_.assign(N,{});
    for(int id=0;id<static_cast<int>(pair_kernels_.size());++id) {
      for(int x:pair_kernels_[id].support)pair_by_vertex_[x].push_back(id);
      for(int coordinate=0;coordinate<4;++coordinate)
        pair_coordinate_index_[coordinate].push_back(id);
    }
    for(int coordinate=0;coordinate<4;++coordinate) {
      auto& index=pair_coordinate_index_[coordinate];
      std::sort(index.begin(),index.end(),[&](int x,int y) {
        int px=pos_[pair_kernels_[x].support[coordinate]];
        int py=pos_[pair_kernels_[y].support[coordinate]];
        return px!=py?px<py:x<y;
      });
    }
    pair_stamp_.assign(pair_kernels_.size(),0);
  }

  static bool clauses_hit(const PairKernel&source,
                          const std::array<int,4>&other_support) {
    for(const auto&clause:source.clauses) {
      bool hit=false;
      for(int x:clause)
        if(std::find(other_support.begin(),other_support.end(),x)!=
           other_support.end()) {hit=true;break;}
      if(!hit)return false;
    }
    return true;
  }

  void audit_four_chord_candidate(int pattern_id,const PairKernel&a,
                                  const PairKernel&b) {
    std::array<int,4> edge_ids{
        a.first_edge,a.second_edge,b.first_edge,b.second_edge};
    std::sort(edge_ids.begin(),edge_ids.end());
    if(std::adjacent_find(edge_ids.begin(),edge_ids.end())!=edge_ids.end())
      throw std::runtime_error("four-chord join repeated an edge");
    std::vector<Cycle> parts;
    parts.reserve(4);
    uint8_t common=31;
    for(int edge:edge_ids) {
      parts.push_back(as_cycle(trans_[edge]));
      common&=trans_[edge].common;
    }
    const bool pure=common!=0;
    four_count_.intrinsic_candidates+=!pure;
    four_count_.parent_pure_candidates+=pure;
    if(pure&&!include_parent_pure_)return;
    Permutation p=make_p(parts);
    if(!hamilton_monodromy(p))
      throw std::runtime_error("21-pattern join failed exact monodromy");
    if(!residence_safe_local(p)) {clear_p(p);return;}
    four_count_.intrinsic_residence_safe+=!pure;
    four_count_.parent_pure_residence_safe+=pure;
    if(!upper_safe_local(p)) {clear_p(p);return;}
    four_count_.intrinsic_upper_safe+=!pure;
    four_count_.parent_pure_upper_safe+=pure;
    std::vector<int> row=materialize(p);
    if(row.empty()||!residence_safe_direct(row)||!upper_safe_direct(row))
      throw std::runtime_error("four-chord local/direct replay mismatch");
    emit(pure?"parent-pure/2+2+2+2":"2+2+2+2",parts,row,pattern_id);
    four_count_.intrinsic_emitted+=!pure;
    four_count_.parent_pure_emitted+=pure;
    clear_p(p);
  }

  void run_indexed_four_chords() {
    build_four_patterns();
    build_crossing_pair_kernels();
    auto position_at=[&](int kernel_id,int coordinate) {
      return pos_[pair_kernels_[kernel_id].support[coordinate]];
    };
    for(int pattern_id=0;
        pattern_id<static_cast<int>(four_patterns_.size());++pattern_id) {
      const auto&pattern=four_patterns_[pattern_id];
      for(int aid=0;aid<static_cast<int>(pair_kernels_.size());++aid) {
        const PairKernel&a=pair_kernels_[aid];
        std::array<int,4> lower{},upper{};
        for(int t=0;t<4;++t) {
          lower[t]=-1;
          upper[t]=N;
          for(int s=0;s<4;++s) {
            int value=pos_[a.support[s]];
            if(pattern.a_ranks[s]<pattern.b_ranks[t])lower[t]=value;
            else {upper[t]=value;break;}
          }
        }
        auto in_box=[&](int bid) {
          const auto&support=pair_kernels_[bid].support;
          for(int t=0;t<4;++t) {
            int value=pos_[support[t]];
            if(!(lower[t]<value&&value<upper[t]))return false;
          }
          return true;
        };
        auto process=[&](int bid) {
          ++four_count_.postings_scanned;
          if(!in_box(bid))return;
          ++four_count_.box_candidates;
          const PairKernel&b=pair_kernels_[bid];
          if(!clauses_hit(a,b.support)||!clauses_hit(b,a.support))return;
          ++four_count_.mutual_rescue_candidates;
          audit_four_chord_candidate(pattern_id,a,b);
        };

        if(!a.clauses.empty()) {
          ++four_count_.rescue_queries;
          const std::vector<int>*seed=&a.clauses.front();
          uint64_t best=UINT64_MAX;
          for(const auto&clause:a.clauses) {
            uint64_t size=0;
            for(int x:clause)size+=pair_by_vertex_[x].size();
            if(size<best){best=size;seed=&clause;}
          }
          if(++current_stamp_==0) {
            std::fill(pair_stamp_.begin(),pair_stamp_.end(),0);
            ++current_stamp_;
          }
          for(int x:*seed)for(int bid:pair_by_vertex_[x]) {
            if(pair_stamp_[bid]==current_stamp_)continue;
            pair_stamp_[bid]=current_stamp_;
            process(bid);
          }
        } else {
          ++four_count_.range_queries;
          int best_coordinate=0;
          size_t best_begin=0,best_end=pair_kernels_.size();
          for(int coordinate=0;coordinate<4;++coordinate) {
            const auto&index=pair_coordinate_index_[coordinate];
            auto begin_it=std::upper_bound(
                index.begin(),index.end(),lower[coordinate],
                [&](int value,int id){return value<position_at(id,coordinate);});
            auto end_it=std::lower_bound(
                index.begin(),index.end(),upper[coordinate],
                [&](int id,int value){return position_at(id,coordinate)<value;});
            size_t begin=begin_it-index.begin(),end=end_it-index.begin();
            if(end-begin<best_end-best_begin) {
              best_coordinate=coordinate;
              best_begin=begin;
              best_end=end;
            }
          }
          const auto&index=pair_coordinate_index_[best_coordinate];
          for(size_t at=best_begin;at<best_end;++at)process(index[at]);
        }
      }
    }
  }

  void emit(const std::string&type,const std::vector<Cycle>&parts,
            const std::vector<int>&row,int pattern_id=-1) {
    std::ostringstream name;
    name<<"candidate_";
    name.width(7);name.fill('0');name<<output_id_++<<".json";
    std::ofstream out(output_/name.str());
    const bool pure=type.rfind("parent-pure/",0)==0;
    out<<"{\n  \"status\":\""
       <<(pure?"PARENT_PURE_LOCAL_LEGAL":"INTRINSIC_MULTIPARENT_LOCAL_LEGAL")
       <<"\",\n";
    out<<"  \"type\":\""<<type<<"\",\n  \"parts\":[";
    for(size_t i=0;i<parts.size();++i) {
      if(i)out<<',';out<<'[';
      for(size_t j=0;j<parts[i].v.size();++j) {
        if(j)out<<',';int x=parts[i].v[j];
        out<<(x==DUMMY?-1:masks_[x]);
      }
      out<<']';
    }
    out<<"],\n";
    if(pattern_id>=0)out<<"  \"pattern_id\":"<<pattern_id<<",\n";
    out<<"  \"middle_path\":[";
    for(size_t i=0;i<row.size();++i){if(i)out<<',';out<<masks_[row[i]];}
    out<<"]\n}\n";
  }

  void test(const std::string&type,const std::vector<Cycle>&parts) {
    TypeCount& count=counts_[type];
    // Single-cycle types were not counted in the outer combinatorial loops.
    if(parts.size()==1){++count.total;++count.disjoint;}
    uint8_t common=31;
    for(const Cycle&c:parts) common&=c.common;
    const bool pure=common!=0;
    if(pure) {
      ++count.parent_pure;
      int support_size=0;
      for(const Cycle&c:parts)support_size+=c.v.size();
      if(!include_parent_pure_||support_size>max_support_)return;
      ++pure_counts_[type].total;
    } else {
      ++count.intrinsic;
    }
    TypeCount& evaluated=pure?pure_counts_[type]:count;
    Permutation p=make_p(parts);
    if(!hamilton_monodromy(p)){clear_p(p);return;}
    ++evaluated.hamilton;
    if(!residence_safe_local(p)){clear_p(p);return;}
    ++evaluated.residence_safe;
    if(!upper_safe_local(p)){clear_p(p);return;}
    std::vector<int> row=materialize(p);
    if(row.empty()) throw std::runtime_error("monodromy/materialization mismatch");
    if(!residence_safe_direct(row))
      throw std::runtime_error("local/direct residence mismatch");
    if(!upper_safe_direct(row))
      throw std::runtime_error("local/direct upper mismatch");
    ++evaluated.upper_safe;
    emit(pure?"parent-pure/"+type:type,parts,row);
    ++evaluated.emitted;
    clear_p(p);
  }

  void write_summary() const {
    std::ofstream out(output_/"summary.json");
    out<<"{\n  \"status\":\"PASS\",\n";
    out<<"  \"scope\":\"exact five-parent transfer census over the requested support interval\",\n";
    out<<"  \"min_support\":"<<min_support_<<",\n";
    out<<"  \"max_support\":"<<max_support_<<",\n";
    out<<"  \"include_parent_pure\":"
       <<(include_parent_pure_?"true":"false")<<",\n";
    out<<"  \"cycle_counts\":{\"3\":"<<cycles_[3].size()
       <<",\"4\":"<<cycles_[4].size()<<",\"5\":"<<cycles_[5].size()
       <<",\"6\":"<<cycles_[6].size()
       <<",\"7\":"<<cycles_[7].size()<<"},\n";
    out<<"  \"transpositions\":"<<trans_.size()<<",\n  \"types\":{\n";
    bool first=true;
    for(const auto&[name,c]:counts_) {
      if(!first)out<<",\n";first=false;
      out<<"    \""<<name<<"\":{";
      out<<"\"total\":"<<c.total<<",\"disjoint\":"<<c.disjoint
         <<",\"parent_pure\":"<<c.parent_pure
         <<",\"intrinsic\":"<<c.intrinsic
         <<",\"hamilton\":"<<c.hamilton
         <<",\"residence_safe\":"<<c.residence_safe
         <<",\"upper_safe\":"<<c.upper_safe
         <<",\"emitted\":"<<c.emitted<<'}';
    }
    out<<"\n  },\n  \"emitted_total\":"<<output_id_<<"\n}\n";
    // Insert the optional pure audit as a sibling JSON file so the primary
    // intrinsic schema and its frozen hashes remain stable.
    if(include_parent_pure_) {
      std::ofstream pure(output_/"parent_pure_summary.json");
      pure<<"{\n  \"status\":\"PASS\",\n  \"types\":{\n";
      bool first_pure=true;
      for(const auto&[name,c]:pure_counts_) {
        if(!first_pure)pure<<",\n";first_pure=false;
        pure<<"    \""<<name<<"\":{";
        pure<<"\"evaluated\":"<<c.total
            <<",\"hamilton\":"<<c.hamilton
            <<",\"residence_safe\":"<<c.residence_safe
            <<",\"upper_safe\":"<<c.upper_safe
            <<",\"emitted\":"<<c.emitted<<'}';
      }
      pure<<"\n  }\n}\n";
    }
  }
};

} // namespace

int main(int argc,char**argv) {
  try {
    if(argc<7||argc>10) throw std::runtime_error(
        "usage: census P0 P1 P2 P3 P4 OUT [--min-support=N] [--max-support=N] [--include-parent-pure]");
    std::array<std::string,PARENTS> source;
    for(int i=0;i<PARENTS;++i)source[i]=argv[i+1];
    int min_support=3,max_support=7;
    bool include_parent_pure=false;
    for(int i=7;i<argc;++i) {
      std::string option=argv[i];
      if(option=="--include-parent-pure") include_parent_pure=true;
      else if(option.rfind("--min-support=",0)==0)
        min_support=std::stoi(option.substr(14));
      else if(option.rfind("--max-support=",0)==0)
        max_support=std::stoi(option.substr(14));
      else throw std::runtime_error("unknown option "+option);
    }
    Census census(source,argv[6],min_support,max_support,include_parent_pure);
    census.run();
    std::cout<<read_file((std::filesystem::path(argv[6])/"summary.json").string());
    return 0;
  } catch(const std::exception&e) {
    std::cerr<<"error: "<<e.what()<<'\n';
    return 2;
  }
}
