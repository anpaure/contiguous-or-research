#!/usr/bin/env python3
"""CNF for a full upper-diamond selector with one fixed GK endpoint.

For every upper U, p(U) is its first free 1 under the linear 10 matching,
so A(U)=U-p(U) is injective.  Choose q in U-p.  The option uses
L=U-p-q and B=U-q.  We ask that all L and all B be distinct.  Then the
physical owner degree is at most two automatically (one A and one B).
"""

from __future__ import annotations

import argparse
import collections
import itertools
import json
from pathlib import Path


def masks_of_weight(n: int, r: int):
    for comb in itertools.combinations(range(n), r):
        x = 0
        for i in comb:
            x |= 1 << i
        yield x


def first_free_one(mask: int, n: int) -> int:
    stack: list[int] = []
    paired: set[int] = set()
    for i in range(n):
        if (mask >> i) & 1:
            stack.append(i)
        elif stack:
            paired.add(i)
            paired.add(stack.pop())
    for i in range(n):
        if ((mask >> i) & 1) and i not in paired:
            return i
    raise AssertionError("no free one")


class Cnf:
    def __init__(self):
        self.nvars = 0
        self.clauses: list[list[int]] = []

    def var(self) -> int:
        self.nvars += 1
        return self.nvars

    def exactly_one(self, xs: list[int]) -> None:
        assert xs
        self.clauses.append(xs)
        self.at_most_one(xs)

    def at_most_one(self, xs: list[int]) -> None:
        if len(xs) <= 1:
            return
        # Sinz sequential encoding.
        ss = [self.var() for _ in range(len(xs) - 1)]
        self.clauses.append([-xs[0], ss[0]])
        for i in range(1, len(xs) - 1):
            self.clauses.append([-xs[i], ss[i]])
            self.clauses.append([-ss[i - 1], ss[i]])
            self.clauses.append([-xs[i], -ss[i - 1]])
        self.clauses.append([-xs[-1], -ss[-1]])

    def write(self, path: Path) -> None:
        with path.open("w") as f:
            f.write(f"p cnf {self.nvars} {len(self.clauses)}\n")
            for c in self.clauses:
                f.write(" ".join(map(str, c)) + " 0\n")


def reverse_free_predecessor(upper: int, n: int, delta: int) -> int:
    order = [(delta - j) % n for j in range(n)]
    stack: list[int] = []
    paired: set[int] = set()
    for i in order:
        if (upper >> i) & 1:
            stack.append(i)
        elif stack:
            paired.add(i)
            paired.add(stack.pop())
    for i in order:
        if ((upper >> i) & 1) and i not in paired:
            return i
    raise AssertionError("no reverse free one")


def linear_matching(mask: int, n: int):
    stack: list[int] = []
    mate: dict[int, int] = {}
    for i in range(n):
        if (mask >> i) & 1:
            stack.append(i)
        elif stack:
            j = stack.pop()
            mate[i] = j
            mate[j] = i
    return mate


