"""Literal subset checks for diagonal subsquares and all-rank coalescence."""

from collections import Counter


def square(path, full):
    hull = {a & b for a in path for b in path}
    hull |= {a | b for a in path for b in path}
    complement = {full ^ value for value in hull}
    assert hull.isdisjoint(complement)
    assert len(hull) == len(path) ** 2
    return hull | complement


def main():
    subsquares = merges = overlaps = 0
    for b in range(2, 11):
        full = (1 << (2 * b)) - 1
        for ell in range(1, b + 1):
            fixed = b - ell + 1
            F = (1 << fixed) - 1
            X = [1 << (fixed + i) for i in range(ell - 1)]
            Y = [1 << (b + i) for i in range(ell - 1)]
            path = [F | sum(X)]
            for x, y in zip(X, Y):
                path.append((path[-1] ^ x) | y)
            assert len(path) == ell
            assert all(t.bit_count() == b for t in path)
            for i, left in enumerate(path):
                for j, right in enumerate(path):
                    assert (left ^ right).bit_count() == 2 * abs(i - j)

            big = square(path, full)
            assert len(big) == 2 * ell * ell
            for start in range(ell):
                for stop in range(start + 1, ell + 1):
                    assert square(path[start:stop], full) <= big
                    subsquares += 1

            for p in range(1, ell + 1):
                for r in range(p + 1):
                    q = ell - p + r
                    if not q or r > q:
                        continue
                    left = square(path[:p], full)
                    right = square(path[p - r :], full)
                    assert len(left & right) == 2 * r * r
                    assert left | right <= big
                    gained = big - (left | right)
                    assert len(gained) == 4 * (p - r) * (q - r)
                    ranks = Counter(t.bit_count() for t in gained)
                    for rank in range(2 * b + 1):
                        d = abs(rank - b)
                        expected = 2 * (
                            max(0, p + q - r - d)
                            - max(0, p - d)
                            - max(0, q - d)
                            + max(0, r - d)
                        )
                        assert ranks[rank] == expected
                    assert 2 * p + 2 * q - 2 * ell == 2 * r
                    if r:
                        overlaps += 1
                    else:
                        merges += 1

    print(f"PASS: {subsquares} literal diagonal-subsquare containments")
    print(f"PASS: {merges} disjoint merges; {overlaps} overlapping coalescences")


if __name__ == "__main__":
    main()
