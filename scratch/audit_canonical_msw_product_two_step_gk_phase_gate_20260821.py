#!/usr/bin/env python3
"""Exact audit for the canonical-MSW product two-step/phase gate.

Run on ssh h100.  The theorem-level checks are:

* q=(pi(x),infinity) is the odd-cycle hole word, while its step-two
  decimation is a contiguous-window order;
* the decimated orders form the exact central wreath factor;
* the product two-step support is the Cartesian product of the exact
  (r+1)-deck on one side and the defective (r+2)-deck on the other;
* the marked-gap lower bound is respected by the literal canonical deck.

The final phase census is deliberately finite evidence only.  It checks the
corrected order convention and both choices of relative stream direction.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from math import comb


def dyck_words(r: int):
    out = []

    def rec(word, up, down):
        if up == r and down == r:
            out.append(word)
            return
        if up < r:
            rec(word + (1,), up + 1, down)
        if down < up:
            rec(word + (0,), up, down + 1)

    rec((), 0, 0)
    return out


def reverse_complement(word):
    return tuple(1 - bit for bit in reversed(word))


@lru_cache(None)
def flip_permutation(word):
    """The one-based MSW recursion for pi(x)."""
    if not word:
        return ()
    height = 0
    first_return = None
    for pos, bit in enumerate(word):
        height += 1 if bit else -1
        if height == 0:
            first_return = pos
            break
    assert first_return is not None
    u = word[1:first_return]
    v = word[first_return + 1 :]
    a = len(u) + 2
    return (
        (a,)
        + tuple(a - z for z in flip_permutation(reverse_complement(u)))
        + (1,)
        + tuple(a + z for z in flip_permutation(v))
    )


def hole_word(word):
    """Zero-based q(x)=(pi(x),infinity)."""
    return tuple(z - 1 for z in flip_permutation(word)) + (len(word),)


def window_order(word):
    """A contiguous-window order obtained by step-two decimation of q."""
    q = hole_word(word)
    return tuple(q[(2 * i) % len(q)] for i in range(len(q)))


def windows(order, size):
    b = len(order)
    return tuple(
        frozenset(order[(start + j) % b] for j in range(size))
        for start in range(b)
    )


def central_factor(r: int):
    return tuple(window_order(word) for word in dyck_words(r))


def support(factor, size):
    return {target for order in factor for target in windows(order, size)}


def marked_gap_K(r: int):
    if r < 3:
        return 0
    cat = comb(2 * (r - 2), r - 2) // (r - 1)
    return (2 * r - 3) * cat


def audit_factor_and_two_step(r: int):
    b = 2 * r + 1
    factor = central_factor(r)
    n = comb(b, r)
    assert len(factor) == n // b

    middle_occ = [target for order in factor for target in windows(order, r)]
    assert len(middle_occ) == n
    assert len(set(middle_occ)) == n

    next_occ = [target for order in factor for target in windows(order, r + 1)]
    assert len(next_occ) == n
    assert len(set(next_occ)) == n

    upper2_occ = [target for order in factor for target in windows(order, r + 2)]
    lower1_occ = [target for order in factor for target in windows(order, r - 1)]
    upper2_support = set(upper2_occ)
    lower1_support = set(lower1_occ)
    all_points = frozenset(range(b))
    assert {all_points - target for target in upper2_support} == lower1_support

    n2 = comb(b, r + 2)
    h1 = comb(b, r - 1) - len(lower1_support)
    assert len(upper2_support) == n2 - h1
    marked_bound = max(Fraction(0), Fraction(marked_gap_K(r)) - Fraction(2 * n, r + 2))
    assert Fraction(h1) >= marked_bound

    # The product occurrence deck after one step of each stream is exactly
    # the Cartesian product.  Explicitly instantiate it in the small cases.
    product_support_formula = n * (n2 - h1)
    product_missing_formula = n * h1
    if r <= 5:
        left = set(next_occ)
        right = upper2_support
        products = {x | frozenset(b + y for y in z) for x in left for z in right}
        assert len(products) == product_support_formula
        all_profile = {
            frozenset(x) | frozenset(b + y for y in z)
            for x in combinations(range(b), r + 1)
            for z in combinations(range(b), r + 2)
        }
        assert len(all_profile) == n * n2
        assert len(all_profile - products) == product_missing_formula

    # q itself is the hole word, not generally a contiguous factor order.
    q_occ = [target for word in dyck_words(r) for target in windows(hole_word(word), r)]
    if r >= 3:
        assert len(set(q_occ)) < n

    return {
        "r": r,
        "b": b,
        "rows": len(factor),
        "middle": n,
        "h1": h1,
        "marked_gap_bound": str(marked_bound),
        "two_step_profile": n * n2,
        "two_step_missing": product_missing_formula,
        "missing_fraction": product_missing_formula / (n * n2),
        "q_distinct_if_misread_as_order": len(set(q_occ)),
    }


def separated_double_swap(order, start, r):
    changed = list(order)
    b = len(order)
    for pos in (start, (start + r) % b):
        nxt = (pos + 1) % b
        changed[pos], changed[nxt] = changed[nxt], changed[pos]
    return tuple(changed)


def audit_separated_swap_touch_bound(r: int):
    """One moved row changes 3 windows and at most 9 q=1 centers."""
    b = 2 * r + 1
    order = tuple(range(b))
    old = windows(order, r)
    for start in range(b):
        new = windows(separated_double_swap(order, start, r), r)
        changed_starts = {i for i in range(b) if old[i] != new[i]}
        assert len(changed_starts) == 3
        touched = changed_starts | {
            (i - r) % b for i in changed_starts
        } | {
            (i + r) % b for i in changed_starts
        }
        assert len(touched) <= 9
        for i in set(range(b)) - touched:
            assert old[i] == new[i]
            assert old[(i - r) % b] == new[(i - r) % b]
            assert old[(i + r) % b] == new[(i + r) % b]
            assert (
                old[(i - r) % b] & old[(i + r) % b]
                == new[(i - r) % b] & new[(i + r) % b]
            )
    return {"b": b, "changed_windows": 3, "q1_centers_per_row_at_most": 9}


def gk_orientation(x, z, b):
    """A-first parity for source (x, complement(z))."""
    d = 0
    minimum = 0
    before = []
    for q in range(b):
        before.append(d)
        d += int(q in x) - int(q in z)
        minimum = min(minimum, d)
    assert d == 0
    return int(
        any(before[q] == minimum and q not in x and q not in z for q in range(b))
    )


def phase_word(left_order, right_order, relative_sign):
    """Monochromatic phase word; sign +/-1 covers independent reversal."""
    b = len(left_order)
    r = (b - 1) // 2
    left = windows(left_order, r)
    right = windows(right_order, r)
    result = []
    for phase in range(b):
        colors = {
            gk_orientation(left[i], right[(phase - relative_sign * i) % b], b)
            for i in range(b)
        }
        result.append(next(iter(colors)) if len(colors) == 1 else None)
    return tuple(result)


def correct_count(word):
    b = len(word)
    r = (b - 1) // 2
    persistent = [int((r * x) % b < r) for x in range(b)]
    assert sum(
        persistent[p] == persistent[(p + 1) % b] for p in range(b)
    ) == 1
    return max(
        sum(
            word[p] is not None
            and word[p] == (persistent[(p + shift) % b] ^ flip)
            for p in range(b)
        )
        for shift in range(b)
        for flip in (0, 1)
    )


EXPECTED_PHASE_CENSUS = {
    5: (
        [(1, 3), (3, 1)],
        [(1, 3), (2, 1)],
    ),
    7: (
        [(0, 10), (1, 10), (2, 2), (3, 2), (4, 1)],
        [(0, 10), (1, 10), (2, 2), (3, 3)],
    ),
    9: (
        [(0, 115), (1, 59), (2, 14), (3, 7), (5, 1)],
        [(0, 115), (1, 59), (2, 20), (3, 2)],
    ),
    11: (
        [(0, 1240), (1, 409), (2, 60), (3, 42), (4, 9), (5, 4)],
        [(0, 1240), (1, 409), (2, 87), (3, 25), (4, 3)],
    ),
    13: (
        [(0, 13527), (1, 3051), (2, 511), (3, 248), (4, 59), (5, 26), (6, 2)],
        [(0, 13527), (1, 3051), (2, 711), (3, 127), (4, 8)],
    ),
}


def audit_phase_census(r: int):
    factor = central_factor(r)
    b = 2 * r + 1
    mono_hist = Counter()
    correct_hist = Counter()
    for left in factor:
        for right in factor:
            words = (
                phase_word(left, right, +1),
                phase_word(left, right, -1),
            )
            mono_hist[max(sum(color is not None for color in word) for word in words)] += 1
            correct_hist[max(correct_count(word) for word in words)] += 1
    got = (sorted(mono_hist.items()), sorted(correct_hist.items()))
    assert got == EXPECTED_PHASE_CENSUS[b], (b, got)
    return {
        "b": b,
        "row_pairs": len(factor) ** 2,
        "best_direction_mono_hist": got[0],
        "best_direction_correct_hist": got[1],
    }


def main():
    for r in range(1, 8):
        print("two_step", audit_factor_and_two_step(r))
    for r in range(2, 20):
        print("separated_swap", audit_separated_swap_touch_bound(r))
    for r in range(2, 7):
        print("phase_census", audit_phase_census(r))
    print("PASS audit_canonical_msw_product_two_step_gk_phase_gate_20260821")


if __name__ == "__main__":
    main()
