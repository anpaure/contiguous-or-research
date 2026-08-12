#if defined(__GNUC__) && !defined(__clang__)
#pragma GCC optimize("O3,unroll-loops")
#if defined(__x86_64__) || defined(__i386__)
#pragma GCC target("avx2,bmi,bmi2,lzcnt,popcnt")
#endif
#endif

#include <cadical.hpp>

#include <algorithm>
#include <array>
#include <bit>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <functional>
#include <iostream>
#include <limits>
#include <memory>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>

using namespace std;

namespace {

constexpr int K = 11;
constexpr int N = 465;
constexpr int LIMIT = 1 << K;
constexpr int MIDDLE = 462;

long long choose_value(int n, int r) {
    if (r < 0 || r > n) return 0;
    r = min(r, n - r);
    long long value = 1;
    for (int i = 1; i <= r; ++i) value = value * (n - r + i) / i;
    return value;
}

int safe_bound(int rank) {
    long long bound = static_cast<long long>(N) - choose_value(K, rank) + 1;
    for (int higher = rank + 1; higher <= K; ++higher)
        bound = min(bound, static_cast<long long>(N) - choose_value(K, higher));
    return static_cast<int>(max<long long>(0, min<long long>(N, bound)));
}

// Exact unrestricted containment-multiplicity cap.  In an N-entry solution,
// choose one interval for every r-set.  An interval of OR-rank s and length
// ell contains at least ell-(N-C(K,r)) selected r-witnesses.  Hence it has
// length at most N-C(K,r) for r>s, and at most
// N-C(K,r)+C(s,r) for r<=s.  Taking the best r subsumes safe_bound().
int containment_bound(int rank) {
    long long bound = N;
    for (int witness_rank = 1; witness_rank <= K; ++witness_rank) {
        const long long family = choose_value(K, witness_rank);
        if (family > N) continue;
        long long candidate = N - family;
        if (witness_rank <= rank)
            candidate += choose_value(rank, witness_rank);
        bound = min(bound, candidate);
    }
    return static_cast<int>(max<long long>(0, min<long long>(N, bound)));
}

struct DirectTarget {
    int target = 0;
    int rank = 0;
    int bound = 0;
    int L0 = 0;
    int R0 = 0;
    int M0 = 0;
    array<int, K> H0{};
};

// Optional globally-WLOG compression of ranks four and seven.  Six generic
// exception slots per layer are enough by the adjacent-shadow theorem; all
// other targets are certified by the chosen rank-five/rank-six schedules.
struct ExceptionSlot {
    int rank = 0;
    int bound = 0;
    int L0 = 0;
    int R0 = 0;
    int M0 = 0;
    array<int, K> value{};
    array<int, K> H0{};
    vector<int> q;
};

struct RankFourShadow {
    int left = 0;
    int right = 0;
    int at_most_four = 0;
    int at_most_three = 0;
    array<int, K> value{};
    vector<int> q;
    vector<int> q_three;
};

struct RankSevenShadow {
    int target = 0;
    int active = 0;
    int L0 = 0;
    int R0 = 0;
    int M0 = 0;
};

struct CentralLayer {
    int rank = 0;
    vector<int> masks;
    vector<array<int, 10>> state;
    vector<array<int, K>> value;
    vector<int> q;  // row-major [slot][mask index]
};

struct BestInterval {
    int left = 0;
    int right = 0;
    int value = 0;
    int target = 0;
    int cost = numeric_limits<int>::max();
};

constexpr array<pair<int, int>, 10> STATES{{
    {0, 0}, {0, 1}, {0, 2}, {0, 3}, {1, 1},
    {1, 2}, {1, 3}, {2, 2}, {2, 3}, {3, 3},
}};

// Optional exact encoding of the four globally valid rank-six band cuts.
// Once state 03 occurs, monotonicity leaves only this total chain.  Its six
// transition positions are enough to express all four pseudo-Boolean sums.
struct BandCutPlan {
    static constexpr int BITS = 9;
    static constexpr array<int, 7> CHAIN{{0, 1, 2, 3, 6, 8, 9}};

    int& next;
    const CentralLayer& rank_six;
    int first_variable = 0;
    int variable_count = 0;
    int one = 0;
    array<array<int, MIDDLE + 1>, 6> boundary{};
    array<array<int, BITS>, 6> bits{};
    vector<vector<int>> clauses;

    BandCutPlan(int& next_variable, const CentralLayer& layer)
        : next(next_variable), rank_six(layer), first_variable(next_variable) {
        build();
        variable_count = next - first_variable;
    }

    int fresh() { return next++; }
    int state(int position, int chain_index) const {
        return rank_six.state[position][CHAIN[chain_index]];
    }
    void add(vector<int> clause) { clauses.push_back(std::move(clause)); }

    vector<int> constant_bits(unsigned value) const {
        int width = 1;
        while ((1u << width) <= value) ++width;
        vector<int> result(width);
        for (int bit = 0; bit < width; ++bit)
            result[bit] = value & (1u << bit) ? one : -one;
        return result;
    }

    // A ripple adder over signed literals.  Keeping the final carry makes the
    // result exact rather than modular.
    vector<int> add_unsigned(const vector<int>& x, const vector<int>& y) {
        const int width = max(x.size(), y.size());
        vector<int> result;
        result.reserve(width + 1);
        int carry = -one;
        for (int bit = 0; bit < width; ++bit) {
            const int a = bit < static_cast<int>(x.size()) ? x[bit] : -one;
            const int b = bit < static_cast<int>(y.size()) ? y[bit] : -one;
            const int sum = fresh();
            const int next_carry = fresh();
            for (int av = 0; av < 2; ++av)
                for (int bv = 0; bv < 2; ++bv)
                    for (int cv = 0; cv < 2; ++cv) {
                        const int parity = av ^ bv ^ cv;
                        add({av ? -a : a, bv ? -b : b, cv ? -carry : carry,
                             parity ? sum : -sum});
                    }
            add({-a, -b, next_carry});
            add({-a, -carry, next_carry});
            add({-b, -carry, next_carry});
            add({-next_carry, a, b});
            add({-next_carry, a, carry});
            add({-next_carry, b, carry});
            result.push_back(sum);
            carry = next_carry;
        }
        result.push_back(carry);
        return result;
    }

    // Lexicographic unsigned comparison from the most significant bit.  The
    // only forbidden first difference is x=1,y=0.
    void add_leq(vector<int> x, vector<int> y) {
        const int width = max(x.size(), y.size());
        x.resize(width, -one);
        y.resize(width, -one);
        int equal_above = one;
        for (int bit = width - 1; bit >= 0; --bit) {
            add({-equal_above, -x[bit], y[bit]});
            if (bit == 0) continue;
            const int next_equal = fresh();
            add({-next_equal, equal_above});
            add({-next_equal, -x[bit], y[bit]});
            add({-next_equal, x[bit], -y[bit]});
            add({-equal_above, -x[bit], -y[bit], next_equal});
            add({-equal_above, x[bit], y[bit], next_equal});
            equal_above = next_equal;
        }
    }

    void build() {
        one = fresh();
        add({one});

        // State 03 occurs at least 93 times.  Any of 11,12,22 in the same
        // monotone schedule would be incomparable with it.
        for (int i = 0; i < MIDDLE; ++i)
            for (int u : {4, 5, 7}) add({-rank_six.state[i][u]});

        // b_j is the number of slots in the first j+1 chain states.  A single
        // boundary selector is forced by the already-present monotonicity.
        for (int j = 0; j < 6; ++j) {
            for (int t = 0; t <= MIDDLE; ++t) boundary[j][t] = fresh();
            for (int bit = 0; bit < BITS; ++bit) bits[j][bit] = fresh();
            add(vector<int>(boundary[j].begin(), boundary[j].end()));

            {
                vector<int> clause{-boundary[j][0]};
                for (int q = j + 1; q < 7; ++q) clause.push_back(state(0, q));
                add(std::move(clause));
            }
            for (int t = 1; t < MIDDLE; ++t) {
                vector<int> before{-boundary[j][t]};
                for (int q = 0; q <= j; ++q)
                    before.push_back(state(t - 1, q));
                add(std::move(before));
                vector<int> after{-boundary[j][t]};
                for (int q = j + 1; q < 7; ++q)
                    after.push_back(state(t, q));
                add(std::move(after));
            }
            {
                vector<int> clause{-boundary[j][MIDDLE]};
                for (int q = 0; q <= j; ++q)
                    clause.push_back(state(MIDDLE - 1, q));
                add(std::move(clause));
            }

            // Convert the unique one-hot boundary to nine binary bits with
            // two clauses per bit, rather than 463*9 implications.
            for (int bit = 0; bit < BITS; ++bit) {
                vector<int> bit_one{-bits[j][bit]};
                vector<int> bit_zero{bits[j][bit]};
                for (int t = 0; t <= MIDDLE; ++t)
                    (t & (1 << bit) ? bit_one : bit_zero)
                        .push_back(boundary[j][t]);
                add(std::move(bit_one));
                add(std::move(bit_zero));
            }
        }

        auto B = [&](int j) {
            return vector<int>(bits[j].begin(), bits[j].end());
        };
        const vector<int> b1 = B(0), b2 = B(1), b3 = B(2);
        const vector<int> b4 = B(3), b5 = B(4), b6 = B(5);
        const vector<int> s12 = add_unsigned(b1, b2);
        const vector<int> s123 = add_unsigned(s12, b3);
        const vector<int> s56 = add_unsigned(b5, b6);
        const vector<int> s456 = add_unsigned(s56, b4);

        // Respectively: x0<=3; 2*x0+x1<=138; sum(width)>=1008;
        // x3>=93.  The boundary identities are proved in the companion note.
        add_leq(add_unsigned(b1, constant_bits(459)), b6);
        add_leq(add_unsigned(s12, constant_bits(786)), s56);
        add_leq(add_unsigned(s123, constant_bits(1008)), s456);
        add_leq(add_unsigned(b3, constant_bits(93)), b4);
    }

    int variables() const { return variable_count; }
};

// Optional exact joint cuts between the independently selected rank-five and
// rank-six monotone bands.  This plan requires BandCutPlan: it reuses the six
// exact binary rank-six boundaries and strengthens x0<=3 to x0<=1.  The
// rank-five schedule is placed on one of the three possible maximal chains
// containing a width-two state; six further boundaries then express all four
// cross-layer inequalities with small guarded arithmetic circuits.
struct JointBandCutPlan {
    static constexpr int BITS = 9;
    static constexpr array<array<int, 7>, 3> CHAINS{{
        {{0, 1, 2, 5, 6, 8, 9}},  // 00 01 02 12 13 23 33
        {{0, 1, 2, 5, 7, 8, 9}},  // 00 01 02 12 22 23 33
        {{0, 1, 4, 5, 6, 8, 9}},  // 00 01 11 12 13 23 33
    }};

    int& next;
    const CentralLayer& rank_five;
    const CentralLayer& rank_six;
    const BandCutPlan& rank_six_plan;
    int first_variable = 0;
    int variable_count = 0;
    int one = 0;
    int e = 0;  // exact x0 after the strengthened x0<=1 comparison
    array<int, 3> chain_selector{};
    array<array<int, MIDDLE + 1>, 6> boundary{};
    array<array<int, BITS>, 6> bits{};
    vector<vector<int>> clauses;

    JointBandCutPlan(int& next_variable, const CentralLayer& lower,
                     const CentralLayer& upper, const BandCutPlan& upper_plan)
        : next(next_variable),
          rank_five(lower),
          rank_six(upper),
          rank_six_plan(upper_plan),
          first_variable(next_variable),
          one(upper_plan.one) {
        build();
        variable_count = next - first_variable;
    }

    int fresh() { return next++; }
    void add(vector<int> clause) { clauses.push_back(std::move(clause)); }

    int lower_state(int position, int chain, int chain_index) const {
        return rank_five.state[position][CHAINS[chain][chain_index]];
    }

    vector<int> constant_bits(unsigned value) const {
        int width = 1;
        while ((1u << width) <= value) ++width;
        vector<int> result(width);
        for (int bit = 0; bit < width; ++bit)
            result[bit] = value & (1u << bit) ? one : -one;
        return result;
    }

    vector<int> add_unsigned(const vector<int>& x, const vector<int>& y) {
        const int width = max(x.size(), y.size());
        vector<int> result;
        result.reserve(width + 1);
        int carry = -one;
        for (int bit = 0; bit < width; ++bit) {
            const int a = bit < static_cast<int>(x.size()) ? x[bit] : -one;
            const int b = bit < static_cast<int>(y.size()) ? y[bit] : -one;
            const int sum = fresh();
            const int next_carry = fresh();
            for (int av = 0; av < 2; ++av)
                for (int bv = 0; bv < 2; ++bv)
                    for (int cv = 0; cv < 2; ++cv) {
                        const int parity = av ^ bv ^ cv;
                        add({av ? -a : a, bv ? -b : b,
                             cv ? -carry : carry, parity ? sum : -sum});
                    }
            add({-a, -b, next_carry});
            add({-a, -carry, next_carry});
            add({-b, -carry, next_carry});
            add({-next_carry, a, b});
            add({-next_carry, a, carry});
            add({-next_carry, b, carry});
            result.push_back(sum);
            carry = next_carry;
        }
        result.push_back(carry);
        return result;
    }

    vector<int> sum_all(initializer_list<vector<int>> terms) {
        auto iterator = terms.begin();
        vector<int> result = *iterator++;
        while (iterator != terms.end())
            result = add_unsigned(result, *iterator++);
        return result;
    }

    // Exact unsigned comparison, active only when guard is true.  All prefix
    // equality definitions are guarded as well, so inactive chain arithmetic
    // imposes no accidental restriction.
    void add_leq_guarded(vector<int> x, vector<int> y, int guard) {
        const int width = max(x.size(), y.size());
        x.resize(width, -one);
        y.resize(width, -one);
        int equal_above = one;
        for (int bit = width - 1; bit >= 0; --bit) {
            add({-guard, -equal_above, -x[bit], y[bit]});
            if (bit == 0) continue;
            const int next_equal = fresh();
            add({-guard, -next_equal, equal_above});
            add({-guard, -next_equal, -x[bit], y[bit]});
            add({-guard, -next_equal, x[bit], -y[bit]});
            add({-guard, -equal_above, -x[bit], -y[bit], next_equal});
            add({-guard, -equal_above, x[bit], y[bit], next_equal});
            equal_above = next_equal;
        }
    }

    void build() {
        // Exactly one of the three maximal rank-five chains containing a
        // width-two state is selected.  The fourth possible chain contains no
        // width-two state and is excluded by the proved y2>=y0+87+4*x0 cut.
        for (int& selector : chain_selector) selector = fresh();
        add({chain_selector[0], chain_selector[1], chain_selector[2]});
        for (int a = 0; a < 3; ++a)
            for (int b = a + 1; b < 3; ++b)
                add({-chain_selector[a], -chain_selector[b]});

        for (int chain = 0; chain < 3; ++chain) {
            array<bool, 10> allowed{};
            for (int state : CHAINS[chain]) allowed[state] = true;
            for (int position = 0; position < MIDDLE; ++position)
                for (int state = 0; state < 10; ++state)
                    if (!allowed[state])
                        add({-chain_selector[chain],
                             -rank_five.state[position][state]});
        }

        // h_j is the number of slots in the first j+1 states of the selected
        // rank-five chain.  The selected chain and the existing monotonicity
        // make exactly one transition selector possible for every j.
        for (int j = 0; j < 6; ++j) {
            for (int t = 0; t <= MIDDLE; ++t) boundary[j][t] = fresh();
            for (int bit = 0; bit < BITS; ++bit) bits[j][bit] = fresh();
            add(vector<int>(boundary[j].begin(), boundary[j].end()));

            for (int chain = 0; chain < 3; ++chain) {
                {
                    vector<int> clause{-boundary[j][0],
                                       -chain_selector[chain]};
                    for (int q = j + 1; q < 7; ++q)
                        clause.push_back(lower_state(0, chain, q));
                    add(std::move(clause));
                }
                for (int t = 1; t < MIDDLE; ++t) {
                    vector<int> before{-boundary[j][t],
                                       -chain_selector[chain]};
                    for (int q = 0; q <= j; ++q)
                        before.push_back(lower_state(t - 1, chain, q));
                    add(std::move(before));
                    vector<int> after{-boundary[j][t],
                                      -chain_selector[chain]};
                    for (int q = j + 1; q < 7; ++q)
                        after.push_back(lower_state(t, chain, q));
                    add(std::move(after));
                }
                {
                    vector<int> clause{-boundary[j][MIDDLE],
                                       -chain_selector[chain]};
                    for (int q = 0; q <= j; ++q)
                        clause.push_back(lower_state(MIDDLE - 1, chain, q));
                    add(std::move(clause));
                }
            }

            for (int bit = 0; bit < BITS; ++bit) {
                vector<int> bit_one{-bits[j][bit]};
                vector<int> bit_zero{bits[j][bit]};
                for (int t = 0; t <= MIDDLE; ++t)
                    (t & (1 << bit) ? bit_one : bit_zero)
                        .push_back(boundary[j][t]);
                add(std::move(bit_one));
                add(std::move(bit_zero));
            }
        }

        auto H = [&](int j) {
            return vector<int>(bits[j].begin(), bits[j].end());
        };
        auto G = [&](int j) {
            return vector<int>(rank_six_plan.bits[j].begin(),
                               rank_six_plan.bits[j].end());
        };
        const vector<int> h1 = H(0), h2 = H(1), h3 = H(2);
        const vector<int> h4 = H(3), h5 = H(4), h6 = H(5);
        const vector<int> g1 = G(0), g2 = G(1), g3 = G(2);
        const vector<int> g4 = G(3), g5 = G(4), g6 = G(5);

        // Strengthen x0<=3 to x0<=1.
        add_leq_guarded(add_unsigned(g1, constant_bits(461)), g6, one);

        // e is exactly the presence of a width-zero rank-six state.  The
        // comparison above ensures there is at most one such slot, hence
        // e equals the integer x0 and may be used as its one-bit value.
        e = fresh();
        vector<int> width_zero_support{-e};
        for (int position = 0; position < MIDDLE; ++position) {
            for (int state : {0, 9}) {
                add({-rank_six.state[position][state], e});
                width_zero_support.push_back(rank_six.state[position][state]);
            }
        }
        add(std::move(width_zero_support));
        const vector<int> e1{e};
        const vector<int> e4{-one, -one, e};

        const vector<int> c3 = constant_bits(3);
        const vector<int> c327 = constant_bits(327);
        const vector<int> c549 = constant_bits(549);

        // Chain A: 00 01 02 12 13 23 33.
        add_leq_guarded(sum_all({h1, c327, e1}), h6,
                        chain_selector[0]);
        add_leq_guarded(sum_all({h2, h4, h1, c549, e4}),
                        sum_all({h3, h5, h6}), chain_selector[0]);
        add_leq_guarded(sum_all({g2, h6}), sum_all({h1, g5, c3}),
                        chain_selector[0]);
        add_leq_guarded(sum_all({h3, h5, g3}),
                        sum_all({h2, h4, g4, c3}), chain_selector[0]);

        // Chain B: 00 01 02 12 22 23 33.
        add_leq_guarded(sum_all({h1, h5, c327, e1}), sum_all({h4, h6}),
                        chain_selector[1]);
        add_leq_guarded(sum_all({h2, h1, h5, c549, e4}),
                        sum_all({h3, h4, h6}), chain_selector[1]);
        add_leq_guarded(sum_all({g2, h4, h6}),
                        sum_all({h1, h5, g5, c3}), chain_selector[1]);
        add_leq_guarded(sum_all({h3, g3}), sum_all({h2, g4, c3}),
                        chain_selector[1]);

        // Chain C: 00 01 11 12 13 23 33.
        add_leq_guarded(sum_all({h1, h3, c327, e1}), sum_all({h2, h6}),
                        chain_selector[2]);
        add_leq_guarded(sum_all({h4, h1, h3, c549, e4}),
                        sum_all({h5, h2, h6}), chain_selector[2]);
        add_leq_guarded(sum_all({g2, h2, h6}),
                        sum_all({h1, h3, g5, c3}), chain_selector[2]);
        add_leq_guarded(sum_all({h5, g3}), sum_all({h4, g4, c3}),
                        chain_selector[2]);
    }

    int variables() const { return variable_count; }
};

// Optional branch-one specialization of the audited boundary-localized
// short-pool theorem.  The surrounding branch unit fixes e=x0=1, so the
// three exact comparisons need only their rank-five chain selectors as
// guards.  All rank-five/rank-six boundary bits and the constant-one literal
// are reused from the existing plans.
struct RankSixBranchProfilePlan {
    static constexpr int BITS = 9;

    int& next;
    const BandCutPlan& rank_six_plan;
    const JointBandCutPlan& joint_plan;
    int first_variable = 0;
    int variable_count = 0;
    int one = 0;
    vector<vector<int>> clauses;

    RankSixBranchProfilePlan(int& next_variable, const BandCutPlan& upper,
                             const JointBandCutPlan& joint)
        : next(next_variable),
          rank_six_plan(upper),
          joint_plan(joint),
          first_variable(next_variable),
          one(joint.one) {
        build();
        variable_count = next - first_variable;
    }

    int fresh() { return next++; }
    void add(vector<int> clause) { clauses.push_back(std::move(clause)); }

    vector<int> constant_bits(unsigned value) const {
        int width = 1;
        while ((1u << width) <= value) ++width;
        vector<int> result(width);
        for (int bit = 0; bit < width; ++bit)
            result[bit] = value & (1u << bit) ? one : -one;
        return result;
    }

    vector<int> add_unsigned(const vector<int>& x, const vector<int>& y) {
        const int width = max(x.size(), y.size());
        vector<int> result;
        result.reserve(width + 1);
        int carry = -one;
        for (int bit = 0; bit < width; ++bit) {
            const int a = bit < static_cast<int>(x.size()) ? x[bit] : -one;
            const int b = bit < static_cast<int>(y.size()) ? y[bit] : -one;
            const int sum = fresh();
            const int next_carry = fresh();
            for (int av = 0; av < 2; ++av)
                for (int bv = 0; bv < 2; ++bv)
                    for (int cv = 0; cv < 2; ++cv) {
                        const int parity = av ^ bv ^ cv;
                        add({av ? -a : a, bv ? -b : b,
                             cv ? -carry : carry, parity ? sum : -sum});
                    }
            add({-a, -b, next_carry});
            add({-a, -carry, next_carry});
            add({-b, -carry, next_carry});
            add({-next_carry, a, b});
            add({-next_carry, a, carry});
            add({-next_carry, b, carry});
            result.push_back(sum);
            carry = next_carry;
        }
        result.push_back(carry);
        return result;
    }

    vector<int> sum_all(initializer_list<vector<int>> terms) {
        auto iterator = terms.begin();
        vector<int> result = *iterator++;
        while (iterator != terms.end())
            result = add_unsigned(result, *iterator++);
        return result;
    }

    void add_leq_guarded(vector<int> x, vector<int> y, int guard) {
        const int width = max(x.size(), y.size());
        x.resize(width, -one);
        y.resize(width, -one);
        int equal_above = one;
        for (int bit = width - 1; bit >= 0; --bit) {
            add({-guard, -equal_above, -x[bit], y[bit]});
            if (bit == 0) continue;
            const int next_equal = fresh();
            add({-guard, -next_equal, equal_above});
            add({-guard, -next_equal, -x[bit], y[bit]});
            add({-guard, -next_equal, x[bit], -y[bit]});
            add({-guard, -equal_above, -x[bit], -y[bit], next_equal});
            add({-guard, -equal_above, x[bit], y[bit], next_equal});
            equal_above = next_equal;
        }
    }

    void build() {
        auto G = [&](int j) {
            return vector<int>(rank_six_plan.bits[j].begin(),
                               rank_six_plan.bits[j].end());
        };
        auto H = [&](int j) {
            return vector<int>(joint_plan.bits[j].begin(),
                               joint_plan.bits[j].end());
        };
        const vector<int> g2 = G(1), g5 = G(4);
        const vector<int> h2 = H(1), h3 = H(2);
        const vector<int> h4 = H(3), h5 = H(4);
        const vector<int> c557 = constant_bits(557);

        // e=1 turns y2>=x1+82+14*e into g2+557<=y2+g5.
        // Add narrower nine-bit terms before the ten-bit constant so these
        // three rows attain the audited minimum 241-variable inventory.
        add_leq_guarded(sum_all({g2, h2, h4, c557}),
                        sum_all({h3, h5, g5}),
                        joint_plan.chain_selector[0]);
        add_leq_guarded(sum_all({g2, h2, c557}), sum_all({h3, g5}),
                        joint_plan.chain_selector[1]);
        add_leq_guarded(sum_all({g2, h4, c557}), sum_all({h5, g5}),
                        joint_plan.chain_selector[2]);
    }

    int variables() const { return variable_count; }
};

// Optional exact endpoint-alignment cuts forced by common flags through
// ranks 3,4,5,6.  This plan requires the adjacent-shadow option because it
// reuses that option's bidirectional rank-six endpoint/width summaries.
// Rank-five summaries and every counted conjunction are defined in both
// directions here.  Four exact 465-input counters enforce the independently
// audited lower bounds 324,324,24,24.
struct EndpointAlignmentCutPlan {
    static constexpr int BITS = 9;

    int& next;
    const CentralLayer& rank_five;
    const array<array<int, 4>, N>& rank_six_by_left;
    const array<array<int, 4>, N>& rank_six_by_right;
    int first_variable = 0;
    int variable_count = 0;
    int one = 0;
    array<int, N> l5pos{}, r5pos{}, l52{}, r52{};
    array<int, N> zl324{}, zr324{}, zl24{}, zr24{};
    vector<vector<int>> clauses;

    EndpointAlignmentCutPlan(
        int& next_variable, const CentralLayer& lower,
        const array<array<int, 4>, N>& upper_by_left,
        const array<array<int, 4>, N>& upper_by_right)
        : next(next_variable),
          rank_five(lower),
          rank_six_by_left(upper_by_left),
          rank_six_by_right(upper_by_right),
          first_variable(next_variable) {
        build();
        variable_count = next - first_variable;
    }

    int fresh() { return next++; }
    void add(vector<int> clause) { clauses.push_back(std::move(clause)); }

    void define_or(int output, const vector<int>& support) {
        vector<int> reverse{-output};
        reverse.reserve(support.size() + 1);
        for (int literal : support) {
            add({-literal, output});
            reverse.push_back(literal);
        }
        add(std::move(reverse));
    }

    void define_z324(int output, int lower, int upper2, int upper3) {
        add({-output, lower});
        add({-output, upper2, upper3});
        add({-lower, -upper2, output});
        add({-lower, -upper3, output});
    }

    void define_z24(int output, int lower, int upper3) {
        add({-output, lower});
        add({-output, upper3});
        add({-lower, -upper3, output});
    }

    void define_xor(int output, int a, int b) {
        add({a, b, -output});
        add({a, -b, output});
        add({-a, b, output});
        add({-a, -b, -output});
    }

    void define_and(int output, int a, int b) {
        add({-output, a});
        add({-output, b});
        add({-a, -b, output});
    }

