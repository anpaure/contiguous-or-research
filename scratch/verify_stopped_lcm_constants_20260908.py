#!/usr/bin/env python3
"""Exact constants for the supplied stopped-LCM proof. Execute only on h100."""
from fractions import Fraction as F
import json
import resource
import signal

resource.setrlimit(resource.RLIMIT_CPU, (5, 5))
resource.setrlimit(resource.RLIMIT_AS, (128 * 1024**2, 128 * 1024**2))
signal.alarm(10)
kappa_limit = (F(1, 5) + 2 * F(63, 200) / 3) / ((1 - F(1, 1024)) * F(4, 5))
kappa_star = F(5131, 10000)
assert kappa_limit == F(2624, 5115) < kappa_star
z = F(4869, 15131)
log_lower = 2 * (z + z**3 / 3 + z**5 / 5)
assert (1 + z) / (1 - z) == 1 / kappa_star
assert log_lower > F(2, 3)
# Machin identity with alternating-series bounds also proves the NB constant.
def atan_bracket(x, pairs=12):
    total = F(0)
    for j in range(2 * pairs):
        total += (-1)**j * x**(2*j+1) / (2*j+1)
    return total, total + x**(4*pairs+1) / (4*pairs+1)
a_lo, a_hi = atan_bracket(F(1, 5))
b_lo, b_hi = atan_bracket(F(1, 239))
pi_lo, pi_hi = 16*a_lo - 4*b_hi, 16*a_hi - 4*b_lo
assert F(25, 8) < pi_lo < pi_hi < 8 * F(63, 100)**2
print(json.dumps({
    'status': 'PASS',
    'kappa_limit': str(kappa_limit),
    'kappa_star': str(kappa_star),
    'positive_kappa_margin': str(kappa_star-kappa_limit),
    'log_lower': str(log_lower),
    'positive_log_margin_above_two_thirds': str(log_lower-F(2, 3)),
    'nb_coefficient_63_over_100_verified': True,
    'pi_lower': str(pi_lo), 'pi_upper': str(pi_hi),
    'scope': 'These exact constants supplement the written proof; no user-reported checker suite was rerun.'
}, indent=2))
