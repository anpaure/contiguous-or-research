#define main msw_factor_fibre_bfs_main
#include "msw_factor_fibre_bfs.cpp"
#undef main

#include <map>

struct Tagged { U64 q; std::string root; std::string history; };

static std::vector<Tagged> switch_tagged(const std::vector<Tagged>& cur,
                                         int n, int m, int a, int b,
                                         int wanted_root) {
    std::vector<int> own(U32{1} << n, -1), rown(U32{1} << n, -1);
    std::vector<U64> rhs(cur.size());
    for (int i = 0; i < (int)cur.size(); ++i) {
        for (U32 x : intervals(cur[i].q, n, m)) own[x] = i;
        rhs[i] = swap_labels(cur[i].q, n, a, b);
        for (U32 x : intervals(rhs[i], n, m)) rown[x] = i;
    }
    DSU d(2 * cur.size());
    for (U32 x = 0; x < (U32{1} << n); ++x)
        if (own[x] >= 0) d.u(own[x], cur.size() + rown[x]);
    std::vector<int> left, right;
    for (int i = 0; i < (int)cur.size(); ++i) {
        if (d.f(i) == wanted_root) left.push_back(i);
        if (d.f(cur.size() + i) == wanted_root) right.push_back(i);
    }
    std::cout << "component " << left.size() << " roots\n";
    for (int i : left)
        std::cout << " - " << cur[i].root << " history=" << cur[i].history
                  << "\n";
    std::vector<char> remove(cur.size());
    for (int i : left) remove[i] = 1;
    std::vector<Tagged> out;
    for (int i = 0; i < (int)cur.size(); ++i)
        if (!remove[i]) out.push_back(cur[i]);
    for (int i : right) {
        Tagged z = cur[i];
        z.q = rhs[i];
        z.history += "(" + std::to_string(a + 1) + " "
                   + std::to_string(b + 1) + ")";
        out.push_back(std::move(z));
    }
    std::sort(out.begin(), out.end(), [](const Tagged& x, const Tagged& y) {
        return x.q < y.q;
    });
    return out;
}

int main() {
    constexpr int m = 4, n = 9;
    std::vector<Tagged> f;
    std::function<void(int,int,int,U32)> gen = [&](int p, int u, int d,
                                                   U32 mask) {
        if (p == 2 * m) {
            U32 x = mask;
            std::vector<int> q;
            for (int e = 0; e < m; ++e) {
                auto aa = g(x, m); auto bb = hfun(aa.first, m);
                q.push_back(aa.second); q.push_back(bb.second); x = bb.first;
            }
            q.push_back(2 * m);
            std::string word;
            for (int i = 0; i < 2 * m; ++i)
                word += ((mask >> i) & 1U) ? '1' : '0';
            f.push_back({canon(q), word, ""});
            return;
        }
        if (u < m) gen(p + 1, u + 1, d, mask | (U32{1} << p));
        if (d < u) gen(p + 1, u, d + 1, mask);
    };
    gen(0, 0, 0, 0);
    std::sort(f.begin(), f.end(), [](const Tagged& x, const Tagged& y) {
        return x.q < y.q;
    });
    const int steps[4][3] = {{0,2,11},{1,3,3},{0,4,12},{0,1,4}};
    for (int s = 0; s < 4; ++s) {
        std::cout << "STEP " << s + 1 << '\n';
        f = switch_tagged(f, n, m, steps[s][0], steps[s][1], steps[s][2]);
    }
}
