"""One bounded h100 LP diagnostic of the complete ternary8 histogram gate.

This is a fractional feasibility calculation, not an integral cover search.
Run with an external five-second timeout. All final certificates use exact
fractions and are also checked against an independent physical-path census.
"""
import itertools
import json
import math
import os
import pathlib
import resource
import signal
import socket
import sys
import time
from fractions import Fraction

assert socket.gethostname().split('.')[0] == 'arboghast'
os.sched_setaffinity(0, set(sorted(os.sched_getaffinity(0))[:2]))
resource.setrlimit(resource.RLIMIT_AS, (1024**3, 1024**3))
started = time.monotonic()
signal.alarm(5)
import numpy as np
from scipy.optimize import linprog

histograms = [(a, b, 8-a-b) for a in range(9) for b in range(9-a)]
hist_index = {h: i for i, h in enumerate(histograms)}
demands = [math.factorial(8) // math.prod(math.factorial(v) for v in h)
           for h in histograms]
heights = []

def dyck(opened, closed, path):
    if closed == 4:
        heights.append(tuple(path))
        return
    if opened < 4:
        dyck(opened + 1, closed, path + [opened + 1 - closed])
    if closed < opened:
        dyck(opened, closed + 1, path + [opened - closed - 1])

dyck(0, 0, [0])
assert len(heights) == 14 and len(set(heights)) == 14
shore_histograms = []
for hh in heights:
    shore_histograms.append(tuple((4-(r+h)//2, h, (r-h)//2)
                                  for r, h in enumerate(hh)))
pair_types = list(itertools.combinations_with_replacement(range(14), 2))
assert len(pair_types) == 105
columns = []
for i, j in pair_types:
    col = [0] * 45
    for a in shore_histograms[i]:
        for b in shore_histograms[j]:
            col[hist_index[tuple(x+y for x, y in zip(a, b))]] += 1
    assert sum(col) == 81
    columns.append(col)

result = linprog(np.ones(105), A_ub=-np.asarray(columns, dtype=float).T,
                 b_ub=-np.asarray(demands, dtype=float), bounds=(0, None),
                 method='highs', options={'time_limit': 2.0})
report = {'host': socket.gethostname(),
          'scope': 'Complete105 histogram types of full geodesic4+4 ternary8 rows; fractional only.',
          'histograms': histograms, 'orbit_sizes': demands,
          'shore_height_sequences': heights, 'pair_types': pair_types,
          'columns': columns, 'lp_status': int(result.status),
          'lp_message': result.message}

def enc(x):
    return [x.numerator, x.denominator]

if result.success:
    primal = [Fraction(float(v)).limit_denominator(1000000)
              if v > 1e-9 else Fraction(0) for v in result.x]
    coverage = [sum(primal[j] * columns[j][i] for j in range(105))
                for i in range(45)]
    assert all(coverage)
    factor = max([Fraction(1)] + [Fraction(demands[i], 1) / coverage[i]
                                  for i in range(45)])
    primal = [v * factor for v in primal]
    assert all(sum(primal[j] * columns[j][i] for j in range(105)) >= demands[i]
               for i in range(45))
    dual = [Fraction(float(-v)).limit_denominator(1000000)
            if v < -1e-9 else Fraction(0) for v in result.ineqlin.marginals]
    max_price = max(sum(dual[i] * col[i] for i in range(45)) for col in columns)
    divisor = max(Fraction(1), max_price)
    dual = [v / divisor for v in dual]
    assert all(v >= 0 for v in dual)
    assert all(sum(dual[i] * col[i] for i in range(45)) <= 1 for col in columns)
    primal_value = sum(primal)
    dual_value = sum(y * d for y, d in zip(dual, demands))
    report.update(lp_objective=float(result.fun),
                  exact_primal_value=enc(primal_value),
                  exact_dual_value=enc(dual_value),
                  primal=[{'type': j, 'shore_types': pair_types[j], 'weight': enc(v)}
                          for j, v in enumerate(primal) if v],
                  dual=[{'histogram': histograms[i], 'weight': enc(v)}
                        for i, v in enumerate(dual) if v],
                  exact_duality_gap=enc(primal_value-dual_value),
                  lower_exceeds_132=dual_value > 132,
                  upper_at_most_132=primal_value <= 132)

    # Independent exhaustive enumeration of actual four-coordinate step words.
    # No Dyck-state formula is used in this verification.
    physical_profiles = set()
    physical_count = [0]
    def physical(point, profile):
        if all(v == 2 for v in point):
            physical_count[0] += 1
            physical_profiles.add(tuple(profile))
            return
        for coordinate in range(4):
            if point[coordinate] == 2:
                continue
            after = list(point)
            after[coordinate] += 1
            hh = tuple(after.count(v) for v in range(3))
            physical(after, profile + [hh])
    physical([0, 0, 0, 0], [(4, 0, 0)])
    assert physical_count[0] == 2520
    assert physical_profiles == set(shore_histograms)
    independent = sorted(physical_profiles)
    independent_columns = []
    for i, a in enumerate(independent):
        for b in independent[i:]:
            col = [0] * 45
            for aa in a:
                for bb in b:
                    combined = tuple(aa[k] + bb[k] for k in range(3))
                    col[hist_index[combined]] += 1
            assert sum(dual[k] * col[k] for k in range(45)) <= 1
            independent_columns.append(tuple(col))
    assert sorted(independent_columns) == sorted(map(tuple, columns))
    report['independent_exact_verification'] = {
        'physical_four_axis_geodesics': physical_count[0],
        'distinct_histogram_paths': len(physical_profiles),
        'pair_types_verified': len(independent_columns),
        'primal_all45_orbits': 'PASS', 'dual_all105_physical_types': 'PASS'}

rank_counts = [sum(d for h, d in zip(histograms, demands) if h[1]+2*h[2] == r)
               for r in range(17)]
report['global_rank_counts'] = rank_counts
report['per_row_rank_counts'] = [min(r+1, 17-r) for r in range(17)]
report['elapsed_seconds'] = time.monotonic() - started
pathlib.Path(sys.argv[1]).write_text(json.dumps(report, separators=(',', ':')) + '\n')
signal.alarm(0)
print(json.dumps({k: report[k] for k in report if k not in
                  ('columns', 'histograms', 'orbit_sizes', 'pair_types')}, indent=2))
