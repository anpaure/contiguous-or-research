#!/usr/bin/env python3
"""Finite audit for the five-Catalan-bank phase-packet matching.

The first four banks are the audited 7/16 construction.  The fifth bank
uses omitted base coordinate 2 (zero based), repeated coordinate p, cyclic
ground (3,...,2k-1,0,1,q), and primitive roots not ending in 1000 or 0100.
"""

from verify_gate_c_phase_packet_four_banks_20260823 import (
    construct as construct_four_banks,
)
from verify_gate_c_phase_packet_three_banks_20260823 import (
    add_packet,
    catalan,
    dyck_words,
    mapped,
    path_data,
    primitive,
)


def construct(b):
    assert b >= 5
    k = b - 1
    p, q = 2 * k, 2 * k + 1
    omega = frozenset(range(2 * k + 2))
    packets, owners = construct_four_banks(b)

    # Omit base coordinate 2 and cyclically order the remaining ground as
    # 3,...,2k-1,0,1,q.  For a primitive root q is added first and ground
    # coordinate 3 is removed last.
    order = tuple(range(3, 2 * k)) + (0, 1, q)
    forbidden_suffixes = {(1, 0, 0, 0), (0, 1, 0, 0)}
    added = 0
    excluded = 0
    for root in dyck_words(k):
        if not primitive(root):
            continue
        if root[-4:] in forbidden_suffixes:
            excluded += 1
            continue
        states, uppers, adds, removes = path_data(root)
        assert adds[0] == 2 * k - 1
        assert removes[-1] == 0
        sequence = (
            frozenset({p} | set(mapped(states[0], order))),
            *(mapped(upper, order) for upper in uppers),
            frozenset({p} | set(mapped(states[-1], order))),
        )
        add_packet(
            packets,
            owners,
            "C",
            root,
            sequence,
            (
                p,
                2,
                tuple(order[i] for i in removes),
                tuple(order[i] for i in adds),
            ),
            omega,
        )
        added += 1

    assert excluded == 2 * catalan(k - 2)
    assert added == catalan(k - 1) - 2 * catalan(k - 2)
    expected = (
        catalan(b - 1)
        + 4 * catalan(b - 2)
        - 2 * catalan(b - 3)
        - 2
    )
    assert len(packets) == expected
    assert len(owners) == (b + 1) * expected
    return packets, owners


def main():
    for b in range(5, 12):
        packets, owners = construct(b)
        expected = (
            catalan(b - 1)
            + 4 * catalan(b - 2)
            - 2 * catalan(b - 3)
            - 2
        )
        print(
            f"b={b}: packets={len(packets)}, vertices={len(owners)}, "
            f"fraction={len(packets) / catalan(b):.9f}"
        )
        assert len(packets) == expected
    print("PASS: five Catalan banks are labelled phase packets and disjoint")


if __name__ == "__main__":
    main()
