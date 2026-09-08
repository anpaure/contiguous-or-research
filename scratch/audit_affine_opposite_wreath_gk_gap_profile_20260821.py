#!/usr/bin/env python3
"""H100 audit for the affine-opposite wreath gap-profile reduction."""

from __future__ import annotations

from math import gcd


def translate(mask: int, t: int, b: int) -> int:
    ans = 0
    for q in range(b):
        if (mask >> q) & 1:
            ans |= 1 << ((q + t) % b)
    return ans


def window_ending(order: list[int], end: int, length: int) -> int:
    b = len(order)
    ans = 0
    for z in range(length):
        ans |= 1 << order[(end - length + 1 + z) % b]
    return ans


def top_excess(xmask: int, ymask: int, b: int) -> int:
    h = 0
    minimum = 0
    for q in range(b):
        h += 1 if (xmask >> q) & 1 else -1
        minimum = min(minimum, h)
        h += 1 if (ymask >> q) & 1 else -1
        minimum = min(minimum, h)
    assert h == 0
    return -minimum


def minimum_signed_interval_weights(xmask: int, b: int) -> list[int]:
    signs = [1 if (xmask >> q) & 1 else -1 for q in range(b)]
    prefix = [0]
    for value in signs + signs:
        prefix.append(prefix[-1] + value)
    return [
        min(prefix[s + t] - prefix[s] for s in range(b))
        for t in range(b + 1)
    ]


def gap_thresholds(xmask: int, b: int) -> list[int]:
    points = [q for q in range(b) if (xmask >> q) & 1]
    rr = len(points)
    gaps = [(points[(i + 1) % rr] - points[i]) % b for i in range(rr)]
    assert all(g > 0 for g in gaps) and sum(gaps) == b
    prefix = [0]
    for value in gaps + gaps:
        prefix.append(prefix[-1] + value)
    return [
        max(prefix[i + m] - prefix[i] for i in range(rr))
        for m in range(1, rr + 1)
    ]


def audit_one(b: int, a: int, literal: bool) -> None:
    r = (b - 1) // 2
    full = (1 << b) - 1
    xbase = sum(1 << ((q * a) % b) for q in range(r))

    ell = minimum_signed_interval_weights(xbase, b)
    assert all(ell[t + 1] - ell[t] in (-1, 1) for t in range(b))
    by_derivative = [ell[t + 1] - ell[t] == -1 for t in range(b)]

    thresholds = gap_thresholds(xbase, b)
    assert all(thresholds[i] < thresholds[i + 1] for i in range(r - 1))
    assert thresholds[-1] == b
    b_shifts = {(t - 1) % b for t in thresholds}
    by_gaps = [t not in b_shifts for t in range(b)]
    assert by_derivative == by_gaps
    assert sum(by_gaps) == r + 1

    # Direct relative-translation orientations are inexpensive enough for
    # the full finite diagnostic range.
    direct = []
    for t in range(b):
        zmask = translate(xbase, t, b)
        ymask = full ^ zmask
        direct.append(bool(top_excess(xbase, ymask, b) & 1))
    assert direct == by_gaps

    phase_pred = [by_gaps[(-a * (p + 1)) % b] for p in range(b)]
    assert sum(phase_pred) == r + 1

    if literal:
        alpha = [(a * i) % b for i in range(b)]
        beta = [(-a * i) % b for i in range(b)]
        xs = [window_ending(alpha, i, r) for i in range(b)]
        ys = [window_ending(beta, j, r + 1) for j in range(b)]
        zs = [full ^ y for y in ys]
        abase = sum(1 << ((a * q) % b) for q in range(-r + 1, 1))
        assert all(xs[i] == translate(abase, a * i, b) for i in range(b))
        for p in range(b):
            parities = []
            for i in range(b):
                j = (p - i) % b
                assert zs[j] == translate(xs[i], -a * (p + 1), b)
                parities.append(bool(top_excess(xs[i], ys[j], b) & 1))
            assert len(set(parities)) == 1
            assert parities[0] == phase_pred[p]

    # Diagnostic only: no four consecutive alternating phase colors.
    assert not any(
        all(phase_pred[(p + q) % b] != phase_pred[(p + q + 1) % b]
            for q in range(3))
        for p in range(b)
    )


def main() -> None:
    literal_cases = 0
    profile_cases = 0
    for b in range(5, 102, 2):
        for a in range(1, b):
            if gcd(a, b) != 1:
                continue
            literal = b <= 31
            audit_one(b, a, literal)
            profile_cases += 1
            literal_cases += int(literal)
    print(
        "PASS affine-opposite gap profile: "
        f"{profile_cases} profiles through odd b=101; "
        f"{literal_cases} literal wreath instances through b=31"
    )


if __name__ == "__main__":
    main()
