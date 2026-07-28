#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <set>
#include <sstream>
#include <string>
#include <tuple>
#include <unordered_set>
#include <vector>

using Mask = uint16_t;

static std::vector<Mask> read_middle_path(const std::string& filename) {
    std::ifstream in(filename);
    std::ostringstream out;
    out << in.rdbuf();
    std::string text = out.str();
    auto key = text.find("\"middle_path\"");
    if (key == std::string::npos) throw std::runtime_error("no middle_path");
    auto left = text.find('[', key);
    auto right = text.find(']', left);
    std::vector<Mask> answer;
    uint32_t value = 0;
    bool inside = false;
    for (size_t i = left + 1; i < right; ++i) {
        if (text[i] >= '0' && text[i] <= '9') {
            value = value * 10 + uint32_t(text[i] - '0');
            inside = true;
        } else if (inside) {
            answer.push_back(Mask(value));
            value = 0;
            inside = false;
        }
    }
    if (inside) answer.push_back(Mask(value));
    return answer;
}

static bool adjacent(Mask a, Mask b) {
    return std::popcount(uint16_t(a ^ b)) == 2;
}

struct Piece {
    int family;  // 0=A, 1=B
    int side;    // 0=left, 1=right
    bool reverse;
};

struct Piece5 {
    int family;  // 0=A (two pieces), 1=B (three pieces)
    int side;
    bool reverse;
};

static std::pair<int, int> bounds5(
    const Piece5& p, int acut, int bcut, int n
) {
    if (!p.family) {
        return p.side == 0 ? std::pair<int,int>{0, acut}
                           : std::pair<int,int>{acut, n};
    }
    if (p.side == 0) return {0, bcut};
    if (p.side == 1) return {bcut, bcut + 3};
    return {bcut + 3, n};
}

static std::pair<Mask, Mask> endpoints5(
    const Piece5& p, int acut, int bcut,
    const std::vector<Mask>& a, const std::vector<Mask>& b
) {
    const auto& row = p.family ? b : a;
    auto [lo, hi] = bounds5(p, acut, bcut, int(row.size()));
    Mask first = row[lo], last = row[hi - 1];
    if (p.reverse) std::swap(first, last);
    return {first, last};
}

static void append_piece5(
    std::vector<Mask>& answer, const Piece5& p, int acut, int bcut,
    const std::vector<Mask>& a, const std::vector<Mask>& b
) {
    const auto& row = p.family ? b : a;
    auto [lo, hi] = bounds5(p, acut, bcut, int(row.size()));
    if (!p.reverse) answer.insert(answer.end(), row.begin() + lo, row.begin() + hi);
    else for (int i = hi - 1; i >= lo; --i) answer.push_back(row[i]);
}

static std::string piece5_name(const Piece5& p) {
    std::string s;
    s += p.family ? 'B' : 'A';
    s += char('1' + p.side);
    s += p.reverse ? 'R' : 'F';
    return s;
}

static std::pair<int,int> bounds6(
    const Piece5& p, const std::array<int,2>& acuts, int bcut, int n
) {
    if (!p.family) {
        if (p.side == 0) return {0, acuts[0] + 1};
        if (p.side == 1) return {acuts[0] + 1, acuts[1] + 1};
        return {acuts[1] + 1, n};
    }
    if (p.side == 0) return {0, bcut};
    if (p.side == 1) return {bcut, bcut + 3};
    return {bcut + 3, n};
}

static std::pair<Mask,Mask> endpoints6(
    const Piece5& p, const std::array<int,2>& acuts, int bcut,
    const std::vector<Mask>& a, const std::vector<Mask>& b
) {
    const auto& row=p.family?b:a;
    auto [lo,hi]=bounds6(p,acuts,bcut,row.size());
    Mask first=row[lo],last=row[hi-1];if(p.reverse)std::swap(first,last);
    return {first,last};
}

