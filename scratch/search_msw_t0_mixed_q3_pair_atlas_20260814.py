#!/usr/bin/env python3
"""Exhaust small paired native-cycle menus around the frozen mixed packet.

Substantive execution belongs on H100.  Unlike the earlier raw-creator
searches, this enumerates every owner-disjoint pair in the requested menu,
so a W3 provider jointly assembled from two individually noncreating cycles
is included.  Expensive typed/topology/seam diagnostics are run only after
the complete q3 deck shows that the pair preserves all old q3 support.
"""

from __future__ import annotations

import argparse
import json
import multiprocessing as mp
from collections import Counter, defaultdict, deque

import audit_msw_t0v_tensor_residence_20260814 as base
import audit_msw_t0v_tensor_typed_currents_20260814 as typed
import audit_msw_t0v_mixed_c8_c6_tensor_20260814 as mixed_tensor
import audit_msw_t0v_mixed_q3_closed_tensor_20260814 as q3closed
import audit_msw_t0v_mixed_q3_loss_providers_20260814 as q3trace
import search_msw_t0_twohex_typed_safe_20260814 as search
import search_msw_t0_mixed_q3_c8_backup_20260814 as c8search
import search_msw_t0_mixed_q3_long_cycle_backup_20260814 as longsearch


W3 = base.bits("110111001111")
_STATE = {}


def difference(old, new):
    result = Counter(new)
    result.subtract(old)
    return Counter({value: amount for value, amount in result.items() if amount})


def q3_deck(selected):
    try:
        return q3closed.q3_deck(selected)
    except AssertionError:
        return None


def catalogue(kind, canonical):
    if kind == "c6":
        return [
            {
                "support": frozenset(row["incidences"]),
                "owners": frozenset(row["owners"]),
                "colours": frozenset(row["colours"]),
                "name": {
                    "index": index,
                    "core": base.bitword(row["core"], 12),
                    "active_one_based": [bit + 1 for bit in row["active"]],
                },
            }
            for index, row in enumerate(search.enumerate_hexes(canonical))
        ]
    if kind == "c8":
        rows = []
        for index, (support, cycle) in enumerate(
            sorted(c8search.alternating_c8s(canonical).items(), key=lambda item: tuple(sorted(item[0])))
        ):
            rows.append({
                "support": support,
                "owners": frozenset(cycle["owners"]),
                "colours": frozenset(cycle["colours"]),
                "name": {
                    "index": index,
                    "owners": [base.bitword(value, 12) for value in cycle["owners"]],
                    "colours": [base.bitword(value, 12) for value in cycle["colours"]],
                },
            })
        return rows
    if kind in ("c10", "c12"):
        k = {"c10": 5, "c12": 6}[kind]
        by_colour, outgoing = longsearch.owner_arc_graph(canonical)
        starts = sorted(longsearch.target_arcs(by_colour))
        seen = set()
        rows = []
        for start, second, first_colour in starts:
            owners = [start, second]
            colours = [first_colour]

            def dfs():
                current = owners[-1]
                if len(colours) == k - 1:
                    for next_owner, colour in outgoing[current]:
                        if next_owner != start or colour in colours:
                            continue
                        all_colours = tuple(colours + [colour])
                        all_owners = tuple(owners)
                        support = longsearch.cycle_support(all_owners, all_colours)
                        if support in seen:
                            continue
                        seen.add(support)
                        rows.append({
                            "support": support,
                            "owners": frozenset(all_owners),
                            "colours": frozenset(all_colours),
                            "name": {
                                "index": len(rows),
                                "owners": [base.bitword(value, 12) for value in all_owners],
                                "colours": [base.bitword(value, 12) for value in all_colours],
                            },
                        })
                    return
                for next_owner, colour in outgoing[current]:
                    if next_owner == start or next_owner in owners or colour in colours:
                        continue
                    owners.append(next_owner)
                    colours.append(colour)
                    dfs()
                    colours.pop()
                    owners.pop()

            dfs()
        return rows
    raise ValueError(kind)


