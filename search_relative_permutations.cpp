#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <algorithm>
#include <array>
#include <atomic>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <mutex>
#include <numeric>
#include <string>
#include <thread>
#include <vector>

using namespace std;

static int coverage(const vector<int>& a) {
    array<uint8_t, 1024> seen{};
    array<int, 16> previous{}, current{};
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
    return accumulate(seen.begin() + 1, seen.end(), 0);
}

static int permute_mask(int x, const array<uint8_t, 9>& permutation) {
    int result = 0;
    for (int bit = 0; bit < 9; ++bit)
        if (x & (1 << bit)) result |= 1 << permutation[bit];
    return result;
}

int main(int argc, char** argv) {
    const string base_path = argc > 1 ? argv[1] : "k9_optimal.txt";
    const int thread_count = argc > 2 ? stoi(argv[2]) : 4;
    const string output_path = argc > 3 ? argv[3] : "relative_permutation_found.txt";
    ifstream input(base_path);
    vector<int> base;
    for (int value; input >> value;) base.push_back(value);
    if (base.size() != 128) return 2;

    vector<vector<int>> templates;
    auto add_interval = [&] (int start, int length, int extra, bool reverse_flag) {
        vector<int> value;
        if (extra >= 0) value.push_back(extra);
        value.insert(value.end(), base.begin() + start, base.begin() + start + length);
        if (reverse_flag) reverse(value.begin(), value.end());
        if (value.size() == 126) templates.push_back(move(value));
    };
    for (int reverse_flag = 0; reverse_flag < 2; ++reverse_flag) {
        add_interval(1, 126, -1, reverse_flag);
        add_interval(0, 126, -1, reverse_flag);
        add_interval(2, 126, -1, reverse_flag);
        add_interval(2, 125, 4, reverse_flag);
        add_interval(1, 125, 21, reverse_flag);
        add_interval(2, 125, 132, reverse_flag);
        add_interval(3, 125, 146, reverse_flag);
    }

    vector<array<uint8_t, 9>> permutations;
    array<uint8_t, 9> identity{};
    iota(identity.begin(), identity.end(), 0);
    do permutations.push_back(identity); while (next_permutation(identity.begin(), identity.end()));

    vector<int> fixed{512};
    fixed.insert(fixed.end(), base.rbegin(), base.rend());
    atomic<size_t> next{0};
    atomic<int> best{0};
    atomic<bool> found{false};
    mutex output_mutex;
    const size_t tasks = templates.size() * permutations.size();

    auto worker = [&] (int id) {
        vector<int> candidate(255);
        copy(fixed.begin(), fixed.end(), candidate.begin());
        while (!found.load(memory_order_relaxed)) {
            const size_t task = next.fetch_add(1, memory_order_relaxed);
            if (task >= tasks) break;
            const size_t template_index = task / permutations.size();
            const size_t permutation_index = task % permutations.size();
            const auto& permutation = permutations[permutation_index];
            for (int i = 0; i < 126; ++i)
                candidate[129 + i] = 512 |
                    permute_mask(templates[template_index][i], permutation);
            const int value = coverage(candidate);
            int old = best.load(memory_order_relaxed);
            if (value > old && best.compare_exchange_strong(old, value)) {
                lock_guard<mutex> lock(output_mutex);
                cerr << "best=" << value << "/1023 template=" << template_index
                     << " permutation=" << permutation_index << " worker=" << id << '\n';
            }
            if (value != 1023) continue;
            bool expected = false;
            if (found.compare_exchange_strong(expected, true)) {
                lock_guard<mutex> lock(output_mutex);
                ofstream output(output_path);
                for (int x : candidate) output << x << ' ';
                output << '\n';
                cerr << "FOUND template=" << template_index
                     << " permutation=" << permutation_index << '\n';
            }
        }
    };
    vector<thread> workers;
    for (int id = 0; id < thread_count; ++id) workers.emplace_back(worker, id);
    for (thread& value : workers) value.join();
    cerr << (found ? "SAT" : "NONE") << " best=" << best << "/1023\n";
    return found ? 0 : 1;
}
