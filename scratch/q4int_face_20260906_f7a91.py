"""Exact optimal-dual-face directions from the complete tight census list."""

import argparse
from fractions import Fraction
from functools import reduce
from math import gcd, lcm
from pathlib import Path
import json

import numpy as np
from scipy.optimize import linprog

from q4int_verify_20260906_f7a91 import DUAL12


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    data = [list(map(int, line.split())) for line in Path('scratch/q4int_censuses_20260906_f7a91.txt').read_text().splitlines()]
    n, k = data[0]
    populations = data[1:n+1]
    columns = data[n+1:]
    a = np.array([c[2:] for c in columns], dtype=float)
    b = np.array([p[4] for p in populations], dtype=float)
    y = [DUAL12.get(tuple(p[:4]), 0) for p in populations]
    bounds = [(0 if value == 0 else -1, 1) for value in y]
    objective = a.sum(axis=0) - 0.01*np.array([value == 0 for value in y])
    result = linprog(objective, A_ub=a, b_ub=np.zeros(k), A_eq=b[None, :], b_eq=[0], bounds=bounds, method='highs')
    assert result.success
    fractions = [Fraction(float(v)).limit_denominator(1000000) for v in result.x]
    denominator = lcm(*(v.denominator for v in fractions))
    direction = [int(v*denominator) for v in fractions]
    divisor = reduce(gcd, direction) or 1
    direction = [v//divisor for v in direction]
    assert sum(p[4]*v for p, v in zip(populations, direction)) == 0
    assert all(v >= 0 for old, v in zip(y, direction) if old == 0)
    slacks = [sum(x*v for x, v in zip(c[2:], direction)) for c in columns]
    assert all(s <= 0 for s in slacks)
    output = {'direction': direction, 'populations': populations,
              'strict_censuses': sum(s < 0 for s in slacks), 'retained_censuses': sum(s == 0 for s in slacks),
              'new_positive_orbits': sum(old == 0 and v > 0 for old, v in zip(y, direction)),
              'explanation': 'For K=max(abs(direction)), y_new=y_old+direction/(2400*K) is a valid optimum dual if K>0. Every old non-tight rectangle has slack at least 1/12, and its volume is at most 100.'}
    Path(args.output).write_text(json.dumps(output, indent=2) + '\n')
    print(json.dumps(output), flush=True)
