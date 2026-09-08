#include "cadical.hpp"

#include <cctype>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

using namespace std;

static vector<int> read_assumptions(const string& path) {
    ifstream input(path);
    if (!input) throw runtime_error("cannot open assumptions file");
    vector<int> result;
    string line;
    while (getline(input, line)) {
        if (line.empty() || line[0] == 'c') continue;
        if (line[0] != 'a') throw runtime_error("expected DIMACS a-line");
        size_t position = 1;
        while (position < line.size()) {
            while (position < line.size() && isspace(static_cast<unsigned char>(line[position])))
                ++position;
            if (position == line.size()) break;
            size_t end = position;
            while (end < line.size() && !isspace(static_cast<unsigned char>(line[end]))) ++end;
            const int literal = stoi(line.substr(position, end - position));
            position = end;
            if (!literal) break;
            result.push_back(literal);
        }
    }
    if (result.empty()) throw runtime_error("assumptions file has no literals");
    return result;
}

int main(int argc, char** argv) {
    try {
        if (argc < 4 || argc > 6) {
            cerr << "usage: q369_cadical_assumption_core FORMULA.cnf "
                    "ASSUMPTIONS OUTPUT.core [SEED] [--minimize]\n";
            return 2;
        }
        int seed = 0;
        bool minimize = false;
        for (int arg = 4; arg < argc; ++arg) {
            if (string(argv[arg]) == "--minimize") minimize = true;
            else seed = stoi(argv[arg]);
        }
        const vector<int> assumptions = read_assumptions(argv[2]);
        CaDiCaL::Solver solver;
        solver.set("quiet", 1);
        solver.set("seed", seed);
        int variables = 0;
        if (const char* error = solver.read_dimacs(argv[1], variables, 1))
            throw runtime_error(error);
        for (int literal : assumptions) {
            if (literal <= 0 || literal > variables)
                throw runtime_error("assumption variable out of range");
            solver.assume(literal);
        }
        const int status = solver.solve();
        if (status != 20) {
            cerr << "status=" << status << " (expected UNSAT=20)\n";
            return status == 10 ? 10 : 1;
        }
        vector<int> core;
        for (int literal : assumptions)
            if (solver.failed(literal)) core.push_back(literal);
        int minimization_solves = 0;
        if (minimize) {
            size_t index = 0;
            while (index < core.size()) {
                vector<int> trial;
                trial.reserve(core.size() - 1);
                for (size_t i = 0; i < core.size(); ++i)
                    if (i != index) trial.push_back(core[i]);
                for (int literal : trial) solver.assume(literal);
                const int trial_status = solver.solve();
                ++minimization_solves;
                if (trial_status == 20) {
                    vector<int> failed;
                    for (int literal : trial)
                        if (solver.failed(literal)) failed.push_back(literal);
                    if (failed.size() >= core.size())
                        throw runtime_error("failed core did not shrink after deletion");
                    core.swap(failed);
                    index = 0;
                } else if (trial_status == 10) {
                    ++index;
                } else {
                    throw runtime_error("UNKNOWN during core minimization");
                }
            }
        }
        ofstream output(argv[3]);
        if (!output) throw runtime_error("cannot open core output");
        output << "c assumptions " << assumptions.size() << " core " << core.size() << '\n';
        output << 'a';
        for (int literal : core) output << ' ' << literal;
        output << " 0\n";
        cerr << "UNSAT assumptions=" << assumptions.size()
             << " failed=" << core.size()
             << " minimization_solves=" << minimization_solves << '\n';
        return 20;
    } catch (const exception& error) {
        cerr << "error: " << error.what() << '\n';
        return 2;
    }
}
