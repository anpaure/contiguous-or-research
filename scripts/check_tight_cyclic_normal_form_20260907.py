"""Check the cyclic normal form for every tight chain-rank shape at b<=4."""

from collections import defaultdict
from itertools import permutations


def windows(pi, size):
    n = len(pi)
    return tuple(
        sum(1 << pi[(i + j) % n] for j in range(size)) for i in range(n)
    )


def column_families(b, p, a, c, alpha, beta):
    n, full = 2 * b, (1 << (2 * b)) - 1

    def chain(coords, length, bottom):
        value = sum(1 << x for x in coords[:bottom])
        out = []
        for i in range(length):
            out.append(value)
            if i + 1 < length:
                value |= 1 << coords[bottom + i]
        return out

    left = chain(list(range(p)), a, alpha)
    right = chain(list(range(p, n)), c, beta)
    rectangle = {x | y for x in left for y in right}
    pair = rectangle | {full ^ x for x in rectangle}
    return {
        rank: frozenset(x for x in pair if x.bit_count() == rank)
        for rank in range(n + 1)
    }


def check(b):
    n = 2 * b
    decks = defaultdict(list)
    for pi in permutations(range(n)):
        key = frozenset(windows(pi, b))
        # Rotations and reversals give enough representatives for testing.
        if len(decks[key]) < 8 * n:
            decks[key].append(pi)

    checked = 0
    for p in range(n + 1):
        q = n - p
        for a in range(1, p + 2):
            for c in range(1, q + 2):
                shape = (a + c - 2 * b, abs(a - c))
                if shape not in {(0, 0), (1, 1), (2, 0)}:
                    continue
                for alpha in range(p - a + 2):
                    for beta in range(q - c + 2):
                        center = alpha + beta + (a + c - 2) / 2
                        if shape == (0, 0) and center != b:
                            continue
                        if shape == (1, 1) and abs(center - b) != 0.5:
                            continue
                        if shape == (2, 0) and center != b:
                            continue

                        kind = {(0, 0): "A", (1, 1): "B", (2, 0): "C"}[shape]
                        fam = column_families(b, p, a, c, alpha, beta)
                        good = False
                        for pi in decks.get(fam[b], []):
                            mid = windows(pi, b)
                            lower = windows(pi, b - 1)
                            if kind == "C":
                                if frozenset(lower) == fam[b - 1]:
                                    good = True
                                    break
                                continue

                            for d in range(1, b):
                                rank_windows = windows(pi, b - d)
                                if kind == "A":
                                    starts = list(range(d, b)) + list(range(b + d, 2 * b))
                                else:
                                    starts = list(range(d, b + 1)) + list(range(b + d, 2 * b))
                                if frozenset(rank_windows[j] for j in starts) != fam[b - d]:
                                    break
                            else:
                                # The d=1 comparison verifies the L_i deletion row.
                                good = True
                                break
                        assert good, (b, p, a, c, alpha, beta, kind)
                        checked += 1
    return checked


def main():
    for b in (2, 3, 4):
        print("b", b, "tight shapes checked", check(b))
    print("PASS: cyclic normal form, including every balanced/unbalanced shore split")


if __name__ == "__main__":
    main()
