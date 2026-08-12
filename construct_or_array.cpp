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
#include <stdexcept>
#include <vector>

using namespace std;

static vector<int> lift_trimmed(vector<int> base, int from_k, int to_k) {
    for (int k = from_k; k < to_k; ++k) {
        const int high = 1 << k;
        vector<int> next;
        next.reserve(2 * base.size());
        next.insert(next.end(), base.begin(), base.end());
        next.push_back(high);
        // The final transformed entry high|base.back() is unnecessary.  If an
        // old mask has a witness ending at base.back(), its first-copy suffix
        // followed by [high] represents the corresponding high-bit mask.
        for (int i = 0; i + 1 < static_cast<int>(base.size()); ++i)
            next.push_back(high | base[i]);
        base.swap(next);
    }
    return base;
}

static vector<int> construct_nonzero(int k) {
    switch (k) {
        case 0: return {};
        case 1: return {1};
        case 2: return {1, 2};
        case 3: return {1, 2, 4, 1};
        case 4: return {1, 2, 4, 8, 1, 10, 5};
        case 5: return {1, 2, 4, 8, 16, 1, 18, 20, 5, 9, 10, 26};
        case 6: return {
            1, 6, 10, 3, 17, 20, 12, 36, 2, 33, 48,
            4, 18, 8, 5, 32, 24, 9, 40, 34, 16
        };
        case 7: return {
            42, 10, 18, 20, 68, 5, 36, 40, 24, 72, 2, 9, 24,
            12, 64, 36, 34, 16, 33, 40, 96, 66, 18, 17, 20, 48,
            96, 1, 66, 6, 8, 32, 3, 4, 9, 65, 80
        };
        case 8:
            return {
                2, 128, 36, 20, 18, 66, 1, 192, 4, 136, 32, 16, 9, 3,
                129, 160, 64, 4, 34, 1, 8, 36, 68, 80, 8, 144, 130, 66,
                96, 40, 1, 136, 4, 144, 2, 17, 48, 96, 72, 136, 129, 16,
                65, 72, 10, 130, 132, 1, 32, 144, 192, 68, 6, 1, 12, 24,
                48, 2, 64, 33, 5, 20, 18, 8, 64, 5, 16, 128, 34, 10, 4, 72
            };
        case 9:
            return {
                21, 132, 146, 50, 26, 1, 274, 20, 268, 320, 70, 134, 14,
                28, 48, 68, 336, 322, 65, 74, 76, 84, 17, 128, 37, 261,
                265, 272, 392, 32, 266, 259, 6, 69, 192, 36, 162, 258, 352,
                80, 448, 386, 385, 288, 9, 56, 168, 96, 416, 260, 140, 24,
                200, 264, 321, 289, 16, 161, 193, 256, 196, 8, 164, 176,
                400, 130, 19, 34, 52, 276, 273, 64, 280, 2, 152, 25, 4,
                49, 112, 98, 100, 33, 13, 137, 384, 10, 328, 40, 88, 18,
                67, 129, 35, 38, 292, 324, 5, 73, 136, 41, 11, 7, 22, 82,
                194, 138, 131, 133, 257, 144, 81, 72, 97, 3, 290, 304,
                296, 44, 104, 66, 224, 208, 148, 388, 262, 12, 42, 160
            };
        case 10:
            return {
                116, 101, 97, 577, 515, 521, 529, 769, 261, 133,
                193, 96, 49, 56, 536, 784, 400, 274, 304, 352,
                321, 448, 896, 648, 140, 148, 145, 161, 641, 137,
                392, 152, 138, 14, 522, 578, 82, 322, 259, 7,
                37, 13, 76, 524, 28, 10, 5, 134, 644, 196,
                384, 224, 168, 162, 176, 164, 136, 416, 800, 608,
                98, 80, 22, 146, 19, 35, 41, 520, 265, 268,
                136, 6, 160, 388, 276, 280, 273, 65, 832, 324,
                292, 44, 520, 517, 514, 259, 272, 385, 289, 36,
                768, 560, 656, 532, 84, 70, 320, 290, 386, 131,
                132, 33, 13, 264, 68, 200, 704, 208, 194, 34,
                67, 81, 88, 192, 336, 324, 5, 288, 49, 18,
                513, 592, 584, 552, 514, 24, 640, 17, 516, 69,
                66, 11, 266, 770, 320, 130, 18, 72, 20, 196,
                129, 704, 96, 528, 545, 257, 576, 776, 772, 258,
                642, 3, 136, 74, 12, 262, 38, 518, 578, 320,
                1, 290, 296, 272, 12, 512, 21, 52, 50, 42,
                104, 73, 136, 133, 516, 33, 546, 288, 640, 260,
                528, 580, 544, 8, 577, 192, 17, 130, 530, 34,
                256, 52, 112, 144, 40, 672, 132, 100, 2, 65,
                20, 25, 32, 265, 328, 392, 130, 520, 192, 96,
                44, 2, 548, 52, 24, 96, 328, 258, 26, 17,
                137, 32, 257, 640, 784, 64, 280, 4, 258, 9,
                129, 162, 512, 194, 65, 384, 272, 5, 18, 516,
                640, 34, 8, 384, 48, 64, 800, 8, 770, 16,
                262, 128, 198, 197
            };
        case 11:
            return {
#include "k11_completed_477.inc"
            };
        case 12:
            return {
#include "k12_optimal_nonzero.inc"
            };
        case 14:
            return {
#include "k14_completed_3676.inc"
            };
        default:
            break;
    }

    if (k == 13) return lift_trimmed(construct_nonzero(12), 12, 13);
    // The cross-seam-completed k=14 factor is the strongest stored base for
    // k>=15.
    return lift_trimmed(construct_nonzero(14), 14, k);
}

static bool covers_nonzero(int k, const vector<int>& values) {
    const int count = 1 << k;
    vector<uint8_t> seen(count);
    array<int, 32> previous{}, current{};
    int previous_size = 0;
    for (int value : values) {
        if (value <= 0 || value >= count) return false;
        int current_size = 0;
        current[current_size++] = value;
        for (int i = 0; i < previous_size; ++i) {
            const int next = previous[i] | value;
            if (next != current[current_size - 1]) current[current_size++] = next;
        }
        for (int i = 0; i < current_size; ++i) seen[current[i]] = true;
        swap(previous, current);
        previous_size = current_size;
    }
    return all_of(seen.begin() + 1, seen.end(), [](uint8_t x) { return x; });
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int k;
    if (!(cin >> k) || k < 0 || k >= 20)
        throw invalid_argument("k must satisfy 0 <= k < 20");

    vector<int> nonzero = construct_nonzero(k);
    if (!covers_nonzero(k, nonzero)) throw runtime_error("construction verification failed");

    cout << nonzero.size() + 1 << '\n' << 0;
    for (int value : nonzero) cout << ' ' << value;
    cout << '\n';
}
