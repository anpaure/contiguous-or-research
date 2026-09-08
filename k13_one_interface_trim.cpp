#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <algorithm>
#include <array>
#include <atomic>
#include <bit>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <mutex>
#include <thread>
#include <vector>
using namespace std;

struct Evaluator {
    vector<uint32_t> stamp = vector<uint32_t>(4096);
    uint32_t generation = 0;
    vector<int> suffixes;
    explicit Evaluator(const vector<int>& base){
        int x=0; for(auto it=base.rbegin();it!=base.rend();++it){x|=*it;if(suffixes.empty()||x!=suffixes.back())suffixes.push_back(x);}
    }
    int score(const vector<int>& oldparts){
        if(++generation==0){fill(stamp.begin(),stamp.end(),0);++generation;}int count=0;
        auto add=[&](int x){if(stamp[x]!=generation)stamp[x]=generation,++count;};
        array<int,16>p{},c{};int pn=0;
        for(int x:oldparts){int cn=0;c[cn++]=x;for(int i=0;i<pn;++i){int v=p[i]|x;if(v!=c[cn-1])c[cn++]=v;}for(int i=0;i<cn;++i)add(c[i]);p.swap(c);pn=cn;}
        int prefix=0;for(int x:oldparts){prefix|=x;for(int s:suffixes)add(prefix|s);}
        return count;
    }
};

int main(int argc,char**argv){
    if(argc<5){cerr<<"usage: k13_one_interface_trim BASE OUTPUT THREADS REVERSE\n";return 2;}
    ifstream in(argv[1]);vector<int>base;for(int x;in>>x;)base.push_back(x);if(base.size()!=926)return 2;if(stoi(argv[4]))reverse(base.begin(),base.end());
    string output=argv[2];int threads=stoi(argv[3]);atomic<int>next_first{0},best{0};atomic<bool>found{false};mutex io;
    auto work=[&](int id){Evaluator ev(base);vector<int>parts;parts.reserve(925);while(!found){int a=next_first.fetch_add(1);if(a>=925)break;for(int b=a+1;b<926&&!found;++b){parts.clear();parts.push_back(0);for(int i=0;i<926;++i)if(i!=a&&i!=b)parts.push_back(base[i]);int sc=ev.score(parts);int old=best.load();while(sc>old&&!best.compare_exchange_weak(old,sc)){}if(sc>old){lock_guard<mutex>g(io);cerr<<"BEST score="<<sc<<"/4096 delete="<<a<<','<<b<<" worker="<<id<<'\n';}if(sc==4096){bool expected=false;if(found.compare_exchange_strong(expected,true)){ofstream out(output);for(int x:base)out<<x<<' ';for(int x:parts)out<<((1<<12)|x)<<' ';out<<'\n';lock_guard<mutex>g(io);cerr<<"FOUND delete="<<a<<','<<b<<" length=1851\n";}break;}}}};
    vector<thread>pool;for(int i=0;i<threads;++i)pool.emplace_back(work,i);for(auto&t:pool)t.join();cout<<"found="<<found<<" best="<<best<<"/4096\n";return found?0:1;
}
