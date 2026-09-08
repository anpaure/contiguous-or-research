#!/usr/bin/env python3
"""Search the candidate-5 singleton-G2 two-target adjacent-window rail.

Substantive execution belongs on H100.  At m=9 the two lost upper-q3
targets A=N0[110111] and B=N5[110111] are adjacent rank-12 sets.  Enumerate
every simple five-owner Johnson rail O0,...,O4 with consecutive four-owner
unions A and B.  Complete the missing rail incidences to every native C8
alternating cycle in the current mixed+C16 factor, then replay exact typed
currents, q3 support, common binary phase, and projected topology.

The same rail census also proves the native-C6 obstruction: every rail is
missing at least three incidences, and all three-missing sets are tested as
the complete new matching of a C6.
"""

from __future__ import annotations

import argparse
import itertools
import json
from collections import Counter, defaultdict

import audit_msw_t0v_tensor_residence_20260814 as base
import audit_msw_t0v_tensor_typed_currents_20260814 as typed
import audit_msw_t0v_mixed_c8_c6_tensor_20260814 as mixed
import audit_msw_t0v_mixed_q3_closed_tensor_20260814 as q3closed
import search_msw_t0_mixed_q3_long_cycle_backup_20260814 as longsearch
import search_msw_t0_mixed_q3_pair_atlas_20260814 as pairsearch


M = 9
WIDTH = 18
G2 = "110111"
N0 = "100011010111"
N5 = "100010011111"
A = base.bits(N0 + G2)
B = base.bits(N5 + G2)

C16_OWNERS = [
    "110010001101",
    "100010001111",
    "000010011111",
    "000010111110",
    "010010110110",
    "110000110110",
    "110000110101",
    "110010100101",
]
C16_COLOURS = [
    "110010001111",
    "100010011111",
    "000010111111",
    "010010111110",
    "110010110110",
    "110000110111",
    "110010110101",
    "110010101101",
]


def bit_values(value):
    return [1 << index for index in range(WIDTH) if value >> index & 1]


def difference(old, new):
    answer = Counter(new)
    answer.subtract(old)
    return Counter({value: amount for value, amount in answer.items() if amount})


def current_factor():
    canonical = base.canonical_edges(M)
    fixed_c8, fixed_c6 = mixed.prefix_packet()
    c16 = longsearch.cycle_support(
        tuple(map(base.bits, C16_OWNERS)),
        tuple(map(base.bits, C16_COLOURS)),
    )
    selected = pairsearch.apply_prefix_packet(
        canonical, [fixed_c8, fixed_c6, c16], M
    )
    return canonical, selected


def rail_rows(selected):
    intersection = A & B
    a_only = A ^ intersection
    b_only = B ^ intersection
    missing_pairs = [sum(row) for row in itertools.combinations(bit_values(intersection), 2)]
    neighbours = defaultdict(list)
    for left in missing_pairs:
        for right in missing_pairs:
            if left != right and (left & right).bit_count() == 1:
                neighbours[left].append(right)

    rows = []
    missing_histogram = Counter()
    for p1 in missing_pairs:
        o1 = intersection ^ p1
        for p2 in neighbours[p1]:
            o2 = intersection ^ p2
            for p3 in neighbours[p2]:
                if p3 == p1:
                    continue
                o3 = intersection ^ p3
                for deleted_left in bit_values(o1):
                    o0 = (o1 ^ deleted_left) | a_only
                    if o0 | o1 | o2 | o3 != A:
                        continue
                    for deleted_right in bit_values(o3):
                        o4 = (o3 ^ deleted_right) | b_only
                        if o1 | o2 | o3 | o4 != B:
                            continue
                        owners = (o0, o1, o2, o3, o4)
                        assert len(set(owners)) == 5
                        colours = tuple(
                            owners[index] | owners[index + 1]
                            for index in range(4)
                        )
                        assert len(set(colours)) == 4
                        required = frozenset(
                            (owners[index + endpoint], colours[index])
                            for index in range(4)
                            for endpoint in (0, 1)
                        )
                        absent = frozenset(required - selected)
                        missing_histogram[len(absent)] += 1
                        if len(absent) <= 4:
                            rows.append({
                                "owners": owners,
                                "colours": colours,
                                "required": required,
                                "absent": absent,
                            })
    return rows, missing_histogram


