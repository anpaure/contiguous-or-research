#include <algorithm>
#include <bit>
#include <iostream>
#include <vector>
using namespace std;

static vector<unsigned char> coverage_avoiding(const vector<int>&a,
                                                const vector<unsigned char>&blocked,
                                                int limit){
    vector<unsigned char>seen(limit);
    for(int left=0;left<(int)a.size();++left){
        if(blocked[left])continue;
        int value=0;
        for(int right=left;right<(int)a.size()&&!blocked[right];++right){
            value|=a[right];seen[value]=1;
        }
    }
    return seen;
}

int main(int argc,char**argv){
    if(argc!=3)return 2;const int k=stoi(argv[1]),wanted=stoi(argv[2]);
    const int limit=1<<k;vector<int>a;for(int x;cin>>x;)a.push_back(x);
    vector<unsigned char>blocked(a.size());
    const auto original=coverage_avoiding(a,blocked,limit);
    int original_count=count(original.begin()+1,original.end(),1);
    for(int step=0;step<wanted;++step){
        int best_position=-1,best_count=-1;
        for(int position=0;position<(int)a.size();++position)if(!blocked[position]){
            blocked[position]=1;
            const auto seen=coverage_avoiding(a,blocked,limit);
            int retained=0;
            for(int mask=1;mask<limit;++mask)retained+=original[mask]&&seen[mask];
            blocked[position]=0;
            if(retained>best_count){best_count=retained;best_position=position;}
        }
        blocked[best_position]=1;
        cerr<<"step="<<step+1<<" position="<<best_position
            <<" retained="<<best_count<<'/'<<original_count<<'\n';
    }
    for(int position=0;position<(int)a.size();++position)
        if(blocked[position])cout<<position<<' ';
    cout<<'\n';
}
