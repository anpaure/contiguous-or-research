#include <algorithm>
#include <bit>
#include <fstream>
#include <iostream>
#include <set>
#include <string>
#include <vector>

using namespace std;

static int wt(int x) { return popcount(static_cast<unsigned>(x)); }

static vector<int> read_all(const string& path) {
    ifstream in(path);
    if (!in) throw runtime_error("cannot open " + path);
    vector<int> values;
    for (;;) {
        int x;
        if (in >> x) {
            values.push_back(x);
            continue;
        }
        if (in.eof()) break;
        throw runtime_error("non-integer input in " + path);
    }
    return values;
}

int main(int argc, char** argv) {
    if (argc != 3) {
        cerr << "usage: ml11_prescribed_extension_verify PATH CYCLE\n";
        return 2;
    }
    vector<int> path, cycle;
    try {
        path = read_all(argv[1]);
        cycle = read_all(argv[2]);
    } catch (const exception& e) {
        cerr << e.what() << '\n';
        return 2;
    }
    if (path.size() != 37 || cycle.size() != 924) {
        cerr << "wrong dimensions path=" << path.size()
             << " cycle=" << cycle.size() << '\n';
        return 1;
    }
    set<int> expected, actual(cycle.begin(), cycle.end());
    for (int x = 0; x < (1 << 11); ++x)
        if (wt(x) == 5 || wt(x) == 6) expected.insert(x);
    if (actual != expected || actual.size() != cycle.size()) {
        cerr << "cycle is not the complete middle two layers\n";
        return 1;
    }
    for (int i = 0; i < static_cast<int>(cycle.size()); ++i) {
        const int x = cycle[i], y = cycle[(i + 1) % cycle.size()];
        if (abs(wt(x) - wt(y)) != 1 || wt(x ^ y) != 1 ||
            ((x & y) != x && (x & y) != y)) {
            cerr << "bad cycle edge at " << i << '\n';
            return 1;
        }
    }
    for (int x : path)
        if (!actual.count(x)) {
            cerr << "path vertex absent from cycle\n";
            return 1;
        }
    int start = -1, direction = 0;
    for (int i = 0; i < static_cast<int>(cycle.size()); ++i) {
        if (cycle[i] != path[0]) continue;
        for (int dir : {-1, 1}) {
            bool okay = true;
            for (int j = 0; j < static_cast<int>(path.size()); ++j)
                if (cycle[(i + dir * j + cycle.size() * path.size()) %
                          cycle.size()] != path[j]) {
                    okay = false;
                    break;
                }
            if (okay) {
                start = i;
                direction = dir;
            }
        }
    }
    if (start < 0) {
        cerr << "prescribed path is not consecutive in the cycle\n";
        return 1;
    }

    // Choose the 93-rank-six cut arc wholly outside the prescribed block:
    // start immediately after the last prescribed vertex and take the next
    // 93 upper-layer vertices in the completion direction.  The outside arc
    // has 443 upper vertices, so this never meets the prescribed block.
    vector<int> cut93;
    int position = (start + direction * static_cast<int>(path.size()) +
                    cycle.size() * path.size()) % cycle.size();
    const int first_cut_colour = cycle[position];
    if (wt(first_cut_colour) != 5) {
        cerr << "first cut is not a rank-five vertex\n";
        return 1;
    }
    while (cut93.size() < 93) {
        if (wt(cycle[position]) == 6) cut93.push_back(cycle[position]);
        position = (position + direction + cycle.size()) % cycle.size();
    }
    const int second_cut_colour = cycle[position];
    if (wt(second_cut_colour) != 5 || first_cut_colour == second_cut_colour) {
        cerr << "second cut is invalid\n";
        return 1;
    }
    if (find(path.begin(), path.end(), first_cut_colour) != path.end() ||
        find(path.begin(), path.end(), second_cut_colour) != path.end()) {
        cerr << "a cut colour lies on the prescribed path\n";
        return 1;
    }
    set<int> path6, cut6(cut93.begin(), cut93.end());
    for (int x : path) if (wt(x) == 6) path6.insert(x);
    for (int x : cut6) if (path6.count(x)) {
        cerr << "93-cut arc intersects prescribed rank-six block\n";
        return 1;
    }
    set<int> all6;
    for (int x : cycle) if (wt(x) == 6) all6.insert(x);
    set<int> cut369;
    set_difference(all6.begin(), all6.end(), cut6.begin(), cut6.end(),
                   inserter(cut369, cut369.end()));
    if (cut6.size() != 93 || cut369.size() != 369 ||
        !includes(cut369.begin(), cut369.end(), path6.begin(), path6.end())) {
        cerr << "invalid complementary 369/93 split\n";
        return 1;
    }
    cout << "PASS ML_11 Hamilton cycle vertices=924 edges=924"
            " prescribed_vertices=37 prescribed_edges=36"
            " cut369_rank6=369 cut93_rank6=93"
            " cuts_outside_prefix=yes disjoint_from_prefix=yes direction="
         << direction << " cut_colours=" << first_cut_colour << ','
         << second_cut_colour << '\n';
}
