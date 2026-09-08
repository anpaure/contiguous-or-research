#!/usr/bin/env python3
"""Independent hostile audit of the highest-valley four-packet theorem.

Run this script on H100, not on the local Mac.  It reconstructs MSW flip
words from the g/h dynamics, rather than importing the theorem's verifier.
"""

from __future__ import annotations

import argparse
import os
from collections import Counter


def dyck_words(m: int):
    words = []

    def visit(prefix: tuple[int, ...], up: int, down: int) -> None:
        if len(prefix) == 2 * m:
            words.append(prefix)
            return
        if up < m:
            visit(prefix + (1,), up + 1, down)
        if down < up:
            visit(prefix + (0,), up, down + 1)

    visit((), 0, 0)
    return words


def msw_flip_word(root: tuple[int, ...]) -> tuple[int, ...]:
    """Reconstruct rho by the defining g/h orbit."""
    m = len(root) // 2
    state = list(root)
    rho = []
    for _ in range(m):
        before = []
        height = 0
        down_zero = 0
        for bit in state:
            before.append(height)
            if bit == 0 and height == 0:
                down_zero += 1
            height += 1 if bit else -1
        seen = 0
        for index, bit in enumerate(state):
            if bit == 0 and before[index] in (0, 1):
                seen += 1
                if seen == down_zero + 1:
                    state[index] = 1
                    rho.append(index)
                    break
        else:
            raise AssertionError("g pivot absent")

        before = []
        height = 0
        up_one = 0
        for bit in state:
            before.append(height)
            if bit == 1 and height == 1:
                up_one += 1
            height += 1 if bit else -1
        seen = 0
        for index, bit in enumerate(state):
            if bit == 1 and before[index] in (0, 1):
                seen += 1
                if seen == up_one:
                    state[index] = 0
                    rho.append(index)
                    break
        else:
            raise AssertionError("h pivot absent")
    rho.append(2 * m)
    assert sorted(rho) == list(range(2 * m + 1))
    return tuple(rho)


def canonical_permutations(L: int, Q: int, O: int):
    A = 2 * L + 2
    B = 2 * Q + 2
    n = A + B + 2 * O + 1
    fixed = tuple(range(A + B, n))
    return {
        "01": tuple(range(A, A + B - 1))
        + (0, A + B - 1)
        + tuple(range(1, A))
        + fixed,
        "001": tuple(range(A, A + B - 1))
        + tuple(range(1, A - 2))
        + (0, A - 2, A + B - 1, A - 1)
        + fixed,
        "011": (A, 0, A + 1, A + B - 1)
        + tuple(range(A + 2, A + B - 1))
        + tuple(range(1, A))
        + fixed,
        "0011": (A,)
        + tuple(range(1, A - 2))
        + (0, A - 2, A + 1, A + B - 1)
        + tuple(range(A + 2, A + B - 1))
        + (A - 1,)
        + fixed,
    }


def packet_specs(L: int, Q: int, valley: int):
    ans = {"01": (valley, valley + 1)}
    if L > 0:
        ans["001"] = (valley - 1, valley + 1)
    if Q > 0:
        ans["011"] = (valley, valley + 2)
    if L > 0 and Q > 0:
        ans["0011"] = (valley - 1, valley + 2)
    return ans


def transpose(word: tuple[int, ...], left: int, right: int):
    result = list(word)
    assert result[left] == 0 and result[right] == 1
    result[left], result[right] = result[right], result[left]
    return tuple(result)


def old_position_permutation(old, new):
    old_rho = msw_flip_word(old)
    new_rho = msw_flip_word(new)
    position = {label: index for index, label in enumerate(old_rho)}
    return tuple(position[label] for label in new_rho)


def dihedral_conjugacies(canonical, actual):
    n = len(canonical)
    ans = []
    for sign in (1, -1):
        for shift in range(n):
            if all(
                actual[(sign * j + shift) % n]
                == (sign * canonical[j] + shift) % n
                for j in range(n)
            ):
                ans.append((sign, shift))
    return ans


