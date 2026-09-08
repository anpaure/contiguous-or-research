"""Prepared, NOT EXECUTED: independent stdlib [5]^4 certificate verifier.

Execute only through ssh h100 after root review and authorization. No local
execution or compilation is authorized. Input is the returned q5 screen
JSON, not Python code. This verifier does not import or run the screen.

All strict chains on the left are enumerated for shore dimensions 1 and 2.
For each, the right-chain DP uses ALL STRICT COMPARABLE JUMPS, including
negative-gain starting nodes, not the screen's saturated-path recurrence.
Coordinate permutations cover all coordinate partitions of these sizes;
shore exchange covers 3+1 from 1+3. Empty shores remain excluded.

The returned raw integer dual is repriced exactly. Its reported corrected
dual is checked algebraically against the complete raw violation bound.
Every primal seed is independently validated and all 48 indexed images
are expanded, checking coverage separately at all 625 points. Reflection
reverses each shore's chain order, preserving its admissibility and charge.

By default a denominator-six dual is proposed by exact nearest rounding
of the raw weights. It is certified ONLY after a second complete strict-
jump pricing pass. Matching its verified objective to the verified primal
may prove the fractional optimum; it never proves an integral optimum or
an actual OR word. The conservative flat-compiler exclusion uses only
verified dual mass >188 and (188/125)*(4/5)>the accepted c9 upper bound.

Guards: Linux only, enabled assertions, 10-second alarm, 256 MiB address
space. Only the caller may authorize and launch a remote verification.
"""

import argparse
from collections import Counter
from fractions import Fraction
from itertools import permutations, product
import json
import resource
import signal
import sys
import time


Q = 5
DIMENSION = 4
EXPECTED_CHAIN_COUNTS = {1: 31, 2: 10271}


def canonical(point):
    histogram = tuple(point.count(a) for a in range(Q))
    return min(histogram, histogram[::-1])


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


def price_dual(numerators, denominator, orbit_index):
    """Return exact maximum slack; a positive value rejects this dual."""
    assert type(denominator) is int and denominator > 0
    assert all(type(n) is int and n >= 0 for n in numerators)
    reports = []
    largest_overall = None
    for shore in (1, 2):
        left = list(product(range(Q), repeat=shore))
        right = list(product(range(Q), repeat=DIMENSION-shore))
        successors = [[j for j, y in enumerate(right) if below(x, y)]
                      for x in right]
        # Product lexicographic order is a topological order for strict <=.
        assert all(j > i for i, row in enumerate(successors) for j in row)
        grid = [[numerators[orbit_index[canonical(x+y)]] for y in right]
                for x in left]
        count = 0
        largest = None
        witness = None
        for indices in all_chains(left):
            count += 1
            gains = [sum(grid[i][j] for i in indices)-denominator
                     for j in range(len(right))]
            best_from = [0] * len(right)
            for i in reversed(range(len(right))):
                continuation = max([0] + [best_from[j] for j in successors[i]])
                best_from[i] = gains[i] + continuation
            # max(best_from) optimizes a NONEMPTY strict right chain.
            slack = max(best_from)-denominator*len(indices)
            if largest is None or slack > largest:
                largest = slack
                witness = [left[i] for i in indices]
        assert count == EXPECTED_CHAIN_COUNTS[shore]
        assert largest is not None
        if largest_overall is None or largest > largest_overall:
            largest_overall = largest
        entry = {"left_dimension": shore, "chains_checked": count,
                 "maximum_mass_minus_cost_numerator": largest}
        if largest > 0:
            entry["violating_left_chain"] = witness
        reports.append(entry)
    assert largest_overall is not None
    return {"complete": True, "feasible": largest_overall <= 0,
            "denominator": denominator, "numerators": numerators,
            "maximum_mass_minus_cost_numerator": largest_overall,
            "nonnegative_violation_numerator": max(0, largest_overall),
            "shore_checks": reports}


