#include <algorithm>
#include <array>
#include <bit>
#include <cassert>
#include <chrono>
#include <cstdint>
#include <iostream>
#include <numeric>
#include <thread>
#include <vector>

namespace {

constexpr int B = 11;
constexpr int R = 5;
constexpr int MASKS = 1 << B;
constexpr int MIDDLE_COUNT = 462;
constexpr int LOWER_COUNT = 330;
constexpr int TARGET_COUNT = MIDDLE_COUNT + LOWER_COUNT;
constexpr int Q_COUNT = 165;
constexpr int B_ROWS = 2 * TARGET_COUNT;
constexpr int STACKED_ROWS = B_ROWS + Q_COUNT;
constexpr int ORBIT_COLUMNS = 4000;
constexpr std::int64_t FACTORIAL_B = 39916800;
constexpr std::int64_t LEHMER_STEP = 7919;

using Word = std::array<std::uint8_t, B>;
using Exposure = std::array<std::int64_t, TARGET_COUNT>;

std::array<int, MASKS> middle_id;
std::array<int, MASKS> lower_id;
std::array<int, MASKS> q_id;
std::vector<int> middle_masks;
std::vector<int> lower_masks;
std::vector<int> q_masks;
std::array<bool, TARGET_COUNT> base_incidence{};
std::array<bool, Q_COUNT> base_q{};

std::vector<int> masks_of_size(int size) {
    std::vector<int> out;
    for (int mask = 0; mask < MASKS; ++mask) {
        if (std::popcount(static_cast<unsigned>(mask)) == size) out.push_back(mask);
    }
    return out;
}

int interval_mask(const Word& word, int start, int length) {
    int mask = 0;
    for (int offset = 0; offset < length; ++offset) {
        mask |= 1 << word[(start + offset) % B];
    }
    return mask;
}

void retained_ids(const Word& word,
                  std::array<int, B - 1>& middle,
                  std::array<int, B - 1>& lower) {
    int middle_mask = interval_mask(word, 0, R);
    int lower_mask = interval_mask(word, 0, R - 1);
    for (int start = 1; start < B; ++start) {
        middle_mask ^= 1 << word[start - 1];
        middle_mask ^= 1 << word[(start + R - 1) % B];
        lower_mask ^= 1 << word[start - 1];
        lower_mask ^= 1 << word[(start + R - 2) % B];
        middle[start - 1] = middle_id[middle_mask];
        lower[start - 1] = lower_id[lower_mask];
        assert(middle[start - 1] >= 0 && lower[start - 1] >= 0);
    }
}

Exposure exposure_for_first_label(int first, std::uint64_t& permutation_count,
                                  std::array<std::uint64_t, 21>& overlap_histogram) {
    Exposure exposure{};
    std::array<std::uint8_t, B - 1> tail{};
    int cursor = 0;
    for (int label = 0; label < B; ++label) {
        if (label != first) tail[cursor++] = static_cast<std::uint8_t>(label);
    }
    std::array<int, B - 1> middle{};
    std::array<int, B - 1> lower{};
    do {
        ++permutation_count;
        Word word{};
        word[0] = static_cast<std::uint8_t>(first);
        std::copy(tail.begin(), tail.end(), word.begin() + 1);
        retained_ids(word, middle, lower);
        int overlap = 0;
        for (int id : middle) overlap += base_incidence[id];
        for (int id : lower) overlap += base_incidence[MIDDLE_COUNT + id];
        ++overlap_histogram[overlap];
        const int duplicate = std::max(0, overlap - 1);
        if (duplicate) {
            for (int id : middle) exposure[id] += duplicate;
            for (int id : lower) exposure[MIDDLE_COUNT + id] += duplicate;
        }
    } while (std::next_permutation(tail.begin(), tail.end()));
    return exposure;
}

int permute_mask(int mask, const Word& relabelling) {
    int image = 0;
    while (mask) {
        const int bit = std::countr_zero(static_cast<unsigned>(mask));
        image |= 1 << relabelling[bit];
        mask &= mask - 1;
    }
    return image;
}

Word lehmer_unrank(std::int64_t index) {
    static constexpr std::array<std::int64_t, B + 1> factorial = {
        1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800
    };
    std::vector<std::uint8_t> pool(B);
    std::iota(pool.begin(), pool.end(), 0);
    Word word{};
    for (int position = 0; position < B; ++position) {
        const int remaining = B - position;
        const auto block = factorial[remaining - 1];
        const auto quotient = static_cast<std::size_t>(index / block);
        index %= block;
        assert(quotient < pool.size());
        word[position] = pool[quotient];
        pool.erase(pool.begin() + static_cast<std::ptrdiff_t>(quotient));
    }
    return word;
}

struct TernaryRow {
    std::vector<std::uint64_t> one;
    std::vector<std::uint64_t> two;
};

void set_entry(TernaryRow& row, int column, int value) {
    value %= 3;
    if (value < 0) value += 3;
    const std::uint64_t bit = std::uint64_t{1} << (column & 63);
    if (value == 1) row.one[column >> 6] |= bit;
    if (value == 2) row.two[column >> 6] |= bit;
}

int entry(const TernaryRow& row, int column) {
    const std::uint64_t bit = std::uint64_t{1} << (column & 63);
    if (row.one[column >> 6] & bit) return 1;
    if (row.two[column >> 6] & bit) return 2;
    return 0;
}

void multiply_by_two(TernaryRow& row) {
    row.one.swap(row.two);
}

void add_ternary(TernaryRow& target, const TernaryRow& source,
                 bool subtract_source, std::uint64_t final_mask) {
    const std::size_t words = target.one.size();
    for (std::size_t i = 0; i < words; ++i) {
        const std::uint64_t valid = (i + 1 == words) ? final_mask : ~std::uint64_t{0};
        const std::uint64_t a1 = target.one[i];
        const std::uint64_t a2 = target.two[i];
        const std::uint64_t source1 = source.one[i];
        const std::uint64_t source2 = source.two[i];
        const std::uint64_t b1 = subtract_source ? source2 : source1;
        const std::uint64_t b2 = subtract_source ? source1 : source2;
        const std::uint64_t a0 = ~(a1 | a2) & valid;
        const std::uint64_t b0 = ~(b1 | b2) & valid;
        target.one[i] = ((a1 & b0) | (a0 & b1) | (a2 & b2)) & valid;
        target.two[i] = ((a2 & b0) | (a0 & b2) | (a1 & b1)) & valid;
    }
}

int rank_mod_three(std::vector<TernaryRow> rows, int columns) {
    const std::uint64_t final_mask = (columns & 63)
        ? ((std::uint64_t{1} << (columns & 63)) - 1)
        : ~std::uint64_t{0};
    int pivot_row = 0;
    for (int column = 0; column < columns && pivot_row < static_cast<int>(rows.size());
         ++column) {
        int selected = pivot_row;
        while (selected < static_cast<int>(rows.size()) && !entry(rows[selected], column)) {
            ++selected;
        }
        if (selected == static_cast<int>(rows.size())) continue;
        std::swap(rows[pivot_row], rows[selected]);
        if (entry(rows[pivot_row], column) == 2) multiply_by_two(rows[pivot_row]);
        assert(entry(rows[pivot_row], column) == 1);
        for (int row = pivot_row + 1; row < static_cast<int>(rows.size()); ++row) {
            const int factor = entry(rows[row], column);
            if (factor == 1) {
                add_ternary(rows[row], rows[pivot_row], true, final_mask);
            } else if (factor == 2) {
                add_ternary(rows[row], rows[pivot_row], false, final_mask);
            }
            assert(entry(rows[row], column) == 0);
        }
        ++pivot_row;
    }
    return pivot_row;
}

int scalar_rank_mod_three(std::vector<std::vector<int>> matrix) {
    if (matrix.empty()) return 0;
    const int rows = static_cast<int>(matrix.size());
    const int columns = static_cast<int>(matrix.front().size());
    int pivot_row = 0;
    for (int column = 0; column < columns && pivot_row < rows; ++column) {
        int selected = pivot_row;
        while (selected < rows && matrix[selected][column] % 3 == 0) ++selected;
        if (selected == rows) continue;
        std::swap(matrix[pivot_row], matrix[selected]);
        if (matrix[pivot_row][column] % 3 == 2) {
            for (int& value : matrix[pivot_row]) value = (2 * value) % 3;
        }
        for (int row = pivot_row + 1; row < rows; ++row) {
            const int factor = matrix[row][column] % 3;
            for (int j = column; factor && j < columns; ++j) {
                matrix[row][j] = (matrix[row][j] - factor * matrix[pivot_row][j]) % 3;
                if (matrix[row][j] < 0) matrix[row][j] += 3;
            }
        }
        ++pivot_row;
    }
    return pivot_row;
}

void rank_engine_self_test() {
    std::uint64_t state = 20260822;
    for (int rows = 1; rows <= 12; ++rows) {
        for (int columns = 1; columns <= 15; ++columns) {
            std::vector<std::vector<int>> scalar(rows, std::vector<int>(columns));
            const int words = (columns + 63) / 64;
            std::vector<TernaryRow> packed(rows);
            for (auto& row : packed) {
                row.one.assign(words, 0);
                row.two.assign(words, 0);
            }
            for (int i = 0; i < rows; ++i) {
                for (int j = 0; j < columns; ++j) {
                    state = state * 6364136223846793005ULL + 1442695040888963407ULL;
                    scalar[i][j] = static_cast<int>((state >> 32) % 3);
                    set_entry(packed[i], j, scalar[i][j]);
                }
            }
            assert(rank_mod_three(packed, columns) == scalar_rank_mod_three(scalar));
        }
    }
}

std::pair<int, int> shallow_rank_test(
    int shallow_size, const Word& identity, const std::vector<Word>& relabellings,
    const std::vector<TernaryRow>& b_rows, int words_per_row) {
    const std::vector<int> target_masks = masks_of_size(shallow_size);
    std::array<int, MASKS> target_id{};
    target_id.fill(-1);
    for (int i = 0; i < static_cast<int>(target_masks.size()); ++i) {
        target_id[target_masks[i]] = i;
    }
    std::vector<bool> base_deck(target_masks.size(), false);
    for (int start = 0; start < B; ++start) {
        base_deck[target_id[interval_mask(identity, start, shallow_size)]] = true;
    }
    std::vector<TernaryRow> q_rows(target_masks.size());
    for (auto& row : q_rows) {
        row.one.assign(words_per_row, 0);
        row.two.assign(words_per_row, 0);
    }
    for (int column = 0; column < static_cast<int>(relabellings.size()); ++column) {
        for (int source = 0; source < static_cast<int>(target_masks.size()); ++source) {
            if (!base_deck[source]) continue;
            const int image = target_id[permute_mask(
                target_masks[source], relabellings[column])];
            set_entry(q_rows[image], column, 1);
        }
    }
    std::vector<TernaryRow> combined = b_rows;
    combined.insert(combined.end(), q_rows.begin(), q_rows.end());
    return {
        rank_mod_three(q_rows, static_cast<int>(relabellings.size())),
        rank_mod_three(combined, static_cast<int>(relabellings.size()))
    };
}

}  // namespace

