#!/usr/bin/env python3
"""Finite audit for the nonidentical endpoint-order CSP theorem.

The proofs in MATH_THEOREM_NONIDENTICAL_ENDPOINT_ORDER_CSP_AND_PAIRING_BARRIER_20260821.md
are independent of this script.  The script checks the exact physical/CSP
dictionary, cyclic-deck rigidity, and the adjacent-swap partial-coordinate
construction in small cases.  Run on H100.
"""

from collections import defaultdict
from functools import lru_cache
import itertools
import math

from explore_complementary_bank_full_upper_coverage_20260821 import tight_factor


def interval(order, start, size):
    b = len(order)
    return frozenset(order[(start + j) % b] for j in range(size))


def deck(order, size):
    return tuple(interval(order, i, size) for i in range(len(order)))


def rotate(order, shift):
    shift %= len(order)
    return order[shift:] + order[:shift]


def conjugate_factor(factor, permutation):
    return [tuple(permutation[x] for x in order) for order in factor]


def product_word(alpha, beta, r):
    b = len(alpha)
    types = "A" * r + "B" * (b - r)
    ia = ib = 0
    out = []
    for time in range(b * b + 2 * b):
        if types[time % b] == "A":
            out.append(("A", alpha[ia % b]))
            ia += 1
        else:
            out.append(("B", beta[ib % b]))
            ib += 1
    return types, out


def target_pair(word, start, length, b):
    x = frozenset(label for side, label in word[start : start + length] if side == "A")
    z = frozenset(label for side, label in word[start : start + length] if side == "B")
    y = frozenset(set(range(b)) - set(z))
    return x, y


def physical_endpoint_union(b, q, s, lookahead, factor_s, factor_t, shifts_0, shifts_1):
    t = s - q
    covered = set()

    for ai, alpha in enumerate(factor_s):
        for bi, beta in enumerate(factor_s):
            shift = shifts_0[(ai, bi)]
            types, word = product_word(alpha, rotate(beta, shift), s)
            for start in range(b * b):
                phase = start % b
                if all(types[(phase + j) % b] == "B" for j in range(lookahead)):
                    pair = target_pair(word, start, b + q, b)
                    assert len(pair[0]) == s and len(pair[1]) == t
                    covered.add(pair)

    for gi, gamma in enumerate(factor_t):
        for di, delta in enumerate(factor_t):
            shift = shifts_1[(gi, di)]
            types, word = product_word(gamma, rotate(delta, shift), t)
            for start in range(b * b):
                phase = start % b
                if all(types[(phase + j) % b] == "A" for j in range(lookahead)):
                    pair = target_pair(word, start, b + q, b)
                    assert len(pair[0]) == s and len(pair[1]) == t
                    covered.add(pair)

    return covered


def csp_endpoint_union(b, q, s, lookahead, factor_s, factor_t, shifts_0, shifts_1):
    t = s - q
    owner_s = {}
    owner_t = {}
    down = defaultdict(list)
    up = defaultdict(list)

    for ai, alpha in enumerate(factor_s):
        for x in range(b):
            target = interval(alpha, x, s)
            assert target not in owner_s
            owner_s[target] = (ai, x)
        for y in range(b):
            down[interval(alpha, y, t)].append((ai, y))

    for di, delta in enumerate(factor_t):
        for y in range(b):
            target = interval(delta, y, t)
            assert target not in owner_t
            owner_t[target] = (di, y)
        for x in range(b):
            up[interval(delta, x, s)].append((di, x))

    assert len(owner_s) == len(list(itertools.combinations(range(b), s)))
    assert len(owner_t) == len(list(itertools.combinations(range(b), t)))

    j_0 = {(phase + q - s) % b for phase in range(s, b - lookahead + 1)}
    j_1 = {(phase - t) % b for phase in range(0, t - lookahead + 1)}
    assert len(j_0) == b - s - lookahead + 1
    assert len(j_1) == t - lookahead + 1

    covered = set()
    for x_set, (ai, x) in owner_s.items():
        for y_set, (di, y) in owner_t.items():
            hit = any(
                (x + yy - shifts_0[(ai, bi)]) % b in j_0
                for bi, yy in down[y_set]
            )
            if not hit:
                hit = any(
                    (xx + y - shifts_1[(gi, di)]) % b in j_1
                    for gi, xx in up[x_set]
                )
            if hit:
                covered.add((x_set, y_set))
    return covered


