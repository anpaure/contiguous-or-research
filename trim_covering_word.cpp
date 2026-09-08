#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#elif defined(__clang__)
#pragma clang optimize on
#endif

#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Scorer {
    int k_;
    vector<uint32_t> seen_;
    uint32_t epoch_ = 0;

    int weight(int mask) const {
        const int rank = popcount(static_cast<unsigned>(mask));
        const bool central = rank == k_ / 2 ||
            ((k_ & 1) && rank == k_ / 2 + 1);
        const bool near = rank == k_ / 2 - 1 || rank == k_ - k_ / 2 + 1;
        return 1 + 100 * central + 8 * near;
    }

public:
    explicit Scorer(int k) : k_(k), seen_(1U << k) {}

    pair<int, int> operator()(const vector<int>& a, vector<int>* missing = nullptr) {
        if (++epoch_ == 0) fill(seen_.begin(), seen_.end(), 0), ++epoch_;
        array<int, 32> previous{}, current{};
        int previous_size = 0;
        int score = 0, covered = 0;
        for (int value : a) {
            int current_size = 0;
            current[current_size++] = value;
            for (int i = 0; i < previous_size; ++i) {
                const int next = previous[i] | value;
                if (next != current[current_size - 1]) current[current_size++] = next;
            }
            for (int i = 0; i < current_size; ++i) {
                const int mask = current[i];
                if (mask && seen_[mask] != epoch_) {
                    seen_[mask] = epoch_;
                    score += weight(mask);
                    ++covered;
                }
            }
            swap(previous, current);
            previous_size = current_size;
        }
        if (missing) {
            missing->clear();
            for (int mask = 1; mask < (1 << k_); ++mask)
                if (seen_[mask] != epoch_) missing->push_back(mask);
        }
        return {score, covered};
    }
};

int main(int argc, char** argv) {
    const int k = argc > 1 ? stoi(argv[1]) : 8;
    const string word = argc > 2 ? argv[2] :
        "1234567182547386125384627513842716358726341568237415876412573641823178456231";
    const int drops = argc > 3 ? stoi(argv[3]) : 4;
    vector<int> source;
    for (char c : word) {
        if (c < '1' || c > char('0' + k)) return 2;
        source.push_back(1 << (c - '1'));
    }
    if (drops < 0 || drops >= static_cast<int>(source.size())) return 2;

    Scorer scorer(k);
    vector<int> chosen(source.size() - drops), best, missing;
    int best_score = -1, best_covered = -1;
    uint64_t tested = 0;

    vector<int> omitted;
    auto dfs = [&] (auto&& self, int at, int still_drop, int write) -> void {
        if (still_drop == 0) {
            for (int i = at; i < static_cast<int>(source.size()); ++i)
                chosen[write++] = source[i];
            const auto [score, covered] = scorer(chosen);
            ++tested;
            if (score > best_score || (score == best_score && covered > best_covered)) {
                best_score = score;
                best_covered = covered;
                best = chosen;
                scorer(best, &missing);
                cerr << "score=" << best_score << " covered=" << best_covered
                     << " tested=" << tested << " omitted:";
                for (int x : omitted) cerr << ' ' << x;
                cerr << " | array:";
                for (int x : best) cerr << ' ' << x;
                cerr << " | missing:";
                for (int x : missing) cerr << ' ' << x;
                cerr << '\n';
            }
            return;
        }
        if (static_cast<int>(source.size()) - at < still_drop) return;
        // Omit this position.
        omitted.push_back(at);
        self(self, at + 1, still_drop - 1, write);
        omitted.pop_back();
        // Keep this position.
        if (static_cast<int>(source.size()) - at > still_drop) {
            chosen[write] = source[at];
            self(self, at + 1, still_drop, write + 1);
        }
    };
    dfs(dfs, 0, drops, 0);
    cout << best.size();
    for (int x : best) cout << ' ' << x;
    cout << '\n';
    return best_covered == (1 << k) - 1 ? 0 : 1;
}
