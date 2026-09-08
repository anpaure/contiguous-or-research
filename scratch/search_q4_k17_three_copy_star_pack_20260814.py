#!/usr/bin/env python3
"""Find the exact q4 k17 three-copy star packing for the common reserve.

All substantive runs belong on H100.  The ground is 0..16, the lifted atom
uses common core C0={13,14,15,16}, C=C0+{0}, P={1,2,3,4}, and the star uses
S={1,2,3,4,5,6}, z=7, E={0,8,...,16}.  Three copies at core S-{1} must be
old-deck and new-deck disjoint.  Leaf cores S-{2,3,4} are signature-distinct.
"""

import json
import random
import sys

sys.path.insert(0, "scratch")
from verify_q4_v13_seven_by_seven_atom_20260814 import BASE, EXTRA, deck


C0 = frozenset((13, 14, 15, 16))
C = C0 | {0}
P = frozenset((1, 2, 3, 4))
H = C | P
S = frozenset((1, 2, 3, 4, 5, 6))
Z = 7
E = tuple((0, 8, 9, 10, 11, 12, 13, 14, 15, 16))


def windows(order):
    n = len(order)
    return {
        frozenset(order[(i+j) % n] for j in range(4))
        for i in range(n)
    }


def owners(core, order):
    return {core | window for window in windows(order)}


def lifted_atom(sign):
    out = set()
    for _, rail_sign, center, order in BASE + EXTRA:
        if rail_sign != sign:
            continue
        out.update(C0 | owner for owner in deck(center, order))
    return out


def candidate(rng):
    old = list(E)
    rng.shuffle(old)
    gap = rng.randrange(len(old))
    new = old[:gap] + [Z] + old[gap:]
    if C0 in windows(old) or C0 in windows(new):
        return None
    return tuple(old), tuple(new)


def main():
    rng = random.Random(20260814)
    atom_positive = lifted_atom(1)
    atom_negative = lifted_atom(-1)
    chosen = []
    attempts = 0
    while len(chosen) < 3 and attempts < 1_000_000:
        attempts += 1
        item = candidate(rng)
        if item is None:
            continue
        old, new = item
        core = S - {1}
        old_deck = owners(core, old)
        new_deck = owners(core, new)
        if old_deck & atom_positive or new_deck & atom_negative:
            continue
        if any(old_deck & prior[2] or new_deck & prior[3] for prior in chosen):
            continue
        chosen.append((old, new, old_deck, new_deck))
    assert len(chosen) == 3

    leaves = {}
    for u in (2, 3, 4):
        for _ in range(1_000_000):
            item = candidate(rng)
            if item is None:
                continue
            old, new = item
            core = S - {u}
            if owners(core, new) & atom_positive:
                continue
            if owners(core, old) & atom_negative:
                continue
            leaves[u] = (old, new)
            break
        assert u in leaves

    # Exact two recoupled star shores.
    shore_minus = []  # old repeated core, new leaf cores; pairs with atom+
    shore_plus = []   # new repeated core, old leaf cores; pairs with atom-
    for old, new, _, _ in chosen:
        shore_minus.append(owners(S - {1}, old))
        shore_plus.append(owners(S - {1}, new))
    for u, (old, new) in leaves.items():
        shore_minus.append(owners(S - {u}, new))
        shore_plus.append(owners(S - {u}, old))

    assert all(len(bank) in (10, 11) for bank in shore_minus + shore_plus)
    assert sum(map(len, shore_minus)) == len(set().union(*shore_minus))
    assert sum(map(len, shore_plus)) == len(set().union(*shore_plus))
    assert not set().union(*shore_minus) & atom_positive
    assert not set().union(*shore_plus) & atom_negative

    result = {
        "status": "PASS",
        "attempts": attempts,
        "C0": sorted(C0),
        "C": sorted(C),
        "P": sorted(P),
        "H": sorted(H),
        "S": sorted(S),
        "z": Z,
        "E": list(E),
        "repeated_core": [
            {"old": list(old), "new": list(new)}
            for old, new, _, _ in chosen
        ],
        "leaves": {
            str(u): {"old": list(old), "new": list(new)}
            for u, (old, new) in leaves.items()
        },
        "shore_minus_owners": sum(map(len, shore_minus)),
        "shore_plus_owners": sum(map(len, shore_plus)),
        "atom_star_collisions": 0,
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
