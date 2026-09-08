"""Literal and arithmetic checks for the c7e42 packet-selector note."""

from collections import Counter
from fractions import Fraction
from itertools import permutations, product
from math import comb, exp, fsum, log, log1p, pi, sqrt
from random import Random


def packet(label, b, h):
    z = label[:-1]
    n = 2 * b - 1
    low, high, length = b - h, b + h, b + 1
    assert len(z) == n and len(set(label)) == 2 * b

    def arc(start, size):
        result = 0
        for j in range(size):
            result |= 1 << z[(start + j) % n]
        return result

    supports = {
        s: {arc(a, s) for a in range(length)}
        for s in range(low, high + 1)
    }
    block = [arc(j, low) for j in range(length + 2 * h)]
    assert all(len(support) == length for support in supports.values())
    for a in range(length):
        for s in range(low, high + 1):
            union = 0
            for letter in block[a : a + s - low + 1]:
                union |= letter
            assert union == arc(a, s)
    return block, supports


def literal_support(word):
    # The distinct suffix unions at one endpoint form an inclusion chain.
    suffixes, result = set(), set()
    for letter in word:
        suffixes = {letter} | {old | letter for old in suffixes}
        result.update(suffixes)
    by_rank = {}
    for target in result:
        by_rank.setdefault(target.bit_count(), set()).add(target)
    return by_rank


def check_words_and_energy():
    rng = Random(0xC7E42)
    words = 0
    for b in range(3, 11):
        for h in sorted({1, min(3, b - 2), b - 2}):
            for t in (1, 2, 4):
                labels = []
                for i in range(t):
                    label = list(range(2 * b))
                    rng.shuffle(label)
                    labels.append(tuple(label))
                if t == 4:
                    labels[-1] = labels[0]
                blocks, supports = zip(*(packet(z, b, h) for z in labels))
                word = [letter for block in blocks for letter in block]
                actual = literal_support(word)
                length, mass = b + 1, t * (b + 1)
                assert len(word) == t * (length + 2 * h)
                designated_holes = 0
                energy_bound = Fraction(0)
                for s in range(b - h, b + h + 1):
                    counts = Counter(target for bank in supports for target in bank[s])
                    designated = set(counts)
                    assert designated <= actual.get(s, set())
                    extra = len(actual.get(s, set())) - len(designated)
                    bound = t * (b + h - s) + (t - 1) * (s - b + h + 1)
                    assert extra <= bound <= t * (2 * h + 1)
                    qvalue = sum(a * (a - 1) for a in counts.values())
                    pair_value = sum(
                        len(supports[i][s] & supports[j][s])
                        for i in range(t)
                        for j in range(t)
                        if i != j
                    )
                    assert qvalue == pair_value
                    size = comb(2 * b, s)
                    q = mass // size
                    floor_value = 2 * q * mass - q * (q + 1) * size
                    energy = qvalue - floor_value
                    assert energy >= 0
                    denominator = q * (q + 1) if q else 2
                    holes = size - len(designated)
                    rank_bound = max(size - mass, 0) + Fraction(energy, denominator)
                    assert holes <= rank_bound
                    energy_bound += rank_bound
                    designated_holes += holes
                far = sum(
                    comb(2 * b, s)
                    for s in range(1, 2 * b + 1)
                    if not b - h <= s <= b + h
                )
                holes = (1 << (2 * b)) - 1 - sum(map(len, actual.values()))
                assert designated_holes - t * (2 * h + 1) ** 2 <= holes
                assert holes <= designated_holes + far
                assert holes <= energy_bound + far
                words += 1
    print(f"Literal words, joins, repeated labels, and energy: {words} cases passed")


def check_scalar_energy():
    vectors = 0
    for n in range(1, 7):
        for loads in product(range(5), repeat=n):
            mass = sum(loads)
            q = mass // n
            qvalue = sum(a * (a - 1) for a in loads)
            floor_value = 2 * q * mass - q * (q + 1) * n
            energy = qvalue - floor_value
            assert energy == sum((a - q) * (a - q - 1) for a in loads)
            assert energy >= 0
            denominator = q * (q + 1) if q else 2
            assert loads.count(0) <= max(n - mass, 0) + Fraction(energy, denominator)
            balanced = [q + 1] * (mass - q * n) + [q] * (n - mass + q * n)
            assert sum(a * (a - 1) for a in balanced) == floor_value
            vectors += 1
    print(f"Scalar floor energy: {vectors} exhaustive vectors passed")


