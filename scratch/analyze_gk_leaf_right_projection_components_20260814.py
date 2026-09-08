#!/usr/bin/env python3
"""Analyze connected components of the leaf-right upper--head projection.

Substantive executions belong on H100.
"""

from __future__ import annotations

import argparse
import collections
import json
from pathlib import Path


def gk(x: int, n: int):
    stack = []
    mate = {}
    for i in range(n):
        if (x >> i) & 1:
            stack.append(i)
        elif stack:
            j = stack.pop()
            mate[j] = i
            mate[i] = j
    free = [i for i in range(n) if i not in mate]
    return mate, free


def invariant_candidates(x: int, n: int):
    mate, free = gk(x, n)
    pairs = tuple(sorted((i, j) for i, j in mate.items() if i < j))
    free_zero = tuple(i for i in free if not ((x >> i) & 1))
    free_one = tuple(i for i in free if (x >> i) & 1)
    # Remove the free letters and record the noncrossing matched skeleton.
    skeleton = tuple((i, j) for i, j in pairs)
    matched_word = tuple((x >> i) & 1 for i in range(n) if i not in free)
    return {
        "mate_pairs": pairs,
        "free_positions": tuple(free),
        "free_zero_count": len(free_zero),
        "first_free_one": free_one[0],
        "last_free_zero": free_zero[-1] if free_zero else -1,
        "matched_word": matched_word,
        "skeleton": skeleton,
    }


def path_profile(x: int, n: int):
    heights = []
    h = 0
    for i in range(n):
        h += 1 if ((x >> i) & 1) else -1
        heights.append(h)
    mate, free = gk(x, n)
    free_zero = [i for i in free if not ((x >> i) & 1)]
    free_one = [i for i in free if (x >> i) & 1]
    return (
        min([0] + heights),
        max(heights),
        free_zero[-1] if free_zero else -1,
        free_one[0] if free_one else -1,
        len(free_zero),
        sum(i for i in range(n) if ((x >> i) & 1)) % 2,
        (x & 1),
        ((x >> (n - 1)) & 1),
    )


