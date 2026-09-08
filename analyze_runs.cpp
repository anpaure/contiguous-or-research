#include <iostream>
#include <vector>
using namespace std;
int main(int argc, char** argv) {
    if (argc != 3) return 2;
    const int k = stoi(argv[1]), d = stoi(argv[2]);
    vector<int> path;
    for (int value; cin >> value;) path.push_back(value);
    int deficit = 0;
    for (int bit = 0; bit < k; ++bit) {
        int i = 0;
        while (i < static_cast<int>(path.size())) {
            if (!(path[i] & (1 << bit))) { ++i; continue; }
            const int first = i;
            while (i < static_cast<int>(path.size()) && (path[i] & (1 << bit))) ++i;
            if (first && i < static_cast<int>(path.size()) && i - first < d + 1) {
                const int value = d + 1 - (i - first);
                deficit += value;
                cout << "bit=" << bit << " run=[" << first << ',' << i - 1
                     << "] length=" << i - first << " deficit=" << value << '\n';
            }
        }
    }
    cout << "total=" << deficit << '\n';
}
