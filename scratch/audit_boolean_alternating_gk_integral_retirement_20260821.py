#!/usr/bin/env python3
"""Exact/finite audit for the alternating GK integral retirement theorem.

The research workflow runs this checker on ssh h100.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from math import comb, exp, floor, isqrt, sqrt


def C(n: int, k: int) -> int:
    return comb(n, k) if 0 <= k <= n else 0


def bracket(mask: int, n: int):
    stack = []
    pairs = []
    for i in range(n):
        if (mask >> i) & 1:
            stack.append(i)
        elif stack:
            pairs.append((stack.pop(), i))
    return tuple(sorted(pairs))


def chain_from_key(key, n: int):
    paired = {i for pair in key for i in pair}
    unpaired = [i for i in range(n) if i not in paired]
    base = sum(1 << i for i, _ in key)
    return [base | sum(1 << i for i in unpaired[len(unpaired)-j:])
            for j in range(len(unpaired) + 1)]


def all_gk_chains(n: int):
    keys = {bracket(mask, n) for mask in range(1 << n)}
    chains = [chain_from_key(key, n) for key in keys]
    return chains


def E(b: int, r: int, u: int) -> int:
    return C(b, r + u) * C(b, r - u)


def n_lagrange(b: int, r: int, k: int) -> int:
    if k == b:
        return int(b % 2 == 1 and r == (b - 1) // 2)
    a = r - k // 2
    c = b - r - (k + 1) // 2
    value = Fraction(
        (k + 1) * C(b, a - 1) * C(b, c)
        + k * C(b + 1, a) * C(b - 1, c - 1),
        b - k,
    )
    assert value.denominator == 1, (b, r, k, value)
    return value.numerator


def n_telescoping(b: int, r: int, k: int) -> int:
    if k % 2 == 0:
        u = k // 2
        value = Fraction(r + u, b) * E(b, r, u) - Fraction(r + u + 1, b) * E(b, r, u + 1)
    else:
        u = k // 2
        value = Fraction(b - r - u, b) * E(b, r, u) - Fraction(b - r - u - 1, b) * E(b, r, u + 1)
    assert value.denominator == 1 and value >= 0, (b, r, k, value)
    return value.numerator


def GA(b: int, r: int, u: int) -> int:
    value = Fraction(b - r - u, b) * E(b, r, u)
    assert value.denominator == 1
    return value.numerator


def GB(b: int, r: int, u: int) -> int:
    value = Fraction(r + u, b) * E(b, r, u)
    assert value.denominator == 1
    return value.numerator


def audit_literal_scd(b: int):
    n = 2 * b
    chains = all_gk_chains(n)
    seen = {}
    stats = Counter()
    chain_records = []
    for chain in chains:
        ranks = [v.bit_count() for v in chain]
        assert ranks == list(range(ranks[0], ranks[-1] + 1))
        assert ranks[0] + ranks[-1] == n
        for v in chain:
            assert v not in seen, (b, v)
            seen[v] = chain
        flips = [(chain[j] ^ chain[j + 1]).bit_length() - 1
                 for j in range(len(chain) - 1)]
        assert all((flips[j] - flips[j + 1]) % 2 for j in range(len(flips)-1))
        mid = chain.index(next(v for v in chain if v.bit_count() == b))
        U = chain[mid]
        k = ranks[-1] - b
        r = sum((U >> (2*j)) & 1 for j in range(b))
        stats[(r, k)] += 1
        if k:
            first = (chain[mid] ^ chain[mid + 1]).bit_length() - 1
            color = first % 2  # even index=A, odd index=B
            assert (color == 0) == (k % 2 == 1), (b, r, k, first)
        chain_records.append((r, k, chain[mid:]))
    assert len(seen) == 1 << n

    for r in range(b + 1):
        for k in range(b + 1):
            assert stats[(r, k)] == n_lagrange(b, r, k)
            assert stats[(r, k)] == n_telescoping(b, r, k)
        assert sum(stats[(r, k)] for k in range(b + 1)) == C(b, r) ** 2
        for u in range((b + 1) // 2 + 1):
            odd_tail = sum(stats[(r, k)] for k in range(2*u, b+1) if k % 2)
            even_tail = sum(stats[(r, k)] for k in range(2*u, b+1) if not k % 2)
            assert odd_tail == GA(b, r, u)
            assert even_tail == GB(b, r, u)
    print("literal_scd", {"b": b, "chains": len(chains), "vertices": len(seen), "PASS": True})
    return chain_records


def audit_longest_selection(b: int, H: int, records):
    selected = []
    for r in range(1, b):
        L = C(b, r) ** 2
        d = abs(2*r-b)
        nr = max(0, (b-d-H+2)//2)
        K = nr * L // b
        assert L % b == 0
        for orient in (0, 1):  # 0=A (odd k), 1=B (even k)
            cc = [rec for rec in records if rec[0] == r and ((rec[1] % 2 == 0) == (orient == 1))]
            cc.sort(key=lambda z: z[1], reverse=True)
            assert K <= len(cc)
            take = cc[:K]
            if nr:
                assert K % nr == 0 and K // nr == L // b
            selected.extend((r, orient, rec) for rec in take)
            for q in range(1, H+1):
                actual = sum(rec[1] >= q for rec in take)
                if orient == 0:
                    total = GA(b, r, q//2)  # q=2u or 2u+1
                else:
                    total = GB(b, r, (q+1)//2) if q % 2 else GB(b, r, q//2)
                assert actual == min(K, total), (b,H,r,orient,q,actual,K,total)

    source_seen = set()
    target_seen = set()
    incidence = 0
    for r, orient, rec in selected:
        rr, k, upper = rec
        source = upper[0]
        assert source not in source_seen
        source_seen.add(source)
        for q in range(1, min(H, k)+1):
            target = upper[q]
            key=(q,target)
            assert key not in target_seen
            target_seen.add(key)
            incidence += 1
    print("longest_selection", {"b":b,"H":H,"selected_chains":len(selected),
                                  "real_incidence":incidence,"PASS":True})


def prime(n: int) -> bool:
    if n < 2:
        return False
    for p in range(2, isqrt(n)+1):
        if n % p == 0:
            return False
    return True


def audit_finite_bounds(b: int, H: int):
    assert b >= 128 and H >= 8 and H <= b//16
    assert b % 2
    checked=0
    total_D=0
    for r in range(b+1):
        L=C(b,r)**2
        d=abs(2*r-b)
        if d > b/16:
            continue
        nr=(b-d-H+2)//2
        K=Fraction(nr*L,b)
        assert K.denominator==1
        Delta=d+H
        assert K >= Fraction(b-d-H+1,2*b)*L
        vals=[]
        maxu=(H+1)//2
        for u in range(maxu+1):
            aa=GA(b,r,u)
            bb=GB(b,r,u)
            if u:
                assert aa <= GA(b,r,u-1)
                assert bb <= GB(b,r,u-1)
            if u <= isqrt(b):
                assert float(Fraction(E(b,r,u),L))*exp(u*u/b) <= 1+1e-12
            if 8 <= u <= sqrt(b):
                assert GA(b,r,0)-aa >= Fraction(u*u,5*b)*L
                assert GB(b,r,0)-bb >= Fraction(u*u,16*b)*L
            vals.append((aa,bb))
        D=0
        positive_u=set()
        for q in range(1,H+1):
            a=GA(b,r,q//2)
            bu=(q+1)//2 if q%2 else q//2
            bb=GB(b,r,bu)
            D += max(Fraction(0),a-K)+max(Fraction(0),bb-K)
            if a>K: positive_u.add(q//2)
            if bb>K: positive_u.add(bu)
            assert max(Fraction(0),a-K) <= Fraction(Delta*L,b)
            assert max(Fraction(0),bb-K) <= Fraction(Delta*L,b)
        assert all(u < 8+4*sqrt(Delta)+1e-12 for u in positive_u)
        # Avoid irrational Fraction arithmetic: square the positive sides.
        rhs_ratio=64*(Delta+1)**1.5/b
        assert float(D/Fraction(L)) <= rhs_ratio*(1+1e-12)
        total_D += D
        checked += 1
    print("finite_bounds", {"b":b,"H":H,"core_splits":checked,
                             "core_deficit_over_W":float(total_D/Fraction(C(2*b,b))),"PASS":True})


def main():
    rec3=audit_literal_scd(3)
    audit_longest_selection(3,1,rec3)
    rec5=audit_literal_scd(5)
    audit_longest_selection(5,2,rec5)
    rec7=audit_literal_scd(7)
    audit_longest_selection(7,2,rec7)
    for b,H in ((257,8),(521,16),(1031,32)):
        assert prime(b)
        audit_finite_bounds(b,H)
    print("ALL BOOLEAN ALTERNATING GK INTEGRAL RETIREMENT CHECKS PASSED")


if __name__ == "__main__":
    main()