def one_cycle(new_incidences, selected):
    owners = {owner for owner, _ in new_incidences}
    colours = {colour for _, colour in new_incidences}
    if len(owners) != len(new_incidences) or len(colours) != len(new_incidences):
        return []
    by_colour = defaultdict(list)
    for owner, colour in selected:
        by_colour[colour].append(owner)
    choices = []
    for _, colour in sorted(new_incidences):
        assert len(by_colour[colour]) == 2
        choices.append(tuple(by_colour[colour]))

    cycles = []
    ordered_new = sorted(new_incidences)
    for removed in itertools.product(*choices):
        if len(set(removed)) != len(removed):
            continue
        if set(removed) != owners:
            continue
        old = frozenset(
            (removed[index], ordered_new[index][1])
            for index in range(len(ordered_new))
        )
        adjacency = defaultdict(set)
        for owner, colour in old | new_incidences:
            adjacency[(0, owner)].add((1, colour))
            adjacency[(1, colour)].add((0, owner))
        if not all(len(values) == 2 for values in adjacency.values()):
            continue
        seen = set()
        stack = [next(iter(adjacency))]
        while stack:
            vertex = stack.pop()
            if vertex in seen:
                continue
            seen.add(vertex)
            stack.extend(adjacency[vertex] - seen)
        if len(seen) != 2 * len(new_incidences):
            continue
        cycles.append(frozenset(old | new_incidences))
    return cycles


def complete_c8(absent, selected):
    """Complete three or four required new incidences to native C8s."""
    if len(absent) == 4:
        return one_cycle(absent, selected)
    if len(absent) != 3:
        return []
    required_owners = {owner for owner, _ in absent}
    required_colours = {colour for _, colour in absent}
    if len(required_owners) != 3 or len(required_colours) != 3:
        return []

    by_colour = defaultdict(list)
    for owner, colour in selected:
        by_colour[colour].append(owner)
    ordered = sorted(absent)
    choices = [tuple(by_colour[colour]) for _, colour in ordered]
    cycles = []
    for removed in itertools.product(*choices):
        if len(set(removed)) != 3:
            continue
        removed_set = set(removed)
        added_owner = removed_set - required_owners
        final_removed = required_owners - removed_set
        if len(added_owner) != 1 or len(final_removed) != 1:
            continue
        new_owner = next(iter(added_owner))
        old_owner = next(iter(final_removed))
        if (new_owner ^ old_owner).bit_count() != 2:
            continue
        extra_colour = new_owner | old_owner
        if extra_colour in required_colours:
            continue
        if (new_owner, extra_colour) in selected:
            continue
        if (old_owner, extra_colour) not in selected:
            continue
        new_matching = frozenset(set(absent) | {(new_owner, extra_colour)})
        # The choices above forced one possible old matching, but one_cycle
        # independently rechecks both selected mates and connectedness.
        cycles.extend(one_cycle(new_matching, selected))
    return sorted(set(cycles), key=lambda support: tuple(sorted(support)))


def encoded_incidence(incidence):
    owner, colour = incidence
    return [base.bitword(owner, WIDTH), base.bitword(colour, WIDTH)]


def encoded_counter(counter):
    return [
        {
            "value": base.bitword(value, WIDTH),
            "delta": amount,
        }
        for value, amount in sorted(counter.items())
    ]


def topology(selected, canonical):
    lifted = base.lifted_edges(selected, canonical, WIDTH)
    answer = []
    for rank in (M, M + 1):
        histogram = Counter(map(len, base.projected_cycles(lifted, rank)))
        answer.append(dict(sorted(histogram.items())))
    assert answer[0] == answer[1]
    return answer[0]


def target_provider_count(selected, target):
    """Count unoriented three-colour path windows with union target."""
    by_colour = defaultdict(list)
    for owner, colour in selected:
        if colour & ~target == 0:
            by_colour[colour].append(owner)
    adjacency = defaultdict(list)
    for colour, owners in by_colour.items():
        assert len(owners) == 2
        left, right = owners
        adjacency[left].append((right, colour))
        adjacency[right].append((left, colour))
    providers = set()
    for o0 in adjacency:
        for o1, c0 in adjacency[o0]:
            for o2, c1 in adjacency[o1]:
                if o2 == o0:
                    continue
                for o3, c2 in adjacency[o2]:
                    if o3 == o1:
                        continue
                    if c0 | c1 | c2 != target:
                        continue
                    forward = (o0, o1, o2, o3)
                    providers.add(min(forward, tuple(reversed(forward))))
    return len(providers)


