#!/usr/bin/env python3
"""Exact audit of the proposed D5 closed-router-tube reduction.

Substantive execution belongs on H100.  The script independently rebuilds
the rank-10 common-core carrier from its displayed set formulae.  It checks
the old/new resource banks, derived immediate-lower tickets, stage and outer
monodromies, internal q=2 residence, and linear upper/lower q2 supports.
"""

from __future__ import annotations

import json
from collections import Counter
from functools import reduce


def union(*sets):
    return frozenset().union(*sets)


def or_all(sets):
    return reduce(frozenset.union, sets, frozenset())


def and_all(sets):
    sets = list(sets)
    return reduce(frozenset.intersection, sets[1:], sets[0])


def counts(values):
    return Counter(values)


def support_report(old, new):
    old, new = counts(old), counts(new)
    losses = {value: load for value, load in old.items() if not new[value]}
    decreases = {
        value: load - new[value]
        for value, load in old.items() if new[value] < load
    }
    return {
        "old_support": len(old),
        "new_support": len(new),
        "old_occurrences": sum(old.values()),
        "new_occurrences": sum(new.values()),
        "support_losses": len(losses),
        "lost_occurrences": sum(losses.values()),
        "load_decrease_targets": len(decreases),
        "load_decrease_occurrences": sum(decreases.values()),
    }


def word(value):
    return "+".join(sorted(value))


def build():
    h = frozenset({"h"})
    d = [
        frozenset({f"k{s}", *(f"t{s}{i}" for i in range(3))})
        for s in range(2)
    ]
    a = [frozenset(f"a{s}{i}" for i in range(3)) for s in range(3)]
    b = [frozenset({f"b{s}"}) for s in range(2)]
    omega = union(h, *d, *a, *b)
    assert len(omega) == 20
    k = [f"k{s}" for s in range(2)]
    t = [[f"t{s}{i}" for i in range(3)] for s in range(2)]
    aa = [[f"a{s}{i}" for i in range(3)] for s in range(3)]
    bb = [f"b{s}" for s in range(2)]
    core = [None] * 3
    core[0] = union(h, d[0], d[1])
    core[1] = union(core[0] - d[0], a[0], b[0])
    core[2] = union(core[1] - d[1], a[1], b[1])
    assert all(len(value) == 9 for value in core)

    stages = []
    epsilon = [1, -1]
    for s in range(2):
        eps = epsilon[s]
        stage = {name: [] for name in ("E", "Z", "W", "R", "Ep",
                                       "Y", "V", "Q", "S")}
        for i in range(3):
            ip = (i + eps) % 3
            im = (i - eps) % 3
            stage["E"].append(union(core[s], {aa[s][i]}))
            stage["Z"].append(union(
                core[s] - {k[s]}, {aa[s][i], aa[s][ip]}
            ))
            stage["W"].append(union(
                core[s] - {k[s], t[s][i]},
                {aa[s][i], aa[s][ip], bb[s]},
            ))
            stage["R"].append(union(
                core[s] - d[s], {t[s][im]}, a[s], {bb[s]}
            ))
            stage["Ep"].append(union(core[s + 1], {aa[s + 1][i]}))
            stage["Y"].append(union(
                core[s], {aa[s][i], aa[s][ip]}
            ))
            stage["V"].append(union(
                core[s] - {k[s]}, {aa[s][i], aa[s][ip], bb[s]}
            ))
            stage["Q"].append(union(
                core[s] - {k[s], t[s][i]}, a[s], {bb[s]}
            ))
            stage["S"].append(union(
                core[s] - d[s], {t[s][im]}, a[s],
                {bb[s], aa[s + 1][i]},
            ))
        for name in ("E", "Z", "W", "R", "Ep"):
            assert all(len(value) == 10 for value in stage[name])
        for name in ("Y", "V", "Q", "S"):
            assert all(len(value) == 11 for value in stage[name])
        assert stage["Ep"] == [
            union(core[s + 1], {aa[s + 1][i]}) for i in range(3)
        ]
        stages.append(stage)

    cap = {name: [] for name in ("P", "C", "T", "F")}
    for i in range(3):
        ip = (i + 1) % 3
        cap["P"].append(union(core[2], {aa[2][i], aa[2][ip]}))
        cap["C"].append(union(
            core[2] - {aa[0][i]}, {aa[2][i], aa[2][ip]}
        ))
        cap["T"].append(union(core[2] - {aa[0][i]}, a[2]))
        cap["F"].append(union(core[2] - {aa[0][i], "h"}, a[2]))
    assert all(len(value) == 11 for name in ("P", "T")
               for value in cap[name])
    assert all(len(value) == 10 for name in ("C", "F")
               for value in cap[name])

    packets = {}
    for state in ("old", "new"):
        lower_paths = []
        upper_paths = []
        for root in range(3):
            if state == "old":
                first_index = root
                second_index = root
            else:
                first_index = (root - epsilon[0]) % 3
                # Stage 0 ends at E1[first_index].  Stage 1's new path
                # indexed j starts at E1[j+epsilon[1]].
                second_index = (first_index - epsilon[1]) % 3
                assert second_index == root
            x = [
                stages[0]["E"][root],
                stages[0]["Z"][first_index],
                stages[0]["W"][first_index],
                stages[0]["R"][first_index],
                stages[0]["Ep"][first_index],
                stages[1]["Z"][second_index],
                stages[1]["W"][second_index],
                stages[1]["R"][second_index],
                stages[1]["Ep"][second_index],
                cap["C"][root], cap["F"][root],
            ]
            y = [
                stages[0]["Y"][first_index],
                stages[0]["V"][first_index],
                stages[0]["Q"][first_index],
                stages[0]["S"][first_index],
                stages[1]["Y"][second_index],
                stages[1]["V"][second_index],
                stages[1]["Q"][second_index],
                stages[1]["S"][second_index],
                cap["P"][root], cap["T"][root],
            ]
            assert len(x) == 11 and len(y) == 10
            assert all(y[i] == union(x[i], x[i + 1]) for i in range(10))
            assert all(len(x[i] ^ x[i + 1]) == 2 for i in range(10))
            assert x[-1] == omega - x[0]
            lower_paths.append(x)
            upper_paths.append(y)
        packets[state] = (lower_paths, upper_paths)
    return omega, stages, packets


