#!/usr/bin/env python3
"""Isolated literal lift variants, bounded CPU workers, and independent verifier.

Run only in a fresh directory containing the authenticated input and executable.
No carrier code, project imports, dependencies, or cyclic interval semantics.
"""

import argparse
import concurrent.futures
import hashlib
import json
import os
from pathlib import Path
import shlex
import subprocess
import time
import unittest


BASE_SHA256 = "f8ea81ab1f8f1280f638e7e607b32a7dd53fc541b30fe1005db8aae692be031b"
STEM = "k17_literal_compress_20260905_a19f7"


def verify(path, k=17):
    """Independent set-valued suffix recurrence, not the C++ multiplicity code."""
    if not 1 <= k <= 17:
        raise ValueError("supported k is 1..17")
    raw = Path(path).read_bytes()
    word = [int(token) for token in raw.split()]
    full = (1 << k) - 1
    if not word or any(value <= 0 or value > full for value in word):
        raise ValueError("word must contain only nonempty k-bit masks")
    seen = set()
    suffixes = set()
    maximum_frontier = 0
    for value in word:
        suffixes = {value} | {value | previous for previous in suffixes}
        seen.update(suffixes)
        maximum_frontier = max(maximum_frontier, len(suffixes))
    missing = sorted(set(range(1, full + 1)) - seen)
    return {
        "path": str(path),
        "k": k,
        "length": len(word),
        "covered_nonempty_masks": len(seen),
        "required_nonempty_masks": full,
        "missing_masks": len(missing),
        "missing_sample": missing[:32],
        "maximum_suffix_frontier": maximum_frontier,
        "sha256": hashlib.sha256(raw).hexdigest(),
        "universal": not missing,
        "semantics": "all nonempty contiguous nonwrapping intervals; bitwise OR",
        "letter_rank_histogram": {
            str(rank): sum(value.bit_count() == rank for value in word)
            for rank in range(1, k + 1)
        },
    }


def write_json(path, value):
    Path(path).write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")


def variants(baseline):
    if hashlib.sha256(baseline.read_bytes()).hexdigest() != BASE_SHA256:
        raise ValueError("baseline hash mismatch")
    word = [int(token) for token in baseline.read_bytes().split()]
    n, z = 12873, 1 << 16
    parent = word[:n]
    if word != parent + [z] + [value | z for value in parent[:-1]]:
        raise ValueError("baseline is not the authenticated trimmed lift")
    # Reversing either copy preserves its internal interval spectrum; the
    # omitted terminal source cell is always supplied by the unmarked suffix.
    for index in range(4):
        source = parent if index < 2 else parent[::-1]
        marked = source[:-1] if index % 2 == 0 else source[:-1][::-1]
        child = source + [z] + [value | z for value in marked]
        path = Path(f"{STEM}.variant{index}.word")
        path.write_text(" ".join(map(str, child)) + "\n")
        report = verify(path)
        write_json(path.with_suffix(".verify.json"), report)
        if not report["universal"]:
            raise ValueError(f"non-universal initial variant {index}")
        yield path, report


