#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <algorithm>
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

static void emit(const vector<int>& a, const char* operation, int i, int j,
                 uint64_t tested) {
    cerr << "FOUND operation=" << operation << " positions=" << i << ',' << j
         << " tested=" << tested << '\n';
    for (int value : a) cout << value << ' ';
    cout << '\n';
}

int main(int argc, char** argv) {
    const int k = argc > 1 ? stoi(argv[1]) : 10;
    vector<int> a;
    for (int value; cin >> value;) a.push_back(value);
    uint64_t tested = 0;
    for (int i = 0; i < static_cast<int>(a.size()); ++i) {
        for (int j = i + 1; j < static_cast<int>(a.size()); ++j) {
            swap(a[i], a[j]);
            ++tested;
            if (verify(a, k)) { emit(a, "swap", i, j, tested); return 0; }
            swap(a[i], a[j]);

            reverse(a.begin() + i, a.begin() + j + 1);
            ++tested;
            if (verify(a, k)) { emit(a, "reverse", i, j, tested); return 0; }
            reverse(a.begin() + i, a.begin() + j + 1);
        }
    }
    for (int from = 0; from < static_cast<int>(a.size()); ++from) {
        for (int to = 0; to < static_cast<int>(a.size()); ++to) {
            if (from == to) continue;
            const int value = a[from];
            a.erase(a.begin() + from);
            a.insert(a.begin() + to, value);
            ++tested;
            if (verify(a, k)) { emit(a, "move", from, to, tested); return 0; }
            a.erase(a.begin() + to);
            a.insert(a.begin() + from, value);
        }
    }
    cerr << "NONE tested=" << tested << '\n';
    return 1;
}
