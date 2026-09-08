#!/usr/bin/env python3
"""Explore exact strong suffix-compatible GK successor structure.

Research-only.  All runs are performed on H100.
"""

from collections import Counter
from itertools import combinations, permutations


def additions(n: int, source: frozenset[int]) -> tuple[int, ...]:
    bits = [i in source for i in range(n)]
    stack: list[int] = []
    matched = [False] * n
    for i, bit in enumerate(bits):
        if bit:
            stack.append(i)
        elif stack:
            j = stack.pop()
            matched[i] = matched[j] = True
    return tuple(
        reversed([i for i in range(n) if not matched[i] and not bits[i]])
    )


def strong_removals(n: int, source: frozenset[int]) -> list[tuple[int, tuple[int, ...]]]:
    add = additions(n, source)
    if len(add) < 2:
        return []
    out = []
    for x in sorted(source):
        successor = frozenset((source - {x}) | {add[0]})
        nxt = additions(n, successor)
        common = min(len(nxt), len(add) - 1)
        if common and nxt[:common] == add[1 : 1 + common]:
            out.append((x, nxt))
    return out


def main() -> None:
    for b in (3, 4):
        print("B", b)
        shown = 0
        for choice in combinations(range(2 * b), b):
            source = frozenset(choice)
            add = additions(2 * b, source)
            if len(add) < 2:
                continue
            if shown < 24:
                word = "".join("1" if i in source else "0" for i in range(2 * b))
                print(word, "ADD", add, "GOOD", strong_removals(2 * b, source))
                shown += 1

    for b in range(2, 8):
        n = 2 * b
        sources = [frozenset(c) for c in combinations(range(n), b)]
        add = {s: additions(n, s) for s in sources}

        def dirty_step(q: tuple[int, ...]) -> tuple[int, ...] | None:
            source = frozenset(q)
            aa = add[source]
            if not aa:
                return None
            qp = q[1:] + (aa[0],)
            ap = add[frozenset(qp)]
            common = min(len(ap), max(0, len(aa) - 1))
            if len(aa) == 1 or (
                common > 0 and ap[:common] == aa[1 : 1 + common]
            ):
                return qp
            return None

        transition_pairs: Counter[tuple[int, int]] = Counter()
        max_dirty = 0
        max_ups = 0
        max_consecutive_ups = 0
        path_hist: Counter[tuple[int, int, int]] = Counter()
        for clean_source in sources:
            if add[clean_source]:
                continue
            for q in permutations(sorted(clean_source)):
                for y in range(n):
                    if y in clean_source:
                        continue
                    cur = q[1:] + (y,)
                    seq: list[int] = [len(add[frozenset(cur)])]
                    seen = {cur}
                    while add[frozenset(cur)]:
                        nxt = dirty_step(cur)
                        if nxt is None or nxt in seen:
                            break
                        seen.add(nxt)
                        seq.append(len(add[frozenset(nxt)]))
                        cur = nxt
                    deltas = [y1 - x1 for x1, y1 in zip(seq, seq[1:])]
                    for pair in zip(deltas, deltas[1:]):
                        transition_pairs[pair] += 1
                    ups = sum(delta == 1 for delta in deltas)
                    consecutive = 0
                    run = 0
                    for delta in deltas:
                        if delta == 1:
                            run += 1
                            consecutive = max(consecutive, run)
                        else:
                            run = 0
                    max_dirty = max(max_dirty, len(seq))
                    max_ups = max(max_ups, ups)
                    max_consecutive_ups = max(max_consecutive_ups, consecutive)
                    path_hist[(seq[0], len(seq), ups)] += 1
        print(
            "EXCURSION",
            b,
            "MAX_DIRTY",
            max_dirty,
            "MAX_UPS",
            max_ups,
            "MAX_CONSECUTIVE_UPS",
            max_consecutive_ups,
            "DELTA_PAIRS",
            sorted(transition_pairs.items()),
            "TOP_PATH_TYPES",
            path_hist.most_common(20),
        )


if __name__ == "__main__":
    main()
