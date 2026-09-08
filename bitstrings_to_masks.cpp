#include <iostream>
#include <string>
using namespace std;
int main(){string s;while(cin>>s){int value=0;for(int i=0;i<(int)s.size();++i)if(s[i]=='1')value|=1<<i;cout<<value<<' ';}cout<<'\n';}
