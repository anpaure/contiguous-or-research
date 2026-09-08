"""Literal bridge-selection audits and dependency-free numerical quadrature.

The quadrature is diagnostic, not a rigorous numerical certificate. The
asymptotic constants in the companion note are defined by exact integrals.
"""

from itertools import product
from math import comb, cos, erf, erfc, exp, log, pi, sin, sqrt
from random import Random


def scd(bits):
    chains = [[0]]
    for bit in bits:
        following = []
        for chain in chains:
            following.append(chain + [chain[-1] | bit])
            if len(chain) > 1:
                following.append([x | bit for x in chain[:-1]])
        chains = following
    return chains


def bridge(chain, universe):
    return [x for x in [chain[0]]
            + [b ^ a for a, b in zip(chain, chain[1:])]
            + [universe ^ chain[-1]] if x]


def unions(word):
    found = set()
    suffixes = set()
    for letter in word:
        suffixes = {letter} | {x | letter for x in suffixes}
        found.update(suffixes)
    return found


def make_word(b, selected):
    p = (1 << b) - 1
    q = ((1 << b) - 1) << b
    left = scd([1 << i for i in range(b - 1)])
    right = scd([1 << i for i in range(b, 2 * b)])
    bridges = [bridge(c, p) for c in left] + [bridge(d, q) for d in right]
    offset = len(left)
    adjacency = [[] for _ in bridges]
    intended = set()
    primary = 0
    pairs = 0
    for i, c in enumerate(left):
        for j, d in enumerate(right):
            if not selected(i, j, len(c), len(d)):
                continue
            pairs += 1
            adjacency[i].append(offset + j)
            adjacency[offset + j].append(i)
            primary += len(bridges[i]) + len(bridges[offset + j])
            for x in c:
                for y in d:
                    intended.add(x | (q ^ y))
                    intended.add((p ^ x) | y)
    word = []
    components = 0
    seam_cost = 0
    for root in range(len(bridges)):
        if not adjacency[root]:
            continue
        stack = [root]
        reverse_circuit = []
        while stack:
            v = stack[-1]
            if adjacency[v]:
                stack.append(adjacency[v].pop())
            else:
                reverse_circuit.append(stack.pop())
        circuit = reverse_circuit[::-1]
        assert circuit[0] == circuit[-1]
        if word:
            word.append(p | q)
            seam_cost += 1
        for v in circuit:
            word.extend(bridges[v])
        seam_cost += len(bridges[root])
        components += 1
    assert len(word) == primary + seam_cost
    assert seam_cost <= (b + 2) * components
    assert len(intended) == 2 * sum(
        len(c) * len(d)
        for i, c in enumerate(left)
        for j, d in enumerate(right)
        if selected(i, j, len(c), len(d))
    )
    actual = unions(word)
    assert intended - {0} <= actual
    proper = lambda s: 0 < (s & p) < p and 0 < (s & q) < q
    assert {s for s in actual if proper(s)} == {
        s for s in intended if proper(s)
    }
    assert abs(len(actual) - len(intended)) <= 4 * (1 << b)
    return len(word), len(actual), pairs, components


def simpson(function, lo, hi, steps):
    assert steps % 2 == 0
    step = (hi - lo) / steps
    value = function(lo) + function(hi)
    value += 4 * sum(function(lo + j * step) for j in range(1, steps, 2))
    value += 2 * sum(function(lo + j * step) for j in range(2, steps, 2))
    return value * step / 3


def profile(tau, steps=4096):
    def integrand(theta, density):
        x, y = cos(theta), sin(theta)
        if min(x, y) < 1e-14:
            return 0.0
        lower = tau * (x + y) / (x * y)
        if lower > 40:
            return 0.0
        gaussian = exp(-lower * lower / 2)
        if density:
            radial = (lower ** 4 + 4 * lower * lower + 8) * gaussian
            return (2 / pi) * x * x * y * y * radial
        radial = ((lower ** 3 + 3 * lower) * gaussian
                  + 3 * sqrt(pi / 2) * erfc(lower / sqrt(2)))
        return (x + y) * x * y * radial / sqrt(pi)

    return tuple(simpson(lambda theta: integrand(theta, density),
                         0.0, pi / 2, steps)
                 for density in (False, True))


def find_threshold(steps):
    lo, hi = 0.0, 2.0
    for _ in range(45):
        mid = (lo + hi) / 2
        if profile(mid, steps)[0] > 1:
            lo = mid
        else:
            hi = mid
    tau = (lo + hi) / 2
    return tau, profile(tau, steps)