    // Increment an exact nine-bit count once for every true input.  The carry
    // out of bit eight is unnecessary: at most 465 increments occur, so the
    // represented integer is always below 2^9.
    vector<int> exact_count(const array<int, N>& input) {
        vector<int> bits(BITS, -one);
        for (int literal : input) {
            vector<int> next_bits(BITS);
            int carry = literal;
            for (int bit = 0; bit < BITS; ++bit) {
                next_bits[bit] = fresh();
                define_xor(next_bits[bit], bits[bit], carry);
                if (bit + 1 < BITS) {
                    const int next_carry = fresh();
                    define_and(next_carry, bits[bit], carry);
                    carry = next_carry;
                }
            }
            bits.swap(next_bits);
        }
        return bits;
    }

    vector<int> constant_bits(unsigned value) const {
        int width = 1;
        while ((1u << width) <= value) ++width;
        vector<int> result(width);
        for (int bit = 0; bit < width; ++bit)
            result[bit] = value & (1u << bit) ? one : -one;
        return result;
    }

    // Exact unsigned x<=y comparison.  The prefix-equality variables are
    // defined in both directions, so the comparator cannot evade a failing
    // most-significant difference.
    void add_leq(vector<int> x, vector<int> y) {
        const int width = max(x.size(), y.size());
        x.resize(width, -one);
        y.resize(width, -one);
        int equal_above = one;
        for (int bit = width - 1; bit >= 0; --bit) {
            add({-equal_above, -x[bit], y[bit]});
            if (bit == 0) continue;
            const int next_equal = fresh();
            add({-next_equal, equal_above});
            add({-next_equal, -x[bit], y[bit]});
            add({-next_equal, x[bit], -y[bit]});
            add({-equal_above, -x[bit], -y[bit], next_equal});
            add({-equal_above, x[bit], y[bit], next_equal});
            equal_above = next_equal;
        }
    }

    void build() {
        one = fresh();
        add({one});

        array<vector<int>, N> l5pos_support, r5pos_support;
        array<vector<int>, N> l52_support, r52_support;
        for (int i = 0; i < MIDDLE; ++i)
            for (int u = 0; u < 10; ++u) {
                const auto [alpha, beta] = STATES[u];
                const int left = i + alpha, right = i + beta;
                const int width = beta - alpha;
                const int z = rank_five.state[i][u];
                if (width == 1 || width == 2) {
                    l5pos_support[left].push_back(z);
                    r5pos_support[right].push_back(z);
                }
                if (width == 2) {
                    l52_support[left].push_back(z);
                    r52_support[right].push_back(z);
                }
            }

        for (int p = 0; p < N; ++p) {
            l5pos[p] = fresh();
            r5pos[p] = fresh();
            l52[p] = fresh();
            r52[p] = fresh();
            define_or(l5pos[p], l5pos_support[p]);
            define_or(r5pos[p], r5pos_support[p]);
            define_or(l52[p], l52_support[p]);
            define_or(r52[p], r52_support[p]);
        }

        for (int p = 0; p < N; ++p) {
            zl324[p] = fresh();
            zr324[p] = fresh();
            zl24[p] = fresh();
            zr24[p] = fresh();
            define_z324(zl324[p], l5pos[p], rank_six_by_left[p][2],
                        rank_six_by_left[p][3]);
            define_z324(zr324[p], r5pos[p], rank_six_by_right[p][2],
                        rank_six_by_right[p][3]);
            define_z24(zl24[p], l52[p], rank_six_by_left[p][3]);
            define_z24(zr24[p], r52[p], rank_six_by_right[p][3]);
        }

        const vector<int> count_l324 = exact_count(zl324);
        const vector<int> count_r324 = exact_count(zr324);
        const vector<int> count_l24 = exact_count(zl24);
        const vector<int> count_r24 = exact_count(zr24);
        add_leq(constant_bits(324), count_l324);
        add_leq(constant_bits(324), count_r324);
        add_leq(constant_bits(24), count_l24);
        add_leq(constant_bits(24), count_r24);
    }

    int variables() const { return variable_count; }
};

// Optional unrestricted local-density cuts.  The final variables rank[p][s]
// are an exact one-hot encoding of |A[p]|=s, obtained from a shared prefix
// popcount circuit.  Both weighted inequalities use that same one-hot layer:
//
//   210 n1 + 84 n2 + 28 n3 + 7 n4 + n5 >= 7392,
//   252 n1 +126 n2 + 56 n3 +21 n4 +6 n5+n6 >=14322.
//
// Every arithmetic gate below is bidirectional.  Consequently this module is
// an exact encoding of the two pseudo-Boolean inequalities, rather than a
// one-way propagation aid.  It allocates no variable and emits no clause when
// K11_FOREST_LOCAL_DENSITY_PB is absent.
struct LocalDensityPBPlan {
    static constexpr int RANKS = K + 1;

    int& next;
    int first_variable = 0;
    int variable_count = 0;
    int one = 0;
    array<array<int, RANKS>, N> rank{};
    vector<vector<int>> clauses;

    explicit LocalDensityPBPlan(int& next_variable)
        : next(next_variable), first_variable(next_variable) {
        build();
        variable_count = next - first_variable;
    }

    int fresh() { return next++; }
    static int entry(int position, int bit) {
        return 1 + position * K + bit;
    }
    void add(vector<int> clause) { clauses.push_back(std::move(clause)); }

    // z = (selector ? when_one : when_zero).  All arguments except z may be
    // signed literals; in particular -one is the constant false literal.
    void define_mux(int z, int selector, int when_zero, int when_one) {
        add({selector, -z, when_zero});
        add({selector, z, -when_zero});
        add({-selector, -z, when_one});
        add({-selector, z, -when_one});
    }

    // Exact full adder.  The eight clauses define sum=a xor b xor carry, and
    // the six remaining clauses define next_carry=majority(a,b,carry).
    pair<int, int> full_adder(int a, int b, int carry) {
        const int sum = fresh();
        const int next_carry = fresh();
        for (int av = 0; av < 2; ++av)
            for (int bv = 0; bv < 2; ++bv)
                for (int cv = 0; cv < 2; ++cv) {
                    const int parity = av ^ bv ^ cv;
                    add({av ? -a : a, bv ? -b : b,
                         cv ? -carry : carry, parity ? sum : -sum});
                }
        add({-a, -b, next_carry});
        add({-a, -carry, next_carry});
        add({-b, -carry, next_carry});
        add({-next_carry, a, b});
        add({-next_carry, a, carry});
        add({-next_carry, b, carry});
        return {sum, next_carry};
    }

    // Exact unsigned ripple addition.  Retaining the final carry prevents
    // modular wraparound.
    vector<int> add_unsigned(const vector<int>& x, const vector<int>& y) {
        const int width = max(x.size(), y.size());
        vector<int> result;
        result.reserve(width + 1);
        int carry = -one;
        for (int bit = 0; bit < width; ++bit) {
            const int a = bit < static_cast<int>(x.size()) ? x[bit] : -one;
            const int b = bit < static_cast<int>(y.size()) ? y[bit] : -one;
            const auto [sum, next_carry] = full_adder(a, b, carry);
            result.push_back(sum);
            carry = next_carry;
        }
        result.push_back(carry);
        return result;
    }

    // A balanced tree keeps the largest operands at 17 bits: both weighted
    // totals are below 465*252 < 2^17.
    vector<int> sum_terms(vector<vector<int>> terms) {
        while (terms.size() > 1) {
            vector<vector<int>> next_level;
            next_level.reserve((terms.size() + 1) / 2);
            for (size_t i = 0; i + 1 < terms.size(); i += 2)
                next_level.push_back(add_unsigned(terms[i], terms[i + 1]));
            if (terms.size() & 1) next_level.push_back(std::move(terms.back()));
            terms.swap(next_level);
        }
        return std::move(terms.front());
    }

    vector<int> constant_bits(unsigned value) const {
        int width = 1;
        while ((1u << width) <= value) ++width;
        vector<int> result(width);
        for (int bit = 0; bit < width; ++bit)
            result[bit] = value & (1u << bit) ? one : -one;
        return result;
    }

    // Exact unsigned x<=y.  equal_above is defined in both directions at
    // every bit, so the first unequal bit cannot be hidden by auxiliaries.
    void add_leq(vector<int> x, vector<int> y) {
        const int width = max(x.size(), y.size());
        x.resize(width, -one);
        y.resize(width, -one);
        int equal_above = one;
        for (int bit = width - 1; bit >= 0; --bit) {
            add({-equal_above, -x[bit], y[bit]});
            if (bit == 0) continue;
            const int next_equal = fresh();
            add({-next_equal, equal_above});
            add({-next_equal, -x[bit], y[bit]});
            add({-next_equal, x[bit], -y[bit]});
            add({-equal_above, -x[bit], -y[bit], next_equal});
            add({-equal_above, x[bit], y[bit], next_equal});
            equal_above = next_equal;
        }
    }

    vector<int> weighted_term(int position,
                              const array<unsigned, RANKS>& weight) {
        unsigned maximum = 0;
        for (unsigned value : weight) maximum = max(maximum, value);
        int width = 1;
        while ((1u << width) <= maximum) ++width;
        vector<int> result(width);
        for (int bit = 0; bit < width; ++bit) {
            const int z = result[bit] = fresh();
            vector<int> reverse{-z};
            for (int s = 0; s < RANKS; ++s)
                if (weight[s] & (1u << bit)) {
                    add({-rank[position][s], z});
                    reverse.push_back(rank[position][s]);
                }
            add(std::move(reverse));
        }
        return result;
    }

    void build() {
        one = fresh();
        add({one});

        // After the first bit the exact prefix-count literals are simply
        // (!A[p][0], A[p][0]).  Each later level is a bank of exact muxes:
        // count(i,s) selects count(i-1,s) or count(i-1,s-1) according to bit i.
        for (int position = 0; position < N; ++position) {
            vector<int> previous{-entry(position, 0), entry(position, 0)};
            for (int bit = 1; bit < K; ++bit) {
                vector<int> current(bit + 2);
                for (int s = 0; s <= bit + 1; ++s) {
                    const int z = current[s] = fresh();
                    const int keep = s < static_cast<int>(previous.size())
                                         ? previous[s]
                                         : -one;
                    const int raise = s > 0 ? previous[s - 1] : -one;
                    define_mux(z, entry(position, bit), keep, raise);
                }
                previous.swap(current);
            }
            for (int s = 0; s < RANKS; ++s) rank[position][s] = previous[s];
        }

        constexpr array<unsigned, RANKS> weight_five{
            0, 210, 84, 28, 7, 1, 0, 0, 0, 0, 0, 0};
        constexpr array<unsigned, RANKS> weight_six{
            0, 252, 126, 56, 21, 6, 1, 0, 0, 0, 0, 0};
        vector<vector<int>> terms_five, terms_six;
        terms_five.reserve(N);
        terms_six.reserve(N);
        for (int position = 0; position < N; ++position) {
            terms_five.push_back(weighted_term(position, weight_five));
            terms_six.push_back(weighted_term(position, weight_six));
        }
        const vector<int> total_five = sum_terms(std::move(terms_five));
        const vector<int> total_six = sum_terms(std::move(terms_six));
        add_leq(constant_bits(7392), total_five);
        // Amortized length-four credit across all 462 six-subcubes.
        add_leq(constant_bits(14322), total_six);
    }

    int variables() const { return variable_count; }
};

// Optional exact residual coordinate-symmetry break for the two exhaustive
// rank-filtration branches.  A coordinate is its complete N-bit occurrence
// column.  Coordinate permutations act by permuting these columns, while all
// target families and every enabled structural circuit are equivariant.
//
// In Type II no literal rank-six entry exists, so the full S_11 action
// survives.  In Type I the canonical endpoint A[0]=63 leaves the stabilizer
// S_6 x S_5.  Sorting the columns lexicographically inside the corresponding
// groups therefore loses no solution.  The prefix-equality variables below
// are bidirectional; they cannot be set false to evade a first-difference
// comparison.
struct ResidualCoordinateLexPlan {
    int& next;
    int first_variable = 0;
    int variable_count = 0;
    int one = 0;
    long long comparator_clauses = 0;
    vector<vector<int>> clauses;

    ResidualCoordinateLexPlan(int& next_variable, bool type_one)
        : next(next_variable), first_variable(next_variable) {
        build(type_one);
        variable_count = next - first_variable;
    }

    static int entry(int position, int bit) {
        return 1 + position * K + bit;
    }

    int fresh() { return next++; }
    void add(vector<int> clause) {
        clauses.push_back(std::move(clause));
        ++comparator_clauses;
    }

    // Enforce occurrence-column(left) <=lex occurrence-column(right).
    void add_column_comparator(int left, int right) {
        int equal_above = one;
        for (int position = 0; position < N; ++position) {
            const int x = entry(position, left);
            const int y = entry(position, right);
            add({-equal_above, -x, y});
            if (position + 1 == N) continue;

            const int next_equal = fresh();
            add({-next_equal, equal_above});
            add({-next_equal, -x, y});
            add({-next_equal, x, -y});
            add({-equal_above, -x, -y, next_equal});
            add({-equal_above, x, y, next_equal});
            equal_above = next_equal;
        }
    }

    void add_group(int first, int last) {
        for (int bit = first; bit < last; ++bit)
            add_column_comparator(bit, bit + 1);
    }

    void build(bool type_one) {
        one = fresh();
        add({one});
        if (type_one) {
            add_group(0, 5);
            add_group(6, 10);
        } else {
            add_group(0, 10);
        }
    }

    int variables() const { return variable_count; }
};

// Optional exact array-level encoding of the no-literal-six-set branch of
// rank-filtration stability.  It reuses LocalDensityPBPlan's exact one-hot
// entry ranks and JointBandCutPlan's exact rank-five width boundaries.
//
// The branch says:
//   * every array entry has rank at most five;
//   * at most 134 entries have rank five;
//   * the rank-at-most-four positions have at most two components; and
//   * the duplicate excess among literal rank-five masks is at most one.
//
// For the last row we choose, WLOG, a singleton selected witness for every
// distinct literal rank-five value.  If n5 is the number of rank-five array
// entries, y0 the number of selected rank-five singleton witnesses, and s
// the number of rank-at-most-four components, the sharp stability row is
// n5-y0+s<=2.  The selected rank-five chain boundaries give a different
// exact expression for y0 on each of the three allowed maximal chains:
//
//   A: y0=462+h1-h6,
//   B: y0=462+h1+h5-h4-h6,
//   C: y0=462+h1+h3-h2-h6.
//
// The sharp comparison is encoded under the corresponding exact-one chain
// selector.  It simultaneously implies s<=2 and duplicate excess<=1.
//
// The exact two-component escape has further physical consequences.  Its
// duplicate excess is zero, its two selected-witness slacks are {1,2}, one
// low component has coordinate union [11], and every adjacent pair in the
// slack-one component is a selected rank-five witness.  The last statement
// also makes every lower target represented there a singleton.  We encode
// these consequences without guessing target names: an exact two-component
// prefix automaton labels the first and second low runs, existential selector
// bits choose the coordinate-complete and slack-one runs, and the latter's
// adjacent pairs are required to occur in the existing selected rank-five
// schedule.
//
// Every gate below is bidirectional.  No variable is allocated and no clause
// is emitted when K11_FOREST_RANK_FILTRATION_TYPE2 is absent.
struct RankFiltrationTypeIIPlan {
    int& next;
    const LocalDensityPBPlan& local;
    const JointBandCutPlan& joint;
    bool expose_duplicate = false;
    int first_variable = 0;
    int variable_count = 0;
    int one = 0;
    long long rank_cap_clauses = 0;
    long long component_definition_clauses = 0;
    long long component_automaton_clauses = 0;
    long long coordinate_separator_clauses = 0;
    long long slack_one_pair_clauses = 0;
    vector<int> n5_count;
    vector<int> first_low_flags;
    vector<int> second_low_flags;
    int two_components_flag = 0;
    int slack_first_flag = 0;
    int slack_second_flag = 0;
    int duplicate_flag = 0;
    vector<vector<int>> clauses;

    RankFiltrationTypeIIPlan(int& next_variable,
                             const LocalDensityPBPlan& local_density,
                             const JointBandCutPlan& joint_band,
                             bool enable_duplicate_flag)
        : next(next_variable),
          local(local_density),
          joint(joint_band),
          expose_duplicate(enable_duplicate_flag),
          first_variable(next_variable),
          one(local_density.one) {
        build();
        variable_count = next - first_variable;
    }

    int fresh() { return next++; }
    void add(vector<int> clause) { clauses.push_back(std::move(clause)); }

    pair<int, int> full_adder(int a, int b, int carry) {
        const int sum = fresh();
        const int next_carry = fresh();
        for (int av = 0; av < 2; ++av)
            for (int bv = 0; bv < 2; ++bv)
                for (int cv = 0; cv < 2; ++cv) {
                    const int parity = av ^ bv ^ cv;
                    add({av ? -a : a, bv ? -b : b,
                         cv ? -carry : carry, parity ? sum : -sum});
                }
        add({-a, -b, next_carry});
        add({-a, -carry, next_carry});
        add({-b, -carry, next_carry});
        add({-next_carry, a, b});
        add({-next_carry, a, carry});
        add({-next_carry, b, carry});
        return {sum, next_carry};
    }

    vector<int> add_unsigned(const vector<int>& x, const vector<int>& y) {
        const int width = max(x.size(), y.size());
        vector<int> result;
        result.reserve(width + 1);
        int carry = -one;
        for (int bit = 0; bit < width; ++bit) {
            const int a = bit < static_cast<int>(x.size()) ? x[bit] : -one;
            const int b = bit < static_cast<int>(y.size()) ? y[bit] : -one;
            const auto [sum, next_carry] = full_adder(a, b, carry);
            result.push_back(sum);
            carry = next_carry;
        }
        result.push_back(carry);
        return result;
    }

    // Wallace compression leaves at most two literals per binary weight;
    // one final exact ripple addition materializes the full, nonmodular sum.
    vector<int> exact_count(const vector<int>& literals) {
        vector<vector<int>> buckets(2);
        buckets[0] = literals;
        for (size_t bit = 0; bit < buckets.size(); ++bit) {
            while (buckets[bit].size() >= 3) {
                const int a = buckets[bit].back();
                buckets[bit].pop_back();
                const int b = buckets[bit].back();
                buckets[bit].pop_back();
                const int c = buckets[bit].back();
                buckets[bit].pop_back();
                const auto [sum, carry] = full_adder(a, b, c);
                buckets[bit].push_back(sum);
                if (bit + 1 == buckets.size()) buckets.emplace_back();
                buckets[bit + 1].push_back(carry);
            }
        }
        while (buckets.size() > 1 && buckets.back().empty())
            buckets.pop_back();
        vector<int> first(buckets.size(), -one), second(buckets.size(), -one);
        for (size_t bit = 0; bit < buckets.size(); ++bit) {
            if (!buckets[bit].empty()) first[bit] = buckets[bit][0];
            if (buckets[bit].size() == 2) second[bit] = buckets[bit][1];
        }
        return add_unsigned(first, second);
    }

    vector<int> constant_bits(unsigned value) const {
        int width = 1;
        while ((1u << width) <= value) ++width;
        vector<int> result(width);
        for (int bit = 0; bit < width; ++bit)
            result[bit] = value & (1u << bit) ? one : -one;
        return result;
    }

    // Direct first-difference comparisons against constants need no
    // auxiliary equality chain.
    void add_leq_constant(const vector<int>& x, unsigned constant) {
        for (int bit = 0; bit < static_cast<int>(x.size()); ++bit) {
            if (constant & (1u << bit)) continue;
            vector<int> clause{-x[bit]};
            for (int higher = bit + 1;
                 higher < static_cast<int>(x.size()); ++higher)
                clause.push_back(constant & (1u << higher) ? -x[higher]
                                                            : x[higher]);
            add(std::move(clause));
        }
    }

    // Exact unsigned x<=y.  The bidirectional prefix-equality chain prevents
    // an auxiliary assignment from hiding the first unequal bit.
    void add_leq(vector<int> x, vector<int> y) {
        const int width = max(x.size(), y.size());
        x.resize(width, -one);
        y.resize(width, -one);
        int equal_above = one;
        for (int bit = width - 1; bit >= 0; --bit) {
            add({-equal_above, -x[bit], y[bit]});
            if (bit == 0) continue;
            const int next_equal = fresh();
            add({-next_equal, equal_above});
            add({-next_equal, -x[bit], y[bit]});
            add({-next_equal, x[bit], -y[bit]});
            add({-equal_above, -x[bit], -y[bit], next_equal});
            add({-equal_above, x[bit], y[bit], next_equal});
            equal_above = next_equal;
        }
    }

    // Exact unsigned x<=y, active only for the selected rank-five chain.
    // Inactive prefix-equality auxiliaries impose no accidental restriction.
    void add_leq_guarded(vector<int> x, vector<int> y, int guard) {
        const int width = max(x.size(), y.size());
        x.resize(width, -one);
        y.resize(width, -one);
        int equal_above = one;
        for (int bit = width - 1; bit >= 0; --bit) {
            add({-guard, -equal_above, -x[bit], y[bit]});
            if (bit == 0) continue;
            const int next_equal = fresh();
            add({-guard, -next_equal, equal_above});
            add({-guard, -next_equal, -x[bit], y[bit]});
            add({-guard, -next_equal, x[bit], -y[bit]});
            add({-guard, -equal_above, -x[bit], -y[bit], next_equal});
            add({-guard, -equal_above, x[bit], y[bit], next_equal});
            equal_above = next_equal;
        }
    }

    // out <-> (left & !right).
    void define_and_not(int out, int left, int right) {
        add({-out, left});
        add({-out, -right});
        add({out, -left, right});
        component_definition_clauses += 3;
    }

    // out <-> (x==y), for exact unsigned bit-vectors.  The two input sums
    // below are ordinary (nonmodular) counters, so equality is tested after
    // zero extension to a common width.
    int define_equal_flag(vector<int> x, vector<int> y) {
        const int width = max(x.size(), y.size());
        x.resize(width, -one);
        y.resize(width, -one);
        vector<int> equal_bits;
        equal_bits.reserve(width);
        for (int bit = 0; bit < width; ++bit) {
            const int equal = fresh();
            add({-equal, -x[bit], y[bit]});
            add({-equal, x[bit], -y[bit]});
            add({equal, x[bit], y[bit]});
            add({equal, -x[bit], -y[bit]});
            component_definition_clauses += 4;
            equal_bits.push_back(equal);
        }
        const int all_equal = fresh();
        for (int equal : equal_bits) {
            add({-all_equal, equal});
            ++component_definition_clauses;
        }
        vector<int> reverse{all_equal};
        for (int equal : equal_bits) reverse.push_back(-equal);
        add(std::move(reverse));
        ++component_definition_clauses;
        return all_equal;
    }

    // Exact signed-literal gates used by the component-prefix automaton.
    void define_or(int out, int left, int right) {
        add({-left, out});
        add({-right, out});
        add({-out, left, right});
        component_automaton_clauses += 3;
    }

    // out <-> left OR (middle AND right).
    void define_or_and(int out, int left, int middle, int right) {
        add({-left, out});
        add({-middle, -right, out});
        add({-out, left, middle});
        add({-out, left, right});
        component_automaton_clauses += 4;
    }

    void define_and(int out, int left, int right) {
        add({-out, left});
        add({-out, right});
        add({out, -left, -right});
        component_automaton_clauses += 3;
    }

    void define_and_not_automaton(int out, int left, int right) {
        add({-out, left});
        add({-out, -right});
        add({out, -left, right});
        component_automaton_clauses += 3;
    }

