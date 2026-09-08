#pragma GCC optimize("O3,unroll-loops")
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")

#include <algorithm>
#include <atomic>
#include <chrono>
#include <cmath>
#include <fstream>
#include <iostream>
#include <mutex>
#include <random>
#include <string>
#include <tuple>
#include <vector>
#include <omp.h>

using namespace std;

struct Point { int x, y, z; };
static bool adjacent(const Point& p, const Point& q) {
    int dx=abs(p.x-q.x), dy=abs(p.y-q.y), dz=abs(p.z-q.z);
    return dx+dy+dz==2 && max({dx,dy,dz})==1;
}

static vector<Point> ring(int radius) {
    const int d[6][3]={{0,1,-1},{-1,1,0},{-1,0,1},{0,-1,1},{1,-1,0},{1,0,-1}};
    vector<Point> v; int x=radius,y=-radius,z=0;
    for(auto& e:d) for(int s=0;s<radius;++s){v.push_back({x,y,z});x+=e[0];y+=e[1];z+=e[2];}
    return v;
}
static vector<Point> spiral(int a){
    const int d[6][3]={{0,-1,1},{1,-1,0},{1,0,-1},{0,1,-1},{-1,1,0},{-1,0,1}};
    vector<Point> v;
    for(int r=a;r>=1;--r){int x=-r,y=r,z=0;for(auto&e:d)for(int s=0;s<r;++s){v.push_back({a+x,a+y,a+z});x+=e[0];y+=e[1];z+=e[2];}}
    v.push_back({a,a,a});return v;
}
static vector<Point> snake(int a){vector<Point>v;for(int x=0;x<=2*a;++x){int lo=max(0,a-x),hi=min(2*a,3*a-x);if(x%2==0)for(int y=lo;y<=hi;++y)v.push_back({x,y,3*a-x-y});else for(int y=hi;y>=lo;--y)v.push_back({x,y,3*a-x-y});}return v;}

struct Run {int l,r;};
struct Score {
    long long capacity=0;
    int full=0;
    long long penalty=0;
    int bad=0;
    int runs=0;
    auto key() const { return tuple<long long,int,long long,int,int>(capacity,full,-penalty,-bad,-runs); }
};

static vector<Run> internal_runs(const vector<Point>& p,int a){
    int side=2*a,m=p.size(); vector<Run> out;
    for(int block=0;block<3;++block)for(int h=1;h<=side;++h){
        auto has=[&](int i){int c=block==0?p[i].x:block==1?p[i].y:p[i].z;return c>=h;};
        for(int i=0;i<m;){if(!has(i)){++i;continue;}int j=i;while(j+1<m&&has(j+1))++j;if(i>0&&j+1<m)out.push_back({i,j});i=j+1;}
    }return out;
}
static Score evaluate(const vector<Point>& p,int a,int D){
    auto runs=internal_runs(p,a); int m=p.size(); vector<pair<int,int>> arc;
    Score s; s.runs=runs.size();
    for(auto r:runs){int len=r.r-r.l+1;int def=max(0,D-len+1);if(def){s.penalty+=1LL*def*def;s.bad++;arc.push_back({r.l-1,r.r+1});}}
    for(int B=0;B<m;++B){int q=m;for(auto [left,right]:arc)if(left>=B)q=min(q,right);int A=q-1;s.full=max(s.full,max(0,A-B+1));}
    auto capacity_of=[&](const vector<int>& alpha,const vector<int>& beta){
        long long cap=0;int previous=0;
        for(int i=0;i<m;++i){int d=alpha[i]-previous;cap+=1LL*(d+1)*beta[i]-1LL*(previous+alpha[i])*(d+1)/2;previous=alpha[i];}
        int tail=D-alpha.back();cap+=1LL*tail*(tail+1)/2;return cap;
    };
    vector<int> alpha(m,0),beta(m,D),requirement(m,0);
    for(auto r:runs){int q=r.r+1,c=r.r-r.l;requirement[q]=max(requirement[q],D-c);}
    for(int i=0;i<m;++i)alpha[i]=max(i?alpha[i-1]:0,requirement[i]);
    long long saturated=capacity_of(alpha,beta);
    vector<int> upper(m,D);
    for(auto r:runs){int pp=r.l-1,c=r.r-r.l;upper[pp]=min(upper[pp],c);}
    for(int i=m-2;i>=0;--i)upper[i]=min(upper[i],upper[i+1]);
    vector<int> zero_alpha(m,0);long long zero=capacity_of(zero_alpha,upper);
    s.capacity=max(saturated,zero);
    return s;
}
static bool valid_path(const vector<Point>& p){for(int i=0;i+1<(int)p.size();++i)if(!adjacent(p[i],p[i+1]))return false;return true;}