def audit(path: Path, witness_path: Path | None) -> None:
    d = json.loads(path.read_text())
    n = d["n"]
    m = d["m"]
    recs = [r for r in d["records"] if r["q"] > r["p"]]
    us = sorted({r["upper"] for r in d["records"]})
    bs = sorted({r["b"] for r in recs})
    ua = {u: set() for u in us}
    ba = {b: set() for b in bs}
    for r in recs:
        ua[r["upper"]].add(r["b"])
        ba[r["b"]].add(r["upper"])

    seen_u = set()
    seen_b = set()
    components = []
    for seed in us:
        if seed in seen_u:
            continue
        cu = {seed}
        cb = set()
        queue = collections.deque([("u", seed)])
        seen_u.add(seed)
        while queue:
            side, x = queue.popleft()
            if side == "u":
                for b in ua[x]:
                    if b not in seen_b:
                        seen_b.add(b)
                        cb.add(b)
                        queue.append(("b", b))
            else:
                for u in ba[x]:
                    if u not in seen_u:
                        seen_u.add(u)
                        cu.add(u)
                        queue.append(("u", u))
        components.append((cu, cb))

    print("INSTANCE", m, "components", len(components))
    size_hist = collections.Counter((len(cu), len(cb), len(cu) - len(cb)) for cu, cb in components)
    balance_hist = collections.Counter(len(cu) - len(cb) for cu, cb in components)
    print("BALANCES", sorted(balance_hist.items()))
    print("NEG", sum(1 for cu, cb in components if len(cu) > len(cb)),
          sum(len(cu) for cu, cb in components if len(cu) > len(cb)),
          sum(len(cb) for cu, cb in components if len(cu) > len(cb)),
          sum(len(cu) - len(cb) for cu, cb in components if len(cu) > len(cb)))
    print("ZERO", sum(1 for cu, cb in components if len(cu) == len(cb)))
    print("POS", sum(1 for cu, cb in components if len(cu) < len(cb)))
    print("TOPSIZES", sorted(size_hist.items(), key=lambda kv: (-abs(kv[0][2]), -kv[0][0], -kv[0][1]))[:100])

    def word(x):
        return "".join(str((x >> i) & 1) for i in range(n))

    for idx, (cu, cb) in enumerate(sorted(components, key=lambda z: (-len(z[0]), -len(z[1])))):
        if any(x & 1 for x in cu | cb):
            # Integer order prioritizes leftmost low-index bits, and hence is a
            # convenient canonical word order only after sorting word strings.
            print("BIT1COMP", idx, len(cu), len(cb), len(cu)-len(cb),
                  min(map(word, cu)), max(map(word, cu)),
                  min(map(word, cb)) if cb else "-", max(map(word, cb)) if cb else "-")
    monotone_upper = (1 << (m + 2)) - 1
    seed_component = next((z for z in components if monotone_upper in z[0]), None)
    if seed_component is not None:
        print("MONOTONE_COMPONENT", len(seed_component[0]), len(seed_component[1]),
              len(seed_component[0]) - len(seed_component[1]))
        cand_u = {x for x in us if (x & 1) and len(gk(x, n)[1]) and
                  len([i for i in gk(x, n)[1] if not ((x >> i) & 1)]) <= 3}
        cand_b = {x for x in bs if (x & 1) and
                  len([i for i in gk(x, n)[1] if not ((x >> i) & 1)]) <= 3}
        print("MONO_VS_BIT1_DEPTH3", len(cand_u-seed_component[0]), len(seed_component[0]-cand_u),
              len(cand_b-seed_component[1]), len(seed_component[1]-cand_b))
        for label, vals in (("Uextra", cand_u-seed_component[0]),
                            ("Bextra", cand_b-seed_component[1])):
            profiles = collections.Counter(path_profile(x, n) for x in vals)
            print(label, "profiles", sorted(profiles.items()))
            print(label, "words", sorted(map(word, vals))[:80])
        def delayed_last_min(x):
            free = gk(x, n)[1]
            fz = [i for i in free if not ((x >> i) & 1)]
            return bool(x & 1) and (not fz or fz[-1] >= 3 * len(fz) - 1)
        delayed_u = {x for x in us if delayed_last_min(x)}
        delayed_b = {x for x in bs if delayed_last_min(x)}
        print("MONO_VS_DELAYED_LAST_MIN",
              len(delayed_u-seed_component[0]), len(seed_component[0]-delayed_u),
              len(delayed_b-seed_component[1]), len(seed_component[1]-delayed_b))
        for label, shore, universe in (("U", seed_component[0], us), ("B", seed_component[1], bs)):
            print("THRESHOLD_SEARCH", label)
            best=[]
            for a in range(-2,8):
                for b0 in range(-3,8):
                    def pred(x):
                        free=gk(x,n)[1];fz=[i for i in free if not((x>>i)&1)]
                        return bool(x&1) and (not fz or fz[-1] >= a*len(fz)+b0)
                    cand={x for x in universe if pred(x)}
                    best.append((len(cand^shore),len(cand-shore),len(shore-cand),a,b0))
            print(sorted(best)[:15])

    if witness_path:
        w = json.loads(witness_path.read_text())
        actual_s = set(w["S"])
        actual_n = set(w["N"])
        neg_u = set().union(*(cu for cu, cb in components if len(cu) > len(cb)))
        neg_b = set().union(*(cb for cu, cb in components if len(cu) > len(cb)))
        print("WITNESS_VS_NEG", len(actual_s ^ neg_u), len(actual_n ^ neg_b))

    # For each component, report which natural GK invariants are constant on
    # the union of its two shores after rank normalization is ignored.
    neg_components = [(cu, cb) for cu, cb in components if len(cu) > len(cb)]
    for idx, (cu, cb) in enumerate(sorted(neg_components, key=lambda z: (-len(z[0]) + len(z[1]), -len(z[0])))[:30]):
        joined = cu | cb
        inv = {k: {invariant_candidates(x, n)[k] for x in joined}
               for k in invariant_candidates(next(iter(joined)), n)}
        constants = {k: next(iter(v)) for k, v in inv.items() if len(v) == 1}
        sample_u = "".join(str((min(cu) >> i) & 1) for i in range(n))
        sample_b = "".join(str((min(cb) >> i) & 1) for i in range(n)) if cb else "-"
        print("NEGCOMP", idx, len(cu), len(cb), len(cu) - len(cb), "const", constants,
              "samples", sample_u, sample_b)
        print("  UPROFILE", sorted(collections.Counter(path_profile(x, n) for x in cu).items()))
        print("  BPROFILE", sorted(collections.Counter(path_profile(x, n) for x in cb).items()))
        print("  UMARG", [sum((x >> i) & 1 for x in cu) for i in range(n)])
        print("  BMARG", [sum((x >> i) & 1 for x in cb) for i in range(n)])


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("catalogue", type=Path)
    p.add_argument("--witness", type=Path)
    a = p.parse_args()
    audit(a.catalogue, a.witness)
