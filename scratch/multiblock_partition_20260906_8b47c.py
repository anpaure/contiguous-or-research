"""Exact checks for the multiblock partition note; decimals are diagnostics.

Run with python3 -B to avoid changing existing Python cache files.
All assertions use integer or rational arithmetic.
"""

from fractions import Fraction as F
from itertools import combinations, combinations_with_replacement, product
from math import comb, factorial

from density_bridge_frontier_20260905_c71e4 import bridge, unions
from four_block_cross_split_20260905_d29f6 import multiply_chains, product_chains, width3
from recursive_scd_coalescent_20260905_f6b82 import grid_width


def q(x, t):
    x = abs(x)
    return 0 if x <= t else min(2 * (x - t), x)


def density3(a, b, c):
    a, b, c = sorted(map(F, (a, b, c)))
    return 1 / c - max(F(0), a + b - c) ** 2 / (4 * a * b * c)


def four_cost(xs):
    a, b, c, d = sorted(map(F, xs))
    return 1 / d + density3(a, b, c)


def five_merge_cost(xs, i, j):
    a, b = F(xs[i]), F(xs[j])
    c, d, e = sorted(F(x) for t, x in enumerate(xs) if t not in (i, j))
    lo, hi = abs(a - b), a + b

    def primitive(s):
        return (s * s / (2 * e) + s * s / (2 * d)
                - (max(F(0), s - d + c) ** 3
                   - max(F(0), s - c - d) ** 3) / (12 * c * d))

    value = primitive(min(hi, e)) - primitive(min(lo, e))
    l, u = max(lo, e), max(hi, e)
    value += u - l + density3(c, d, e) * (u * u - l * l) / 2
    return value / (2 * a * b)


def binomial_interpolant(k, x):
    lo = x.numerator // x.denominator
    s = x - lo
    left = comb(k, lo) if 0 <= lo <= k else 0
    right = comb(k, lo + 1) if 0 <= lo + 1 <= k else 0
    return (1 - s) * left + s * right


def scd(bits):
    chains = [[0]]
    for bit in bits:
        following = []
        for chain in chains:
            following.append(chain + [chain[-1] | bit])
            if len(chain) > 1:
                following.append([x | bit for x in chain[:-1]])
        chains = following
    return chains


def check_shifted_partitions():
    cases = 0
    for left_size, right_size in ((2, 3), (3, 3), (3, 4), (4, 4), (4, 5)):
        k = left_size + right_size
        left_u = (1 << left_size) - 1
        right_u = ((1 << right_size) - 1) << left_size
        full = left_u | right_u
        left = scd([1 << i for i in range(left_size - 1)])
        right = scd([1 << i for i in range(left_size, k - 1)])
        # Unequal prefix/suffix cuts deliberately destroy the common center.
        left = [part for chain in left for part in (chain[:1], chain[1:]) if part]
        right = [part for chain in right for part in (chain[:2], chain[2:]) if part]
        seen = set()
        ledger = 0
        rectangle_pairs = []
        for c, d in product(left, right):
            for sign in (0, 1):
                desired = d if sign == 0 else [right_u ^ y for y in reversed(d)]
                targets = {x | y for x, y in product(c, desired)}
                targets |= {full ^ x for x in tuple(targets)}
                assert not (seen & targets)
                seen.update(targets)
                ledger += len(c) + len(d)
                rectangle_pairs.append((c, desired))
        assert seen == set(range(1 << k))
        for t in (F(1, 3), F(2, 3), F(1), F(3, 2), F(2)):
            lhs = F(0)
            for c, d in rectangle_pairs:
                a, b = len(c), len(d)
                center = F(c[0].bit_count() + c[-1].bit_count()
                           + d[0].bit_count() + d[-1].bit_count() - k, 2)
                u, v = F(a + b, 2), F(abs(a - b), 2)
                local = (q(center - u, t) + q(center + u, t)
                         - q(center - v, t) - q(center + v, t))
                assert local <= a + b
                lhs += 2 * local
            middle = F(k, 2)
            bound = (2 * binomial_interpolant(k, middle + t)
                     - binomial_interpolant(k, middle + 2 * t))
            assert lhs == 2 * bound
            assert ledger >= bound
            cases += 1
    return cases


def four_charge(lengths):
    a, b, c, d = sorted(lengths)
    return a * b * c + d * width3(a, b, c)


def check_finite_switch():
    cases = 0
    for scale in range(1, 9):
        for a, b, c in combinations_with_replacement(range(1, scale + 1), 3):
            for d, e in combinations_with_replacement(range(2 * scale, 2 * scale + 6), 2):
                baseline = sum(four_charge((a, b, c, r))
                               for r in range(abs(d - e) + 1, d + e, 2))
                alternative = a * b * c * d + e * grid_width((a, b, c, d))
                assert F(scale * (baseline - alternative), a * b * c * d * e) >= F(37, 192)
                cases += 1
    return cases


