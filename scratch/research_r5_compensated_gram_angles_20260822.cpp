#if defined(__clang__)
#pragma clang diagnostic push
#pragma clang diagnostic ignored "-Wreturn-type"
#endif
#define main complete_r5_rank_certificate_main
#include "verify_complete_r5_compensated_q2_surjectivity_20260822.cpp"
#undef main
#if defined(__clang__)
#pragma clang diagnostic pop
#endif

#include <cmath>
#include <iomanip>
#include <gmpxx.h>

namespace {

int harmonic_value(int mask, int level) {
    int value = 1;
    for (int pair = 0; pair < level; ++pair) {
        const int first = (mask >> (2 * pair)) & 1;
        const int second = (mask >> (2 * pair + 1)) & 1;
        value *= first - second;
    }
    return value;
}

struct CoefficientVector {
    int size;
    std::vector<int> masks;
    std::vector<long double> coefficient;
};

Exposure second_moment_for_first_label(int first) {
    Exposure second{};
    std::array<std::uint8_t, B - 1> tail{};
    int cursor = 0;
    for (int label = 0; label < B; ++label) {
        if (label != first) tail[cursor++] = static_cast<std::uint8_t>(label);
    }
    std::array<int, B - 1> middle{};
    std::array<int, B - 1> lower{};
    do {
        Word word{};
        word[0] = static_cast<std::uint8_t>(first);
        std::copy(tail.begin(), tail.end(), word.begin() + 1);
        retained_ids(word, middle, lower);
        int overlap = 0;
        for (int id : middle) overlap += base_incidence[id];
        for (int id : lower) overlap += base_incidence[MIDDLE_COUNT + id];
        const int weight = overlap * (overlap - 1) / 2;
        if (weight) {
            for (int id : middle) second[id] += weight;
            for (int id : lower) second[MIDDLE_COUNT + id] += weight;
        }
    } while (std::next_permutation(tail.begin(), tail.end()));
    return second;
}

std::vector<long double> overlap_kernel(int left_size, int right_size,
                                        int level) {
    const auto left = masks_of_size(left_size);
    const auto right = masks_of_size(right_size);
    const int max_overlap = std::min(left_size, right_size);
    std::vector<long double> sums(max_overlap + 1, 0.0L);
    std::vector<std::uint64_t> counts(max_overlap + 1, 0);
    for (int left_mask : left) {
        const int left_value = harmonic_value(left_mask, level);
        for (int right_mask : right) {
            const int overlap = std::popcount(
                static_cast<unsigned>(left_mask & right_mask));
            sums[overlap] += static_cast<long double>(
                left_value * harmonic_value(right_mask, level));
            ++counts[overlap];
        }
    }
    for (int overlap = 0; overlap <= max_overlap; ++overlap) {
        assert(counts[overlap] > 0);
        sums[overlap] /= static_cast<long double>(counts[overlap]);
    }
    return sums;
}

long double gram_entry(const CoefficientVector& left,
                       const CoefficientVector& right, int level) {
    const auto kernel = overlap_kernel(left.size, right.size, level);
    long double answer = 0.0L;
    for (int i = 0; i < static_cast<int>(left.masks.size()); ++i) {
        if (left.coefficient[i] == 0.0L) continue;
        for (int j = 0; j < static_cast<int>(right.masks.size()); ++j) {
            if (right.coefficient[j] == 0.0L) continue;
            const int overlap = std::popcount(static_cast<unsigned>(
                left.masks[i] & right.masks[j]));
            answer += left.coefficient[i] * right.coefficient[j]
                    * kernel[overlap];
        }
    }
    return answer;
}

long double residual_fraction(
    const std::array<std::array<long double, 5>, 5>& gram) {
    std::array<std::array<long double, 5>, 5> correlation{};
    for (int row = 0; row < 5; ++row) {
        assert(gram[row][row] > 0.0L);
        for (int column = 0; column < 5; ++column) {
            correlation[row][column] = gram[row][column]
                / std::sqrt(gram[row][row] * gram[column][column]);
        }
    }
    std::array<std::array<long double, 5>, 4> augmented{};
    for (int row = 0; row < 4; ++row) {
        for (int column = 0; column < 4; ++column) {
            augmented[row][column] = correlation[row][column];
        }
        augmented[row][4] = correlation[row][4];
    }
    for (int column = 0; column < 4; ++column) {
        int pivot = column;
        for (int row = column + 1; row < 4; ++row) {
            if (std::abs(augmented[row][column])
                > std::abs(augmented[pivot][column])) pivot = row;
        }
        assert(std::abs(augmented[pivot][column]) > 1.0e-30L);
        std::swap(augmented[pivot], augmented[column]);
        const long double divisor = augmented[column][column];
        for (int entry = column; entry <= 4; ++entry) {
            augmented[column][entry] /= divisor;
        }
        for (int row = 0; row < 4; ++row) {
            if (row == column) continue;
            const long double multiple = augmented[row][column];
            for (int entry = column; entry <= 4; ++entry) {
                augmented[row][entry] -= multiple * augmented[column][entry];
            }
        }
    }
    long double projection = 0.0L;
    for (int row = 0; row < 4; ++row) {
        projection += correlation[4][row] * augmented[row][4];
    }
    return 1.0L - projection;
}

mpq_class exact_gram_entry(const CoefficientVector& left,
                           const CoefficientVector& right, int level) {
    const int max_overlap = std::min(left.size, right.size);
    std::vector<std::int64_t> harmonic_sum(max_overlap + 1, 0);
    std::vector<std::uint64_t> count(max_overlap + 1, 0);
    for (int left_mask : left.masks) {
        for (int right_mask : right.masks) {
            const int overlap = std::popcount(static_cast<unsigned>(
                left_mask & right_mask));
            harmonic_sum[overlap] += harmonic_value(left_mask, level)
                                      * harmonic_value(right_mask, level);
            ++count[overlap];
        }
    }
    std::vector<mpz_class> weighted(max_overlap + 1);
    for (int i = 0; i < static_cast<int>(left.masks.size()); ++i) {
        if (left.coefficient[i] == 0.0L) continue;
        const auto left_value = static_cast<std::int64_t>(left.coefficient[i]);
        assert(static_cast<long double>(left_value) == left.coefficient[i]);
        for (int j = 0; j < static_cast<int>(right.masks.size()); ++j) {
            if (right.coefficient[j] == 0.0L) continue;
            const auto right_value = static_cast<std::int64_t>(right.coefficient[j]);
            assert(static_cast<long double>(right_value) == right.coefficient[j]);
            const int overlap = std::popcount(static_cast<unsigned>(
                left.masks[i] & right.masks[j]));
            weighted[overlap] += mpz_class(static_cast<long>(left_value))
                               * static_cast<long>(right_value);
        }
    }
    mpq_class answer = 0;
    for (int overlap = 0; overlap <= max_overlap; ++overlap) {
        answer += mpq_class(
            weighted[overlap] * static_cast<long>(harmonic_sum[overlap]),
            mpz_class(static_cast<unsigned long>(count[overlap])));
    }
    return answer;
}

mpq_class exact_residual_fraction(
    const std::array<std::array<mpq_class, 5>, 5>& gram) {
    std::array<std::array<mpq_class, 5>, 4> matrix{};
    for (int row = 0; row < 4; ++row) {
        for (int column = 0; column < 4; ++column) {
            matrix[row][column] = gram[row][column];
        }
        matrix[row][4] = gram[row][4];
    }
    for (int column = 0; column < 4; ++column) {
        int pivot = column;
        while (pivot < 4 && matrix[pivot][column] == 0) ++pivot;
        assert(pivot < 4);
        std::swap(matrix[pivot], matrix[column]);
        const mpq_class divisor = matrix[column][column];
        for (int entry = column; entry <= 4; ++entry) {
            matrix[column][entry] /= divisor;
        }
        for (int row = 0; row < 4; ++row) {
            if (row == column) continue;
            const mpq_class multiple = matrix[row][column];
            for (int entry = column; entry <= 4; ++entry) {
                matrix[row][entry] -= multiple * matrix[column][entry];
            }
        }
    }
    mpq_class projection = 0;
    for (int row = 0; row < 4; ++row) {
        projection += gram[4][row] * matrix[row][4];
    }
    return 1 - projection / gram[4][4];
}

}  // namespace

