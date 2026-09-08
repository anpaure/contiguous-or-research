"""Remote-only catalogue/all-rank LP screen of all 60 labelled fixed matchings."""

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from hashlib import sha256
import json
import importlib.util
import os
from pathlib import Path
import shutil
import subprocess
import sys


parser = argparse.ArgumentParser()
parser.add_argument("--output", required=True, type=Path)
parser.add_argument("--parallel", type=int, default=4)
parser.add_argument("--seconds", type=float, default=30)
parser.add_argument("--type6-variants", action="store_true",
                    help="Screen all four last-label variants for each of the six involutive matchings.")
parser.add_argument("--save-primal", action="store_true")
args = parser.parse_args()
root = Path(__file__).resolve().parent
out = args.output.resolve()
assert out.is_dir() and out.parent == root and out.name.startswith("run-")
source_names = ["binary10_involution_completion_20260907.py",
                "binary10_involution_matching_core_20260907.py",
                "binary10_involution_catalogue_20260907.cpp"]
hashes = {}
for name in source_names:
    shutil.copy2(root/name, out/name)
    hashes[name] = sha256((out/name).read_bytes()).hexdigest()
(out/"sources.json").write_text(json.dumps(hashes, indent=2)+"\n")
print("SCREEN_START", str(out), "parallel", args.parallel, flush=True)
jobs = [(index,0) for index in range(60)]
if args.type6_variants:
    spec = importlib.util.spec_from_file_location("screen_core",out/source_names[1])
    core_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(core_module)
    lower, matchings = core_module.all_fixed_matchings()
    jobs = []
    for index, upper in enumerate(matchings):
        f = dict(zip(lower,(31^b for b in upper)))
        if all(f[f[a]] == a for a in lower):
            assignments = core_module.last_assignments(lower,upper)
            assert len(assignments) == 4
            jobs.extend((index,variant) for variant in range(4))
    assert len(jobs) == 24
print("SCREEN_JOB_COUNT",len(jobs),flush=True)


def run(job):
    index, variant = job
    environment = os.environ.copy()
    environment.update(BINARY10_MATCHING_INDEX=str(index),
                       BINARY10_LAST_VARIANT=str(variant),
                       BINARY10_CORE_FIRST_ORDER="regular", OMP_NUM_THREADS="1",
                       OPENBLAS_NUM_THREADS="1", MKL_NUM_THREADS="1")
    command = [sys.executable, "-u", str(out/source_names[0]),
               "--core", str(out/source_names[1]),
               "--catalogue", str(root/"binary10_involution_catalogue_20260907"),
               "--seconds", str(args.seconds), "--lp-threads", "1"]
    prefix = f"matching-{index:02d}-last-{variant}"
    if args.save_primal:
        command.extend(["--lp-artifact",str(out/f"{prefix}.primal.json")])
    log = out/f"{prefix}.log"
    with log.open("w") as stream:
        stream.write(f"BINARY10_MATCHING_INDEX={index}\nBINARY10_LAST_VARIANT={variant}\nBINARY10_CORE_FIRST_ORDER=regular\n")
        stream.flush()
        completed = subprocess.run(command, env=environment, stdout=stream,
                                   stderr=subprocess.STDOUT, check=False)
    lines = log.read_text().splitlines()
    record = {"index": index, "last_variant":variant,"exit": completed.returncode,
              "summary": [line for line in lines if line.startswith(
                  ("COLUMN_SUMMARY", "LP_STATUS", "LP_ACTIVE", "INFEASIBLE", "VERIFIED"))]}
    (out/f"{prefix}.status.json").write_text(json.dumps(record, indent=2)+"\n")
    return record


records = []
with ThreadPoolExecutor(max_workers=args.parallel) as pool:
    futures = [pool.submit(run, job) for job in jobs]
    for future in as_completed(futures):
        record = future.result()
        records.append(record)
        print("SCREEN_RESULT", json.dumps(record, sort_keys=True), flush=True)
records.sort(key=lambda record: (record["index"],record["last_variant"]))
(out/"summary.json").write_text(json.dumps(records, indent=2)+"\n")
print("SCREEN_FINISHED", len(records), flush=True)
