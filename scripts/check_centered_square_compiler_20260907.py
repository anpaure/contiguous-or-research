"""Finite checks of the centered-square compiler; the note contains the proof."""

from itertools import product
from fractions import Fraction

from check_symmetrized_convex_fractional_20260907 import finite_majorant


def join(values):
    value = 0
    for item in values:
        value |= item
    return value


def interval_unions(word):
    ending, seen = set(), set()
    for letter in word:
        assert letter > 0
        ending = {letter} | {old | letter for old in ending}
        seen.update(ending)
    return seen


def derivative(source, starts, low, high):
    period = len(source)
    return [
        join(source[(j + offset) % period] for offset in range(low))
        for j in range(starts + high - low)
    ]


def main():
    identities = 0
    for period in range(1, 5):
        for source in product(range(1, 8), repeat=period):
            for low, high in ((1, 3), (2, 4), (3, 6)):
                block = derivative(source, period, low, high)
                for start in range(period):
                    for length in range(low, high + 1):
                        actual = join(block[start : start + length - low + 1])
                        target = join(
                            source[(start + offset) % period]
                            for offset in range(length)
                        )
                        assert actual == target
                        identities += 1

    blocks = flags = 0
    for b in range(2, 11):
        full = (1 << (2 * b)) - 1
        for ell in range(1, b + 1):
            fixed = b - ell + 1
            F = (1 << fixed) - 1
            G = F << fixed
            X = [1 << (2 * fixed + i) for i in range(ell - 1)]
            Y = [1 << (2 * fixed + ell - 1 + i) for i in range(ell - 1)]
            source = [F] + X + [G] + Y[::-1]
            assert len(source) == 2 * ell and join(source) == full
            rectangle = {
                F | join(X[:i]) | join(Y[:j])
                for i in range(ell)
                for j in range(ell)
            }
            complement = {full ^ target for target in rectangle}
            assert len(rectangle) == ell * ell
            assert rectangle.isdisjoint(complement)
            family = rectangle | complement
            middle = {s for s in family if s.bit_count() == b}
            assert len(middle) == 2 * ell
            cyclic_seen = {
                join(source[(start + j) % len(source)] for j in range(length))
                for start in range(len(source))
                for length in range(1, len(source) + 1)
            }
            for rank in range(ell, 2 * b - ell + 1):
                assert {s for s in cyclic_seen if s.bit_count() == rank} == {
                    s for s in family if s.bit_count() == rank
                }

            for q in range(ell):
                upper = {s for s in family if s.bit_count() == b + q}
                number = sum((s & u) == s for s in middle for u in upper)
                assert number == 2 * (q + 1) * (ell - q)
                assert len(upper) == 2 * (ell - q)
                flags += 1

            for H in range(ell):
                block = derivative(source, 2 * ell, ell - H, ell + H)
                assert len(block) == 2 * ell + 2 * H
                required = {s for s in family if abs(s.bit_count() - b) <= H}
                assert len(required) == 2 * ((2 * H + 1) * ell - H * (H + 1))
                seen = interval_unions(block)
                assert required <= seen
                if H <= b - ell:
                    assert {s for s in seen if abs(s.bit_count() - b) <= H} == required
                for target in required:
                    length = ell + target.bit_count() - b
                    assert any(
                        target
                        == join(source[(start + j) % len(source)] for j in range(length))
                        for start in range(len(source))
                    )
                blocks += 1

    interfaces = 0
    for b, epsilon in [
        (8, Fraction(1, 10)),
        (12, Fraction(1, 10)),
        (20, Fraction(1, 20)),
        (30, Fraction(1, 50)),
    ]:
        ranks, majorant, weights, _, crossing = finite_majorant(b, epsilon)
        for H in range(crossing - 1):
            if ranks[H] <= b + 1:
                continue
            gamma = ranks[H] / (ranks[H] - (b + 1))
            assert all(weights[a] == 0 for a in range(1, crossing - 1))
            charge = gamma * sum(a * weights[a] for a in range(1, b + 1))
            assert charge == gamma * (majorant[0] - (b + 1))
            for q in range(H + 1):
                incidence = gamma * sum(
                    weights[a] * max(0, a - q) for a in range(1, b + 1)
                )
                assert incidence >= ranks[q]
            block_cost = gamma * sum(
                weights[a] * (a + H) for a in range(1, b + 1)
            )
            assert block_cost <= (1 + Fraction(H, crossing - 1)) * charge
            interfaces += 1

    print(f"PASS: {identities} arbitrary-set derivative identities")
    print(f"PASS: {blocks} square blocks; {flags} exact rank-flag counts")
    print(f"PASS: {interfaces} finite long-side fractional block interfaces")


if __name__ == "__main__":
    main()
