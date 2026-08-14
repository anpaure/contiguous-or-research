#!/usr/bin/env python3
"""Analyze literal head-shore cut capacity for the flat D5 C6 atlas.

Substantive execution belongs on H100.  The frozen pre/post incidence
factors differ at 477 head colours.  Project each factor to its rank-12
head-colour chronology, retain exactly the owner-labelled Johnson edges common to both
phases, and compare the resulting path supply with the ordered port demand
of the certified flat 226-three-cycle word.

This first-stage analyzer deliberately makes no geometric router choices.
It records the exact common-path boundary pairing and the strongest possible
matching capacity when every context cut must use a distinct pair of owner
occurrences.  A later compiler may only weaken this supply by imposing
Johnson-cross-edge or collar constraints.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path


HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import search_t2_cross_suffix_alternating_cycles_20260813 as base  # noqa:E402


def bits(word: str) -> int:
    return int(word[::-1], 2)


def word(value: int, width: int = 22) -> str:
    return f"{value:0{width}b}"[::-1]


def candidate_rows(candidate):
    owners = [bits(value) for value in candidate["owners"]]
    heads = [bits(value) for value in candidate["new_colours"]]
    assert len(owners) == len(heads) == len(set(owners)) == len(set(heads))
    return [
        (owners[index], heads[index - 1], heads[index])
        for index in range(len(owners))
    ]


def toggle(selected, cycles):
    out = set(selected)
    for cycle in cycles:
        for owner, old, new in cycle:
            assert (owner, old) in out
            assert (owner, new) not in out
            out.remove((owner, old))
            out.add((owner, new))
    return out


def head_edges(factor):
    """Return internal rank-11 owner -> unordered head-colour pair."""
    by_owner, _ = base.factor_maps(factor)
    return {
        owner: tuple(sorted(colours))
        for owner, colours in by_owner.items()
        if len(colours) == 2
    }


def component_paths(common_edges, boundary_roles):
    """Traverse all nontrivial common projected-head components."""
    adjacency = defaultdict(list)
    for owner, (left, right) in common_edges.items():
        adjacency[left].append((right, owner))
        adjacency[right].append((left, owner))
    assert all(len(row) <= 2 for row in adjacency.values())

    seen_edges = set()
    paths = []
    starts = sorted(owner for owner, row in adjacency.items() if len(row) == 1)
    for start in starts:
        if all(owner in seen_edges for _, owner in adjacency[start]):
            continue
        heads = [start]
        owners = []
        previous = None
        current = start
        while True:
            choices = [
                (nxt, owner)
                for nxt, owner in adjacency[current]
                if owner not in seen_edges
            ]
            if not choices:
                break
            assert len(choices) == 1
            nxt, owner = choices[0]
            seen_edges.add(owner)
            owners.append(owner)
            heads.append(nxt)
            previous, current = current, nxt
            del previous
        paths.append({
            "heads": heads,
            "edge_owners": owners,
            "left_roles": boundary_roles.get(heads[0], []),
            "right_roles": boundary_roles.get(heads[-1], []),
        })

    # The canonical factor is a path forest, so the common subgraph has no
    # cycles.  Every common q1 edge must have been consumed above.
    assert len(seen_edges) == len(common_edges)
    return paths, adjacency


def maximum_path_matching(edge_count: int) -> int:
    # A path with edge_count edges has edge-matching number ceil(edge_count/2).
    return (edge_count + 1) // 2


def cycle_action(cycle):
    return {
        value: cycle[(index + 1) % len(cycle)]
        for index, value in enumerate(cycle)
    }


def apply_factor_word(value, factors):
    for factor in reversed(factors):
        value = cycle_action(factor).get(value, value)
    return value


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("selection")
    parser.add_argument("flat_certificate")
    args = parser.parse_args()

    selection_bytes = Path(args.selection).read_bytes()
    flat_bytes = Path(args.flat_certificate).read_bytes()
    selection = json.loads(selection_bytes)
    flat = json.loads(flat_bytes)
    assert selection["status"] == "SAT" and flat["status"] == "PASS"
    assert flat["selection_sha256"] == hashlib.sha256(selection_bytes).hexdigest()

    cycles = []
    target = {}
    head_old_at = {}
    head_new_at = {}
    changed_owners = set()
    tokens = set()
    pre_changed = set()
    post_changed = set()
    for item in selection["selection"]:
        rows = candidate_rows(item["candidate"])
        cycles.append(rows)
        heads = [bits(value) for value in item["candidate"]["new_colours"]]
        assert not set(target).intersection(heads)
        target.update(cycle_action(heads))
        for owner, old, new in rows:
            assert owner not in changed_owners
            changed_owners.add(owner)
            tokens.add(old)
            tokens.add(new)
            pre_changed.add((owner, old))
            post_changed.add((owner, new))
            assert old not in head_old_at and new not in head_new_at
            head_old_at[old] = owner
            head_new_at[new] = owner
    assert len(changed_owners) == len(tokens) == 477
    assert len(pre_changed) == len(post_changed) == 477

    pre = set(base.canonical_edges(11))
    base.apply_t2(pre, list(base.dyck_words(5)))
    assert pre_changed <= pre
    post = toggle(pre, cycles)
    assert post_changed <= post

    pre_edges = head_edges(pre)
    post_edges = head_edges(post)
    assert set(pre_edges) == set(post_edges)
    changed_labels = {
        owner for owner in pre_edges if pre_edges[owner] != post_edges[owner]
    }
    assert changed_labels == changed_owners

    common_edges = {
        owner: pre_edges[owner]
        for owner in pre_edges
        if pre_edges[owner] == post_edges[owner]
    }

    # Each changed owner keeps one tail colour and changes its head colour.
    # The common projected-head forest is cut at all 477 such owner edges.
    token_boundary = {token: token for token in tokens}
    tails_by_changed_owner = {}
    boundary_roles = defaultdict(list)
    for token in sorted(tokens):
        boundary_roles[token].append(("head", token))
    pre_by_owner, pre_by_colour = base.factor_maps(pre)
    post_by_owner, post_by_colour = base.factor_maps(post)
    for owner in sorted(changed_owners):
        old_pair = set(pre_by_owner[owner])
        new_pair = set(post_by_owner[owner])
        tail = old_pair & new_pair
        old = old_pair - new_pair
        new = new_pair - old_pair
        assert len(tail) == len(old) == len(new) == 1
        tail_colour = next(iter(tail))
        tails_by_changed_owner[owner] = tail_colour
        boundary_roles[tail_colour].append(("tail", owner))

    paths, common_adjacency = component_paths(common_edges, boundary_roles)

    # Isolated head vertices can occur when both incident owner edges are
    # changed.  Add them as zero-edge components so capacity deficits are not
    # hidden by the edge traversal.
    isolated_boundary = sorted(
        head for head in boundary_roles if head not in common_adjacency
    )
    for head in isolated_boundary:
        paths.append({
            "heads": [head],
            "edge_owners": [],
            "left_roles": boundary_roles[head],
            "right_roles": boundary_roles[head],
        })

    head_to_path = {}
    for index, path in enumerate(paths):
        for head in path["heads"]:
            assert head not in head_to_path
            head_to_path[head] = index

    appearances = Counter(bits(token) for factor in flat["factors"] for token in factor)
    assert set(appearances) == tokens
    assert sum(appearances.values()) == 678
    assert max(appearances.values()) == 3
    flat_factors = [tuple(bits(value) for value in factor) for factor in flat["factors"]]
    assert all(apply_factor_word(token, flat_factors) == target[token] for token in tokens)

    factor_occurrences = defaultdict(list)
    for factor_index, factor in enumerate(flat_factors):
        for port_index, token in enumerate(factor):
            factor_occurrences[token].append([factor_index, port_index])

    token_path = {}
    for token in token_boundary:
        assert token in head_to_path
        token_path[token] = head_to_path[token]

    component_demand = Counter(token_path[token] for token in tokens for _ in range(appearances[token]))
    deficits = []
    endpoint_type_histogram = Counter()
    path_edge_histogram = Counter()
    path_matching_capacity_histogram = Counter()
    token_end_count_histogram = Counter()
    for index, path in enumerate(paths):
        edge_count = len(path["edge_owners"])
        capacity = maximum_path_matching(edge_count)
        demand = component_demand[index]
        endpoint_roles = path["left_roles"] + (
            [] if len(path["heads"]) == 1 else path["right_roles"]
        )
        head_tokens = sorted({value for kind, value in endpoint_roles if kind == "head"})
        tail_count = sum(kind == "tail" for kind, _ in endpoint_roles)
        endpoint_type_histogram[(len(head_tokens), tail_count)] += 1
        path_edge_histogram[edge_count] += 1
        path_matching_capacity_histogram[capacity] += 1
        token_end_count_histogram[len(head_tokens)] += 1
        if demand > capacity:
            deficits.append({
                "path_index": index,
                "edge_count": edge_count,
                "head_owner_count": len(path["heads"]),
                "matching_capacity": capacity,
                "demand": demand,
                "deficit": demand - capacity,
                "head_tokens": [word(token) for token in head_tokens],
                "head_token_demands": [appearances[token] for token in head_tokens],
                "left_roles": [
                    [kind, word(value)] for kind, value in path["left_roles"]
                ],
                "right_roles": [
                    [kind, word(value)] for kind, value in path["right_roles"]
                ],
                "head_owners": [word(head) for head in path["heads"]],
                "common_edge_owners": [word(owner) for owner in path["edge_owners"]],
            })

    # A still weaker single-token capacity check ignores collisions between
    # opposite token ends of the same common component.
    per_token_deficits = []
    for token in sorted(tokens):
        index = token_path[token]
        edge_count = len(paths[index]["edge_owners"])
        capacity = maximum_path_matching(edge_count)
        if appearances[token] > capacity:
            per_token_deficits.append({
                "token": word(token),
                "demand": appearances[token],
                "path_index": index,
                "path_edge_count": edge_count,
                "path_matching_capacity": capacity,
            })

    common_degree_histogram_on_tokens = Counter(
        len(common_adjacency.get(token, [])) for token in tokens
    )
    isolated_tokens = sorted(
        token for token in tokens if not common_adjacency.get(token)
    )
    assert isolated_tokens
    isolated_cause_histogram = Counter()
    for token in isolated_tokens:
        stable_incidence_owners = set(pre_by_colour[token]) & set(post_by_colour[token])
        assert len(stable_incidence_owners) == 1
        stable_owner = next(iter(stable_incidence_owners))
        if stable_owner in changed_owners:
            isolated_cause_histogram["stable_incidence_is_changed_tail_owner"] += 1
        else:
            assert len(pre_by_owner[stable_owner]) == len(post_by_owner[stable_owner]) == 1
            isolated_cause_histogram["stable_incidence_is_degree_one_endpoint"] += 1
    isolated_flat_demands = Counter(appearances[token] for token in isolated_tokens)
    obstruction_token = isolated_tokens[0]

    incident_owner_pairs = []
    for owner in sorted(set(pre_by_owner) | set(post_by_owner)):
        old_pair = tuple(sorted(pre_by_owner.get(owner, ())))
        new_pair = tuple(sorted(post_by_owner.get(owner, ())))
        if obstruction_token not in old_pair and obstruction_token not in new_pair:
            continue
        incident_owner_pairs.append({
            "edge_owner": word(owner),
            "pre_head_pair": [word(value) for value in old_pair],
            "post_head_pair": [word(value) for value in new_pair],
            "phase_common_projected_edge": old_pair == new_pair and len(old_pair) == 2,
        })
    tail_roles = sorted(
        owner for owner, tail in tails_by_changed_owner.items()
        if tail == obstruction_token
    )
    minimum_obstruction = {
        "token": word(obstruction_token),
        "target_image": word(target[obstruction_token]),
        "target_preimage": word(next(
            value for value, image in target.items() if image == obstruction_token
        )),
        "flat_word_demand": appearances[obstruction_token],
        "flat_factor_occurrences_zero_based_factor_port": factor_occurrences[
            obstruction_token
        ],
        "old_head_owner": word(head_old_at[obstruction_token]),
        "new_head_owner": word(head_new_at[obstruction_token]),
        "tail_roles_at_changed_owners": [word(owner) for owner in tail_roles],
        "incident_projected_edges_pre_or_post": incident_owner_pairs,
        "phase_common_projected_head_degree": 0,
        "maximum_distinct_owner_occurrence_cut_sites": 0,
        "unavoidable_minimum_demand_in_any_factorization": 1,
    }

    report = {
        "status": "CAPACITY_PASS" if not deficits else "CAPACITY_OBSTRUCTION",
        "selection_sha256": hashlib.sha256(selection_bytes).hexdigest(),
        "flat_certificate_sha256": hashlib.sha256(flat_bytes).hexdigest(),
        "factor_count": len(flat["factors"]),
        "port_appearances": sum(appearances.values()),
        "maximum_token_appearances": max(appearances.values()),
        "flat_product_verified_on_all_moved_tokens": True,
        "changed_head_tokens": len(tokens),
        "changed_owner_occurrences": len(changed_owners),
        "distinct_tail_head_occurrences": len(set(tails_by_changed_owner.values())),
        "tail_head_multiplicity_histogram": dict(sorted(Counter(
            Counter(tails_by_changed_owner.values()).values()
        ).items())),
        "phase_common_projected_head_edges": len(common_edges),
        "phase_common_degree_histogram_on_moved_head_tokens": dict(sorted(
            common_degree_histogram_on_tokens.items()
        )),
        "isolated_moved_head_tokens": len(isolated_tokens),
        "isolated_moved_head_token_values": [word(token) for token in isolated_tokens],
        "isolated_moved_head_token_cause_histogram": dict(sorted(
            isolated_cause_histogram.items()
        )),
        "isolated_flat_word_port_demand": sum(
            appearances[token] for token in isolated_tokens
        ),
        "isolated_flat_word_demand_histogram": dict(sorted(
            isolated_flat_demands.items()
        )),
        "common_path_components_including_isolates": len(paths),
        "isolated_boundary_owner_components": len(isolated_boundary),
        "common_path_endpoint_type_histogram_heads_tails": {
            f"{heads},{tails}": count
            for (heads, tails), count in sorted(endpoint_type_histogram.items())
        },
        "common_path_edge_count_histogram": {
            str(length): count for length, count in sorted(path_edge_histogram.items())
        },
        "common_path_matching_capacity_histogram": {
            str(capacity): count
            for capacity, count in sorted(path_matching_capacity_histogram.items())
        },
        "token_ends_per_common_path_histogram": {
            str(count): total for count, total in sorted(token_end_count_histogram.items())
        },
        "total_common_path_edge_matching_capacity": sum(
            maximum_path_matching(len(path["edge_owners"])) for path in paths
        ),
        "demand_paths": sum(value > 0 for value in component_demand.values()),
        "deficient_paths": len(deficits),
        "total_path_capacity_deficit": sum(row["deficit"] for row in deficits),
        "per_token_deficits_even_before_path_sharing": len(per_token_deficits),
        "per_token_deficit_witnesses": per_token_deficits,
        "path_deficit_witnesses": deficits,
        "minimum_zero_capacity_obstruction": minimum_obstruction,
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
