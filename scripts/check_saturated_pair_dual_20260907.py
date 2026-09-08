"""Exact finite checks of the three-rank dual and two-orbit primal.

Every pair of saturated chains is determined, for these counts, by its
support sizes and rank intervals.  This enumerates those parameters and
subtracts ordinary within-pair duplicate targets, not only occurrences.
"""

from collections import Counter
from math import comb


def profile(a, c, bottom, rank):
    return max(
        0,
        min(a - 1, rank - bottom) - max(0, rank - bottom - c + 1) + 1,
    )


def main():
    shapes = 0
    equality = Counter()
    for b in range(2, 11):
        n = 2 * b
        for p in range(n + 1):
            q = n - p
            for a in range(1, p + 2):
                for c in range(1, q + 2):
                    for alpha in range(p - a + 2):
                        for beta in range(q - c + 2):
                            bottom = alpha + beta
                            ranks = (b - 1, b, b + 1)
                            masses = [
                                profile(a, c, bottom, s)
                                + profile(a, c, bottom, n - s)
                                for s in ranks
                            ]
                            if a == p + 1 and c == q + 1:
                                # Maximal shore chains intersect their
                                # complements only at their two endpoints.
                                duplicates = Counter(
                                    [0, n] if p in (0, n) else [0, p, q, n]
                                )
                                masses = [
                                    value - duplicates[s]
                                    for value, s in zip(masses, ranks)
                                ]
                            # Multiply the dual by 2b: weight 1/b in the
                            # middle and 1/2 in each adjacent rank.
                            dual = 2 * masses[1] + b * (masses[0] + masses[2])
                            assert dual <= 2 * b * (a + c), (
                                b, p, a, c, alpha, beta, masses
                            )
                            if dual == 2 * b * (a + c):
                                key = (a + c - 2 * b, abs(a - c))
                                assert key in {(0, 0), (1, 1), (2, 0)}
                                equality[key] += 1
                            shapes += 1

        W = comb(n, b)
        # The orbit masses are
        # tA = W(b-1)/(2b(b+1)), tB = W/(b(b+1)).
        # All inequalities below are scaled by 2b(b+1).
        for s in range(n + 1):
            d = abs(s - b)
            count_A = 2 * max(0, b - d)
            count_B = 2 * b if d == 0 else max(0, 2 * (b - d) + 1)
            incidence = W * (b - 1) * count_A + 2 * W * count_B
            assert incidence >= 2 * b * (b + 1) * comb(n, s)
            if d <= 1:
                assert incidence == 2 * b * (b + 1) * comb(n, s)
        charge = W * (b - 1) * (2 * b) + 2 * W * (2 * b + 1)
        assert charge == 2 * W * (b * (b + 1) + 1)

    print(f"PASS: {shapes} ordinary-incidence dual shape checks")
    print(f"PASS: all-rank two-orbit primal for b=2,...,10; equality types {dict(equality)}")


if __name__ == "__main__":
    main()
