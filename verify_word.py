#!/usr/bin/env python3
"""Verify an ordinary OR-universal word using only the standard library.

All distinct suffix unions are enumerated; there is no interval-length
cutoff. Optional checks certify an explicitly supplied cyclic opening and
its periodic-core lift. No witness arrays or other files are autosaved.
"""

from __future__ import annotations

from math import comb
from pathlib import Path
import argparse
import hashlib
import json
import re


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def lower_bounds(k: int) -> tuple[int, list[dict]]:
    """Exact endpoint bound at every rank, including both sides of tau."""
    smaller = 0
    rows = []
    for rank in range(1, k + 1):
        width = comb(k, rank)

        def capacity(t: int) -> int:
            return t * width + t * (t + 1) // 2

        lo, hi = 0, 1
        while capacity(hi) < smaller:
            hi *= 2
        while lo < hi:
            mid = (lo + hi) // 2
            if capacity(mid) >= smaller:
                hi = mid
            else:
                lo = mid + 1
        require(capacity(lo) >= smaller and
                (lo == 0 or capacity(lo - 1) < smaller),
                "endpoint-bound arithmetic failed")
        rows.append(dict(rank=rank, width=width, smaller_targets=smaller,
                         delay=lo, lower_bound=width + lo,
                         capacity_at_delay=capacity(lo),
                         capacity_at_previous_delay=capacity(lo - 1) if lo else None))
        smaller += width
    require(smaller == (1 << k) - 1, "binomial layer total failed")
    return max((row["lower_bound"] for row in rows), default=0), rows


