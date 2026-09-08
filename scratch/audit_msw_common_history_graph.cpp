#include <algorithm>
#include <bit>
#include <cassert>
#include <cstdint>
#include <functional>
#include <iostream>
#include <numeric>
#include <string>
#include <unordered_set>
#include <utility>
#include <vector>

// Exact finite audit of the length-d common-history relation among the tight
// MSW owner cycles.  Run remotely on h100.

using U = std::uint32_t;

static std::pair<U, int> g(U x, int m) {
    std::vector<int> before(2 * m);
    int height = 0, d0 = 0;
    for (int i = 0; i < 2 * m; ++i) {
        before[i] = height;
        if (((x >> i) & 1U) == 0 && height == 0) ++d0;
        height += ((x >> i) & 1U) ? 1 : -1;
    }
    int seen = 0;
    for (int i = 0; i < 2 * m; ++i)
        if (((x >> i) & 1U) == 0 &&
            (before[i] == 0 || before[i] == 1) && ++seen == d0 + 1)
            return {x | (U{1} << i), i};
    assert(false); return {};
}

static std::pair<U, int> hmap(U y, int m) {
    std::vector<int> before(2 * m);
    int height = 0, u1 = 0;
    for (int i = 0; i < 2 * m; ++i) {
        before[i] = height;
        if (((y >> i) & 1U) != 0 && height == 1) ++u1;
        height += ((y >> i) & 1U) ? 1 : -1;
    }
    int seen = 0;
    for (int i = 0; i < 2 * m; ++i)
        if (((y >> i) & 1U) != 0 &&
            (before[i] == 0 || before[i] == 1) && ++seen == u1)
            return {y & ~(U{1} << i), i};
    assert(false); return {};
}

static long long choose(int n, int r) {
    if (r < 0 || r > n) return 0;
    long long ans = 1;
    for (int i = 1; i <= r; ++i) ans = ans * (n-r+i) / i;
    return ans;
}

static int area_stat(U x, int m) {
    int h=0,a=0;
    for(int i=0;i<2*m;++i){h+=((x>>i)&1U)?1:-1;a+=h;}
    return a;
}

struct State {
    std::vector<U> maximal;
    std::vector<U> forced;
};

static bool compatible(const State& a, const State& b) {
    assert(a.maximal.size() == b.maximal.size());
    for (std::size_t j = 0; j < a.maximal.size(); ++j)
        if ((a.forced[j] | b.forced[j]) & ~(a.maximal[j] & b.maximal[j]))
            return false;
    return true;
}

static bool exact_history(const State& a, const State& b) {
    return a.maximal == b.maximal;
}

static bool same_forced_history(const State& a, const State& b) {
    return a.forced == b.forced;
}

static std::vector<U> rp_order(int m) {
    const int ambient=m+1, length=2*ambient;
    std::vector<unsigned char> bits(length); bits[0]=1; bits[1]=0;
    std::vector<U> out;
    std::function<void(int,int,int,bool)> rec=[&](int n,int k,int pos,bool dir){
        if(k==0||k==n){
            U x=0; for(int i=2;i<length;++i) if(bits[i]) x|=U{1}<<(i-2);
            out.push_back(x); return;
        }
        if(k==1){bits[pos]=1;rec(n,k+1,pos+1,dir);bits[pos]=0;return;}
        if(dir){
            bits[pos]=1;rec(n,k+1,pos+1,false);bits[pos]=0;
            rec(n-1,k-1,pos+1,true);
        }else{
            rec(n-1,k-1,pos+1,false);
            bits[pos]=1;rec(n,k+1,pos+1,true);bits[pos]=0;
        }
    };
    rec(ambient,1,2,true); return out;
}

