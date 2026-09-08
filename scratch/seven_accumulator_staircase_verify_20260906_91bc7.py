"""Exact checks for the new six-staircase terminal / seven-accumulator policy.

No Brownian simulation or numerical quadrature is a premise of these checks.
"""

from fractions import Fraction
from itertools import product
from math import comb, prod
from random import Random

from six_staircase_cover_20260906_91bc7 import (
    COVER, best_staircase_chains, finite_principal, path_staircase_chains,
    rectangle_chains,
)


def product_chains(left, right):
    return [[left[i] | right[j] for i, j in chain]
            for chain in rectangle_chains(len(left), len(right))]


def bridge(chain, support):
    values = [chain[0]]
    values += [b & ~a for a, b in zip(chain, chain[1:])]
    values.append(support & ~chain[-1])
    values = [x for x in values if x]
    assert len(chain) <= len(values) <= len(chain) + 1
    return values


def terminal_rectangles(slots):
    ordered = sorted(enumerate(slots), key=lambda item: (len(item[1][0]), item[0]))
    small, small_support = ordered[0][1]
    large = [item[1] for item in ordered[1:]]
    lengths = tuple(len(chain) for chain, _ in large)
    cuts = tuple(a // 2 for a in lengths)
    for pair in COVER:
        families = []
        for indices in pair:
            local = tuple(lengths[i] for i in indices)
            thresholds = tuple(cuts[i] for i in indices)
            points = best_staircase_chains(local, thresholds)
            families.append(([
                [large[indices[0]][0][x] | large[indices[1]][0][y]
                 | large[indices[2]][0][z] for x, y, z in chain]
                for chain in points
            ], sum(large[i][1] for i in indices)))
        (left, u), (right, v) = families
        for chain in left:
            for child in product_chains(chain, small):
                for other in right:
                    yield child, u | small_support, other, v


def consume(slots, unread):
    if not unread:
        yield slots
        return
    i = min(range(7), key=lambda j: (len(slots[j][0]), j))
    old, old_support = slots[i]
    following, support = unread[0]
    for child in product_chains(old, following):
        next_slots = list(slots)
        next_slots[i] = (child, old_support | support)
        yield from consume(next_slots, unread[1:])


def interval_unions(word):
    seen, suffixes = set(), set()
    for x in word:
        assert x
        suffixes = {x} | {old | x for old in suffixes}
        seen.update(suffixes)
    return seen


def assemble(rectangles, dimension):
    indices, vertices, adjacency = {}, [], []
    principal = endpoint = edges = 0

    def vertex(chain, support):
        key = (support, tuple(chain))
        if key not in indices:
            indices[key] = len(vertices)
            vertices.append(bridge(chain, support))
            adjacency.append([])
        return indices[key]

    for c, u, d, v in rectangles:
        assert not u & v and u | v == (1 << dimension) - 1
        dc = [v ^ x for x in reversed(d)]
        a, b = vertex(c, u), vertex(dc, v)
        adjacency[a].append(b)
        adjacency[b].append(a)
        principal += len(c) + len(d)
        endpoint += len(vertices[a]) + len(vertices[b]) - len(c) - len(d)
        edges += 1
    word, closing, components, arcs = [], 0, 0, 0
    for root in range(len(vertices)):
        if not adjacency[root]:
            continue
        stack, reverse = [root], []
        while stack:
            at = stack[-1]
            if adjacency[at]:
                stack.append(adjacency[at].pop())
            else:
                reverse.append(stack.pop())
        path = reverse[::-1]
        assert path[0] == path[-1] == root
        arcs += len(path) - 1
        for i in path:
            word.extend(vertices[i])
        closing += len(vertices[root])
        components += 1
    assert arcs == 2 * edges
    assert len(word) == principal + endpoint + closing
    assert 0 <= endpoint <= 2 * edges
    assert closing <= (dimension + 1) * len(vertices)
    return word, (principal, endpoint, closing, edges, len(vertices), components)


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


def full_cube(sizes):
    dimension = sum(sizes)
    banks, supports = [], []
    start = 0
    for size in sizes:
        support = ((1 << size) - 1) << start
        banks.append(scd([1 << i for i in range(start, start + size - 1)]))
        supports.append(support)
        start += size

    def rectangles():
        for originals in product(*banks):
            for signs in product((0, 1), repeat=len(sizes) - 1):
                desired = [([support ^ x for x in reversed(chain)] if sign else chain,
                            support)
                           for chain, support, sign in zip(originals, supports, (0,) + signs)]
                for slots in consume(desired[:7], desired[7:]):
                    yield from terminal_rectangles(slots)

    word, ledger = assemble(rectangles(), dimension)
    assert interval_unions(word) == set(range(1, 1 << dimension))
    print("FULL_CUBE_PASS", {"blocks": sizes, "k": dimension, "length": len(word),
                             "ledger_M_end_close_E_V_components": ledger}, flush=True)


def rational_certificate():
    operator = {0: Fraction(1)}
    for p in (1, 3, 5):
        following = {}
        for degree, value in operator.items():
            following[degree + 2] = following.get(degree + 2, 0) + value / (p * (p + 1))
            following[degree] = following.get(degree, 0) - value * p / (p + 1)
        operator = following
    assert operator == {6: Fraction(1, 720), 4: Fraction(-35, 720),
                        2: Fraction(259, 720), 0: Fraction(-225, 720)}
    assert -120 * operator[4] == Fraction(35, 6)
    assert -20 * operator[2] == Fraction(-259, 36)
    assert -operator[0] == Fraction(5, 16)

    def arctan_bounds(q, terms):
        value = sum((Fraction((-1) ** j, (2 * j + 1) * q ** (2 * j + 1))
                     for j in range(terms)), Fraction(0))
        following = Fraction((-1) ** terms, (2 * terms + 1) * q ** (2 * terms + 1))
        return min(value, value + following), max(value, value + following)

    a, b = arctan_bounds(5, 40)
    c, d = arctan_bounds(239, 8)
    lo, hi = 16 * a - 4 * d, 16 * b - 4 * c
    lower = (225 * lo ** 6 - 2590 * hi ** 4 + 4200 * lo ** 2) / 4608
    upper = (225 * hi ** 6 - 2590 * lo ** 4 + 4200 * hi ** 2) / 4608
    assert Fraction(1188229, 1000000) < lower <= upper < Fraction(11883, 10000)
    assert Fraction(275, 192) < Fraction(1197, 1000) ** 2
    print("EXACT_CONSTANT_PASS", {"lower": float(lower), "upper": float(upper),
                                  "proved_upper": "11883/10000"}, flush=True)


def structural_checks():
    rank_occurrences = [0] * 7
    multiplicities = []
    for bits in product((0, 1), repeat=6):
        count = sum(all(bits[a] >= bits[b] >= bits[c] for a, b, c in pair)
                    for pair in COVER)
        assert count >= 1
        rank_occurrences[sum(bits)] += count
        multiplicities.append(count)
    assert rank_occurrences == [5, 10, 15, 20, 15, 10, 5]
    assert sum(x - 1 for x in multiplicities) == 16
    rng = Random(906917)
    cases = 0
    for size in range(2, 7):
        for _ in range(30):
            u = [rng.randrange(1, 3) for _ in range(size + 1)]
            lengths = [a + b for a, b in zip(u, u[1:])]
            chains = path_staircase_chains(lengths, u[:-1])
            expected = prod(u[1:-1])
            assert len(chains) == expected
            assert sum(map(len, chains)) == expected * sum(u)
            flat = [point for chain in chains for point in chain]
            support = {point for point in product(*(range(a) for a in lengths))
                       if all((point[i] >= u[i]) >= (point[i + 1] >= u[i + 1])
                              for i in range(size - 1))}
            assert len(flat) == len(set(flat)) and set(flat) == support
            total_rank = sum(a - 1 for a in lengths)
            assert all(sum(chain[0]) + sum(chain[-1]) == total_rank for chain in chains)
            assert all(all(sum(y) == sum(x) + 1 for x, y in zip(chain, chain[1:]))
                       for chain in chains)
            cases += 1
    radii, histories = [0] * 7, [0] * 7
    step_bound = 0
    for _ in range(100000):
        i = min(range(7), key=lambda j: (radii[j], j))
        previous = radii[i]
        radii[i] = abs(previous + rng.randrange(-9, 10))
        step_bound = max(step_bound, abs(radii[i] - previous))
        histories[i] = max(histories[i], radii[i])
        ordered = sorted(radii)
        largest = ordered[-1]
        assert largest == max(histories)
        assert largest - ordered[1] <= step_bound
        assert all(largest - step_bound <= x <= largest for x in histories)
    for a in (2, 4, 6, 8):
        assert finite_principal((a,) * 6, (a // 2,) * 6) == 5 * a ** 5 // 4
    print("STRUCTURE_PASS", {"balanced_paths": cases, "minimum_updates": 100000,
                              "rank_occurrences": rank_occurrences}, flush=True)


def volume_checks():
    rng = Random(917907)

    def charge(slots, unread):
        if not unread:
            r, *large = sorted(slots)
            return r * finite_principal(large, [a // 2 for a in large])
        i = min(range(7), key=lambda j: (slots[j], j))
        a, b = slots[i], unread[0]
        result = 0
        for r in range(abs(a - b) + 1, a + b, 2):
            following = list(slots)
            following[i] = r
            result += charge(following, unread[1:])
        return result

    def expected(slots, unread):
        if not unread:
            _, *large = sorted(slots)
            return Fraction(finite_principal(large, [a // 2 for a in large]), prod(large))
        i = min(range(7), key=lambda j: (slots[j], j))
        a, b = slots[i], unread[0]
        result = Fraction(0)
        for r in range(abs(a - b) + 1, a + b, 2):
            following = list(slots)
            following[i] = r
            result += Fraction(r, a * b) * expected(following, unread[1:])
        return result

    cases = 0
    for n in range(7, 11):
        for _ in range(45):
            lengths = [rng.randrange(1, 5) for _ in range(n)]
            assert Fraction(charge(lengths[:7], lengths[7:]), prod(lengths)) == expected(
                lengths[:7], lengths[7:])
            cases += 1
    print("VOLUME_NORMALIZATION_PASS", cases, flush=True)


def terminal_checks():
    rng = Random(917906)
    for trial in range(35):
        lengths = [rng.randrange(1, 5) for _ in range(7)]
        if trial < 6:
            lengths = [trial % 2 + 1] + [2] * 6
        slots = []
        bit = 0
        for a in lengths:
            support = 1 << bit
            chain = [support]
            bit += 1
            for _ in range(a - 1):
                support |= 1 << bit
                chain.append(support)
                bit += 1
            support |= 1 << bit
            bit += 1
            slots.append((chain, support))
        rectangles = list(terminal_rectangles(slots))
        principal = sum(len(c) + len(d) for c, _, d, _ in rectangles)
        r, *large = sorted(lengths)
        bound = r * finite_principal(large, [a // 2 for a in large])
        assert principal <= bound
        if lengths[1:] == [2] * 6 and lengths[0] <= 2:
            assert principal == 40 * lengths[0]
        word, ledger = assemble(rectangles, bit)
        assert ledger[0] == principal
        full = (1 << bit) - 1
        required = set()
        for points in product(*(chain for chain, _ in slots)):
            value = 0
            for x in points:
                value |= x
            required.update((value, full ^ value))
        assert required <= interval_unions(word)
    print("TERMINAL_LITERAL_PASS", 35, flush=True)


if __name__ == "__main__":
    rational_certificate()
    structural_checks()
    volume_checks()
    terminal_checks()
    for sizes in [(2,) * 7, (2,) * 8, (2,) * 9,
                  (2,) * 6 + (3,), (2,) * 5 + (3, 3), (2,) * 7 + (3,)]:
        full_cube(sizes)
