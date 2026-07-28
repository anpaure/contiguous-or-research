#!/usr/bin/env python3
"""Independent exhaustive verifier/compiler for sigma SAT certificates."""

from __future__ import annotations

import argparse
from collections import Counter
import json
import math
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
from verify_preservable_shrink_hall import (
    demand_intervals,
    envelopes,
    first_intermediate_pins,
    greedy_core,
    maximum_matching,
    missing_masks,
    prune_envelope,
    verify_pins,
)


def mask_rank_hist(values: list[int]) -> dict[int, int]:
    out = Counter(value.bit_count() for value in values)
    return dict(sorted(out.items()))


def shadow_counts(cycle: list[int], k: int, rank: int):
    n = len(cycle)
    answer = []
    full = (1 << k) - 1
    for q in range(1, min(rank, k - rank) + 1):
        lower = Counter()
        upper = Counter()
        for i in range(n):
            intersection = full
            union = 0
            for h in range(q + 1):
                intersection &= cycle[(i + h) % n]
                union |= cycle[(i + h) % n]
            if intersection.bit_count() == rank - q:
                lower[intersection] += 1
            if union.bit_count() == rank + q:
                upper[union] += 1
        answer.append((q, lower, upper))
    return answer


def residence(cycle: list[int], depth: int):
    n = len(cycle)
    deleted = []
    inserted = []
    for i in range(n):
        old = cycle[i]
        new = cycle[(i + 1) % n]
        drop = old & ~new
        add = new & ~old
        assert drop.bit_count() == add.bit_count() == 1
        deleted.append(drop.bit_length() - 1)
        inserted.append(add.bit_length() - 1)
    bad = []
    for i, coordinate in enumerate(inserted):
        for h in range(1, depth + 1):
            if deleted[(i + h) % n] == coordinate:
                bad.append((i, h, coordinate))
                break
    return bad


def safe_cuts(cycle: list[int], k: int, rank: int):
    n = len(cycle)
    q1 = [cycle[i] | cycle[(i + 1) % n] for i in range(n)]
    q2 = [
        cycle[i] | cycle[(i + 1) % n] | cycle[(i + 2) % n]
        for i in range(n)
    ]
    count1 = Counter(x for x in q1 if x.bit_count() == rank + 1)
    count2 = Counter(x for x in q2 if x.bit_count() == rank + 2)
    all2 = set(x for x in range(1 << k) if x.bit_count() == rank + 2)
    answer = []
    for cut in range(n):
        if count1[q1[cut]] < 2:
            continue
        removed = Counter()
        for index in ((cut - 1) % n, cut):
            if q2[index].bit_count() == rank + 2:
                removed[q2[index]] += 1
        if all(count2[target] - removed[target] >= 1 for target in all2):
            answer.append(cut)
    return answer


