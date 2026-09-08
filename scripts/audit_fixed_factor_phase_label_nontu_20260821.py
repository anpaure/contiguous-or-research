#!/usr/bin/env python3
"""Exact finite certificate for the b=5 fixed-factor non-TU note."""

from collections import Counter
from fractions import Fraction
from itertools import combinations, product


B = 5
ORDERS = ((0, 1, 2, 3, 4), (0, 2, 4, 1, 3))
SCHEDULE = "AABBB"


def deck(order, length):
    return {
        frozenset(order[(start + step) % B] for step in range(length))
        for start in range(B)
    }


def word(i, j, theta):
    alpha, beta = ORDERS[i], ORDERS[j]
    ia = ib = 0
    out = []
    for pos in range(B * B):
        if SCHEDULE[pos % B] == "A":
            out.append(("A", alpha[ia % B]))
            ia += 1
        else:
            out.append(("B", beta[(ib + theta) % B]))
            ib += 1
    return out


def windows(sequence, length):
    return [
        frozenset(sequence[(start + step) % (B * B)] for step in range(length))
        for start in range(B * B)
    ]


all_pairs = {frozenset(pair) for pair in combinations(range(B), 2)}
all_triples = {frozenset(triple) for triple in combinations(range(B), 3)}
assert deck(ORDERS[0], 2).isdisjoint(deck(ORDERS[1], 2))
assert deck(ORDERS[0], 2) | deck(ORDERS[1], 2) == all_pairs
assert deck(ORDERS[0], 3).isdisjoint(deck(ORDERS[1], 3))
assert deck(ORDERS[0], 3) | deck(ORDERS[1], 3) == all_triples

# All four order pairs partition the 100 split-(2,3) middle targets.
middle = []
for i in range(2):
    for j in range(2):
        current = windows(word(i, j, 0), 5)
        assert len(set(current)) == 25
        assert all(sum(side == "A" for side, _ in target) == 2 for target in current)
        middle.extend(current)
assert len(middle) == 100
assert len(set(middle)) == 100

# Every origin candidate is internally simple at q=1.
for i in range(2):
    for j in range(2):
        for theta in range(B):
            current = windows(word(i, j, theta), 6)
            assert all(len(target) == 6 for target in current)
            assert len(set(current)) == 25

v1 = frozenset(
    (("A", 0), ("A", 1), ("B", 0), ("B", 1), ("B", 2), ("B", 3))
)
v2 = frozenset(
    (("A", 0), ("A", 1), ("B", 0), ("B", 1), ("B", 2), ("B", 4))
)
columns = ((0, 0, 3), (0, 0, 0), (0, 1, 1))
upper = [set(windows(word(*column), 6)) for column in columns]

matrix = [
    [int((i, j) == (0, 0)) for i, j, theta in columns],
    [int(v1 in targets) for targets in upper],
    [int(v2 in targets) for targets in upper],
]
assert matrix == [[1, 1, 0], [1, 0, 1], [0, 1, 1]]

det = (
    matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
    - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
    + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])
)
assert det == -2

common = upper[0] & upper[1] & upper[2]
assert len(common) == 3
loads = Counter(target for targets in upper for target in targets)
assert sum(multiplicity == 3 for multiplicity in loads.values()) == 3

# Exact complete fixed-q LP gap.
items = tuple((i, j) for i in range(2) for j in range(2))
candidates = tuple((i, j, theta) for i, j in items for theta in range(B))
target_sets = {
    candidate: set(windows(word(*candidate), 6)) for candidate in candidates
}

compatibility_counts = {}
for left, right in combinations(items, 2):
    compatibility_counts[left, right] = sum(
        target_sets[left + (theta,)].isdisjoint(target_sets[right + (phi,)])
        for theta in range(B)
        for phi in range(B)
    )
assert compatibility_counts == {
    ((0, 0), (0, 1)): 0,
    ((0, 0), (1, 0)): 25,
    ((0, 0), (1, 1)): 25,
    ((0, 1), (1, 0)): 25,
    ((0, 1), (1, 1)): 25,
    ((1, 0), (1, 1)): 0,
}

for i in range(2):
    target_multiplicities = Counter()
    family = set().union(
        *(target_sets[i, j, theta] for j in range(2) for theta in range(B))
    )
    for target in family:
        vector = tuple(
            sum(target in target_sets[i, j, theta] for theta in range(B))
            for j in range(2)
        )
        target_multiplicities[vector] += 1
    assert target_multiplicities == Counter({(2, 0): 25, (3, 3): 25, (0, 2): 25})

fractional_weights = {
    (i, j, theta): Fraction(1, 5) if j == 0 else Fraction(2, 15)
    for i, j, theta in candidates
}
assert all(
    sum(fractional_weights[i, j, theta] for theta in range(B)) <= 1
    for i, j in items
)
all_upper_targets = set().union(*target_sets.values())
assert all(
    sum(
        fractional_weights[candidate]
        for candidate in candidates
        if target in target_sets[candidate]
    )
    <= 1
    for target in all_upper_targets
)
assert sum(fractional_weights.values()) == Fraction(10, 3)

