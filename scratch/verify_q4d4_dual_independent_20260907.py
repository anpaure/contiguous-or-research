"""Independent exact proper-shore certificate check. Execute ONLY on ssh h100."""

import argparse
from fractions import Fraction
from itertools import permutations, product
import json
import resource
import signal
import sys


def canonical(point):
    counts = tuple(point.count(i) for i in range(4))
    return min(counts, counts[::-1])


TWICE = {
    (0, 2, 1, 1): 1,
    (0, 2, 2, 0): 4,
    (0, 3, 0, 1): 3,
    (1, 0, 2, 1): 1,
    (1, 1, 0, 2): 2,
    (1, 1, 1, 1): 2,
}


def below(x, y):
    return x != y and all(a <= b for a, b in zip(x, y))


def all_chains(points):
    successors = [[j for j, y in enumerate(points) if below(x, y)]
                  for x in points]

    def visit(chain):
        yield chain
        for j in successors[chain[-1]]:
            yield from visit(chain + (j,))

    for i in range(len(points)):
        yield from visit((i,))


def verify_dual():
    reports = []
    for shore in (1, 2):
        left = list(product(range(4), repeat=shore))
        right = list(product(range(4), repeat=4-shore))
        # This independently prices through ALL strict comparable jumps,
        # not the screen's saturated-path positive-node recurrence.
        successors = [[j for j, y in enumerate(right) if below(x, y)]
                      for x in right]
        count = 0
        largest = -10**9
        for indices in all_chains(left):
            count += 1
            chain = [left[i] for i in indices]
            gains = [sum(TWICE.get(canonical(x+y), 0) for x in chain)-2
                     for y in right]
            best_from = [0] * len(right)
            for i in reversed(range(len(right))):
                best_from[i] = gains[i] + max(
                    [0] + [best_from[j] for j in successors[i]])
            slack = max(best_from)-2*len(chain)
            largest = max(largest, slack)
            assert slack <= 0, (shore, chain, slack)
        assert count == (15 if shore == 1 else 1007)
        reports.append({"left_dimension": shore, "chains": count,
                        "max_twice_dual_minus_twice_cost": largest})
    total = sum(TWICE.get(canonical(x), 0)
                for x in product(range(4), repeat=4))
    assert total == 192
    return reports


def verify_primal(certificate):
    points = list(product(range(4), repeat=4))
    coverage = {x: Fraction(0) for x in points}
    perms = list(permutations(range(4)))
    charge = Fraction(0)
    for seed in certificate["exact_fractional_primal"]["seeds"]:
        left = [tuple(x) for x in seed["C"]]
        right = [tuple(x) for x in seed["D"]]
        shore = seed["left_dimension"]
        assert 1 <= shore <= 3
        for chain, dimension in ((left, shore), (right, 4-shore)):
            assert chain and all(len(x) == dimension for x in chain)
            assert all(all(0 <= a < 4 for a in x) for x in chain)
            assert all(below(x, y) for x, y in zip(chain, chain[1:]))
        weight = Fraction(seed["weight"])
        assert weight > 0
        charge += weight*(len(left)+len(right))
        for x in left:
            for y in right:
                point = x+y
                for p in perms:
                    image = tuple(point[p[i]] for i in range(4))
                    coverage[image] += weight/48
                    coverage[tuple(3-a for a in image)] += weight/48
    assert charge == 96
    assert all(x >= 1 for x in coverage.values())
    return {"exact_charge": str(charge), "points_checked": len(coverage),
            "minimum_coverage": str(min(coverage.values()))}


def main():
    if sys.platform != "linux":
        raise SystemExit("Run only through ssh h100")
    resource.setrlimit(resource.RLIMIT_AS, (256*1024**2, 256*1024**2))
    signal.alarm(10)
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate")
    args = parser.parse_args()
    with open(args.certificate, encoding="utf-8") as handle:
        certificate = json.load(handle)
    dual = verify_dual()
    primal = verify_primal(certificate)
    p = Fraction(22, 7)
    beta_lower = (40*p*p-3*p**4)/128
    assert beta_lower > Fraction(4, 5)
    assert Fraction(96, 64)*beta_lower > Fraction(6, 5)
    assert Fraction(11807038039, 10**10) < Fraction(6, 5)
    print(json.dumps({"status": "EXACT_PROPER_SHORE_FRACTIONAL_OPTIMUM_96",
                      "dual": dual, "primal": primal,
                      "scope": "All strict chain pairs on nonempty complementary shores; no OR-word optimum claimed."},
                     sort_keys=True))


if __name__ == "__main__":
    main()
