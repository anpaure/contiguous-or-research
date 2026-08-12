#include <cstdlib>
#include <fstream>
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

static vector<vector<int>> read_cnf(const string& path, int& variables) {
    ifstream input(path);
    if (!input) throw runtime_error("cannot open CNF");
    string token;
    long long declared_clauses = -1;
    vector<vector<int>> clauses;
    while (input >> token) {
        if (token == "c") {
            string rest;
            getline(input, rest);
            continue;
        }
        if (token == "p") {
            string kind;
            input >> kind >> variables >> declared_clauses;
            if (kind != "cnf") throw runtime_error("bad header");
            continue;
        }
        int literal = stoi(token);
        vector<int> clause;
        while (literal) {
            clause.push_back(literal);
            if (!(input >> literal)) throw runtime_error("truncated clause");
        }
        clauses.push_back(std::move(clause));
    }
    if (variables < 1 || declared_clauses != static_cast<long long>(clauses.size()))
        throw runtime_error("CNF header mismatch");
    return clauses;
}

static unordered_map<int, int> read_targets(const string& path) {
    ifstream input(path);
    if (!input) throw runtime_error("cannot open selector map");
    unordered_map<int, int> result;
    string line;
    while (getline(input, line)) {
        if (line.empty()) continue;
        istringstream parser(line);
        int variable, target;
        if (!(parser >> variable >> target)) throw runtime_error("bad selector map line");
        result[variable] = target;
    }
    return result;
}

static string clause_smt(const vector<int>& clause) {
    if (clause.empty()) return "false";
    if (clause.size() == 1)
        return clause[0] > 0 ? "v" + to_string(clause[0])
                             : "(not v" + to_string(-clause[0]) + ")";
    string result = "(or";
    for (int literal : clause) {
        result += " ";
        if (literal < 0) result += "(not v" + to_string(-literal) + ")";
        else result += "v" + to_string(literal);
    }
    return result + ")";
}

int main(int argc, char** argv) {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    try {
        if (argc != 4) {
            cerr << "usage: q369_core_named_smt CORE_CNF SELECTOR_MAP OUTPUT\n";
            return 2;
        }
        int variables = 0;
        const auto clauses = read_cnf(argv[1], variables);
        const auto targets = read_targets(argv[2]);
        ofstream output(argv[3]);
        if (!output) throw runtime_error("cannot open output");
        output << "(set-logic QF_BOOL)\n"
               << "(set-option :produce-unsat-cores true)\n"
               << "(set-option :sat.core.minimize true)\n";
        for (int variable = 1; variable <= variables; ++variable)
            output << "(declare-fun v" << variable << " () Bool)\n";
        int named = 0;
        for (const auto& clause : clauses) {
            bool target_clause = !clause.empty();
            int target = -1;
            for (int literal : clause) {
                auto found = targets.find(literal);
                if (literal <= 0 || found == targets.end()) {
                    target_clause = false;
                    break;
                }
                if (target < 0) target = found->second;
                else if (target != found->second) throw runtime_error("mixed target clause");
            }
            const string formula = clause_smt(clause);
            if (target_clause) {
                output << "(assert (! " << formula << " :named t" << target << "))\n";
                ++named;
            } else {
                output << "(assert " << formula << ")\n";
            }
        }
        output << "(check-sat)\n(get-unsat-core)\n";
        cerr << "variables=" << variables << " clauses=" << clauses.size()
             << " named_targets=" << named << '\n';
        return 0;
    } catch (const exception& error) {
        cerr << "error: " << error.what() << '\n';
        return 2;
    }
}
