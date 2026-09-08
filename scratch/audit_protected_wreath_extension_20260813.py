#!/usr/bin/env python3
"""Symmetry-reduced exact-cover audit for prescribed tight wreath rows.

Run substantive instances only on the H100 host.  A wreath is an unoriented
cyclic order on n=2m+1 points and covers its n cyclic m-windows.  We test
whether pairwise window-disjoint prescribed wreaths extend to a factor of all
m-subsets.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import random
import time
from collections import Counter, defaultdict

from ortools.sat.python import cp_model


def canonical_cycle(seq):
    """Canonical tuple modulo cyclic rotation and reversal."""
    seq = tuple(seq)
    n = len(seq)
    rots = [seq[i:] + seq[:i] for i in range(n)]
    rev = tuple(reversed(seq))
    rots.extend(rev[i:] + rev[:i] for i in range(n))
    return min(rots)


def all_wreaths(n):
    """All unoriented cyclic orders, represented with 0 first."""
    out = []
    for tail in itertools.permutations(range(1, n)):
        if tail[0] < tail[-1]:
            out.append((0,) + tail)
    return out


def permute_cycle(cyc, p):
    return canonical_cycle(tuple(p[x] for x in cyc))


def dihedral_group(n):
    out = []
    for a in range(n):
        out.append(tuple((x + a) % n for x in range(n)))
        out.append(tuple((a - x) % n for x in range(n)))
    return sorted(set(out))


def build_instance(m):
    n = 2 * m + 1
    vertices = list(itertools.combinations(range(n), m))
    vi = {s: i for i, s in enumerate(vertices)}
    cycles = all_wreaths(n)
    masks = []
    windows = []
    for cyc in cycles:
        ws = []
        mask = 0
        for j in range(n):
            s = tuple(sorted(cyc[(j + a) % n] for a in range(m)))
            idx = vi[s]
            ws.append(idx)
            mask |= 1 << idx
        assert len(set(ws)) == n
        windows.append(tuple(sorted(ws)))
        masks.append(mask)
    ci = {c: i for i, c in enumerate(cycles)}
    by_vertex = [[] for _ in vertices]
    for w, ws in enumerate(windows):
        for v in ws:
            by_vertex[v].append(w)
    return {
        "m": m,
        "n": n,
        "vertices": vertices,
        "cycles": cycles,
        "ci": ci,
        "masks": masks,
        "windows": windows,
        "by_vertex": by_vertex,
    }


def orbit_key_tuple(inst, ids, group):
    cycles = inst["cycles"]
    ci = inst["ci"]
    images = []
    for p in group:
        images.append(tuple(sorted(ci[permute_cycle(cycles[w], p)] for w in ids)))
    return min(images)


def exact_cover(inst, forced, time_limit=30.0, workers=1):
    masks = inst["masks"]
    forced_mask = 0
    for w in forced:
        if forced_mask & masks[w]:
            return False, None, "OVERLAP", 0.0
        forced_mask |= masks[w]
    full_mask = (1 << len(inst["vertices"])) - 1
    rem_mask = full_mask ^ forced_mask
    eligible = [w for w, mask in enumerate(masks) if not (mask & forced_mask)]
    model = cp_model.CpModel()
    x = {w: model.new_bool_var(f"x{w}") for w in eligible}
    for v in range(len(inst["vertices"])):
        if (rem_mask >> v) & 1:
            ws = [w for w in inst["by_vertex"][v] if w in x]
            if not ws:
                return False, None, "EMPTY_ROW", 0.0
            model.add_exactly_one(x[w] for w in ws)
    need = math.comb(inst["n"], inst["m"]) // inst["n"] - len(forced)
    model.add(sum(x.values()) == need)
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = time_limit
    solver.parameters.num_search_workers = workers
    solver.parameters.random_seed = 1729
    t0 = time.time()
    status = solver.solve(model)
    elapsed = time.time() - t0
    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        sol = tuple(sorted(tuple(forced) + tuple(w for w in eligible if solver.value(x[w]))))
        return True, sol, solver.status_name(status), elapsed
    return False, None, solver.status_name(status), elapsed


def dfs_exact_cover(inst, forced, limit=None):
    """Enumerate factors extending forced rows (intended for m<=3)."""
    masks = inst["masks"]
    forced_mask = 0
    for w in forced:
        if forced_mask & masks[w]:
            return []
        forced_mask |= masks[w]
    full_mask = (1 << len(inst["vertices"])) - 1
    solutions = []
    need = math.comb(inst["n"], inst["m"]) // inst["n"]

    def rec(covered, chosen):
        if limit is not None and len(solutions) >= limit:
            return
        if covered == full_mask:
            if len(chosen) == need:
                solutions.append(tuple(chosen))
            return
        if len(chosen) >= need:
            return
        best = None
        opts_best = None
        missing = full_mask ^ covered
        while missing:
            bit = missing & -missing
            v = bit.bit_length() - 1
            opts = [w for w in inst["by_vertex"][v] if not (masks[w] & covered)]
            if not opts:
                return
            if opts_best is None or len(opts) < len(opts_best):
                best, opts_best = v, opts
                if len(opts) == 1:
                    break
            missing ^= bit
        for w in opts_best:
            rec(covered | masks[w], chosen + [w])

    rec(forced_mask, list(forced))
    return solutions


def audit(m, max_triples, sample_triples, skip_triples, time_limit, workers, seed):
    rng = random.Random(seed)
    t0 = time.time()
    inst = build_instance(m)
    n = inst["n"]
    canonical = inst["ci"][tuple(range(n))]
    c_mask = inst["masks"][canonical]
    compatible = [w for w, z in enumerate(inst["masks"]) if w != canonical and not (z & c_mask)]
    group = dihedral_group(n)

    pair_orbits = {}
    for w in compatible:
        key = orbit_key_tuple(inst, (canonical, w), group)
        pair_orbits.setdefault(key, w)

    pair_results = []
    for num, (key, w) in enumerate(sorted(pair_orbits.items())):
        ok, sol, status, sec = exact_cover(inst, (canonical, w), time_limit, workers)
        pair_results.append({
            "orbit_key": list(key), "representative": w, "extendable": ok,
            "status": status, "seconds": sec, "completion": list(sol) if sol else None,
        })

    triple_candidates = []
    if not skip_triples:
        for ai, a in enumerate(compatible):
            am = inst["masks"][a]
            for b in compatible[ai + 1:]:
                if not (am & inst["masks"][b]):
                    triple_candidates.append((a, b))

    # Exact simultaneous orbit classification is affordable at m=3.  At m=4
    # retain either the requested prefix or a deterministic random sample.
    triple_orbits = {}
    triples_to_scan = triple_candidates
    if max_triples is not None and len(triples_to_scan) > max_triples:
        triples_to_scan = triples_to_scan[:max_triples]
    if sample_triples and len(triple_candidates) > sample_triples:
        triples_to_scan = rng.sample(triple_candidates, sample_triples)
    for a, b in triples_to_scan:
        key = orbit_key_tuple(inst, (canonical, a, b), group)
        triple_orbits.setdefault(key, (a, b))

    triple_results = []
    for key, (a, b) in sorted(triple_orbits.items()):
        ok, sol, status, sec = exact_cover(inst, (canonical, a, b), time_limit, workers)
        triple_results.append({
            "orbit_key": list(key), "representative": [a, b], "extendable": ok,
            "status": status, "seconds": sec, "completion": list(sol) if sol else None,
        })

    pairwise_extendable_but_triple_not = []
    if m <= 3:
        pair_cache = {}
        for rec in triple_results:
            if rec["extendable"] or rec["status"] == "UNKNOWN":
                continue
            a, b = rec["representative"]
            pairs = ((canonical, a), (canonical, b), (a, b))
            oks = []
            for pair in pairs:
                key = tuple(sorted(pair))
                if key not in pair_cache:
                    pair_cache[key] = exact_cover(
                        inst, key, time_limit, workers)[0]
                oks.append(pair_cache[key])
            if all(oks):
                pairwise_extendable_but_triple_not.append(rec["orbit_key"])

    factors = None
    if m <= 3:
        fs = dfs_exact_cover(inst, (canonical,))
        factors = {
            "count_containing_canonical": len(fs),
            "sample": [list(x) for x in fs[:20]],
        }

    return {
        "parameters": {"m": m, "n": n, "factor_rows": math.comb(n, m) // n},
        "counts": {
            "vertices": len(inst["vertices"]),
            "wreaths": len(inst["cycles"]),
            "compatible_with_canonical": len(compatible),
            "pair_orbits": len(pair_orbits),
            "pair_nonextendable": sum(not x["extendable"] for x in pair_results),
            "pair_unknown": sum(x["status"] == "UNKNOWN" for x in pair_results),
            "pairwise_disjoint_candidate_pairs_for_triples": len(triple_candidates),
            "triple_orbits_tested": len(triple_orbits),
            "triple_nonextendable": sum(not x["extendable"] and x["status"] != "UNKNOWN" for x in triple_results),
            "triple_unknown": sum(x["status"] == "UNKNOWN" for x in triple_results),
            "pairwise_extendable_but_triple_nonextendable":
                len(pairwise_extendable_but_triple_not),
        },
        "canonical_cycle": list(range(n)),
        "pair_results": pair_results,
        "triple_results": triple_results,
        "pairwise_extendable_but_triple_nonextendable_orbits":
            pairwise_extendable_but_triple_not,
        "factors": factors,
        "elapsed_seconds": time.time() - t0,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--m", type=int, required=True)
    ap.add_argument("--max-triples", type=int)
    ap.add_argument("--sample-triples", type=int, default=0)
    ap.add_argument("--skip-triples", action="store_true")
    ap.add_argument("--time-limit", type=float, default=30.0)
    ap.add_argument("--workers", type=int, default=1)
    ap.add_argument("--seed", type=int, default=1729)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    ans = audit(args.m, args.max_triples, args.sample_triples, args.skip_triples,
                args.time_limit, args.workers, args.seed)
    with open(args.output, "w") as f:
        json.dump(ans, f, indent=2, sort_keys=True)
        f.write("\n")
    print(json.dumps(ans["counts"], sort_keys=True))
    print(f"elapsed_seconds={ans['elapsed_seconds']:.3f}")


if __name__ == "__main__":
    main()
