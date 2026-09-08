"""One h100 necessary histogram LP for a fixed literal four-row repair.

The fixed repair breaks coordinate symmetry. Feasible orbit-count weights
are ONLY a necessary condition for its residual physical cover.
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
report = {'host': socket.gethostname(), 'scope': 'Necessary all45-histogram '
          'row-count relaxation after subtracting the ACTUAL UNION of a fixed '
          'four-row charge48 repair. Only105 double-endpoint-truncated types. '
          'A feasible LP is NOT a fractional cover of the fixed residual targets.',
          'phase': 'imports', 'status': 'RUNNING'}

class Stop(Exception):
    pass

def timeout(signum, frame):
    raise Stop('2.5-second internal time limit')

def enc(v):
    return [v.numerator, v.denominator]

signal.signal(signal.SIGALRM, timeout)
signal.setitimer(signal.ITIMER_REAL, 2.5)
try:
    import numpy as np
    from scipy.optimize import linprog
    histograms = [tuple(h) for h in old['histograms']]
    hi = {h: i for i, h in enumerate(histograms)}
    demands = old['orbit_sizes']
    ambient = list(itertools.product(range(3), repeat=8))

    def histogram(point):
        return tuple(point.count(value) for value in range(3))

    def repair(shift):
        chains, row_sets = [], []
        for t in range(4):
            a, b = t, (t+shift) % 4
            zero, top = (0,)*4, (2,)*4
            ea = tuple(int(j == a) for j in range(4))
            two_a = tuple(2*int(j == a) for j in range(4))
            before_b = tuple(2*int(j != b) for j in range(4))
            after_b = tuple(1 if j == b else 2 for j in range(4))
            chain = (zero, ea, two_a, before_b, after_b, top)
            assert len(set(chain)) == 6
            assert all(x != y and all(xx <= yy for xx, yy in zip(x,y))
                       for x,y in zip(chain, chain[1:]))
            chains.append(chain)
            row_sets.append({left+right for left in chain for right in chain})
        corner_set = {left+right for left in ((0,)*4, (2,)*4)
                      for right in ((0,)*4, (2,)*4)}
        assert all(len(s) == 36 for s in row_sets)
        assert all(a & b == corner_set for a,b in itertools.combinations(row_sets,2))
        union = set().union(*row_sets)
        # Independent ambient membership replay; no row-pair union used.
        replay = {point for point in ambient
                  if any(point[:4] in chain and point[4:] in chain for chain in chains)}
        assert replay == union and len(union) == 132
        boundary = {point for point in ambient
                    if sum(value != 0 for value in point) <= 1
                    or sum(value != 2 for value in point) <= 1}
        assert boundary <= union
        counts = [0]*45
        ranks = [0]*17
        for point in union:
            counts[hi[histogram(point)]] += 1
            ranks[sum(point)] += 1
        assert ranks[7] == ranks[9] == 16 and ranks[8] == 18
        assert sum(sum(point) == 8 and 1 not in point for point in union) == 10
        if shift == 2:
            assert {tuple(2-v for v in point) for point in union} == union
        return {'shift': shift, 'shore_chains': chains, 'union_targets': sorted(union),
                'union_size': len(union), 'occurrences': 144, 'principal_cost': 48,
                'rank_counts': ranks, 'histogram_counts': counts,
                'extremal_boundary_targets': len(boundary), 'literal_replay': 'PASS'}

    report['phase'] = 'literal_repair'
    repair1, repair2 = repair(1), repair(2)
    assert repair1['histogram_counts'] == repair2['histogram_counts']
    remaining = [d-r for d,r in zip(demands,repair2['histogram_counts'])]
    assert all(value >= 0 for value in remaining) and sum(remaining) == 3**8-132
    heights = old['shore_height_sequences']
    profiles = [tuple((4-(r+h)//2, h, (r-h)//2)
                      for r,h in enumerate(hh))[1:8] for hh in heights]
    assert len(profiles) == 14 and all(len(p) == 7 for p in profiles)
    pairs = list(itertools.combinations_with_replacement(range(14), 2))
    columns = []
    for left, right in pairs:
        col = [0]*45
        for a in profiles[left]:
            for b in profiles[right]:
                col[hi[tuple(a[k]+b[k] for k in range(3))]] += 1
        assert sum(col) == 49
        columns.append(col)
    assert len(columns) == 105
    report.update(histograms=histograms, original_orbit_sizes=demands,
                  remaining_orbit_counts=remaining, repairs=[repair1,repair2],
                  repair_variants_have_identical_union_histograms=True,
                  used_repair_shift=2, pair_types=pairs, columns=columns)
    report['phase'] = 'sole_lp'
    result = linprog(np.ones(105), A_ub=-np.asarray(columns,dtype=float).T,
                     b_ub=-np.asarray(remaining,dtype=float), bounds=(0,None),
                     method='highs', options={'time_limit':1.0})
    report.update(lp_status=int(result.status), lp_message=result.message,
                  floating_row_count=float(result.fun) if result.fun is not None else None)
    if result.success:
        report['phase'] = 'exact_certificate'
        xx = [F(float(v)).limit_denominator(1000000) if v > 1e-9 else F(0)
              for v in result.x]
        support = [j for j,x in enumerate(xx) if x]
        coverage = [sum(xx[j]*columns[j][i] for j in support) for i in range(45)]
        assert all(coverage[i] > 0 for i in range(45) if remaining[i])
        scale = max([F(1)] + [F(remaining[i])/coverage[i] for i in range(45) if remaining[i]])
        xx = [x*scale for x in xx]
        coverage = [sum(xx[j]*columns[j][i] for j in support) for i in range(45)]
        assert all(coverage[i] >= remaining[i] for i in range(45))
        yy = [F(float(-v)).limit_denominator(1000000) if v < -1e-9 else F(0)
              for v in result.ineqlin.marginals]
        ds = [i for i,y in enumerate(yy) if y]
        prices = [sum(yy[i]*col[i] for i in ds) for col in columns]
        divisor = max([F(1)] + prices)
        yy = [y/divisor for y in yy]
        assert all(y >= 0 for y in yy)
        assert all(sum(yy[i]*col[i] for i in ds) <= 1 for col in columns)
        upper = sum(xx)
        lower = sum(yy[i]*remaining[i] for i in ds)
        report.update(exact_primal_row_count=enc(upper), exact_dual_row_count=enc(lower),
                      exact_duality_gap=enc(upper-lower),
                      exact_167_minus_primal=enc(F(167)-upper),
                      excludes_167_rows=lower > 167,
                      necessary_feasibility_at_167=upper <= 167,
                      exact_relaxation_total_charge=enc(F(48)+14*upper),
                      primal=[{'type':j,'shore_types':pairs[j],'weight':enc(xx[j])} for j in support],
                      dual=[{'histogram':histograms[i],'weight':enc(yy[i])} for i in ds],
                      all45_exact_remaining_coverages=[enc(c) for c in coverage],
                      exact_primal_scaling=enc(scale),exact_dual_scaling=enc(divisor))
        report['status'] = 'EXACT_NECESSARY_HISTOGRAM_CERTIFICATES_PASS'
        report['phase'] = 'done'
    else:
        report['status'] = 'LP_DID_NOT_FINISH_SUCCESSFULLY'
except Stop as stop:
    report['status'] = str(stop)
finally:
    signal.setitimer(signal.ITIMER_REAL,0)
    report['elapsed_seconds'] = time.monotonic()-started
    output.write_text(json.dumps(report,separators=(',',':'))+'\n')
    print(json.dumps({key:value for key,value in report.items()
                      if key not in ('histograms','original_orbit_sizes','remaining_orbit_counts',
                                     'repairs','pair_types','columns','all45_exact_remaining_coverages')},indent=2))
