#!/usr/bin/env python3
"""Independent replay of the frozen 36-owner three-splice reset package.

Run on H100 only.  No random search is repeated.
"""

import argparse
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path


def fs_cycle(value):
    return tuple(frozenset(owner) for owner in value)


def edge_set(cycles):
    return {
        frozenset((owner, cycle[(i + 1) % len(cycle)]))
        for cycle in cycles for i, owner in enumerate(cycle)
    }


def cycles_from_edges(edges):
    adjacency = defaultdict(set)
    for edge in edges:
        a, b = tuple(edge)
        assert len(a ^ b) == 2
        adjacency[a].add(b)
        adjacency[b].add(a)
    assert all(len(values) == 2 for values in adjacency.values())
    seen = set()
    result = []
    for start in adjacency:
        if start in seen:
            continue
        cycle = []
        previous = None
        current = start
        while current not in seen:
            seen.add(current)
            cycle.append(current)
            neighbors = list(adjacency[current])
            nxt = neighbors[0] if neighbors[0] != previous else neighbors[1]
            previous, current = current, nxt
        assert current == start
        result.append(tuple(cycle))
    return result


def fused_router(router):
    result = []
    i = 0
    for _ in range(3):
        result.append(router[i][0])
        j = (i - 1) % 3
        result.extend(router[j][1:])
        i = j
    assert i == 0 and len(result) == 18
    return tuple(result)


def palettes(cycles):
    out = [[] for _ in range(5)]
    for cycle in cycles:
        for i, owner in enumerate(cycle):
            one = cycle[(i + 1) % len(cycle)]
            two = cycle[(i + 2) % len(cycle)]
            out[0].append(owner)
            out[1].append(owner & one)
            out[2].append(owner | one)
            out[3].append(owner & one & two)
            out[4].append(owner | one | two)
    return out


def run_minima(cycles, upper):
    answer = [1000, 1000]
    for cycle in cycles:
        trace = [
            cycle[i] | cycle[(i + 1) % len(cycle)]
            for i in range(len(cycle))
        ] if upper else cycle
        for coordinate in range(13):
            word = [int(bool(owner & {coordinate})) for owner in trace]
            if all(value == word[0] for value in word):
                continue
            for i, value in enumerate(word):
                if word[i - 1] == value:
                    continue
                length = 1
                while word[(i + length) % len(word)] == value:
                    length += 1
                answer[value] = min(answer[value], length)
    return answer[1], answer[0]


def first_return(cycles, marked):
    answer = {}
    for cycle in cycles:
        for start in set(cycle) & marked:
            i = cycle.index(start)
            for step in range(1, len(cycle) + 1):
                value = cycle[(i + step) % len(cycle)]
                if value in marked:
                    answer[start] = value
                    break
    return answer


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("witness")
    args = parser.parse_args()
    path = Path(args.witness)
    raw = path.read_bytes()
    data = json.loads(raw)
    assert data["status"] == "SAT"
    w = data["witness"]
    exterior_b = fs_cycle(w["external_b_cycle"])
    exterior_c = fs_cycle(w["external_c_cycle"])
    cable = fs_cycle(w["cable_cycle"])
    router = tuple(fs_cycle(cycle) for cycle in w["router_cycles"])
    old = tuple(fs_cycle(cycle) for cycle in w["old_cycles"])
    new = tuple(fs_cycle(cycle) for cycle in w["new_cycles"])
    additions = {
        frozenset((frozenset(a), frozenset(b))) for a, b in w["additions"]
    }

    base_old = (exterior_b, exterior_c, cable) + router
    base_new = (exterior_b, exterior_c, cable, fused_router(router))
    owners = [owner for cycle in base_old for owner in cycle]
    assert len(owners) == len(set(owners)) == 36
    assert all(len(owner) == 7 and owner <= set(range(13)) for owner in owners)

    base_old_edges = edge_set(base_old)
    old_edges = edge_set(old)
    base_new_edges = edge_set(base_new)
    new_edges = edge_set(new)
    removed_old = base_old_edges - old_edges
    removed_new = base_new_edges - new_edges
    added_old = old_edges - base_old_edges
    added_new = new_edges - base_new_edges
    assert len(removed_old) == len(removed_new) == 6
    assert added_old == added_new == additions
    assert len(additions) == 6
    assert all(len(a ^ b) == 2 for edge in additions for a, b in [tuple(edge)])
    assert {frozenset(cycle) for cycle in cycles_from_edges(old_edges)} == {
        frozenset(cycle) for cycle in old
    }
    assert {frozenset(cycle) for cycle in cycles_from_edges(new_edges)} == {
        frozenset(cycle) for cycle in new
    }

    op, np = palettes(old), palettes(new)
    assert all(len(values) == len(set(values)) == 36 for values in op[:3])
    assert all(Counter(op[k]) == Counter(np[k]) for k in range(5))
    q2_distinct = [len(set(op[k])) for k in (3, 4)]
    old_min = (*run_minima(old, False), *run_minima(old, True))
    new_min = (*run_minima(new, False), *run_minima(new, True))
    assert old_min == new_min == (3, 3, 4, 2)

    if w.get("terminal_heads") is None:
        mark_b, mark_c = exterior_b[0], exterior_c[0]
        tail = None
    else:
        mark_b, mark_c = map(frozenset, w["terminal_heads"])
        tail = frozenset(w["terminal_tail"])
        assert mark_b in exterior_b and mark_c in exterior_c
        assert tail not in set(owners)
        signature = (
            len(tail - mark_b), len(tail - mark_c), len(mark_b - mark_c),
            len(tail & mark_b & mark_c), len(tail | mark_b | mark_c),
        )
        assert list(signature) == w["terminal_signature"]
        assert signature in ((1, 1, 1, 6, 9), (1, 1, 2, 5, 9))
    mark_u = router[2][0]
    old_map = first_return(old, {mark_b, mark_c, mark_u})
    new_map = first_return(new, {mark_b, mark_c, mark_u})
    quotient = first_return(new, {mark_b, mark_c})
    assert old_map == {mark_b: mark_b, mark_c: mark_c, mark_u: mark_u}
    assert len(new_map) == 3 and len(set(new_map.values())) == 3
    assert quotient == {mark_b: mark_c, mark_c: mark_b}

    print(json.dumps({
        "status": "PASS",
        "witness_sha256": hashlib.sha256(raw).hexdigest(),
        "owner_rank": 7,
        "ground": 13,
        "physical_owners": 36,
        "ambient_exterior_owners": 12,
        "added_router_cable_owners": 24,
        "old_component_lengths": sorted(map(len, old)),
        "new_component_lengths": sorted(map(len, new)),
        "removed_edges_each_phase": 6,
        "added_cross_edges_each_phase": 6,
        "q1_simple": True,
        "q2_distinct_values": q2_distinct,
        "lower_upper_q2_occurrence_current_zero": True,
        "old_new_minima": old_min,
        "old_marked_return_identity": True,
        "new_full_marked_return_three_cycle": True,
        "hidden_auxiliary_quotient_transposition": True,
        "terminal_signature": None if tail is None else signature,
        "external_tail_is_distinct_unmodified_owner": tail is not None,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
