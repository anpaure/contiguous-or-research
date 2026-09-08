"""Exact finite checks for the pair-arc induced-residual theorem.

Only stdout is written. Finite checks do not establish matching reachability.
"""

from collections import Counter
from fractions import Fraction as F
from itertools import combinations, permutations
from math import comb, factorial


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def pairings(points):
    if not points:
        yield ()
        return
    first = points[0]
    for j in range(1, len(points)):
        rest = points[1:j] + points[j + 1:]
        for matching in pairings(rest):
            yield ((first, points[j]),) + matching


def census(r, m):
    b, s = 2 * r + 1, 2 * r
    all_starts = (1 << b) - 2
    membership = []
    for k in (r, r - 1):
        membership.append([
            sum(1 << ((position - j) % b) for j in range(k))
            for position in range(b)
        ])
    total = live = 0
    counts = [Counter(), Counter()]
    for points in combinations(range(b), 2 * m):
        for pairs in pairings(points):
            total += 1
            data = []
            for shore, masks in enumerate(membership):
                splits = [masks[a] ^ masks[c] for a, c in pairs]
                both = [masks[a] & masks[c] for a, c in pairs]
                seen = bad = 0
                for mask in splits:
                    bad |= seen & mask
                    seen |= mask
                if m == 2 and shore == 0:
                    assert bad & all_starts != all_starts
                if bad & all_starts:
                    break
                data.append((splits, both))
            if len(data) != 2:
                continue
            live += 1
            for shore, (splits, both) in enumerate(data):
                for start in range(1, b):
                    bit = 1 << start
                    j = sum(bool(mask & bit) for mask in splits)
                    h = sum(bool(mask & bit) for mask in both)
                    assert j <= 1
                    counts[shore][j, h] += 1
    weight = 2 ** m * factorial(m) * factorial(b - 2 * m)
    assert total * weight == factorial(b)
    assert all(sum(row.values()) == s * live for row in counts)
    return live * weight, [Counter({key: value * weight for key, value in row.items()})
                           for row in counts], F(live, total)


def brute_census(r, m):
    b = 2 * r + 1
    live = 0
    counts = [Counter(), Counter()]
    for word in permutations(range(b)):
        data = []
        for k in (r, r - 1):
            histogram = Counter()
            for start in range(1, b):
                window = set(word[(start + j) % b] for j in range(k))
                j = sum((2 * i in window) != (2 * i + 1 in window) for i in range(m))
                h = sum(2 * i in window and 2 * i + 1 in window for i in range(m))
                if j > 1:
                    break
                histogram[j, h] += 1
            if sum(histogram.values()) != b - 1:
                break
            data.append(histogram)
        if len(data) == 2:
            live += 1
            for shore in range(2):
                counts[shore].update(data[shore])
    return live, counts


def statistics(r, m, z, counts):
    b, s = 2 * r + 1, 2 * r
    results = []
    for shore, k in enumerate((r, r - 1)):
        population = comb(b, k)
        classes = {
            (j, h): comb(m, j) * comb(m - j, h) * 2 ** j
            * choose(b - 2 * m, k - j - 2 * h)
            for j in (0, 1) for h in range(m - j + 1)
        }
        retained = sum(classes.values())
        mean = F(s * z, retained)
        degree = {key: F(counts[shore][key], size) if size else F(0)
                  for key, size in classes.items()}
        assert all(value.denominator == 1 for value in degree.values())
        u2 = sum(F(size, retained) * (degree[key] / mean - 1) ** 2
                 for key, size in classes.items() if size)
        u4 = sum(F(size, retained) * (degree[key] / mean - 1) ** 4
                 for key, size in classes.items() if size)
        atoms = []
        for bits in range(1 << (2 * m)):
            size = bits.bit_count()
            probability = F(choose(b - 2 * m, k - size), population)
            if not probability:
                continue
            j = sum(((bits >> (2 * i)) & 1) != ((bits >> (2 * i + 1)) & 1)
                    for i in range(m))
            h = sum((bits >> (2 * i)) & 3 == 3 for i in range(m))
            value = degree[j, h] / mean - 1 if j <= 1 else F(0)
            atoms.append((bits, probability, value))
        assert sum(probability for _, probability, _ in atoms) == 1
        assert sum(probability * value for _, probability, value in atoms) == 0
        assert sum(probability * value ** 2 for _, probability, value in atoms) == F(retained, population) * u2
        moments = [sum(probability * value for bits, probability, value in atoms if bits & (1 << i))
                   for i in range(2 * m)]
        rest = -sum(moments) / (b - 2 * m)
        gram = F(k * (b - k), b * (b - 1))
        coefficients = [moment / gram for moment in moments]
        other_coefficient = rest / gram
        projected = []
        for bits, probability, value in atoms:
            linear = k * other_coefficient + sum(
                coefficients[i] - other_coefficient
                for i in range(2 * m) if bits & (1 << i)
            )
            projected.append((bits, probability, value, linear))
        p1_second = sum(probability * linear ** 2 for _, probability, _, linear in projected)
        p1_fourth = sum(probability * linear ** 4 for _, probability, _, linear in projected)
        assert p1_second == (sum(moment ** 2 for moment in moments) + (b - 2 * m) * rest ** 2) / gram
        for i in range(2 * m):
            assert sum(probability * (value - linear)
                       for bits, probability, value, linear in projected if bits & (1 << i)) == 0
        quadratic_test = sum(
            probability * (value - linear)
            * (1 if ((bits & 1) != 0) == ((bits & 2) != 0) else -1)
            for bits, probability, value, linear in projected
        )
        results.append((F(retained, population), u2, u4, p1_second, p1_fourth, quadratic_test))
    return results


