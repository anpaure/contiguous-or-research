#!/usr/bin/env python3
"""Run the prior best k=0..8 owner faces against a larger pair pool."""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import subprocess
import sys
import time
from collections import Counter
from pathlib import Path

sys.path.insert(0, "scratch")
from search_q4_k17_z17_reflection_fixed_face_kissat_20260814 import read_instance


def digest_rows(options) -> str:
    payload = "\n".join(" ".join(map(str, rows)) for rows in options) + "\n"
    return hashlib.sha256(payload.encode("ascii")).hexdigest()


def write_instance(path, self_options, pair_options) -> None:
    with open(path, "w", encoding="ascii") as stream:
        stream.write(f"680 35 {len(self_options)} {len(pair_options)}\n")
        for group, rows in self_options:
            stream.write(" ".join(map(str, (group,) + tuple(rows))) + "\n")
        for rows in pair_options:
            stream.write(" ".join(map(str, rows)) + "\n")


def replay(self_options, pair_options, state):
    chosen_self = tuple(state["self_indices"])
    chosen_pairs = tuple(state["pair_indices"])
    if len(chosen_self) != 35 or len(chosen_pairs) != 54:
        raise ValueError("selection cardinality mismatch")
    groups = [self_options[index][0] for index in chosen_self]
    if len(set(groups)) != 35:
        raise ValueError("self-group one-hot mismatch")
    loads = [0] * 680
    for index in chosen_self:
        for row in self_options[index][1]:
            loads[row] += 1
    for index in chosen_pairs:
        for row in pair_options[index]:
            loads[row] += 1
    energy = sum((load - 1) ** 2 for load in loads)
    if energy != state["energy"]:
        raise ValueError(f"energy replay mismatch {energy} != {state['energy']}")
    histogram = Counter(loads)
    return {
        "energy": energy,
        "load_histogram": {str(key): value
                           for key, value in sorted(histogram.items())},
        "holes": histogram[0],
        "doubles": histogram[2],
        "selected_self": len(chosen_self),
        "selected_pairs": len(chosen_pairs),
        "selected_self_groups": len(set(groups)),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prior-report", required=True)
    parser.add_argument("--pair-instance", required=True)
    parser.add_argument("--tabu-binary", required=True)
    parser.add_argument("--workdir", required=True)
    parser.add_argument("--report", required=True)
    parser.add_argument("--seconds", type=float, default=30.0)
    parser.add_argument("--threads", type=int, default=8)
    parser.add_argument("--parallel", type=int, default=3)
    parser.add_argument("--seed", type=int, default=20260814)
    args = parser.parse_args()
    started = time.time()
    workdir = Path(args.workdir)
    workdir.mkdir(parents=True, exist_ok=True)

    prior = json.loads(Path(args.prior_report).read_text())
    _, _, _, global_pairs = read_instance(args.pair_instance)
    best = []
    for k in range(9):
        candidates = [record for record in prior["faces"] if record["k"] == k]
        best.append(min(candidates, key=lambda record:
                        (record["energy"], record["face"])))

    jobs = []
    for record in best:
        _, _, self_options, old_pairs = read_instance(record["instance"])
        if tuple(old_pairs) != tuple(global_pairs[:len(old_pairs)]):
            raise ValueError(f"frozen pair prefix mismatch at k={record['k']}")
        stem = f"best_k{record['k']}_source_face{record['face']:02d}"
        instance = workdir / f"{stem}.dat"
        state = workdir / f"{stem}.solution.json"
        stdout = workdir / f"{stem}.out"
        progress = workdir / f"{stem}.progress"
        metadata = workdir / f"{stem}.self_metadata.json"
        write_instance(instance, self_options, global_pairs)
        Path(metadata).write_text(json.dumps({
            "k": record["k"],
            "source_face_record": record,
            "source_instance": record["instance"],
            "source_state": record["state"],
            "matching": record["matching"],
            "new_edges": record["new_edges"],
            "strong_completion": record["strong_completion"],
            "self_option_count": len(self_options),
            "self_option_rows_sha256": digest_rows(
                [rows for _, rows in self_options]),
            "witness_reconstruction_sources": {
                "builder": "scratch/search_q4_k17_z17_reflection_nondihedral_subset_portfolio_20260814.py",
                "map": "/dev/shm/q4z17_group100k.map.json",
                "primary": "scratch/search_q4_k17_nondihedral_self_fixed_lower_20260814.h100.out",
                "audit": "scratch/audit_q4_k17_nondihedral_self_fixed_lower_20260814.h100.out",
            },
        }, indent=2, sort_keys=True) + "\n")
        seed_state = json.loads(Path(record["state"]).read_text())
        seed_replay = replay(self_options, global_pairs, seed_state)
        jobs.append({
            "k": record["k"], "source_face": record["face"],
            "source_record": record, "self_options_data": self_options,
            "instance": str(instance), "seed_state": record["state"],
            "state": str(state), "stdout": str(stdout),
            "progress": str(progress), "metadata": str(metadata),
            "self_options": len(self_options), "seed_replay": seed_replay,
        })

    def run(job):
        with open(job["stdout"], "w", encoding="ascii") as out, open(
            job["progress"], "w", encoding="ascii"
        ) as err:
            completed = subprocess.run([
                args.tabu_binary, job["instance"], job["seed_state"],
                job["state"], str(args.seconds), str(args.threads),
                str((args.seed + job["k"]) % (2**63 - 1)),
            ], stdout=out, stderr=err, check=False)
        if completed.returncode not in (0, 1):
            raise RuntimeError(f"tabu failed for k={job['k']}: {completed.returncode}")
        state = json.loads(Path(job["state"]).read_text())
        replay_result = replay(job["self_options_data"], global_pairs, state)
        return {
            key: value for key, value in job.items()
            if key != "self_options_data"
        } | {"result_status": state["status"], "replay": replay_result}

    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.parallel) as pool:
        future_to_k = {pool.submit(run, job): job["k"] for job in jobs}
        for future in concurrent.futures.as_completed(future_to_k):
            result = future.result()
            results.append(result)
            print(json.dumps({
                "k": result["k"], "energy": result["replay"]["energy"],
                "holes": result["replay"]["holes"],
            }, sort_keys=True), file=sys.stderr, flush=True)
    results.sort(key=lambda result: result["k"])
    winner = min(results, key=lambda result:
                 (result["replay"]["energy"], result["k"]))
    report = {
        "status": "PASS" if winner["replay"]["energy"] == 0
                  else "NO_CERTIFICATE_IN_CAPPED_BESTK_PORTFOLIO",
        "scope": "one prior-best literal owner face for each k=0..8, tabu cap",
        "pair_instance": args.pair_instance,
        "pair_options": len(global_pairs),
        "frozen_prefix_options": len(read_instance(best[0]["instance"])[3]),
        "prior_report": args.prior_report,
        "seconds_per_face": args.seconds,
        "threads_per_face": args.threads,
        "parallel_faces": args.parallel,
        "winner_k": winner["k"],
        "winner_state": winner["state"],
        "results": results,
        "elapsed_seconds": time.time() - started,
    }
    Path(args.report).write_text(json.dumps(report, indent=2,
                                           sort_keys=True) + "\n")
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
