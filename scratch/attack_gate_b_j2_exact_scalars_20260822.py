#!/usr/bin/env python3
"""Exact j=2 scalar extraction for Gate-B formula discovery only."""

from __future__ import annotations

import argparse
from fractions import Fraction

from research_w2_hahn_venn_exact_20260822 import (
    coefficient_vectors,
    conditional_scalars,
    gram_entry,
    orbit_factor,
    residual_fraction,
    superset_sums,
)


def run(r: int) -> None:
    b, masks, coefficients = coefficient_vectors(r)
    metadata = (
        (r, "c_m"),
        (r - 1, "c_l"),
        (r, "w_m"),
        (r - 1, "w_l"),
        (r - 2, "q"),
    )
    transforms = {
        name: superset_sums(b, masks[size], coefficients[name])
        for size, name in metadata
    }
    level = 2
    gram = [[Fraction() for _ in range(5)] for _ in range(5)]
    for row, (left_size, left_name) in enumerate(metadata):
        for column, (right_size, right_name) in enumerate(metadata):
            gram[row][column] = gram_entry(
                b,
                left_size,
                right_size,
                level,
                transforms[left_name],
                transforms[right_name],
            )
    alpha = residual_fraction(gram)
    central, delta, xi = conditional_scalars(gram)
    theta = orbit_factor(r, level)
    assert alpha == central * xi / delta
    print(f"r={r}")
    print(f"alpha={alpha}")
    print(f"central={central}")
    print(f"delta={delta}")
    print(f"xi={xi}")
    print(f"theta={theta}")
    print(f"theta_xi={theta * xi}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("r", type=int)
    run(parser.parse_args().r)
