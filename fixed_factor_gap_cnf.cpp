#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#endif

#include <algorithm>
#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

struct Descriptor {
    int fixed_or = 0;
    vector<int> entries;
};

int main(int argc, char** argv) {
    if (argc != 5) return 2;
    const int k = stoi(argv[1]);
    const int d = stoi(argv[2]);
    const int gap = stoi(argv[3]);
    const string output_path = argv[4];
    const int limit = 1 << k;
    vector<int> central;
    for (int value; cin >> value;) central.push_back(value);
    if (central.empty()) return 2;
    const int n = central.size() + d;
    if (gap < 0 || gap > n) return 2;
    const int extra_index = n;

    vector<int> envelope(n, limit - 1);
    for (int position = 0; position < n; ++position)
        for (int i = max(0, position - d);
             i <= min(static_cast<int>(central.size()) - 1, position); ++i)
            envelope[position] &= central[i];

    int variable_count = (n + 1) * k;
    auto x = [&] (int entry, int bit) { return entry * k + bit + 1; };
    vector<vector<int>> clauses;
    for (int position = 0; position < n; ++position) {
        vector<int> nonzero;
        for (int bit = 0; bit < k; ++bit) {
            if (envelope[position] & (1 << bit)) nonzero.push_back(x(position, bit));
            else clauses.push_back({-x(position, bit)});
        }
        clauses.push_back(move(nonzero));
    }
    {
        vector<int> nonzero;
        for (int bit = 0; bit < k; ++bit) nonzero.push_back(x(extra_index, bit));
        clauses.push_back(move(nonzero));
    }
    for (int start = 0; start < static_cast<int>(central.size()); ++start) {
        for (int bit = 0; bit < k; ++bit) {
            if (!(central[start] & (1 << bit))) continue;
            vector<int> cover;
            for (int position = start; position <= start + d; ++position)
                cover.push_back(x(position, bit));
            clauses.push_back(move(cover));
        }
    }

    auto add_factor_run = [&] (Descriptor& descriptor, int first, int last) {
        if (first > last) return;
        if (last - first + 1 >= d + 1) {
            int value = 0;
            for (int position = first; position <= last; ++position)
                value |= envelope[position];
            descriptor.fixed_or |= value;
        } else {
            for (int position = first; position <= last; ++position)
                descriptor.entries.push_back(position);
        }
    };

    const int total_length = n + 1;
    vector<Descriptor> descriptors;
    descriptors.reserve(total_length * (total_length + 1) / 2);
    vector<uint8_t> fixed_seen(limit);
    for (int left = 0; left < total_length; ++left) {
        for (int right = left; right < total_length; ++right) {
            Descriptor descriptor;
            if (right < gap) {
                add_factor_run(descriptor, left, right);
            } else if (left > gap) {
                add_factor_run(descriptor, left - 1, right - 1);
            } else {
                add_factor_run(descriptor, left, gap - 1);
                descriptor.entries.push_back(extra_index);
                add_factor_run(descriptor, gap, right - 1);
            }
            sort(descriptor.entries.begin(), descriptor.entries.end());
            descriptor.entries.erase(unique(descriptor.entries.begin(),
                                              descriptor.entries.end()),
                                     descriptor.entries.end());
            if (descriptor.entries.empty()) fixed_seen[descriptor.fixed_or] = 1;
            descriptors.push_back(move(descriptor));
        }
    }

    int constrained_targets = 0;
    long long selectors = 0;
    for (int target = 1; target < limit; ++target) {
        if (fixed_seen[target]) continue;
        ++constrained_targets;
        vector<int> witnesses;
        for (const Descriptor& descriptor : descriptors) {
            if (descriptor.fixed_or & ~target) continue;
            if ((target & ~descriptor.fixed_or) && descriptor.entries.empty()) continue;
            const int select = ++variable_count;
            ++selectors;
            witnesses.push_back(select);
            for (int bit = 0; bit < k; ++bit) {
                if (!(target & (1 << bit))) {
                    for (int entry : descriptor.entries)
                        clauses.push_back({-select, -x(entry, bit)});
                } else if (!(descriptor.fixed_or & (1 << bit))) {
                    vector<int> cover{-select};
                    for (int entry : descriptor.entries) cover.push_back(x(entry, bit));
                    clauses.push_back(move(cover));
                }
            }
        }
        if (witnesses.empty()) {
            cerr << "structural UNSAT target=" << target << '\n';
            return 1;
        }
        clauses.push_back(move(witnesses));
    }

    ofstream output(output_path);
    output << "p cnf " << variable_count << ' ' << clauses.size() << '\n';
    for (const vector<int>& clause : clauses) {
        for (int literal : clause) output << literal << ' ';
        output << "0\n";
    }
    cerr << "gap=" << gap << " constrained=" << constrained_targets
         << " selectors=" << selectors << " variables=" << variable_count
         << " clauses=" << clauses.size() << '\n';
}
