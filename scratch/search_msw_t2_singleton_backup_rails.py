#!/usr/bin/env python3
"""Search literal private backup rails for the singleton T2 residual.

The resident singleton construction has, after the forced Z seam backup,
exactly two nested ungraded loss families and one saturated loss:

  B | {p0} | (D0 union ... union Dk),       1 <= k < h,
  C | {p0} | (D0 union D-1 ... union D-k),  1 <= k < h,
  H | {p0,p1} | all clock coordinates.

This script searches for three owner paths that create those values while
avoiding every owner and used lower facet of the protected singleton T2
factor.  Heavy executions belong on h100 only.
"""

from collections import Counter
from itertools import combinations, permutations
import sys

import audit_msw_t2_singleton_a_clock as s
import audit_msw_t2_complete_ml13_cyclic as full


HBASE = s.base.bits("1000111011111")
BACKUP_HEAD = s.base.bits("0000111011110")


def dset(h, j):
    return sum(1 << ((j + k) % (2 * h)) for k in range(h))


def facets(target, rank):
    return [x for x in range(1 << 13)
            if x.bit_count() == rank and x & ~target == 0]


def resources(path):
    owners = set(path)
    lower = {
        (x[0] & y[0], x[1] & y[1], x[2] & y[2])
        for x, y in zip(path, path[1:])
    }
    if len(owners) != len(path) or len(lower) != len(path) - 1:
        return None
    for x, y in zip(path, path[1:]):
        assert sum((x[i] ^ y[i]).bit_count() for i in range(3)) == 2
    return owners, lower


def path_union(path):
    return tuple(
        __import__("functools").reduce(int.__or__, (x[i] for x in path), 0)
        for i in range(3)
    )


def bc_candidates(target, h, sign):
    """Use a noncanonical monotone clock staircase, then exchange base.

    Put P_k=D0 union ... union D_{sign*k}.  Two adjacent h-subsets K0,K1
    of P_1 have union P_1; subsequent K_k introduce the unique new clock
    coordinate of P_k.  Thus every prefix after the base exchange has the
    desired literal union, while no owner at the already-used payload D0
    is required.
    """
    fs = facets(target, 7)
    out = []
    reflect = lambda x: (h - 1 - x) % (2 * h) if sign < 0 else x
    p1 = {reflect(x) for x in range(h + 1)}
    k0 = p1 - {reflect(0)}             # canonical D_{sign}
    k1 = p1 - {reflect(1)}             # noncanonical for every h >= 2
    masks = [sum(1 << x for x in k0), sum(1 << x for x in k1)]
    current = set(k1)
    for k in range(2, h):
        current.remove(reflect(k))
        current.add(reflect(h + k - 1))
        masks.append(sum(1 << x for x in current))
    for x, y in permutations(fs, 2):
        assert (x ^ y).bit_count() == 2
        path = [(x, 1, masks[0]), (x, 1, masks[1])]
        path += [(y, 1, masks[1])]
        path += [(y, 1, masks[j]) for j in range(2, h)]
        ro = resources(path)
        if ro is None:
            continue
        # Every successive prefix creates the required nested value.
        for k in range(1, h):
            got = path_union(path[:k + 2])
            want_clock = 0
            for j in range(k + 1):
                want_clock |= dset(h, sign * j)
            assert got == (target, 1, want_clock)
        out.append((path, ro, (x, y)))
    return out


def h_candidates(h):
    """Clock once, take two base exchanges and a tag exchange, then sweep."""
    fs = facets(HBASE, 7)
    out = []
    for x0, x1, x2 in permutations(fs, 3):
        if (x0 ^ x1).bit_count() != 2 or (x1 ^ x2).bit_count() != 2:
            continue
        if x0 | x1 | x2 != HBASE:
            continue
        path = [
            (x0, 1, dset(h, 0)),
            (x0, 1, dset(h, 1)),
            (x1, 1, dset(h, 1)),
            (x2, 1, dset(h, 1)),
            (x2, 2, dset(h, 1)),
        ]
        path += [(x2, 2, dset(h, j)) for j in range(2, h + 2)]
        assert path_union(path) == (HBASE, 3, (1 << (2 * h)) - 1)
        ro = resources(path)
        if ro is None:
            continue
        out.append((path, ro, (x0, x1, x2)))
    return out


