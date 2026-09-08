#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <algorithm>
#include <array>
#include <cstdint>
#include <iostream>
#include <vector>

using namespace std;

namespace {
constexpr int k = 14;
constexpr int limit = 1 << k;
constexpr int max_h = 10;
constexpr int max_join_colors = max_h * (max_h - 1) / 2;

struct JoinColors {
    array<uint16_t, max_join_colors> values{};
    uint8_t size = 0;
};
}  // namespace

int main(int argc, char** argv) {
    const int horizon = argc > 1 ? stoi(argv[1]) : 10;
    if (horizon != max_h) return 2;
    vector<int> input;
    for (int value; cin >> value;) input.push_back(value);
    if (input.empty()) return 3;

    vector<vector<int>> blocks;
    for (int first = 0; first < static_cast<int>(input.size());) {
        const int remaining = input.size() - first;
        const int length = remaining < 2 * horizon ? remaining : horizon;
        if (length < horizon) return 4;
        blocks.emplace_back(input.begin() + first, input.begin() + first + length);
        first += length;
    }
    const int block_count = blocks.size(), node_count = 2 * block_count;

    auto at = [&](int node, int position) {
        const int block = node >> 1;
        const bool reversed = node & 1;
        return reversed ? blocks[block][blocks[block].size() - 1 - position]
                        : blocks[block][position];
    };
    auto block_size = [&](int node) { return static_cast<int>(blocks[node >> 1].size()); };

    vector<JoinColors> joins(static_cast<size_t>(node_count) * node_count);
    for (int left = 0; left < node_count; ++left) {
        vector<int> suffix(horizon);
        int value = 0;
        for (int length = 1; length < horizon && length <= block_size(left); ++length) {
            value |= at(left, block_size(left) - length);
            suffix[length] = value;
        }
        for (int right = 0; right < node_count; ++right) {
            JoinColors& colors = joins[static_cast<size_t>(left) * node_count + right];
            vector<int> prefix(horizon);
            value = 0;
            for (int length = 1; length < horizon && length <= block_size(right); ++length) {
                value |= at(right, length - 1);
                prefix[length] = value;
            }
            for (int a = 1; a < horizon && a <= block_size(left); ++a)
                for (int b = 1; a + b <= horizon && b <= block_size(right); ++b)
                    colors.values[colors.size++] = suffix[a] | prefix[b];
        }
    }

    array<uint8_t, limit> internal{};
    for (const auto& block : blocks)
        for (int left = 0; left < static_cast<int>(block.size()); ++left) {
            int value = 0;
            for (int right = left; right < static_cast<int>(block.size()) &&
                 right - left + 1 <= horizon; ++right) {
                value |= block[right];
                internal[value] = 1;
            }
        }

    vector<int> order(block_count);
    for (int i = 0; i < block_count; ++i) order[i] = 2 * i;
    array<int, limit> boundary_count{};
    auto join = [&](int left, int right) -> const JoinColors& {
        return joins[static_cast<size_t>(left) * node_count + right];
    };
    auto recompute_boundary = [&]() {
        boundary_count.fill(0);
        for (int i = 0; i + 1 < block_count; ++i) {
            const JoinColors& colors = join(order[i], order[i + 1]);
            for (int p = 0; p < colors.size; ++p) ++boundary_count[colors.values[p]];
        }
    };
    recompute_boundary();

    array<uint8_t, limit> protected_color{};
    int covered = 0;
    for (int mask = 1; mask < limit; ++mask) {
        protected_color[mask] = internal[mask] || boundary_count[mask] > 0;
        covered += protected_color[mask];
    }

    // Audit that horizon-10 colors equal the complete coverage of the input.
    array<uint8_t, limit> exhaustive{};
    vector<int> previous, current;
    for (int value : input) {
        current.clear();
        current.push_back(value);
        for (int old : previous) {
            const int united = old | value;
            if (united != current.back()) current.push_back(united);
        }
        for (int united : current) exhaustive[united] = 1;
        previous.swap(current);
    }
    int exhaustive_covered = 0;
    for (int mask = 1; mask < limit; ++mask) exhaustive_covered += exhaustive[mask];
    if (covered != exhaustive_covered) {
        cerr << "horizon_audit_failed short=" << covered
             << " exhaustive=" << exhaustive_covered << '\n';
        return 5;
    }

    array<int, limit> delta{};
    array<uint8_t, limit> in_touched{};
    vector<int> touched;
    auto add_delta = [&](const JoinColors& colors, int amount) {
        for (int p = 0; p < colors.size; ++p) {
            const int mask = colors.values[p];
            if (!in_touched[mask]) {
                in_touched[mask] = 1;
                touched.push_back(mask);
            }
            delta[mask] += amount;
        }
    };

    cerr << "blocks=" << block_count << " horizon=" << horizon
         << " initial_covered=" << covered << '\n';
    int iteration = 0;
    while (covered < limit - 1) {
        int best_left = -1, best_right = -1, best_gain = 0;
        int best_fragility = 1 << 30;
        long long moves = 0, preserving = 0;
        for (int left = 0; left < block_count; ++left)
            for (int right = left; right < block_count; ++right) {
                if (left == 0 && right + 1 == block_count) continue;
                ++moves;
                touched.clear();
                if (left > 0) {
                    add_delta(join(order[left - 1], order[left]), -1);
                    add_delta(join(order[left - 1], order[right] ^ 1), +1);
                }
                if (right + 1 < block_count) {
                    add_delta(join(order[right], order[right + 1]), -1);
                    add_delta(join(order[left] ^ 1, order[right + 1]), +1);
                }
                bool valid = true;
                int gain = 0, fragility = 0;
                for (int mask : touched) {
                    const int next = boundary_count[mask] + delta[mask];
                    if (protected_color[mask] && !internal[mask] && next <= 0) {
                        valid = false;
                        break;
                    }
                    gain += !protected_color[mask] && next > 0;
                    fragility += protected_color[mask] && !internal[mask] && next == 1;
                }
                if (valid) {
                    ++preserving;
                    if (gain > best_gain || (gain == best_gain && gain > 0 &&
                                             fragility < best_fragility)) {
                        best_gain = gain;
                        best_fragility = fragility;
                        best_left = left;
                        best_right = right;
                    }
                }
                for (int mask : touched) {
                    delta[mask] = 0;
                    in_touched[mask] = 0;
                }
            }
        if (best_gain == 0) {
            cerr << "two_opt_frontier iteration=" << iteration
                 << " covered=" << covered << " moves=" << moves
                 << " preserving=" << preserving << '\n';
            break;
        }

        reverse(order.begin() + best_left, order.begin() + best_right + 1);
        for (int i = best_left; i <= best_right; ++i) order[i] ^= 1;
        recompute_boundary();
        const int before = covered;
        for (int mask = 1; mask < limit; ++mask)
            if (!protected_color[mask] && (internal[mask] || boundary_count[mask] > 0)) {
                protected_color[mask] = 1;
                ++covered;
            }
        ++iteration;
        cerr << "accept iteration=" << iteration << " segment=[" << best_left
             << ',' << best_right << "] gain=" << covered - before
             << " covered=" << covered << " fragility=" << best_fragility << '\n';
    }

    vector<int> output;
    output.reserve(input.size());
    for (int node : order)
        for (int i = 0; i < block_size(node); ++i) output.push_back(at(node, i));
    if (output.size() != input.size()) return 6;

    // Independent exhaustive suffix-OR audit of the final word.
    exhaustive.fill(0);
    previous.clear();
    for (int value : output) {
        current.clear();
        current.push_back(value);
        for (int old : previous) {
            const int united = old | value;
            if (united != current.back()) current.push_back(united);
        }
        for (int united : current) exhaustive[united] = 1;
        previous.swap(current);
    }
    exhaustive_covered = 0;
    for (int mask = 1; mask < limit; ++mask) exhaustive_covered += exhaustive[mask];
    cerr << "final_covered=" << exhaustive_covered << '/' << limit - 1 << '\n';
    if (exhaustive_covered < covered) return 7;

    for (int value : output) cout << value << ' ';
    cout << '\n';
    return 0;
}
