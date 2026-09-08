#!/usr/bin/env python3
"""Search one literal cut-open C6 compiler on the first flat D5 factor.

Run on H100 only.  Three actual old-factor edges are cut and cross-spliced
to the three phase-common P2--Q0 edges of one 18-owner router.  The search
requires exact lower/upper q1 refill, the prescribed boundary 3-cycle,
zero affected q2 occurrence current, simple affected decks, and the exact
two-move clock-disjoint collar guard at every one of the six joins.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter, defaultdict
from itertools import permutations, product
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import solve_d5_tapped_c6_212_coinstantiation_20260814 as d5  # noqa:E402
from search_d5_rank7_resident_two_channel_cable_router_compatibility_20260814 import (  # noqa:E402
    port_cycle,
)


GROUND = frozenset(range(23))
RANK = 11


def edge_key(a, b):
    return frozenset((a, b))


def cycle_edges(cycle):
    return {
        edge_key(owner, cycle[(i + 1) % len(cycle)])
        for i, owner in enumerate(cycle)
    }


def router_edges(cycles, switched):
    edges = set().union(*(cycle_edges(cycle) for cycle in cycles))
    if switched:
        for i, cycle in enumerate(cycles):
            edges.remove(edge_key(cycle[0], cycle[1]))
            edges.add(edge_key(cycle[0], cycles[(i - 1) % 3][1]))
    return edges


def neighbors(owner):
    return (
        frozenset((owner - {removed}) | {added})
        for removed in owner for added in GROUND - owner
    )


def q1(edge):
    a, b = tuple(edge)
    return a & b, a | b


def exact_refill(removed, added):
    return all(
        Counter(q1(edge)[shore] for edge in removed)
        == Counter(q1(edge)[shore] for edge in added)
        for shore in (0, 1)
    )


def context_data(selection, certificate, flat, factor_index):
    rows, raw_old, _ = d5.extract_rows(selection, certificate)
    del rows
    _, by_colour = d5.base.factor_maps(raw_old)
    old_tail = {}
    for item in selection["selection"]:
        owners = [d5.base.bits(word) for word in item["candidate"]["owners"]]
        colours = [d5.base.bits(word) for word in item["candidate"]["new_colours"]]
        for i, tail in enumerate(owners):
            old_colour = colours[i - 1]
            assert old_colour not in old_tail
            old_tail[old_colour] = tail

    words = tuple(flat["factors"][factor_index])
    tokens = tuple(d5.base.bits(word) for word in words)
    context_edges = []
    for token in tokens:
        x = old_tail[token]
        other = [owner for owner in by_colour[token] if owner != x]
        assert len(other) == 1
        context_edges.append((frozenset(d5.bits_of(x)), frozenset(d5.bits_of(other[0]))))

    canonical = set(d5.base.canonical_edges(11))
    integer_adjacency, _ = d5.factor_adjacency(d5.lifted_edges(raw_old, canonical))
    adjacency = {
        frozenset(d5.bits_of(owner)): {
            frozenset(d5.bits_of(neighbor)) for neighbor in neighbors
        }
        for owner, neighbors in integer_adjacency.items()
    }
    assert all(y in adjacency[x] for x, y in context_edges)
    return words, tokens, tuple(context_edges), adjacency


def port_records(context_edge):
    x, y = context_edge
    records = []
    for orientation, (left, right) in enumerate(((x, y), (y, x))):
        for p in neighbors(left):
            for q in neighbors(right):
                if len(p ^ q) != 2:
                    continue
                cut_lower = p & q
                p_extra = tuple(p - cut_lower)
                q_extra = tuple(q - cut_lower)
                assert len(p_extra) == len(q_extra) == 1
                records.append({
                    "p": p,
                    "q": q,
                    "cut_lower": cut_lower,
                    "p_extra": p_extra[0],
                    "q_extra": q_extra[0],
                    "orientation": orientation,
                    "left": left,
                    "right": right,
                })
    return records


def central_patterns(records, context_edges):
    answer = []
    diagnostics = Counter()
    distinct_histogram = Counter()
    first_aggregate_exact = None
    for context_permutation in permutations(range(3)):
        per_port = [records[context_permutation[i]] for i in range(3)]
        by_z = []
        for port in per_port:
            grouped = defaultdict(list)
            for record in port:
                grouped[record["q_extra"]].append(record)
            by_z.append(grouped)
        for z in set(by_z[0]) & set(by_z[1]) & set(by_z[2]):
            for triple in product(*(group[z] for group in by_z)):
                cuts = [record["cut_lower"] for record in triple]
                h = cuts[0] & cuts[1] & cuts[2]
                if len(h) != RANK - 2:
                    continue
                extras = [tuple(cut - h) for cut in cuts]
                if any(len(extra) != 1 for extra in extras):
                    continue
                active = tuple(extra[0] for extra in extras)
                if len(set(active)) != 3 or z in active:
                    continue
                if not all(
                    triple[i]["p_extra"] == active[(i + 1) % 3]
                    for i in range(3)
                ):
                    continue
                diagnostics["central_router_patterns"] += 1
                context_cut_edges = {edge_key(*edge) for edge in context_edges}
                cuts = {edge_key(record["p"], record["q"]) for record in triple}
                crosses = {
                    edge_key(record["left"], record["p"])
                    for record in triple
                } | {
                    edge_key(record["right"], record["q"])
                    for record in triple
                }
                if not exact_refill(context_cut_edges | cuts, crosses):
                    continue
                diagnostics["aggregate_q1_exact"] += 1
                removed = context_cut_edges | cuts
                distinct = tuple(len({q1(edge)[shore] for edge in removed}) for shore in (0, 1))
                distinct_histogram[distinct] += 1
                q1_simple = distinct == (6, 6)
                boundary = set().union(*(set(edge) for edge in context_edges))
                endpoints = {
                    owner for record in triple for owner in (record["p"], record["q"])
                }
                endpoint_simple = (
                    len(boundary) == 6 and len(endpoints) == 6 and not (boundary & endpoints)
                )
                if endpoint_simple:
                    diagnostics["endpoint_owner_simple_ignoring_q1"] += 1
                if first_aggregate_exact is None:
                    first_aggregate_exact = {
                        "context_permutation": context_permutation,
                        "z": z,
                        "h": h,
                        "active": active,
                        "records": triple,
                        "removed_edges": tuple(removed),
                        "added_edges": tuple(crosses),
                        "removed_lower": tuple(q1(edge)[0] for edge in removed),
                        "removed_upper": tuple(q1(edge)[1] for edge in removed),
                        "added_lower": tuple(q1(edge)[0] for edge in crosses),
                        "added_upper": tuple(q1(edge)[1] for edge in crosses),
                        "distinct_lower_upper": distinct,
                        "endpoint_owner_simple": endpoint_simple,
                    }
                if not q1_simple:
                    continue
                diagnostics["removed_q1_simple"] += 1
                if not endpoint_simple:
                    continue
                diagnostics["endpoint_owner_simple"] += 1
                answer.append({
                    "context_permutation": context_permutation,
                    "z": z,
                    "h": h,
                    "active": active,
                    "records": triple,
                })
    return answer, diagnostics, distinct_histogram, first_aggregate_exact


def adjacency_from_edges(edges):
    adjacency = defaultdict(set)
    for edge in edges:
        a, b = tuple(edge)
        assert len(a ^ b) == 2
        adjacency[a].add(b)
        adjacency[b].add(a)
    return adjacency


def boundary_matching(edges, boundary):
    adjacency = adjacency_from_edges(edges)
    assert all(len(adjacency[node]) == (1 if node in boundary else 2) for node in adjacency)
    matching = set()
    for start in boundary:
        previous = None
        current = start
        while True:
            choices = adjacency[current] - ({previous} if previous is not None else set())
            assert len(choices) == 1
            nxt = next(iter(choices))
            previous, current = current, nxt
            if current in boundary:
                matching.add(edge_key(start, current))
                break
    assert len(matching) == len(boundary) // 2
    return matching


def context_collar(endpoint, cut_neighbor, adjacency):
    first = next(owner for owner in adjacency[endpoint] if owner != cut_neighbor)
    second = next(owner for owner in adjacency[first] if owner != endpoint)
    return first, second


def affected_q2(edges, centers):
    adjacency = adjacency_from_edges(edges)
    lower, upper = [], []
    for center in centers:
        assert len(adjacency[center]) == 2
        left, right = tuple(adjacency[center])
        lower.append(left & center & right)
        upper.append(left | center | right)
    return tuple(lower), tuple(upper)


def collar_guard(endpoint, cut_neighbor, router_endpoint, router_edges_phase, adjacency, clocks):
    exterior_one, exterior_two = context_collar(endpoint, cut_neighbor, adjacency)
    router_adj = adjacency_from_edges(router_edges_phase)
    inward_one = next(iter(router_adj[router_endpoint]))
    inward_two = next(owner for owner in router_adj[inward_one] if owner != router_endpoint)
    supports = (
        exterior_two ^ exterior_one,
        exterior_one ^ endpoint,
        endpoint ^ router_endpoint,
        router_endpoint ^ inward_one,
        inward_one ^ inward_two,
    )
    assert all(len(support) == 2 for support in supports)
    clock_disjoint = not ((supports[1] | supports[2]) & clocks)
    triple_disjoint = all(
        len(supports[i] | supports[i + 1] | supports[i + 2]) == 6
        for i in range(3)
    )
    return {
        "exterior_one": exterior_one,
        "exterior_two": exterior_two,
        "supports": supports,
        "clock_disjoint": clock_disjoint,
        "triple_disjoint": triple_disjoint,
    }


def encode_set(value):
    return d5.base.bitword(sum(1 << x for x in value), 23)


def encode(value):
    if isinstance(value, frozenset):
        if all(isinstance(item, int) for item in value):
            return encode_set(value)
        return sorted(encode(item) for item in value)
    if isinstance(value, set):
        return sorted(encode(item) for item in value)
    if isinstance(value, tuple) or isinstance(value, list):
        return [encode(item) for item in value]
    if isinstance(value, dict):
        return {str(key): encode(item) for key, item in value.items()}
    return value


def try_clock(pattern, context_edges, adjacency, tokens):
    h = pattern["h"]
    z = pattern["z"]
    active = pattern["active"]
    x_pool = sorted(GROUND - h - {z} - set(active))
    for x1, x2 in permutations(x_pool, 2):
        for y1, y2 in permutations(sorted(h), 2):
            k = (h - {y1, y2}) | {x1, x2}
            cycles = tuple(
                port_cycle(k, x1, x2, y1, y2, z, active[i], active[(i + 1) % 3])
                for i in range(3)
            )
            if any(cycles[i][3] != pattern["records"][i]["p"] for i in range(3)):
                continue
            if any(cycles[i][4] != pattern["records"][i]["q"] for i in range(3)):
                continue
            router_owners = set().union(*map(set, cycles))
            if len(router_owners) != 18:
                continue
            boundary = set().union(*(set(edge) for edge in context_edges))
            collar_owners = set(boundary)
            for x, y in context_edges:
                collar_owners.update(context_collar(x, y, adjacency))
                collar_owners.update(context_collar(y, x, adjacency))
            if router_owners & collar_owners:
                continue

            old_router = router_edges(cycles, False)
            new_router = router_edges(cycles, True)
            cuts = {edge_key(cycle[3], cycle[4]) for cycle in cycles}
            crosses = set()
            for record in pattern["records"]:
                crosses.add(edge_key(record["left"], record["p"]))
                crosses.add(edge_key(record["right"], record["q"]))
            old_network = (old_router - cuts) | crosses
            new_network = (new_router - cuts) | crosses

            old_matching = boundary_matching(old_network, boundary)
            new_matching = boundary_matching(new_network, boundary)
            expected_old = {edge_key(*edge) for edge in context_edges}
            token_to_edge = dict(zip(tokens, context_edges))
            expected_new = {
                edge_key(token_to_edge[tokens[i]][0], token_to_edge[tokens[(i + 1) % 3]][1])
                for i in range(3)
            }
            if old_matching != expected_old or new_matching != expected_new:
                continue

            context_cut_edges = {edge_key(*edge) for edge in context_edges}
            if not exact_refill(context_cut_edges | cuts, crosses):
                continue
            base_edges = old_router | context_cut_edges
            for phase_edges in (old_network, new_network):
                for shore in (0, 1):
                    base_values = [q1(edge)[shore] for edge in base_edges]
                    phase_values = [q1(edge)[shore] for edge in phase_edges]
                    if Counter(base_values) != Counter(phase_values):
                        break
                    if len(phase_values) != len(set(phase_values)):
                        break
                else:
                    continue
                break
            else:
                pass
            if any(
                Counter(q1(edge)[shore] for edge in base_edges)
                != Counter(q1(edge)[shore] for edge in phase_edges)
                or len([q1(edge)[shore] for edge in phase_edges])
                != len({q1(edge)[shore] for edge in phase_edges})
                for phase_edges in (old_network, new_network) for shore in (0, 1)
            ):
                continue

            collar_edges = set()
            collar_first = set()
            for x, y in context_edges:
                for endpoint, cut_neighbor in ((x, y), (y, x)):
                    one, two = context_collar(endpoint, cut_neighbor, adjacency)
                    collar_edges.add(edge_key(endpoint, one))
                    collar_edges.add(edge_key(one, two))
                    collar_first.add(one)
            old_extended = old_network | collar_edges
            new_extended = new_network | collar_edges
            centers = router_owners | boundary | collar_first
            old_q2 = affected_q2(old_extended, centers)
            new_q2 = affected_q2(new_extended, centers)
            if any(Counter(old_q2[s]) != Counter(new_q2[s]) for s in (0, 1)):
                continue
            if any(len(values) != len(set(values)) for values in old_q2 + new_q2):
                continue

            clocks = frozenset((x1, x2, y1, y2))
            collars = []
            valid = True
            for phase_router in (old_router - cuts, new_router - cuts):
                for context_index, record in enumerate(pattern["records"]):
                    original_index = pattern["context_permutation"][context_index]
                    x, y = context_edges[original_index]
                    for endpoint, cut_neighbor, router_endpoint in (
                        (record["left"], record["right"], record["p"]),
                        (record["right"], record["left"], record["q"]),
                    ):
                        audit = collar_guard(
                            endpoint, cut_neighbor, router_endpoint,
                            phase_router, adjacency, clocks,
                        )
                        collars.append(audit)
                        if not audit["clock_disjoint"] or not audit["triple_disjoint"]:
                            valid = False
            if not valid:
                continue

            return {
                "parameters": {
                    "h": h, "z": z, "active": active,
                    "x1": x1, "x2": x2, "y1": y1, "y2": y2, "k": k,
                },
                "context_permutation": pattern["context_permutation"],
                "router_cycles": cycles,
                "context_edges": context_edges,
                "records": pattern["records"],
                "removed_edges": tuple(context_cut_edges | cuts),
                "added_edges": tuple(crosses),
                "old_matching": old_matching,
                "new_matching": new_matching,
                "expected_new_matching": expected_new,
                "old_q2": old_q2,
                "new_q2": new_q2,
                "affected_q2_centers": len(centers),
                "collars": collars,
                "old_network_edges": tuple(old_network),
                "new_network_edges": tuple(new_network),
            }
    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("selection")
    parser.add_argument("certificate")
    parser.add_argument("flat_atlas")
    parser.add_argument("--factor-index", type=int, default=0)
    args = parser.parse_args()
    selection_raw = Path(args.selection).read_bytes()
    certificate_raw = Path(args.certificate).read_bytes()
    flat_raw = Path(args.flat_atlas).read_bytes()
    selection = json.loads(selection_raw)
    certificate = json.loads(certificate_raw)
    flat = json.loads(flat_raw)
    words, tokens, context_edges, adjacency = context_data(
        selection, certificate, flat, args.factor_index
    )
    raw_records = tuple(port_records(edge) for edge in context_edges)
    records = tuple(
        [
            record for record in port
            if len({
                context_edges[index][0], context_edges[index][1],
                record["p"], record["q"],
            }) == 4
        ]
        for index, port in enumerate(raw_records)
    )
    patterns, pattern_diagnostics, distinct_histogram, first_exact = central_patterns(
        records, context_edges
    )
    witness = None
    tested_patterns = 0
    for pattern in patterns:
        tested_patterns += 1
        witness = try_clock(pattern, context_edges, adjacency, tokens)
        if witness is not None:
            break
    result = {
        "status": (
            "PASS" if witness is not None
            else "UNSAT_BARE_ROUTER_AGGREGATE_Q1_REFILL"
            if pattern_diagnostics["central_router_patterns"]
            and not pattern_diagnostics["aggregate_q1_exact"]
            else "UNSAT_BARE_ROUTER_Q1_SIMPLE"
            if pattern_diagnostics["aggregate_q1_exact"]
            and not pattern_diagnostics["removed_q1_simple"]
            else "NO_WITNESS"
        ),
        "scope": (
            "first flat factor; canonical P2--Q0 cut; three ordinary bare splices; "
            "aggregate exact q1 refill required before clocks/collars"
        ),
        "selection_sha256": hashlib.sha256(selection_raw).hexdigest(),
        "certificate_sha256": hashlib.sha256(certificate_raw).hexdigest(),
        "flat_atlas_sha256": hashlib.sha256(flat_raw).hexdigest(),
        "factor_index": args.factor_index,
        "factor_words": words,
        "context_edges": context_edges,
        "per_context_edge_raw_cross_legal_pairs": tuple(map(len, raw_records)),
        "per_context_edge_four_owner_cross_legal_pairs": tuple(map(len, records)),
        "per_context_edge_unoriented_four_owner_cross_legal_pairs": tuple(
            len({
                (
                    edge_key(record["p"], record["q"]),
                    frozenset((
                        edge_key(record["left"], record["p"]),
                        edge_key(record["right"], record["q"]),
                    )),
                )
                for record in port
            })
            for port in records
        ),
        "pattern_diagnostics": dict(pattern_diagnostics),
        "aggregate_exact_distinct_lower_upper_histogram": {
            f"{lower},{upper}": count
            for (lower, upper), count in sorted(distinct_histogram.items())
        },
        "first_aggregate_exact_pattern": first_exact,
        "owner_simple_patterns": len(patterns),
        "tested_patterns": tested_patterns,
        "witness": witness,
    }
    print(json.dumps(encode(result), indent=2, sort_keys=True))
    if witness is None:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
