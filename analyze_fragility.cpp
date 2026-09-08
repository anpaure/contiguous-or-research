#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <iostream>
#include <tuple>
#include <vector>

using namespace std;

struct Evaluation {
    int covered = 0;
    int score = 0;
    vector<int> missing;
};

static Evaluation evaluate(const vector<int>& a, int k) {
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
    Evaluation result;
    for (int mask = 1; mask < (1 << k); ++mask) {
        const int rank = popcount(static_cast<unsigned>(mask));
        const int weight = 1 + 100 * (rank == k / 2) +
            8 * (rank == k / 2 - 1 || rank == k / 2 + 1);
        if (seen[mask]) ++result.covered, result.score += weight;
        else result.missing.push_back(mask);
    }
    return result;
}

int main(int argc, char** argv) {
    const int k = argc > 1 ? stoi(argv[1]) : 10;
    const int target = argc > 2 ? stoi(argv[2]) : 644;
    vector<int> a;
    for (int value; cin >> value;) a.push_back(value);

    vector<int> witness_count(1 << k), shortest(1 << k, a.size() + 1);
    vector<pair<int, int>> sole(1 << k, {-1, -1});
    for (int left = 0; left < static_cast<int>(a.size()); ++left) {
        int value = 0;
        for (int right = left; right < static_cast<int>(a.size()); ++right) {
            value |= a[right];
            ++witness_count[value];
            shortest[value] = min(shortest[value], right - left + 1);
            sole[value] = {left, right};
        }
    }
    vector<tuple<int, int, int, vector<int>>> candidates;
    for (int position = 0; position < static_cast<int>(a.size()); ++position) {
        const int old = a[position];
        a[position] = target;
        Evaluation result = evaluate(a, k);
        candidates.push_back({result.score, result.covered, position, result.missing});
        a[position] = old;
    }
    sort(candidates.begin(), candidates.end(), [] (const auto& lhs, const auto& rhs) {
        if (get<0>(lhs) != get<0>(rhs)) return get<0>(lhs) > get<0>(rhs);
        return get<1>(lhs) > get<1>(rhs);
    });
    vector<int> fragility(a.size());
    for (int mask = 1; mask < (1 << k); ++mask) {
        if (witness_count[mask] != 1) continue;
        for (int position = sole[mask].first; position <= sole[mask].second; ++position)
            ++fragility[position];
    }
    vector<int> positions(a.size());
    for (int i = 0; i < static_cast<int>(a.size()); ++i) positions[i] = i;
    sort(positions.begin(), positions.end(), [&] (int x, int y) {
        return fragility[x] != fragility[y] ? fragility[x] < fragility[y] : x < y;
    });
    cout << "least fragile positions:";
    for (int i = 0; i < min(100, static_cast<int>(positions.size())); ++i)
        cout << ' ' << positions[i] << ':' << fragility[positions[i]];
    cout << "\n\n";
    cout << "unique witnesses:\n";
    for (int mask = 1; mask < (1 << k); ++mask)
        if (witness_count[mask] == 1)
            cout << mask << "=[" << sole[mask].first << ',' << sole[mask].second
                 << "] len=" << shortest[mask] << '\n';
    cout << "\nbest replacements by " << target << ":\n";
    for (int i = 0; i < min(30, static_cast<int>(candidates.size())); ++i) {
        const auto& [score, covered, position, missing] = candidates[i];
        cout << "position=" << position << " old=" << a[position]
             << " score=" << score << " covered=" << covered << " missing:";
        for (int mask : missing) cout << ' ' << mask;
        cout << '\n';
    }
}
