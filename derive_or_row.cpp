#include <iostream>
#include <vector>
using namespace std;
int main(int argc, char** argv) {
    if (argc != 2) return 2;
    const int d = stoi(argv[1]);
    vector<int> row;
    for (int value; cin >> value;) row.push_back(value);
    for (int q = 0; q < d; ++q) {
        vector<int> next;
        for (int i = 0; i + 1 < static_cast<int>(row.size()); ++i)
            next.push_back(row[i] | row[i + 1]);
        row.swap(next);
    }
    for (int value : row) cout << value << ' ';
    cout << '\n';
}
