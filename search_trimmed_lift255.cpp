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
#include <vector>

using namespace std;

static int covered(const vector<int>& a, int bits, vector<int>* missing = nullptr) {
    vector<uint8_t> seen(1 << bits);
    array<int, 32> previous{}, current{};
    int previous_size = 0;
    for (int x : a) {
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
    int result = 0;
    for (int x = 1; x < (1 << bits); ++x) {
        result += seen[x];
        if (!seen[x] && missing) missing->push_back(x);
    }
    return result;
}

static vector<int> make_candidate(const vector<int>& base,
                                  const vector<int>& residue) {
    constexpr int high = 512;
    vector<int> result;
    result.reserve(255);
    result.push_back(high);
    result.insert(result.end(), base.rbegin(), base.rend());
    for (int x : residue) result.push_back(high | x);
    return result;
}

static void print_candidate(const vector<int>& a) {
    for (int x : a) cout << x << ' ';
    cout << '\n';
}

int main(int argc, char** argv) {
    const string base_path = argc > 1 ? argv[1] : "k9_optimal.txt";
    ifstream input(base_path);
    vector<int> base;
    for (int value; input >> value;) base.push_back(value);
    if (base.size() != 128) return 2;

    int best = 0;
    vector<int> best_array;
    auto test = [&] (const vector<int>& residue, const string& description) {
        if (residue.size() != 126) return false;
        vector<int> candidate = make_candidate(base, residue);
        const int value = covered(candidate, 10);
        if (value > best) {
            best = value;
            best_array = candidate;
            vector<int> missing;
            covered(candidate, 10, &missing);
            cerr << "best=" << best << "/1023 " << description << " missing";
            for (int x : missing) cerr << ' ' << x;
            cerr << '\n';
        }
        if (value == 1023) {
            cerr << "FOUND " << description << '\n';
            print_candidate(candidate);
            return true;
        }
        return false;
    };

    // Literal deletion of two entries from B, in either direction.
    for (int reverse_flag = 0; reverse_flag < 2; ++reverse_flag) {
        vector<int> order = base;
        if (reverse_flag) reverse(order.begin(), order.end());
        for (int first = 0; first < 128; ++first) {
            for (int second = first + 1; second < 128; ++second) {
                vector<int> residue;
                residue.reserve(126);
                for (int i = 0; i < 128; ++i)
                    if (i != first && i != second) residue.push_back(order[i]);
                if (test(residue, "delete " + to_string(reverse_flag) + " " +
                                   to_string(first) + " " + to_string(second)))
                    return 0;
            }
        }
    }

    // Replace the three entries outside a length-125 interval by one arbitrary
    // nonzero residue.  This contains the known one-hole seed as
    // forward,start=2,z=4.
    for (int reverse_flag = 0; reverse_flag < 2; ++reverse_flag) {
        vector<int> order = base;
        if (reverse_flag) reverse(order.begin(), order.end());
        for (int start = 0; start + 125 <= 128; ++start) {
            for (int z = 1; z < 512; ++z) {
                vector<int> residue;
                residue.reserve(126);
                residue.push_back(z);
                residue.insert(residue.end(), order.begin() + start,
                               order.begin() + start + 125);
                if (test(residue, "replace-prefix " + to_string(reverse_flag) + " " +
                                   to_string(start) + " " + to_string(z)))
                    return 0;
                reverse(residue.begin(), residue.end());
                if (test(residue, "replace-suffix " + to_string(reverse_flag) + " " +
                                   to_string(start) + " " + to_string(z)))
                    return 0;
            }
        }
    }

    // The initial high element can repair one of two arbitrary deletions by a
    // cross-boundary suffix/prefix union.  The last base entry is already
    // represented by the leading [high] followed by the first entry of
    // reverse(B), so omit it for free and exhaust the remaining choices.
    for (int first = 0; first < 127; ++first) {
        for (int second = first + 1; second < 127; ++second) {
            for (int z = 1; z < 512; ++z) {
                vector<int> residue;
                residue.reserve(126);
                residue.push_back(z);
                for (int i = 0; i < 127; ++i)
                    if (i != first && i != second) residue.push_back(base[i]);
                if (test(residue, "two-delete-prefix " + to_string(first) + " " +
                                   to_string(second) + " " + to_string(z)))
                    return 0;
                reverse(residue.begin(), residue.end());
                if (test(residue, "two-delete-suffix " + to_string(first) + " " +
                                   to_string(second) + " " + to_string(z)))
                    return 0;
            }
        }
    }

    cerr << "NONE best=" << best << "/1023\n";
    print_candidate(best_array);
    return 1;
}
