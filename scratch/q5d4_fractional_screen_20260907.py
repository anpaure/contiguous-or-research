"""Prepared, NOT EXECUTED: bounded all-chain fractional [5]^4 screen.

Run only in a root-authorized ``ssh h100`` session. No local execution,
compilation, or mathematical computation is authorized by this file's
preparation. Python, NumPy, and SciPy must already exist on that host.

Scope: complementary NONEMPTY coordinate shores, all strict chain pairs,
and row charge |C|+|D|. Coordinate permutation reduces a split to its shore
dimensions. Shore exchange reduces 3+1 to 1+3. We therefore enumerate
EVERY strict left chain in [5]^1 and [5]^2, and use the right-node DP to
price every strict right chain in [5]^3 and [5]^2. No chain or point-orbit
count is assumed, copied from q=4, or hard-coded.

For fixed C, a right node z has gain sum_C y(x,z)-unit. Every strict
right chain extends to a saturated bottom-to-top grid path, and any subset
of the vertices on such a path is a strict chain. Replacing negative gains
by zero in a maximum-path DP computes the largest nonnegative violation
over nonempty right chains (allowing the empty subset cannot create a
positive violation). This also prices nonsaturated chains.

The point-orbit master uses S4 and simultaneous coordinate reversal.
An orbit is the coordinate histogram, identified with its reversal.
Uniform indexed development over all 48 group elements makes coverage
constant within each point orbit. Thus exact orbit coverage >= population
is equivalent to pointwise coverage >= 1 after development. Seed weights
are TOTAL developed mass, not the weight on each of the 48 images.
Under simultaneous reflection, reverse each shore's chain order; this
preserves admissibility and cost. Coordinate permutations transport shores.

Floating LPs and pricing only propose columns and dual vectors. Every
reported primal is rationalized and checked exactly. A nontrivial universal
dual is reported only after a COMPLETE integer pricing pass. If raw weights
n_i/D have maximum nonnegative violation v/D, every rectangle has cost
c>=2; hence weights 2*n_i/(2*D+v) are universally feasible. No interrupted
pricing pass is a certificate. Timeout or incomplete search means UNKNOWN
unless an already-complete exact certificate closes a stated gate.

The improvement threshold is 5^3*c9/beta5, where
beta5=(40*pi^2-3*pi^4)/128. Exact Machin bounds enclose the threshold;
the certified c9 interval is retained from the reviewed q4 source.
A fractional candidate is NOT an actual OR word, integral cover, or proof
of compatible fine-point refinement. Empty-shore splits are not included.

Reviewed source (read only):
  /Users/amir.nuriyev/.codex/worktrees/aa30/problem/research_round1/
    q4d4_fractional_screen_round7.py
    ROUND7_THRESHOLD_AND_Q4D4_SCREEN.md

Guards: Linux-only, explicit --authorized-h100-run acknowledgement,
one numerical thread, <=30 s internal wall budget, <=2 GiB address space,
CPU and signal limits. An external process timeout is additionally prudent
because Python signal handling may be delayed inside a native solver.
The output path must be new; existing results are never overwritten.
"""

import argparse
from collections import Counter
from fractions import Fraction
from itertools import product
import json
import math
import os
import signal
import sys
import time


Q = 5
DIMENSION = 4
GROUP_SIZE = 48
CANONICAL_LEFT_DIMENSIONS = (1, 2)


def check_time(deadline, stage):
    if time.monotonic() >= deadline:
        raise TimeoutError(stage + " deadline")


def orbit(point):
    histogram = tuple(point.count(a) for a in range(Q))
    return min(histogram, histogram[::-1])


def below(x, y):
    return x != y and all(a <= b for a, b in zip(x, y))


def strict_chains(points, deadline):
    """All nonempty strict chains, including every comparable jump."""
    upper = []
    for x in points:
        check_time(deadline, "left-chain comparabilities")
        upper.append([j for j, y in enumerate(points) if below(x, y)])
    answer = []

    def extend(chain):
        if len(answer) % 256 == 0:
            check_time(deadline, "left-chain enumeration")
        answer.append(chain)
        for j in upper[chain[-1]]:
            extend(chain + (j,))

    for i in range(len(points)):
        extend((i,))
    return answer


