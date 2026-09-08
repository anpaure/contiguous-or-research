"""One bounded h100 LP for56 endpoint-truncated ternary shore profiles.

All45 histograms/all ranks are constrained. This produces fractional
certificates only and does not launch an integral search.
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
from fractions import Fraction as F

assert socket.gethostname().split('.')[0] == 'arboghast'
os.sched_setaffinity(0, set(sorted(os.sched_getaffinity(0))[:2]))
resource.setrlimit(resource.RLIMIT_AS, (1024**3, 1024**3))
started = time.monotonic()
old = json.loads(pathlib.Path(sys.argv[1]).read_text())
output = pathlib.Path(sys.argv[2])
report = {'host': socket.gethostname(), 'scope': '56 shore histogram profiles '
          'from14 full4-axis ternary Dyck types and four endpoint choices; '
          'all1596 unordered pairs, all45 histogram inequalities, actual variable '
          'charge; fractional LP only.', 'phase': 'imports', 'status': 'RUNNING'}

class Stop(Exception):
    pass

def timeout(signum, frame):
    raise Stop('4.5-second internal time limit')

def enc(value):
    return [value.numerator, value.denominator]

signal.signal(signal.SIGALRM, timeout)
signal.setitimer(signal.ITIMER_REAL, 4.5)
try:
    import numpy as np
    from scipy.optimize import linprog
    report['phase'] = 'columns'
    histograms = [tuple(h) for h in old['histograms']]
    demands = old['orbit_sizes']
    assert len(histograms) == 45 and sum(demands) == 3**8
    hi = {h: i for i, h in enumerate(histograms)}
    heights = old['shore_height_sequences']
    assert len(heights) == 14
    full_profiles = [tuple((4-(r+h)//2, h, (r-h)//2)
                           for r, h in enumerate(hh)) for hh in heights]
    # mode0 full[0..8], mode1 dropbottom[1..8],
    # mode2 droptop[0..7], mode3 dropboth[1..7].
    intervals = [(0, 9), (1, 9), (0, 8), (1, 8)]
    profiles = []
    metadata = []
    for parent, profile in enumerate(full_profiles):
        for mode, (start, end) in enumerate(intervals):
            profiles.append(profile[start:end])
            metadata.append({'full_dyck_type': parent, 'endpoint_mode': mode,
                             'retained_ranks': list(range(start, end)),
                             'length': end-start})
    assert len(profiles) == len(set(profiles)) == 56
    pairs = list(itertools.combinations_with_replacement(range(56), 2))
    assert len(pairs) == 1596
    columns, costs = [], []
    for left, right in pairs:
        col = [0] * 45
        for a in profiles[left]:
            for b in profiles[right]:
                col[hi[tuple(a[k]+b[k] for k in range(3))]] += 1
        assert sum(col) == len(profiles[left]) * len(profiles[right])
        columns.append(col)
        costs.append(len(profiles[left]) + len(profiles[right]))
    gate = F(35 * 3**7, 32)
    report.update(histograms=histograms, orbit_sizes=demands,
                  full_height_sequences=heights, shore_profiles=metadata,
                  pair_types=pairs, columns=columns, costs=costs,
                  exact_improvement_gate=enc(gate))
    report['phase'] = 'sole_lp'
    result = linprog(np.asarray(costs, dtype=float),
                     A_ub=-np.asarray(columns, dtype=float).T,
                     b_ub=-np.asarray(demands, dtype=float),
                     bounds=(0, None), method='highs', options={'time_limit': 2.0})
    report.update(lp_status=int(result.status), lp_message=result.message,
                  floating_objective=float(result.fun) if result.fun is not None else None)
    if not result.success:
        report['status'] = 'LP_DID_NOT_FINISH_SUCCESSFULLY'
    else:
        report['phase'] = 'exact_certificates'
        primal = [F(float(value)).limit_denominator(1000000)
                  if value > 1e-9 else F(0) for value in result.x]
        support = [j for j, weight in enumerate(primal) if weight]
        coverage = [sum(primal[j] * columns[j][i] for j in support) for i in range(45)]
        assert all(coverage)
        factor = max([F(1)] + [F(demands[i]) / coverage[i] for i in range(45)])
        primal = [weight * factor for weight in primal]
        coverage = [sum(primal[j] * columns[j][i] for j in support) for i in range(45)]
        assert all(coverage[i] >= demands[i] for i in range(45))
        dual = [F(float(-value)).limit_denominator(1000000)
                if value < -1e-9 else F(0) for value in result.ineqlin.marginals]
        dual_support = [i for i, weight in enumerate(dual) if weight]
        prices = [sum(dual[i] * col[i] for i in dual_support) for col in columns]
        divisor = max([F(1)] + [price / cost for price, cost in zip(prices, costs)])
        dual = [weight / divisor for weight in dual]
        assert all(weight >= 0 for weight in dual)
        assert all(sum(dual[i] * col[i] for i in dual_support) <= cost
                   for col, cost in zip(columns, costs))
        primal_value = sum(primal[j] * costs[j] for j in support)
        dual_value = sum(dual[i] * demands[i] for i in dual_support)
        report.update(exact_primal_value=enc(primal_value), exact_dual_value=enc(dual_value),
                      exact_duality_gap=enc(primal_value-dual_value),
                      exact_gate_minus_primal=enc(gate-primal_value),
                      exact_gate_minus_dual=enc(gate-dual_value),
                      primal_has_strict_margin=primal_value < gate,
                      dual_excludes_strict_margin=dual_value >= gate,
                      primal=[{'pair_type': j, 'shore_types': pairs[j],
                               'cost': costs[j], 'weight': enc(primal[j])} for j in support],
                      dual=[{'histogram': histograms[i], 'weight': enc(dual[i])}
                            for i in dual_support],
                      all45_exact_primal_coverages=[enc(value) for value in coverage],
                      exact_primal_scaling=enc(factor), exact_dual_scaling=enc(divisor))

        report['phase'] = 'physical_profile_replay'
        actual = set()
        physical_count = [0]
        def visit(point, profile):
            if all(value == 2 for value in point):
                physical_count[0] += 1
                actual.add(tuple(profile))
                return
            for coordinate in range(4):
                if point[coordinate] == 2:
                    continue
                after = list(point)
                after[coordinate] += 1
                visit(after, profile + [tuple(after.count(value) for value in range(3))])
        visit([0, 0, 0, 0], [(4, 0, 0)])
        assert physical_count[0] == 2520 and actual == set(full_profiles)
        actual_cropped = {p[start:end] for p in actual for start, end in intervals}
        assert actual_cropped == set(profiles)
        # Rebuild every physical histogram pair without the Dyck-state formula.
        actual_profiles = sorted(actual_cropped)
        rebuilt = []
        for i, aa in enumerate(actual_profiles):
            for bb in actual_profiles[i:]:
                col = [0] * 45
                for a in aa:
                    for b in bb:
                        col[hi[tuple(a[k]+b[k] for k in range(3))]] += 1
                cost = len(aa)+len(bb)
                assert sum(dual[h] * col[h] for h in dual_support) <= cost
                rebuilt.append((cost, tuple(col)))
        assert sorted(rebuilt) == sorted(zip(costs, map(tuple, columns)))
        report['independent_exact_replay'] = {
            'physical_full_geodesics': physical_count[0], 'cropped_profiles': len(actual_cropped),
            'physical_pair_types': len(rebuilt), 'all45_primal_orbits': 'PASS',
            'all1596_physical_dual_inequalities': 'PASS'}
        report['status'] = 'EXACT_CERTIFICATES_PASS'
        report['phase'] = 'done'
except Stop as stop:
    report['status'] = str(stop)
finally:
    signal.setitimer(signal.ITIMER_REAL, 0)
    report['elapsed_seconds'] = time.monotonic() - started
    output.write_text(json.dumps(report, separators=(',', ':')) + '\n')
    print(json.dumps({key: value for key, value in report.items()
                      if key not in ('histograms', 'orbit_sizes', 'full_height_sequences',
                                     'shore_profiles', 'pair_types', 'columns', 'costs',
                                     'all45_exact_primal_coverages')}, indent=2))
