#!/usr/bin/env python3
"""Computation C1 (block 44.6): return-time spectra of equivariant
2-factors in the middle levels of Q_n, n = 7, 9, 11, 13.

Two explicit rotation-invariant 1-factorization families:
  LEXICAL (Kierstead--Trotter 1988, ICALP'18 form): interpret the
    characteristic bitstring as a lattice path; the i-lexical
    up-matching flips the i-th 0-bit (down-step) encountered when
    scanning down-steps row-wise from top to bottom and right to
    left within a row (no padding needed at the middle levels).
  MODULAR (Duffus--Kierstead--Snevily, JCTA 65 (1994) 334-342):
    for |B| = m, add the j-th largest element of the complement,
    j == i + Sigma(B) (mod m+1), 1 <= j <= m+1.

For matching pairs, the union is a disjoint set of cycles
alternating between levels m and m+1.  We report, per pair:
  #cycles, cycle lengths (and divisibility by 2n -- Theorem 27.4
  check), and the per-element flip return-time spectrum (the MDCU
  gap-band diagnostic): fraction of gaps within n +- 1, +- 2,
  max |gap - n|.

Tests predictions (P-a)/(P-b) of block 44.7.  Cheap: W(13) = 1716.
"""
import itertools
import sys
from collections import Counter


def heights(bits):
    """Height before each position; bits is a tuple of 0/1."""
    h = 0
    out = []
    for b in bits:
        out.append(h)
        h += 1 if b else -1
    return out


def lex_up(bits, i):
    """i-lexical up-matching partner: flip i-th down-step in
    row-wise top-to-bottom, right-to-left scan.  bits: tuple with
    m ones (level m of Q_n).  Returns new tuple or None."""
    h = heights(bits)
    downs = [p for p, b in enumerate(bits) if b == 0]
    # row of a down-step = its starting height h[p] (step occupies
    # h[p] -> h[p]-1); scan by descending row, then right-to-left.
    order = sorted(downs, key=lambda p: (-h[p], -p))
    if i >= len(order):
        return None
    p = order[i]
    return bits[:p] + (1,) + bits[p + 1:]


def dks_up(bits, i, n, m):
    """DKS modular up-matching m_i: add j-th largest element of the
    complement, j == i + Sigma(B) (mod m+1).  Elements 1..n (paper
    convention); bits index 0..n-1 holds element p+1."""
    B = [p + 1 for p, b in enumerate(bits) if b == 1]
    comp = sorted((p + 1 for p, b in enumerate(bits) if b == 0),
                  reverse=True)
    j = ((i + sum(B) - 1) % (m + 1)) + 1
    e = comp[j - 1]
    p = e - 1
    return bits[:p] + (1,) + bits[p + 1:]


def build_matching(n, m, kind, i):
    """Dict: level-m tuple -> level-(m+1) tuple."""
    M = {}
    for ones in itertools.combinations(range(n), m):
        bits = tuple(1 if p in ones else 0 for p in range(n))
        up = lex_up(bits, i) if kind == "lex" else dks_up(bits, i, n, m)
        assert up is not None and sum(up) == m + 1
        M[bits] = up
    # verify it is a perfect matching (injective on upper level)
    assert len(set(M.values())) == len(M), f"{kind}_{i} not a matching"
    return M


def cycles_of(Ma, Mb):
    """Cycle decomposition of the union of two perfect matchings."""
    inv_b = {v: k for k, v in Mb.items()}
    seen = set()
    cycles = []
    for start in Ma:
        if start in seen:
            continue
        cyc = []
        x = start
        while x not in seen:
            seen.add(x)
            up = Ma[x]
            cyc.append(x)
            cyc.append(up)
            x = inv_b[up]
        cycles.append(cyc)
    return cycles


def flip_seq(cyc):
    """Element flipped at each step around the cycle (cyclic)."""
    L = len(cyc)
    seq = []
    for t in range(L):
        a, b = cyc[t], cyc[(t + 1) % L]
        d = [p for p in range(len(a)) if a[p] != b[p]]
        assert len(d) == 1
        seq.append(d[0])
    return seq


def spectrum(cycles, n):
    lens = Counter(len(c) for c in cycles)
    bad_div = [l for l in lens if l % (2 * n) != 0]
    gaps = Counter()
    for cyc in cycles:
        seq = flip_seq(cyc)
        pos = {}
        for t, e in enumerate(seq):
            pos.setdefault(e, []).append(t)
        L = len(seq)
        for e, ps in pos.items():
            for a, b in zip(ps, ps[1:] + [ps[0] + L]):
                gaps[b - a] += 1
    total = sum(gaps.values())
    within1 = sum(v for g, v in gaps.items() if abs(g - n) <= 1) / total
    within2 = sum(v for g, v in gaps.items() if abs(g - n) <= 2) / total
    mx = max(abs(g - n) for g in gaps)
    return lens, bad_div, within1, within2, mx


def main():
    ns = [int(a) for a in sys.argv[1:]] or [7, 9, 11, 13]
    for n in ns:
        m = (n - 1) // 2
        pairs = {
            "lex(0,1)": ("lex", 0, "lex", 1),
            f"lex(0,{m})": ("lex", 0, "lex", m),
            "dks(1,2)": ("dks", 1, "dks", 2),
            f"dks(1,{m + 1})": ("dks", 1, "dks", m + 1),
            "mix lex0/dks1": ("lex", 0, "dks", 1),
        }
        for name, (ka, ia, kb, ib) in pairs.items():
            Ma = build_matching(n, m, ka, ia)
            Mb = build_matching(n, m, kb, ib)
            if Ma == Mb:
                print(f"n={n} {name}: identical matchings, skip")
                continue
            cyc = cycles_of(Ma, Mb)
            lens, bad, w1, w2, mx = spectrum(cyc, n)
            print(f"n={n} {name}: cycles={sum(lens.values())} "
                  f"lens={dict(sorted(lens.items()))} "
                  f"div2n={'OK' if not bad else f'FAIL{bad}'} "
                  f"gapfrac|d|<=1={w1:.3f} <=2={w2:.3f} maxdev={mx}",
                  flush=True)
    print("STATUS:C1DONE")


if __name__ == "__main__":
    main()