def check_switch_word(sizes, scale_squared):
    universes, decompositions = [], []
    k = 0
    for size in sizes:
        universes.append(((1 << size) - 1) << k)
        decompositions.append(scd([1 << i for i in range(k, k + size - 1)]))
        k += size
    full = (1 << k) - 1
    adjacency, partition = {}, set()
    main_cost = edges = switched = baseline_cost = 0
    for chains in product(*decompositions):
        a, b, c, d, e = map(len, chains)
        switch = max(a, b, c) ** 2 <= scale_squared <= min(d, e) ** 2 / F(4)
        baseline_cost += 16 * sum(four_charge((a, b, c, r))
                                  for r in range(abs(d - e) + 1, d + e, 2))
        for signs in product((0, 1), repeat=4):
            factors = [(u, tuple(chain) if sign == 0 else tuple(u ^ x for x in reversed(chain)))
                       for u, chain, sign in zip(universes, chains, (0,) + signs)]
            if switch:
                four_tuples = [(factors[:4], factors[4])]
                switched += 1
            else:
                four_tuples = []
                for child in multiply_chains(factors[3][1], factors[4][1]):
                    current = factors[:3] + [(universes[3] | universes[4], tuple(child))]
                    fixed = max(range(4), key=lambda i: len(current[i][1]))
                    four_tuples.append(([v for i, v in enumerate(current) if i != fixed],
                                        current[fixed]))
            for moving_factors, fixed in four_tuples:
                moving_support = sum(u for u, _ in moving_factors)
                for chain in product_chains([chain for _, chain in moving_factors]):
                    left = (moving_support, tuple(chain))
                    right = (fixed[0], tuple(fixed[0] ^ x for x in reversed(fixed[1])))
                    adjacency.setdefault(left, []).append(right)
                    adjacency.setdefault(right, []).append(left)
                    main_cost += len(chain) + len(fixed[1])
                    edges += 1
                    required = {x | y for x in chain for y in fixed[1]}
                    required |= {full ^ x for x in tuple(required)}
                    assert not (partition & required)
                    partition.update(required)
    assert partition == set(range(full + 1))
    assert main_cost < baseline_cost if switched else main_cost == baseline_cost
    word = []
    for root in adjacency:
        if not adjacency[root]:
            continue
        stack, circuit = [root], []
        while stack:
            if adjacency[stack[-1]]:
                stack.append(adjacency[stack[-1]].pop())
            else:
                circuit.append(stack.pop())
        circuit.reverse()
        assert circuit[0] == circuit[-1]
        for support, chain in circuit:
            word.extend(bridge(chain, support))
    assert all(word)
    assert main_cost <= len(word) <= main_cost + 2 * edges + (k + 1) * len(adjacency)
    assert unions(word) == set(range(1, full + 1))
    return len(word), main_cost, baseline_cost, switched


def main():
    tested = 0
    for a, b, c, t in product(range(1, 13), range(1, 13), range(-30, 31), range(1, 10)):
        # All coordinates here are doubled, so no floating point is used.
        u, v = a + b, abs(a - b)
        value = q(c - u, t) + q(c + u, t) - q(c - v, t) - q(c + v, t)
        assert value <= 2 * u
        tested += 1
    print(f"Translated-rectangle dual checks: {tested}")
    print(f"Exact shifted full-cube partition checks: {check_shifted_partitions()}")

    four_checks = 0
    for xs in combinations_with_replacement(range(1, 9), 4):
        isolated = [1 / F(x) + density3(*(y for j, y in enumerate(xs) if i != j))
                    for i, x in enumerate(xs)]
        assert four_cost(xs) == min(isolated)
        four_checks += 1
    print(f"Four-factor exchange formula checks: {four_checks}")

    equal = (F(1),) * 5
    assert five_merge_cost(equal, 0, 1) == F(73, 48)
    xs = (2, 2, 3, 3, 3)
    values = [(five_merge_cost(xs, i, j), (i, j)) for i, j in combinations(range(5), 2)]
    greedy = five_merge_cost(xs, 0, 1)
    best, pair = min(values)
    assert best < greedy
    print(f"Five equal lengths: {five_merge_cost(equal, 0, 1)}")
    print(f"Continuum non-greedy example {xs}: smallest pair={greedy}, optimum={best}, pair={pair}")

    print(f"Exact finite conditional-saving checks: {check_finite_switch()}")
    for sizes, scale_squared in (((1, 1, 1, 2, 2), 1), ((3, 3, 3, 2, 2), 1),
                                 ((2, 2, 2, 4, 4), 4), ((4, 4, 4, 2, 2), 2)):
        length, charge, baseline, switched = check_switch_word(sizes, scale_squared)
        print(f"Literal switched word: sizes={sizes}, length={length}, charge={charge}, "
              f"baseline={baseline}, switched_tuples={switched}")

    # Exact probability lower bounds in the note give the displayed Delta.
    small_probability_factor = F(1, 2) * (F(1, 3) - F(1, 20))
    assert small_probability_factor == F(17, 120)
    delta_factor = F(37, 192) * small_probability_factor ** 3 * F(12, 5) ** 2 * 2
    assert delta_factor == F(181781, 28_800_000)
    e_upper = sum((F(1, factorial(j)) for j in range(6)), F(0)) + F(7, 4320)
    assert e_upper < F(87, 32)
    assert F(87, 32) ** 4 < 55
    assert F(22, 7) ** 2 < 10
    delta_lower = delta_factor / 550
    assert delta_lower > F(11, 1_000_000)
    beta = F(3) / F(2) ** F(4, 3)  # Diagnostic display only.
    print(f"Eight-block improvement: Delta > {delta_lower} > 11/1000000")
    print(f"Moving-center barrier diagnostic: {beta:.12f}")
    print("All mathematical assertions above used exact arithmetic.")


if __name__ == "__main__":
    main()
