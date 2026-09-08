"""Exact lower certificate for one independent tube-rounding obstruction.

This checks the finite rational constants, not an arbitrary integral-cover
lower bound. The asymptotic concentration proof is in the companion note.
"""

from collections import Counter
from importlib.util import module_from_spec, spec_from_file_location
from itertools import product
from math import comb, prod
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "scratch/q4d6_fractional_template_20260906_c52e9.py"
spec = spec_from_file_location("fractional_certificate", SOURCE)
certificate = module_from_spec(spec)
spec.loader.exec_module(certificate)
rows = certificate.rows()
points = list(product(range(4), repeat=6))
population = Counter(certificate.orbit(p) for p in points)
counts = [Counter(certificate.orbit(x + y) for x, y in product(c, d))
          for _, c, d in rows]

certificate.check()
assert len(rows) == 14
assert max(weight for weight, _, _ in rows) < 21600

# Fixed-denominator floor arithmetic always underestimates the true
# positive product. Integer truncation cannot invalidate the lower bound.
scale = 10**15
lower = {}
approx = {}
for orbit, size in population.items():
    value = scale
    factors = []
    for (weight, _, _), census in zip(rows, counts):
        numerator = 1440 * census[orbit]
        assert numerator % size == 0
        exponent = numerator // size
        assert 0 <= exponent <= 1440
        for _ in range(exponent):
            value = value * (21600 - weight) // 21600
        factors.append((1 - weight / 21600) ** exponent)
    lower[orbit] = value
    approx[orbit] = prod(factors)

rank_lower = Counter()
rank_approx = Counter()
for point in points:
    orbit = certificate.orbit(point)
    rank_lower[sum(point)] += lower[orbit]
    rank_approx[sum(point)] += approx[orbit]

spline = [sum((-1)**j * comb(6, j) * max(0, t-j)**5
              for j in range(7)) for t in range(7)]
assert spline == [0, 1, 26, 66, 26, 1, 0]
coefficients = {7: 1, 8: 26, 9: 66, 10: 26, 11: 1}
scaled_lower = sum(weight * rank_lower[rank]
                   for rank, weight in coefficients.items())
assert scaled_lower > (813 * 120 * scale) // 4  # z_* > 203.25
z = sum(weight * rank_approx[rank]
        for rank, weight in coefficients.items()) / 120
total_holes = sum(rank_approx.values()) / 4096
print("PASS integer certificate: central hole coefficient z_* > 203.25")
print("Approximate central coefficient:", z)
print("Approximate charge after additive chain-pair repair:", 1248 + 2*z)
print("Approximate whole-grid missed fraction:", total_holes)
