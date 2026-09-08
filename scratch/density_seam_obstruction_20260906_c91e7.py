"""Finite checks for the seam-robust density-hole obstruction.

This file reads and writes no files. The asymptotic assertions require the
proof, not these computations. Run directly with python3.
"""

import itertools
import math
import random
from fractions import Fraction


def cyclic_unions(word, k):
    full = (1 << k) - 1
    seen = set()
    n = len(word)
    for start in range(n):
        value = 0
        for length in range(n):
            value |= word[(start + length) % n]
            seen.add(value)
            if value == full:
                break
    return seen


def rank_profile(sets, k):
    result = [0] * (k + 1)
    for value in sets:
        result[value.bit_count()] += 1
    return result


def check_cuts():
    words = 0
    cuts = 0
    for k, max_length in ((1, 5), (2, 5), (3, 5), (4, 4)):
        for length in range(2, max_length + 1):
            for word in itertools.product(range(1, 1 << k), repeat=length):
                words += 1
                for cut in range(1, length):
                    left = set()
                    right = set()
                    value = 0
                    for i in range(cut - 1, -1, -1):
                        value |= word[i]
                        left.add(value)
                    value = 0
                    for i in range(cut, length):
                        value |= word[i]
                        right.add(value)
                    crossing = {a | b for a in left for b in right}
                    counts = rank_profile(crossing, k)
                    assert all(counts[s] <= s for s in range(1, k + 1))
                    cuts += 1
    print("CUT_CHECK_PASS", "words", words, "cuts", cuts)


def check_local_lemma_parameters():
    cases = 0
    for maximum in range(1, 25):
        for layer in range(8 * maximum, 8 * maximum + 80):
            largest_x = Fraction(maximum, layer - 4 * maximum)
            for length in range(1, maximum + 1):
                x = Fraction(length, layer - 4 * maximum)
                p = Fraction(length, layer)
                assert x * (1 - 2 * largest_x) >= p
                assert x * (1 - largest_x) ** 2 >= p
                assert x / (1 - largest_x) == Fraction(
                    length, layer - 5 * maximum
                )
                cases += 1
    print("LLL_PARAMETER_CHECK_PASS", cases)


def check_fragments(rng):
    cases = 0
    for k in range(2, 7):
        full = (1 << k) - 1
        for _ in range(300):
            sources = [
                [rng.randrange(1, full + 1) for _ in range(rng.randrange(2, 9))]
                for _ in range(3)
            ]
            pool = set().union(*(cyclic_unions(word, k) for word in sources))
            fragments = []
            for _ in range(rng.randrange(1, 9)):
                source = rng.choice(sources)
                start = rng.randrange(len(source))
                length = rng.randrange(1, len(source) + 1)
                fragment = [source[(start + j) % len(source)] for j in range(length)]
                if rng.randrange(2):
                    fragment.reverse()
                fragments.append(fragment)
            word = list(itertools.chain.from_iterable(fragments))
            new_counts = rank_profile(cyclic_unions(word, k) - pool, k)
            assert all(
                new_counts[s] <= len(fragments) * s for s in range(1, k + 1)
            )
            cases += 1
    print("FRAGMENT_CHECK_PASS", cases)


def first_rank_outputs(word, start, k):
    result = [None] * k
    value = 0
    for offset in range(len(word)):
        value |= word[(start + offset) % len(word)]
        rank = value.bit_count()
        if rank == k:
            break
        result[rank] = value
    return result


def check_seam_locality(rng):
    cases = 0
    for k in range(2, 7):
        for _ in range(100):
            blocks = []
            for _ in range(5):
                order = list(range(k))
                rng.shuffle(order)
                blocks.append([1 << x for x in order])
            changed = rng.randrange(len(blocks))
            replacement = blocks[changed][:]
            rng.shuffle(replacement)
            old_word = list(itertools.chain.from_iterable(blocks))
            new_blocks = blocks[:]
            new_blocks[changed] = replacement
            new_word = list(itertools.chain.from_iterable(new_blocks))
            for j in range(len(blocks)):
                if j in (changed, (changed - 1) % len(blocks)):
                    continue
                for start in range(j * k, (j + 1) * k):
                    assert first_rank_outputs(old_word, start, k) == first_rank_outputs(
                        new_word, start, k
                    )
            cases += 1
    print("SEAM_LOCALITY_CHECK_PASS", cases)