static bool random_two_opt(vector<Point>& p,mt19937_64& rng){
    int m=p.size();
    for(int tries=0;tries<300;++tries){int i=rng()%(m-2),j=i+1+rng()%(m-i-1);if(j>=m-1)continue;if(adjacent(p[i],p[j])&&adjacent(p[i+1],p[j+1])){reverse(p.begin()+i+1,p.begin()+j+1);return true;}}
    return false;
}
static bool random_backbite(vector<Point>& p,mt19937_64& rng){
    int m=p.size();
    bool left=rng()&1;
    vector<int> candidate;
    if(left){for(int i=2;i<m;++i)if(adjacent(p[0],p[i]))candidate.push_back(i);if(candidate.empty())return false;int i=candidate[rng()%candidate.size()];reverse(p.begin(),p.begin()+i);}
    else{for(int i=0;i+2<m;++i)if(adjacent(p[m-1],p[i]))candidate.push_back(i);if(candidate.empty())return false;int i=candidate[rng()%candidate.size()];reverse(p.begin()+i+1,p.end());}
    return true;
}
static bool random_relocate(vector<Point>& p,mt19937_64& rng){
    int m=p.size();
    for(int tries=0;tries<1000;++tries){
        int l=1+rng()%(m-2), r=l+rng()%(m-1-l); if(r>=m-1)continue;
        if(!adjacent(p[l-1],p[r+1]))continue;
        int e=rng()%(m-1); if(e>=l-1&&e<=r)continue;
        bool rev=false;
        if(adjacent(p[e],p[l])&&adjacent(p[r],p[e+1]))rev=false;
        else if(adjacent(p[e],p[r])&&adjacent(p[l],p[e+1]))rev=true;
        else continue;
        vector<Point> seg(p.begin()+l,p.begin()+r+1);if(rev)reverse(seg.begin(),seg.end());
        vector<Point> rest;rest.reserve(m-(r-l+1));for(int i=0;i<m;++i)if(i<l||i>r)rest.push_back(p[i]);
        int insert_after=e;
        if(e>r)insert_after-=r-l+1;
        rest.insert(rest.begin()+insert_after+1,seg.begin(),seg.end());p.swap(rest);return true;
    }return false;
}

int main(int argc,char**argv){
    if(argc!=7){cerr<<"usage: order_search a D seconds threads seed(spiral|snake) output\n";return 2;}
    int a=stoi(argv[1]),D=stoi(argv[2]),seconds=stoi(argv[3]),threads=stoi(argv[4]);string seed=argv[5],output=argv[6];
    vector<Point> initial=seed=="spiral"?spiral(a):snake(a);if(!valid_path(initial)){cerr<<"bad seed\n";return 2;}
    mutex mu;vector<Point> global_path=initial;Score global=evaluate(initial,a,D);atomic<bool>stop(false);
    auto deadline=chrono::steady_clock::now()+chrono::seconds(seconds);omp_set_num_threads(threads);
#pragma omp parallel
    {
        int tid=omp_get_thread_num();mt19937_64 rng(0x123456789abcdefULL^(uint64_t(tid)<<40)^chrono::high_resolution_clock::now().time_since_epoch().count());
        vector<Point> cur;Score cs,observed;
        while(chrono::steady_clock::now()<deadline){
            {lock_guard<mutex>lk(mu);cur=global_path;cs=global;observed=global;}
            for(int kick=0;kick<tid+1;++kick){vector<Point>q=cur;bool ok=(rng()%3==0)?random_two_opt(q,rng):(rng()%2?random_relocate(q,rng):random_backbite(q,rng));if(ok)cur.swap(q);}cs=evaluate(cur,a,D);
            for(int it=0;it<200000&&chrono::steady_clock::now()<deadline;++it){
                vector<Point> q=cur;int kind=rng()%10;bool moved=kind<4?random_two_opt(q,rng):kind<7?random_backbite(q,rng):random_relocate(q,rng);if(!moved)continue;Score ns=evaluate(q,a,D);
                long long oldv=1000000000LL*cs.capacity+1000000LL*cs.full-10000LL*cs.penalty-100LL*cs.bad-cs.runs;
                long long newv=1000000000LL*ns.capacity+1000000LL*ns.full-10000LL*ns.penalty-100LL*ns.bad-ns.runs;
                double temp=2e8*(1.0-double(it%20000)/20000.0)+1e5;bool accept=newv>=oldv;
                if(!accept){double u=double(rng()>>11)/9007199254740992.0;accept=u<exp(double(newv-oldv)/temp);}if(accept){cur.swap(q);cs=ns;}
                if(cs.key()>observed.key()){
                    lock_guard<mutex>lk(mu);
                    if(cs.key()>global.key()){global=cs;global_path=cur;cerr<<"capacity="<<global.capacity<<" full="<<global.full<<" penalty="<<global.penalty<<" bad="<<global.bad<<" runs="<<global.runs<<" tid="<<tid<<"\n";ofstream out(output);for(auto p:global_path)out<<p.x<<' '<<p.y<<' '<<p.z<<'\n';}
                    observed=global;
                }
            }
        }
    }
    cerr<<"FINAL capacity="<<global.capacity<<" full="<<global.full<<" penalty="<<global.penalty<<" bad="<<global.bad<<" runs="<<global.runs<<"\n";
    return 0;
}
