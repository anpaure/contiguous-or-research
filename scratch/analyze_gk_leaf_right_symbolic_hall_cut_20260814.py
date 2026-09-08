#!/usr/bin/env python3
"""Test symbolic descriptions of a leaf-right head Hall witness.

Substantive executions belong on H100.  The input witness is the canonical
alternating-reachability set produced from a maximum upper--head matching.
"""

from __future__ import annotations

import argparse
import collections
import json
from pathlib import Path


def matching(x: int, n: int) -> tuple[dict[int, int], list[int]]:
    stack: list[int] = []
    mate: dict[int, int] = {}
    for i in range(n):
        if (x >> i) & 1:
            stack.append(i)
        elif stack:
            j = stack.pop()
            mate[i] = j
            mate[j] = i
    return mate, [i for i in range(n) if i not in mate]


def free_parts(x: int, n: int) -> tuple[list[int], list[int]]:
    _mate, free = matching(x, n)
    return (
        [i for i in free if not ((x >> i) & 1)],
        [i for i in free if (x >> i) & 1],
    )


def tight_boundary(x: int, n: int) -> bool:
    free_zero, free_one = free_parts(x, n)
    return not free_zero or free_zero[-1] + 1 == free_one[0]


def runs(x: int, n: int) -> tuple[int, ...]:
    return tuple((x >> i) & 1 for i in range(n))


def audit(catalogue_path: Path, witness_path: Path) -> None:
    catalogue = json.loads(catalogue_path.read_text())
    witness = json.loads(witness_path.read_text())
    m = catalogue["m"]
    n = catalogue["n"]
    records = [r for r in catalogue["records"] if r["q"] > r["p"]]
    all_upper = {r["upper"] for r in catalogue["records"]}
    all_head = {r["b"] for r in records}
    actual_s = set(witness["S"])
    actual_n = set(witness["N"])

    predicates = {
        "bit0+at-most-3-free-zeros": lambda x: bool(x & 1)
        and len(free_parts(x, n)[0]) <= 3,
        "at-most-3-free-zeros": lambda x: len(free_parts(x, n)[0]) <= 3,
        "bit0+tight": lambda x: bool(x & 1) and tight_boundary(x, n),
        "tight": lambda x: tight_boundary(x, n),
        "bit0": lambda x: bool(x & 1),
        "bit0+adjacent-boundary": lambda x: bool(x & 1)
        and bool(free_parts(x, n)[0])
        and free_parts(x, n)[0][-1] + 1 == free_parts(x, n)[1][0],
    }
    print("INSTANCE", m, n, len(all_upper), len(all_head))
    for name, pred in predicates.items():
        s = {x for x in all_upper if pred(x)}
        candidate_heads = {x for x in all_head if pred(x)}
        neighbors = {r["b"] for r in records if r["upper"] in s}
        print(
            "PREDICATE",
            name,
            "S",
            len(s),
            "N",
            len(neighbors),
            "head-predicate",
            len(candidate_heads),
            "def",
            len(s) - len(neighbors),
            "Ssym",
            len(s ^ actual_s),
            "Nsym",
            len(neighbors ^ actual_n),
            "N-vs-headpred",
            len(neighbors ^ candidate_heads),
        )

    # Classify precisely why the most promising predicate differs.
    s0 = {x for x in all_upper if (x & 1) and tight_boundary(x, n)}
    n0 = {r["b"] for r in records if r["upper"] in s0}
    for label, values in (
        ("S-extra", s0 - actual_s),
        ("S-missing", actual_s - s0),
        ("N-extra", n0 - actual_n),
        ("N-missing", actual_n - n0),
    ):
        counter: collections.Counter[tuple[int, ...]] = collections.Counter()
        examples = []
        for x in values:
            fz, fo = free_parts(x, n)
            key = (
                len(fz),
                len(fo),
                fz[-1] if fz else -1,
                fo[0] if fo else -1,
            )
            counter[key] += 1
            if len(examples) < 12:
                examples.append("".join(map(str, runs(x, n))))
        print(label, len(values), sorted(counter.items()), examples)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("catalogue", type=Path)
    parser.add_argument("witness", type=Path)
    args = parser.parse_args()
    audit(args.catalogue, args.witness)
