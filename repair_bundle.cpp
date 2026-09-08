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

int main(int argc, char** argv) {
    if (argc < 5) return 2;
    const int k = stoi(argv[1]);
    vector<int> bundle;
    for (int i = 2; i < argc; ++i) bundle.push_back(stoi(argv[i]));
    vector<int> input;
    for (int value; cin >> value;) input.push_back(value);
    vector<int> remainder = input;
    for (int value : bundle) {
        const auto found = find(remainder.begin(), remainder.end(), value);
        if (found == remainder.end()) return 2;
        remainder.erase(found);
    }
    sort(bundle.begin(), bundle.end());
    uint64_t tested = 0;
    do {
        for (int position = 0; position <= static_cast<int>(remainder.size()); ++position) {
            vector<int> candidate = remainder;
            candidate.insert(candidate.begin() + position, bundle.begin(), bundle.end());
            ++tested;
            if (!verify(candidate, k)) continue;
            cerr << "FOUND position=" << position << " tested=" << tested << '\n';
            for (int value : candidate) cout << value << ' ';
            cout << '\n';
            return 0;
        }
        for (int position = 0; position + static_cast<int>(bundle.size()) <=
             static_cast<int>(input.size()); ++position) {
            vector<int> candidate = input;
            for (int offset = 0; offset < static_cast<int>(bundle.size()); ++offset) {
                const auto found = find(candidate.begin() + position + offset,
                                        candidate.end(), bundle[offset]);
                const auto fallback = found == candidate.end()
                    ? find(candidate.begin(), candidate.begin() + position + offset,
                           bundle[offset]) : found;
                if (fallback == candidate.end()) return 2;
                iter_swap(candidate.begin() + position + offset, fallback);
            }
            ++tested;
            if (!verify(candidate, k)) continue;
            cerr << "FOUND swap-position=" << position << " tested=" << tested << '\n';
            for (int value : candidate) cout << value << ' ';
            cout << '\n';
            return 0;
        }
    } while (next_permutation(bundle.begin(), bundle.end()));
    cerr << "NONE tested=" << tested << '\n';
    return 1;
}
