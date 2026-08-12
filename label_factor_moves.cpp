#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <algorithm>
#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

static int coverage(const vector<int>& a, int k) {
    vector<uint8_t> seen(1 << k);
    vector<int> previous, current;
    for (int x : a) {
        current.clear();
        current.push_back(x);
        for (int old : previous) {
            const int value = old | x;
            if (current.back() != value) current.push_back(value);
        }
        for (int value : current) seen[value] = 1;
        previous.swap(current);
    }
    int result = 0;
    for (int mask = 1; mask < (1 << k); ++mask) result += seen[mask];
    return result;
}

int main(int argc, char** argv) {
    if (argc != 4) return 2;
    const int k = stoi(argv[1]);
    const int d = stoi(argv[2]);
    ifstream central_input(argv[3]);
    vector<int> central, a;
    for (int x; central_input >> x;) central.push_back(x);
    for (int x; cin >> x;) a.push_back(x);
    const int factor_length = central.size() + d;
    vector<int> envelope(factor_length, (1 << k) - 1);
    for (int position = 0; position < factor_length; ++position)
        for (int i = max(0, position - d);
             i <= min(static_cast<int>(central.size()) - 1, position); ++i)
            envelope[position] &= central[i];
    auto valid = [&] (int position) {
        for (int start = max(0, position - d);
             start <= min(static_cast<int>(central.size()) - 1, position); ++start) {
            int value = 0;
            for (int i = start; i <= start + d; ++i) value |= a[i];
            if (value != central[start]) return false;
        }
        return true;
    };

    const int original = coverage(a, k);
    int best = original, improving = 0, valid_moves = 0;
    vector<int> best_array = a;
    for (int position = 0; position < static_cast<int>(a.size()); ++position) {
        const int old = a[position];
        if (position < factor_length) {
            for (int value = envelope[position]; value;
                 value = (value - 1) & envelope[position]) {
                if (value == old) continue;
                a[position] = value;
                if (!valid(position)) continue;
                ++valid_moves;
                const int score = coverage(a, k);
                improving += score > original;
                if (score > best) { best = score; best_array = a; }
            }
        } else {
            for (int value = 1; value < (1 << k); ++value) {
                if (value == old) continue;
                a[position] = value;
                ++valid_moves;
                const int score = coverage(a, k);
                improving += score > original;
                if (score > best) { best = score; best_array = a; }
            }
        }
        a[position] = old;
    }
    cerr << "original=" << original << " best=" << best
         << " valid_moves=" << valid_moves << " improving=" << improving << '\n';
    for (int value : best_array) cout << value << ' ';
    cout << '\n';
}