def owner_arc_graph(selected):
    by_colour = defaultdict(list)
    owners = set()
    for owner, colour in selected:
        by_colour[colour].append(owner)
        owners.add(owner)
    assert all(len(values) == 2 for values in by_colour.values())
    outgoing = defaultdict(list)
    full = (1 << WIDTH) - 1
    for owner in owners:
        absent = full ^ owner
        while absent:
            bit = absent & -absent
            absent -= bit
            colour = owner | bit
            if (owner, colour) in selected:
                continue
            for removed_owner in by_colour[colour]:
                outgoing[owner].append((removed_owner, colour))
    return by_colour, outgoing


def target_start_arcs(selected, by_colour):
    starts = set()
    for target in (A, B):
        positions = bit_values(target)
        for chosen in itertools.combinations(positions, M):
            owner = sum(chosen)
            absent = target ^ owner
            while absent:
                bit = absent & -absent
                absent -= bit
                colour = owner | bit
                if (owner, colour) in selected:
                    continue
                for removed_owner in by_colour[colour]:
                    starts.add((owner, removed_owner, colour))
    return starts


def target_relevant_cycles(selected, k):
    """Every native C_(2k) containing a possible A/B provider incidence."""
    by_colour, outgoing = owner_arc_graph(selected)
    starts = target_start_arcs(selected, by_colour)
    seen = set()
    for start, second, first_colour in sorted(starts):
        owners = [start, second]
        colours = [first_colour]

        def dfs():
            current = owners[-1]
            if len(colours) == k - 1:
                for next_owner, colour in outgoing[current]:
                    if next_owner != start or colour in colours:
                        continue
                    support = longsearch.cycle_support(
                        tuple(owners), tuple(colours + [colour])
                    )
                    seen.add(support)
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
    return starts, seen


def johnson_neighbours(owner, target):
    inside = bit_values(owner)
    outside = bit_values(target ^ owner)
    return [
        (owner ^ removed) | added
        for removed in inside for added in outside
    ]


def offset_two_rail_census(selected, cycle_banks, limit):
    """Census O0..O5 with unions O0..O3=A and O2..O5=B."""
    intersection = A & B
    shared_owners = [
        sum(row) for row in itertools.combinations(bit_values(intersection), M)
    ]
    shared_owner_set = set(shared_owners)
    cycles = {}
    incidence_index = {}
    for kind, bank in cycle_banks.items():
        rows = []
        index = defaultdict(set)
        for cycle_index, support in enumerate(sorted(bank, key=lambda row: tuple(sorted(row)))):
            new = frozenset(support - selected)
            old = frozenset(support & selected)
            rows.append((support, new, old))
            for incidence in new:
                index[incidence].add(cycle_index)
        cycles[kind] = rows
        incidence_index[kind] = index

    total = 0
    histogram = Counter()
    shared_histogram = Counter()
    closure_counts = Counter()
    closure_supports = {kind: set() for kind in cycle_banks}
    examples = []
    for o2 in shared_owners:
        for o3 in johnson_neighbours(o2, intersection):
            if o3 not in shared_owner_set:
                continue
            c2 = o2 | o3
            assert c2.bit_count() == M + 1
            left_arms = []
            for o1 in johnson_neighbours(o2, A):
                for o0 in johnson_neighbours(o1, A):
                    owners = (o0, o1, o2, o3)
                    if len(set(owners)) != 4 or o0 | o1 | o2 | o3 != A:
                        continue
                    c0, c1 = o0 | o1, o1 | o2
                    if len({c0, c1, c2}) != 3:
                        continue
                    left_arms.append((o0, o1, c0, c1))
            right_arms = []
            for o4 in johnson_neighbours(o3, B):
                for o5 in johnson_neighbours(o4, B):
                    owners = (o2, o3, o4, o5)
                    if len(set(owners)) != 4 or o2 | o3 | o4 | o5 != B:
                        continue
                    c3, c4 = o3 | o4, o4 | o5
                    if len({c2, c3, c4}) != 3:
                        continue
                    right_arms.append((o4, o5, c3, c4))
            for o0, o1, c0, c1 in left_arms:
                for o4, o5, c3, c4 in right_arms:
                    owners = (o0, o1, o2, o3, o4, o5)
                    colours = (c0, c1, c2, c3, c4)
                    if len(set(owners)) != 6 or len(set(colours)) != 5:
                        continue
                    required = frozenset(
                        (owners[index + endpoint], colours[index])
                        for index in range(5) for endpoint in (0, 1)
                    )
                    absent = frozenset(required - selected)
                    total += 1
                    histogram[len(absent)] += 1
                    shared_histogram[
                        (c2.bit_count(), (intersection ^ c2).bit_count())
                    ] += 1
                    if len(absent) > 4:
                        continue
                    found = []
                    for kind in cycle_banks:
                        candidate_ids = None
                        for incidence in absent:
                            ids = incidence_index[kind].get(incidence, set())
                            candidate_ids = set(ids) if candidate_ids is None else candidate_ids & ids
                        if candidate_ids is None:
                            candidate_ids = set()
                        for cycle_index in candidate_ids:
                            support, new, old = cycles[kind][cycle_index]
                            if required & old:
                                continue
                            assert absent <= new
                            closure_counts[kind] += 1
                            closure_supports[kind].add(support)
                            found.append(kind)
                    if len(examples) < limit:
                        examples.append({
                            "owners": [base.bitword(value, WIDTH) for value in owners],
                            "colours": [base.bitword(value, WIDTH) for value in colours],
                            "shared_H": base.bitword(c2, WIDTH),
                            "omitted_from_intersection": base.bitword(intersection ^ c2, WIDTH),
                            "missing_incidences": [
                                encoded_incidence(row) for row in sorted(absent)
                            ],
                            "native_closures": found,
                        })
    return {
        "total_offset_two_rails": total,
        "missing_incidence_histogram": dict(sorted(histogram.items())),
        "shared_H_rank_and_omission_histogram": {
            f"{rank}:{omitted}": amount
            for (rank, omitted), amount in sorted(shared_histogram.items())
        },
        "closure_realizations": dict(closure_counts),
        "distinct_closing_cycles": {
            kind: len(rows) for kind, rows in closure_supports.items()
        },
        "examples_missing_at_most_four": examples,
    }


