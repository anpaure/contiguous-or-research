#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <algorithm>
#include <bit>
#include <iostream>
#include <map>
#include <tuple>
#include <vector>
using namespace std;

struct Candidate { int left, length, envelope_union; };

int main(int argc, char** argv) {
    if (argc < 5) return 2;
    const int k = stoi(argv[1]), d = stoi(argv[2]);
    vector<int> targets;
    for (int i = 3; i < argc; ++i) targets.push_back(stoi(argv[i]));
    const int full = (1 << k) - 1;
    vector<int> central;
    for (int value; cin >> value;) central.push_back(value);
    const int m = central.size(), n = m + d;
    vector<int> envelope(n, full);
    for (int position = 0; position < n; ++position)
        for (int i = max(0, position - d); i <= min(m - 1, position); ++i)
            envelope[position] &= central[i];

    vector<vector<Candidate>> candidates(targets.size());
    for (int t = 0; t < static_cast<int>(targets.size()); ++t)
        for (int length = 1; length <= d; ++length)
            for (int left = 0; left + length <= n; ++left) {
                int allowed = 0;
                bool position_nonzero = true;
                for (int p = left; p < left + length; ++p) {
                    allowed |= envelope[p];
                    position_nonzero &= (targets[t] & envelope[p]) != 0;
                }
                if ((targets[t] & ~allowed) == 0 && position_nonzero)
                    candidates[t].push_back({left, length, allowed});
            }
    for (int t = 0; t < static_cast<int>(targets.size()); ++t) {
        cout << "target=" << targets[t] << " candidates=" << candidates[t].size() << '\n';
        for (const auto& c : candidates[t])
            cout << "  [" << c.left << ',' << c.left + c.length - 1 << "] len="
                 << c.length << " envelope_union=" << c.envelope_union << '\n';
    }

    long long combinations = 0, successful = 0, nonzero_failures = 0,
              target_failures = 0, central_failures = 0;
    map<pair<int, int>, long long> central_failure_frequency;
    vector<int> choice(targets.size());
    auto visit = [&](auto&& self, int depth) -> void {
        if (depth < static_cast<int>(targets.size())) {
            for (int i = 0; i < static_cast<int>(candidates[depth].size()); ++i) {
                choice[depth] = i;
                self(self, depth + 1);
            }
            return;
        }
        ++combinations;
        vector<int> forbidden(n);
        for (int t = 0; t < static_cast<int>(targets.size()); ++t) {
            const Candidate& c = candidates[t][choice[t]];
            for (int p = c.left; p < c.left + c.length; ++p)
                forbidden[p] |= full & ~targets[t];
        }
        vector<int> legal(n);
        bool nonzero = true;
        for (int p = 0; p < n; ++p) {
            legal[p] = envelope[p] & ~forbidden[p];
            nonzero &= legal[p] != 0;
        }
        if (!nonzero) { ++nonzero_failures; return; }
        for (int t = 0; t < static_cast<int>(targets.size()); ++t) {
            const Candidate& c = candidates[t][choice[t]];
            int united = 0;
            for (int p = c.left; p < c.left + c.length; ++p) united |= legal[p];
            if (united != targets[t]) { ++target_failures; return; }
        }
        bool central_ok = true;
        for (int i = 0; i < m; ++i) {
            int united = 0;
            for (int p = i; p <= i + d; ++p) united |= legal[p];
            const int missing = central[i] & ~united;
            if (!missing) continue;
            central_ok = false;
            for (int bits = missing; bits; bits &= bits - 1) {
                const int bit = countr_zero(static_cast<unsigned>(bits));
                ++central_failure_frequency[{bit, i}];
            }
        }
        if (!central_ok) { ++central_failures; return; }
        ++successful;
        cout << "successful_choice";
        for (int t = 0; t < static_cast<int>(targets.size()); ++t) {
            const Candidate& c = candidates[t][choice[t]];
            cout << ' ' << targets[t] << ":[" << c.left << ','
                 << c.left + c.length - 1 << ']';
        }
        cout << '\n';
    };
    visit(visit, 0);
    cout << "combinations=" << combinations << " successful=" << successful
         << " nonzero_failures=" << nonzero_failures
         << " target_failures=" << target_failures
         << " central_failures=" << central_failures << '\n';
    vector<tuple<long long, int, int>> failures;
    for (auto [key, count] : central_failure_frequency)
        failures.push_back({count, key.first, key.second});
    sort(failures.rbegin(), failures.rend());
    cout << "top_central_failures";
    for (int i = 0; i < min<int>(30, failures.size()); ++i) {
        auto [count, bit, window] = failures[i];
        cout << ' ' << "b" << bit << "@" << window << ':' << count;
    }
    cout << '\n';
}
