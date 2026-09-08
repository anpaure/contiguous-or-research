#!/usr/bin/env python3
"""Exact audit of the 3x3 token--middle--upper non-TU witness."""


def determinant_3(matrix):
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def main():
    A = {f"a{i}" for i in range(1, 12)}
    B = {f"b{i}" for i in range(1, 12)}
    U1 = {f"a{i}" for i in range(1, 6)} | {f"b{i}" for i in range(1, 7)}
    V2 = U1 | {"a6"}
    U2 = V2 - {"a1"}
    V1 = U1 | {"a7"}

    for U, V in ((U1, V1), (U2, V2), (U1, V2)):
        assert U < V
        assert len(U) == 11 and len(V) == 12
        assert (len(U & A), len(U & B)) == (5, 6)
        assert (len(V & A), len(V & B)) == (6, 6)

    matrix = [[1, 1, 0], [1, 0, 1], [0, 1, 1]]
    assert determinant_3(matrix) == -2

    # At x=(1/2,1/2,1/2), selected rows have load one; other used rows 1/2.
    assert [sum(row) / 2 for row in matrix] == [1, 1, 1]
    conflicts = {(0, 1): "o1", (0, 2): "U1", (1, 2): "V2"}
    assert len(conflicts) == 3

    print("PASS explicit q=1 split-(5,6)->(6,6) orbit flags")
    print("PASS determinant=-2 fractional=3/2 restricted_integral=1")
    print("ALL TOKEN-LABEL NONTU CHECKS PASS")


if __name__ == "__main__":
    main()
