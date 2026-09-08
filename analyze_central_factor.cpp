#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <algorithm>
#include <bit>
#include <iostream>
#include <map>
#include <set>
#include <vector>

using namespace std;

static vector<int> derivative(const vector<int>& values) {
    vector<int> result;
    result.reserve(values.size() - 1);
    for (int i = 0; i + 1 < static_cast<int>(values.size()); ++i)
        result.push_back(values[i] | values[i + 1]);
    return result;
}

static map<int, int> rank_distribution(const vector<int>& values) {
    map<int, int> result;
    for (int value : values)
        ++result[popcount(static_cast<unsigned>(value))];
    return result;
}

static void print_distribution(const char* label, const vector<int>& values) {
    cout << label << " count=" << values.size()
         << " distinct=" << set<int>(values.begin(), values.end()).size()
         << " ranks=";
    for (auto [rank, count] : rank_distribution(values))
        cout << rank << ':' << count << ' ';
    cout << '\n';
}

int main(int argc, char** argv) {
    if (argc != 3) return 2;
    const int k = stoi(argv[1]);
    const int d = stoi(argv[2]);
    const int universe = (1 << k) - 1;
    vector<int> a;
    for (int value; cin >> value;) a.push_back(value);
    if (a.size() <= static_cast<size_t>(d)) return 2;

    vector<vector<int>> rows{a};
    for (int q = 1; q <= d; ++q) rows.push_back(derivative(rows.back()));
    const vector<int>& t = rows[d];

    bool run_condition = true;
    for (int bit = 0; bit < k; ++bit) {
        int position = 0;
        while (position < static_cast<int>(t.size())) {
            if (!(t[position] & (1 << bit))) {
                ++position;
                continue;
            }
            const int first = position;
            while (position < static_cast<int>(t.size()) &&
                   (t[position] & (1 << bit))) ++position;
            const bool internal = first > 0 && position < static_cast<int>(t.size());
            if (internal && position - first <= d) {
                run_condition = false;
                cout << "short-run bit=" << bit << " first=" << first
                     << " length=" << position - first << '\n';
            }
        }
    }

    vector<int> maximum(a.size(), universe);
    for (int position = 0; position < static_cast<int>(a.size()); ++position) {
        const int first = max(0, position - d);
        const int last = min(static_cast<int>(t.size()) - 1, position);
        for (int index = first; index <= last; ++index)
            maximum[position] &= t[index];
    }
    bool is_subfactor = true;
    int equal_entries = 0;
    for (int i = 0; i < static_cast<int>(a.size()); ++i) {
        is_subfactor &= (a[i] & ~maximum[i]) == 0;
        equal_entries += a[i] == maximum[i];
    }

    cout << "k=" << k << " n=" << a.size() << " d=" << d
         << " run_condition=" << run_condition
         << " subfactor=" << is_subfactor
         << " equal_entries=" << equal_entries << '\n';
    for (int q = 0; q <= d; ++q) {
        const string label = "D^" + to_string(q) + " A";
        print_distribution(label.c_str(), rows[q]);
    }
    vector<int> max_row = maximum;
    for (int q = 0; q <= d; ++q) {
        const string label = "D^" + to_string(q) + " Amax";
        print_distribution(label.c_str(), max_row);
        if (q < d) max_row = derivative(max_row);
    }
    cout << "max_factor_valid=" << (max_row == t) << '\n';
}