int main(int argc, char** argv) {
    int max_m = argc > 1 ? std::stoi(argv[1]) : 8;
    for (int m = 2; m <= max_m; ++m) {
        const int R = m + 1, n = 2*m + 1;
        assert(n < 31);
        std::vector<std::vector<int>> rows;
        std::vector<U> roots;
        std::function<void(int,int,int,U)> gen = [&](int pos,int up,int down,U mask) {
            if (pos == 2*m) {
                U x = mask;
                std::vector<int> omitted;
                for (int e = 0; e < m; ++e) {
                    auto a = g(x,m); auto b = hmap(a.first,m);
                    omitted.push_back(a.second); omitted.push_back(b.second);
                    x = b.first;
                }
                omitted.push_back(2*m);
                std::vector<int> tight(n);
                for (int j=0;j<n;++j) tight[j]=omitted[(2*j)%n];
                rows.push_back(std::move(tight));
                roots.push_back(mask);
                return;
            }
            if (up<m) gen(pos+1,up+1,down,mask|(U{1}<<pos));
            if (down<up) gen(pos+1,up,down+1,mask);
        };
        gen(0,0,0,0);
        std::vector<std::vector<int>> flip_words(rows.size(),
                                                 std::vector<int>(n));
        for(int c=0;c<(int)rows.size();++c)
            for(int j=0;j<n;++j) flip_words[c][(2*j)%n]=rows[c][j];

        long long W=choose(n,R), half=1LL<<(n-1);
        int d=0; while (1LL*d*W+1LL*d*(d+1)/2<half) ++d;
        const int s=R-d;
        assert(s>0);

        std::vector<std::vector<State>> states(rows.size());
        for (std::size_t c=0;c<rows.size();++c) {
            for (int orientation=0;orientation<2;++orientation) {
                std::vector<int> order=rows[c];
                if (orientation) std::reverse(order.begin(),order.end());
                for (int shift=0;shift<n;++shift) {
                    State st;
                    for (int j=0;j<d;++j) {
                        int start=(shift+j)%n;
                        U p=0;
                        for (int z=0;z<s;++z) p|=U{1}<<order[(start+z)%n];
                        U f=(U{1}<<order[start]) |
                            (U{1}<<order[(start+s-1)%n]);
                        st.maximal.push_back(p); st.forced.push_back(f);
                    }
                    states[c].push_back(std::move(st));
                }
            }
        }

        std::vector<std::vector<int>> graph(rows.size());
        std::vector<std::vector<int>> transposition_graph(rows.size());
        std::vector<std::vector<int>> adjacent_graph(rows.size());
        long long compatible_pairs=0, compatible_state_pairs=0;
        long long transposition_pairs=0;
        long long compatible_adjacent_pairs=0;
        std::vector<long long> root_distance_hist(m+1);
        const auto pair_compatible = [&](int a, int b) {
            for (const State& x : states[a])
                for (const State& y : states[b])
                    if (compatible(x, y)) return true;
            return false;
        };
        const auto pair_exact = [&](int a, int b) {
            for (const State& x : states[a])
                for (const State& y : states[b])
                    if (exact_history(x, y)) return true;
            return false;
        };
        const auto pair_same_forced = [&](int a, int b) {
            for (const State& x : states[a])
                for (const State& y : states[b])
                    if (same_forced_history(x, y) && compatible(x, y)) return true;
            return false;
        };
        const auto pair_same_forced_orient = [&](int a, int b, int oa, int ob) {
            for (int sa=0; sa<n; ++sa)
                for (int sb=0; sb<n; ++sb) {
                    const State& x=states[a][oa*n+sa];
                    const State& y=states[b][ob*n+sb];
                    if (same_forced_history(x,y) && compatible(x,y)) return true;
                }
            return false;
        };
        const auto pair_same_ordered_rails = [&](int a,int b) {
            for(int sa=0;sa<n;++sa) for(int sb=0;sb<n;++sb) {
                bool direct=true,cross=true;
                for(int j=0;j<d;++j) {
                    int xa=rows[a][(sa+j)%n];
                    int xb=rows[a][(sa+s-1+j)%n];
                    int ya=rows[b][(sb+j)%n];
                    int yb=rows[b][(sb+s-1+j)%n];
                    direct &= xa==ya && xb==yb;
                    cross &= xa==yb && xb==ya;
                }
                if(direct || cross) return true;
            }
            return false;
        };

        // For larger cases, audit the full Catalan transposition graph rather
        // than all root pairs.  This is the natural sparse candidate for a
        // symbolic connectivity proof.
        if (rows.size() > 1000) {
            std::vector<int> root_index(1U << (2*m), -1);
            for (int i=0;i<(int)roots.size();++i) root_index[roots[i]]=i;
            std::vector<std::vector<int>> sparse(rows.size());
            std::vector<std::vector<int>> adjacent(rows.size());
            long long total_transpositions=0,compatible_transpositions=0;
            long long exact_transpositions=0;
            std::vector<std::vector<int>> exact(rows.size());
            long long same_forced_transpositions=0;
            std::vector<std::vector<int>> same_forced(rows.size());
            long long same_forced_00_transpositions=0;
            std::vector<std::vector<int>> same_forced_00(rows.size());
            long long same_ordered_rail_transpositions=0;
            std::vector<std::vector<int>> same_ordered_rail(rows.size());
            std::vector<std::vector<int>> same_forced_directed_higher(rows.size());
            std::vector<int> same_forced_lower(rows.size());
            long long same_forced_adjacent=0;
            std::vector<std::vector<int>> same_forced_adjacent_graph(rows.size());
            std::vector<int> same_forced_adjacent_lower(rows.size());
            std::vector<int> same_forced_higher(rows.size());
            std::vector<int> same_forced_long_higher(rows.size());
            std::vector<int> shortest_higher_gap(rows.size(),1<<20);
            std::vector<std::pair<int,int>> shortest_higher_positions(
                rows.size(),{-1,-1});
            std::vector<int> minimum_q_change_cover(rows.size(),1<<20);
            std::vector<std::vector<std::pair<int,int>>> same_forced_higher_moves(
                rows.size());
            long long compatible_adjacent=0;
            std::vector<int> compatible_lower(rows.size()), compatible_adjacent_lower(rows.size());
            long long extreme_total=0,extreme_compatible=0;
            std::vector<int> extreme_bad_examples;
            std::vector<std::string> extreme_good_examples;
            for(int a=0;a<(int)roots.size();++a) {
                U x=roots[a];
                for(int p=0;p<2*m;++p) if((x>>p)&1U)
                for(int q=0;q<2*m;++q) if(((x>>q)&1U)==0) {
                    U y=x^(U{1}<<p)^(U{1}<<q);
                    int b=root_index[y];
                    if(b<=a) continue;
                    ++total_transpositions;
                    if(pair_compatible(a,b)) {
                        ++compatible_transpositions;
                        sparse[a].push_back(b); sparse[b].push_back(a);
                        int lo=std::min(p,q),hi=std::max(p,q);
                        if(hi-lo==1) {
                            ++compatible_adjacent;
                            adjacent[a].push_back(b); adjacent[b].push_back(a);
                        }
                        int aa=area_stat(roots[a],m),ab=area_stat(roots[b],m);
                        if(aa>ab) ++compatible_lower[a];
                        if(ab>aa) ++compatible_lower[b];
                        if(hi-lo==1){
                            if(aa>ab) ++compatible_adjacent_lower[a];
                            if(ab>aa) ++compatible_adjacent_lower[b];
                        }
                    }
                    if(pair_exact(a,b)) {
                        ++exact_transpositions;
                        exact[a].push_back(b); exact[b].push_back(a);
                    }
                    if(pair_same_forced(a,b)) {
                        ++same_forced_transpositions;
                        same_forced[a].push_back(b); same_forced[b].push_back(a);
                        int aa=area_stat(roots[a],m),ab=area_stat(roots[b],m);
                        int sf_lo=std::min(p,q),sf_hi=std::max(p,q);
                        if(aa>ab) ++same_forced_lower[a];
                        if(ab>aa) ++same_forced_lower[b];
                        if(aa<ab) ++same_forced_higher[a];
                        if(ab<aa) ++same_forced_higher[b];
                        if(aa<ab) same_forced_directed_higher[a].push_back(b);
                        if(ab<aa) same_forced_directed_higher[b].push_back(a);
                        if(aa<ab) same_forced_higher_moves[a].push_back({sf_lo,sf_hi});
                        if(ab<aa) same_forced_higher_moves[b].push_back({sf_lo,sf_hi});
                        std::vector<int> changed;
                        for(int z=0;z<n;++z)
                            if(flip_words[a][z]!=flip_words[b][z]) changed.push_back(z);
                        assert(!changed.empty());
                        int maximum_gap=0;
                        for(int z=0;z<(int)changed.size();++z) {
                            int next=changed[(z+1)%changed.size()];
                            if(z+1==(int)changed.size()) next+=n;
                            maximum_gap=std::max(maximum_gap,next-changed[z]);
                        }
                        int change_cover=n-maximum_gap+1;
                        if(aa<ab) minimum_q_change_cover[a]=std::min(
                            minimum_q_change_cover[a],change_cover);
                        if(ab<aa) minimum_q_change_cover[b]=std::min(
                            minimum_q_change_cover[b],change_cover);
                        if(aa<ab && sf_hi-sf_lo<shortest_higher_gap[a]) {
                            shortest_higher_gap[a]=sf_hi-sf_lo;
                            shortest_higher_positions[a]={sf_lo,sf_hi};
                        }
                        if(ab<aa && sf_hi-sf_lo<shortest_higher_gap[b]) {
                            shortest_higher_gap[b]=sf_hi-sf_lo;
                            shortest_higher_positions[b]={sf_lo,sf_hi};
                        }
                        if(aa<ab && sf_hi-sf_lo>=2*d+1) ++same_forced_long_higher[a];
                        if(ab<aa && sf_hi-sf_lo>=2*d+1) ++same_forced_long_higher[b];
                        int lo=sf_lo,hi=sf_hi;
                        if(hi-lo==1) {
                            ++same_forced_adjacent;
                            same_forced_adjacent_graph[a].push_back(b);
                            same_forced_adjacent_graph[b].push_back(a);
                            if(aa>ab) ++same_forced_adjacent_lower[a];
                            if(ab>aa) ++same_forced_adjacent_lower[b];
                        }
                        if(pair_same_forced_orient(a,b,0,0)) {
                            ++same_forced_00_transpositions;
                            same_forced_00[a].push_back(b);
                            same_forced_00[b].push_back(a);
                        }
                        if(pair_same_ordered_rails(a,b)) {
                            ++same_ordered_rail_transpositions;
                            same_ordered_rail[a].push_back(b);
                            same_ordered_rail[b].push_back(a);
                        }
                    }
                }
            }
            for(int a=0;a<(int)roots.size();++a) {
                U x=roots[a]; int first_zero=-1,last_one=-1;
                for(int p=0;p<2*m;++p) if(((x>>p)&1U)==0){first_zero=p;break;}
                for(int p=2*m-1;p>=0;--p) if((x>>p)&1U){last_one=p;break;}
                if(first_zero<last_one) {
                    U y=x^(U{1}<<first_zero)^(U{1}<<last_one);
                    int b=root_index[y]; assert(b>=0); ++extreme_total;
                    if(pair_compatible(a,b)) {
                        ++extreme_compatible;
                        if(extreme_good_examples.size()<8) {
                            int si=-1,sj=-1;
                            for(int i=0;i<(int)states[a].size()&&si<0;++i)
                            for(int j=0;j<(int)states[b].size();++j)
                                if(compatible(states[a][i],states[b][j])){si=i;sj=j;break;}
                            std::string ex;
                            auto add_word=[&](U z){for(int t=0;t<2*m;++t)ex.push_back(((z>>t)&1U)?'1':'0');};
                            add_word(x);ex.push_back('>');add_word(y);
                            ex += "@"+std::to_string(si/n)+":"+std::to_string(si%n)
                                +","+std::to_string(sj/n)+":"+std::to_string(sj%n);
                            extreme_good_examples.push_back(ex);
                        }
                    }
                    else if(extreme_bad_examples.size()<12) extreme_bad_examples.push_back(a);
                }
            }
            std::vector<int> seen(rows.size());
            int components=0,active=0,min_degree=-1,max_degree=0;
            for(int i=0;i<(int)rows.size();++i) {
                if(!sparse[i].empty()) {
                    ++active;
                    min_degree=min_degree<0?(int)sparse[i].size():std::min(min_degree,(int)sparse[i].size());
                    max_degree=std::max(max_degree,(int)sparse[i].size());
                }
                if(seen[i]) continue;
                ++components; seen[i]=1; std::vector<int> stack{i};
                while(!stack.empty()) {int z=stack.back();stack.pop_back();
                    for(int w:sparse[z]) if(!seen[w]){seen[w]=1;stack.push_back(w);}}
            }
            std::cout<<"m="<<m<<" R="<<R<<" d="<<d<<" q="<<d+1
                     <<" roots="<<rows.size()<<" sparse_only=1 total_transpositions="
                     <<total_transpositions<<" compatible_transpositions="
                     <<compatible_transpositions<<" components="<<components
                     <<" active="<<active<<" degree_min="<<min_degree
                     <<" degree_max="<<max_degree;
            int no_lower=0,no_adjacent_lower=0;
            int min_lower=-1,min_adjacent_lower=-1;
            int minimum_area=*std::min_element(roots.begin(),roots.end(),[&](U x,U y){return area_stat(x,m)<area_stat(y,m);});
            for(int i=0;i<(int)rows.size();++i) if(roots[i]!=minimum_area){
                if(!compatible_lower[i])++no_lower;
                else min_lower=min_lower<0?compatible_lower[i]:std::min(min_lower,compatible_lower[i]);
                if(!compatible_adjacent_lower[i])++no_adjacent_lower;
                else min_adjacent_lower=min_adjacent_lower<0?compatible_adjacent_lower[i]:std::min(min_adjacent_lower,compatible_adjacent_lower[i]);
            }
            std::fill(seen.begin(),seen.end(),0);
            int acomp=0,aactive=0,amin=-1,amax=0;
            for(int i=0;i<(int)rows.size();++i){
                if(!adjacent[i].empty()){
                    ++aactive;amin=amin<0?(int)adjacent[i].size():std::min(amin,(int)adjacent[i].size());
                    amax=std::max(amax,(int)adjacent[i].size());}
                if(seen[i])continue;++acomp;seen[i]=1;std::vector<int> stack{i};
                while(!stack.empty()){int z=stack.back();stack.pop_back();for(int w:adjacent[z])if(!seen[w]){seen[w]=1;stack.push_back(w);}}
            }
            std::fill(seen.begin(),seen.end(),0);
            int sfcomp=0,sfactive=0,sfmin=-1,sfmax=0;
            for(int i=0;i<(int)rows.size();++i){
                if(!same_forced[i].empty()){
                    ++sfactive;sfmin=sfmin<0?(int)same_forced[i].size():std::min(sfmin,(int)same_forced[i].size());
                    sfmax=std::max(sfmax,(int)same_forced[i].size());}
                if(seen[i])continue;++sfcomp;seen[i]=1;std::vector<int> stack{i};
                while(!stack.empty()){int z=stack.back();stack.pop_back();for(int w:same_forced[z])if(!seen[w]){seen[w]=1;stack.push_back(w);}}
            }
            std::fill(seen.begin(),seen.end(),0);
            int sfa_comp=0,sfa_active=0,sfa_min=-1,sfa_max=0;
            for(int i=0;i<(int)rows.size();++i){
                if(!same_forced_adjacent_graph[i].empty()){
                    ++sfa_active;sfa_min=sfa_min<0?(int)same_forced_adjacent_graph[i].size():std::min(sfa_min,(int)same_forced_adjacent_graph[i].size());
                    sfa_max=std::max(sfa_max,(int)same_forced_adjacent_graph[i].size());}
                if(seen[i])continue;++sfa_comp;seen[i]=1;std::vector<int> stack{i};
                while(!stack.empty()){int z=stack.back();stack.pop_back();for(int w:same_forced_adjacent_graph[z])if(!seen[w]){seen[w]=1;stack.push_back(w);}}
            }
            std::fill(seen.begin(),seen.end(),0);
            int sf00_comp=0,sf00_active=0,sf00_min=-1,sf00_max=0;
            for(int i=0;i<(int)rows.size();++i){
                if(!same_forced_00[i].empty()){
                    ++sf00_active;sf00_min=sf00_min<0?(int)same_forced_00[i].size():std::min(sf00_min,(int)same_forced_00[i].size());
                    sf00_max=std::max(sf00_max,(int)same_forced_00[i].size());}
                if(seen[i])continue;++sf00_comp;seen[i]=1;std::vector<int> stack{i};
                while(!stack.empty()){int z=stack.back();stack.pop_back();for(int w:same_forced_00[z])if(!seen[w]){seen[w]=1;stack.push_back(w);}}
            }
            std::fill(seen.begin(),seen.end(),0);
            int rail_comp=0,rail_active=0,rail_min=-1,rail_max=0;
            for(int i=0;i<(int)rows.size();++i){
                if(!same_ordered_rail[i].empty()){
                    ++rail_active;rail_min=rail_min<0?(int)same_ordered_rail[i].size():std::min(rail_min,(int)same_ordered_rail[i].size());
                    rail_max=std::max(rail_max,(int)same_ordered_rail[i].size());}
                if(seen[i])continue;++rail_comp;seen[i]=1;std::vector<int> stack{i};
                while(!stack.empty()){int z=stack.back();stack.pop_back();for(int w:same_ordered_rail[z])if(!seen[w]){seen[w]=1;stack.push_back(w);}}
            }
            int sf_no_lower=0,sfa_no_lower=0,sf_min_lower=-1,sfa_min_lower=-1;
            int sf_no_higher=0,sf_min_higher=-1,sf_no_long_higher=0,
                sf_min_long_higher=-1;
            int maximum_area=*std::max_element(roots.begin(),roots.end(),[&](U x,U y){return area_stat(x,m)<area_stat(y,m);});
            for(int i=0;i<(int)rows.size();++i) {
              if(roots[i]!=minimum_area){
                if(!same_forced_lower[i]) ++sf_no_lower;
                else sf_min_lower=sf_min_lower<0?same_forced_lower[i]:std::min(sf_min_lower,same_forced_lower[i]);
                if(!same_forced_adjacent_lower[i]) ++sfa_no_lower;
                else sfa_min_lower=sfa_min_lower<0?same_forced_adjacent_lower[i]:std::min(sfa_min_lower,same_forced_adjacent_lower[i]);
              }
              if(roots[i]!=maximum_area){
                if(!same_forced_higher[i]) ++sf_no_higher;
                else sf_min_higher=sf_min_higher<0?same_forced_higher[i]:std::min(sf_min_higher,same_forced_higher[i]);
                if(!same_forced_long_higher[i]) ++sf_no_long_higher;
                else sf_min_long_higher=sf_min_long_higher<0?same_forced_long_higher[i]:std::min(sf_min_long_higher,same_forced_long_higher[i]);
              }
            }
            // Greedy parent selection toward increasing area, preferring a
            // parent with the smallest current child load.  This measures
            // whether the monotone DAG plausibly has a bounded-degree
            // spanning arborescence; it is not a proof of optimality.
            std::vector<int> child_load(rows.size()), parent(rows.size(),-1);
            std::vector<int> order_index(rows.size());
            std::iota(order_index.begin(),order_index.end(),0);
            std::sort(order_index.begin(),order_index.end(),[&](int a,int b){
                return area_stat(roots[a],m)>area_stat(roots[b],m);
            });
            int orphan=0;
            for(int vertex:order_index) if(roots[vertex]!=maximum_area) {
                int best=-1;
                for(int candidate:same_forced_directed_higher[vertex])
                    if(best<0 || child_load[candidate]<child_load[best]) best=candidate;
                if(best<0) ++orphan;
                else {parent[vertex]=best;++child_load[best];}
            }
            int greedy_max_children=*std::max_element(child_load.begin(),child_load.end());
            auto has_move=[&](int vertex,int p,int q){
                return std::find(same_forced_higher_moves[vertex].begin(),
                                 same_forced_higher_moves[vertex].end(),
                                 std::pair<int,int>{p,q})!=
                       same_forced_higher_moves[vertex].end();
            };
            auto valley_neighbourhood_good=[&](int vertex,int v){
                U x=roots[vertex];
                if(v<0 || v+1>=2*m || ((x>>v)&3U)!=2U) return false;
                if(has_move(vertex,v,v+1)) return true;
                bool left=v>0 && (((x>>(v-1))&1U)==0);
                bool right=v+2<2*m && (((x>>(v+2))&1U)!=0);
                return (left && has_move(vertex,v-1,v+1)) ||
                       (right && has_move(vertex,v,v+2)) ||
                       (left && right && has_move(vertex,v-1,v+2));
            };
            int no_leftmost_valley_packet=0,no_rightmost_valley_packet=0,
                no_any_valley_packet=0;
            int no_low_left_valley_packet=0,no_low_right_valley_packet=0,
                no_high_left_valley_packet=0,no_high_right_valley_packet=0,
                no_short_next_left_packet=0,no_short_next_right_packet=0,
                no_high_left_outer_move=0,no_high_right_outer_move=0,
                no_high_left_leftbiased_move=0,no_high_right_leftbiased_move=0,
                no_high_left_rightbiased_move=0,no_high_right_rightbiased_move=0;
            std::vector<std::string> high_outer_exceptions;
            for(int vertex=0;vertex<(int)rows.size();++vertex)
                if(roots[vertex]!=maximum_area) {
                    int leftmost=-1,rightmost=-1;
                    int low_left=-1,low_right=-1,high_left=-1,high_right=-1;
                    int low_height=1<<20,high_height=-1;
                    int short_next_left=-1,short_next_right=-1,short_next=1<<20;
                    int root_height=0;
                    std::vector<int> height_before(2*m+1);
                    for(int z=0;z<2*m;++z) {
                        height_before[z]=root_height;
                        root_height+=((roots[vertex]>>z)&1U)?1:-1;
                    }
                    for(int v=0;v+1<2*m;++v)
                        if(((roots[vertex]>>v)&3U)==2U) {
                            if(leftmost<0) leftmost=v;
                            rightmost=v;
                            int h=height_before[v];
                            if(h<low_height){low_height=h;low_left=low_right=v;}
                            else if(h==low_height)low_right=v;
                            if(h>high_height){high_height=h;high_left=high_right=v;}
                            else if(h==high_height)high_right=v;
                            int target=height_before[v+1],z=v+2;
                            while(z<2*m && height_before[z]!=target)++z;
                            int span=z-(v+1);
                            if(span<short_next){short_next=span;short_next_left=short_next_right=v;}
                            else if(span==short_next)short_next_right=v;
                        }
                    if(!valley_neighbourhood_good(vertex,leftmost))
                        ++no_leftmost_valley_packet;
                    if(!valley_neighbourhood_good(vertex,rightmost))
                        ++no_rightmost_valley_packet;
                    bool any=false;
                    for(int v=leftmost;v<=rightmost && !any;++v)
                        any=valley_neighbourhood_good(vertex,v);
                    if(!any) ++no_any_valley_packet;
                    if(!valley_neighbourhood_good(vertex,low_left))
                        ++no_low_left_valley_packet;
                    if(!valley_neighbourhood_good(vertex,low_right))
                        ++no_low_right_valley_packet;
                    if(!valley_neighbourhood_good(vertex,high_left))
                        ++no_high_left_valley_packet;
                    if(!valley_neighbourhood_good(vertex,high_right))
                        ++no_high_right_valley_packet;
                    auto outer_move_good=[&](int v){
                        int p=(v>0 && (((roots[vertex]>>(v-1))&1U)==0))?v-1:v;
                        int q=(v+2<2*m && (((roots[vertex]>>(v+2))&1U)!=0))?v+2:v+1;
                        return has_move(vertex,p,q);
                    };
                    if(!outer_move_good(high_left)) {
                        ++no_high_left_outer_move;
                        if(high_outer_exceptions.size()<20) {
                            std::string out;
                            for(int z=0;z<2*m;++z) out.push_back(((roots[vertex]>>z)&1U)?'1':'0');
                            out += "@v="+std::to_string(high_left)+" moves=";
                            for(auto [p,q]:same_forced_higher_moves[vertex])
                                if(p>=high_left-1 && q<=high_left+2)
                                    out += std::to_string(p)+"-"+std::to_string(q)+",";
                            high_outer_exceptions.push_back(out);
                        }
                    }
                    if(!outer_move_good(high_right)) ++no_high_right_outer_move;
                    auto biased_move_good=[&](int v,bool left_bias){
                        bool left=v>0 && (((roots[vertex]>>(v-1))&1U)==0);
                        bool right=v+2<2*m && (((roots[vertex]>>(v+2))&1U)!=0);
                        int p=v,q=v+1;
                        if(left && (!right || left_bias)) p=v-1;
                        else if(right) q=v+2;
                        return has_move(vertex,p,q);
                    };
                    if(!biased_move_good(high_left,true))
                        ++no_high_left_leftbiased_move;
                    if(!biased_move_good(high_right,true))
                        ++no_high_right_leftbiased_move;
                    if(!biased_move_good(high_left,false))
                        ++no_high_left_rightbiased_move;
                    if(!biased_move_good(high_right,false))
                        ++no_high_right_rightbiased_move;
                    if(!valley_neighbourhood_good(vertex,short_next_left))
                        ++no_short_next_left_packet;
                    if(!valley_neighbourhood_good(vertex,short_next_right))
                        ++no_short_next_right_packet;
                }
            int no_small_q_change_cover=0,max_minimum_q_change_cover=0;
            const int q_change_cover_bound=n-4*d;
            for(int vertex=0;vertex<(int)rows.size();++vertex)
                if(roots[vertex]!=maximum_area) {
                    if(minimum_q_change_cover[vertex]>q_change_cover_bound)
                        ++no_small_q_change_cover;
                    if(minimum_q_change_cover[vertex]<(1<<20))
                        max_minimum_q_change_cover=std::max(
                            max_minimum_q_change_cover,
                            minimum_q_change_cover[vertex]);
                }
            std::fill(seen.begin(),seen.end(),0);
            int ecomp=0,eactive=0,emin=-1,emax=0;
            for(int i=0;i<(int)rows.size();++i){
                if(!exact[i].empty()){
                    ++eactive;emin=emin<0?(int)exact[i].size():std::min(emin,(int)exact[i].size());
                    emax=std::max(emax,(int)exact[i].size());}
                if(seen[i])continue;++ecomp;seen[i]=1;std::vector<int> stack{i};
                while(!stack.empty()){int z=stack.back();stack.pop_back();for(int w:exact[z])if(!seen[w]){seen[w]=1;stack.push_back(w);}}
            }
            std::cout<<" compatible_adjacent="<<compatible_adjacent
                     <<" adjacent_components="<<acomp<<" adjacent_active="<<aactive
                     <<" adjacent_degree_min="<<amin<<" adjacent_degree_max="<<amax
                     <<" exact_transpositions="<<exact_transpositions
                     <<" exact_components="<<ecomp<<" exact_active="<<eactive
                     <<" exact_degree_min="<<emin<<" exact_degree_max="<<emax
                     <<" same_forced_transpositions="<<same_forced_transpositions
                     <<" same_forced_components="<<sfcomp
                     <<" same_forced_active="<<sfactive
                     <<" same_forced_degree_min="<<sfmin
                     <<" same_forced_degree_max="<<sfmax
                     <<" same_forced_00_transpositions="<<same_forced_00_transpositions
                     <<" same_forced_00_components="<<sf00_comp
                     <<" same_forced_00_active="<<sf00_active
                     <<" same_forced_00_degree_min="<<sf00_min
                     <<" same_forced_00_degree_max="<<sf00_max
                     <<" same_ordered_rail_transpositions="<<same_ordered_rail_transpositions
                     <<" same_ordered_rail_components="<<rail_comp
                     <<" same_ordered_rail_active="<<rail_active
                     <<" same_ordered_rail_degree_min="<<rail_min
                     <<" same_ordered_rail_degree_max="<<rail_max
                     <<" same_forced_no_lower="<<sf_no_lower
                     <<" same_forced_min_lower="<<sf_min_lower
                     <<" same_forced_no_higher="<<sf_no_higher
                     <<" same_forced_min_higher="<<sf_min_higher
                     <<" same_forced_no_long_higher="<<sf_no_long_higher
                     <<" same_forced_min_long_higher="<<sf_min_long_higher
                     <<" same_forced_greedy_orphan="<<orphan
                     <<" same_forced_greedy_max_children="<<greedy_max_children
                     <<" no_leftmost_valley_packet="<<no_leftmost_valley_packet
                     <<" no_rightmost_valley_packet="<<no_rightmost_valley_packet
                     <<" no_any_valley_packet="<<no_any_valley_packet
                     <<" no_low_left_valley_packet="<<no_low_left_valley_packet
                     <<" no_low_right_valley_packet="<<no_low_right_valley_packet
                     <<" no_high_left_valley_packet="<<no_high_left_valley_packet
                     <<" no_high_right_valley_packet="<<no_high_right_valley_packet
                     <<" no_high_left_outer_move="<<no_high_left_outer_move
                     <<" no_high_right_outer_move="<<no_high_right_outer_move
                     <<" no_high_left_leftbiased_move="<<no_high_left_leftbiased_move
                     <<" no_high_right_leftbiased_move="<<no_high_right_leftbiased_move
                     <<" no_high_left_rightbiased_move="<<no_high_left_rightbiased_move
                     <<" no_high_right_rightbiased_move="<<no_high_right_rightbiased_move
                     <<" no_short_next_left_packet="<<no_short_next_left_packet
                     <<" no_short_next_right_packet="<<no_short_next_right_packet
                     <<" q_change_cover_bound="<<q_change_cover_bound
                     <<" no_small_q_change_cover="<<no_small_q_change_cover
                     <<" max_minimum_q_change_cover="<<max_minimum_q_change_cover
                     <<" same_forced_adjacent="<<same_forced_adjacent
                     <<" same_forced_adjacent_components="<<sfa_comp
                     <<" same_forced_adjacent_active="<<sfa_active
                     <<" same_forced_adjacent_degree_min="<<sfa_min
                     <<" same_forced_adjacent_degree_max="<<sfa_max
                     <<" same_forced_adjacent_no_lower="<<sfa_no_lower
                     <<" same_forced_adjacent_min_lower="<<sfa_min_lower
                     <<" no_lower="<<no_lower<<" min_lower="<<min_lower
                     <<" no_adjacent_lower="<<no_adjacent_lower
                     <<" min_adjacent_lower="<<min_adjacent_lower
                     <<" extreme="<<extreme_compatible<<'/'<<extreme_total
                     <<" extreme_bad=";
            for(int x:extreme_bad_examples)std::cout<<x<<',';
            std::cout<<'\n';
            for(const auto& ex:extreme_good_examples)std::cout<<"extreme_example "<<ex<<'\n';
            for(const auto& ex:high_outer_exceptions)
                std::cout<<"high_outer_exception "<<ex<<'\n';
            if(argc>2) for(int a=0;a<(int)roots.size();++a) {
                std::cout<<"same_forced_shortest root=";
                for(int p=0;p<2*m;++p)std::cout<<(((roots[a]>>p)&1U)?'1':'0');
                std::cout<<" area="<<area_stat(roots[a],m)
                         <<" p="<<shortest_higher_positions[a].first
                         <<" q="<<shortest_higher_positions[a].second<<'\n';
            }
            continue;
        }
        int min_mult=-1,max_mult=0;
        for (int a=0;a<(int)rows.size();++a) {
            for (int b=a+1;b<(int)rows.size();++b) {
                int mult=0;
                for (const State& x:states[a]) for (const State& y:states[b])
                    if (compatible(x,y)) ++mult;
                if (mult) {
                    graph[a].push_back(b); graph[b].push_back(a);
                    ++compatible_pairs; compatible_state_pairs+=mult;
                    int distance=std::popcount(roots[a]^roots[b])/2;
                    assert(distance>=1 && distance<=m);
                    ++root_distance_hist[distance];
                    if (distance==1) {
                        transposition_graph[a].push_back(b);
                        transposition_graph[b].push_back(a);
                        ++transposition_pairs;
                        U diff=roots[a]^roots[b];
                        int lo=std::countr_zero(diff);
                        int hi=31-std::countl_zero(diff);
                        if(hi-lo==1) {
                            ++compatible_adjacent_pairs;
                            adjacent_graph[a].push_back(b);
                            adjacent_graph[b].push_back(a);
                        }
                    }
                    min_mult=min_mult<0?mult:std::min(min_mult,mult);
                    max_mult=std::max(max_mult,mult);
                }
            }
        }
        int components=0, active=0,min_degree=-1,max_degree=0;
        std::vector<int> seen(rows.size());
        for (int i=0;i<(int)rows.size();++i) {
            if (!graph[i].empty()) {
                ++active;
                min_degree=min_degree<0?(int)graph[i].size():std::min(min_degree,(int)graph[i].size());
                max_degree=std::max(max_degree,(int)graph[i].size());
            }
            if (seen[i]) continue;
            ++components; seen[i]=1;
            std::vector<int> stack{i};
            while(!stack.empty()) {
                int x=stack.back();stack.pop_back();
                for(int y:graph[x]) if(!seen[y]){seen[y]=1;stack.push_back(y);}
            }
        }
        int transposition_components=0,transposition_active=0;
        std::fill(seen.begin(),seen.end(),0);
        for (int i=0;i<(int)rows.size();++i) {
            if (!transposition_graph[i].empty()) ++transposition_active;
            if (seen[i]) continue;
            ++transposition_components; seen[i]=1;
            std::vector<int> stack{i};
            while(!stack.empty()) {
                int x=stack.back();stack.pop_back();
                for(int y:transposition_graph[x]) if(!seen[y]) {
                    seen[y]=1;stack.push_back(y);
                }
            }
        }
        int adjacent_components=0,adjacent_active=0,adjacent_min=-1,adjacent_max=0;
        std::fill(seen.begin(),seen.end(),0);
        for(int i=0;i<(int)rows.size();++i) {
            if(!adjacent_graph[i].empty()) {
                ++adjacent_active;
                adjacent_min=adjacent_min<0?(int)adjacent_graph[i].size():std::min(adjacent_min,(int)adjacent_graph[i].size());
                adjacent_max=std::max(adjacent_max,(int)adjacent_graph[i].size());
            }
            if(seen[i]) continue;
            ++adjacent_components; seen[i]=1; std::vector<int> stack{i};
            while(!stack.empty()){int x=stack.back();stack.pop_back();
                for(int y:adjacent_graph[x])if(!seen[y]){seen[y]=1;stack.push_back(y);}}
        }
        std::vector<U> rp=rp_order(m);
        std::vector<int> root_index(1U<<(2*m),-1);
        for(int i=0;i<(int)roots.size();++i) root_index[roots[i]]=i;
        long long rp_compatible=0; long long rp_first_bad=-1;
        for(int i=1;i<(int)rp.size();++i){
            int a=root_index[rp[i-1]],b=root_index[rp[i]];
            assert(a>=0&&b>=0);
            bool ok=false;
            for(const State& x:states[a]) for(const State& y:states[b])
                if(compatible(x,y)){ok=true;goto rp_done;}
            rp_done:
            if(ok) ++rp_compatible;
            else if(rp_first_bad<0) rp_first_bad=i;
        }
        std::cout<<"m="<<m<<" R="<<R<<" d="<<d<<" q="<<d+1
                 <<" history_letter_rank="<<s<<" roots="<<rows.size()
                 <<" graph_edges="<<compatible_pairs
                 <<" state_edges="<<compatible_state_pairs
                 <<" components="<<components<<" active="<<active
                 <<" degree_min="<<min_degree<<" degree_max="<<max_degree
                 <<" multiplicity_min="<<min_mult<<" multiplicity_max="<<max_mult
                 <<" transposition_edges="<<transposition_pairs
                 <<" compatible_adjacent_edges="<<compatible_adjacent_pairs
                 <<" adjacent_components="<<adjacent_components
                 <<" adjacent_active="<<adjacent_active
                 <<" adjacent_degree_min="<<adjacent_min
                 <<" adjacent_degree_max="<<adjacent_max
                 <<" transposition_components="<<transposition_components
                 <<" transposition_active="<<transposition_active
                 <<" rp_compatible="<<rp_compatible<<'/'<<(rp.size()-1)
                 <<" rp_first_bad="<<rp_first_bad
                 <<" root_distance_hist=";
        for(int j=1;j<=m;++j) if(root_distance_hist[j])
            std::cout<<j<<':'<<root_distance_hist[j]<<',';
        std::cout<<'\n';
    }
}
