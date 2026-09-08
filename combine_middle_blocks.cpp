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
#include <random>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

static int violations(const vector<int>& q, int k) {
    int result = 0;
    for (int bit = 0; bit < k; ++bit) {
        int start = 0;
        while (start < static_cast<int>(q.size())) {
            if (!(q[start] & (1 << bit))) { ++start; continue; }
            int end = start + 1;
            while (end < static_cast<int>(q.size()) && (q[end] & (1 << bit))) ++end;
            if (start > 0 && end < static_cast<int>(q.size()) && end - start < 3)
                result += 3 - (end - start);
            start = end;
        }
    }
    return result;
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

static vector<int> parse(const string& line) {
    istringstream input(line);
    vector<int> result;
    for (int value; input >> value;) result.push_back(value);
    return result;
}

int main(int argc, char** argv) {
    if (argc < 3) return 2;
    const int k = stoi(argv[1]), old_k = k - 1;
    const int output_threshold = argc > 3 ? stoi(argv[3]) : -1;
    const int permutation_samples = argc > 4 ? stoi(argv[4]) : 1;
    ifstream prefix_file(argv[2]);
    vector<int> x;
    for (int value; prefix_file >> value;) x.push_back(value);
    int wanted_high = 0;
    for (int mask = 1; mask < (1 << k); ++mask)
        wanted_high += popcount(static_cast<unsigned>(mask)) >= (k + 1) / 2;
    const int high_bit = 1 << old_k;
    int tested = 0, best_high = 0, best_violations = 1000000;
    string line;
    while (getline(cin, line)) {
        vector<int> p = parse(line);
        if (p.empty()) continue;
        vector<int> y;
        for (int value : p) y.push_back(high_bit | value);
        uint64_t hash = 0xcbf29ce484222325ULL;
        for (int value : p) hash = (hash ^ static_cast<unsigned>(value)) * 0x100000001b3ULL;
        mt19937_64 rng(hash);
        for (int sample = 0; sample < permutation_samples; ++sample) {
            vector<int> permutation(old_k);
            iota(permutation.begin(), permutation.end(), 0);
            if (sample) shuffle(permutation.begin(), permutation.end(), rng);
            vector<int> permuted_x;
            permuted_x.reserve(x.size());
            for (int mask : x) {
                int value = 0;
                for (int bit = 0; bit < old_k; ++bit)
                    if (mask & (1 << bit)) value |= 1 << permutation[bit];
                permuted_x.push_back(value);
            }
        for (int reverse_x = 0; reverse_x < 2; ++reverse_x) {
            vector<int> xv = permuted_x;
            if (reverse_x) reverse(xv.begin(), xv.end());
            for (int order = 0; order < 2; ++order) {
                vector<int> q;
                if (!order) {
                    q = xv;
                    q.insert(q.end(), y.begin(), y.end());
                } else {
                    q = y;
                    q.insert(q.end(), xv.begin(), xv.end());
                }
                ++tested;
                const int bad = violations(q, k);
                const int high = high_coverage(q, k, (k + 1) / 2);
                if (high > best_high || (high == best_high && bad < best_violations)) {
                    best_high = high;
                    best_violations = bad;
                    cerr << "tested=" << tested << " high=" << high
                         << " violations=" << bad << '\n';
                }
                if (!bad && high >= (output_threshold < 0 ? wanted_high : output_threshold)) {
                    for (int value : q) cout << value << ' ';
                    cout << '\n' << flush;
                }
            }
        }
        }
    }
    cerr << "done tested=" << tested << " best_high=" << best_high
         << " best_violations=" << best_violations << '\n';
}
