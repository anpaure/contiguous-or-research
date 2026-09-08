"""Exact grouped-chain cylinder words and asymptotic cost diagnostics."""

from math import comb, erf, erfc, exp, pi, sqrt

from density_bridge_frontier_20260905_c71e4 import bridge, scd, simpson, unions


def extend_chain(chain, bits):
    chains = [chain]
    for bit in bits:
        following = []
        for current in chains:
            following.append(current + [current[-1] | bit])
            if len(current) > 1:
                following.append([x | bit for x in current[:-1]])
        chains = following
    return chains


def product_width(a, t):
    middle = (a - 1 + t) // 2
    return sum(comb(t, middle - j) for j in range(a)
               if 0 <= middle - j <= t)


def grouped_pair_word(c, d, p, q, bits):
    new_support = sum(bits)
    a, length_d = len(c), len(d)
    if a <= length_d:
        moving, universe = c, p | new_support
        fixed = bridge(d, q)
    else:
        moving, universe = d, q | new_support
        fixed = bridge(c, p)
    chains = extend_chain(moving, bits)
    m, maximum = sorted((a, length_d))
    assert len(chains) == product_width(m, len(bits))
    assert sum(map(len, chains)) == m * (1 << len(bits))
    word = list(fixed)
    for chain in chains:
        word.extend(bridge(chain, universe))
        word.extend(fixed)
    bound = (m * (1 << len(bits))
             + (maximum + 2) * product_width(m, len(bits)) + maximum + 1)
    assert all(word)
    assert len(word) <= bound
    return word, bound


def audit_words():
    pairs_checked = 0
    for b in range(2, 6):
        p, q = (1 << b) - 1, ((1 << b) - 1) << b
        left = scd([1 << i for i in range(b - 1)])
        right = scd([1 << i for i in range(b, 2 * b)])
        for t in range(5):
            bits = [1 << i for i in range(2 * b, 2 * b + t)]
            new_sets = [z << (2 * b) for z in range(1 << t)]
            word = []
            bound = 0
            for c in left:
                for d in right:
                    block, block_bound = grouped_pair_word(c, d, p, q, bits)
                    actual = unions(block)
                    required = {
                        target | z
                        for x in c for y in d for z in new_sets
                        for target in (x | (q ^ y), (p ^ x) | y)
                    } - {0}
                    assert required <= actual
                    word.extend(block)
                    bound += block_bound
                    pairs_checked += 1
            actual = unions(word)
            assert actual == set(range(1, 1 << (2 * b + t)))
            assert len(word) <= bound
            print(f"  b={b}, t={t}, k={2*b+t}: length={len(word)}, bound={bound}, targets={len(actual)}")
    return pairs_checked


def asymptotic_cost(lam, steps=8192):
    if lam == 0:
        return sqrt(2)

    def integrand(m):
        upper_tail = m * exp(-m * m / 2) + sqrt(pi / 2) * erfc(m / sqrt(2))
        return 2 * m * exp(-m * m / 2) * erf(m / (2 * sqrt(lam))) * upper_tail

    integral = simpson(integrand, 0.0, 12.0, steps)
    return sqrt(1 + lam) * (0.5 + integral / sqrt(pi))


def finite_bound_ratio(b, t):
    histogram = []
    for dimension in (b - 1, b):
        width = comb(dimension, dimension // 2)
        previous = 0
        row = []
        for bottom in range(dimension // 2 + 1):
            current = comb(dimension, bottom)
            row.append((dimension - 2 * bottom + 1, (current - previous) / width))
            previous = current
        histogram.append(row)
    cumulative = [0.0]
    for j in range(t + 1):
        cumulative.append(cumulative[-1] + comb(t, j) / (1 << t))
    probabilities = {}
    for a in range(1, b + 2):
        middle = (a - 1 + t) // 2
        probabilities[a] = cumulative[min(t, middle) + 1] - cumulative[max(0, middle - a + 1)]
    expectation = 0.0
    for a, probability_a in histogram[0]:
        for c, probability_c in histogram[1]:
            m, maximum = sorted((a, c))
            expectation += probability_a * probability_c * (
                m + (maximum + 2) * probabilities[m] + (maximum + 1) * 2.0 ** (-t))
    multiplier = ((1 << t) * comb(b - 1, (b - 1) // 2) * comb(b, b // 2)
                  / comb(2 * b + t, (2 * b + t) // 2))
    return multiplier * expectation


def main():
    print("Literal full-cube grouped repair audits:")
    print(f"Pair cylinders verified: {audit_words()}")
    print("Asymptotic cost diagnostics:")
    for lam in (0, 0.01, 0.05, 0.1, 0.2, 0.3, 0.5, 1.0, 2.0):
        print(f"  lambda={lam:.6f}: coefficient={asymptotic_cost(lam):.12f}")
    lo, hi = 0.01, 2.0
    for _ in range(55):
        a, b = (2 * lo + hi) / 3, (lo + 2 * hi) / 3
        if asymptotic_cost(a, 4096) < asymptotic_cost(b, 4096):
            hi = b
        else:
            lo = a
    lam = (lo + hi) / 2
    print(f"Numerical minimizer diagnostic: lambda={lam:.12f}, coefficient={asymptotic_cost(lam):.12f}")
    print("Finite upper-bound ledger at lambda=1/2:")
    for b in (32, 128, 512, 2048):
        print(f"  b={b}, t={b}: ratio={finite_bound_ratio(b, b):.12f}")


if __name__ == "__main__":
    main()
