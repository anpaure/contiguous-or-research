#!/usr/bin/env python3
"""Post-run census cross-check and linear-time one-deletion edit reconstruction."""

import argparse
from collections import Counter
import csv
import hashlib
import json
from pathlib import Path
import random
import re

from k17_literal_compress_20260905_a19f7 import BASE_SHA256, STEM, verify, write_json


def missing_masks(word):
    seen, suffixes = set(), set()
    for letter in word:
        suffixes = {letter} | {letter | previous for previous in suffixes}
        seen.update(suffixes)
    return set(range(1, 1 << 17)) - seen


def edit_recipe(source, candidate):
    if len(source) != len(candidate) + 1:
        return {"status": "not_a_one_deletion_candidate"}
    n = len(candidate)
    prefix = [0] * (n + 1)
    suffix = [0] * (n + 1)
    for p in range(n):
        prefix[p + 1] = prefix[p] + (source[p] != candidate[p])
    for p in reversed(range(n)):
        suffix[p] = suffix[p + 1] + (source[p + 1] != candidate[p])
    deleted = min(range(n + 1), key=lambda p: prefix[p] + suffix[p])
    retained = source[:deleted] + source[deleted + 1:]
    changes = []
    for p, (old, new) in enumerate(zip(retained, candidate)):
        if old != new:
            changes.append({
                "original_position": p if p < deleted else p + 1,
                "candidate_position": p,
                "old": old,
                "new": new,
            })
            retained[p] = new
    if retained != candidate:
        raise ValueError("edit recipe failed exact replay")
    return {
        "status": "REPLAYED_EXACTLY",
        "indexing": "zero-based; delete first, then change candidate positions",
        "deleted_position": deleted,
        "deleted_mask": source[deleted],
        "substitutions": changes,
        "substitution_count": len(changes),
        "scope": "minimal Hamming alignment with one deletion, not a minimal general edit proof",
    }


def audit(directory):
    directory = directory.resolve()
    result = {"directory": str(directory), "censuses": [], "candidates": [], "workers": []}
    rng = random.Random(20260905)
    for worker in range(4):
        base = directory / f"{STEM}.variant{worker}.word"
        word = [int(token) for token in base.read_bytes().split()]
        if not verify(base)["universal"]:
            raise ValueError("initial variant is not universal")
        census_path = directory / f"{STEM}.worker{worker}.census.tsv"
        with census_path.open() as stream:
            rows = list(csv.DictReader(stream, delimiter="\t"))
        if len(rows) != 2 * len(word) - 1:
            raise ValueError("incomplete census")
        keys = set()
        histograms = {"delete": Counter(), "merge": Counter()}
        for row in rows:
            kind = row["operation"]
            p, q, holes = map(int, (row["position"], row["right_position"], row["missing"]))
            lost = [int(token) for token in row["lost_targets"].split(",") if token]
            if (kind, p) in keys or kind not in histograms:
                raise ValueError("invalid or duplicate census key")
            keys.add((kind, p))
            if q != p + (kind == "merge") or not 0 <= p <= q < len(word):
                raise ValueError("invalid census interval")
            if int(row["letter"]) != word[p] or len(set(lost)) != holes:
                raise ValueError("invalid census mask or loss count")
            histograms[kind][holes] += 1
        if sum(histograms["delete"].values()) != len(word):
            raise ValueError("deletion census is incomplete")
        if sum(histograms["merge"].values()) != len(word) - 1:
            raise ValueError("merge census is incomplete")
        sampled = {i for i, row in enumerate(rows) if int(row["missing"]) <= 2}
        sampled.update(rng.sample(range(len(rows)), 24))
        for index in sorted(sampled):
            row = rows[index]
            p, q = int(row["position"]), int(row["right_position"])
            replacement = [] if row["operation"] == "delete" else [word[p] | word[q]]
            changed = word[:p] + replacement + word[q + 1:]
            expected = {int(token) for token in row["lost_targets"].split(",") if token}
            if missing_masks(changed) != expected:
                raise ValueError(f"independent census check failed: {worker} {index}")
        result["censuses"].append({
            "worker": worker,
            "rows": len(rows),
            "damage_histograms": histograms,
            "independent_full_word_rechecks": len(sampled),
            "minimum_damage_moves": [row for row in rows if int(row["missing"]) <= 2],
            "sha256": hashlib.sha256(census_path.read_bytes()).hexdigest(),
        })
        candidate_path = directory / f"{STEM}.worker{worker}.best.word"
        if candidate_path.exists():
            report = verify(candidate_path)
            if not report["universal"]:
                raise ValueError("candidate failed independent verification")
            candidate = [int(token) for token in candidate_path.read_bytes().split()]
            recipe = edit_recipe(word, candidate)
            report["recipe_from_variant"] = recipe
            named = directory / f"{STEM}.k17_upper{len(candidate)}.worker{worker}.word"
            named.write_bytes(candidate_path.read_bytes())
            report["retained_named_word"] = str(named)
            write_json(named.with_suffix(".verify.json"), report)
            result["candidates"].append(report)
        log = (directory / f"{STEM}.worker{worker}.log").read_text()
        final = next((line for line in reversed(log.splitlines()) if line.startswith("FINAL ")), None)
        if final is None:
            raise ValueError("search worker has not finished")
        fields = dict(re.findall(r"(\w+)=([^ ]+)", final))
        result["workers"].append(fields)
    result["status"] = "PASS_INDEPENDENT_LITERAL_AUDIT"
    result["total_search_trials"] = sum(int(worker["trials"]) for worker in result["workers"])
    result["total_accepted_repair_moves"] = sum(int(worker["accepted"]) for worker in result["workers"])
    result["total_census_moves"] = sum(census["rows"] for census in result["censuses"])
    result["total_independent_census_rechecks"] = sum(
        census["independent_full_word_rechecks"] for census in result["censuses"]
    )
    write_json(directory / f"{STEM}.audit.json", result)
    print(json.dumps(result, indent=2, sort_keys=True))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path)
    parser.add_argument("--replay", action="store_true",
                        help="rebuild the preferred witness from the authenticated baseline only")
    args = parser.parse_args()
    if args.replay:
        baseline = args.directory / "k17_upper25746.word"
        raw = baseline.read_bytes()
        if hashlib.sha256(raw).hexdigest() != BASE_SHA256:
            raise ValueError("baseline hash mismatch")
        parent = [int(token) for token in raw.split()][:12873]
        word = parent[1:][::-1] + [65536, 50122, 33642] + [x | 65536 for x in parent[3:]]
        output = args.directory / f"{STEM}.replayed_k17_upper25745.word"
        output.write_text(" ".join(map(str, word)) + "\n")
        report = verify(output)
        expected = "ef69969f6f72bc85173c9ccb413b7c111a398e725b956f2a91cbe5decbabca38"
        if not report["universal"] or report["length"] != 25745 or report["sha256"] != expected:
            raise ValueError("deterministic replay failed literal verification or byte identity")
        write_json(output.with_suffix(".verify.json"), report)
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        audit(args.directory)


if __name__ == "__main__":
    main()
