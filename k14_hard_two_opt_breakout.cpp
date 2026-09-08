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
#include <tuple>
#include <vector>
using namespace std;

static bool adjacent(int a, int b) {
    return popcount(static_cast<unsigned>(a ^ b)) == 2;
}

struct Eval { int deficit = 0, critical = 0, rank5 = 0, upper8 = 0; };
struct Candidate { Eval eval; int left, right; vector<int> path; };

static Eval evaluate(const vector<int>& path) {
    Eval e;
    for (int bit = 0; bit < 14; ++bit) {
        int i = 0;
        while (i < static_cast<int>(path.size())) {
            if (!(path[i] & (1 << bit))) { ++i; continue; }
            const int first = i;
            while (i < static_cast<int>(path.size()) && (path[i] & (1 << bit))) ++i;
            if (first && i < static_cast<int>(path.size()) && i - first < 3)
                e.deficit += 3 - (i - first);
        }
    }
    vector<uint8_t> seen5(1 << 14), seen8(1 << 14);
    for (int i = 0; i + 1 < static_cast<int>(path.size()); ++i)
        seen8[path[i] | path[i + 1]] = 1;
    for (int i = 0; i + 2 < static_cast<int>(path.size()); ++i)
        seen5[path[i] & path[i + 1] & path[i + 2]] = 1;
    for (int x = 0; x < (1 << 14); ++x) {
        if (popcount(static_cast<unsigned>(x)) == 5) e.rank5 += seen5[x];
        if (popcount(static_cast<unsigned>(x)) == 8) e.upper8 += seen8[x];
    }
    // The current Hall witness is the rank-5 star centred at mask 440:
    // 440 and its nine rank-6 supersets have only nine eligible windows.
    // Giving 440 a singleton (triple-intersection) envelope breaks that
    // specific deficiency without weakening the hard rank-6 edge condition.
    e.critical = seen5[440];
    return e;
}

static bool better(const Eval& a, const Eval& b) {
    return tie(a.deficit, b.critical, b.rank5, b.upper8) <
           tie(b.deficit, a.critical, a.rank5, a.upper8);
}

template<class Callback>
static void enumerate_moves(vector<int>& path, Callback callback) {
    vector<int> colors(1 << 14);
    for (int i = 0; i + 1 < static_cast<int>(path.size()); ++i)
        ++colors[path[i] & path[i + 1]];
    const int n = path.size();
    for (int left = 0; left < n; ++left) for (int right = left + 2; right < n; ++right) {
        if (left && !adjacent(path[left - 1], path[right])) continue;
        if (right + 1 < n && !adjacent(path[left], path[right + 1])) continue;
        vector<int> changed;
        auto change = [&](int a, int b, int delta) {
            const int c = a & b;
            colors[c] += delta;
            changed.push_back(c);
        };
        if (left) change(path[left - 1], path[left], -1);
        if (right + 1 < n) change(path[right], path[right + 1], -1);
        if (left) change(path[left - 1], path[right], +1);
        if (right + 1 < n) change(path[left], path[right + 1], +1);
        bool hard = true;
        for (int c : changed) hard &= colors[c] > 0;
        if (hard) {
            reverse(path.begin() + left, path.begin() + right + 1);
            callback(left, right, evaluate(path));
            reverse(path.begin() + left, path.begin() + right + 1);
        }
        if (right + 1 < n) change(path[left], path[right + 1], -1);
        if (left) change(path[left - 1], path[right], -1);
        if (right + 1 < n) change(path[right], path[right + 1], +1);
        if (left) change(path[left - 1], path[left], +1);
    }
}

int main(int argc, char** argv) {
    const int keep = argc > 1 ? stoi(argv[1]) : 128;
    const int allowance = argc > 2 ? stoi(argv[2]) : 2;
    vector<int> original_path;
    for (int x; cin >> x;) original_path.push_back(x);
    if (original_path.size() != 3432) return 2;
    const Eval original = evaluate(original_path);
    const int required_critical = original.critical;
    vector<Candidate> first;
    vector<int> working = original_path;
    enumerate_moves(working, [&](int left, int right, const Eval& e) {
        if (e.critical < required_critical) return;
        if (e.rank5 < original.rank5 - 3) return;
        if (e.deficit > original.deficit + allowance) return;
        vector<int> path = original_path;
        reverse(path.begin() + left, path.begin() + right + 1);
        first.push_back({e, left, right, move(path)});
    });
    sort(first.begin(), first.end(), [](const Candidate& a, const Candidate& b) {
        if (better(a.eval, b.eval)) return true;
        if (better(b.eval, a.eval)) return false;
        return tie(a.left, a.right) < tie(b.left, b.right);
    });
    vector<Candidate> stratified;
    const int quota = max(1, keep / (allowance + 1));
    for (int delta = 0; delta <= allowance; ++delta) {
        int taken = 0;
        for (Candidate& candidate : first)
            if (candidate.eval.deficit == original.deficit + delta && taken < quota) {
                stratified.push_back(move(candidate));
                ++taken;
            }
    }
    first.swap(stratified);

    Eval best = original;
    vector<int> best_path = original_path;
    int best_first_l = -1, best_first_r = -1, best_second_l = -1, best_second_r = -1;
    long long second_moves = 0;
    for (int index = 0; index < static_cast<int>(first.size()); ++index) {
        vector<int> path = first[index].path;
        enumerate_moves(path, [&](int left, int right, const Eval& e) {
            ++second_moves;
            if (e.critical < required_critical) return;
            if (e.rank5 < original.rank5 - 1) return;
            if (!better(e, best)) return;
            best = e;
            // enumerate_moves invokes the callback while [left,right] is
            // already reversed.  Copying path therefore captures both moves;
            // reversing the copy once more used to silently discard move two.
            best_path = path;
            best_first_l = first[index].left;
            best_first_r = first[index].right;
            best_second_l = left;
            best_second_r = right;
        });
        if (index % 16 == 15)
            cerr << "tested=" << index + 1 << '/' << first.size()
                 << " best_deficit=" << best.deficit << '\n';
    }
    cerr << "original=" << original.deficit << ',' << original.critical << ','
         << original.rank5 << ',' << original.upper8
         << " best=" << best.deficit << ',' << best.critical << ','
         << best.rank5 << ',' << best.upper8
         << " first=[" << best_first_l << ',' << best_first_r << ']'
         << " second=[" << best_second_l << ',' << best_second_r << ']'
         << " candidates=" << first.size() << " second_moves=" << second_moves << '\n';
    for (int x : best_path) cout << x << ' ';
    cout << '\n';
}
