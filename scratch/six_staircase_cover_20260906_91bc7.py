"""Five products of directed three-factor staircases, with literal chain costs.

Optional numerical optimization is exploratory, not a coefficient certificate.
"""

import argparse
from itertools import product
from math import pi, sqrt


COVER = (
    ((0, 1, 2), (3, 4, 5)),
    ((1, 2, 4), (3, 5, 0)),
    ((1, 4, 3), (5, 2, 0)),
    ((0, 4, 1), (2, 3, 5)),
    ((4, 2, 3), (5, 0, 1)),
)


def width3(a, b, c):
    a, b, c = sorted((a, b, c))
    return a * b - max(a + b - c, 0) ** 2 / 4


def truncated_width(a, b, c, p):
    return p * c - (max(c - a - b + 2 * p, 0) ** 2
                    - max(c - a - b, 0) ** 2) / 4


def directed_chain_bound(lengths, cuts):
    a, b, c = lengths
    u, v, z = cuts
    h, p = a - u, min(a - u, v)
    w = max(z, min(b - v, c))
    value = truncated_width(a, b, w, p)
    if h >= v:
        value += width3(h - v, b - v, c)
    else:
        value += width3(a - h, v - h, z)
    return value


def staircase_cost(lengths, cuts):
    a, b, c = lengths
    u, v, z = cuts
    volume = a * v * z + (a - u) * (b - v) * c
    count = min(directed_chain_bound(lengths, cuts),
                directed_chain_bound((c, b, a), (c - z, b - v, a - u)))
    return volume, count


def principal(lengths, cuts, cover=COVER):
    total = 0
    for left, right in cover:
        vl, wl = staircase_cost(tuple(lengths[i] for i in left),
                                 tuple(cuts[i] for i in left))
        vr, wr = staircase_cost(tuple(lengths[i] for i in right),
                                 tuple(cuts[i] for i in right))
        total += vl * wr + vr * wl
    return total


def rectangle_chains(a, b):
    return [[(x, j) for x in range(a - j)]
            + [(a - j - 1, y) for y in range(j + 1, b)]
            for j in range(min(a, b))]


def hook_chains(a, b, u, v):
    h, p = a - u, min(a - u, v)
    chains = rectangle_chains(a, b)[:p]
    if h > v:
        chains += [[(u + x, v + y) for x, y in chain]
                   for chain in rectangle_chains(h - v, b - v)]
    elif v > h:
        chains += [[(x, h + y) for x, y in chain]
                   for chain in rectangle_chains(a - h, v - h)]
    return chains


def staircase_chains(lengths, cuts):
    a, b, c = lengths
    u, v, z = cuts
    result = []
    for first in hook_chains(a, b, u, v):
        low = sum(y < v for x, y in first)
        for second in hook_chains(len(first), c, low, z):
            result.append([first[i] + (j,) for i, j in second])
    return result


def best_staircase_chains(lengths, cuts):
    a, b, c = lengths
    u, v, z = cuts
    forward = staircase_chains(lengths, cuts)
    dual = staircase_chains((c, b, a), (c - z, b - v, a - u))
    if len(forward) <= len(dual):
        return forward
    return [[(a - 1 - x[2], b - 1 - x[1], c - 1 - x[0])
             for x in reversed(chain)] for chain in dual]


def finite_chain_count(lengths, cuts):
    a, b, c = lengths
    u, v, z = cuts
    h, p = a - u, min(a - u, v)
    w = max(z, min(b - v, c))
    result = sum(min(a + b - 1 - 2 * j, w) for j in range(p))
    if h >= v:
        x, y, t = h - v, b - v, c
    else:
        x, y, t = a - h, v - h, z
    result += sum(min(x + y - 1 - 2 * j, t) for j in range(min(x, y)))
    return result


def finite_principal(lengths, cuts, cover=COVER):
    total = 0
    for pair in cover:
        data = []
        for indices in pair:
            a, b, c = local = tuple(lengths[i] for i in indices)
            u, v, z = thresholds = tuple(cuts[i] for i in indices)
            volume = a * v * z + (a - u) * (b - v) * c
            count = min(finite_chain_count(local, thresholds),
                        finite_chain_count((c, b, a), (c - z, b - v, a - u)))
            data.append((volume, count))
        (v, w), (z, t) = data
        total += v * t + z * w
    return total


def path_staircase_chains(lengths, cuts):
    chains = [[(x,) for x in range(lengths[0])]]
    for i in range(1, len(lengths)):
        following = []
        for chain in chains:
            low = sum(point[-1] < cuts[i - 1] for point in chain)
            for hook in hook_chains(len(chain), lengths[i], low, cuts[i]):
                following.append([chain[j] + (x,) for j, x in hook])
        chains = following
    return chains


def audit():
    for bits in product((0, 1), repeat=6):
        assert any(all(bits[a] >= bits[b] >= bits[c] for a, b, c in pair)
                   for pair in COVER)
    checked = 0
    for lengths in product(range(1, 5), repeat=3):
        for cuts in product(*(range(a + 1) for a in lengths)):
            chains = staircase_chains(lengths, cuts)
            expected = {x for x in product(*(range(a) for a in lengths))
                        if all((x[i] >= cuts[i]) >= (x[i + 1] >= cuts[i + 1])
                               for i in range(2))}
            flat = [x for chain in chains for x in chain]
            assert len(flat) == len(set(flat)) and set(flat) == expected
            assert all(all(all(a <= b for a, b in zip(x, y))
                           for x, y in zip(chain, chain[1:])) for chain in chains)
            assert len(chains) == finite_chain_count(lengths, cuts)
            best = best_staircase_chains(lengths, cuts)
            assert {x for chain in best for x in chain} == expected
            assert sum(map(len, best)) == len(expected)
            assert all(all(all(a <= b for a, b in zip(x, y))
                           for x, y in zip(chain, chain[1:])) for chain in best)
            checked += 1
    for a in (2, 4, 6, 10):
        chains = staircase_chains((a, a, a), (a // 2,) * 3)
        assert len(chains) == (a // 2) ** 2
        assert sum(map(len, chains)) == a ** 3 // 2
        assert principal((a,) * 6, (a / 2,) * 6) == 5 * a ** 5 / 4
    print("STAIRCASE_AUDIT_PASS", checked)


def optimize(values, iterations):
    import numpy as np
    from scipy.optimize import differential_evolution

    for r in values:
        best = None
        for small in range(6):
            lengths = np.ones(6)
            lengths[small] = r
            answer = differential_evolution(
                lambda cuts: principal(lengths, cuts) / r,
                [(0, x) for x in lengths], seed=906917 + small,
                maxiter=iterations, popsize=12, tol=1e-9, polish=True,
            )
            item = (answer.fun, small, answer.x.tolist())
            if best is None or item[0] < best[0]:
                best = item
        print("NUMERICAL_ONE_SMALL", {"r": r, "best": best,
                                      "half_cut": 5 * (3 - r) / 8,
                                      "six_clock_Jensen_if_uniform": best[0] * sqrt(pi) / 2},
              flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--optimize", type=float, nargs="*")
    parser.add_argument("--iterations", type=int, default=160)
    args = parser.parse_args()
    if args.optimize is None:
        audit()
    else:
        optimize(args.optimize, args.iterations)
