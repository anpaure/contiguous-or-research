#!/usr/bin/env python3
"""Finite checks for the microbank-orbit codegree note.

The proof in the note is symbolic.  This script independently simulates
the coherent FIFO tour, checks the endpoint distance counts, and verifies
the defect-one Johnson profile on small instances.
"""

from collections import Counter
from fractions import Fraction
from itertools import combinations, product
from math import comb, factorial, log2


def coherent_targets(b: int):
    """Return (empty pair, doubled pair, target) for the zero-state tour."""
    bits = [0] * b
    out = []
    for s in range(b):
        queue = [(s + i) % b for i in range(b)]
        current = {2 * j + bits[j] for j in range(b)}
        for k in range(1, b):
            doubled = (s + k) % b
            current.add(2 * doubled + (bits[doubled] ^ 1))
            front = queue.pop(0)
            current.remove(2 * front + bits[front])
            out.append((s, doubled, frozenset(current)))
            if front != s:
                bits[front] ^= 1

        # The boundary step is not a retained middle flag.
        current.add(2 * s + bits[s])
        front = queue.pop(0)
        current.remove(2 * front + bits[front])
        bits[front] ^= 1
        assert not queue
        assert current == {2 * j + bits[j] for j in range(b)}

    assert bits == [0] * b
    assert len(out) == b * (b - 1)
    assert len({target for _, _, target in out}) == len(out)
    return out


def coherent_lmu_targets(b: int):
    """Return the lower, middle, upper targets attached to one zero-state tour."""
    bits = [0] * b
    out = []
    for s in range(b):
        queue = [(s + i) % b for i in range(b)]
        current = {2 * j + bits[j] for j in range(b)}
        for k in range(1, b):
            doubled = (s + k) % b
            current.add(2 * doubled + (bits[doubled] ^ 1))
            front = queue.pop(0)
            current.remove(2 * front + bits[front])
            middle = frozenset(current)
            if front != s:
                bits[front] ^= 1

            following = set(current)
            if k < b - 1:
                next_pair = (s + k + 1) % b
                following.add(2 * next_pair + (bits[next_pair] ^ 1))
                next_front = queue[0]
                following.remove(2 * next_front + bits[next_front])
            else:
                following.add(2 * s + bits[s])
                next_front = queue[0]
                following.remove(2 * next_front + bits[next_front])
            following = frozenset(following)
            out.append(
                (
                    frozenset(middle & following),
                    middle,
                    frozenset(middle | following),
                )
            )

        current.add(2 * s + bits[s])
        front = queue.pop(0)
        current.remove(2 * front + bits[front])
        bits[front] ^= 1

    assert bits == [0] * b
    assert len(out) == b * (b - 1)
    for rank_index in range(3):
        assert len({row[rank_index] for row in out}) == len(out)
    return out


def completed_lmu_targets(b: int):
    """Return the completed cyclic word and all b^2 attached target triples."""
    bits = [0] * b
    word = []
    middle = []
    current = {2 * j + bits[j] for j in range(b)}
    for s in range(b):
        queue = [(s + i) % b for i in range(b)]
        for k in range(1, b):
            doubled = (s + k) % b
            letter = 2 * doubled + (bits[doubled] ^ 1)
            word.append(letter)
            current.add(letter)
            front = queue.pop(0)
            current.remove(2 * front + bits[front])
            if front != s:
                bits[front] ^= 1
            middle.append(frozenset(current))

        letter = 2 * s + bits[s]
        word.append(letter)
        current.add(letter)
        front = queue.pop(0)
        current.remove(2 * front + bits[front])
        bits[front] ^= 1
        middle.append(frozenset(current))

    assert bits == [0] * b
    assert len(word) == len(middle) == b * b
    lower = [
        frozenset(middle[i] & middle[(i + 1) % (b * b)])
        for i in range(b * b)
    ]
    upper = [
        frozenset(middle[i] | middle[(i + 1) % (b * b)])
        for i in range(b * b)
    ]
    for family in (lower, middle, upper):
        assert len(set(family)) == b * b
    return word, lower, middle, upper


