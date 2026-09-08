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
#include <fstream>
#include <iostream>
#include <limits>
#include <string>
#include <vector>

using namespace std;

static long long choose_value(int n,int r){
    if(r<0||r>n)return 0;
    r=min(r,n-r);long long value=1;
    for(int i=1;i<=r;++i)value=value*(n-r+i)/i;
    return value;
}

static int safe_bound(int k,int n,int rank){
    long long bound=(long long)n-choose_value(k,rank)+1;
    for(int higher=rank+1;higher<=k;++higher)
        bound=min(bound,(long long)n-choose_value(k,higher));
    return static_cast<int>(max<long long>(0,min<long long>(n,bound)));
}

struct PhaseInterval { int left=0,right=0,value=0,cost=0; };
struct CentralOffsets { int L0=0,R0=0,left=0,right=0; };

int main(int argc,char**argv){
    if(argc<5||argc>6){
        cerr<<"usage: program k n seed_array output_array [sat_seed]\n";
        return 2;
    }
    const int k=stoi(argv[1]),n=stoi(argv[2]),limit=1<<k;
    const int sat_seed=argc==6?stoi(argv[5]):1;
    vector<int> seed;
    {ifstream input(argv[3]);for(int value;input>>value;)seed.push_back(value);}
    if((int)seed.size()!=n)return 3;

    long long variable_total=(long long)n*k;
    for(int target=1;target<limit;++target)
        variable_total+=(long long)n*(3+popcount((unsigned)target));
    if(variable_total>numeric_limits<int>::max())return 4;

    CaDiCaL::Solver solver;
    solver.set("quiet",1);
    solver.set("seed",sat_seed);
    // Reserve room for explicit equal-rank endpoint distinctness below.
    solver.declare_more_variables((int)variable_total+2000000);
    auto add=[&](initializer_list<int> clause){
        for(int literal:clause)solver.add(literal);solver.add(0);
    };
    auto add_vector=[&](const vector<int>&clause){
        for(int literal:clause)solver.add(literal);solver.add(0);
    };
    auto A=[&](int position,int bit){return 1+position*k+bit;};
    for(int position=0;position<n;++position){
        vector<int> nonzero;
        for(int bit=0;bit<k;++bit){
            const int variable=A(position,bit);
            solver.phase(seed[position]&(1<<bit)?variable:-variable);
            nonzero.push_back(variable);
        }
        add_vector(nonzero);
    }

    int next=n*k+1;
    int phase_exact=0;
    long long clauses= n;
    vector<CentralOffsets> central[2]; // ranks 5 and 6 for k=11.
    for(int target=1;target<limit;++target){
        const int rank=popcount((unsigned)target);
        const int bound=safe_bound(k,n,rank);
        PhaseInterval best;
        best.cost=numeric_limits<int>::max();
        for(int left=0;left<n;++left){
            int value=0;
            for(int right=left;right<n&&right-left+1<=bound;++right){
                value|=seed[right];
                const int difference=popcount((unsigned)(value^target));
                // Exact existing witnesses dominate.  Otherwise prefer the
                // smallest bit discrepancy and then a short interval.
                const int cost=1024*difference+(right-left+1);
                if(cost<best.cost)best={left,right,value,cost};
            }
        }
        if(best.value==target)++phase_exact;

        const int L0=next;next+=n;
        const int R0=next;next+=n;
        const int M0=next;next+=n;
        vector<int> H0(k,-1);
        for(int bit=0;bit<k;++bit)if(target&(1<<bit)){H0[bit]=next;next+=n;}
        auto L=[&](int position){return L0+position;};
        auto R=[&](int position){return R0+position;};
        auto M=[&](int position){return M0+position;};
        auto H=[&](int bit,int position){return H0[bit]+position;};
        if(k==11&&(rank==5||rank==6))
            central[rank-5].push_back({L0,R0,best.left,best.right});
        for(int position=0;position<n;++position){
            solver.phase(position>=best.left?L(position):-L(position));
            solver.phase(position<=best.right?R(position):-R(position));
            solver.phase(position>=best.left&&position<=best.right?
                         M(position):-M(position));
        }

        add({L(n-1)});++clauses;
        for(int position=0;position+1<n;++position){
            add({-L(position),L(position+1)});++clauses;
        }
        add({R(0)});++clauses;
        for(int position=0;position+1<n;++position){
            add({-R(position+1),R(position)});++clauses;
        }
        vector<int> some_m;some_m.reserve(n);
        for(int position=0;position<n;++position){
            add({-M(position),L(position)});
            add({-M(position),R(position)});
            add({-L(position),-R(position),M(position)});
            clauses+=3;some_m.push_back(M(position));
        }
        add_vector(some_m);++clauses;
        if(bound<=0){solver.add(0);++clauses;}
        else if(bound<n)for(int position=0;position+bound<n;++position){
            add({-M(position),-M(position+bound)});++clauses;
        }
        for(int bit=0;bit<k;++bit){
            if(!(target&(1<<bit))){
                for(int position=0;position<n;++position){
                    add({-M(position),-A(position,bit)});++clauses;
                }
            }else{
                int phase_occurrence=best.left;
                for(int position=best.left;position<=best.right;++position)
                    if(seed[position]&(1<<bit)){phase_occurrence=position;break;}
                vector<int> occurrence;occurrence.reserve(n);
                for(int position=0;position<n;++position){
                    const int h=H(bit,position);
                    solver.phase(position==phase_occurrence?h:-h);
                    add({-h,M(position)});
                    add({-h,A(position,bit)});
                    clauses+=2;occurrence.push_back(h);
                }
                add_vector(occurrence);++clauses;
            }
        }
    }
    if(next-1!=variable_total){
        cerr<<"variable mismatch "<<next-1<<' '<<variable_total<<'\n';return 5;
    }

    // Equal-rank target intervals have distinct left endpoints and distinct
    // right endpoints.  This follows mathematically from incomparability but
    // is very indirect in the raw bit clauses.  Materialize each start/end
    // transition and add sequential at-most-one constraints at every physical
    // position.  For k=11 this explicitly exposes the two 462-of-465 endpoint
    // injections behind the six-component forest theorem.
    auto at_most_one=[&](const vector<int>& literals,const vector<uint8_t>& phase){
        if(literals.size()<2)return;
        int prefix=next++;
        solver.phase(phase[0]?prefix:-prefix);
        add({-literals[0],prefix});++clauses;
        bool phase_prefix=phase[0];
        for(int i=1;i+1<(int)literals.size();++i){
            const int current=next++;
            phase_prefix=phase_prefix||phase[i];
            solver.phase(phase_prefix?current:-current);
            add({-literals[i],current});
            add({-prefix,current});
            add({-literals[i],-prefix});
            clauses+=3;prefix=current;
        }
        add({-literals.back(),-prefix});++clauses;
    };
    for(int layer=0;layer<2;++layer){
        const int count=central[layer].size();
        if(k==11&&count!=462)return 6;
        vector<vector<int>> starts(n),ends(n);
        vector<vector<uint8_t>> start_phase(n),end_phase(n);
        for(const CentralOffsets& value:central[layer]){
            for(int position=0;position<n;++position){
                const int start=next++,end=next++;
                solver.phase(position==value.left?start:-start);
                solver.phase(position==value.right?end:-end);
                starts[position].push_back(start);
                ends[position].push_back(end);
                start_phase[position].push_back(position==value.left);
                end_phase[position].push_back(position==value.right);
                const int lp=value.L0+position;
                if(position==0){
                    add({-start,lp});add({-lp,start});clauses+=2;
                }else{
                    const int previous=value.L0+position-1;
                    add({-start,lp});add({-start,-previous});
                    add({-lp,previous,start});clauses+=3;
                }
                const int rp=value.R0+position;
                if(position+1==n){
                    add({-end,rp});add({-rp,end});clauses+=2;
                }else{
                    const int following=value.R0+position+1;
                    add({-end,rp});add({-end,-following});
                    add({-rp,following,end});clauses+=3;
                }
            }
        }
        for(int position=0;position<n;++position){
            at_most_one(starts[position],start_phase[position]);
            at_most_one(ends[position],end_phase[position]);
        }
    }
    cerr<<"variables="<<variable_total<<" clauses="<<clauses
        <<" actual_variables="<<next-1
        <<" exact_phase_targets="<<phase_exact<<'/'<<(limit-1)<<'\n';
    const int result=solver.solve();
    if(result!=10){cerr<<(result==20?"UNSAT":"UNKNOWN")<<'\n';return 1;}
    ofstream output(argv[4]);
    for(int position=0;position<n;++position){
        int value=0;
        for(int bit=0;bit<k;++bit)
            if(solver.val(A(position,bit))>0)value|=1<<bit;
        output<<value<<' ';
    }
    output<<'\n';
    cerr<<"SAT\n";
    return 0;
}
