#!/usr/bin/env python3
"""Independent literal physical audit; no C++ catalogue/scoring code imported."""
import argparse
from collections import Counter, defaultdict
from concurrent.futures import ProcessPoolExecutor
from functools import cache
from hashlib import sha256
import importlib.util
from itertools import combinations
import json
from pathlib import Path
import sys

K, R, N, W = 17, 9, 1430, 24310
FULL = (1 << K) - 1
RANKS = (10, 7, 11, 6)


def check(condition, message):
    if not condition:
        raise ValueError(message)


def rotate(value, shift):
    shift %= K
    return ((value << shift) | (value >> (K - shift))) & FULL


@cache
def canonical(value):
    return min(rotate(value, shift) for shift in range(K))


@cache
def representatives(rank):
    return frozenset(canonical(sum(1 << bit for bit in items)) for items in combinations(range(K), rank))


def stable(value):
    return json.dumps(value, separators=(",", ":"), sort_keys=True).encode()


def run_lengths(cycle, bit, positive):
    size = len(cycle)
    zero = next((i for i, value in enumerate(cycle) if bool(value & (1 << bit)) != positive), None)
    if zero is None:
        yield size
        return
    length = 0
    for step in range(1, size + 1):
        if bool(cycle[(zero + step) % size] & (1 << bit)) == positive:
            length += 1
        elif length:
            yield length
            length = 0


