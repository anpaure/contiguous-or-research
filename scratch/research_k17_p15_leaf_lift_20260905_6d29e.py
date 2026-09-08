#!/usr/bin/env python3
"""Read-only finite lift experiments from the literal P15 answer chronology."""

import argparse
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from analyze_answer_symmetries_20260905 import extract_middle


def rotate(mask, shift, n):
    shift %= n
    return ((mask << shift) | (mask >> (n - shift))) & ((1 << n) - 1)


def canonical(mask, n):
    return min(rotate(mask, shift, n) for shift in range(n))


def unmatched(mask, n, opening=1):
    remaining = list(range(n))
    while len(remaining) > 1:
        for j, bit in enumerate(remaining):
            following = remaining[(j + 1) % len(remaining)]
            if (mask >> bit) & 1 == opening and (mask >> following) & 1 != opening:
                remaining = [b for b in remaining if b not in (bit, following)]
                break
        else:
            raise AssertionError((mask, n, remaining))
    return remaining[0]


def analyze(cycles, n):
    full, rank = (1 << n) - 1, (n + 1) // 2
    lower = [set() for _ in range(rank)]
    upper = [set() for _ in range(n - rank + 1)]
    runs = Counter()
    for cycle in cycles:
        for i, value in enumerate(cycle):
            lo, hi = value, value
            for q in range(1, rank):
                lo &= cycle[(i + q) % len(cycle)]
                hi |= cycle[(i + q) % len(cycle)]
                if lo.bit_count() == rank - q:
                    lower[q].add(lo)
                if q < len(upper) and hi.bit_count() == rank + q:
                    upper[q].add(hi)
            inserted = value & ~cycle[i - 1]
            while inserted:
                bit = inserted & -inserted
                length = 1
                while cycle[(i + length) % len(cycle)] & bit:
                    length += 1
                    assert length <= len(cycle)
                runs[length] += 1
                inserted ^= bit
    from math import comb
    return {
        "lengths": sorted(map(len, cycles), reverse=True),
        "distinct_middle": len({value for row in cycles for value in row}),
        "bad_edges": sum((a ^ b).bit_count() != 2 for row in cycles
                         for a, b in zip(row, row[1:] + row[:1])),
        "runs": dict(sorted(runs.items())),
        "lower_holes": [comb(n, rank - q) - len(lower[q]) for q in range(1, rank)],
        "upper_holes": [comb(n, rank + q) - len(upper[q]) for q in range(1, len(upper))],
    }


def small_cycle_lifts(old_seed):
    found, seen = [], set()
    for pin in range(17):
        for zero in range(17):
            if pin == zero:
                continue
            injection = [b for b in range(17) if b not in (pin, zero)]
            seed = [(1 << pin) | sum(((value >> j) & 1) << b for j, b in enumerate(injection))
                    for value in old_seed]
            if len({canonical(value, 17) for value in seed}) != 3:
                continue
            for voltage in range(1, 17):
                if (seed[-1] ^ rotate(seed[0], voltage, 17)).bit_count() != 2:
                    continue
                cycle = [rotate(value, sheet * voltage, 17) for sheet in range(17) for value in seed]
                edge_reps = [canonical(a & b, 17) for a, b in zip(cycle[:3], cycle[1:4])]
                if len(set(edge_reps)) != 3:
                    continue
                key = tuple(sorted(canonical(value, 17) for value in cycle))
                if key in seen:
                    continue
                report = analyze([cycle], 17)
                if min(report["runs"]) < 4:
                    continue
                seen.add(key)
                found.append({"pin": pin, "zero": zero, "seed": seed, "voltage": voltage,
                              "middle_reps": sorted({canonical(value, 17) for value in seed}),
                              "lower_reps": sorted(edge_reps), "runs": report["runs"]})
    print("small cycle lifts", len(found), found, flush=True)
    return found