def verify_primal(certificate, points, orbits, orbit_index):
    primal = certificate["exact_fractional_primal"]
    coverage = {point: Fraction() for point in points}
    exact_orbit_coverage = [Fraction() for _ in orbits]
    perms = list(permutations(range(DIMENSION)))
    assert len(perms) == 24
    assert primal["group_size"] == 48
    charge = Fraction()
    seeds = primal["seeds"]
    assert seeds
    for seed in seeds:
        left = [tuple(x) for x in seed["C"]]
        right = [tuple(x) for x in seed["D"]]
        shore = seed["left_dimension"]
        assert type(shore) is int and 1 <= shore < DIMENSION
        for chain, dimension in ((left, shore), (right, DIMENSION-shore)):
            assert chain and all(len(x) == dimension for x in chain)
            assert all(all(type(a) is int and 0 <= a < Q for a in x)
                       for x in chain)
            assert all(below(x, y) for x, y in zip(chain, chain[1:]))
        weight = Fraction(seed["weight"])
        assert weight > 0
        cost = len(left)+len(right)
        assert seed["cost"] == cost
        charge += weight*cost
        census = [0] * len(orbits)
        image_weight = weight/48
        for x in left:
            for y in right:
                point = x+y
                census[orbit_index[canonical(point)]] += 1
                for permutation in perms:
                    image = tuple(point[permutation[i]] for i in range(DIMENSION))
                    coverage[image] += image_weight
                    coverage[tuple(Q-1-a for a in image)] += image_weight
        assert census == seed["census"]
        for i, count in enumerate(census):
            exact_orbit_coverage[i] += weight*count
    assert charge == Fraction(primal["cost"]) == Fraction(566, 3)
    assert len(coverage) == 625 and all(value >= 1 for value in coverage.values())
    assert exact_orbit_coverage == [Fraction(x) for x in primal["orbit_coverage"]]
    pointwise_orbit_totals = [Fraction() for _ in orbits]
    for point, value in coverage.items():
        pointwise_orbit_totals[orbit_index[canonical(point)]] += value
    assert pointwise_orbit_totals == exact_orbit_coverage
    return {"exact_charge": str(charge), "points_checked": len(coverage),
            "indexed_images_per_seed": 48, "seeds_checked": len(seeds),
            "minimum_pointwise_coverage": str(min(coverage.values())),
            "proof": "Every indexed coordinate-permutation/reflection image was expanded and every point's exact Fraction coverage is at least one."}


