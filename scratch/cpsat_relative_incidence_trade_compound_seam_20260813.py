#!/usr/bin/env python3
"""CP-SAT search for an exact local/global incidence trade installing C4--U5.

Heavy computation: run only on h100.

Each rank-m facet chooses an unordered pair of its rank-(m+1) supersets.
Owners have degree two.  Optional upper-current constraints preserve the
complete multiplicity vector of rank-(m+2) unions.  The selected internal
portal rows are frozen literally.  The objective minimizes changed facet
pairs relative to the first-aligned packet factor.
"""

from __future__ import annotations

import argparse
import collections
import itertools
import json
import time

from ortools.sat.python import cp_model

import audit_msw_inverse_trade_portal_shadow_20260813 as base
import audit_pbbs_portal_compound_coexistence_20260813 as co
import search_relative_inverse_trade_for_compound_seam_20260813 as rel


def old_factor_data(m: int):
    _, _, rows = co.full_first_aligned_packet(m)
    old = {}
    upper = collections.Counter()
    row_of_facet = {}
    for rid, row in enumerate(sorted(rows)):
        n = 2 * m + 1
        owners = [co.cyc_window(row, t, m + 1) for t in range(n)]
        for t in range(n):
            a, b = owners[t], owners[(t + 1) % n]
            f = a & b
            assert len(f) == m and f not in old
            pair = frozenset((a, b))
            old[f] = pair
            upper[a | b] += 1
            row_of_facet[f] = rid
    return rows, old, upper, row_of_facet


def solve(m: int, d: int, upper_mode: str, time_limit: float, workers: int,
          feasibility_only: bool, max_changes: int | None):
    started = time.time()
    n = 2 * m + 1
    ground = frozenset(range(n))
    rows, old, old_upper, row_of_facet = old_factor_data(m)
    protected_rows = rel.selected_portal_rows(m, d)
    protected_facets = set()
    for row in protected_rows:
        owners = [co.cyc_window(row, t, m + 1) for t in range(n)]
        protected_facets.update(owners[t] & owners[(t + 1) % n] for t in range(n))

    C4, U5 = co.c_owner(m, 4), co.height_owner(m, 5)
    F = C4 & U5
    assert len(F) == m
    desired = frozenset((C4, U5))
    assert old[F] != desired

    model = cp_model.CpModel()
    owner_terms = collections.defaultdict(list)
    upper_terms = collections.defaultdict(list)
    old_vars = []
    nonold_vars = []
    desired_var = None
    facet_vars = {}

    for facet_tuple in itertools.combinations(range(n), m):
        facet = frozenset(facet_tuple)
        outside = sorted(ground - facet)
        terms = []
        for x, y in itertools.combinations(outside, 2):
            a, b = facet | {x}, facet | {y}
            pair = frozenset((a, b))
            v = model.new_bool_var(f"f{','.join(map(str,facet_tuple))}_{x}_{y}")
            terms.append(v)
            owner_terms[a].append(v)
            owner_terms[b].append(v)
            upper_terms[facet | {x, y}].append(v)
            if pair == old[facet]:
                old_vars.append(v)
                if facet in protected_facets:
                    model.add(v == 1)
            else:
                nonold_vars.append(v)
            if facet == F and pair == desired:
                desired_var = v
        model.add_exactly_one(terms)
        facet_vars[facet] = terms

    assert desired_var is not None
    model.add(desired_var == 1)
    for terms in owner_terms.values():
        model.add(sum(terms) == 2)
    if upper_mode == "exact":
        all_uppers = set(upper_terms) | set(old_upper)
        for u in all_uppers:
            model.add(sum(upper_terms.get(u, ())) == old_upper.get(u, 0))
    elif upper_mode == "cover":
        # Preserve the support of the initial rank-(m+2) load vector, not its
        # multiplicities.  (The initial factor need not cover every possible
        # rank-(m+2) target.)
        for u in old_upper:
            model.add(sum(upper_terms.get(u, ())) >= 1)
    else:
        assert upper_mode == "none"

    if max_changes is not None:
        model.add(sum(nonold_vars) <= max_changes)
    if not feasibility_only:
        model.maximize(sum(old_vars))
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = time_limit
    solver.parameters.num_search_workers = workers
    solver.parameters.log_search_progress = True
    status = solver.solve(model)
    answer = {
        "m": m,
        "d": d,
        "upper_mode": upper_mode,
        "feasibility_only": feasibility_only,
        "max_changes": max_changes,
        "status": solver.status_name(status),
        "wall_seconds": time.time() - started,
        "facets": len(old),
        "candidate_triples": sum(len(x) for x in facet_vars.values()),
        "protected_rows": len(protected_rows),
        "protected_facets": len(protected_facets),
    }
    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        changed = []
        new_upper = collections.Counter()
        for facet, terms in facet_vars.items():
            chosen = None
            outside = sorted(ground - facet)
            for v, (x, y) in zip(terms, itertools.combinations(outside, 2)):
                if solver.boolean_value(v):
                    chosen = frozenset((facet | {x}, facet | {y}))
                    new_upper[facet | {x, y}] += 1
                    break
            assert chosen is not None
            if chosen != old[facet]:
                changed.append(
                    {
                        "facet": sorted(facet),
                        "old_owners": [sorted(x) for x in sorted(old[facet], key=lambda z: tuple(z))],
                        "new_owners": [sorted(x) for x in sorted(chosen, key=lambda z: tuple(z))],
                        "old_upper": sorted(set().union(*old[facet])),
                        "new_upper": sorted(set().union(*chosen)),
                    }
                )
        answer["changed_facets"] = len(changed)
        answer["changes"] = changed
        answer["upper_removed"] = [
            sorted(x) for x in (old_upper - new_upper).elements()
        ]
        answer["upper_added"] = [
            sorted(x) for x in (new_upper - old_upper).elements()
        ]
    return answer


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("m", type=int)
    ap.add_argument("d", type=int)
    ap.add_argument("--no-upper-exact", action="store_true")
    ap.add_argument("--upper-cover", action="store_true")
    ap.add_argument("--time-limit", type=float, default=300)
    ap.add_argument("--workers", type=int, default=32)
    ap.add_argument("--feasibility-only", action="store_true")
    ap.add_argument("--max-changes", type=int)
    ap.add_argument("--json")
    args = ap.parse_args()
    if args.upper_cover and args.no_upper_exact:
        ap.error("choose at most one of --upper-cover and --no-upper-exact")
    upper_mode = "cover" if args.upper_cover else (
        "none" if args.no_upper_exact else "exact"
    )
    out = solve(
        args.m,
        args.d,
        upper_mode,
        args.time_limit,
        args.workers,
        args.feasibility_only,
        args.max_changes,
    )
    payload = json.dumps(out, indent=2, sort_keys=True)
    print(payload)
    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            f.write(payload + "\n")


if __name__ == "__main__":
    main()
