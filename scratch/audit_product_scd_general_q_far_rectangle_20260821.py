#!/usr/bin/env python3
from fractions import Fraction
from math import comb


def determinant(matrix):
    a = [[Fraction(x) for x in row] for row in matrix]
    det = Fraction(1)
    n = len(a)
    for col in range(n):
        pivot = next((row for row in range(col, n) if a[row][col]), None)
        if pivot is None:
            return 0
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            det = -det
        value = a[col][col]
        det *= value
        for j in range(col, n):
            a[col][j] /= value
        for row in range(col + 1, n):
            value = a[row][col]
            if value:
                for j in range(col, n):
                    a[row][j] -= value * a[col][j]
    return det


def target_interval(b, q, a, c):
    lo = max(a, c + q)
    hi = min(b - a, b - c + q)
    return lo, hi


def shift_interval(q, a, c):
    lo = min(q, max(0, c - a))
    hi = max(0, min(q, q + c - a))
    return lo, hi


def formula_audit():
    for b in (5, 7, 11, 23, 43, 101, 503):
        h = (b - 1) // 2
        counts = [comb(b, d) - (comb(b, d - 1) if d else 0) for d in range(h + 1)]
        w = comb(2 * b, b)
        d1 = sum(counts[d] ** 2 * (b - 2 * d) for d in range(h + 1))
        for q in range(1, min(h, 12) + 1):
            equal_loss = endpoint_mass = 0
            difference_zero = [0] * (b + 2)
            difference_q = [0] * (b + 2)
            for a, ca in enumerate(counts):
                for c, cc in enumerate(counts):
                    lo, hi = target_interval(b, q, a, c)
                    number = max(0, hi - lo + 1)
                    zlo, zhi = shift_interval(q, a, c)
                    if number:
                        assert zlo <= zhi
                        for z in range(zlo, zhi + 1):
                            assert lo - z >= max(a, c)
                            assert hi - z <= b - max(a, c)
                    multiplicity = ca * cc
                    if a == c:
                        equal_loss += multiplicity * number
                    else:
                        endpoint_mass += multiplicity * number
                        if a > c:
                            assert zlo <= 0 <= zhi
                            source_lo, source_hi = lo, hi
                            difference_zero[source_lo] += multiplicity
                            difference_zero[source_hi + 1] -= multiplicity
                        else:
                            assert zlo <= q <= zhi
                            source_lo, source_hi = lo - q, hi - q
                            difference_q[source_lo] += multiplicity
                            difference_q[source_hi + 1] -= multiplicity
            assert equal_loss + endpoint_mass == comb(2 * b, b + q)
            assert equal_loss == sum(
                counts[d] ** 2 * max(0, b - 2 * d - q + 1)
                for d in range(h + 1)
            )
            assert equal_loss <= d1

            trim = 0
            loads_zero = []
            loads_q = []
            running_zero = running_q = 0
            for r in range(b + 1):
                running_zero += difference_zero[r]
                running_q += difference_q[r]
                loads_zero.append(running_zero)
                loads_q.append(running_q)
            for r in range(q, b - q + 1):
                load_zero = loads_zero[r]
                load_q = loads_q[r]
                t = min(r, b - r)
                oriented_off_diagonal = (
                    comb(b, t) ** 2 - sum(value * value for value in counts[: t + 1])
                ) // 2
                assert load_zero <= oriented_off_diagonal
                assert load_q <= oriented_off_diagonal
                left_size = comb(b, r) ** 2
                cap_a = Fraction((r - q + 1) * left_size, b)
                cap_b = Fraction((b - r - q + 1) * left_size, b)
                trim += max(Fraction(0), load_q - cap_a)
                trim += max(Fraction(0), load_zero - cap_b)
            assert trim <= Fraction(2 * (q - 1) * w, b)
        print("formula PASS", b)


def minor_audit():
    rows = [
        ("C", 1, 1),
        ("P", 2, 1),
        ("C", 3, 0),
        ("C", 2, 1),
        ("P", 0, 0),
        ("C", 4, 1),
    ]
    columns = [
        (0, 0, 0, 2, 5),
        (0, 0, 1, 1, 4),
        (0, 1, 1, 2, 4),
        (2, 1, 0, 3, 3),
        (2, 1, 1, 2, 2),
        (1, 0, 1, 1, 3),
    ]
    matrix = []
    for row in rows:
        values = []
        for a, c, z, lo, hi in columns:
            if row[0] == "P":
                values.append(int((a, c) == row[1:]))
            else:
                values.append(int(z == row[2] and lo <= row[1] <= hi))
        matrix.append(values)
    expected = [
        [0, 1, 0, 0, 0, 1],
        [0, 0, 0, 1, 1, 0],
        [1, 0, 0, 1, 0, 0],
        [0, 1, 1, 0, 1, 1],
        [1, 1, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0],
    ]
    assert matrix == expected
    assert determinant(matrix) == 2
    for a, c, z, lo, hi in columns:
        L, U = target_interval(5, 2, a, c)
        zlo, zhi = shift_interval(2, a, c)
        assert zlo <= z <= zhi
        assert (lo, hi) == (L - z, U - z)
    print("determinant-2 constant-shift minor PASS")


if __name__ == "__main__":
    formula_audit()
    minor_audit()
    print("ALL GENERAL-Q PRODUCT-SCD CHECKS PASS")