    void build() {
        // Type II has no literal rank-six entry and, more strongly, no entry
        // of rank above five.  LocalDensityPBPlan supplies exact rank flags.
        for (int position = 0; position < N; ++position)
            for (int rank = 6; rank <= K; ++rank) {
                add({-local.rank[position][rank]});
                ++rank_cap_clauses;
            }

        vector<int> rank_five;
        rank_five.reserve(N);
        for (int position = 0; position < N; ++position)
            rank_five.push_back(local.rank[position][5]);
        n5_count = exact_count(rank_five);
        const vector<int>& n5 = n5_count;
        add_leq_constant(n5, 134);

        // Since every nonzero entry now has rank at most five, rank<=4 is
        // exactly !rank5.  Count the starts of its physical components.
        vector<int> component_starts;
        component_starts.reserve(N);
        component_starts.push_back(-local.rank[0][5]);
        for (int position = 1; position < N; ++position) {
            const int start = fresh();
            define_and_not(start, local.rank[position - 1][5],
                           local.rank[position][5]);
            component_starts.push_back(start);
        }
        const vector<int> components = exact_count(component_starts);
        add_leq_constant(components, 2);

        // Encode n5-y0+components<=2 on the selected maximal chain.  Chains
        // B and C have the additional width-zero states 22 and 11,
        // respectively; omitting those blocks would unsoundly restrict the
        // search to chain A.
        auto H = [&](int j) {
            return vector<int>(joint.bits[j].begin(), joint.bits[j].end());
        };
        const vector<int> h1 = H(0), h2 = H(1), h3 = H(2);
        const vector<int> h4 = H(3), h5 = H(4), h6 = H(5);
        const vector<int> c464 = constant_bits(464);
        array<vector<int>, 3> stability_left{{
            add_unsigned(add_unsigned(n5, h6), components),
            add_unsigned(
                add_unsigned(add_unsigned(n5, h4), h6), components),
            add_unsigned(
                add_unsigned(add_unsigned(n5, h2), h6), components),
        }};
        array<vector<int>, 3> stability_right{{
            add_unsigned(h1, c464),
            add_unsigned(add_unsigned(h1, h5), c464),
            add_unsigned(add_unsigned(h1, h3), c464),
        }};
        for (int chain = 0; chain < 3; ++chain)
            add_leq_guarded(stability_left[chain], stability_right[chain],
                            joint.chain_selector[chain]);

        int stability_tight = 0;
        if (expose_duplicate) {
            array<int, 3> chain_equal{};
            for (int chain = 0; chain < 3; ++chain)
                chain_equal[chain] = define_equal_flag(
                    stability_left[chain], stability_right[chain]);

            // Select exactly the equality flag belonging to the active
            // chain.  Equalities on inactive chains cannot activate it.
            stability_tight = fresh();
            for (int chain = 0; chain < 3; ++chain) {
                add({-joint.chain_selector[chain], -chain_equal[chain],
                     stability_tight});
                add({-stability_tight, -joint.chain_selector[chain],
                     chain_equal[chain]});
                component_definition_clauses += 2;
            }
        }

        // Prefix automaton for the first and second physical low components.
        // seen_one[p] says that a low-component start has occurred by p;
        // seen_two[p] says that two starts have occurred.  The existing
        // exact comparison components<=2 makes seen_two[N-1] precisely the
        // two-component branch literal.
        vector<int> seen_one(N), seen_two(N);
        first_low_flags.resize(N);
        second_low_flags.resize(N);
        vector<int>& first_low = first_low_flags;
        vector<int>& second_low = second_low_flags;
        seen_one[0] = component_starts[0];
        seen_two[0] = -one;
        first_low[0] = -local.rank[0][5];
        second_low[0] = -one;
        for (int position = 1; position < N; ++position) {
            seen_one[position] = fresh();
            define_or(seen_one[position], seen_one[position - 1],
                      component_starts[position]);
            seen_two[position] = fresh();
            define_or_and(seen_two[position], seen_two[position - 1],
                          seen_one[position - 1], component_starts[position]);

            const int low = -local.rank[position][5];
            first_low[position] = fresh();
            define_and_not_automaton(first_low[position], low,
                                     seen_two[position]);
            second_low[position] = fresh();
            define_and(second_low[position], low, seen_two[position]);
        }
        two_components_flag = seen_two[N - 1];
        const int two_components = two_components_flag;

        // The audited stability identity is
        //
        //   n5-y0+components <= 2.
        //
        // Its only feasible cases are (delta,components)=(0,1),(1,1),
        // (0,2).  Thus the inequality is tight exactly in the latter two
        // cases, and duplicate excess one is precisely
        // stability_tight AND !two_components.
        if (expose_duplicate) {
            duplicate_flag = fresh();
            add({-duplicate_flag, stability_tight});
            add({-duplicate_flag, -two_components});
            add({duplicate_flag, -stability_tight, two_components});
            component_definition_clauses += 3;
        }

        auto exact_one_if = [&](int condition, int first, int second) {
            add({-condition, first, second});
            add({-first, condition});
            add({-second, condition});
            add({-first, -second});
        };

        // If there are two low components, choose one which contains every
        // coordinate.  First materialize the selected component exactly,
        // then use a deterministic prefix OR for each coordinate.  This is
        // larger than a one-way existential pick bank but avoids thousands
        // of symmetric occurrence witnesses in the SAT search.
        const int complete_first = fresh();
        const int complete_second = fresh();
        exact_one_if(two_components, complete_first, complete_second);
        coordinate_separator_clauses += 4;
        vector<int> chosen_low(N);
        for (int position = 0; position < N; ++position) {
            const int chosen = chosen_low[position] = fresh();
            add({-complete_first, -first_low[position], chosen});
            add({-complete_second, -second_low[position], chosen});
            add({-chosen, complete_first, complete_second});
            add({-chosen, -complete_first, first_low[position]});
            add({-chosen, -complete_second, second_low[position]});
            coordinate_separator_clauses += 5;
        }
        for (int bit = 0; bit < K; ++bit) {
            int has = fresh();
            const int first_entry = LocalDensityPBPlan::entry(0, bit);
            add({-has, chosen_low[0]});
            add({-has, first_entry});
            add({has, -chosen_low[0], -first_entry});
            coordinate_separator_clauses += 3;
            for (int position = 1; position < N; ++position) {
                const int next_has = fresh();
                const int entry = LocalDensityPBPlan::entry(position, bit);
                add({-has, next_has});
                add({-chosen_low[position], -entry, next_has});
                add({-next_has, has, chosen_low[position]});
                add({-next_has, has, entry});
                coordinate_separator_clauses += 4;
                has = next_has;
            }
            add({-two_components, has});
            ++coordinate_separator_clauses;
        }

        // Choose the slack-one component.  For a low component C of length
        // m, slack one is equivalent to selecting all m-1 internal adjacent
        // pairs as distinct rank-five witnesses.  The existing central row
        // already has exactly 462 distinct rank-five values, so forcing each
        // physical pair to occur in that row simultaneously gives rank five
        // and distinctness, with no new mask-assignment variables.
        slack_first_flag = fresh();
        slack_second_flag = fresh();
        const int slack_first = slack_first_flag;
        const int slack_second = slack_second_flag;
        exact_one_if(two_components, slack_first, slack_second);
        slack_one_pair_clauses += 4;
        for (int left = 0; left + 1 < N; ++left) {
            vector<int> support;
            for (int slot = max(0, left - 3);
                 slot <= min(MIDDLE - 1, left); ++slot) {
                const int alpha = left - slot;
                const int beta = left + 1 - slot;
                for (int state = 0; state < 10; ++state)
                    if (STATES[state].first == alpha &&
                        STATES[state].second == beta)
                        support.push_back(joint.rank_five.state[slot][state]);
            }

            vector<int> first_clause{-slack_first, -first_low[left],
                                     -first_low[left + 1]};
            first_clause.insert(first_clause.end(), support.begin(),
                                support.end());
            add(std::move(first_clause));
            vector<int> second_clause{-slack_second, -second_low[left],
                                      -second_low[left + 1]};
            second_clause.insert(second_clause.end(), support.begin(),
                                 support.end());
            add(std::move(second_clause));
            slack_one_pair_clauses += 2;
        }
    }

    int variables() const { return variable_count; }
};

// Optional coordinate-sensitive localization inside the exact Type-II
// two-component branch.  The selected slack-one component has every internal
// adjacent pair at rank five.  Hence any rank-at-most-four target which is
// not contained in the coordinate union of the slack-two component must
// occur literally in the slack-one component.
//
// If d is the coordinate deficit of the slack-two component and z=n5 is the
// number of (necessarily distinct) literal rank-five separators, the exact
// consequences used here are
//
//   d<=2,  d>=1 -> z<=96,  d>=2 -> z<=31,
//
// and the component-local rank counts
//
//   d>=1 -> (a1,a2,a3,a4)>=(1,10,45,120),
//   d>=2 -> (a1,a2,a3,a4)>=(2,19,81,204).
//
// Every gate is bidirectional.  The plan is dormant outside the selected
// two-component branch and introduces no target-name or witness variables.
struct TypeIITwoComponentPinPlan {
    int& next;
    const LocalDensityPBPlan& local;
    const RankFiltrationTypeIIPlan& type_two;
    int first_variable = 0;
    int variable_count = 0;
    int one = 0;
    long long membership_clauses = 0;
    long long coordinate_union_clauses = 0;
    long long deficit_clauses = 0;
    long long threshold_clauses = 0;
    long long rank_counter_clauses = 0;
    long long rank_row_clauses = 0;
    vector<int> slack_one_membership;
    vector<int> slack_two_membership;
    vector<int> slack_two_has;
    // Retain the exact per-coordinate occurrence bank.  The original
    // localization module already allocates and constrains these literals;
    // exposing them here changes neither its variable inventory nor its
    // clause stream and lets later exact counters reuse them at zero cost.
    array<vector<int>, K> slack_two_occurrence;
    array<vector<int>, 5> slack_one_rank_count;
    vector<vector<int>> clauses;

    TypeIITwoComponentPinPlan(
        int& next_variable, const LocalDensityPBPlan& local_density,
        const RankFiltrationTypeIIPlan& type_two_plan)
        : next(next_variable),
          local(local_density),
          type_two(type_two_plan),
          first_variable(next_variable),
          one(local_density.one) {
        build();
        variable_count = next - first_variable;
    }

    int fresh() { return next++; }
    void add(vector<int> clause) { clauses.push_back(std::move(clause)); }

    pair<int, int> full_adder(int a, int b, int carry) {
        const int sum = fresh();
        const int next_carry = fresh();
        for (int av = 0; av < 2; ++av)
            for (int bv = 0; bv < 2; ++bv)
                for (int cv = 0; cv < 2; ++cv) {
                    const int parity = av ^ bv ^ cv;
                    add({av ? -a : a, bv ? -b : b, cv ? -carry : carry,
                         parity ? sum : -sum});
                }
        add({-a, -b, next_carry});
        add({-a, -carry, next_carry});
        add({-b, -carry, next_carry});
        add({-next_carry, a, b});
        add({-next_carry, a, carry});
        add({-next_carry, b, carry});
        rank_counter_clauses += 14;
        return {sum, next_carry};
    }

    vector<int> add_unsigned(const vector<int>& x, const vector<int>& y) {
        const int width = max(x.size(), y.size());
        vector<int> result;
        result.reserve(width + 1);
        int carry = -one;
        for (int bit = 0; bit < width; ++bit) {
            const int a = bit < static_cast<int>(x.size()) ? x[bit] : -one;
            const int b = bit < static_cast<int>(y.size()) ? y[bit] : -one;
            const auto [sum, next_carry] = full_adder(a, b, carry);
            result.push_back(sum);
            carry = next_carry;
        }
        result.push_back(carry);
        return result;
    }

    vector<int> exact_count(const vector<int>& literals) {
        vector<vector<int>> buckets(2);
        buckets[0] = literals;
        for (size_t bit = 0; bit < buckets.size(); ++bit) {
            while (buckets[bit].size() >= 3) {
                const int a = buckets[bit].back();
                buckets[bit].pop_back();
                const int b = buckets[bit].back();
                buckets[bit].pop_back();
                const int c = buckets[bit].back();
                buckets[bit].pop_back();
                const auto [sum, carry] = full_adder(a, b, c);
                buckets[bit].push_back(sum);
                if (bit + 1 == buckets.size()) buckets.emplace_back();
                buckets[bit + 1].push_back(carry);
            }
        }
        while (buckets.size() > 1 && buckets.back().empty())
            buckets.pop_back();
        vector<int> first(buckets.size(), -one), second(buckets.size(), -one);
        for (size_t bit = 0; bit < buckets.size(); ++bit) {
            if (!buckets[bit].empty()) first[bit] = buckets[bit][0];
            if (buckets[bit].size() == 2) second[bit] = buckets[bit][1];
        }
        return add_unsigned(first, second);
    }

    // out is the component selected by (select_first,select_second).  The
    // selector pair is exact-one precisely under the two-component flag and
    // both selected component banks are exact physical memberships.
    void define_selected_component(int out, int select_first,
                                   int select_second, int first, int second) {
        add({-select_first, -first, out});
        add({-select_second, -second, out});
        add({-out, select_first, select_second});
        add({-out, -select_first, first});
        add({-out, -select_second, second});
        membership_clauses += 5;
    }

    void define_and(int out, int left, int right, long long& counter) {
        add({-out, left});
        add({-out, right});
        add({out, -left, -right});
        counter += 3;
    }

    // Enforce x<=constant when all literals in `escape` are false.
    void add_leq_constant_if(const vector<int>& x, unsigned constant,
                             const vector<int>& escape) {
        for (int bit = 0; bit < static_cast<int>(x.size()); ++bit) {
            if (constant & (1u << bit)) continue;
            vector<int> clause = escape;
            clause.push_back(-x[bit]);
            for (int higher = bit + 1;
                 higher < static_cast<int>(x.size()); ++higher)
                clause.push_back(constant & (1u << higher) ? -x[higher]
                                                            : x[higher]);
            add(std::move(clause));
            ++threshold_clauses;
        }
    }

    // Enforce constant<=x when all literals in `escape` are false.
    void add_constant_leq_if(unsigned constant, const vector<int>& x,
                             const vector<int>& escape) {
        for (int bit = 0; bit < static_cast<int>(x.size()); ++bit) {
            if (!(constant & (1u << bit))) continue;
            vector<int> clause = escape;
            clause.push_back(x[bit]);
            for (int higher = bit + 1;
                 higher < static_cast<int>(x.size()); ++higher)
                clause.push_back(constant & (1u << higher) ? -x[higher]
                                                            : x[higher]);
            add(std::move(clause));
            ++rank_row_clauses;
        }
    }

    void build() {
        const int two_components = type_two.two_components_flag;
        const int slack_first = type_two.slack_first_flag;
        const int slack_second = type_two.slack_second_flag;

        slack_one_membership.resize(N);
        slack_two_membership.resize(N);
        for (int position = 0; position < N; ++position) {
            const int in_one = slack_one_membership[position] = fresh();
            define_selected_component(
                in_one, slack_first, slack_second,
                type_two.first_low_flags[position],
                type_two.second_low_flags[position]);

            const int in_two = slack_two_membership[position] = fresh();
            define_selected_component(
                in_two, slack_first, slack_second,
                type_two.second_low_flags[position],
                type_two.first_low_flags[position]);
        }

        // Exact coordinate union of the selected slack-two component.
        slack_two_has.resize(K);
        for (int bit = 0; bit < K; ++bit) {
            vector<int>& occurrences = slack_two_occurrence[bit];
            occurrences.reserve(N);
            const int has = slack_two_has[bit] = fresh();
            for (int position = 0; position < N; ++position) {
                const int occurrence = fresh();
                define_and(occurrence, slack_two_membership[position],
                           LocalDensityPBPlan::entry(position, bit),
                           coordinate_union_clauses);
                add({-occurrence, has});
                ++coordinate_union_clauses;
                occurrences.push_back(occurrence);
            }
            vector<int> reverse{-has};
            reverse.insert(reverse.end(), occurrences.begin(),
                           occurrences.end());
            add(std::move(reverse));
            ++coordinate_union_clauses;
        }

        // Under two components, at most two coordinate-union bits may be
        // absent from the slack-two component.
        for (int a = 0; a < K; ++a)
            for (int b = a + 1; b < K; ++b)
                for (int c = b + 1; c < K; ++c) {
                    add({-two_components, slack_two_has[a],
                         slack_two_has[b], slack_two_has[c]});
                    ++deficit_clauses;
                }

        // Missing one coordinate forces z=n5<=96; missing two force z<=31.
        for (int bit = 0; bit < K; ++bit)
            add_leq_constant_if(type_two.n5_count, 96,
                                {-two_components, slack_two_has[bit]});
        for (int a = 0; a < K; ++a)
            for (int b = a + 1; b < K; ++b)
                add_leq_constant_if(
                    type_two.n5_count, 31,
                    {-two_components, slack_two_has[a], slack_two_has[b]});

        // Count literal entry ranks one through four inside the selected
        // slack-one component.  Slack-one rigidity makes these counts at
        // least the numbers of lower masks meeting the slack-two deficit.
        for (int rank = 1; rank <= 4; ++rank) {
            vector<int> literals;
            literals.reserve(N);
            for (int position = 0; position < N; ++position) {
                const int selected = fresh();
                define_and(selected, slack_one_membership[position],
                           local.rank[position][rank], rank_counter_clauses);
                literals.push_back(selected);
            }
            slack_one_rank_count[rank] = exact_count(literals);
        }

        constexpr array<unsigned, 4> row_one{{1, 10, 45, 120}};
        constexpr array<unsigned, 4> row_two{{2, 19, 81, 204}};
        for (int bit = 0; bit < K; ++bit)
            for (int rank = 1; rank <= 4; ++rank)
                add_constant_leq_if(
                    row_one[rank - 1], slack_one_rank_count[rank],
                    {-two_components, slack_two_has[bit]});
        for (int a = 0; a < K; ++a)
            for (int b = a + 1; b < K; ++b)
                for (int rank = 1; rank <= 4; ++rank)
                    add_constant_leq_if(
                        row_two[rank - 1], slack_one_rank_count[rank],
                        {-two_components, slack_two_has[a],
                         slack_two_has[b]});
    }

    int variables() const { return variable_count; }
};

// Optional reverse coordinate-load inequalities in the exact Type-II
// two-component branch.  Let C1 be the selected slack-one component, C2 the
// selected slack-two component, and
//
//   o_b = #{p in C2 : b in A[p]}.
//
// If b is absent from C1, the audited reverse pin theorem gives
//
//   o_b >= 59,
//   3*o_b + z + y2 >= 386.
//
// In the two-component branch z=y0, and all three admissible rank-five
// chains satisfy
//
//   y0+y2 = 462+h1+h3+h5-h2-h4-h6.
//
// The coupled row is therefore encoded without a chain case split as
//
//   h2+h4+h6 <= 3*o_b+h1+h3+h5+76.
//
// Every occurrence, counter, sum, and guarded prefix-equality gate is exact.
// The 5,115 C2 occurrence literals are reused from
// TypeIITwoComponentPinPlan and cost no new variables or clauses here.
struct TypeIIReversePinLoadPlan {
    int& next;
    const LocalDensityPBPlan& local;
    const JointBandCutPlan& joint;
    const RankFiltrationTypeIIPlan& type_two;
    const TypeIITwoComponentPinPlan& pin;
    int first_variable = 0;
    int variable_count = 0;
    int one = 0;
    long long slack_one_union_variable_count = 0;
    long long slack_one_union_clauses = 0;
    long long occurrence_counter_variable_count = 0;
    long long occurrence_counter_clauses = 0;
    long long arithmetic_variable_count = 0;
    long long arithmetic_clauses = 0;
    long long threshold_clauses = 0;
    vector<int> slack_one_has;
    array<vector<int>, K> slack_one_occurrence;
    array<vector<int>, K> slack_two_occurrence_count;
    vector<vector<int>> clauses;

    TypeIIReversePinLoadPlan(
        int& next_variable, const LocalDensityPBPlan& local_density,
        const JointBandCutPlan& joint_band,
        const RankFiltrationTypeIIPlan& type_two_plan,
        const TypeIITwoComponentPinPlan& pin_plan)
        : next(next_variable),
          local(local_density),
          joint(joint_band),
          type_two(type_two_plan),
          pin(pin_plan),
          first_variable(next_variable),
          one(local_density.one) {
        build();
        variable_count = next - first_variable;
    }

    int fresh() { return next++; }
    void add(vector<int> clause) { clauses.push_back(std::move(clause)); }

    pair<int, int> full_adder(int a, int b, int carry,
                              long long& variable_counter,
                              long long& clause_counter) {
        const int sum = fresh();
        const int next_carry = fresh();
        variable_counter += 2;
        for (int av = 0; av < 2; ++av)
            for (int bv = 0; bv < 2; ++bv)
                for (int cv = 0; cv < 2; ++cv) {
                    const int parity = av ^ bv ^ cv;
                    add({av ? -a : a, bv ? -b : b, cv ? -carry : carry,
                         parity ? sum : -sum});
                }
        add({-a, -b, next_carry});
        add({-a, -carry, next_carry});
        add({-b, -carry, next_carry});
        add({-next_carry, a, b});
        add({-next_carry, a, carry});
        add({-next_carry, b, carry});
        clause_counter += 14;
        return {sum, next_carry};
    }

    vector<int> add_unsigned(const vector<int>& x, const vector<int>& y,
                             long long& variable_counter,
                             long long& clause_counter) {
        const int width = max(x.size(), y.size());
        vector<int> result;
        result.reserve(width + 1);
        int carry = -one;
        for (int bit = 0; bit < width; ++bit) {
            const int a = bit < static_cast<int>(x.size()) ? x[bit] : -one;
            const int b = bit < static_cast<int>(y.size()) ? y[bit] : -one;
            const auto [sum, next_carry] =
                full_adder(a, b, carry, variable_counter, clause_counter);
            result.push_back(sum);
            carry = next_carry;
        }
        result.push_back(carry);
        return result;
    }

    // Wallace compression leaves at most two literals at each weight.  The
    // final ripple retains its last carry, so this is the ordinary integer
    // count rather than a modular sum.
    vector<int> exact_count(const vector<int>& literals) {
        vector<vector<int>> buckets(2);
        buckets[0] = literals;
        for (size_t bit = 0; bit < buckets.size(); ++bit) {
            while (buckets[bit].size() >= 3) {
                const int a = buckets[bit].back();
                buckets[bit].pop_back();
                const int b = buckets[bit].back();
                buckets[bit].pop_back();
                const int c = buckets[bit].back();
                buckets[bit].pop_back();
                const auto [sum, carry] = full_adder(
                    a, b, c, occurrence_counter_variable_count,
                    occurrence_counter_clauses);
                buckets[bit].push_back(sum);
                if (bit + 1 == buckets.size()) buckets.emplace_back();
                buckets[bit + 1].push_back(carry);
            }
        }
        while (buckets.size() > 1 && buckets.back().empty())
            buckets.pop_back();
        vector<int> first(buckets.size(), -one), second(buckets.size(), -one);
        for (size_t bit = 0; bit < buckets.size(); ++bit) {
            if (!buckets[bit].empty()) first[bit] = buckets[bit][0];
            if (buckets[bit].size() == 2) second[bit] = buckets[bit][1];
        }
        return add_unsigned(first, second, occurrence_counter_variable_count,
                            occurrence_counter_clauses);
    }

    vector<int> constant_bits(unsigned value) const {
        int width = 1;
        while ((1u << width) <= value) ++width;
        vector<int> result(width);
        for (int bit = 0; bit < width; ++bit)
            result[bit] = value & (1u << bit) ? one : -one;
        return result;
    }

    // Enforce constant<=x whenever every escape literal is false.  The
    // direct first-difference encoding needs one clause per set bit of the
    // constant and no auxiliary variable.
    void add_constant_leq_if(unsigned constant, const vector<int>& x,
                             const vector<int>& escape) {
        for (int bit = 0; bit < static_cast<int>(x.size()); ++bit) {
            if (!(constant & (1u << bit))) continue;
            vector<int> clause = escape;
            clause.push_back(x[bit]);
            for (int higher = bit + 1;
                 higher < static_cast<int>(x.size()); ++higher)
                clause.push_back(constant & (1u << higher) ? -x[higher]
                                                            : x[higher]);
            add(std::move(clause));
            ++threshold_clauses;
        }
    }

    // Exact unsigned x<=y under a disjunctive escape.  Prefix equality is
    // bidirectional on the active branch, and every definition is escaped so
    // inactive auxiliaries cannot constrain the surrounding formula.
    void add_leq_if(vector<int> x, vector<int> y,
                    const vector<int>& escape) {
        const int width = max(x.size(), y.size());
        x.resize(width, -one);
        y.resize(width, -one);
        int equal_above = one;
        auto add_escaped = [&](initializer_list<int> tail) {
            vector<int> clause = escape;
            clause.insert(clause.end(), tail.begin(), tail.end());
            add(std::move(clause));
            ++arithmetic_clauses;
        };
        for (int bit = width - 1; bit >= 0; --bit) {
            add_escaped({-equal_above, -x[bit], y[bit]});
            if (bit == 0) continue;
            const int next_equal = fresh();
            ++arithmetic_variable_count;
            add_escaped({-next_equal, equal_above});
            add_escaped({-next_equal, -x[bit], y[bit]});
            add_escaped({-next_equal, x[bit], -y[bit]});
            add_escaped({-equal_above, -x[bit], -y[bit], next_equal});
            add_escaped({-equal_above, x[bit], y[bit], next_equal});
            equal_above = next_equal;
        }
    }

    void build() {
        const int two_components = type_two.two_components_flag;

        // Exact coordinate union of C1.
        slack_one_has.resize(K);
        for (int bit = 0; bit < K; ++bit) {
            const int has = slack_one_has[bit] = fresh();
            ++slack_one_union_variable_count;
            vector<int>& occurrences = slack_one_occurrence[bit];
            occurrences.reserve(N);
            for (int position = 0; position < N; ++position) {
                const int occurrence = fresh();
                ++slack_one_union_variable_count;
                add({-occurrence, pin.slack_one_membership[position]});
                add({-occurrence,
                     LocalDensityPBPlan::entry(position, bit)});
                add({occurrence, -pin.slack_one_membership[position],
                     -LocalDensityPBPlan::entry(position, bit)});
                add({-occurrence, has});
                slack_one_union_clauses += 4;
                occurrences.push_back(occurrence);
            }
            vector<int> reverse{-has};
            reverse.insert(reverse.end(), occurrences.begin(),
                           occurrences.end());
            add(std::move(reverse));
            ++slack_one_union_clauses;
        }

        // Reuse the existing exact C2 occurrence flags and count o_b.
        for (int bit = 0; bit < K; ++bit) {
            if (static_cast<int>(pin.slack_two_occurrence[bit].size()) != N)
                throw runtime_error("missing retained slack-two occurrence bank");
            slack_two_occurrence_count[bit] =
                exact_count(pin.slack_two_occurrence[bit]);
            add_constant_leq_if(
                59, slack_two_occurrence_count[bit],
                {-two_components, slack_one_has[bit]});
        }

        auto H = [&](int j) {
            return vector<int>(joint.bits[j].begin(), joint.bits[j].end());
        };
        const vector<int> h1 = H(0), h2 = H(1), h3 = H(2);
        const vector<int> h4 = H(3), h5 = H(4), h6 = H(5);

        // Shared chain-independent boundary arithmetic.
        const vector<int> left_24 =
            add_unsigned(h2, h4, arithmetic_variable_count,
                         arithmetic_clauses);
        const vector<int> left =
            add_unsigned(left_24, h6, arithmetic_variable_count,
                         arithmetic_clauses);
        const vector<int> right_13 =
            add_unsigned(h1, h3, arithmetic_variable_count,
                         arithmetic_clauses);
        const vector<int> right_5c =
            add_unsigned(h5, constant_bits(76), arithmetic_variable_count,
                         arithmetic_clauses);
        const vector<int> right_core =
            add_unsigned(right_13, right_5c, arithmetic_variable_count,
                         arithmetic_clauses);

        for (int bit = 0; bit < K; ++bit) {
            const vector<int>& occurrence_count =
                slack_two_occurrence_count[bit];
            vector<int> doubled{-one};
            doubled.insert(doubled.end(), occurrence_count.begin(),
                           occurrence_count.end());
            const vector<int> triple =
                add_unsigned(occurrence_count, doubled,
                             arithmetic_variable_count, arithmetic_clauses);
            const vector<int> right =
                add_unsigned(triple, right_core, arithmetic_variable_count,
                             arithmetic_clauses);
            add_leq_if(left, right,
                       {-two_components, slack_one_has[bit]});
        }
    }

    int variables() const { return variable_count; }
};

// Optional companion coordinate-load inequalities in the exact Type-II
// two-component branch.  Let C1 be the selected slack-one component and C2
// the selected slack-two component.  If a coordinate b is absent from C2,
// all 176 lower masks of ranks one through four that contain b must occur
// literally in C1, and the 210 rank-five masks containing b force
//
//   #{p in C1 : b in A[p]} >= 176,
//   |C1| + z >= 211,
//
// where z is the number of literal rank-five separators.  The first row
// reuses the exact C1 occurrence bank retained by TypeIIReversePinLoadPlan.
// The second reuses the four exact C1 rank counters and the exact z counter.
// No occurrence conjunction is rebuilt here.
struct TypeIICompanionPinLoadPlan {
    int& next;
    const RankFiltrationTypeIIPlan& type_two;
    const TypeIITwoComponentPinPlan& pin;
    const TypeIIReversePinLoadPlan& reverse;
    int first_variable = 0;
    int variable_count = 0;
    int one = 0;
    long long occurrence_counter_variable_count = 0;
    long long occurrence_counter_clauses = 0;
    long long arithmetic_variable_count = 0;
    long long arithmetic_clauses = 0;
    long long threshold_clauses = 0;
    array<vector<int>, K> slack_one_occurrence_count;
    vector<vector<int>> clauses;

    TypeIICompanionPinLoadPlan(
        int& next_variable, const RankFiltrationTypeIIPlan& type_two_plan,
        const TypeIITwoComponentPinPlan& pin_plan,
        const TypeIIReversePinLoadPlan& reverse_plan)
        : next(next_variable),
          type_two(type_two_plan),
          pin(pin_plan),
          reverse(reverse_plan),
          first_variable(next_variable),
          one(reverse_plan.one) {
        build();
        variable_count = next - first_variable;
    }

    int fresh() { return next++; }
    void add(vector<int> clause) { clauses.push_back(std::move(clause)); }

