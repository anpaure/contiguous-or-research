#!/usr/bin/env python3
"""Bounded exact arithmetic audit; execute only on h100."""
import resource
import signal

resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
resource.setrlimit(resource.RLIMIT_AS, (512 * 1024 * 1024, 512 * 1024 * 1024))
signal.alarm(45)

from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import platform
import time

started = time.monotonic()
checks = {}

def record(name, value, bound, relation="lt"):
    valid = value < bound if relation == "lt" else value > bound
    assert valid, name
    checks[name] = {
        "value_numerator": str(value.numerator),
        "value_denominator": str(value.denominator),
        "bound_numerator": str(bound.numerator),
        "bound_denominator": str(bound.denominator),
        "relation": relation,
        "pass": True,
    }

def digits(value, places=50):
    scale = 10 ** places
    low = value.numerator * scale // value.denominator
    def display(number):
        raw = str(number).zfill(places + 1)
        return raw[:-places] + "." + raw[-places:]
    return {
        "lower": display(low),
        "upper": display(low + 1),
        "denominator": str(scale),
        "lower_numerator": str(low),
        "upper_numerator": str(low + 1),
        "strict_upper": True,
    }

nb_square = Fraction(6000, 5999) * Fraction(800, 799)
record("NB_squared_factor", nb_square, Fraction(1001, 1000) ** 2)

pi_lower = 16 * (Fraction(1, 5) - Fraction(1, 3 * 5**3)) - 4 * Fraction(1, 239)
record("Machin_lower_exceeds_25_over_8", pi_lower, Fraction(25, 8), "gt")

depth_coefficient_square = (
    Fraction(1001, 1000) ** 2 * Fraction(7, 10) ** 2
    / (Fraction(799, 1000) ** 2 * 4 * Fraction(25, 8) * Fraction(99, 100))
)
record("depth_coefficient_square_below_1_over_16", depth_coefficient_square, Fraction(1, 16))

Q = 4 * 200**3
lcm_j = math.lcm(*range(1, 33))
q_powers = [Q**j for j in range(33)]
raw_numerator = 0
for i in range(1, 281):
    q_i = Fraction(251, 1000) + Fraction(i**3, Q)
    assert 0 < q_i < 1
    base = Q - (251 * (Q // 1000) + i**3)
    series_numerator = 0
    base_power = 1
    for j in range(1, 33):
        base_power *= base
        series_numerator += base_power * (lcm_j // j) * q_powers[32-j]
    raw_numerator += (2*i - 1) * series_numerator

S = Fraction(raw_numerator, 200**2 * lcm_j * Q**32)
record("integral_certificate_above_1_41", S, Fraction(141, 100), "gt")
assert Fraction(280, 200) ** 2 == Fraction(49, 25)
assert Fraction(251, 1000) + Fraction(5, 7) < 1

# Independently evaluate the same finite expression with Fraction operations.
S_replay = Fraction(0)
for i in range(1, 281):
    q_i = Fraction(251, 1000) + Fraction(i**3, Q)
    term = 1 - q_i
    power = Fraction(1)
    series = Fraction(0)
    for j in range(1, 33):
        power *= term
        series += power / j
    S_replay += Fraction(2*i - 1, 200**2) * series
assert S == S_replay

report = {
    "status": "PASS",
    "hostname": platform.node(),
    "arithmetic": "exact integers and fractions; no floating-point mathematical premise",
    "limits": {"cpu_seconds": 30, "wall_seconds": 45, "address_space_bytes": 512*1024*1024},
    "checks": checks,
    "S": {"numerator": str(S.numerator), "denominator": str(S.denominator), "decimal_enclosure": digits(S)},
    "S_minus_1_41": {"numerator": str((S-Fraction(141,100)).numerator), "denominator": str((S-Fraction(141,100)).denominator), "decimal_enclosure": digits(S-Fraction(141,100))},
    "NB_squared_factor_enclosure": digits(nb_square),
    "depth_coefficient_square_enclosure": digits(depth_coefficient_square),
    "independent_fraction_replay": True,
    "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    "elapsed_wall_seconds": time.monotonic()-started,
}
Path("depth_product_rational_certificate.json").write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps({"status": report["status"], "S": digits(S), "margin": digits(S-Fraction(141,100)), "checks": list(checks), "elapsed_wall_seconds": report["elapsed_wall_seconds"]}, indent=2))
