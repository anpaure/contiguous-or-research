#include <algorithm>
#include <array>
#include <iostream>
#include <numeric>
#include <vector>

using Order = std::array<int, 9>;

static constexpr std::array<Order, 4> negative{{
    {{1,8,6,7,4,5,3,9,2}},
    {{1,9,8,6,7,4,5,2,3}},
    {{1,5,3,9,8,6,7,2,4}},
    {{1,7,3,9,4,5,8,2,6}},
}};

static constexpr std::array<Order, 4> positive{{
    {{1,9,3,5,4,7,6,8,2}},
    {{1,5,4,7,6,8,9,2,3}},
    {{1,7,6,8,9,3,5,2,4}},
    {{1,8,5,4,9,3,7,2,6}},
}};

static int kendall(const std::vector<int>& a, const std::vector<int>& b) {
    std::vector<int> pos(a.size() + 1);
    for (int i = 0; i < (int)a.size(); ++i) pos[a[i]] = i;
    std::vector<int> p;
    for (int x : b) p.push_back(pos[x]);
    int inv = 0;
    for (int i = 0; i < (int)p.size(); ++i)
        for (int j = i + 1; j < (int)p.size(); ++j)
            inv += p[i] > p[j];
    return inv;
}

static int cyclic_distance(const Order& aa, const Order& bb) {
    std::vector<int> a(aa.begin(), aa.end()), b(bb.begin(), bb.end());
    int best = 1000000, n = (int)a.size();
    for (int rev = 0; rev < 2; ++rev) {
        std::vector<int> c = b;
        if (rev) std::reverse(c.begin(), c.end());
        for (int shift = 0; shift < n; ++shift) {
            std::rotate(c.begin(), c.begin() + 1, c.end());
            best = std::min(best, kendall(a, c));
        }
    }
    return best;
}

template<class Family>
static void report(const char* name, const Family& f) {
    std::cout << name << '\n';
    int minimum = 1000000;
    for (int i = 0; i < (int)f.size(); ++i)
        for (int j = i + 1; j < (int)f.size(); ++j) {
            int d = cyclic_distance(f[i], f[j]);
            minimum = std::min(minimum, d);
            std::cout << i << ' ' << j << ' ' << d << '\n';
        }
    std::cout << "minimum " << minimum << '\n';
}

int main() {
    report("negative", negative);
    report("positive", positive);
}
