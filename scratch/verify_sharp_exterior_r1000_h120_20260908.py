"""One exact-rational certificate for the finite exterior bound.

Run only on the authorized h100 mathematical execution host.
No search, floating point, asymptotic estimate, or large enumeration.
"""

from fractions import Fraction
from math import comb
import json
import resource

resource.setrlimit(resource.RLIMIT_CPU, (10, 10))
resource.setrlimit(resource.RLIMIT_AS, (256 * 1024**2, 256 * 1024**2))

r = 1000
H = 120
theta = Fraction(
    8 * (r + 1) * (r + H) * (H * H - H + r),
    (2 * r + 1) * (r + 2) ** 2,
) * Fraction(H + 1, H) ** 3
ratio = Fraction(comb(2 * r, r - H), comb(2 * r, r))
upper_bound = theta * ratio
threshold = Fraction(1, 25000)
assert upper_bound < threshold

scale = 10**15
lower_numerator = upper_bound.numerator * scale // upper_bound.denominator
assert Fraction(lower_numerator, scale) <= upper_bound
assert upper_bound < Fraction(lower_numerator + 1, scale)

print(json.dumps({
    "r": r,
    "H": H,
    "theta_numerator": theta.numerator,
    "theta_denominator": theta.denominator,
    "decimal_enclosure_denominator": scale,
    "decimal_enclosure_lower_numerator": lower_numerator,
    "decimal_enclosure_upper_numerator": lower_numerator + 1,
    "strictly_below_1_over_25000": True,
    "method": "exact integer cross-multiplication through Fraction",
}, indent=2))
