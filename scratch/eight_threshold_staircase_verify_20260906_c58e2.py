"""Independent witness, staircase, padding, and literal compiler verification.

Only the explicit eight-bit witness is imported. No solver is needed, and
no code from the seven-accumulator theorem under audit is used.
"""

from collections import Counter
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from itertools import product
from math import comb, factorial, prod
from random import Random

from catalan_threshold_cover_20260906_c58e2 import COVER4


def binary_check():
    counts = Counter()
    for value in range(256):
        for a, b in COVER4:
            if all(all((value >> order[j] & 1) >= (value >> order[j + 1] & 1)
                       for j in range(3)) for order in (a, b)):
                counts[value] += 1
    assert len(COVER4) == 14 and set(counts) == set(range(256))
    occurrences = [sum(counts[x] for x in range(256) if x.bit_count() == r)
                   for r in range(9)]
    assert occurrences == [14, 28, 42, 56, 70, 56, 42, 28, 14]
    assert all(counts[x] == 1 for x in range(256) if 3 <= x.bit_count() <= 5)
    assert sum(v - 1 for v in counts.values()) == 94
    middle, lower, upper = [], [], []
    for a, b in COVER4:
        path = [sum(1 << x for x in a[:4 - j] + b[:j]) for j in range(5)]
        assert path[0] ^ path[-1] == 255
        assert all((x ^ y).bit_count() == 2 for x, y in zip(path, path[1:]))
        middle += path
        lower += [x & y for x, y in zip(path, path[1:])]
        upper += [x | y for x, y in zip(path, path[1:])]
    assert len(set(middle)) == 70
    assert len(set(lower)) == len(set(upper)) == 56
    encoding = bytes(x for pair in COVER4 for order in pair for x in order)
    print("BINARY_WITNESS_PASS", {"families": 14, "targets": 256,
                                  "rank_occurrences": occurrences,
                                  "coordinate_byte_sha256": sha256(encoding).hexdigest()}, flush=True)


@lru_cache(None)
def staircase(l, s):
    chains = [tuple((x,) for x in range(2 * s))]
    for _ in range(1, l):
        following = []
        for chain in chains:
            assert sum(x[-1] >= s for x in chain) == s
            length = len(chain)
            for j in range(s):
                points = [chain[i] + (j,) for i in range(length - j)]
                points += [chain[length - j - 1] + (y,) for y in range(j + 1, 2 * s)]
                following.append(tuple(points))
        chains = following
    return tuple(chains)


def staircase_check():
    tested = 0
    for l in range(1, 7):
        for s in range(1, 4):
            chains = staircase(l, s)
            flat = [x for chain in chains for x in chain]
            expected = {x for x in product(range(2 * s), repeat=l)
                        if all((x[i] >= s) >= (x[i + 1] >= s) for i in range(l - 1))}
            assert len(flat) == len(set(flat)) and set(flat) == expected
            assert len(chains) == s ** (l - 1)
            assert len(flat) == (l + 1) * s ** l
            assert min(map(len, chains)) == 2 * s + l - 1
            assert all(sum(c[0]) + sum(c[-1]) == l * (2 * s - 1) for c in chains)
            assert all(all(sum(y) == sum(x) + 1 and all(a <= b for a, b in zip(x, y))
                           for x, y in zip(c, c[1:])) for c in chains)
            polynomial = [1]
            for width in [s] * (l - 1) + [(l + 1) * s]:
                next_poly = [0] * (len(polynomial) + width - 1)
                for i, value in enumerate(polynomial):
                    for j in range(width):
                        next_poly[i + j] += value
                polynomial = next_poly
            rank_counts = Counter(map(sum, flat))
            assert polynomial == [rank_counts[i] for i in range(len(polynomial))]
            tested += 1
    print("ACTUAL_STAIRCASE_PARTITIONS_PASS", tested, flush=True)


def product_scd(left, right):
    a, b = len(left), len(right)
    for j in range(min(a, b)):
        yield ([left[i] | right[j] for i in range(a - j)]
               + [left[a - j - 1] | right[i] for i in range(j + 1, b)])


def distinct(chain):
    result = []
    for x in chain:
        if not result or x != result[-1]:
            result.append(x)
    return result


