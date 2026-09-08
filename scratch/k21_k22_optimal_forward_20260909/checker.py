#!/usr/bin/env python3
"""One fixed independent forward first-occurrence census for two supplied words.

No existing verifier is imported. No ending/suffix recurrence, segment tree,
cyclic extension, SAT solver, or search is used. Mathematics is permitted only
on the declared H100 host and under the fixed one-run resource limits.
"""
import hashlib
import json
import math
import resource
import signal
import socket
import sys
import time
from array import array
from pathlib import Path


HOST = "arboghast"
ROOT = Path("/home/amodo/exact-b-k21-k22-optimal-forward-20260909")
INPUTS = (
    (21, 352719,
     "eb44ff87a669ae0163bdf926283c22c5494e08322efb5c947994a676dc3af1d2",
     Path("/home/amodo/k21_optimal352719_forward_input.word")),
    (22, 705435,
     "a32fe59af4511fcf1a0e032e3f57ae358a9b74492a3f6d56aa8f4564c77ba2dd",
     Path("/home/amodo/k22_optimal705435_forward_input.word")),
)
CAPS = dict(cpu_seconds=60, wall_seconds=90,
            address_space_bytes=2*1024**3, maximum_file_bytes=256*1024**2)


def write_json(path, obj):
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n")


def all_rank_lower_bounds(k):
    """Every tau is minimal, certified on both sides with exact integers."""
    lower_rank_total = 0
    rows = []
    for rank in range(1, k + 1):
        count = math.comb(k, rank)
        discriminant = (2*count + 1)**2 + 8*lower_rank_total
        tau = max(0, (math.isqrt(discriminant) - (2*count + 1)) // 2)
        while tau*count + tau*(tau + 1)//2 < lower_rank_total:
            tau += 1
        attained_capacity = tau*count + tau*(tau + 1)//2
        preceding_capacity = ((tau - 1)*count + (tau - 1)*tau//2
                              if tau else None)
        assert attained_capacity >= lower_rank_total
        assert tau == 0 or preceding_capacity < lower_rank_total
        rows.append(dict(rank=rank, rank_size=count,
                         smaller_nonempty_target_count=lower_rank_total,
                         tau=tau, lower_bound=count+tau,
                         capacity_at_tau=attained_capacity,
                         capacity_at_tau_minus_one=preceding_capacity))
        lower_rank_total += count
    assert lower_rank_total == (1 << k) - 1
    best = max(row["lower_bound"] for row in rows)
    return dict(all_rank_rows=rows, B=best,
                maximizing_ranks=[row["rank"] for row in rows
                                  if row["lower_bound"] == best])


def scan_word(k, expected_length, expected_sha, source):
    wall_begin = time.monotonic()
    cpu_begin = time.process_time()
    raw = source.read_bytes()
    input_sha = hashlib.sha256(raw).hexdigest()
    if input_sha != expected_sha:
        raise ValueError(f"raw SHA mismatch in {source}: {input_sha}")
    tokens = raw.split()
    if not all(token.isdigit() for token in tokens):
        raise ValueError(f"nondecimal token in {source}")
    word = [int(token) for token in tokens]
    del tokens
    n = len(word)
    full = (1 << k) - 1
    lower = all_rank_lower_bounds(k)
    base = dict(k=k, input_path=str(source), input_sha256=input_sha,
                expected_input_sha256=expected_sha, input_sha_matches=True,
                input_bytes=len(raw), expected_length=expected_length,
                length=n, endpoint_lower_bound=lower)
    if n != expected_length or any(letter < 1 or letter > full for letter in word):
        base.update(status="FAIL_INPUT", valid_length=n == expected_length,
                    invalid_letter_positions=[i for i, value in enumerate(word)
                                              if value < 1 or value > full])
        write_json(ROOT / f"k{k}_forward_certificate.json", base)
        return base

    # Signed 32-bit witness endpoints suffice for these fixed word lengths.
    assert array("i").itemsize == 4 and n < 2**31
    witness_start = array("i", [-1]) * (full + 1)
    witness_end = array("i", [-1]) * (full + 1)
    next_at = [n] * k
    bit_values = [1 << coordinate for coordinate in range(k)]
    rank_counts = [0] * (k + 1)
    distinct = 0
    events_examined = 0

    # Sweep starts backwards only to maintain the first occurrence of each
    # coordinate AT OR AFTER that start. The actual enumeration from each
    # start is forward, by increasing first-occurrence position.
    for left in range(n - 1, -1, -1):
        mask = word[left]
        while mask:
            bit = mask & -mask
            next_at[bit.bit_length() - 1] = left
            mask ^= bit

        event_bits = {}
        for coordinate, right in enumerate(next_at):
            if right != n:
                event_bits[right] = event_bits.get(right, 0) | bit_values[coordinate]
        assert left in event_bits  # Each letter was checked nonempty.
        interval_union = 0
        for right in sorted(event_bits):
            interval_union |= event_bits[right]
            assert 0 <= left <= right < n and 1 <= interval_union <= full
            if witness_start[interval_union] == -1:
                witness_start[interval_union] = left
                witness_end[interval_union] = right
                rank_counts[interval_union.bit_count()] += 1
                distinct += 1
            events_examined += 1

    # Completeness is checked over EVERY target, not inferred from the size
    # of a set of possibly invalid masks. The endpoint arrays contain only
    # ordinary intervals emitted by the first-occurrence construction.
    missing = []
    for target in range(1, full + 1):
        left = witness_start[target]
        if left == -1:
            missing.append(target)
        else:
            assert 0 <= left <= witness_end[target] < n
    assert distinct + len(missing) == full
    assert sum(rank_counts) == distinct and rank_counts[0] == 0
    if not missing:
        assert rank_counts[1:] == [math.comb(k, rank) for rank in range(1, k+1)]

    # The reproducible witness format is target-indexed, with index0 unused,
    # signed int32 native endian. A witness for target T is [start[T],end[T]],
    # with ZERO-based inclusive ordinary endpoints. The two arrays together
    # use32 MiB at k22. Each is a complete target-indexed witness table.
    witness_files = {}
    for side, values in (("start", witness_start), ("end", witness_end)):
        payload = values.tobytes()
        name = f"k{k}_ordinary_witness_{side}.int32"
        (ROOT / name).write_bytes(payload)
        witness_files[side] = dict(file=name, bytes=len(payload),
                                   sha256=hashlib.sha256(payload).hexdigest())
    (ROOT / f"k{k}_optimal{expected_length}.word").write_bytes(raw)
    base.update(
        status="PASS" if not missing else "FAIL_MISSING_TARGETS",
        expected_nonempty_targets=full, distinct_nonempty_targets=distinct,
        missing_target_count=len(missing), missing_targets=missing,
        target_rank_counts={rank: rank_counts[rank] for rank in range(1, k+1)},
        first_occurrence_events=events_examined,
        all_letters_nonzero_and_in_cube=True,
        upper_bound_verified=not missing,
        gap_above_all_rank_endpoint_bound=n-lower["B"],
        length_equals_all_rank_endpoint_bound=n == lower["B"],
        optimality_certified=(not missing and n == lower["B"]),
        witness_format=dict(dtype="signed int32", byteorder=sys.byteorder,
                            entries=full+1, index_zero_unused=True,
                            endpoints="zero-based inclusive ordinary intervals",
                            files=witness_files),
        cpu_seconds=time.process_time()-cpu_begin,
        wall_seconds=time.monotonic()-wall_begin,
    )
    write_json(ROOT / f"k{k}_forward_certificate.json", base)
    print(json.dumps(dict(k=k, status=base["status"], length=n,
                          targets=distinct, missing=len(missing),
                          B=lower["B"], sha256=input_sha,
                          gap=n-lower["B"],
                          optimality_certified=base["optimality_certified"],
                          cpu_seconds=base["cpu_seconds"])), flush=True)
    return base


def main():
    assert socket.gethostname().split(".")[0] == HOST
    resource.setrlimit(resource.RLIMIT_CPU, (CAPS["cpu_seconds"],)*2)
    resource.setrlimit(resource.RLIMIT_AS, (CAPS["address_space_bytes"],)*2)
    resource.setrlimit(resource.RLIMIT_FSIZE, (CAPS["maximum_file_bytes"],)*2)
    signal.alarm(CAPS["wall_seconds"])
    wall_begin = time.monotonic()
    cpu_begin = time.process_time()
    ROOT.mkdir(exist_ok=False)
    source_bytes = Path(__file__).read_bytes()
    source_sha = hashlib.sha256(source_bytes).hexdigest()
    (ROOT / "checker.py").write_bytes(source_bytes)
    write_json(ROOT / "run_started.json", dict(status="RUNNING_NOT_CERTIFIED",
               source_sha256=source_sha, hostname=socket.gethostname(),
               resource_caps=CAPS))
    try:
        results = [scan_word(k, length, sha, path)
                   for k, length, sha, path in INPUTS]
    except MemoryError:
        write_json(ROOT / "run_failure.json", dict(status="INCONCLUSIVE_MEMORY_LIMIT"))
        raise
    except Exception as error:
        write_json(ROOT / "run_failure.json", dict(status="ERROR_NOT_CERTIFIED",
                                                   exception=repr(error)))
        raise
    report = dict(
        status="PASS_OPTIMAL_FULL_CUBES" if all(r.get("optimality_certified")
                                                for r in results) else "FAIL",
        source_sha256=source_sha, hostname=socket.gethostname(), resource_caps=CAPS,
        verification_method=("For each ordinary start, enumerate the sorted first "
                             "appearance positions of every coordinate. Add all bits "
                             "appearing at a shared position simultaneously. These "
                             "are exactly all distinct OR values of intervals with "
                             "that start. No suffix recurrence, tree, cyclic scan, "
                             "or previous verifier is used."),
        input_results=results,
        elapsed_cpu_seconds=time.process_time()-cpu_begin,
        elapsed_wall_seconds=time.monotonic()-wall_begin,
        scope=("Only the two SHA-pinned supplied literals and their independently "
               "derived all-rank endpoint lower bounds. Whole-run PASS requires "
               "complete ordinary-interval coverage AND equality to the maximum "
               "all-rank bound for BOTH words. No cyclic opening, periodic lift, "
               "constructor, optimization or unprovided schedule is replayed."),
    )
    write_json(ROOT / "k21_k22_optimal_forward_complete_certificate.json", report)
    print(json.dumps(dict(status=report["status"],
                          report=str(ROOT / "k21_k22_optimal_forward_complete_certificate.json"),
                          cpu_seconds=report["elapsed_cpu_seconds"],
                          wall_seconds=report["elapsed_wall_seconds"])), flush=True)


if __name__ == "__main__":
    main()
