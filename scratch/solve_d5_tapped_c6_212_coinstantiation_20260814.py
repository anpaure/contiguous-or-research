#!/usr/bin/env python3
"""Coinstantiate all 212 tapped marked-C6 D5 reset boxes.

Run on H100 only.  The finite menu consists of literal coordinate
relabelings of the two rank-11 tapped templates.  A candidate is rejected
if an internal owner meets the protected radius-two old/new D5 terminal
halo, or if any q1/q2 resource meets the halo resource banks.  The selected
boxes must be mutually disjoint on the same five typed banks.  Prescribed
T/B/C socket owners are the sole owner exemptions.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import random
import sys
from collections import Counter, defaultdict, deque
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import search_t2_cross_suffix_alternating_cycles_20260813 as base  # noqa:E402


GROUND_SIZE = 23
RANK = 11
BANK_NAMES = ("owner", "lower_q1", "upper_q1", "lower_q2", "upper_q2")


def bits_of(value):
    return {i for i in range(GROUND_SIZE) if value >> i & 1}


def bitset(values):
    answer = 0
    for value in values:
        answer |= 1 << value
    return answer


def encode_set(values):
    values = frozenset(values)
    if not values or isinstance(next(iter(values)), int):
        return bitset(values)
    return values


def port_cycle(K, x1, x2, y1, y2, z, a0, a1):
    def add(values, *labels):
        return frozenset(set(values).union(labels))

    return (
        add(K, z, a0),
        add(K, a0, a1),
        add(set(K) - {x1}, y1, a0, a1),
        add(set(K) - {x1, x2}, y1, y2, a0, a1),
        add(set(K) - {x1, x2}, y1, y2, z, a0),
        add(set(K) - {x2}, y2, z, a0),
    )


def banks(cycles):
    result = [[] for _ in BANK_NAMES]
    for cycle in cycles:
        size = len(cycle)
        assert size == len(set(cycle))
        for i, owner in enumerate(cycle):
            one = cycle[(i + 1) % size]
            two = cycle[(i + 2) % size]
            assert len(owner) == RANK and len(owner ^ one) == 2
            result[0].append(encode_set(owner))
            result[1].append(encode_set(owner & one))
            result[2].append(encode_set(owner | one))
            result[3].append(encode_set(owner & one & two))
            result[4].append(encode_set(owner | one | two))
    return tuple(tuple(values) for values in result)


def template(kind):
    K = frozenset(
        {"h", "x1", "x2", "k0", "k1"}
        | {f"g{i}" for i in range(4)}
    )
    unused = {f"v{i}" for i in range(6)}
    exterior = {"z", "a0", "a1", "a2", "y1", "y2", "f0", "f1"}
    universe = K | exterior | unused
    assert len(K) == 9 and len(universe) == GROUND_SIZE
    router = tuple(
        port_cycle(K, "x1", "x2", "y1", "y2", "z", f"a{i}", f"a{(i + 1) % 3}")
        for i in range(3)
    )
    B = router[0][0]
    U = router[2][0]
    if kind == "adjacent":
        C = router[1][0]
        T = frozenset(K | {"z", "f0"})
        Kp = frozenset((K - {"h"}) | {"z"})
        spectator = port_cycle(Kp, "k0", "k1", "a0", "a1", "f0", "h", "f1")
    elif kind == "distance_two":
        C = router[1][5]
        T = frozenset((K - {"x2"}) | {"z", "a0", "a1"})
        Kp = frozenset((K - {"h", "x2"}) | {"z", "a1"})
        spectator = port_cycle(Kp, "a1", "k0", "f0", "f1", "h", "a0", "a2")
    else:
        raise ValueError(kind)
    assert spectator[0] == T
    cycles = router + (spectator,)
    typed = banks(cycles)
    assert all(len(values) == len(set(values)) == 24 for values in typed)
    return {
        "kind": kind,
        "universe": universe,
        "cycles": cycles,
        "T": T,
        "B": B,
        "C": C,
        "U": U,
        "banks": typed,
    }


TEMPLATES = {name: template(name) for name in ("adjacent", "distance_two")}


def jdist(a, b):
    return (a ^ b).bit_count() // 2


def lifted_edges(current, canonical, n_even=22):
    z = 1 << n_even
    mask = z - 1
    answer = list(current)
    answer.extend((z | (mask ^ colour), z | (mask ^ owner)) for owner, colour in canonical)
    canonical_by_owner, _ = base.factor_maps(canonical)
    endpoints = [owner for owner, colours in canonical_by_owner.items() if len(colours) == 1]
    answer.extend((owner, z | owner) for owner in endpoints)
    return answer


def factor_adjacency(edges):
    by_colour = defaultdict(list)
    for left, right in edges:
        if left.bit_count() == RANK:
            owner, colour = left, right
        else:
            assert right.bit_count() == RANK
            owner, colour = right, left
        by_colour[colour].append(owner)
    adjacency = defaultdict(set)
    edge_resources = []
    for colour, owners in by_colour.items():
        assert len(owners) == 2
        left, right = owners
        adjacency[left].add(right)
        adjacency[right].add(left)
        edge_resources.append((left & right, colour))
    assert all(len(neighbors) == 2 for neighbors in adjacency.values())
    return adjacency, edge_resources


def extract_rows(selection, certificate):
    selected = set(base.canonical_edges(11))
    base.apply_t2(selected, list(base.dyck_words(5)))
    _, by_colour = base.factor_maps(selected)
    state = {
        base.bits(word): value
        for word, value in certificate["owner_union_graph"]["three_state_assignment"]
    }
    raw_rows = []
    for item in selection["selection"]:
        owners = tuple(base.bits(word) for word in item["candidate"]["owners"])
        colours = tuple(base.bits(word) for word in item["candidate"]["new_colours"])
        rows = [
            (owners[i], colours[i - 1], colours[i]) for i in range(len(owners))
        ]
        raw_rows.extend(rows)
    removed_owner = {old: tail for tail, old, _ in raw_rows}
    result = []
    for row_index, (tail, old_colour, new_colour) in enumerate(raw_rows):
        old_head = next(owner for owner in by_colour[old_colour] if owner != tail)
        new_head = next(
            owner for owner in by_colour[new_colour]
            if owner != removed_owner[new_colour]
        )
        if state[old_head] == state[new_head]:
            continue
        distance = jdist(old_head, new_head)
        assert distance in (1, 2)
        kind = "adjacent" if distance == 1 else "distance_two"
        signature = (
            jdist(tail, old_head),
            jdist(tail, new_head),
            distance,
            (tail & old_head & new_head).bit_count(),
            (tail | old_head | new_head).bit_count(),
        )
        expected = (1, 1, 1, 10, 13) if distance == 1 else (1, 1, 2, 9, 13)
        assert signature == expected
        result.append({
            "source_row": row_index,
            "kind": kind,
            "T": tail,
            "B": old_head,
            "C": new_head,
            "signature": signature,
        })
    assert len(result) == 212
    removed = {(tail, old) for tail, old, _ in raw_rows}
    added = {(tail, new) for tail, _, new in raw_rows}
    switched = (selected - removed) | added
    return result, selected, switched


def ball(adjacencies, roots, radius):
    seen = set(roots)
    frontier = set(roots)
    for _ in range(radius):
        frontier = {
            neighbor
            for vertex in frontier
            for adjacency in adjacencies
            for neighbor in adjacency[vertex]
            if neighbor not in seen
        }
        seen.update(frontier)
    return seen


def protected_banks(rows, old_edges, new_edges):
    terminals = {row[key] for row in rows for key in ("T", "B", "C")}
    canonical = set(base.canonical_edges(11))
    old_adj, old_q1 = factor_adjacency(lifted_edges(old_edges, canonical))
    new_adj, new_q1 = factor_adjacency(lifted_edges(new_edges, canonical))
    for row in rows:
        row["collar_guard"] = collar_guard(row, old_adj, new_adj)
    halo = ball((old_adj, new_adj), terminals, 2)

    lower_q1 = set()
    upper_q1 = set()
    for adjacency in (old_adj, new_adj):
        for owner in halo:
            for neighbor in adjacency[owner]:
                lower_q1.add(owner & neighbor)
                upper_q1.add(owner | neighbor)

    lower_q2 = set()
    upper_q2 = set()
    for adjacency in (old_adj, new_adj):
        centers = halo | {
            neighbor for owner in halo for neighbor in adjacency[owner]
        }
        for center in centers:
            left, right = tuple(adjacency[center])
            triple = (left, center, right)
            if any(value in halo for value in triple):
                lower_q2.add(left & center & right)
                upper_q2.add(left | center | right)

    return {
        "terminals": terminals,
        "halo": halo,
        "typed": (halo, lower_q1, upper_q1, lower_q2, upper_q2),
        "counts": {
            "terminals": len(terminals),
            "owner_radius_two_halo": len(halo),
            "lower_q1": len(lower_q1),
            "upper_q1": len(upper_q1),
            "lower_q2": len(lower_q2),
            "upper_q2": len(upper_q2),
            "collar_guard_size_histogram": dict(sorted(Counter(
                row["collar_guard"].bit_count() for row in rows
            ).items())),
        },
    }


def collar_guard(row, old_adj, new_adj):
    guard = 0
    for root in (row["T"], row["B"], row["C"]):
        for adjacency in (old_adj, new_adj):
            for one in adjacency[root]:
                guard |= root ^ one
                two = next(value for value in adjacency[one] if value != root)
                guard |= one ^ two
    return guard


def cells(sets):
    answer = defaultdict(list)
    for coordinate in range(GROUND_SIZE):
        key = tuple(coordinate in value for value in sets)
        answer[key].append(coordinate)
    return answer


def template_cells(tpl):
    answer = defaultdict(list)
    for label in tpl["universe"]:
        key = tuple(label in tpl[name] for name in ("T", "B", "C"))
        answer[key].append(label)
    return answer


def collar_capacity(row):
    tpl = TEMPLATES[row["kind"]]
    source = template_cells(tpl)
    target = cells(tuple(bits_of(row[name]) for name in ("T", "B", "C")))
    requirements = Counter(
        tuple(label in tpl[name] for name in ("T", "B", "C"))
        for label in ("x1", "x2", "y1", "y2")
    )
    deficits = []
    for cell, required in requirements.items():
        available_values = [
            value for value in target[cell]
            if not (row["collar_guard"] >> value & 1)
        ]
        if len(available_values) < required:
            deficits.append({
                "cell": "".join("1" if value else "0" for value in cell),
                "required_clock_roles": required,
                "available_coordinates": available_values,
                "all_cell_coordinates": target[cell],
                "guarded_coordinates": [
                    value for value in target[cell]
                    if row["collar_guard"] >> value & 1
                ],
            })
    return deficits


def map_candidate(row, rng, collar_mode):
    tpl = TEMPLATES[row["kind"]]
    source = template_cells(tpl)
    target = cells(tuple(bits_of(row[name]) for name in ("T", "B", "C")))
    assert {key: len(value) for key, value in source.items()} == {
        key: len(value) for key, value in target.items()
    }
    mapping = {}
    for key, labels in source.items():
        labels = sorted(labels)
        values = list(target[key])
        clock_labels = [
            label for label in labels if label in {"x1", "x2", "y1", "y2"}
        ] if collar_mode == "full" else []
        allowed = [
            value for value in values
            if not (row["collar_guard"] >> value & 1)
        ]
        rng.shuffle(allowed)
        assert len(allowed) >= len(clock_labels)
        chosen_clock_values = allowed[:len(clock_labels)]
        rng.shuffle(clock_labels)
        mapping.update(zip(clock_labels, chosen_clock_values))
        remaining_labels = [label for label in labels if label not in clock_labels]
        remaining_values = [value for value in values if value not in chosen_clock_values]
        rng.shuffle(remaining_values)
        mapping.update(zip(remaining_labels, remaining_values))
    assert len(mapping) == GROUND_SIZE and len(set(mapping.values())) == GROUND_SIZE

    mapped_cycles = tuple(
        tuple(frozenset(mapping[label] for label in owner) for owner in cycle)
        for cycle in tpl["cycles"]
    )
    typed = banks(mapped_cycles)
    mapped_terminals = {
        name: bitset(mapping[label] for label in tpl[name])
        for name in ("T", "B", "C", "U")
    }
    assert mapped_terminals["T"] == row["T"]
    assert mapped_terminals["B"] == row["B"]
    assert mapped_terminals["C"] == row["C"]
    exemptions = (
        {row["T"], row["B"], row["C"]},
        {row["T"] & row["B"], row["T"] & row["C"]},
        {row["T"] | row["B"], row["T"] | row["C"]},
        {row["T"] & row["B"] & row["C"]},
        {row["T"] | row["B"] | row["C"]},
    )
    internal_owners = tuple(value for value in typed[0] if value not in exemptions[0])
    assert len(internal_owners) == 21
    selected_typed = (internal_owners,) + tuple(
        tuple(value for value in typed[k] if value not in exemptions[k])
        for k in range(1, len(BANK_NAMES))
    )
    return {
        "mapping": tuple(mapping[label] for label in sorted(tpl["universe"])),
        "mapping_labels": tuple(sorted(tpl["universe"])),
        "U": mapped_terminals["U"],
        "clock_mask": bitset(mapping[label] for label in ("x1", "x2", "y1", "y2")),
        "typed": selected_typed,
    }


def generate_menus(rows, protected, menu_size, seed, max_attempt_factor, collar_mode):
    menus = []
    diagnostics = []
    protected_typed = protected["typed"]
    for index, row in enumerate(rows):
        rng = random.Random(seed + 1000003 * index)
        menu = []
        seen = set()
        rejections = Counter()
        attempts = 0
        maximum = max(menu_size * max_attempt_factor, menu_size)
        deficits = collar_capacity(row) if collar_mode == "full" else []
        if deficits:
            menus.append(menu)
            diagnostics.append({
                "row": index,
                "source_row": row["source_row"],
                "kind": row["kind"],
                "attempts": 0,
                "accepted": 0,
                "rejections": {"exact_collar_capacity": 1},
                "collar_deficits": deficits,
            })
            continue
        while len(menu) < menu_size and attempts < maximum:
            attempts += 1
            candidate = map_candidate(row, rng, collar_mode)
            key = candidate["mapping"]
            if key in seen:
                rejections["duplicate_mapping"] += 1
                continue
            seen.add(key)
            if collar_mode == "full" and candidate["clock_mask"] & row["collar_guard"]:
                rejections["collar_clock"] += 1
                continue
            bad = None
            for bank_index, values in enumerate(candidate["typed"]):
                if set(values) & protected_typed[bank_index]:
                    bad = BANK_NAMES[bank_index]
                    break
            if bad is not None:
                rejections[f"protected_{bad}"] += 1
                continue
            menu.append(candidate)
        menus.append(menu)
        diagnostics.append({
            "row": index,
            "kind": row["kind"],
            "attempts": attempts,
            "accepted": len(menu),
            "rejections": dict(sorted(rejections.items())),
            "collar_deficits": [],
        })
    return menus, diagnostics


def solve_greedy(menus, seed, passes):
    best = None
    for trial in range(passes):
        rng = random.Random(seed + 7919 * trial)
        order = sorted(range(len(menus)), key=lambda i: (len(menus[i]), rng.random()))
        used = [set() for _ in BANK_NAMES]
        chosen = {}
        for row_index in order:
            options = list(range(len(menus[row_index])))
            rng.shuffle(options)
            winner = None
            winner_score = None
            for option_index in options:
                candidate = menus[row_index][option_index]
                if any(set(values) & used[k] for k, values in enumerate(candidate["typed"])):
                    continue
                score = sum(
                    sum(value in used[k] for value in values)
                    for k, values in enumerate(candidate["typed"])
                )
                if winner is None or score < winner_score:
                    winner, winner_score = option_index, score
                    if score == 0:
                        break
            if winner is None:
                break
            chosen[row_index] = winner
            for k, values in enumerate(menus[row_index][winner]["typed"]):
                used[k].update(values)
        if best is None or len(chosen) > len(best):
            best = chosen
        if len(chosen) == len(menus):
            return chosen, trial + 1
    return best, passes


def conflict_free(rows, menus, chosen, protected):
    assert len(chosen) == len(rows)
    used = [set() for _ in BANK_NAMES]
    for row_index, option_index in sorted(chosen.items()):
        candidate = menus[row_index][option_index]
        for k, values in enumerate(candidate["typed"]):
            assert len(values) == len(set(values))
            assert not (set(values) & protected["typed"][k])
            assert not (set(values) & used[k])
            used[k].update(values)
        assert candidate["U"] not in (rows[row_index]["T"], rows[row_index]["B"], rows[row_index]["C"])
    return tuple(len(values) for values in used)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("selection")
    parser.add_argument("certificate")
    parser.add_argument("--menu-size", type=int, default=128)
    parser.add_argument("--seed", type=int, default=20260814)
    parser.add_argument("--max-attempt-factor", type=int, default=200)
    parser.add_argument("--passes", type=int, default=200)
    parser.add_argument("--collar-mode", choices=("full", "none"), default="full")
    args = parser.parse_args()
    selection = json.loads(Path(args.selection).read_text())
    certificate = json.loads(Path(args.certificate).read_text())
    rows, old_edges, new_edges = extract_rows(selection, certificate)
    protected = protected_banks(rows, old_edges, new_edges)
    menus, diagnostics = generate_menus(
        rows, protected, args.menu_size, args.seed, args.max_attempt_factor,
        args.collar_mode,
    )
    collar_infeasible = [item for item in diagnostics if item["collar_deficits"]]
    if collar_infeasible:
        chosen, trials = {}, 0
        status = "UNSAT_COLLAR"
    else:
        chosen, trials = solve_greedy(menus, args.seed + 17, args.passes)
        status = "SAT" if len(chosen) == len(rows) else "MENU_UNRESOLVED"
    used_counts = None
    if status == "SAT":
        used_counts = conflict_free(rows, menus, chosen, protected)

    result = {
        "status": status,
        "scope": (
            "literal coordinate relabelings of tapped rank-11 C6 boxes; "
            "radius-two old/new D5 socket halo protected; intended T/B/C "
            "owner sockets exempt; exposed graft collars not constructed"
        ),
        "selection_sha256": sha(args.selection),
        "certificate_sha256": sha(args.certificate),
        "seed": args.seed,
        "collar_mode": args.collar_mode,
        "menu_size_requested": args.menu_size,
        "menu_size_histogram": dict(sorted(Counter(map(len, menus)).items())),
        "row_kind_histogram": dict(sorted(Counter(row["kind"] for row in rows).items())),
        "protected": protected["counts"],
        "greedy_trials": trials,
        "rows_assigned": len(chosen),
        "collar_infeasible_rows": len(collar_infeasible),
        "smallest_exact_unsat_core": None if not collar_infeasible else {
            "rows": 1,
            "row": collar_infeasible[0]["row"],
            "source_row": collar_infeasible[0]["source_row"],
            "kind": collar_infeasible[0]["kind"],
            "deficits": collar_infeasible[0]["collar_deficits"],
        },
        "selected_resource_counts": None if used_counts is None else dict(zip(BANK_NAMES, used_counts)),
        "diagnostics": diagnostics,
        "chosen": [] if status != "SAT" else [
            {
                "row": row_index,
                "source_row": rows[row_index]["source_row"],
                "kind": rows[row_index]["kind"],
                "T": base.bitword(rows[row_index]["T"], GROUND_SIZE),
                "B": base.bitword(rows[row_index]["B"], GROUND_SIZE),
                "C": base.bitword(rows[row_index]["C"], GROUND_SIZE),
                "U": base.bitword(menus[row_index][option_index]["U"], GROUND_SIZE),
                "mapping_labels": menus[row_index][option_index]["mapping_labels"],
                "mapping": menus[row_index][option_index]["mapping"],
            }
            for row_index, option_index in sorted(chosen.items())
        ],
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    if status != "SAT":
        raise SystemExit(2)


if __name__ == "__main__":
    main()
