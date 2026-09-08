#!/usr/bin/env python3
"""Finite diagnostics for a four-column cyclic-variance Gate-B proof."""

from __future__ import annotations

import argparse
from fractions import Fraction

import numpy as np

from research_w2_hahn_venn_exact_20260822 import (
    coefficient_vectors,
    gram_entry,
    superset_sums,
)


def rotate_mask(mask: int, b: int, amount: int = 1) -> int:
    amount %= b
    full = (1 << b) - 1
    return ((mask << amount) | (mask >> (b - amount))) & full


def shifted_vector(masks: list[int], values: list[int], b: int) -> list[int]:
    lookup = {mask: value for mask, value in zip(masks, values)}
    # x'(B)=x(tau^{-1}B), where tau increments coordinate labels.
    return [lookup[rotate_mask(mask, b, -1)] for mask in masks]


def run(r: int) -> None:
    b, masks, coefficient = coefficient_vectors(r)
    meta = ((r, "c_m"), (r - 1, "c_l"), (r, "w_m"), (r - 1, "w_l"))
    differences: dict[str, list[int]] = {}
    transforms = {}
    for size, name in meta:
        shifted = shifted_vector(masks[size], coefficient[name], b)
        differences[name] = [x - y for x, y in zip(coefficient[name], shifted)]
        transforms[(name, "base")] = superset_sums(b, masks[size], coefficient[name])
        transforms[(name, "diff")] = superset_sums(b, masks[size], differences[name])

    for level in range(2, r - 1):
        base = np.zeros((4, 4), dtype=float)
        diff = np.zeros((4, 4), dtype=float)
        for i, (si, ni) in enumerate(meta):
            for j, (sj, nj) in enumerate(meta):
                base[i, j] = float(gram_entry(
                    b, si, sj, level,
                    transforms[(ni, "base")], transforms[(nj, "base")],
                ))
                diff[i, j] = float(gram_entry(
                    b, si, sj, level,
                    transforms[(ni, "diff")], transforms[(nj, "diff")],
                ))
        diagonal = np.diag(np.diag(base))
        normalized = np.diag(1 / np.sqrt(np.diag(base))) @ diff @ np.diag(
            1 / np.sqrt(np.diag(base))
        )
        eigen = np.linalg.eigvalsh(normalized)
        rank = np.linalg.matrix_rank(diff, tol=max(np.linalg.norm(diff), 1.0) * 1e-11)
        print(
            f"r={r} j={level} rank={rank} "
            f"eig={','.join(f'{x:.6g}' for x in eigen)}"
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("r", type=int)
    run(parser.parse_args().r)