static void append_piece6(
    std::vector<Mask>& answer, const Piece5& p,
    const std::array<int,2>& acuts, int bcut,
    const std::vector<Mask>& a, const std::vector<Mask>& b
) {
    const auto& row=p.family?b:a;
    auto [lo,hi]=bounds6(p,acuts,bcut,row.size());
    if(!p.reverse)answer.insert(answer.end(),row.begin()+lo,row.begin()+hi);
    else for(int i=hi-1;i>=lo;--i)answer.push_back(row[i]);
}

static std::pair<Mask, Mask> endpoints(
    const Piece& p,
    int acut,
    int bcut,
    const std::vector<Mask>& a,
    const std::vector<Mask>& b
) {
    const auto& row = p.family ? b : a;
    int cut = p.family ? bcut : acut;
    Mask first, last;
    if (p.side == 0) {
        first = row.front();
        last = row[cut - 1];
    } else {
        first = row[cut];
        last = row.back();
    }
    if (p.reverse) std::swap(first, last);
    return {first, last};
}

static void append_piece(
    std::vector<Mask>& answer,
    const Piece& p,
    int acut,
    int bcut,
    const std::vector<Mask>& a,
    const std::vector<Mask>& b
) {
    const auto& row = p.family ? b : a;
    int cut = p.family ? bcut : acut;
    int lo = p.side == 0 ? 0 : cut;
    int hi = p.side == 0 ? cut : int(row.size());
    if (!p.reverse) {
        answer.insert(answer.end(), row.begin() + lo, row.begin() + hi);
    } else {
        for (int i = hi - 1; i >= lo; --i) answer.push_back(row[i]);
    }
}

static bool resident_depth2(const std::vector<Mask>& t) {
    const Mask full = (Mask(1) << 14) - 1;
    std::vector<Mask> p(t.size() + 2, full);
    for (int i = 0; i < int(p.size()); ++i) {
        for (int j = std::max(0, i - 2); j <= std::min(i, int(t.size()) - 1); ++j) {
            p[i] &= t[j];
        }
    }
    for (int i = 0; i < int(t.size()); ++i) {
        if (Mask(p[i] | p[i + 1] | p[i + 2]) != t[i]) return false;
    }
    return true;
}

static std::array<int, 7> upper_holes(const std::vector<Mask>& t) {
    std::array<int, 7> holes{};
    std::vector<Mask> row = t;
    for (int q = 1; q <= 7; ++q) {
        std::vector<Mask> next;
        next.reserve(row.size() - 1);
        std::unordered_set<Mask> seen;
        seen.reserve(row.size() * 2);
        for (int i = 0; i + 1 < int(row.size()); ++i) {
            Mask value = Mask(row[i] | row[i + 1]);
            next.push_back(value);
            seen.insert(value);
        }
        int rank = 7 + q;
        int count = 0;
        for (int value = 1; value < (1 << 14); ++value) {
            if (std::popcount(uint16_t(value)) == rank && !seen.count(Mask(value))) ++count;
        }
        holes[q - 1] = count;
        row.swap(next);
    }
    return holes;
}

// Exact one-target version of sigma_compiler_rank_hall.py for target {x}.
static int singleton_x_candidates(const std::vector<Mask>& t) {
    const Mask full = (Mask(1) << 14) - 1;
    const Mask x = Mask(1) << 13;
    const int n = int(t.size());
    std::vector<Mask> allowed(n + 2, full);
    for (int i = 0; i < n + 2; ++i) {
        for (int j = std::max(0, i - 2); j <= std::min(i, n - 1); ++j) {
            allowed[i] &= t[j];
        }
    }
    // mandatory[lo][width-1] for cells of width 1 or 2.  A coordinate is
    // mandatory precisely when all of its allowed carriers for some middle
    // cell lie in that short cell.
    std::vector<Mask> mandatory1(n + 2, 0), mandatory2(n + 1, 0);
    for (int start = 0; start < n; ++start) {
        for (int bit = 0; bit < 14; ++bit) {
            Mask flag = Mask(1) << bit;
            if (!(t[start] & flag)) continue;
            std::array<int, 3> carriers{};
            int count = 0;
            for (int p = start; p <= start + 2; ++p) {
                if (allowed[p] & flag) carriers[count++] = p;
            }
            if (count == 1) mandatory1[carriers[0]] |= flag;
            if (count == 2 && carriers[1] == carriers[0] + 1) {
                mandatory2[carriers[0]] |= flag;
            }
        }
    }
    int candidates = 0;
    for (int p = 0; p < n + 2; ++p) {
        if ((allowed[p] & x) && !(mandatory1[p] & ~x)) ++candidates;
    }
    for (int p = 0; p < n + 1; ++p) {
        Mask envelope = Mask(allowed[p] | allowed[p + 1]);
        Mask mandatory = Mask(mandatory1[p] | mandatory1[p + 1] | mandatory2[p]);
        if ((envelope & x) && !(mandatory & ~x) &&
            (allowed[p] & x) && (allowed[p + 1] & x)) ++candidates;
    }
    return candidates;
}

