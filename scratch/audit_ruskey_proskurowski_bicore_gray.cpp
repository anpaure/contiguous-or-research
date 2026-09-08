#include <algorithm>
#include <bit>
#include <cassert>
#include <cstdint>
#include <functional>
#include <iostream>
#include <string>
#include <unordered_set>
#include <utility>
#include <vector>

// Audit the explicit Ruskey--Proskurowski transposition Gray order of Dyck
// words against the exact alternating MSW bi-core criterion.  This program is
// intended for remote execution on h100; it is deliberately self-contained.

using Word = std::uint64_t;

static std::pair<Word, int> g(Word x, int m) {
    std::vector<int> before(2 * m);
    int height = 0, down_zero = 0;
    for (int i = 0; i < 2 * m; ++i) {
        before[i] = height;
        if (((x >> i) & 1ULL) == 0 && height == 0) ++down_zero;
        height += ((x >> i) & 1ULL) ? 1 : -1;
    }
    int seen = 0;
    for (int i = 0; i < 2 * m; ++i) {
        if (((x >> i) & 1ULL) == 0 &&
            (before[i] == 0 || before[i] == 1) && ++seen == down_zero + 1)
            return {x | (1ULL << i), i};
    }
    assert(false);
    return {};
}

static std::pair<Word, int> hmap(Word y, int m) {
    std::vector<int> before(2 * m);
    int height = 0, up_one = 0;
    for (int i = 0; i < 2 * m; ++i) {
        before[i] = height;
        if (((y >> i) & 1ULL) != 0 && height == 1) ++up_one;
        height += ((y >> i) & 1ULL) ? 1 : -1;
    }
    int seen = 0;
    for (int i = 0; i < 2 * m; ++i) {
        if (((y >> i) & 1ULL) != 0 &&
            (before[i] == 0 || before[i] == 1) && ++seen == up_one)
            return {y & ~(1ULL << i), i};
    }
    assert(false);
    return {};
}

static long long choose(int n, int r) {
    if (r < 0 || r > n) return 0;
    long long ans = 1;
    for (int i = 1; i <= r; ++i) ans = ans * (n - r + i) / i;
    return ans;
}

static long long catalan(int r) { return choose(2 * r, r) / (r + 1); }

static bool is_dyck(Word x, int m) {
    int height = 0;
    for (int i = 0; i < 2 * m; ++i) {
        height += ((x >> i) & 1ULL) ? 1 : -1;
        if (height < 0) return false;
    }
    return height == 0;
}

// Algorithm 1 in Ruskey--Proskurowski, called on T(m+1,1) and with the
// initial 10 prefix discarded.  Indices are zero-based here, so the paper's
// initial pos=3 becomes pos=2.
static std::vector<Word> rp_order(int m) {
    const int ambient_n = m + 1;
    const int length = 2 * ambient_n;
    assert(length < 64);
    std::vector<unsigned char> bits(length);
    bits[0] = 1;
    bits[1] = 0;
    std::vector<Word> output;
    output.reserve(static_cast<std::size_t>(catalan(m)));

    std::function<void(int, int, int, bool)> rec =
        [&](int n, int k, int pos, bool dir) {
            if (k == 0 || k == n) {
                Word word = 0;
                for (int i = 2; i < length; ++i)
                    if (bits[i]) word |= 1ULL << (i - 2);
                output.push_back(word);
                return;
            }
            if (k == 1) {
                bits[pos] = 1;
                rec(n, k + 1, pos + 1, dir);
                bits[pos] = 0;
                return;
            }
            if (dir) {
                bits[pos] = 1;
                rec(n, k + 1, pos + 1, false);
                bits[pos] = 0;
                rec(n - 1, k - 1, pos + 1, true);
            } else {
                rec(n - 1, k - 1, pos + 1, false);
                bits[pos] = 1;
                rec(n, k + 1, pos + 1, true);
                bits[pos] = 0;
            }
        };
    rec(ambient_n, 1, 2, true);
    return output;
}

struct Ranks {
    std::vector<int> insertion;
    std::vector<int> deletion;
};

static Ranks msw_ranks(Word root, int m) {
    Ranks ranks{std::vector<int>(2 * m, -1), std::vector<int>(2 * m, -1)};
    Word current = root;
    for (int j = 0; j < m; ++j) {
        auto inserted = g(current, m);
        ranks.insertion[inserted.second] = j + 1;
        auto deleted = hmap(inserted.first, m);
        ranks.deletion[deleted.second] = j + 1;
        current = deleted.first;
    }
    return ranks;
}

int main(int argc, char** argv) {
    const int min_m = argc > 2 ? std::stoi(argv[1]) : 2;
    const int max_m = argc > 2 ? std::stoi(argv[2])
                               : (argc > 1 ? std::stoi(argv[1]) : 13);
    for (int m = min_m; m <= max_m; ++m) {
        auto order = rp_order(m);
        assert(static_cast<long long>(order.size()) == catalan(m));
        std::unordered_set<Word> unique(order.begin(), order.end());
        assert(unique.size() == order.size());
        for (Word x : order) assert(is_dyck(x, m));

        const int k = 2 * m + 1;
        const int R = m + 1;
        const long long W = choose(k, R);
        const long long lower_half = 1LL << (k - 1);
        int d = 0;
        while (1LL * d * W + 1LL * d * (d + 1) / 2 < lower_half) ++d;
        const int h = d;

        std::vector<Ranks> ranks;
        ranks.reserve(order.size());
        for (Word x : order) ranks.push_back(msw_ranks(x, m));

        long long plus = 0, minus = 0, both = 0, neither = 0;
        long long parity_fail[2] = {0, 0};
        long long first_fail[2] = {-1, -1};
        for (std::size_t i = 1; i < order.size(); ++i) {
            const Word old_word = order[i - 1], new_word = order[i];
            const Word removed = old_word & ~new_word;
            const Word inserted = new_word & ~old_word;
            assert(std::popcount(removed) == 1 && std::popcount(inserted) == 1);
            const int q = std::countr_zero(removed);
            const int p = std::countr_zero(inserted);
            const bool plus_safe = ranks[i - 1].deletion[q] > h &&
                                   ranks[i].deletion[p] > h;
            const bool minus_safe = ranks[i - 1].insertion[p] <= m - h &&
                                    ranks[i].insertion[q] <= m - h;
            plus += plus_safe;
            minus += minus_safe;
            both += plus_safe && minus_safe;
            neither += !plus_safe && !minus_safe;
            for (int initial = 0; initial < 2; ++initial) {
                // State 0 means plus.  The sign of target order[i] alternates.
                const bool target_plus = ((static_cast<int>(i) + initial) & 1) == 0;
                const bool safe = target_plus ? plus_safe : minus_safe;
                if (!safe) {
                    ++parity_fail[initial];
                    if (first_fail[initial] < 0) first_fail[initial] = i;
                }
            }
        }
        std::cout << "m=" << m << " C=" << order.size() << " h=" << h
                  << " q=" << h + 1 << " plus=" << plus << " minus=" << minus
                  << " both=" << both << " neither=" << neither
                  << " parity0_fail=" << parity_fail[0]
                  << " first0=" << first_fail[0]
                  << " parity1_fail=" << parity_fail[1]
                  << " first1=" << first_fail[1] << '\n';
    }
}