integral_optimum = 0
for origins in product(range(-1, B), repeat=len(items)):
    chosen = [
        item + (theta,)
        for item, theta in zip(items, origins)
        if theta >= 0
    ]
    if all(
        target_sets[left].isdisjoint(target_sets[right])
        for left, right in combinations(chosen, 2)
    ):
        integral_optimum = max(integral_optimum, len(chosen))
assert integral_optimum == 2

c, cp, d = ORDERS[0], ORDERS[1], (0, 2, 1, 3, 4)
assert deck(c, 2).isdisjoint(deck(cp, 2))
assert deck(d, 2) & deck(c, 2) == {
    frozenset((1, 2)),
    frozenset((3, 4)),
    frozenset((0, 4)),
}
assert deck(d, 2) & deck(cp, 2) == {
    frozenset((0, 2)),
    frozenset((1, 3)),
}


def walecki(block_size):
    half = (block_size - 1) // 2
    modulus = 2 * half
    infinity = modulus
    cycles = []
    for shift in range(half):
        cycle = [infinity, shift]
        for distance in range(1, half):
            cycle.extend(
                ((shift - distance) % modulus, (shift + distance) % modulus)
            )
        cycle.append((shift - half) % modulus)
        assert len(cycle) == block_size
        cycles.append(tuple(cycle))
    return tuple(cycles)


def generic_deck(order, length):
    block_size = len(order)
    return {
        frozenset(order[(start + step) % block_size] for step in range(length))
        for start in range(block_size)
    }


def generic_word(alpha, beta, theta):
    block_size = len(alpha)
    schedule = "AA" + "B" * (block_size - 2)
    ia = ib = 0
    out = []
    for position in range(block_size * block_size):
        if schedule[position % block_size] == "A":
            out.append(("A", alpha[ia % block_size]))
            ia += 1
        else:
            out.append(("B", beta[(ib + theta) % block_size]))
            ib += 1
    return out


def generic_windows(sequence, length):
    period = len(sequence)
    return [
        frozenset(sequence[(start + step) % period] for step in range(length))
        for start in range(period)
    ]


# Replay the arbitrary-odd-b formula on several larger exact Walecki banks.
for block_size in (5, 7, 9, 11, 13):
    cycles = walecki(block_size)
    factor_size = (block_size - 1) // 2
    edge_occurrences = [
        edge for cycle in cycles for edge in generic_deck(cycle, 2)
    ]
    assert len(edge_occurrences) == block_size * (block_size - 1) // 2
    assert len(set(edge_occurrences)) == len(edge_occurrences)

    bank = {
        (i, j, theta): set(
            generic_windows(
                generic_word(cycles[i], cycles[j], theta), block_size + 1
            )
        )
        for i in range(factor_size)
        for j in range(factor_size)
        for theta in range(block_size)
    }
    assert all(len(targets) == block_size * block_size for targets in bank.values())
    assert all(
        Counter(sum(side == "A" for side, _ in target) for target in targets)
        == Counter({2: block_size * (block_size - 2), 3: 2 * block_size})
        for targets in bank.values()
    )

    for i in range(factor_size):
        split_two = {
            target
            for j in range(factor_size)
            for theta in range(block_size)
            for target in bank[i, j, theta]
            if sum(side == "A" for side, _ in target) == 2
        }
        assert len(split_two) == block_size * block_size
        assert all(
            sum(
                target in bank[i, j, theta]
                for theta in range(block_size)
            )
            == block_size - 2
            for j in range(factor_size)
            for target in split_two
        )
        assert all(
            bank[i, j, theta] & bank[i, k, phi]
            for j, k in combinations(range(factor_size), 2)
            for theta in range(block_size)
            for phi in range(block_size)
        )

    target_unions = [
        set().union(
            *(
                bank[i, j, theta]
                for j in range(factor_size)
                for theta in range(block_size)
            )
        )
        for i in range(factor_size)
    ]
    assert all(
        target_unions[i].isdisjoint(target_unions[j])
        for i, j in combinations(range(factor_size), 2)
    )
    generic_weight = Fraction(1, factor_size * (block_size - 2))
    assert block_size * generic_weight <= 1
    generic_targets = set().union(*bank.values())
    assert all(
        sum(generic_weight for targets in bank.values() if target in targets) <= 1
        for target in generic_targets
    )
    generic_lp = Fraction(factor_size * block_size, block_size - 2)
    assert len(bank) * generic_weight == generic_lp
    assert generic_lp > factor_size

print("PASS")
print("middle targets: 100/100 distinct")
print("all 20 q=1 origin candidates: 25/25 targets distinct")
print("minor:", matrix, "determinant:", det)
print("three-column common upper targets:", len(common))
print("complete fixed-q LP/integer optima: 10/3 and", integral_optimum)
print("integrality gap: 5/3")
print("factor exchange witness: PASS")
print("odd-b Walecki gap family through b=13: PASS")
