#!/usr/bin/env python3
"""Exact boundary-loss census for rectangle-replacing slab-fan words.

Substantial instances belong on h100.
"""

import argparse
import math
from collections import Counter

import verify_product_scd_diagonal_slab_fan_atlas as base


def outer_diagonal_count(a, b, depth):
    """Cells (i,j) in [0,a)x[0,b) on i+j=depth."""
    lo = max(0, depth - (b - 1))
    hi = min(a - 1, depth)
    total = max(0, hi - lo + 1)
    axes = 0
    if depth < a:
        axes += 1
    if depth < b:
        axes += 1
    return total, max(0, total - axes), axes


def oriented_profile(nrows, ncols, radius, depth, slab_height):
    cost = 0
    lost = mixed = axes = fan_count = boundary_fans = 0
    lost_roots = Counter()
    owner_window_roots = Counter()
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
            cost += height + width - 1
            owner_window_roots[x + y] += max(
                0, height + width - 1 - (depth + 1) + 1
            )
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
                    cost += fan_a + fan_b - 1
                    owner_window_roots[x] += max(
                        0, fan_a + fan_b - 1 - (depth + 1) + 1
                    )
                    fan_count += 1
                    if effective_radius == depth:
                        t, m, z = outer_diagonal_count(
                            fan_a, fan_b, depth
                        )
                        lost += t
                        mixed += m
                        axes += z
                        if t:
                            boundary_fans += 1
                            lost_roots[x] += t
                    break
            fan_a = min(height, local_radius + 1)
            fan_b = min(ncols - y, local_radius + 1)
            cost += fan_a + fan_b - 1
            owner_window_roots[x + y] += max(
                0, fan_a + fan_b - 1 - (depth + 1) + 1
            )
            fan_count += 1
            effective_radius = min(local_radius, fan_a + fan_b - 2)
            if effective_radius == depth:
                t, m, z = outer_diagonal_count(fan_a, fan_b, depth)
                lost += t
                mixed += m
                axes += z
                if t:
                    boundary_fans += 1
                    lost_roots[x + y] += t
        x += height
    return (
        cost,
        lost,
        mixed,
        axes,
        fan_count,
        boundary_fans,
        lost_roots,
        owner_window_roots,
    )


def grid_profile(a, b, radius, depth):
    candidates = []
    for height in range(1, depth + 2):
        candidates.append(
            oriented_profile(a, b, radius, depth, height)
        )
        candidates.append(
            oriented_profile(b, a, radius, depth, height)
        )
    # Among source-cost minimizers choose the fewest lost cells, then fans.
    return min(candidates, key=lambda x: (x[0], x[1], x[4]))


def census(k):
    r, width, d = base.parameters(k)
    h = k // 2
    totals = [0] * 6
    rank_hist = Counter()
    owner_base_rank_hist = Counter()
    boundary_diagonal_targets = 0
    type_count = 0
    for u, (a, ca) in enumerate(base.chain_types(h)):
        for v, (b, cb) in enumerate(base.chain_types(k - h)):
            radius = r - d - 1 - u - v
            if radius < 0:
                continue
            profile = grid_profile(a, b, radius, d)
            mult = ca * cb
            for j, value in enumerate(profile[:6]):
                totals[j] += mult * value
            if profile[1]:
                type_count += 1
                for root_sum, value in profile[6].items():
                    rank_hist[u + v + root_sum + d] += mult * value
            for root_sum, value in profile[7].items():
                owner_base_rank_hist[u + v + root_sum] += mult * value
            target_local_rank = r - d - u - v
            boundary_diagonal_targets += (
                mult * outer_diagonal_count(a, b, target_local_rank)[0]
            )
    return (
        r,
        width,
        d,
        totals,
        type_count,
        rank_hist,
        boundary_diagonal_targets,
        owner_base_rank_hist,
    )


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("k", nargs="+", type=int)
    args = ap.parse_args()
    for k in args.k:
        (
            r,
            width,
            d,
            values,
            types,
            rank_hist,
            boundary_diagonal_targets,
            owner_base_rank_hist,
        ) = census(k)
        cost, lost, mixed, axes, fans, boundary_fans = values
        print(
            f"k={k} d={d} source/W={cost/width:.12f} "
            f"lost/W={lost/width:.12f} mixed/W={mixed/width:.12f} "
            f"axes/W={axes/width:.12f} fanWords/W={fans/width:.12f} "
            f"boundaryFanWords/W={boundary_fans/width:.12f} "
            f"repair-singletons/W={(cost+lost)/width:.12f} "
            f"whole-rank(R-d)/W={boundary_diagonal_targets/width:.12f} "
            f"violating-types={types}",
            flush=True,
        )
        compatible_base = r - d
        compatible = owner_base_rank_hist[compatible_base]
        all_owner_windows = sum(owner_base_rank_hist.values())
        print(
            f"  internal-q-windows/W={all_owner_windows/width:.12f} "
            f"compatible-base-rank-{compatible_base}/W={compatible/width:.12f} "
            f"base-rank-range={min(owner_base_rank_hist, default=None)}.."
            f"{max(owner_base_rank_hist, default=None)}",
            flush=True,
        )
        print(
            "  lost-ranks",
            [(rank, value / width) for rank, value in sorted(rank_hist.items())],
            flush=True,
        )
