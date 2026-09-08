"""Independent Fraction/Boole-rule checks of the integer integral certificate."""

import argparse
from fractions import Fraction as F
from itertools import product
import json
from math import isqrt
import subprocess

from cross_hook_cover_20260906_6e2d1 import main_cost


def check_record(record):
    indices = record["cell"]
    n, k = record["N"], record["K"]
    order, coefficients = record["order"], record["coeff"]
    polynomial = record["poly"]
    lower = polynomial[0] + sum(min(0, c) for c in polynomial[1:])
    assert lower >= 0
    weights = (7, 32, 12, 32, 7)
    moment = F(0)
    for grid in product(range(5), repeat=3):
        s = [F(x, 4) for x in grid]
        lengths = [i + x for i, x in zip(indices, s)] + [F(n)]
        a, b, c, d = [lengths[i] for i in order]
        t = sum(v * x for v, x in zip(coefficients, lengths)) / k
        local = (t, a - t, b - a + t, c - b + a - t)
        assert all(0 <= u <= x for u, x in zip(local, (a, b, c, d)))
        delta = d - c + b - a
        assert delta >= 0 if record["positive_delta"] else delta <= 0
        eta = delta if record["positive_delta"] else F(0)
        assert t + eta <= (a if record["positive_delta"] else d)
        cuts = [F(0)] * 4
        for i, u in zip(order, local):
            cuts[i] = u
        q = main_cost(lengths, cuts, tuple(order))
        x, y, z, w = lengths
        base = x * y * (z + w)
        if indices[0] + indices[1] + 2 - indices[2] > 0:
            base -= w * (x + y - z) ** 2 / 4
        expected = 4 * k ** 3 * (base - q)
        actual = sum(value * s[0] ** (h // 16) * s[1] ** ((h // 4) % 4)
                     * s[2] ** (h % 4) for h, value in enumerate(polynomial))
        assert actual == expected >= lower
        weight = weights[grid[0]] * weights[grid[1]] * weights[grid[2]]
        moment += weight * x * y * z * expected / 90 ** 3
    # Tensor Boole quadrature is exact: each separate variable has degree <=4.
    assert moment == F(record["moment"], 2160)
    square = n * n + sum((i + 1) ** 2 for i in indices)
    root = isqrt(square)
    root += root * root < square
    bound = F(45360 * 7, 22) * moment * n ** 2 / (4 * k ** 3 * square ** 5 * root)
    assert bound == F(record["numerator"], record["denominator"])
    assert record["quotient"] == (bound.numerator << 64) // bound.denominator


def main(executable, samples):
    output = subprocess.run([executable, "--sample", "192", "16", str(samples)],
                            check=True, capture_output=True, text=True).stdout
    records = [json.loads(line) for line in output.splitlines()]
    assert records
    for record in records:
        check_record(record)
    delta = F(453819283540955815, 1 << 64)
    old_upper = F("1.26947180564")
    assert delta > F(49, 2000)
    assert old_upper - delta < F("1.245")
    print(f"PASS {len(records)} independently integrated cells; {125*len(records)} "
          "exact polynomial/physical-cost evaluations")
    print(f"Exact saving: {delta}")
    print(f"Certified upper endpoint diagnostic: {float(old_upper-delta):.12f}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("executable")
    parser.add_argument("--samples", type=int, default=160)
    args = parser.parse_args()
    main(args.executable, args.samples)