def check_pair_census():
    cases = 0
    for b in range(3, 26):
        n, length = 2 * b - 1, b + 1
        for s in range(1, n):
            arcs = [frozenset((a + j) % n for j in range(s)) for a in range(length)]
            actual = Counter(
                len(arcs[i] - arcs[j])
                for i in range(length)
                for j in range(length)
                if i != j
            )
            formula = Counter()
            for d in range(1, b + 1):
                distance = s - max(s - d, 0) - max(s - (n - d), 0)
                formula[distance] += 2 * (length - d)
            assert actual == formula
            assert sum(actual.values()) == length * (length - 1)
            assert actual[0] == 0
            cases += 1
    print(f"All-rank packet pair census: {cases} cases passed")


def check_conditional_expectation():
    b, h = 3, 1
    width = comb(2 * b, b)
    length, cost = b + 1, b + 1 + 2 * h
    t = width // cost
    ranks = range(b - h, b + h + 1)
    atlas = [(label, *packet(label, b, h)) for label in permutations(range(2 * b))]
    residual = {
        s: {mask for mask in range(1 << (2 * b)) if mask.bit_count() == s}
        for s in ranks
    }
    probability_miss = {s: 1 - Fraction(length, comb(2 * b, s)) for s in ranks}
    initial = sum(Fraction(len(residual[s])) * probability_miss[s] ** t for s in ranks)
    previous = initial
    word, chosen = [], []
    for j in range(t):
        scored = []
        for label, block, supports in atlas:
            score = sum(
                len(residual[s] - supports[s]) * probability_miss[s] ** (t - j - 1)
                for s in ranks
            )
            scored.append(score)
        assert sum(scored, Fraction(0)) / len(scored) == previous
        index = min(range(len(atlas)), key=lambda i: (scored[i], atlas[i][0]))
        label, block, supports = atlas[index]
        assert scored[index] <= previous
        previous = scored[index]
        for s in ranks:
            residual[s].difference_update(supports[s])
        chosen.append(label)
        word.extend(block)
    assert sum(map(len, residual.values())) <= initial
    assert len(word) == t * cost <= width
    actual = literal_support(word)
    holes = (1 << (2 * b)) - 1 - sum(map(len, actual.values()))
    print(
        f"Exact rational selector: length={len(word)}, width={width}, "
        f"designated band holes={sum(map(len, residual.values()))}, "
        f"bound={initial}, actual nonempty holes={holes}"
    )
    print(f"Selected six-coordinate labels: {chosen}")


def expectation_density(b, c=1.0):
    h = int(sqrt(2 * b * log(2 * b))) + 1
    assert h <= b - 2
    width = comb(2 * b, b)
    length, cost = b + 1, b + 1 + 2 * h
    # For this calibration c=1, so the position budget uses exact integers.
    assert c == 1.0
    t = width // cost
    mass_ratio = (length * t) / width
    terms = []
    for offset in range(-h, h + 1):
        size = comb(2 * b, b + offset)
        p = length / size
        mean = mass_ratio * (width / size)
        correction = -log1p(-p) / p if p else 1.0
        terms.append((size / (1 << (2 * b))) * exp(-mean * correction))
    return mass_ratio, fsum(terms)


def gaussian_calibration():
    subdivisions = 40000
    step = 6.0 / subdivisions
    value = 2 * step / sqrt(pi) * fsum(
        exp(-x * x - exp(x * x))
        for i in range(subdivisions)
        for x in ((i + 0.5) * step,)
    )
    print(f"Numerical Gaussian eta(1)={value:.12f}, coverage={1-value:.12f}")
    assert 0.2392687 < value < 0.2392689
    assert value <= exp(-1) / sqrt(2)
    for b in (51, 101, 251, 501, 1001, 2501):
        mass, holes = expectation_density(b)
        print(f"b={b}: M/W={mass:.9f}, exact designated expected hole density={holes:.9f}")


if __name__ == "__main__":
    check_words_and_energy()
    check_scalar_energy()
    check_pair_census()
    check_conditional_expectation()
    gaussian_calibration()
