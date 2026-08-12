#include <algorithm>
#include <atomic>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <mutex>
#include <string>
#include <tuple>
#include <vector>

using namespace std;

#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif

struct Eval {
    int deficit = 0;
    int possible5 = 0;
    int lower = 0;
    int upper = 0;
    int focus = 0;
    int potential = 0;
    vector<int> ranks;
};

static int pc(int value) {
    return __builtin_popcount(static_cast<unsigned>(value));
}

static bool adjacent(int a, int b) {
    return pc(a ^ b) == 2 && pc(a & b) == 5;
}

static Eval evaluate(const vector<int> &path, const vector<char> &focusMask) {
    constexpr int k = 11;
    constexpr int centralRank = 6;
    constexpr int delay = 3;
    constexpr int full = (1 << k) - 1;
    Eval result;
    result.ranks.assign(k + 1, 0);

    for (int bit = 0; bit < k; ++bit) {
        int position = 0;
        while (position < static_cast<int>(path.size())) {
            if (!(path[position] & (1 << bit))) {
                ++position;
                continue;
            }
            const int first = position;
            while (position < static_cast<int>(path.size()) &&
                   (path[position] & (1 << bit))) {
                ++position;
            }
            if (first && position < static_cast<int>(path.size())) {
                result.deficit += max(0, delay + 1 - (position - first));
            }
        }
    }

    vector<uint8_t> count(1 << k, 0);
    auto record = [&](int value, int wantedRank) {
        if (pc(value) != wantedRank) return;
        if (!count[value]) {
            ++result.ranks[wantedRank];
            if (wantedRank < centralRank) ++result.lower;
            if (wantedRank > centralRank) ++result.upper;
            if (focusMask[value]) ++result.focus;
        }
        if (count[value] != 255) ++count[value];
    };

    for (int value : path) record(value, centralRank);
    for (int length = 2; length <= delay + 1; ++length) {
        for (int left = 0; left + length <= static_cast<int>(path.size()); ++left) {
            int value = full;
            for (int j = left; j < left + length; ++j) value &= path[j];
            record(value, centralRank - length + 1);
        }
    }
    for (int length = 2; centralRank + length - 1 <= k; ++length) {
        for (int left = 0; left + length <= static_cast<int>(path.size()); ++left) {
            int value = 0;
            for (int j = left; j < left + length; ++j) value |= path[j];
            record(value, centralRank + length - 1);
        }
    }

    for (int mask = 1; mask <= full; ++mask) {
        if (pc(mask) == 5 &&
            (count[mask] || !(mask & ~path.front()) || !(mask & ~path.back()))) {
            ++result.possible5;
        }
        if (pc(mask) < 3 || !count[mask]) continue;
        int reward = 1024;
        for (int bonus = 256, occurrence = 1;
             bonus && occurrence < count[mask]; bonus >>= 1, ++occurrence) {
            reward += bonus;
        }
        result.potential += reward;
    }
    return result;
}

static bool invariant(const Eval &e) {
    return e.deficit == 0 && e.ranks[3] == 165 && e.ranks[4] == 330 &&
           e.ranks[5] == 461 && e.ranks[6] == 462 && e.possible5 == 462;
}

static tuple<int, int, int> score(const Eval &e) {
    return {e.upper, e.focus, e.potential};
}

int main(int argc, char **argv) {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    if (argc != 2) {
        cerr << "usage: k11_targeted_2opt output_path < seed_path\n";
        return 2;
    }

    vector<int> seed;
    for (int value; cin >> value;) seed.push_back(value);
    if (seed.size() != 462) {
        cerr << "expected 462 path vertices\n";
        return 2;
    }

    vector<char> focusMask(1 << 11, 0);
    vector<char> initiallySeen(1 << 11, 0);
    for (int length = 2; 6 + length - 1 <= 11; ++length) {
        for (int left = 0; left + length <= static_cast<int>(seed.size()); ++left) {
            int value = 0;
            for (int j = left; j < left + length; ++j) value |= seed[j];
            if (pc(value) == 6 + length - 1) initiallySeen[value] = 1;
        }
    }
    for (int mask = 1; mask < (1 << 11); ++mask) {
        if (pc(mask) > 6 && !initiallySeen[mask]) focusMask[mask] = 1;
    }

    Eval initial = evaluate(seed, focusMask);
    cerr << "initial deficit=" << initial.deficit
         << " lower=" << initial.lower << " possible5=" << initial.possible5
         << " upper=" << initial.upper << " focus=" << initial.focus << '\n';

    vector<int> best = seed;
    Eval bestEval = initial;
    mutex bestMutex;
    atomic<long long> checked{0}, validBoundary{0}, retained{0};
    const int n = static_cast<int>(seed.size());

#pragma omp parallel for schedule(dynamic, 1)
    for (int left = 0; left < n; ++left) {
        for (int right = left + 2; right < n; ++right) {
            ++checked;
            if (left && !adjacent(seed[left - 1], seed[right])) continue;
            if (right + 1 < n && !adjacent(seed[left], seed[right + 1])) continue;
            ++validBoundary;
            vector<int> candidate = seed;
            reverse(candidate.begin() + left, candidate.begin() + right + 1);
            Eval value = evaluate(candidate, focusMask);
            if (!invariant(value)) continue;
            ++retained;
            lock_guard<mutex> lock(bestMutex);
            if (score(value) > score(bestEval)) {
                bestEval = value;
                best.swap(candidate);
                cerr << "best left=" << left << " right=" << right
                     << " upper=" << bestEval.upper
                     << " focus=" << bestEval.focus
                     << " potential=" << bestEval.potential << '\n';
            }
        }
    }

    ofstream output(argv[1]);
    for (int value : best) output << value << ' ';
    output << '\n';
    cerr << "checked=" << checked << " boundary_valid=" << validBoundary
         << " invariant=" << retained << " final_upper=" << bestEval.upper
         << " final_focus=" << bestEval.focus << '\n';
    return 0;
}
