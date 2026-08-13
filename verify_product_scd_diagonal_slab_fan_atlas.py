#!/usr/bin/env python3
"""Exact-integer census for the diagonal slab-fan atlas.

Run substantial parameter lists on the remote h100 host.  This script is a
replay of equations (5.1)--(5.9) in the accompanying theorem.
"""

import math
import sys


def parameters(k):
    r = (k + 1) // 2
    width = math.comb(k, r)
    lower = sum(math.comb(k, s) for s in range(1, r))
    d = 0
    while d * width + d * (d + 1) // 2 < lower:
        d += 1
    return r, width, d


def chain_types(n):
    return [
        (n - 2 * u + 1,
         math.comb(n, u) - (math.comb(n, u - 1) if u else 0))
        for u in range(n // 2 + 1)
    ]


def oriented_cost(nrows, ncols, radius, depth, slab_height):
    cost = 0
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
            y += width
            full_rectangles += 1

        local_radius = radius - x - y
        if local_radius >= 0 and y < ncols:
            if full_rectangles == 0:
                effective_radius = min(
                    radius - x, (nrows - x - 1) + (ncols - 1)
                )
                if effective_radius <= depth:
                    cost += (
                        min(nrows - x, radius - x + 1)
                        + min(ncols, radius - x + 1)
                        - 1
                    )
                    break
            cost += (
                min(height, local_radius + 1)
                + min(ncols - y, local_radius + 1)
                - 1
            )
        x += height
    return cost


def grid_cost(nrows, ncols, radius, depth):
    return min(
        [
            oriented_cost(nrows, ncols, radius, depth, height)
            for height in range(1, depth + 2)
        ]
        + [
            oriented_cost(ncols, nrows, radius, depth, height)
            for height in range(1, depth + 2)
        ]
    )


def census(k):
    r, width, d = parameters(k)
    h = k // 2
    total = 0
    for u, (a, count_a) in enumerate(chain_types(h)):
        for v, (b, count_b) in enumerate(chain_types(k - h)):
            radius = r - d - 1 - u - v
            if radius >= 0:
                total += count_a * count_b * grid_cost(a, b, radius, d)
    return width, d, total


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit(
            "usage: verify_product_scd_diagonal_slab_fan_atlas.py K [K ...]"
        )
    for argument in sys.argv[1:]:
        k = int(argument)
        width, d, total = census(k)
        print(f"k={k} d={d} SF/W={total / width:.10f}", flush=True)
