#!/usr/bin/env python3
"""Small exact search for serializing interleaved GK middle chains.

For a rank-b source S, let a_1(S),a_2(S),... be the labels added on
the upward Greene--Kleitman chain (using 1 as an opening parenthesis).
We count Johnson neighbours S'=S-x+a_1(S) for which
a_1(S')=a_2(S).  Iterating such transitions is the first necessary
condition for one word to realize the prescribed retired chains.

This is exploratory only.  Run on H100.
"""

from __future__ import annotations

from collections import Counter
from itertools import combinations, permutations


def additions(n: int, ones: frozenset[int]) -> tuple[int, ...]:
    bits = [int(i in ones) for i in range(n)]
    stack: list[int] = []
    matched = [False] * n
    for i, bit in enumerate(bits):
        if bit:
            stack.append(i)
        elif stack:
            j = stack.pop()
            matched[j] = matched[i] = True
    zeros = [i for i in range(n) if not matched[i] and not bits[i]]
    ones_unmatched = [i for i in range(n) if not matched[i] and bits[i]]
    assert len(zeros) == len(ones_unmatched)
    return tuple(reversed(zeros))


def main() -> None:
    for b in range(2, 10):
        n = 2 * b
        all_sets = [frozenset(c) for c in combinations(range(n), b)]
        add = {s: additions(n, s) for s in all_sets}
        out_hist: Counter[int] = Counter()
        strict_hist: Counter[int] = Counter()
        kchange: Counter[int] = Counter()
        examples: list[tuple[frozenset[int], tuple[int, ...]]] = []
        for s in all_sets:
            aa = add[s]
            if len(aa) < 2:
                continue
            y0, y1 = aa[:2]
            candidates = []
            strict = []
            for x in s:
                sp = frozenset((s - {x}) | {y0})
                ap = add[sp]
                if ap and ap[0] == y1:
                    candidates.append(x)
                    kchange[len(ap) - len(aa)] += 1
                    # Stronger: the entire common remaining prefix agrees.
                    common = min(len(ap), len(aa) - 1)
                    if ap[:common] == aa[1 : 1 + common]:
                        strict.append(x)
            out_hist[len(candidates)] += 1
            strict_hist[len(strict)] += 1
            if not candidates and len(examples) < 3:
                examples.append((s, aa))
        print(
            "B",
            b,
            "VERTICES",
            len(all_sets),
            "OUT",
            sorted(out_hist.items()),
            "STRICT",
            sorted(strict_hist.items()),
            "ZERO_EXAMPLES",
            examples,
            "KCHANGE",
            sorted(kchange.items()),
        )

    # Ordered FIFO states.  The successor is forced by the first GK addition.
    # Retain a state only when this successor also supplies the second GK
    # addition (if one is claimed).  We report directed cycles of the resulting
    # partial functional graph.  This is a diagnostic, not a theorem.
    for b in range(2, 7):
        n = 2 * b
        add_cache: dict[frozenset[int], tuple[int, ...]] = {}

        def aa(s: frozenset[int]) -> tuple[int, ...]:
            if s not in add_cache:
                add_cache[s] = additions(n, s)
            return add_cache[s]

        nxt: dict[tuple[int, ...], tuple[int, ...]] = {}
        good_states = 0
        for q in permutations(range(n), b):
            s = frozenset(q)
            a = aa(s)
            if not a:
                continue
            qp = q[1:] + (a[0],)
            sp = frozenset(qp)
            ap = aa(sp)
            common = min(len(ap), max(0, len(a) - 1))
            if len(a) == 1 or (common > 0 and ap[:common] == a[1 : 1 + common]):
                nxt[q] = qp
                good_states += 1

        seen: dict[tuple[int, ...], int] = {}
        cycle_lengths: list[int] = []
        cycle_source_lengths: list[int] = []
        for start in nxt:
            if start in seen:
                continue
            path: list[tuple[int, ...]] = []
            loc: dict[tuple[int, ...], int] = {}
            cur = start
            while cur in nxt and cur not in seen and cur not in loc:
                loc[cur] = len(path)
                path.append(cur)
                cur = nxt[cur]
            if cur in loc:
                cyc = path[loc[cur] :]
                cycle_lengths.append(len(cyc))
                cycle_source_lengths.append(len({frozenset(q) for q in cyc}))
            for q in path:
                seen[q] = 1

        # Longest compatible suffix in the partial functional DAG.
        memo_len: dict[tuple[int, ...], int] = {}
        memo_src: dict[tuple[int, ...], int] = {}

        def plen(q: tuple[int, ...]) -> int:
            if q in memo_len:
                return memo_len[q]
            qp = nxt.get(q)
            if qp is None or qp not in nxt:
                memo_len[q] = 1
            else:
                memo_len[q] = 1 + plen(qp)
            return memo_len[q]

        longest_start = max(nxt, key=plen)
        longest = plen(longest_start)
        cur = longest_start
        srcs: list[frozenset[int]] = []
        while cur in nxt:
            srcs.append(frozenset(cur))
            qp = nxt[cur]
            if qp not in nxt:
                break
            cur = qp
        print(
            "FIFO",
            b,
            "GOOD",
            good_states,
            "TOTAL",
            1,
            "CYCLES",
            len(cycle_lengths),
            "MAX_STATE",
            max(cycle_lengths, default=0),
            "MAX_SOURCE",
            max(cycle_source_lengths, default=0),
            "TOP_STATE",
            sorted(cycle_lengths, reverse=True)[:10],
            "TOP_SOURCE",
            sorted(cycle_source_lengths, reverse=True)[:10],
            "MAX_PATH",
            longest,
            "MAX_PATH_DISTINCT_SOURCES",
            len(set(srcs)),
        )


if __name__ == "__main__":
    main()
