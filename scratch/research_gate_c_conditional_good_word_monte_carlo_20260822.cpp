#include <algorithm>
#include <iostream>
#include <numeric>
#include <random>
#include <string>
#include <vector>

static bool good(const std::vector<int>& sigma, int a) {
  int k = sigma.size(), h = 0, lo = k, hi = -k;
  for (int u = 1; u < k; ++u) {
    int r = (sigma[(a + u) % k] - sigma[a] + k) % k;
    h += ((r-u)&1) ? -1 : 1;
    lo = std::min(lo,h); hi=std::max(hi,h);
  }
  return lo>=0 && hi<=h;
}

int main(int argc,char**argv){
 int k=argc>1?std::stoi(argv[1]):101;
 int samples=argc>2?std::stoi(argv[2]):1000000;
 std::mt19937_64 rng(1234567+k);
 std::vector<int> values[2],positions[2],sigma(k);
 sigma[0]=0;
 for(int v=1;v<k;++v){values[v&1].push_back(v);positions[v&1].push_back(v);}
 std::vector<long long> hit(k);
 for(int z=0;z<samples;++z){
  std::shuffle(positions[0].begin(),positions[0].end(),rng);
  std::shuffle(positions[1].begin(),positions[1].end(),rng);
  for(int r=0;r<2;++r)for(int i=0;i<(int)values[r].size();++i)sigma[values[r][i]]=positions[r][i];
  for(int u=1;u<k;++u)hit[u]+=good(sigma,u);
 }
 double sum=0,mx=0;int arg=0;
 for(int u=1;u<k;++u){double p=1.0*hit[u]/samples;sum+=p;if(p>mx){mx=p;arg=u;}}
 std::cout<<"K="<<k<<" sum="<<sum<<" max="<<mx<<" arg="<<arg<<" Kmax="<<k*mx<<"\n";
 for(int u:{1,2,3,k/4,k/2,k-3,k-2,k-1})if(u>0&&u<k)std::cout<<u<<':'<<1.0*hit[u]/samples<<' ';
 std::cout<<'\n';
}
