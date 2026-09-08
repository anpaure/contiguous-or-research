#!/usr/bin/env python3
"""Exact MSW wreath-bank versus alternating-GK phase compatibility census."""

from __future__ import annotations

import argparse
from collections import Counter
from itertools import product
from math import comb


def dyck_words(m: int):
    def rec(pos: int, ones: int, word: list[str]):
        if pos == 2 * m:
            yield "".join(word)
            return
        if ones < m:
            word.append("1")
            yield from rec(pos + 1, ones + 1, word)
            word.pop()
        zeros = pos - ones
        if zeros < ones:
            word.append("0")
            yield from rec(pos + 1, ones, word)
            word.pop()

    yield from rec(0, 0, [])


def mu(word: str) -> str:
    return word[::-1].translate(str.maketrans("01", "10"))


def rho(word: str) -> list[int]:
    if not word:
        return []
    height = 0
    close = None
    for i, bit in enumerate(word):
        height += 1 if bit == "1" else -1
        if height == 0:
            close = i
            break
    assert close is not None
    u = word[1:close]
    v = word[close + 1 :]
    d = len(u) + 2
    return [d] + [d - x for x in rho(mu(u))] + [1] + [d + x for x in rho(v)]


def canonical_cycle(seq):
    seq = tuple(seq)
    rots = [seq[i:] + seq[:i] for i in range(len(seq))]
    rev = tuple(reversed(seq))
    rots.extend(rev[i:] + rev[:i] for i in range(len(seq)))
    return min(rots)


def msw_row(word: str) -> tuple[int, ...]:
    m = len(word) // 2
    n = 2 * m + 1
    omitted = [x - 1 for x in rho(word)] + [2 * m]
    return canonical_cycle(tuple(omitted[(-1 - 2 * j) % n] for j in range(n)))


def windows(order: tuple[int, ...], size: int) -> list[int]:
    b = len(order)
    return [
        sum(1 << order[(end - q) % b] for q in range(size))
        for end in range(b)
    ]


def top_excess(x: int, y: int, b: int) -> int:
    height = 0
    minimum = 0
    for q in range(b):
        height += 1 if x >> q & 1 else -1
        minimum = min(minimum, height)
        height += 1 if y >> q & 1 else -1
        minimum = min(minimum, height)
    assert height == 0
    return -minimum


def phase_profile(alpha: tuple[int, ...], beta: tuple[int, ...], h: int):
    b = len(alpha)
    m = (b - 1) // 2
    aa = windows(alpha, m)
    bb = windows(beta, m + 1)
    colors = []
    minima = []
    for p in range(b):
        kk = [top_excess(aa[i], bb[(p - i) % b], b) for i in range(b)]
        parity = {k & 1 for k in kk}
        colors.append(next(iter(parity)) if len(parity) == 1 else None)
        minima.append(min(kk))
    tau = [1 if (m * x) % b < m else 0 for x in range(b)]
    mono = sum(c is not None for c in colors)
    persistent = sum(c is not None and minima[p] >= h for p, c in enumerate(colors))
    correct = max(
        sum(colors[p] == (tau[(p + shift) % b] ^ flip) for p in range(b))
        for shift in range(b)
        for flip in (0, 1)
    )
    correct_persistent = max(
        sum(
            colors[p] == (tau[(p + shift) % b] ^ flip) and minima[p] >= h
            for p in range(b)
        )
        for shift in range(b)
        for flip in (0, 1)
    )
    return mono, persistent, correct, correct_persistent, tuple(colors), tuple(minima)


def build_rows(m: int):
    roots = list(dyck_words(m))
    rows = [msw_row(word) for word in roots]
    b = 2 * m + 1
    seen = set()
    seen_upper = set()
    for row in rows:
        ww = set(windows(row, m))
        uu = set(windows(tuple(reversed(row)), m + 1))
        assert len(ww) == b
        assert len(uu) == b
        assert not (seen & ww)
        assert not (seen_upper & uu)
        seen |= ww
        seen_upper |= uu
    assert len(seen) == comb(b, m)
    assert len(seen_upper) == comb(b, m + 1)
    return roots, rows


