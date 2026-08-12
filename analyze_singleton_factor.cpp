#include <algorithm>
#include <bit>
#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char** argv) {
    if (argc != 3) return 2;
    const int k = stoi(argv[1]), d = stoi(argv[2]);
    vector<int> central;
    for (int value; cin >> value;) central.push_back(value);
    const int n = central.size() + d;
    vector<int> envelope(n, (1 << k) - 1), forced(n);
    for (int position = 0; position < n; ++position)
        for (int i = max(0, position - d);
             i <= min(static_cast<int>(central.size()) - 1, position); ++i)
            envelope[position] &= central[i];
    for (int bit = 0; bit < k; ++bit)
        for (int i = 0; i < static_cast<int>(central.size()); ++i)
            if (central[i] & (1 << bit)) {
                int only = -1, count = 0;
                for (int position = i; position <= i + d; ++position)
                    if (envelope[position] & (1 << bit)) {
                        only = position;
                        ++count;
                    }
                if (count == 1) forced[only] |= 1 << bit;
            }
    vector<vector<int>> candidate(k);
    for (int bit = 0; bit < k; ++bit)
        for (int position = 0; position < n; ++position)
            if ((envelope[position] & (1 << bit)) &&
                !(forced[position] & ~(1 << bit)))
                candidate[bit].push_back(position);

    vector<int> owner(n, -1);
    auto augment = [&] (auto&& self, int bit, vector<unsigned char>& seen) -> bool {
        for (int position : candidate[bit]) if (!seen[position]) {
            seen[position] = 1;
            if (owner[position] < 0 || self(self, owner[position], seen)) {
                owner[position] = bit;
                return true;
            }
        }
        return false;
    };
    int matching = 0;
    for (int bit = 0; bit < k; ++bit) {
        vector<unsigned char> seen(n);
        matching += augment(augment, bit, seen);
    }
    cout << "matching=" << matching << '/' << k << '\n';
    for (int bit = 0; bit < k; ++bit) {
        cout << "bit=" << bit << " candidates=" << candidate[bit].size();
        if (candidate[bit].size() <= 20)
            for (int position : candidate[bit]) cout << ' ' << position;
        cout << '\n';
    }
    cout << "forced_positions";
    for (int position = 0; position < n; ++position)
        if (forced[position]) cout << ' ' << position << ':' << forced[position];
    cout << '\n';
}
