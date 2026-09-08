#include <algorithm>
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <numeric>
#include <random>
#include <string>
#include <vector>

static std::uint64_t choose_u64(int n, int k) {
    if (k < 0 || k > n) return 0;
    if (k > n - k) k = n - k;
    std::uint64_t z = 1;
    for (int i = 1; i <= k; ++i) {
        z = z * static_cast<std::uint64_t>(n - k + i) / i;
    }
    return z;
}

struct Edge {
    std::vector<int> m;
    std::vector<int> l;
};

int main(int argc, char** argv) {
    const int r = argc > 1 ? std::atoi(argv[1]) : 4;
    const std::uint64_t seed = argc > 2 ? std::strtoull(argv[2], nullptr, 10) : 1;
    const double gamma = argc > 3 ? std::atof(argv[3]) : 0.25;
    const int max_rounds = argc > 4 ? std::atoi(argv[4]) : 10000;
    const int b = 2 * r + 1;
    if (r < 2 || r > 4) {
        std::cerr << "This exact diagnostic supports 2 <= r <= 4.\n";
        return 2;
    }

    const int universe = 1 << b;
    std::vector<int> mid_index(universe, -1), low_index(universe, -1);
    std::vector<int> mid_masks, low_masks;
    for (int mask = 0; mask < universe; ++mask) {
        const int pc = __builtin_popcount(static_cast<unsigned>(mask));
        if (pc == r) {
            mid_index[mask] = static_cast<int>(mid_masks.size());
            mid_masks.push_back(mask);
        }
        if (pc == r - 1) {
            low_index[mask] = static_cast<int>(low_masks.size());
            low_masks.push_back(mask);
        }
    }

    std::vector<Edge> edges;
    std::vector<int> word(b);
    std::iota(word.begin(), word.end(), 0);
    do {
        Edge e;
        e.m.reserve(2 * r);
        e.l.reserve(2 * r);
        for (int s = 1; s < b; ++s) {
            int mm = 0, ll = 0;
            for (int j = 0; j < r; ++j) {
                const int bit = 1 << word[(s + j) % b];
                mm |= bit;
                if (j < r - 1) ll |= bit;
            }
            e.m.push_back(mid_index[mm]);
            e.l.push_back(low_index[ll]);
        }
        edges.push_back(std::move(e));
    } while (std::next_permutation(word.begin(), word.end()));

    std::vector<unsigned char> used_m(mid_masks.size(), 0), used_l(low_masks.size(), 0);
    std::vector<unsigned char> alive(edges.size(), 1);
    std::vector<int> deg_m(mid_masks.size()), deg_l(low_masks.size());
    std::mt19937_64 rng(seed);
    std::uniform_real_distribution<double> unif(0.0, 1.0);
    std::uint64_t accepted_total = 0;

    auto recompute = [&]() -> std::uint64_t {
        std::fill(deg_m.begin(), deg_m.end(), 0);
        std::fill(deg_l.begin(), deg_l.end(), 0);
        std::uint64_t z = 0;
        for (std::size_t ei = 0; ei < edges.size(); ++ei) {
            if (!alive[ei]) continue;
            const Edge& e = edges[ei];
            bool ok = true;
            for (int v : e.m) if (used_m[v]) { ok = false; break; }
            if (ok) for (int v : e.l) if (used_l[v]) { ok = false; break; }
            if (!ok) {
                alive[ei] = 0;
                continue;
            }
            ++z;
            for (int v : e.m) ++deg_m[v];
            for (int v : e.l) ++deg_l[v];
        }
        return z;
    };

    auto stats = [](const std::vector<int>& d, const std::vector<unsigned char>& used) {
        long double sum = 0.0L, sum2 = 0.0L;
        int mx = 0, mn = -1, count = 0, zero = 0;
        for (std::size_t i = 0; i < d.size(); ++i) {
            if (used[i]) continue;
            ++count;
            sum += d[i];
            sum2 += static_cast<long double>(d[i]) * d[i];
            mx = std::max(mx, d[i]);
            if (mn < 0 || d[i] < mn) mn = d[i];
            if (d[i] == 0) ++zero;
        }
        const long double avg = count ? sum / count : 0.0L;
        const long double var = count ? sum2 / count - avg * avg : 0.0L;
        return std::vector<long double>{static_cast<long double>(count), avg,
                                        static_cast<long double>(mx),
                                        static_cast<long double>(mn),
                                        static_cast<long double>(zero),
                                        avg > 0 ? mx / avg : 0.0L,
                                        avg > 0 ? std::sqrt(std::max(0.0L, var)) / avg : 0.0L};
    };

    for (int round = 0; round <= max_rounds; ++round) {
        const std::uint64_t z = recompute();
        const auto sm = stats(deg_m, used_m);
        const auto sl = stats(deg_l, used_l);
        if (round < 20 || round % 10 == 0 || z == 0) {
            std::cout << std::setprecision(8)
                      << "round=" << round << " Z=" << z
                      << " accepted=" << accepted_total
                      << " Mleft=" << static_cast<std::uint64_t>(sm[0])
                      << " Mavg=" << static_cast<double>(sm[1])
                      << " Mmax=" << static_cast<std::uint64_t>(sm[2])
                      << " Mratio=" << static_cast<double>(sm[5])
                      << " Mcv=" << static_cast<double>(sm[6])
                      << " Mzero=" << static_cast<std::uint64_t>(sm[4])
                      << " Lleft=" << static_cast<std::uint64_t>(sl[0])
                      << " Lavg=" << static_cast<double>(sl[1])
                      << " Lmax=" << static_cast<std::uint64_t>(sl[2])
                      << " Lratio=" << static_cast<double>(sl[5])
                      << " Lcv=" << static_cast<double>(sl[6])
                      << " Lzero=" << static_cast<std::uint64_t>(sl[4]) << '\n';
        }
        if (z == 0 || sm[0] == 0 || sl[0] == 0) break;

        const long double dbar_m = sm[1];
        const double p = gamma / (r * static_cast<double>(dbar_m));
        std::vector<int> marked;
        for (std::size_t ei = 0; ei < edges.size(); ++ei) {
            if (alive[ei] && unif(rng) < p) marked.push_back(static_cast<int>(ei));
        }
        if (marked.empty()) continue;

        std::vector<unsigned char> collision(marked.size(), 0);
        for (std::size_t i = 0; i < marked.size(); ++i) {
            const Edge& a = edges[marked[i]];
            for (std::size_t j = i + 1; j < marked.size(); ++j) {
                const Edge& c = edges[marked[j]];
                bool hit = false;
                for (int x : a.m) {
                    if (std::find(c.m.begin(), c.m.end(), x) != c.m.end()) {
                        hit = true; break;
                    }
                }
                if (!hit) for (int x : a.l) {
                    if (std::find(c.l.begin(), c.l.end(), x) != c.l.end()) {
                        hit = true; break;
                    }
                }
                if (hit) collision[i] = collision[j] = 1;
            }
        }
        int accepted_round = 0;
        for (std::size_t i = 0; i < marked.size(); ++i) {
            if (collision[i]) continue;
            const Edge& e = edges[marked[i]];
            bool ok = true;
            for (int v : e.m) if (used_m[v]) { ok = false; break; }
            if (ok) for (int v : e.l) if (used_l[v]) { ok = false; break; }
            if (!ok) continue;
            for (int v : e.m) used_m[v] = 1;
            for (int v : e.l) used_l[v] = 1;
            ++accepted_round;
        }
        accepted_total += accepted_round;
    }
    return 0;
}