def lifted_menu(endpoints, adjacent_only=False):
    n = 17
    lower_reps = [value for value in range(1 << n)
                  if value.bit_count() == 8 and canonical(value, n) == value]
    choices, weights, by_lower, by_middle, by_upper = [], [], [], defaultdict(list), defaultdict(list)
    inherited_counts = Counter()
    for lower in lower_reps:
        local = Counter()
        for pin in range(n):
            if not (lower >> pin) & 1:
                continue
            for zero in range(n):
                if (lower >> zero) & 1 or (adjacent_only and zero != (pin + 1) % n):
                    continue
                injection = [b for b in range(n) if b not in (pin, zero)]
                old = sum(((lower >> b) & 1) << j for j, b in enumerate(injection))
                a, b = endpoints[old]
                added = tuple(sorted(injection[(value & ~old).bit_length() - 1] for value in (a, b)))
                local[added] += 1
        group = []
        for (a, b), weight in sorted(local.items()):
            index = len(choices)
            choices.append((lower, a, b))
            weights.append(weight)
            group.append(index)
            u, v = lower | (1 << a), lower | (1 << b)
            by_middle[canonical(u, n)].append(index)
            by_middle[canonical(v, n)].append(index)
            by_upper[canonical(u | v, n)].append(index)
        by_lower.append(group)
        inherited_counts[sum(local.values())] += 1
    weighted_degrees = Counter(sum(weights[i] for i in group) for group in by_middle.values())
    print("lift menu", "adjacent" if adjacent_only else "all_pairs", {
        "lower_owners": len(lower_reps), "choices": len(choices),
        "local_domain_histogram": dict(sorted(Counter(map(len, by_lower)).items())),
        "inherited_count_histogram": dict(sorted(inherited_counts.items())),
        "upper_middle_orbits": len(by_middle),
        "weighted_middle_degree_histogram": dict(sorted(weighted_degrees.items())),
        "upper10_orbits_with_support": len(by_upper),
        "weighted_upper10_min": min(sum(weights[i] for i in group) for group in by_upper.values()),
        "self_loop_choices": sum(canonical(l | (1 << a), n) == canonical(l | (1 << b), n)
                                 for l, a, b in choices),
    }, flush=True)
    if not adjacent_only:
        assert inherited_counts == {72: 1430}
        assert weighted_degrees == {144: 1430}
    return choices, by_lower, by_middle, by_upper


def decode(choices, selected):
    adjacency, edge_ids = defaultdict(list), {}
    for index in selected:
        lower, a, b = choices[index]
        for shift in range(17):
            lo = rotate(lower, shift, 17)
            u = lo | (1 << ((a + shift) % 17))
            v = lo | (1 << ((b + shift) % 17))
            adjacency[u].append(v)
            adjacency[v].append(u)
            assert lo not in edge_ids
            edge_ids[lo] = index
    assert len(edge_ids) == len(adjacency) == 24310
    assert all(len(row) == 2 for row in adjacency.values())
    cycles, seen = [], set()
    for start in sorted(adjacency):
        if start in seen:
            continue
        row, previous, current = [], None, start
        while current not in seen:
            seen.add(current)
            row.append(current)
            left, right = sorted(adjacency[current])
            previous, current = current, left if left != previous else right
        assert current == start
        cycles.append(row)
    return cycles, edge_ids


def exact_count(literals, count, top):
    assert count in (1, 2)
    clauses, counters = [], {}
    if count == 1:
        clauses.append(literals)
    else:
        clauses.extend(literals[:i] + literals[i + 1:] for i in range(len(literals)))
    for i, literal in enumerate(literals):
        if i >= count:
            clauses.append([-literal, -counters[i - 1, count - 1]])
        if i == len(literals) - 1:
            break
        for j in range(min(count, i + 1)):
            top += 1
            counters[i, j] = top
            if j == 0:
                clauses.append([-literal, top])
            if (i - 1, j) in counters:
                clauses.append([-counters[i - 1, j], top])
            if j and (i - 1, j - 1) in counters:
                clauses.append([-literal, -counters[i - 1, j - 1], top])
    return clauses, top