def finite_histogram_profile(b, tau):
    histograms = []
    for dimension in (b - 1, b):
        width = comb(dimension, dimension // 2)
        previous = 0
        histogram = []
        for bottom in range(dimension // 2 + 1):
            current = comb(dimension, bottom)
            histogram.append((dimension - 2 * bottom + 1,
                              (current - previous) / width))
            previous = current
        histograms.append(histogram)
    length = area = 0.0
    for a, probability_a in histograms[0]:
        for c, probability_c in histograms[1]:
            if a * c / (a + c) > tau * sqrt(b):
                probability = probability_a * probability_c
                length += probability * (a + c)
                area += probability * a * c
    pairs = comb(b - 1, (b - 1) // 2) * comb(b, b // 2)
    return length * (pairs / comb(2 * b, b)), area * (2 * pairs / (1 << (2 * b)))


def audit_tensor():
    rng = Random(161803)
    cases = 0
    for periods in ((2, 3), (3, 4), (2, 3, 5)):
        for _ in range(20):
            factors = [[rng.randrange(1, 4) << (2 * i) for _ in range(period)]
                       for i, period in enumerate(periods)]
            size = 1
            for period in periods:
                size *= period
            word = []
            for time in range(size):
                mask = 0
                for factor in factors:
                    mask |= factor[time % len(factor)]
                word.append(mask)
            predicted = set()
            for length in range(1, max(periods) + 1):
                decks = []
                for factor in factors:
                    deck = set()
                    for start in range(len(factor)):
                        mask = 0
                        for offset in range(length):
                            mask |= factor[(start + offset) % len(factor)]
                        deck.add(mask)
                    decks.append(deck)
                for target_tuple in product(*decks):
                    mask = 0
                    for target in target_tuple:
                        mask |= target
                    predicted.add(mask)
            assert predicted == unions(word + word)
            cases += 1
    return cases


def max_unions(word):
    found = set()
    suffixes = set()
    for letter in word:
        suffixes = {letter} | {
            tuple(max(a, b) for a, b in zip(letter, value))
            for value in suffixes
        }
        found.update(suffixes)
    return found


def audit_plateau():
    rng = Random(20260905)
    cases = 0
    for p, q, r in [(1, 1, 3), (1, 2, 5), (2, 2, 6), (2, 3, 8)]:
        potential = p + q
        height = r - potential
        width = (p + 1) * (q + 1)
        points = list(product(range(p + 1), range(q + 1), range(r + 1)))
        for _ in range(100):
            n = rng.randrange(1, 3 * width)
            word = [rng.choice(points) for _ in range(n)]
            actual = max_unions(word)
            missing = [sum((x, y, potential + j - x - y) not in actual
                           for x in range(p + 1) for y in range(q + 1))
                       for j in range(height + 1)]
            for a in range(height):
                for b in range(a + 1, height + 1):
                    distance = b - a
                    rhs = (2 * (distance + potential) * (n - width)
                           + 4 * sum(missing[a:b + 1])
                           + 2 * (potential - 1) * (missing[a] + missing[b]))
                    assert distance * width <= rhs
                    cases += 1
    return cases


def audit_fixed_split():
    rng = Random(271828)
    cases = 0
    for b in range(2, 5):
        p = (1 << b) - 1
        q = p << b
        for _ in range(80):
            word = []
            for block in range(rng.randrange(1, 8)):
                half = p if block % 2 == 0 else q
                letters = []
                total = 0
                for _ in range(rng.randrange(1, b + 2)):
                    letter = rng.randrange(1, p + 1)
                    if half == q:
                        letter <<= b
                    letters.append(letter)
                    total |= letter
                letters[-1] |= half ^ total
                word.extend(letters)
            actual = unions(word)
            holes = ((1 << (2 * b)) - 1) - len(actual)
            for lo in range(1, b):
                for hi in range(lo, b):
                    rank_sum = sum(comb(b, s) for s in range(lo, hi + 1))
                    assert holes >= ((1 << b) - 2) * rank_sum - (hi - lo + 1) * len(word)
                    cases += 1
    return cases


def main():
    print("Numerical integral diagnostics (not interval-certified):")
    for steps in (2048, 8192):
        tau, (cost, density) = find_threshold(steps)
        print(f"  steps={steps}: tau={tau:.12f}, cost={cost:.12f}, density={density:.12f}")
    assert abs(profile(0)[0] - sqrt(2)) < 1e-10
    assert abs(profile(0)[1] - 1) < 1e-10
    wall = erf(sqrt(log(sqrt(2)))) - sqrt(2 / pi) * sqrt(log(sqrt(2)))
    print(f"Full-half block hole-density lower bound at cost one: {wall:.12f}")
    print("Finite SCD histogram limits (principal length, intended density):")
    for b in (32, 128, 512, 2048):
        cost, density = finite_histogram_profile(b, tau)
        print(f"  b={b}: cost={cost:.9f}, density={density:.9f}")
    exhaustive = 0
    for b in (2, 3):
        columns = comb(b, b // 2)
        edges = comb(b - 1, (b - 1) // 2) * columns
        for mask in range(1 << edges):
            make_word(b, lambda i, j, a, c: bool(mask & (1 << (i * columns + j))))
            exhaustive += 1
    print(f"All edge selections audited in b=2,3: {exhaustive}")
    print("Literal selected-edge bridge audits:")
    rng = Random(314159)
    for b in range(2, 7):
        a_count = comb(b - 1, (b - 1) // 2)
        c_count = comb(b, b // 2)
        chosen = {(i, j) for i in range(a_count) for j in range(c_count)
                  if rng.random() < 0.45}
        for label, selector in [
            ("threshold", lambda i, j, a, c: a * c / (a + c) > tau * sqrt(b)),
            ("random", lambda i, j, a, c: (i, j) in chosen),
        ]:
            n, covered, pairs, components = make_word(b, selector)
            print(f"  b={b}, {label}: n={n}, targets={covered}, pairs={pairs}, components={components}")
    print(f"Plateau inequalities checked: {audit_plateau()}")
    print(f"Fixed-split density inequalities checked: {audit_fixed_split()}")
    print(f"Exact synchronous tensor identities checked: {audit_tensor()}")


if __name__ == "__main__":
    main()
