#!/usr/bin/env python3
"""Independent exact replay for the six-owner adjacent-terminal cable."""

from __future__ import annotations

from hashlib import sha256
import json


def cyc_runs(bits: list[int]) -> tuple[int, int]:
    n = len(bits)
    assert 0 < sum(bits) < n
    doubled = bits + bits
    best = {0: 0, 1: 0}
    run = 1
    for i in range(1, 2 * n):
        if doubled[i] == doubled[i - 1]:
            run += 1
        else:
            best[doubled[i - 1]] = max(best[doubled[i - 1]], min(run, n))
            run = 1
    best[doubled[-1]] = max(best[doubled[-1]], min(run, n))
    return best[1], best[0]


def build(rank: int):
    ground = [f"g{i}" for i in range(2 * rank - 1)]
    # K has rank-2 labels.  The first two are the clock deletions.
    K = set(ground[: rank - 2])
    x1, x2 = ground[0], ground[1]
    a, z, b, y1, y2 = ground[rank - 2 : rank + 3]
    assert len(K | {a, z, b, y1, y2}) == rank + 3

    C = K | {a, z}
    E = K | {a, b}
    P1 = (K - {x1}) | {y1, a, b}
    P2 = (K - {x1, x2}) | {y1, y2, a, b}
    Q0 = (K - {x1, x2}) | {y1, y2, z, a}
    Q1 = (K - {x2}) | {y2, z, a}
    cyc = [C, E, P1, P2, Q0, Q1]

    assert all(len(v) == rank for v in cyc)
    assert len({frozenset(v) for v in cyc}) == 6
    assert all(len(cyc[i] ^ cyc[(i + 1) % 6]) == 2 for i in range(6))

    lower = [cyc[i] & cyc[(i + 1) % 6] for i in range(6)]
    upper = [cyc[i] | cyc[(i + 1) % 6] for i in range(6)]
    low2 = [cyc[i] & cyc[(i + 1) % 6] & cyc[(i + 2) % 6] for i in range(6)]
    up2 = [cyc[i] | cyc[(i + 1) % 6] | cyc[(i + 2) % 6] for i in range(6)]
    for deck in (lower, upper, low2, up2):
        assert len({frozenset(v) for v in deck}) == 6

    variable = [g for g in ground if 0 < sum(g in v for v in cyc) < 6]
    owner_runs = [cyc_runs([int(g in v) for v in cyc]) for g in variable]
    upper_variable = [g for g in ground if 0 < sum(g in v for v in upper) < 6]
    upper_runs = [cyc_runs([int(g in v) for v in upper]) for g in upper_variable]
    assert min(a for a, _ in owner_runs) == 3
    assert min(b for _, b in owner_runs) == 3
    assert min(a for a, _ in upper_runs) == 4
    assert min(b for _, b in upper_runs) == 2

    # The edge C-E and the complementary five-edge arc are distinct channels.
    assert len(C ^ E) == 2
    long_arc = [C, Q1, Q0, P2, P1, E]
    assert all(len(long_arc[i] ^ long_arc[i + 1]) == 2 for i in range(5))
    assert all(
        frozenset({frozenset(long_arc[i]), frozenset(long_arc[i + 1])})
        != frozenset({frozenset(C), frozenset(E)})
        for i in range(5)
    )

    return {
        "rank": rank,
        "ground": len(ground),
        "owners": len(cyc),
        "lower": len(lower),
        "upper": len(upper),
        "lower_q2": len(low2),
        "upper_q2": len(up2),
        "owner_min": [3, 3],
        "upper_min": [4, 2],
    }


def main() -> None:
    rows = [build(rank) for rank in range(4, 51)]
    payload = json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()
    print("ADJACENT_TERMINAL_RESIDENT_TWO_CHANNEL_CABLE PASS")
    print("checked ranks 4..50")
    print(rows[0])
    print(rows[-1])
    print("result digest", sha256(payload).hexdigest())


if __name__ == "__main__":
    main()
