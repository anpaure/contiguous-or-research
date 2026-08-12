#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <numeric>
#include <random>
#include <string>
#include <vector>

using namespace std;

static bool universal_skipping(const vector<int>& a, int bits, int skip) {
    vector<uint8_t> seen(1 << bits);
    array<int, 32> previous{}, current{};
    int previous_size = 0;
    for (int position = 0; position < static_cast<int>(a.size()); ++position) {
        if (position == skip) continue;
        const int x = a[position];
        int current_size = 0;
        current[current_size++] = x;
        for (int i = 0; i < previous_size; ++i) {
            const int value = previous[i] | x;
            if (value != current[current_size - 1]) current[current_size++] = value;
        }
        for (int i = 0; i < current_size; ++i) seen[current[i]] = 1;
        previous.swap(current);
        previous_size = current_size;
    }
    for (int x = 1; x < (1 << bits); ++x)
        if (!seen[x]) return false;
    return true;
}

int main(int argc, char** argv) {
    if (argc < 5) {
        cerr << "usage: greedy_prune_or BITS INPUT OUTPUT SEED\n";
        return 2;
    }
    const int bits = stoi(argv[1]);
    const uint64_t seed = stoull(argv[4]);
    ifstream input(argv[2]);
    vector<int> a;
    for (int x; input >> x;) if (x != 0) a.push_back(x);
    if (!universal_skipping(a, bits, -1)) {
        cerr << "input is not universal\n";
        return 3;
    }

    mt19937_64 rng(seed);
    vector<uint64_t> priority(a.size());
    for (uint64_t& x : priority) x = rng();
    int attempts = 0, removed = 0;
    // Priorities stay attached to entries.  After any deletion, revisit the
    // surviving entry now at that index only if it has not yet been tested.
    vector<uint8_t> tested(a.size());
    while (true) {
        int chosen = -1;
        for (int i = 0; i < static_cast<int>(a.size()); ++i)
            if (!tested[i] && (chosen < 0 || priority[i] < priority[chosen])) chosen = i;
        if (chosen < 0) break;
        ++attempts;
        if (universal_skipping(a, bits, chosen)) {
            a.erase(a.begin() + chosen);
            priority.erase(priority.begin() + chosen);
            tested.erase(tested.begin() + chosen);
            ++removed;
            if (removed % 25 == 0)
                cerr << "removed=" << removed << " remaining=" << a.size() << '\n';
        } else {
            tested[chosen] = 1;
        }
    }

    ofstream out(argv[3]);
    for (int x : a) out << x << ' ';
    out << '\n';
    cout << "seed=" << seed << " attempts=" << attempts << " removed=" << removed
         << " final=" << a.size() << '\n';
    return 0;
}
