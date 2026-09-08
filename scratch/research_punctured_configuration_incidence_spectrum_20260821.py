#!/usr/bin/env python3
"""Exact-codegree normalized incidence spectrum for punctured configurations.

The target--configuration incidence matrix B is not materialized.  Its
Gram matrix BB^T is filled from the exact layer/intersection codegree table,
then normalized to a Markov Gram matrix.  Research diagnostic; substantive
instances belong on H100.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from itertools import combinations
from math import comb, factorial, sqrt

import numpy as np
from scipy.sparse.linalg import eigsh


def masks(n: int, k: int) -> list[int]:
    return [sum(1 << x for x in row) for row in combinations(range(n), k)]


def codegree(r: int, layer_a: int, layer_b: int, inter: int) -> int:
    c = 2 * r - 1
    if layer_a == 0 and layer_b == 0:
        if inter == r:
            return 2 * r * factorial(r) * factorial(r + 1)
        return 2 * c * factorial(r - inter) ** 2 * factorial(inter) * factorial(inter + 1)
    if layer_a == 1 and layer_b == 1:
        if inter == r - 1:
            return 2 * (r + 2) * factorial(r) * factorial(r + 1)
        if inter == 0:
            return 24 * c * factorial(r - 1) ** 2
        return 2 * c * factorial(r - 1 - inter) ** 2 * factorial(inter) * factorial(inter + 3)
    if layer_a > layer_b:
        layer_a, layer_b = layer_b, layer_a
    assert (layer_a, layer_b) == (0, 1)
    if inter == 0:
        return 6 * c * factorial(r) * factorial(r - 1)
    if inter == r - 1:
        return (4 * r - 1) * factorial(r - 1) * factorial(r + 1)
    return (
        2
        * c
        * factorial(r - inter)
        * factorial(r - 1 - inter)
        * factorial(inter)
        * factorial(inter + 2)
    )


def general_codegree(r: int, k: int, h: int, a: int) -> int:
    b = 2 * r + 1
    if a == 0:
        placements = b - k - h + 1
    elif a < min(k, h):
        placements = 2
    else:
        placements = abs(k - h) + 1
    positional = (b - 2) * placements + (1 if a == min(k, h) else 0)
    return (
        positional
        * factorial(a)
        * factorial(k - a)
        * factorial(h - a)
        * factorial(b - k - h + a)
    )


def specht_blocks(r: int) -> list[dict]:
    n = 2 * r + 1
    layers = (r, r - 1)
    degrees = {
        r: 2 * r * factorial(r) * factorial(r + 1),
        r - 1: 2 * (r + 2) * factorial(r) * factorial(r + 1),
    }
    result = []
    for j in range(r):
        raw = {}
        norms = {k: 2**j * comb(n - 2 * j, k - j) for k in layers}
        for k in layers:
            for h in layers:
                value = 0
                for q in range(j + 1):
                    sign_count = comb(j, q) * (-1 if (j - q) % 2 else 1)
                    for z in range(max(0, h - j - (n - k - j)), min(k - j, h - j) + 1):
                        count = comb(k - j, z) * comb(n - k - j, h - j - z)
                        value += sign_count * count * general_codegree(r, k, h, q + z)
                raw[k, h] = value
        block = np.empty((2, 2), dtype=np.float64)
        for row, k in enumerate(layers):
            for col, h in enumerate(layers):
                block[row, col] = (
                    raw[k, h]
                    * sqrt(norms[k] / norms[h])
                    / (4 * r * sqrt(degrees[k] * degrees[h]))
                )
        assert np.max(np.abs(block - block.T)) < 1e-8
        eig = np.linalg.eigvalsh(block)[::-1]
        result.append(
            {
                "j": j,
                "block": block.tolist(),
                "eigenvalues": eig.tolist(),
                "multiplicity": comb(n, j) - (comb(n, j - 1) if j else 0),
            }
        )
    return result


def audit(r: int, eigen_count: int) -> None:
    b = 2 * r + 1
    middle = masks(b, r)
    lower = masks(b, r - 1)
    vertices = [(0, x) for x in middle] + [(1, x) for x in lower]
    n = len(vertices)
    d_middle = 2 * r * factorial(r) * factorial(r + 1)
    d_lower = 2 * (r + 2) * factorial(r) * factorial(r + 1)
    degrees = np.array([d_middle if layer == 0 else d_lower for layer, _ in vertices], dtype=np.float64)
    gram = np.empty((n, n), dtype=np.float64)
    for i, (li, xi) in enumerate(vertices):
        gram[i, i] = degrees[i]
        for j in range(i):
            lj, xj = vertices[j]
            value = codegree(r, li, lj, (xi & xj).bit_count())
            gram[i, j] = gram[j, i] = value
    gram /= np.sqrt(degrees[:, None] * degrees[None, :])
    gram /= 4 * r
    values = eigsh(gram, k=min(eigen_count, n - 1), which="LA", return_eigenvectors=False)
    values = np.sort(values)[::-1]
    print(
        "PUNCTURED_CONFIG_INCIDENCE_SPECTRUM",
        {
            "r": r,
            "vertices": n,
            "top_normalized_gram_eigenvalues": [float(x) for x in values],
            "top_singular_values": [sqrt(max(0.0, float(x))) for x in values],
        },
        flush=True,
    )
    print("PUNCTURED_CONFIG_SPECHT_BLOCKS", {"r": r, "blocks": specht_blocks(r)}, flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--r", type=int, nargs="+", default=[2, 3, 4, 5, 6])
    parser.add_argument("--eigen-count", type=int, default=20)
    args = parser.parse_args()
    for value in args.r:
        audit(value, args.eigen_count)
