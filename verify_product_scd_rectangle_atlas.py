#!/usr/bin/env python3
"""Exact integer census for the product-SCD rectangle atlas.

The computation grows quickly.  In this project it is intended to run on
the remote h100 host, not on the local Mac.  It verifies equations (3.9),
(4.1)--(4.5), and the safe Type-1 boundary-fan cover of Section 6 in
MATH_THEOREM_PRODUCT_SCD_RECTANGLE_ATLAS_AND_COEFFICIENT_ONE_GATE_20260813.md.
"""

import math
import sys
from functools import lru_cache


def parameters(k: int):
    r = (k + 1) // 2
    width = math.comb(k, r)
    lower = sum(math.comb(k, s) for s in range(1, r))
    d = 0
    while d * width + d * (d + 1) // 2 < lower:
        d += 1
    return r, width, d


def chain_types(n: int):
    return [
        (n - 2 * u + 1,
         math.comb(n, u) - (math.comb(n, u - 1) if u else 0))
        for u in range(n // 2 + 1)
    ]


def active_interval(i, ncols, base, low, high):
    left = max(0, low - base - i)
    right = min(ncols - 1, high - base - i)
    return None if left > right else (left, right)


def interval_length(interval):
    return 0 if interval is None else interval[1] - interval[0] + 1


def intersection(first, second):
    if first is None or second is None:
        return None
    result = (max(first[0], second[0]), min(first[1], second[1]))
    return None if result[0] > result[1] else result


def one_axis_census(k: int, pair_larger_half: bool):
    r, width, d = parameters(k)
    low, high = d + 1, r - d - 1
    nx = (k + 1) // 2 if pair_larger_half else k // 2
    ny = k - nx
    x_types = chain_types(nx)
    y_types = chain_types(ny)

    @lru_cache(None)
    def row_guillotine(nrows, ncols, base):
        rows = []
        for i in range(nrows):
            interval = active_interval(i, ncols, base, low, high)
            if interval is not None:
                rows.append((i, interval[0], interval[1]))
        if not rows:
            return 0

        count = len(rows)
        dp = [10**100] * (count + 1)
        dp[0] = 0
        for end in range(1, count + 1):
            left, right = 10**9, -1
            for start in range(end, max(0, end - d), -1):
                _, row_left, row_right = rows[start - 1]
                left = min(left, row_left)
                right = max(right, row_right)
                height = rows[end - 1][0] - rows[start - 1][0] + 1
                if height > d:
                    continue
                hull_width = right - left + 1
                max_rectangle_width = d + 1 - height
                chunks = (hull_width + max_rectangle_width - 1) // max_rectangle_width
                slab_cost = hull_width + chunks * (height - 1)
                dp[end] = min(dp[end], dp[start - 1] + slab_cost)
        return dp[count]

    @lru_cache(None)
    def symmetric_guillotine(nrows, ncols, base):
        return min(
            row_guillotine(nrows, ncols, base),
            row_guillotine(ncols, nrows, base),
        )

    def paired_grid_cost(short_type, other_type):
        # Type short_type-1 is longer by two vertices than type short_type.
        long_rows = nx - 2 * (short_type - 1) + 1
        short_rows = nx - 2 * short_type + 1
        ncols = ny - 2 * other_type + 1
        long_base = short_type - 1 + other_type
        short_base = short_type + other_type
        independent = (
            symmetric_guillotine(long_rows, ncols, long_base)
            + symmetric_guillotine(short_rows, ncols, short_base)
        )
        if short_rows < 2:
            return independent

        paired = (
            symmetric_guillotine(long_rows - 2, ncols, long_base + 1)
            + symmetric_guillotine(short_rows - 2, ncols, short_base + 1)
        )
        for long_row, short_row in ((0, 0), (long_rows - 1, short_rows - 1)):
            long_active = active_interval(long_row, ncols, long_base, low, high)
            short_active = active_interval(short_row, ncols, short_base, low, high)
            shared_width = interval_length(intersection(long_active, short_active))
            paired += (
                interval_length(long_active)
                + interval_length(short_active)
                - 2 * shared_width
            )
            if shared_width:
                # Each common chunk has width at most d-1 and costs B+1.
                paired += shared_width + (shared_width + d - 2) // (d - 1)
        return min(independent, paired)

    independent_total = sum(
        x_count * y_count * symmetric_guillotine(x_length, y_length, u + v)
        for u, (x_length, x_count) in enumerate(x_types)
        for v, (y_length, y_count) in enumerate(y_types)
    )

    # Strong HC-SCP Type-1 block counts.  A chain can be used in one block.
    pair_counts = [0] * len(x_types)
    carry = 0
    for u in range(1, len(x_types)):
        pair_counts[u] = x_types[u - 1][1] - carry
        assert pair_counts[u] >= 0
        carry = pair_counts[u]

    used = [0] * len(x_types)
    for u in range(1, len(x_types)):
        used[u - 1] += pair_counts[u]
        used[u] += pair_counts[u]

    paired_total = 0
    for u in range(1, len(x_types)):
        for v, (_, y_count) in enumerate(y_types):
            paired_total += pair_counts[u] * y_count * paired_grid_cost(u, v)
    for u, (x_length, x_count) in enumerate(x_types):
        residue = x_count - used[u]
        assert residue >= 0
        for v, (y_length, y_count) in enumerate(y_types):
            paired_total += residue * y_count * symmetric_guillotine(
                x_length, y_length, u + v
            )
    return r, width, d, independent_total, paired_total


def census(k: int):
    small = one_axis_census(k, False)
    large = one_axis_census(k, True)
    assert small[:4] == large[:4]
    r, width, d, independent = small[:4]
    paired = min(small[4], large[4])
    return r, width, d, independent, paired


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit("usage: verify_product_scd_rectangle_atlas.py K [K ...]")
    for argument in sys.argv[1:]:
        k = int(argument)
        _, width, d, independent, paired = census(k)
        print(
            f"k={k} d={d} RG/W={independent / width:.10f} "
            f"PAIR/W={paired / width:.10f} "
            f"SAVING/W={(independent - paired) / width:.10f}",
            flush=True,
        )
