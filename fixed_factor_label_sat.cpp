#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <cadical.hpp>

#include <algorithm>
#include <bit>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(int argc, char** argv) {
    if (argc < 4 || argc > 6) return 2;
    const int k = stoi(argv[1]);
    const int d = stoi(argv[2]);
    const bool natural = string(argv[3]) == "natural";
    const int maximum_target_rank = argc > 4 ? stoi(argv[4]) : k;
    const int minimum_target_rank = argc > 5 ? stoi(argv[5]) : 1;
    vector<int> central;
    for (int value; cin >> value;) central.push_back(value);
    if (central.empty()) return 2;
    const int central_rank = popcount(static_cast<unsigned>(central.front()));
    const int n = central.size() + d;
    const int limit = 1 << k;
    vector<int> envelope(n, limit - 1);
    for (int position = 0; position < n; ++position)
        for (int i = max(0, position - d);
             i <= min(static_cast<int>(central.size()) - 1, position); ++i)
            envelope[position] &= central[i];

    auto length_range = [&] (int target_rank) {
        const int maximum_length = min(d, target_rank);
        if (!natural) return pair<int,int>{1, maximum_length};
        const int length = target_rank <= central_rank - d ? 1
            : target_rank - (central_rank - d) + 1;
        return pair<int,int>{length, length};
    };
    long long selector_count = 0;
    for (int target = 1; target < limit; ++target) {
        const int target_rank = popcount(static_cast<unsigned>(target));
        if (target_rank >= central_rank || target_rank > maximum_target_rank ||
            target_rank < minimum_target_rank) continue;
        const auto [first_length, last_length] = length_range(target_rank);
        for (int length = first_length; length <= last_length; ++length)
            selector_count += n - length + 1;
    }
    const long long declared = static_cast<long long>(n) * k + selector_count;
    if (declared > 2000000000LL) return 2;

    CaDiCaL::Solver solver;
    solver.set("quiet", 1);
    solver.declare_more_variables(static_cast<int>(declared));
    int variables = n * k;
    auto x = [&] (int position, int bit) { return position * k + bit + 1; };
    auto clause = [&] (const vector<int>& values) {
        for (int value : values) solver.add(value);
        solver.add(0);
    };
    for (int position = 0; position < n; ++position) {
        vector<int> nonzero;
        for (int bit = 0; bit < k; ++bit) {
            solver.phase(-x(position, bit));
            if (envelope[position] & (1 << bit)) nonzero.push_back(x(position, bit));
            else clause({-x(position, bit)});
        }
        clause(nonzero);
    }
    for (int start = 0; start < static_cast<int>(central.size()); ++start)
        for (int bit = 0; bit < k; ++bit) if (central[start] & (1 << bit)) {
            vector<int> cover;
            for (int position = start; position <= start + d; ++position)
                cover.push_back(x(position, bit));
            clause(cover);
        }

    for (int target = 1; target < limit; ++target) {
        const int target_rank = popcount(static_cast<unsigned>(target));
        if (target_rank >= central_rank || target_rank > maximum_target_rank ||
            target_rank < minimum_target_rank) continue;
        const auto [first_length, last_length] = length_range(target_rank);
        vector<int> witnesses;
        for (int length = first_length; length <= last_length; ++length)
            for (int left = 0; left + length <= n; ++left) {
                const int select = ++variables;
                solver.phase(-select);
                witnesses.push_back(select);
                for (int bit = 0; bit < k; ++bit) {
                    if (!(target & (1 << bit))) {
                        for (int position = left; position < left + length; ++position)
                            clause({-select, -x(position, bit)});
                    } else {
                        vector<int> cover{-select};
                        for (int position = left; position < left + length; ++position)
                            cover.push_back(x(position, bit));
                        clause(cover);
                    }
                }
            }
        clause(witnesses);
    }
    cerr << "n=" << n << " selectors=" << selector_count
         << " variables=" << variables << '\n';
    const int result = solver.solve();
    if (result != 10) {
        cerr << (result == 20 ? "UNSAT" : "UNKNOWN") << '\n';
        return 1;
    }
    cerr << "SAT\n";
    for (int position = 0; position < n; ++position) {
        int value = 0;
        for (int bit = 0; bit < k; ++bit)
            if (solver.val(x(position, bit)) > 0) value |= 1 << bit;
        cout << value << ' ';
    }
    cout << '\n';
}