    pair<int, int> full_adder(int a, int b, int carry,
                              long long& variable_counter,
                              long long& clause_counter) {
        const int sum = fresh();
        const int next_carry = fresh();
        variable_counter += 2;
        for (int av = 0; av < 2; ++av)
            for (int bv = 0; bv < 2; ++bv)
                for (int cv = 0; cv < 2; ++cv) {
                    const int parity = av ^ bv ^ cv;
                    add({av ? -a : a, bv ? -b : b, cv ? -carry : carry,
                         parity ? sum : -sum});
                }
        add({-a, -b, next_carry});
        add({-a, -carry, next_carry});
        add({-b, -carry, next_carry});
        add({-next_carry, a, b});
        add({-next_carry, a, carry});
        add({-next_carry, b, carry});
        clause_counter += 14;
        return {sum, next_carry};
    }

    vector<int> add_unsigned(const vector<int>& x, const vector<int>& y,
                             long long& variable_counter,
                             long long& clause_counter) {
        const int width = max(x.size(), y.size());
        vector<int> result;
        result.reserve(width + 1);
        int carry = -one;
        for (int bit = 0; bit < width; ++bit) {
            const int a = bit < static_cast<int>(x.size()) ? x[bit] : -one;
            const int b = bit < static_cast<int>(y.size()) ? y[bit] : -one;
            const auto [sum, next_carry] =
                full_adder(a, b, carry, variable_counter, clause_counter);
            result.push_back(sum);
            carry = next_carry;
        }
        result.push_back(carry);
        return result;
    }

    vector<int> exact_count(const vector<int>& literals) {
        vector<vector<int>> buckets(2);
        buckets[0] = literals;
        for (size_t bit = 0; bit < buckets.size(); ++bit) {
            while (buckets[bit].size() >= 3) {
                const int a = buckets[bit].back();
                buckets[bit].pop_back();
                const int b = buckets[bit].back();
                buckets[bit].pop_back();
                const int c = buckets[bit].back();
                buckets[bit].pop_back();
                const auto [sum, carry] = full_adder(
                    a, b, c, occurrence_counter_variable_count,
                    occurrence_counter_clauses);
                buckets[bit].push_back(sum);
                if (bit + 1 == buckets.size()) buckets.emplace_back();
                buckets[bit + 1].push_back(carry);
            }
        }
        while (buckets.size() > 1 && buckets.back().empty())
            buckets.pop_back();
        vector<int> first(buckets.size(), -one), second(buckets.size(), -one);
        for (size_t bit = 0; bit < buckets.size(); ++bit) {
            if (!buckets[bit].empty()) first[bit] = buckets[bit][0];
            if (buckets[bit].size() == 2) second[bit] = buckets[bit][1];
        }
        return add_unsigned(first, second, occurrence_counter_variable_count,
                            occurrence_counter_clauses);
    }

    // Enforce constant<=x whenever every escape literal is false.
    void add_constant_leq_if(unsigned constant, const vector<int>& x,
                             const vector<int>& escape) {
        for (int bit = 0; bit < static_cast<int>(x.size()); ++bit) {
            if (!(constant & (1u << bit))) continue;
            vector<int> clause = escape;
            clause.push_back(x[bit]);
            for (int higher = bit + 1;
                 higher < static_cast<int>(x.size()); ++higher)
                clause.push_back(constant & (1u << higher) ? -x[higher]
                                                            : x[higher]);
            add(std::move(clause));
            ++threshold_clauses;
        }
    }

    void build() {
        const int two_components = type_two.two_components_flag;

        for (int bit = 0; bit < K; ++bit) {
            if (static_cast<int>(reverse.slack_one_occurrence[bit].size()) != N)
                throw runtime_error("missing retained slack-one occurrence bank");
            slack_one_occurrence_count[bit] =
                exact_count(reverse.slack_one_occurrence[bit]);
            add_constant_leq_if(
                176, slack_one_occurrence_count[bit],
                {-two_components, pin.slack_two_has[bit]});
        }

        // C1 contains only ranks one through four.  Sum the exact retained
        // rank counters once, add z, and share the result across all eleven
        // named-coordinate guards.
        const vector<int> n1_12 =
            add_unsigned(pin.slack_one_rank_count[1],
                         pin.slack_one_rank_count[2],
                         arithmetic_variable_count, arithmetic_clauses);
        const vector<int> n1_34 =
            add_unsigned(pin.slack_one_rank_count[3],
                         pin.slack_one_rank_count[4],
                         arithmetic_variable_count, arithmetic_clauses);
        const vector<int> n1 =
            add_unsigned(n1_12, n1_34, arithmetic_variable_count,
                         arithmetic_clauses);
        const vector<int> n1z =
            add_unsigned(n1, type_two.n5_count, arithmetic_variable_count,
                         arithmetic_clauses);
        for (int bit = 0; bit < K; ++bit)
            add_constant_leq_if(211, n1z,
                                {-two_components, pin.slack_two_has[bit]});
    }

    int variables() const { return variable_count; }
};

// Optional exact array-level encoding of the one-literal-six-set branch of
// rank-filtration stability.  The surrounding rank-six branch-one module
// already fixes A[0]=63 and forbids every other literal rank-six entry.  This
// plan encodes the exact next peel on positions 1,...,464:
//
//   * every suffix entry has rank at most five;
//   * at most 133 entries have rank five;
//   * the suffix rank-at-most-four positions form exactly one component; and
//   * literal rank-five values are all distinct.
//
// As in Type II, choose one singleton selected witness for every distinct
// literal rank-five value.  Then delta_5=0 is n5=y0.  The exact y0 formula
// depends on the selected maximal chain, so all three duplicate-free
// equalities are guarded by their exact-one chain selectors.
//
// No variable is allocated and no clause is emitted when
// K11_FOREST_RANK_FILTRATION_TYPE1 is absent.
struct RankFiltrationTypeIPlan {
    int& next;
    const LocalDensityPBPlan& local;
    const JointBandCutPlan& joint;
    int first_variable = 0;
    int variable_count = 0;
    int one = 0;
    long long rank_cap_clauses = 0;
    long long component_definition_clauses = 0;
    vector<vector<int>> clauses;

    RankFiltrationTypeIPlan(int& next_variable,
                            const LocalDensityPBPlan& local_density,
                            const JointBandCutPlan& joint_band)
        : next(next_variable),
          local(local_density),
          joint(joint_band),
          first_variable(next_variable),
          one(local_density.one) {
        build();
        variable_count = next - first_variable;
    }

    int fresh() { return next++; }
    void add(vector<int> clause) { clauses.push_back(std::move(clause)); }

    pair<int, int> full_adder(int a, int b, int carry) {
        const int sum = fresh();
        const int next_carry = fresh();
        for (int av = 0; av < 2; ++av)
            for (int bv = 0; bv < 2; ++bv)
                for (int cv = 0; cv < 2; ++cv) {
                    const int parity = av ^ bv ^ cv;
                    add({av ? -a : a, bv ? -b : b,
                         cv ? -carry : carry, parity ? sum : -sum});
                }
        add({-a, -b, next_carry});
        add({-a, -carry, next_carry});
        add({-b, -carry, next_carry});
        add({-next_carry, a, b});
        add({-next_carry, a, carry});
        add({-next_carry, b, carry});
        return {sum, next_carry};
    }

    vector<int> add_unsigned(const vector<int>& x, const vector<int>& y) {
        const int width = max(x.size(), y.size());
        vector<int> result;
        result.reserve(width + 1);
        int carry = -one;
        for (int bit = 0; bit < width; ++bit) {
            const int a = bit < static_cast<int>(x.size()) ? x[bit] : -one;
            const int b = bit < static_cast<int>(y.size()) ? y[bit] : -one;
            const auto [sum, next_carry] = full_adder(a, b, carry);
            result.push_back(sum);
            carry = next_carry;
        }
        // Retain the final carry: every count and boundary sum in this plan
        // is an ordinary integer, never a modular residue.
        result.push_back(carry);
        return result;
    }

    vector<int> exact_count(const vector<int>& literals) {
        vector<vector<int>> buckets(2);
        buckets[0] = literals;
        for (size_t bit = 0; bit < buckets.size(); ++bit) {
            while (buckets[bit].size() >= 3) {
                const int a = buckets[bit].back();
                buckets[bit].pop_back();
                const int b = buckets[bit].back();
                buckets[bit].pop_back();
                const int c = buckets[bit].back();
                buckets[bit].pop_back();
                const auto [sum, carry] = full_adder(a, b, c);
                buckets[bit].push_back(sum);
                if (bit + 1 == buckets.size()) buckets.emplace_back();
                buckets[bit + 1].push_back(carry);
            }
        }
        while (buckets.size() > 1 && buckets.back().empty())
            buckets.pop_back();
        vector<int> first(buckets.size(), -one), second(buckets.size(), -one);
        for (size_t bit = 0; bit < buckets.size(); ++bit) {
            if (!buckets[bit].empty()) first[bit] = buckets[bit][0];
            if (buckets[bit].size() == 2) second[bit] = buckets[bit][1];
        }
        return add_unsigned(first, second);
    }

    vector<int> constant_bits(unsigned value) const {
        int width = 1;
        while ((1u << width) <= value) ++width;
        vector<int> result(width);
        for (int bit = 0; bit < width; ++bit)
            result[bit] = value & (1u << bit) ? one : -one;
        return result;
    }

    void add_leq_constant(const vector<int>& x, unsigned constant) {
        for (int bit = 0; bit < static_cast<int>(x.size()); ++bit) {
            if (constant & (1u << bit)) continue;
            vector<int> clause{-x[bit]};
            for (int higher = bit + 1;
                 higher < static_cast<int>(x.size()); ++higher)
                clause.push_back(constant & (1u << higher) ? -x[higher]
                                                            : x[higher]);
            add(std::move(clause));
        }
    }

    void add_equal(vector<int> x, vector<int> y) {
        const int width = max(x.size(), y.size());
        x.resize(width, -one);
        y.resize(width, -one);
        for (int bit = 0; bit < width; ++bit) {
            add({-x[bit], y[bit]});
            add({x[bit], -y[bit]});
        }
    }

    void add_equal_guarded(vector<int> x, vector<int> y, int guard) {
        const int width = max(x.size(), y.size());
        x.resize(width, -one);
        y.resize(width, -one);
        for (int bit = 0; bit < width; ++bit) {
            add({-guard, -x[bit], y[bit]});
            add({-guard, x[bit], -y[bit]});
        }
    }

    void define_and_not(int out, int left, int right) {
        add({-out, left});
        add({-out, -right});
        add({out, -left, right});
        component_definition_clauses += 3;
    }

    void build() {
        // Branch one has already fixed A[0] to rank six.  Exact rank-five
        // equality applies to the compressed suffix positions 1,...,464.
        for (int position = 1; position < N; ++position)
            for (int rank = 6; rank <= K; ++rank) {
                add({-local.rank[position][rank]});
                ++rank_cap_clauses;
            }

        vector<int> rank_five;
        rank_five.reserve(N);
        for (int position = 0; position < N; ++position)
            rank_five.push_back(local.rank[position][5]);
        const vector<int> n5 = exact_count(rank_five);
        add_leq_constant(n5, 133);

        // Count low components in the 464-position suffix.  Position one is
        // its own left boundary; later starts are high-to-low transitions.
        vector<int> component_starts;
        component_starts.reserve(N - 1);
        component_starts.push_back(-local.rank[1][5]);
        for (int position = 2; position < N; ++position) {
            const int start = fresh();
            define_and_not(start, local.rank[position - 1][5],
                           local.rank[position][5]);
            component_starts.push_back(start);
        }
        const vector<int> components = exact_count(component_starts);
        for (int bit = 0; bit < static_cast<int>(components.size()); ++bit)
            add({bit == 0 ? components[bit] : -components[bit]});

        // Exact duplicate-free row n5=y0 on each allowed maximal chain:
        //   A: n5+h6       = h1+462,
        //   B: n5+h4+h6    = h1+h5+462,
        //   C: n5+h2+h6    = h1+h3+462.
        auto H = [&](int j) {
            return vector<int>(joint.bits[j].begin(), joint.bits[j].end());
        };
        const vector<int> h1 = H(0), h2 = H(1), h3 = H(2);
        const vector<int> h4 = H(3), h5 = H(4), h6 = H(5);
        const vector<int> c462 = constant_bits(462);
        array<vector<int>, 3> left{{
            add_unsigned(n5, h6),
            add_unsigned(add_unsigned(n5, h4), h6),
            add_unsigned(add_unsigned(n5, h2), h6),
        }};
        array<vector<int>, 3> right{{
            add_unsigned(h1, c462),
            add_unsigned(add_unsigned(h1, h5), c462),
            add_unsigned(add_unsigned(h1, h3), c462),
        }};
        for (int chain = 0; chain < 3; ++chain)
            add_equal_guarded(left[chain], right[chain],
                              joint.chain_selector[chain]);
    }

    int variables() const { return variable_count; }
};

// Optional exact production encoding of the audited rank-seven truncated
// width moment.  The proof actually establishes
//
//   sum min(width_7,4) >= 930  in Type II,
//   sum min(width_7,4) >= 940  in Type I.
//
// Adjacent-shadow compression exposes a crossed witness for every active
// rank-seven target and six generic slots cover the inactive exceptions.
// Give an inactive target its maximum possible truncated credit four.  An
// active target already contributes the unavoidable width-one unit; three
// virtual literals certify the additional thresholds two, three, and four.
// Counting false virtual literals therefore gives the exact safe projections
//
//   deficits <= 390  in Type II,
//   deficits <= 380  in Type I.
//
// No containment cap is needed: only widths through four are used.  Every
// implication involving the otherwise-free crossed interval is guarded by
// active, so inactive virtual credit does not constrain that interval.
struct RankSevenTruncatedWidthPlan {
    int& next;
    const vector<RankSevenShadow>& shadows;
    bool type_one = false;
    int first_variable = 0;
    int variable_count = 0;
    int one = 0;
    int credit_variable_count = 0;
    int counter_variable_count = 0;
    long long location_clauses = 0;
    long long inactive_credit_clauses = 0;
    long long counter_clauses = 0;
    long long comparator_clauses = 0;
    vector<vector<int>> clauses;

    RankSevenTruncatedWidthPlan(int& next_variable,
                                const vector<RankSevenShadow>& rank_seven,
                                bool enable_type_one, int constant_one)
        : next(next_variable),
          shadows(rank_seven),
          type_one(enable_type_one),
          first_variable(next_variable),
          one(constant_one) {
        build();
        variable_count = next - first_variable;
    }

    int fresh() { return next++; }
    void add(vector<int> clause) { clauses.push_back(std::move(clause)); }

    pair<int, int> full_adder(int a, int b, int carry) {
        const int sum = fresh();
        const int next_carry = fresh();
        for (int av = 0; av < 2; ++av)
            for (int bv = 0; bv < 2; ++bv)
                for (int cv = 0; cv < 2; ++cv) {
                    const int parity = av ^ bv ^ cv;
                    add({av ? -a : a, bv ? -b : b,
                         cv ? -carry : carry, parity ? sum : -sum});
                }
        add({-a, -b, next_carry});
        add({-a, -carry, next_carry});
        add({-b, -carry, next_carry});
        add({-next_carry, a, b});
        add({-next_carry, a, carry});
        add({-next_carry, b, carry});
        counter_clauses += 14;
        return {sum, next_carry};
    }

    vector<int> add_unsigned(const vector<int>& x, const vector<int>& y) {
        const int width = max(x.size(), y.size());
        vector<int> result;
        result.reserve(width + 1);
        int carry = -one;
        for (int bit = 0; bit < width; ++bit) {
            const int a = bit < static_cast<int>(x.size()) ? x[bit] : -one;
            const int b = bit < static_cast<int>(y.size()) ? y[bit] : -one;
            const auto [sum, next_carry] = full_adder(a, b, carry);
            result.push_back(sum);
            carry = next_carry;
        }
        result.push_back(carry);
        return result;
    }

    vector<int> exact_count(const vector<int>& literals) {
        vector<vector<int>> buckets(2);
        buckets[0] = literals;
        for (size_t bit = 0; bit < buckets.size(); ++bit) {
            while (buckets[bit].size() >= 3) {
                const int a = buckets[bit].back();
                buckets[bit].pop_back();
                const int b = buckets[bit].back();
                buckets[bit].pop_back();
                const int c = buckets[bit].back();
                buckets[bit].pop_back();
                const auto [sum, carry] = full_adder(a, b, c);
                buckets[bit].push_back(sum);
                if (bit + 1 == buckets.size()) buckets.emplace_back();
                buckets[bit + 1].push_back(carry);
            }
        }
        while (buckets.size() > 1 && buckets.back().empty())
            buckets.pop_back();
        vector<int> first(buckets.size(), -one), second(buckets.size(), -one);
        for (size_t bit = 0; bit < buckets.size(); ++bit) {
            if (!buckets[bit].empty()) first[bit] = buckets[bit][0];
            if (buckets[bit].size() == 2) second[bit] = buckets[bit][1];
        }
        return add_unsigned(first, second);
    }

    void add_leq_constant(const vector<int>& x, unsigned constant) {
        for (int bit = 0; bit < static_cast<int>(x.size()); ++bit) {
            if (constant & (1u << bit)) continue;
            vector<int> clause{-x[bit]};
            for (int higher = bit + 1;
                 higher < static_cast<int>(x.size()); ++higher)
                clause.push_back(constant & (1u << higher) ? -x[higher]
                                                            : x[higher]);
            add(std::move(clause));
            ++comparator_clauses;
        }
    }

    void build() {
        vector<int> deficit_literals;
        deficit_literals.reserve(shadows.size() * 3);
        for (const RankSevenShadow& item : shadows) {
            auto L = [&](int position) { return item.L0 + position; };
            auto R = [&](int position) { return item.R0 + position; };
            for (int threshold = 2; threshold <= 4; ++threshold) {
                const int credit = fresh();
                ++credit_variable_count;
                deficit_literals.push_back(-credit);

                // Inactive targets receive the maximum projected credit.
                add({item.active, credit});
                ++inactive_credit_clauses;

                // If the actual left endpoint is position, active&credit
                // forces the actual right endpoint to be at least
                // position+threshold.  L is the existing exact monotone
                // 0...01...1 left-threshold vector.
                for (int position = 0; position < N; ++position) {
                    vector<int> clause{-credit, -item.active, -L(position)};
                    if (position > 0) clause.push_back(L(position - 1));
                    if (position + threshold < N)
                        clause.push_back(R(position + threshold));
                    add(std::move(clause));
                    ++location_clauses;
                }
            }
        }

        const int counter_first = next;
        const vector<int> deficits = exact_count(deficit_literals);
        counter_variable_count = next - counter_first;
        add_leq_constant(deficits, type_one ? 380u : 390u);
    }

    int variables() const { return variable_count; }
};

// Cheap exact encoding of the stronger set-valued part of the named-cell
// theorem.  Rather than merely count eligible actual-OR cells, choose the
// already-existing witness for every lower target inside the named family.
//
// Type I: every rank-at-most-four witness may be chosen in suffix positions
// 1,...,464 with physical length at most two.
//
// Type II: in the one-component/no-duplicate case the global length-three
// cap is already exact.  In the other two audited cases (duplicate excess
// one, or two low components), every lower witness may be chosen with length
// at most two.  In the two-component case an internal pair of the slack-one
// component is already forced to be a selected rank-five witness, so an
// exact lower-target witness of length two automatically lies in the
// slack-two component.  Literal rank-five separators similarly exclude all
// crossing pairs.
//
// Crossed rank-three/rank-four witnesses already have length at most two;
// only direct targets and generic exception slots need extra clauses.
struct NamedCellFamilyPlan {
    int& next;
    const JointBandCutPlan& joint;
    bool type_one = false;
    const RankFiltrationTypeIIPlan* type_two = nullptr;
    int first_variable = 0;
    int variable_count = 0;
    int short_mode = 0;
    int one = 0;
    int capped_direct_targets = 0;
    int capped_exception_slots = 0;
    long long mode_clauses = 0;
    long long location_clauses = 0;
    long long width_clauses = 0;
    vector<vector<int>> clauses;

    NamedCellFamilyPlan(int& next_variable, const JointBandCutPlan& joint_plan,
                        bool enable_type_one,
                        const RankFiltrationTypeIIPlan* type_two_plan,
                        const vector<DirectTarget>& direct,
                        const vector<ExceptionSlot>& exception_three,
                        const vector<ExceptionSlot>& exception_four)
        : next(next_variable), joint(joint_plan), type_one(enable_type_one),
          type_two(type_two_plan), first_variable(next_variable),
          one(joint_plan.one) {
        if (!type_one) {
            short_mode = next++;
            const int two_components = type_two->two_components_flag;
            const int duplicate = type_two->duplicate_flag;
            // short_mode <-> (two_components OR duplicate).
            add({-two_components, short_mode});
            add({-duplicate, short_mode});
            add({-short_mode, two_components, duplicate});
            mode_clauses += 3;
        }

        for (const DirectTarget& item : direct)
            if (item.rank <= 4) {
                cap_witness(item.M0);
                ++capped_direct_targets;
            }
        for (const ExceptionSlot& slot : exception_three) {
            cap_witness(slot.M0);
            ++capped_exception_slots;
        }
        for (const ExceptionSlot& slot : exception_four) {
            cap_witness(slot.M0);
            ++capped_exception_slots;
        }

        // The named-cell Hall count also forces selected rank-five width
        // y2 >= 96+z in Type I and the duplicate Type-II branch, and
        // y2 >= 95+z in the two-component Type-II branch.  Here z=y0 and
        // both y0 and y2 are boundary differences determined by the selected
        // rank-five maximal chain.  Encode those exact chainwise rows
        // directly on the existing h-boundaries.
        if (type_one) {
            add_width_rows(96, one);
        } else {
            add_width_rows(96, type_two->duplicate_flag);
            add_width_rows(95, type_two->two_components_flag);
        }
        variable_count = next - first_variable;
    }

    void add(vector<int> clause) { clauses.push_back(std::move(clause)); }

    void cap_witness(int inside_base) {
        if (type_one) {
            // A[0] is the unique literal six-set; the named low core is in
            // the compressed suffix.  This unit is logically implied by the
            // exact target bits but is valuable propagation.
            add({-inside_base});
            ++location_clauses;
        }
        for (int position = 0; position + 2 < N; ++position) {
            vector<int> clause;
            if (!type_one) clause.push_back(-short_mode);
            clause.push_back(-(inside_base + position));
            clause.push_back(-(inside_base + position + 2));
            add(std::move(clause));
            ++location_clauses;
        }
    }

    pair<int, int> full_adder(int a, int b, int carry) {
        const int sum = next++;
        const int next_carry = next++;
        for (int av = 0; av < 2; ++av)
            for (int bv = 0; bv < 2; ++bv)
                for (int cv = 0; cv < 2; ++cv) {
                    const int parity = av ^ bv ^ cv;
                    add({av ? -a : a, bv ? -b : b,
                         cv ? -carry : carry, parity ? sum : -sum});
                }
        add({-a, -b, next_carry});
        add({-a, -carry, next_carry});
        add({-b, -carry, next_carry});
        add({-next_carry, a, b});
        add({-next_carry, a, carry});
        add({-next_carry, b, carry});
        width_clauses += 14;
        return {sum, next_carry};
    }

    vector<int> add_unsigned(const vector<int>& x, const vector<int>& y) {
        const int width = max(x.size(), y.size());
        vector<int> result;
        result.reserve(width + 1);
        int carry = -one;
        for (int bit = 0; bit < width; ++bit) {
            const int a = bit < static_cast<int>(x.size()) ? x[bit] : -one;
            const int b = bit < static_cast<int>(y.size()) ? y[bit] : -one;
            const auto [sum, next_carry] = full_adder(a, b, carry);
            result.push_back(sum);
            carry = next_carry;
        }
        result.push_back(carry);
        return result;
    }

    vector<int> sum_all(initializer_list<vector<int>> terms) {
        auto iterator = terms.begin();
        vector<int> result = *iterator++;
        while (iterator != terms.end())
            result = add_unsigned(result, *iterator++);
        return result;
    }

    vector<int> constant_bits(unsigned value) const {
        int width = 1;
        while ((1u << width) <= value) ++width;
        vector<int> result(width);
        for (int bit = 0; bit < width; ++bit)
            result[bit] = value & (1u << bit) ? one : -one;
        return result;
    }

    int define_and(int left, int right) {
        const int out = next++;
        add({-out, left});
        add({-out, right});
        add({out, -left, -right});
        width_clauses += 3;
        return out;
    }

    void add_leq_guarded(vector<int> x, vector<int> y, int guard) {
        const int width = max(x.size(), y.size());
        x.resize(width, -one);
        y.resize(width, -one);
        int equal_above = one;
        for (int bit = width - 1; bit >= 0; --bit) {
            add({-guard, -equal_above, -x[bit], y[bit]});
            ++width_clauses;
            if (bit == 0) continue;
            const int next_equal = next++;
            add({-guard, -next_equal, equal_above});
            add({-guard, -next_equal, -x[bit], y[bit]});
            add({-guard, -next_equal, x[bit], -y[bit]});
            add({-guard, -equal_above, -x[bit], -y[bit], next_equal});
            add({-guard, -equal_above, x[bit], y[bit], next_equal});
            width_clauses += 5;
            equal_above = next_equal;
        }
    }

    void add_width_rows(unsigned offset, int branch_guard) {
        auto H = [&](int j) {
            return vector<int>(joint.bits[j].begin(), joint.bits[j].end());
        };
        const vector<int> h1 = H(0), h2 = H(1), h3 = H(2);
        const vector<int> h4 = H(3), h5 = H(4), h6 = H(5);
        const vector<int> constant = constant_bits(462 + offset);

        // A: 00,01,02,12,13,23,33, so y2=(h3-h2)+(h5-h4).
        // B: 00,01,02,12,22,23,33, so y2=h3-h2.
        // C: 00,01,11,12,13,23,33, so y2=h5-h4.
        array<vector<int>, 3> left{{
            sum_all({h2, h4, h1, constant}),
            sum_all({h2, h1, h5, constant}),
            sum_all({h4, h1, h3, constant}),
        }};
        array<vector<int>, 3> right{{
            sum_all({h3, h5, h6}),
            sum_all({h3, h4, h6}),
            sum_all({h5, h2, h6}),
        }};
        for (int chain = 0; chain < 3; ++chain) {
            const int guard = branch_guard == one
                                  ? joint.chain_selector[chain]
                                  : define_and(branch_guard,
                                               joint.chain_selector[chain]);
            add_leq_guarded(std::move(left[chain]), std::move(right[chain]),
                            guard);
        }
    }