def terminal(slots):
    ordered = sorted(enumerate(slots), key=lambda x: (len(x[1][0]), x[0]))
    small, small_support = ordered[0][1]
    large = [x[1] for x in ordered[1:]]
    r = len(small)
    a = [len(chain) for chain, _ in large]
    padded = 2 * ((max(a) + 1) // 2)
    s = padded // 2
    pad_bound = r * 140 * s ** 7
    line_bound = r * (a[-1] + a[-2]) * prod(a[:-2])
    records = []
    if pad_bound <= line_bound:
        for pair in COVER4:
            families = []
            for indices in pair:
                images = []
                for chain in staircase(4, s):
                    image = []
                    for point in chain:
                        value = 0
                        for i, level in zip(indices, point):
                            value |= large[i][0][min(level, a[i] - 1)]
                        image.append(value)
                    images.append(distinct(image))
                families.append((images, sum(large[i][1] for i in indices)))
            (left, u), (right, v) = families
            for chain in left:
                for c in product_scd(chain, small):
                    records += [(c, u | small_support, d, v) for d in right]
        label = "padded"
    else:
        first, u = large[-1]
        moving, moving_support = large[-2]
        fixed = large[:-2]
        v = moving_support | sum(support for _, support in fixed)
        children = list(product_scd(first, small))
        for choice in product(*(chain for chain, _ in fixed)):
            constant = 0
            for x in choice:
                constant |= x
            d = [constant | x for x in moving]
            records += [(c, u | small_support, d, v) for c in children]
        label = "line"
    actual = sum(len(c) + len(d) for c, _, d, _ in records)
    bound = min(pad_bound, line_bound)
    assert actual <= bound
    if label == "line":
        assert actual == line_bound
    return records, bound, label


def bridge(chain, support):
    values = [chain[0]] + [b & ~a for a, b in zip(chain, chain[1:])]
    values.append(support & ~chain[-1])
    values = [x for x in values if x]
    assert len(chain) - 1 <= len(values) <= len(chain) + 1
    return values


def assemble(records, dimension):
    names, words, adjacency = {}, [], []
    main = edges = endpoint = 0

    def vertex(chain, support):
        key = support, tuple(chain)
        if key not in names:
            names[key] = len(words)
            words.append(bridge(chain, support))
            adjacency.append([])
        return names[key]

    for c, u, d, v in records:
        assert not u & v and u | v == (1 << dimension) - 1
        complement = [v ^ x for x in reversed(d)]
        i, j = vertex(c, u), vertex(complement, v)
        adjacency[i].append(j)
        adjacency[j].append(i)
        main += len(c) + len(d)
        endpoint += len(words[i]) + len(words[j]) - len(c) - len(d)
        edges += 1
    word, closing, components, traversed = [], 0, 0, 0
    for root in range(len(words)):
        if not adjacency[root]:
            continue
        stack, reverse = [root], []
        while stack:
            v = stack[-1]
            if adjacency[v]:
                stack.append(adjacency[v].pop())
            else:
                reverse.append(stack.pop())
        path = reverse[::-1]
        assert path[0] == path[-1] == root
        for v in path:
            word.extend(words[v])
        closing += len(words[root])
        traversed += len(path) - 1
        components += 1
    assert traversed == 2 * edges
    assert len(word) == main + endpoint + closing
    assert -2 * edges <= endpoint <= 2 * edges
    assert closing <= (dimension + 1) * len(words)
    return word, (main, endpoint, closing, edges, len(words), components)


def assemble_rows(records, dimension):
    rows = {}
    main = edges = 0
    for c, u, d, v in records:
        assert not u & v and u | v == (1 << dimension) - 1
        rows.setdefault((u, v, tuple(d)), []).append(c)
        main += len(c) + len(d)
        edges += 1
    word = []
    closing_allowance = 0
    for (u, v, d), left_chains in rows.items():
        fixed = bridge([v ^ x for x in reversed(d)], v)
        word.extend(fixed)
        closing_allowance += len(d) + 1
        for c in left_chains:
            word.extend(bridge(c, u))
            word.extend(fixed)
    assert len(word) <= main + 2 * edges + closing_allowance
    return word, (main, edges, closing_allowance)


def unions(word):
    seen, endings = set(), set()
    for x in word:
        assert x
        endings = {x} | {y | x for y in endings}
        seen.update(endings)
    return seen


def literal_terminal_checks():
    cases = [(1,) + (2,) * 8, (2,) * 9, (1, 3) + (4,) * 7,
             (1, 2, 2, 2, 2, 2, 2, 2, 8), (2, 2, 2, 3, 3, 3, 3, 3, 3)]
    kinds = Counter()
    for lengths in cases:
        slots, bit = [], 0
        for a in lengths:
            value = 1 << bit
            bit += 1
            chain = [value]
            for _ in range(a - 1):
                value |= 1 << bit
                bit += 1
                chain.append(value)
            support = value | (1 << bit)
            bit += 1
            slots.append((chain, support))
        records, bound, kind = terminal(slots)
        kinds[kind] += 1
        word, ledger = assemble(records, bit)
        full = (1 << bit) - 1
        required = set()
        for choice in product(*(chain for chain, _ in slots)):
            value = 0
            for x in choice:
                value |= x
            required.update((value, full ^ value))
        assert required <= unions(word)
        row_word, row_ledger = assemble_rows(records, bit)
        assert required <= unions(row_word)
        print("PADDED_TERMINAL_PASS", {"lengths": lengths, "branch": kind,
                                       "principal_bound": bound, "actual_main": ledger[0],
                                       "word_length": len(word), "row_word_length": len(row_word),
                                       "row_M_E_closing_bound": row_ledger}, flush=True)
    assert kinds["padded"] and kinds["line"]

    assert bridge([0, 1], 1) == [1]
    unpivoted = [([0, 1 << i], 1 << i) for i in range(9)]
    records, bound, _ = terminal(unpivoted)
    word, ledger = assemble(records, 9)
    row_word, row_ledger = assemble_rows(records, 9)
    assert ledger[0] == bound == 280 and ledger[1] == -28
    assert unions(word) == unions(row_word) == set(range(1, 512))
    print("EMPTY_FULL_ENDPOINT_AND_ROW_COMPILER_PASS",
          {"Euler_length": len(word), "ledger": ledger,
           "row_length": len(row_word), "row_ledger": row_ledger}, flush=True)


def consume(slots, unread):
    if not unread:
        yield slots
        return
    i = min(range(9), key=lambda j: (len(slots[j][0]), j))
    old, u = slots[i]
    following, v = unread[0]
    for child in product_scd(old, following):
        next_slots = list(slots)
        next_slots[i] = child, u | v
        yield from consume(next_slots, unread[1:])


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
    banks, supports, first = [], [], 0
    for size in sizes:
        banks.append(scd([1 << i for i in range(first, first + size - 1)]))
        supports.append(((1 << size) - 1) << first)
        first += size
    dimension = sum(sizes)
    bound = 0
    choices = Counter()

    def records():
        nonlocal bound
        for originals in product(*banks):
            for signs in product((0, 1), repeat=len(sizes) - 1):
                desired = [([support ^ x for x in reversed(chain)] if sign else chain, support)
                           for chain, support, sign in zip(originals, supports, (0,) + signs)]
                for slots in consume(desired[:9], desired[9:]):
                    pairs, charge, kind = terminal(slots)
                    bound += charge
                    choices[kind] += 1
                    yield from pairs

    word, ledger = assemble(records(), dimension)
    assert ledger[0] <= bound
    seen = bytearray(1 << dimension)
    endings = []
    for x in word:
        assert x
        following = [x]
        for y in endings:
            value = x | y
            if value != following[-1]:
                following.append(value)
        endings = following
        for value in endings:
            seen[value] = 1
    assert not seen[0] and seen.count(1) == (1 << dimension) - 1
    print("FULL_CUBE_PASS", {"blocks": sizes, "dimension": dimension, "length": len(word),
                             "bound": bound, "M_end_close_E_V_components": ledger,
                             "terminal_branches": dict(choices)}, flush=True)


def exact_constant():
    op = {0: Fraction(1)}
    for p in (1, 3, 5, 7):
        following = Counter()
        for degree, value in op.items():
            following[degree + 2] += value / (p * (p + 1))
            following[degree] -= value * p / (p + 1)
        op = dict(following)
    assert op == {8: Fraction(1, 40320), 6: Fraction(-84, 40320),
                  4: Fraction(1974, 40320), 2: Fraction(-12916, 40320),
                  0: Fraction(11025, 40320)}
    odd_moments = {1: Fraction(1, 4), 3: Fraction(1, 8),
                   5: Fraction(1, 4), 7: Fraction(17, 16)}
    coefficients = {8 - degree: -value * Fraction(factorial(7), factorial(7 - degree))
                    * odd_moments[7 - degree] * Fraction(35, 64)
                    for degree, value in op.items() if degree < 8}
    assert coefficients == {2: Fraction(735, 512), 4: Fraction(-11515, 4096),
                            6: Fraction(22603, 12288), 8: Fraction(-20825, 131072)}

    def atan_bounds(q, n):
        value = sum((Fraction((-1) ** j, (2 * j + 1) * q ** (2 * j + 1))
                     for j in range(n)), Fraction(0))
        next_term = Fraction((-1) ** n, (2 * n + 1) * q ** (2 * n + 1))
        return min(value, value + next_term), max(value, value + next_term)

    a, b = atan_bounds(5, 40)
    c, d = atan_bounds(239, 8)
    lo, hi = 16 * a - 4 * d, 16 * b - 4 * c
    lower = sum(value * (lo if value > 0 else hi) ** degree
                for degree, value in coefficients.items())
    upper = sum(value * (hi if value > 0 else lo) ** degree
                for degree, value in coefficients.items())
    assert Fraction(11807038038, 10 ** 10) < lower <= upper < Fraction(11807038039, 10 ** 10)
    assert upper < Fraction(118071, 100000)
    assert Fraction(5775, 4096) < Fraction(297, 250) ** 2
    print("EXACT_NINE_CLOCK_CONSTANT_PASS", {"lower": float(lower), "upper": float(upper),
                                             "proved_bound": "118071/100000"}, flush=True)


def clock_invariants():
    rng = Random(906583)
    radii = [0] * 9
    history = [0] * 9
    jump = 0
    for _ in range(100000):
        i = min(range(9), key=lambda j: (radii[j], j))
        old = radii[i]
        radii[i] = abs(old + rng.randrange(-10, 11))
        jump = max(jump, abs(radii[i] - old))
        history[i] = max(history[i], radii[i])
        order = sorted(radii)
        assert order[-1] == max(history)
        assert order[-1] - order[1] <= jump
        assert all(order[-1] - jump <= x <= order[-1] for x in history)
    print("NINE_CLOCK_DETERMINISTIC_INVARIANTS_PASS", 100000, flush=True)


def volume_check():
    rng = Random(906585)

    def upper(slots):
        r, *a = sorted(slots)
        s = (a[-1] + 1) // 2
        return r * min(140 * s ** 7, (a[-1] + a[-2]) * prod(a[:-2]))

    def evaluate(slots, unread, weighted):
        if not unread:
            value = upper(slots)
            return Fraction(value, prod(slots)) if weighted else value
        i = min(range(9), key=lambda j: (slots[j], j))
        a, b = slots[i], unread[0]
        result = Fraction(0) if weighted else 0
        for r in range(abs(a - b) + 1, a + b, 2):
            child = list(slots)
            child[i] = r
            value = evaluate(child, unread[1:], weighted)
            result += Fraction(r, a * b) * value if weighted else value
        return result

    cases = 0
    for n in range(9, 13):
        for _ in range(30):
            lengths = [rng.randrange(1, 5) for _ in range(n)]
            raw = evaluate(lengths[:9], lengths[9:], False)
            weighted = evaluate(lengths[:9], lengths[9:], True)
            assert Fraction(raw, prod(lengths)) == weighted
            cases += 1
    print("ACTUAL_VOLUME_NORMALIZATION_PASS", cases, flush=True)


if __name__ == "__main__":
    binary_check()
    staircase_check()
    exact_constant()
    clock_invariants()
    volume_check()
    literal_terminal_checks()
    for sizes in [(2,) * 9, (2,) * 10, (2,) * 8 + (3,), (2,) * 7 + (3, 3)]:
        full_cube(sizes)
