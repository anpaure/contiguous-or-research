#!/usr/bin/env python3
"""Count slab-atlas atoms under one-period-(q+2)-rail-per-atom charging.

Substantial instances must run on h100.
"""

import argparse

import analyze_product_scd_fan_rectangle_hybrid_boundary as hybrid
import verify_product_scd_diagonal_slab_fan_atlas as base


def oriented_atoms(nrows, ncols, radius, depth, slab_height):
    rectangles = fans = boundary_fans = bases = 0
    x = 0
    while x < nrows:
        height = min(slab_height, nrows - x)
        width = depth + 2 - height
        y = 0
        full_rectangles = 0
        while (
            y + width <= ncols
            and radius - x - y >= height + width - 2
        ):
            rectangles += 1
            bases += 1
            y += width
            full_rectangles += 1

        local_radius = radius - x - y
        if local_radius >= 0 and y < ncols:
            if full_rectangles == 0:
                effective_radius = min(
                    radius - x, (nrows - x - 1) + (ncols - 1)
                )
                if effective_radius <= depth:
                    fan_a = min(nrows - x, radius - x + 1)
                    fan_b = min(ncols, radius - x + 1)
                    if fan_a > 0 and fan_b > 0:
                        fans += 1
                        bases += 1
                        if effective_radius == depth:
                            boundary_fans += 1
                    break
            fan_a = min(height, local_radius + 1)
            fan_b = min(ncols - y, local_radius + 1)
            if fan_a > 0 and fan_b > 0:
                fans += 1
                bases += 1
                effective_radius = min(local_radius, fan_a + fan_b - 2)
                if effective_radius == depth:
                    boundary_fans += 1
        x += height
    return rectangles, fans, boundary_fans, bases


def grid_atoms(a, b, radius, depth):
    # Match the hybrid script's exact cost/loss/fan tie-break, then return
    # the atom counts of that chosen orientation.
    candidates = []
    for height in range(1, depth + 2):
        p = hybrid.oriented_profile(a, b, radius, depth, height)
        candidates.append((p, oriented_atoms(a, b, radius, depth, height)))
        p = hybrid.oriented_profile(b, a, radius, depth, height)
        candidates.append((p, oriented_atoms(b, a, radius, depth, height)))
    return min(candidates, key=lambda z: (z[0][0], z[0][1], z[0][4]))


def grid_atoms_min_count(a, b, radius, depth):
    candidates = []
    for height in range(1, depth + 2):
        p = hybrid.oriented_profile(a, b, radius, depth, height)
        c = oriented_atoms(a, b, radius, depth, height)
        candidates.append((p, c))
        p = hybrid.oriented_profile(b, a, radius, depth, height)
        c = oriented_atoms(b, a, radius, depth, height)
        candidates.append((p, c))
    return min(
        candidates,
        key=lambda z: (z[1][0] + z[1][1], z[1][2], z[0][0]),
    )


def census(k):
    r, W, d = base.parameters(k)
    h = k // 2
    totals = [0, 0, 0, 0]
    source = lost = 0
    min_count_atoms = min_count_source = min_count_lost = 0
    for u, (a, ca) in enumerate(base.chain_types(h)):
        for v, (b, cb) in enumerate(base.chain_types(k - h)):
            radius = r - d - 1 - u - v
            if radius < 0:
                continue
            profile, counts = grid_atoms(a, b, radius, d)
            profile_mc, counts_mc = grid_atoms_min_count(a, b, radius, d)
            mult = ca * cb
            source += mult * profile[0]
            lost += mult * profile[1]
            for j, value in enumerate(counts):
                totals[j] += mult * value
            min_count_atoms += mult * (counts_mc[0] + counts_mc[1])
            min_count_source += mult * profile_mc[0]
            min_count_lost += mult * profile_mc[1]
    q = d + 1
    N = q + 2
    rectangles, fans, boundary_fans, bases = totals
    atoms = rectangles + fans
    return (
        r, W, d, source, lost, rectangles, fans, boundary_fans, bases,
        N * atoms, min_count_atoms, min_count_source, min_count_lost,
        N * min_count_atoms,
    )


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("k", nargs="+", type=int)
    args = ap.parse_args()
    for k in args.k:
        (
            r,
            W,
            d,
            source,
            lost,
            rectangles,
            fans,
            boundary_fans,
            bases,
            clock_charge,
            min_count_atoms,
            min_count_source,
            min_count_lost,
            min_count_clock_charge,
        ) = census(k)
        print(
            f"k={k} d={d} source/W={source/W:.12f} "
            f"rectangles/W={rectangles/W:.12f} fans/W={fans/W:.12f} "
            f"boundary-fans/W={boundary_fans/W:.12f} "
            f"bases/W={bases/W:.12f} lost/W={lost/W:.12f} "
            f"one-clock-per-atom/W={clock_charge/W:.12f} "
            f"min-count-atoms/W={min_count_atoms/W:.12f} "
            f"min-count-clock/W={min_count_clock_charge/W:.12f} "
            f"min-count-source/W={min_count_source/W:.12f} "
            f"min-count-lost/W={min_count_lost/W:.12f}",
            flush=True,
        )