int main() {
    middle_id.fill(-1);
    lower_id.fill(-1);
    q_id.fill(-1);
    middle_masks = masks_of_size(R);
    lower_masks = masks_of_size(R - 1);
    q_masks = masks_of_size(R - 2);
    for (int i = 0; i < MIDDLE_COUNT; ++i) middle_id[middle_masks[i]] = i;
    for (int i = 0; i < LOWER_COUNT; ++i) lower_id[lower_masks[i]] = i;
    for (int i = 0; i < Q_COUNT; ++i) q_id[q_masks[i]] = i;

    Word identity{};
    std::iota(identity.begin(), identity.end(), 0);
    std::array<int, B - 1> base_middle{};
    std::array<int, B - 1> base_lower{};
    retained_ids(identity, base_middle, base_lower);
    base_incidence.fill(false);
    for (int id : base_middle) base_incidence[id] = true;
    for (int id : base_lower) base_incidence[MIDDLE_COUNT + id] = true;

    std::array<Exposure, B> partial{};
    std::array<std::uint64_t, B> counts{};
    std::array<std::array<std::uint64_t, 21>, B> histograms{};
    std::vector<std::thread> workers;
    for (int first = 0; first < B; ++first) {
        workers.emplace_back([first, &partial, &counts, &histograms] {
            partial[first] = exposure_for_first_label(
                first, counts[first], histograms[first]);
        });
    }
    for (auto& worker : workers) worker.join();
    Exposure exposure{};
    for (const auto& local : partial) {
        for (int i = 0; i < TARGET_COUNT; ++i) exposure[i] += local[i];
    }
    std::array<Exposure, B> second_partial{};
    workers.clear();
    for (int first = 0; first < B; ++first) {
        workers.emplace_back([first, &second_partial] {
            second_partial[first] = second_moment_for_first_label(first);
        });
    }
    for (auto& worker : workers) worker.join();
    Exposure second{};
    for (const auto& local : second_partial) {
        for (int i = 0; i < TARGET_COUNT; ++i) second[i] += local[i];
    }

    CoefficientVector middle_incidence{R, middle_masks,
        std::vector<long double>(MIDDLE_COUNT, 0.0L)};
    CoefficientVector lower_incidence{R - 1, lower_masks,
        std::vector<long double>(LOWER_COUNT, 0.0L)};
    CoefficientVector middle_exposure{R, middle_masks,
        std::vector<long double>(MIDDLE_COUNT, 0.0L)};
    CoefficientVector lower_exposure{R - 1, lower_masks,
        std::vector<long double>(LOWER_COUNT, 0.0L)};
    CoefficientVector shallow{R - 2, q_masks,
        std::vector<long double>(Q_COUNT, 0.0L)};

    for (int id : base_middle) middle_incidence.coefficient[id] = 1.0L;
    for (int id : base_lower) lower_incidence.coefficient[id] = 1.0L;
    for (int i = 0; i < MIDDLE_COUNT; ++i) {
        middle_exposure.coefficient[i] = exposure[i];
    }
    for (int i = 0; i < LOWER_COUNT; ++i) {
        lower_exposure.coefficient[i] = exposure[MIDDLE_COUNT + i];
    }
    for (int start = 0; start < B; ++start) {
        shallow.coefficient[q_id[interval_mask(identity, start, R - 2)]] = 1.0L;
    }
    const std::array<CoefficientVector, 5> vectors = {
        middle_incidence, lower_incidence,
        middle_exposure, lower_exposure, shallow
    };
    CoefficientVector middle_second{R, middle_masks,
        std::vector<long double>(MIDDLE_COUNT, 0.0L)};
    CoefficientVector lower_second{R - 1, lower_masks,
        std::vector<long double>(LOWER_COUNT, 0.0L)};
    for (int i = 0; i < MIDDLE_COUNT; ++i) {
        middle_second.coefficient[i] = second[i];
    }
    for (int i = 0; i < LOWER_COUNT; ++i) {
        lower_second.coefficient[i] = second[MIDDLE_COUNT + i];
    }
    const std::array<CoefficientVector, 5> second_vectors = {
        middle_incidence, lower_incidence,
        middle_second, lower_second, shallow
    };

    std::cout << std::setprecision(18);
    for (int level = 2; level <= R - 2; ++level) {
        std::array<std::array<long double, 5>, 5> gram{};
        for (int i = 0; i < 5; ++i) {
            for (int j = 0; j < 5; ++j) {
                gram[i][j] = gram_entry(vectors[i], vectors[j], level);
            }
        }
        std::cout << "diagonal";
        for (int i = 0; i < 5; ++i) std::cout << ' ' << gram[i][i];
        std::cout << '\n';
        std::cout << "r=5 k=3 j=" << level
                  << " alpha=" << residual_fraction(gram) << '\n';
        std::array<std::array<mpq_class, 5>, 5> exact_gram{};
        for (int i = 0; i < 5; ++i) {
            for (int j = 0; j < 5; ++j) {
                exact_gram[i][j] = exact_gram_entry(vectors[i], vectors[j], level);
            }
        }
        const mpq_class exact_alpha = exact_residual_fraction(exact_gram);
        const mpq_class expected = level == 2
            ? mpq_class("25610183932380883339249166148/"
                        "280256277166865583655644272238")
            : mpq_class("2824584316655122245743670177/"
                        "5429668689045287473387817249");
        assert(exact_alpha == expected);
        const mpq_class relative_eigenvalue = exact_alpha
            * (level == 2 ? mpq_class(180, 7) : mpq_class(75, 7));
        const mpq_class expected_eigenvalue = level == 2
            ? mpq_class("109757931138775214311067854920/"
                        "46709379527810930609274045373")
            : mpq_class("211843823749134168430775263275/"
                        "38007680823317012313714720743");
        assert(relative_eigenvalue == expected_eigenvalue);
        std::cout << "exact_alpha=" << exact_alpha
                  << " alpha*Theta=" << relative_eigenvalue << '\n';

        std::array<std::array<mpq_class, 5>, 5> second_gram{};
        for (int i = 0; i < 5; ++i) {
            for (int j = 0; j < 5; ++j) {
                second_gram[i][j] = exact_gram_entry(
                    second_vectors[i], second_vectors[j], level);
            }
        }
        mpq_class second_alpha = exact_residual_fraction(second_gram);
        mpq_class expected_second = level == 2
            ? mpq_class("920020551945270166975711/"
                        "12998197791101807219670856")
            : mpq_class("596657511940736589690394281/"
                        "1103569337664148347762679657");
        second_alpha.canonicalize();
        expected_second.canonicalize();
        assert(second_alpha == expected_second);
        std::cout << "second_order_alpha=" << second_alpha
                  << " decimal=" << second_alpha.get_d() << '\n';
    }
    std::cout << "PASS exact r=5 compensated Gram angles\n";
}