def tight_map(pi):
    n = len(pi)
    inverse_two = (n + 1) // 2
    return tuple((pi[(2 * j) % n] * inverse_two) % n for j in range(n))


def changed_tight_positions(pi):
    n = len(pi)
    inverse_two = (n + 1) // 2
    return {
        (z * inverse_two) % n
        for z, value in enumerate(pi)
        if z != value
    }


def bad_positions(pi, d: int):
    n = len(pi)
    m = (n - 1) // 2
    s = m + 1 - d
    changed = changed_tight_positions(pi)
    return changed | {(x - (s - 1)) % n for x in changed}


def cyclic_gap_data(values, n: int):
    ordered = sorted(values)
    return [
        ((ordered[(i + 1) % len(ordered)] - ordered[i]) % n,
         ordered[i], ordered[(i + 1) % len(ordered)])
        for i in range(len(ordered))
    ]


def consecutive(values, left: int, right: int, n: int) -> bool:
    ordered = sorted(values)
    return ordered[(ordered.index(left) + 1) % len(ordered)] == right % n


def mountain(size: int):
    return (1,) * size + (0,) * size


def highest_valleys(word):
    height = 0
    values = []
    for index in range(len(word) - 1):
        height += 1 if word[index] else -1
        if word[index:index + 2] == (0, 1):
            values.append((height + 1, index))
    if not values:
        return []
    maximum = max(height for height, _ in values)
    return [index for height, index in values if height == maximum]


def valley_parameters(word, valley: int):
    left_zeros = 0
    index = valley
    while index >= 0 and word[index] == 0:
        left_zeros += 1
        index -= 1
    right_ones = 0
    index = valley + 1
    while index < len(word) and word[index] == 1:
        right_ones += 1
        index += 1
    m = len(word) // 2
    L = left_zeros - 1
    Q = right_ones - 1
    O = m - 2 - L - Q
    return L, Q, O


def audit_canonical_formulas(max_parameter: int):
    checks = 0
    for L in range(max_parameter + 1):
        for Q in range(max_parameter + 1):
            for O in range(max_parameter + 1):
                old = mountain(L + 1) + mountain(Q + 1) + mountain(O)
                valley = 2 * L + 1
                formulas = canonical_permutations(L, Q, O)
                for name, (left, right) in packet_specs(L, Q, valley).items():
                    actual = old_position_permutation(
                        old, transpose(old, left, right)
                    )
                    assert actual == formulas[name], (L, Q, O, name)
                    assert sorted(actual) == list(range(len(actual)))
                    checks += 1
    return checks


def audit_context(max_m: int):
    checks = 0
    orientations = Counter()
    for m in range(2, max_m + 1):
        words = dyck_words(m)
        for word in words:
            for valley in highest_valleys(word):
                L, Q, O = valley_parameters(word, valley)
                formulas = canonical_permutations(L, Q, O)
                for name, (left, right) in packet_specs(L, Q, valley).items():
                    actual = old_position_permutation(
                        word, transpose(word, left, right)
                    )
                    conjugacies = dihedral_conjugacies(formulas[name], actual)
                    assert conjugacies, (m, word, valley, L, Q, O, name)
                    orientations[(name, conjugacies[0][0])] += 1
                    checks += 1
    return checks, orientations