def disjoint(candidate, forbidden_owners, forbidden_lower):
    owners, lower = candidate[1]
    return not (owners & forbidden_owners or lower & forbidden_lower)


def exposure(paths):
    owners = set()
    lower = set()
    for path in paths:
        ro = resources(path)
        assert ro is not None
        owners |= ro[0]
        lower |= ro[1]
    alpha = 0
    for facet in lower:
        alpha = max(alpha, sum(
            all((facet[i] & owner[i]) == facet[i] for i in range(3))
            for owner in owners
        ))
    beta = 0
    for owner in owners:
        beta = max(beta, sum(
            all((facet[i] & owner[i]) == facet[i] for i in range(3))
            for facet in lower
        ))
    return alpha, beta


def describe(label, row, h):
    path, (owners, lower), bases = row
    print(label, "length", len(path), "bases",
          [full.word(x) for x in bases],
          "owner_count", len(owners), "lower_count", len(lower),
          "union", full.word(path_union(path)[0]),
          format(path_union(path)[1], "03b")[::-1],
          format(path_union(path)[2], f"0{2*h}b")[::-1])
    for i, x in enumerate(path):
        print(" ", label, "OWNER", i, full.word(x[0]),
              format(x[1], "03b")[::-1],
              format(x[2], f"0{2*h}b")[::-1])


def main():
    hmax = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    old_orders, new_orders, sold, snew = s.reconstruct()
    owners = set(sold)
    tag, p = s.quotient_and_coloring(
        owners, sold, snew, (BACKUP_HEAD,)
    )
    assert p == 3
    for h in range(2, hmax + 1):
        main_cycles = s.expand_orders(new_orders, snew, tag, h)
        main_palette = s.palettes(main_cycles)
        forbidden_owners = set(main_palette[0])
        forbidden_lower = set(main_palette[1])

        banks = [
            ("B", bc_candidates(s.base.bits("1011110011010"), h, +1)),
            ("C", bc_candidates(s.base.bits("1010111011010"), h, -1)),
            ("H", h_candidates(h)),
        ]
        clean = []
        for label, rows in banks:
            rows = [r for r in rows
                    if disjoint(r, forbidden_owners, forbidden_lower)]
            print("CANDIDATES", "h", h, label, len(rows))
            clean.append((label, rows))

        solution = None
        for b in clean[0][1]:
            bo, bl = b[1]
            for c in clean[1][1]:
                co, cl = c[1]
                if bo & co or bl & cl:
                    continue
                used_o = forbidden_owners | bo | co
                used_l = forbidden_lower | bl | cl
                for hh in clean[2][1]:
                    if disjoint(hh, used_o, used_l):
                        solution = (b, c, hh)
                        break
                if solution:
                    break
            if solution:
                break
        print("BACKUP_RAIL_SOLUTION", "h", h, int(solution is not None))
        if not solution:
            continue
        all_owners = set().union(*(x[1][0] for x in solution))
        all_lower = set().union(*(x[1][1] for x in solution))
        print("BACKUP_RAIL_COUNTS", "h", h,
              "owners", len(all_owners), "lower", len(all_lower),
              "exposure", exposure([x[0] for x in solution]),
              "main_owner_collision", len(all_owners & forbidden_owners),
              "main_lower_collision", len(all_lower & forbidden_lower))
        if h in (2, hmax):
            for (label, _), row in zip(clean, solution):
                describe(label, row, h)


if __name__ == "__main__":
    main()