    int variables() const { return variable_count; }
};

// Optional exact encoding of the strongest currently proved six-subcube
// lower-tail law.  For every six-set U, let
//
//   p_U = #{position : A[position] is a subset of U}.
//
// The exact run-credit theorem and the independently proved p_U>=28 give
//
//   sum_U gamma(p_U) <= 462,
//   sum_U (gamma(p_U)-1)_+ <= 369,
//   gamma(28,29,30,31,>=32) = (7,5,3,1,0).
//
// Each support bit is defined exactly from the five coordinates outside U.
// A Wallace compressor followed by one exact ripple addition computes p_U.
// On the valid range p_U>=28, if g=[p_U<=31], the three binary bits of
// gamma(p_U) are
//
//   gamma_0=g, gamma_1=g & !p_U[0], gamma_2=g & !p_U[1].
//
// A second Wallace compressor sums these 462 three-bit charges exactly.
// The plan stores clauses in a flat zero-terminated buffer: 4.3 million
// vector objects would otherwise cost substantially more memory than their
// literals.  No variable is allocated and no clause is emitted when
// K11_FOREST_SUBCUBE_DEFICIENCY is absent.
struct SubcubeRunCreditPlan {
    int& next;
    int first_variable = 0;
    int variable_count = 0;
    long long clause_count = 0;
    bool type1_core = false;
    int type1_core_variables = 0;
    long long type1_core_clauses = 0;
    int one = 0;
    // Retain the already exact support row for the canonical Type-I endpoint
    // T=63.  This is only a reference bank: populating it allocates no new
    // variable and emits no clause.
    array<int, N> endpoint_support{};
    vector<int> flat;

    explicit SubcubeRunCreditPlan(int& next_variable, bool enable_type1_core)
        : next(next_variable), first_variable(next_variable),
          type1_core(enable_type1_core) {
        // The exact inventory is about nineteen million integers including
        // zero terminators.  Reserving once avoids repeated large copies.
        flat.reserve(20'000'000);
        build();
        variable_count = next - first_variable;
    }

    int fresh() { return next++; }
    static int entry(int position, int bit) {
        return 1 + position * K + bit;
    }
    void add(initializer_list<int> clause) {
        flat.insert(flat.end(), clause.begin(), clause.end());
        flat.push_back(0);
        ++clause_count;
    }
    void add(const vector<int>& clause) {
        flat.insert(flat.end(), clause.begin(), clause.end());
        flat.push_back(0);
        ++clause_count;
    }

    pair<int, int> full_adder(int a, int b, int carry) {
        const int sum = fresh();
        const int next_carry = fresh();
        for (int av = 0; av < 2; ++av)
            for (int bv = 0; bv < 2; ++bv)
                for (int cv = 0; cv < 2; ++cv) {
                    const int parity = av ^ bv ^ cv;
                    add({av ? -a : a, bv ? -b : b,
                         cv ? -carry : carry, parity ? sum : -sum});
                }
        add({-a, -b, next_carry});
        add({-a, -carry, next_carry});
        add({-b, -carry, next_carry});
        add({-next_carry, a, b});
        add({-next_carry, a, carry});
        add({-next_carry, b, carry});
        return {sum, next_carry};
    }

    vector<int> add_unsigned(const vector<int>& x, const vector<int>& y) {
        const int width = max(x.size(), y.size());
        vector<int> result;
        result.reserve(width + 1);
        int carry = -one;
        for (int bit = 0; bit < width; ++bit) {
            const int a = bit < static_cast<int>(x.size()) ? x[bit] : -one;
            const int b = bit < static_cast<int>(y.size()) ? y[bit] : -one;
            const auto [sum, next_carry] = full_adder(a, b, carry);
            result.push_back(sum);
            carry = next_carry;
        }
        result.push_back(carry);
        return result;
    }

    // Compress equal-weight literals three at a time, leaving at most two
    // per weight, then add the two residual binary rows.  Every gate is an
    // equivalence, so the returned bits are the exact (not modular) sum.
    vector<int> exact_weighted_count(vector<vector<int>> buckets) {
        buckets.resize(max<size_t>(buckets.size(), 2));
        for (size_t bit = 0; bit < buckets.size(); ++bit) {
            while (buckets[bit].size() >= 3) {
                const int a = buckets[bit].back();
                buckets[bit].pop_back();
                const int b = buckets[bit].back();
                buckets[bit].pop_back();
                const int c = buckets[bit].back();
                buckets[bit].pop_back();
                const auto [sum, carry] = full_adder(a, b, c);
                buckets[bit].push_back(sum);
                if (bit + 1 == buckets.size()) buckets.emplace_back();
                buckets[bit + 1].push_back(carry);
            }
        }
        while (buckets.size() > 1 && buckets.back().empty())
            buckets.pop_back();
        vector<int> first(buckets.size(), -one), second(buckets.size(), -one);
        for (size_t bit = 0; bit < buckets.size(); ++bit) {
            if (!buckets[bit].empty()) first[bit] = buckets[bit][0];
            if (buckets[bit].size() == 2) second[bit] = buckets[bit][1];
        }
        return add_unsigned(first, second);
    }

    vector<int> exact_count(const vector<int>& literals) {
        vector<vector<int>> buckets(2);
        buckets[0] = literals;
        return exact_weighted_count(std::move(buckets));
    }

    // Direct first-difference comparators against an unsigned constant.
    // No auxiliaries are needed because the other operand is constant.
    void add_geq_constant(const vector<int>& x, unsigned constant) {
        for (int bit = 0; bit < static_cast<int>(x.size()); ++bit) {
            if (!(constant & (1u << bit))) continue;
            vector<int> clause{x[bit]};
            for (int higher = bit + 1;
                 higher < static_cast<int>(x.size()); ++higher)
                clause.push_back(constant & (1u << higher) ? -x[higher]
                                                            : x[higher]);
            add(clause);
        }
    }
    void add_leq_constant(const vector<int>& x, unsigned constant) {
        for (int bit = 0; bit < static_cast<int>(x.size()); ++bit) {
            if (constant & (1u << bit)) continue;
            vector<int> clause{-x[bit]};
            for (int higher = bit + 1;
                 higher < static_cast<int>(x.size()); ++higher)
                clause.push_back(constant & (1u << higher) ? -x[higher]
                                                            : x[higher]);
            add(clause);
        }
    }

    // out <-> (left & !right).
    void define_and_not(int out, int left, int right) {
        add({-out, left});
        add({-out, -right});
        add({out, -left, right});
    }

    void build() {
        one = fresh();
        add({one});

        vector<vector<int>> total_charge(3);
        vector<vector<int>> residual_charge(3);
        vector<int> endpoint_count;
        int endpoint_low31 = 0;
        for (int mask = 1; mask < LIMIT; ++mask) {
            if (popcount(static_cast<unsigned>(mask)) != 6) continue;

            vector<int> support;
            support.reserve(N);
            for (int position = 0; position < N; ++position) {
                const int z = fresh();
                vector<int> reverse{z};
                for (int bit = 0; bit < K; ++bit) {
                    if (mask & (1 << bit)) continue;
                    add({-z, -entry(position, bit)});
                    reverse.push_back(entry(position, bit));
                }
                add(reverse);
                support.push_back(z);
                if (mask == 63) endpoint_support[position] = z;
            }

            const vector<int> count = exact_count(support);
            // The independent marked-run packing theorem proves p_U>=28.
            // Encoding it here makes the compact five-value credit formula
            // below exactly equivalent to gamma_{6,3}(p_U).
            add_geq_constant(count, 28);

            // g <-> (count<=31), equivalently all bits 5 and above are zero.
            const int g = fresh();
            vector<int> low_reverse{g};
            for (int bit = 5; bit < static_cast<int>(count.size()); ++bit) {
                add({-g, -count[bit]});
                low_reverse.push_back(count[bit]);
            }
            add(low_reverse);

            const int gamma_two = fresh();
            const int gamma_four = fresh();
            define_and_not(gamma_two, g, count[0]);
            define_and_not(gamma_four, g, count[1]);
            total_charge[0].push_back(g);
            total_charge[1].push_back(gamma_two);
            total_charge[2].push_back(gamma_four);
            residual_charge[1].push_back(gamma_two);
            residual_charge[2].push_back(gamma_four);
            if (type1_core && mask == 63) {
                endpoint_count = count;
                endpoint_low31 = g;
            }
        }

        const vector<int> charge = exact_weighted_count(std::move(total_charge));
        add_leq_constant(charge, MIDDLE);
        const vector<int> residual =
            exact_weighted_count(std::move(residual_charge));
        add_leq_constant(residual, 369);

        if (type1_core) {
            const int core_first_variable = next;
            const long long core_first_clause = clause_count;

            // Type I fixes A[0]=63.  Hence position zero is supported by
            // exactly one six-subcube, U=63.  For every other U the core
            // support equals p_U, while p_63^C=p_63-1.  The core theorem
            // gives p_63^C>=28, hence p_63>=29.
            add_geq_constant(endpoint_count, 29);

            // eq32 <-> (p_63=32).  Together with endpoint_low31=[p<=31],
            // the exact correction
            //
            //   eta(p_63-1)-gamma(p_63)
            //     = 2 [p_63<=31] + [p_63=32]
            //
            // changes the unrestricted charge sum into the suffix-core
            // charge sum without a second 464-input population count.
            const int eq32 = fresh();
            vector<int> reverse{eq32};
            for (int bit = 0;
                 bit < static_cast<int>(endpoint_count.size()); ++bit) {
                const int condition =
                    bit == 5 ? endpoint_count[bit] : -endpoint_count[bit];
                add({-eq32, condition});
                reverse.push_back(-condition);
            }
            add(reverse);

            const vector<int> core_charge =
                add_unsigned(charge, {eq32, endpoint_low31});
            add_leq_constant(core_charge, 461);

            type1_core_variables = next - core_first_variable;
            type1_core_clauses = clause_count - core_first_clause;
        }
    }

    int variables() const { return variable_count; }

    template <class AddLiteral>
    void emit(AddLiteral add_literal) const {
        for (int literal : flat) add_literal(literal);
    }
};

// Optional exact Type-I boundary-facet pin load.  In the inner rank-five
// peel P_5 || C_4 || Q_5, every five-set R has at least twenty support
// positions in C_4.  For the six facets R=63\{b}, the existing support row
// for T=63 and exact rank-five flags identify those positions without a new
// support bank:
//
//   y[b,i] <-> support_T[i] & !A[i,b] & !rank5[i],  i=1,...,464.
//
// Each of the six exact counts is constrained to be at least twenty.  The
// true constant is reused from SubcubeRunCreditPlan.  No object is built and
// no variable or clause is added when the guard is absent.
struct TypeIFacetPinLoadPlan {
    int& next;
    const LocalDensityPBPlan& local;
    const SubcubeRunCreditPlan& subcube;
    int first_variable = 0;
    int variable_count = 0;
    int one = 0;
    int gate_variable_count = 0;
    int counter_variable_count = 0;
    long long gate_clauses = 0;
    long long counter_clauses = 0;
    long long comparator_clauses = 0;
    array<vector<int>, 6> facet_support;
    vector<vector<int>> clauses;

    TypeIFacetPinLoadPlan(int& next_variable,
                         const LocalDensityPBPlan& local_density,
                         const SubcubeRunCreditPlan& subcube_plan)
        : next(next_variable),
          local(local_density),
          subcube(subcube_plan),
          first_variable(next_variable),
          one(subcube_plan.one) {
        build();
        variable_count = next - first_variable;
    }

    static int entry(int position, int bit) {
        return 1 + position * K + bit;
    }
    int fresh() { return next++; }
    void add_gate(initializer_list<int> clause) {
        clauses.emplace_back(clause);
        ++gate_clauses;
    }
    void add_counter(initializer_list<int> clause) {
        clauses.emplace_back(clause);
        ++counter_clauses;
    }
    void add_comparator(vector<int> clause) {
        clauses.push_back(std::move(clause));
        ++comparator_clauses;
    }

    pair<int, int> full_adder(int a, int b, int carry) {
        const int sum = fresh();
        const int next_carry = fresh();
        counter_variable_count += 2;
        for (int av = 0; av < 2; ++av)
            for (int bv = 0; bv < 2; ++bv)
                for (int cv = 0; cv < 2; ++cv) {
                    const int parity = av ^ bv ^ cv;
                    add_counter({av ? -a : a, bv ? -b : b,
                                 cv ? -carry : carry,
                                 parity ? sum : -sum});
                }
        add_counter({-a, -b, next_carry});
        add_counter({-a, -carry, next_carry});
        add_counter({-b, -carry, next_carry});
        add_counter({-next_carry, a, b});
        add_counter({-next_carry, a, carry});
        add_counter({-next_carry, b, carry});
        return {sum, next_carry};
    }

    vector<int> add_unsigned(const vector<int>& x, const vector<int>& y) {
        const int width = max(x.size(), y.size());
        vector<int> result;
        result.reserve(width + 1);
        int carry = -one;
        for (int bit = 0; bit < width; ++bit) {
            const int a = bit < static_cast<int>(x.size()) ? x[bit] : -one;
            const int b = bit < static_cast<int>(y.size()) ? y[bit] : -one;
            const auto [sum, next_carry] = full_adder(a, b, carry);
            result.push_back(sum);
            carry = next_carry;
        }
        result.push_back(carry);
        return result;
    }

    vector<int> exact_count(const vector<int>& literals) {
        vector<vector<int>> buckets(2);
        buckets[0] = literals;
        for (size_t bit = 0; bit < buckets.size(); ++bit) {
            while (buckets[bit].size() >= 3) {
                const int a = buckets[bit].back();
                buckets[bit].pop_back();
                const int b = buckets[bit].back();
                buckets[bit].pop_back();
                const int c = buckets[bit].back();
                buckets[bit].pop_back();
                const auto [sum, carry] = full_adder(a, b, c);
                buckets[bit].push_back(sum);
                if (bit + 1 == buckets.size()) buckets.emplace_back();
                buckets[bit + 1].push_back(carry);
            }
        }
        while (buckets.size() > 1 && buckets.back().empty())
            buckets.pop_back();
        vector<int> first(buckets.size(), -one), second(buckets.size(), -one);
        for (size_t bit = 0; bit < buckets.size(); ++bit) {
            if (!buckets[bit].empty()) first[bit] = buckets[bit][0];
            if (buckets[bit].size() == 2) second[bit] = buckets[bit][1];
        }
        return add_unsigned(first, second);
    }

    void add_geq_constant(const vector<int>& x, unsigned constant) {
        for (int bit = 0; bit < static_cast<int>(x.size()); ++bit) {
            if (!(constant & (1u << bit))) continue;
            vector<int> clause{x[bit]};
            for (int higher = bit + 1;
                 higher < static_cast<int>(x.size()); ++higher)
                clause.push_back(constant & (1u << higher) ? -x[higher]
                                                            : x[higher]);
            add_comparator(std::move(clause));
        }
    }

    void build() {
        for (int bit = 0; bit < 6; ++bit) {
            facet_support[bit].reserve(N - 1);
            for (int position = 1; position < N; ++position) {
                const int z = fresh();
                ++gate_variable_count;
                const int support = subcube.endpoint_support[position];
                const int coordinate = entry(position, bit);
                const int rank_five = local.rank[position][5];
                // z <-> support & !coordinate & !rank_five.
                add_gate({-z, support});
                add_gate({-z, -coordinate});
                add_gate({-z, -rank_five});
                add_gate({z, -support, coordinate, rank_five});
                facet_support[bit].push_back(z);
            }
            const vector<int> count = exact_count(facet_support[bit]);
            add_geq_constant(count, 20);
        }
    }

    int variables() const { return variable_count; }
};

// Optional codimension-two refinement of the Type-I boundary pin load.  For
// every ridge Q=63\{b,c}, the inner C_4 core contains at least ten positions
// whose entries are proper subsets of Q.  Reuse the exact facet literal
//
//   facet_support[b][i] <-> i in C_4 and A[i] subseteq 63\{b}
//
// and define
//
//   z[b,c,i] <-> facet_support[b][i] & !A[i,c] & !rank4[i].
//
// The fifteen exact counts are constrained to be at least ten.  The guard
// requires the facet module, so retaining its variable references costs no
// additional CNF.
struct TypeIRidgePinLoadPlan {
    int& next;
    const LocalDensityPBPlan& local;
    const TypeIFacetPinLoadPlan& facet;
    int first_variable = 0;
    int variable_count = 0;
    int one = 0;
    int gate_variable_count = 0;
    int counter_variable_count = 0;
    long long gate_clauses = 0;
    long long counter_clauses = 0;
    long long comparator_clauses = 0;
    vector<vector<int>> clauses;

    TypeIRidgePinLoadPlan(int& next_variable,
                         const LocalDensityPBPlan& local_density,
                         const TypeIFacetPinLoadPlan& facet_plan)
        : next(next_variable),
          local(local_density),
          facet(facet_plan),
          first_variable(next_variable),
          one(facet_plan.one) {
        build();
        variable_count = next - first_variable;
    }

    static int entry(int position, int bit) {
        return 1 + position * K + bit;
    }
    int fresh() { return next++; }
    void add_gate(initializer_list<int> clause) {
        clauses.emplace_back(clause);
        ++gate_clauses;
    }
    void add_counter(initializer_list<int> clause) {
        clauses.emplace_back(clause);
        ++counter_clauses;
    }
    void add_comparator(vector<int> clause) {
        clauses.push_back(std::move(clause));
        ++comparator_clauses;
    }

    pair<int, int> full_adder(int a, int b, int carry) {
        const int sum = fresh();
        const int next_carry = fresh();
        counter_variable_count += 2;
        for (int av = 0; av < 2; ++av)
            for (int bv = 0; bv < 2; ++bv)
                for (int cv = 0; cv < 2; ++cv) {
                    const int parity = av ^ bv ^ cv;
                    add_counter({av ? -a : a, bv ? -b : b,
                                 cv ? -carry : carry,
                                 parity ? sum : -sum});
                }
        add_counter({-a, -b, next_carry});
        add_counter({-a, -carry, next_carry});
        add_counter({-b, -carry, next_carry});
        add_counter({-next_carry, a, b});
        add_counter({-next_carry, a, carry});
        add_counter({-next_carry, b, carry});
        return {sum, next_carry};
    }

    vector<int> add_unsigned(const vector<int>& x, const vector<int>& y) {
        const int width = max(x.size(), y.size());
        vector<int> result;
        result.reserve(width + 1);
        int carry = -one;
        for (int bit = 0; bit < width; ++bit) {
            const int a = bit < static_cast<int>(x.size()) ? x[bit] : -one;
            const int b = bit < static_cast<int>(y.size()) ? y[bit] : -one;
            const auto [sum, next_carry] = full_adder(a, b, carry);
            result.push_back(sum);
            carry = next_carry;
        }
        result.push_back(carry);
        return result;
    }

    vector<int> exact_count(const vector<int>& literals) {
        vector<vector<int>> buckets(2);
        buckets[0] = literals;
        for (size_t bit = 0; bit < buckets.size(); ++bit) {
            while (buckets[bit].size() >= 3) {
                const int a = buckets[bit].back();
                buckets[bit].pop_back();
                const int b = buckets[bit].back();
                buckets[bit].pop_back();
                const int c = buckets[bit].back();
                buckets[bit].pop_back();
                const auto [sum, carry] = full_adder(a, b, c);
                buckets[bit].push_back(sum);
                if (bit + 1 == buckets.size()) buckets.emplace_back();
                buckets[bit + 1].push_back(carry);
            }
        }
        while (buckets.size() > 1 && buckets.back().empty())
            buckets.pop_back();
        vector<int> first(buckets.size(), -one), second(buckets.size(), -one);
        for (size_t bit = 0; bit < buckets.size(); ++bit) {
            if (!buckets[bit].empty()) first[bit] = buckets[bit][0];
            if (buckets[bit].size() == 2) second[bit] = buckets[bit][1];
        }
        return add_unsigned(first, second);
    }

    void add_geq_constant(const vector<int>& x, unsigned constant) {
        for (int bit = 0; bit < static_cast<int>(x.size()); ++bit) {
            if (!(constant & (1u << bit))) continue;
            vector<int> clause{x[bit]};
            for (int higher = bit + 1;
                 higher < static_cast<int>(x.size()); ++higher)
                clause.push_back(constant & (1u << higher) ? -x[higher]
                                                            : x[higher]);
            add_comparator(std::move(clause));
        }
    }

    void build() {
        for (int first = 0; first < 6; ++first)
            for (int second = first + 1; second < 6; ++second) {
                vector<int> strict_support;
                strict_support.reserve(N - 1);
                for (int position = 1; position < N; ++position) {
                    const int z = fresh();
                    ++gate_variable_count;
                    const int in_facet = facet.facet_support[first][position - 1];
                    const int coordinate = entry(position, second);
                    const int rank_four = local.rank[position][4];
                    // z <-> in_facet & !coordinate & !rank_four.
                    add_gate({-z, in_facet});
                    add_gate({-z, -coordinate});
                    add_gate({-z, -rank_four});
                    add_gate({z, -in_facet, coordinate, rank_four});
                    strict_support.push_back(z);
                }
                const vector<int> count = exact_count(strict_support);
                add_geq_constant(count, 10);
            }
    }

    int variables() const { return variable_count; }
};

// Optional exact Type-I global rank-one/rank-two interaction.  Every
// nonliteral rank-two target is represented by an adjacent pair of singleton
// atoms inside the rank-at-most-four core.  Two such witnesses for distinct
// targets cannot overlap, because three consecutive singleton entries would
// form a rank-at-most-three interval of length three, while every such core
// interval contains a selected rank-five witness.  Hence
//
//   n2 + floor(n1/2) >= C(11,2)=55,
//
// equivalently n1+2*n2>=110.  The exact rank flags already exist; this plan
// only counts the two rows, adds their weighted totals, and exposes the
// redundant propagation inequality.
struct TypeIGlobalPairProfilePlan {
    int& next;
    const LocalDensityPBPlan& local;
    int first_variable = 0;
    int variable_count = 0;
    int one = 0;
    long long counter_variable_count = 0;
    long long counter_clauses = 0;
    long long arithmetic_variable_count = 0;
    long long arithmetic_clauses = 0;
    long long comparator_clauses = 0;
    vector<vector<int>> clauses;

    TypeIGlobalPairProfilePlan(int& next_variable,
                               const LocalDensityPBPlan& local_density)
        : next(next_variable),
          local(local_density),
          first_variable(next_variable),
          one(local_density.one) {
        build();
        variable_count = next - first_variable;
    }

    int fresh() { return next++; }
    void add(vector<int> clause) { clauses.push_back(std::move(clause)); }

    pair<int, int> full_adder(int a, int b, int carry,
                              long long& variable_counter,
                              long long& clause_counter) {
        const int sum = fresh();
        const int next_carry = fresh();
        variable_counter += 2;
        for (int av = 0; av < 2; ++av)
            for (int bv = 0; bv < 2; ++bv)
                for (int cv = 0; cv < 2; ++cv) {
                    const int parity = av ^ bv ^ cv;
                    add({av ? -a : a, bv ? -b : b, cv ? -carry : carry,
                         parity ? sum : -sum});
                }
        add({-a, -b, next_carry});
        add({-a, -carry, next_carry});
        add({-b, -carry, next_carry});
        add({-next_carry, a, b});
        add({-next_carry, a, carry});
        add({-next_carry, b, carry});
        clause_counter += 14;
        return {sum, next_carry};
    }

    vector<int> add_unsigned(const vector<int>& x, const vector<int>& y,
                             long long& variable_counter,
                             long long& clause_counter) {
        const int width = max(x.size(), y.size());
        vector<int> result;
        result.reserve(width + 1);
        int carry = -one;
        for (int bit = 0; bit < width; ++bit) {
            const int a = bit < static_cast<int>(x.size()) ? x[bit] : -one;
            const int b = bit < static_cast<int>(y.size()) ? y[bit] : -one;
            const auto [sum, next_carry] =
                full_adder(a, b, carry, variable_counter, clause_counter);
            result.push_back(sum);
            carry = next_carry;
        }
        result.push_back(carry);
        return result;
    }

    vector<int> exact_count(const vector<int>& literals) {
        vector<vector<int>> buckets(2);
        buckets[0] = literals;
        for (size_t bit = 0; bit < buckets.size(); ++bit) {
            while (buckets[bit].size() >= 3) {
                const int a = buckets[bit].back();
                buckets[bit].pop_back();
                const int b = buckets[bit].back();
                buckets[bit].pop_back();
                const int c = buckets[bit].back();
                buckets[bit].pop_back();
                const auto [sum, carry] = full_adder(
                    a, b, c, counter_variable_count, counter_clauses);
                buckets[bit].push_back(sum);
                if (bit + 1 == buckets.size()) buckets.emplace_back();
                buckets[bit + 1].push_back(carry);
            }
        }
        while (buckets.size() > 1 && buckets.back().empty())
            buckets.pop_back();
        vector<int> first(buckets.size(), -one), second(buckets.size(), -one);
        for (size_t bit = 0; bit < buckets.size(); ++bit) {
            if (!buckets[bit].empty()) first[bit] = buckets[bit][0];
            if (buckets[bit].size() == 2) second[bit] = buckets[bit][1];
        }
        return add_unsigned(first, second, counter_variable_count,
                            counter_clauses);
    }

    void add_geq_constant(const vector<int>& x, unsigned constant) {
        for (int bit = 0; bit < static_cast<int>(x.size()); ++bit) {
            if (!(constant & (1u << bit))) continue;
            vector<int> clause{x[bit]};
            for (int higher = bit + 1;
                 higher < static_cast<int>(x.size()); ++higher)
                clause.push_back(constant & (1u << higher) ? -x[higher]
                                                            : x[higher]);
            add(std::move(clause));
            ++comparator_clauses;
        }
    }

    void build() {
        vector<int> rank_one, rank_two;
        rank_one.reserve(N);
        rank_two.reserve(N);
        for (int position = 0; position < N; ++position) {
            rank_one.push_back(local.rank[position][1]);
            rank_two.push_back(local.rank[position][2]);
        }
        const vector<int> n1 = exact_count(rank_one);
        const vector<int> n2 = exact_count(rank_two);
        vector<int> doubled_n2{-one};
        doubled_n2.insert(doubled_n2.end(), n2.begin(), n2.end());
        const vector<int> profile =
            add_unsigned(n1, doubled_n2, arithmetic_variable_count,
                         arithmetic_clauses);
        add_geq_constant(profile, 110);
    }

    int variables() const { return variable_count; }
};

int state_index(int alpha, int beta) {
    for (int u = 0; u < static_cast<int>(STATES.size()); ++u)
        if (STATES[u] == pair<int, int>{alpha, beta}) return u;
    return -1;
}

template <class Callback>
void for_combinations(int n, int take, Callback callback) {
    vector<int> selected;
    selected.reserve(take);
    std::function<void(int, int)> visit = [&](int first, int remaining) {
        if (remaining == 0) {
            callback(selected);
            return;
        }
        for (int value = first; value <= n - remaining; ++value) {
            selected.push_back(value);
            visit(value + 1, remaining - 1);
            selected.pop_back();
        }
    };
    visit(0, take);
}

BestInterval best_interval(const vector<int>& seed, int target, int bound) {
    BestInterval best;
    best.target = target;
    for (int left = 0; left < N; ++left) {
        int value = 0;
        for (int right = left; right < N && right - left + 1 <= bound; ++right) {
            value |= seed[right];
            const int difference = popcount(static_cast<unsigned>(value ^ target));
            const int cost = 1024 * difference + (right - left + 1);
            if (cost < best.cost) best = {left, right, value, target, cost};
        }
    }
    return best;
}

vector<BestInterval> central_phase(const vector<int>& seed, int rank,
                                   bool& exact_schedule) {
    vector<BestInterval> result;
    result.reserve(MIDDLE);
    const int bound = safe_bound(rank);
    for (int target = 1; target < LIMIT; ++target)
        if (popcount(static_cast<unsigned>(target)) == rank)
            result.push_back(best_interval(seed, target, bound));

    exact_schedule = all_of(result.begin(), result.end(), [](const BestInterval& x) {
        return x.value == x.target;
    });
    if (!exact_schedule) return result;

    sort(result.begin(), result.end(), [](const BestInterval& x, const BestInterval& y) {
        return pair<int, int>{x.left, x.right} < pair<int, int>{y.left, y.right};
    });
    int previous_left = -1, previous_right = -1;
    int previous_alpha = -1, previous_beta = -1;
    for (int i = 0; i < MIDDLE; ++i) {
        const int alpha = result[i].left - i;
        const int beta = result[i].right - i;
        if (result[i].left <= previous_left || result[i].right <= previous_right ||
            alpha < 0 || beta > 3 || alpha > beta || alpha < previous_alpha ||
            beta < previous_beta || (rank == 5 && beta - alpha > 2)) {
            exact_schedule = false;
            break;
        }
        previous_left = result[i].left;
        previous_right = result[i].right;
        previous_alpha = alpha;
        previous_beta = beta;
    }
    return result;
}

}  // namespace

