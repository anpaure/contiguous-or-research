#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <algorithm>
#include <bit>
#include <fstream>
#include <iostream>
#include <limits>
#include <vector>
using namespace std;

struct Eval { int deficit=0, lower=0, upper=0, covered=0; };

static Eval evaluate(const vector<int>& path, int k, int rank, int d) {
    Eval e;
    for (int bit=0; bit<k; ++bit) {
        int i=0;
        while (i<(int)path.size()) {
            if (!(path[i]&(1<<bit))) { ++i; continue; }
            const int first=i;
            while (i<(int)path.size() && (path[i]&(1<<bit))) ++i;
            if (first && i<(int)path.size()) e.deficit += max(0,d+1-(i-first));
        }
    }
    vector<unsigned char> seen(1<<k);
    auto record=[&](int x,int wanted){
        if (popcount((unsigned)x)!=wanted || seen[x]) return;
        seen[x]=1; ++e.covered;
        if (wanted<rank) ++e.lower;
        if (wanted>rank) ++e.upper;
    };
    for (int x:path) record(x,rank);
    const int full=(1<<k)-1;
    for (int length=2; length<=d+1; ++length)
        for (int left=0; left+length<=(int)path.size(); ++left) {
            int x=full;
            for (int j=left;j<left+length;++j) x&=path[j];
            record(x,rank-length+1);
        }
    for (int length=2; rank+length-1<=k; ++length)
        for (int left=0; left+length<=(int)path.size(); ++left) {
            int x=0;
            for (int j=left;j<left+length;++j) x|=path[j];
            record(x,rank+length-1);
        }
    return e;
}

int main(int argc,char**argv) {
    if (argc!=5) return 2;
    const int k=stoi(argv[1]), rank=stoi(argv[2]), d=stoi(argv[3]);
    const string cycle_path=argv[4];
    const int full=(1<<k)-1;
    vector<int> t;
    for(int x;cin>>x;) t.push_back(x);
    vector<unsigned char> seen(1<<k);
    for(int i=0;i+1<(int)t.size();++i) {
        if(popcount((unsigned)(t[i]^t[i+1]))!=2) return 3;
        seen[t[i]&t[i+1]]=1;
    }
    int missing=-1;
    for(int x=0;x<=full;++x)
        if(popcount((unsigned)x)==rank-1 && !seen[x]) {
            if(missing>=0) return 4;
            missing=x;
        }
    if(missing<0) return 4;
    if (missing & ~t.front()) {
        if (missing & ~t.back()) return 5;
        reverse(t.begin(),t.end());
    }

    vector<int> best;
    Eval best_eval; best_eval.deficit=numeric_limits<int>::max();
    for(int i=0;i+1<(int)t.size();++i) {
        const int edge=t[i]&t[i+1];
        if (edge & ~t.back()) continue;
        if (missing & ~t[i+1]) continue;
        vector<int> candidate=t;
        reverse(candidate.begin()+i+1,candidate.end());
        bool valid=true;
        for(int j=0;j+1<(int)candidate.size();++j)
            valid &= popcount((unsigned)(candidate[j]^candidate[j+1]))==2;
        if(!valid || (missing&~candidate.front()) || (missing&~candidate.back())) continue;
        Eval cur=evaluate(candidate,k,rank,d);
        if(cur.deficit<best_eval.deficit ||
           (cur.deficit==best_eval.deficit && cur.lower>best_eval.lower) ||
           (cur.deficit==best_eval.deficit && cur.lower==best_eval.lower &&
            cur.upper>best_eval.upper)) {
            best=move(candidate); best_eval=cur;
        }
    }
    if(best.empty()) return 6;

    vector<int> permutation(k,-1), inside, outside;
    for(int bit=0;bit<k;++bit)
        ((missing&(1<<bit))?inside:outside).push_back(bit);
    for(int i=0;i<(int)inside.size();++i) permutation[inside[i]]=i;
    for(int i=0;i<(int)outside.size();++i) permutation[outside[i]]=inside.size()+i;
    auto permute=[&](int x){int y=0;for(int b=0;b<k;++b)if(x&(1<<b))y|=1<<permutation[b];return y;};

    ofstream cycle(cycle_path);
    cycle << permute(missing) << ' ';
    for(int i=0;i<(int)best.size();++i) {
        cycle << permute(best[i]) << ' ';
        if(i+1<(int)best.size()) cycle << permute(best[i]&best[i+1]) << ' ';
    }
    cycle << '\n';
    cerr << "missing="<<missing<<" deficit="<<best_eval.deficit
         <<" lower="<<best_eval.lower<<" upper="<<best_eval.upper<<'\n';
    for(int x:best) cout<<x<<' ';
    cout<<'\n';
}
