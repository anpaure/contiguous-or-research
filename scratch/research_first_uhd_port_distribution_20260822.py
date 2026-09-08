#!/usr/bin/env python3
"""Exact diagnostics for first-UHD Dyck atoms and their FIFO ports.

For a Dyck word of semilength r, the macro word has length r-1.  If its
first factor U(A/B)D starts at the one-based macro position p, its port is
(u,v)=(2p+2,2p+3).  We orient an atom by requiring that selected horizontal
block to be A.

The script checks:

* the exact inclusion-exclusion formula for the number of atoms of type p;
* the port-count parity theorem;
* the raw-square/FIFO displacement identities; and
* the exact-order obstruction E_next != (u v) E_current, even up to rotation.

The enumeration is evidence only; the accompanying mathematical argument is
independent of it.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from math import comb

from audit_dyck_tail_seam_automaton_20260822 import dyck_words, macro, rho


def catalan(n: int) -> int:
    if n < 0:
        return 0
    return comb(2 * n, n) // (n + 1)


def predicted_port_count(r: int, p: int) -> int:
    """Atoms whose first UHD starts at one-based macro position p."""
    answer = 0
    for k in range((p - 1) // 3 + 1):
        answer += (-2) ** k * comb(p - 2 * k - 1, k) * catalan(r - 3 - 3 * k)
    return answer


def rotations(word: tuple[int, ...]):
    for shift in range(len(word)):
        yield word[shift:] + word[:shift]


def atom_record(raw: str, r: int):
    motzkin = macro(raw)
    start = next(
        (
            i
            for i in range(len(motzkin) - 2)
            if motzkin[i] == "U"
            and motzkin[i + 1] in {"A", "B"}
            and motzkin[i + 2] == "D"
        ),
        None,
    )
    if start is None or motzkin[start + 1] != "A":
        return None

    # start is zero-based; p is one-based.  The selected H block is p+1,
    # whose two binary coordinates are 2p+2 and 2p+3.
    p = start + 1
    u, v = 2 * p + 2, 2 * p + 3
    order = rho(raw)
    s = order.index(u) // 2 + 1
    gamma = order[: 2 * (s - 1)]
    c = order[2 * s - 2]
    d = order[2 * s + 1]
    delta = order[2 * s + 2 :]

    hole_word = (
        gamma
        + (v, d, c, v)
        + delta
        + (2 * r + 1,)
        + gamma
        + (u, d, c, u)
        + delta
        + (2 * r + 1,)
    )
    insertion = hole_word[::2]
    removal = hole_word[1::2]
    aligned_removal = tuple(
        removal[(j + r) % (2 * r + 1)] for j in range(2 * r + 1)
    )
    transposed = tuple(v if x == u else u if x == v else x for x in insertion)
    root = frozenset(i + 1 for i, bit in enumerate(raw) if bit == "1")
    common_base = root - {u}
    assert aligned_removal == transposed
    assert (insertion.index(u) - insertion.index(v)) % (2 * r + 1) == r + 2
    return {
        "p": p,
        "port": (u, v),
        "phase": s,
        "macro": motzkin,
        "E": insertion,
        "tau_E": transposed,
        "base": common_base,
    }


def audit(r: int):
    records = [
        record
        for raw in dyck_words(r)
        for record in [atom_record(raw, r)]
        if record is not None
    ]
    by_position = Counter(record["p"] for record in records)
    by_position_phase = Counter((record["p"], record["phase"]) for record in records)
    for p in range(1, r - 2):
        assert by_position[p] == predicted_port_count(r, p)
        assert by_position[p] % 2 == catalan(r - 3) % 2

    # No outgoing transposed insertion order is an incoming order of another
    # atom of the same port type, even after changing the cyclic origin.
    orders = defaultdict(set)
    bases = defaultdict(set)
    for record in records:
        orders[record["p"]].add(record["E"])
        bases[record["p"]].add(record["base"])
    for record in records:
        assert not any(
            rotated in orders[record["p"]]
            for rotated in rotations(record["tau_E"])
        )
        u, v = record["port"]
        moving_palette = frozenset(range(1, 2 * r + 1)) - {u, v}
        # A shortened u-rail ends on the complementary moving base.  Such a
        # base cannot start another oriented Dyck atom: every Dyck base has
        # coordinate 1, whereas its moving-palette complement does not.
        assert 1 in record["base"] and 2 * r not in record["base"]
        assert moving_palette - record["base"] not in bases[record["p"]]

    return {
        "r": r,
        "atoms": len(records),
        "port_counts": tuple(by_position[p] for p in range(1, r - 2)),
        "odd_port_classes": sum(by_position[p] % 2 for p in range(1, r - 2)),
        "phase_values_by_port": {
            p: tuple(
                sorted(s for (position, s), count in by_position_phase.items()
                       if position == p and count)
            )
            for p in range(1, r - 2)
        },
        "odd_port_phase_cells": sum(count % 2 for count in by_position_phase.values()),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-r", type=int, default=12)
    args = parser.parse_args()
    for r in range(4, args.max_r + 1):
        print("FIRST_UHD_PORT_DISTRIBUTION_PASS", audit(r), flush=True)


if __name__ == "__main__":
    main()
