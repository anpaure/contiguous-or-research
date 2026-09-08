#!/usr/bin/env python3
"""Portfolio of k-nondihedral + (35-k)-strong reflection faces.

Run only on H100.  For each k=0,...,8, sample four masks of the eight
pairwise-disjoint new nondihedral fixed edges (repeating the unique masks
at k=0,8 but using distinct strong completions).  Delete their endpoints,
find an exact strong distance-two matching on the remaining fixed rows,
build the literal 680-row owner instance, and run a short stochastic search.
"""

from __future__ import annotations

import argparse
import itertools
import json
import random
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

import networkx as nx

sys.path.insert(0, "scratch")
from build_q4_k17_z17_reflection_hybrid8_nondihedral_face_20260814 import (
    multiplied_candidate,
)
from search_q4_k17_z17_quotient_exact_cover_20260814 import (
    K,
    owner_orbits,
)
from search_q4_k17_z17_reflection_invariant_owner_cover_20260814 import (
    enumerate_strong_self_columns,
    paired_columns,
    reflection_action,
)


def write_instance(path, groups, pair_options):
    self_options = []
    for group, record in enumerate(groups):
        for candidate, rows in record["options"]:
            self_options.append((group, candidate, rows))
    with open(path, "w", encoding="ascii") as stream:
        stream.write(f"680 35 {len(self_options)} {len(pair_options)}\n")
        for group, _, rows in self_options:
            stream.write(" ".join(map(str, (group,) + rows)) + "\n")
        for _, rows in pair_options:
            stream.write(" ".join(map(str, rows)) + "\n")
    return self_options