def make_pricing_data(orbit_index, deadline):
    data = []
    for r in CANONICAL_LEFT_DIMENSIONS:
        check_time(deadline, "pricing setup")
        left = list(product(range(Q), repeat=r))
        right = sorted(product(range(Q), repeat=DIMENSION-r),
                       key=lambda x: (sum(x), x))
        right_index = {x: i for i, x in enumerate(right)}
        predecessors = []
        for x in right:
            parents = []
            for a in range(DIMENSION-r):
                if x[a]:
                    y = list(x)
                    y[a] -= 1
                    parents.append(right_index[tuple(y)])
            predecessors.append(parents)
        chains = strict_chains(left, deadline)
        orbit_grid = [[orbit_index[orbit(x+y)] for y in right]
                      for x in left]
        data.append({"r": r, "left": left, "right": right,
                     "predecessors": predecessors, "chains": chains,
                     "orbit_grid": orbit_grid})
    return data


def price_all(data, weights, unit, deadline, columns=False):
    """Integer weights/unit give exact universal nonnegative violation."""
    worst = 0
    candidates = []
    checked = 0
    for shore in data:
        r = shore["r"]
        left, right = shore["left"], shore["right"]
        predecessors, grid = shore["predecessors"], shore["orbit_grid"]
        for chain in shore["chains"]:
            if checked % 16 == 0:
                check_time(deadline, "floating pricing" if columns
                           else "integer certificate pricing")
            checked += 1
            gains = [sum(weights[grid[i][j]] for i in chain)-unit
                     for j in range(len(right))]
            dp = [0] * len(right)
            parent = [-1] * len(right)
            take = [False] * len(right)
            for j in range(len(right)):
                best = 0
                predecessor = -1
                for p in predecessors[j]:
                    if dp[p] > best:
                        best, predecessor = dp[p], p
                parent[j] = predecessor
                if gains[j] > 0:
                    dp[j] = best + gains[j]
                    take[j] = True
                else:
                    dp[j] = best
            violation = dp[-1] - unit*len(chain)
            worst = max(worst, violation)
            if columns and violation > 1e-8:
                selected = []
                j = len(right)-1
                while j >= 0:
                    if take[j]:
                        selected.append(right[j])
                    j = parent[j]
                selected.reverse()
                assert selected
                candidates.append((violation, r,
                                   tuple(left[i] for i in chain),
                                   tuple(selected)))
    check_time(deadline, "completed pricing")
    if columns:
        candidates.sort(key=lambda item: item[0], reverse=True)
    return worst, candidates, checked


def atan_bounds(inv, terms):
    partial = sum((Fraction((-1)**j, (2*j+1)*inv**(2*j+1))
                   for j in range(terms)), Fraction())
    next_term = Fraction((-1)**terms, (2*terms+1)*inv**(2*terms+1))
    return min(partial, partial+next_term), max(partial, partial+next_term)


def threshold_bounds():
    a, b = atan_bounds(5, 40)
    c, d = atan_bounds(239, 8)
    pi_lo, pi_hi = 16*a-4*d, 16*b-4*c
    assert Fraction(3141, 1000) < pi_lo < pi_hi < Fraction(22, 7)
    assert 3*pi_lo*pi_lo > 20  # beta5 is decreasing on this interval.

    def beta5(p):
        return (40*p*p-3*p**4)/128

    beta_lo, beta_hi = beta5(pi_hi), beta5(pi_lo)
    assert 0 < beta_lo < beta_hi
    c9_lo = Fraction(11807038038, 10**10)
    c9_hi = Fraction(11807038039, 10**10)
    factor = Q**(DIMENSION-1)  # q^3, never the q4-specific factor 64.
    return factor*c9_lo/beta_hi, factor*c9_hi/beta_lo


