#include <algorithm>
#include <array>
#include <cassert>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <tuple>
#include <vector>

using P = std::array<int,3>;
using Label = std::pair<int,int>;

static Label labL(const P& v, int m) {
    int x=v[0],y=v[1],z=v[2];
    int i=std::min(y,m-x), t=x+y-i;
    int j=std::min(t,m-z);
    return {i,j};
}
static Label labR(const P& v, int m) {
    int x=v[0],y=v[1],z=v[2];
    int i=std::min(z,m-x), t=x+z-i;
    int j=std::min(t,m-y);
    return {i,j};
}
static int rankp(const P& v) { return v[0]+v[1]+v[2]; }

struct Piece { std::string name; std::vector<P> pts; };

int main(int argc,char**argv){
    int m=argc>1?std::stoi(argv[1]):3;
    std::map<Label,std::vector<P>> R;
    std::map<Label,std::vector<P>> L;
    for(int x=0;x<=m;x++)for(int y=0;y<=m;y++)for(int z=0;z<=m;z++){
        P v{x,y,z}; R[labR(v,m)].push_back(v); L[labL(v,m)].push_back(v);
    }
    for(auto& [q,a]:R) std::sort(a.begin(),a.end(),[](P x,P y){return rankp(x)<rankp(y);});
    for(auto& [q,a]:L) std::sort(a.begin(),a.end(),[](P x,P y){return rankp(x)<rankp(y);});
    std::map<Label,std::vector<P>> pre,suf;
    std::vector<Piece> pieces;
    std::set<Label> usedPre,usedSuf;
    for(auto& [q,a]:R){
        auto [i,j]=q;
        if(i+j<=m){
            P u{j,i,i};
            for(P v:a) (rankp(v)<=rankp(u)?pre[q]:suf[q]).push_back(v);
        }
    }
    for(int i=0;i<=m-2;i++)for(int j=0;j<=m-i-1;j++){
        Piece q; q.name="Q("+std::to_string(i)+","+std::to_string(j)+")";
        q.pts=pre[{i,j}]; q.pts.insert(q.pts.end(),suf[{i+1,j}].begin(),suf[{i+1,j}].end());
        pieces.push_back(q); usedPre.insert({i,j}); usedSuf.insert({i+1,j});
    }
    // special reunion
    pieces.push_back({"R(0,"+std::to_string(m)+")",R[{0,m}]}); usedPre.insert({0,m}); usedSuf.insert({0,m});
    for(auto& [q,a]:R){
        auto [i,j]=q;
        if(i+j<=m){
            if(!usedPre.count(q)&&!pre[q].empty()) pieces.push_back({"P("+std::to_string(i)+","+std::to_string(j)+")",pre[q]});
            if(!usedSuf.count(q)&&!suf[q].empty()) pieces.push_back({"S("+std::to_string(i)+","+std::to_string(j)+")",suf[q]});
        }else pieces.push_back({"R("+std::to_string(i)+","+std::to_string(j)+")",a});
    }
    std::map<P,int> rp;
    for(int a=0;a<(int)pieces.size();a++)for(P v:pieces[a].pts){assert(!rp.count(v));rp[v]=a;}
    assert((int)rp.size()==(m+1)*(m+1)*(m+1));
    std::map<Label,int> li;
    int ct=0; for(auto& [q,a]:L)li[q]=ct++;
    std::vector<std::set<int>> gr(pieces.size());
    std::vector<std::set<int>> gl(L.size());
    std::map<std::pair<int,int>,std::vector<std::string>> glgen;
    // right precedence from each L chain, consecutive distinct piece names along rank.
    for(auto& [lab,a]:L){
        std::vector<int> seq; for(P v:a){int q=rp[v];if(seq.empty()||seq.back()!=q)seq.push_back(q);}
        for(int z=1;z<(int)seq.size();z++)if(seq[z-1]!=seq[z])gr[seq[z-1]].insert(seq[z]);
        std::cout<<"L("<<lab.first<<","<<lab.second<<") :";for(int q:seq)std::cout<<" "<<pieces[q].name;std::cout<<"\n";
    }
    std::cout<<"\nR piece sequences (higher rank forces earlier L, so reversed arcs):\n";
    for(int qi=0;qi<(int)pieces.size();qi++){
        auto &a=pieces[qi].pts;
        std::vector<int> seq; for(P v:a){int q=li[labL(v,m)];if(seq.empty()||seq.back()!=q)seq.push_back(q);}
        std::cout<<pieces[qi].name<<" :";for(int q:seq){auto it=std::next(L.begin(),q);std::cout<<" L("<<it->first.first<<","<<it->first.second<<")";}std::cout<<"\n";
        for(int z=1;z<(int)seq.size();z++)if(seq[z-1]!=seq[z]){
            gl[seq[z]].insert(seq[z-1]);
            glgen[{seq[z],seq[z-1]}].push_back(pieces[qi].name);
        }
    }
    std::cout<<"\nRight precedence edges:\n";
    for(int a=0;a<(int)gr.size();a++)for(int b:gr[a])std::cout<<pieces[a].name<<" -> "<<pieces[b].name<<"\n";
    std::cout<<"\nShort right-precedence cycles (canonical rotation, length <= 7):\n";
    {
      std::set<std::vector<int>> cyc;
      for(int s=0;s<(int)gr.size();++s){
        std::vector<int> path{s};std::vector<char>in(gr.size());in[s]=1;
        auto dfs=[&](auto&&self,int u)->void{if(path.size()>7)return;for(int v:gr[u]){
          if(v==s&&path.size()>=2){auto c=path;int z=std::min_element(c.begin(),c.end())-c.begin();std::rotate(c.begin(),c.begin()+z,c.end());cyc.insert(c);}
          else if(!in[v]&&v>=s){in[v]=1;path.push_back(v);self(self,v);path.pop_back();in[v]=0;}
        }};dfs(dfs,s);
      }
      for(auto&c:cyc){std::cout<<"cycle";for(int a:c)std::cout<<" "<<pieces[a].name;std::cout<<"\n";}
    }
    std::cout<<"\nLeft precedence edges:\n";
    std::vector<Label> labs;for(auto &[q,a]:L)labs.push_back(q);
    for(int a=0;a<(int)gl.size();a++)for(int b:gl[a]){
        std::cout<<"L("<<labs[a].first<<","<<labs[a].second<<") -> L("<<labs[b].first<<","<<labs[b].second<<") via";
        for(auto&s:glgen[{a,b}])std::cout<<" "<<s;
        std::cout<<"\n";
    }
    std::cout<<"\nShort left-precedence cycles (canonical rotation, length <= 6):\n";
    std::set<std::vector<int>> cycles;
    for(int s=0;s<(int)gl.size();++s){
        std::vector<int> path{s}; std::vector<char> in(gl.size());in[s]=1;
        auto dfs=[&](auto&& self,int u)->void{
            if(path.size()>6)return;
            for(int v:gl[u]){
                if(v==s&&path.size()>=2){
                    auto c=path; int z=std::min_element(c.begin(),c.end())-c.begin();
                    std::rotate(c.begin(),c.begin()+z,c.end());cycles.insert(c);
                }else if(!in[v]&&v>=s){in[v]=1;path.push_back(v);self(self,v);path.pop_back();in[v]=0;}
            }
        }; dfs(dfs,s);
    }
    for(auto&c:cycles){
        std::cout<<"cycle";
        for(int a:c)std::cout<<" L("<<labs[a].first<<","<<labs[a].second<<")";
        std::cout<<"\n";
        for(int z=0;z<(int)c.size();z++){
            int a=c[z],b=c[(z+1)%c.size()];std::cout<<"  via";
            for(auto&s:glgen[{a,b}])std::cout<<" "<<s;
            std::cout<<"\n";
        }
    }
}
