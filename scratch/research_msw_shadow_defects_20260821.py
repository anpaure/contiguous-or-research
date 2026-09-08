#!/usr/bin/env python3
"""Exact shadow-defect counts of the canonical MSW Catalan wreath factor."""

from __future__ import annotations

import argparse
from collections import Counter


def dyck_words(m: int):
    def rec(pos: int, ones: int, word: list[str]):
        if pos == 2 * m:
            yield "".join(word)
            return
        if ones < m:
            word.append("1")
            yield from rec(pos + 1, ones + 1, word)
            word.pop()
        if pos - ones < ones:
            word.append("0")
            yield from rec(pos + 1, ones, word)
            word.pop()

    yield from rec(0, 0, [])


def mu(word: str) -> str:
    return word[::-1].translate(str.maketrans("01", "10"))


def rho(word: str) -> list[int]:
    if not word:
        return []
    h = 0
    close = None
    for i, bit in enumerate(word):
        h += 1 if bit == "1" else -1
        if h == 0:
            close = i
            break
    assert close is not None
    u, v = word[1:close], word[close + 1 :]
    d = len(u) + 2
    return [d] + [d - x for x in rho(mu(u))] + [1] + [d + x for x in rho(v)]


def msw_row(word: str):
    m = len(word) // 2
    b = 2 * m + 1
    q = [x - 1 for x in rho(word)] + [b - 1]
    return tuple(q[(-1 - 2 * j) % b] for j in range(b))


def window_masks(order, k):
    b = len(order)
    mask = sum(1 << order[j] for j in range(k))
    ans = [mask]
    for i in range(1, b):
        mask ^= 1 << order[i - 1]
        mask ^= 1 << order[(i + k - 1) % b]
        ans.append(mask)
    assert ans[-1] != ans[0]
    return ans


def binom(n: int, k: int) -> int:
    if k < 0 or k > n:
        return 0
    z = 1
    for i in range(1, k + 1):
        z = z * (n - k + i) // i
    return z


def main(ms, max_depth):
    for m in ms:
        b = 2 * m + 1
        counts = [Counter() for _ in range(max_depth + 1)]
        rows = 0
        for word in dyck_words(m):
            order = msw_row(word)
            rows += 1
            for q in range(max_depth + 1):
                k = m - q
                if k >= 1:
                    counts[q].update(window_masks(order, k))
        data = []
        for q in range(max_depth + 1):
            k = m - q
            if k < 1:
                continue
            total = binom(b, k)
            hist = Counter(counts[q].values())
            holes = total - len(counts[q])
            data.append(
                {
                    "q": q,
                    "rank": k,
                    "targets": total,
                    "slots": b * rows,
                    "holes": holes,
                    "hole_over_middle": holes / binom(b, m),
                    "covered_fraction": len(counts[q]) / total,
                    "max_mult": max(hist, default=0),
                    "hist_head": sorted(hist.items())[:8],
                }
            )
        print({"m": m, "b": b, "rows": rows, "depths": data}, flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--m", type=int, nargs="+", required=True)
    parser.add_argument("--max-depth", type=int, default=3)
    args = parser.parse_args()
    main(args.m, args.max_depth)