def main():
    omega, stages, packets = build()
    old_x, old_y = packets["old"]
    new_x, new_y = packets["new"]

    old_owner_bank = counts(value for path in old_x for value in path)
    new_owner_bank = counts(value for path in new_x for value in path)
    old_upper_bank = counts(value for path in old_y for value in path)
    new_upper_bank = counts(value for path in new_y for value in path)
    old_lower_tickets = counts(
        path[i] & path[i + 1] for path in old_x for i in range(10)
    )
    new_lower_tickets = counts(
        path[i] & path[i + 1] for path in new_x for i in range(10)
    )
    assert old_owner_bank == new_owner_bank
    assert old_upper_bank == new_upper_bank
    assert old_lower_tickets == new_lower_tickets
    old_ticket_locations = {}
    for row, path in enumerate(old_x):
        for position in range(10):
            ticket = path[position] & path[position + 1]
            old_ticket_locations.setdefault(ticket, []).append([row, position])
    duplicate_tickets = {
        word(ticket): locations
        for ticket, locations in old_ticket_locations.items()
        if len(locations) > 1
    }

    old_lower_q2 = [
        and_all(path[i:i + 3]) for path in old_x for i in range(9)
    ]
    new_lower_q2 = [
        and_all(path[i:i + 3]) for path in new_x for i in range(9)
    ]
    old_upper_q2 = [
        or_all(path[i:i + 3]) for path in old_x for i in range(9)
    ]
    new_upper_q2 = [
        or_all(path[i:i + 3]) for path in new_x for i in range(9)
    ]

    internal_residence = {}
    for state, (paths, upper_paths) in packets.items():
        lower_ok = True
        upper_ok = True
        for path, upath in zip(paths, upper_paths):
            supports = [path[i] ^ path[i + 1] for i in range(10)]
            lower_ok &= all(not supports[i] & supports[i + 1]
                            for i in range(9))
            upper_supports = [upath[i] ^ upath[i + 1] for i in range(9)]
            assert all(len(value) == 2 for value in upper_supports)
            upper_ok &= all(
                not upper_supports[i] & upper_supports[i + 1]
                for i in range(8)
            )
        internal_residence[state] = {
            "lower_q2": bool(lower_ok),
            "upper_q2": bool(upper_ok),
        }

    stage_actions = {
        "old_stage_0": [0, 1, 2],
        "old_stage_1": [0, 1, 2],
        "new_stage_0": [2, 0, 1],
        "new_stage_1": [1, 2, 0],
    }
    outer_actions = {
        "old": [0, 1, 2],
        "new": [0, 1, 2],
    }
    required_d5_actions = {
        "tail_0": [0, 2, 1],
        "tail_1": [2, 1, 0],
        "tail_2": [1, 0, 2],
    }
    assert all(action != outer_actions["new"]
               for action in required_d5_actions.values())

    report = {
        "status": "REDUCTION_FAIL",
        "carrier_finite_replay": "PASS",
        "ground_size": len(omega),
        "owner_bank": {
            "occurrences": sum(old_owner_bank.values()),
            "support": len(old_owner_bank),
            "simple": max(old_owner_bank.values()) == 1,
            "old_new_equal": old_owner_bank == new_owner_bank,
        },
        "immediate_upper_bank": {
            "occurrences": sum(old_upper_bank.values()),
            "support": len(old_upper_bank),
            "simple": max(old_upper_bank.values()) == 1,
            "old_new_equal": old_upper_bank == new_upper_bank,
        },
        "derived_immediate_lower_ticket_bank": {
            "occurrences": sum(old_lower_tickets.values()),
            "support": len(old_lower_tickets),
            "simple": max(old_lower_tickets.values()) == 1,
            "old_new_equal": old_lower_tickets == new_lower_tickets,
            "multiplicity_histogram": dict(sorted(Counter(
                old_lower_tickets.values()
            ).items())),
            "duplicates": duplicate_tickets,
        },
        "stage_actions": stage_actions,
        "outer_actions": outer_actions,
        "required_d5_tail_fixed_transpositions": required_d5_actions,
        "outer_action_matches_any_required_reset": False,
        "permutation_parity_obstruction": (
            "C6 stage actions lie in A3; each D5 tail-fixed reset is odd"
        ),
        "internal_residence_excluding_terminal_crossings": internal_residence,
        "linear_lower_q2_current": support_report(old_lower_q2, new_lower_q2),
        "linear_upper_q2_current": support_report(old_upper_q2, new_upper_q2),
        "conclusions": {
            "common_X_Y_and_lower_ticket_bank": True,
            "identity_outer_monodromy_both_states": True,
            "closed_tube_realizes_D5_reset": False,
            "terminal_crossing_residence_audited": False,
            "support_monotonicity_follows_from_nonzero_current": False,
        },
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