def compile_cut(cycle: list[int], cut: int, k: int, rank: int, delay: int):
    central = cycle[cut + 1 :] + cycle[: cut + 1]
    envelope = envelopes(central, delay, k)
    targets = [
        value
        for value in range(1, 1 << k)
        if value.bit_count() <= rank - delay
    ]

    # Cutting removes one lower q1 colour.  The right boundary flag restores
    # it and may restore the two deeper cyclic windows removed by the cut.
    first = cycle[(cut + 1) % len(cycle)]
    last = cycle[cut]
    f1 = first & last
    assert f1.bit_count() == rank - 1
    best = None

    def flags(prefix: list[int]):
        if len(prefix) == delay:
            yield prefix
            return
        current = prefix[-1]
        for removed in (bit for bit in range(k) if (current >> bit) & 1):
            yield from flags(prefix + [current ^ (1 << removed)])

    for flag in flags([f1]):
        boundary = [
            (delay - q, len(central) + q - 1, flag[q - 1])
            for q in range(1, delay + 1)
        ]
        boundary_pruned = prune_envelope(envelope, boundary)
        boundary_rows = [boundary_pruned]
        for _ in range(delay):
            boundary_rows.append(
                [x | y for x, y in zip(boundary_rows[-1], boundary_rows[-1][1:])]
            )
        if boundary_rows[delay] != central:
            continue
        if any(
            boundary_rows[depth][position] != value
            for depth, position, value in boundary
        ):
            continue
        try:
            intermediate = first_intermediate_pins(boundary_rows, k, rank, delay)
        except AssertionError:
            continue
        pins = boundary + intermediate
        pruned = prune_envelope(envelope, pins)
        demands = demand_intervals(central, pins, k, delay)
        core = greedy_core(pruned, demands, k)
        matching = maximum_matching(targets, core, pruned)
        result = {
            "cut": cut,
            "flag": flag,
            "hall": matching.size,
            "target_count": len(targets),
            "pins": len(pins),
            "envelope_mass": sum(x.bit_count() for x in envelope),
            "pruned_mass": sum(x.bit_count() for x in pruned),
            "core_mass": sum(x.bit_count() for x in core),
        }
        if best is None or matching.size > best["hall"]:
            best = result
        if matching.size != len(targets):
            continue

        word = pruned[:]
        for left, position in enumerate(matching.left_to_right):
            assert position >= 0
            word[position] = targets[left]
        verify_pins(word, central, pins, delay)
        missing = missing_masks(word, k)
        result.update(
            {
                "word_mass": sum(x.bit_count() for x in word),
                "word_rank_histogram": mask_rank_hist(word),
                "missing": missing,
                "word": word,
            }
        )
        if not missing:
            return result
    return best


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--compiled-word", type=Path)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()

    data = json.loads(args.certificate.read_text())
    k = data["k"]
    rank = data["r"]
    delay = data.get("residence_depth", 0) or 3
    cycle = data["middle_cycle"]
    width = math.comb(k, rank)
    assert len(cycle) == width
    assert len(set(cycle)) == width
    assert all(x.bit_count() == rank for x in cycle)
    assert set(cycle) == set(x for x in range(1 << k) if x.bit_count() == rank)

    bad = residence(cycle, delay)
    shadows = shadow_counts(cycle, k, rank)
    shadow_report = []
    for q, lower, upper in shadows:
        target_lower = math.comb(k, rank - q)
        target_upper = math.comb(k, rank + q)
        assert len(lower) == target_lower
        assert len(upper) == target_upper
        shadow_report.append(
            {
                "q": q,
                "lower_distinct": len(lower),
                "lower_target": target_lower,
                "lower_loads": sorted(Counter(lower.values()).items()),
                "upper_distinct": len(upper),
                "upper_target": target_upper,
                "upper_loads": sorted(Counter(upper.values()).items()),
            }
        )
    assert not bad

    cuts = safe_cuts(cycle, k, rank)
    compiled = []
    best_failed = None
    for cut in cuts:
        result = compile_cut(cycle, cut, k, rank, delay)
        if result is None:
            continue
        if result.get("missing") == []:
            compiled.append(result)
            break
        if best_failed is None or result["hall"] > best_failed["hall"]:
            best_failed = result

    report = {
        "status": "COMPILED" if compiled else "CENTRAL_ONLY",
        "k": k,
        "rank": rank,
        "delay": delay,
        "cycle_length": len(cycle),
        "residence_violations": len(bad),
        "shadows": shadow_report,
        "safe_cuts": len(cuts),
        "first_compiled": compiled[0] if compiled else None,
        "best_failed": best_failed,
    }
    if args.report:
        args.report.write_text(json.dumps(report, indent=2) + "\n")
    if compiled and args.compiled_word:
        args.compiled_word.write_text(" ".join(map(str, compiled[0]["word"])) + "\n")
    # Avoid printing a 465-entry word in the console summary.
    console = json.loads(json.dumps(report))
    if console["first_compiled"]:
        console["first_compiled"].pop("word", None)
    print(json.dumps(console, sort_keys=True))


if __name__ == "__main__":
    main()
