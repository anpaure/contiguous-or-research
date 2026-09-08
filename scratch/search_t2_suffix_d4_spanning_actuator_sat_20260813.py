#!/usr/bin/env python3
"""Search a q2-safe, vertex-disjoint spanning suffix-tree actuator on D_4.

Substantive execution belongs on H100.  Candidate generation proves each
reported per-edge length minimal by exhausting every shorter directed-path
split.  SAT selects a rooted suffix arborescence with disjoint incidence
resources; rejected models are blocked unless the simultaneous factor toggle
is q2-support-safe and merges every touched lifted component into one.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
from collections import Counter, defaultdict, deque
from itertools import combinations
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import search_t2_cross_suffix_alternating_cycles_20260813 as base  # noqa:E402
from audit_t2_cross_suffix_c16_full_ml_topology_20260813 import (  # noqa:E402
    graph_components,
    lifted_edges,
)
from verify_t2_c16_suffix_component_residence_20260813 import (  # noqa:E402
    seam_collar_report,
    toggle,
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
    m, n = 10, 20
    suffixes = list(base.dyck_words(4))
    suffix_edges = [
        (left, right)
        for left, right in combinations(suffixes, 2)
        if (base.bits(left) ^ base.bits(right)).bit_count() == 2
    ]
    canonical = base.canonical_edges(m)
    post = set(canonical)
    base.apply_t2(post, suffixes)
    by_owner, by_colour = base.factor_maps(post)
    internal = {owner for owner, colours in by_owner.items() if len(colours) == 2}
    base.INTERNAL_OWNERS = internal
    loads = Counter(
        colours[0] | colours[1]
        for colours in by_owner.values() if len(colours) == 2
    )
    base_components, base_which = graph_components(
        lifted_edges(post, canonical, n)
    )

    def reverse_steps(owner):
        for colour in by_owner[owner]:
            remainder = colour
            while remainder:
                bit = remainder & -remainder
                remainder -= bit
                predecessor = colour ^ bit
                if predecessor in internal and (predecessor, colour) not in post:
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

    def exact_paths(start, target, length, distance, stop_after=None):
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
                owner, n, post, by_colour
            ):
                if next_owner in owners or colour in colours:
                    continue
                rec(next_owner, owners + [next_owner], colours + [colour])
                if stop_after is not None and len(answer) >= stop_after:
                    return

        rec(start, [start], [])
        return answer

    candidate_limit = 160
    edge_candidates = []
    edge_minimums = []
    for edge_index, (left, right) in enumerate(suffix_edges):
        candidates = {}
        lower_bound = None
        for prefix in (base.T2[4][0], base.T2[5][0]):
            a = base.bits(prefix) | (base.bits(left) << 12)
            b = base.bits(prefix) | (base.bits(right) << 12)
            distance_b = distances_to(b, 14)
            distance_a = distances_to(a, 14)
            bound = distance_b[a] + distance_a[b]
            lower_bound = bound if lower_bound is None else min(lower_bound, bound)

        minimum = None
        exhausted_shorter_cycles = 0
        for total_length in range(lower_bound, lower_bound + 5):
            found_at_length = {}
            cycles_checked_at_length = 0
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
                            cycles_checked_at_length += 1
                            _, losses, _ = base.q2_current(
                                cycle, by_owner, loads
                            )
                            if losses:
                                continue
                            owners, new_colours = cycle
                            key = (tuple(owners), tuple(new_colours))
                            found_at_length[key] = {
                                "suffix_edge": [left, right],
                                "prefix": prefix,
                                "incidence_length": 2 * total_length,
                                "owners": tuple(owners),
                                "new_colours": tuple(new_colours),
                            }
                            if len(found_at_length) >= candidate_limit:
                                break
                        if len(found_at_length) >= candidate_limit:
                            break
                    if len(found_at_length) >= candidate_limit:
                        break
                if len(found_at_length) >= candidate_limit:
                    break
            if found_at_length:
                minimum = total_length
                candidates = found_at_length
                break
            exhausted_shorter_cycles += cycles_checked_at_length
        assert candidates, (left, right, lower_bound)
        edge_candidates.append(list(candidates.values()))
        edge_minimums.append({
            "suffix_edge": [left, right],
            "directed_distance_lower_bound": 2 * lower_bound,
            "shortest_q2_safe_incidence_length": 2 * minimum,
            "retained_candidates": len(candidates),
            "shorter_label_simple_cycles_checked": exhausted_shorter_cycles,
        })
        print(
            f"c edge {edge_index}/{len(suffix_edges)} {left} {right}: "
            f"C{2 * minimum}, candidates={len(candidates)}",
            file=sys.stderr,
            flush=True,
        )

    # SAT variables are oriented candidate uses.  Each nonroot suffix gets
    # exactly one incoming arc.  One-hot depths force every chosen parent arc
    # to point from smaller to larger depth, hence give a spanning arborescence.
    root = suffixes[0]
    suffix_index = {word: i for i, word in enumerate(suffixes)}
    variable = 1
    orientation = {}
    variable_to_choice = {}
    incoming = defaultdict(list)
    resources = defaultdict(list)
    for edge_index, candidates in enumerate(edge_candidates):
        left, right = suffix_edges[edge_index]
        for candidate_index, candidate in enumerate(candidates):
            directions = []
            if right != root:
                directions.append((left, right))
            if left != root:
                directions.append((right, left))
            for source, target in directions:
                orientation[(edge_index, candidate_index, source, target)] = variable
                variable_to_choice[variable] = (
                    edge_index, candidate_index, source, target
                )
                incoming[target].append(variable)
                for owner in candidate["owners"]:
                    resources[("owner", owner)].append(variable)
                for colour in candidate["new_colours"]:
                    resources[("colour", colour)].append(variable)
                variable += 1

    depth_variables = {}
    for word in suffixes:
        allowed = [0] if word == root else list(range(1, len(suffixes)))
        for depth in allowed:
            depth_variables[(word, depth)] = variable
            variable += 1

    clauses = []
    next_variable = variable
    for word in suffixes:
        if word == root:
            clauses.append([depth_variables[(word, 0)]])
            continue
        clauses.append(incoming[word])
        next_variable = at_most_one(incoming[word], clauses, next_variable)
        depth_group = [
            depth_variables[(word, depth)] for depth in range(1, len(suffixes))
        ]
        clauses.append(depth_group)
        next_variable = at_most_one(depth_group, clauses, next_variable)
    for variables in resources.values():
        next_variable = at_most_one(variables, clauses, next_variable)

    for key, arc_variable in orientation.items():
        _, _, source, target = key
        source_depths = [0] if source == root else range(1, len(suffixes))
        target_depths = range(1, len(suffixes))
        for source_depth in source_depths:
            for target_depth in target_depths:
                if source_depth >= target_depth:
                    clauses.append([
                        -arc_variable,
                        -depth_variables[(source, source_depth)],
                        -depth_variables[(target, target_depth)],
                    ])

    kissat = os.environ.get("KISSAT", "kissat")
    rejected_models = 0
    chosen_payload = None
    while True:
        with tempfile.TemporaryDirectory(prefix="t2_d4_tree_") as directory:
            cnf = Path(directory) / "tree.cnf"
            with cnf.open("w", encoding="utf-8") as handle:
                handle.write(f"p cnf {next_variable - 1} {len(clauses)}\n")
                for clause in clauses:
                    handle.write(" ".join(map(str, clause)) + " 0\n")
            completed = subprocess.run(
                [kissat, "--quiet", str(cnf)],
                check=False,
                capture_output=True,
                text=True,
            )
        assert completed.returncode == 10, completed.stdout + completed.stderr
        model = {
            int(value)
            for line in completed.stdout.splitlines() if line.startswith("v ")
            for value in line.split()[1:] if int(value) > 0
        }
        chosen_variables = sorted(set(model) & set(variable_to_choice))
        assert len(chosen_variables) == len(suffixes) - 1
        choices = [variable_to_choice[x] for x in chosen_variables]
        cycles = []
        for edge_index, candidate_index, _, _ in choices:
            candidate = edge_candidates[edge_index][candidate_index]
            owners = candidate["owners"]
            new_colours = candidate["new_colours"]
            cycles.append([
                (owners[i], new_colours[i - 1], new_colours[i])
                for i in range(len(owners))
            ])

        q2_delta = Counter()
        for cycle in cycles:
            for owner, old, new in cycle:
                other = next(x for x in by_owner[owner] if x != old)
                q2_delta[other | old] -= 1
                q2_delta[other | new] += 1
        q2_losses = [
            target for target, delta in q2_delta.items()
            if loads[target] and loads[target] + delta == 0
        ]

        simultaneous = toggle(post, cycles)
        after_components, after_which = graph_components(
            lifted_edges(simultaneous, canonical, n)
        )
        touched_owners = [
            owner for cycle in cycles for owner, _, _ in cycle
        ]
        touched_outputs = {after_which[owner] for owner in touched_owners}
        suffix_representatives = [
            base.bits(base.T2[4][0]) | (base.bits(word) << 12)
            for word in suffixes
        ]
        suffix_outputs = {after_which[owner] for owner in suffix_representatives}
        if not q2_losses and len(touched_outputs) == 1 and len(suffix_outputs) == 1:
            chosen_payload = (
                choices, cycles, q2_delta, after_components, after_which
            )
            break
        clauses.append([-x for x in chosen_variables])
        rejected_models += 1
        assert rejected_models < 10000

    choices, cycles, q2_delta, after_components, after_which = chosen_payload
    changed_lower = {owner for cycle in cycles for owner, _, _ in cycle}
    added = {(owner, new) for cycle in cycles for owner, _, new in cycle}
    simultaneous_edges = lifted_edges(toggle(post, cycles), canonical, n)
    upper = seam_collar_report(
        simultaneous_edges,
        m + 1,
        lambda label, pair: label in changed_lower,
        n + 1,
    )
    lower = seam_collar_report(
        simultaneous_edges,
        m,
        lambda label, pair: any(
            colour == label and owner in pair for owner, colour in added
        ),
        n + 1,
    )
    upper_bad = [x for x in upper["seams"] if x["collisions"]]
    lower_bad = [x for x in lower["seams"] if x["collisions"]]

    selection = []
    touched_base = set()
    touched_after = set()
    for edge_index, candidate_index, source, target in choices:
        candidate = edge_candidates[edge_index][candidate_index]
        cycle = cycles[len(selection)]
        component_ids = {base_which[owner] for owner, _, _ in cycle}
        touched_base |= component_ids
        touched_after |= {after_which[owner] for owner, _, _ in cycle}
        selection.append({
            "suffix_edge": candidate["suffix_edge"],
            "orientation": [source, target],
            "prefix": candidate["prefix"],
            "incidence_length": candidate["incidence_length"],
            "component_arity": len(component_ids),
            "owners": [base.bitword(x, n) for x in candidate["owners"]],
            "new_colours": [
                base.bitword(x, n) for x in candidate["new_colours"]
            ],
        })

    output_component = next(iter(touched_after))
    print(json.dumps({
        "m": m,
        "suffix_vertices": suffixes,
        "all_suffix_edges": len(suffix_edges),
        "edge_minimums": edge_minimums,
        "selection": selection,
        "rejected_sat_models": rejected_models,
        "simultaneous": {
            "owner_disjoint": True,
            "colour_disjoint": True,
            "q2_support_losses": 0,
            "q2_negative_occurrences": sum(
                -delta for delta in q2_delta.values() if delta < 0
            ),
            "base_components_met": len(touched_base),
            "output_components": len(touched_after),
            "component_reduction": len(base_components) - len(after_components),
            "output_component_owner_length": len(
                after_components[output_component]
            ) // 2,
            "upper_bad_2_collars": len(upper_bad),
            "lower_bad_2_collars": len(lower_bad),
            "minimum_upper_seam_gap": min(upper["seam_gaps"]),
            "minimum_lower_seam_gap": min(lower["seam_gaps"]),
        },
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
