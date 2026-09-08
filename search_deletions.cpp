#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <array>
#include <cstdint>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

static int coverage_deleted(const vector<int>& a, int k, const array<int, 3>& removed,
                            int remove_count) {
    vector<uint8_t> seen(1 << k);
    array<int, 32> previous{}, current{};
    int previous_size = 0, removed_at = 0;
    for (int position = 0; position < static_cast<int>(a.size()); ++position) {
        if (removed_at < remove_count && position == removed[removed_at]) {
            ++removed_at;
            continue;
        }
        const int value = a[position];
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
    int covered = 0;
    for (int mask = 1; mask < (1 << k); ++mask) covered += seen[mask];
    return covered;
}

int main(int argc, char** argv) {
    if (argc < 5) return 2;
    const int k = stoi(argv[1]);
    const int remove_count = stoi(argv[2]);
    const int shard = stoi(argv[3]);
    const int shards = stoi(argv[4]);
    if (remove_count < 1 || remove_count > 3 || shard < 0 || shard >= shards) return 2;
    vector<int> a;
    for (int value; cin >> value;) a.push_back(value);
    const bool emit_best = argc > 5 && string(argv[5]) == "best";
    uint64_t tested = 0, ordinal = 0;
    int best_coverage = -1;
    array<int, 3> best_removed{-1, -1, -1};
    array<int, 3> removed{-1, -1, -1};
    for (int i = 0; i < static_cast<int>(a.size()); ++i) {
        removed[0] = i;
        const int j_begin = remove_count >= 2 ? i + 1 : static_cast<int>(a.size());
        if (remove_count == 1) {
            if (ordinal++ % shards != static_cast<uint64_t>(shard)) continue;
            ++tested;
            {
                const int covered = coverage_deleted(a, k, removed, remove_count);
                if (covered > best_coverage) best_coverage = covered, best_removed = removed;
                if (covered == (1 << k) - 1) goto found;
            }
            continue;
        }
        for (int j = j_begin; j < static_cast<int>(a.size()); ++j) {
            removed[1] = j;
            if (remove_count == 2) {
                if (ordinal++ % shards != static_cast<uint64_t>(shard)) continue;
                ++tested;
                {
                    const int covered = coverage_deleted(a, k, removed, remove_count);
                    if (covered > best_coverage) best_coverage = covered, best_removed = removed;
                    if (covered == (1 << k) - 1) goto found;
                }
                continue;
            }
            for (int l = j + 1; l < static_cast<int>(a.size()); ++l) {
                removed[2] = l;
                if (ordinal++ % shards != static_cast<uint64_t>(shard)) continue;
                ++tested;
                {
                    const int covered = coverage_deleted(a, k, removed, remove_count);
                    if (covered > best_coverage) best_coverage = covered, best_removed = removed;
                    if (covered == (1 << k) - 1) goto found;
                }
            }
        }
    }
    cerr << "NONE tested=" << tested << " best_coverage=" << best_coverage << '\n';
    if (emit_best) {
        for (int position = 0; position < static_cast<int>(a.size()); ++position) {
            bool skip = false;
            for (int i = 0; i < remove_count; ++i) skip |= position == best_removed[i];
            if (!skip) cout << a[position] << ' ';
        }
        cout << '\n';
    }
    return 1;

found:
    cerr << "FOUND removed:";
    for (int i = 0; i < remove_count; ++i) cerr << ' ' << removed[i];
    cerr << " tested=" << tested << '\n';
    for (int position = 0; position < static_cast<int>(a.size()); ++position) {
        bool skip = false;
        for (int i = 0; i < remove_count; ++i) skip |= position == removed[i];
        if (!skip) cout << a[position] << ' ';
    }
    cout << '\n';
    return 0;
}
