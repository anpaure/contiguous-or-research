#include <algorithm>
#include <bit>
#include <iostream>
#include <limits>
#include <vector>
using namespace std;

int main(int argc,char**argv){
    if(argc!=2)return 2;const int k=stoi(argv[1]),limit=1<<k;
    vector<int>a;for(int x;cin>>x;)a.push_back(x);
    vector<unsigned char>seen(limit);
    for(int left=0;left<(int)a.size();++left){
        int value=0;for(int right=left;right<(int)a.size();++right){
            value|=a[right];seen[value]=1;
        }
    }
    vector<int>missing;
    for(int mask=1;mask<limit;++mask)if(!seen[mask])missing.push_back(mask);
    sort(missing.begin(),missing.end(),[&](int x,int y){
        return popcount((unsigned)x)>popcount((unsigned)y);
    });
    vector<unsigned char>selected(a.size());
    for(int target:missing){
        int best_cost=numeric_limits<int>::max(),best_left=-1,best_right=-1;
        vector<int>best_add;
        for(int left=0;left<(int)a.size();++left)
            for(int right=left;right<(int)a.size()&&right-left<12;++right){
                vector<int>add;
                bool has_variable=false;
                int fixed_or=0;
                for(int position=left;position<=right;++position){
                    if(selected[position]){has_variable=true;continue;}
                    if(a[position]&~target){add.push_back(position);has_variable=true;}
                    else fixed_or|=a[position];
                }
                if((target&~fixed_or)&&!has_variable){
                    int position=left;
                    while(position<=right&&selected[position])++position;
                    if(position>right)continue;
                    add.push_back(position);has_variable=true;
                    fixed_or=0;
                    for(int p=left;p<=right;++p)
                        if(!selected[p]&&find(add.begin(),add.end(),p)==add.end())
                            fixed_or|=a[p];
                }
                sort(add.begin(),add.end());add.erase(unique(add.begin(),add.end()),add.end());
                const int cost=10000*(int)add.size()+20*(right-left+1)+
                    popcount((unsigned)(fixed_or^target));
                if(cost<best_cost){best_cost=cost;best_left=left;best_right=right;best_add=add;}
            }
        if(best_left<0)return 3;
        for(int position:best_add)selected[position]=1;
        cerr<<"target="<<target<<" interval=["<<best_left<<','<<best_right
            <<"] add="<<best_add.size()<<" total="
            <<count(selected.begin(),selected.end(),1)<<'\n';
    }
    for(int position=0;position<(int)selected.size();++position)
        if(selected[position])cout<<position<<' ';
    cout<<'\n';
}
