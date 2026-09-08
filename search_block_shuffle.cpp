#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <algorithm>
#include <bit>
#include <cstdint>
#include <iostream>
#include <random>
#include <vector>

using namespace std;

static int violations(const vector<int>& q, int k) {
    int result = 0;
    for (int bit = 0; bit < k; ++bit) {
        int start = 0;
        while (start < static_cast<int>(q.size())) {
            if (!(q[start] & (1 << bit))) { ++start; continue; }
            int end = start + 1;
            while (end < static_cast<int>(q.size()) && (q[end] & (1 << bit))) ++end;
            if (start && end < static_cast<int>(q.size()) && end - start < 3)
                result += 3 - (end - start);
            start = end;
        }
    }
    return result;
}

static int high_coverage(const vector<int>& q, int k, int rank) {
    vector<unsigned char> seen(1 << k);
    int count = 0;
    for (int left = 0; left < static_cast<int>(q.size()); ++left) {
        int value = 0;
        for (int right = left; right < static_cast<int>(q.size()); ++right) {
            value |= q[right];
            if (popcount(static_cast<unsigned>(value)) >= rank && !seen[value])
                seen[value] = 1, ++count;
            if (value == (1 << k) - 1) break;
        }
    }
    return count;
}

static vector<int> composition(int total, int parts, mt19937_64& rng) {
    vector<int> result(parts, 3);
    for (int remaining = total - 3 * parts; remaining > 0; --remaining)
        ++result[rng() % parts];
    shuffle(result.begin(), result.end(), rng);
    return result;
}

int main(int argc, char** argv) {
    const int k = argc > 1 ? stoi(argv[1]) : 10;
    const uint64_t iterations = argc > 2 ? stoull(argv[2]) : 10000000ULL;
    const uint64_t seed = argc > 3 ? stoull(argv[3]) : 1;
    vector<int> input;
    for (int value; cin >> value;) input.push_back(value);
    if (input.size() % 2) return 2;
    const int side = input.size() / 2;
    vector<int> x(input.begin(), input.begin() + side);
    vector<int> y(input.begin() + side, input.end());
    int wanted = 0;
    const int rank = (k + 1) / 2;
    for (int mask = 1; mask < (1 << k); ++mask)
        wanted += popcount(static_cast<unsigned>(mask)) >= rank;
    mt19937_64 rng(seed);
    int best_bad = 1000000, best_high = 0;
    for (uint64_t iteration = 0; iteration < iterations; ++iteration) {
        const int parts = 1 + rng() % (side / 3);
        vector<int> cx = composition(side, parts, rng);
        vector<int> cy = composition(side, parts, rng);
        const bool x_first = rng() & 1;
        const bool reverse_x = rng() & 1;
        const bool reverse_y = rng() & 1;
        if (reverse_x) reverse(x.begin(), x.end());
        if (reverse_y) reverse(y.begin(), y.end());
        vector<int> q;
        q.reserve(input.size());
        int px = 0, py = 0;
        for (int part = 0; part < parts; ++part) {
            auto append_x = [&] {
                q.insert(q.end(), x.begin() + px, x.begin() + px + cx[part]);
                px += cx[part];
            };
            auto append_y = [&] {
                q.insert(q.end(), y.begin() + py, y.begin() + py + cy[part]);
                py += cy[part];
            };
            if (x_first) append_x(), append_y();
            else append_y(), append_x();
        }
        if (reverse_x) reverse(x.begin(), x.end());
        if (reverse_y) reverse(y.begin(), y.end());
        const int bad = violations(q, k);
        if (bad < best_bad) {
            best_bad = bad;
            cerr << "violations=" << bad << " parts=" << parts
                 << " at=" << iteration << '\n';
        }
        if (bad) continue;
        const int high = high_coverage(q, k, rank);
        if (high > best_high) {
            best_high = high;
            cerr << "rootable high=" << high << '/' << wanted
                 << " parts=" << parts << " at=" << iteration << '\n';
        }
        if (high == wanted) {
            for (int value : q) cout << value << ' ';
            cout << '\n';
            return 0;
        }
    }
    return 1;
}
