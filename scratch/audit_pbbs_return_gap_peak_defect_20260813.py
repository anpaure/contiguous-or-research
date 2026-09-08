#!/usr/bin/env python3
"""Audit g(D) >= 2*(m-peaks(D))+1 for PBBS omitted-label returns.

This implements the rooted-Dyck skew product from
MATH_ATTACK_H_PBBS_CATALAN_PACKING_DECISION_20260725.md:

    (u,D) -> (u + delta(D) mod 2m+1, phi(D)).

For each quotient phi-cycle, one lifted component is materialized and the
cyclic gap from every omitted-label occurrence to the next occurrence of
the same physical label is measured.  Other lifted components are spatial
translations and have the same gap spectrum.

Substantial instances must be run on h100, not on the local Mac.
"""

from __future__ import annotations

import argparse
import json
import math
import time
from collections import Counter, defaultdict


def dyck_words(m: int):
    def rec(pos: int, height: int, ones: int, bits: list[str]):
        if pos == 2 * m:
            if height == 0:
                yield "".join(bits)
            return
        if ones < m:
            bits.append("1")
            yield from rec(pos + 1, height + 1, ones + 1, bits)
            bits.pop()
        zeros = pos - ones
        if zeros < ones:
            bits.append("0")
            yield from rec(pos + 1, height - 1, ones, bits)
            bits.pop()

    yield from rec(0, 0, 0, [])


def phi_delta(word: str) -> tuple[str, int]:
    height = 0
    max_height = 0
    marked = None
    for i, bit in enumerate(word):
        height += 1 if bit == "1" else -1
        if height > max_height:
            max_height = height
            marked = i
    assert marked is not None and word[marked] == "1"
    p = word[:marked]
    q = word[marked + 1 :]
    flip = str.maketrans("01", "10")
    out = q.translate(flip) + "0" + p.translate(flip)
    return out, marked + 1


def peaks(word: str) -> int:
    return sum(word[i : i + 2] == "10" for i in range(len(word) - 1))


def audit(m: int) -> dict:
    started = time.time()
    n = 2 * m + 1
    words = list(dyck_words(m))
    index = {word: i for i, word in enumerate(words)}
    nxt = [0] * len(words)
    delta = [0] * len(words)
    defect = [m - peaks(word) for word in words]
    for i, word in enumerate(words):
        out, step = phi_delta(word)
        nxt[i] = index[out]
        delta[i] = step
        assert defect[nxt[i]] == defect[i]

    seen = [False] * len(words)
    quotient_cycles = []
    all_gap_hist = Counter()
    by_defect = defaultdict(Counter)
    violations = []
    equality_examples = []
    minimum_margin = None

    for seed in range(len(words)):
        if seen[seed]:
            continue
        cyc = []
        cur = seed
        while not seen[cur]:
            seen[cur] = True
            cyc.append(cur)
            cur = nxt[cur]
        assert cur == seed
        p = len(cyc)
        voltage = sum(delta[i] for i in cyc) % n
        lift_mult = n // math.gcd(n, voltage)
        length = p * lift_mult

        residues = [0] * length
        residue = 0
        for t in range(length):
            residues[t] = residue
            residue = (residue + delta[cyc[t % p]]) % n
        assert residue == 0

        positions = defaultdict(list)
        for t, residue in enumerate(residues):
            positions[residue].append(t)
        next_gap = [None] * length
        for pp in positions.values():
            for a, b in zip(pp, pp[1:] + [pp[0] + length]):
                next_gap[a] = b - a

        d = defect[cyc[0]]
        assert all(defect[i] == d for i in cyc)
        # Each quotient phase appears lift_mult times.  Translation by one
        # quotient lap preserves its next-return gap, but audit all copies.
        for t, gap in enumerate(next_gap):
            assert gap is not None
            phase = cyc[t % p]
            bound = 2 * defect[phase] + 1
            margin = gap - bound
            minimum_margin = margin if minimum_margin is None else min(minimum_margin, margin)
            all_gap_hist[gap] += 1
            by_defect[d][gap] += 1
            if gap == bound and len(equality_examples) < 20:
                equality_examples.append({
                    "word": words[phase], "defect": d, "gap": gap,
                    "quotient_period": p, "voltage": voltage,
                })
            if gap < bound and len(violations) < 100:
                violations.append({
                    "word": words[phase], "defect": defect[phase],
                    "gap": gap, "bound": bound, "margin": margin,
                    "quotient_period": p, "voltage": voltage,
                    "delta": delta[phase],
                })

        quotient_cycles.append({
            "period": p,
            "voltage": voltage,
            "lift_multiplier": lift_mult,
            "defect": d,
        })

    return {
        "m": m,
        "n": n,
        "catalan": len(words),
        "quotient_cycles": len(quotient_cycles),
        "quotient_period_hist": dict(sorted(Counter(x["period"] for x in quotient_cycles).items())),
        "lift_occurrences_audited": sum(
            x["period"] * x["lift_multiplier"] for x in quotient_cycles
        ),
        "gap_hist": dict(sorted(all_gap_hist.items())),
        "gap_hist_by_defect": {
            str(d): dict(sorted(hist.items())) for d, hist in sorted(by_defect.items())
        },
        "minimum_margin_g_minus_2d_plus_1": minimum_margin,
        "violation_count_capped": len(violations),
        "violations": violations,
        "equality_examples": equality_examples,
        "seconds": time.time() - started,
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("m", type=int)
    ap.add_argument("--json")
    args = ap.parse_args()
    result = audit(args.m)
    payload = json.dumps(result, indent=2, sort_keys=True)
    print(payload)
    if args.json:
        with open(args.json, "w", encoding="utf-8") as out:
            out.write(payload + "\n")


if __name__ == "__main__":
    main()
