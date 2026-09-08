#!/usr/bin/env python3
"""Exact finite costs for GK selection constrained to cyclic-rotation diagonals."""

from __future__ import annotations

import argparse
import itertools
import math


def rot(s: frozenset[int], t: int, b: int) -> frozenset[int]:
    return frozenset((x + t) % b for x in s)


def orbits(b: int, size: int) -> list[list[frozenset[int]]]:
    unseen = {frozenset(c) for c in itertools.combinations(range(b), size)}
    ans = []
    while unseen:
        base = min(unseen, key=lambda z: tuple(sorted(z)))
        orb = [rot(base, t, b) for t in range(b)]
        # For prime b and 0<size<b every orbit is free.
        assert len(set(orb)) == b
        for z in orb:
            unseen.remove(z)
        ans.append(orb)
    return ans


def top_excess(x: frozenset[int], y: frozenset[int], b: int) -> int:
    height = 0
    minimum = 0
    for i in range(b):
        for bit in (i in x, i in y):
            height += 1 if bit else -1
            minimum = min(minimum, height)
    assert height == 0
    return -minimum


def audit(b: int, r: int, h: int) -> dict[str, int | float]:
    xo = orbits(b, r)
    yo = orbits(b, b - r)
    assert len(xo) == len(yo)
    nsub = math.comb(b, r)
    dsplit = abs(2 * r - b)
    nphase = max(0, (b - dsplit - h + 2) // 2)

    full = 0
    unconstrained_kept = 0
    diagonal_kept = 0
    min_diag_values = []
    worst_block_deleted = 0
    worst_block_by_orientation = {0: 0, 1: 0}
    for xs in xo:
        for ys in yo:
            entries = []
            diagonal = []
            for delta in range(b):
                vals = [
                    min(top_excess(xs[i], ys[(i + delta) % b], b), h)
                    for i in range(b)
                ]
                parity = top_excess(xs[0], ys[delta], b) & 1
                assert all((top_excess(xs[i], ys[(i + delta) % b], b) & 1) == parity for i in range(b))
                entries.extend((parity, v) for v in vals)
                diagonal.append((parity, sum(vals)))
            full += sum(v for _, v in entries)
            for parity in (0, 1):
                edge_vals = sorted((v for p, v in entries if p == parity), reverse=True)
                diagonal_vals = sorted((v for p, v in diagonal if p == parity), reverse=True)
                unconstrained_kept += sum(edge_vals[: nphase * b])
                diagonal_kept += sum(diagonal_vals[:nphase])
                if diagonal_vals and len(diagonal_vals) > nphase:
                    deleted_here = diagonal_vals[nphase:]
                    min_diag_values.extend(deleted_here)
                    worst_block_by_orientation[parity] = max(
                        worst_block_by_orientation[parity], sum(deleted_here)
                    )
            worst_block_deleted = max(
                worst_block_deleted,
                sum(v for p, v in diagonal)
                - sum(
                    sum(sorted((v for pp, v in diagonal if pp == p), reverse=True)[:nphase])
                    for p in (0, 1)
                ),
            )

    lsplit = nsub * nsub
    return {
        "b": b,
        "r": r,
        "h": h,
        "N": nsub,
        "orbits": len(xo),
        "nphase": nphase,
        "full": full,
        "unconstrained_deficit": full - unconstrained_kept,
        "diagonal_deficit": full - diagonal_kept,
        "extra_diagonal_cost": unconstrained_kept - diagonal_kept,
        "diag_deficit_over_Lr": (full - diagonal_kept) / lsplit,
        "extra_over_Lr": (unconstrained_kept - diagonal_kept) / lsplit,
        "deleted_diag_mean": (sum(min_diag_values) / len(min_diag_values) if min_diag_values else 0),
        "worst_block_deleted": worst_block_deleted,
        "worst_block_by_orientation": worst_block_by_orientation,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--b", type=int, nargs="+", default=[5, 7, 11, 13])
    parser.add_argument("--h", type=int, default=0, help="0 chooses floor(sqrt(b))")
    args = parser.parse_args()
    for b in args.b:
        h = args.h or max(1, math.isqrt(b))
        r = (b - 1) // 2
        print(audit(b, r, h))


if __name__ == "__main__":
    main()
