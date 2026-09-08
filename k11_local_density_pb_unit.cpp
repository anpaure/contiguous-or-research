#include <algorithm>
#include <cassert>
#include <cstdint>
#include <iostream>
#include <utility>
#include <vector>

using namespace std;

namespace {

struct CNF {
    int variables = 0;
    vector<vector<int>> clauses;

    int fresh() { return ++variables; }
    void add(initializer_list<int> clause) { clauses.emplace_back(clause); }

    bool accepts(uint64_t assignment) const {
        for (const vector<int>& clause : clauses) {
            bool satisfied = false;
            for (int literal : clause) {
                const bool value = (assignment >> (abs(literal) - 1)) & 1u;
                if (value == (literal > 0)) {
                    satisfied = true;
                    break;
                }
            }
            if (!satisfied) return false;
        }
        return true;
    }
};

void append_full_adder(CNF& cnf, int a, int b, int carry, int sum,
                       int next_carry) {
    for (int av = 0; av < 2; ++av)
        for (int bv = 0; bv < 2; ++bv)
            for (int cv = 0; cv < 2; ++cv) {
                const int parity = av ^ bv ^ cv;
                cnf.add({av ? -a : a, bv ? -b : b, cv ? -carry : carry,
                         parity ? sum : -sum});
            }
    cnf.add({-a, -b, next_carry});
    cnf.add({-a, -carry, next_carry});
    cnf.add({-b, -carry, next_carry});
    cnf.add({-next_carry, a, b});
    cnf.add({-next_carry, a, carry});
    cnf.add({-next_carry, b, carry});
}

void check_full_adder_truth_table() {
    CNF cnf;
    const int a = cnf.fresh(), b = cnf.fresh(), carry = cnf.fresh();
    const int sum = cnf.fresh(), next_carry = cnf.fresh();
    append_full_adder(cnf, a, b, carry, sum, next_carry);
    for (uint64_t assignment = 0; assignment < (1u << cnf.variables);
         ++assignment) {
        const int av = (assignment >> (a - 1)) & 1u;
        const int bv = (assignment >> (b - 1)) & 1u;
        const int cv = (assignment >> (carry - 1)) & 1u;
        const int sv = (assignment >> (sum - 1)) & 1u;
        const int nv = (assignment >> (next_carry - 1)) & 1u;
        const bool expected = sv == (av ^ bv ^ cv) &&
                              nv == ((av + bv + cv) >= 2);
        assert(cnf.accepts(assignment) == expected);
    }
}

void check_mux_truth_table() {
    CNF cnf;
    const int selector = cnf.fresh(), when_zero = cnf.fresh();
    const int when_one = cnf.fresh(), output = cnf.fresh();
    cnf.add({selector, -output, when_zero});
    cnf.add({selector, output, -when_zero});
    cnf.add({-selector, -output, when_one});
    cnf.add({-selector, output, -when_one});
    for (uint64_t assignment = 0; assignment < (1u << cnf.variables);
         ++assignment) {
        const bool s = (assignment >> (selector - 1)) & 1u;
        const bool z = (assignment >> (when_zero - 1)) & 1u;
        const bool o = (assignment >> (when_one - 1)) & 1u;
        const bool r = (assignment >> (output - 1)) & 1u;
        assert(cnf.accepts(assignment) == (r == (s ? o : z)));
    }
}

void check_ripple_adders() {
    for (int width = 1; width <= 4; ++width) {
        CNF cnf;
        vector<int> x(width), y(width);
        for (int& variable : x) variable = cnf.fresh();
        for (int& variable : y) variable = cnf.fresh();
        const int one = cnf.fresh();
        cnf.add({one});
        vector<int> result;
        int carry = -one;
        for (int bit = 0; bit < width; ++bit) {
            const int sum = cnf.fresh();
            const int next_carry = cnf.fresh();
            append_full_adder(cnf, x[bit], y[bit], carry, sum, next_carry);
            result.push_back(sum);
            carry = next_carry;
        }
        result.push_back(carry);

        const uint64_t input_mask = (uint64_t{1} << (2 * width)) - 1;
        const int auxiliary_count = cnf.variables - 2 * width - 1;
        for (unsigned xv = 0; xv < (1u << width); ++xv)
            for (unsigned yv = 0; yv < (1u << width); ++yv) {
                uint64_t fixed = xv | (uint64_t{yv} << width) |
                                 (uint64_t{1} << (one - 1));
                int satisfying = 0;
                unsigned decoded = 0;
                for (uint64_t aux = 0; aux < (uint64_t{1} << auxiliary_count);
                     ++aux) {
                    const uint64_t assignment =
                        fixed | (aux << (2 * width + 1));
                    if (!cnf.accepts(assignment)) continue;
                    ++satisfying;
                    decoded = 0;
                    for (int bit = 0; bit < static_cast<int>(result.size());
                         ++bit)
                        if ((assignment >> (result[bit] - 1)) & 1u)
                            decoded |= 1u << bit;
                }
                (void)input_mask;
                assert(satisfying == 1);
                assert(decoded == xv + yv);
            }
    }
}

void check_unsigned_comparators() {
    for (int width = 1; width <= 5; ++width) {
        CNF cnf;
        vector<int> x(width), y(width);
        for (int& variable : x) variable = cnf.fresh();
        for (int& variable : y) variable = cnf.fresh();
        const int one = cnf.fresh();
        cnf.add({one});
        int equal_above = one;
        for (int bit = width - 1; bit >= 0; --bit) {
            cnf.add({-equal_above, -x[bit], y[bit]});
            if (bit == 0) continue;
            const int next_equal = cnf.fresh();
            cnf.add({-next_equal, equal_above});
            cnf.add({-next_equal, -x[bit], y[bit]});
            cnf.add({-next_equal, x[bit], -y[bit]});
            cnf.add({-equal_above, -x[bit], -y[bit], next_equal});
            cnf.add({-equal_above, x[bit], y[bit], next_equal});
            equal_above = next_equal;
        }

        const int auxiliary_count = cnf.variables - 2 * width - 1;
        for (unsigned xv = 0; xv < (1u << width); ++xv)
            for (unsigned yv = 0; yv < (1u << width); ++yv) {
                const uint64_t fixed = xv | (uint64_t{yv} << width) |
                                       (uint64_t{1} << (one - 1));
                int satisfying = 0;
                for (uint64_t aux = 0; aux < (uint64_t{1} << auxiliary_count);
                     ++aux) {
                    const uint64_t assignment =
                        fixed | (aux << (2 * width + 1));
                    satisfying += cnf.accepts(assignment);
                }
                assert(satisfying == (xv <= yv ? 1 : 0));
            }
    }
}

}  // namespace

int main() {
    check_mux_truth_table();
    check_full_adder_truth_table();
    check_ripple_adders();
    check_unsigned_comparators();
    cout << "PASS: mux, full-adder, ripple-adder, and unsigned-comparator "
            "truth tables\n";
}
