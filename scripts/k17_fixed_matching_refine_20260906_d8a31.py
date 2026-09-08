#!/usr/bin/env python3
"""Isolated, bounded fixed-M0 CP-SAT refinement; never invokes a compiler.

Only P changes. U1 and positive residence >= 4 are hard; L2 is minimized or
required complete. U2, L3 and all-width upper decks are independently audited,
not constrained. UNKNOWN is not an infeasibility certificate. Search is h100-only.
"""

import argparse
from collections import Counter, defaultdict
from dataclasses import dataclass
from functools import cache
from hashlib import sha256
import json
import math
import os
from pathlib import Path
import shlex
import signal
import socket
import subprocess
import sys
import time
import traceback

from ortools.sat.python import cp_model
import ortools

K, N, W = 17, 1430, 24310
FULL = (1 << K) - 1
HEADER = "K17QF1 17 1430 24310 3"
RANKS = (10, 7, 11, 6)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def rotate(mask, shift):
    shift %= K
    return ((mask << shift) | (mask >> (K - shift))) & FULL


@cache
def canonical(mask):
    return min(rotate(mask, shift) for shift in range(K))


@cache
def representatives(rank):
    return frozenset(mask for mask in range(FULL + 1)
                     if mask.bit_count() == rank and canonical(mask) == mask)


def decode_factor(body, data):
    lines = body.decode("ascii").splitlines()
    require(len(lines) == N + 1 and lines[0] == HEADER, "body header/length")
    rows = sorted(tuple(map(int, line.split())) for line in lines[1:])
    require(all(len(row) == 3 for row in rows), "body triples")
    require([row[0] for row in rows] == sorted(representatives(8)), "canonical lower rows exactly once")
    require(tuple(data[key] for key in ("k", "r", "N", "W", "d")) == (17, 9, N, W, 3), "JSON header")
    choices = sorted([low, min(a, b), max(a, b)] for low, a, b in rows)
    require(sorted(data["choices"]) == choices, "body/JSON choices disagree")
    if "colored_choices" in data:
        require(data["colored_choices"] == [list(row) for row in rows], "colored JSON disagrees with body")
    return rows


def positive_runs(cycle, bit, positive=True):
    size = len(cycle)
    outside = next((i for i, mask in enumerate(cycle) if bool(mask & (1 << bit)) != positive), None)
    if outside is None:
        yield size
        return
    length = 0
    for step in range(1, size + 1):
        if bool(cycle[(outside + step) % size] & (1 << bit)) == positive:
            length += 1
        elif length:
            yield length
            length = 0


