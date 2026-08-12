#include <algorithm>
#include <bit>
#include <cstdint>
#include <iostream>
#include <vector>
using namespace std;

int main(int argc, char** argv) {
    if (argc != 4) return 2;
    const int k = stoi(argv[1]), d = stoi(argv[2]), central_rank = stoi(argv[3]);
    const int limit = 1 << k;
    vector<int> central;
    for (int value; cin >> value;) central.push_back(value);
    const int n = central.size() + d;
    vector<int> envelope(n, limit - 1);
    for (int p = 0; p < n; ++p)
        for (int i = max(0, p - d);
             i <= min(static_cast<int>(central.size()) - 1, p); ++i)
            envelope[p] &= central[i];
    vector<uint8_t> possible(limit);
    for (int length = 1; length <= d; ++length) {
        for (int left = 0; left + length <= n; ++left) {
            int union_envelope = 0;
            for (int p = left; p < left + length; ++p)
                union_envelope |= envelope[p];
            for (int target = union_envelope; target;
                 target = (target - 1) & union_envelope) {
                if (popcount(static_cast<unsigned>(target)) >= central_rank) continue;
                bool nonzero_labels = true;
                for (int p = left; p < left + length; ++p)
                    nonzero_labels &= (target & envelope[p]) != 0;
                if (nonzero_labels) possible[target] = 1;
            }
        }
    }
    int total = 0;
    for (int rank = 1; rank < central_rank; ++rank) {
        vector<int> missing;
        for (int mask = 1; mask < limit; ++mask)
            if (popcount(static_cast<unsigned>(mask)) == rank) {
                if (possible[mask]) ++total;
                else missing.push_back(mask);
            }
        cout << "rank " << rank << " possible="
             << ([&] { int value=0; for(int m=1;m<limit;++m)
                    value += possible[m] && popcount(static_cast<unsigned>(m))==rank;
                    return value; })()
             << " missing=" << missing.size();
        if (missing.size() <= 32) for (int x : missing) cout << ' ' << x;
        cout << '\n';
    }
    cout << "total=" << total << '\n';
}
