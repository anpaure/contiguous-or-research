#include <algorithm>
#include <iostream>
using namespace std;

int main(int argc, char** argv) {
    if (argc != 2) return 2;
    const int full = (1 << stoi(argv[1])) - 1;
    for (int x; cin >> x;) cout << (full ^ x) << ' ';
    cout << '\n';
}
