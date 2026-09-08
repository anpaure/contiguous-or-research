#define main audit_hook_repair_unused_main
#include "audit_hook_repair.cpp"
#undef main

struct Half { Lab lab; std::vector<Pt> a; };

static std::pair<std::vector<Half>,std::vector<Half>> cap_halves(int m) {
    auto rawR=raw(false,m); std::vector<Half>A,B;
    for(auto&c:rawR) {
        Lab q=rr(c.a[0],m); int i=q.first,j=q.second;
        if(i+j>=m) continue;
        int cut=-1;
        for(int z=0;z+1<(int)c.a.size();++z) {
            Lab x=ll(c.a[z],m), y=ll(c.a[z+1],m);
            if ((x==Lab{i,m-i}&&y.first>i)||(y==Lab{i,m-i}&&x.first>i)) cut=z;
        }
        assert(cut>=0);
        A.push_back({q,{c.a.begin(),c.a.begin()+cut+1}});
        B.push_back({q,{c.a.begin()+cut+1,c.a.end()}});
    }
    return {A,B};
}

static bool compatible(const Half&a,const Half&b,int m) {
    Pt x=a.a.back(),y=b.a.front();for(int z=0;z<3;z++)if(x[z]>y[z])return false;
    std::set<Lab>s;for(Pt p:a.a)s.insert(ll(p,m));for(Pt p:b.a)if(s.count(ll(p,m)))return false;
    return true;
}

int main(){
 for(int m=1;m<=30;m++){
  auto [A,B]=cap_halves(m);int n=A.size();std::vector<std::vector<int>>g(n);long long e=0;
  for(int i=0;i<n;i++)for(int j=0;j<n;j++)if(compatible(A[i],B[j],m)){g[i].push_back(j);e++;}
  std::vector<int>mr(n,-1);auto aug=[&](auto&&self,int u,std::vector<char>&v)->bool{for(int x:g[u])if(!v[x]){v[x]=1;if(mr[x]<0||self(self,mr[x],v)){mr[x]=u;return true;}}return false;};int z=0;for(int i=0;i<n;i++){std::vector<char>v(n);z+=aug(aug,i,v);}
  std::cout<<"m="<<m<<" halves="<<n<<" edges="<<e<<" matching="<<z<<" deficit="<<n-z<<"\n";
  if(m<=5)for(int j=0;j<n;j++)if(mr[j]>=0)std::cout<<"  A("<<A[mr[j]].lab.first<<","<<A[mr[j]].lab.second<<")->B("<<B[j].lab.first<<","<<B[j].lab.second<<")\n";
  auto RR=raw(false,m);std::vector<Half>all;
  std::set<Lab>doub;for(auto&x:A)doub.insert(x.lab);
  for(auto&x:A)all.push_back(x);for(auto&x:B)all.push_back(x);
  for(auto&c:RR){Lab q=rr(c.a[0],m);if(!doub.count(q))all.push_back({q,c.a});}
  int N=all.size();std::vector<std::vector<int>>gg(N);long long ee=0;
  for(int i=0;i<N;i++)for(int j=0;j<N;j++)if(i!=j&&compatible(all[i],all[j],m)){gg[i].push_back(j);ee++;}
  std::vector<int>mm(N,-1);auto aa=[&](auto&&self,int u,std::vector<char>&v)->bool{for(int x:gg[u])if(!v[x]){v[x]=1;if(mm[x]<0||self(self,mm[x],v)){mm[x]=u;return true;}}return false;};int zz=0;for(int i=0;i<N;i++){std::vector<char>v(N);zz+=aa(aa,i,v);}
  std::cout<<"  allpieces="<<N<<" compat="<<ee<<" pathcover="<<N-zz<<" rawW="<<RR.size()<<"\n";
 }
}