def inspect(support, rails, selected, canonical, old_typed, old_q3):
    after = set(selected)
    after.symmetric_difference_update(support)
    assert all(
        len(values) == 2
        for values in typed.maps(after)[1].values()
    )
    typed_currents = {
        name: difference(old_typed[name], new_deck)
        for name, new_deck in typed.typed_decks(after).items()
    }


def local_typed_current(selected, support):
    by_owner, by_colour = typed.maps(selected)
    changed_owners = {owner for owner, _ in support}
    changed_colours = {colour for _, colour in support}
    answer = {
        "owner": Counter(),
        "upper_q1": Counter(),
        "lower_q1": Counter(),
        "upper_q2": Counter(),
        "lower_q2": Counter(),
    }
    for owner in changed_owners:
        old_colours = set(by_owner[owner])
        new_colours = old_colours ^ {
            colour for changed_owner, colour in support
            if changed_owner == owner
        }
        assert len(old_colours) == len(new_colours)
        if len(old_colours) == 2:
            old_left, old_right = old_colours
            new_left, new_right = new_colours
            answer["upper_q2"][old_left | old_right] -= 1
            answer["upper_q2"][new_left | new_right] += 1
            answer["lower_q2"][old_left & old_right] -= 1
            answer["lower_q2"][new_left & new_right] += 1
    for colour in changed_colours:
        old_owners = set(by_colour[colour])
        new_owners = old_owners ^ {
            owner for owner, changed_colour in support
            if changed_colour == colour
        }
        assert len(old_owners) == len(new_owners) == 2
        old_left, old_right = old_owners
        new_left, new_right = new_owners
        answer["lower_q1"][old_left & old_right] -= 1
        answer["lower_q1"][new_left & new_right] += 1
    return {
        name: Counter({value: amount for value, amount in delta.items() if amount})
        for name, delta in answer.items()
    }


def add_currents(left, right):
    answer = {}
    for name in left:
        delta = Counter(left[name])
        delta.update(right[name])
        answer[name] = Counter({value: amount for value, amount in delta.items() if amount})
    return answer


def current_signature(current):
    return tuple(
        (name, tuple(sorted(delta.items())))
        for name, delta in sorted(current.items())
    )


def negate_signature(signature):
    return tuple(
        (name, tuple((value, -amount) for value, amount in rows))
        for name, rows in signature
    )