def certify_primal(support, populations, deadline):
    """Exact certificate of uniformly developed, pointwise fractional cover."""
    check_time(deadline, "rational primal")
    assert support and all(isinstance(w, Fraction) and w > 0
                           for w, _ in support)
    coverage = [sum((w*col["census"][i] for w, col in support), Fraction())
                for i in range(len(populations))]
    assert all(a >= b for a, b in zip(coverage, populations))
    cost = sum((w*col["cost"] for w, col in support), Fraction())
    check_time(deadline, "rational primal completion")
    return {
        "cost": str(cost), "cost_decimal_diagnostic": float(cost),
        "orbit_coverage": [str(x) for x in coverage],
        "development": "Uniform indexed S4 times simultaneous reflection",
        "group_size": GROUP_SIZE,
        "weight_semantics": "Seed weight is total developed mass; each indexed image gets weight/48",
        "pointwise_proof": "Orbit transitivity makes developed coverage equal to exact orbit coverage divided by its population, hence at least one at every point.",
        "seeds": [{"weight": str(w), "left_dimension": col["r"],
                   "C": col["C"], "D": col["D"], "cost": col["cost"],
                   "census": col["census"]} for w, col in support],
    }


def rational_primal(solution, catalogue, populations, deadline):
    support = []
    coverage = [Fraction() for _ in populations]
    assert len(solution) == len(catalogue)
    for value, col in zip(solution, catalogue):
        check_time(deadline, "primal rationalization")
        if not math.isfinite(float(value)):
            raise ValueError("nonfinite primal proposal")
        if value <= 1e-10:
            continue
        weight = Fraction(float(value)).limit_denominator(10**6)
        if weight <= 0:
            continue
        support.append((weight, col))
        for i, count in enumerate(col["census"]):
            coverage[i] += weight*count
    if not support or any(value <= 0 for value in coverage):
        return None
    factor = min([Fraction(1)] + [a/b for a, b in zip(coverage, populations)])
    return certify_primal([(w/factor, col) for w, col in support],
                          populations, deadline)


def update_status(report, threshold_lo, threshold_hi):
    primal = report.get("exact_fractional_primal")
    dual = report.get("exact_universal_dual")
    cost = Fraction(primal["cost"]) if primal is not None else None
    lower = Fraction(dual["objective"]) if dual is not None else None
    if cost is not None and lower is not None:
        assert lower <= cost, "exact primal/dual certificates contradict weak duality"
        if lower == cost:
            report["exact_fractional_optimum"] = str(cost)
    report["status"] = "UNKNOWN"
    if cost is not None and cost < threshold_lo:
        report["status"] = "EXACT_FRACTIONAL_CANDIDATE_BELOW_THRESHOLD"
        report["next_gate"] = "Actual compatible colored refinement or integral cover; a fractional candidate is not an OR word."
    elif lower is not None and lower >= threshold_hi:
        report["status"] = "EXACT_DUAL_BLOCKS_FLAT_IMPROVEMENT"


