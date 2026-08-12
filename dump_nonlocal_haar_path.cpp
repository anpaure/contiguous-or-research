#define main msw_factor_fibre_bfs_main
#include "msw_factor_fibre_bfs.cpp"
#undef main

static std::vector<U64> switch_root(const std::vector<U64>& cur,
                                    int n, int m, int a, int b, int root) {
    std::vector<int> own(U32{1}<<n,-1), rown(U32{1}<<n,-1);
    std::vector<U64> rhs(cur.size());
    for (int i=0;i<(int)cur.size();++i) {
        for (U32 x:intervals(cur[i],n,m)) own[x]=i;
        rhs[i]=swap_labels(cur[i],n,a,b);
        for (U32 x:intervals(rhs[i],n,m)) rown[x]=i;
    }
    DSU d(2*cur.size());
    for (U32 x=0;x<(U32{1}<<n);++x)
        if (own[x]>=0) d.u(own[x],cur.size()+rown[x]);
    std::vector<int> L,R;
    for (int i=0;i<(int)cur.size();++i) {
        if (d.f(i)==root) L.push_back(i);
        if (d.f(cur.size()+i)==root) R.push_back(i);
    }
    assert(!L.empty() && L.size()==R.size());
    std::cout << "component size " << L.size() << "\nREMOVED\n";
    for (int i:L) { for (int x:unpack(cur[i],n)) std::cout<<x+1<<'.'; std::cout<<'\n'; }
    std::cout << "ADDED\n";
    for (int i:R) { for (int x:unpack(rhs[i],n)) std::cout<<x+1<<'.'; std::cout<<'\n'; }
    std::vector<char> del(cur.size()); for(int i:L)del[i]=1;
    std::vector<U64> nx;
    for(int i=0;i<(int)cur.size();++i)if(!del[i])nx.push_back(cur[i]);
    for(int i:R)nx.push_back(rhs[i]);
    std::sort(nx.begin(),nx.end()); return nx;
}

int main() {
    constexpr int m=4,n=9;
    std::vector<U64> f;
    std::function<void(int,int,int,U32)>gen=[&](int p,int u,int d,U32 mask){
        if(p==2*m){U32 x=mask;std::vector<int>q;for(int e=0;e<m;++e){auto a=g(x,m);auto b=hfun(a.first,m);q.push_back(a.second);q.push_back(b.second);x=b.first;}q.push_back(2*m);f.push_back(canon(q));return;}
        if(u<m)gen(p+1,u+1,d,mask|(U32{1}<<p)); if(d<u)gen(p+1,u,d+1,mask);
    };
    gen(0,0,0,0); std::sort(f.begin(),f.end());
    const int steps[4][3]={{0,2,11},{1,3,3},{0,4,12},{0,1,4}};
    for(int s=0;s<4;++s){std::cout<<"STEP "<<s+1<<" swap "<<steps[s][0]+1<<','<<steps[s][1]+1<<" root "<<steps[s][2]<<'\n';f=switch_root(f,n,m,steps[s][0],steps[s][1],steps[s][2]);}
}
