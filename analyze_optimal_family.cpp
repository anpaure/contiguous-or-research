#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <algorithm>
#include <bit>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <vector>
using namespace std;

static long long choose(int n, int r) {
    if (r < 0 || r > n) return 0;
    r = min(r, n - r);
    long long result = 1;
    for (int i = 1; i <= r; ++i) result = result * (n - r + i) / i;
    return result;
}

int main(int argc, char** argv) {
    if (argc != 3) return 2;
    const int k = stoi(argv[1]), limit = 1 << k;
    ifstream in(argv[2]);
    int declared = 0;
    in >> declared;
    vector<int> a;
    for (int x; in >> x;) if (x) a.push_back(x);
    if (declared != static_cast<int>(a.size()) + 1) return 3;

    vector<int> entry_count(k + 1), entry_distinct(k + 1);
    vector<uint8_t> entry_seen(limit);
    for (int x : a) {
        const int r = popcount(static_cast<unsigned>(x));
        ++entry_count[r];
        if (!entry_seen[x]) ++entry_distinct[r];
        entry_seen[x] = 1;
    }
    cout << "k=" << k << " n=" << a.size() << " entries";
    for (int r = 1; r <= k; ++r) if (entry_count[r])
        cout << ' ' << r << ':' << entry_count[r] << '/' << entry_distinct[r];
    cout << '\n';

    vector<int> shortest(limit, 1 << 30), witnesses(limit);
    for (int left = 0; left < static_cast<int>(a.size()); ++left) {
        int value = 0;
        for (int right = left; right < static_cast<int>(a.size()); ++right) {
            value |= a[right];
            const int length = right - left + 1;
            if (length < shortest[value]) {
                shortest[value] = length;
                witnesses[value] = 1;
            } else if (length == shortest[value]) ++witnesses[value];
            if (value == limit - 1) break;
        }
    }
    for (int r = 1; r <= k; ++r) {
        map<int, int> histogram;
        int unique_shortest = 0;
        for (int x = 1; x < limit; ++x)
            if (popcount(static_cast<unsigned>(x)) == r) {
                ++histogram[shortest[x]];
                unique_shortest += witnesses[x] == 1;
            }
        cout << " rank=" << r << " shortest";
        for (auto [length, count] : histogram) cout << ' ' << length << ':' << count;
        cout << " unique=" << unique_shortest << '/' << choose(k, r) << '\n';
    }

    const int central_rank = (k + 1) / 2;
    const int width = choose(k, central_rank);
    const int d = static_cast<int>(a.size()) - width;
    cout << " central_rank=" << central_rank << " width=" << width << " d=" << d;
    if (d < 0 || d > 16) { cout << " no-fixed-row\n"; return 0; }
    vector<int> central;
    vector<uint8_t> central_seen(limit);
    int exact_rank = 0, distinct = 0;
    for (int left = 0; left + d < static_cast<int>(a.size()); ++left) {
        int x = 0;
        for (int j = 0; j <= d; ++j) x |= a[left + j];
        central.push_back(x);
        if (popcount(static_cast<unsigned>(x)) == central_rank) {
            ++exact_rank;
            if (!central_seen[x]) ++distinct;
            central_seen[x] = 1;
        }
    }
    int johnson = 0;
    for (int i = 0; i + 1 < static_cast<int>(central.size()); ++i)
        johnson += popcount(static_cast<unsigned>(central[i] ^ central[i + 1])) == 2;
    cout << " central_windows=" << central.size() << " exact_rank=" << exact_rank
         << " distinct=" << distinct << " johnson_edges=" << johnson << '/'
         << max<int>(0, central.size() - 1) << '\n';

    if (exact_rank != static_cast<int>(central.size())) return 0;

    if (d == 2) {
        vector<int> pairs;
        pairs.reserve(a.size() - 1);
        map<int, int> pair_ranks, envelope_ranks, entry_envelope_ranks;
        int pair_equals_envelope = 0, entry_equals_envelope = 0;
        for (int i = 0; i + 1 < static_cast<int>(a.size()); ++i) {
            const int value = a[i] | a[i + 1];
            pairs.push_back(value);
            ++pair_ranks[popcount(static_cast<unsigned>(value))];
        }
        for (int i = 1; i < static_cast<int>(central.size()); ++i) {
            const int envelope = central[i - 1] & central[i];
            ++envelope_ranks[popcount(static_cast<unsigned>(envelope))];
            pair_equals_envelope += pairs[i] == envelope;
        }
        for (int i = 2; i + 2 < static_cast<int>(a.size()); ++i) {
            const int envelope = central[i - 2] & central[i - 1] & central[i];
            ++entry_envelope_ranks[popcount(static_cast<unsigned>(envelope))];
            entry_equals_envelope += a[i] == envelope;
        }
        cout << " pair_ranks";
        for (auto [r, count] : pair_ranks) cout << ' ' << r << ':' << count;
        cout << " pair_equals_central_intersection=" << pair_equals_envelope
             << '/' << max<int>(0, central.size() - 1) << " pair_envelope_ranks";
        for (auto [r, count] : envelope_ranks) cout << ' ' << r << ':' << count;
        cout << '\n';
        cout << " entry_equals_triple_envelope=" << entry_equals_envelope
             << '/' << max<int>(0, a.size() - 4) << " triple_envelope_ranks";
        for (auto [r, count] : entry_envelope_ranks) cout << ' ' << r << ':' << count;
        cout << '\n';
    }

    for (int length = 2; central_rank + length - 1 <= k; ++length) {
        vector<uint8_t> seen(limit);
        for (int left = 0; left + length <= static_cast<int>(central.size()); ++left) {
            int x = 0;
            for (int j = 0; j < length; ++j) x |= central[left + j];
            if (popcount(static_cast<unsigned>(x)) == central_rank + length - 1)
                seen[x] = 1;
        }
        cout << " upper_depth=" << length - 1 << " covered="
             << accumulate(seen.begin(), seen.end(), 0) << '/'
             << choose(k, central_rank + length - 1) << '\n';
    }
    for (int length = 2; length <= d + 1; ++length) {
        vector<uint8_t> seen(limit);
        for (int left = 0; left + length <= static_cast<int>(central.size()); ++left) {
            int x = limit - 1;
            for (int j = 0; j < length; ++j) x &= central[left + j];
            if (popcount(static_cast<unsigned>(x)) == central_rank - length + 1)
                seen[x] = 1;
        }
        cout << " lower_depth=" << length - 1 << " covered="
             << accumulate(seen.begin(), seen.end(), 0) << '/'
             << choose(k, central_rank - length + 1) << '\n';
    }
}
