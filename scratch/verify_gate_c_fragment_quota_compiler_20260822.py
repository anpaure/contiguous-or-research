#!/usr/bin/env python3
"""Independent finite/algebraic checks for the Gate-C fragment compiler.

The verifier checks a complete phase-refined labelled family at b=3 (the
smallest inexpensive exhaustive instance), all exact degree and pair formulas,
all fragment starts through L=floor(b^2/2), simultaneous rank-token marginals,
the quota inequality, the serialization ledger, and the reopened asymptotic
scale numerically.  The theorem itself is stated for b>=5; the same finite
identities have no exceptional behavior at b=3.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import combinations, permutations
from math import ceil, comb, factorial, lgamma, log, sqrt


def cyclic_orders(points: tuple[int, ...]):
    """All directed cyclic orders modulo rotation, rooted at the minimum."""
    root = min(points)
    rest = tuple(x for x in points if x != root)
    for tail in permutations(rest):
        yield (root,) + tail


def rooted_phase_word(
    alpha: tuple[int, ...],
    beta: tuple[int, ...],
    root_a: int,
    root_b: int,
) -> tuple[int, ...]:
    """Word from an arbitrary pair of stream roots."""
    b = len(alpha)
    ia, ib = root_a % b, root_b % b
    out: list[int] = []
    for t in range(b * b):
        if t % b % 2 == 0:  # B,A,...,B
            out.append(beta[ib])
            ib = (ib + 1) % b
        else:
            out.append(alpha[ia])
            ia = (ia + 1) % b
    return tuple(out)


def phase_word(
    alpha: tuple[int, ...], beta: tuple[int, ...], rho: int
) -> tuple[int, ...]:
    """The unique (r_A,r_B)=(rho,0) representative of a phase coset."""
    return rooted_phase_word(alpha, beta, rho, 0)


def window_mask(word: tuple[int, ...], start: int, length: int) -> int:
    m = len(word)
    mask = 0
    for j in range(length):
        mask |= 1 << word[(start + j) % m]
    return mask


def check_phase_quotient_and_cyclic_wrap() -> int:
    checks = 0
    for b in (3, 5, 7):
        h = (b - 1) // 2
        alpha = tuple(range(b))
        beta = tuple(range(b, 2 * b))

        orbits = []
        for rho in range(b):
            orbit = {
                ((rho + t * h) % b, (t * (h + 1)) % b)
                for t in range(b)
            }
            assert len(orbit) == b
            assert sum(root_b == 0 for _, root_b in orbit) == 1
            orbits.append(orbit)
        assert len(set().union(*orbits)) == b * b
        assert all(
            orbits[i].isdisjoint(orbits[j])
            for i in range(b)
            for j in range(i)
        )

        for root_a in range(b):
            for root_b in range(b):
                word = rooted_phase_word(alpha, beta, root_a, root_b)
                advanced = rooted_phase_word(
                    alpha, beta, root_a + h, root_b + h + 1
                )
                assert advanced == word[b:] + word[:b]
                checks += 1

        n = b * b
        for length in range(1, n):
            for q in range(1, n):
                brute = sum(
                    0 in {(start + j) % n for j in range(length)}
                    and q in {(start + j) % n for j in range(length)}
                    for start in range(n)
                )
                formula = max(0, length - q) + max(0, length - (n - q))
                assert brute == formula
                assert brute <= length - 1
                checks += 1
    return checks


def check_single_atom_distance_profiles() -> int:
    checks = 0
    for b in (5, 7, 9, 11):
        alpha = tuple(range(b))
        beta = tuple(range(b, 2 * b))
        word = phase_word(alpha, beta, 0)
        central = [window_mask(word, t, b) for t in range(b * b)]
        assert len(set(central)) == b * b
        for x in central:
            profile = Counter(b - (x & y).bit_count() for y in central if y != x)
            for d in range(1, b + 1):
                expected = 0 if d == b else 4 * min(d, b - d)
                assert profile[d] == expected
                checks += 1
    return checks


def exhaustive_atom_and_fragment_check() -> tuple[int, int, int]:
    b = 3
    omega = tuple(range(2 * b))
    w_middle = comb(2 * b, b)
    d_hat = b * factorial(b) ** 2
    n_hat = b * w_middle * factorial(b - 1) ** 2

    atoms: list[tuple[tuple[int, ...], tuple[int, ...]]] = []
    full_degree: Counter[int] = Counter()
    full_pairs: Counter[tuple[int, int]] = Counter()

    for aset in combinations(omega, b):
        a_set = set(aset)
        bset = tuple(x for x in omega if x not in a_set)
        for alpha in cyclic_orders(tuple(aset)):
            for beta in cyclic_orders(bset):
                for rho in range(b):
                    word = phase_word(alpha, beta, rho)
                    central = tuple(window_mask(word, t, b) for t in range(b * b))
                    assert len(set(central)) == b * b
                    assert all(x.bit_count() == b for x in central)

                    # Every cyclic recurrence gap has the asserted lower bound.
                    for symbol in omega:
                        positions = [i for i, x in enumerate(word) if x == symbol]
                        gaps = [
                            (
                                positions[(i + 1) % len(positions)]
                                - positions[i]
                                - 1
                            )
                            % (b * b)
                            + 1
                            for i in range(len(positions))
                        ]
                        assert min(gaps) >= 2 * b - 2

                    atoms.append((word, central))
                    full_degree.update(central)
                    for x, y in combinations(central, 2):
                        full_pairs[tuple(sorted((x, y)))] += 1

    assert len(atoms) == n_hat
    middle_vertices = [m for m in range(1 << (2 * b)) if m.bit_count() == b]
    assert len(middle_vertices) == w_middle
    assert set(full_degree.values()) == {d_hat}

    for x, y in combinations(middle_vertices, 2):
        d = b - (x & y).bit_count()
        n_d = 0 if d == b else 4 * min(d, b - d)
        n_d_shell = comb(b, d) ** 2
        expected = Fraction(d_hat * n_d, n_d_shell)
        assert expected.denominator == 1
        assert full_pairs[(x, y)] == expected.numerator

    fragment_count = 0
    marginal_checks = 0
    for length in range(1, b * b // 2 + 1):
        frag_degree: Counter[int] = Counter()
        frag_pairs: Counter[tuple[int, int]] = Counter()
        token_load = {s: Counter() for s in range(1, 2 * b - 1)}

        for word, central in atoms:
            for start in range(b * b):
                deck = tuple(central[(start + j) % (b * b)] for j in range(length))
                assert len(set(deck)) == length
                g_test = 2 * b - 2
                linear = tuple(
                    word[(start + q) % (b * b)]
                    for q in range(length + g_test - 1)
                )
                frag_degree.update(deck)
                for x, y in combinations(deck, 2):
                    frag_pairs[tuple(sorted((x, y)))] += 1
                for s in token_load:
                    for j in range(length):
                        target = window_mask(word, start + j, s)
                        assert target.bit_count() == s
                        linear_target = sum(1 << x for x in set(linear[j : j + s]))
                        assert target == linear_target
                        token_load[s][target] += 1
                fragment_count += 1

        d_l = length * d_hat
        assert set(frag_degree.values()) == {d_l}
        assert sum(frag_degree.values()) == w_middle * d_l
        assert len(atoms) * b * b == w_middle * d_hat
        max_pair = max(frag_pairs.values(), default=0)
        assert Fraction(max_pair, d_l) <= Fraction(4, b * b)
        for x, y in combinations(middle_vertices, 2):
            d = b - (x & y).bit_count()
            n_d = 0 if d == b else 4 * min(d, b - d)
            lam = Fraction(d_hat * n_d, comb(b, d) ** 2)
            assert lam.denominator == 1
            assert frag_pairs[(x, y)] <= (length - 1) * lam.numerator

        for s, loads in token_load.items():
            expected = Fraction(d_l * w_middle, comb(2 * b, s))
            assert expected.denominator == 1
            targets = [m for m in range(1 << (2 * b)) if m.bit_count() == s]
            assert {loads[m] for m in targets} == {expected.numerator}
            assert sum(loads.values()) == w_middle * d_hat * length
            marginal_checks += len(targets)

    return len(atoms), fragment_count, marginal_checks


def compositions(total: int, parts: int):
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in compositions(total - first, parts - 1):
            yield (first,) + tail


def quota_and_length_check() -> int:
    checks = 0
    for n_targets in range(1, 7):
        for total in range(n_targets, n_targets + 6):
            low, rem = divmod(total, n_targets)
            quota = (low + 1,) * rem + (low,) * (n_targets - rem)
            assert min(quota) >= 1 and sum(quota) == total
            for load in compositions(total, n_targets):
                holes = sum(x == 0 for x in load)
                overflow = sum(max(0, a - q) for a, q in zip(load, quota))
                deficit = sum(max(0, q - a) for a, q in zip(load, quota))
                assert overflow == deficit
                assert holes <= overflow
                checks += 1

    for w_middle, length, g in [(1000, 73, 20), (1001, 100, 77), (10_000, 333, 91)]:
        t = ceil(w_middle / length)
        actual = t * (length + g - 1)
        bound = w_middle + length + (w_middle / length + 1) * (g - 1)
        assert actual < bound + 1e-12
        checks += 1
    return checks


def scale_check() -> tuple[int, int]:
    checks = 0
    positive_support = 0
    for c in (0.5, 1.0, 1.5):
        previous_g_ratio = None
        previous_pair = None
        for b in (1001, 10_001, 100_001, 1_000_001):
            h_band = ceil(sqrt(2 * b * log(2 * b)))
            g = b + h_band + 2
            length = ceil(c * b * log(b) / log(log(b)))
            assert g <= length <= b * b / 2

            g_ratio = g / length
            pair_parameter = 4 * length / (b * b)
            assert g_ratio < 1
            assert pair_parameter < 1
            if previous_g_ratio is not None:
                assert g_ratio < previous_g_ratio
                assert pair_parameter < previous_pair
            previous_g_ratio = g_ratio
            previous_pair = pair_parameter

            # W * Dhat = b * (2b)! exactly.
            log_support = log(b) + lgamma(2 * b + 1) - length * log(log(b))
            normalized = log_support / (b * log(b))
            assert log_support > 0
            assert abs(normalized - (2 - c)) < 0.25
            positive_support += 1
            checks += 1

    # At c=2 the negative linear Stirling correction forces decay; above
    # two the negative b log b term does so.
    b = 1_000_001
    for c in (2.0, 2.5):
        length = ceil(c * b * log(b) / log(log(b)))
        log_support = log(b) + lgamma(2 * b + 1) - length * log(log(b))
        assert log_support < 0
        checks += 1

    for b in range(3, 16, 2):
        w_middle = comb(2 * b, b)
        d_hat = b * factorial(b) ** 2
        assert w_middle * d_hat == b * factorial(2 * b)
        checks += 1

    # A finite check of the outside-band count used by the compiler.
    for b in (101, 501, 1001):
        h_band = ceil(sqrt(2 * b * log(2 * b)))
        tail = sum(comb(2 * b, s) for s in range(1, 2 * b + 1) if abs(s - b) > h_band)
        w_middle = comb(2 * b, b)
        asserted_bound = 2 * (2 * b + 1) / ((2 * b) ** 2)
        assert tail / w_middle <= asserted_bound
        checks += 1

    return checks, positive_support


def main() -> None:
    phase_wrap_checks = check_phase_quotient_and_cyclic_wrap()
    profile_checks = check_single_atom_distance_profiles()
    atoms, fragments, marginals = exhaustive_atom_and_fragment_check()
    quota_checks = quota_and_length_check()
    scale_checks, support_checks = scale_check()
    print(
        "GATE_C_FRAGMENT_QUOTA_COMPILER_PASS "
        f"phase_wrap={phase_wrap_checks} "
        f"profiles={profile_checks} "
        f"atoms={atoms} fragments={fragments} marginals={marginals} "
        f"quota={quota_checks} scale={scale_checks} support={support_checks}"
    )


if __name__ == "__main__":
    main()