static int combined_hall_deficiency(const std::vector<Mask>& t) {
    const Mask full=(Mask(1)<<14)-1;int n=t.size();
    std::vector<Mask> allowed(n+2,full);
    for(int i=0;i<n+2;++i)for(int j=std::max(0,i-2);j<=std::min(i,n-1);++j)allowed[i]&=t[j];
    std::vector<Mask> mandatory1(n+2,0),mandatory2(n+1,0);
    for(int start=0;start<n;++start)for(int bit=0;bit<14;++bit){Mask flag=Mask(1)<<bit;if(!(t[start]&flag))continue;
        std::array<int,3> carriers{};int count=0;for(int p=start;p<=start+2;++p)if(allowed[p]&flag)carriers[count++]=p;
        if(count==1)mandatory1[carriers[0]]|=flag;
        if(count==2&&carriers[1]==carriers[0]+1)mandatory2[carriers[0]]|=flag;
    }
    struct Cell{Mask envelope,mandatory;int p,q;};std::vector<Cell> cells;cells.reserve(2*n+3);
    for(int p=0;p<n+2;++p)cells.push_back({allowed[p],mandatory1[p],p,-1});
    for(int p=0;p<n+1;++p)cells.push_back({Mask(allowed[p]|allowed[p+1]),Mask(mandatory1[p]|mandatory1[p+1]|mandatory2[p]),p,p+1});
    std::vector<std::vector<int>> adj;
    for(int target=1;target<(1<<14);++target){int rank=std::popcount(uint16_t(target));if(rank>6)continue;adj.emplace_back();auto&row=adj.back();
        for(int ci=0;ci<int(cells.size());++ci){auto c=cells[ci];
            if((target&~c.envelope)||(c.mandatory&~target)||!(allowed[c.p]&target)||(c.q>=0&&!(allowed[c.q]&target)))continue;
            row.push_back(ci);
        }
    }
    int L=adj.size(),R=cells.size();std::vector<int> lm(L,-1),rm(R,-1),dist(L);
    auto bfs=[&](){std::vector<int> queue;bool found=false;for(int i=0;i<L;++i){if(lm[i]<0){dist[i]=0;queue.push_back(i);}else dist[i]=-1;}
        for(size_t h=0;h<queue.size();++h){int x=queue[h];for(int y:adj[x]){int z=rm[y];if(z<0)found=true;else if(dist[z]<0){dist[z]=dist[x]+1;queue.push_back(z);}}}return found;};
    auto dfs=[&](auto&&self,int x)->bool{for(int y:adj[x]){int z=rm[y];if(z<0||(dist[z]==dist[x]+1&&self(self,z))){lm[x]=y;rm[y]=x;return true;}}dist[x]=-1;return false;};
    int matching=0;while(bfs())for(int i=0;i<L;++i)if(lm[i]<0&&dfs(dfs,i))++matching;
    return L-matching;
}

static std::string piece_name(const Piece& p) {
    std::string s;
    s += p.family ? 'B' : 'A';
    s += p.side ? '2' : '1';
    s += p.reverse ? 'R' : 'F';
    return s;
}