@lru_cache(None)
def factor(b, rank):
    return tuple(tight_factor(b, rank))


def check_exact_csp():
    cases = (
        (5, 1, 3, 1),
        (5, 1, 4, 1),
        (7, 1, 4, 2),
        (7, 1, 5, 1),
        (7, 2, 5, 2),
    )
    for b, q, s, lookahead in cases:
        t = s - q
        fs = list(factor(b, s))
        ft0 = list(factor(b, t))
        permutation = list(range(b))
        permutation[0], permutation[1] = permutation[1], permutation[0]
        ft = conjugate_factor(ft0, permutation)

        shifts_0 = {
            (i, j): (3 * i + 2 * j + 1) % b
            for i in range(len(fs))
            for j in range(len(fs))
        }
        shifts_1 = {
            (i, j): (2 * i + 4 * j + 3) % b
            for i in range(len(ft))
            for j in range(len(ft))
        }
        physical = physical_endpoint_union(
            b, q, s, lookahead, fs, ft, shifts_0, shifts_1
        )
        csp = csp_endpoint_union(b, q, s, lookahead, fs, ft, shifts_0, shifts_1)
        assert physical == csp
        print(
            "PASS exact CSP",
            (b, q, s, lookahead),
            "targets",
            len(csp),
        )


def check_zero_coordinate_bound():
    cases = (
        (7, 1, 3, 1),
        (7, 1, 5, 1),
        (7, 2, 5, 2),
    )
    for b, q, s, lookahead in cases:
        t = s - q
        fs = list(factor(b, s))
        ft0 = list(factor(b, t))
        permutation = list(range(b))
        permutation[0], permutation[2] = permutation[2], permutation[0]
        ft = conjugate_factor(ft0, permutation)

        shifts_0 = {
            (i, j): (i + 3 * j + 2) % b
            for i in range(len(fs))
            for j in range(len(fs))
        }
        shifts_1 = {
            (i, j): (4 * i + 2 * j + 1) % b
            for i in range(len(ft))
            for j in range(len(ft))
        }
        covered = physical_endpoint_union(
            b, q, s, lookahead, fs, ft, shifts_0, shifts_1
        )

        x_sets = [frozenset(x) for x in itertools.combinations(range(b), s)]
        y_sets = [frozenset(y) for y in itertools.combinations(range(b), t)]
        up_degree = {x: 0 for x in x_sets}
        down_degree = {y: 0 for y in y_sets}
        for gamma in ft:
            for x in deck(gamma, s):
                up_degree[x] += 1
        for beta in fs:
            for y in deck(beta, t):
                down_degree[y] += 1

        c_s = math.comb(b, s)
        c_t = math.comb(b, t)
        a_0 = b - s - lookahead + 1
        a_1 = t - lookahead + 1
        if c_s >= c_t:
            zero_x = [x for x in x_sets if up_degree[x] == 0]
            assert len(zero_x) >= c_s - c_t
            row_cap = a_0 * len(fs)
            for x in zero_x:
                assert sum(xx == x for xx, _ in covered) <= row_cap
            lower = (c_s - c_t) * max(0, c_t - row_cap)
        else:
            zero_y = [y for y in y_sets if down_degree[y] == 0]
            assert len(zero_y) >= c_t - c_s
            column_cap = a_1 * len(ft)
            for y in zero_y:
                assert sum(yy == y for _, yy in covered) <= column_cap
            lower = (c_t - c_s) * max(0, c_s - column_cap)
        misses = c_s * c_t - len(covered)
        assert misses >= lower
        assert lower > 0
        print(
            "PASS deterministic zero-coordinate bound",
            (b, q, s, lookahead),
            "lower",
            lower,
            "actual random-origin misses",
            misses,
        )


def cycle_edges(order):
    b = len(order)
    return frozenset(
        frozenset((order[i], order[(i + 1) % b])) for i in range(b)
    )


