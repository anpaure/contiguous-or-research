#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(int argc, char** argv) {
    if (argc != 5) return 2;
    const int k = stoi(argv[1]);
    const int n = stoi(argv[2]);
    const int gap = stoi(argv[3]);
    ifstream input(argv[4]);
    vector<uint8_t> truth((n + 1) * k + 1);
    string token;
    bool sat = false;
    while (input >> token) {
        if (token == "s") {
            input >> token;
            sat = token == "SATISFIABLE";
        } else if (token != "v") {
            const int literal = stoi(token);
            if (literal > 0 && literal < static_cast<int>(truth.size()))
                truth[literal] = 1;
        }
    }
    if (!sat) return 1;
    vector<int> values(n + 1);
    for (int entry = 0; entry <= n; ++entry)
        for (int bit = 0; bit < k; ++bit)
            if (truth[entry * k + bit + 1]) values[entry] |= 1 << bit;
    for (int position = 0; position <= n; ++position) {
        const int entry = position == gap ? n
            : position - (position > gap);
        cout << values[entry] << ' ';
    }
    cout << '\n';
}
