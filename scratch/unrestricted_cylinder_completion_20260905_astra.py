"""Literal-OR checks for the unrestricted cylinder-completion lemma.

Run directly with Python 3. No third-party packages or certificate files.
"""

from itertools import product
from math import comb


def linear_unions(word):
    seen = set()
    suffixes = set()
    for letter in word:
        suffixes = {letter} | {value | letter for value in suffixes}
        seen.update(suffixes)
    return seen


def cyclic_unions(word):
    seen = set()
    for start in range(len(word)):
        value = 0
        for length in range(len(word)):
            value |= word[(start + length) % len(word)]
            seen.add(value)
    return seen


def normalize(word):
    cut = max(range(len(word)), key=lambda i: word[i].bit_count())
    rotated = word[cut + 1:] + word[:cut + 1]
    recorded = rotated[-1]
    blocks = []
    for letter in rotated:
        fresh = letter & ~recorded
        if fresh:
            blocks.append(fresh)
            recorded |= fresh
    return rotated + blocks[:-1]


def lift(word, bit):
    return word + [bit] + [letter | bit for letter in word[:-1]]


def develop(seed, k):
    word = []
    mask = (1 << k) - 1
    for _ in range(k):
        word.extend(seed)
        seed = [((letter << 1) & mask) | (letter >> (k - 1))
                for letter in seed]
    return word


UNIVERSAL = {0: [], 1: [1], 2: [1, 2], 3: [1, 2, 4, 1]}


def complete(word, k, t, cyclic=False):
    covered = cyclic_unions(word) if cyclic else linear_unions(word)
    holes = set(range(1, 1 << k)) - covered
    base = normalize(word) if cyclic else list(word)
    result = list(base)
    for coordinate in range(k, k + t):
        result = lift(result, 1 << coordinate)
    assert len(result) == (1 << t) * len(base)
    for target in holes:
        result.extend(target | (letter << k)
                      for letter in [0] + UNIVERSAL[t])
    expected = (1 << t) * len(base) + len(holes) * (len(UNIVERSAL[t]) + 1)
    assert len(result) == expected
    assert all(result)
    assert linear_unions(result) == set(range(1, 1 << (k + t)))
    return result


def main():
    for k, word in UNIVERSAL.items():
        assert linear_unions(word) == set(range(1, 1 << k))
        assert linear_unions([0] + word) == set(range(1 << k))

    words = 0
    completions = 0
    for k in range(1, 4):
        for length in range(1, 4):
            for values in product(range(1, 1 << k), repeat=length):
                word = list(values)
                words += 1
                cyclic = cyclic_unions(word)
                normalized = normalize(word)
                assert cyclic <= linear_unions(normalized)
                support = 0
                for letter in word:
                    support |= letter
                overhead = max(0, support.bit_count()
                               - max(letter.bit_count() for letter in word) - 1)
                assert len(normalized) <= len(word) + overhead
                for t in range(4):
                    for use_cycle in (False, True):
                        complete(word, k, t, use_cycle)
                        completions += 1
                for rank in range(1, k + 1):
                    assert sum(value.bit_count() == rank for value in cyclic) <= length
                holes = (1 << k) - 1 - len(cyclic)
                assert holes >= sum(max(0, comb(k, s) - length)
                                    for s in range(1, k + 1))

    a7 = develop([3, 5, 64, 20, 36], 7)
    assert len(a7) == comb(7, 3)
    assert cyclic_unions(a7) == set(range(1, 128))
    a9 = develop([1, 130, 136, 12, 36, 48, 80, 272, 18, 17, 9, 65, 96, 68], 9)
    assert len(a9) == comb(9, 4)
    assert sorted(set(range(1, 512)) - cyclic_unions(a9)) == [
        59, 118, 199, 219, 236, 285, 355, 365, 398, 433, 438, 472]
    for word, k in ((a7, 7), (a9, 9)):
        for t in range(4):
            completed = complete(word, k, t, cyclic=True)
            print(f"finite base k={k}, t={t}, completed length={len(completed)}")

    example = complete([1, 2, 4], 3, 2)
    assert example == [1, 2, 4, 8, 9, 10, 16, 17, 18, 20, 24, 25, 5, 13, 21]
    for k in range(3, 9):
        full = (1 << k) - 1
        separated = [full]
        for target in range(1, full):
            if target.bit_count() != k // 2:
                separated.extend([target, full])
        missing = set(range(1, full + 1)) - linear_unions(separated)
        assert missing == {target for target in range(1, full)
                           if target.bit_count() == k // 2}
        assert len(missing) == comb(k, k // 2)
    print(f"PASS: {words} exhaustive base words, {completions} completions")
    print(f"PASS: explicit 5-coordinate example {example}")
    print("PASS: same-dimension sparse-hole counterexamples, k=3,...,8")


if __name__ == "__main__":
    main()
