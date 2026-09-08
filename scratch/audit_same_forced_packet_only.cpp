#include <algorithm>
#include <cassert>
#include <cstdint>
#include <functional>
#include <iostream>
#include <string>
#include <utility>
#include <vector>

// Fast exact audit of the four local area-increasing packets
//   01->10, 001->100, 011->110, 0011->1010
// in the native tight-MSW same-forced graph.  Unlike the full graph audit,
// this computes only the O(m) candidate moves at each Dyck root.

using U = std::uint64_t;

static std::pair<U, int> g(U x, int m) {
    std::vector<int> before(2 * m);
    int height = 0, d0 = 0;
    for (int i = 0; i < 2 * m; ++i) {
        before[i] = height;
        if (((x >> i) & 1U) == 0 && height == 0) ++d0;
        height += ((x >> i) & 1U) ? 1 : -1;
    }
    int seen = 0;
    for (int i = 0; i < 2 * m; ++i)
        if (((x >> i) & 1U) == 0 &&
            (before[i] == 0 || before[i] == 1) && ++seen == d0 + 1)
            return {x | (U{1} << i), i};
    assert(false);
    return {};
}

static std::pair<U, int> hmap(U y, int m) {
    std::vector<int> before(2 * m);
    int height = 0, u1 = 0;
    for (int i = 0; i < 2 * m; ++i) {
        before[i] = height;
        if (((y >> i) & 1U) != 0 && height == 1) ++u1;
        height += ((y >> i) & 1U) ? 1 : -1;
    }
    int seen = 0;
    for (int i = 0; i < 2 * m; ++i)
        if (((y >> i) & 1U) != 0 &&
            (before[i] == 0 || before[i] == 1) && ++seen == u1)
            return {y & ~(U{1} << i), i};
    assert(false);
    return {};
}

static long long choose(int n, int r) {
    if (r < 0 || r > n) return 0;
    long long ans = 1;
    for (int i = 1; i <= r; ++i) ans = ans * (n - r + i) / i;
    return ans;
}

static std::vector<int> tight_order(U root, int m) {
    U x = root;
    const int n = 2 * m + 1;
    std::vector<int> rho;
    rho.reserve(n);
    for (int e = 0; e < m; ++e) {
        auto a = g(x, m);
        auto b = hmap(a.first, m);
        rho.push_back(a.second);
        rho.push_back(b.second);
        x = b.first;
    }
    rho.push_back(2 * m);
    std::vector<int> tight(n);
    for (int j = 0; j < n; ++j) tight[j] = rho[(2 * j) % n];
    return tight;
}

struct Signature {
    std::uint64_t word;
    int orientation;
    int start;
};

static std::vector<Signature> forced_signatures(const std::vector<int>& row,
                                                int d, int s) {
    const int n = static_cast<int>(row.size());
    assert(10 * d <= 64);
    std::vector<Signature> out;
    out.reserve(2 * n);
    for (int orientation = 0; orientation < 2; ++orientation) {
        for (int start = 0; start < n; ++start) {
            std::uint64_t signature = 0;
            for (int j = 0; j < d; ++j) {
                auto at = [&](int z) {
                    z %= n;
                    if (z < 0) z += n;
                    return orientation ? row[(n - 1 - z + n) % n] : row[z];
                };
                int a = at(start + j);
                int b = at(start + s - 1 + j);
                if (a > b) std::swap(a, b);
                std::uint64_t code = static_cast<std::uint64_t>(32 * a + b);
                signature |= code << (10 * j);
            }
            out.push_back({signature, orientation, start});
        }
    }
    std::sort(out.begin(), out.end(), [](const Signature& a, const Signature& b) {
        if (a.word != b.word) return a.word < b.word;
        if (a.orientation != b.orientation) return a.orientation < b.orientation;
        return a.start < b.start;
    });
    return out;
}

