"""Literal four-block words and an exact-rational integral certificate.

The certified integration uses a composite midpoint rule, a proved global
second-derivative bound, exact fractions, and integer square-root bounds.
"""

from fractions import Fraction as F
from itertools import product
from math import comb, isqrt, pi, sqrt
import argparse

from density_bridge_frontier_20260905_c71e4 import bridge, scd, unions


def multiply_chains(left, right):
    if len(left) > len(right):
        left, right = right, left
    result = []
    for i in range(len(left)):
        last = len(left) - 1 - i
        result.append([left[j] | right[i] for j in range(last + 1)]
                      + [left[last] | right[j] for j in range(i + 1, len(right))])
    return result


def product_chains(factors):
    result = [[0]]
    for factor in factors:
        result = [chain for current in result for chain in multiply_chains(current, factor)]
    return result


def width3(a, b, c):
    a, b, c = sorted((a, b, c))
    return a * b - max(0, a + b - c) ** 2 // 4


def paired_box_word(chains, universes, signs):
    desired = [chain if sign == 0 else [universe ^ x for x in reversed(chain)]
               for chain, universe, sign in zip(chains, universes, signs)]
    fixed_index = max(range(4), key=lambda i: len(chains[i]))
    others = [i for i in range(4) if i != fixed_index]
    moving = product_chains([desired[i] for i in others])
    total = 1
    for i in others:
        total *= len(chains[i])
    assert sum(map(len, moving)) == total
    width = width3(*(len(chains[i]) for i in others))
    assert len(moving) == width
    fixed_chain = [universes[fixed_index] ^ x for x in reversed(desired[fixed_index])]
    fixed = bridge(fixed_chain, universes[fixed_index])
    moving_universe = sum(universes[i] for i in others)
    word = list(fixed)
    for chain in moving:
        word.extend(bridge(chain, moving_universe))
        word.extend(fixed)
    longest = len(chains[fixed_index])
    bound = total + (longest + 2) * width + longest + 1
    assert len(word) <= bound
    assert all(word)
    return word, desired, bound


def audit_words():
    cases = 0
    for block_sizes in ((2, 2, 2, 2), (2, 3, 2, 3), (3, 3, 3, 3), (4, 4, 4, 4)):
        universes = []
        decompositions = []
        offset = 0
        for size in block_sizes:
            universes.append(((1 << size) - 1) << offset)
            decompositions.append(scd([1 << i for i in range(offset, offset + size - 1)]))
            offset += size
        full = (1 << offset) - 1
        word = []
        bound = 0
        for chains in product(*decompositions):
            for tail_signs in product((0, 1), repeat=3):
                block, desired, local_bound = paired_box_word(chains, universes, (0,) + tail_signs)
                actual = unions(block)
                required = set()
                for target_tuple in product(*desired):
                    target = 0
                    for part in target_tuple:
                        target |= part
                    required.add(target)
                    required.add(full ^ target)
                assert required - {0} <= actual
                word.extend(block)
                bound += local_bound
                cases += 1
        assert unions(word) == set(range(1, full + 1))
        print(f"  block sizes={block_sizes}: n={len(word)}, bound={bound}, targets={full}")
    for a, b, c in product(range(1, 9), repeat=3):
        coefficients = [1]
        for side in (a, b, c):
            following = [0] * (len(coefficients) + side - 1)
            for i, value in enumerate(coefficients):
                for j in range(side):
                    following[i + j] += value
            coefficients = following
        assert max(coefficients) == width3(a, b, c)
    print(f"  paired boxes verified={cases}; exact width formulas verified=512")


def arctan_bounds(x, terms=40):
    value = F(0)
    power = x
    for j in range(terms):
        value += (-1) ** j * power / (2 * j + 1)
        power *= x * x
    following = value + (-1) ** terms * power / (2 * terms + 1)
    return min(value, following), max(value, following)


def pi_bounds():
    a, A = arctan_bounds(F(1, 5))
    b, B = arctan_bounds(F(1, 239))
    return 16 * a - 4 * B, 16 * A - 4 * b