def check_tour_endpoint_counts(b: int) -> None:
    flags = coherent_targets(b)
    by_signature = {(e, d): target for e, d, target in flags}
    hist = Counter()
    relation_hist = Counter()
    complement_count = 0

    universe = frozenset(range(2 * b))
    for i, (e, d, a) in enumerate(flags):
        for f, g, z in flags[i + 1 :]:
            distance = len(a - z)
            hist[distance] += 1
            if a == universe - z:
                complement_count += 1

            if distance in (1, b - 1):
                if e == f:
                    relation = "same_empty"
                elif d == g:
                    relation = "same_doubled"
                elif e == g and d == f:
                    relation = "reversed"
                elif d == f:
                    relation = "first_double_second_empty"
                elif e == g:
                    relation = "first_empty_second_double"
                else:
                    relation = "other"
                relation_hist[(distance, relation)] += 1

    r = (b - 1) // 2
    assert hist[1] == b * (b * b - 5) // 4
    assert hist[b - 1] == b * b
    assert complement_count == 0

    assert relation_hist[(1, "same_empty")] == b * (b - 2)
    assert relation_hist[(1, "same_doubled")] == b * r * (r - 1)
    assert sum(v for (j, _), v in relation_hist.items() if j == 1) == hist[1]

    assert relation_hist[(b - 1, "reversed")] == b
    assert (
        relation_hist[(b - 1, "first_double_second_empty")]
        == b * (b - 1) // 2
    )
    assert (
        relation_hist[(b - 1, "first_empty_second_double")]
        == b * (b - 1) // 2
    )
    assert (
        sum(v for (j, _), v in relation_hist.items() if j == b - 1)
        == hist[b - 1]
    )

    normalized_one = Fraction(2 * hist[1], b * (b - 1) * b * b)
    assert normalized_one == Fraction(b * b - 5, 2 * b * b * (b - 1))
    normalized_top = Fraction(2 * hist[b - 1], b * (b - 1) * b * b)
    assert normalized_top == Fraction(2, b * (b - 1))

    # The explicit distance-(b-1) rules in (3.2a).
    for e in range(b):
        for d in range(b):
            if e == d:
                continue
            gap = (d - e) % b
            g = (d + 1) % b if gap % 2 else (d - 1) % b
            assert g != e
            assert len(by_signature[(e, d)] - by_signature[(d, g)]) == b - 1

            reverse_distance = len(
                by_signature[(e, d)] - by_signature[(d, e)]
            )
            assert (reverse_distance == b - 1) == (gap in (2, b - 2))


def all_defect_one_targets(b: int):
    out = []
    for empty in range(b):
        for doubled in range(b):
            if doubled == empty:
                continue
            split = [j for j in range(b) if j not in (empty, doubled)]
            for choices in product((0, 1), repeat=b - 2):
                target = {2 * doubled, 2 * doubled + 1}
                target.update(2 * j + bit for j, bit in zip(split, choices))
                out.append(frozenset(target))
    assert len(out) == b * (b - 1) * 2 ** (b - 2)
    assert len(set(out)) == len(out)
    return out


def pairing_ratio(b: int, j: int) -> Fraction:
    a = b - j
    numerator = 4 * a * j * (a * j - 1) + a * (a - 1) + j * (j - 1)
    denominator = b * (b - 1) * comb(b, j)
    return Fraction(numerator, denominator)


def check_defect_profile(b: int) -> None:
    targets = all_defect_one_targets(b)
    root = targets[0]
    hist = Counter(len(root - z) for z in targets)
    for j in range(b + 1):
        expected = comb(b, j) ** 2 * pairing_ratio(b, j)
        assert expected.denominator == 1
        assert hist[j] == expected.numerator

    if b >= 7:
        nontrivial = [pairing_ratio(b, j) for j in range(1, b)]
        assert max(nontrivial) == Fraction(5 * (b - 2), b * b)


def check_lambda_formula(b: int) -> None:
    d1 = factorial(b) * b * (b - 1) // 4
    for j in range(b + 1):
        a = b - j
        lam = Fraction(
            factorial(a)
            * factorial(j)
            * (4 * a * j * (a * j - 1) + a * (a - 1) + j * (j - 1)),
            4,
        )
        assert lam / d1 == pairing_ratio(b, j)


def check_augmented_tail(b: int) -> None:
    rows = coherent_lmu_targets(b)
    q = b * (b - 1)
    lower = [row[0] for row in rows]
    middle = [row[1] for row in rows]
    upper = [row[2] for row in rows]

    lower_middle = sum(1 for a in lower for z in middle if a < z)
    middle_upper = sum(1 for a in middle for z in upper if a < z)
    lower_upper = sum(1 for a in lower for z in upper if a < z)
    assert lower_middle == middle_upper == b * (2 * b - 3)
    assert lower_upper == b * (7 * b - 11) // 2

    def ordered_johnson_one(family):
        return sum(
            1
            for a in family
            for z in family
            if a != z and len(a - z) == 1
        )

    assert ordered_johnson_one(lower) == q * (b + 3) // 2
    expected_middle = b * (b * b - 5) // 2
    assert ordered_johnson_one(middle) == expected_middle
    assert ordered_johnson_one(upper) == expected_middle

    rank_families = {b - 1: lower, b: middle, b + 1: upper}
    max_ratio = Fraction(0)
    small_sigma_max_average = {0: Fraction(0), 1: Fraction(0), 2: Fraction(0)}
    min_ambient_sigma_three = None
    for r, first_family in rank_families.items():
        for s, second_family in rank_families.items():
            type_counts = Counter()
            for a in first_family:
                for z in second_family:
                    if r == s and a == z:
                        continue
                    intersection = len(a & z)
                    u = r - intersection
                    v = s - intersection
                    type_counts[(u, v)] += 1

            for (u, v), count in type_counts.items():
                sigma = min(u, r - u) + min(v, 2 * b - r - v)
                ambient = comb(r, u) * comb(2 * b - r, v)
                ratio = Fraction(count, q * ambient)
                max_ratio = max(max_ratio, ratio)
                if sigma <= 2:
                    small_sigma_max_average[sigma] = max(
                        small_sigma_max_average[sigma], Fraction(count, q)
                    )

            for intersection in range(max(0, r + s - 2 * b), min(r, s) + 1):
                u = r - intersection
                v = s - intersection
                sigma = min(u, r - u) + min(v, 2 * b - r - v)
                if sigma >= 3:
                    ambient = comb(r, u) * comb(2 * b - r, v)
                    if min_ambient_sigma_three is None:
                        min_ambient_sigma_three = ambient
                    else:
                        min_ambient_sigma_three = min(
                            min_ambient_sigma_three, ambient
                        )

    assert small_sigma_max_average[0] == 0
    assert small_sigma_max_average[1] == Fraction(2 * b - 3, b - 1)
    assert small_sigma_max_average[2] == Fraction(b + 3, 2)
    assert min_ambient_sigma_three == b * b * (b - 1) // 2
    lower_bound = Fraction(2 * b - 3, b * (b - 1))
    assert max_ratio == lower_bound
    assert max_ratio <= Fraction(2, b)


