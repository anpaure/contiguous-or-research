#!/usr/bin/env python3
"""Independent hostile audit of the frozen D5 three-splice package.

Run only on H100.  This script is standalone: it does not import the search,
verifier, or palette-dump implementations.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path


def cycle(raw):
    return tuple(frozenset(owner) for owner in raw)


def undirected_edge(left, right):
    assert left != right
    return frozenset((left, right))


def edges(cycles):
    return {
        undirected_edge(owner, item[(index + 1) % len(item)])
        for item in cycles
        for index, owner in enumerate(item)
    }


def components(edge_bank):
    adjacency = defaultdict(set)
    for item in edge_bank:
        left, right = tuple(item)
        assert len(left) == len(right) == 7
        assert len(left ^ right) == 2
        adjacency[left].add(right)
        adjacency[right].add(left)
    assert all(len(neighbors) == 2 for neighbors in adjacency.values())
    unseen = set(adjacency)
    result = []
    while unseen:
        start = next(iter(unseen))
        previous = None
        current = start
        found = []
        while current not in found:
            found.append(current)
            unseen.discard(current)
            candidates = adjacency[current]
            nxt = next(value for value in candidates if value != previous)
            previous, current = current, nxt
        assert current == start and len(found) >= 3
        result.append(tuple(found))
    return result


def fused_router(router):
    answer = []
    index = 0
    for _ in range(3):
        answer.append(router[index][0])
        source = (index - 1) % 3
        answer.extend(router[source][1:])
        index = source
    assert index == 0 and len(answer) == 18
    return tuple(answer)


def decks(cycles):
    result = [[] for _ in range(5)]
    for item in cycles:
        for index, owner in enumerate(item):
            one = item[(index + 1) % len(item)]
            two = item[(index + 2) % len(item)]
            result[0].append(owner)
            result[1].append(owner & one)
            result[2].append(owner | one)
            result[3].append(owner & one & two)
            result[4].append(owner | one | two)
    return result


def run_minima(cycles, use_upper=False):
    minima = [1000, 1000]
    for item in cycles:
        trace = tuple(
            item[index] | item[(index + 1) % len(item)]
            for index in range(len(item))
        ) if use_upper else item
        for coordinate in range(13):
            word = tuple(int(coordinate in owner) for owner in trace)
            if len(set(word)) == 1:
                continue
            for start, value in enumerate(word):
                if word[start - 1] == value:
                    continue
                length = 1
                while word[(start + length) % len(word)] == value:
                    length += 1
                minima[value] = min(minima[value], length)
    return minima[1], minima[0]


def first_return(cycles, marks):
    answer = {}
    for item in cycles:
        for mark in marks & set(item):
            start = item.index(mark)
            for step in range(1, len(item) + 1):
                nxt = item[(start + step) % len(item)]
                if nxt in marks:
                    answer[mark] = nxt
                    break
    return answer


def terminal_signature(tail, mark_b, mark_c):
    return (
        len(tail - mark_b),
        len(tail - mark_c),
        len(mark_b - mark_c),
        len(tail & mark_b & mark_c),
        len(tail | mark_b | mark_c),
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("witness")
    args = parser.parse_args()
    raw = json.loads(Path(args.witness).read_text())
    assert raw["status"] == "SAT"
    witness = raw["witness"]

    exterior_b = cycle(witness["external_b_cycle"])
    exterior_c = cycle(witness["external_c_cycle"])
    cable = cycle(witness["cable_cycle"])
    router = tuple(cycle(item) for item in witness["router_cycles"])
    base_old = (exterior_b, exterior_c, cable) + router
    base_new = (exterior_b, exterior_c, cable, fused_router(router))
    old = tuple(cycle(item) for item in witness["old_cycles"])
    new = tuple(cycle(item) for item in witness["new_cycles"])

    owner_occurrences = [owner for item in base_old for owner in item]
    assert all(len(item) == 6 for item in base_old)
    assert len(owner_occurrences) == len(set(owner_occurrences)) == 36
    assert all(len(owner) == 7 and owner <= set(range(13)) for owner in owner_occurrences)

    old_base_edges, new_base_edges = edges(base_old), edges(base_new)
    old_edges, new_edges = edges(old), edges(new)
    removed_old = old_base_edges - old_edges
    removed_new = new_base_edges - new_edges
    added_old = old_edges - old_base_edges
    added_new = new_edges - new_base_edges
    declared_additions = {
        undirected_edge(frozenset(left), frozenset(right))
        for left, right in witness["additions"]
    }
    assert len(removed_old) == len(removed_new) == 6
    assert added_old == added_new == declared_additions
    assert len(declared_additions) == 6
    assert all(len(tuple(item)[0] ^ tuple(item)[1]) == 2 for item in declared_additions)
    assert sorted(map(len, components(old_edges))) == [6, 12, 18]
    assert sorted(map(len, components(new_edges))) == [36]

    old_decks, new_decks = decks(old), decks(new)
    names = ("owner", "lower_q1", "upper_q1", "lower_q2", "upper_q2")
    distinct = {}
    for index, name in enumerate(names):
        assert Counter(old_decks[index]) == Counter(new_decks[index])
        assert len(old_decks[index]) == len(set(old_decks[index])) == 36
        assert len(new_decks[index]) == len(set(new_decks[index])) == 36
        distinct[name] = 36

    old_minima = (*run_minima(old), *run_minima(old, True))
    new_minima = (*run_minima(new), *run_minima(new, True))
    assert old_minima == new_minima == (3, 3, 4, 2)

    # The six ingredients are themselves resident C6 traces.  This is
    # stronger than the global post-splice minimum check.
    ingredient_minima = [
        (*run_minima((item,)), *run_minima((item,), True))
        for item in base_old
    ]
    assert all(value[0] >= 3 and value[1] >= 3
               and value[2] >= 4 and value[3] >= 2
               for value in ingredient_minima)

    mark_b, mark_c = map(frozenset, witness["terminal_heads"])
    tail = frozenset(witness["terminal_tail"])
    mark_u = router[2][0]
    marks = {mark_b, mark_u, mark_c}
    assert first_return(old, marks) == {
        mark_b: mark_b, mark_u: mark_u, mark_c: mark_c,
    }
    assert first_return(new, marks) == {
        mark_b: mark_u, mark_u: mark_c, mark_c: mark_b,
    }
    assert first_return(new, {mark_b, mark_c}) == {
        mark_b: mark_c, mark_c: mark_b,
    }

    assert tail not in set(owner_occurrences)
    signature = terminal_signature(tail, mark_b, mark_c)
    assert signature == tuple(witness["terminal_signature"])
    assert signature in ((1, 1, 1, 6, 9), (1, 1, 2, 5, 9))
    lifted = signature[:3] + (signature[3] + 4, signature[4] + 4)
    assert lifted in ((1, 1, 1, 10, 13), (1, 1, 2, 9, 13))

    print(json.dumps({
        "status": "PASS",
        "variant": "adjacent" if signature[2] == 1 else "hard",
        "owners_distinct": len(set(owner_occurrences)),
        "ambient_exterior_owners": len(exterior_b) + len(exterior_c),
        "added_cable_router_owners": len(cable) + sum(map(len, router)),
        "old_component_lengths": [6, 12, 18],
        "new_component_lengths": [36],
        "typed_deck_distinct_counts": distinct,
        "typed_decks_equal": True,
        "old_new_run_minima": old_minima,
        "ingredient_run_minima": ingredient_minima,
        "marked_action": "(B U C)",
        "suppressed_action": "(B C)",
        "terminal_signature": signature,
        "lifted_signature": lifted,
        "tail_distinct_from_bank": True,
        "cut_open_context_substitution_verified": False,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