int main(int argc, char** argv) {
    if (argc < 2) {
        std::cerr << "usage: search_k14_intersection_four_piece CANDIDATE.json [LIMIT]\n";
        return 2;
    }
    int output_limit = argc >= 3 ? std::stoi(argv[2]) : 1000;
    bool five_piece = argc >= 4 && std::string(argv[3]) == "five";
    bool six_piece = argc >= 4 && std::string(argv[3]) == "six";
    auto middle = read_middle_path(argv[1]);
    if (middle.size() != 3432) throw std::runtime_error("expected 3432 middle sets");
    const int half = int(middle.size()) / 2;
    std::vector<Mask> a(middle.begin(), middle.begin() + half);
    std::vector<Mask> b(middle.begin() + half, middle.end());

    if(six_piece){
        std::array<int,1<<14> apos;apos.fill(-1);for(int i=0;i<half;++i)apos[a[i]]=i;
        std::vector<std::array<Piece5,6>> templates6;std::set<std::string> keys;
        std::array<int,3> ap0{0,1,2};
        do{
            std::array<int,3> bp0{0,1,2};
            do{
                for(int start_family=0;start_family<2;++start_family)for(int bits=0;bits<64;++bits){
                    std::array<Piece5,6> row;int ai=0,bi=0;
                    for(int p=0;p<6;++p){int fam=start_family^(p&1);row[p]={fam,fam?bp0[bi++]:ap0[ai++],bool(bits>>p&1)};}
                    std::string fwd,rev;for(auto p:row)fwd+=piece5_name(p)+":";
                    for(int p=5;p>=0;--p){auto z=row[p];z.reverse=!z.reverse;rev+=piece5_name(z)+":";}
                    std::string key=std::min(fwd,rev);if(keys.insert(key).second)templates6.push_back(row);
                }
            }while(std::next_permutation(bp0.begin(),bp0.end()));
        }while(std::next_permutation(ap0.begin(),ap0.end()));
        std::cerr<<"six_templates="<<templates6.size()<<"\n";
        long long endpoint_pass=0,resident_pass=0,resident_x_pass=0,upper_pass=0,hall_pass=0;int emitted=0;
        for(int bcut=1;bcut+3<half;++bcut){
            Mask lost_left=Mask((b[bcut-1]|b[bcut])&~(Mask(1)<<13));
            Mask lost_right=Mask((b[bcut+2]|b[bcut+3])&~(Mask(1)<<13));
            int pa=apos[lost_left],qa=apos[lost_right];if(pa<0||qa<0)continue;
            for(int pside=0;pside<2;++pside)for(int qside=0;qside<2;++qside){
                int pc=pa-(pside?1:0),qc=qa-(qside?1:0);
                if(pc<0||pc>=half-1||qc<0||qc>=half-1||pc==qc)continue;
                std::array<int,2> acuts{std::min(pc,qc),std::max(pc,qc)};
                for(int ti=0;ti<int(templates6.size());++ti){auto const&row=templates6[ti];bool okay=true;
                    for(int p=0;p<5;++p){auto l=endpoints6(row[p],acuts,bcut,a,b),r=endpoints6(row[p+1],acuts,bcut,a,b);if(!adjacent(l.second,r.first)){okay=false;break;}}
                    if(!okay)continue;++endpoint_pass;std::vector<Mask> candidate;candidate.reserve(middle.size());for(auto p:row)append_piece6(candidate,p,acuts,bcut,a,b);
                    if(!resident_depth2(candidate))continue;++resident_pass;int xc=singleton_x_candidates(candidate);if(!xc)continue;++resident_x_pass;
                    auto holes=upper_holes(candidate);if(std::any_of(holes.begin(),holes.end(),[](int h){return h;}))continue;++upper_pass;
                    int deficiency=combined_hall_deficiency(candidate);if(deficiency)continue;++hall_pass;
                    std::cout<<"{\"acuts\":["<<acuts[0]<<','<<acuts[1]<<"],\"bcut\":"<<bcut<<",\"template\":"<<ti<<",\"x_candidates\":"<<xc<<",\"pieces\":[";
                    for(int p=0;p<6;++p){if(p)std::cout<<',';std::cout<<'\"'<<piece5_name(row[p])<<'\"';}std::cout<<"]}\n";
                    if(++emitted>=output_limit)goto done6;
                }
            }
        }
done6:
        std::cerr<<"endpoint_pass="<<endpoint_pass<<" resident_pass="<<resident_pass<<" resident_x_pass="<<resident_x_pass<<" upper_pass="<<upper_pass<<" hall_pass="<<hall_pass<<" emitted="<<emitted<<"\n";
        return emitted?0:1;
    }

    if (five_piece) {
        std::vector<std::array<Piece5, 5>> templates5;
        std::set<std::string> keys;
        std::array<int, 3> bp0{0,1,2};
        do {
            for (int aswap = 0; aswap < 2; ++aswap) {
                std::array<int,2> ap = aswap ? std::array<int,2>{1,0}
                                             : std::array<int,2>{0,1};
                for (int bits = 0; bits < 32; ++bits) {
                    std::array<Piece5,5> row;
                    row[0] = {1,bp0[0],bool(bits&1)};
                    row[1] = {0,ap[0],bool(bits&2)};
                    row[2] = {1,bp0[1],bool(bits&4)};
                    row[3] = {0,ap[1],bool(bits&8)};
                    row[4] = {1,bp0[2],bool(bits&16)};
                    std::string fwd, rev;
                    for (auto p : row) fwd += piece5_name(p) + ":";
                    for (int pos = 4; pos >= 0; --pos) {
                        Piece5 p = row[pos]; p.reverse = !p.reverse;
                        rev += piece5_name(p) + ":";
                    }
                    std::string key = std::min(fwd, rev);
                    if (keys.insert(key).second) templates5.push_back(row);
                }
            }
        } while (std::next_permutation(bp0.begin(), bp0.end()));
        std::cerr << "five_templates=" << templates5.size() << "\n";
        long long endpoint_pass = 0, resident_pass = 0, resident_x_pass = 0,
                  upper_pass = 0, x_pass = 0;
        int emitted = 0;
        for (int acut = 1; acut < half; ++acut) {
            for (int bcut = 1; bcut + 3 < half; ++bcut) {
                for (int ti = 0; ti < int(templates5.size()); ++ti) {
                    const auto& row = templates5[ti];
                    bool okay = true;
                    for (int p = 0; p < 4; ++p) {
                        auto left = endpoints5(row[p], acut, bcut, a, b);
                        auto right = endpoints5(row[p+1], acut, bcut, a, b);
                        if (!adjacent(left.second, right.first)) { okay=false; break; }
                    }
                    if (!okay) continue;
                    ++endpoint_pass;
                    std::vector<Mask> candidate;
                    candidate.reserve(middle.size());
                    for (auto p : row) append_piece5(candidate,p,acut,bcut,a,b);
                    if (!resident_depth2(candidate)) continue;
                    ++resident_pass;
                    int xcandidates = singleton_x_candidates(candidate);
                    if (xcandidates) ++resident_x_pass;
                    auto holes = upper_holes(candidate);
                    if (xcandidates) {
                        std::cerr << "resident_x_candidate acut=" << acut
                                  << " bcut=" << bcut << " template=" << ti
                                  << " x=" << xcandidates << " holes=";
                        for (int h : holes) std::cerr << h << ',';
                        std::cerr << " pieces=";
                        for (auto p : row) std::cerr << piece5_name(p) << ':';
                        std::cerr << "\n";
                    }
                    if (std::any_of(holes.begin(),holes.end(),[](int h){return h;})) continue;
                    ++upper_pass;
                    if (!xcandidates) continue;
                    ++x_pass;
                    std::cout << "{\"acut\":" << acut
                              << ",\"bcut\":" << bcut
                              << ",\"template\":" << ti
                              << ",\"x_candidates\":" << xcandidates
                              << ",\"pieces\":[";
                    for (int p=0;p<5;++p) {
                        if (p) std::cout << ',';
                        std::cout << '\"' << piece5_name(row[p]) << '\"';
                    }
                    std::cout << "]}\n";
                    if (++emitted >= output_limit) goto done5;
                }
            }
        }
done5:
        std::cerr << "endpoint_pass=" << endpoint_pass
                  << " resident_pass=" << resident_pass
                  << " resident_x_pass=" << resident_x_pass
                  << " upper_pass=" << upper_pass
                  << " singleton_x_pass=" << x_pass
                  << " emitted=" << emitted << "\n";
        return 0;
    }

    std::vector<std::array<Piece, 4>> templates;
    // Alternate families.  Enumerate piece order and all orientations; retain
    // one representative of a path/reversal pair by lexicographic encoding.
    std::set<std::string> template_keys;
    for (int start_family = 0; start_family < 2; ++start_family) {
        for (int aswap = 0; aswap < 2; ++aswap) {
            for (int bswap = 0; bswap < 2; ++bswap) {
                std::array<int, 2> ai = aswap ? std::array<int,2>{1,0} : std::array<int,2>{0,1};
                std::array<int, 2> bi = bswap ? std::array<int,2>{1,0} : std::array<int,2>{0,1};
                for (int bits = 0; bits < 16; ++bits) {
                    std::array<Piece, 4> row;
                    int ap = 0, bp = 0;
                    for (int pos = 0; pos < 4; ++pos) {
                        int family = start_family ^ (pos & 1);
                        int side = family ? bi[bp++] : ai[ap++];
                        row[pos] = Piece{family, side, bool(bits >> pos & 1)};
                    }
                    std::string forward, backward;
                    for (auto p : row) forward += piece_name(p) + ":";
                    for (int pos = 3; pos >= 0; --pos) {
                        Piece p = row[pos]; p.reverse = !p.reverse;
                        backward += piece_name(p) + ":";
                    }
                    std::string key = std::min(forward, backward);
                    if (template_keys.insert(key).second) templates.push_back(row);
                }
            }
        }
    }
    std::cerr << "templates=" << templates.size() << "\n";

    long long endpoint_pass = 0, resident_pass = 0, resident_x_pass = 0,
              upper_pass = 0, x_pass = 0;
    int emitted = 0;
    for (int acut = 1; acut < half; ++acut) {
        for (int bcut = 1; bcut < half; ++bcut) {
            for (int ti = 0; ti < int(templates.size()); ++ti) {
                const auto& row = templates[ti];
                bool okay = true;
                for (int p = 0; p < 3; ++p) {
                    auto left = endpoints(row[p], acut, bcut, a, b);
                    auto right = endpoints(row[p + 1], acut, bcut, a, b);
                    if (!adjacent(left.second, right.first)) { okay = false; break; }
                }
                if (!okay) continue;
                ++endpoint_pass;
                std::vector<Mask> candidate;
                candidate.reserve(middle.size());
                for (const auto& piece : row) append_piece(candidate, piece, acut, bcut, a, b);
                if (!resident_depth2(candidate)) continue;
                ++resident_pass;
                int xcandidates = singleton_x_candidates(candidate);
                if (xcandidates) ++resident_x_pass;
                auto holes = upper_holes(candidate);
                if (std::any_of(holes.begin(), holes.end(), [](int h){ return h != 0; })) continue;
                ++upper_pass;
                if (!xcandidates) continue;
                ++x_pass;
                std::cout << "{\"acut\":" << acut
                          << ",\"bcut\":" << bcut
                          << ",\"template\":" << ti
                          << ",\"x_candidates\":" << xcandidates
                          << ",\"pieces\":[";
                for (int p = 0; p < 4; ++p) {
                    if (p) std::cout << ',';
                    std::cout << '\"' << piece_name(row[p]) << '\"';
                }
                std::cout << "]}\n";
                if (++emitted >= output_limit) goto done;
            }
        }
    }
done:
    std::cerr << "endpoint_pass=" << endpoint_pass
              << " resident_pass=" << resident_pass
              << " resident_x_pass=" << resident_x_pass
              << " upper_pass=" << upper_pass
              << " singleton_x_pass=" << x_pass
              << " emitted=" << emitted << "\n";
    return 0;
}
