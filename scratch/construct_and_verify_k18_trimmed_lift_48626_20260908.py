#!/usr/bin/env python3
"""One deterministic k17->k18 trimmed lift and complete literal replay.

Run only on h100. No deletions, optimization, or search are performed.
"""
import argparse
import hashlib
import json
import platform
import resource
import signal
import time
from array import array
from math import comb
from pathlib import Path


def sha_file(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    assert platform.node().split(".")[0] == "arboghast", "h100 only"
    resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
    resource.setrlimit(resource.RLIMIT_AS, (1024**3, 1024**3))
    signal.alarm(45)
    started = time.monotonic()
    args.out.mkdir(parents=True, exist_ok=False)
    raw = args.input.read_bytes()
    base = [int(line) for line in raw.decode("ascii").splitlines() if line.strip()]
    assert len(base) == 24313
    assert all(0 < a < (1 << 17) for a in base)
    new_bit = 1 << 17
    word = base + [new_bit] + [a | new_bit for a in base[:-1]]
    assert len(word) == 48626 == 2 * len(base)
    full = (1 << 18) - 1
    assert all(0 < a <= full for a in word)
    word_path = args.out / "k18_upper48626.word"
    word_path.write_text("".join(f"{a}\n" for a in word), encoding="ascii")

    # Complete ending-OR census. Keep a latest start for equal suffix unions.
    lefts = array("i", [-1]) * (full + 1)
    rights = array("i", [-1]) * (full + 1)
    suffix = {}
    count = 0
    suffix_occurrences = 0
    for end, letter in enumerate(word):
        current = {letter: end}
        for value, start in suffix.items():
            value |= letter
            if start > current.get(value, -1):
                current[value] = start
        suffix = current
        suffix_occurrences += len(current)
        for value, start in current.items():
            if lefts[value] < 0:
                lefts[value] = start
                rights[value] = end
                count += 1
    assert count == full == 262143
    assert all(lefts[target] >= 0 for target in range(1, full + 1))

    # Independent interval OR queries using a segment tree on the literal word.
    size = 1
    while size < len(word):
        size <<= 1
    tree = [0] * (2 * size)
    tree[size:size + len(word)] = word
    for i in range(size - 1, 0, -1):
        tree[i] = tree[2 * i] | tree[2 * i + 1]
    rank_counts = [0] * 19
    witness_path = args.out / "k18_upper48626.all_target_witnesses.jsonl"
    with witness_path.open("w", encoding="ascii") as stream:
        for target in range(1, full + 1):
            start, end = lefts[target], rights[target]
            assert 0 <= start <= end < len(word)
            l, r, value = start + size, end + 1 + size, 0
            while l < r:
                if l & 1:
                    value |= tree[l]
                    l += 1
                if r & 1:
                    r -= 1
                    value |= tree[r]
                l >>= 1
                r >>= 1
            assert value == target
            rank_counts[target.bit_count()] += 1
            stream.write(json.dumps([target, start, end], separators=(",", ":")) + "\n")
    assert rank_counts[1:] == [comb(18, j) for j in range(1, 19)]

    # Exact endpoint lower-bound calculation, not merely the central candidate.
    lower_rows = []
    smaller = 0
    for s in range(1, 19):
        mass = comb(18, s)
        delay = 0
        while delay * mass + delay * (delay + 1) // 2 < smaller:
            delay += 1
        lower_rows.append(dict(rank=s, mass=mass, lower_rank_mass=smaller,
                               delay=delay, endpoint_bound=mass + delay))
        smaller += mass
    B18 = max(row["endpoint_bound"] for row in lower_rows)
    central = lower_rows[8]
    assert central == dict(rank=9, mass=48620, lower_rank_mass=106761,
                           delay=3, endpoint_bound=48623)
    assert B18 == 48623 and len(word) - B18 == 3
    report = dict(status="PASS", k=18, construction="Exact trimmed one-coordinate lift; no deletions or search",
                  input_word=args.input.name, input_length=len(base), input_sha256=hashlib.sha256(raw).hexdigest(),
                  new_coordinate_bit_mask=new_bit, output_length=len(word), output_sha256=sha_file(word_path),
                  nonempty_targets=full, ending_or_targets_found=count,
                  independent_segment_tree_witnesses_replayed=count,
                  witness_columns=["target_mask", "inclusive_zero_based_start", "inclusive_zero_based_end"],
                  witness_file=witness_path.name, witness_sha256=sha_file(witness_path),
                  rank_target_counts=rank_counts[1:], suffix_state_occurrences=suffix_occurrences,
                  all_letters_nonempty=True, endpoint_lower_bound=B18, lower_bound_rows=lower_rows,
                  upper_minus_lower=3, exact_optimality_claim=False,
                  resource_caps=dict(cpu_seconds=30, wall_seconds=45, address_space_bytes=1024**3),
                  host=platform.node(), elapsed_seconds=time.monotonic() - started)
    (args.out / "k18_upper48626_certificate.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({k:v for k,v in report.items() if k != "lower_bound_rows"}, indent=2), flush=True)


if __name__ == "__main__":
    main()
