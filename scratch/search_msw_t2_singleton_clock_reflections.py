#!/usr/bin/env python3
"""Search clock-coordinate reflections in the forced-Z singleton T2 clock.

Compares ungraded literal union support.  Heavy runs belong on h100 only.
"""

from collections import Counter
from itertools import combinations
import sys

import audit_msw_t2_singleton_a_clock as s
import audit_msw_t2_complete_ml13_cyclic as full


NEIGHBOURS = (s.B, s.C, s.D, s.E)


def ungraded(cycles):
    out = set()
    witness = {}
    for cid, cycle in enumerate(cycles):
        ell = len(cycle)
        for i in range(ell):
            bo = to = co = 0
            for width in range(1, ell + 1):
                x = cycle[(i + width - 1) % ell]
                bo |= x[0]
                to |= x[1]
                co |= x[2]
                key = (bo, to, co)
                out.add(key)
                witness.setdefault(key, (cid, i, width, ell, x[4]))
    return out, witness


def main():
    hmax = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    old_orders, new_orders, sold, snew = s.reconstruct()
    owners = set(sold)
    backup_head = s.base.bits("0000111011110")
    tag, p = s.quotient_and_coloring(owners, sold, snew, (backup_head,))
    print("neighbour_order", [full.word(v) for v in NEIGHBOURS])

    affected = set()
    for v in (s.A, *NEIGHBOURS):
        # The affected occurrence bank is the 65-owner connected component
        # of the union of old/new successors containing a.
        pass
    stack = [s.A]
    pred_old = {w: v for v, w in sold.items()}
    pred_new = {w: v for v, w in snew.items()}
    while stack:
        v = stack.pop()
        if v in affected:
            continue
        affected.add(v)
        stack.extend((sold[v], snew[v], pred_old[v], pred_new[v]))
    print("affected_union_component_size", len(affected))

    for h in range(2, hmax + 1):
        rows = []
        for mask in range(16):
            reflected = {
                NEIGHBOURS[j] for j in range(4) if (mask >> j) & 1
            }
            old_cycles = s.expand_orders(
                old_orders, sold, tag, h, reflected
            )
            new_cycles = s.expand_orders(
                new_orders, snew, tag, h, reflected
            )
            old, ow = ungraded(old_cycles)
            new, nw = ungraded(new_cycles)
            loss = old - new
            birth = new - old
            po = s.palettes(old_cycles)
            pn = s.palettes(new_cycles)
            rmin, _ = s.run_minima(new_cycles, p, h)
            rows.append((len(loss), mask, len(old), len(new), len(birth),
                         tuple(max(c.values()) for c in po),
                         tuple(max(c.values()) for c in pn), rmin,
                         loss, ow))
        rows.sort(key=lambda z: (z[0], z[1]))
        print("REFLECTION_SEARCH h", h)
        for row in rows:
            print(
                " mask", row[1],
                "loss", row[0], "birth", row[4],
                "old", row[2], "new", row[3],
                "palette_old", row[5], "palette_new", row[6],
                "run_min", row[7],
            )
        best = rows[0]
        for key in sorted(best[8], key=lambda z: (z[0], z[1], z[2])):
            print(
                " BEST_UNGRADED_LOSS",
                "h", h, "mask", best[1],
                "base", full.word(key[0]),
                "base_rank", key[0].bit_count(),
                "tags", format(key[1], f"0{p}b")[::-1],
                "clock", format(key[2], f"0{2*h}b")[::-1],
                "old", best[9][key],
            )

        for label, reflected in (
            ("affected_all", affected - {s.A}),
            ("affected_all_complement", set(sold) - affected),
            ("global_all", set(sold) - {s.A}),
        ):
            oc = s.expand_orders(old_orders, sold, tag, h, reflected)
            nc = s.expand_orders(new_orders, snew, tag, h, reflected)
            os, ow = ungraded(oc)
            ns, nw = ungraded(nc)
            rmin, _ = s.run_minima(nc, p, h)
            print(
                " DOMAIN_REFLECTION", label,
                "size", len(reflected),
                "loss", len(os - ns), "birth", len(ns - os),
                "run_min", rmin,
            )


if __name__ == "__main__":
    main()
