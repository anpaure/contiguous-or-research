#include <bit>
#include <iostream>
#include <vector>
using namespace std;
int main(int argc,char**argv){
    if(argc!=3)return 2;const int target=stoi(argv[1]),k=stoi(argv[2]);
    vector<int>p;for(int x;cin>>x;)p.push_back(x);
    for(int i=0;i<(int)p.size();++i)if(!(p[i]&~target)&&
        popcount((unsigned)p[i])+1==popcount((unsigned)target)){
        cout<<"position="<<i<<" value="<<p[i];
        if(i)cout<<" prev="<<p[i-1]<<" pu="<<(p[i-1]|p[i])
                 <<" pi="<<(p[i-1]&p[i]);
        if(i+1<(int)p.size())cout<<" next="<<p[i+1]<<" nu="<<(p[i]|p[i+1])
                 <<" ni="<<(p[i]&p[i+1]);
        cout<<'\n';
    }
}
