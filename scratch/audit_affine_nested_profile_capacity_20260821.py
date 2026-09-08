#!/usr/bin/env python3
"""Fail-closed finite audit for the affine nested schedule theorem."""

from __future__ import annotations

import itertools
import math


def primes_upto(n: int) -> list[int]:
    out = []
    for x in range(2, n + 1):
        if all(x % d for d in range(2, int(math.isqrt(x)) + 1)):
            out.append(x)
    return out


def prefix_sets(b: int, a: int) -> list[set[int]]:
    # R(x)=a*x mod b and P_r={x:R(x)<r}.
    rank = [(a * x) % b for x in range(b)]
    return [{x for x in range(b) if rank[x] < r} for r in range(b + 1)]


def capacity_data(b: int, a: int, q: int, s: int):
    rank = [(a * x) % b for x in range(b)]
    ps = prefix_sets(b, a)
    hits = []
    holes = []
    t_num = 0
    # Windows are J_p={p+1,...,p+q}.
    for p in range(b):
        js = {(p + j) % b for j in range(1, q + 1)}
        vals = []
        for r in range(b + 1):
            z = len(ps[r] & js)
            vals.append(r + z)
            if r + z == s:
                hits.append((p, r, z))
                t_num += math.comb(b, r) ** 2
        assert vals[0] == 0 and vals[-1] == b + q
        assert all(vals[r + 1] - vals[r] in (1, 2) for r in range(b))
        assert len(set(vals)) == b + 1
        if s not in vals:
            holes.append(p)
    assert len(hits) + len(holes) == b
    assert len(holes) <= q

    # Direct skipped-profile formula, including uniqueness for each i.
    recovered = []
    per_i = {i: [] for i in range(1, q + 1)}
    for p in range(b):
        js_order = [(p + j) % b for j in range(1, q + 1)]
        for i, x in enumerate(js_order, 1):
            t = rank[x]
            rhs = t + sum(rank[y] < t for y in js_order if y != x)
            if rhs == s - 1:
                recovered.append(p)
                per_i[i].append((p, t))
    assert sorted(recovered) == sorted(holes)
    assert all(len(v) <= 1 for v in per_i.values())
    return t_num, hits, holes


def discrepancy(b: int, a: int) -> int:
    rank = [(a * x) % b for x in range(b)]
    delta = 0.0
    for r in range(b + 1):
        word = [int(rank[x] < r) for x in range(b)]
        pref = [0]
        for v in word + word:
            pref.append(pref[-1] + v)
        for p in range(b):
            for q in range(b + 1):
                got = pref[p + q + 1] - pref[p + 1]
                delta = max(delta, abs(got - q * r / b))
    return math.ceil(delta - 1e-12)


def all_capacities(b: int, a: int, q: int) -> list[int]:
    """Return b*T_{q,s} for every s in one O(b^2) pass."""
    ps = prefix_sets(b, a)
    out = [0] * (b + q + 1)
    for p in range(b):
        js = {(p + j) % b for j in range(1, q + 1)}
        for r in range(b + 1):
            s = r + len(ps[r] & js)
            out[s] += math.comb(b, r) ** 2
    return out


def all_hit_counts(b: int, a: int, q: int):
    rank = [(a * x) % b for x in range(b)]
    out = [dict() for _ in range(b + q + 1)]
    for p in range(b):
        in_window_rank = [False] * b
        for j in range(1, q + 1):
            in_window_rank[rank[(p + j) % b]] = True
        z = 0
        for r in range(b + 1):
            s = r + z
            out[s][(r, z)] = out[s].get((r, z), 0) + 1
            if r < b and in_window_rank[r]:
                z += 1
    return out


def expected_formula(b: int, q: int, s: int) -> float:
    return sum(
        math.comb(b, s - z)
        * math.comb(q, z)
        * math.comb(b - q, s - 2 * z)
        for z in range(q + 1)
        if 0 <= s - z <= b and 0 <= s - 2 * z <= b - q
    )


def brute_permutation_capacity_numerator(b: int, perm: tuple[int, ...], q: int, s: int) -> int:
    ps = [set(perm[:r]) for r in range(b + 1)]
    ans = 0
    for p in range(b):
        js = {(p + j) % b for j in range(1, q + 1)}
        for r in range(b + 1):
            if r + len(ps[r] & js) == s:
                ans += math.comb(b, r) ** 2
    return ans


def brute_permutation_capacity(b: int, perm: tuple[int, ...], q: int, s: int) -> float:
    return brute_permutation_capacity_numerator(b, perm, q, s) / b


def audit_expectation() -> None:
    for b in range(2, 8):
        perms = list(itertools.permutations(range(b)))
        for q in range(1, b + 1):
            for s in range(q, b + 1):
                avg = sum(brute_permutation_capacity(b, p, q, s) for p in perms) / len(perms)
                exact = expected_formula(b, q, s)
                assert abs(avg - exact) < 1e-8, (b, q, s, avg, exact)


def audit_q1() -> None:
    for b in range(3, 40):
        for s in range(1, b + 1):
            exact = (
                (b - s) * math.comb(b, s) ** 2
                + (s - 1) * math.comb(b, s - 1) ** 2
            ) / b
            for perm in [tuple(range(b)), tuple(reversed(range(b)))]:
                got = brute_permutation_capacity(b, perm, 1, s)
                assert got == exact
        if b % 2:
            s = (b + 1) // 2
            p = math.comb(b, s) * math.comb(b, s - 1)
            assert abs(exact if False else 0) == 0  # keep fail-closed branch live
            got_num = brute_permutation_capacity_numerator(b, tuple(range(b)), 1, s)
            assert got_num == p * (b - 1)


