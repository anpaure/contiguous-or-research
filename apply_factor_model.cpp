#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int main(int argc, char** argv) {
    if (argc != 4 && argc != 5) return 2;
    const int k = stoi(argv[1]);
    const int n = stoi(argv[2]);
    const bool append_extra = argc == 5;
    const int extra = append_extra ? stoi(argv[3]) : 0;
    ifstream input(argv[append_extra ? 4 : 3]);
    vector<uint8_t> truth(n * k + 1);
    string line;
    bool sat = false;
    while (getline(input, line)) {
        istringstream values(line);
        string prefix;
        if (!(values >> prefix)) continue;
        if (prefix == "s") {
            string status;
            values >> status;
            sat = status == "SATISFIABLE";
        } else if (prefix == "v") {
            for (int literal; values >> literal;) {
                if (!literal) break;
            if (literal > 0 && literal < static_cast<int>(truth.size()))
                truth[literal] = 1;
            }
        }
    }
    if (!sat) return 1;
    for (int position = 0; position < n; ++position) {
        int value = 0;
        for (int bit = 0; bit < k; ++bit)
            if (truth[position * k + bit + 1]) value |= 1 << bit;
        cout << value << ' ';
    }
    if (append_extra) cout << extra << ' ';
    cout << '\n';
}
