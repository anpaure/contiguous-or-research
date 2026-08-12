#include <algorithm>
#include <bit>
#include <cstdint>
#include <iostream>
#include <map>
#include <set>
#include <tuple>
#include <vector>

using Mask = std::uint32_t;

struct ChainData {
    std::vector<int> bottom;
    std::vector<int> stars;
    std::vector<int> top_zeros;
    int radius = 0;
};

static ChainData gk_chain(Mask x, int k) {
    std::vector<int> zero_stack;
    std::vector<char> paired(k, false);
    for (int i = 0; i < k; ++i) {
        if (((x >> i) & 1U) == 0) {
            zero_stack.push_back(i);
        } else if (!zero_stack.empty()) {
            const int j = zero_stack.back();
            zero_stack.pop_back();
            paired[i] = paired[j] = true;
        }
    }

    ChainData c;
    for (int i = 0; i < k; ++i) {
        if (!paired[i]) c.stars.push_back(i);
        else if ((x >> i) & 1U) c.bottom.push_back(i);
        else c.top_zeros.push_back(i);
    }
    c.radius = static_cast<int>(c.stars.size()) / 2;
    return c;
}

static std::vector<std::vector<int>> permutations(std::vector<int> a) {
    std::sort(a.begin(), a.end());
    std::vector<std::vector<int>> out;
    do out.push_back(a); while (std::next_permutation(a.begin(), a.end()));
    return out;
}

static std::vector<std::vector<int>> fiber(Mask x, int k) {
    const ChainData c = gk_chain(x, k);
    const auto ps = permutations(c.bottom);
    const auto qs = permutations(c.top_zeros);
    std::vector<std::vector<int>> out;
    for (const auto& p : ps) for (const auto& q : qs) {
        std::vector<int> pi;
        pi.insert(pi.end(), p.begin(), p.end());
        pi.insert(pi.end(), c.stars.begin(), c.stars.end());
        pi.insert(pi.end(), q.begin(), q.end());
        out.push_back(std::move(pi));
    }
    return out;
}

static std::vector<Mask> chain_sets(Mask x, int k) {
    const ChainData c = gk_chain(x, k);
    Mask cur = 0;
    for (int z : c.bottom) cur |= Mask{1} << z;
    std::vector<Mask> out{cur};
    for (int z : c.stars) {
        cur |= Mask{1} << z;
        out.push_back(cur);
    }
    return out;
}

static bool quotient_compatible(Mask x, Mask y, int k) {
    const ChainData d = gk_chain(y, k);
    Mask anchor = 0;
    for (int z : d.bottom) anchor |= Mask{1} << z;
    if (anchor == 0) anchor = Mask{1} << d.stars.front();
    const auto cx = chain_sets(x, k);
    const auto cy = chain_sets(y, k);
    for (Mask a : cx) for (Mask b : cy) {
        a &= ~anchor;
        b &= ~anchor;
        if ((a & ~b) != 0 && (b & ~a) != 0) return false;
    }
    return true;
}

static bool source_center_passes_fence(Mask x, Mask y, int k) {
    const ChainData d = gk_chain(y, k);
    Mask anchor = 0;
    for (int z : d.bottom) anchor |= Mask{1} << z;
    if (anchor == 0) anchor = Mask{1} << d.stars.front();
    Mask a = x & ~anchor;
    Mask cur = 0;
    if (a == 0) return true;
    for (int z : d.stars) {
        cur |= Mask{1} << z;
        if (a == cur) return true;
    }
    return (cur & ~a) == 0;
}

static Mask prefix_mask(const std::vector<int>& pi, int m) {
    Mask x = 0;
    for (int i = 0; i < m; ++i) x |= Mask{1} << pi[i];
    return x;
}

static bool in_fiber(const std::vector<int>& pi, Mask x, int k) {
    const ChainData c = gk_chain(x, k);
    const int b = static_cast<int>(c.bottom.size());
    const int s = static_cast<int>(c.stars.size());
    std::set<int> got_bottom(pi.begin(), pi.begin() + b);
    std::set<int> want_bottom(c.bottom.begin(), c.bottom.end());
    if (got_bottom != want_bottom) return false;
    for (int i = 0; i < s; ++i) if (pi[b + i] != c.stars[i]) return false;
    std::set<int> got_top(pi.begin() + b + s, pi.end());
    std::set<int> want_top(c.top_zeros.begin(), c.top_zeros.end());
    return got_top == want_top;
}

static std::vector<Mask> coollex(int m) {
    const int k = 2 * m;
    std::vector<int> w(k, 0);
    for (int i = 0; i < m; ++i) w[i] = 1;
    std::vector<Mask> out;
    const std::uint64_t total = [&] {
        std::uint64_t z = 1;
        for (int i = 1; i <= m; ++i) z = z * (m + i) / i;
        return z;
    }();
    for (std::uint64_t step = 0; step < total; ++step) {
        Mask x = 0;
        for (int i = 0; i < k; ++i) if (w[i]) x |= Mask{1} << i;
        out.push_back(x);
        int len = k;
        for (int i = 2; i < k; ++i) {
            if (w[i-2] == 0 && w[i-1] == 1 && (w[i] == 0 || w[i] == 1)) {
                len = i + 1;
                break;
            }
        }
        const int last = w[len - 1];
        for (int i = len - 1; i > 0; --i) w[i] = w[i - 1];
        w[0] = last;
    }
    return out;
}

