#include <algorithm>
#include <bit>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main(int argc, char** argv) {
    if (argc != 4) return 2;
    const int k = stoi(argv[1]), d = stoi(argv[2]), maximum_rank = stoi(argv[3]);
    const int limit = 1 << k;
    vector<int> central;
    for (int value; cin >> value;) central.push_back(value);
    const int n = central.size() + d;
    vector<int> envelope(n, limit - 1), forced(n);
    for (int position = 0; position < n; ++position)
        for (int i = max(0, position - d);
             i <= min(static_cast<int>(central.size()) - 1, position); ++i)
            envelope[position] &= central[i];
    for (int bit = 0; bit < k; ++bit)
        for (int i = 0; i < static_cast<int>(central.size()); ++i)
            if (central[i] & (1 << bit)) {
                int only = -1, count = 0;
                for (int position = i; position <= i + d; ++position)
                    if (envelope[position] & (1 << bit)) { only = position; ++count; }
                if (count == 1) forced[only] |= 1 << bit;
            }

    vector<int> targets;
    for (int mask = 1; mask < limit; ++mask)
        if (popcount(static_cast<unsigned>(mask)) <= maximum_rank)
            targets.push_back(mask);
    vector<vector<int>> edge(targets.size());
    long long edge_count = 0;
    for (int i = 0; i < static_cast<int>(targets.size()); ++i)
        for (int position = 0; position < n; ++position)
            if (!(targets[i] & ~envelope[position]) && !(forced[position] & ~targets[i])) {
                edge[i].push_back(position);
                ++edge_count;
            }

    vector<int> owner(n, -1);
    auto dfs = [&] (auto&& self, int left, vector<unsigned char>& seen) -> bool {
        for (int position : edge[left]) {
            if (seen[position]) continue;
            seen[position] = 1;
            const int other = owner[position];
            if (other < 0 || self(self, other, seen)) {
                owner[position] = left;
                return true;
            }
        }
        return false;
    };
    int matching = 0;
    for (int left = 0; left < static_cast<int>(targets.size()); ++left) {
        vector<unsigned char> seen(n);
        matching += dfs(dfs, left, seen);
    }
    cout << "targets=" << targets.size() << " edges=" << edge_count
         << " matching=" << matching << '\n';
    if (matching < static_cast<int>(targets.size())) {
        vector<unsigned char> reach_left(targets.size()),reach_position(n);
        queue<int> todo;
        cout << "unmatched";
        for (int left = 0; left < static_cast<int>(targets.size()); ++left) {
            bool matched = false;
            for (int position : edge[left]) matched |= owner[position] == left;
            if (!matched) {
                reach_left[left]=1;todo.push(left);
                cout << ' ' << targets[left] << " candidates";
                for(int position:edge[left])
                    cout << ' ' << position << ':' << envelope[position]
                         << ':' << forced[position] << ':'
                         << (owner[position]<0?0:targets[owner[position]]);
            }
        }
        cout << '\n';
        while(!todo.empty()){
            const int left=todo.front();todo.pop();
            for(int position:edge[left])if(!reach_position[position]){
                reach_position[position]=1;
                if(owner[position]>=0&&!reach_left[owner[position]]){
                    reach_left[owner[position]]=1;todo.push(owner[position]);
                }
            }
        }
        int left_count=0,position_count=0;
        for(unsigned char value:reach_left)left_count+=value;
        for(unsigned char value:reach_position)position_count+=value;
        cout<<"hall left="<<left_count<<" positions="<<position_count<<" masks";
        if(left_count<=64)for(int left=0;left<(int)targets.size();++left)
            if(reach_left[left])cout<<' '<<targets[left];
        cout<<" places";
        if(position_count<=64)for(int position=0;position<n;++position)
            if(reach_position[position])cout<<' '<<position;
        cout<<'\n';
    }
}