def pair_atlas(selected, canonical, old_typed, old_q3, cycle_banks, limit):
    target_edges = {
        target: frozenset(
            (owner, colour) for owner, colour in selected
            if colour & ~target == 0
        )
        for target in (A, B)
    }
    data = {}
    for support in set().union(*cycle_banks.values()):
        data[support] = {
            "owners": {owner for owner, _ in support},
            "colours": {colour for _, colour in support},
            "typed": local_typed_current(selected, support),
            "target_support": {
                target: frozenset(
                    incidence for incidence in support
                    if incidence[1] & ~target == 0
                )
                for target in (A, B)
            },
        }
        data[support]["typed_signature"] = current_signature(data[support]["typed"])

    counts = {}
    exact_rows = []
    menus = (("C6+C6", "C6", "C6"), ("C6+C8", "C6", "C8"), ("C8+C8", "C8", "C8"))
    for menu, left_kind, right_kind in menus:
        left_bank = sorted(cycle_banks[left_kind], key=lambda row: tuple(sorted(row)))
        right_bank = sorted(cycle_banks[right_kind], key=lambda row: tuple(sorted(row)))
        row_counts = Counter({
            "inverse_typed_signature_pairs": 0,
            "owner_colour_disjoint_inverse_pairs": 0,
            "zero_typed_create_both_targets": 0,
            "nonpath_factor": 0,
            "zero_typed_binary": 0,
        })
        right_by_signature = defaultdict(list)
        for right in right_bank:
            right_by_signature[data[right]["typed_signature"]].append(right)
        right_position = {support: index for index, support in enumerate(right_bank)}
        for left_index, left in enumerate(left_bank):
            left_data = data[left]
            inverse = negate_signature(left_data["typed_signature"])
            inverse_rows = right_by_signature.get(inverse, [])
            for right in inverse_rows:
                if left_kind == right_kind and right_position[right] <= left_index:
                    continue
                row_counts["inverse_typed_signature_pairs"] += 1
                right_data = data[right]
                if left_data["owners"] & right_data["owners"]:
                    continue
                if left_data["colours"] & right_data["colours"]:
                    continue
                row_counts["owner_colour_disjoint_inverse_pairs"] += 1
                combined = add_currents(left_data["typed"], right_data["typed"])
                assert all(not delta for delta in combined.values())
                loads = {}
                for target in (A, B):
                    edges = set(target_edges[target])
                    edges.symmetric_difference_update(left_data["target_support"][target])
                    edges.symmetric_difference_update(right_data["target_support"][target])
                    loads[target] = target_provider_count(edges, target)
                if not loads[A] or not loads[B]:
                    continue
                row_counts["zero_typed_create_both_targets"] += 1
                after = set(selected)
                after.symmetric_difference_update(left)
                after.symmetric_difference_update(right)
                # Target-local counting was the fast filter; full q3 replay
                # binds every zero-current dual creator.
                try:
                    full_q3 = q3closed.q3_deck(after)
                except AssertionError:
                    row_counts["nonpath_factor"] += 1
                    continue
                assert full_q3[A] == loads[A] and full_q3[B] == loads[B]
                binary = pairsearch.common_binary_phase(selected, after)
                if binary:
                    row_counts["zero_typed_binary"] += 1
                report = {
                    "menu": menu,
                    "left_support": [encoded_incidence(row) for row in sorted(left)],
                    "right_support": [encoded_incidence(row) for row in sorted(right)],
                    "target_loads": {
                        "A": loads[A],
                        "B": loads[B],
                    },
                    "typed_zero_through_q2": True,
                    "typed_currents": {
                        name: encoded_counter(delta)
                        for name, delta in combined.items()
                    },
                    "common_binary_phase": binary,
                }
                if binary:
                    report["old_topology"] = topology(selected, canonical)
                    report["new_topology"] = topology(after, canonical)
                    exact_rows.append(report)
        counts[menu] = dict(row_counts)
    return counts, exact_rows[:limit]
    q3 = q3closed.q3_deck(after)
    q3_current = difference(old_q3, q3)
    casualties = [
        value for value, amount in q3_current.items()
        if amount < 0 and q3[value] == 0
    ]
    old_topology = topology(selected, canonical)
    new_topology = topology(after, canonical)
    return {
        "cycle_incidences": [encoded_incidence(row) for row in sorted(support)],
        "old_incidences": [
            encoded_incidence(row) for row in sorted(support & selected)
        ],
        "new_incidences": [
            encoded_incidence(row) for row in sorted(support - selected)
        ],
        "witness_rails": [
            {
                "owners": [base.bitword(value, WIDTH) for value in row["owners"]],
                "colours": [base.bitword(value, WIDTH) for value in row["colours"]],
            }
            for row in rails[:4]
        ],
        "target_loads": {
            "A_old": old_q3[A],
            "A_new": q3[A],
            "B_old": old_q3[B],
            "B_new": q3[B],
        },
        "typed_zero_through_q2": all(not delta for delta in typed_currents.values()),
        "typed_currents": {
            name: encoded_counter(delta)
            for name, delta in typed_currents.items()
        },
        "q3_current": encoded_counter(q3_current),
        "q3_support_casualties": [base.bitword(value, WIDTH) for value in casualties],
        "common_binary_phase": pairsearch.common_binary_phase(selected, after),
        "old_topology": old_topology,
        "new_topology": new_topology,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=20)
    args = parser.parse_args()
    canonical, selected = current_factor()
    rails, missing_histogram = rail_rows(selected)

    c6_supports = set()
    c8_supports = set()
    support_to_rails = defaultdict(list)
    completion_counts = Counter()
    for rail in rails:
        absent = rail["absent"]
        if len(absent) == 3:
            completions = one_cycle(absent, selected)
            completion_counts["c6_completions"] += len(completions)
            for support in completions:
                c6_supports.add(support)
                support_to_rails[support].append(rail)
        completions = complete_c8(absent, selected)
        completion_counts["c8_completions"] += len(completions)
        for support in completions:
            c8_supports.add(support)
            support_to_rails[support].append(rail)

    old_typed = typed.typed_decks(selected)
    old_q3 = q3closed.q3_deck(selected)
    rows = []
    for kind, supports in (("C6", c6_supports), ("C8", c8_supports)):
        for support in sorted(supports, key=lambda row: tuple(sorted(row))):
            report = inspect(
                support, support_to_rails[support], selected, canonical,
                old_typed, old_q3,
            )
            report["kind"] = kind
            rows.append(report)

    exhaustive_counts = {}
    exhaustive_dual = []
    cycle_banks = {}
    for kind, k in (("C6", 3), ("C8", 4)):
        starts, supports = target_relevant_cycles(selected, k)
        cycle_banks[kind] = supports
        dual = []
        for support in sorted(supports, key=lambda row: tuple(sorted(row))):
            after = set(selected)
            after.symmetric_difference_update(support)
            load_a = target_provider_count(after, A)
            if not load_a:
                continue
            load_b = target_provider_count(after, B)
            if not load_b:
                continue
            report = inspect(
                support, [], selected, canonical, old_typed, old_q3
            )
            report["kind"] = kind
            dual.append(report)
        exhaustive_counts[kind] = {
            "target_start_arcs": len(starts),
            "distinct_target_relevant_cycles": len(supports),
            "cycles_creating_both_targets": len(dual),
            "zero_typed_binary_cycles": sum(
                row["typed_zero_through_q2"] and row["common_binary_phase"]
                for row in dual
            ),
        }
        exhaustive_dual.extend(dual)

    offset_two = offset_two_rail_census(selected, cycle_banks, args.limit)

    pair_counts, pair_solutions = pair_atlas(
        selected, canonical, old_typed, old_q3, cycle_banks, args.limit
    )

    positive = [
        row for row in rows
        if row["target_loads"]["A_new"] > row["target_loads"]["A_old"]
        and row["target_loads"]["B_new"] > row["target_loads"]["B_old"]
    ]
    exact = [
        row for row in positive
        if row["typed_zero_through_q2"]
        and row["common_binary_phase"]
    ]
    print(json.dumps({
        "status": "PASS",
        "target_A": base.bitword(A, WIDTH),
        "target_B": base.bitword(B, WIDTH),
        "target_intersection": base.bitword(A & B, WIDTH),
        "target_symmetric_difference": base.bitword(A ^ B, WIDTH),
        "total_rails": sum(missing_histogram.values()),
        "missing_incidence_histogram": dict(sorted(missing_histogram.items())),
        "retained_rails_missing_at_most_four": len(rails),
        "raw_completion_counts": dict(completion_counts),
        "distinct_c6_cycles": len(c6_supports),
        "distinct_c8_cycles": len(c8_supports),
        "cycles_replayed": len(rows),
        "cycles_creating_both_targets": len(positive),
        "exact_zero_typed_binary_solutions": len(exact),
        "solutions": exact[:args.limit],
        "positive_near_misses": positive[:args.limit],
        "exhaustive_single_cycle_counts": exhaustive_counts,
        "exhaustive_dual_creators": exhaustive_dual[:args.limit],
        "offset_two_six_owner_census": offset_two,
        "target_relevant_disjoint_pair_counts": pair_counts,
        "pair_solutions": pair_solutions,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