def all_decks(selected):
    result = typed.typed_decks(selected)
    result["upper_q3"] = q3_deck(selected)
    return result


def support_safe(old, new):
    return all(new[value] > 0 for value in old)


def apply_prefix_packet(canonical, supports, m):
    selected = set(canonical)
    used_owners = set()
    for suffix_word in base.dyck_words(m - 6):
        suffix = base.bits(suffix_word) << 12
        for support in supports:
            incidences = {
                (owner | suffix, colour | suffix)
                for owner, colour in support
            }
            owners = {owner for owner, _ in incidences}
            assert not used_owners & owners
            used_owners |= owners
            selected.symmetric_difference_update(incidences)
    return selected


def current_by_suffix_weight(old, new, m):
    delta = difference(old, new)
    counts = Counter()
    mask = (1 << 12) - 1
    for value, amount in delta.items():
        suffix_weight = (value & ~mask).bit_count()
        counts[(suffix_weight, 1 if amount > 0 else -1)] += abs(amount)
    return counts


def common_binary_phase(old_selected, new_selected):
    adjacency = defaultdict(set)
    for selected in (old_selected, new_selected):
        by_colour = defaultdict(list)
        for owner, colour in selected:
            by_colour[colour].append(owner)
        for owners in by_colour.values():
            assert len(owners) == 2
            left, right = owners
            adjacency[left].add(right)
            adjacency[right].add(left)
    phase = {}
    for root in sorted(adjacency):
        if root in phase:
            continue
        phase[root] = 0
        queue = deque([root])
        while queue:
            left = queue.popleft()
            for right in adjacency[left]:
                wanted = 1 - phase[left]
                if right in phase:
                    if phase[right] != wanted:
                        return False
                else:
                    phase[right] = wanted
                    queue.append(right)
    return True


def component_data(canonical, selected, m):
    lifted = base.lifted_edges(selected, canonical, 2 * m)
    histograms = []
    for rank in (m, m + 1):
        cycles = base.projected_cycles(lifted, rank)
        histograms.append(dict(sorted(Counter(map(len, cycles)).items())))
    assert histograms[0] == histograms[1]
    return {"components": sum(histograms[0].values()), "histogram": histograms[0]}


def diagnose(pair):
    state = _STATE
    left = state["left"][pair[0]]
    right = state["right"][pair[1]]
    supports = state["fixed_supports"] + [left["support"], right["support"]]
    base_selected = apply_prefix_packet(state["canonical"], supports, 6)
    final = all_decks(base_selected)
    typed_safe = all(
        support_safe(state["old_decks"][name], final[name])
        for name in state["old_decks"]
    ) and final["upper_q2"][search.TARGET] > 0
    if not typed_safe:
        return {"typed_q3_safe": False}

    base_topology = component_data(state["canonical"], base_selected, 6)
    binary = common_binary_phase(state["canonical"], base_selected)

    widths = {}
    no_g2 = True
    suffix_safe = True
    for m in (7, 8):
        canonical = base.canonical_edges(m)
        selected = apply_prefix_packet(canonical, supports, m)
        old = all_decks(canonical)
        new = all_decks(selected)
        casualties = {
            name: [
                base.bitword(value, 2 * m)
                for value in old[name]
                if new[name][value] == 0
            ]
            for name in old
        }
        if any(casualties.values()):
            suffix_safe = False
        signature = current_by_suffix_weight(old["upper_q3"], new["upper_q3"], m)
        # At suffix semilength two, a two-colour seam has suffix rank four.
        if m == 8 and any(weight == 4 and amount for (weight, _), amount in signature.items()):
            no_g2 = False
        widths[str(m)] = {
            "q3_current_by_suffix_weight_and_sign": {
                f"{weight}:{sign}": amount
                for (weight, sign), amount in sorted(signature.items())
            },
            "support_casualties": casualties,
            "topology": component_data(canonical, selected, m),
        }

    return {
        "typed_q3_safe": True,
        "no_two_colour_G2_seam": no_g2,
        "suffix_safe_m7_m8": suffix_safe,
        "common_binary_phase": binary,
        "base_topology": base_topology,
        "widths": widths,
        "left": left["name"],
        "right": right["name"],
    }