static bool common_signature(const std::vector<Signature>& a,
                             const std::vector<Signature>& b,
                             Signature* wa = nullptr,
                             Signature* wb = nullptr) {
    std::size_t i = 0, j = 0;
    while (i < a.size() && j < b.size()) {
        if (a[i].word < b[j].word) {
            ++i;
        } else if (b[j].word < a[i].word) {
            ++j;
        } else {
            if (wa) *wa = a[i];
            if (wb) *wb = b[j];
            return true;
        }
    }
    return false;
}

static bool common_signature_restricted(const std::vector<Signature>& a,
                                        const std::vector<Signature>& b,
                                        bool require_orientation_zero,
                                        bool require_same_start) {
    for (const auto& x : a) {
        if (require_orientation_zero && x.orientation != 0) continue;
        for (const auto& y : b) {
            if (y.word != x.word) continue;
            if (require_orientation_zero && y.orientation != 0) continue;
            if (require_same_start && y.start != x.start) continue;
            return true;
        }
    }
    return false;
}

static std::string root_word(U root, int m) {
    std::string out;
    out.reserve(2 * m);
    for (int i = 0; i < 2 * m; ++i) out.push_back((root >> i) & 1U ? '1' : '0');
    return out;
}

int main(int argc, char** argv) {
    const int m = argc > 1 ? std::stoi(argv[1]) : 13;
    const int n = 2 * m + 1, R = m + 1;
    assert(n < 63);
    const long long W = choose(n, R), half = 1LL << (n - 1);
    int d = 0;
    while (1LL * d * W + 1LL * d * (d + 1) / 2 < half) ++d;
    if (argc > 2) d = std::stoi(argv[2]);
    const int s = R - d;
    assert(10 * d <= 64);

    std::uint64_t roots = 0, nonmountain = 0, good = 0;
    std::uint64_t good_orientation_zero = 0, good_same_start = 0;
    std::uint64_t high_left_good = 0, high_right_good = 0;
    std::uint64_t high_left_same_start_good = 0,
                  high_right_same_start_good = 0;
    std::uint64_t high_left_orientation_zero_good = 0,
                  high_right_orientation_zero_good = 0;
    std::uint64_t pattern_count[4] = {0, 0, 0, 0};
    std::vector<std::string> exceptions;
    std::vector<std::string> nonadjacent_examples;

    const std::uint64_t maximum_roots = argc > 3 ? std::stoull(argv[3]) : 0;
    bool stop = false;
    std::function<void(int, int, int, U)> visit = [&](int pos, int up, int down,
                                                       U root) {
        if (stop) return;
        if (pos != 2 * m) {
            if (up < m) visit(pos + 1, up + 1, down, root | (U{1} << pos));
            if (down < up) visit(pos + 1, up, down + 1, root);
            return;
        }
        ++roots;
        const U mountain = (U{1} << m) - 1;
        if (root == mountain) return;
        ++nonmountain;
        auto source = forced_signatures(tight_order(root, m), d, s);

        struct Move { int p, q, type; };
        std::vector<Move> moves;
        std::vector<int> valley_height(2 * m, -1);
        int current_height = 0, maximum_valley_height = -1;
        for (int v = 0; v + 1 < 2 * m; ++v) {
            current_height += ((root >> v) & 1U) ? 1 : -1;
            if (((root >> v) & 3U) != 2U) continue;  // word[v:v+2] == 01
            valley_height[v] = current_height + 1;  // height before position v
            maximum_valley_height = std::max(maximum_valley_height, valley_height[v]);
            moves.push_back({v, v + 1, 0});
            const bool left = v > 0 && ((root >> (v - 1)) & 1U) == 0;
            const bool right = v + 2 < 2 * m && ((root >> (v + 2)) & 1U) != 0;
            if (left) moves.push_back({v - 1, v + 1, 1});
            if (right) moves.push_back({v, v + 2, 2});
            if (left && right) moves.push_back({v - 1, v + 2, 3});
        }
        std::stable_sort(moves.begin(), moves.end(), [](const Move& a, const Move& b) {
            if (a.q - a.p != b.q - b.p) return a.q - a.p < b.q - b.p;
            if (a.p != b.p) return a.p < b.p;
            return a.type < b.type;
        });

        bool found = false;
        bool found_orientation_zero = false, found_same_start = false;
        bool found_high_left = false, found_high_right = false;
        bool found_high_left_same_start = false,
             found_high_right_same_start = false;
        bool found_high_left_orientation_zero = false,
             found_high_right_orientation_zero = false;
        int high_left = -1, high_right = -1;
        for (int v = 0; v < 2 * m; ++v)
            if (valley_height[v] == maximum_valley_height) {
                if (high_left < 0) high_left = v;
                high_right = v;
            }
        for (const Move move : moves) {
            assert(((root >> move.p) & 1U) == 0);
            assert(((root >> move.q) & 1U) != 0);
            U mate = root ^ (U{1} << move.p) ^ (U{1} << move.q);
            auto target = forced_signatures(tight_order(mate, m), d, s);
            const bool this_same_start = common_signature_restricted(
                source, target, false, true);
            const bool this_orientation_zero = common_signature_restricted(
                source, target, true, false);
            found_orientation_zero |= common_signature_restricted(
                source, target, true, false);
            found_same_start |= common_signature_restricted(
                source, target, false, true);
            Signature a{}, b{};
            if (!common_signature(source, target, &a, &b)) continue;
            const int valley = move.type == 0 || move.type == 2 ? move.p : move.p + 1;
            found_high_left |= valley == high_left;
            found_high_right |= valley == high_right;
            found_high_left_same_start |= valley == high_left && this_same_start;
            found_high_right_same_start |= valley == high_right && this_same_start;
            found_high_left_orientation_zero |=
                valley == high_left && this_orientation_zero;
            found_high_right_orientation_zero |=
                valley == high_right && this_orientation_zero;
            if (found) continue;
            ++good;
            ++pattern_count[move.type];
            found = true;
            if (move.type != 0 && nonadjacent_examples.size() < 20) {
                nonadjacent_examples.push_back(
                    root_word(root, m) + ">" + root_word(mate, m) + "@" +
                    std::to_string(move.p) + ":" + std::to_string(move.q) +
                    " witness=" + std::to_string(a.orientation) + ":" +
                    std::to_string(a.start) + "," +
                    std::to_string(b.orientation) + ":" +
                    std::to_string(b.start));
            }
        }
        good_orientation_zero += found_orientation_zero;
        good_same_start += found_same_start;
        high_left_good += found_high_left;
        high_right_good += found_high_right;
        high_left_same_start_good += found_high_left_same_start;
        high_right_same_start_good += found_high_right_same_start;
        high_left_orientation_zero_good += found_high_left_orientation_zero;
        high_right_orientation_zero_good += found_high_right_orientation_zero;
        if (!found && exceptions.size() < 100) exceptions.push_back(root_word(root, m));
        if (roots % 100000 == 0) std::cerr << "visited=" << roots << '\n';
        if (maximum_roots && roots >= maximum_roots) stop = true;
    };
    visit(0, 0, 0, 0);

    std::cout << "m=" << m << " R=" << R << " d=" << d << " s=" << s
              << " roots=" << roots << " nonmountain=" << nonmountain
              << " packet_good=" << good << " packet_bad=" << nonmountain - good
              << " packet_good_orientation_zero=" << good_orientation_zero
              << " packet_good_same_start=" << good_same_start
              << " high_left_good=" << high_left_good
              << " high_right_good=" << high_right_good
              << " high_left_same_start_good=" << high_left_same_start_good
              << " high_right_same_start_good=" << high_right_same_start_good
              << " high_left_orientation_zero_good="
              << high_left_orientation_zero_good
              << " high_right_orientation_zero_good="
              << high_right_orientation_zero_good
              << " pattern_01=" << pattern_count[0]
              << " pattern_001=" << pattern_count[1]
              << " pattern_011=" << pattern_count[2]
              << " pattern_0011=" << pattern_count[3] << '\n';
    for (const auto& x : exceptions) std::cout << "exception " << x << '\n';
    for (const auto& x : nonadjacent_examples) std::cout << "nonadjacent " << x << '\n';
}