def physical_audit(rows):
    """Literal 24,310-owner audit, independent of descriptors and CP-SAT labels."""
    require(len(rows) == N and [row[0] for row in rows] == sorted(representatives(8)), "audit lower rows")
    adjacency = defaultdict(list)
    facets = Counter()
    colors = [set(), set()]
    for low, a, b in rows:
        require(0 <= a < K and 0 <= b < K and a != b and not low & ((1 << a) | (1 << b)),
                "valid distinct added coordinates")
        first, second = low | (1 << a), low | (1 << b)
        require(canonical(first) != canonical(second), "quotient loop")
        colors[0].add(canonical(first))
        colors[1].add(canonical(second))
        for shift in range(K):
            u, v = rotate(first, shift), rotate(second, shift)
            adjacency[u].append(v)
            adjacency[v].append(u)
            facets[u & v] += 1
    require(all(color == representatives(9) for color in colors), "each color is a perfect matching")
    require(len(adjacency) == W and all(mask.bit_count() == 9 and len(neighbors) == 2
                                      and neighbors[0] != neighbors[1]
                                      for mask, neighbors in adjacency.items()), "physical degree two")
    require(len(facets) == W and set(facets.values()) == {1}
            and all(mask.bit_count() == 8 for mask in facets), "physical facets exactly once")
    seen, cycles = set(), []
    for start in sorted(adjacency):
        if start in seen:
            continue
        previous, current = None, start
        cycle = []
        while current not in seen:
            seen.add(current)
            cycle.append(current)
            left, right = sorted(adjacency[current])
            require(previous is None or previous in (left, right), "physical predecessor")
            previous, current = current, left if previous is None or left != previous else right
        require(current == start and len(cycle) >= 3, "physical cycle closes simply")
        cycles.append(cycle)
    require(len(seen) == W, "physical owner coverage")
    cycles.sort(key=lambda cycle: (-len(cycle), cycle[0]))
    owner_component = {mask: i for i, cycle in enumerate(cycles) for mask in cycle}
    component_orbits = {frozenset(owner_component[rotate(cycle[0], shift)] for shift in range(K))
                        for cycle in cycles}
    require(all(len(orbit) in (1, K) for orbit in component_orbits), "physical component rotation orbits")

    loads = [Counter() for _ in RANKS]
    upper = defaultdict(set)
    positive, zero = Counter(), Counter()
    constant_three = 0
    for cycle in cycles:
        size = len(cycle)
        total, common = 0, FULL
        for mask in cycle:
            total |= mask
            common &= mask
        if size == 3:
            constant_three += common.bit_count()
        for bit in range(K):
            positive.update(positive_runs(cycle, bit))
            zero.update(positive_runs(cycle, bit, False))
        for i, a in enumerate(cycle):
            b, c, d = (cycle[(i + step) % size] for step in (1, 2, 3))
            for rank, mask, counts in zip(RANKS, (a | b, a & b & c, a | b | c, a & b & c & d), loads):
                if mask.bit_count() == rank:
                    counts[canonical(mask)] += 1
            union = a
            for age in range(1, size):
                old = union
                union |= cycle[(i + age) % size]
                if union != old and union.bit_count() > 9:
                    upper[union.bit_count()].add(canonical(union))
                if union == total:
                    break
    require(positive[1] == 0, "exact factor excludes positive runs of length one")
    require(all(value % K == 0 for counts in loads for value in counts.values()), "17-sheet shadow loads")
    require(all(value % K == 0 for value in (positive[2], positive[3], constant_three)), "17-sheet residence")
    missing = [sorted(representatives(rank) - counts.keys()) for rank, counts in zip(RANKS, loads)]
    upper_missing = {rank: sorted(representatives(rank) - upper[rank]) for rank in range(10, 18)}
    require(upper_missing[10] == missing[0] and upper_missing[11] == missing[2], "short/all-width upper agree")
    score = dict(bad2_orbits=positive[2] // K, bad3_orbits=positive[3] // K,
                 constant_bad3_orbits=constant_three // K,
                 residence_shortfall_orbits=(2 * positive[2] + positive[3]) // K,
                 missing_orbits=list(map(len, missing)),
                 pair_collisions=[sum((v // K) * (v // K - 1) // 2 for v in counts.values()) for counts in loads],
                 invalid_rank_starts=[N - sum(counts.values()) // K for counts in loads],
                 quotient_cycles=len(component_orbits), physical_cycles=len(cycles),
                 zero_voltage_cycles=sum(len(orbit) == K for orbit in component_orbits),
                 min_component=min(map(len, cycles)), max_component=max(map(len, cycles)), quotient_loops=0)
    physical = dict(degree2_owners=W, once_only_rank8_facets=W,
                    positive_bad_runs_by_length=[positive[i] for i in (1, 2, 3)],
                    residence_shortfall=2 * positive[2] + positive[3], minimum_positive_run=min(positive),
                    short_zero_gaps_not_forbidden=sum(zero[i] for i in (1, 2, 3)),
                    all_width_upper_missing_orbits_by_rank_10_to_17=[len(upper_missing[r]) for r in range(10, 18)],
                    physical_cycle_lengths=list(map(len, cycles)))
    carrier = not score["residence_shortfall_orbits"] and not any(missing) and not any(upper_missing.values())
    return dict(audit_method="independent_literal_physical_expansion", quotient_score=score,
                physical_audit=physical, missing_deck_orbit_representatives=missing,
                all_width_upper_missing_representatives=upper_missing,
                positive_run_histogram=dict(sorted(positive.items())),
                zero_gap_histogram_not_forbidden=dict(sorted(zero.items())),
                carrier_gates_pass=carrier, connectivity_pending=len(cycles) != 1,
                full_gates_pass=carrier and len(cycles) == 1, is_compiled_word=False)


def load_seed(body_path, json_path):
    body, raw_json = body_path.read_bytes(), json_path.read_bytes()
    data = json.loads(raw_json)
    rows = decode_factor(body, data)
    report = physical_audit(rows)
    require(data["quotient_score"] == report["quotient_score"], "seed quotient metrics fail independent audit")
    if "physical_audit" in data:
        require(data["physical_audit"] == report["physical_audit"], "seed physical metrics fail independent audit")
    q = report["quotient_score"]
    require(q["residence_shortfall_orbits"] == 0 and q["missing_orbits"][0] == 0, "seed must be resident/U1 complete")
    source = dict(body=str(body_path.resolve()), json=str(json_path.resolve()),
                  body_sha256=sha256(body).hexdigest(), json_sha256=sha256(raw_json).hexdigest())
    return rows, report, source


@dataclass(frozen=True, slots=True)
class Descriptor:
    lower: int
    added: int
    middle: int
    next: int
    shift: int
    ins: int
    delete: int
    umask: int
    lmask: int
    u1: int
    l2: int


class Catalogue:
    def __init__(self, rows):
        # This orbit/phase table is not used by the literal physical auditor.
        canon, phase = [-1] * (FULL + 1), [-1] * (FULL + 1)
        reps = [[] for _ in range(K + 1)]
        for mask in range(FULL + 1):
            if canon[mask] >= 0:
                continue
            reps[mask.bit_count()].append(mask)
            for shift in range(K):
                image = rotate(mask, shift)
                if canon[image] < 0:
                    canon[image], phase[image] = mask, shift
        require([len(reps[r]) for r in (7, 8, 9, 10)] == [1144, N, N, 1144], "central free-orbit counts")
        base_middle = [low | (1 << a) for low, a, _ in rows]
        base_inverse = {canon[mask]: l for l, mask in enumerate(base_middle)}
        require(len(base_inverse) == N, "frozen M0 perfect matching")
        self.rows, self.edges = rows, []
        self.by_lower = [[] for _ in rows]
        self.by_middle = {mask: [] for mask in reps[9]}
        self.u1 = {mask: [] for mask in reps[10]}
        self.l2 = {mask: [] for mask in reps[7]}
        self.seed_selection = [-1] * N
        self.excluded_parallel_loops = 0
        for l, (low, base_added, seed_added) in enumerate(rows):
            for added in range(K):
                if low & (1 << added) or added == base_added:
                    continue
                middle = low | (1 << added)
                if canon[middle] == canon[base_middle[l]]:
                    self.excluded_parallel_loops += 1
                    continue
                j = base_inverse[canon[middle]]
                shift = (phase[middle] - phase[base_middle[j]]) % K
                next_low = rotate(rows[j][0], shift)
                ins, delete = next_low & ~low, low & ~next_low
                umask, lmask = base_middle[l] | middle, low & next_low
                require(middle == rotate(base_middle[j], shift), "descriptor middle phase")
                require(ins.bit_count() == delete.bit_count() == 1, "descriptor Johnson step")
                require(umask.bit_count() == 10 and lmask.bit_count() == 7, "descriptor shadow ranks")
                e = len(self.edges)
                self.edges.append(Descriptor(l, added, canon[middle], j, shift,
                                             ins.bit_length() - 1, delete.bit_length() - 1,
                                             umask, lmask, canon[umask], canon[lmask]))
                self.by_lower[l].append(e)
                self.by_middle[canon[middle]].append(e)
                self.u1[canon[umask]].append(e)
                self.l2[canon[lmask]].append(e)
                if added == seed_added:
                    self.seed_selection[l] = e
        require(all(e >= 0 for e in self.seed_selection), "all seed P edges in model")


def phase_nogoods(cat):
    for e, a in enumerate(cat.edges):
        for f in cat.by_lower[a.next]:
            b = cat.edges[f]
            if a.ins == (b.delete + a.shift) % K:
                yield "bad2", (e, f)
            for g in cat.by_lower[b.next]:
                c = cat.edges[g]
                if a.ins == (c.delete + a.shift + b.shift) % K:
                    yield "bad3", (e, f, g)
                # Only voltage zero gives physical triangles. Nonzero lifts have
                # length 51 and must not be excluded merely for quotient length 3.
                if (c.next == a.lower and (a.shift + b.shift + c.shift) % K == 0
                        and a.lower < b.lower and a.lower < c.lower):
                    yield "zero_voltage_triangle", (e, f, g)


def build_model(cat, mode, initial_l2):
    started = time.monotonic()
    model = cp_model.CpModel()
    x = [model.new_bool_var(f"p_{a.lower}_{a.added}") for a in cat.edges]
    neg = [var.Not() for var in x]
    for edges in cat.by_lower:
        model.add_exactly_one(x[e] for e in edges)
    for edges in cat.by_middle.values():
        model.add_exactly_one(x[e] for e in edges)
    for edges in cat.u1.values():
        model.add_bool_or(x[e] for e in edges)
    selected = set(cat.seed_selection)
    clauses = Counter()
    for kind, edges in phase_nogoods(cat):
        model.add_bool_or(neg[e] for e in edges)
        clauses[kind] += 1
        require(not selected.issuperset(edges), "seed violates eager residence/triangle clause")
    missing = []
    for label, edges in cat.l2.items():
        miss = model.new_bool_var(f"l2_missing_{label}")
        # miss <=> no selected edge has this label, in BOTH directions.
        model.add_bool_or([miss] + [x[e] for e in edges])
        model.add_bool_and(neg[e] for e in edges).only_enforce_if(miss)
        model.add_hint(miss, int(not selected.intersection(edges)))
        missing.append(miss)
    for e, var in enumerate(x):
        model.add_hint(var, int(e in selected))
    if mode == "hard":
        model.add(sum(missing) == 0)
    else:
        model.add(sum(missing) <= initial_l2)
        model.minimize(sum(missing))
    require(sum(not selected.intersection(edges) for edges in cat.l2.values()) == initial_l2, "seed L2 vs model")
    require(all(selected.intersection(edges) for edges in cat.u1.values()), "seed U1 vs model")
    require(not model.validate(), "invalid CP-SAT model: " + model.validate())
    hints = model.proto.solution_hint
    require(len(hints.vars) == len(set(hints.vars)) == len(model.proto.variables), "complete unique hints")
    census = dict(mode=mode, incidence_edges=9 * N, fixed_m0_edges=N, candidate_edges=len(x),
                  excluded_parallel_quotient_loops=cat.excluded_parallel_loops,
                  candidate_degree_histogram=dict(sorted(Counter(map(len, cat.by_lower)).items())),
                  boolean_variables=len(model.proto.variables), missing_flags=len(missing),
                  constraints=len(model.proto.constraints), matching_exactly_one=2 * N,
                  u1_hard_covers=len(cat.u1), l2_labels=len(cat.l2), phase_nogoods=dict(clauses),
                  unavailable_u1_labels=[label for label, edges in cat.u1.items() if not edges],
                  unavailable_l2_labels=[label for label, edges in cat.l2.items() if not edges],
                  hinted_variables=len(hints.vars), hint_complete=True,
                  hint_feasible=(mode == "optimize" or initial_l2 == 0), initial_l2_missing=initial_l2,
                  build_seconds=time.monotonic() - started, ortools_version=ortools.__version__)
    return model, x, missing, census


def write_json(path, value):
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="ascii")
    temporary.replace(path)


def publish(directory, name, rows, seed_rows, source, initial_l2, expected_l2, mode):
    require([(l, a) for l, a, _ in rows] == [(l, a) for l, a, _ in seed_rows], "M0 columns changed")
    report = physical_audit(rows)
    q = report["quotient_score"]
    require(q["residence_shortfall_orbits"] == 0 and q["missing_orbits"][0] == 0, "independent resident/U1 gate failed")
    require(q["missing_orbits"][1] == expected_l2 <= initial_l2, "independent L2 objective mismatch/regression")
    body = (HEADER + "\n" + "".join(f"{low} {a} {b}\n" for low, a, b in rows)).encode("ascii")
    data = dict(schema="k17-fixed-matching-refine-d8a31-v1", k=K, r=9, d=3, N=N, W=W,
                deck_order=["U1", "L2", "U2", "L3"], quotient_score=q,
                physical_audit=report["physical_audit"], source=source, mode=mode,
                matching_columns=["M0", "P"], colored_choices=[list(row) for row in rows],
                choices=[[low, min(a, b), max(a, b)] for low, a, b in rows],
                is_compiled_word=False, solver_feasible_for_mode=(mode == "optimize" or expected_l2 == 0))
    raw_json = (json.dumps(data, indent=2, sort_keys=True) + "\n").encode("ascii")
    require(decode_factor(body, json.loads(raw_json)) == rows, "serialization round trip")
    paths = {kind: str(directory / (name + suffix)) for kind, suffix in
             (("body", ".txt"), ("json", ".json"), ("audit", ".audit.json"))}
    require(not any(Path(path).exists() for path in paths.values()), "immutable candidate already exists")
    report.update(body_sha256=sha256(body).hexdigest(), json_sha256=sha256(raw_json).hexdigest(),
                  m0_preserved=True, source=source, status="EXACT_FACTOR_AUDIT_PASS")
    # The manifest is replaced last. Readers only see fully audited immutable triples.
    Path(paths["body"]).write_bytes(body)
    Path(paths["json"]).write_bytes(raw_json)
    write_json(Path(paths["audit"]), report)
    best = dict(paths=paths, body_sha256=report["body_sha256"], json_sha256=report["json_sha256"],
                quotient_score=q, full_gates_pass=report["full_gates_pass"],
                solver_feasible_for_mode=data["solver_feasible_for_mode"], baseline_only=name == "initial")
    write_json(directory / "best.manifest.json", best)
    print(json.dumps(dict(event="AUDITED_CANDIDATE", name=name, **best)), flush=True)
    return best


def run(args):
    # Bound the entire owned process as well as CP-SAT. A watchdog exit is not UNSAT;
    # the last published manifest remains valid even without a terminal result.json.
    signal.alarm(math.ceil(args.seconds + 120))
    started = time.monotonic()
    rows, seed_report, source = load_seed(args.seed_body, args.seed_json)
    args.directory.mkdir(exist_ok=False)
    initial_l2 = seed_report["quotient_score"]["missing_orbits"][1]
    best = publish(args.directory, "initial", rows, rows, source, initial_l2, initial_l2, args.mode)
    cat = Catalogue(rows)
    model, x, missing, census = build_model(cat, args.mode, initial_l2)
    census.update(source=source, pid=os.getpid(), seconds=args.seconds, workers=args.workers,
                  random_seed=args.random_seed, watchdog_seconds=math.ceil(args.seconds + 120))
    write_json(args.directory / "model_census.json", census)
    print(json.dumps(dict(event="MODEL_CENSUS", **census)), flush=True)
    if args.check_only:
        write_json(args.directory / "result.json", dict(status="MODEL_BUILT_ONLY", best_audited=best, census=census))
        return

    class Incumbent(cp_model.CpSolverSolutionCallback):
        def __init__(self):
            super().__init__()
            self.best = best
            self.best_l2 = initial_l2
            self.solutions = 0
            self.improvements = 0
            self.error = None

        def on_solution_callback(self):
            try:
                self.solutions += 1
                l2 = sum(self.value(var) for var in missing)
                if l2 >= self.best_l2:
                    return
                candidate = []
                for l, edges in enumerate(cat.by_lower):
                    chosen = [e for e in edges if self.boolean_value(x[e])]
                    require(len(chosen) == 1, "solver row degree")
                    candidate.append((rows[l][0], rows[l][1], cat.edges[chosen[0]].added))
                self.improvements += 1
                self.best = publish(args.directory, f"candidate{self.improvements:04d}_l2_{l2:04d}",
                                    candidate, rows, source, initial_l2, l2, args.mode)
                self.best_l2 = l2
            except Exception:
                self.error = traceback.format_exc()
                self.stop_search()

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = args.seconds
    solver.parameters.num_search_workers = args.workers
    solver.parameters.random_seed = args.random_seed
    solver.parameters.log_search_progress = True
    callback = Incumbent()
    status = solver.solve(model, callback)
    has_solution = status in (cp_model.FEASIBLE, cp_model.OPTIMAL)
    result = dict(status=solver.status_name(status), scope="fixed M0; resident and U1 hard; L2 " + args.mode,
                  has_solver_solution=has_solution, solver_solutions=callback.solutions,
                  audited_improvements=callback.improvements, best_audited=callback.best,
                  l2_improvement=initial_l2 - callback.best_l2,
                  objective=(solver.objective_value if has_solution and args.mode == "optimize" else None),
                  best_objective_bound=(solver.best_objective_bound if args.mode == "optimize" else None),
                  solver_wall_seconds=solver.wall_time, total_wall_seconds=time.monotonic() - started,
                  workers=args.workers, requested_solver_seconds=args.seconds, source=source,
                  response_stats=solver.response_stats(), is_compiled_word=False)
    if callback.error or status == cp_model.MODEL_INVALID or (status == cp_model.INFEASIBLE and args.mode == "optimize"):
        result.update(status="FAIL_CLOSED", error=callback.error or "invalid model or infeasible known-feasible model")
    if status == cp_model.UNKNOWN:
        result["interpretation"] = "No solver solution/proof in this budget; not an UNSAT claim. Baseline remains audited."
    elif status == cp_model.INFEASIBLE and args.mode == "hard":
        result["interpretation"] = "Only this fixed-M0 resident/U1/hard-L2 model is infeasible; no unrestricted claim."
    write_json(args.directory / "result.json", result)
    print(json.dumps(dict(event="FINISH", **result)), flush=True)
    signal.alarm(0)
    require(result["status"] != "FAIL_CLOSED", str(result.get("error")))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed-body", type=Path, required=True)
    parser.add_argument("--seed-json", type=Path)
    parser.add_argument("--directory", type=Path)
    parser.add_argument("--seconds", type=float, default=600)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--mode", choices=("optimize", "hard"), default="optimize")
    parser.add_argument("--random-seed", type=int, default=17090631)
    actions = parser.add_mutually_exclusive_group()
    actions.add_argument("--detach", action="store_true", help="launch one detached bounded run and return its PID")
    actions.add_argument("--check-only", action="store_true", help="audit seed and build/census without solving")
    actions.add_argument("--audit-only", action="store_true", help="read-only independent audit; no output files")
    args = parser.parse_args()
    if not math.isfinite(args.seconds) or not 0 < args.seconds <= 600 or not 1 <= args.workers <= 8:
        parser.error("seconds must be in (0,600] and workers in 1..8")
    if socket.gethostname().split(".")[0].lower() not in ("h100", "arboghast"):
        parser.error("model construction, audits and search are restricted to h100")
    args.seed_body = args.seed_body.resolve(strict=True)
    args.seed_json = (args.seed_json or args.seed_body.with_suffix(".json")).resolve(strict=True)
    if args.audit_only:
        _, report, source = load_seed(args.seed_body, args.seed_json)
        print(json.dumps(dict(source=source, **report), sort_keys=True), flush=True)
        return
    if args.directory is None:
        parser.error("--directory is required except for --audit-only")
    args.directory = args.directory.resolve()
    require(args.directory.parent.is_dir() and not args.directory.exists(), "new output directory needs an existing parent")
    if not args.detach:
        run(args)
        return
    args.directory.mkdir(exist_ok=False)
    command = [sys.executable, "-u", str(Path(__file__).resolve()), "--seed-body", str(args.seed_body),
               "--seed-json", str(args.seed_json), "--directory", str(args.directory / "search"),
               "--seconds", str(args.seconds), "--workers", str(args.workers), "--mode", args.mode,
               "--random-seed", str(args.random_seed)]
    env = dict(os.environ, OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1", MKL_NUM_THREADS="1",
               NUMEXPR_NUM_THREADS="1", PYTHONDONTWRITEBYTECODE="1")
    with (args.directory / "driver.log").open("x") as log:
        process = subprocess.Popen(command, cwd=args.directory, stdin=subprocess.DEVNULL, stdout=log,
                                   stderr=subprocess.STDOUT, start_new_session=True, env=env)
    manifest = dict(pid=process.pid, host=socket.gethostname(), directory=str(args.directory),
                    command=command, shell_command=shlex.join(command), seconds=args.seconds,
                    workers=args.workers, watchdog_seconds=math.ceil(args.seconds + 120), launched_unix=time.time())
    write_json(args.directory / "launch.json", manifest)
    print(json.dumps(manifest, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
