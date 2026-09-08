#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(int argc, char** argv) {
    if (argc < 5) return 2;
    const int k = stoi(argv[1]);
    ifstream array_input(argv[2]), model_input(argv[3]);
    vector<int> positions;
    for (int i = 4; i < argc; ++i) positions.push_back(stoi(argv[i]));
    sort(positions.begin(), positions.end());
    positions.erase(unique(positions.begin(), positions.end()), positions.end());
    vector<int> a;
    for (int value; array_input >> value;) a.push_back(value);
    vector<uint8_t> truth(positions.size() * k + 1);
    string token;
    while (model_input >> token) {
        if (token == "s") {
            model_input >> token;
            if (token != "SATISFIABLE") return 1;
        } else if (token != "v") {
            const int literal = stoi(token);
            if (literal > 0 && literal < static_cast<int>(truth.size()))
                truth[literal] = 1;
        }
    }
    for (int i = 0; i < static_cast<int>(positions.size()); ++i) {
        int value = 0;
        for (int bit = 0; bit < k; ++bit) {
            const bool raw = truth[i * k + bit + 1];
            const bool seed_bit = a[positions[i]] & (1 << bit);
            if (raw ^ seed_bit) value |= 1 << bit;
        }
        a[positions[i]] = value;
    }
    for (int value : a) cout << value << ' ';
    cout << '\n';
}
