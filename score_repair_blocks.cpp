#include <algorithm>
#include <iostream>
#include <tuple>
#include <vector>
using namespace std;

int main(int argc,char**argv){
    if(argc!=3)return 2;
    const int k=stoi(argv[1]),length=stoi(argv[2]),limit=1<<k;
    vector<int>a;for(int x;cin>>x;)a.push_back(x);
    vector<tuple<int,int,int>> score;
    for(int first=0;first+length<=(int)a.size();++first){
        const int last=first+length;
        vector<unsigned char>seen(limit);
        for(int left=0;left<first;++left){
            int value=0;
            for(int right=left;right<first;++right){value|=a[right];seen[value]=1;}
        }
        for(int left=last;left<(int)a.size();++left){
            int value=0;
            for(int right=left;right<(int)a.size();++right){value|=a[right];seen[value]=1;}
        }
        int missing=0;
        for(int mask=1;mask<limit;++mask)missing+=!seen[mask];
        score.emplace_back(missing,first,last-1);
    }
    sort(score.begin(),score.end());
    for(int i=0;i<min<int>(30,score.size());++i){
        auto [missing,first,last]=score[i];
        cout<<"missing="<<missing<<" first="<<first<<" last="<<last<<'\n';
    }
}
