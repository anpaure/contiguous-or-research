#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <cadical.hpp>

#include <algorithm>
#include <array>
#include <bit>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <utility>
#include <vector>
using namespace std;

struct Edge { int u, v, variable; bool dummy; };

int main(int argc, char** argv) {
    if (argc < 6) return 2;
    const string raw_mode=argv[argc-1];
    string mode_spec=raw_mode;
    int sat_seed=stoi(argv[1])*1009+stoi(argv[2]);
    if(const size_t colon=mode_spec.find(':');colon!=string::npos) {
        sat_seed=stoi(mode_spec.substr(colon+1));
        mode_spec.resize(colon);
    }
    const bool all_edges=mode_spec.rfind("all",0)==0;
    const bool target_edges=mode_spec.rfind("target",0)==0;
    // `case` is the exact distance-13 decomposition used for the k=11
    // score-549 checkpoint.  RECOMBINE_EXTRA_UPPER supplies one rank-(r+1)
    // colour W.  Besides seed edges, expose only edges whose upper colour is
    // one of the seed's missing colours or W.  Since twelve upper colours are
    // missing and distance <=12 is already UNSAT, every distance-13 repair
    // has twelve new edges for those colours and just one remaining new edge;
    // its colour is W.  Iterating W over the layer is therefore exhaustive at
    // distance 13 while using roughly 700 rather than 6930 candidate edges.
    const bool color_case=mode_spec.rfind("case",0)==0;
    const string mode=all_edges?mode_spec.substr(3):
        (target_edges?mode_spec.substr(6):
         (color_case?mode_spec.substr(4):mode_spec));
    const bool ordered=mode.rfind("ord",0)==0;
    const string core_mode=ordered?mode.substr(3):mode;
    const bool shadow_only=core_mode=="shadow";
    const bool upper_base=core_mode.rfind("upperbase",0)==0;
    const bool upper_base_lazy=core_mode=="upperbaselazy";
    const bool upper_base_runs=core_mode=="upperbaseruns";
    const bool upper_base_global_runs=core_mode=="upperbaseglobalruns";
    const bool lower_base=core_mode.rfind("lowerbase",0)==0;
    const bool lower_base_lazy=core_mode=="lowerbaselazy";
    const bool lower_base_runs=core_mode=="lowerbaseruns";
    const bool lower_base_global_runs=core_mode=="lowerbaseglobalruns";
    const bool both_base=core_mode.rfind("bothbase",0)==0;
    const bool both_base_lazy=core_mode=="bothbaselazy";
    const bool rainbow_lower=core_mode.rfind("rainbowlower",0)==0;
    const bool rainbow_lower_runs=core_mode=="rainbowlowerruns";
    const bool hybrid=core_mode.rfind("hybrid",0)==0;
    const bool pair_runs=core_mode.rfind("pairruns",0)==0;
    const bool upper_runs=core_mode=="upperruns";
    const bool lower_runs=core_mode=="lowerruns";
    const bool r7_runs=core_mode=="r7runs";
    const bool incremental=core_mode.rfind("inc",0)==0||shadow_only||hybrid||
                           upper_base_lazy||upper_base_runs||lower_base_lazy||
                           lower_base_runs||both_base_lazy||rainbow_lower_runs;
    const int near_limit=core_mode.rfind("near",0)==0?stoi(core_mode.substr(4)):
        (core_mode.rfind("inc",0)==0&&core_mode.size()>3?
         stoi(core_mode.substr(3)):
         (hybrid&&core_mode.size()>6?stoi(core_mode.substr(6)):
          (pair_runs&&core_mode.size()>8?stoi(core_mode.substr(8)):-1)));
    const bool lazy_full=core_mode=="lazy"||incremental;
    const bool use_pair=both_base||
                        (core_mode!="base"&&!upper_base&&!lower_base&&
                         !rainbow_lower&&
                         !incremental&&!r7_runs)||hybrid;
    const bool use_quad=core_mode=="quad"||core_mode=="full";
    // Hybrid mode checks coordinate runs lazily after obtaining a connected
    // path.  Enumerating every possible short run in the full Johnson graph
    // consumes several gigabytes and is redundant with those exact lazy cuts.
    const bool use_runs=core_mode=="full"||pair_runs||upper_runs||
                        lower_runs||r7_runs||upper_base_global_runs||
                        lower_base_global_runs;
    const bool factorability_enforced=use_runs||(lazy_full&&!shadow_only);
    const bool pair_cover4=use_pair&&!upper_runs;
    const bool pair_cover8=use_pair&&!lower_runs;
    const bool compact_pair_shadows=getenv("RECOMBINE_COMPACT_PAIR_SHADOWS");
    const bool compact_four_shadows=getenv("RECOMBINE_COMPACT_FOUR_SHADOWS");
    const int k=stoi(argv[1]), rank=stoi(argv[2]);
    const int factor_d=getenv("RECOMBINE_D")?stoi(getenv("RECOMBINE_D")):3;
    const int full=(1<<k)-1;
    const int path_count=argc-4;
    vector<vector<int>> paths(path_count);
    for (int p=0;p<path_count;++p) {
        ifstream in(argv[3+p]);
        for(int x;in>>x;) paths[p].push_back(x);
    }
    // Optional exact induced-subgraph branch.  Every listed mask is removed
    // from every supplied permutation before the Johnson graph is built.
    // With the variable absent, the historical input stream is unchanged.
    if(const char* raw_excluded=getenv("RECOMBINE_EXCLUDE_MASKS")) {
        ifstream in(raw_excluded);
        set<int> excluded;
        for(int x;in>>x;) excluded.insert(x);
        if(excluded.empty()) return 8;
        for(auto& path:paths) {
            const size_t before=path.size();
            erase_if(path,[&](int x){return excluded.count(x);});
            if(before-path.size()!=excluded.size()) return 8;
        }
        cerr<<"excluded_masks="<<excluded.size()<<'\n';
    }
    for(int p=1;p<path_count;++p) if(paths[0].size()!=paths[p].size()) return 3;
    const int n=paths[0].size(), dummy=n;
    vector<int> masks=paths[0], index(1<<k,-1);
    for(int i=0;i<n;++i) {
        if(popcount((unsigned)masks[i])!=rank || index[masks[i]]>=0) return 4;
        index[masks[i]]=i;
    }
    for(int p=1;p<path_count;++p) for(int x:paths[p]) if(index[x]<0) return 5;
    vector<unsigned char> externally_covered(1<<k);
    if(const char* raw_covered=getenv("RECOMBINE_PRECOVERED_MASKS")) {
        ifstream in(raw_covered);
        int count=0;
        for(int x;in>>x;) {
            if(x<=0||x>full) return 8;
            if(!externally_covered[x]) ++count;
            externally_covered[x]=1;
        }
        cerr<<"externally_covered_masks="<<count<<'\n';
    }
    const int required_start_subset=getenv("RECOMBINE_START_CONTAINS")?
        stoi(getenv("RECOMBINE_START_CONTAINS")):-1;
    if(required_start_subset>full) return 8;

    set<pair<int,int>> pairs;
    for(const auto& path:paths) for(int i=0;i+1<n;++i) {
        int u=index[path[i]],v=index[path[i+1]];
        if(u>v) swap(u,v);
        if(popcount((unsigned)(masks[u]^masks[v]))!=2) {
            if(all_edges) continue;
            return 6;
        }
        pairs.insert({u,v});
    }
    // Optional audited sparse candidate augmentation.  Each line contains
    // two rank-`rank` masks naming one Johnson edge.  This is useful when a
    // path is overlaid with a certified path forest (for example, the
    // coordinate-12 section of the exact k=12 optimum) without completing
    // that forest by arbitrary seam edges first.
    if(const char* raw_extra_edges=getenv("RECOMBINE_EXTRA_EDGE_FILE")) {
        ifstream extra_input(raw_extra_edges);
        int left_mask,right_mask,added=0;
        while(extra_input>>left_mask>>right_mask) {
            if(left_mask<0||left_mask>full||right_mask<0||right_mask>full)
                return 8;
            int u=index[left_mask],v=index[right_mask];
            if(u<0||v<0||u==v||
               popcount((unsigned)(left_mask^right_mask))!=2) return 8;
            if(u>v)swap(u,v);
            added+=pairs.insert({u,v}).second;
        }
        if(!extra_input.eof()) return 8;
        cerr<<"extra_candidate_edges="<<added<<'\n';
    }
    // In the sparse recombination mode, candidate edges are taken only from
    // the supplied paths.  Prefixing the mode by "all" instead exposes the
    // complete Johnson graph.  This is still a small graph for J(11,6): 462
    // vertices and 6930 edges, and it lets the SAT solver synthesize a new
    // path rather than merely splice the currently known ones.
    if(all_edges) for(int u=0;u<n;++u) for(int v=u+1;v<n;++v)
        if(popcount((unsigned)(masks[u]^masks[v]))==2) pairs.insert({u,v});
    if(target_edges) {
        // Preserve all supplied path edges, and expose every Johnson edge
        // capable of repairing an upper color absent from the preferred
        // (last) path.  This gives an exact, very small neighborhood around a
        // nearly complete path instead of the entire 6930-edge graph.
        vector<unsigned char> seen7(1<<k),seen8(1<<k);
        const vector<int>& preferred=paths.back();
        for(int i=0;i+1<n;++i) {
            unsigned char& count=seen7[preferred[i]|preferred[i+1]];
            if(count!=255)++count;
        }
        for(int i=0;i+2<n;++i)
        {
            unsigned char& count=seen8[preferred[i]|preferred[i+1]|preferred[i+2]];
            if(count!=255)++count;
        }
        for(int target=0;target<=full;++target) {
            const int tr=popcount((unsigned)target);
            // A rank-7 color used once is just as constraining as a missing
            // one: deleting its unique edge would lose that target.  Expose
            // every alternative edge for both missing and singleton colors.
            // For rank 8, expose the induced graph only for genuinely absent
            // triple unions; pair witnesses for existing colors are retained
            // from the seed path.
            if((tr!=rank+1||seen7[target]>1)&&(tr!=rank+2||seen8[target])) continue;
            for(int u=0;u<n;++u) for(int v=u+1;v<n;++v) {
                if(popcount((unsigned)(masks[u]^masks[v]))!=2) continue;
                if(tr==rank+1) {
                    if((masks[u]|masks[v])==target) pairs.insert({u,v});
                } else if(!(masks[u]&~target)&&!(masks[v]&~target)) {
                    pairs.insert({u,v});
                }
            }
        }
    }
    if(color_case) {
        const char* raw_extra=getenv("RECOMBINE_EXTRA_UPPER");
        if(!raw_extra) return 8;
        const int extra_upper=stoi(raw_extra);
        vector<unsigned char> seen(1<<k), allowed(1<<k);
        const vector<int>& preferred=paths.back();
        for(int i=0;i+1<n;++i) seen[preferred[i]|preferred[i+1]]=1;
        for(int target=0;target<=full;++target)
            if(popcount((unsigned)target)==rank+1&&!seen[target])
                allowed[target]=1;
        if(extra_upper>=0&&extra_upper<=full&&
           popcount((unsigned)extra_upper)==rank+1)
            allowed[extra_upper]=1;
        for(int u=0;u<n;++u) for(int v=u+1;v<n;++v) {
            if(popcount((unsigned)(masks[u]^masks[v]))!=2) continue;
            if(allowed[masks[u]|masks[v]]) pairs.insert({u,v});
        }
    }
    const int canonical_endpoint_mask=(1<<rank)-1;
    const int canonical_neighbor_mask=canonical_endpoint_mask^
        (1<<(rank-3))^(1<<rank);
    int canonical_u=index[canonical_endpoint_mask];
    int canonical_v=index[canonical_neighbor_mask];
    if(canonical_u>canonical_v)swap(canonical_u,canonical_v);
    // In a full graph this is a WLOG symmetry normalization.  In a sparse
    // portfolio it is enabled only when the preferred seed supplied the same
    // canonical first edge; imposing it then deliberately searches that
    // particularly strong component of the restricted neighborhood.
    // A bit-permutation normalization is WLOG for unrestricted existence,
    // but not inside a Hamming ball around the fixed preferred path: applying
    // the permutation changes which preferred edges count as dropped.  Keep
    // the exact omitted-colour/endpoint symmetry only when no distance bound
    // is active.
    // In a complete Johnson graph the normalization is WLOG.  In a sparse
    // union of supplied paths it deliberately selects only one symmetry
    // component, because an arbitrary bit permutation need not preserve that
    // sparse graph.  Allow an exhaustive sparse-union run to disable it.
    const bool canonicalize=!getenv("RECOMBINE_NO_CANONICAL")&&near_limit<0&&
        !upper_base&&!lower_base&&!both_base&&
        !rainbow_lower_runs&&
        (all_edges||pairs.count({canonical_u,canonical_v}));
    if(getenv("RECOMBINE_SECOND_ORBIT")&&
       (!canonicalize||!ordered||!all_edges||k!=11||rank!=6)) return 9;
    // The third-edge split is a refinement of the certified four-way
    // second-edge split.  Its orbit table also uses the delay-three run
    // condition, so refuse it outside that exact WLOG setting.
    if(getenv("RECOMBINE_THIRD_ORBIT")&&
       (!getenv("RECOMBINE_SECOND_ORBIT")||!canonicalize||!ordered||
        !all_edges||k!=11||rank!=6||factor_d!=3||
        !factorability_enforced)) return 9;
    if(getenv("RECOMBINE_FOURTH_ORBIT")&&
       (!getenv("RECOMBINE_THIRD_ORBIT")||!canonicalize||!ordered||
        !all_edges||k!=11||rank!=6||factor_d!=3||
        !factorability_enforced)) return 9;
    if(getenv("RECOMBINE_C0_MOMENT")&&
       (!canonicalize||k!=11||rank!=6)) return 9;
    if(getenv("RECOMBINE_PREFIX_MOMENTS")&&
       (!canonicalize||!ordered||k!=11||rank!=6)) return 9;
    if(getenv("RECOMBINE_PREFIX_UPPER_MOMENTS")&&
       (!canonicalize||!ordered||k!=11||rank!=6)) return 9;
    vector<int> canonical_prefix_masks;
    vector<Edge> edges;
    vector<vector<int>> incident(n+1);
    map<pair<int,int>,int> edge_index;
    int variables=0;
    auto add_edge=[&](int u,int v,bool is_dummy){
        if(u>v) swap(u,v);
        const int id=edges.size();
        edges.push_back({u,v,++variables,is_dummy});
        incident[u].push_back(id); incident[v].push_back(id);
        edge_index[{u,v}]=id;
    };
    for(auto [u,v]:pairs) add_edge(u,v,false);
    for(int v=0;v<n;++v) add_edge(v,dummy,true);

    CaDiCaL::Solver solver;
    solver.set("quiet",1);
    solver.set("seed",sat_seed);
    // Hybrid models enforce the expensive rank-4/rank-8 layers up front and
    // normally need only a handful of lazy rank-3/rank-9 targets.  Reserving
    // five million variables for every portfolio process caused avoidable Pod
    // OOM kills.  One million is the hybrid default, while long lazy runs may
    // raise it explicitly through RECOMBINE_VARIABLE_RESERVE before CaDiCaL
    // creates internal extension variables.
    const int declared_variable_limit=getenv("RECOMBINE_VARIABLE_RESERVE")?
        stoi(getenv("RECOMBINE_VARIABLE_RESERVE")):
        (hybrid?1000000:((lazy_full||n>1000)?5000000:500000));
    solver.declare_more_variables(declared_variable_limit);
    vector<unsigned char> phase_edge(edges.size());
    // Unlike phase_edge, seed_edge is immutable: repair phase hints below
    // may deliberately move the preferred phase away from the input path,
    // while distance and extra-colour accounting must continue to refer to
    // the actual preferred path.
    vector<unsigned char> seed_edge(edges.size());
    const vector<int>& preferred=paths.back();
    for(int i=0;i+1<n;++i) {
        int u=index[preferred[i]],v=index[preferred[i+1]];if(u>v)swap(u,v);
        const auto found=edge_index.find({u,v});
        if(found!=edge_index.end()) {
            phase_edge[found->second]=1;
            seed_edge[found->second]=1;
        }
    }
    // Optional rank-colour repair phase.  Each line contains
    //     lower_colour  desired_upper_colour
    // and replaces the seed preference for that lower colour by the unique
    // Johnson edge with the requested upper colour.  This changes phases
    // only, never the feasible set.  For the k=11 score-549 seed, a max-flow
    // assignment safely fills all twelve absent rank-7 colours this way.
    if(const char* phase_repairs=getenv("RECOMBINE_PHASE_REPAIRS")) {
        ifstream phase_input(phase_repairs);
        for(int lower,upper;phase_input>>lower>>upper;) {
            for(int id=0;id<(int)edges.size();++id) if(!edges[id].dummy) {
                const Edge&e=edges[id];
                if((masks[e.u]&masks[e.v])!=lower) continue;
                phase_edge[id]=(masks[e.u]|masks[e.v])==upper;
            }
        }
    }
    for(int endpoint:{index[preferred.front()],index[preferred.back()]}) {
        int u=endpoint,v=dummy;if(u>v)swap(u,v);
        phase_edge[edge_index[{u,v}]]=1;
    }
    for(int id=0;id<(int)edges.size();++id)
        solver.phase(phase_edge[id]?edges[id].variable:-edges[id].variable);
    const char* dump_cnf_path=getenv("RECOMBINE_DUMP_CNF");
    vector<vector<int>> recorded_clauses;
    auto clause=[&](const vector<int>& c){
        if(dump_cnf_path) recorded_clauses.push_back(c);
        for(int x:c)solver.add(x);
        solver.add(0);
    };
    auto var=[&](){return ++variables;};

    auto at_most=[&](const vector<int>& literals,int maximum) {
        if(maximum<0||maximum>=(int)literals.size())return;
        if(maximum==0){for(int literal:literals)clause({-literal});return;}
        vector<int> previous;
        for(int literal:literals) {
            vector<int> current(maximum);
            for(int& value:current)value=var();
            clause({-literal,current[0]});
            for(int j=0;j<(int)previous.size();++j)
                clause({-previous[j],current[j]});
            for(int j=0;j+1<(int)previous.size()&&j+1<maximum;++j)
                clause({-literal,-previous[j],current[j+1]});
            if((int)previous.size()==maximum)
                clause({-literal,-previous[maximum-1]});
            previous.swap(current);
        }
    };

    // Exact truncated unary counter for a lower cardinality bound.  State
    // current[j] means that at least j+1 input literals seen so far are true.
    // Only `minimum` columns are needed, so a small certified lower-distance
    // bound costs O(minimum*|literals|), rather than encoding an almost-full
    // upper bound on the complementary retained literals.
    auto at_least=[&](const vector<int>& literals,int minimum) {
        if(minimum<=0)return;
        if(minimum>(int)literals.size()){clause({});return;}
        vector<int> previous;
        for(int literal:literals) {
            const int width=min(minimum,(int)previous.size()+1);
            vector<int> current(width);
            for(int& value:current)value=var();
            if(previous.empty()) {
                clause({-literal,current[0]});
                clause({-current[0],literal});
            } else {
                clause({-literal,current[0]});
                clause({-previous[0],current[0]});
                clause({-current[0],literal,previous[0]});
            }
            for(int j=1;j<width;++j) {
                const int below=previous[j-1];
                if(j<(int)previous.size()) {
                    const int same=previous[j];
                    clause({-same,current[j]});
                    clause({-literal,-below,current[j]});
                    clause({-current[j],same,literal});
                    clause({-current[j],same,below});
                } else {
                    clause({-literal,-below,current[j]});
                    clause({-current[j],literal});
                    clause({-current[j],below});
                }
            }
            previous.swap(current);
        }
        clause({previous[minimum-1]});
    };

    if(near_limit>=0) {
        vector<int> dropped;
        for(int i=0;i+1<n;++i) {
            int u=index[preferred[i]],v=index[preferred[i+1]];if(u>v)swap(u,v);
            dropped.push_back(-edges[edge_index[{u,v}]].variable);
        }
        at_most(dropped,near_limit);
    }

    // A separately proof-certified radius exclusion can be imported as a
    // redundant lower-distance constraint in an unrestricted search.  If at
    // least `minimum` preferred edges must be dropped, then at most
    // (n-1-minimum) of the preferred real edges may remain selected.  This
    // does not alter phases or candidate-edge support.  For the audited
    // k=11 score-549 seed, RECOMBINE_MIN_DISTANCE=19 is currently certified
    // by K11_DISTANCE18_AUDIT.md in a relaxation weaker than this model.
    if(const char* raw_minimum=getenv("RECOMBINE_MIN_DISTANCE")) {
        const int minimum=stoi(raw_minimum);
        if(minimum<0||minimum>n-1)return 9;
        vector<int> dropped_seed;
        for(int id=0;id<(int)edges.size();++id)
            if(!edges[id].dummy&&seed_edge[id])
                dropped_seed.push_back(-edges[id].variable);
        if((int)dropped_seed.size()!=n-1)return 9;
        at_least(dropped_seed,minimum);
        cerr<<"minimum_seed_distance="<<minimum<<'\n';
    }

    // Every real vertex and the dummy have degree exactly two.  Sparse
    // recombination graphs use direct triples for at-most-two.  In the full
    // Johnson graph a real vertex has degree 31 (including its dummy edge),
    // so a sequential counter is vastly smaller than C(31,3) clauses at each
    // of 462 vertices.
    for(int v=0;v<n;++v) {
        const auto& a=incident[v];
        for(int omitted=0;omitted<(int)a.size();++omitted) {
            vector<int> c;
            for(int i=0;i<(int)a.size();++i) if(i!=omitted)c.push_back(edges[a[i]].variable);
            clause(c);
        }
        vector<int> literals;
        literals.reserve(a.size());
        for(int id:a)literals.push_back(edges[id].variable);
        if(a.size()<=8) {
            for(int i=0;i<(int)a.size();++i) for(int j=i+1;j<(int)a.size();++j)
                for(int h=j+1;h<(int)a.size();++h)
                    clause({-edges[a[i]].variable,-edges[a[j]].variable,
                            -edges[a[h]].variable});
        } else at_most(literals,2);
    }
    const auto& da=incident[dummy];
    for(int omitted=0;omitted<(int)da.size();++omitted) {
        vector<int> c; c.reserve(da.size()-1);
        for(int i=0;i<(int)da.size();++i) if(i!=omitted)c.push_back(edges[da[i]].variable);
        clause(c);
    }
    vector<array<int,2>> prefix(da.size()-1);
    for(auto& row:prefix) row={var(),var()};
    clause({-edges[da[0]].variable,prefix[0][0]});
    for(int i=1;i<(int)da.size()-1;++i) {
        const int x=edges[da[i]].variable;
        clause({-x,prefix[i][0]});
        clause({-prefix[i-1][0],prefix[i][0]});
        clause({-x,-prefix[i-1][0],prefix[i][1]});
        clause({-prefix[i-1][1],prefix[i][1]});
        clause({-x,-prefix[i-1][1]});
    }
    clause({-edges[da.back()].variable,-prefix.back()[1]});

    if(ordered) {
        // Give every selected edge one direction and require one incoming and
        // one outgoing selected arc at every vertex.  Binary path positions
        // then eliminate all subtours in the initial SAT model: dummy->v
        // fixes pos(v)=1, and every real arc u->v enforces pos(v)=pos(u)+1.
        // A real directed cycle would imply pos=pos+L modulo 2^b.  We choose
        // 2^b>n below, so this is impossible.  This is much smaller than a
        // unary order encoding and avoids expensive lazy connectivity rounds.
        vector<array<int,2>> arc(edges.size());
        vector<vector<int>> outgoing(n+1),incoming(n+1);
        vector<int> phase_preferred=preferred;
        if(canonicalize&&phase_preferred.back()==canonical_endpoint_mask)
            reverse(phase_preferred.begin(),phase_preferred.end());
        vector<int> preferred_position(n,-1);
        for(int i=0;i<n;++i) preferred_position[index[phase_preferred[i]]]=i;
        for(int id=0;id<(int)edges.size();++id) {
            arc[id]={var(),var()}; // e.u->e.v and e.v->e.u
            const Edge&e=edges[id];
            auto desired_arc=[&](int from,int to) {
                if(from==dummy)
                    return to==index[phase_preferred.front()];
                if(to==dummy)
                    return from==index[phase_preferred.back()];
                return preferred_position[to]==preferred_position[from]+1;
            };
            solver.phase(desired_arc(e.u,e.v)?arc[id][0]:-arc[id][0]);
            solver.phase(desired_arc(e.v,e.u)?arc[id][1]:-arc[id][1]);
            clause({-arc[id][0],e.variable});
            clause({-arc[id][1],e.variable});
            clause({-e.variable,arc[id][0],arc[id][1]});
            clause({-arc[id][0],-arc[id][1]});
            outgoing[e.u].push_back(arc[id][0]);
            incoming[e.v].push_back(arc[id][0]);
            outgoing[e.v].push_back(arc[id][1]);
            incoming[e.u].push_back(arc[id][1]);
        }
        if(required_start_subset>=0) {
            int candidates=0;
            for(int id:incident[dummy]) {
                const Edge&e=edges[id];
                const int real=e.u==dummy?e.v:e.u;
                // add_edge(real,dummy) stores dummy->real as arc[id][1].
                const int outgoing_from_dummy=e.u==dummy?arc[id][0]:arc[id][1];
                if((masks[real]&required_start_subset)==required_start_subset)
                    ++candidates;
                else clause({-outgoing_from_dummy});
            }
            if(!candidates) clause({});
            cerr<<"start_contains="<<required_start_subset
                <<" candidates="<<candidates<<'\n';
        }
        if(canonicalize) {
            // Canonical symmetry representative.  The 461 distinct real
            // edge colours omit one rank-(r-1) set.  Bit permutations may
            // send it to {0,...,r-2}; its stabilizer may send an endpoint
            // containing it to {0,...,r-1}; path reversal makes that endpoint
            // the start.  The matching missing-colour clauses are added once
            // by_lower has been built below.
            const int fixed_endpoint=(1<<rank)-1;
            const int fixed_vertex=index[fixed_endpoint];
            int a=fixed_vertex,b=dummy;if(a>b)swap(a,b);
            const int id=edge_index[{a,b}];
            clause({edges[id].variable});
            // add_edge stores real--dummy as u--v, so arc[1] is dummy->real.
            clause({arc[id][1]});

            // The missing colour forbids the first transition from removing
            // bit r-1.  The stabilizer of the fixed colour and endpoint is
            // transitive on the remaining removed bits and on added bits, so
            // one may also normalize the first real neighbour.  The chosen
            // representative agrees with the reversed 549-shadow seed for
            // k=11 (63 -> 119), preserving an excellent complete phase.
            const int fixed_neighbor_mask=fixed_endpoint^
                (1<<(rank-3))^(1<<rank);
            const int fixed_neighbor=index[fixed_neighbor_mask];
            int c=fixed_vertex,e=fixed_neighbor;if(c>e)swap(c,e);
            const int first_id=edge_index[{c,e}];
            clause({edges[first_id].variable});
            const Edge&first_edge=edges[first_id];
            clause({first_edge.u==fixed_vertex?
                    arc[first_id][0]:arc[first_id][1]});
            canonical_prefix_masks={fixed_endpoint,fixed_neighbor_mask};

            // After fixing the omitted colour, endpoint, and first real
            // edge, the stabilizer has only four possible orbits for the
            // second real edge.  The common undistinguished endpoint bits
            // form one orbit, bit rank-1 is distinguished by the endpoint,
            // the bit removed by the first edge is distinguished, and the
            // still-unused outside bits form one orbit.  Removing the bit
            // added by the first edge would repeat the first lower colour,
            // so those two apparent cases are already impossible.
            //
            // RECOMBINE_SECOND_ORBIT=0,1,2,3 selects representatives
            //   common -> first-removed,
            //   common -> fresh-outside,
            //   endpoint-special -> first-removed,
            //   endpoint-special -> fresh-outside.
            // Running all four values is exhaustive modulo the stabilizer
            // of the already canonical prefix.  This option is deliberately
            // available only inside the WLOG canonical branch.
            if(const char* raw_second=getenv("RECOMBINE_SECOND_ORBIT")) {
                const int orbit=stoi(raw_second);
                if(orbit<0||orbit>=4) return 9;
                const int common_remove=0;
                const int endpoint_special=rank-1;
                const int first_removed=rank-3;
                const int fresh_outside=rank+1;
                const int remove_bit=(orbit<2)?common_remove:endpoint_special;
                const int add_bit=(orbit%2==0)?first_removed:fresh_outside;
                const int second_neighbor_mask=canonical_neighbor_mask^
                    (1<<remove_bit)^(1<<add_bit);
                const int second_neighbor=index[second_neighbor_mask];
                if(second_neighbor<0) return 9;
                int d=fixed_neighbor,e=second_neighbor;if(d>e)swap(d,e);
                const auto found_second=edge_index.find({d,e});
                if(found_second==edge_index.end()) return 9;
                const int second_id=found_second->second;
                clause({edges[second_id].variable});
                const Edge&second_edge=edges[second_id];
                clause({second_edge.u==fixed_neighbor?
                        arc[second_id][0]:arc[second_id][1]});
                canonical_prefix_masks.push_back(second_neighbor_mask);
                cerr<<"canonical_second_orbit="<<orbit
                    <<" second_mask="<<second_neighbor_mask<<'\n';

                // Refine the canonical prefix by one more transition.  For
                // each second-edge orbit, the setwise stabilizer of
                // C,E,F,G has respectively 4,6,2,3 legal orbits for H.
                // Besides the rainbow lower-colour condition, factorability
                // excludes removing bit 6 here: bit 6 was introduced on the
                // first edge, so E,F,G,H would otherwise contain the
                // forbidden internal run 0,1,1,0.  The exact representatives
                // and proof are recorded in K11_THIRD_EDGE_ORBITS.md.
                if(const char* raw_third=getenv("RECOMBINE_THIRD_ORBIT")) {
                    static constexpr int third_count[4]={4,6,2,3};
                    static constexpr int third_mask[4][6]={
                        {125,252, 95,222, -1, -1},
                        {245,252,500,215,222,470},
                        {126,222, -1, -1, -1, -1},
                        {222,246,470, -1, -1, -1}
                    };
                    const int third_orbit=stoi(raw_third);
                    if(third_orbit<0||third_orbit>=third_count[orbit]) return 9;
                    const int third_neighbor_mask=third_mask[orbit][third_orbit];
                    const int third_neighbor=index[third_neighbor_mask];
                    if(third_neighbor<0||third_neighbor==fixed_vertex||
                       third_neighbor==fixed_neighbor||
                       third_neighbor==second_neighbor) return 9;
                    int f=second_neighbor,g=third_neighbor;if(f>g)swap(f,g);
                    const auto found_third=edge_index.find({f,g});
                    if(found_third==edge_index.end()) return 9;
                    const int third_id=found_third->second;
                    clause({edges[third_id].variable});
                    const Edge&third_edge=edges[third_id];
                    clause({third_edge.u==second_neighbor?
                            arc[third_id][0]:arc[third_id][1]});
                    canonical_prefix_masks.push_back(third_neighbor_mask);
                    cerr<<"canonical_third_orbit="<<third_orbit
                        <<" third_mask="<<third_neighbor_mask<<'\n';

                    // One final exact prefix split.  At H, the coordinates
                    // introduced on transitions 1, 2, and 3 are all still
                    // unavailable for removal: removing them would complete
                    // internal 1-runs of lengths 3, 2, and 1 respectively
                    // (the last case also repeats the preceding lower
                    // colour).  The 15 remaining labelled transitions split
                    // into the residual-stabilizer orbits tabulated below.
                    // K11_FOURTH_EDGE_ORBITS.md proves completeness, and the
                    // independent checker enumerates every raw transition.
                    if(const char* raw_fourth=getenv("RECOMBINE_FOURTH_ORBIT")) {
                        static constexpr int fourth_count[4][6]={
                            {4,6,2,3,0,0},
                            {6,6,8,3,3,4},
                            {2,3,0,0,0,0},
                            {3,3,4,0,0,0}
                        };
                        static constexpr int fourth_mask[4][6][8]={
                          {
                            {221, 95,237,111, -1, -1, -1, -1},
                            {476,221,222,492,237,238, -1, -1},
                            {207,111, -1, -1, -1, -1, -1, -1},
                            {462,238,207, -1, -1, -1, -1, -1},
                            {-1,-1,-1,-1,-1,-1,-1,-1},
                            {-1,-1,-1,-1,-1,-1,-1,-1}
                          },{
                            {469,221,215,485,237,231, -1, -1},
                            {476,221,222,492,237,238, -1, -1},
                            {980,476,469,470,996,492,485,486},
                            {455,231,207, -1, -1, -1, -1, -1},
                            {462,238,207, -1, -1, -1, -1, -1},
                            {966,486,462,455, -1, -1, -1, -1}
                          },{
                            {238,111, -1, -1, -1, -1, -1, -1},
                            {462,238,207, -1, -1, -1, -1, -1},
                            {-1,-1,-1,-1,-1,-1,-1,-1},
                            {-1,-1,-1,-1,-1,-1,-1,-1},
                            {-1,-1,-1,-1,-1,-1,-1,-1},
                            {-1,-1,-1,-1,-1,-1,-1,-1}
                          },{
                            {462,238,207, -1, -1, -1, -1, -1},
                            {486,238,231, -1, -1, -1, -1, -1},
                            {966,486,462,455, -1, -1, -1, -1},
                            {-1,-1,-1,-1,-1,-1,-1,-1},
                            {-1,-1,-1,-1,-1,-1,-1,-1},
                            {-1,-1,-1,-1,-1,-1,-1,-1}
                          }
                        };
                        const int fourth_orbit=stoi(raw_fourth);
                        if(fourth_orbit<0||
                           fourth_orbit>=fourth_count[orbit][third_orbit])
                            return 9;
                        const int fourth_neighbor_mask=
                            fourth_mask[orbit][third_orbit][fourth_orbit];
                        const int fourth_neighbor=index[fourth_neighbor_mask];
                        if(fourth_neighbor<0||fourth_neighbor==fixed_vertex||
                           fourth_neighbor==fixed_neighbor||
                           fourth_neighbor==second_neighbor||
                           fourth_neighbor==third_neighbor) return 9;
                        int h=third_neighbor,i=fourth_neighbor;if(h>i)swap(h,i);
                        const auto found_fourth=edge_index.find({h,i});
                        if(found_fourth==edge_index.end()) return 9;
                        const int fourth_id=found_fourth->second;
                        clause({edges[fourth_id].variable});
                        const Edge&fourth_edge=edges[fourth_id];
                        clause({fourth_edge.u==third_neighbor?
                                arc[fourth_id][0]:arc[fourth_id][1]});
                        canonical_prefix_masks.push_back(fourth_neighbor_mask);
                        cerr<<"canonical_fourth_orbit="<<fourth_orbit
                            <<" fourth_mask="<<fourth_neighbor_mask<<'\n';
                    }
                }
            }
        }
        for(int v=0;v<=n;++v) {
            clause(outgoing[v]);
            clause(incoming[v]);
        }

        // Choose enough binary bits that no proper real subtour can wrap
        // modulo 2^b.  The earlier k=11-only value b=9 is invalid once this
        // encoder is reused for the 1716 vertices of J(13,7).
        int position_bits=1;
        while((1<<position_bits)<=n)++position_bits;
        vector<vector<int>> position(n,vector<int>(position_bits));
        vector<vector<int>> carry(n,vector<int>(position_bits));
        for(int v=0;v<n;++v) {
            const int desired_position=preferred_position[v]+1;
            for(int bit=0;bit<position_bits;++bit) {
                position[v][bit]=var();
                solver.phase((desired_position&(1<<bit))?
                             position[v][bit]:-position[v][bit]);
            }
            // carry[v][b] means all position bits 0,...,b-1 are one.
            for(int bit=2;bit<position_bits;++bit) {
                carry[v][bit]=var();
                const bool desired_carry=(desired_position&((1<<bit)-1))==
                                           ((1<<bit)-1);
                solver.phase(desired_carry?carry[v][bit]:-carry[v][bit]);
                const int previous=bit==2?position[v][0]:carry[v][bit-1];
                const int next_bit=position[v][bit-1];
                clause({-carry[v][bit],previous});
                clause({-carry[v][bit],next_bit});
                clause({carry[v][bit],-previous,-next_bit});
            }
        }
        auto add_increment=[&](int from,int to,int selected_arc) {
            if(to==dummy) return;
            if(from==dummy) {
                for(int bit=0;bit<position_bits;++bit)
                    clause({-selected_arc,bit==0?position[to][bit]:-position[to][bit]});
                return;
            }
            // Low bit is complemented when adding one.
            clause({-selected_arc,position[from][0],position[to][0]});
            clause({-selected_arc,-position[from][0],-position[to][0]});
            for(int bit=1;bit<position_bits;++bit) {
                const int x=position[from][bit];
                const int y=bit==1?position[from][0]:carry[from][bit];
                const int z=position[to][bit];
                // z = x xor y, gated by selected_arc.
                clause({-selected_arc,x,y,-z});
                clause({-selected_arc,x,-y,z});
                clause({-selected_arc,-x,y,z});
                clause({-selected_arc,-x,-y,-z});
            }
        };
        for(int id=0;id<(int)edges.size();++id) {
            const Edge&e=edges[id];
            add_increment(e.u,e.v,arc[id][0]);
            add_increment(e.v,e.u,arc[id][1]);
        }
        cerr<<"ordered_connectivity=1 variables="<<variables<<'\n';
    }

    // All 461 real path edges have distinct rank-5 intersection colors.
    vector<vector<int>> by_lower(1<<k), by_upper(1<<k);
    for(int id=0;id<(int)edges.size();++id) if(!edges[id].dummy) {
        const Edge&e=edges[id];
        by_lower[masks[e.u]&masks[e.v]].push_back(e.variable);
        by_upper[masks[e.u]|masks[e.v]].push_back(e.variable);
    }

    // Exact sparse colour-support decomposition for a small Hamming ball.
    // If the preferred path misses m upper colours and a candidate replaces
    // at most m+q preferred edges, then one new edge is mandatory for each
    // missing colour and at most q further ("extra") new edges remain.  In
    // particular, those extra edges use at most q distinct upper colours.
    //
    // RECOMBINE_EXTRA_SUPPORT=q adds the corresponding redundant, but useful,
    // propagation.  For a colour already present in the seed, every selected
    // non-seed edge activates its support variable.  For a seed-missing
    // colour, the first selected edge is mandatory and every *pair* of
    // selected edges activates the support variable.  At most q support
    // variables may be active.  The ordinary near-distance cardinality bound
    // remains responsible for multiplicity, so this does not change the
    // feasible set when q >= near_limit - missing_upper_count.
    if(const char* raw_support=getenv("RECOMBINE_EXTRA_SUPPORT")) {
        const int support_limit=stoi(raw_support);
        if(support_limit<0) return 9;
        vector<unsigned char> seed_upper_seen(1<<k);
        for(int id=0;id<(int)edges.size();++id)
            if(!edges[id].dummy&&seed_edge[id]) {
                const Edge&e=edges[id];
                seed_upper_seen[masks[e.u]|masks[e.v]]=1;
            }
        int missing_upper_count=0;
        for(int upper=0;upper<=full;++upper)
            if(popcount((unsigned)upper)==rank+1&&!seed_upper_seen[upper])
                ++missing_upper_count;
        // Refuse an accidentally heuristic setting.  With a distance bound
        // d, at most d-missing_upper_count extra edges exist; hence that is
        // the smallest support cap guaranteed not to exclude a candidate.
        const int safe_support=max(0,near_limit-missing_upper_count);
        if(near_limit<0||support_limit<safe_support) return 9;
        vector<int> support_literals;
        for(int upper=0;upper<=full;++upper)
            if(popcount((unsigned)upper)==rank+1) {
                vector<int> nonseed;
                for(int id=0;id<(int)edges.size();++id)
                    if(!edges[id].dummy&&!seed_edge[id]) {
                        const Edge&e=edges[id];
                        if((masks[e.u]|masks[e.v])==upper)
                            nonseed.push_back(e.variable);
                    }
                if(nonseed.empty()) continue;
                const int z=var();
                solver.phase(-z);
                support_literals.push_back(z);
                if(seed_upper_seen[upper]) {
                    for(int e:nonseed) clause({-e,z});
                } else {
                    for(int i=0;i<(int)nonseed.size();++i)
                        for(int j=i+1;j<(int)nonseed.size();++j)
                            clause({-nonseed[i],-nonseed[j],z});
                }
            }
        at_most(support_literals,support_limit);
        cerr<<"extra_colour_support="<<support_limit
            <<" selectors="<<support_literals.size()<<'\n';
    }
    if(canonicalize) {
        const int fixed_missing=(1<<(rank-1))-1;
        for(int literal:by_lower[fixed_missing]) clause({-literal});
        for(int target=0;target<=full;++target)
            if(target!=fixed_missing&&
               popcount((unsigned)target)==rank-1)
                clause(by_lower[target]);

        // Exact omitted-colour flag moment.  The six rank-six supersets of
        // C0={0,1,2,3,4} are an independent set in the selected path because
        // every edge between two of them has the forbidden lower colour C0.
        // Summing their six degree-two equations says that the selected real
        // cut edges plus selected dummy endpoint edges incident with this set
        // total exactly 12.  This global equality is logically redundant but
        // much more direct for propagation than resolving the six degree
        // constraints together with all C0 edge exclusions.
        auto add_lower_flag_moment=[&](int lower,int total) {
            vector<int> moment;
            for(int id=0;id<(int)edges.size();++id) {
                const Edge&e=edges[id];
                if(e.dummy) {
                    const int v=e.u==dummy?e.v:e.u;
                    if((masks[v]&lower)==lower)
                        moment.push_back(e.variable);
                } else {
                    const bool left=(masks[e.u]&lower)==lower;
                    const bool right=(masks[e.v]&lower)==lower;
                    if(left!=right) moment.push_back(e.variable);
                }
            }
            at_most(moment,total);
            at_least(moment,total);
            cerr<<"lower_flag_moment="<<lower<<" total="<<total
                <<" support="<<moment.size()<<'\n';
        };
        if(getenv("RECOMBINE_C0_MOMENT"))
            add_lower_flag_moment(fixed_missing,12);
        if(getenv("RECOMBINE_PREFIX_MOMENTS")) {
            set<int> prefix_lowers;
            for(int i=0;i+1<(int)canonical_prefix_masks.size();++i)
                prefix_lowers.insert(canonical_prefix_masks[i]&
                                     canonical_prefix_masks[i+1]);
            if(prefix_lowers.size()+1!=canonical_prefix_masks.size()||
               prefix_lowers.count(fixed_missing)) return 9;
            for(int lower:prefix_lowers)add_lower_flag_moment(lower,10);
        }
        if(getenv("RECOMBINE_PREFIX_UPPER_MOMENTS")) {
            set<int> prefix_uppers;
            for(int i=0;i+1<(int)canonical_prefix_masks.size();++i)
                prefix_uppers.insert(canonical_prefix_masks[i]|
                                     canonical_prefix_masks[i+1]);
            for(int upper:prefix_uppers) {
                vector<int> moment;
                for(int id=0;id<(int)edges.size();++id) {
                    const Edge&e=edges[id];
                    if(e.dummy) {
                        const int v=e.u==dummy?e.v:e.u;
                        if((masks[v]&~upper)==0)
                            moment.push_back(e.variable);
                    } else {
                        const bool left=(masks[e.u]&~upper)==0;
                        const bool right=(masks[e.v]&~upper)==0;
                        if(left!=right) moment.push_back(e.variable);
                        else if(left) {
                            // An internal selected edge contributes two to
                            // the degree sum.  Repeating its literal in the
                            // exact counter implements coefficient two.
                            moment.push_back(e.variable);
                            moment.push_back(e.variable);
                        }
                    }
                }
                at_most(moment,14);
                at_least(moment,14);
                cerr<<"upper_flag_moment="<<upper
                    <<" total=14 support_occurrences="<<moment.size()<<'\n';
            }
        }
    }
    if(lower_base||both_base) {
        for(int target=0;target<=full;++target)
            if(popcount((unsigned)target)==rank-1) clause(by_lower[target]);
    } else if(!upper_base)
        for(auto& list:by_lower) for(int i=0;i<(int)list.size();++i)
            for(int j=i+1;j<(int)list.size();++j) clause({-list[i],-list[j]});
    if((!lower_base&&!rainbow_lower)||both_base)
      for(int target=0;target<=full;++target)
        if(popcount((unsigned)target)==rank+1&&!externally_covered[target])
            clause(by_upper[target]);

    // The 461 real edges omit exactly one of the 462 rank-(r-1) colors.
    // That omitted color must be contained in an endpoint, otherwise the
    // missing lower mask cannot be supplied by the boundary factor window.
    if(!upper_base&&!lower_base&&!both_base)
      for(int target=0;target<=full;++target)
      if(popcount((unsigned)target)==rank-1) {
        vector<int> possible=by_lower[target];
        for(int v=0;v<n;++v) if((masks[v]&target)==target) {
            int a=v,b=dummy;if(a>b)swap(a,b);
            possible.push_back(edges[edge_index[{a,b}]].variable);
        }
        clause(possible);
    }

    vector<unsigned char> target_constrained(1<<k);

    // Compact exact witness for one rank-(r-2) or rank-(r+2) target.  At a
    // possible center, the incident support edges split into two groups,
    // according to which of the two excess coordinates they remove (lower
    // target) or which of the two missing coordinates they add (upper
    // target).  A three-vertex window has the requested meet/union exactly
    // when one selected edge comes from each group.  Three hierarchical OR/
    // AND variables per center replace all cross-product pair variables.
    auto add_compact_pair_target=[&](int target) {
        const int wanted=popcount((unsigned)target);
        const bool lower=wanted==rank-2;
        if(!lower&&wanted!=rank+2){clause({});return array<int,3>{0,0,0};}
        vector<int> center_witnesses;
        int group_variables=0,group_edges=0;
        for(int center=0;center<n;++center) {
            const int difference=lower?(masks[center]&~target):
                                       (target&~masks[center]);
            if((lower&&(masks[center]&target)!=target)||
               (!lower&&(masks[center]&~target)!=0)||
               popcount((unsigned)difference)!=2) continue;
            const int first=countr_zero((unsigned)difference);
            const int second=countr_zero((unsigned)(difference&
                                                    (difference-1)));
            array<vector<int>,2> groups;
            for(int id:incident[center]) if(!edges[id].dummy) {
                const Edge&e=edges[id];
                const int neighbor=e.u==center?e.v:e.u;
                if(lower) {
                    if((masks[neighbor]&target)!=target) continue;
                    if(!(masks[neighbor]&(1<<first)))groups[0].push_back(id);
                    else if(!(masks[neighbor]&(1<<second)))groups[1].push_back(id);
                } else {
                    if((masks[neighbor]&~target)!=0) continue;
                    if(masks[neighbor]&(1<<first))groups[0].push_back(id);
                    else if(masks[neighbor]&(1<<second))groups[1].push_back(id);
                }
            }
            if(groups[0].empty()||groups[1].empty())continue;
            array<int,2> present;
            array<bool,2> desired_present={false,false};
            for(int side=0;side<2;++side) {
                present[side]=var(); ++group_variables;
                vector<int> reverse_clause={-present[side]};
                for(int id:groups[side]) {
                    desired_present[side]|=phase_edge[id];
                    clause({-edges[id].variable,present[side]});
                    reverse_clause.push_back(edges[id].variable);
                    ++group_edges;
                }
                solver.phase(desired_present[side]?present[side]:-present[side]);
                clause(reverse_clause);
            }
            const int witness=var(); ++group_variables;
            solver.phase((desired_present[0]&&desired_present[1])?
                         witness:-witness);
            clause({-witness,present[0]});
            clause({-witness,present[1]});
            clause({-present[0],-present[1],witness});
            center_witnesses.push_back(witness);
        }
        clause(center_witnesses);
        return array<int,3>{(int)center_witnesses.size(),group_variables,
                            group_edges};
    };

    // Compact exact witness for one rank-(r-3) or rank-(r+3) target.  Fix a
    // candidate middle edge b--c of a four-vertex path.  Its meet (lower) or
    // union (upper) differs from the target in exactly two coordinates x,y.
    // There are precisely two ways to assign x,y to the two outer edges.
    //
    // For each assignment use one existential gate z with only
    //
    //   z -> selected(b--c),
    //   z -> OR(suitable real outer edges at b),
    //   z -> OR(suitable real outer edges at c).
    //
    // Finally OR all z.  Reverse implications are deliberately unnecessary:
    // after projecting out the z variables, the clauses say exactly that at
    // least one supported three-edge path exists.  Opposite assignments make
    // the two outer endpoints automatically distinct.  This remains exact in
    // a sparse candidate graph because each long clause contains only support
    // edges actually present in that graph.
    auto add_compact_four_target=[&](int target) {
        const int wanted=popcount((unsigned)target);
        const bool lower=wanted==rank-3;
        if(!lower&&wanted!=rank+3) {
            clause({});
            return array<long long,4>{0,0,0,0};
        }
        vector<int> witnesses;
        long long eligible_centers=0,orientation_gates=0,
                  group_edge_occurrences=0;
        for(int middle_id=0;middle_id<(int)edges.size();++middle_id) {
            const Edge&middle=edges[middle_id];
            if(middle.dummy)continue;
            const int b=middle.u,c=middle.v;
            const int core=lower?(masks[b]&masks[c]):(masks[b]|masks[c]);
            const int difference=lower?(core&~target):(target&~core);
            if((lower&&((core&target)!=target))||
               (!lower&&((core&~target)!=0))||
               popcount((unsigned)difference)!=2)continue;
            ++eligible_centers;
            const int first=countr_zero((unsigned)difference);
            const int second=countr_zero((unsigned)(difference&
                                                    (difference-1)));
            for(int orientation=0;orientation<2;++orientation) {
                const int bit_b=orientation?second:first;
                const int bit_c=orientation?first:second;
                array<vector<int>,2> groups;
                for(int side=0;side<2;++side) {
                    const int center=side?c:b;
                    const int bit=side?bit_c:bit_b;
                    for(int id:incident[center]) if(!edges[id].dummy) {
                        const Edge&e=edges[id];
                        const int neighbor=e.u==center?e.v:e.u;
                        if(lower) {
                            if((masks[neighbor]&target)!=target||
                               (masks[neighbor]&(1<<bit)))continue;
                        } else {
                            if((masks[neighbor]&~target)!=0||
                               !(masks[neighbor]&(1<<bit)))continue;
                        }
                        groups[side].push_back(id);
                    }
                }
                if(groups[0].empty()||groups[1].empty())continue;
                const int witness=var();
                bool desired=phase_edge[middle_id];
                clause({-witness,middle.variable});
                for(int side=0;side<2;++side) {
                    vector<int> support={-witness};
                    bool side_desired=false;
                    support.reserve(groups[side].size()+1);
                    for(int id:groups[side]) {
                        support.push_back(edges[id].variable);
                        side_desired|=phase_edge[id];
                    }
                    desired&=side_desired;
                    group_edge_occurrences+=groups[side].size();
                    clause(support);
                }
                solver.phase(desired?witness:-witness);
                witnesses.push_back(witness);
                ++orientation_gates;
            }
        }
        clause(witnesses);
        return array<long long,4>{eligible_centers,orientation_gates,
                                  orientation_gates,
                                  group_edge_occurrences};
    };

    // Pair-of-incident-edge witnesses encode three consecutive vertices and
    // simultaneously cover the rank-4 intersection and rank-8 union layers.
    // The compact option is logically equivalent but avoids materializing
    // every cross-product pair.
    if(use_pair) {
    if(compact_pair_shadows) {
        long long centers=0,compact_variables=0,edge_occurrences=0;
        for(int target=0;target<=full;++target) {
            const int wanted=popcount((unsigned)target);
            if((pair_cover4&&wanted==rank-2)||
               (pair_cover8&&wanted==rank+2)) {
                const auto stats=add_compact_pair_target(target);
                target_constrained[target]=1;
                centers+=stats[0];compact_variables+=stats[1];
                edge_occurrences+=stats[2];
            }
        }
        cerr<<"compact_pair_shadows=1 centers="<<centers
            <<" variables="<<compact_variables
            <<" group_edge_occurrences="<<edge_occurrences<<'\n';
    } else {
    vector<vector<int>> cover4(1<<k),cover8(1<<k);
    for(int center=0;center<n;++center) {
        vector<int> real;
        for(int id:incident[center]) if(!edges[id].dummy) real.push_back(id);
        for(int i=0;i<(int)real.size();++i) for(int j=i+1;j<(int)real.size();++j) {
            const Edge&a=edges[real[i]],&b=edges[real[j]];
            const int left=a.u==center?a.v:a.u, right=b.u==center?b.v:b.u;
            if(left==right) continue;
            const int w=var();
            solver.phase((phase_edge[real[i]]&&phase_edge[real[j]])?w:-w);
            clause({-w,a.variable}); clause({-w,b.variable});
            clause({-a.variable,-b.variable,w});
            const int meet=masks[left]&masks[center]&masks[right];
            const int join=masks[left]|masks[center]|masks[right];
            if(pair_cover4&&popcount((unsigned)meet)==rank-2)
                cover4[meet].push_back(w);
            if(pair_cover8&&popcount((unsigned)join)==rank+2)
                cover8[join].push_back(w);
        }
    }
    for(int target=0;target<=full;++target) {
        if(pair_cover4&&popcount((unsigned)target)==rank-2)
            { clause(cover4[target]); target_constrained[target]=1; }
        if(pair_cover8&&popcount((unsigned)target)==rank+2)
            { clause(cover8[target]); target_constrained[target]=1; }
    }
    }
    }

    // Enumerate unoriented simple real paths on four vertices.  Their three
    // selected edges witness the rank-3 intersection and rank-9 union layers.
    if(use_quad) {
    if(compact_four_shadows) {
        long long centers=0,gates=0,compact_variables=0,
                  group_edge_occurrences=0;
        for(int target=0;target<=full;++target) {
            const int wanted=popcount((unsigned)target);
            if(wanted==rank-3||wanted==rank+3) {
                const auto stats=add_compact_four_target(target);
                target_constrained[target]=1;
                centers+=stats[0];gates+=stats[1];
                compact_variables+=stats[2];
                group_edge_occurrences+=stats[3];
            }
        }
        cerr<<"compact_four_shadows=1 centers="<<centers
            <<" orientation_gates="<<gates
            <<" variables="<<compact_variables
            <<" group_edge_occurrences="<<group_edge_occurrences<<'\n';
    } else {
    vector<vector<int>> cover3(1<<k),cover9(1<<k);
    for(int b=0;b<n;++b) for(int ebc:incident[b]) if(!edges[ebc].dummy) {
        int c=edges[ebc].u==b?edges[ebc].v:edges[ebc].u;
        for(int eab:incident[b]) if(!edges[eab].dummy && eab!=ebc) {
            int a=edges[eab].u==b?edges[eab].v:edges[eab].u;
            if(a==c) continue;
            for(int ecd:incident[c]) if(!edges[ecd].dummy && ecd!=ebc) {
                int d=edges[ecd].u==c?edges[ecd].v:edges[ecd].u;
                if(d==a||d==b||a>d) continue;
                const int w=var();
                solver.phase((phase_edge[eab]&&phase_edge[ebc]&&
                              phase_edge[ecd])?w:-w);
                clause({-w,edges[eab].variable});
                clause({-w,edges[ebc].variable});
                clause({-w,edges[ecd].variable});
                clause({-edges[eab].variable,-edges[ebc].variable,
                        -edges[ecd].variable,w});
                const int meet=masks[a]&masks[b]&masks[c]&masks[d];
                const int join=masks[a]|masks[b]|masks[c]|masks[d];
                if(popcount((unsigned)meet)==rank-3) cover3[meet].push_back(w);
                if(popcount((unsigned)join)==rank+3) cover9[join].push_back(w);
            }
        }
    }
    for(int target=0;target<=full;++target) {
        if(popcount((unsigned)target)==rank-3)
            { clause(cover3[target]); target_constrained[target]=1; }
        if(popcount((unsigned)target)==rank+3)
            { clause(cover9[target]); target_constrained[target]=1; }
    }
    }
    }

    // Forbid internal coordinate runs of lengths 1, 2, and 3.  Paths touching
    // the dummy are endpoints and are intentionally not forbidden.
    if(use_runs) for(int bit=0;bit<k;++bit) {
        for(int b=0;b<n;++b) if(masks[b]&(1<<bit)) {
            vector<int> outs;
            for(int id:incident[b]) if(!edges[id].dummy) {
                int a=edges[id].u==b?edges[id].v:edges[id].u;
                if(!(masks[a]&(1<<bit))) outs.push_back(id);
            }
            for(int i=0;i<(int)outs.size();++i) for(int j=i+1;j<(int)outs.size();++j)
                clause({-edges[outs[i]].variable,-edges[outs[j]].variable});
        }
        if(factor_d>=2) for(int b=0;b<n;++b) if(masks[b]&(1<<bit))
            for(int ebc:incident[b]) if(!edges[ebc].dummy) {
                int c=edges[ebc].u==b?edges[ebc].v:edges[ebc].u;
                if(c<b || !(masks[c]&(1<<bit))) continue;
                for(int eab:incident[b]) if(!edges[eab].dummy && eab!=ebc) {
                    int a=edges[eab].u==b?edges[eab].v:edges[eab].u;
                    if(masks[a]&(1<<bit)) continue;
                    for(int ecd:incident[c]) if(!edges[ecd].dummy && ecd!=ebc) {
                        int d=edges[ecd].u==c?edges[ecd].v:edges[ecd].u;
                        if(!(masks[d]&(1<<bit)))
                            clause({-edges[eab].variable,-edges[ebc].variable,-edges[ecd].variable});
                    }
                }
            }
        if(factor_d>=3) for(int b=0;b<n;++b) if(masks[b]&(1<<bit))
            for(int ebc:incident[b]) if(!edges[ebc].dummy) {
                int c=edges[ebc].u==b?edges[ebc].v:edges[ebc].u;
                if(!(masks[c]&(1<<bit))) continue;
                for(int ecd:incident[c]) if(!edges[ecd].dummy && ecd!=ebc) {
                    int d=edges[ecd].u==c?edges[ecd].v:edges[ecd].u;
                    if(!(masks[d]&(1<<bit))) continue;
                    for(int eab:incident[b]) if(!edges[eab].dummy && eab!=ebc) {
                        int a=edges[eab].u==b?edges[eab].v:edges[eab].u;
                        if(masks[a]&(1<<bit)) continue;
                        for(int ede:incident[d]) if(!edges[ede].dummy && ede!=ecd) {
                            int e=edges[ede].u==d?edges[ede].v:edges[ede].u;
                            if(!(masks[e]&(1<<bit)))
                                clause({-edges[eab].variable,-edges[ebc].variable,
                                        -edges[ecd].variable,-edges[ede].variable});
                        }
                    }
                }
            }
    }

    // Add, on demand, all candidate selected-edge paths whose Boolean meet or
    // join is a requested target.  Delaying these constraints until a target
    // is actually missing keeps the full-Johnson-graph model compact.
    auto constrain_target=[&](int target) {
        if(target_constrained[target]) return;
        target_constrained[target]=1;
        const int wanted=popcount((unsigned)target);
        if(compact_pair_shadows&&abs(wanted-rank)==2) {
            const auto stats=add_compact_pair_target(target);
            cerr<<" constrain="<<target<<" rank="<<wanted
                <<" compact_centers="<<stats[0]
                <<" compact_variables="<<stats[1]
                <<" group_edge_occurrences="<<stats[2]<<'\n';
            return;
        }
        if(compact_four_shadows&&abs(wanted-rank)==3) {
            const auto stats=add_compact_four_target(target);
            cerr<<" constrain="<<target<<" rank="<<wanted
                <<" compact_centers="<<stats[0]
                <<" orientation_gates="<<stats[1]
                <<" compact_variables="<<stats[2]
                <<" group_edge_occurrences="<<stats[3]<<'\n';
            return;
        }
        const bool lower=wanted<rank;
        const int vertex_count=abs(wanted-rank)+1;
        vector<int> witnesses,path_vertices,path_edges;
        vector<unsigned char> used(n);
        auto allowed_vertex=[&](int v) {
            return lower ? (masks[v]&target)==target : (masks[v]&~target)==0;
        };
        auto dfs=[&](auto&& self,int v,int aggregate) -> void {
            if((int)path_vertices.size()==vertex_count) {
                if(aggregate!=target || path_vertices.front()>path_vertices.back()) return;
                const int w=var(); witnesses.push_back(w);
                for(int id:path_edges) clause({-w,edges[id].variable});
                vector<int> reverse_clause;
                reverse_clause.reserve(path_edges.size()+1);
                for(int id:path_edges) reverse_clause.push_back(-edges[id].variable);
                reverse_clause.push_back(w);
                clause(reverse_clause);
                return;
            }
            for(int id:incident[v]) if(!edges[id].dummy) {
                const Edge&e=edges[id]; const int u=e.u==v?e.v:e.u;
                if(used[u]||!allowed_vertex(u)) continue;
                used[u]=1;path_vertices.push_back(u);path_edges.push_back(id);
                self(self,u,lower?(aggregate&masks[u]):(aggregate|masks[u]));
                path_edges.pop_back();path_vertices.pop_back();used[u]=0;
            }
        };
        for(int start=0;start<n;++start) if(allowed_vertex(start)) {
            used[start]=1;path_vertices={start};path_edges.clear();
            dfs(dfs,start,masks[start]);used[start]=0;
        }
        cerr<<" constrain="<<target<<" rank="<<wanted
            <<" witnesses="<<witnesses.size()<<'\n';
        clause(witnesses);
    };

    if(const char* initial_targets=getenv("RECOMBINE_TARGETS")) {
        ifstream target_input(initial_targets);
        for(int target;target_input>>target;)constrain_target(target);
    }

    cerr<<"vertices="<<n<<" real_edges="<<pairs.size()<<" variables="<<variables<<'\n';
    if(dump_cnf_path) {
        ofstream dump(dump_cnf_path);
        dump << "p cnf " << variables << ' ' << recorded_clauses.size() << '\n';
        for(const vector<int>& c:recorded_clauses) {
            for(int literal:c) dump << literal << ' ';
            dump << "0\n";
        }
        dump.close();
        cerr << "dumped_cnf=" << dump_cnf_path
             << " clauses=" << recorded_clauses.size() << '\n';
        if(getenv("RECOMBINE_DUMP_ONLY")) return 0;
    }
    for(int round=0;;++round) {
        if(solver.solve()!=10) { cerr<<"UNSAT round="<<round<<'\n'; return 1; }
        vector<vector<int>> selected(n+1);
        for(const Edge&e:edges) if(solver.val(e.variable)>0) {
            selected[e.u].push_back(e.v); selected[e.v].push_back(e.u);
        }
        vector<int> component(n+1,-1); vector<vector<int>> comps;
        for(int start=0;start<=n;++start) if(component[start]<0) {
            int id=comps.size(); comps.push_back({}); queue<int>q; q.push(start);component[start]=id;
            while(!q.empty()){int u=q.front();q.pop();comps.back().push_back(u);
                for(int v:selected[u])if(component[v]<0){component[v]=id;q.push(v);}}
        }
        cerr<<"round="<<round<<" cycles="<<comps.size();for(auto&c:comps)cerr<<' '<<c.size();cerr<<'\n';
        if(comps.size()==1) {
            vector<int> order; int previous=dummy,current=selected[dummy][0];
            while(current!=dummy){order.push_back(current);int next=selected[current][0]==previous?selected[current][1]:selected[current][0];previous=current;current=next;}
            if((int)order.size()!=n)return 7;
            if(lazy_full) {
                bool refined=false;
                // Coordinate factorability: an internal run of ones in the
                // prescribed central row must have length at least d+1=4.
                if(!shadow_only) for(int bit=0;bit<k;++bit) {
                    int i=0;
                    while(i<n) {
                        if(!(masks[order[i]]&(1<<bit))){++i;continue;}
                        const int first=i;
                        while(i<n&&(masks[order[i]]&(1<<bit)))++i;
                        if(first&&i<n&&i-first<=factor_d) {
                            vector<int> forbid;
                            for(int j=first-1;j<i;++j) {
                                int a=order[j],b=order[j+1];if(a>b)swap(a,b);
                                forbid.push_back(-edges[edge_index[{a,b}]].variable);
                            }
                            clause(forbid); refined=true;
                        }
                    }
                }
                vector<unsigned char> covered=externally_covered;
                for(int v:order) covered[masks[v]]=1;
                for(int length=2;length<=factor_d+1;++length)
                    for(int left=0;left+length<=n;++left) {
                        int value=full;
                        for(int j=left;j<left+length;++j)value&=masks[order[j]];
                        if(popcount((unsigned)value)==rank-length+1)covered[value]=1;
                    }
                for(int length=2;rank+length-1<=k;++length)
                    for(int left=0;left+length<=n;++left) {
                        int value=0;
                        for(int j=left;j<left+length;++j)value|=masks[order[j]];
                        if(popcount((unsigned)value)==rank+length-1)covered[value]=1;
                    }
                for(int target=1;target<=full;++target) if(!covered[target]) {
                    const int r=popcount((unsigned)target);
                    if(upper_base&&r<rank) continue;
                    if(lower_base&&r>rank) continue;
                    if(upper_base_runs) continue;
                    if(lower_base_runs) continue;
                    if(rainbow_lower_runs) continue;
                    // Exactly one rank-(r-1) edge color is absent; the
                    // endpoint clause above makes it available to the factor
                    // as a truncated boundary window.
                    if(r==rank-1) continue;
                    if((r>=rank-factor_d&&r<=rank-2)||
                       (r>=rank+2&&r<=rank+3)) {
                        constrain_target(target); refined=true;
                    } else if(r>=rank-factor_d) {
                        // Ranks 4--8 are enforced above.  Ranks 10--11 are
                        // normally automatic; if one is absent, exclude this
                        // exact path and let the solver produce another one.
                        vector<int> block;
                        for(int j=0;j+1<n;++j) {
                            int a=order[j],b=order[j+1];if(a>b)swap(a,b);
                            block.push_back(-edges[edge_index[{a,b}]].variable);
                        }
                        clause(block); refined=true; break;
                    }
                }
                if(refined) continue;
            }
            for(int v:order)cout<<masks[v]<<' ';cout<<'\n';return 0;
        }
        for(auto&comp:comps) if(comp.size()!=n+1) {
            vector<unsigned char> inside(n+1);for(int v:comp)inside[v]=1;vector<int> cut;
            for(const Edge&e:edges)if(inside[e.u]!=inside[e.v])cut.push_back(e.variable);
            clause(cut);
        }
    }
}
