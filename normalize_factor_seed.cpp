#include <algorithm>
#include <bit>
#include <iostream>
#include <stdexcept>
#include <vector>
using namespace std;

int main(int argc, char** argv) {
    if (argc != 3) return 2;
    const int k = stoi(argv[1]);
    const int d = stoi(argv[2]);
    vector<int> a;
    for (int value; cin >> value;) a.push_back(value);
    if (a.size() < static_cast<size_t>(d + 2)) return 2;
    int first = 0, second = 0;
    for (int i = 0; i <= d; ++i) first |= a[i];
    for (int i = 1; i <= d + 1; ++i) second |= a[i];
    const int rank = popcount(static_cast<unsigned>(first));
    if (popcount(static_cast<unsigned>(second)) != rank ||
        popcount(static_cast<unsigned>(first ^ second)) != 2)
        throw runtime_error("first central pair is not Johnson-adjacent");
    vector<int> common, first_only, second_only, outside;
    for (int bit = 0; bit < k; ++bit) {
        const bool x = first & (1 << bit), y = second & (1 << bit);
        if (x && y) common.push_back(bit);
        else if (x) first_only.push_back(bit);
        else if (y) second_only.push_back(bit);
        else outside.push_back(bit);
    }
    vector<int> permutation(k, -1);
    for (int i = 0; i < rank - 1; ++i) permutation[common[i]] = i;
    permutation[first_only[0]] = rank - 1;
    permutation[second_only[0]] = rank;
    for (int i = 0; i < static_cast<int>(outside.size()); ++i)
        permutation[outside[i]] = rank + 1 + i;
    for (int value : a) {
        int transformed = 0;
        for (int bit = 0; bit < k; ++bit)
            if (value & (1 << bit)) transformed |= 1 << permutation[bit];
        cout << transformed << ' ';
    }
    cout << '\n';
}
