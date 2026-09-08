#!/usr/bin/env python3
"""Exact and asymptotic audit for the literal common-order b^(1/4) barrier."""

from functools import lru_cache
from math import comb, erfc, exp, pi, sqrt


@lru_cache(maxsize=None)
def binomial_row(b: int) -> tuple[int, ...]:
    row = [1]
    for j in range(b):
        row.append(row[-1] * (b - j) // (j + 1))
    return tuple(row)


def direct_loss(b: int, q: int) -> int:
    row = binomial_row(b)
    return sum(
        row[s] * row[s - q] - min(row[s], row[s - q]) ** 2
        for s in range(q, b + 1)
    )


def identity_loss(b: int, q: int) -> int:
    row = binomial_row(b)
    m = (b - q) // 2
    if (b - q) % 2:
        a = 2 * sum(row[j] ** 2 for j in range(m + 1))
    else:
        a = 2 * sum(row[j] ** 2 for j in range(m)) + row[m] ** 2
    return comb(2 * b, b + q) - a


def audit_exact() -> None:
    for b in range(3, 62):
        for q in range(1, b):
            lhs = direct_loss(b, q)
            rhs = identity_loss(b, q)
            assert lhs == rhs, (b, q, lhs, rhs)


def audit_one_offset() -> None:
    c = 1.0
    target = exp(-c * c) - erfc(c)
    reports = []
    for b in (101, 503, 1009, 5003, 10007):
        q = round(c * sqrt(b))
        ratio = identity_loss(b, q) / comb(2 * b, b)
        reports.append((b, q, ratio, target, abs(ratio - target)))
    assert reports[-1][4] < 0.006, reports[-1]
    print("one_offset", reports)


def audit_small_q_expansion() -> None:
    reports = []
    for b in (1009, 5003, 10007):
        q = max(3, round(b ** 0.22))
        actual = identity_loss(b, q) / comb(2 * b, b)
        leading = 2 * q / sqrt(pi * b)
        reports.append((b, q, actual, leading, actual / leading))
    assert abs(reports[-1][-1] - 1.0) < 0.12, reports[-1]
    print("small_q", reports)


def audit_pointwise_cardinality() -> None:
    # Simulate arbitrary bank sizes and overlaps.  The inequality is purely
    # K <= min(f_s,f_t), so integer-scaled C-values suffice.
    for b in range(5, 31):
        row = binomial_row(b)
        for q in range(1, b):
            for s in range(q, b + 1):
                x, y = row[s], row[s - q]
                # Test the extremal overlap and several smaller overlaps after
                # clearing the harmless common b factors.
                for k in {0, min(x, y) // 2, min(x, y)}:
                    lhs_num = x * y * x * y - x * y * k * k
                    rhs_num = x * y * (x * y - min(x, y) ** 2)
                    assert lhs_num >= rhs_num


if __name__ == "__main__":
    audit_exact()
    audit_pointwise_cardinality()
    audit_one_offset()
    audit_small_q_expansion()
    print("PASS")
