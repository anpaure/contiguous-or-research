#include <algorithm>
#include <array>
#include <bit>
#include <iostream>
#include <numeric>
#include <random>
#include <vector>

using namespace std;

static int score(int k, const vector<int>& a) {
    vector<char> seen(1 << k);
    vector<int> previous;
    int result = 0;
    for (int value : a) {
        vector<int> current{value};
        for (int x : previous) {
            x |= value;
            if (x != current.back()) current.push_back(x);
        }
        for (int x : current) if (!seen[x]) seen[x] = 1, ++result;
        previous.swap(current);
    }
    return result;
}

static vector<int> translate(int k, const vector<int>& lower, int first_upper,
                             vector<int> startup_order) {
    const int m = (k - 1) / 2;
    const int first_lower = lower[0];
    const int initial_extra = first_upper ^ first_lower;
    vector<int> a{initial_extra};
    for (int x : startup_order) a.push_back(x);

    // Recency blocks after the singleton startup.
    vector<int> blocks;
    for (auto it = startup_order.rbegin(); it != startup_order.rend(); ++it)
        blocks.push_back(*it);
    blocks.push_back(initial_extra);

    for (int i = 1; i < static_cast<int>(lower.size()); ++i) {
        const int old_lower = lower[i - 1];
        const int new_lower = lower[i];
        const int upper = old_lower | new_lower;
        const int removed = old_lower & ~new_lower;
        const int added = new_lower & ~old_lower;
        int request = added;
        bool at_removed = false;
        for (int block : blocks) {
            if (block & removed) at_removed = true;
            if (at_removed) request |= block & new_lower;
        }
        a.push_back(request);
        vector<int> next{request};
        for (int block : blocks) if ((block &= ~request)) next.push_back(block);
        blocks.swap(next);

        // Sanity-check that the requested middle edge is present.
        int prefix = 0;
        bool got_lower = false, got_upper = false;
        for (int block : blocks) {
            prefix |= block;
            got_lower |= prefix == new_lower;
            got_upper |= prefix == upper;
        }
        if (!got_lower || !got_upper) return {};
    }
    return a;
}

static bool dfs(int k, const vector<int>& lower_masks, const vector<int>& upper_masks,
                const array<int, 128>& lower_id, const array<int, 128>& upper_id,
                vector<int>& path, uint64_t used_lower, uint64_t used_upper,
                mt19937_64& rng) {
    if (path.size() == lower_masks.size()) return true;
    struct Choice { int degree, mask, upper; };
    vector<Choice> choices;
    const int current = path.back();
    for (int next : lower_masks) {
        const int id = lower_id[next];
        if (used_lower >> id & 1) continue;
        if (popcount(static_cast<unsigned>(current ^ next)) != 2) continue;
        const int upper = current | next;
        const int uid = upper_id[upper];
        if (used_upper >> uid & 1) continue;
        int degree = 0;
        for (int future : lower_masks) {
            const int fid = lower_id[future];
            if (used_lower >> fid & 1 || future == next) continue;
            if (popcount(static_cast<unsigned>(next ^ future)) == 2 &&
                !(used_upper >> upper_id[next | future] & 1)) ++degree;
        }
        choices.push_back({degree, next, upper});
    }
    shuffle(choices.begin(), choices.end(), rng);
    stable_sort(choices.begin(), choices.end(), [](auto a, auto b) {
        return a.degree < b.degree;
    });
    for (auto choice : choices) {
        path.push_back(choice.mask);
        if (dfs(k, lower_masks, upper_masks, lower_id, upper_id, path,
                used_lower | (1ULL << lower_id[choice.mask]),
                used_upper | (1ULL << upper_id[choice.upper]), rng)) return true;
        path.pop_back();
    }
    return false;
}

int main(int argc, char** argv) {
    const int k = argc > 1 ? stoi(argv[1]) : 5;
    const int trials = argc > 2 ? stoi(argv[2]) : 100;
    const int m = (k - 1) / 2;
    vector<int> lower, upper;
    array<int, 128> lower_id, upper_id;
    lower_id.fill(-1); upper_id.fill(-1);
    for (int x = 0; x < (1 << k); ++x) {
        int w = popcount(static_cast<unsigned>(x));
        if (w == m) lower_id[x] = lower.size(), lower.push_back(x);
        if (w == m + 1) upper_id[x] = upper.size(), upper.push_back(x);
    }
    mt19937_64 rng(1234567);
    int global_best = 0;
    if (k == 5) {
        vector<int> known_lower{6, 12, 24, 17, 3, 10, 18, 20, 5, 9};
        vector<int> known_startup{2, 4};
        auto known = translate(k, known_lower, 7, known_startup);
        cerr << "known score=" << score(k, known) << ':';
        for (int x : known) cerr << ' ' << x;
        cerr << '\n';
        vector<int> canonical{3, 10, 12, 9, 17, 5, 6, 20, 24, 18};
        int canonical_best = 0;
        for (int direction = 0; direction < 2; ++direction) {
            for (int shift = 0; shift < static_cast<int>(canonical.size()); ++shift) {
                rotate(canonical.begin(), canonical.begin() + 1, canonical.end());
                const int q = canonical.back() | canonical.front();
                vector<int> startup;
                for (int x = canonical.front(); x; x &= x - 1) startup.push_back(x & -x);
                do {
                    auto a = translate(k, canonical, q, startup);
                    int s = score(k, a);
                    if (s > canonical_best) {
                        canonical_best = s;
                        cerr << "canonical score=" << s << ':';
                        for (int x : a) cerr << ' ' << x;
                        cerr << '\n';
                    }
                } while (next_permutation(startup.begin(), startup.end()));
            }
            reverse(canonical.begin(), canonical.end());
        }
    }
    for (int trial = 0; trial < trials; ++trial) {
        const int first_lower = lower[rng() % lower.size()];
        vector<int> possible_first_upper;
        for (int q : upper) if ((q & first_lower) == first_lower)
            possible_first_upper.push_back(q);
        const int first_upper = possible_first_upper[rng() % possible_first_upper.size()];
        vector<int> path{first_lower};
        if (!dfs(k, lower, upper, lower_id, upper_id, path,
                 1ULL << lower_id[first_lower], 1ULL << upper_id[first_upper], rng)) continue;
        vector<int> singles;
        for (int x = first_lower; x; x &= x - 1) singles.push_back(x & -x);
        do {
            auto a = translate(k, path, first_upper, singles);
            int s = score(k, a);
            if (s > global_best) {
                global_best = s;
                cout << "score=" << s << " length=" << a.size() << ':';
                for (int x : a) cout << ' ' << x;
                cout << '\n';
                if (s == (1 << k) - 1) return 0;
            }
        } while (next_permutation(singles.begin(), singles.end()));
    }
}
