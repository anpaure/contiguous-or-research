#!/usr/bin/env python3
"""Exact k17-boundary insertion search against the q4 V13 atom.

The reduced atom uses labels 0..12, leaving no fresh marker at k=17 after
the four-label common core is restored.  Enumerate every period-10 cyclic
word in which 2,3,4 are consecutive, insert 1 immediately before that
triple, and test the two cross-shore collision conditions needed by the
positive common-reserve recoupling.
"""

import itertools
import json
import sys

sys.path.insert(0, "scratch")
from verify_q4_v13_seven_by_seven_atom_20260814 import BASE, EXTRA, deck


def owner_set(rails, sign):
    return {
        owner
        for _, rail_sign, center, order in rails
        if rail_sign == sign
        for owner in deck(center, order)
    }


def main():
    atom_positive = owner_set(BASE + EXTRA, 1)
    atom_negative = owner_set(BASE + EXTRA, -1)
    target = frozenset(range(5))
    assert target in atom_positive and target not in atom_negative

    tested = 0
    old_safe = 0
    both_safe = 0
    witnesses = []
    auxiliary = tuple(range(5, 13))
    for omitted in auxiliary:
        retained = tuple(x for x in auxiliary if x != omitted)
        for triple in itertools.permutations((2, 3, 4)):
            for tail in itertools.permutations(retained):
                tested += 1
                old = triple + tail
                old_deck = set(deck(0, old))
                if old_deck & atom_positive:
                    continue
                old_safe += 1
                new = (1,) + old
                new_deck = set(deck(0, new))
                assert target in new_deck
                if new_deck & atom_negative:
                    continue
                both_safe += 1
                if len(witnesses) < 20:
                    witnesses.append({
                        "omitted": omitted,
                        "old": old,
                        "new": new,
                        "old_atom_positive_intersection": 0,
                        "new_atom_negative_intersection": 0,
                    })

    result = {
        "status": "PASS",
        "tested": tested,
        "old_safe": old_safe,
        "both_safe": both_safe,
        "witnesses": witnesses,
    }
    print(json.dumps(result, indent=2))
    if not witnesses:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