def check_permutation_pass_inventory():
    permutations = 0
    for k in range(2, 9):
        first = [1 << x for x in range(k)]
        totals = [0] * k
        repeats = [[0] * (k + 1) for _ in range(k)]
        count = math.factorial(k)
        for order in itertools.permutations(range(k)):
            word = first + [1 << x for x in order]
            outputs = [first_rank_outputs(word, start, k) for start in range(k)]
            for s in range(1, k):
                values = [row[s] for row in outputs]
                distinct = len(set(values))
                assert distinct == 1 + sum(
                    values[j] != values[j + 1] for j in range(k - 1)
                )
                totals[s] += distinct
                for a in range(2, k + 1):
                    repeats[s][a] += values[k - a] == values[k - a + 1]
            permutations += 1
        harmonic = [Fraction(0)]
        for j in range(1, k):
            harmonic.append(harmonic[-1] + Fraction(1, j))
        for s in range(1, k):
            expected = k - s + 1 + (k - s) * (harmonic[k - 1] - harmonic[k - s])
            assert Fraction(totals[s], count) == expected
            for a in range(2, k + 1):
                expected_repeat = Fraction(s - a + 1, k - a + 1) if a <= s else 0
                assert Fraction(repeats[s][a], count) == expected_repeat
    print("EXACT_PASS_INVENTORY_CHECK_PASS", "permutations", permutations)


def permutation_block(rng, k, depth):
    order = list(range(k))
    rng.shuffle(order)
    word = []
    for i in range(k):
        value = 0
        for j in range(depth):
            value |= 1 << order[(i + j) % k]
        word.append(value)
    return word


def simulations(rng):
    print("SIMULATIONS: k depth length/W mean_holes/2^k finite_expectation_floor")
    for k, trials in ((8, 40), (10, 40), (12, 30), (14, 20), (16, 12), (18, 6)):
        width = math.comb(k, k // 2)
        count = math.ceil(width / k)
        n = count * k
        finite_floor = sum(
            math.comb(k, s) * math.exp(-n / (math.comb(k, s) - 5 * k))
            for s in range(1, k)
            if math.comb(k, s) >= 8 * k
        ) / (1 << k)
        harmonic = [0.0]
        for j in range(1, k):
            harmonic.append(harmonic[-1] + 1 / j)
        singleton_floor = sum(
            math.comb(k, s) * math.exp(
                -count * (k - s + 1 + (k - s) * (harmonic[k - 1] - harmonic[k - s]))
                / (math.comb(k, s) - 5 * k)
            )
            for s in range(1, k)
            if math.comb(k, s) >= 8 * k
        ) / (1 << k)
        for depth in sorted({1, max(1, k // 2 - math.isqrt(k))}):
            samples = []
            for _ in range(trials):
                word = list(
                    itertools.chain.from_iterable(
                        permutation_block(rng, k, depth) for _ in range(count)
                    )
                )
                samples.append(((1 << k) - 1 - len(cyclic_unions(word, k))) / (1 << k))
            print(k, depth, f"{n / width:.6f}", f"{sum(samples) / trials:.6f}",
                  f"{(singleton_floor if depth == 1 else finite_floor):.6f}")


def integral_check():
    # The integrand decreases on [0, infinity), so left/right sums bracket
    # the truncated integral in exact arithmetic. Printed values use floats.
    steps = 500000
    endpoint = 2.0
    h = endpoint / steps
    for coefficient in (1.0, (1 + math.log(2)) / 2):
        f = lambda x: math.exp(-x * x - coefficient * math.exp(x * x))
        right = h * sum(f(j * h) for j in range(1, steps + 1))
        left = right + h * (f(0) - f(endpoint))
        scale = 2 / math.sqrt(math.pi)
        tail_bound = math.exp(-endpoint ** 2 - coefficient * math.exp(endpoint ** 2)) / (
            endpoint * math.sqrt(math.pi)
        )
        print("MONOTONE_QUADRATURE", coefficient,
              scale * right, scale * left + tail_bound)
    print("ANALYTIC_POSITIVE_LOWER_BOUND",
          math.erf(1 / math.sqrt(2)) * math.exp(-math.exp(0.5)))


if __name__ == "__main__":
    rng = random.Random(20260906)
    check_cuts()
    check_local_lemma_parameters()
    check_fragments(rng)
    check_seam_locality(rng)
    check_permutation_pass_inventory()
    integral_check()
    simulations(rng)