def verify(args: argparse.Namespace) -> dict:
    k = args.k
    require(k >= 0, "--k must be nonnegative")
    if args.sha256 is not None:
        require(re.fullmatch(r"[0-9a-fA-F]{64}", args.sha256) is not None,
                "--sha256 must contain exactly 64 hexadecimal characters")
    require(args.lift_word is None or args.cyclic_core is not None,
            "--lift-word requires --cyclic-core")
    if args.json is not None:
        require(args.json.resolve() != args.word.resolve(),
                "JSON output must not overwrite the input word")
        require(args.lift_word is None or
                args.json.resolve() != args.lift_word.resolve(),
                "JSON output must not overwrite the lift word")

    raw = args.word.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    require(args.sha256 is None or digest == args.sha256.lower(),
            "input SHA-256 does not match --sha256")
    tokens = raw.split()
    require(all(token.isdigit() for token in tokens),
            "expected whitespace-separated unsigned decimal masks")
    word = [int(token) for token in tokens]
    del tokens
    full = (1 << k) - 1
    require(all(0 < value <= full for value in word),
            "word contains an empty or out-of-range mask")
    bound, bound_rows = lower_bounds(k)
    require(len(word) >= bound, "word is shorter than the endpoint lower bound")
    require(args.allow_nonoptimal or len(word) == bound,
            "length differs from B(k); use --allow-nonoptimal for an upper word")

    period = args.cyclic_core
    core = None
    delay = None
    if period is not None:
        require(k >= 1 and period >= 1, "cyclic checks need k>=1 and a positive period")
        delay = len(word) - period
        require(0 <= delay < period, "cyclic opening must have length M+d with 0<=d<M")
        core = word[:period]
        require(word == core + core[:delay], "word is not C followed by its first d letters")

    covered = set()
    previous = {}
    ranks = [0] * (k + 1)
    events = maximum_suffixes = maximum_first_witness_span = 0
    # A target enters this set only if its first witness is longer than M;
    # any later witness of length<=M removes it. No witness array is stored.
    unconfirmed_short = set()
    for right, letter in enumerate(word):
        current = {letter: right}
        for target, left in previous.items():
            union = target | letter
            current[union] = max(current.get(union, -1), left)
        require(len(current) <= k, "suffix-chain cardinality failed")
        maximum_suffixes = max(maximum_suffixes, len(current))
        events += len(current)
        for target, left in current.items():
            span = right - left + 1
            if target not in covered:
                covered.add(target)
                ranks[target.bit_count()] += 1
                maximum_first_witness_span = max(maximum_first_witness_span, span)
                if period is not None and span > period:
                    unconfirmed_short.add(target)
            if period is not None and span <= period:
                unconfirmed_short.discard(target)
        previous = current
    require(len(covered) == full,
            f"incomplete coverage: {full - len(covered)} nonempty targets missing")
    require(ranks == [0] + [comb(k, rank) for rank in range(1, k + 1)],
            "target-rank census failed")
    report = dict(status="PASS_OPTIMAL" if len(word) == bound else "PASS_UNIVERSAL",
                  k=k, word=str(args.word), length=len(word), input_sha256=digest,
                  input_bytes=len(raw), nonempty_targets=full,
                  covered_nonempty_targets=len(covered), missing_targets=0,
                  target_rank_counts=ranks, endpoint_lower_bound=bound,
                  gap_to_lower_bound=len(word) - bound,
                  all_rank_lower_bounds=bound_rows,
                  maximizing_ranks=[row["rank"] for row in bound_rows
                                    if row["lower_bound"] == bound],
                  suffix_union_events=events, maximum_distinct_suffix_unions=maximum_suffixes,
                  maximum_first_witness_span=maximum_first_witness_span,
                  all_letters_nonempty=True, interval_type="ordinary, nonwrapping")
    if period is not None:
        require(not unconfirmed_short,
                "the supplied opening does not provide length<=M witnesses for every target")
        cyclic_bound = comb(k, k // 2)
        require(period >= cyclic_bound, "cyclic endpoint lower bound failed")
        report["cyclic_core"] = dict(length=period, opening_delay=delay,
                                     all_targets_have_witness_span_at_most_period=True,
                                     cyclic_lower_bound=cyclic_bound,
                                     optimal=period == cyclic_bound)
        if args.lift_word is not None:
            z = 1 << k
            lifted = word + [z] + [core[(delay + j) % period] | z
                                   for j in range(period - 1)]
            normalized = ("\n".join(map(str, lifted)) + "\n").encode("ascii")
            lift_raw = args.lift_word.read_bytes()
            require(lift_raw == normalized,
                    "lift word is not byte-identical to the normalized periodic-core lift")
            report["periodic_core_lift"] = dict(
                word=str(args.lift_word), k=k + 1, length=len(lifted),
                input_sha256=hashlib.sha256(lift_raw).hexdigest(),
                byte_identical=True, format="one decimal mask per line, final newline")
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("word", type=Path)
    parser.add_argument("--k", type=int, required=True)
    parser.add_argument(
        "--allow-nonoptimal",
        action="store_true",
        help="verify universal coverage without requiring length B(k)",
    )
    parser.add_argument("--sha256", help="optional expected raw input SHA-256")
    parser.add_argument("--json", "--output", dest="json", type=Path,
                        help="write one compact JSON report to this requested path")
    parser.add_argument("--cyclic-core", type=int, metavar="M",
                        help="also certify C=word[:M] from this C+C[:d] opening")
    parser.add_argument("--lift-word", type=Path,
                        help="check the periodic-core lift against this raw word")
    args = parser.parse_args()
    try:
        report = verify(args)
        if args.json is not None:
            args.json.write_text(json.dumps(report, indent=2) + "\n")
    except (ValueError, OSError, MemoryError) as error:
        parser.exit(1, f"FAIL: {error}\n")
    print(f"{report['status']} k={report['k']} length={report['length']} "
          f"covered={report['covered_nonempty_targets']}/{report['nonempty_targets']} "
          f"B={report['endpoint_lower_bound']} gap={report['gap_to_lower_bound']}")
    print(f"SHA-256 {report['input_sha256']}")
    if "cyclic_core" in report:
        print("Cyclic core:", json.dumps(report["cyclic_core"], sort_keys=True))
    if "periodic_core_lift" in report:
        print("Periodic lift:", json.dumps(report["periodic_core_lift"], sort_keys=True))


if __name__ == "__main__":
    main()