def main():
    if sys.platform != "linux":
        raise SystemExit("Linux-only: execute solely in an authorized ssh h100 session")
    if not __debug__:
        raise SystemExit("Exact certificate checks require assertions; do not use python -O")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--authorized-h100-run", action="store_true")
    parser.add_argument("--seconds", type=float, default=30.0)
    parser.add_argument("--max-rounds", type=int, default=60)
    parser.add_argument("--memory-mib", type=int, default=2048)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    if not args.authorized_h100_run:
        parser.error("--authorized-h100-run requires prior root authorization and ssh h100")
    if not math.isfinite(args.seconds) or not 1.0 <= args.seconds <= 30.0:
        parser.error("--seconds must be finite and between 1 and 30")
    if args.max_rounds < 0:
        parser.error("--max-rounds must be nonnegative")
    if not 512 <= args.memory_mib <= 2048:
        parser.error("--memory-mib must be between 512 and 2048")
    if os.path.exists(args.output):
        parser.error("--output already exists; choose a new result path")

    import resource

    started = time.monotonic()
    hard_deadline = started + args.seconds
    # Reserve time for exact integer pricing and then a small report window.
    certificate_deadline = hard_deadline - 0.25
    search_deadline = started + 0.60*args.seconds
    report = {
        "scope": "All strict chain pairs on complementary nonempty coordinate shores of [5]^4; symmetric point-orbit covering LP",
        "status": "UNKNOWN", "integral_word": False, "q": Q,
        "dimension": DIMENSION, "covered_splits": [[1, 3], [2, 2], [3, 1]],
        "canonical_left_dimensions": list(CANONICAL_LEFT_DIMENSIONS),
        "shore_exchange_reduction": "Every 3+1 rectangle becomes a 1+3 rectangle of the same cost and orbit census after swapping shores and permuting coordinates.",
        "compute_host_requirement": "Prior root authorization; ssh h100 only",
        "wall_budget_seconds": args.seconds, "memory_limit_mib": args.memory_mib,
        "dual_certificate_status": "not_completed", "rounds": [],
    }

    def interrupted(signum, _frame):
        raise TimeoutError("signal guard " + str(signum))

    try:
        memory_limit = args.memory_mib*1024**2
        resource.setrlimit(resource.RLIMIT_AS, (memory_limit, memory_limit))
        cpu_limit = max(1, math.ceil(args.seconds))
        resource.setrlimit(resource.RLIMIT_CPU, (cpu_limit, cpu_limit+1))
        for signum in (signal.SIGALRM, signal.SIGTERM, signal.SIGXCPU):
            signal.signal(signum, interrupted)
        signal.setitimer(signal.ITIMER_REAL, args.seconds)
        for name in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
                     "NUMEXPR_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
            os.environ[name] = "1"

        threshold_lo, threshold_hi = threshold_bounds()
        report["improvement_threshold_lower"] = str(threshold_lo)
        report["improvement_threshold_upper"] = str(threshold_hi)
        report["threshold_diagnostic"] = [float(threshold_lo), float(threshold_hi)]
        report["threshold_formula"] = "q^3*c9/beta5, q=5; beta5=(40*pi^2-3*pi^4)/128"

        counts = Counter(orbit(x) for x in product(range(Q), repeat=DIMENSION))
        orbits = sorted(counts)
        assert sum(counts.values()) == Q**DIMENSION
        orbit_index = {o: i for i, o in enumerate(orbits)}
        populations = [counts[o] for o in orbits]
        report["orbits"] = orbits
        report["point_orbit_count"] = len(orbits)
        report["populations"] = populations
        catalogue, keys = [], {}

        def add(r, C, D):
            check_time(certificate_deadline, "column validation")
            C, D = tuple(C), tuple(D)
            assert 1 <= r < DIMENSION
            for chain, dimension in ((C, r), (D, DIMENSION-r)):
                assert chain and all(len(x) == dimension for x in chain)
                assert all(all(isinstance(a, int) and 0 <= a < Q for a in x)
                           for x in chain)
                assert all(below(x, y) for x, y in zip(chain, chain[1:]))
            census = [0] * len(orbits)
            for x in C:
                for y in D:
                    census[orbit_index[orbit(x+y)]] += 1
            cost = len(C)+len(D)
            assert sum(census) == len(C)*len(D) and cost >= 2
            key = (cost, tuple(census))
            if key in keys:
                return keys[key], False
            col = {"r": r, "C": C, "D": D, "cost": cost, "census": census}
            keys[key] = col
            catalogue.append(col)
            return col, True

        # One singleton seed per point orbit. Giving it total developed
        # weight equal to the orbit population covers every point exactly
        # once. This requires no q-specific hook or integral construction.
        representatives = {}
        for point in product(range(Q), repeat=DIMENSION):
            representatives.setdefault(orbit(point), point)
        fallback = []
        for o in orbits:
            point = representatives[o]
            col, _ = add(1, (point[:1],), (point[1:],))
            fallback.append((Fraction(counts[o]), col))
        report["exact_fractional_primal"] = certify_primal(
            fallback, populations, certificate_deadline)
        report["primal_origin"] = "Exact pointwise singleton feasibility fallback"
        update_status(report, threshold_lo, threshold_hi)

        data = make_pricing_data(orbit_index, certificate_deadline)
        chain_counts = {str(shore["r"]): len(shore["chains"]) for shore in data}
        expected_checks = sum(chain_counts.values())
        report["canonical_left_chain_counts"] = chain_counts
        report["pricing_data_complete"] = True
        report["right_grid_sizes"] = {str(shore["r"]): len(shore["right"])
                                      for shore in data}
        last_dual = None

        try:
            check_time(search_deadline, "column-generation setup")
            import numpy as np
            from scipy.optimize import linprog

            for iteration in range(args.max_rounds):
                check_time(search_deadline, "column generation")
                A = np.asarray([col["census"] for col in catalogue], dtype=float).T
                costs = np.asarray([col["cost"] for col in catalogue], dtype=float)
                remaining = search_deadline-time.monotonic()
                if remaining <= 0.05:
                    break
                result = linprog(costs, A_ub=-A,
                                 b_ub=-np.asarray(populations, dtype=float),
                                 bounds=(0, None), method="highs",
                                 options={"time_limit": remaining, "threads": 1})
                if not result.success:
                    report["solver_message"] = str(result.message)
                    break
                proposal = [-float(x) for x in result.ineqlin.marginals]
                assert all(math.isfinite(x) for x in proposal)
                last_dual = [max(0.0, x) for x in proposal]
                primal = rational_primal(result.x, catalogue, populations,
                                          search_deadline)
                if primal is not None and Fraction(primal["cost"]) < Fraction(
                        report["exact_fractional_primal"]["cost"]):
                    report["exact_fractional_primal"] = primal
                    report["primal_origin"] = "Rationalized and exactly rescaled LP proposal"
                update_status(report, threshold_lo, threshold_hi)
                worst, candidates, checked = price_all(
                    data, last_dual, 1.0, search_deadline, columns=True)
                assert checked == expected_checks
                entry = {"iteration": iteration, "columns": len(catalogue),
                         "objective_diagnostic": float(result.fun),
                         "pricing_violation_diagnostic": float(worst),
                         "left_chains_checked": checked}
                report["rounds"].append(entry)
                added = 0
                for _, r, C, D in candidates:
                    check_time(search_deadline, "column insertion")
                    _, is_new = add(r, C, D)
                    added += int(is_new)
                    if added >= 64:
                        break
                entry["added"] = added
                if worst <= 1e-8 or added == 0:
                    break
        except TimeoutError as exc:
            report["search_time_limit_note"] = str(exc)

        report["columns"] = len(catalogue)
        if last_dual is not None:
            den = 10**9
            numerators = [max(0, math.floor(x*den)) for x in last_dual]
            violation, _, checked = price_all(
                data, numerators, den, certificate_deadline, columns=False)
            assert isinstance(violation, int) and violation >= 0
            assert checked == expected_checks
            cert_den = 2*den+violation
            cert_num = [2*x for x in numerators]
            objective = Fraction(sum(n*p for n, p in zip(cert_num, populations)),
                                 cert_den)
            report["exact_universal_dual"] = {
                "numerators": cert_num, "denominator": cert_den,
                "objective": str(objective),
                "objective_decimal_diagnostic": float(objective),
                "raw_denominator": den, "raw_numerators": numerators,
                "exact_raw_max_violation_numerator": violation,
                "canonical_left_chain_counts": chain_counts,
                "left_chains_checked": checked,
                "integer_pricing_complete": True,
                "proof": "Every strict canonical left chain was checked by integer right-node DP. Coordinate permutations and shore exchange cover splits 1+3, 2+2, and 3+1. Since cost>=2, scaling raw weights by 2D/(2D+v) proves universal feasibility. Empty shores are excluded.",
            }
            report["dual_certificate_status"] = "complete_integer_pricing"
            update_status(report, threshold_lo, threshold_hi)
    except TimeoutError as exc:
        report["time_limit_note"] = str(exc)
    except MemoryError:
        report["error"] = "MemoryError: bounded address-space budget exhausted"
    except Exception as exc:
        report["error"] = type(exc).__name__ + ": " + str(exc)
        # Never promote a result after a failed mathematical assertion.
        if isinstance(exc, AssertionError):
            report["status"] = "CERTIFICATE_CHECK_FAILED"
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        report["elapsed_seconds"] = time.monotonic()-started
        with open(args.output, "x", encoding="utf-8") as handle:
            json.dump(report, handle, indent=2)
            handle.write("\n")
        print(json.dumps({key: report.get(key) for key in
                          ("status", "elapsed_seconds", "columns",
                           "dual_certificate_status", "error", "time_limit_note",
                           "search_time_limit_note")}, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