def audit(m: int, h: int):
    roots, rows = build_rows(m)
    b = 2 * m + 1
    raw_hist = Counter()
    flexible_hist = Counter()
    best_raw = None
    best_flexible = None
    for ia, ib in product(range(len(rows)), repeat=2):
        raw = phase_profile(rows[ia], rows[ib], h)
        raw_hist[raw[:4]] += 1
        candidate = (raw[:4], ia, ib, raw[4], raw[5])
        if best_raw is None or candidate[0] > best_raw[0]:
            best_raw = candidate

        variants = []
        for ra in (False, True):
            for rb in (False, True):
                alpha = tuple(reversed(rows[ia])) if ra else rows[ia]
                beta = tuple(reversed(rows[ib])) if rb else rows[ib]
                variants.append((phase_profile(alpha, beta, h), ra, rb))
        flex, ra, rb = max(variants, key=lambda item: item[0][:4])
        flexible_hist[flex[:4]] += 1
        candidate = (flex[:4], ia, ib, ra, rb, flex[4], flex[5])
        if best_flexible is None or candidate[0] > best_flexible[0]:
            best_flexible = candidate

    need_each_orientation = max(0, (b - 1 - h + 2) // 2)
    need_total = 2 * need_each_orientation
    raw_enough = sum(count for key, count in raw_hist.items() if key[3] >= need_total)
    flex_enough = sum(count for key, count in flexible_hist.items() if key[3] >= need_total)
    def summary(hist):
        total = sum(hist.values())
        return {
            "blocks": total,
            "zero_mono": sum(v for k, v in hist.items() if k[0] == 0),
            "mono_mean": sum(k[0] * v for k, v in hist.items()) / total,
            "mono_max": max(k[0] for k in hist),
            "persistent_mean": sum(k[1] * v for k, v in hist.items()) / total,
            "persistent_max": max(k[1] for k in hist),
            "correct_mean": sum(k[2] * v for k, v in hist.items()) / total,
            "correct_max": max(k[2] for k in hist),
            "correct_persistent_mean": sum(k[3] * v for k, v in hist.items()) / total,
            "correct_persistent_max": max(k[3] for k in hist),
        }
    raw_summary = summary(raw_hist)
    flexible_summary = summary(flexible_hist)
    expected = {
        2: (4, 2, 2, 1, 0, 0, 6, 0),
        3: (25, 20, 9, 4, 0, 10, 24, 0),
        4: (196, 156, 57, 5, 3, 115, 113, 5),
        5: (1764, 1493, 399, 5, 41, 1240, 711, 67),
        6: (17424, 15290, 3068, 6, 380, 13527, 5195, 666),
    }
    if h == 2 and m in expected:
        values = expected[m]
        assert raw_summary["blocks"] == values[0]
        assert raw_summary["zero_mono"] == values[1]
        assert round(raw_summary["mono_mean"] * values[0]) == values[2]
        assert raw_summary["mono_max"] == values[3]
        assert round(raw_summary["persistent_mean"] * values[0]) == values[4]
        assert flexible_summary["zero_mono"] == values[5]
        assert round(flexible_summary["mono_mean"] * values[0]) == values[6]
        assert round(flexible_summary["persistent_mean"] * values[0]) == values[7]
        assert raw_enough == 0 and flex_enough == 0
    print(
        {
            "m": m,
            "b": b,
            "H": h,
            "rows": len(rows),
            "source_windows": len(rows) * b,
            "need_total_persistent": need_total,
            "raw_summary": raw_summary,
            "flexible_summary": flexible_summary,
            "raw_hist": sorted(raw_hist.items()),
            "flexible_hist": sorted(flexible_hist.items()),
            "raw_enough_blocks": raw_enough,
            "flexible_enough_blocks": flex_enough,
            "best_raw": best_raw,
            "best_flexible": best_flexible,
        },
        flush=True,
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--m", type=int, nargs="+", default=[2, 3, 4, 5, 6])
    parser.add_argument("--H", type=int, default=2)
    args = parser.parse_args()
    for mm in args.m:
        audit(mm, args.H)
