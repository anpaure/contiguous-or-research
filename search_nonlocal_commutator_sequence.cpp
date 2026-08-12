#define main msw_factor_fibre_bfs_main
#include "msw_factor_fibre_bfs.cpp"
#undef main

struct StepState { std::vector<U64> f; std::string path; };

static std::vector<std::pair<std::vector<U64>,int>> all_switches(
        const std::vector<U64>& cur,int n,int m,int a,int b) {
    std::vector<int> own(U32{1}<<n,-1),rown(U32{1}<<n,-1);
    std::vector<U64> rhs(cur.size());
    for(int i=0;i<(int)cur.size();++i){
        for(U32 x:intervals(cur[i],n,m)){assert(own[x]<0);own[x]=i;}
        rhs[i]=swap_labels(cur[i],n,a,b);
        for(U32 x:intervals(rhs[i],n,m)){assert(rown[x]<0);rown[x]=i;}
    }
    DSU d(2*cur.size());
    for(U32 x=0;x<(U32{1}<<n);++x)if(own[x]>=0)d.u(own[x],cur.size()+rown[x]);
    std::unordered_map<int,std::pair<std::vector<int>,std::vector<int>>> cs;
    for(int i=0;i<(int)cur.size();++i){cs[d.f(i)].first.push_back(i);cs[d.f(cur.size()+i)].second.push_back(i);}
    std::vector<std::pair<std::vector<U64>,int>> out;
    for(auto &kv:cs){auto L=kv.second.first,R=kv.second.second;assert(L.size()==R.size());std::vector<char>del(cur.size());for(int i:L)del[i]=1;std::vector<U64>nx;for(int i=0;i<(int)cur.size();++i)if(!del[i])nx.push_back(cur[i]);for(int i:R)nx.push_back(rhs[i]);std::sort(nx.begin(),nx.end());out.push_back({std::move(nx),(int)L.size()});}
    return out;
}

static std::vector<U64> msw(int m) {
    std::vector<U64> f; std::function<void(int,int,int,U32)>gen=[&](int p,int u,int d,U32 mask){
        if(p==2*m){U32 x=mask;std::vector<int>q;for(int e=0;e<m;++e){auto a=g(x,m);auto b=hfun(a.first,m);q.push_back(a.second);q.push_back(b.second);x=b.first;}q.push_back(2*m);f.push_back(canon(q));return;}
        if(u<m)gen(p+1,u+1,d,mask|(U32{1}<<p));if(d<u)gen(p+1,u,d+1,mask);
    };gen(0,0,0,0);std::sort(f.begin(),f.end());return f;
}

static void dump_difference(const std::vector<U64>&a,const std::vector<U64>&b,int n){
    std::cout<<"NEG\n";for(U64 z:a)if(!std::binary_search(b.begin(),b.end(),z)){for(int x:unpack(z,n))std::cout<<x+1<<'.';std::cout<<'\n';}
    std::cout<<"POS\n";for(U64 z:b)if(!std::binary_search(a.begin(),a.end(),z)){for(int x:unpack(z,n))std::cout<<x+1<<'.';std::cout<<'\n';}
}

int main(int argc,char**argv){int m=argc>1?std::stoi(argv[1]):5,n=2*m+1;std::vector<StepState>lev{{msw(m),""}};
 for(int depth=0;depth<m-1;++depth){int a=depth&1,b=depth+2;std::vector<StepState>next;std::unordered_set<std::string>seen;for(auto &st:lev)for(auto &z:all_switches(st.f,n,m,a,b)){auto k=state_key(z.first);if(seen.insert(k).second)next.push_back({std::move(z.first),st.path+" "+std::to_string(a+1)+","+std::to_string(b+1)+"["+std::to_string(z.second)+"]"});}lev.swap(next);std::cerr<<"depth="<<depth+1<<" states="<<lev.size()<<'\n';}
 for(auto &st:lev)for(auto &z:all_switches(st.f,n,m,0,1)){if(shadow_key(st.f,n,m-1)==shadow_key(z.first,n,m-1)&&shadow_key(st.f,n,m-2)!=shadow_key(z.first,n,m-2)){std::cout<<"FOUND m="<<m<<" path="<<st.path<<" 1,2["<<z.second<<"]\n";dump_difference(st.f,z.first,n);return 0;}}
 std::cout<<"NONE m="<<m<<" states="<<lev.size()<<'\n';
}