def audit_residue(max_parameter: int):
    row_checks = 0
    exceptions = []
    for d in range(1, max_parameter + 1):
        for L in range(max_parameter + 1):
            for Q in range(max_parameter + 1):
                for O in range(max_parameter + 1):
                    m = L + Q + O + 2
                    if d > m:
                        continue
                    formulas = canonical_permutations(L, Q, O)
                    if L == Q == 0 and O >= 2 * d:
                        gaps = cyclic_gap_data(bad_positions(formulas["01"], d), 2*m+1)
                        assert max(gaps)[0] >= d + 1
                        row_checks += 1
                    if L > 0 and Q == 0 and L + O >= 2 * d:
                        gaps = cyclic_gap_data(bad_positions(formulas["001"], d), 2*m+1)
                        assert max(gaps)[0] >= d + 1
                        row_checks += 1
                    if L == 0 and Q > 0 and Q + O >= 2 * d:
                        gaps = cyclic_gap_data(bad_positions(formulas["011"], d), 2*m+1)
                        assert max(gaps)[0] >= d + 1
                        row_checks += 1
                    if L > 0 and Q > 0 and L + Q + O >= 3 * d - 1:
                        gaps = cyclic_gap_data(bad_positions(formulas["0011"], d), 2*m+1)
                        if max(gaps)[0] < d + 1:
                            exceptions.append((d, L, Q, O))
                        row_checks += 1
    assert all((L, Q, O) == (d, d, d - 1) for d, L, Q, O in exceptions)
    assert len(exceptions) == max_parameter
    return row_checks, exceptions


def audit_ordering(max_parameter: int):
    states = 0
    for d in range(1, max_parameter + 1):
        for L in range(1, max_parameter + 1):
            for Q in range(1, max_parameter + 1):
                for O in range(max_parameter + 1):
                    T = L + Q + O
                    if T < 3 * d - 1:
                        continue
                    m = T + 2
                    n = 2 * m + 1
                    pi = canonical_permutations(L, Q, O)["0011"]
                    values = bad_positions(pi, d)
                    maximum_gap = max(cyclic_gap_data(values, n))[0]
                    no_gap = maximum_gap <= d

                    if Q + O <= d - 2:
                        assert consecutive(values, d - Q - O - 1, L, n)

                    if Q + O >= d - 1 and no_gap:
                        assert consecutive(values, 0, L, n)
                        assert L <= d and Q <= d and O >= d - 1
                        middle_left = L + Q + d + 2
                        middle_right = T + L + 3
                        assert consecutive(values, middle_left, middle_right, n)
                        last = T + L + d + 4
                        assert last < n
                        assert consecutive(values, last, 0, n)
                        assert L + O <= 2 * d - 1
                        assert Q + O <= 2 * d - 1
                        assert T + O <= 4 * d - 2
                    states += 1
    return states


def audit_exceptional_cuts(max_d: int):
    checks = 0
    for d in range(1, max_d + 1):
        L = Q = d
        O = d - 1
        formulas = canonical_permutations(L, Q, O)
        n = 6 * d + 3
        s = 2 * d + 2
        for name, (a, b) in {
            "001": (d + 1, 4 * d + 2),
            "011": (d + 2, 4 * d + 4),
        }.items():
            qmap = tight_map(formulas[name])
            for j in range(d):
                assert qmap[(b + s - 1 + j) % n] == a + j
                assert qmap[(b + j) % n] == a + s - 1 + j
                checks += 1
    return checks


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--formula-max", type=int, default=10)
    parser.add_argument("--context-max-m", type=int, default=10)
    parser.add_argument("--residue-max", type=int, default=30)
    parser.add_argument("--ordering-max", type=int, default=60)
    parser.add_argument("--exception-max-d", type=int, default=100)
    args = parser.parse_args()

    print(f"host={os.uname().nodename}")
    formula_checks = audit_canonical_formulas(args.formula_max)
    print(f"canonical_formula_checks={formula_checks}")
    context_checks, orientations = audit_context(args.context_max_m)
    print(f"context_packet_checks={context_checks}")
    print("context_orientation_counts=" + repr(sorted(orientations.items())))
    residue_checks, exceptions = audit_residue(args.residue_max)
    print(f"residue_row_checks={residue_checks}")
    print(f"direct_0011_exceptions={exceptions}")
    ordering_states = audit_ordering(args.ordering_max)
    print(f"ordering_states={ordering_states}")
    exceptional_checks = audit_exceptional_cuts(args.exception_max_d)
    print(f"exceptional_ordered_pair_checks={exceptional_checks}")
    print("PASS")


if __name__ == "__main__":
    main()
