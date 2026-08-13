#!/usr/bin/env python3
"""Exact-integer census for the product-SCD antidiagonal-strip atlas.

Substantial parameter lists should be run on the remote h100 host.  The
per-grid cost is the literal central antidiagonal word plus two boundary
fans for each rank strip; no sharing between the three words is charged.
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
        (
            n - 2 * u + 1,
            math.comb(n, u) - (math.comb(n, u - 1) if u else 0),
        )
        for u in range(n // 2 + 1)
    ]


def diagonal_length(a, b, q):
    """Number of cells (i,j) in [0,a)x[0,b) with i+j=q."""
    left = max(0, q - (b - 1))
    right = min(a - 1, q)
    return max(0, right - left + 1)


def fan_cost(a, b, radius):
    """Cost of the exact diagonal fan on a truncated product downset."""
    if a <= 0 or b <= 0 or radius < 0:
        return 0
    return min(a, radius + 1) + min(b, radius + 1) - 1


def oriented_slab_cost(nrows, ncols, radius, depth, slab_height):
    """The exact slab-fan recurrence from the diagonal-fan atlas."""
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


def slab_cost(a, b, radius, depth):
    if a <= 0 or b <= 0 or radius < 0:
        return 0
    return min(
        [
            oriented_slab_cost(a, b, radius, depth, height)
            for height in range(1, depth + 2)
        ]
        + [
            oriented_slab_cost(b, a, radius, depth, height)
            for height in range(1, depth + 2)
        ]
    )


def strip_cost(a, b, lower, upper, depth):
    """Cover local diagonal band lower <= i+j <= upper.

    Each depth-wide strip begins at q.  Its central antidiagonal word has
    one letter per cell of local rank q.  The two missing axis triangles
    are covered by fans rooted at (q+1,0) and (0,q+1).
    """
    if a <= 0 or b <= 0 or depth <= 0:
        return 0
    lower = max(0, lower)
    upper = min(upper, a + b - 2)
    if lower > upper:
        return 0

    total = 0
    q = lower
    while q <= upper:
        thickness = min(depth, upper - q + 1)
        total += diagonal_length(a, b, q)

        # A boundary target has local offset radius at most thickness-2.
        if thickness >= 2:
            total += fan_cost(a - q - 1, b, thickness - 2)
            total += fan_cost(a, b - q - 1, thickness - 2)
        q += depth
    return total


def phased_strip_cost(a, b, lower, upper, depth):
    """Best legal phase for the depth-wide strip partition."""
    lower = max(0, lower)
    upper = min(upper, a + b - 2)
    if lower > upper:
        return 0
    first_min = max(0, lower - depth + 1)
    best = None
    for first in range(first_min, lower + 1):
        value = strip_cost(a, b, first, upper, depth)
        if best is None or value < best:
            best = value
    return best


def verify_small(max_dimension=14, max_depth=8):
    """Literal cell-level verification of every boundary-complete strip."""
    for a in range(1, max_dimension + 1):
        for b in range(1, max_dimension + 1):
            for depth in range(1, max_depth + 1):
                for q in range(a + b - 1):
                    for thickness in range(
                        1, min(depth, a + b - 1 - q) + 1
                    ):
                        target = {
                            (i, j)
                            for i in range(a)
                            for j in range(b)
                            if q <= i + j <= q + thickness - 1
                        }

                        left = max(0, q - (b - 1))
                        right = min(a - 1, q)
                        covered = {
                            (y, q - x)
                            for x in range(left, right + 1)
                            for y in range(x, right + 1)
                            if y - x + 1 <= thickness
                        }

                        if thickness >= 2:
                            covered |= {
                                (q + 1 + i, j)
                                for i in range(max(0, a - q - 1))
                                for j in range(b)
                                if i + j <= thickness - 2
                            }
                            covered |= {
                                (i, q + 1 + j)
                                for i in range(a)
                                for j in range(max(0, b - q - 1))
                                if i + j <= thickness - 2
                            }
                        assert target <= covered, (a, b, depth, q, thickness)
    print("PASS_SMALL_STRIP_COVER", flush=True)


def strip_core_ribbon_cost(a, b, lower, upper, depth):
    """Central strip words plus two global boundary-ribbon atlases.

    If a cell in a depth-wide rank block is not covered by its central
    antidiagonal word, one coordinate is at most depth-2.  Hence two
    width-(depth-1) product ribbons contain the entire remainder.
    """
    if a <= 0 or b <= 0 or depth <= 0:
        return 0
    lower = max(0, lower)
    upper = min(upper, a + b - 2)
    if lower > upper:
        return 0

    central = 0
    q = lower
    while q <= upper:
        central += diagonal_length(a, b, q)
        q += depth

    ribbon = max(0, depth - 1)
    return (
        central
        + slab_cost(a, min(b, ribbon), upper, depth)
        + slab_cost(min(a, ribbon), b, upper, depth)
    )


def census(k):
    r, width, d = parameters(k)
    h = k // 2
    total = 0
    phased_total = 0
    ribbon_total = 0
    central = 0
    source_rank_letters = 0
    source_rank_owner_windows = 0
    for u, (a, count_a) in enumerate(chain_types(h)):
        for v, (b, count_b) in enumerate(chain_types(k - h)):
            lower = d + 1 - u - v
            upper = r - d - 1 - u - v
            multiplicity = count_a * count_b
            total += multiplicity * strip_cost(a, b, lower, upper, d)
            phased_total += multiplicity * phased_strip_cost(
                a, b, lower, upper, d
            )
            ribbon_total += multiplicity * strip_core_ribbon_cost(
                a, b, lower, upper, d
            )

            q = max(0, lower)
            upper_clipped = min(upper, a + b - 2)
            while q <= upper_clipped:
                central += multiplicity * diagonal_length(a, b, q)
                q += d


            source_q = r - d - u - v
            source_length = diagonal_length(a, b, source_q)
            source_rank_letters += multiplicity * source_length
            source_rank_owner_windows += multiplicity * max(
                0, source_length - d
            )
    assert source_rank_letters == math.comb(k, r - d)
    return (
        width,
        d,
        total,
        phased_total,
        ribbon_total,
        central,
        source_rank_letters,
        source_rank_owner_windows,
    )


if __name__ == "__main__":
    if "--self-test" in sys.argv:
        verify_small()
        sys.argv.remove("--self-test")
    if len(sys.argv) < 2:
        raise SystemExit(
            "usage: verify_product_scd_antidiagonal_strip_atlas.py K [K ...]"
        )
    for argument in sys.argv[1:]:
        k = int(argument)
        (
            width,
            d,
            total,
            phased_total,
            ribbon_total,
            central,
            source_rank_letters,
            source_rank_owner_windows,
        ) = census(k)
        print(
            f"k={k} d={d} ADS/W={total / width:.10f} "
            f"phased/W={phased_total / width:.10f} "
            f"ADS+ribbon/W={ribbon_total / width:.10f} "
            f"central/W={central / width:.10f} "
            f"rank(R-d)/W={source_rank_letters / width:.10f} "
            f"owner-windows/W={source_rank_owner_windows / width:.10f}",
            flush=True,
        )
