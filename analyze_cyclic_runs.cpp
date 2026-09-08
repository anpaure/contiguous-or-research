#include <bit>
#include <iostream>
#include <vector>
using namespace std;

int main(int argc, char** argv) {
    if (argc != 3) return 2;
    const int k = stoi(argv[1]), minimum = stoi(argv[2]);
    vector<int> path;
    for (int value; cin >> value;) path.push_back(value);
    int deficit = 0;
    for (int bit = 0; bit < k; ++bit) {
        vector<int> starts;
        for (int i = 0; i < static_cast<int>(path.size()); ++i)
            if ((path[i] & (1 << bit)) &&
                !(path[(i + path.size() - 1) % path.size()] & (1 << bit)))
                starts.push_back(i);
        for (int start : starts) {
            int length = 0;
            while (length < static_cast<int>(path.size()) &&
                   (path[(start + length) % path.size()] & (1 << bit))) ++length;
            if (length < minimum) {
                deficit += minimum - length;
                cout << "bit=" << bit << " start=" << start
                     << " length=" << length << '\n';
            }
        }
    }
    cout << "total=" << deficit << '\n';
}