def worker(chunk):
    state = _STATE
    counts = Counter()
    solutions = []
    for i in chunk:
        left = state["left"][i]
        start = i + 1 if state["same"] else 0
        for j in range(start, len(state["right"])):
            right = state["right"][j]
            if left["owners"] & right["owners"]:
                continue
            counts["owner_disjoint_pairs"] += 1
            selected = set(state["mixed"])
            selected.symmetric_difference_update(left["support"])
            selected.symmetric_difference_update(right["support"])
            deck = q3_deck(selected)
            if deck is None:
                counts["nonpath_factors"] += 1
                continue
            if deck[W3] == 0:
                continue
            counts["creates_W3"] += 1
            if any(deck[value] == 0 for value in state["old_q3"]):
                continue
            counts["q3_support_safe"] += 1
            row = diagnose((i, j))
            if not row["typed_q3_safe"]:
                continue
            counts["typed_q3_safe"] += 1
            if row["no_two_colour_G2_seam"]:
                counts["no_G2_seam"] += 1
            if row["base_topology"]["components"] == state["mixed_topology_components"]:
                counts["zero_net_topology_count"] += 1
            if row["common_binary_phase"]:
                counts["common_binary_phase"] += 1
            if len(solutions) < state["limit"]:
                solutions.append(row)
    return counts, solutions


def chunks(size, workers):
    result = [[] for _ in range(workers)]
    for index in range(size):
        result[index % workers].append(index)
    return [chunk for chunk in result if chunk]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "menu",
        choices=("c6c6", "c6c8", "c8c8", "c6c10", "c8c10", "c6c12"),
    )
    parser.add_argument("--workers", type=int, default=32)
    parser.add_argument("--limit", type=int, default=20)
    args = parser.parse_args()

    canonical = base.canonical_edges(6)
    fixed_c8, fixed_c6 = mixed_tensor.prefix_packet()
    fixed_supports = [fixed_c8, fixed_c6]
    fixed_owners = {owner for support in fixed_supports for owner, _ in support}
    mixed = set(canonical)
    for support in fixed_supports:
        mixed.symmetric_difference_update(support)
    old_decks = all_decks(canonical)

    left_kind, right_kind = {
        "c6c6": ("c6", "c6"),
        "c6c8": ("c6", "c8"),
        "c8c8": ("c8", "c8"),
        "c6c10": ("c6", "c10"),
        "c8c10": ("c8", "c10"),
        "c6c12": ("c6", "c12"),
    }[args.menu]
    left = [row for row in catalogue(left_kind, canonical) if not row["owners"] & fixed_owners]
    right = left if left_kind == right_kind else [
        row for row in catalogue(right_kind, canonical) if not row["owners"] & fixed_owners
    ]

    global _STATE
    _STATE = {
        "canonical": canonical,
        "mixed": mixed,
        "old_decks": old_decks,
        "old_q3": old_decks["upper_q3"],
        "fixed_supports": fixed_supports,
        "left": left,
        "right": right,
        "same": left_kind == right_kind,
        "limit": args.limit,
        "mixed_topology_components": component_data(canonical, mixed, 6)["components"],
    }

    work = chunks(len(left), args.workers)
    context = mp.get_context("fork")
    with context.Pool(processes=len(work)) as pool:
        rows = pool.map(worker, work)
    counts = Counter()
    solutions = []
    for partial_counts, partial_solutions in rows:
        counts.update(partial_counts)
        solutions.extend(partial_solutions)
    solutions = solutions[:args.limit]
    print(json.dumps({
        "status": "PASS",
        "menu": args.menu,
        "catalogue_sizes": [len(left), len(right)],
        "counts": dict(sorted(counts.items())),
        "solutions": solutions,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