def test_cardinality():
    from itertools import product
    for literals in ([1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 1, 2, 3]):
        primary = max(literals)
        for bound in (1, 2):
            clauses, top = exact_count(literals, bound, primary)
            for assignment in product((False, True), repeat=primary):
                expected = sum(assignment[x - 1] for x in literals) == bound
                actual = False
                for aux in product((False, True), repeat=top - primary):
                    values = assignment + aux
                    if all(any(values[abs(x) - 1] == (x > 0) for x in clause) for clause in clauses):
                        actual = True
                        break
                assert expected == actual, (literals, bound, assignment)


def solve_menu(menu, seconds, rounds, upper_eager, resident_eager, seed, output):
    import json
    import subprocess
    import time

    test_cardinality()
    choices, by_lower, by_middle, by_upper = menu
    clauses, top = [], len(choices)
    if resident_eager:
        top = 2 * len(choices)
        frames = {rotate(rep, shift, 17): (rep, shift)
                  for rep in by_middle for shift in range(17)}
        ages = {}
        for rep in by_middle:
            for bit in range(17):
                if rep >> bit & 1:
                    for age in (1, 2, 3):
                        top += 1
                        ages[rep, bit, age] = top
        incoming, outgoing = defaultdict(list), defaultdict(list)
        for i, (lower, a, b) in enumerate(choices):
            for direction, (deleted, inserted) in enumerate(((a, b), (b, a))):
                arc = 2 * i + direction + 1
                source, sphase = frames[lower | (1 << deleted)]
                target, tphase = frames[lower | (1 << inserted)]
                outgoing[source].append(arc)
                incoming[target].append(arc)
                shift = (tphase - sphase) % 17
                leave, enter = (deleted - sphase) % 17, (inserted - tphase) % 17
                clauses.append([-arc, ages[target, enter, 1]])
                for age in (1, 2, 3):
                    clauses.append([-arc, -ages[source, leave, age]])
                for bit in range(17):
                    if source >> bit & 1 and bit != leave:
                        for age in (1, 2):
                            clauses.append([-arc, -ages[source, bit, age],
                                            ages[target, (bit - shift) % 17, age + 1]])
        groups = ([[2 * i + direction + 1 for i in group for direction in (0, 1)]
                   for group in by_lower] + list(incoming.values()) + list(outgoing.values()))
        for group in groups:
            rows, top = exact_count(group, 1, top)
            clauses.extend(rows)
        if upper_eager:
            clauses.extend([2 * i + direction + 1 for i in group for direction in (0, 1)]
                           for group in by_upper.values())
    else:
        for group in by_lower:
            rows, top = exact_count([i + 1 for i in group], 1, top)
            clauses.extend(rows)
        for group in by_middle.values():
            rows, top = exact_count([i + 1 for i in group], 2, top)
            clauses.extend(rows)
        if upper_eager:
            clauses.extend([i + 1 for i in group] for group in by_upper.values())
    print("SAT base", {"variables": top, "clauses": len(clauses),
                       "upper10_eager": upper_eager, "resident_eager": resident_eager}, flush=True)
    started = time.monotonic()
    accumulated = set()
    for round_index in range(rounds):
        remaining = seconds - (time.monotonic() - started)
        if remaining <= 0:
            break
        dimacs = f"p cnf {top} {len(clauses)}\n" + "".join(
            " ".join(map(str, row)) + " 0\n" for row in clauses)
        try:
            result = subprocess.run(["kissat", "-q", f"--seed={seed}", f"--time={max(1, int(remaining))}"],
                                    input=dimacs, text=True, capture_output=True, timeout=remaining + 2)
        except subprocess.TimeoutExpired:
            print("SAT round", round_index, "TIMEOUT", flush=True)
            return
        status = {10: "SAT", 20: "UNSAT", 0: "UNKNOWN"}.get(result.returncode, "ERROR")
        print("SAT round", round_index, status, "seconds", round(time.monotonic() - started, 3), flush=True)
        if result.returncode != 10:
            if result.returncode not in (0, 20):
                print(result.stderr, result.stdout)
            return
        model = [int(value) for line in result.stdout.splitlines() if line.startswith("v ")
                 for value in line[2:].split()]
        positive = {value for value in model if value > 0}
        assert all(any((abs(x) in positive) == (x > 0) for x in row) for row in clauses)
        selected = ([(i - 1) // 2 for i in model if 0 < i <= 2 * len(choices)] if resident_eager else
                    [i - 1 for i in model if 0 < i <= len(choices)])
        cycles, edge_ids = decode(choices, selected)
        report = analyze(cycles, 17)
        cuts = set()
        for cycle in cycles:
            for i, value in enumerate(cycle):
                inserted = value & ~cycle[i - 1]
                for length in (1, 2, 3):
                    after = cycle[(i + length) % len(cycle)]
                    if inserted & ~after:
                        cuts.add(tuple(sorted({edge_ids[cycle[(i - 1 + step) % len(cycle)]
                                                              & cycle[(i + step) % len(cycle)]]
                                               for step in range(length + 1)})))
                        break
        print("factor", {**report, "runs": {r: report["runs"].get(r, 0) for r in (1, 2, 3, 4)}},
              "resident_cuts", len(cuts), flush=True)
        if resident_eager:
            assert not cuts
        if not cuts:
            payload = {"k": 17, "source": "answers/k15.word", "choices": [choices[i] for i in selected],
                       "report": report, "seed": seed, "upper10_eager": upper_eager,
                       "status": "RESIDENT_RAINBOW_FACTOR_NOT_COMPILED"}
            if output:
                output.write_text(json.dumps(payload, indent=2) + "\n")
                print("resident output", str(output), flush=True)
            return
        assert not cuts.intersection(accumulated)
        clauses.extend([-i - 1 for i in cut] for cut in sorted(cuts))
        accumulated.update(cuts)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--menu", choices=("adjacent", "all_pairs", "both"))
    parser.add_argument("--solve", action="store_true")
    parser.add_argument("--seconds", type=float, default=30)
    parser.add_argument("--rounds", type=int, default=100)
    parser.add_argument("--upper-eager", action="store_true")
    parser.add_argument("--resident-eager", action="store_true")
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--small-lifts", action="store_true")
    args = parser.parse_args()
    middle = extract_middle(list(map(int, (ROOT / "answers/k15.word").read_text().split())), 15)
    cycles = [middle[:6390], middle[6390:]]
    print("P15", analyze(cycles, 15), flush=True)
    endpoints = {}
    for cycle in cycles:
        for a, b in zip(cycle, cycle[1:] + cycle[:1]):
            assert a & b not in endpoints
            endpoints[a & b] = (a, b)
    for opening in (0, 1):
        hits = Counter()
        for lower, (a, b) in endpoints.items():
            extension = lower | (1 << unmatched(lower, 15, opening))
            hits[(extension == a, extension == b)] += 1
        print("P15 unmatched matching", opening, dict(hits), flush=True)
    for length, cycle in zip((426, 3), cycles):
        seed = cycle[:length]
        assert all(rotate(a, 4, 15) == b for a, b in zip(cycle, cycle[length:]))
        for pin, zero in ((15, 16), (16, 15)):
            lifted = [value | (1 << pin) for value in seed]
            reps = [canonical(value, 17) for value in lifted]
            print("padded seed", length, pin, zero, "distinct_orbits", len(set(reps)),
                  "collisions", len(reps) - len(set(reps)), flush=True)
    if args.small_lifts:
        small_cycle_lifts(cycles[1][:3])
    if args.menu:
        for mode in (("adjacent", "all_pairs") if args.menu == "both" else (args.menu,)):
            menu = lifted_menu(endpoints, adjacent_only=mode == "adjacent")
            if args.solve:
                solve_menu(menu, args.seconds, args.rounds, args.upper_eager,
                           args.resident_eager, args.seed, args.output)


if __name__ == "__main__":
    main()
