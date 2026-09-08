"""Exploratory quadrature for balanced Brownian/SCD accumulators, not a certificate."""

import math

import numpy as np
from numpy.polynomial.legendre import leggauss


def density3(a, b, c):
    a, b, c = np.sort(np.broadcast_arrays(a, b, c), axis=0)
    return 1 / c - np.maximum(0, a + b - c) ** 2 / (4 * a * b * c)


def cost5pair(a, b, c, d, e):
    c, d, e = np.sort(np.broadcast_arrays(c, d, e), axis=0)
    lo, hi = abs(a - b), a + b

    def q(s):
        return (s * s / (2 * e) + s * s / (2 * d)
                - (np.maximum(0, s - d + c) ** 3
                   - np.maximum(0, s - c - d) ** 3) / (12 * c * d))

    l, u = np.maximum(lo, e), np.maximum(hi, e)
    return (q(np.minimum(hi, e)) - q(np.minimum(lo, e)) + u - l
            + density3(c, d, e) * (u * u - l * l) / 2) / (2 * a * b)


def cost(p, z):
    if p == 2:
        return 1 + 1 / z
    if p == 3:
        return np.full_like(z, 2)
    if p == 4:
        return 2 - z / 4
    if p == 5:
        return np.minimum(cost5pair(z, 1, 1, 1, 1), cost5pair(1, 1, z, 1, 1))
    raise ValueError(p)


def main():
    print("Exploratory quadrature only; not an upper-bound certificate.")
    for order in (80, 160, 320):
        nodes, weights = leggauss(order)
        x, wx = 15 * (nodes + 1), 15 * weights
        z, wz = (nodes + 1) / 2, weights / 2
        for p in range(2, 6):
            inner = np.sum((wz * z * cost(p, z))[None, :]
                           * np.sinh(x[:, None] * z[None, :]), axis=1)
            integrand = p / 2 * x ** p / np.sinh(x) ** (p + 1) * inner
            print(f"order={order} p={p} estimate={np.dot(wx, integrand):.15f}")
    print(f"pi^2/8={math.pi ** 2 / 8:.15f}; floor={2 / math.sqrt(math.e):.15f}")
    for z in (0.001, 0.25, 0.5, 0.75, 1):
        print(f"z={z}: merge small={cost5pair(z, 1, 1, 1, 1)}, "
              f"merge equal={cost5pair(1, 1, z, 1, 1)}")


if __name__ == "__main__":
    main()