def audit(path):
    path = Path(path)
    data = json.loads(path.read_text())
    check((data["k"], data["r"], data["N"], data["W"], data["d"]) == (17, 9, 1430, 24310, 3), "instance header")
    choices = sorted((int(low), min(int(a), int(b)), max(int(a), int(b))) for low, a, b in data["choices"])
    check(len(choices) == N and {low for low, a, b in choices} == representatives(8), "exactly one row per lower orbit")
    adjacency = defaultdict(list)
    facets = Counter()
    loops = 0
    for low, a, b in choices:
        check(0 <= a < b < K and not low & ((1 << a) | (1 << b)), "valid distinct extensions")
        first, second = low | (1 << a), low | (1 << b)
        loops += canonical(first) == canonical(second)
        for shift in range(K):
            u, v = rotate(first, shift), rotate(second, shift)
            check(u != v and (u & v).bit_count() == 8, "physical Johnson edge")
            adjacency[u].append(v)
            adjacency[v].append(u)
            facets[u & v] += 1
    check(len(adjacency) == W and all(value.bit_count() == R and len(neighbors) == 2 and neighbors[0] != neighbors[1]
                                     for value, neighbors in adjacency.items()), "degree two at every distinct rank-nine owner")
    check(len(facets) == W and set(facets.values()) == {1} and all(value.bit_count() == 8 for value in facets), "every rank-eight facet once")
    check(loops == 0, "pipeline quotient loops excluded")

    body = path.with_suffix(".txt")
    check(body.exists(), "restartable matching body exists")
    lines = body.read_text().splitlines()
    check(lines[0] == "K17QF1 17 1430 24310 3" and len(lines) == N + 1, "body header/length")
    coloured = [tuple(map(int, line.split())) for line in lines[1:]]
    check(all(len(row) == 3 for row in coloured), "body triples")
    check(sorted((low, min(a, b), max(a, b)) for low, a, b in coloured) == choices, "JSON and body agree")
    for column in (1, 2):
        mids = [canonical(row[0] | (1 << row[column])) for row in coloured]
        check(len(set(mids)) == N and set(mids) == representatives(9), "body colour is a perfect matching")

    seen = set()
    cycles = []
    for start in sorted(adjacency):
        if start in seen:
            continue
        cycle = []
        previous, current = None, start
        while current not in seen:
            seen.add(current)
            cycle.append(current)
            left, right = sorted(adjacency[current])
            check(previous is None or previous in (left, right), "physical predecessor edge")
            previous, current = current, left if previous is None or left != previous else right
        check(current == start and len(cycle) >= 3, "actual cyclic order closes")
        cycles.append(cycle)
    check(len(seen) == W, "physical traversal covers all owners")
    cycles.sort(key=lambda cycle: (-len(cycle), cycle[0]))
    owner_component = {value: i for i, cycle in enumerate(cycles) for value in cycle}
    component_seen = set()
    quotient_cycles = 0
    for i, cycle in enumerate(cycles):
        if i in component_seen:
            continue
        quotient_cycles += 1
        orbit = {owner_component[rotate(cycle[0], shift)] for shift in range(K)}
        check(len(orbit) in (1, K) and not orbit & component_seen, "rotation orbit of physical components")
        component_seen.update(orbit)

    loads = [Counter() for _ in RANKS]
    positive, zero = Counter(), Counter()
    upper_got = defaultdict(set)
    constant_bad3_physical = 0
    for cycle in cycles:
        size = len(cycle)
        total_union, common = 0, FULL
        for value in cycle:
            total_union |= value
            common &= value
        if size == 3:
            constant_bad3_physical += common.bit_count()
        for bit in range(K):
            positive.update(run_lengths(cycle, bit, True))
            zero.update(run_lengths(cycle, bit, False))
        for i, a in enumerate(cycle):
            b, c, d = (cycle[(i + age) % size] for age in (1, 2, 3))
            for rank, mask, counts in zip(RANKS, (a | b, a & b & c, a | b | c, a & b & c & d), loads):
                if mask.bit_count() == rank:
                    counts[canonical(mask)] += 1
            union = a
            for age in range(1, size):
                old = union
                union |= cycle[(i + age) % size]
                if old != union and union.bit_count() > R:
                    upper_got[union.bit_count()].add(canonical(union))
                if union == total_union:
                    break

    check(positive[1] == 0, "positive run one is excluded by exact factor")
    check(all(value % K == 0 for counts in loads for value in counts.values()), "shadow multiplicities have 17 sheets")
    check(positive[2] % K == positive[3] % K == constant_bad3_physical % K == 0, "residence orbit multiplicities")
    missing_sets = [sorted(representatives(rank) - counts.keys()) for rank, counts in zip(RANKS, loads)]
    missing = list(map(len, missing_sets))
    pairs = [sum((value // K) * (value // K - 1) // 2 for value in counts.values()) for counts in loads]
    invalid = [N - sum(counts.values()) // K for counts in loads]
    upper_missing = {rank: sorted(representatives(rank) - upper_got[rank]) for rank in range(10, 18)}
    check(upper_missing[10] == missing_sets[0] and upper_missing[11] == missing_sets[2], "arbitrary-width U1/U2 agree with short decks")
    q = data["quotient_score"]
    actual = dict(bad2_orbits=positive[2] // K, bad3_orbits=positive[3] // K,
                  constant_bad3_orbits=constant_bad3_physical // K,
                  residence_shortfall_orbits=(2 * positive[2] + positive[3]) // K,
                  missing_orbits=missing, pair_collisions=pairs, invalid_rank_starts=invalid,
                  physical_cycles=len(cycles), quotient_cycles=quotient_cycles,
                  zero_voltage_cycles=sum(len(cycle) % K != 0 for cycle in cycles) // K,
                  min_component=min(map(len, cycles)), max_component=max(map(len, cycles)), quotient_loops=loops)
    # A voltage-zero component can have a length divisible by 17. Count its
    # 17-element physical-component orbit, rather than infer voltage from length.
    component_orbits = {tuple(sorted(owner_component[rotate(cycle[0], shift)] for shift in range(K))) for cycle in cycles}
    actual["zero_voltage_cycles"] = sum(len(set(orbit)) == K for orbit in component_orbits)
    for name, value in actual.items():
        check(q[name] == value, f"quotient mismatch {name}: saved={q[name]} actual={value}")
    cpp = data.get("physical_audit")
    if cpp:
        check(cpp["positive_bad_runs_by_length"] == [positive[i] for i in (1, 2, 3)], "C++ positive runs")
        check(cpp["residence_shortfall"] == 2 * positive[2] + positive[3], "C++ shortfall")
        check(cpp["minimum_positive_run"] == min(positive), "C++ minimum positive run")
        check(cpp["short_zero_gaps_not_forbidden"] == sum(zero[i] for i in (1, 2, 3)), "C++ zero-gap diagnostic")
        check(cpp["physical_cycle_lengths"] == list(map(len, cycles)), "C++ physical component sizes")
        check(cpp["all_width_upper_missing_orbits_by_rank_10_to_17"] == [len(upper_missing[r]) for r in range(10, 18)], "C++ all-width upper deck")
    passed = not actual["residence_shortfall_orbits"] and not any(missing) and not any(upper_missing.values())
    report = dict(status="EXACT_FACTOR_AUDIT_PASS", candidate=str(path), quotient_score=actual,
                  body_sha256=sha256(body.read_bytes()).hexdigest(), json_sha256=sha256(path.read_bytes()).hexdigest(),
                  choices_sha256=sha256(stable(choices)).hexdigest(), physical_cycles_sha256=sha256(stable(cycles)).hexdigest(),
                  degree2_owners=W, once_only_rank8_facets=W, positive_run_histogram=dict(sorted(positive.items())),
                  zero_gap_histogram_not_forbidden=dict(sorted(zero.items())),
                  physical_bad_runs_by_length=[positive[i] for i in (1, 2, 3)],
                  physical_residence_shortfall=2 * positive[2] + positive[3], minimum_positive_run=min(positive),
                  physical_cycle_lengths=list(map(len, cycles)), missing_deck_orbit_representatives=missing_sets,
                  all_width_upper_missing_orbits_by_rank={r: len(upper_missing[r]) for r in range(10, 18)},
                  all_width_upper_missing_representatives=upper_missing, carrier_gates_pass=passed,
                  connectivity_pending=len(cycles) != 1, is_compiled_word=False)
    output = path.with_suffix(".independent_audit.json")
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    return dict(path=str(path), report=str(output), score=actual, body_sha256=report["body_sha256"],
                all_upper=[len(upper_missing[r]) for r in range(10, 18)], carrier_pass=passed)


def pipeline_attempt(result, pipeline):
    # The independent pipeline is attempted as soon as residence and U1 pass;
    # compilation is only attempted after every carrier gate and connectivity.
    score = result["score"]
    if score["residence_shortfall_orbits"] or score["missing_orbits"][0]:
        return
    spec = importlib.util.spec_from_file_location("f6c2e_pipeline", pipeline)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    path = Path(result["path"])
    data = json.loads(path.read_text())
    catalogue = module.QuotientCatalogue(17)
    selected = catalogue.ids_from_explicit(data["choices"])
    cycles, report = module.validate_cycle_cover(catalogue, selected)
    path.with_suffix(".pipeline_audit.json").write_text(json.dumps(report, indent=2) + "\n")
    if report["carrier_pass"] and len(cycles) == 1:
        result["compile"] = module.compile_carrier(path, path.with_suffix(".compiled.txt"),
                                                  path.with_suffix(".compile_audit.json"), 8, int(data["seed"]))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*", type=Path)
    parser.add_argument("--directory", type=Path)
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--pipeline", type=Path)
    args = parser.parse_args()
    if not 1 <= args.workers <= 8:
        parser.error("workers must be 1..8")
    paths = args.paths
    if args.directory:
        paths += sorted(path for kind in ("initial", "best", "residence", "u1")
                        for path in args.directory.glob(f"*.{kind}.json"))
    if not paths:
        parser.error("give JSON candidates or --directory")
    with ProcessPoolExecutor(max_workers=args.workers) as pool:
        results = list(pool.map(audit, paths))
    for result in results:
        if args.pipeline:
            pipeline_attempt(result, args.pipeline)
        print(json.dumps(result, sort_keys=True), flush=True)
    if args.directory:
        (args.directory / "independent_summary.json").write_text(json.dumps(results, indent=2, sort_keys=True) + "\n")
    print(f"INDEPENDENT_AUDIT_PASS candidates={len(results)}", flush=True)


if __name__ == "__main__":
    main()
