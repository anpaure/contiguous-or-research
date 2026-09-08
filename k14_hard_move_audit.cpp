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
#include <vector>
using namespace std;

static bool adjacent(int a, int b) {
    return popcount(static_cast<unsigned>(a ^ b)) == 2;
}

struct Eval { int deficit = 0, rank5 = 0, upper8 = 0; };

static Eval evaluate(const vector<int>& path) {
    Eval result;
    for (int bit = 0; bit < 14; ++bit) {
        int i = 0;
        while (i < static_cast<int>(path.size())) {
            if (!(path[i] & (1 << bit))) { ++i; continue; }
            const int first = i;
            while (i < static_cast<int>(path.size()) && (path[i] & (1 << bit))) ++i;
            if (first && i < static_cast<int>(path.size()) && i - first < 3)
                result.deficit += 3 - (i - first);
        }
    }
    vector<uint8_t> seen5(1 << 14), seen8(1 << 14);
    for (int i = 0; i + 1 < static_cast<int>(path.size()); ++i)
        seen8[path[i] | path[i + 1]] = 1;
    for (int i = 0; i + 2 < static_cast<int>(path.size()); ++i)
        seen5[path[i] & path[i + 1] & path[i + 2]] = 1;
    for (int x = 0; x < (1 << 14); ++x) {
        if (popcount(static_cast<unsigned>(x)) == 5) result.rank5 += seen5[x];
        if (popcount(static_cast<unsigned>(x)) == 8) result.upper8 += seen8[x];
    }
    return result;
}

static bool better(const Eval& a, const Eval& b) {
    if (a.deficit != b.deficit) return a.deficit < b.deficit;
    if (a.rank5 != b.rank5) return a.rank5 > b.rank5;
    return a.upper8 > b.upper8;
}

int main() {
    vector<int> path;
    for (int x; cin >> x;) path.push_back(x);
    if (path.size() != 3432) return 2;
    vector<int> colors(1 << 14);
    for (int i = 0; i + 1 < static_cast<int>(path.size()); ++i) {
        if (!adjacent(path[i], path[i + 1])) return 3;
        ++colors[path[i] & path[i + 1]];
    }
    int distinct = 0;
    for (int x = 0; x < (1 << 14); ++x)
        distinct += popcount(static_cast<unsigned>(x)) == 6 && colors[x];
    if (distinct != 3003) return 4;

    const Eval original = evaluate(path);
    Eval best = original;
    vector<int> best_path = path;
    long long valid = 0, hard_valid = 0;
    int best_left = -1, best_right = -1;
    const int n = path.size();
    for (int left = 0; left < n; ++left) for (int right = left + 2; right < n; ++right) {
        if (left && !adjacent(path[left - 1], path[right])) continue;
        if (right + 1 < n && !adjacent(path[left], path[right + 1])) continue;
        ++valid;
        vector<int> changed;
        auto remove_color = [&](int a, int b) {
            const int c = a & b;
            --colors[c]; changed.push_back(c);
        };
        auto add_color = [&](int a, int b) {
            const int c = a & b;
            ++colors[c]; changed.push_back(c);
        };
        if (left) remove_color(path[left - 1], path[left]);
        if (right + 1 < n) remove_color(path[right], path[right + 1]);
        if (left) add_color(path[left - 1], path[right]);
        if (right + 1 < n) add_color(path[left], path[right + 1]);
        bool hard = true;
        for (int c : changed) hard &= colors[c] > 0;
        if (hard) {
            ++hard_valid;
            reverse(path.begin() + left, path.begin() + right + 1);
            const Eval current = evaluate(path);
            if (better(current, best)) {
                best = current;
                best_path = path;
                best_left = left;
                best_right = right;
            }
            reverse(path.begin() + left, path.begin() + right + 1);
        }
        if (right + 1 < n) remove_color(path[left], path[right + 1]);
        if (left) remove_color(path[left - 1], path[right]);
        if (right + 1 < n) add_color(path[right], path[right + 1]);
        if (left) add_color(path[left - 1], path[left]);
    }
    cerr << "original=" << original.deficit << ',' << original.rank5 << ',' << original.upper8
         << " best=" << best.deficit << ',' << best.rank5 << ',' << best.upper8
         << " move=[" << best_left << ',' << best_right << "]"
         << " valid=" << valid << " hard_valid=" << hard_valid << '\n';
    for (int x : best_path) cout << x << ' ';
    cout << '\n';
}