int main(int argc, char** argv) {
    if (argc < 3 || argc > 4) {
        cerr << "usage: k11_forest_sat seed_array output_array [sat_seed]\n";
        return 2;
    }
    const int sat_seed = argc == 4 ? stoi(argv[3]) : 1;
    const bool adjacent_shadows = [] {
        const char* value = getenv("K11_FOREST_ADJACENT_SHADOWS");
        return value && *value && string(value) != "0";
    }();
    const bool band_cuts = [] {
        const char* value = getenv("K11_FOREST_BAND_CUTS");
        return value && *value && string(value) != "0";
    }();
    const bool joint_band_cuts = [] {
        const char* value = getenv("K11_FOREST_JOINT_BAND_CUTS");
        return value && *value && string(value) != "0";
    }();
    const bool endpoint_alignment_cuts = [] {
        const char* value = getenv("K11_FOREST_ENDPOINT_ALIGNMENT_CUTS");
        return value && *value && string(value) != "0";
    }();
    const bool rank_three_shadows = [] {
        const char* value = getenv("K11_FOREST_RANK3_SHADOWS");
        return value && *value && string(value) != "0";
    }();
    const bool canonical_rank_six_entry = [] {
        const char* value = getenv("K11_FOREST_CANONICAL_RANK6_ENTRY");
        return value && *value && string(value) != "0";
    }();
    const bool singleton_pool_cut = [] {
        const char* value = getenv("K11_FOREST_SINGLETON_POOL_CUT");
        return value && *value && string(value) != "0";
    }();
    const bool rank_six_boundary_entry = [] {
        const char* value = getenv("K11_FOREST_RANK6_BOUNDARY_ENTRY");
        return value && *value && string(value) != "0";
    }();
    const bool local_density_pb = [] {
        const char* value = getenv("K11_FOREST_LOCAL_DENSITY_PB");
        return value && *value && string(value) != "0";
    }();
    const bool rank_filtration_type2 = [] {
        const char* value = getenv("K11_FOREST_RANK_FILTRATION_TYPE2");
        return value && *value && string(value) != "0";
    }();
    const bool rank_filtration_type1 = [] {
        const char* value = getenv("K11_FOREST_RANK_FILTRATION_TYPE1");
        return value && *value && string(value) != "0";
    }();
    const bool subcube_deficiency = [] {
        const char* value = getenv("K11_FOREST_SUBCUBE_DEFICIENCY");
        return value && *value && string(value) != "0";
    }();
    const bool containment_caps = [] {
        const char* value = getenv("K11_FOREST_CONTAINMENT_CAPS");
        return value && *value && string(value) != "0";
    }();
    const bool residual_coordinate_lex = [] {
        const char* value = getenv("K11_FOREST_RESIDUAL_COORD_LEX");
        return value && *value && string(value) != "0";
    }();
    const bool named_cell_hall = [] {
        const char* value = getenv("K11_FOREST_NAMED_CELL_HALL");
        return value && *value && string(value) != "0";
    }();
    const bool type1_prefix_chain = [] {
        const char* value = getenv("K11_FOREST_TYPE1_PREFIX_CHAIN");
        return value && *value && string(value) != "0";
    }();
    const bool type1_facet_pin_load = [] {
        const char* value = getenv("K11_FOREST_TYPE1_FACET_PIN_LOAD");
        return value && *value && string(value) != "0";
    }();
    const bool type1_ridge_pin_load = [] {
        const char* value = getenv("K11_FOREST_TYPE1_RIDGE_PIN_LOAD");
        return value && *value && string(value) != "0";
    }();
    const bool type1_global_pair_profile = [] {
        const char* value = getenv("K11_FOREST_TYPE1_GLOBAL_PAIR_PROFILE");
        return value && *value && string(value) != "0";
    }();
    const bool two_component_pin_localization = [] {
        const char* value =
            getenv("K11_FOREST_TWO_COMPONENT_PIN_LOCALIZATION");
        return value && *value && string(value) != "0";
    }();
    const bool type2_reverse_pin_load = [] {
        const char* value = getenv("K11_FOREST_TYPE2_REVERSE_PIN_LOAD");
        return value && *value && string(value) != "0";
    }();
    const bool type2_companion_pin_load = [] {
        const char* value = getenv("K11_FOREST_TYPE2_COMPANION_PIN_LOAD");
        return value && *value && string(value) != "0";
    }();
    const bool rank_seven_truncated_width = [] {
        const char* value = getenv("K11_FOREST_RANK7_TRUNCATED_WIDTH");
        return value && *value && string(value) != "0";
    }();
    const bool q369_top_layer_cut = [] {
        const char* value = getenv("K11_FOREST_Q369_TOP_LAYER_CUT");
        return value && *value && string(value) != "0";
    }();
    string portal_branch_mode;
    if (const char* value = getenv("K11_FOREST_PORTAL_BRANCH")) {
        portal_branch_mode = value;
        if (portal_branch_mode != "q19_factor_prefix" &&
            portal_branch_mode != "q19_fixed_row" &&
            portal_branch_mode != "q19_abstract" &&
            portal_branch_mode != "q369_schedule") {
            cerr << "K11_FOREST_PORTAL_BRANCH must be absent, "
                    "q19_factor_prefix, q19_fixed_row, q19_abstract, or "
                    "q369_schedule\n";
            return 2;
        }
    }
    int rank_six_branch = -1;
    if (const char* value = getenv("K11_FOREST_RANK6_BRANCH")) {
        const string text(value);
        if (text == "0")
            rank_six_branch = 0;
        else if (text == "1")
            rank_six_branch = 1;
        else {
            cerr << "K11_FOREST_RANK6_BRANCH must be absent or exactly 0 or 1\n";
            return 2;
        }
    }
    string min_component_mode;
    if (const char* value = getenv("K11_FOREST_MIN_COMPONENT")) {
        min_component_mode = value;
        if (min_component_mode != "e0c1" && min_component_mode != "e1c2") {
            cerr << "K11_FOREST_MIN_COMPONENT must be absent, e0c1, or e1c2\n";
            return 2;
        }
    }
    if (rank_three_shadows && !adjacent_shadows) {
        cerr << "K11_FOREST_RANK3_SHADOWS requires "
                "K11_FOREST_ADJACENT_SHADOWS\n";
        return 2;
    }
    if (joint_band_cuts && !band_cuts) {
        cerr << "K11_FOREST_JOINT_BAND_CUTS requires "
                "K11_FOREST_BAND_CUTS\n";
        return 2;
    }
    if (endpoint_alignment_cuts && !adjacent_shadows) {
        cerr << "K11_FOREST_ENDPOINT_ALIGNMENT_CUTS requires "
                "K11_FOREST_ADJACENT_SHADOWS\n";
        return 2;
    }
    if (singleton_pool_cut && (!band_cuts || !joint_band_cuts)) {
        cerr << "K11_FOREST_SINGLETON_POOL_CUT requires both "
                "K11_FOREST_BAND_CUTS and K11_FOREST_JOINT_BAND_CUTS\n";
        return 2;
    }
    if (rank_filtration_type2 &&
        (!local_density_pb || !band_cuts || !joint_band_cuts)) {
        cerr << "K11_FOREST_RANK_FILTRATION_TYPE2 requires "
                "K11_FOREST_LOCAL_DENSITY_PB, K11_FOREST_BAND_CUTS, and "
                "K11_FOREST_JOINT_BAND_CUTS\n";
        return 2;
    }
    if (rank_filtration_type2 && rank_six_branch == 1) {
        cerr << "K11_FOREST_RANK_FILTRATION_TYPE2 is incompatible with "
                "K11_FOREST_RANK6_BRANCH=1\n";
        return 2;
    }
    if (rank_filtration_type1 &&
        (!local_density_pb || !band_cuts || !joint_band_cuts ||
         rank_six_branch != 1)) {
        cerr << "K11_FOREST_RANK_FILTRATION_TYPE1 requires "
                "K11_FOREST_LOCAL_DENSITY_PB, K11_FOREST_BAND_CUTS, "
                "K11_FOREST_JOINT_BAND_CUTS, and "
                "K11_FOREST_RANK6_BRANCH=1\n";
        return 2;
    }
    if (residual_coordinate_lex &&
        (rank_filtration_type1 == rank_filtration_type2)) {
        cerr << "K11_FOREST_RESIDUAL_COORD_LEX requires exactly one of "
                "K11_FOREST_RANK_FILTRATION_TYPE1 or "
                "K11_FOREST_RANK_FILTRATION_TYPE2\n";
        return 2;
    }
    if (named_cell_hall &&
        (rank_filtration_type1 == rank_filtration_type2)) {
        cerr << "K11_FOREST_NAMED_CELL_HALL requires exactly one of "
                "K11_FOREST_RANK_FILTRATION_TYPE1 or "
                "K11_FOREST_RANK_FILTRATION_TYPE2\n";
        return 2;
    }
    if (type1_prefix_chain &&
        (!rank_filtration_type1 || !residual_coordinate_lex)) {
        cerr << "K11_FOREST_TYPE1_PREFIX_CHAIN requires "
                "K11_FOREST_RANK_FILTRATION_TYPE1 and "
                "K11_FOREST_RESIDUAL_COORD_LEX\n";
        return 2;
    }
    if (type1_facet_pin_load &&
        (!rank_filtration_type1 || !subcube_deficiency)) {
        cerr << "K11_FOREST_TYPE1_FACET_PIN_LOAD requires "
                "K11_FOREST_RANK_FILTRATION_TYPE1 and "
                "K11_FOREST_SUBCUBE_DEFICIENCY\n";
        return 2;
    }
    if (type1_ridge_pin_load && !type1_facet_pin_load) {
        cerr << "K11_FOREST_TYPE1_RIDGE_PIN_LOAD requires "
                "K11_FOREST_TYPE1_FACET_PIN_LOAD\n";
        return 2;
    }
    if (type1_global_pair_profile && !rank_filtration_type1) {
        cerr << "K11_FOREST_TYPE1_GLOBAL_PAIR_PROFILE requires "
                "K11_FOREST_RANK_FILTRATION_TYPE1\n";
        return 2;
    }
    if (two_component_pin_localization && !rank_filtration_type2) {
        cerr << "K11_FOREST_TWO_COMPONENT_PIN_LOCALIZATION requires "
                "K11_FOREST_RANK_FILTRATION_TYPE2\n";
        return 2;
    }
    if (type2_reverse_pin_load && !two_component_pin_localization) {
        cerr << "K11_FOREST_TYPE2_REVERSE_PIN_LOAD requires "
                "K11_FOREST_TWO_COMPONENT_PIN_LOCALIZATION\n";
        return 2;
    }
    if (type2_companion_pin_load && !type2_reverse_pin_load) {
        cerr << "K11_FOREST_TYPE2_COMPANION_PIN_LOAD requires "
                "K11_FOREST_TYPE2_REVERSE_PIN_LOAD\n";
        return 2;
    }
    if (rank_seven_truncated_width &&
        (!adjacent_shadows ||
         (rank_filtration_type1 == rank_filtration_type2))) {
        cerr << "K11_FOREST_RANK7_TRUNCATED_WIDTH requires "
                "K11_FOREST_ADJACENT_SHADOWS and exactly one of "
                "K11_FOREST_RANK_FILTRATION_TYPE1 or "
                "K11_FOREST_RANK_FILTRATION_TYPE2\n";
        return 2;
    }
    if (rank_six_branch >= 0 &&
        (!canonical_rank_six_entry || !rank_six_boundary_entry || !band_cuts ||
         !joint_band_cuts)) {
        cerr << "K11_FOREST_RANK6_BRANCH requires "
                "K11_FOREST_CANONICAL_RANK6_ENTRY, "
                "K11_FOREST_RANK6_BOUNDARY_ENTRY, K11_FOREST_BAND_CUTS, and "
                "K11_FOREST_JOINT_BAND_CUTS\n";
        return 2;
    }
    if ((!min_component_mode.empty()) &&
        ((min_component_mode == "e0c1" && rank_six_branch != 0) ||
         (min_component_mode == "e1c2" && rank_six_branch != 1))) {
        cerr << "K11_FOREST_MIN_COMPONENT=e0c1 requires "
                "K11_FOREST_RANK6_BRANCH=0, while e1c2 requires branch=1\n";
        return 2;
    }
    if (!portal_branch_mode.empty() &&
        (!adjacent_shadows || !rank_three_shadows || band_cuts ||
         joint_band_cuts || endpoint_alignment_cuts ||
         canonical_rank_six_entry || singleton_pool_cut ||
         rank_six_boundary_entry || local_density_pb ||
         rank_filtration_type2 || rank_filtration_type1 ||
         subcube_deficiency || named_cell_hall ||
         type1_facet_pin_load ||
         type1_ridge_pin_load ||
         type1_global_pair_profile ||
         two_component_pin_localization ||
         type2_reverse_pin_load ||
         type2_companion_pin_load ||
         rank_seven_truncated_width ||
         rank_six_branch >= 0 ||
         !min_component_mode.empty())) {
        cerr << "K11_FOREST_PORTAL_BRANCH requires exactly adjacent and "
                "rank-three shadows; containment caps are optional and all "
                "other structural modules must be absent\n";
        return 2;
    }
    if (q369_top_layer_cut && portal_branch_mode != "q369_schedule") {
        cerr << "K11_FOREST_Q369_TOP_LAYER_CUT requires "
                "K11_FOREST_PORTAL_BRANCH=q369_schedule\n";
        return 2;
    }
    vector<int> seed;
    {
        ifstream input(argv[1]);
        for (int value; input >> value;) seed.push_back(value);
    }
    if (static_cast<int>(seed.size()) != N) {
        cerr << "seed must contain exactly 465 integers\n";
        return 3;
    }
    for (int value : seed)
        if (value <= 0 || value >= LIMIT) {
            cerr << "seed entry outside 1..2047\n";
            return 3;
        }

    int next = N * K + 1;
    auto A = [](int position, int bit) { return 1 + position * K + bit; };
    auto witness_bound = [&](int rank) {
        return containment_caps ? containment_bound(rank) : safe_bound(rank);
    };

    vector<DirectTarget> direct;
    direct.reserve(LIMIT - 1 - 2 * MIDDLE);
    for (int target = 1; target < LIMIT; ++target) {
        const int rank = popcount(static_cast<unsigned>(target));
        if (rank == 5 || rank == 6) continue;
        if (adjacent_shadows && (rank == 4 || rank == 7)) continue;
        if (rank_three_shadows && rank == 3) continue;
        DirectTarget item;
        item.target = target;
        item.rank = rank;
        item.bound = witness_bound(rank);
        item.H0.fill(-1);
        item.L0 = next;
        next += N;
        item.R0 = next;
        next += N;
        item.M0 = next;
        next += N;
        for (int bit = 0; bit < K; ++bit)
            if (target & (1 << bit)) {
                item.H0[bit] = next;
                next += N;
            }
        direct.push_back(item);
    }

    array<CentralLayer, 2> central;
    for (int layer = 0; layer < 2; ++layer) {
        CentralLayer& data = central[layer];
        data.rank = 5 + layer;
        for (int mask = 1; mask < LIMIT; ++mask)
            if (popcount(static_cast<unsigned>(mask)) == data.rank)
                data.masks.push_back(mask);
        if (static_cast<int>(data.masks.size()) != MIDDLE) return 4;
        data.state.resize(MIDDLE);
        data.value.resize(MIDDLE);
        for (int i = 0; i < MIDDLE; ++i) {
            for (int u = 0; u < 10; ++u) data.state[i][u] = next++;
            for (int bit = 0; bit < K; ++bit) data.value[i][bit] = next++;
        }
        data.q.resize(MIDDLE * MIDDLE);
        for (int& variable : data.q) variable = next++;
    }

    vector<int> rank_three_masks, rank_four_masks, rank_seven_masks;
    vector<ExceptionSlot> exception_three, exception_four, exception_seven;
    vector<RankFourShadow> rank_four_shadow;
    vector<RankSevenShadow> rank_seven_shadow;
    array<array<int, 4>, N> rank_six_by_left{};
    array<array<int, 4>, N> rank_six_by_right{};
    if (adjacent_shadows) {
        for (int mask = 1; mask < LIMIT; ++mask) {
            const int rank = popcount(static_cast<unsigned>(mask));
            if (rank_three_shadows && rank == 3)
                rank_three_masks.push_back(mask);
            if (rank == 4) rank_four_masks.push_back(mask);
            if (rank == 7) rank_seven_masks.push_back(mask);
        }
        if (rank_four_masks.size() != 330 || rank_seven_masks.size() != 330)
            return 4;
        if (rank_three_shadows && rank_three_masks.size() != 165) return 4;

        auto allocate_exception_slots = [&](int rank, const vector<int>& masks,
                                            vector<ExceptionSlot>& slots) {
            slots.resize(6);
            for (ExceptionSlot& slot : slots) {
                slot.rank = rank;
                slot.bound = witness_bound(rank);
                slot.L0 = next;
                next += N;
                slot.R0 = next;
                next += N;
                slot.M0 = next;
                next += N;
                for (int bit = 0; bit < K; ++bit) {
                    slot.value[bit] = next++;
                    slot.H0[bit] = next;
                    next += N;
                }
                slot.q.resize(masks.size());
                for (int& variable : slot.q) variable = next++;
            }
        };
        if (rank_three_shadows)
            allocate_exception_slots(3, rank_three_masks, exception_three);
        allocate_exception_slots(4, rank_four_masks, exception_four);
        allocate_exception_slots(7, rank_seven_masks, exception_seven);

        // A crossed rank-four witness is the nonempty intersection of two
        // proper rank-five extensions of length at most three, hence has
        // physical length at most two.  These are all possible candidates.
        for (int left = 0; left < N; ++left)
            for (int right = left; right < N && right <= left + 1; ++right) {
                RankFourShadow item;
                item.left = left;
                item.right = right;
                item.at_most_four = next++;
                if (rank_three_shadows) item.at_most_three = next++;
                for (int bit = 0; bit < K; ++bit) item.value[bit] = next++;
                item.q.resize(rank_four_masks.size());
                for (int& variable : item.q) variable = next++;
                if (rank_three_shadows) {
                    item.q_three.resize(rank_three_masks.size());
                    for (int& variable : item.q_three) variable = next++;
                }
                rank_four_shadow.push_back(std::move(item));
            }

        rank_seven_shadow.resize(rank_seven_masks.size());
        for (int column = 0; column < static_cast<int>(rank_seven_masks.size());
             ++column) {
            RankSevenShadow& item = rank_seven_shadow[column];
            item.target = rank_seven_masks[column];
            item.active = next++;
            item.L0 = next;
            next += N;
            item.R0 = next;
            next += N;
            item.M0 = next;
            next += N;
        }

        // Unary endpoint/length summaries for the selected rank-six row.
        // B[l][d] means that its unique interval beginning at l is [l,l+d];
        // the right-hand array is the dual statement for a fixed right end.
        for (int endpoint = 0; endpoint < N; ++endpoint)
            for (int length = 0; length < 4; ++length) {
                rank_six_by_left[endpoint][length] = next++;
                rank_six_by_right[endpoint][length] = next++;
            }
    }

    unique_ptr<BandCutPlan> band_cut_plan;
    if (band_cuts) band_cut_plan = make_unique<BandCutPlan>(next, central[1]);
    unique_ptr<JointBandCutPlan> joint_band_cut_plan;
    if (joint_band_cuts)
        joint_band_cut_plan = make_unique<JointBandCutPlan>(
            next, central[0], central[1], *band_cut_plan);
    unique_ptr<EndpointAlignmentCutPlan> endpoint_alignment_cut_plan;
    if (endpoint_alignment_cuts)
        endpoint_alignment_cut_plan = make_unique<EndpointAlignmentCutPlan>(
            next, central[0], rank_six_by_left, rank_six_by_right);
    unique_ptr<RankSixBranchProfilePlan> rank_six_branch_profile_plan;
    if (rank_six_branch == 1)
        rank_six_branch_profile_plan = make_unique<RankSixBranchProfilePlan>(
            next, *band_cut_plan, *joint_band_cut_plan);
    unique_ptr<LocalDensityPBPlan> local_density_pb_plan;
    if (local_density_pb)
        local_density_pb_plan = make_unique<LocalDensityPBPlan>(next);
    unique_ptr<RankFiltrationTypeIIPlan> rank_filtration_type2_plan;
    if (rank_filtration_type2)
        rank_filtration_type2_plan = make_unique<RankFiltrationTypeIIPlan>(
            next, *local_density_pb_plan, *joint_band_cut_plan,
            named_cell_hall);
    unique_ptr<RankFiltrationTypeIPlan> rank_filtration_type1_plan;
    if (rank_filtration_type1)
        rank_filtration_type1_plan = make_unique<RankFiltrationTypeIPlan>(
            next, *local_density_pb_plan, *joint_band_cut_plan);
    unique_ptr<RankSevenTruncatedWidthPlan> rank_seven_truncated_width_plan;
    if (rank_seven_truncated_width)
        rank_seven_truncated_width_plan =
            make_unique<RankSevenTruncatedWidthPlan>(
                next, rank_seven_shadow, rank_filtration_type1,
                joint_band_cut_plan->one);
    unique_ptr<TypeIITwoComponentPinPlan> two_component_pin_plan;
    if (two_component_pin_localization)
        two_component_pin_plan = make_unique<TypeIITwoComponentPinPlan>(
            next, *local_density_pb_plan, *rank_filtration_type2_plan);
    unique_ptr<TypeIIReversePinLoadPlan> type2_reverse_pin_load_plan;
    if (type2_reverse_pin_load)
        type2_reverse_pin_load_plan = make_unique<TypeIIReversePinLoadPlan>(
            next, *local_density_pb_plan, *joint_band_cut_plan,
            *rank_filtration_type2_plan, *two_component_pin_plan);
    unique_ptr<TypeIICompanionPinLoadPlan> type2_companion_pin_load_plan;
    if (type2_companion_pin_load)
        type2_companion_pin_load_plan =
            make_unique<TypeIICompanionPinLoadPlan>(
                next, *rank_filtration_type2_plan, *two_component_pin_plan,
                *type2_reverse_pin_load_plan);
    unique_ptr<NamedCellFamilyPlan> named_cell_hall_plan;
    if (named_cell_hall)
        named_cell_hall_plan = make_unique<NamedCellFamilyPlan>(
            next, *joint_band_cut_plan, rank_filtration_type1,
            rank_filtration_type2_plan.get(), direct, exception_three,
            exception_four);
    unique_ptr<SubcubeRunCreditPlan> subcube_deficiency_plan;
    if (subcube_deficiency)
        subcube_deficiency_plan = make_unique<SubcubeRunCreditPlan>(
            next, rank_filtration_type1);
    unique_ptr<TypeIFacetPinLoadPlan> type1_facet_pin_load_plan;
    if (type1_facet_pin_load)
        type1_facet_pin_load_plan = make_unique<TypeIFacetPinLoadPlan>(
            next, *local_density_pb_plan, *subcube_deficiency_plan);
    unique_ptr<TypeIRidgePinLoadPlan> type1_ridge_pin_load_plan;
    if (type1_ridge_pin_load)
        type1_ridge_pin_load_plan = make_unique<TypeIRidgePinLoadPlan>(
            next, *local_density_pb_plan, *type1_facet_pin_load_plan);
    unique_ptr<TypeIGlobalPairProfilePlan> type1_global_pair_profile_plan;
    if (type1_global_pair_profile)
        type1_global_pair_profile_plan =
            make_unique<TypeIGlobalPairProfilePlan>(
                next, *local_density_pb_plan);
    unique_ptr<ResidualCoordinateLexPlan> residual_coordinate_lex_plan;
    if (residual_coordinate_lex)
        residual_coordinate_lex_plan = make_unique<ResidualCoordinateLexPlan>(
            next, rank_filtration_type1);
    const int variable_total = next - 1;

    CaDiCaL::Solver solver;
    if (const char* proof_path = getenv("K11_FOREST_PROOF");
        proof_path && *proof_path && !solver.trace_proof(proof_path)) {
        cerr << "could not open proof trace " << proof_path << '\n';
        return 6;
    }
    solver.set("quiet", 1);
    solver.set("seed", sat_seed);
    solver.declare_more_variables(variable_total);
    long long clauses = 0;
    auto add = [&](initializer_list<int> clause) {
        for (int literal : clause) solver.add(literal);
        solver.add(0);
        ++clauses;
    };
    auto add_vector = [&](const vector<int>& clause) {
        for (int literal : clause) solver.add(literal);
        solver.add(0);
        ++clauses;
    };
    long long canonical_rank_six_entry_clauses = 0;
    long long singleton_pool_clauses = 0;
    long long rank_six_boundary_entry_clauses = 0;
    long long rank_six_branch_anchor_clauses = 0;
    long long rank_six_branch_unit_clauses = 0;
    long long min_component_schedule_clauses = 0;
    long long min_component_low_cap_clauses = 0;
    long long min_component_exception_clauses = 0;
    long long portal_branch_clauses = 0;
    long long q369_top_layer_clauses = 0;
    long long q369_rank_four_clauses = 0;
    long long type1_prefix_chain_clauses = 0;

    if (band_cut_plan)
        for (const vector<int>& clause : band_cut_plan->clauses)
            add_vector(clause);
    if (joint_band_cut_plan)
        for (const vector<int>& clause : joint_band_cut_plan->clauses)
            add_vector(clause);
    if (endpoint_alignment_cut_plan)
        for (const vector<int>& clause : endpoint_alignment_cut_plan->clauses)
            add_vector(clause);
    if (rank_six_branch_profile_plan)
        for (const vector<int>& clause : rank_six_branch_profile_plan->clauses)
            add_vector(clause);
    if (local_density_pb_plan)
        for (const vector<int>& clause : local_density_pb_plan->clauses)
            add_vector(clause);
    if (rank_filtration_type2_plan)
        for (const vector<int>& clause : rank_filtration_type2_plan->clauses)
            add_vector(clause);
    if (rank_filtration_type1_plan)
        for (const vector<int>& clause : rank_filtration_type1_plan->clauses)
            add_vector(clause);
    if (rank_seven_truncated_width_plan)
        for (const vector<int>& clause :
             rank_seven_truncated_width_plan->clauses)
            add_vector(clause);
    if (two_component_pin_plan)
        for (const vector<int>& clause : two_component_pin_plan->clauses)
            add_vector(clause);
    if (type2_reverse_pin_load_plan)
        for (const vector<int>& clause :
             type2_reverse_pin_load_plan->clauses)
            add_vector(clause);
    if (type2_companion_pin_load_plan)
        for (const vector<int>& clause :
             type2_companion_pin_load_plan->clauses)
            add_vector(clause);
    if (named_cell_hall_plan)
        for (const vector<int>& clause : named_cell_hall_plan->clauses)
            add_vector(clause);
    if (subcube_deficiency_plan)
        subcube_deficiency_plan->emit([&](int literal) {
            solver.add(literal);
            if (literal == 0) ++clauses;
        });
    if (type1_facet_pin_load_plan)
        for (const vector<int>& clause : type1_facet_pin_load_plan->clauses)
            add_vector(clause);
    if (type1_ridge_pin_load_plan)
        for (const vector<int>& clause : type1_ridge_pin_load_plan->clauses)
            add_vector(clause);
    if (type1_global_pair_profile_plan)
        for (const vector<int>& clause :
             type1_global_pair_profile_plan->clauses)
            add_vector(clause);
    if (residual_coordinate_lex_plan)
        for (const vector<int>& clause : residual_coordinate_lex_plan->clauses)
            add_vector(clause);

    // In the Type-I branch A[0]=63.  The residual lex quotient orders the
    // five outside coordinate columns, so their first occurrences are
    // nested in the reverse coordinate order.  Every prefix OR through
    // position zero therefore lies in the fixed chain
    //
    //   63,1087,1599,1855,1983,2047.
    //
    // Every other upper target may choose a witness avoiding position zero.
    // This is a consequence of the existing array/coordinate normalization;
    // it introduces no new variables or prescribed middle-row structure.
    if (type1_prefix_chain) {
        constexpr int endpoint_mask = 63;
        constexpr array<int, 12> canonical_by_rank{{
            -1, -1, -1, -1, -1, -1, 63, 1087, 1599, 1855, 1983, 2047,
        }};
        for (const DirectTarget& item : direct) {
            if (item.rank < 7 || item.rank > 10) continue;
            // If the target does not contain A[0]=63, an existing absent-bit
            // clause already forces Inside(0)=false.  Only endpoint supersets
            // need the residual-lex consequence exposed explicitly.
            if ((item.target & endpoint_mask) != endpoint_mask) continue;
            if (item.target == canonical_by_rank[item.rank]) continue;
            add({-(item.M0 + 0)});
            ++type1_prefix_chain_clauses;
        }
        if (adjacent_shadows) {
            const auto canonical = lower_bound(rank_seven_masks.begin(),
                                               rank_seven_masks.end(),
                                               canonical_by_rank[7]);
            if (canonical == rank_seven_masks.end() ||
                *canonical != canonical_by_rank[7])
                return 4;
            const int canonical_column =
                static_cast<int>(canonical - rank_seven_masks.begin());
            for (int column = 0;
                 column < static_cast<int>(rank_seven_masks.size()); ++column) {
                if ((rank_seven_masks[column] & endpoint_mask) != endpoint_mask)
                    continue;
                if (rank_seven_masks[column] == canonical_by_rank[7]) continue;
                const RankSevenShadow& item = rank_seven_shadow[column];
                add({-item.active, -(item.M0 + 0)});
                ++type1_prefix_chain_clauses;
            }
            // Every generic slot already selects exactly one rank-seven
            // target.  Hence Inside(0) may be true iff that target is the
            // unique canonical rank-seven prefix value 1087.  One clause per
            // slot is equivalent to all 329 noncanonical target guards.
            for (const ExceptionSlot& slot : exception_seven) {
                add({-(slot.M0 + 0), slot.q[canonical_column]});
                ++type1_prefix_chain_clauses;
            }
        }
    }

    if (!portal_branch_mode.empty()) {
        constexpr array<int, 19> prefix_rank_six{{
            489, 429, 940, 828, 860, 1876, 1862, 1734, 1731, 1251,
            243, 123, 95, 543, 670, 1690, 1434, 1436, 444,
        }};
        constexpr array<int, 22> prefix_entries{{
            489, 425, 424, 300, 780, 788, 836, 1604, 1602, 1218, 195,
            99, 83, 27, 30, 538, 154, 1176, 408, 4, 32, 514,
        }};
        CentralLayer& upper = central[1];
        const int short_state = state_index(0, 2);
        const int long_state = state_index(0, 3);
        const int short_prefix =
            portal_branch_mode == "q369_schedule" ? 369 : 19;
        for (int i = 0; i < MIDDLE; ++i) {
            add({upper.state[i][i < short_prefix ? short_state : long_state]});
            ++portal_branch_clauses;
        }
        if (portal_branch_mode == "q19_factor_prefix") {
            for (int position = 0;
                 position < static_cast<int>(prefix_entries.size()); ++position)
                for (int bit = 0; bit < K; ++bit) {
                    add({prefix_entries[position] & (1 << bit)
                             ? A(position, bit)
                             : -A(position, bit)});
                    ++portal_branch_clauses;
                }
        } else if (portal_branch_mode == "q19_fixed_row") {
            for (int i = 0; i < static_cast<int>(prefix_rank_six.size()); ++i) {
                const auto found = lower_bound(upper.masks.begin(),
                                               upper.masks.end(),
                                               prefix_rank_six[i]);
                if (found == upper.masks.end() || *found != prefix_rank_six[i])
                    return 4;
                const int column = static_cast<int>(found - upper.masks.begin());
                add({upper.q[i * MIDDLE + column]});
                ++portal_branch_clauses;
            }
        } else if (portal_branch_mode == "q19_abstract") {
            constexpr array<int, 12> required_rank_seven{{
                251, 493, 607, 941, 956, 1267,
                1468, 1694, 1763, 1884, 1946, 1990,
            }};
            for (int required : required_rank_seven) {
                const auto found = find_if(
                    rank_seven_shadow.begin(), rank_seven_shadow.end(),
                    [required](const RankSevenShadow& item) {
                        return item.target == required;
                    });
                if (found == rank_seven_shadow.end()) return 4;
                const RankSevenShadow& item = *found;
                auto L = [&](int p) { return item.L0 + p; };
                auto R = [&](int p) { return item.R0 + p; };

                // Select the crossed-witness encoding and force its exact
                // length-four interval to start in zero-based 0..17.  If the
                // unary left threshold first becomes true at start, the two
                // implications below fix the right endpoint to start+3.
                add({item.active});
                add({L(17)});
                portal_branch_clauses += 2;
                for (int start = 0; start <= 17; ++start) {
                    if (start == 0) {
                        add({-L(start), R(start + 3)});
                        add({-L(start), -R(start + 4)});
                    } else {
                        add({-L(start), L(start - 1), R(start + 3)});
                        add({-L(start), L(start - 1), -R(start + 4)});
                    }
                    portal_branch_clauses += 2;
                }
            }
        }
        if (portal_branch_mode == "q19_fixed_row" ||
            portal_branch_mode == "q19_abstract") {
            auto target = find_if(direct.begin(), direct.end(),
                                  [](const DirectTarget& item) {
                                      return item.target == 958;
                                  });
            if (target == direct.end()) return 4;
            // L(p) means p is at or to the right of the selected left end;
            // R(p) means p is at or to the left of the selected right end.
            // These four units fix the direct witness to zero-based [18,21].
            add({target->L0 + 18});
            add({-(target->L0 + 17)});
            add({target->R0 + 21});
            add({-(target->R0 + 22)});
            portal_branch_clauses += 4;
        }
    }

    if (q369_top_layer_cut) {
        // In q369_schedule the 369 selected rank-six triples, together with
        // the 1023 masks of ranks 1,...,5, saturate all
        //   465 + 464 + 463 = 1392
        // physical intervals of lengths at most three.  Delete those 369
        // triple cells from the short-interval containment poset.  Its 463
        // maximal remaining cells, in increasing endpoint order, are
        //
        //   pairs [s,s+1],   s=0,...,368,
        //   triples [s,s+2], s=369,...,462.
        //
        // Every rank-five value must occupy a maximal remaining cell: a
        // strict residual superinterval would otherwise have a distinct OR
        // of rank at most five properly containing it.  The 462 monotone
        // rank-five witnesses therefore omit exactly one cell of this list.
        // Row i can only use list cell i or i+1.  Existing exact-one and
        // monotonicity clauses turn the binary choices below into the single
        // omission schedule; no new selector variables are necessary.
        CentralLayer& lower = central[0];
        const int pair_here = state_index(0, 1);
        const int pair_next = state_index(1, 2);
        const int triple_here = state_index(0, 2);
        const int triple_next = state_index(1, 3);
        for (int i = 0; i < MIDDLE; ++i) {
            if (i < 368)
                add({lower.state[i][pair_here], lower.state[i][pair_next]});
            else if (i == 368)
                add({lower.state[i][pair_here], lower.state[i][triple_next]});
            else
                add({lower.state[i][triple_here], lower.state[i][triple_next]});
            ++q369_top_layer_clauses;
        }

        // After the rank-five cells are removed, every rank-four witness is
        // maximal in the residual rank<=4 poset.  A crossed rank-four
        // witness has length one or two.  Independently of which one of the
        // 463 cells above was omitted, its only possible crossed locations
        // are an early singleton (position 0,...,368) or a late pair (start
        // 369,...,463).  The omitted early pair / late triple, if rank four,
        // is necessarily handled by an exception slot because it has no two
        // proper rank-five endpoint extensions.  Suppressing the other q
        // flags is therefore an exact consequence, not a heuristic cap.
        //
        // The second-state literal in row i says that the omitted pool cell
        // is at or before i.  Thus omission 0 is skip(0), omission 462 is
        // !skip(461), and an internal omission j is !skip(j-1)&skip(j).
        // An early singleton ceases to be maximal when either adjacent pair
        // is omitted; dually a late pair ceases to be maximal when either
        // containing triple is omitted.  The guarded clauses below encode
        // those exact next-layer exclusions as well.
        auto skipped = [&](int i) {
            return lower.state[i][i < 368 ? pair_next : triple_next];
        };
        auto forbid_omission = [&](int q, int omitted) {
            if (omitted == 0)
                add({-q, -skipped(0)});
            else if (omitted == MIDDLE)
                add({-q, skipped(MIDDLE - 1)});
            else
                add({-q, skipped(omitted - 1), -skipped(omitted)});
            ++q369_rank_four_clauses;
        };
        for (const RankFourShadow& item : rank_four_shadow) {
            const bool singleton = item.left == item.right;
            const bool allowed = singleton ? item.left <= 368 : item.left >= 369;
            for (int q : item.q) {
                if (!allowed) {
                    add({-q});
                    ++q369_rank_four_clauses;
                    continue;
                }
                if (singleton) {
                    forbid_omission(q, item.left);
                    if (item.left > 0) forbid_omission(q, item.left - 1);
                } else {
                    if (item.left <= MIDDLE)
                        forbid_omission(q, item.left);
                    if (item.left > 369)
                        forbid_omission(q, item.left - 1);
                }
            }
        }
    }

    // The canonical and oriented-boundary gates already imply
    // e -> A[0]=63.  The one mismatch implication below anchors the converse
    // witness choice, after which the unit clause selects one exact portfolio
    // branch: e=0 has no literal rank-six entry, while e=1 has A[0]=63.
    if (rank_six_branch >= 0) {
        constexpr int canonical = (1 << 6) - 1;
        const int e = joint_band_cut_plan->e;
        vector<int> anchor{e};
        anchor.reserve(K + 1);
        for (int bit = 0; bit < K; ++bit)
            anchor.push_back(canonical & (1 << bit) ? -A(0, bit) : A(0, bit));
        add_vector(anchor);
        ++rank_six_branch_anchor_clauses;
        add({rank_six_branch == 1 ? e : -e});
        ++rank_six_branch_unit_clauses;
    }

    // The odd cross-layer theorem allows at most one distinct literal
    // rank-six entry.  Coordinate permutations are transitive on six-sets,
    // so a satisfiability-preserving symmetry break fixes that possible mask
    // to the low six bits.  No clause requires the canonical mask to occur.
    if (canonical_rank_six_entry) {
        constexpr int canonical = (1 << 6) - 1;
        for (int position = 0; position < N; ++position)
            for (int mask : central[1].masks) {
                if (mask == canonical) continue;
                vector<int> mismatch;
                mismatch.reserve(K);
                for (int bit = 0; bit < K; ++bit)
                    mismatch.push_back(mask & (1 << bit) ? -A(position, bit)
                                                         : A(position, bit));
                add_vector(mismatch);
                ++canonical_rank_six_entry_clauses;
            }
    }

    // Any literal rank-six entry may be deliberately selected as a singleton
    // witness.  The audited monotone-band theorem then localizes it to one of
    // the two physical endpoints, so the standalone necessary cut forbids
    // every rank-six mask at positions 1,...,463.  Two rank-six endpoint
    // entries are impossible; when the coordinate-canonical gate is active,
    // reversal symmetry may therefore put the sole possible entry at the
    // left endpoint.  In that interaction branch, the global canonical
    // clauses already forbid every noncanonical mask and this gate forbids
    // only mask 63 at positions 1,...,464.
    if (rank_six_boundary_entry) {
        constexpr int canonical = (1 << 6) - 1;
        const int last_position = canonical_rank_six_entry ? N - 1 : N - 2;
        for (int position = 1; position <= last_position; ++position) {
            for (int mask : central[1].masks) {
                if (canonical_rank_six_entry && mask != canonical) continue;
                vector<int> mismatch;
                mismatch.reserve(K);
                for (int bit = 0; bit < K; ++bit)
                    mismatch.push_back(mask & (1 << bit) ? -A(position, bit)
                                                         : A(position, bit));
                add_vector(mismatch);
                ++rank_six_boundary_entry_clauses;
            }
        }
    }

    // The short-interval pool theorem gives x3>=93+2*x0.  BandCutPlan already
    // enforces x3>=93, while JointBandCutPlan's e is exactly x0 in {0,1}.
    // With g3 and g4 denoting the exact boundaries before and after state 03,
    // the guarded suffix clauses below say e -> g4-g3>=95.
    if (singleton_pool_cut) {
        const int e = joint_band_cut_plan->e;
        const auto& g3 = band_cut_plan->boundary[2];
        const auto& g4 = band_cut_plan->boundary[3];
        for (int t = 0; t <= MIDDLE; ++t) {
            vector<int> clause{-e, -g3[t]};
            for (int s = t + 95; s <= MIDDLE; ++s)
                clause.push_back(g4[s]);
            add_vector(clause);
            ++singleton_pool_clauses;
        }
    }

    // A length-465 optimum is zero-free: deleting a zero would contradict the
    // proved lower bound 465.  Enforcing this also improves propagation.
    for (int position = 0; position < N; ++position) {
        vector<int> nonzero;
        for (int bit = 0; bit < K; ++bit) {
            const int variable = A(position, bit);
            solver.phase(seed[position] & (1 << bit) ? variable : -variable);
            nonzero.push_back(variable);
        }
        add_vector(nonzero);
    }

    int exact_phase_targets = 0;
    for (const DirectTarget& item : direct) {
        const int target = item.target;
        const int bound = item.bound;
        const BestInterval best = best_interval(seed, target, bound);
        if (best.value == target) ++exact_phase_targets;
        auto L = [&](int p) { return item.L0 + p; };
        auto R = [&](int p) { return item.R0 + p; };
        auto Inside = [&](int p) { return item.M0 + p; };
        auto H = [&](int bit, int p) { return item.H0[bit] + p; };

        for (int p = 0; p < N; ++p) {
            solver.phase(p >= best.left ? L(p) : -L(p));
            solver.phase(p <= best.right ? R(p) : -R(p));
            solver.phase(p >= best.left && p <= best.right ? Inside(p) : -Inside(p));
        }
        add({L(N - 1)});
        for (int p = 0; p + 1 < N; ++p) add({-L(p), L(p + 1)});
        add({R(0)});
        for (int p = 0; p + 1 < N; ++p) add({-R(p + 1), R(p)});
        vector<int> some_inside;
        some_inside.reserve(N);
        for (int p = 0; p < N; ++p) {
            add({-Inside(p), L(p)});
            add({-Inside(p), R(p)});
            add({-L(p), -R(p), Inside(p)});
            some_inside.push_back(Inside(p));
        }
        add_vector(some_inside);
        if (bound <= 0) {
            add_vector({});
        } else if (bound < N) {
            for (int p = 0; p + bound < N; ++p)
                add({-Inside(p), -Inside(p + bound)});
        }

        for (int bit = 0; bit < K; ++bit) {
            if (!(target & (1 << bit))) {
                for (int p = 0; p < N; ++p) add({-Inside(p), -A(p, bit)});
                continue;
            }
            int phase_occurrence = best.left;
            for (int p = best.left; p <= best.right; ++p)
                if (seed[p] & (1 << bit)) {
                    phase_occurrence = p;
                    break;
                }
            vector<int> occurrence;
            occurrence.reserve(N);
            for (int p = 0; p < N; ++p) {
                const int h = H(bit, p);
                solver.phase(p == phase_occurrence ? h : -h);
                add({-h, Inside(p)});
                add({-h, A(p, bit)});
                occurrence.push_back(h);
            }
            add_vector(occurrence);
        }
    }

    array<vector<BestInterval>, 2> phase_witnesses;
    array<bool, 2> exact_central_phase{};
    for (int layer = 0; layer < 2; ++layer)
        phase_witnesses[layer] =
            central_phase(seed, central[layer].rank, exact_central_phase[layer]);

    // The two globally-WLOG monotone band schedules and their small physical
    // interval ORs.
    for (int layer = 0; layer < 2; ++layer) {
        CentralLayer& data = central[layer];

        for (int i = 0; i < MIDDLE; ++i) {
            vector<int> one_state(data.state[i].begin(), data.state[i].end());
            add_vector(one_state);
            for (int u = 0; u < 10; ++u)
                for (int v = u + 1; v < 10; ++v)
                    add({-data.state[i][u], -data.state[i][v]});

            int phase_state = layer == 0 ? state_index(0, 2) : state_index(0, 3);
            int phase_mask = -1;
            if (exact_central_phase[layer]) {
                const BestInterval& witness = phase_witnesses[layer][i];
                phase_state = state_index(witness.left - i, witness.right - i);
                phase_mask = witness.target;
            }
            for (int u = 0; u < 10; ++u)
                solver.phase(u == phase_state ? data.state[i][u] : -data.state[i][u]);

            // Rank-five witnesses may WLOG use the rank-six pruning bound 3.
            if (data.rank == 5) add({-data.state[i][state_index(0, 3)]});

            for (int u = 0; u < 10; ++u) {
                const auto [alpha, beta] = STATES[u];
                const int z = data.state[i][u];
                for (int bit = 0; bit < K; ++bit) {
                    const int c = data.value[i][bit];
                    vector<int> positive{-z, -c};
                    for (int p = i + alpha; p <= i + beta; ++p) {
                        positive.push_back(A(p, bit));
                        add({-z, -A(p, bit), c});
                    }
                    add_vector(positive);
                }
            }

            // Exact cardinality of the central value.  K=11 is small enough
            // that the direct subset clauses are both simple and compact.
            for_combinations(K, data.rank + 1, [&](const vector<int>& subset) {
                vector<int> clause;
                for (int bit : subset) clause.push_back(-data.value[i][bit]);
                add_vector(clause);
            });
            for_combinations(K, K - data.rank + 1, [&](const vector<int>& subset) {
                vector<int> clause;
                for (int bit : subset) clause.push_back(data.value[i][bit]);
                add_vector(clause);
            });

            for (int bit = 0; bit < K; ++bit) {
                const bool present = phase_mask >= 0 && (phase_mask & (1 << bit));
                solver.phase(present ? data.value[i][bit] : -data.value[i][bit]);
            }
            for (int column = 0; column < MIDDLE; ++column) {
                const int q = data.q[i * MIDDLE + column];
                solver.phase(phase_mask == data.masks[column] ? q : -q);
                const int mask = data.masks[column];
                for (int bit = 0; bit < K; ++bit)
                    if (mask & (1 << bit)) add({-q, data.value[i][bit]});
            }
        }

        for (int i = 0; i + 1 < MIDDLE; ++i)
            for (int u = 0; u < 10; ++u)
                for (int v = 0; v < 10; ++v)
                    if (STATES[v].first < STATES[u].first ||
                        STATES[v].second < STATES[u].second)
                        add({-data.state[i][u], -data.state[i + 1][v]});

        for (int column = 0; column < MIDDLE; ++column) {
            vector<int> occurrence;
            occurrence.reserve(MIDDLE);
            for (int i = 0; i < MIDDLE; ++i)
                occurrence.push_back(data.q[i * MIDDLE + column]);
            add_vector(occurrence);
        }
    }

    // Exact minimal-component portfolios.  These clauses are deliberately
    // opt-in: without K11_FOREST_MIN_COMPONENT the original formula is byte
    // for byte unchanged.  P_i is the i-th selected rank-five interval and
    // Q_i the i-th selected rank-six interval in their common monotone order.
    //
    // e0c1: reversal is sound because there is no anchored literal entry, so
    // choose the left colour as the perfect matching.  Then
    //   Q_i=[l(P_i),r(P_{i+1})], i<461,
    // and Q_461 is a proper same-left extension of P_461.
    //
    // e1c2: Q_0=[0,0] is the canonical literal six-set and the other component
    // is P_0,Q_1,...,Q_461,P_461, with
    //   Q_{i+1}=[l(P_i),r(P_{i+1})].
    if (!min_component_mode.empty()) {
        CentralLayer& lower = central[0];
        CentralLayer& upper = central[1];

        auto add_or_equivalence = [&](int out, int x, int y) {
            add({-x, out});
            add({-y, out});
            add({-out, x, y});
            min_component_schedule_clauses += 3;
        };
        auto add_and_equivalence = [&](int out, int x, int y) {
            add({-out, x});
            add({-out, y});
            add({out, -x, -y});
            min_component_schedule_clauses += 3;
        };
        auto imply_state_projection = [&](int premise,
                                          const vector<int>& support) {
            vector<int> clause{-premise};
            clause.insert(clause.end(), support.begin(), support.end());
            add_vector(clause);
            ++min_component_schedule_clauses;
        };

        if (min_component_mode == "e1c2") {
            constexpr int canonical = (1 << 6) - 1;
            add({upper.state[0][state_index(0, 0)]});
            ++min_component_schedule_clauses;
            for (int bit = 0; bit < K; ++bit) {
                add({canonical & (1 << bit) ? upper.value[0][bit]
                                             : -upper.value[0][bit]});
                ++min_component_schedule_clauses;
            }

            for (int i = 0; i < MIDDLE - 1; ++i) {
                // l(Q_{i+1})=l(P_i): alpha(Q)=alpha(P_i)-1.
                for (int u = 0; u < 10; ++u) {
                    vector<int> support;
                    const int wanted = STATES[u].first - 1;
                    for (int v = 0; v < 10; ++v)
                        if (STATES[v].first == wanted)
                            support.push_back(upper.state[i + 1][v]);
                    imply_state_projection(lower.state[i][u], support);
                }
                // r(Q_{i+1})=r(P_{i+1}): beta(Q)=beta(P_{i+1}).
                for (int u = 0; u < 10; ++u) {
                    vector<int> support;
                    const int wanted = STATES[u].second;
                    for (int v = 0; v < 10; ++v)
                        if (STATES[v].second == wanted)
                            support.push_back(upper.state[i + 1][v]);
                    imply_state_projection(lower.state[i + 1][u], support);
                }
                for (int bit = 0; bit < K; ++bit)
                    add_or_equivalence(upper.value[i + 1][bit],
                                       lower.value[i][bit],
                                       lower.value[i + 1][bit]);
            }
            for (int i = 1; i < MIDDLE - 1; ++i)
                for (int bit = 0; bit < K; ++bit)
                    add_and_equivalence(lower.value[i][bit],
                                        upper.value[i][bit],
                                        upper.value[i + 1][bit]);
        } else {
            // In e0c1 reversal exchanges the endpoint colours and preserves
            // every other enabled condition, so taking left as perfect loses
            // no solutions in this named branch.
            for (int i = 0; i < MIDDLE - 1; ++i) {
                // l(Q_i)=l(P_i): alpha(Q)=alpha(P_i).
                for (int u = 0; u < 10; ++u) {
                    vector<int> support;
                    const int wanted = STATES[u].first;
                    for (int v = 0; v < 10; ++v)
                        if (STATES[v].first == wanted)
                            support.push_back(upper.state[i][v]);
                    imply_state_projection(lower.state[i][u], support);
                }
                // r(Q_i)=r(P_{i+1}): beta(Q)=beta(P_{i+1})+1.
                for (int u = 0; u < 10; ++u) {
                    vector<int> support;
                    const int wanted = STATES[u].second + 1;
                    for (int v = 0; v < 10; ++v)
                        if (STATES[v].second == wanted)
                            support.push_back(upper.state[i][v]);
                    imply_state_projection(lower.state[i + 1][u], support);
                }
                for (int bit = 0; bit < K; ++bit)
                    add_or_equivalence(upper.value[i][bit],
                                       lower.value[i][bit],
                                       lower.value[i + 1][bit]);
            }
            // Q_461 is the proper same-left extension of P_461.
            for (int u = 0; u < 10; ++u) {
                vector<int> support;
                for (int v = 0; v < 10; ++v)
                    if (STATES[v].first == STATES[u].first &&
                        STATES[v].second > STATES[u].second)
                        support.push_back(upper.state[MIDDLE - 1][v]);
                imply_state_projection(lower.state[MIDDLE - 1][u], support);
            }
            for (int i = 1; i < MIDDLE; ++i)
                for (int bit = 0; bit < K; ++bit)
                    add_and_equivalence(lower.value[i][bit],
                                        upper.value[i - 1][bit],
                                        upper.value[i][bit]);
        }

        if (min_component_mode == "e1c2") {
            // After deleting A[0], all rank<=4 witnesses have length at most
            // two.  These clauses apply the theorem to direct and generic
            // exception witnesses, while crossed candidates already have
            // length at most two by construction.
            for (const DirectTarget& item : direct)
                if (item.rank <= 4)
                    for (int p = 0; p + 2 < N; ++p) {
                        add({-(item.M0 + p), -(item.M0 + p + 2)});
                        ++min_component_low_cap_clauses;
                    }
            auto cap_exception_slots = [&](vector<ExceptionSlot>& slots) {
                for (ExceptionSlot& slot : slots)
                    if (slot.rank <= 4)
                        for (int p = 0; p + 2 < N; ++p) {
                            add({-(slot.M0 + p), -(slot.M0 + p + 2)});
                            ++min_component_low_cap_clauses;
                        }
            };
            cap_exception_slots(exception_three);
            cap_exception_slots(exception_four);

            // At most four rank-three/rank-four targets require a generic
            // slot.  Retain the existing six-slot allocation, but duplicate
            // the target names of slots 4,5 from slots 0,1.  Witness variables
            // remain independent, so this is complete even when fillers are
            // needed because fewer than four exceptions occur.
            auto restrict_to_four_exception_names =
                [&](vector<ExceptionSlot>& slots) {
                    if (slots.size() != 6) return;
                    for (int duplicate = 4; duplicate < 6; ++duplicate) {
                        const int source = duplicate - 4;
                        for (int column = 0;
                             column < static_cast<int>(slots[duplicate].q.size());
                             ++column) {
                            const int x = slots[duplicate].q[column];
                            const int y = slots[source].q[column];
                            add({-x, y});
                            add({x, -y});
                            min_component_exception_clauses += 2;
                        }
                    }
                };
            restrict_to_four_exception_names(exception_three);
            restrict_to_four_exception_names(exception_four);
        }
    }

    long long adjacent_rank_four_flags = 0;
    long long adjacent_rank_seven_flags = 0;
    if (adjacent_shadows) {
        auto add_interval_thresholds = [&](int L0, int R0, int M0, int bound) {
            auto L = [&](int p) { return L0 + p; };
            auto R = [&](int p) { return R0 + p; };
            auto Inside = [&](int p) { return M0 + p; };
            add({L(N - 1)});
            for (int p = 0; p + 1 < N; ++p) add({-L(p), L(p + 1)});
            add({R(0)});
            for (int p = 0; p + 1 < N; ++p) add({-R(p + 1), R(p)});
            vector<int> some_inside;
            some_inside.reserve(N);
            for (int p = 0; p < N; ++p) {
                add({-Inside(p), L(p)});
                add({-Inside(p), R(p)});
                add({-L(p), -R(p), Inside(p)});
                some_inside.push_back(Inside(p));
            }
            add_vector(some_inside);
            if (bound <= 0) {
                add_vector({});
            } else if (bound < N) {
                for (int p = 0; p + bound < N; ++p)
                    add({-Inside(p), -Inside(p + bound)});
            }
        };

        auto encode_exception_slots = [&](const vector<int>& masks,
                                          vector<ExceptionSlot>& slots) {
            for (ExceptionSlot& slot : slots) {
                add_interval_thresholds(slot.L0, slot.R0, slot.M0, slot.bound);
                auto Inside = [&](int p) { return slot.M0 + p; };
                auto H = [&](int bit, int p) { return slot.H0[bit] + p; };
                for (int bit = 0; bit < K; ++bit) {
                    vector<int> occurrence{-slot.value[bit]};
                    occurrence.reserve(N + 1);
                    for (int p = 0; p < N; ++p) {
                        const int h = H(bit, p);
                        add({-h, Inside(p)});
                        add({-h, A(p, bit)});
                        add({-Inside(p), -A(p, bit), slot.value[bit]});
                        occurrence.push_back(h);
                    }
                    add_vector(occurrence);
                }
                for_combinations(K, slot.rank + 1, [&](const vector<int>& subset) {
                    vector<int> clause;
                    for (int bit : subset) clause.push_back(-slot.value[bit]);
                    add_vector(clause);
                });
                for_combinations(K, K - slot.rank + 1,
                                 [&](const vector<int>& subset) {
                                     vector<int> clause;
                                     for (int bit : subset)
                                         clause.push_back(slot.value[bit]);
                                     add_vector(clause);
                                 });
                vector<int> one_target;
                one_target.reserve(masks.size());
                for (int column = 0; column < static_cast<int>(masks.size());
                     ++column) {
                    const int q = slot.q[column];
                    one_target.push_back(q);
                    for (int bit = 0; bit < K; ++bit)
                        if (masks[column] & (1 << bit))
                            add({-q, slot.value[bit]});
                }
                // Exact cardinality makes two distinct target flags
                // incompatible, so the one positive clause is exact-one.
                add_vector(one_target);
            }
        };
        if (rank_three_shadows)
            encode_exception_slots(rank_three_masks, exception_three);
        encode_exception_slots(rank_four_masks, exception_four);
        encode_exception_slots(rank_seven_masks, exception_seven);

        // At most six rank-four targets need not be crossed by the chosen
        // rank-five endpoint flags.  A crossed witness has length one or two;
        // materialize all 929 such physical intervals once and share them
        // across the 330 targets.
        vector<vector<int>> cover_three(rank_three_masks.size());
        vector<vector<int>> cover_four(rank_four_masks.size());
        for (RankFourShadow& item : rank_four_shadow) {
            for (int bit = 0; bit < K; ++bit) {
                vector<int> positive{-item.value[bit]};
                for (int p = item.left; p <= item.right; ++p) {
                    positive.push_back(A(p, bit));
                    add({-A(p, bit), item.value[bit]});
                }
                add_vector(positive);
            }
            // If this interval is assigned a target, its OR has rank at most
            // four.  The four forced target bits then give equality.
            for_combinations(K, 5, [&](const vector<int>& subset) {
                vector<int> clause{-item.at_most_four};
                for (int bit : subset) clause.push_back(-item.value[bit]);
                add_vector(clause);
            });
            if (rank_three_shadows)
                for_combinations(K, 4, [&](const vector<int>& subset) {
                    vector<int> clause{-item.at_most_three};
                    for (int bit : subset) clause.push_back(-item.value[bit]);
                    add_vector(clause);
                });

            vector<int> left_extensions;
            vector<int> right_extensions;
            for (int i = 0; i < MIDDLE; ++i)
                for (int u = 0; u < 10; ++u) {
                    const auto [alpha, beta] = STATES[u];
                    const int left = i + alpha, right = i + beta;
                    const int z = central[0].state[i][u];
                    if (left == item.left && right > item.right)
                        left_extensions.push_back(z);
                    if (right == item.right && left < item.left)
                        right_extensions.push_back(z);
                }

            for (int column = 0; column < static_cast<int>(rank_four_masks.size());
                 ++column) {
                const int q = item.q[column];
                cover_four[column].push_back(q);
                add({-q, item.at_most_four});
                for (int bit = 0; bit < K; ++bit)
                    if (rank_four_masks[column] & (1 << bit))
                        add({-q, item.value[bit]});
                vector<int> left_clause{-q};
                left_clause.insert(left_clause.end(), left_extensions.begin(),
                                   left_extensions.end());
                add_vector(left_clause);
                vector<int> right_clause{-q};
                right_clause.insert(right_clause.end(), right_extensions.begin(),
                                    right_extensions.end());
                add_vector(right_clause);
                ++adjacent_rank_four_flags;
            }
            if (rank_three_shadows)
                for (int column = 0;
                     column < static_cast<int>(rank_three_masks.size());
                     ++column) {
                    const int q = item.q_three[column];
                    cover_three[column].push_back(q);
                    add({-q, item.at_most_three});
                    for (int bit = 0; bit < K; ++bit)
                        if (rank_three_masks[column] & (1 << bit))
                            add({-q, item.value[bit]});
                    vector<int> left_clause{-q};
                    left_clause.insert(left_clause.end(),
                                       left_extensions.begin(),
                                       left_extensions.end());
                    add_vector(left_clause);
                    vector<int> right_clause{-q};
                    right_clause.insert(right_clause.end(),
                                        right_extensions.begin(),
                                        right_extensions.end());
                    add_vector(right_clause);
                }
        }
        if (rank_three_shadows)
            for (int column = 0;
                 column < static_cast<int>(rank_three_masks.size()); ++column) {
                for (const ExceptionSlot& slot : exception_three)
                    cover_three[column].push_back(slot.q[column]);
                add_vector(cover_three[column]);
            }
        for (int column = 0; column < static_cast<int>(rank_four_masks.size());
             ++column) {
            for (const ExceptionSlot& slot : exception_four)
                cover_four[column].push_back(slot.q[column]);
            add_vector(cover_four[column]);
        }

        // Summarize the selected rank-six schedule by physical endpoint and
        // length.  Definitions are bidirectional, so the comparisons below
        // do not merely guess an endpoint flag.
        for (int endpoint = 0; endpoint < N; ++endpoint)
            for (int length = 0; length < 4; ++length) {
                vector<int> begins{-rank_six_by_left[endpoint][length]};
                vector<int> ends{-rank_six_by_right[endpoint][length]};
                for (int i = 0; i < MIDDLE; ++i)
                    for (int u = 0; u < 10; ++u) {
                        const auto [alpha, beta] = STATES[u];
                        const int left = i + alpha, right = i + beta;
                        const int z = central[1].state[i][u];
                        if (left == endpoint && right - left == length) {
                            begins.push_back(z);
                            add({-z, rank_six_by_left[endpoint][length]});
                        }
                        if (right == endpoint && right - left == length) {
                            ends.push_back(z);
                            add({-z, rank_six_by_right[endpoint][length]});
                        }
                    }
                add_vector(begins);
                add_vector(ends);
            }

        // For a nonexceptional rank-seven target choose its crossed witness
        // J=[l,r].  The rank-six schedule must contain a proper prefix of J
        // starting at l and a proper suffix ending at r.  Since both six-sets
        // lie in J and are distinct subsets of the seven-set, their union is
        // the target; only the four absent bits need explicit array clauses.
        for (int column = 0; column < static_cast<int>(rank_seven_masks.size());
             ++column) {
            RankSevenShadow& item = rank_seven_shadow[column];
            const int target = item.target;
            add_interval_thresholds(item.L0, item.R0, item.M0,
                                    witness_bound(7));
            auto L = [&](int p) { return item.L0 + p; };
            auto R = [&](int p) { return item.R0 + p; };
            auto Inside = [&](int p) { return item.M0 + p; };
            for (int bit = 0; bit < K; ++bit)
                if (!(target & (1 << bit)))
                    for (int p = 0; p < N; ++p)
                        add({-item.active, -Inside(p), -A(p, bit)});

            for (int left = 0; left < N; ++left) {
                vector<int> used{-item.active, -L(left)};
                if (left > 0) used.push_back(L(left - 1));
                for (int length = 0; length < 4; ++length)
                    used.push_back(rank_six_by_left[left][length]);
                add_vector(used);
                for (int length = 0; length < 4; ++length) {
                    vector<int> clause{-item.active, -L(left),
                                       -rank_six_by_left[left][length]};
                    if (left > 0) clause.push_back(L(left - 1));
                    const int next_position = left + length + 1;
                    if (next_position < N) clause.push_back(R(next_position));
                    add_vector(clause);
                    ++adjacent_rank_seven_flags;
                }
            }
            for (int right = 0; right < N; ++right) {
                vector<int> used{-item.active, -R(right)};
                if (right + 1 < N) used.push_back(R(right + 1));
                for (int length = 0; length < 4; ++length)
                    used.push_back(rank_six_by_right[right][length]);
                add_vector(used);
                for (int length = 0; length < 4; ++length) {
                    vector<int> clause{-item.active, -R(right),
                                       -rank_six_by_right[right][length]};
                    if (right + 1 < N) clause.push_back(R(right + 1));
                    const int previous_position = right - length - 1;
                    if (previous_position >= 0)
                        clause.push_back(L(previous_position));
                    add_vector(clause);
                    ++adjacent_rank_seven_flags;
                }
            }
            vector<int> covered{item.active};
            for (const ExceptionSlot& slot : exception_seven)
                covered.push_back(slot.q[column]);
            add_vector(covered);
        }
    }

    // Materialize the two endpoint-colour matchings.  Schedule pairs that
    // would nest in the wrong rank direction are impossible.  Legal shared
    // endpoints expose C5 subset C6 directly to propagation.
    long long left_forest_cases = 0, right_forest_cases = 0;
    CentralLayer& lower = central[0];
    CentralLayer& upper = central[1];
    for (int i = 0; i < MIDDLE; ++i) {
        const int first_j = max(0, i - 3);
        const int last_j = min(MIDDLE - 1, i + 3);
        for (int j = first_j; j <= last_j; ++j) {
            for (int u = 0; u < 10; ++u) {
                const auto [a5, b5] = STATES[u];
                const int l5 = i + a5, r5 = i + b5;
                for (int v = 0; v < 10; ++v) {
                    const auto [a6, b6] = STATES[v];
                    const int l6 = j + a6, r6 = j + b6;
                    const int z5 = lower.state[i][u], z6 = upper.state[j][v];
                    if (l5 == l6) {
                        ++left_forest_cases;
                        if (r5 >= r6) {
                            add({-z5, -z6});
                        } else {
                            for (int bit = 0; bit < K; ++bit)
                                add({-z5, -z6, -lower.value[i][bit],
                                     upper.value[j][bit]});
                        }
                    }
                    if (r5 == r6) {
                        ++right_forest_cases;
                        if (l6 >= l5) {
                            add({-z5, -z6});
                        } else {
                            for (int bit = 0; bit < K; ++bit)
                                add({-z5, -z6, -lower.value[i][bit],
                                     upper.value[j][bit]});
                        }
                    }
                }
            }
        }
    }

    cerr << "variables=" << variable_total << " clauses=" << clauses
         << " direct_targets=" << direct.size()
         << " exact_direct_phase=" << exact_phase_targets << '/' << direct.size()
         << " exact_central_phase=" << exact_central_phase[0] << ','
         << exact_central_phase[1]
         << " forest_cases_LR=" << left_forest_cases << ',' << right_forest_cases
         << " adjacent_shadows=" << adjacent_shadows
         << " band_cuts=" << band_cuts
         << " joint_band_cuts=" << joint_band_cuts
         << " endpoint_alignment_cuts=" << endpoint_alignment_cuts
         << " rank3_shadows=" << rank_three_shadows
         << " canonical_rank6_entry=" << canonical_rank_six_entry
         << " singleton_pool_cut=" << singleton_pool_cut
         << " rank6_boundary_entry=" << rank_six_boundary_entry
         << " local_density_pb=" << local_density_pb
         << " rank_filtration_type2=" << rank_filtration_type2
         << " rank_filtration_type1=" << rank_filtration_type1
         << " named_cell_hall=" << named_cell_hall
         << " residual_coordinate_lex=" << residual_coordinate_lex
         << " type1_prefix_chain=" << type1_prefix_chain
         << " type1_facet_pin_load=" << type1_facet_pin_load
         << " type1_ridge_pin_load=" << type1_ridge_pin_load
         << " type1_global_pair_profile=" << type1_global_pair_profile
         << " two_component_pin_localization="
         << two_component_pin_localization
         << " type2_reverse_pin_load=" << type2_reverse_pin_load
         << " type2_companion_pin_load=" << type2_companion_pin_load
         << " rank7_truncated_width=" << rank_seven_truncated_width
         << " subcube_deficiency=" << subcube_deficiency
         << " containment_caps=" << containment_caps
         << " portal_branch="
         << (portal_branch_mode.empty() ? string("none") : portal_branch_mode)
         << " portal_branch_clauses=" << portal_branch_clauses
         << " q369_top_layer_cut=" << q369_top_layer_cut
         << " q369_top_layer_clauses=" << q369_top_layer_clauses
         << " q369_rank_four_clauses=" << q369_rank_four_clauses
         << " type1_prefix_chain_clauses=" << type1_prefix_chain_clauses
         << " canonical_rank6_entry_clauses="
         << canonical_rank_six_entry_clauses
         << " singleton_pool_clauses=" << singleton_pool_clauses
         << " rank6_boundary_entry_clauses="
         << rank_six_boundary_entry_clauses
         << " rank6_branch="
         << (rank_six_branch < 0 ? string("none")
                                 : to_string(rank_six_branch))
         << " rank6_branch_anchor_clauses="
         << rank_six_branch_anchor_clauses
         << " rank6_branch_unit_clauses=" << rank_six_branch_unit_clauses;
    if (!min_component_mode.empty())
        cerr << " min_component=" << min_component_mode
             << " min_component_schedule_clauses="
             << min_component_schedule_clauses
             << " min_component_low_cap_clauses="
             << min_component_low_cap_clauses
             << " min_component_exception_clauses="
             << min_component_exception_clauses;
    if (adjacent_shadows)
        cerr << " shadow4_candidates=" << rank_four_shadow.size()
             << " shadow4_flags=" << adjacent_rank_four_flags
             << " shadow7_comparisons=" << adjacent_rank_seven_flags
             << " exception_slots=" << exception_three.size() << ','
             << exception_four.size() << ',' << exception_seven.size();
    if (band_cut_plan)
        cerr << " band_cut_variables=" << band_cut_plan->variables()
             << " band_cut_clauses=" << band_cut_plan->clauses.size();
    if (joint_band_cut_plan)
        cerr << " joint_band_cut_variables=" << joint_band_cut_plan->variables()
             << " joint_band_cut_clauses="
             << joint_band_cut_plan->clauses.size();
    if (endpoint_alignment_cut_plan)
        cerr << " endpoint_alignment_cut_variables="
             << endpoint_alignment_cut_plan->variables()
             << " endpoint_alignment_cut_clauses="
             << endpoint_alignment_cut_plan->clauses.size();
    if (rank_six_branch_profile_plan)
        cerr << " rank6_branch_profile_variables="
             << rank_six_branch_profile_plan->variables()
             << " rank6_branch_profile_clauses="
             << rank_six_branch_profile_plan->clauses.size();
    if (local_density_pb_plan)
        cerr << " local_density_pb_variables="
             << local_density_pb_plan->variables()
             << " local_density_pb_clauses="
             << local_density_pb_plan->clauses.size();
    if (rank_filtration_type2_plan)
        cerr << " rank_filtration_type2_variables="
             << rank_filtration_type2_plan->variables()
             << " rank_filtration_type2_clauses="
             << rank_filtration_type2_plan->clauses.size()
             << " rank_filtration_type2_rank_cap_clauses="
             << rank_filtration_type2_plan->rank_cap_clauses
             << " rank_filtration_type2_component_definition_clauses="
             << rank_filtration_type2_plan->component_definition_clauses
             << " rank_filtration_type2_component_automaton_clauses="
             << rank_filtration_type2_plan->component_automaton_clauses
             << " rank_filtration_type2_coordinate_separator_clauses="
             << rank_filtration_type2_plan->coordinate_separator_clauses
             << " rank_filtration_type2_slack_one_pair_clauses="
             << rank_filtration_type2_plan->slack_one_pair_clauses;
    if (rank_filtration_type1_plan)
        cerr << " rank_filtration_type1_variables="
             << rank_filtration_type1_plan->variables()
             << " rank_filtration_type1_clauses="
             << rank_filtration_type1_plan->clauses.size()
             << " rank_filtration_type1_rank_cap_clauses="
             << rank_filtration_type1_plan->rank_cap_clauses
             << " rank_filtration_type1_component_definition_clauses="
             << rank_filtration_type1_plan->component_definition_clauses;
    if (rank_seven_truncated_width_plan)
        cerr << " rank7_truncated_width_variables="
             << rank_seven_truncated_width_plan->variables()
             << " rank7_truncated_width_clauses="
             << rank_seven_truncated_width_plan->clauses.size()
             << " rank7_truncated_width_credit_variables="
             << rank_seven_truncated_width_plan->credit_variable_count
             << " rank7_truncated_width_counter_variables="
             << rank_seven_truncated_width_plan->counter_variable_count
             << " rank7_truncated_width_location_clauses="
             << rank_seven_truncated_width_plan->location_clauses
             << " rank7_truncated_width_inactive_clauses="
             << rank_seven_truncated_width_plan->inactive_credit_clauses
             << " rank7_truncated_width_counter_clauses="
             << rank_seven_truncated_width_plan->counter_clauses
             << " rank7_truncated_width_comparator_clauses="
             << rank_seven_truncated_width_plan->comparator_clauses;
    if (two_component_pin_plan)
        cerr << " two_component_pin_variables="
             << two_component_pin_plan->variables()
             << " two_component_pin_clauses="
             << two_component_pin_plan->clauses.size()
             << " two_component_pin_membership_clauses="
             << two_component_pin_plan->membership_clauses
             << " two_component_pin_coordinate_union_clauses="
             << two_component_pin_plan->coordinate_union_clauses
             << " two_component_pin_deficit_clauses="
             << two_component_pin_plan->deficit_clauses
             << " two_component_pin_threshold_clauses="
             << two_component_pin_plan->threshold_clauses
             << " two_component_pin_rank_counter_clauses="
             << two_component_pin_plan->rank_counter_clauses
             << " two_component_pin_rank_row_clauses="
             << two_component_pin_plan->rank_row_clauses;
    if (type2_reverse_pin_load_plan)
        cerr << " type2_reverse_pin_load_variables="
             << type2_reverse_pin_load_plan->variables()
             << " type2_reverse_pin_load_clauses="
             << type2_reverse_pin_load_plan->clauses.size()
             << " type2_reverse_pin_load_slack_one_union_variables="
             << type2_reverse_pin_load_plan->slack_one_union_variable_count
             << " type2_reverse_pin_load_slack_one_union_clauses="
             << type2_reverse_pin_load_plan->slack_one_union_clauses
             << " type2_reverse_pin_load_counter_variables="
             << type2_reverse_pin_load_plan->occurrence_counter_variable_count
             << " type2_reverse_pin_load_counter_clauses="
             << type2_reverse_pin_load_plan->occurrence_counter_clauses
             << " type2_reverse_pin_load_arithmetic_variables="
             << type2_reverse_pin_load_plan->arithmetic_variable_count
             << " type2_reverse_pin_load_arithmetic_clauses="
             << type2_reverse_pin_load_plan->arithmetic_clauses
             << " type2_reverse_pin_load_threshold_clauses="
             << type2_reverse_pin_load_plan->threshold_clauses;
    if (type2_companion_pin_load_plan)
        cerr << " type2_companion_pin_load_variables="
             << type2_companion_pin_load_plan->variables()
             << " type2_companion_pin_load_clauses="
             << type2_companion_pin_load_plan->clauses.size()
             << " type2_companion_pin_load_counter_variables="
             << type2_companion_pin_load_plan
                    ->occurrence_counter_variable_count
             << " type2_companion_pin_load_counter_clauses="
             << type2_companion_pin_load_plan->occurrence_counter_clauses
             << " type2_companion_pin_load_arithmetic_variables="
             << type2_companion_pin_load_plan->arithmetic_variable_count
             << " type2_companion_pin_load_arithmetic_clauses="
             << type2_companion_pin_load_plan->arithmetic_clauses
             << " type2_companion_pin_load_threshold_clauses="
             << type2_companion_pin_load_plan->threshold_clauses;
    if (named_cell_hall_plan)
        cerr << " named_cell_hall_variables="
             << named_cell_hall_plan->variables()
             << " named_cell_hall_clauses="
             << named_cell_hall_plan->clauses.size()
             << " named_cell_hall_mode_clauses="
             << named_cell_hall_plan->mode_clauses
             << " named_cell_hall_location_clauses="
             << named_cell_hall_plan->location_clauses
             << " named_cell_hall_width_clauses="
             << named_cell_hall_plan->width_clauses
             << " named_cell_hall_direct_targets="
             << named_cell_hall_plan->capped_direct_targets
             << " named_cell_hall_exception_slots="
             << named_cell_hall_plan->capped_exception_slots;
    if (subcube_deficiency_plan)
        cerr << " subcube_deficiency_variables="
             << subcube_deficiency_plan->variables()
             << " subcube_deficiency_clauses="
             << subcube_deficiency_plan->clause_count
             << " subcube_type1_core_variables="
             << subcube_deficiency_plan->type1_core_variables
             << " subcube_type1_core_clauses="
             << subcube_deficiency_plan->type1_core_clauses;
    if (type1_facet_pin_load_plan)
        cerr << " type1_facet_pin_load_variables="
             << type1_facet_pin_load_plan->variables()
             << " type1_facet_pin_load_clauses="
             << type1_facet_pin_load_plan->clauses.size()
             << " type1_facet_pin_load_gate_variables="
             << type1_facet_pin_load_plan->gate_variable_count
             << " type1_facet_pin_load_counter_variables="
             << type1_facet_pin_load_plan->counter_variable_count
             << " type1_facet_pin_load_gate_clauses="
             << type1_facet_pin_load_plan->gate_clauses
             << " type1_facet_pin_load_counter_clauses="
             << type1_facet_pin_load_plan->counter_clauses
             << " type1_facet_pin_load_comparator_clauses="
             << type1_facet_pin_load_plan->comparator_clauses;
    if (type1_ridge_pin_load_plan)
        cerr << " type1_ridge_pin_load_variables="
             << type1_ridge_pin_load_plan->variables()
             << " type1_ridge_pin_load_clauses="
             << type1_ridge_pin_load_plan->clauses.size()
             << " type1_ridge_pin_load_gate_variables="
             << type1_ridge_pin_load_plan->gate_variable_count
             << " type1_ridge_pin_load_counter_variables="
             << type1_ridge_pin_load_plan->counter_variable_count
             << " type1_ridge_pin_load_gate_clauses="
             << type1_ridge_pin_load_plan->gate_clauses
             << " type1_ridge_pin_load_counter_clauses="
             << type1_ridge_pin_load_plan->counter_clauses
             << " type1_ridge_pin_load_comparator_clauses="
             << type1_ridge_pin_load_plan->comparator_clauses;
    if (type1_global_pair_profile_plan)
        cerr << " type1_global_pair_profile_variables="
             << type1_global_pair_profile_plan->variables()
             << " type1_global_pair_profile_clauses="
             << type1_global_pair_profile_plan->clauses.size()
             << " type1_global_pair_profile_counter_variables="
             << type1_global_pair_profile_plan->counter_variable_count
             << " type1_global_pair_profile_counter_clauses="
             << type1_global_pair_profile_plan->counter_clauses
             << " type1_global_pair_profile_arithmetic_variables="
             << type1_global_pair_profile_plan->arithmetic_variable_count
             << " type1_global_pair_profile_arithmetic_clauses="
             << type1_global_pair_profile_plan->arithmetic_clauses
             << " type1_global_pair_profile_comparator_clauses="
             << type1_global_pair_profile_plan->comparator_clauses;
    if (residual_coordinate_lex_plan)
        cerr << " residual_coordinate_lex_variables="
             << residual_coordinate_lex_plan->variables()
             << " residual_coordinate_lex_clauses="
             << residual_coordinate_lex_plan->clauses.size();
    cerr
         << '\n';

    if (const char* dimacs_path = getenv("K11_FOREST_DIMACS");
        dimacs_path && *dimacs_path) {
        if (const char* error = solver.write_dimacs(dimacs_path, variable_total)) {
            cerr << "could not write DIMACS " << dimacs_path << ": " << error << '\n';
            return 7;
        }
        cerr << "DIMACS=" << dimacs_path << '\n';
    }

    if (const char* build_only = getenv("K11_FOREST_BUILD_ONLY");
        build_only && string(build_only) != "0") {
        cerr << "BUILD_ONLY\n";
        return 0;
    }

    const int result = solver.solve();
    if (result != 10) {
        cerr << (result == 20 ? "UNSAT" : "UNKNOWN") << '\n';
        return 1;
    }
    ofstream output(argv[2]);
    if (!output) return 5;
    for (int position = 0; position < N; ++position) {
        int value = 0;
        for (int bit = 0; bit < K; ++bit)
            if (solver.val(A(position, bit)) > 0) value |= 1 << bit;
        output << value << (position + 1 == N ? '\n' : ' ');
    }
    cerr << "SAT\n";
    return 0;
}
