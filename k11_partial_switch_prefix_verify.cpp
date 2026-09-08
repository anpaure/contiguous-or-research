#include <algorithm>
#include <bit>
#include <fstream>
#include <iostream>
#include <set>
#include <string>
#include <vector>

using namespace std;

static int wt(int x) { return popcount(static_cast<unsigned>(x)); }

static vector<int> read_vector(ifstream& in) {
    int n = -1;
    if (!(in >> n) || n < 0) throw runtime_error("invalid vector length");
    vector<int> values(n);
    for (int& x : values)
        if (!(in >> x)) throw runtime_error("truncated vector");
    return values;
}

int main(int argc, char** argv) {
    if (argc != 2) {
        cerr << "usage: k11_partial_switch_prefix_verify CERTIFICATE\n";
        return 2;
    }
    ifstream in(argv[1]);
    if (!in) {
        cerr << "cannot open certificate\n";
        return 2;
    }
    vector<int> a, p, u;
    int seam = -1;
    try {
        a = read_vector(in);
        p = read_vector(in);
        u = read_vector(in);
        if (!(in >> seam)) throw runtime_error("missing seam");
    } catch (const exception& e) {
        cerr << e.what() << '\n';
        return 2;
    }
    string junk;
    if (in >> junk) {
        cerr << "trailing certificate data\n";
        return 2;
    }
    if (a.size() != 22 || p.size() != 19 || u.size() != 18 || seam != 958) {
        cerr << "wrong certificate dimensions\n";
        return 1;
    }
    for (int x : a)
        if (x <= 0 || x >= (1 << 11)) {
            cerr << "invalid array entry\n";
            return 1;
        }
    const vector<int> missing7{
        251, 493, 607, 941, 956, 1267,
        1468, 1694, 1763, 1884, 1946, 1990,
    };
    set<int> p_seen, u_seen;
    for (int i = 0; i < 19; ++i) {
        const int triple = a[i] | a[i + 1] | a[i + 2];
        if (triple != p[i] || wt(p[i]) != 6 || !p_seen.insert(p[i]).second) {
            cerr << "bad rank-six triple at " << i + 1 << '\n';
            return 1;
        }
    }
    for (int i = 0; i < 18; ++i) {
        const int portal = a[i] | a[i + 1] | a[i + 2] | a[i + 3];
        if (portal != u[i] || portal != (p[i] | p[i + 1]) || wt(u[i]) != 7 ||
            !u_seen.insert(u[i]).second) {
            cerr << "bad rank-seven portal at " << i + 1 << '\n';
            return 1;
        }
    }
    for (int target : missing7)
        if (!u_seen.count(target)) {
            cerr << "missing required rank-seven portal " << target << '\n';
            return 1;
        }
    const int seam_value = a[18] | a[19] | a[20] | a[21];
    if (seam_value != seam || wt(seam_value) != 8) {
        cerr << "bad rank-eight seam\n";
        return 1;
    }
    const int continuation_core = a[19] | a[20] | a[21];
    if (continuation_core != 550 || wt(continuation_core) != 4) {
        cerr << "bad continuation core\n";
        return 1;
    }
    cout << "PASS q=19 rank6_triples=19 rank7_portals=18"
            " required_rank7=12 seam=958 continuation_core=550/rank4\n";
}