def main():
    if sys.platform != "linux":
        raise SystemExit("Linux only: run through an authorized ssh h100 session")
    if not __debug__:
        raise SystemExit("Assertions are certificate checks; do not run with python -O")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("certificate")
    parser.add_argument("--skip-denominator-six", action="store_true")
    args = parser.parse_args()
    started = time.monotonic()
    report = {"status": "UNKNOWN", "q": Q, "dimension": DIMENSION,
              "scope": "All strict chain pairs on nonempty complementary coordinate shores; 3+1 follows from 1+3 by shore exchange.",
              "actual_OR_word": False, "integral_optimum_claimed": False,
              "input_certificate": args.certificate}

    def time_limit(_signum, _frame):
        raise TimeoutError("10-second independent-verifier alarm")

    try:
        resource.setrlimit(resource.RLIMIT_AS, (256*1024**2, 256*1024**2))
        signal.signal(signal.SIGALRM, time_limit)
        signal.alarm(10)
        with open(args.certificate, encoding="utf-8") as handle:
            certificate = json.load(handle)
        assert certificate["q"] == Q and certificate["dimension"] == DIMENSION
        points = list(product(range(Q), repeat=DIMENSION))
        assert len(points) == 625
        counts = Counter(canonical(point) for point in points)
        orbits = sorted(counts)
        assert orbits == [tuple(o) for o in certificate["orbits"]]
        populations = [counts[o] for o in orbits]
        assert populations == certificate["populations"]
        orbit_index = {o: i for i, o in enumerate(orbits)}
        report["orbits"] = orbits
        report["populations"] = populations

        supplied_dual = certificate["exact_universal_dual"]
        raw_num = supplied_dual["raw_numerators"]
        raw_den = supplied_dual["raw_denominator"]
        assert len(raw_num) == len(orbits)
        raw_check = price_dual(raw_num, raw_den, orbit_index)
        violation = raw_check["nonnegative_violation_numerator"]
        assert violation == supplied_dual["exact_raw_max_violation_numerator"]
        cert_num = supplied_dual["numerators"]
        cert_den = supplied_dual["denominator"]
        assert cert_num == [2*n for n in raw_num]
        assert cert_den == 2*raw_den+violation
        # For every nonempty rectangle c>=2 and raw mass <= D*c+v.
        # Thus 2*raw_mass/(2D+v) <= c, also if the raw vector violates.
        dual_objective = Fraction(sum(n*p for n, p in zip(cert_num, populations)),
                                  cert_den)
        assert dual_objective == Fraction(supplied_dual["objective"])
        raw_check["raw_objective"] = str(Fraction(
            sum(n*p for n, p in zip(raw_num, populations)), raw_den))
        report["raw_dual_strict_jump_check"] = raw_check
        report["verified_corrected_dual"] = {
            "numerators": cert_num, "denominator": cert_den,
            "objective": str(dual_objective),
            "feasibility_proof": "Complete strict-jump raw pricing followed by checked cost>=2 scaling 2D/(2D+v)."}

        primal_check = verify_primal(certificate, points, orbits, orbit_index)
        report["pointwise_primal_check"] = primal_check
        primal_cost = Fraction(primal_check["exact_charge"])
        assert dual_objective <= primal_cost
        assert dual_objective > 188
        p = Fraction(22, 7)
        beta_lower = (40*p*p-3*p**4)/128
        assert 3*Fraction(3141, 1000)**2 > 20
        assert beta_lower > Fraction(4, 5)
        c9_upper = Fraction(11807038039, 10**10)
        conservative_coefficient = Fraction(188, 125)*Fraction(4, 5)
        assert conservative_coefficient > c9_upper
        report["conservative_flat_exclusion"] = {
            "verified_dual_greater_than": 188,
            "beta5_lower_bound": "4/5",
            "beta5_at_22_over_7": str(beta_lower),
            "coefficient_lower_bound": str(conservative_coefficient),
            "accepted_c9_upper_bound": str(c9_upper),
            "proof": "beta5 decreases on the accepted pi interval (3141/1000,22/7), so beta5>beta5(22/7)>4/5. The verified flat charge exceeds 188, and (188/125)*(4/5)>c9_upper."}
        report["status"] = "EXACT_DUAL_BLOCKS_FLAT_IMPROVEMENT"

        if not args.skip_denominator_six:
            # Exact nearest integer to 6*n/D, with ties rounded upward.
            # This is only a proposal until ALL inequalities are repriced.
            sixths = [(12*n+raw_den)//(2*raw_den) for n in raw_num]
            rounded_check = price_dual(sixths, 6, orbit_index)
            rounded_objective = Fraction(sum(n*p for n, p in zip(sixths, populations)), 6)
            rounded_check["objective"] = str(rounded_objective)
            report["denominator_six_proposal_check"] = rounded_check
            if rounded_check["feasible"]:
                assert rounded_objective <= primal_cost
                report["verified_denominator_six_dual"] = {
                    "numerators": sixths, "denominator": 6,
                    "objective": str(rounded_objective)}
                if rounded_objective == primal_cost:
                    report["exact_fractional_optimum"] = str(primal_cost)
                    report["status"] = "EXACT_PROPER_SHORE_FRACTIONAL_OPTIMUM_566_OVER_3"
    except TimeoutError as exc:
        report["time_limit_note"] = str(exc)
        # A previously completed base certificate remains valid; an
        # incomplete optional rounded-dual pass is not a certificate.
    except Exception as exc:
        report["status"] = "VERIFICATION_FAILED"
        report["error"] = type(exc).__name__ + ": " + str(exc)
    finally:
        signal.alarm(0)
        report["elapsed_seconds"] = time.monotonic()-started
        print(json.dumps(report, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
