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
#include <numeric>
#include <vector>

using namespace std;

static vector<int> reflected_gray(int n, int choose) {
    if (choose == 0) return {0};
    if (choose == n) return {(1 << n) - 1};
    vector<int> first = reflected_gray(n - 1, choose);
    vector<int> second = reflected_gray(n - 1, choose - 1);
    reverse(second.begin(), second.end());
    for (int& value : second) value |= 1 << (n - 1);
    first.insert(first.end(), second.begin(), second.end());
    return first;
}

static int permute_mask(int value, const vector<int>& permutation) {
    int result = 0;
    for (int bit = 0; bit < static_cast<int>(permutation.size()); ++bit)
        if (value & (1 << bit)) result |= 1 << permutation[bit];
    return result;
}

int main(int argc, char** argv) {
    if (argc < 2) return 2;
    const bool reverse_high = argc > 2 && stoi(argv[2]);
    const bool reverse_low = argc > 3 && stoi(argv[3]);
    ifstream input(argv[1]);
    vector<int> high_path;
    for (int value; input >> value;) high_path.push_back(value);
    if (high_path.size() != 252) return 2;
    if (reverse_high) reverse(high_path.begin(), high_path.end());

    vector<int> low_path = reflected_gray(10, 6);
    if (reverse_low) reverse(low_path.begin(), low_path.end());
    const int endpoint = high_path.back();
    int extra = 0;
    while (endpoint & (1 << extra)) ++extra;
    const int target = endpoint | (1 << extra);
    vector<int> source_one, source_zero, target_one, target_zero;
    for (int bit = 0; bit < 10; ++bit) {
        (low_path.front() & (1 << bit) ? source_one : source_zero).push_back(bit);
        (target & (1 << bit) ? target_one : target_zero).push_back(bit);
    }
    vector<int> permutation(10);
    for (int i = 0; i < 6; ++i) permutation[source_one[i]] = target_one[i];
    for (int i = 0; i < 4; ++i) permutation[source_zero[i]] = target_zero[i];
    for (int& value : low_path) value = permute_mask(value, permutation);

    constexpr int high_bit = 1 << 10;
    for (int value : high_path) cout << (high_bit | value) << ' ';
    for (int value : low_path) cout << value << ' ';
    cout << '\n';
}
