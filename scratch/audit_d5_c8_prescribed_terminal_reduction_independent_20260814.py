#!/usr/bin/env python3
"""Independent audit of the D5-to-resident-C8 row-reset reduction.

Substantive execution belongs on H100 only.  The audit has two independent
parts.  First it rebuilds the complementary-square C8, its exact lower-q2
current, and the four fixed heptagonal backups over every requested
admissible (m,q).  Second it rebuilds the frozen D5 rows and classifies the
literal Johnson geometry of the 212 nontrivial terminal triples.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import search_t2_cross_suffix_alternating_cycles_20260813 as base  # noqa:E402


def insert_fixed(base_order, fixed, length):
    out = []
    iterator = iter(base_order)
    for position in range(1, length + 1):
        out.append(fixed[position] if position in fixed else next(iterator))
    assert next(iterator, None) is None
    return out


def c8_paths(m, q):
    assert q >= 5 and m >= max(q + 8, 2 * q + 2)
    C = [("c", index) for index in range(m - 3)]
    Q = [("q", index) for index in range(4)]
    Z = [("z", index) for index in range(m - 3)]
    a = ("a", 0)
    ground = set(C + Q + Z + [a])
    n = m - 1
    w = n - q
    paths = []
    t_values = []
    for j in range(4):
        p = C[j]
        t = C[j + q]
        d = Z[m - 4 - j]
        t_values.append(t)
        U = set(C + [a, Q[j], Q[(j + 1) % 4]])
        missing = [Q[(j + 2) % 4], Q[(j + 3) % 4]]
        alpha = next(value for value in missing if value[1] % 2 == 0)
        beta = next(value for value in missing if value[1] % 2 == 1)
        gamma = [C[(j + step) % len(C)] for step in range(1, len(C))]
        assert gamma[q - 1] == t

        forward = [U]
        departures = gamma + [a, Q[j], Q[(j + 1) % 4]]
        arrivals = Z + [alpha, beta]
        for departure, arrival in zip(departures, arrivals):
            forward.append((forward[-1] - {departure}) | {arrival})
        B = {p} | (ground - U)
        assert forward[-1] == B

        rho_base = [value for value in gamma if value != t]
        if j < 3:
            rho = insert_fixed(rho_base, {w: Q[j]}, n - 3)
        else:
            rho_base = [
                value for value in rho_base if value not in {C[1], C[2]}
            ]
            rho = insert_fixed(
                rho_base,
                {w: Q[j], w + 1: C[1], w + 2: C[2]},
                n - 3,
            )
        departures = [value for value in Z if value != d] + [
            Q[(j + 3) % 4], d, Q[(j + 2) % 4]
        ]
        arrivals = rho + [Q[(j + 1) % 4], t, a]
        ret = [B]
        for departure, arrival in zip(departures, arrivals):
            ret.append((ret[-1] - {departure}) | {arrival})
        R = set(C + [Q[j], Q[(j + 1) % 4], Q[(j + 2) % 4]])
        assert ret[-2] == R and ret[-1] == U
        path = forward + ret[1:-1]
        assert len(path) == 2 * n and path[0] == U and path[-1] == R
        paths.append(path)
    return ground, C, Q, paths, t_values


def palettes(cycles):
    owners = Counter()
    lowers = Counter()
    uppers = Counter()
    for cycle in cycles:
        for index, owner in enumerate(cycle):
            successor = cycle[(index + 1) % len(cycle)]
            assert len(owner ^ successor) == 2
            owners[frozenset(owner)] += 1
            lowers[frozenset(owner & successor)] += 1
            uppers[frozenset(owner | successor)] += 1
    return owners, lowers, uppers


def triple_intersections(cycles):
    result = Counter()
    for cycle in cycles:
        for index, owner in enumerate(cycle):
            value = owner & cycle[(index + 1) % len(cycle)]
            value &= cycle[(index + 2) % len(cycle)]
            result[frozenset(value)] += 1
    return result


def cyclic_runs(bits):
    if all(bits) or not any(bits):
        return None
    length = len(bits)
    runs = {}
    for value in (False, True):
        starts = [
            index for index in range(length)
            if bits[index] == value and bits[index - 1] != value
        ]
        assert len(starts) == 1
        run = 0
        while bits[(starts[0] + run) % length] == value:
            run += 1
        runs[value] = run
    return runs[True], runs[False]


def backup_cycle(target, anchor, outside):
    core = set(target) - {anchor}
    toggles = [anchor] + list(outside)
    assert len(toggles) == 7 and len(set(toggles)) == 7
    return [
        core | {
            toggles[index],
            toggles[(index + 1) % 7],
            toggles[(index + 2) % 7],
        }
        for index in range(7)
    ]


def audit_c8(m, q):
    ground, C, Q, paths, t_values = c8_paths(m, q)
    switched_paths = [sum(paths, [])]
    old_palettes = palettes(paths)
    new_palettes = palettes(switched_paths)
    assert old_palettes == new_palettes
    assert all(max(bank.values()) == 1 for bank in old_palettes)
    assert all(len(bank) == 8 * m - 8 for bank in old_palettes)

    old_q2 = triple_intersections(paths)
    new_q2 = triple_intersections(switched_paths)
    losses = Counter({
        value: old_q2[value] - new_q2[value]
        for value in old_q2 if old_q2[value] > new_q2[value]
    })
    births = Counter({
        value: new_q2[value] - old_q2[value]
        for value in new_q2 if new_q2[value] > old_q2[value]
    })
    predicted_losses = {
        frozenset(
            (set(C) - {t_values[index]})
            | {Q[index], Q[(index + 1) % 4]}
        )
        for index in range(4)
    }
    predicted_births = {
        frozenset(
            (set(C) - {t_values[index]})
            | {Q[(index + 1) % 4], Q[(index + 2) % 4]}
        )
        for index in range(4)
    }
    assert set(losses) == predicted_losses
    assert set(births) == predicted_births
    assert set(losses.values()) == {1} == set(births.values())
    assert all(new_q2[value] == 0 for value in predicted_losses)

    used = tuple(set(bank) for bank in old_palettes)
    backups = []
    for index in range(4):
        target = frozenset(
            (set(C) - {t_values[index]})
            | {Q[index], Q[(index + 1) % 4]}
        )
        anchor = C[0]
        outside = (
            ("a", 0), Q[(index + 2) % 4], Q[(index + 3) % 4],
            ("z", 0), ("z", 1), ("z", 2),
        )
        assert anchor in target and set(outside) <= ground - set(target)
        cycle = backup_cycle(target, anchor, outside)
        banks = palettes([cycle])
        assert all(len(bank) == 7 and max(bank.values()) == 1 for bank in banks)
        assert all(not set(bank) & used_bank for bank, used_bank in zip(banks, used))
        for bank, used_bank in zip(banks, used):
            used_bank.update(bank)
        assert triple_intersections([cycle])[target] == 1
        for trace, expected in (
            (cycle, (3, 4)),
            ([cycle[r] & cycle[(r + 1) % 7] for r in range(7)], (2, 5)),
            ([cycle[r] | cycle[(r + 1) % 7] for r in range(7)], (4, 3)),
        ):
            actual = {
                cyclic_runs([coordinate in row for row in trace])
                for coordinate in ground
            } - {None}
            assert actual == {expected}
        backups.append(cycle)

    backup_q2 = triple_intersections(backups)
    combined_old = old_q2 + backup_q2
    combined_new = new_q2 + backup_q2
    assert all(combined_new[target] > 0 for target in combined_old)
    return {
        "m": m,
        "q": q,
        "main_palette_size_each": 8 * m - 8,
        "lower_q2_losses": len(losses),
        "lower_q2_births": len(births),
        "backups": len(backups),
        "backup_owners": sum(map(len, backups)),
        "residual_support_losses": 0,
    }


def johnson_distance(left, right):
    return (left ^ right).bit_count() // 2


def audit_d5(selection, certificate):
    m, n = 11, 22
    canonical = base.canonical_edges(m)
    post = set(canonical)
    base.apply_t2(post, list(base.dyck_words(5)))
    _, by_colour = base.factor_maps(post)
    assignment = {
        base.bits(word): state
        for word, state in certificate["owner_union_graph"][
            "three_state_assignment"
        ]
    }
    histogram = Counter()
    examples = {}
    pass_rows = reset_rows = 0
    for item in selection["selection"]:
        owners = tuple(
            base.bits(word) for word in item["candidate"]["owners"]
        )
        colours = tuple(
            base.bits(word) for word in item["candidate"]["new_colours"]
        )
        rows = [
            (owners[index], colours[index - 1], colours[index])
            for index in range(len(owners))
        ]
        removed_owner = {old: owner for owner, old, _ in rows}
        for tail, old, new in rows:
            old_head = next(owner for owner in by_colour[old] if owner != tail)
            new_head = next(
                owner for owner in by_colour[new]
                if owner != removed_owner[new]
            )
            states = (
                assignment[tail], assignment[old_head], assignment[new_head]
            )
            assert states[0] != states[1] and states[0] != states[2]
            if states[1] == states[2]:
                pass_rows += 1
                continue
            reset_rows += 1
            signature = (
                johnson_distance(tail, old_head),
                johnson_distance(tail, new_head),
                johnson_distance(old_head, new_head),
                (tail & old_head & new_head).bit_count(),
                (tail | old_head | new_head).bit_count(),
            )
            histogram[signature] += 1
            examples.setdefault(signature, [
                base.bitword(value, n + 1)
                for value in (tail, old_head, new_head)
            ])
    assert pass_rows == 265 and reset_rows == 212
    assert histogram == Counter({
        (1, 1, 1, 10, 13): 48,
        (1, 1, 2, 9, 13): 164,
    })
    return {
        "pass_rows": pass_rows,
        "reset_rows": reset_rows,
        "terminal_geometry_histogram": {
            ",".join(map(str, key)): value
            for key, value in sorted(histogram.items())
        },
        "literal_marked_pair_relabelling_impossible_rows": 164,
        "examples": {
            ",".join(map(str, key)): value
            for key, value in sorted(examples.items())
        },
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("selection")
    parser.add_argument("certificate")
    parser.add_argument("--max-m", type=int, default=50)
    args = parser.parse_args()
    selection_path = Path(args.selection)
    certificate_path = Path(args.certificate)
    selection_raw = selection_path.read_bytes()
    certificate_raw = certificate_path.read_bytes()
    selection = json.loads(selection_raw)
    certificate = json.loads(certificate_raw)
    assert hashlib.sha256(selection_raw).hexdigest() == (
        "94deb656dac1d8955b20d851e92600156d703842d6de169d4b6bea356fa3ec32"
    )
    assert certificate["selection_sha256"] == hashlib.sha256(
        selection_raw
    ).hexdigest()

    c8_cases = []
    for m in range(13, args.max_m + 1):
        for q in range(5, m):
            if m >= max(q + 8, 2 * q + 2):
                c8_cases.append(audit_c8(m, q))
    assert c8_cases
    print(json.dumps({
        "status": "PASS",
        "scope": {
            "abstract_internal_clauses_1_and_3": "PASS",
            "internal_clause_2": "PASS",
            "internal_clause_4_after_four_backups": "PASS",
            "exposed_terminal_clauses_2_and_4": "UNPROVED",
            "simultaneous_212_copy_embedding": "UNPROVED",
        },
        "selection_sha256": hashlib.sha256(selection_raw).hexdigest(),
        "certificate_sha256": hashlib.sha256(certificate_raw).hexdigest(),
        "c8_admissible_cases": len(c8_cases),
        "c8_parameter_range": {"min_m": 13, "max_m": args.max_m},
        "c8_first": c8_cases[0],
        "c8_last": c8_cases[-1],
        "d5": audit_d5(selection, certificate),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