def check_deck_rigidity_and_adjacent_swaps():
    for b in (5, 7):
        orders = [(0,) + tail for tail in itertools.permutations(range(1, b))]
        for size in range(2, b - 1):
            groups = defaultdict(list)
            for order in orders:
                groups[frozenset(deck(order, size))].append(order)
            for same_deck in groups.values():
                assert len(same_deck) == 2
                assert len({cycle_edges(order) for order in same_deck}) == 1

            for order in orders:
                for position in range(b):
                    changed = list(order)
                    nxt = (position + 1) % b
                    changed[position], changed[nxt] = changed[nxt], changed[position]
                    changed = tuple(changed)
                    assert len(set(deck(order, size)) & set(deck(changed, size))) == b - 2
        print("PASS deck rigidity and adjacent swaps", b)


def endpoint_source(alpha, beta, r, q, lookahead, wanted):
    b = len(alpha)
    types, word = product_word(alpha, beta, r)
    out = set()
    for start in range(b * b):
        phase = start % b
        if all(types[(phase + j) % b] == wanted for j in range(lookahead)):
            out.add(target_pair(word, start, b + q, b))
    return out


def check_adjacent_swap_block():
    for b, q, s, lookahead in ((7, 1, 4, 1), (11, 1, 6, 1), (11, 2, 6, 2)):
        t = s - q
        alpha = tuple(range(b))
        beta = tuple((3 * i) % b for i in range(b))
        gamma = list(alpha)
        gamma[0], gamma[1] = gamma[1], gamma[0]
        gamma = tuple(gamma)
        delta = list(beta)
        delta[2], delta[3] = delta[3], delta[2]
        delta = tuple(delta)

        j_0 = {(phase + q - s) % b for phase in range(s, b - lookahead + 1)}
        j_1 = {(phase - t) % b for phase in range(0, t - lookahead + 1)}
        shift_1 = next(
            shift
            for shift in range(b)
            if j_0.isdisjoint({(value + shift) % b for value in j_1})
        )

        source_0 = endpoint_source(alpha, beta, s, q, lookahead, "B")
        source_1 = endpoint_source(gamma, rotate(delta, shift_1), t, q, lookahead, "A")
        union = source_0 | source_1

        good_x = {
            i for i in range(b) if interval(alpha, i, s) == interval(gamma, i, s)
        }
        good_y = {
            j for j in range(b) if interval(beta, j, t) == interval(delta, j, t)
        }
        assert len(good_x) == len(good_y) == b - 2

        certified = set()
        shifted_j_1 = {(value + shift_1) % b for value in j_1}
        for i in good_x:
            for j in good_y:
                if (i + j) % b in j_0 | shifted_j_1:
                    certified.add((interval(alpha, i, s), interval(beta, j, t)))
        assert certified <= union

        a = b - s - lookahead + 1
        c = t - lookahead + 1
        assert len(certified) >= (a + c) * b - 4 * b
        print(
            "PASS adjacent-swap block",
            (b, q, s, lookahead),
            "certified",
            len(certified),
            "physical union",
            len(union),
        )


def check_diagonal_signs():
    for b in (5, 7, 11):
        for eps_a in (-1, 1):
            for eps_b in (-1, 1):
                respects = True
                values = {}
                for i in range(b):
                    for j in range(b):
                        diagonal = (i + j) % b
                        image = (eps_a * i + eps_b * j + 3) % b
                        if diagonal in values and values[diagonal] != image:
                            respects = False
                        values[diagonal] = image
                assert respects == (eps_a == eps_b)
    print("PASS two-sided diagonal sign classification")


def check_interior_phase_budget():
    for b in (5, 7, 11, 13):
        for q in range(1, (b - 1) // 2 + 1):
            total = 0
            for r in range(q, b - q + 1):
                types = "A" * r + "B" * (b - r)
                counts = [
                    sum(types[(phase + j) % b] == "A" for j in range(q))
                    for phase in range(b)
                ]
                for z in range(1, q):
                    assert counts.count(z) == 2
                total += 2 * (q - 1) * math.comb(b, r) ** 2 // b
            assert total <= 2 * (q - 1) * math.comb(2 * b, b) // b
        print("PASS interior phase budget", b)


def main():
    check_exact_csp()
    check_zero_coordinate_bound()
    check_deck_rigidity_and_adjacent_swaps()
    check_adjacent_swap_block()
    check_diagonal_signs()
    check_interior_phase_budget()
    print("ALL NONIDENTICAL ENDPOINT-ORDER CSP CHECKS PASS")


if __name__ == "__main__":
    main()
