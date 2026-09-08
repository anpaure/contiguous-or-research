#!/usr/bin/env python3
"""Exhaustive r<=5 fixed-site PBBS audit. Execute only on ssh h100."""

from collections import Counter, defaultdict
from itertools import combinations
import json
import socket
import time


def first_after_min(w):
    value = 0
    prefixes = []
    for bit in w:
        value += 2 * bit - 1
        prefixes.append(value)
    return prefixes.index(min(prefixes))


def last_before_max(w):
    value = 0
    prefixes = []
    for bit in w:
        prefixes.append(value)
        value += 2 * bit - 1
    maximum = max(prefixes)
    return max(i for i, value in enumerate(prefixes) if value == maximum)


def literal_cancellation(w, pattern=(1, 0)):
    alive = list(range(len(w)))
    while len(alive) > 1:
        erased = set()
        for j, i in enumerate(alive):
            nxt = alive[(j + 1) % len(alive)]
            if (w[i], w[nxt]) == pattern:
                erased.update((i, nxt))
        assert erased, (w, pattern, alive)
        alive = [i for i in alive if i not in erased]
    assert w[alive[0]] == 0
    return alive[0]


def at_fixed_zero(w, site):
    return tuple(0 if i == site else 1 - bit for i, bit in enumerate(w))


def root(w, selected):
    n = len(w)
    return tuple(w[(selected + j) % n] for j in range(1, n))


def root_height(d):
    value = high = 0
    for bit in d:
        value += 2 * bit - 1
        assert value >= 0, d
        high = max(high, value)
    assert value == 0
    return high


def phi_delta(d):
    if not d:
        return (), 0
    value = high = 0
    marked = None
    for i, bit in enumerate(d):
        value += 2 * bit - 1
        if value > high:
            high, marked = value, i
    assert marked is not None and d[marked] == 1
    return (tuple(1 - b for b in d[marked + 1:]) + (0,)
            + tuple(1 - b for b in d[:marked])), marked + 1


def equality_incoming_gap(w, selected):
    n = len(w)
    particles = {i for i in range(n) if w[(i - 1) % n] == w[i]}
    assert selected in particles
    length = next(step for step in range(1, n + 1)
                  if (selected - step) % n in particles)
    previous = (selected - length) % n
    # For the distinguished zero, the incoming particle is another zero.
    assert w[previous] == w[selected] == 0
    assert length % 2 == 1
    return (length - 1) // 2


def audit(r):
    n = 2 * r + 1
    words = []
    for ones in combinations(range(n), r):
        chosen = set(ones)
        words.append(tuple(int(i in chosen) for i in range(n)))
    labels, forward, heights, incoming = {}, {}, {}, {}
    for w in words:
        label = first_after_min(w)
        assert label == literal_cancellation(w)
        inverse_label = last_before_max(w)
        assert inverse_label == literal_cancellation(w, (0, 1))
        nxt = at_fixed_zero(w, label)
        assert sum(nxt) == r
        assert all(not (x and y) for x, y in zip(w, nxt))
        assert tuple(i for i, (x, y) in enumerate(zip(w, nxt))
                     if x == y == 0) == (label,)
        assert at_fixed_zero(nxt, last_before_max(nxt)) == w
        assert at_fixed_zero(at_fixed_zero(w, inverse_label),
                             first_after_min(at_fixed_zero(w, inverse_label))) == w
        d = root(w, label)
        height = root_height(d)
        pd, delta = phi_delta(d)
        assert first_after_min(nxt) == (label + delta) % n
        assert root(nxt, first_after_min(nxt)) == pd
        assert root_height(pd) == height
        z = equality_incoming_gap(w, label)
        assert w[(label - 1) % n] == w[label] == 0
        assert (z == 0) == (w[(label - 2) % n] == 0)
        labels[w], forward[w], heights[w], incoming[w] = label, nxt, height, z
    assert len(set(forward.values())) == len(words)

    unseen = set(words)
    cycle_lengths = Counter()
    gaps = Counter()
    sum_t = 0
    all_trace_checks = 0
    top_zero_by_gap = Counter()
    while unseen:
        start = min(unseen)
        cycle = []
        cur = start
        while cur in unseen:
            unseen.remove(cur)
            cycle.append(cur)
            cur = forward[cur]
        assert cur == start
        length = len(cycle)
        cycle_lengths[length] += 1
        assert length >= n
        selected = defaultdict(list)
        for time_index, w in enumerate(cycle):
            selected[labels[w]].append(time_index)
        assert set(selected) == set(range(n))
        assert len(set(map(len, selected.values()))) == 1
        for label, positions in selected.items():
            for a, b in zip(positions, positions[1:] + [positions[0] + length]):
                gap = b - a
                assert gap % 2 == 1
                assert gap >= 2 * heights[cycle[a]] + 1
                t = (gap - 1) // 2
                gaps[gap] += 1
                sum_t += t
                if incoming[cycle[a]] == 0:
                    top_zero_by_gap[gap] += 1
                # At physical birth time a, edge q is the Johnson edge
                # X_(a-1+2q) -> X_(a+1+2q). Its label is inserted at
                # q=0 and removed at q=T+1, with no internal change.
                owners = [tuple(1 - bit for bit in cycle[(a - 1 + 2*q) % length])
                          for q in range(t + 3)]
                expected = [0] + [1] * (t + 1) + [0]
                assert [owner[label] for owner in owners] == expected
                for left, right in zip(owners, owners[1:]):
                    assert sum(left) == sum(right) == r + 1
                    if r:
                        assert sum(x != y for x, y in zip(left, right)) == 2
                # Exact repair includes both insertion and removal edges.
                assert len(owners) - 1 == t + 2
                all_trace_checks += 1
    assert all_trace_checks == len(words)
    assert sum_t == r * len(words)
    return {
        "r": r, "n": n, "states": len(words),
        "cycle_lengths": dict(sorted(cycle_lengths.items())),
        "gap_histogram": dict(sorted(gaps.items())),
        "top_zero_gap_histogram": dict(sorted(top_zero_by_gap.items())),
        "mean_T_exact_numerator": sum_t,
        "mean_T_exact_denominator": len(words),
        "trace_endpoint_checks": all_trace_checks,
        "all_checks": "PASS",
    }


if __name__ == "__main__":
    assert socket.gethostname().lower() == "arboghast", "Run only on verified h100 host"
    started = time.monotonic()
    # r=0 is omitted: its degenerate one-edge self-loop has a repeated
    # boundary trace; the stated physical sampling task is r>=1.
    rows = [audit(r) for r in range(1, 6)]
    print(json.dumps({"host": socket.gethostname(), "elapsed_seconds": time.monotonic()-started,
                      "scope": "exhaustive r=1,...,5, no sampling", "results": rows}, indent=2))
