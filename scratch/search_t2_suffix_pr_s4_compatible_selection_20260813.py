#!/usr/bin/env python3
"""Search a vertex-disjoint q2-safe actuator on every PR edge of D_4."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tempfile
from collections import Counter, defaultdict, deque
from functools import lru_cache
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import search_t2_cross_suffix_alternating_cycles_20260813 as base  # noqa:E402


def ascent(word):
    return len(word) - len(word.lstrip("1"))


def flip(word):
    k = ascent(word)
    return "1" * (k - 1) + "01" + word[k + 1:]


def insert(word):
    k = ascent(word)
    return "1" * (k + 1) + "00" + word[k + 1:]


@lru_cache(None)
def family(n, k):
    if k == n:
        return ("1" * n + "0" * n,)
    if k == 1:
        return tuple(flip(word) for word in family(n, 2))
    return (
        tuple(flip(word) for word in reversed(family(n, k + 1)))
        + tuple(insert(word) for word in family(n - 1, k - 1))
    )


def pr_path(n):
    return (
        sum((family(n, k) for k in range(n, 1, -1)), ())
        + tuple(reversed(family(n, 1)))
    )


def at_most_one(variables, clauses, next_variable):
    variables = sorted(set(variables))
    if len(variables) <= 1:
        return next_variable
    auxiliaries = list(range(next_variable, next_variable + len(variables) - 1))
    clauses.append([-variables[0], auxiliaries[0]])
    for i in range(1, len(variables) - 1):
        clauses.append([-variables[i], auxiliaries[i]])
        clauses.append([-auxiliaries[i - 1], auxiliaries[i]])
        clauses.append([-variables[i], -auxiliaries[i - 1]])
    clauses.append([-variables[-1], -auxiliaries[-1]])
    return next_variable + len(auxiliaries)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dump-candidates")
    args = parser.parse_args()
    m, n = 10, 20
    minimum_owner_lengths = [10, 9, 9, 11, 9, 12, 9, 11, 7, 11, 10, 11, 10]
    selected = base.canonical_edges(m)
    base.apply_t2(selected, list(base.dyck_words(4)))
    by_owner, by_colour = base.factor_maps(selected)
    internal = {owner for owner, colours in by_owner.items() if len(colours) == 2}
    base.INTERNAL_OWNERS = internal
    loads = Counter(
        colours[0] | colours[1]
        for colours in by_owner.values() if len(colours) == 2
    )

    def reverse_steps(owner):
        for colour in by_owner[owner]:
            remainder = colour
            while remainder:
                bit = remainder & -remainder
                remainder -= bit
                predecessor = colour ^ bit
                if predecessor in internal and (predecessor, colour) not in selected:
                    yield predecessor, colour

    def distances_to(target, maximum):
        distance = {target: 0}
        queue = deque([target])
        while queue:
            owner = queue.popleft()
            if distance[owner] >= maximum:
                continue
            for predecessor, _ in reverse_steps(owner):
                if predecessor not in distance:
                    distance[predecessor] = distance[owner] + 1
                    queue.append(predecessor)
        return distance

    def exact_paths(start, target, length, distance):
        answer = []

        def rec(owner, owners, colours):
            remainder = length - len(owners) + 1
            if distance.get(owner, 10**9) > remainder:
                return
            if remainder == 0:
                if owner == target:
                    answer.append((owners, colours))
                return
            for next_owner, colour in base.directed_steps(
                owner, n, selected, by_colour
            ):
                if next_owner in owners or colour in colours:
                    continue
                rec(next_owner, owners + [next_owner], colours + [colour])

        rec(start, [start], [])
        return answer

    path = pr_path(4)
    candidate_groups = []
    for edge_index, (left, right) in enumerate(zip(path, path[1:])):
        candidates = {}
        total_length = minimum_owner_lengths[edge_index]
        for prefix in (base.T2[4][0], base.T2[5][0]):
            a = base.bits(prefix) | (base.bits(left) << 12)
            b = base.bits(prefix) | (base.bits(right) << 12)
            distance_b = distances_to(b, total_length)
            distance_a = distances_to(a, total_length)
            for forward_length in range(
                distance_b[a], total_length - distance_a[b] + 1
            ):
                reverse_length = total_length - forward_length
                forward = exact_paths(a, b, forward_length, distance_b)
                reverse = exact_paths(b, a, reverse_length, distance_a)
                for p in forward:
                    for q in reverse:
                        cycle = base.combine_cycle(p, q)
                        if cycle is None:
                            continue
                        _, losses, _ = base.q2_current(
                            cycle, by_owner, loads
                        )
                        if losses:
                            continue
                        owners, new_colours = cycle
                        key = (tuple(owners), tuple(new_colours))
                        candidates[key] = {
                            "suffix_edge": [left, right],
                            "prefix": prefix,
                            "incidence_length": 2 * len(owners),
                            "owners": owners,
                            "new_colours": new_colours,
                        }
        assert candidates, (left, right)
        candidate_groups.append(list(candidates.values()))
        print(
            f"c edge {edge_index}: {left} {right}, "
            f"candidates={len(candidates)}",
            file=sys.stderr,
            flush=True,
        )

    if args.dump_candidates:
        serializable = []
        for group in candidate_groups:
            serializable.append([
                {
                    **candidate,
                    "owners": [base.bitword(x, n) for x in candidate["owners"]],
                    "new_colours": [
                        base.bitword(x, n) for x in candidate["new_colours"]
                    ],
                }
                for candidate in group
            ])
        Path(args.dump_candidates).write_text(
            json.dumps(serializable, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )

    def compatible(left, right):
        return not (
            set(left["owners"]) & set(right["owners"])
            or set(left["new_colours"]) & set(right["new_colours"])
        )

    pair_compatibility = {}
    for i in range(len(candidate_groups)):
        for j in range(i + 1, len(candidate_groups)):
            count = sum(
                compatible(left, right)
                for left in candidate_groups[i]
                for right in candidate_groups[j]
            )
            pair_compatibility[(i, j)] = count
            if count == 0:
                print(f"c incompatible edge pair: {i} {j}", file=sys.stderr)

    # Exact arc-consistency diagnostic for the binary conflict CSP.
    domains = [set(range(len(group))) for group in candidate_groups]
    changed = True
    while changed and all(domains):
        changed = False
        for i in range(len(domains)):
            remove = set()
            for x in domains[i]:
                for j in range(len(domains)):
                    if i == j:
                        continue
                    if not any(
                        compatible(candidate_groups[i][x], candidate_groups[j][y])
                        for y in domains[j]
                    ):
                        remove.add(x)
                        break
            if remove:
                domains[i] -= remove
                changed = True
    print(
        "c arc domains: " + " ".join(str(len(domain)) for domain in domains),
        file=sys.stderr,
    )

    candidate_variables = []
    variable_to_candidate = {}
    resources = defaultdict(list)
    variable = 1
    for edge_index, candidates in enumerate(candidate_groups):
        group = []
        for candidate in candidates:
            group.append(variable)
            variable_to_candidate[variable] = candidate
            for owner in candidate["owners"]:
                resources[("owner", owner)].append(variable)
            for colour in candidate["new_colours"]:
                resources[("colour", colour)].append(variable)
            variable += 1
        candidate_variables.append(group)

    clauses = []
    next_variable = variable
    for group in candidate_variables:
        clauses.append(group)
        next_variable = at_most_one(group, clauses, next_variable)
    for variables in resources.values():
        next_variable = at_most_one(variables, clauses, next_variable)

    with tempfile.TemporaryDirectory(prefix="t2_s4_sat_") as directory:
        cnf = Path(directory) / "selection.cnf"
        with cnf.open("w", encoding="utf-8") as handle:
            handle.write(f"p cnf {next_variable - 1} {len(clauses)}\n")
            for clause in clauses:
                handle.write(" ".join(map(str, clause)) + " 0\n")
        completed = subprocess.run(
            ["kissat", "--quiet", str(cnf)],
            check=False,
            capture_output=True,
            text=True,
        )
    if completed.returncode == 20:
        print(json.dumps({
            "m": m,
            "path": list(path),
            "candidate_counts": list(map(len, candidate_groups)),
            "arc_consistent_domain_counts": list(map(len, domains)),
            "vertex_disjoint_selection": False,
        }, indent=2, sort_keys=True))
        return
    assert completed.returncode == 10, completed.stdout + completed.stderr
    model = set()
    for line in completed.stdout.splitlines():
        if line.startswith("v "):
            model.update(int(x) for x in line.split()[1:] if int(x) > 0)
    chosen = [
        variable_to_candidate[next(v for v in group if v in model)]
        for group in candidate_variables
    ]
    for candidate in chosen:
        candidate["owners"] = [base.bitword(x, n) for x in candidate["owners"]]
        candidate["new_colours"] = [
            base.bitword(x, n) for x in candidate["new_colours"]
        ]
    print(json.dumps({
        "m": m,
        "path": list(path),
        "candidate_counts": list(map(len, candidate_groups)),
        "selection": chosen,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