int main() {
    const auto started = std::chrono::steady_clock::now();
    rank_engine_self_test();
    middle_id.fill(-1);
    lower_id.fill(-1);
    q_id.fill(-1);
    middle_masks = masks_of_size(R);
    lower_masks = masks_of_size(R - 1);
    q_masks = masks_of_size(R - 2);
    assert(static_cast<int>(middle_masks.size()) == MIDDLE_COUNT);
    assert(static_cast<int>(lower_masks.size()) == LOWER_COUNT);
    assert(static_cast<int>(q_masks.size()) == Q_COUNT);
    for (int i = 0; i < MIDDLE_COUNT; ++i) middle_id[middle_masks[i]] = i;
    for (int i = 0; i < LOWER_COUNT; ++i) lower_id[lower_masks[i]] = i;
    for (int i = 0; i < Q_COUNT; ++i) q_id[q_masks[i]] = i;

    Word identity{};
    std::iota(identity.begin(), identity.end(), 0);
    std::array<int, B - 1> base_middle{};
    std::array<int, B - 1> base_lower{};
    retained_ids(identity, base_middle, base_lower);
    for (int id : base_middle) base_incidence[id] = true;
    for (int id : base_lower) base_incidence[MIDDLE_COUNT + id] = true;
    for (int start = 0; start < B; ++start) {
        base_q[q_id[interval_mask(identity, start, R - 2)]] = true;
    }

    std::array<Exposure, B> partial{};
    std::array<std::uint64_t, B> partial_counts{};
    std::array<std::array<std::uint64_t, 21>, B> partial_histograms{};
    std::vector<std::thread> workers;
    for (int first = 0; first < B; ++first) {
        workers.emplace_back([first, &partial, &partial_counts, &partial_histograms] {
            partial[first] = exposure_for_first_label(
                first, partial_counts[first], partial_histograms[first]);
        });
    }
    for (auto& worker : workers) worker.join();
    assert(std::accumulate(partial_counts.begin(), partial_counts.end(),
                           std::uint64_t{0}) == FACTORIAL_B);
    for (auto count : partial_counts) assert(count == 3628800);
    std::array<std::uint64_t, 21> overlap_histogram{};
    for (const auto& local : partial_histograms) {
        for (int overlap = 0; overlap <= 20; ++overlap) {
            overlap_histogram[overlap] += local[overlap];
        }
    }
    constexpr std::array<std::uint64_t, 21> expected_histogram = {
        29094585, 5542849, 2616794, 1432981, 769080, 291672, 105751,
        37412, 13419, 6187, 3259, 1235, 873, 298, 231, 90, 50, 10, 21, 2, 1
    };
    assert(overlap_histogram == expected_histogram);
    Exposure exposure{};
    for (const auto& local : partial) {
        for (int i = 0; i < TARGET_COUNT; ++i) exposure[i] += local[i];
    }

    const auto middle_sum = std::accumulate(exposure.begin(),
                                            exposure.begin() + MIDDLE_COUNT,
                                            std::int64_t{0});
    const auto lower_sum = std::accumulate(exposure.begin() + MIDDLE_COUNT,
                                           exposure.end(), std::int64_t{0});
    assert(middle_sum == lower_sum);
    assert(middle_sum % (B - 1) == 0);
    const auto d_zero = middle_sum / (B - 1);
    assert(d_zero > 0);
    std::int64_t d_zero_from_histogram = 0;
    for (int overlap = 2; overlap <= 20; ++overlap) {
        d_zero_from_histogram += static_cast<std::int64_t>(overlap_histogram[overlap])
                               * (overlap - 1);
    }
    assert(d_zero_from_histogram == d_zero);
    constexpr std::int64_t CHECK_MOD = 1000000007;
    std::int64_t weighted_checksum = 0;
    std::int64_t square_checksum = 0;
    for (int i = 0; i < TARGET_COUNT; ++i) {
        weighted_checksum = (weighted_checksum
            + ((i + 1LL) * (exposure[i] % CHECK_MOD)) % CHECK_MOD) % CHECK_MOD;
        square_checksum = (square_checksum
            + ((exposure[i] % CHECK_MOD) * (exposure[i] % CHECK_MOD)) % CHECK_MOD)
            % CHECK_MOD;
    }
    assert(d_zero == 9913785);
    assert(middle_sum == 99137850);
    assert(*std::max_element(exposure.begin(), exposure.end()) == 1919808);
    assert(weighted_checksum == 408475218);
    assert(square_checksum == 915177100);

    const int words_per_row = (ORBIT_COLUMNS + 63) / 64;
    std::vector<TernaryRow> stacked(STACKED_ROWS);
    for (auto& row : stacked) {
        row.one.assign(words_per_row, 0);
        row.two.assign(words_per_row, 0);
    }
    std::vector<Word> used;
    used.reserve(ORBIT_COLUMNS);
    for (int column = 0; column < ORBIT_COLUMNS; ++column) {
        const auto index = (LEHMER_STEP * column) % FACTORIAL_B;
        const Word relabelling = lehmer_unrank(index);
        assert(std::find(used.begin(), used.end(), relabelling) == used.end());
        used.push_back(relabelling);

        for (int source = 0; source < MIDDLE_COUNT; ++source) {
            const int image = middle_id[permute_mask(middle_masks[source], relabelling)];
            if (base_incidence[source]) set_entry(stacked[image], column, 1);
            set_entry(stacked[TARGET_COUNT + image], column,
                      static_cast<int>(exposure[source] % 3));
        }
        for (int source = 0; source < LOWER_COUNT; ++source) {
            const int image_local = lower_id[permute_mask(lower_masks[source], relabelling)];
            const int source_global = MIDDLE_COUNT + source;
            const int image_global = MIDDLE_COUNT + image_local;
            if (base_incidence[source_global]) set_entry(stacked[image_global], column, 1);
            set_entry(stacked[TARGET_COUNT + image_global], column,
                      static_cast<int>(exposure[source_global] % 3));
        }
        for (int source = 0; source < Q_COUNT; ++source) {
            const int image = q_id[permute_mask(q_masks[source], relabelling)];
            if (base_q[source]) set_entry(stacked[B_ROWS + image], column, 1);
        }
    }

    std::vector<TernaryRow> b_rows(stacked.begin(), stacked.begin() + B_ROWS);
    std::vector<TernaryRow> q_rows(stacked.begin() + B_ROWS, stacked.end());
    const int rank_b = rank_mod_three(b_rows, ORBIT_COLUMNS);
    const int rank_q = rank_mod_three(q_rows, ORBIT_COLUMNS);
    const int rank_stacked = rank_mod_three(stacked, ORBIT_COLUMNS);
    const auto [rank_q2, rank_stacked_q2] = shallow_rank_test(
        2, identity, used, b_rows, words_per_row);
    const auto [rank_q4, rank_stacked_q4] = shallow_rank_test(
        4, identity, used, b_rows, words_per_row);

    const auto elapsed = std::chrono::duration<double>(
        std::chrono::steady_clock::now() - started).count();
    std::cout << "r=5 base exposure: D0=" << d_zero
              << " middle_sum=" << middle_sum
              << " max=" << *std::max_element(exposure.begin(), exposure.end())
              << " checksums=" << weighted_checksum << ',' << square_checksum << '\n';
    std::cout << "overlap_histogram:";
    for (int overlap = 0; overlap <= 20; ++overlap) {
        if (overlap_histogram[overlap]) {
            std::cout << ' ' << overlap << ':' << overlap_histogram[overlap];
        }
    }
    std::cout << '\n';
    std::cout << "ranks over F_3: B=" << rank_b << " Q=" << rank_q
              << " stacked=" << rank_stacked << '\n';
    std::cout << "extra shallow ranks over F_3: k=2 Q=" << rank_q2
              << " stacked=" << rank_stacked_q2
              << "; k=4 Q=" << rank_q4
              << " stacked=" << rank_stacked_q4 << '\n';
    std::cout << "elapsed_seconds=" << elapsed << '\n';

    assert(rank_b == 1581);
    assert(rank_q == 155);
    assert(rank_stacked == 1735);
    assert(rank_q2 == 45);
    assert(rank_stacked_q2 == 1625);
    assert(rank_q4 == 320);
    assert(rank_stacked_q4 == 1900);
    std::cout << "PASS complete r=5 compensated q=2 rank certificate: "
              << "rank(B)=1581, rank(Q3)=155, rank([B;Q3])=1735, "
              << "and full balanced images at k=2,3,4\n";
}
