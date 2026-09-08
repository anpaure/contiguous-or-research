#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <array>
#include <cstdint>
#include <iostream>
#include <vector>

using namespace std;

static bool verify(const vector<int>& a, int k) {
    vector<uint8_t> seen(1 << k);
    array<int, 32> previous{}, current{};
    int previous_size = 0;
    for (int value : a) {
        int current_size = 0;
        current[current_size++] = value;
        for (int i = 0; i < previous_size; ++i) {
            const int next = previous[i] | value;
            if (next != current[current_size - 1]) current[current_size++] = next;
        }
        for (int i = 0; i < current_size; ++i) seen[current[i]] = 1;
        previous.swap(current);
        previous_size = current_size;
    }
    for (int mask = 1; mask < (1 << k); ++mask) if (!seen[mask]) return false;
    return true;
}

int main(int argc, char** argv) {
    const int k = argc > 1 ? stoi(argv[1]) : 10;
    vector<int> a;
    for (int value; cin >> value;) a.push_back(value);
    uint64_t tested = 0;
    for (int position = 0; position < static_cast<int>(a.size()); ++position) {
        const int old = a[position];
        for (int proposal = 1; proposal < (1 << k); ++proposal) {
            if (proposal == old) continue;
            ++tested;
            a[position] = proposal;
            if (!verify(a, k)) continue;
            cerr << "FOUND position=" << position << " old=" << old
                 << " new=" << proposal << " tested=" << tested << '\n';
            for (int value : a) cout << value << ' ';
            cout << '\n';
            return 0;
        }
        a[position] = old;
    }
    cerr << "NONE tested=" << tested << '\n';
    return 1;
}
