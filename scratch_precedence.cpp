#include <bits/stdc++.h>
using namespace std;

struct Label { int i,j; auto operator<=>(const Label&) const = default; };
struct Pt { int x,y,z; int rank() const {return x+y+z;} };
Label labL(Pt p,int m){int i=min(p.y,m-p.x),t=p.x+p.y-i,j=min(t,m-p.z);return{i,j};}
Label labR(Pt p,int m){int i=min(p.z,m-p.x),t=p.x+p.z-i,j=min(t,m-p.y);return{i,j};}
string rid(Pt p,int m,int splitMode=0){
 auto [i,j]=labR(p,m); int r=p.rank();
 if(i+j>m) return "U"+to_string(i)+","+to_string(j);
 bool pre=r<=j+2*i;
 if(pre){
   if(i<=m-2 && j<=m-i-1) return "Q"+to_string(i)+","+to_string(j);
   if(i==0&&j==m) return "B";
   string s="P"+to_string(i)+","+to_string(j);
   if(splitMode){auto [h,k]=labL(p,m); int cut=0;
     if(splitMode==5) { s += "h"+to_string(h); return s; }
     if(splitMode==1) cut=0;
     if(splitMode==2) cut=i-1;
     if(splitMode==3) cut=i/2;
     if(splitMode==4) cut=j?0:i-1;
     s += (h<=cut?"a":"b");
   }
   return s;
 }
 if(1<=i&&i<=m-1&&j<=m-i) return "Q"+to_string(i-1)+","+to_string(j);
 if(i==0&&j==m) return "B";
 return "S"+to_string(i)+","+to_string(j);
}
int main(int argc,char**argv){int m=argc>1?atoi(argv[1]):3; bool topo=argc>2; int splitMode=argc>3?atoi(argv[3]):0; string del=argc>4?argv[4]:"";map<Label,vector<Pt>> L; set<Label> rawR;
 auto deleted=[&](const string&q){if(del.empty())return false;stringstream ss(del);string t;while(getline(ss,t,';'))if(q==t||(!t.empty()&&t.back()=='*'&&q.starts_with(t.substr(0,t.size()-1))))return true;return false;};
 for(int x=0;x<=m;x++)for(int y=0;y<=m;y++)for(int z=0;z<=m;z++){Pt p{x,y,z};L[labL(p,m)].push_back(p);rawR.insert(labR(p,m));}
 if(argc>2 && string(argv[2])=="raw"){for(auto [i,j]:rawR)cout<<i<<","<<j<<"\n";return 0;}
 map<string,set<string>> G; set<string> V;
 for(auto &[l,v]:L){sort(v.begin(),v.end(),[](Pt a,Pt b){return a.rank()<b.rank();});
   string prev=""; for(auto p:v){string q=rid(p,m,splitMode); bool keep=(splitMode||q[0]!='P') && !deleted(q); if(keep)V.insert(q); if(prev!=""&&prev!=q&&(splitMode||(prev[0]!='P'&&q[0]!='P'))&&!deleted(prev)&&!deleted(q))G[prev].insert(q); prev=q;}
   if(topo) continue;
   cout<<"L("<<l.i<<","<<l.j<<"): "; string last="";
   for(auto p:v){string q=rid(p,m,splitMode); if(q!=last){cout<<q<<"["<<p.rank()<<"] ";last=q;}}
   cout<<"\n";
 }
 if(topo){
   if(argc>5&&string(argv[5])=="edges")for(auto &[u,vs]:G)for(auto v:vs)cerr<<"E "<<u<<" -> "<<v<<"\n";
   map<string,int> indeg; for(auto x:V)indeg[x]=0;for(auto &[u,vs]:G)for(auto v:vs)indeg[v]++;
   set<string> z;for(auto &[v,d]:indeg)if(!d)z.insert(v);int cnt=0,lev=0;map<string,int> depth;
   while(!z.empty()){string u=*z.begin();z.erase(z.begin());cnt++;cout<<setw(4)<<cnt<<" "<<setw(8)<<u<<" d="<<depth[u]<<"\n";for(auto v:G[u]){depth[v]=max(depth[v],depth[u]+1);if(!--indeg[v])z.insert(v);}}
   cerr<<"V="<<V.size()<<" topo="<<cnt<<"\n";
   if(cnt<(int)V.size()){
     map<string,int> col; vector<string> st,cyc;
     function<bool(string)> dfs=[&](string u){col[u]=1;st.push_back(u);for(auto v:G[u]){if(!col[v]){if(dfs(v))return true;}else if(col[v]==1){auto it=find(st.begin(),st.end(),v);cyc.assign(it,st.end());cyc.push_back(v);return true;}}st.pop_back();col[u]=2;return false;};
     for(auto u:V)if(!col[u]&&dfs(u))break;
     cerr<<"cycle:";for(auto u:cyc)cerr<<" "<<u;cerr<<"\n";
   }
   auto block=[](string s){if(s[0]=='U')return 0;if(s=="B")return 1;if(s[0]=='S')return 2;if(s[0]=='Q')return 3;return 9;};
   auto nums=[](string s){int p=s.find_first_of("0123456789"),c=s.find(',',p);return pair{p==(int)string::npos?-1:stoi(s.substr(p,c-p)),c==(int)string::npos?-1:stoi(s.substr(c+1))};};
   int bad=0;for(auto &[u,vs]:G)for(auto v:vs){int bu=block(u),bv=block(v);bool ok=bu<bv;if(bu==bv&&bu==0){auto [i,j]=nums(u);auto [I,J]=nums(v);ok=I<i;}if(bu==bv&&bu==2){auto [i,j]=nums(u);auto [I,J]=nums(v);ok=J<j;}if(bu==bv&&bu==3){auto [i,j]=nums(u);auto [I,J]=nums(v);ok=J<j||(J==j&&I>i);}if(!ok){bad++;cerr<<"BAD "<<u<<" -> "<<v<<"\n";}}
   cerr<<"classification_bad="<<bad<<"\n";
 }
}
