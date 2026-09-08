#!/usr/bin/env python3
"""Find three packed q4 star insertion potentials at the k=17 boundary.

Substantive search belongs on H100.  The emitted literal orders are checked
against both lifted shores of the V13 atom and the no-fresh insertion pair.
"""

from __future__ import annotations

import json
import random
import sys

sys.path.insert(0, "scratch")
from verify_q4_v13_seven_by_seven_atom_20260814 import BASE, EXTRA, deck


GROUND = frozenset(range(17))
C0 = frozenset((13, 14, 15, 16))
C = C0 | {0}
P = frozenset((1, 2, 3, 4))
H = C | P
S = frozenset((1, 2, 3, 4, 5, 6))
Z = 7
E = tuple(sorted(GROUND - S - {Z}))
OLD_INSERTION = (2, 3, 4, 6, 7, 8, 10, 12, 9, 11)
NEW_INSERTION = (1,) + OLD_INSERTION


def windows(order):
    n = len(order)
    return {
        frozenset(order[(i + j) % n] for j in range(4))
        for i in range(n)
    }


def core_deck(core, order):
    return {frozenset(core) | window for window in windows(order)}


def insert(order, value, cut):
    return tuple(order[:cut]) + (value,) + tuple(order[cut:])


def lifted_atom(sign):
    return {
        C0 | owner
        for _, rail_sign, center, order in BASE + EXTRA
        if rail_sign == sign
        for owner in deck(center, order)
    }


def main():
    assert len(E) == 10 and C0 <= set(E)
    rng = random.Random(20260814)
    atom_positive = lifted_atom(1)
    atom_negative = lifted_atom(-1)
    insertion_old = core_deck(C, OLD_INSERTION)
    insertion_new = core_deck(C, NEW_INSERTION)
    assert not (insertion_old & atom_positive)
    assert not (insertion_new & atom_negative)
    assert H in insertion_new and H not in insertion_old

    attempts = 0
    solution = None
    for restart in range(10000):
        packed = []
        small_union = set()
        big_union = set()
        for copy in range(3):
            found = None
            for _ in range(20000):
                attempts += 1
                order = list(E)
                rng.shuffle(order)
                cut = rng.randrange(11)
                large = insert(order, Z, cut)
                small_windows = windows(order)
                large_windows = windows(large)
                if C0 in small_windows or C0 in large_windows:
                    continue
                if small_windows & small_union or large_windows & big_union:
                    continue
                found = (tuple(order), large, cut,
                         small_windows, large_windows)
                break
            if found is None:
                break
            order, large, cut, small_windows, large_windows = found
            packed.append({"small": order, "large": large, "cut": cut})
            small_union |= small_windows
            big_union |= large_windows
        if len(packed) == 3:
            solution = packed
            break
    assert solution is not None

    # Use copy i also as the leaf potential Phi_{i+2}.  Different star
    # cores are automatically signature-disjoint because toggles avoid S.
    phi1_small = set()
    phi1_big = set()
    for item in solution:
        small = core_deck(S - {1}, item["small"])
        big = core_deck(S - {1}, item["large"])
        assert not (small & phi1_small)
        assert not (big & phi1_big)
        phi1_small |= small
        phi1_big |= big

    leaf_small = set()
    leaf_big = set()
    for u, item in zip((2, 3, 4), solution):
        leaf_small |= core_deck(S - {u}, item["small"])
        leaf_big |= core_deck(S - {u}, item["large"])

    macro_minus = insertion_old | phi1_small | leaf_big
    macro_plus = insertion_new | phi1_big | leaf_small
    assert len(macro_minus) == 10 + 3 * 10 + 3 * 11 == 73
    assert len(macro_plus) == 11 + 3 * 11 + 3 * 10 == 74
    assert H not in macro_minus and H in macro_plus
    assert not (macro_minus & atom_positive)
    assert not (macro_plus & atom_negative)

    result = {
        "status": "PASS",
        "attempts": attempts,
        "ground": sorted(GROUND),
        "C0": sorted(C0),
        "C": sorted(C),
        "P": sorted(P),
        "H": sorted(H),
        "S": sorted(S),
        "z": Z,
        "E": list(E),
        "insertion_old": list(OLD_INSERTION),
        "insertion_new": list(NEW_INSERTION),
        "packed_phi1_and_leaf_orders": [
            {"small": list(item["small"]),
             "large": list(item["large"]),
             "cut": item["cut"]}
            for item in solution
        ],
        "phi1_small_owners": len(phi1_small),
        "phi1_big_owners": len(phi1_big),
        "macro_minus_owners": len(macro_minus),
        "macro_plus_owners": len(macro_plus),
        "atom_positive_collision": len(macro_minus & atom_positive),
        "atom_negative_collision": len(macro_plus & atom_negative),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
