#include <iostream>
#include <stdexcept>
#include <vector>
using namespace std;

int main(int argc, char** argv) {
    if (argc != 3) return 2;
    const int position = stoi(argv[1]);
    const int replacement = stoi(argv[2]);
    vector<int> values;
    for (int value; cin >> value;) values.push_back(value);
    if (position < 0 || position >= static_cast<int>(values.size()))
        throw out_of_range("position");
    values[position] = replacement;
    for (int value : values) cout << value << ' ';
    cout << '\n';
}
