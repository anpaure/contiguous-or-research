#include <fstream>
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>

using namespace std;

constexpr int K = 11;
constexpr int N = 465;
constexpr int LIMIT = 1 << K;

static int xvar(int position, int bit) {
    return position * K + bit + 1;
}

int main(int argc, char** argv) {
    try {
        if (argc != 8) {
            cerr << "usage: q369_forbid_duplicate_cnf INPUT.cnf OUTPUT.cnf "
                    "L1 R1 L2 R2 MASK\n"
                    "positions are zero-based and inclusive\n";
            return 2;
        }
        const int left1 = stoi(argv[3]), right1 = stoi(argv[4]);
        const int left2 = stoi(argv[5]), right2 = stoi(argv[6]);
        const int mask = stoi(argv[7]);
        if (left1 < 0 || left1 > right1 || right1 >= N ||
            left2 < 0 || left2 > right2 || right2 >= N ||
            mask < 0 || mask >= LIMIT)
            throw runtime_error("invalid cell or mask");

        ifstream input(argv[1]);
        if (!input) throw runtime_error("cannot open input CNF");
        vector<string> prefix, clauses;
        string line;
        int variables = -1;
        long long clause_count = -1;
        while (getline(input, line)) {
            if (line.empty() || line[0] == 'c') {
                prefix.push_back(line);
                continue;
            }
            if (line[0] == 'p') {
                string p, format;
                istringstream parser(line);
                parser >> p >> format >> variables >> clause_count;
                if (!parser || p != "p" || format != "cnf")
                    throw runtime_error("invalid DIMACS header");
                break;
            }
            throw runtime_error("content before DIMACS header");
        }
        if (variables < N * K || clause_count < 0)
            throw runtime_error("missing or incompatible DIMACS header");
        while (getline(input, line)) clauses.push_back(line);

        vector<vector<int>> added;
        vector<int> deviation;
        auto encode_cell = [&](int left, int right) {
            for (int bit = 0; bit < K; ++bit) {
                const int value = ++variables;
                vector<int> backward{-value};
                for (int p = left; p <= right; ++p) {
                    const int x = xvar(p, bit);
                    added.push_back({-x, value});
                    backward.push_back(x);
                }
                added.push_back(move(backward));
                // This literal is true exactly when the cell OR differs from
                // MASK in this coordinate.
                deviation.push_back(mask & (1 << bit) ? -value : value);
            }
        };
        encode_cell(left1, right1);
        encode_cell(left2, right2);
        added.push_back(move(deviation));

        ofstream output(argv[2]);
        if (!output) throw runtime_error("cannot open output CNF");
        for (const string& comment : prefix) output << comment << '\n';
        output << "p cnf " << variables << ' ' << clause_count + added.size() << '\n';
        for (const string& clause : clauses) output << clause << '\n';
        for (const vector<int>& clause : added) {
            for (int literal : clause) output << literal << ' ';
            output << "0\n";
        }
        cerr << "added_variables=" << 2 * K
             << " added_clauses=" << added.size() << '\n';
        return 0;
    } catch (const exception& error) {
        cerr << "error: " << error.what() << '\n';
        return 2;
    }
}
