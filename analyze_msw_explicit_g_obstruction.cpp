#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <tuple>
#include <vector>

using namespace std;

struct Step { uint64_t word; int bit; };

static Step gstep(uint64_t x, int m) {
    vector<int> before(2 * m);
    int h = 0, d0 = 0;
    for (int i = 0; i < 2 * m; ++i) {
        before[i] = h;
        if (!(x >> i & 1ULL) && h == 0) ++d0;
        h += (x >> i & 1ULL) ? 1 : -1;
    }
    int ord = 0;
    for (int i = 0; i < 2 * m; ++i)
        if (!(x >> i & 1ULL) && (before[i] == 0 || before[i] == 1) &&
            ++ord == d0 + 1)
            return {x | (1ULL << i), i};
    return {0, -1};
}

static Step hstep(uint64_t y, int m) {
    vector<int> before(2 * m);
    int h = 0, u1 = 0;
    for (int i = 0; i < 2 * m; ++i) {
        before[i] = h;
        if ((y >> i & 1ULL) && h == 1) ++u1;
        h += (y >> i & 1ULL) ? 1 : -1;
    }
    int ord = 0;
    for (int i = 0; i < 2 * m; ++i)
        if ((y >> i & 1ULL) && (before[i] == 0 || before[i] == 1) &&
            ++ord == u1)
            return {y & ~(1ULL << i), i};
    return {0, -1};
}

static int flaws(uint64_t x, int m) {
    int h = 0, e = 0;
    for (int i = 0; i < 2 * m; ++i) {
        bool up = x >> i & 1ULL;
        h += up ? 1 : -1;
        if (!up && h < 0) ++e;
    }
    return e;
}

static uint64_t target(int m) {
    uint64_t z = 0;
    for (int p : {1, 2, 3, 5, 6, 8}) z |= 1ULL << (p - 1);
    for (int p = 9; p <= m + 4; ++p) z |= 1ULL << (p - 1);
    return z;
}

int main(int argc, char **argv) {
    int max_m = argc > 1 ? stoi(argv[1]) : 20;
    for (int m = 4; m <= max_m; ++m) {
        uint64_t s = target(m);
        vector<tuple<int,int,int,int,int,int>> stage1;
        vector<tuple<int,int,int,int>> full;
        for (int p = 0; p < 2 * m; ++p) if (s >> p & 1ULL)
        for (int q = p + 1; q < 2 * m; ++q) if (s >> q & 1ULL) {
            uint64_t x = s & ~(1ULL << p) & ~(1ULL << q);
            Step gs = gstep(x, m);
            if (gs.bit != p && gs.bit != q) continue;
            int b = gs.bit == p ? q : p;
            int e = flaws(x, m);
            int actual_b = -1;
            int actual_a = -1;
            if (e > 0) {
                for (int cand_b = 0; cand_b < 2 * m; ++cand_b)
                    if (!(x >> cand_b & 1ULL)) {
                        for (int a = 0; a < 2 * m; ++a) if (x >> a & 1ULL) {
                            uint64_t prev = (x & ~(1ULL << a)) | (1ULL << cand_b);
                            Step gp = gstep(prev, m);
                            Step hp = gp.bit < 0 ? Step{0,-1} : hstep(gp.word, m);
                            if (hp.word == x && hp.bit == cand_b) {
                                actual_b = cand_b;
                                actual_a = a;
                            }
                        }
                    }
            }
            stage1.emplace_back(p + 1, q + 1, gs.bit + 1, e,
                                actual_a + 1, actual_b + 1);
            if (e == 0) continue;
            bool ok = false;
            for (int a = 0; a < 2 * m; ++a) if (x >> a & 1ULL) {
                uint64_t prev = (x & ~(1ULL << a)) | (1ULL << b);
                Step gp = gstep(prev, m);
                Step hp = gp.bit < 0 ? Step{0,-1} : hstep(gp.word, m);
                if (hp.word == x && hp.bit == b) { ok = true; break; }
            }
            if (ok) full.emplace_back(p + 1, q + 1, gs.bit + 1, e);
        }
        cout << "m=" << m << " stage1=" << stage1.size() << " full=" << full.size() << " pairs=";
        for (auto [p,q,a,e,ap,b] : stage1)
            cout << '(' << p << ',' << q << ";a='" << a << ",e=" << e
                 << ",aprev=" << ap << ",bprev=" << b << ")";
        cout << '\n';
    }
}