def limiting_atom_checks():
    for m in range(2, 11):
        values = []
        for bits in range(1 << m):
            split = bits.bit_count()
            value = F(m - 1, 2) if split == 0 else -F(m - 1, 2 * m) if split == 1 else F(0)
            values.append(value)
        assert sum(values) == 0
        density = F(m + 1, 2 ** m)
        u2 = sum(value ** 2 for value in values) / (2 ** m * density)
        u4 = sum(value ** 4 for value in values) / (2 ** m * density)
        assert 1 + u2 == F((m + 1) ** 2, 4 * m)
        assert u4 == F((m - 1) ** 4, 16 * (m + 1)) * (1 + F(1, m ** 3))
        for pair in range(m):
            correlation = sum(value * (-1 if bits & (1 << pair) else 1)
                              for bits, value in enumerate(values)) / 2 ** m
            assert correlation == F(m - 1, m * 2 ** m)
        assert F(factorial(m - 1), factorial(2 * m - 1)) > 0
        mean_length = F(m, 2 * m)
        second_length = F(m * (m + 1), 2 * m * (2 * m + 1))
        assert second_length - mean_length ** 2 == F(1, 4 * (2 * m + 1))


def endpoint_order_checks():
    for m in range(2, 6):
        accepted = 0
        for other_events in permutations(range(1, 2 * m)):
            events = (0,) + other_events
            accepted += all(events[(position + 1) % (2 * m)] == event + 1
                            for position, event in enumerate(events) if event % 2 == 0)
        assert accepted == factorial(m - 1)
        assert F(accepted, factorial(2 * m - 1)) == F(factorial(m - 1), factorial(2 * m - 1))


if __name__ == "__main__":
    limiting_atom_checks()
    endpoint_order_checks()
    print("Exact limiting-atom identities: m=2,...,10 passed")
    print("Exact disjoint-arc endpoint-order counts: m=2,...,5 passed")
    for r, m in ((2, 2), (3, 2), (3, 3)):
        z, counts, _ = census(r, m)
        assert (z, counts) == brute_census(r, m)
        print(f"Compressed/full-permutation census agrees: r={r}, m={m}, rows={z}")
    for r, m in ((4, 2), (8, 2), (16, 2), (24, 2), (5, 3), (8, 3)):
        z, counts, fraction = census(r, m)
        if not z:
            print(f"r={r}, m={m}: empty finite catalogue")
            continue
        stats = statistics(r, m, z, counts)
        limit_fraction = F(factorial(m - 1), factorial(2 * m - 1))
        print(f"r={r}, m={m}: Z/Z0={float(fraction):.8f}, limit={float(limit_fraction):.8f}")
        for shore, (density, u2, u4, p12, p14, quadratic) in zip(("M", "L"), stats):
            print(f"  {shore}: density={float(density):.8f}, 1+U2={float(1 + u2):.8f}, "
                  f"U4={float(u4):.8f}, P1^2={float(p12):.3e}, P1^4={float(p14):.3e}, "
                  f"quadratic_test={float(quadratic):.8f}")
    print("No computation above samples the stopped matching-arrival law.")
