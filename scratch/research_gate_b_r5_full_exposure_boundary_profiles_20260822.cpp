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

#include <gmpxx.h>

namespace {

std::int64_t falling_small(int value, int length) {
    std::int64_t answer = 1;
    for (int offset = 0; offset < length; ++offset) answer *= value - offset;
    return answer;
}

std::int64_t choose_small(int n, int k) {
    if (k < 0 || k > n) return 0;
    std::int64_t answer = 1;
    for (int i = 1; i <= k; ++i) answer = answer * (n - i + 1) / i;
    return answer;
}

std::int64_t extra_pair_numerator(int inside_hits, int outside_hits,
                                  int inside_size, int outside_size,
                                  int pairs) {
    std::int64_t answer = 0;
    for (int chosen_inside = 0; chosen_inside <= pairs; ++chosen_inside) {
        const int chosen_outside = pairs - chosen_inside;
        std::int64_t term = choose_small(pairs, chosen_inside)
            * falling_small(inside_hits, chosen_inside)
            * falling_small(inside_size - chosen_inside, chosen_outside)
            * falling_small(outside_hits, chosen_outside)
            * falling_small(outside_size - chosen_outside, chosen_inside);
        if (chosen_outside & 1) term = -term;
        answer += term;
    }
    return answer;
}

std::vector<std::int64_t> boundary_profile(
    const std::vector<int>& masks,
    const Exposure& exposure,
    int offset,
    int level) {
    constexpr int K = R - 2;
    std::vector<std::int64_t> answer(B, 0);
    const int all_mask = (1 << B) - 1;
    for (int start = 0; start < B; ++start) {
        const int inside_left = start;
        const int outside_left = (start - 1 + B) % B;
        const int inside_right = (start + K - 1) % B;
        const int outside_right = (start + K) % B;
        int interval = 0;
        for (int position = 0; position < K; ++position) {
            interval |= 1 << ((start + position) % B);
        }
        const int boundary_mask = (1 << inside_left) | (1 << outside_left)
            | (1 << inside_right) | (1 << outside_right);
        const int inside_pool = interval & ~boundary_mask;
        const int outside_pool = (all_mask ^ interval) & ~boundary_mask;
        for (int index = 0; index < static_cast<int>(masks.size()); ++index) {
            const int mask = masks[index];
            const int left = ((mask >> inside_left) & 1)
                           - ((mask >> outside_left) & 1);
            const int right = ((mask >> inside_right) & 1)
                            - ((mask >> outside_right) & 1);
            if (!left || !right) continue;
            const auto extra = extra_pair_numerator(
                std::popcount(static_cast<unsigned>(mask & inside_pool)),
                std::popcount(static_cast<unsigned>(mask & outside_pool)),
                K - 2, B - K - 2, level - 2);
            answer[start] += exposure[offset + index] * left * right * extra;
        }
    }
    return answer;
}

mpq_class exact_rho(const std::vector<std::int64_t>& left,
                    const std::vector<std::int64_t>& right) {
    mpz_class g00 = 0, g01 = 0, g11 = 0, h0 = 0, h1 = 0;
    for (int i = 0; i < B; ++i) {
        const mpz_class a(static_cast<long>(left[i]));
        const mpz_class c(static_cast<long>(right[i]));
        g00 += a * a;
        g01 += a * c;
        g11 += c * c;
        h0 += a;
        h1 += c;
    }
    const mpz_class determinant = g00 * g11 - g01 * g01;
    assert(determinant != 0);
    const mpq_class projection(
        g11 * h0 * h0 - 2 * g01 * h0 * h1 + g00 * h1 * h1,
        determinant);
    mpq_class answer = (mpq_class(B) - projection) / B;
    answer.canonicalize();
    return answer;
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
    std::uint64_t total = 0;
    for (int first = 0; first < B; ++first) {
        total += counts[first];
        for (int i = 0; i < TARGET_COUNT; ++i) exposure[i] += partial[first][i];
    }
    assert(total == FACTORIAL_B);

    for (int level = 2; level <= R - 2; ++level) {
        const auto middle = boundary_profile(middle_masks, exposure, 0, level);
        const auto lower = boundary_profile(
            lower_masks, exposure, MIDDLE_COUNT, level);
        const mpq_class rho = exact_rho(middle, lower);
        constexpr int ELL = B - (R - 2);
        std::cout << "r=5 j=" << level << " rho=" << rho
                  << " decimal=" << rho.get_d() << '\n';
        std::cout << "profile_middle";
        for (auto value : middle) std::cout << ' ' << value;
        std::cout << '\n';
        std::cout << "profile_lower";
        for (auto value : lower) std::cout << ' ' << value;
        std::cout << '\n';
        std::cout << "three_state_defect "
                  << middle[0] + middle[ELL] - middle[3] << ' '
                  << lower[0] + lower[ELL] - lower[3] << '\n';
    }
    std::cout << "PASS exact r=5 full-exposure boundary profiles\n";
}
