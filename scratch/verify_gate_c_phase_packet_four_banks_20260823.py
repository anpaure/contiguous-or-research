#!/usr/bin/env python3
"""Audit the 7/16 four-Catalan-bank phase-packet matching.

This extends the independently checked three-bank construction by the
second shifted primitive bank, with its unique zigzag root deleted.
"""

from verify_gate_c_phase_packet_three_banks_20260823 import (
    add_packet,
    catalan,
    dyck_words,
    mapped,
    path_data,
    primitive,
    construct as construct_three_banks,
)


def construct(b):
    k = b - 1
    a, p, q = 1, 2 * k, 2 * k + 1
    omega = frozenset(range(2 * k + 2))
    packets, owners = construct_three_banks(b)

    # Omit base coordinate 1 (zero-based) and cyclically order the remaining
    # ground coordinates as 2,...,2k-1,0,q.  Delete the unique primitive root
    # whose inner Dyck word is zigzag.
    order = tuple(range(2, 2 * k)) + (0, q)
    zigzag_inner = tuple(bit for _ in range(k - 1) for bit in (1, 0))
    added = 0
    for root in dyck_words(k):
        if not primitive(root) or root[1:-1] == zigzag_inner:
            continue
        states, uppers, adds, removes = path_data(root)
        assert adds[0] == 2 * k - 1
        sequence = (
            frozenset({p} | set(mapped(states[0], order))),
            *(mapped(upper, order) for upper in uppers),
            frozenset({p} | set(mapped(states[-1], order))),
        )
        add_packet(
            packets,
            owners,
            "B",
            root,
            sequence,
            (
                p,
                a,
                tuple(order[i] for i in removes),
                tuple(order[i] for i in adds),
            ),
            omega,
        )
        added += 1

    assert added == catalan(k - 1) - 1
    expected = catalan(b - 1) + 3 * catalan(b - 2) - 2
    assert len(packets) == expected
    assert len(owners) == (b + 1) * expected
    return packets, owners


def main():
    for b in range(3, 11):
        packets, owners = construct(b)
        expected = catalan(b - 1) + 3 * catalan(b - 2) - 2
        assert len(packets) == expected
        print(
            f"b={b}: packets={len(packets)}, vertices={len(owners)}, "
            f"fraction={len(packets) / catalan(b):.9f}"
        )
    print("PASS: four Catalan banks are labelled phase packets and disjoint")


if __name__ == "__main__":
    main()
