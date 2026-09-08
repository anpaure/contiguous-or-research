#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <bit>
#include <iostream>
#include <vector>

using namespace std;

static bool rootable(const vector<int>& q, int k) {
    for (int bit = 0; bit < k; ++bit) {
        int start = 0;
        while (start < static_cast<int>(q.size())) {
            if (!(q[start] & (1 << bit))) { ++start; continue; }
            int end = start + 1;
            while (end < static_cast<int>(q.size()) && (q[end] & (1 << bit))) ++end;
            if (start && end < static_cast<int>(q.size()) && end - start < 3)
                return false;
            start = end;
        }
    }
    return true;
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

int main(int argc, char** argv) {
    const int k = argc > 1 ? stoi(argv[1]) : 10;
    const int rank = argc > 2 ? stoi(argv[2]) : (k + 1) / 2;
    vector<int> original;
    for (int value; cin >> value;) original.push_back(value);
    int wanted = 0;
    for (int mask = 1; mask < (1 << k); ++mask)
        wanted += popcount(static_cast<unsigned>(mask)) >= rank;
    uint64_t tested = 0, rootable_count = 0;
    int best = high_coverage(original, k, rank);
    vector<int> q;
    q.reserve(original.size() + 1);
    for (int position = 0; position <= static_cast<int>(original.size()); ++position) {
        for (int inserted = 1; inserted < (1 << k); ++inserted) {
            if (popcount(static_cast<unsigned>(inserted)) != rank) continue;
            ++tested;
            q = original;
            q.insert(q.begin() + position, inserted);
            if (!rootable(q, k)) continue;
            ++rootable_count;
            const int high = high_coverage(q, k, rank);
            if (high > best) {
                best = high;
                cerr << "best=" << best << '/' << wanted << " position=" << position
                     << " inserted=" << inserted << '\n';
            }
            if (high == wanted) {
                for (int value : q) cout << value << ' ';
                cout << '\n';
            }
        }
    }
    cerr << "tested=" << tested << " rootable=" << rootable_count
         << " best=" << best << '/' << wanted << '\n';
}
