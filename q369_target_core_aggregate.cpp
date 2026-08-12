#include <algorithm>
#include <cctype>
#include <fstream>
#include <iostream>
#include <map>
#include <stdexcept>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

struct Target { int mask, rank; };

int main(int argc, char** argv) {
    try {
        if (argc < 3) {
            cerr << "usage: q369_target_core_aggregate GUARDMAP.tsv CORE...\n";
            return 2;
        }
        ifstream map_input(argv[1]);
        if (!map_input) throw runtime_error("cannot open guard map");
        string header;
        getline(map_input, header);
        unordered_map<int, Target> target;
        for (int guard, mask, rank; map_input >> guard >> mask >> rank;)
            target.emplace(guard, Target{mask, rank});
        if (target.empty()) throw runtime_error("empty guard map");

        map<int, int> frequency;
        vector<int> core_sizes;
        for (int arg = 2; arg < argc; ++arg) {
            ifstream input(argv[arg]);
            if (!input) throw runtime_error("cannot open " + string(argv[arg]));
            string line;
            vector<int> core;
            while (getline(input, line)) {
                if (line.empty() || line[0] == 'c') continue;
                if (line[0] != 'a') throw runtime_error("invalid core a-line");
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
                    if (!target.count(literal)) throw runtime_error("unknown core guard");
                    core.push_back(literal);
                }
            }
            sort(core.begin(), core.end());
            core.erase(unique(core.begin(), core.end()), core.end());
            core_sizes.push_back(core.size());
            for (int guard : core) ++frequency[guard];
        }

        const int cores = argc - 2;
        vector<int> by_frequency(cores + 1), common_by_rank(12);
        for (const auto [guard, count] : frequency) {
            ++by_frequency[count];
            if (count == cores) ++common_by_rank[target.at(guard).rank];
        }
        cout << "cores=" << cores << " sizes";
        for (int size : core_sizes) cout << ' ' << size;
        cout << "\nfrequency";
        for (int value = 1; value <= cores; ++value)
            if (by_frequency[value]) cout << ' ' << value << ':' << by_frequency[value];
        cout << "\ncommon_by_rank";
        for (int rank = 1; rank <= 5; ++rank)
            cout << ' ' << rank << ':' << common_by_rank[rank];
        cout << "\ncommon_targets";
        vector<Target> common;
        for (const auto [guard, count] : frequency)
            if (count == cores) common.push_back(target.at(guard));
        sort(common.begin(), common.end(), [](Target a, Target b) { return a.mask < b.mask; });
        for (Target value : common) cout << ' ' << value.mask;
        cout << '\n';
        return 0;
    } catch (const exception& error) {
        cerr << "error: " << error.what() << '\n';
        return 2;
    }
}