def build(m: int, cnf_path: Path, map_path: Path, deltas: list[int] | None,
          q_mode: str, lower_hole_dual_a: bool) -> None:
    n = 2 * m + 1
    full = (1 << n) - 1
    allowed_lowers: set[int] | None = None
    if lower_hole_dual_a:
        all_owners = set(masks_of_weight(n, m + 1))
        a_image = set()
        for upper in masks_of_weight(n, m + 2):
            p = first_free_one(upper, n)
            a_image.add(upper ^ (1 << p))
        a_holes = all_owners - a_image
        forbidden_lowers = {full ^ a for a in a_holes}
        allowed_lowers = set(masks_of_weight(n, m)) - forbidden_lowers
        assert len(allowed_lowers) == len(a_image)
    cnf = Cnf()
    by_upper: dict[int, list[int]] = collections.defaultdict(list)
    by_lower: dict[int, list[int]] = collections.defaultdict(list)
    by_b: dict[int, list[int]] = collections.defaultdict(list)
    records = []
    a_seen = set()
    for upper in masks_of_weight(n, m + 2):
        p = first_free_one(upper, n)
        a = upper ^ (1 << p)
        assert a not in a_seen
        a_seen.add(a)
        if deltas is None:
            qs = [q for q in range(n) if q != p and ((upper >> q) & 1)]
        else:
            qs = sorted({reverse_free_predecessor(upper, n, d % n) for d in deltas} - {p})
        if q_mode in ("leaf", "leaf_right", "leaf_type_min",
                      "leaf_type_max", "leaf_type_cyclic",
                      "leaf_type_extremes", "leaf_type_three"):
            mate = linear_matching(a, n)
            qs = [q for q in qs if q not in mate or mate[q] == q + 1]
            if q_mode == "leaf_right":
                qs = [q for q in qs if q > p]
            elif q_mode.startswith("leaf_type_"):
                by_type: dict[int, list[int]] = collections.defaultdict(list)
                for q in qs:
                    lower = a ^ (1 << q)
                    ml = linear_matching(lower, n)
                    free_zeros = [i for i in range(n)
                                  if not ((lower >> i) & 1) and i not in ml]
                    t = len(free_zeros) - 1 - free_zeros.index(p)
                    assert t in (0, 1, 2)
                    by_type[t].append(q)
                if q_mode == "leaf_type_min":
                    qs = [min(v) for v in by_type.values()]
                elif q_mode == "leaf_type_max":
                    qs = [max(v) for v in by_type.values()]
                elif q_mode == "leaf_type_cyclic":
                    qs = [min(v, key=lambda q: (q - p) % n)
                          for v in by_type.values()]
                elif q_mode == "leaf_type_extremes":
                    qs = sorted({q for v in by_type.values()
                                 for q in (min(v), max(v))})
                else:
                    qs = sorted({q for v in by_type.values()
                                 for q in (min(v), max(v),
                                           min(v, key=lambda x: (x - p) % n))})
        for q in qs:
            lower = a ^ (1 << q)
            if allowed_lowers is not None and lower not in allowed_lowers:
                continue
            b = upper ^ (1 << q)
            x = cnf.var()
            rec = {"var": x, "upper": upper, "p": p, "q": q,
                   "a": a, "b": b, "lower": lower}
            records.append(rec)
            by_upper[upper].append(x)
            by_lower[lower].append(x)
            by_b[b].append(x)
    for xs in by_upper.values():
        cnf.exactly_one(xs)
    for xs in by_lower.values():
        cnf.at_most_one(xs)
    for xs in by_b.values():
        cnf.at_most_one(xs)
    cnf.write(cnf_path)
    map_path.write_text(json.dumps({"m": m, "n": n, "deltas": deltas,
                                    "q_mode": q_mode,
                                    "lower_hole_dual_a": lower_hole_dual_a,
                                    "records": records}))
    print(json.dumps({"m": m, "uppers": len(by_upper), "options": len(records),
                      "lowers": len(by_lower), "owners_b": len(by_b),
                      "vars": cnf.nvars, "clauses": len(cnf.clauses)}))


def decode(map_path: Path, sol_path: Path, out_path: Path) -> None:
    data = json.loads(map_path.read_text())
    positives: set[int] = set()
    status = None
    for line in sol_path.read_text().splitlines():
        if line.startswith("s "):
            status = line
        if line.startswith("v "):
            positives.update(int(x) for x in line[2:].split() if int(x) > 0)
    chosen = [r for r in data["records"] if r["var"] in positives]
    out = {"status": status, "m": data["m"], "n": data["n"], "chosen": chosen}
    out_path.write_text(json.dumps(out, indent=2, sort_keys=True))
    print(json.dumps({"status": status, "chosen": len(chosen)}))


def main() -> None:
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("build")
    b.add_argument("m", type=int)
    b.add_argument("cnf", type=Path)
    b.add_argument("mapping", type=Path)
    b.add_argument("--deltas", type=int, nargs="*")
    b.add_argument("--q-mode", choices=("all", "leaf", "leaf_right",
                                        "leaf_type_min", "leaf_type_max",
                                        "leaf_type_cyclic", "leaf_type_extremes",
                                        "leaf_type_three"), default="all")
    b.add_argument("--lower-hole-dual-a", action="store_true")
    d = sub.add_parser("decode")
    d.add_argument("mapping", type=Path)
    d.add_argument("solution", type=Path)
    d.add_argument("output", type=Path)
    a = p.parse_args()
    if a.cmd == "build":
        build(a.m, a.cnf, a.mapping, a.deltas, a.q_mode,
              a.lower_hole_dual_a)
    else:
        decode(a.mapping, a.solution, a.output)


if __name__ == "__main__":
    main()
