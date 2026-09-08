#!/usr/bin/env python3
"""Complete the first flat strand-seam q1 witness through q2 collars.

Run on H100 only.  The three non-current-router cuts are completed to
resident C6 identity rails.  The program checks the complete local q1 bank,
the affected old/new q2 occurrence decks, the explicit crossing-q2 delta,
and the three-support residence condition at all nine seam joins.
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


def decode(word):
    return frozenset(i for i, c in enumerate(word) if c == "1")


def decode_edge(value):
    return frozenset(decode(word) for word in value)


def edge(a, b):
    return frozenset((a, b))


def cycle_edges(cycle):
    return {edge(owner, cycle[(i + 1) % len(cycle)]) for i, owner in enumerate(cycle)}


def router_edges(cycles, switched):
    result = set().union(*(cycle_edges(cycle) for cycle in cycles))
    if switched:
        for i, cycle in enumerate(cycles):
            result.remove(edge(cycle[0], cycle[1]))
            result.add(edge(cycle[0], cycles[(i - 1) % 3][1]))
    return result


def adjacency(edges):
    result = defaultdict(set)
    for e in edges:
        a, b = tuple(e)
        assert len(a ^ b) == 2
        result[a].add(b)
        result[b].add(a)
    return result


def q1(e):
    a, b = tuple(e)
    return a & b, a | b


def q1_decks(edges):
    return tuple(tuple(q1(e)[shore] for e in edges) for shore in (0, 1))


def exact(left, right):
    return all(Counter(left[s]) == Counter(right[s]) for s in range(len(left)))


def affected_q2(edges, centers):
    adj = adjacency(edges)
    lower, upper = [], []
    for center in centers:
        assert len(adj[center]) == 2
        left, right = tuple(adj[center])
        lower.append(left & center & right)
        upper.append(left | center | right)
    return tuple(lower), tuple(upper)


def counter_delta(after, before):
    delta = Counter(after)
    delta.subtract(before)
    return {value: coefficient for value, coefficient in delta.items() if coefficient}


def support_collar_ok(edges, seam_edge):
    adj = adjacency(edges)
    left, right = tuple(seam_edge)
    left1 = next(owner for owner in adj[left] if owner != right)
    left2 = next(owner for owner in adj[left1] if owner != left)
    right1 = next(owner for owner in adj[right] if owner != left)
    right2 = next(owner for owner in adj[right1] if owner != right)
    supports = (
        left2 ^ left1, left1 ^ left, left ^ right,
        right ^ right1, right1 ^ right2,
    )
    return supports, all(
        len(supports[i] | supports[i + 1] | supports[i + 2]) == 6
        for i in range(3)
    )


def context_collars(selection, certificate, context_edges):
    _, raw_old, _ = d5.extract_rows(selection, certificate)
    canonical = set(d5.base.canonical_edges(11))
    integer_adj, _ = d5.factor_adjacency(d5.lifted_edges(raw_old, canonical))

    def integer(owner):
        return sum(1 << x for x in owner)

    collar_edges = set()
    first = set()
    second = set()
    for cut in context_edges:
        x, y = tuple(cut)
        for endpoint, other in ((x, y), (y, x)):
            endpoint_i, other_i = integer(endpoint), integer(other)
            one_i = next(value for value in integer_adj[endpoint_i] if value != other_i)
            two_i = next(value for value in integer_adj[one_i] if value != endpoint_i)
            one = frozenset(d5.bits_of(one_i))
            two = frozenset(d5.bits_of(two_i))
            collar_edges.add(edge(endpoint, one))
            collar_edges.add(edge(one, two))
            first.add(one)
            second.add(two)
    return collar_edges, first, second


def rail_candidates(cut, forbidden, seam_edges, fixed_old, fixed_new, limit, counters):
    p0, q0 = tuple(cut)
    answer = []
    for p, q in ((p0, q0), (q0, p0)):
        lower = p & q
        a_next = next(iter(p - lower))
        z = next(iter(q - lower))
        for active in sorted(lower):
            h = lower - {active}
            x_pool = sorted(GROUND - h - {active, a_next, z})
            for x1, x2 in permutations(x_pool, 2):
                for y1, y2 in permutations(sorted(h), 2):
                    counters["rail_parameter_trials"] += 1
                    k = (h - {y1, y2}) | {x1, x2}
                    cycle = port_cycle(k, x1, x2, y1, y2, z, active, a_next)
                    if cycle[3] != p or cycle[4] != q:
                        continue
                    owners = set(cycle)
                    if len(owners) != 6 or owners & forbidden != {p, q}:
                        continue
                    decks = q1_decks(cycle_edges(cycle))
                    if any(len(values) != len(set(values)) for values in decks):
                        continue
                    rail_without_cut = cycle_edges(cycle) - {cut}
                    valid = True
                    for phase_fixed in (fixed_old, fixed_new):
                        phase_edges = phase_fixed | rail_without_cut
                        for join in seam_edges:
                            if p in join or q in join:
                                _, ok = support_collar_ok(phase_edges, join)
                                if not ok:
                                    valid = False
                                    break
                        if not valid:
                            break
                    if not valid:
                        continue
                    counters["rail_collar_candidates"] += 1
                    answer.append({
                        "cycle": cycle, "cut": cut,
                        "parameters": (h, active, a_next, z, x1, x2, y1, y2, k),
                    })
                    if len(answer) >= limit:
                        return answer
    return answer


def direct_rail_candidates(cut, forbidden, seam_edges, fixed_old, fixed_new, limit, counters):
    """Complete cut as the direct A--B edge of an unchanged resident C6."""
    a0_raw, b0_raw = tuple(cut)
    answer = []
    for a_owner, b_owner in ((a0_raw, b0_raw), (b0_raw, a0_raw)):
        lower = a_owner & b_owner
        z = next(iter(a_owner - lower))
        a1 = next(iter(b_owner - lower))
        for active in sorted(lower):
            k = lower - {active}
            for x1, x2 in permutations(sorted(k), 2):
                exterior = sorted(GROUND - k - {z, active, a1})
                for y1, y2 in permutations(exterior, 2):
                    counters["direct_rail_parameter_trials"] += 1
                    cycle = port_cycle(k, x1, x2, y1, y2, z, active, a1)
                    if cycle[0] != a_owner or cycle[1] != b_owner:
                        continue
                    owners = set(cycle)
                    if len(owners) != 6 or owners & forbidden != {a_owner, b_owner}:
                        continue
                    decks = q1_decks(cycle_edges(cycle))
                    if any(len(values) != len(set(values)) for values in decks):
                        continue
                    rail_without_cut = cycle_edges(cycle) - {cut}
                    valid = True
                    for phase_fixed in (fixed_old, fixed_new):
                        phase_edges = phase_fixed | rail_without_cut
                        for join in seam_edges:
                            if a_owner in join or b_owner in join:
                                _, ok = support_collar_ok(phase_edges, join)
                                if not ok:
                                    valid = False
                                    break
                        if not valid:
                            break
                    if not valid:
                        continue
                    counters["direct_rail_collar_candidates"] += 1
                    answer.append({
                        "cycle": cycle, "cut": cut, "phase": "direct_A_B",
                        "parameters": (k, active, a1, z, x1, x2, y1, y2),
                    })
                    if len(answer) >= limit:
                        return answer
    return answer


def encode_set(value):
    return d5.base.bitword(sum(1 << x for x in value), 23)


def encode(value):
    if isinstance(value, frozenset):
        if all(isinstance(x, int) for x in value):
            return encode_set(value)
        return sorted(encode(x) for x in value)
    if isinstance(value, (tuple, list, set)):
        return [encode(x) for x in value]
    if isinstance(value, dict):
        return {str(k): encode(v) for k, v in value.items()}
    return value


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("selection")
    parser.add_argument("certificate")
    parser.add_argument("q1_witness")
    parser.add_argument("--rail-menu", type=int, default=64)
    parser.add_argument("--witness-index", type=int, default=0)
    args = parser.parse_args()
    selection_raw = Path(args.selection).read_bytes()
    certificate_raw = Path(args.certificate).read_bytes()
    q1_raw = Path(args.q1_witness).read_bytes()
    selection = json.loads(selection_raw)
    certificate = json.loads(certificate_raw)
    report = json.loads(q1_raw)
    assert report["status"] == "PASS"
    witness = report.get("witnesses", [report["witness"]])[args.witness_index]
    router = tuple(tuple(decode(owner) for owner in cycle) for cycle in witness["router_cycles"])
    roles = witness["roles"]
    context_edges = {decode_edge(role["collar"]["old"][0]) for role in roles}
    auxiliary_cuts = tuple(decode_edge(role["auxiliary_edge"]) for role in roles)
    router_cuts = {decode_edge(role["router_edge"]) for role in roles}
    seam_edges = {decode_edge(e) for role in roles for e in role["collar"]["new"]}
    old_router = router_edges(router, False)
    new_router = router_edges(router, True)
    collar_edges, context_first, context_second = context_collars(
        selection, certificate, context_edges
    )

    fixed_owner_forbidden = set().union(*map(set, router))
    fixed_owner_forbidden |= set().union(*(set(e) for e in context_edges | seam_edges))
    fixed_owner_forbidden |= context_first | context_second
    fixed_old = (old_router - router_cuts) | seam_edges | collar_edges
    fixed_new = (new_router - router_cuts) | seam_edges | collar_edges
    counters = Counter()
    menus = []
    for cut in auxiliary_cuts:
        menu = rail_candidates(
            cut, fixed_owner_forbidden | set().union(*(set(other) for other in auxiliary_cuts)),
            seam_edges, fixed_old, fixed_new, args.rail_menu, counters,
        )
        if len(menu) < args.rail_menu:
            menu.extend(direct_rail_candidates(
                cut,
                fixed_owner_forbidden | set().union(*(set(other) for other in auxiliary_cuts)),
                seam_edges, fixed_old, fixed_new, args.rail_menu - len(menu), counters,
            ))
        menus.append(menu)

    solution = None
    for choices in product(*menus):
        counters["rail_menu_products"] += 1
        rail_owners = [owner for choice in choices for owner in choice["cycle"]]
        intended = set().union(*(set(cut) for cut in auxiliary_cuts))
        if len(set(rail_owners)) != 18 or set(rail_owners) & fixed_owner_forbidden != intended:
            continue
        rail_edges = set().union(*(cycle_edges(choice["cycle"]) for choice in choices))
        before_old = old_router | rail_edges | context_edges
        before_new = new_router | rail_edges | context_edges
        after_old = (old_router - router_cuts) | (rail_edges - set(auxiliary_cuts)) | seam_edges
        after_new = (new_router - router_cuts) | (rail_edges - set(auxiliary_cuts)) | seam_edges
        before_q1_old, before_q1_new = q1_decks(before_old), q1_decks(before_new)
        after_q1_old, after_q1_new = q1_decks(after_old), q1_decks(after_new)
        if not exact(before_q1_old, after_q1_old) or not exact(before_q1_new, after_q1_new):
            continue
        if any(len(values) != len(set(values)) for values in before_q1_old + after_q1_old):
            continue
        counters["full_q1_simple"] += 1

        extended_before_old = before_old | collar_edges
        extended_before_new = before_new | collar_edges
        extended_after_old = after_old | collar_edges
        extended_after_new = after_new | collar_edges
        centers = set().union(*map(set, router)) | set(rail_owners)
        centers |= set().union(*(set(e) for e in context_edges)) | context_first
        q2_before_old = affected_q2(extended_before_old, centers)
        q2_before_new = affected_q2(extended_before_new, centers)
        q2_after_old = affected_q2(extended_after_old, centers)
        q2_after_new = affected_q2(extended_after_new, centers)
        if not exact(q2_before_old, q2_before_new):
            continue
        if not exact(q2_after_old, q2_after_new):
            continue
        if any(len(values) != len(set(values)) for values in q2_after_old + q2_after_new):
            continue
        counters["affected_q2_simple_zero_current"] += 1

        collar_audits = []
        valid = True
        for phase_edges in (extended_after_old, extended_after_new):
            for join in seam_edges:
                supports, ok = support_collar_ok(phase_edges, join)
                collar_audits.append({"join": join, "supports": supports, "pass": ok})
                if not ok:
                    valid = False
        if not valid:
            continue
        counters["all_nine_collars"] += 1
        solution = {
            "rails": choices,
            "before_q1": before_q1_old,
            "after_q1": after_q1_old,
            "q2_before_old": q2_before_old,
            "q2_after_old": q2_after_old,
            "q2_after_new": q2_after_new,
            "crossing_q2_delta_lower": counter_delta(q2_after_old[0], q2_before_old[0]),
            "crossing_q2_delta_upper": counter_delta(q2_after_old[1], q2_before_old[1]),
            "collar_audits": collar_audits,
            "affected_centers": len(centers),
        }
        break

    output = {
        "status": "PASS" if solution else "NO_WITNESS",
        "selection_sha256": hashlib.sha256(selection_raw).hexdigest(),
        "certificate_sha256": hashlib.sha256(certificate_raw).hexdigest(),
        "q1_witness_sha256": hashlib.sha256(q1_raw).hexdigest(),
        "witness_index": args.witness_index,
        "rail_menu_sizes": tuple(map(len, menus)),
        "counters": dict(counters),
        "solution": solution,
    }
    print(json.dumps(encode(output), indent=2, sort_keys=True))
    if solution is None:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
