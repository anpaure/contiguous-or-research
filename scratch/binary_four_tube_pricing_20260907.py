"""Rank-symmetrized LP with constructive four-coordinate tube upper costs.

Numerical exploration only: the LP is fractional, not a word certificate.
"""

from fractions import Fraction as F
from itertools import combinations, combinations_with_replacement
from math import comb


def rho(ranks):
    if len(ranks) == 1:
        return F(2, 3)
    two = {1: F(23, 24), 2: F(5, 6), 3: F(35, 48), 4: F(2, 3)}
    if len(ranks) == 2:
        return two[ranks[1] - ranks[0]]
    if len(ranks) == 3 and ranks[-1] - ranks[0] == 4:
        return max(two[y - x] for x, y in zip(ranks, ranks[1:]))
    return F(1)


def main():
    import numpy as np
    from scipy.optimize import linprog

    types = [r for size in range(1, 6) for r in combinations(range(5), size)]
    columns = list(combinations_with_replacement(types, 2))
    costs = [len(a) * rho(b) + len(b) * rho(a) for a, b in columns]
    matrix = np.array([[sum(i + j == s for i in a for j in b)
                        for a, b in columns] for s in range(9)], dtype=float)
    sizes = np.array([comb(8, s) for s in range(9)], dtype=float)
    result = linprog(np.array(costs, dtype=float), A_ub=-matrix,
                     b_ub=-sizes, bounds=(0, None), method="highs")
    assert result.success
    print("rank types", len(types), "columns", len(columns), flush=True)
    print("fractional weighted cost", result.fun, "baseline 140", flush=True)
    print("dual", -result.ineqlin.marginals, flush=True)
    for i, weight in enumerate(result.x):
        if weight > 1e-7:
            print(columns[i], "cost", costs[i], "weight", weight,
                  "rhos", tuple(map(rho, columns[i])), flush=True)


if __name__ == "__main__":
    main()
