"""Exploratory fractional pricing of binary tubes with every support split.

All quoted rho values are constructive asymptotic chain-count upper bounds.
The LP is numerical and fractional: no OR word or integral cover is claimed.
"""

from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations, combinations_with_replacement, product
from math import comb, factorial


def density(n, x):
    if n == 1:
        return F(0 < x < 1)
    return sum((-1)**j * comb(n, j) * max(F(0), x-j)**(n-1)
               for j in range(n+1)) / factorial(n-1)


def density_polynomial(n, intercept, slope, mid):
    if n == 1:
        return [F(0 < intercept-slope*mid < 1)]
    out = [F(0)] * n
    for j in range(n+1):
        if intercept-slope*mid <= j:
            continue
        factor = F((-1)**j * comb(n, j), factorial(n-1))
        for power in range(n):
            out[power] += (factor * comb(n-1, power)
                           * (intercept-j)**(n-1-power) * (-slope)**power)
    return out


@lru_cache(None)
def two_cell_upper(d, changed):
    a, t = changed, d-changed
    if not t:
        return density(d, F(d, 2))
    top = min(2*a, t)
    cuts = sorted({F(0), F(top)}
                  | {F(2*a-4*j) for j in range(a+1) if 0 < 2*a-4*j < top}
                  | {F(t-2*j) for j in range(t+1) if 0 < t-2*j < top})
    value = F(0)
    for low, high in zip(cuts, cuts[1:]):
        mid = (low+high)/2
        p = density_polynomial(a, F(a, 2), F(1, 4), mid)
        q = density_polynomial(t, F(t, 2), F(1, 2), mid)
        for i, x in enumerate(p):
            for j, y in enumerate(q):
                value += x*y*(high**(i+j+1)-low**(i+j+1))/F(i+j+1)
    return value


@lru_cache(None)
def rho(d, ranks):
    if d == 1:
        return F(1)
    a = len(ranks)-1
    if ranks[-1]-ranks[0] == a:
        # Complete staircase on a active axes, product with d-a free axes.
        return sum(density(d, F(d+a, 2)-j) for j in range(a+1))
    if len(ranks) == 2:
        return min(F(1), two_cell_upper(d, ranks[1]-ranks[0]))
    if ranks[-1]-ranks[0] == d:
        # An antichain cannot use both endpoint cells. Dilworth's theorem
        # makes the maximum of the two sub-tube widths an upper bound too.
        return max(rho(d, ranks[:-1]), rho(d, ranks[1:]))
    return F(1)


def main():
    import argparse
    import numpy as np
    from scipy.optimize import linprog

    parser = argparse.ArgumentParser()
    parser.add_argument("--dimension", type=int, default=8)
    args = parser.parse_args()
    dimension = args.dimension
    columns, costs = [], []
    for r in range(1, dimension//2+1):
        s = dimension-r
        left = [x for size in range(1, r+2) for x in combinations(range(r+1), size)]
        right = [x for size in range(1, s+2) for x in combinations(range(s+1), size)]
        for a, b in (combinations_with_replacement(left, 2) if r == s else product(left, right)):
            columns.append((r, a, s, b))
            costs.append(len(a)*rho(s,b)+len(b)*rho(r,a))
    matrix = np.array([[sum(i+j == z for i in a for j in b)
                        for r,a,s,b in columns] for z in range(dimension+1)], dtype=float)
    sizes = np.array([comb(dimension,z) for z in range(dimension+1)], dtype=float)
    result = linprog(np.array(costs, dtype=float), A_ub=-matrix,
                     b_ub=-sizes, bounds=(0,None), method="highs")
    assert result.success
    print("dimension", dimension, "columns", len(columns), flush=True)
    print("fractional upper-model cost", result.fun, flush=True)
    print("dual", -result.ineqlin.marginals, flush=True)
    for i, weight in enumerate(result.x):
        if weight > 1e-7:
            r,a,s,b = columns[i]
            print(columns[i], "cost", costs[i], "weight", weight,
                  "rhos", (rho(r,a),rho(s,b)), flush=True)
    print("four-dimensional two-cell bounds",
          [two_cell_upper(4,j) for j in range(1,5)], flush=True)


if __name__ == "__main__":
    main()