def sample_masks(rng):
    result = []
    for size in range(9):
        masks = list(itertools.combinations(range(8), size))
        if len(masks) >= 4:
            chosen = rng.sample(masks, 4)
        else:
            chosen = [masks[0]] * 4
        result.extend((size, tuple(mask), replicate)
                      for replicate, mask in enumerate(chosen))
    assert len(result) == 36
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--map", required=True)
    parser.add_argument("--primary", required=True)
    parser.add_argument("--audit", required=True)
    parser.add_argument("--energy-binary", required=True)
    parser.add_argument("--workdir", required=True)
    parser.add_argument("--report", required=True)
    parser.add_argument("--seconds", type=float, default=10)
    parser.add_argument("--threads", type=int, default=32)
    parser.add_argument("--seed", type=int, default=20260814)
    args = parser.parse_args()
    rng = random.Random(args.seed)
    workdir = Path(args.workdir)
    workdir.mkdir(parents=True, exist_ok=True)

    pool = json.load(open(args.map, encoding="utf-8"))
    primary = json.load(open(args.primary, encoding="utf-8"))
    audit = json.load(open(args.audit, encoding="utf-8"))
    representatives, orbit_index = owner_orbits()
    reflection = reflection_action(representatives, orbit_index)
    fixed = {vertex for vertex in range(1430)
             if reflection[vertex] == vertex}
    nonfixed_representatives = sorted(
        vertex for vertex in range(1430) if vertex < reflection[vertex]
    )
    nonfixed_index = {}
    for index, vertex in enumerate(nonfixed_representatives):
        nonfixed_index[vertex] = index
        nonfixed_index[reflection[vertex]] = index

    nondihedral_by_deck = {}
    for row in primary["examples"]:
        for multiplier in range(1, K):
            candidate = multiplied_candidate(row, multiplier, orbit_index)
            nondihedral_by_deck.setdefault(candidate["edge"], candidate)
    assert len(nondihedral_by_deck) == 8
    nondihedral = {}
    for candidate in nondihedral_by_deck.values():
        signature = tuple(sorted(set(candidate["edge"]) & fixed))
        rows = tuple(sorted({nonfixed_index[vertex]
                             for vertex in candidate["edge"]
                             if vertex not in fixed}))
        assert len(signature) == 2 and len(rows) == 4
        nondihedral[signature] = (candidate, rows)
    new_edges = tuple(sorted(nondihedral))
    expected = {
        tuple(edge) for edge in
        audit["new_fixed_face_completion"]["new_nondihedral_edges"]
    }
    assert set(new_edges) == expected

    strong_candidates, raw, simple = enumerate_strong_self_columns(
        orbit_index, reflection
    )
    strong_lifts = defaultdict(list)
    for candidate in strong_candidates:
        signature = tuple(sorted(set(candidate["edge"]) & fixed))
        rows = tuple(sorted({nonfixed_index[vertex]
                             for vertex in candidate["edge"]
                             if vertex not in fixed}))
        assert len(signature) == 2 and len(rows) == 4
        strong_lifts[signature].append((candidate, rows))
    assert len(strong_lifts) == 1260

    pair_options = []
    pair_indices, pool_self = paired_columns(pool["candidates"], reflection)
    assert not pool_self and len(pair_indices) == 27008
    for left, right in pair_indices:
        columns = [pool["candidates"][left], pool["candidates"][right]]
        union = set(columns[0]["edge"]) | set(columns[1]["edge"])
        rows = tuple(sorted({nonfixed_index[vertex] for vertex in union}))
        assert len(union) == 20 and len(rows) == 10
        pair_options.append((columns, rows))

    faces = []
    seen_completions = defaultdict(set)
    for face_index, (size, mask, replicate) in enumerate(sample_masks(rng)):
        chosen_new = tuple(new_edges[index] for index in mask)
        removed = {vertex for edge in chosen_new for vertex in edge}
        graph = nx.Graph()
        graph.add_nodes_from(fixed - removed)
        graph.add_edges_from(edge for edge in strong_lifts
                             if not (set(edge) & removed))
        completion = None
        for attempt in range(100):
            local_rng = random.Random(
                args.seed + 10007 * face_index + 1000003 * attempt
            )
            for left, right in graph.edges:
                graph[left][right]["weight"] = local_rng.random()
            raw_matching = nx.max_weight_matching(
                graph, maxcardinality=True, weight="weight"
            )
            candidate_completion = tuple(sorted(
                tuple(sorted(edge)) for edge in raw_matching
            ))
            if len(candidate_completion) != 35 - size:
                continue
            key = tuple(sorted(chosen_new))
            if candidate_completion not in seen_completions[key]:
                seen_completions[key].add(candidate_completion)
                completion = candidate_completion
                break
        assert completion is not None
        combined = set(chosen_new) | set(completion)
        assert len(combined) == 35
        assert len({vertex for edge in combined for vertex in edge}) == 70

        groups = []
        for signature in sorted(chosen_new):
            groups.append({
                "kind": "nondihedral", "signature": signature,
                "options": [nondihedral[signature]],
            })
        for signature in completion:
            groups.append({
                "kind": "strong", "signature": signature,
                "options": strong_lifts[signature],
            })
        assert len(groups) == 35
        stem = f"face_{face_index:02d}_k{size}_r{replicate}"
        instance = workdir / f"{stem}.dat"
        state = workdir / f"{stem}.solution.json"
        progress = workdir / f"{stem}.progress"
        stdout = workdir / f"{stem}.out"
        self_options = write_instance(instance, groups, pair_options)
        with open(stdout, "w", encoding="ascii") as out_stream, open(
            progress, "w", encoding="ascii"
        ) as error_stream:
            completed = subprocess.run([
                args.energy_binary, str(instance), str(state),
                str(args.seconds), str(args.threads),
                str((args.seed + face_index) % (2**63 - 1)),
            ], stdout=out_stream, stderr=error_stream, check=False)
        assert completed.returncode in (0, 1)
        result = json.load(open(state, encoding="utf-8"))
        record = {
            "face": face_index,
            "k": size,
            "replicate": replicate,
            "new_edge_indices": list(mask),
            "new_edges": [list(edge) for edge in chosen_new],
            "strong_completion": [list(edge) for edge in completion],
            "matching": [list(edge) for edge in sorted(combined)],
            "self_options": len(self_options),
            "pair_options": len(pair_options),
            "energy": result["energy"],
            "status": result["status"],
            "lower_unit_c4_bound": 35 - size,
            "instance": str(instance),
            "state": str(state),
            "progress": str(progress),
        }
        faces.append(record)
        print(json.dumps({
            "face": face_index, "k": size, "energy": result["energy"],
            "self_options": len(self_options),
        }, sort_keys=True), file=sys.stderr, flush=True)
        if result["energy"] == 0:
            break

    pareto = []
    for record in faces:
        dominated = any(
            other["energy"] <= record["energy"]
            and other["k"] >= record["k"]
            and (other["energy"] < record["energy"]
                 or other["k"] > record["k"])
            for other in faces
        )
        if not dominated:
            pareto.append(record["face"])
    top_three = [record["face"] for record in sorted(
        faces, key=lambda record: (record["energy"], -record["k"],
                                   record["face"])
    )[:3]]
    report = {
        "status": "PASS" if any(face["energy"] == 0 for face in faces)
                  else "NO_CERTIFICATE_IN_CAPPED_PORTFOLIO",
        "faces_requested": 36,
        "faces_completed": len(faces),
        "seconds_per_face": args.seconds,
        "threads": args.threads,
        "strong_raw_orders": raw,
        "strong_quotient_simple_orders": simple,
        "new_nondihedral_edges": [list(edge) for edge in new_edges],
        "top_three_faces": top_three,
        "pareto_faces": pareto,
        "faces": faces,
    }
    Path(args.report).write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="ascii"
    )
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
