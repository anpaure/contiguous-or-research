#!/usr/bin/env python3
"""Select one of three common-neighbour leads for 164 D5 reset rows.

Run on H100 only.  The solver requires pairwise distinct auxiliary owners,
connector lower facets, and connector upper colours.  It reports additional
collisions with the prescribed D5 terminal owner set but does not claim a
full factor embedding.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import search_t2_cross_suffix_alternating_cycles_20260813 as base  # noqa:E402


def jdist(a, b):
    return (a ^ b).bit_count() // 2


def records(selection, certificate):
    m = 11
    selected = set(base.canonical_edges(m))
    base.apply_t2(selected, list(base.dyck_words(5)))
    _, by_colour = base.factor_maps(selected)
    state = {
        base.bits(word): value
        for word, value in certificate["owner_union_graph"][
            "three_state_assignment"
        ]
    }
    result = []
    terminals = set()
    for item in selection["selection"]:
        owners = tuple(base.bits(word) for word in item["candidate"]["owners"])
        colours = tuple(base.bits(word) for word in item["candidate"]["new_colours"])
        rows = [
            (owners[index], colours[index - 1], colours[index])
            for index in range(len(owners))
        ]
        removed_owner = {old: owner for owner, old, _ in rows}
        for tail, old_colour, new_colour in rows:
            old_head = next(o for o in by_colour[old_colour] if o != tail)
            new_head = next(
                o for o in by_colour[new_colour] if o != removed_owner[new_colour]
            )
            terminals.update((tail, old_head, new_head))
            if state[old_head] == state[new_head] or jdist(old_head, new_head) != 2:
                continue
            # Direct four-choice formula from the two-by-two symmetric difference.
            core = old_head & new_head
            left = [1 << i for i in range(23) if old_head >> i & 1 and not new_head >> i & 1]
            right = [1 << i for i in range(23) if new_head >> i & 1 and not old_head >> i & 1]
            assert len(left) == len(right) == 2
            common = [core | x | y for x in left for y in right]
            assert tail in common
            menu = []
            for owner in common:
                if owner == tail:
                    continue
                lower = owner & new_head
                upper = owner | new_head
                menu.append((owner, lower, upper))
            assert len(menu) == 3 and len(set(menu)) == 3
            result.append({
                "tail": tail,
                "old_head": old_head,
                "new_head": new_head,
                "menu": menu,
            })
    assert len(result) == 164
    return result, terminals


def solve(rows):
    assignment = {}
    used = [set(), set(), set()]

    def available(index):
        return [
            option for option in rows[index]["menu"]
            if all(option[k] not in used[k] for k in range(3))
        ]

    def dfs():
        if len(assignment) == len(rows):
            return True
        best_index = None
        best_options = None
        for index in range(len(rows)):
            if index in assignment:
                continue
            options = available(index)
            if not options:
                return False
            if best_options is None or len(options) < len(best_options):
                best_index, best_options = index, options
                if len(options) == 1:
                    break
        for option in best_options:
            assignment[best_index] = option
            for k in range(3):
                used[k].add(option[k])
            if dfs():
                return True
            for k in range(3):
                used[k].remove(option[k])
            del assignment[best_index]
        return False

    assert dfs()
    return [assignment[index] for index in range(len(rows))]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("selection")
    parser.add_argument("certificate")
    args = parser.parse_args()
    selection = json.loads(Path(args.selection).read_text())
    certificate = json.loads(Path(args.certificate).read_text())
    rows, terminals = records(selection, certificate)
    chosen = solve(rows)
    assert all(len({option[k] for option in chosen}) == len(chosen) for k in range(3))
    print(json.dumps({
        "status": "SAT",
        "rows": len(rows),
        "owner_lower_upper_injective": True,
        "chosen_auxiliary_owners_in_terminal_set": sum(
            option[0] in terminals for option in chosen
        ),
        "all_option_owner_terminal_collision_histogram": dict(sorted(Counter(
            sum(option[0] in terminals for option in row["menu"])
            for row in rows
        ).items())),
        "chosen": [
            {
                "row": index,
                "owner": base.bitword(option[0], 23),
                "lower": base.bitword(option[1], 23),
                "upper": base.bitword(option[2], 23),
            }
            for index, option in enumerate(chosen)
        ],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