def check_completed_tour(b: int) -> None:
    word, lower, middle, upper = completed_lmu_targets(b)
    length = b * b

    # Packet s emits pairs s+1,...,s-1,s.  Verify the closed occurrence
    # formula used in Theorem I.3A.3 (positions are one-based).
    for j in range(b):
        actual = [i + 1 for i, label in enumerate(word) if label // 2 == j]
        expected = sorted(
            s * (b - 1) + j + b * (s >= j)
            for s in range(b)
        )
        assert actual == expected

    cyclic_gaps = []
    for label in range(2 * b):
        positions = [i for i, value in enumerate(word) if value == label]
        for i, position in enumerate(positions):
            cyclic_gaps.append((positions[(i + 1) % len(positions)] - position) % length)
    assert Counter(cyclic_gaps) == Counter(
        {
            2 * b - 2: b * (b - 2),
            2 * b - 1: b,
            4 * b - 3: b,
        }
    )

    # Every cyclic window up through the asserted threshold is clean.
    doubled_word = word + word
    window_length = 2 * b - 2
    for start in range(length):
        window = doubled_word[start : start + window_length]
        assert len(window) == len(set(window))

    for target_rank in range(1, 2 * b - 2):
        distinct_windows = {
            frozenset(doubled_word[start : start + target_rank])
            for start in range(length)
        }
        expected = (
            b * (target_rank + 1) if target_rank <= b - 1 else b * b
        )
        assert len(distinct_windows) == expected

    middle_lower = sum(1 for a in middle for z in lower if z < a)
    middle_upper = sum(1 for a in middle for z in upper if a < z)
    assert middle_lower == b * (5 * b - 1) // 2
    assert middle_upper == 2 * b * b

    families = {b - 1: lower, b: middle, b + 1: upper}
    max_ratio = Fraction(0)
    small_sigma_max_average = {0: Fraction(0), 1: Fraction(0), 2: Fraction(0)}
    for r, first_family in families.items():
        for s, second_family in families.items():
            type_counts = Counter()
            for a in first_family:
                for z in second_family:
                    if r == s and a == z:
                        continue
                    intersection = len(a & z)
                    type_counts[(r - intersection, s - intersection)] += 1
            for (u, v), count in type_counts.items():
                sigma = min(u, r - u) + min(v, 2 * b - r - v)
                ambient = comb(r, u) * comb(2 * b - r, v)
                ratio = Fraction(count, b * b * ambient)
                max_ratio = max(max_ratio, ratio)
                if sigma <= 2:
                    small_sigma_max_average[sigma] = max(
                        small_sigma_max_average[sigma],
                        Fraction(count, b * b),
                    )

    assert small_sigma_max_average[0] == 0
    assert small_sigma_max_average[1] == Fraction(5 * b - 1, 2 * b)
    assert small_sigma_max_average[2] == Fraction(b * b + 6 * b + 1, 2 * b)
    assert max_ratio == Fraction(5 * b - 1, 2 * b * b)

    # The completed packet's two-coordinate profile algebra.
    same_pair = b - 1
    different_pair = Fraction(b * b - 2, 4)
    packet_lambda = same_pair + (2 * b - 2) * different_pair
    assert packet_lambda == Fraction(b * b * (b - 1), 2)
    block_count = (2 * b - 1) * b * b
    forced_lambda = Fraction(block_count * comb(b, 2), comb(2 * b, 2))
    assert packet_lambda == forced_lambda


def main() -> None:
    for b in range(5, 34, 2):
        check_tour_endpoint_counts(b)
        check_lambda_formula(b)
        check_augmented_tail(b)
        check_completed_tour(b)

    # Full defect-one enumeration is quadratic in q*2^(b-2), so keep it small.
    for b in (5, 7):
        check_defect_profile(b)

    gamma = Fraction(1, 20)
    g = float(gamma)
    binary_entropy = -g * log2(g) - (1 - g) * log2(1 - g)
    assert 2 * binary_entropy < 1

    print(
        "verified: FIFO, augmented, and completed-tour counts; clean-gap law; "
        "defect-one profiles; and packet profile/entropy identities"
    )


if __name__ == "__main__":
    main()
