#!/usr/bin/env python3
"""Finite audit for the slow Gate-C cover-down and phase packet note."""

from __future__ import annotations

from itertools import combinations
from math import ceil, comb, exp, floor, lgamma, log, sqrt
from random import Random


def type_period(b: int) -> list[str]:
    h = (b - 1) // 2
    out: list[str] = []
    for _ in range(h):
        out.extend(("B", "A"))
    out.append("B")
    assert len(out) == b
    return out


def phase_word(b: int, cyc_a: list[int] | None = None,
               cyc_b: list[int] | None = None, periods: int | None = None):
    if cyc_a is None:
        cyc_a = list(range(b))
    if cyc_b is None:
        cyc_b = list(range(b))
    if periods is None:
        periods = b
    pat = type_period(b)
    ia = ib = 0
    ans = []
    for t in range(periods * b):
        if pat[t % b] == "A":
            ans.append(("A", cyc_a[ia % b]))
            ia += 1
        else:
            ans.append(("B", cyc_b[ib % b]))
            ib += 1
    return ans


def window(word, t: int, ell: int):
    n = len(word)
    return frozenset(word[(t + i) % n] for i in range(ell))


def audit_packet_forward() -> int:
    states = 0
    for b in (3, 5, 7, 9, 11):
        word = phase_word(b, periods=b + 3)
        for q in range(b):
            start = q * b
            block = word[start:start + 2 * b]
            assert len(block) == 2 * b
            counts = {z: block.count(z) for z in set(block)}
            dup = [z for z, c in counts.items() if c == 2]
            assert len(dup) == 1
            u = dup[0]
            assert block[0] == block[-1] == u
            omega = {("A", i) for i in range(b)} | {("B", i) for i in range(b)}
            omitted = omega - set(block)
            assert len(omitted) == 1
            v = next(iter(omitted))
            x = block[1:b]
            y = block[b:2 * b - 1]
            assert len(set(x)) == len(set(y)) == b - 1
            assert set(x).isdisjoint(y)
            assert set(x) | set(y) == omega - {u, v}
            for i in range(b + 1):
                actual = frozenset(block[i:i + b])
                if i == 0:
                    expected = frozenset({u} | set(x))
                elif i == b:
                    expected = frozenset({u} | set(y))
                else:
                    expected = frozenset(set(x[i - 1:]) | set(y[:i]))
                assert actual == expected
            states += 1
    return states


def audit_packet_converse() -> int:
    rng = Random(20260822)
    trials = 0
    for b in (3, 5, 7, 9, 11):
        pat = type_period(b)
        for _ in range(100):
            omega = list(range(2 * b))
            rng.shuffle(omega)
            u, v = omega[:2]
            rest = omega[2:]
            rng.shuffle(rest)
            x, y = rest[:b - 1], rest[b - 1:]
            target = [u] + x + y + [u]

            b_events = [target[t] for t in range(2 * b) if pat[t % b] == "B"]
            a_events = [target[t] for t in range(2 * b) if pat[t % b] == "A"]
            assert b_events[0] == b_events[-1]
            assert len(set(b_events)) == b
            assert len(a_events) == b - 1 and len(set(a_events)) == b - 1

            cyc_b = b_events[:-1]
            cyc_a = a_events + [v]
            ia = ib = 0
            produced = []
            for t in range(2 * b):
                if pat[t % b] == "A":
                    produced.append(cyc_a[ia % b])
                    ia += 1
                else:
                    produced.append(cyc_b[ib % b])
                    ib += 1
            assert produced == target
            trials += 1
    return trials


def audit_equality_runs() -> int:
    checks = 0
    for b in (3, 5, 7, 9):
        word = phase_word(b)
        omega = sorted(set(word))
        mids = [window(word, t, b) for t in range(b * b)]
        for z, y in combinations(omega, 2):
            good = [((z in c) == (y in c)) for c in mids]
            for t in range(b * b):
                assert not all(good[(t + i) % (b * b)] for i in range(b + 1))
                checks += 1
    return checks


def equality_size(b: int, m: int) -> int:
    # [z^b] (1+z^2)^m (1+z)^(2b-2m)
    return sum(comb(m, j) * comb(2 * b - 2 * m, b - 2 * j)
               for j in range(m + 1) if 0 <= b - 2 * j <= 2 * b - 2 * m)


def audit_junta_enumerator() -> int:
    checks = 0
    for b in (5, 7, 9, 15, 25, 51):
        for m in range(0, min(4, (b - 1) // 2) + 1):
            direct = 0
            if b <= 9:
                omega = range(2 * b)
                pairs = [(2 * i, 2 * i + 1) for i in range(m)]
                for c in combinations(omega, b):
                    ss = set(c)
                    if all((z in ss) == (y in ss) for z, y in pairs):
                        direct += 1
                assert direct == equality_size(b, m)
            assert 0 < equality_size(b, m) <= comb(2 * b, b)
            checks += 1
    return checks


def audit_slow_schedule() -> tuple[int, float]:
    # Use a=sqrt(log b), a concrete sequence satisfying a->infinity and a=o(log b).
    checks = 0
    worst_margin = float("inf")
    c = 1.5
    theta = 0.2
    for b in (1001, 3001, 10001, 30001, 100001, 300001):
        if b % 2 == 0:
            b += 1
        a = sqrt(log(b))
        hband = ceil(sqrt(2 * b * log(2 * b)))
        g = b + hband
        ell = floor(c * b * log(b) / a)
        assert ell > g and ell <= b * b // 2
        rounds = ceil(a / -log(1 - theta))
        assert (1 - theta) ** rounds <= exp(-a)
        seam_ratio = g / ell
        assert seam_ratio <= 2.0 * a / (c * log(b))

        # Exact logarithmic expectation at the terminal independent density.
        log_support = log(b) + lgamma(2 * b + 1) - ell * a
        normalized = log_support / (b * log(b))
        # The finite values approach 2-c from above or below; retain a broad exact sanity margin.
        assert normalized > (2 - c) - 0.12
        worst_margin = min(worst_margin, normalized - (2 - c))
        checks += 1
    return checks, worst_margin


def main() -> None:
    packet_states = audit_packet_forward()
    converse_trials = audit_packet_converse()
    equality_checks = audit_equality_runs()
    junta_checks = audit_junta_enumerator()
    schedule_checks, margin = audit_slow_schedule()
    print(
        "GATE_C_SLOW_COVERDOWN_PACKET_PASS",
        f"packet_states={packet_states}",
        f"converse_trials={converse_trials}",
        f"equality_run_checks={equality_checks}",
        f"junta_checks={junta_checks}",
        f"schedule_checks={schedule_checks}",
        f"support_margin={margin:.6f}",
    )


if __name__ == "__main__":
    main()
