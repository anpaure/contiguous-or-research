"""Exact small threshold-cover searches; no asymptotic conclusion is inferred."""

import argparse
from fractions import Fraction
from itertools import combinations, permutations, product
from math import comb


def matchings(vertices):
    if not vertices:
        yield ()
        return
    a = vertices[0]
    for i, b in enumerate(vertices[1:], 1):
        for rest in matchings(vertices[1:i] + vertices[i + 1:]):
            yield ((a, b),) + rest


def allowed(m, edges):
    return sum(1 << x for x in range(1 << m)
               if all((x >> a & 1) >= (x >> b & 1) for a, b in edges))


def matching_menu(m):
    result = []
    for matching in matchings(tuple(range(m))):
        for flips in product((0, 1), repeat=len(matching)):
            edges = tuple((b, a) if flip else (a, b)
                          for (a, b), flip in zip(matching, flips))
            result.append((allowed(m, edges), edges))
    return result


def path_menu(m, split):
    result = {}
    for p in permutations(range(m)):
        left, right = p[:split], p[split:]
        if split * 2 == m and left > right:
            continue
        edges = tuple(zip(left, left[1:])) + tuple(zip(right, right[1:]))
        mask = allowed(m, edges)
        result.setdefault(mask, (left, right))
    return [(mask, paths) for mask, paths in result.items()]


def exact_tight_cover(menu, m, count, tight_ranks):
    """All chosen covers must be disjoint on the named capacity-tight ranks."""
    full = (1 << (1 << m)) - 1
    tight = sum(1 << x for x in range(1 << m) if x.bit_count() in tight_ranks)
    choices = [[] for _ in range(1 << m)]
    for i, (mask, _) in enumerate(menu):
        for x in range(1 << m):
            if mask >> x & 1:
                choices[x].append(i)
    nodes = 0

    def visit(indices, covered):
        nonlocal nodes
        nodes += 1
        if len(indices) == count:
            return indices if covered == full else None
        missing = full ^ covered
        if not missing:
            return indices
        options = None
        while missing:
            bit = missing & -missing
            missing ^= bit
            x = bit.bit_length() - 1
            candidates = [i for i in choices[x] if not (menu[i][0] & covered & tight)]
            if options is None or len(candidates) < len(options):
                options = candidates
            if not options:
                return None
        for i in options:
            answer = visit(indices + [i], covered | menu[i][0])
            if answer is not None:
                return answer
        return None

    # Coordinate symmetry permits fixing this first cover.
    answer = visit([0], menu[0][0])
    return answer, nodes


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--paths", type=int, default=6)
    args = parser.parse_args()
    menu = matching_menu(6)
    full = (1 << 64) - 1
    triples = 0
    witness = None
    for i, j, k in combinations(range(len(menu)), 3):
        triples += 1
        if menu[i][0] | menu[j][0] | menu[k][0] == full:
            witness = [menu[t][1] for t in (i, j, k)]
            break
    print("MATCHINGS6", {"candidates": len(menu), "triples_tested": triples,
                         "three_cover": witness}, flush=True)
    alternating = [((0, 1), (2, 3), (4, 5)), ((1, 2), (3, 4), (5, 0))]
    covered = allowed(6, alternating[0]) | allowed(6, alternating[1])
    missing = [x for x in range(64) if not (covered >> x & 1)]
    residuals = []
    for i in (0, 2, 4):
        conditions = {i: 0, (i + 1) % 6: 1, (i + 3) % 6: 0, (i + 4) % 6: 1}
        residuals.append({x for x in range(64)
                          if all((x >> j & 1) == b for j, b in conditions.items())})
    assert set(missing) == set.union(*residuals)
    assert sum(map(len, residuals)) == len(missing) == 12
    print("ALTERNATING6_RESIDUAL", [sorted(x) for x in residuals], flush=True)
    m = args.paths
    menu = path_menu(m, m // 2)
    coefficients = [sum(1 for i in range(m // 2 + 1)
                        if 0 <= r - i <= m - m // 2) for r in range(m + 1)]
    lower = max((comb(m, r) + coefficients[r] - 1) // coefficients[r]
                for r in range(m + 1))
    tight = [r for r in range(m + 1) if lower * coefficients[r] == comb(m, r)]
    print("PATH_MENU", {"m": m, "candidates": len(menu), "rank_lower": lower,
                        "tight_ranks": tight}, flush=True)
    answer, nodes = exact_tight_cover(menu, m, lower, tight)
    print("PATH_COVER", {"m": m, "count": lower, "nodes": nodes,
                         "witness": None if answer is None else [menu[i][1] for i in answer],
                         "equal_side_charge": str(Fraction(lower * (m + 2), 2 ** (m - 1)))},
          flush=True)


if __name__ == "__main__":
    main()
