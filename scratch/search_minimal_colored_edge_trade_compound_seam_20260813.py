#!/usr/bin/env python3
"""Search minimal colored owner-edge trades installing C4--U5.

Heavy runs belong on h100.  A rank-m facet is a color; its current factor
edge joins the two incident rank-(m+1) owners selected by the first-aligned
MSW packet.  We search t=3 explicitly and t<=bound by a CP-SAT model on a
small closure of current-factor edges.  Owner degrees, facet colors, selected
portal rows, and optionally rank-(m+2) upper-current multiplicities are exact.
"""

from __future__ import annotations

import argparse
import collections
import itertools
import json

from ortools.sat.python import cp_model

import audit_msw_inverse_trade_portal_shadow_20260813 as base
import audit_pbbs_portal_compound_coexistence_20260813 as co
import cpsat_relative_incidence_trade_compound_seam_20260813 as global_cp
import search_relative_inverse_trade_for_compound_seam_20260813 as rel


def edge_union(edge):
    return frozenset().union(*edge)


def owner_incidence(old):
    ans = collections.defaultdict(list)
    for f, e in old.items():
        for v in e:
            ans[v].append((f, e))
    assert all(len(x) == 2 for x in ans.values())
    return ans


def protected_facets(m, d):
    ans = set()
    for row in rel.selected_portal_rows(m, d):
        owners = [co.cyc_window(row, t, m + 1) for t in range(2 * m + 1)]
        ans.update(owners[t] & owners[(t + 1) % (2 * m + 1)] for t in range(2 * m + 1))
    return ans


def explicit_t3(m, d, upper_exact):
    _, old, _, _ = global_cp.old_factor_data(m)
    inc = owner_incidence(old)
    frozen = protected_facets(m, d)
    C, U = co.c_owner(m, 4), co.height_owner(m, 5)
    F0 = C & U
    e0 = old[F0]
    assert frozenset((C, U)) != e0 and F0 not in frozen
    out = []
    for fc, ec in inc[C]:
        if fc in frozen or fc == F0:
            continue
        X = next(iter(ec - {C}))
        for fu, eu in inc[U]:
            if fu in frozen or fu in (F0, fc):
                continue
            Y = next(iter(eu - {U}))
            neg = {F0: e0, fc: ec, fu: eu}
            remaining = list(e0) + [X, Y]
            for perm in itertools.permutations(remaining):
                # Partition a permutation into the two labeled positive edges.
                pfc = frozenset((perm[0], perm[1]))
                pfu = frozenset((perm[2], perm[3]))
                if len(pfc) != 2 or len(pfu) != 2:
                    continue
                if not all(fc < v for v in pfc) or not all(fu < v for v in pfu):
                    continue
                pos = {F0: frozenset((C, U)), fc: pfc, fu: pfu}
                old_deg = collections.Counter(v for e in neg.values() for v in e)
                new_deg = collections.Counter(v for e in pos.values() for v in e)
                if old_deg != new_deg:
                    continue
                if upper_exact and collections.Counter(map(edge_union, neg.values())) != collections.Counter(map(edge_union, pos.values())):
                    continue
                rec = {
                    "negative": [
                        {"facet": sorted(f), "owners": [sorted(v) for v in e]}
                        for f, e in neg.items()
                    ],
                    "positive": [
                        {"facet": sorted(f), "owners": [sorted(v) for v in e]}
                        for f, e in pos.items()
                    ],
                }
                if rec not in out:
                    out.append(rec)
    return out


def closure_facets(m, d, radius):
    _, old, _, _ = global_cp.old_factor_data(m)
    inc = owner_incidence(old)
    C, U = co.c_owner(m, 4), co.height_owner(m, 5)
    F0 = C & U
    facets = {F0}
    owners = set(old[F0]) | {C, U}
    frontier = set(owners)
    for _ in range(radius):
        new_facets = {f for v in frontier for f, _ in inc[v]}
        facets |= new_facets
        next_owners = {v for f in new_facets for v in old[f]}
        frontier = next_owners - owners
        owners |= next_owners
    return facets


def cpsat_local(m, d, radius, upper_exact, max_changes, seconds, workers):
    _, old, _, _ = global_cp.old_factor_data(m)
    frozen = protected_facets(m, d)
    C, U = co.c_owner(m, 4), co.height_owner(m, 5)
    F0 = C & U
    desired = frozenset((C, U))
    facets = closure_facets(m, d, radius) - frozen
    facets.add(F0)
    owner_balance = collections.defaultdict(list)
    upper_balance = collections.defaultdict(list)
    changed = []
    vars_by_facet = {}
    model = cp_model.CpModel()
    ground = frozenset(range(2 * m + 1))
    for f in facets:
        outs = sorted(ground - f)
        terms = []
        for x, y in itertools.combinations(outs, 2):
            edge = frozenset((f | {x}, f | {y}))
            var = model.new_bool_var(f"x_{hash(f)}_{x}_{y}")
            terms.append((edge, var))
            sign = 0
            for v in edge:
                owner_balance[v].append(var)
            upper_balance[edge_union(edge)].append(var)
            if edge != old[f]:
                changed.append(var)
            if f == F0 and edge == desired:
                model.add(var == 1)
        model.add_exactly_one(v for _, v in terms)
        vars_by_facet[f] = terms
    model.add(sum(changed) <= max_changes)
    touched_owners = set(owner_balance)
    for v in touched_owners:
        old_degree_inside = sum(v in old[f] for f in facets)
        model.add(sum(owner_balance[v]) == old_degree_inside)
    if upper_exact:
        uppers = set(upper_balance) | {edge_union(old[f]) for f in facets}
        for u in uppers:
            old_count = sum(edge_union(old[f]) == u for f in facets)
            model.add(sum(upper_balance.get(u, ())) == old_count)
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = seconds
    solver.parameters.num_search_workers = workers
    status = solver.solve(model)
    out = {
        "status": solver.status_name(status),
        "m": m,
        "d": d,
        "radius": radius,
        "upper_exact": upper_exact,
        "max_changes": max_changes,
        "facets_in_closure": len(facets),
    }
    if status in (cp_model.FEASIBLE, cp_model.OPTIMAL):
        changes = []
        for f, terms in vars_by_facet.items():
            chosen = next(e for e, v in terms if solver.boolean_value(v))
            if chosen != old[f]:
                changes.append(
                    {
                        "facet": sorted(f),
                        "old_owners": [sorted(v) for v in old[f]],
                        "new_owners": [sorted(v) for v in chosen],
                        "old_upper": sorted(edge_union(old[f])),
                        "new_upper": sorted(edge_union(chosen)),
                    }
                )
        out["changed_facets"] = len(changes)
        out["changes"] = changes
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("m", type=int)
    ap.add_argument("d", type=int)
    ap.add_argument("--radius", type=int, default=4)
    ap.add_argument("--max-changes", type=int, default=12)
    ap.add_argument("--seconds", type=float, default=300)
    ap.add_argument("--workers", type=int, default=32)
    ap.add_argument("--no-upper-exact", action="store_true")
    ap.add_argument("--json")
    args = ap.parse_args()
    upper = not args.no_upper_exact
    out = {
        "t3": explicit_t3(args.m, args.d, upper),
        "local": cpsat_local(
            args.m, args.d, args.radius, upper, args.max_changes,
            args.seconds, args.workers,
        ),
    }
    payload = json.dumps(out, indent=2, sort_keys=True)
    print(payload)
    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            f.write(payload + "\n")


if __name__ == "__main__":
    main()
