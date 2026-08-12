#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

static vector<int> gray(int n, int r) {
    if (!r) return {0};
    if (r == n) return {(1 << n) - 1};
    vector<int> a = gray(n - 1, r), b = gray(n - 1, r - 1);
    reverse(b.begin(), b.end());
    for (int& x : b) x |= 1 << (n - 1);
    a.insert(a.end(), b.begin(), b.end());
    return a;
}

int main(int argc, char** argv) {
    if (argc != 3) return 2;
    for (int x : gray(stoi(argv[1]), stoi(argv[2]))) cout << x << ' ';
    cout << '\n';
}