def run(args):
    started = time.time()
    inputs = list(variants(args.baseline))
    commands = []
    for index, (path, _) in enumerate(inputs):
        commands.append([
            str(args.executable.resolve()), "17", str(path),
            f"{STEM}.worker{index}", str(args.seconds),
            str(202609050 + index), "census" if args.seconds == 0 else "search",
        ])
    write_json(f"{STEM}.commands.json", {
        "cwd": str(Path.cwd()),
        "driver_pid": os.getpid(),
        "commands": [shlex.join(command) for command in commands],
        "max_workers": args.workers,
        "seconds_per_worker_including_census": args.seconds,
        "external_timeout_seconds": args.seconds + 60,
        "source_sha256": {
            name: hashlib.sha256(Path(name).read_bytes()).hexdigest()
            for name in [f"{STEM}.cpp", f"{STEM}.py"]
        },
    })

    def worker(index):
        command = commands[index]
        env = dict(os.environ, OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1")
        with Path(f"{STEM}.worker{index}.log").open("w") as log:
            result = subprocess.run(command, stdout=log, stderr=subprocess.STDOUT,
                                    env=env, timeout=args.seconds + 60, check=False)
        return {"worker": index, "returncode": result.returncode}

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        statuses = list(pool.map(worker, range(4)))
    reports = []
    for path in sorted(Path.cwd().glob(f"{STEM}.worker*.best.word")):
        report = verify(path)
        write_json(path.with_suffix(".verify.json"), report)
        reports.append(report)
    near_misses = []
    for path in sorted(Path.cwd().glob(f"{STEM}.worker*.near.word")):
        report = verify(path)
        write_json(path.with_suffix(".verify.json"), report)
        near_misses.append(report)
    summary = {
        "baseline": verify(args.baseline),
        "variants": [report for _, report in inputs],
        "workers": statuses,
        "candidates": reports,
        "near_misses_not_upper_bounds": near_misses,
        "elapsed_seconds": time.time() - started,
        "claim": "Only universal candidate reports justify a shorter upper bound.",
    }
    write_json(f"{STEM}.summary.json", summary)
    print(json.dumps(summary, indent=2, sort_keys=True))
    if any(status["returncode"] != 0 for status in statuses):
        raise SystemExit(1)
    if any(not report["universal"] for report in reports):
        raise SystemExit("candidate failed independent verification")


class VerifierTests(unittest.TestCase):
    def test_file_validation_and_nonwrapping(self):
        import tempfile
        with tempfile.TemporaryDirectory(prefix=STEM) as directory:
            path = Path(directory) / "test.word"
            path.write_text("1 2 4\n")
            report = verify(path, 3)
            self.assertFalse(report["universal"])
            self.assertEqual(report["missing_sample"], [5])
            path.write_text("1 2 4 1\n")
            self.assertTrue(verify(path, 3)["universal"])
            for invalid in ["", "0", "-1", "8", "1 garbage"]:
                path.write_text(invalid)
                with self.assertRaises(ValueError):
                    verify(path, 3)

    def test_suffix_recurrence_against_brute_force(self):
        import itertools
        for length in range(1, 6):
            for word in itertools.product(range(1, 4), repeat=length):
                seen, suffixes = set(), set()
                for value in word:
                    suffixes = {value} | {old | value for old in suffixes}
                    seen.update(suffixes)
                brute = set()
                for start in range(length):
                    value = 0
                    for entry in word[start:]:
                        value |= entry
                        brute.add(value)
                self.assertEqual(seen, brute)

    def test_nonwrapping(self):
        # 5 is supplied only by wrapping for [1, 2, 4], so must remain absent.
        seen, suffixes = set(), set()
        for value in [1, 2, 4]:
            suffixes = {value} | {old | value for old in suffixes}
            seen.update(suffixes)
        self.assertNotIn(5, seen)
        self.assertEqual(seen, {1, 2, 3, 4, 6, 7})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="mode", required=True)
    run_parser = sub.add_parser("run")
    run_parser.add_argument("--directory", type=Path, required=True)
    run_parser.add_argument("--baseline", type=Path, default=Path("k17_upper25746.word"))
    run_parser.add_argument("--executable", type=Path, default=Path("compressor"))
    run_parser.add_argument("--seconds", type=float, default=360)
    run_parser.add_argument("--workers", type=int, choices=range(1, 5), default=4)
    verify_parser = sub.add_parser("verify")
    verify_parser.add_argument("word", type=Path)
    verify_parser.add_argument("--k", type=int, default=17)
    verify_parser.add_argument("--output", type=Path)
    sub.add_parser("test")
    args = parser.parse_args()
    if args.mode == "run":
        if args.seconds < 0 or args.seconds > 600:
            parser.error("search budget must be between 0 and 600 seconds per worker")
        os.chdir(args.directory)
        run(args)
    elif args.mode == "verify":
        report = verify(args.word, args.k)
        if args.output:
            write_json(args.output, report)
        print(json.dumps(report, indent=2, sort_keys=True))
        if not report["universal"]:
            raise SystemExit(1)
    else:
        unittest.main(argv=[__file__], exit=True)


if __name__ == "__main__":
    main()