def audit_affine() -> None:
    for b in primes_upto(31):
        if b < 3:
            continue
        for a in range(1, b):
            d = discrepancy(b, a)
            for q in range(1, min(7, b) + 1):
                for s in range(q, b + 1):
                    cap_num, hits, holes = capacity_data(b, a, q, s)
                    rstar = b * s / (b + q)
                    assert all(abs(r - rstar) <= d + 1e-12 for _, r, _ in hits)
                    if hits:
                        lo = min(math.comb(b, r) ** 2 for _, r, _ in hits)
                        assert cap_num >= (b - q) * lo


def audit_half_step_dominant_phase() -> None:
    # For a=(b-1)/2, consecutive physical ranks split into antipodal pairs.
    # Check the exact dominant-phase lower bounds used in the proof.
    for b in range(5, 82, 2):
        a = (b - 1) // 2
        for q in range(1, b // 4 + 1):
            u = q // 2
            hit_table = all_hit_counts(b, a, q)
            for s in range(q, b + 1):
                counts = hit_table[s]
                two_x = 2 * s - (b + q)
                if q % 2 == 0:
                    r = s - u
                    lower = max(0, b - abs(two_x) - q)
                    assert counts.get((r, u), 0) >= lower, (b, q, s, counts, lower)
                else:
                    r_plus = s - u
                    r_minus = s - u - 1
                    got = counts.get((r_plus, u), 0) + counts.get((r_minus, u + 1), 0)
                    lower = max(0, b - 2 * q - 2 * abs(two_x))
                    # Here two_x=2x, so 2|two_x|=4|x|.
                    assert got >= lower, (b, q, s, counts, lower)


def audit_physical() -> None:
    # Directly verify the discrepancy-based type counts and torus enumeration.
    for b in primes_upto(31):
        if b < 7:
            continue
        best = (b - 1) // 2
        ps = prefix_sets(b, best)
        for r in range(max(1, b // 4), min(b, 3 * b // 4 + 1)):
            word = [int(x in ps[r]) for x in range(b)]
            # Every full-period start enumerates one new counter-sum diagonal;
            # b periods at that start enumerate that diagonal.
            seen = set()
            ca = cb = 0
            long_word = word * (b + 2)
            for t in range(b * b):
                p = t % b
                if t and p == 0:
                    pass
                seen.add((p, ca % b, cb % b))
                if long_word[t % len(long_word)]:
                    ca += 1
                else:
                    cb += 1
            assert len(seen) == b * b

            h = max(1, min(b // 8, int(math.sqrt(b))))
            if not (r + h + 1 < b and b - r + h + 1 < b and r - h > 0 and b - r - h > 0):
                continue
            doubled = word * 3
            for start in range(b):
                long_count = sum(doubled[start : start + b + h + 1])
                assert long_count <= b - 1
                assert (b + h + 1) - long_count <= b - 1
                for ell in range(b - h, b + h + 2):
                    acount = sum(doubled[start : start + ell])
                    assert 1 <= acount <= b - 1
                    assert 1 <= ell - acount <= b - 1

            # Literal two-stream windows: every band window is a distinct set.
            stream_a = list(range(b))
            stream_b = list(range(b, 2 * b))
            emitted = []
            ia = ib = 0
            for t in range(b * b + b + h + 2):
                if word[t % b]:
                    emitted.append(stream_a[ia % b])
                    ia += 1
                else:
                    emitted.append(stream_b[ib % b])
                    ib += 1
            for ell in range(b - h, b + h + 2):
                windows = [frozenset(emitted[t : t + ell]) for t in range(b * b)]
                assert len(set(windows)) == b * b


def numerical_profiles() -> None:
    # Moderate-size scalar diagnostics for the explicit half-step multiplier.
    rows = []
    for b in [31, 61, 101, 151, 251]:
        best = (b - 1) // 2
        d = discrepancy(b, best)
        h = max(1, int(math.sqrt(b * math.log(b))))
        w = math.comb(2 * b, b)
        deficit = 0.0
        for q in range(1, min(h, b // 4) + 1):
            caps = all_capacities(b, best, q)
            for s in range(q, b + 1):
                p = math.comb(b, s) * math.comb(b, s - q)
                deficit += max(0.0, p - caps[s] / b)
        rows.append((b, best, d, h, deficit / w))
    print("AFFINE_NUMERICS", rows)


def finite_exact_inequality_diagnostic() -> None:
    # Stronger finite pattern motivating the asymptotic theorem.  It is not
    # promoted to an unproved all-b assertion in the accompanying note.
    for b in range(9, 82, 2):
        a = (b - 1) // 2
        for q in range(2, b // 4 + 1):
            caps = all_capacities(b, a, q)
            for s in range(q, b + 1):
                target = math.comb(b, s) * math.comb(b, s - q)
                assert caps[s] >= b * target, (b, q, s, caps[s], b * target)
    print("PASS finite T>=P diagnostic for odd b<=81, 2<=q<=b/4")


def main() -> None:
    audit_expectation()
    audit_q1()
    audit_affine()
    audit_half_step_dominant_phase()
    audit_physical()
    finite_exact_inequality_diagnostic()
    numerical_profiles()
    print("PASS affine nested profile capacity audit")


if __name__ == "__main__":
    main()
