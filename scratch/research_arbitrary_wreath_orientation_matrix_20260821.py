#!/usr/bin/env python3
"""Finite diagnostics for GK orientations on pairs of cyclic interval decks.

Research only.  Run on h100.  Cyclic orders are represented with first label 0
to quotient out rotation of the counter.
"""

from __future__ import annotations

import argparse
import itertools
from collections import Counter, defaultdict


def windows(order: tuple[int, ...], length: int) -> list[int]:
    b = len(order)
    ans = []
    for i in range(b):
        mask = 0
        for q in range(length):
            mask |= 1 << order[(i + q) % b]
        ans.append(mask)
    return ans


def top_excess(xmask: int, ymask: int, b: int) -> int:
    height = 0
    minimum = 0
    for q in range(b):
        height += 1 if (xmask >> q) & 1 else -1
        minimum = min(minimum, height)
        height += 1 if (ymask >> q) & 1 else -1
        minimum = min(minimum, height)
    assert height == 0
    return -minimum


def orientation_matrix(alpha, beta, r):
    b = len(alpha)
    xs = windows(alpha, r)
    ys = windows(beta, b - r)
    return [[top_excess(xs[i], ys[j], b) & 1 for j in range(b)] for i in range(b)]


def phase_word(matrix):
    """Return -1 on mixed antidiagonals, otherwise their common 0/1 color."""
    b = len(matrix)
    out = []
    for p in range(b):
        vals = {matrix[i][(p - i) % b] for i in range(b)}
        out.append(next(iter(vals)) if len(vals) == 1 else -1)
    return tuple(out)


def best_almost_alternating_score(word):
    """Optimize against cyclic words with exactly one equal adjacent edge."""
    b = len(word)
    best = 0
    best_tau = None
    for defect in range(b):
        for bit0 in range(2):
            tau = [bit0]
            for q in range(1, b):
                tau.append(tau[-1] if q - 1 == defect else 1 - tau[-1])
            # The wrap edge is the defect when defect=b-1.
            if defect == b - 1:
                tau = [(bit0 + q) & 1 for q in range(b)]
            assert sum(tau[q] == tau[(q + 1) % b] for q in range(b)) == 1
            score = sum(word[q] == tau[q] for q in range(b))
            if score > best:
                best, best_tau = score, tuple(tau)
    return best, best_tau


def best_almost_alternating_correlation(matrix):
    b = len(matrix)
    phase_sums = [sum(1 if matrix[i][(p-i) % b] else -1 for i in range(b)) for p in range(b)]
    best = -10**9
    arg = None
    for defect in range(b):
        for bit0 in range(2):
            if defect == b - 1:
                tau = [(bit0 + q) & 1 for q in range(b)]
            else:
                tau = [bit0]
                for q in range(1, b):
                    tau.append(tau[-1] if q - 1 == defect else 1 - tau[-1])
            corr = sum((1 if tau[p] else -1) * phase_sums[p] for p in range(b))
            if corr > best:
                best, arg = corr, (tuple(tau), tuple(phase_sums))
    return best, arg


def variation_stats(matrix):
    b = len(matrix)
    hflip = sum(matrix[i][j] != matrix[i][(j + 1) % b] for i in range(b) for j in range(b))
    vflip = sum(matrix[i][j] != matrix[(i + 1) % b][j] for i in range(b) for j in range(b))
    square_odd = sum(
        matrix[i][j] ^ matrix[(i + 1) % b][j]
        ^ matrix[i][(j + 1) % b] ^ matrix[(i + 1) % b][(j + 1) % b]
        for i in range(b) for j in range(b)
    )
    checker = sum(
        matrix[i][j] == matrix[(i + 1) % b][(j + 1) % b]
        and matrix[i][j] != matrix[(i + 1) % b][j]
        and matrix[i][j] != matrix[i][(j + 1) % b]
        for i in range(b) for j in range(b)
    )
    return hflip, vflip, square_odd, checker


def canonicalize_dihedral(order):
    b = len(order)
    seqs = []
    for rev in (order, tuple(reversed(order))):
        for s in range(b):
            seqs.append(tuple(rev[(s + i) % b] for i in range(b)))
    return min(seqs)


def exhaustive(b: int):
    assert b % 2 == 1
    r = (b - 1) // 2
    orders = [(0,) + p for p in itertools.permutations(range(1, b))]
    score_hist = Counter()
    mono_hist = Counter()
    flip_hist = Counter()
    max_records = []
    max_flip_records = []
    max_score = -1
    max_hflip = -1
    max_corr = -10**9
    max_corr_records = []
    max_flip_sum = -1
    max_flip_sum_records = []
    max_checker = -1
    max_checker_records = []
    for ai, alpha in enumerate(orders):
        for beta in orders:
            m = orientation_matrix(alpha, beta, r)
            word = phase_word(m)
            score, tau = best_almost_alternating_score(word)
            corr, corr_arg = best_almost_alternating_correlation(m)
            mono = sum(x >= 0 for x in word)
            hs, vs, sq, chk = variation_stats(m)
            score_hist[score] += 1
            mono_hist[mono] += 1
            flip_hist[(hs, vs, sq, chk)] += 1
            if score > max_score:
                max_score = score
                max_records = [(alpha, beta, word, tau, (hs, vs, sq, chk))]
            elif score == max_score and len(max_records) < 20:
                max_records.append((alpha, beta, word, tau, (hs, vs, sq, chk)))
            max_hflip = max(max_hflip, hs, vs)
            if hs + vs > max_flip_sum:
                max_flip_sum = hs + vs
                max_flip_sum_records = [(alpha, beta, word, (hs, vs, sq, chk))]
            elif hs + vs == max_flip_sum and len(max_flip_sum_records) < 20:
                max_flip_sum_records.append((alpha, beta, word, (hs, vs, sq, chk)))
            if chk > max_checker:
                max_checker = chk
                max_checker_records = [(alpha, beta, word, (hs, vs, sq, chk))]
            elif chk == max_checker and len(max_checker_records) < 20:
                max_checker_records.append((alpha, beta, word, (hs, vs, sq, chk)))
            if corr > max_corr:
                max_corr = corr
                max_corr_records = [(alpha, beta, corr_arg, word)]
            elif corr == max_corr and len(max_corr_records) < 20:
                max_corr_records.append((alpha, beta, corr_arg, word))
            if max(hs, vs) > (max_flip_records[0][0] if max_flip_records else -1):
                max_flip_records = [(max(hs, vs), alpha, beta, word, (hs, vs, sq, chk))]
            elif max(hs, vs) == max_flip_records[0][0] and len(max_flip_records) < 20:
                max_flip_records.append((max(hs, vs), alpha, beta, word, (hs, vs, sq, chk)))
        if ai % 100 == 0:
            print(f"progress alpha {ai}/{len(orders)}")
    print("b", b, "pairs", len(orders) ** 2)
    print("score_hist", sorted(score_hist.items()))
    print("mono_hist", sorted(mono_hist.items()))
    print("max_score", max_score, "max_hvflip", max_hflip)
    print("max_corr", max_corr)
    print("max_flip_sum", max_flip_sum)
    print("max_checker", max_checker)
    for rec in max_records:
        print("MAX", rec)
    for rec in max_flip_records:
        print("MAXFLIP", rec)
    for rec in max_corr_records:
        print("MAXCORR", rec)
    for rec in max_flip_sum_records:
        print("MAXFLIPSUM", rec)
    for rec in max_checker_records:
        print("MAXCHECKER", rec)
    print("top flip triples", flip_hist.most_common(10))


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("b", type=int)
    args = ap.parse_args()
    exhaustive(args.b)
