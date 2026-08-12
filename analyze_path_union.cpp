#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <algorithm>
#include <bit>
#include <fstream>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <utility>
#include <vector>
using namespace std;

static vector<int> read_path(const string& name) {
    ifstream in(name);
    vector<int> path;
    for (int x; in >> x;) path.push_back(x);
    return path;
}

static pair<int,int> canon(int a, int b) {
    if (a > b) swap(a,b);
    return {a,b};
}

int main(int argc, char** argv) {
    if (argc < 3) return 2;
    vector<vector<int>> paths;
    for (int i = 1; i < argc; ++i) paths.push_back(read_path(argv[i]));
    const int n = paths[0].size();
    if (!n) return 2;
    map<pair<int,int>, unsigned> edges;
    set<int> vertex_set(paths[0].begin(), paths[0].end());
    for (int p = 0; p < static_cast<int>(paths.size()); ++p) {
        if (static_cast<int>(paths[p].size()) != n ||
            set<int>(paths[p].begin(), paths[p].end()) != vertex_set) return 3;
        set<pair<int,int>> local;
        for (int i = 0; i + 1 < n; ++i) {
            if (popcount(static_cast<unsigned>(paths[p][i] ^ paths[p][i+1])) != 2) return 4;
            local.insert(canon(paths[p][i], paths[p][i+1]));
        }
        for (auto e : local) edges[e] |= 1u << p;
    }
    vector<int> index(1 << 20, -1), masks(vertex_set.begin(), vertex_set.end());
    sort(masks.begin(), masks.end());
    for (int i = 0; i < n; ++i) index[masks[i]] = i;
    vector<vector<int>> graph(n);
    map<unsigned,int> provenance;
    map<int,int> lower_multiplicity, upper_multiplicity;
    for (auto [e, source] : edges) {
        ++provenance[source];
        int u=index[e.first],v=index[e.second];
        graph[u].push_back(v);graph[v].push_back(u);
        ++lower_multiplicity[e.first&e.second];
        ++upper_multiplicity[e.first|e.second];
    }
    vector<unsigned char> seen(n);
    int components=0;
    for (int s=0;s<n;++s) if(!seen[s]) {
        ++components; queue<int> q; q.push(s);seen[s]=1;
        while(!q.empty()){int u=q.front();q.pop();for(int v:graph[u])if(!seen[v])seen[v]=1,q.push(v);}
    }
    int min_degree=n,max_degree=0;
    long long degree_sum=0;
    for(auto& a:graph){min_degree=min(min_degree,(int)a.size());max_degree=max(max_degree,(int)a.size());degree_sum+=a.size();}
    cout << "vertices=" << n << " paths=" << paths.size() << " union_edges=" << edges.size()
         << " components=" << components << " degree=" << min_degree << '-' << max_degree
         << " average_degree=" << double(degree_sum)/n << '\n';
    cout << "provenance";
    for(auto [mask,count]:provenance) cout << " mask" << mask << '=' << count;
    cout << '\n';
    cout << "distinct_lower=" << lower_multiplicity.size()
         << " distinct_upper=" << upper_multiplicity.size() << '\n';
    map<int,int> lm,um;
    for(auto [x,c]:lower_multiplicity)++lm[c];
    for(auto [x,c]:upper_multiplicity)++um[c];
    cout << "lower_multiplicity";for(auto [c,n]:lm)cout << ' ' << c << ':' << n;cout << '\n';
    cout << "upper_multiplicity";for(auto [c,n]:um)cout << ' ' << c << ':' << n;cout << '\n';
}
