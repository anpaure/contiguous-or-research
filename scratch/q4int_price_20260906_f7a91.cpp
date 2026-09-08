// Asymmetric all-split, all-strict-chain pricing, for a residual point demand.
#include <algorithm>
#include <array>
#include <cmath>
#include <functional>
#include <queue>
#include <random>
#include <vector>

struct Grid {
    int d, n;
    std::vector<std::vector<int>> points, successors, predecessors;
    explicit Grid(int dimension): d(dimension), n(1 << (2*d)), points(n,std::vector<int>(d)),
                                  successors(n), predecessors(n) {
        for (int i=0;i<n;++i) {
            int x=i;
            for (int j=d-1;j>=0;--j) { points[i][j]=x%4; x/=4; }
            int stride=1;
            for (int j=d-1;j>=0;--j) {
                if (points[i][j]) predecessors[i].push_back(i-stride);
                stride*=4;
            }
        }
        for (int i=0;i<n;++i) for (int j=i+1;j<n;++j) {
            bool ok=true;
            for (int k=0;k<d;++k) ok &= points[i][k]<=points[j][k];
            if (ok) successors[i].push_back(j);
        }
    }
};

struct Split {
    int mask;
    Grid left,right;
    std::vector<std::vector<int>> cells;
    explicit Split(int m): mask(m), left(__builtin_popcount(unsigned(m))), right(6-left.d),
                           cells(left.n,std::vector<int>(right.n)) {
        for (int i=0;i<left.n;++i) for (int j=0;j<right.n;++j) {
            int a=0,b=0,x=0;
            for (int k=0;k<6;++k) x=4*x+((mask>>k)&1 ? left.points[i][a++] : right.points[j][b++]);
            cells[i][j]=x;
        }
    }
};

extern "C" int price_q4int(const double* dual, int limit, int seed, int* output, double* maximum) {
    static std::vector<Split> splits;
    if (splits.empty()) for (int mask=1;mask<63;++mask) {
        int r=__builtin_popcount(unsigned(mask));
        if (r<3 || (r==3 && (mask&1))) splits.emplace_back(mask);
    }
    struct Candidate {
        double priority;
        std::array<int,23> row;
        bool operator<(const Candidate& other) const { return priority>other.priority; }
    };
    std::mt19937 rng(seed);
    std::priority_queue<Candidate> heap;
    *maximum=0;
    for (const Split& s:splits) {
        const int a=s.left.n,b=s.right.n;
        std::vector<std::vector<double>> table(a,std::vector<double>(b));
        std::vector<bool> allowed(a,false);
        for (int i=0;i<a;++i) for (int j=0;j<b;++j) {
            table[i][j]=dual[s.cells[i][j]];
            allowed[i]=allowed[i] || table[i][j]>1e-10;
        }
        std::vector<double> sums(b),best(b);
        std::vector<int> previous(b),chain;
        std::function<void(int)> extend=[&](int i) {
            chain.push_back(i);
            for (int j=0;j<b;++j) sums[j]+=table[i][j];
            for (int j=0;j<b;++j) {
                double value=0;
                int pred=-1;
                for (int k:s.right.predecessors[j]) if (best[k]>value) { value=best[k]; pred=k; }
                previous[j]=pred;
                best[j]=value+std::max(0.0,sums[j]-1.0);
            }
            double reduced=best.back()-chain.size();
            *maximum=std::max(*maximum,reduced);
            if (reduced>1e-7) {
                double priority=reduced+1e-8*(double(rng())/rng.max());
                if (int(heap.size())<limit || priority>heap.top().priority) {
                    Candidate c{};
                    c.priority=priority;
                    c.row[0]=s.mask; c.row[1]=int(chain.size());
                    for (int h=0;h<int(chain.size());++h) c.row[3+h]=chain[h];
                    std::vector<int> d;
                    for (int j=b-1;j>=0;j=previous[j]) if (sums[j]>1+1e-10) d.push_back(j);
                    std::reverse(d.begin(),d.end());
                    c.row[2]=int(d.size());
                    for (int h=0;h<int(d.size());++h) c.row[3+chain.size()+h]=d[h];
                    if (int(heap.size())==limit) heap.pop();
                    heap.push(c);
                }
            }
            for (int j:s.left.successors[i]) if (allowed[j]) extend(j);
            for (int j=0;j<b;++j) sums[j]-=table[i][j];
            chain.pop_back();
        };
        for (int i=0;i<a;++i) if (allowed[i]) extend(i);
    }
    int n=0;
    while (!heap.empty()) {
        for (int j=0;j<23;++j) output[23*n+j]=heap.top().row[j];
        ++n; heap.pop();
    }
    return n;
}