int main(int argc, char** argv) {
    const int m_max = argc > 1 ? std::stoi(argv[1]) : 5;
    for (int m = 1; m <= m_max; ++m) {
        const int k = 2 * m;
        std::map<std::pair<int,int>, std::uint64_t> transitions;
        std::map<std::pair<int,int>, std::tuple<Mask,Mask,std::vector<int>,std::vector<int>>> examples;
        std::map<std::pair<int,int>, std::uint64_t> center_arcs;
        std::vector<std::set<Mask>> out_by_radius(m + 1);
        std::uint64_t state_arcs = 0;

        for (Mask x = 0; x < (Mask{1} << k); ++x) {
            if (std::popcount(x) != m) continue;
            const int dx = gk_chain(x, k).radius;
            for (const auto& pi : fiber(x, k)) {
                for (int pos = m; pos < k; ++pos) {
                    const int incoming = pi[pos];
                    std::vector<int> sigma;
                    sigma.push_back(incoming);
                    for (int y : pi) if (y != incoming) sigma.push_back(y);
                    const Mask y = prefix_mask(sigma, m);
                    if (y == x || !in_fiber(sigma, y, k)) continue;
                    const int dy = gk_chain(y, k).radius;
                    ++state_arcs;
                    ++transitions[{dx,dy}];
                    examples.try_emplace({dx,dy}, x, y, pi, sigma);
                    center_arcs[{static_cast<int>(x),static_cast<int>(y)}] = 1;
                    out_by_radius[dx].insert(x);
                }
            }
        }

        std::cout << "m=" << m << " center_arcs=" << center_arcs.size()
                  << " state_arcs=" << state_arcs << '\n';
        std::cout << " radius transitions:";
        for (const auto& [p,c] : transitions) {
            std::cout << ' ' << p.first << "->" << p.second << ':' << c;
        }
        std::cout << '\n';
        if (m == 3) {
            for (const auto& [r, ex] : examples) {
                const auto& [x,y,pi,sigma] = ex;
                std::cout << "  ex " << r.first << "->" << r.second
                          << " x=" << x << " y=" << y << " pi=";
                for (int z : pi) std::cout << z + 1;
                std::cout << " sigma=";
                for (int z : sigma) std::cout << z + 1;
                std::cout << '\n';
            }
        }
        std::cout << " sources by radius:";
        for (int d = 0; d <= m; ++d) std::cout << ' ' << d << ':' << out_by_radius[d].size();
        std::cout << '\n';
        const auto cl = coollex(m);
        std::set<Mask> distinct(cl.begin(), cl.end());
        std::uint64_t compatible = 0, radius_pm_one = 0, johnson = 0;
        std::uint64_t quotient_ok = 0;
        std::uint64_t center_fence_ok = 0;
        std::map<std::pair<int,int>, std::uint64_t> quotient_radii;
        std::uint64_t radius_up = 0, radius_down = 0;
        std::uint64_t max_run = 1, run = 1;
        for (std::size_t i = 0; i < cl.size(); ++i) {
            const Mask x = cl[i], y = cl[(i + 1) % cl.size()];
            const int dx = gk_chain(x, k).radius;
            const int dy = gk_chain(y, k).radius;
            if (std::popcount(x ^ y) == 2) ++johnson;
            if (std::abs(dx - dy) == 1) {
                ++radius_pm_one;
                if (dy > dx) ++radius_up; else ++radius_down;
            }
            const bool good = center_arcs.contains({static_cast<int>(x),static_cast<int>(y)});
            if (quotient_compatible(x, y, k)) {
                ++quotient_ok;
                ++quotient_radii[{dx,dy}];
            }
            if (source_center_passes_fence(x, y, k)) ++center_fence_ok;
            if (good) {
                ++compatible;
                ++run;
                max_run = std::max(max_run, run);
            } else {
                run = 1;
            }
        }
        std::cout << " coollex distinct=" << distinct.size() << '/' << cl.size()
                  << " johnson=" << johnson
                  << " radius_pm1=" << radius_pm_one
                  << "(up=" << radius_up << ",down=" << radius_down << ')'
                  << " compatible=" << compatible
                  << " quotient_ok=" << quotient_ok
                  << " center_fence_ok=" << center_fence_ok
                  << " max_run_states=" << max_run << '\n';
        if (m == 3) {
            std::cout << "  coollex radii:";
            for (Mask x : cl) std::cout << ' ' << gk_chain(x, k).radius;
            std::cout << '\n';
        }
        std::cout << "  coollex quotient radii:";
        for (const auto& [r,c] : quotient_radii) std::cout << ' ' << r.first << "->" << r.second << ':' << c;
        std::cout << '\n';
    }
}