def sqrt_bounds(x, scale=10 ** 20):
    integer = isqrt((x.numerator * scale * scale) // x.denominator)
    return F(integer, scale), F(integer + 1, scale)


def certify_three_block():
    pl, pu = pi_bounds()
    r2l, r2u = sqrt_bounds(F(2))
    r3l, r3u = sqrt_bounds(F(3))
    ql, qu = 3 - 2 * r2u, 3 - 2 * r2l
    al, _ = arctan_bounds(ql)
    _, au = arctan_bounds(qu)
    angle_lower, angle_upper = pl / 4 + al, pu / 4 + au
    lower = r3l / pu * (F(1, 3) + 3 / r2u * angle_lower)
    upper = r3u / pl * (F(1, 3) + 3 / r2l * angle_upper)
    assert upper < F(130107, 100000)
    print(f"Exact-rational three-block enclosure: {float(lower):.15f} .. {float(upper):.15f}")


def numerical_four_block(n):
    total = 0.0
    for i in range(n):
        x = (i + 0.5) / n
        for j in range(n):
            v = (j + 0.5) / n
            q = 1 + v * v * (1 + x * x)
            root = sqrt(q + 1)
            g = 105 / ((q + 1) ** 4 * root)
            h = (48 - (105*q**3 + 210*q*q + 168*q + 48) / ((q + 1) ** 3 * root)) / q**4
            p = x * v * v
            s = max(0.0, v * (x + 1) - 1) ** 2 / 4
            total += x * v ** 3 * ((2*p - s)*g + (p - s)*h)
    return 48 / pi * total / n ** 2


def certify_four_block(n):
    scale = 10 ** 16
    upper_sum = 0
    lower_sum = 0
    denominator = 2 * n
    for i in range(n):
        x = F(2 * i + 1, denominator)
        for j in range(n):
            v = F(2 * j + 1, denominator)
            q = 1 + v * v * (1 + x * x)
            root_lower, root_upper = sqrt_bounds(q + 1)
            polynomial = 105*q**3 + 210*q*q + 168*q + 48
            g_lower = 105 / ((q + 1) ** 4 * root_upper)
            g_upper = 105 / ((q + 1) ** 4 * root_lower)
            h_lower = (48 - polynomial / ((q + 1) ** 3 * root_lower)) / q**4
            h_upper = (48 - polynomial / ((q + 1) ** 3 * root_upper)) / q**4
            p = x * v * v
            s = max(F(0), v * (x + 1) - 1) ** 2 / 4
            factor = x * v ** 3
            lower = factor * ((2*p - s)*g_lower + (p - s)*h_lower)
            upper = factor * ((2*p - s)*g_upper + (p - s)*h_upper)
            assert 0 <= lower <= upper
            lower_sum += (lower.numerator * scale) // lower.denominator
            upper_sum += -((-upper.numerator * scale) // upper.denominator)
    # |H_xx| <= 644 and |H_vv| <= 2860 almost everywhere; H is C^1.
    error = F(146, n * n)
    integral_lower = F(lower_sum, scale * n * n) - error
    integral_upper = F(upper_sum, scale * n * n) + error
    pl, pu = pi_bounds()
    lower = 48 * integral_lower / pu
    upper = 48 * integral_upper / pl
    print(f"Certified four-block enclosure, n={n}: {float(lower):.12f} .. {float(upper):.12f}")
    if n >= 1024:
        assert upper < F(127, 100)
        print("Exact rational comparison: c4 < 127/100")
    elif n >= 512:
        assert upper < F(32, 25)
        print("Exact rational comparison: c4 < 32/25")
    return lower, upper


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--certify", type=int, default=0)
    args = parser.parse_args()
    audit_words()
    certify_three_block()
    for n in (64, 128, 256):
        print(f"Four-block midpoint diagnostic n={n}: {numerical_four_block(n):.12f}")
    if args.certify:
        certify_four_block(args.certify)


if __name__ == "__main__":
    main()
