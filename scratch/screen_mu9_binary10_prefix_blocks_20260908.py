#!/usr/bin/env python3
"""H100-only finite local screen; no solver and no partition search."""
from collections import Counter
from itertools import permutations
from math import comb, factorial
from pathlib import Path
import json
import resource
import socket
import sys
import time

FULL9, PIVOT, N = 511, 1 << 9, 126


def rotate(mask, step):
    step %= 9
    return ((mask << step) & FULL9) | (mask >> (9-step) if step else 0)


def bits(mask):
    return [i for i in range(9) if mask & (1 << i)]


def prefix_deck(left, right):
    lp = [0]
    rp = [0]
    for x in left:
        lp.append(lp[-1] | (1 << x))
    for x in right:
        rp.append(rp[-1] | (1 << x))
    return [a | b for a in lp for b in rp]


def make_block(start, p, S, U, V):
    ss = [S[(start+j) % N] for j in range(p)]
    bset = U[(start-1) % N]
    adds = [ss[j+1] & ~ss[j] for j in range(p-1)]
    removes = [ss[j] & ~ss[j+1] for j in range(p-1)]
    b5 = bset & ~ss[0]
    common = FULL9
    for mask in ss:
        common &= mask
    reasons = []
    if any(mask.bit_count() != 1 for mask in adds + removes + [b5]):
        reasons.append("nonsingleton_difference")
    if common.bit_count() != 5-p:
        reasons.append("wrong_common_intersection_rank")
    if reasons:
        return {"start": start, "p": p, "valid": False, "reasons": reasons}
    ac = [bits(mask)[0] for mask in adds]
    bc = bits(common) + [bits(mask)[0] for mask in reversed(removes)] + bits(b5)
    used = set(ac + bc)
    cc = sorted(set(range(9)) - used)
    if len(ac + bc) != len(used) or len(bc) != 5 or len(cc) != 5-p:
        reasons.append("coordinate_collision_or_wrong_shore_size")
    if reasons:
        return {"start": start, "p": p, "valid": False, "reasons": reasons}
    left = ac + [9] + cc
    deck = prefix_deck(left, bc)
    expected4 = set(ss)
    expected5 = {U[(start+j-1) % N] for j in range(p)}
    expected6 = {V[(start+j-2) % N] for j in range(1, p)}
    actual = {rank: {x for x in deck if not x & PIVOT and x.bit_count() == rank}
              for rank in (4, 5, 6)}
    for rank, expected in ((4, expected4), (5, expected5), (6, expected6)):
        if actual[rank] != expected or len(expected) != (p if rank < 6 else p-1):
            reasons.append("rank_%d_deck_mismatch" % rank)
    return {"start": start, "p": p, "valid": not reasons, "reasons": reasons,
            "left": left, "right": bc, "common": bits(common), "c": cc,
            "free_choices": factorial(5-p)**2,
            "fixed_no_z_rank6": sorted(actual[6]),
            "covered_V_indices": [(start+j-2) % N for j in range(1, p)],
            "dropped_V_index_after_block": (start+p-2) % N}


def main():
    assert socket.gethostname().lower() == "arboghast", "Run only via ssh h100"
    resource.setrlimit(resource.RLIMIT_CPU, (10, 10))
    resource.setrlimit(resource.RLIMIT_AS, (256 << 20, 256 << 20))
    started = time.monotonic()
    final_word = [int(x) for x in Path(sys.argv[1]).read_text().split()]
    seed = [3,18,130,258,264,72,96,36,33,48,24,272,144,192]
    parent = [rotate(seed[i],5*t) for t in range(9) for i in range(14)]
    assert len(final_word) == len(parent) == N
    def windows(word, length):
        out = []
        for start in range(N):
            mask = 0
            for j in range(length):
                mask |= word[(start+j) % N]
            out.append(mask)
        return out
    for length in range(2, N+1):
        assert windows(final_word, length) == windows(parent, length)
    S, U, V = [windows(parent, length) for length in (3,4,5)]
    assert len(set(S)) == comb(9,4) and {x.bit_count() for x in S} == {4}
    assert len(set(U)) == comb(9,5) and {x.bit_count() for x in U} == {5}
    wanted6 = {x for x in range(512) if x.bit_count() == 6}
    fixed = []
    for e in range(3):
        blocks = [make_block(t,3,S,U,V) for t in range(e,N,3)]
        all6, all_decks, candidates = set(), [], 0
        for b in blocks:
            if not b["valid"]:
                continue
            outcomes = set()
            for common in permutations(b["common"]):
                for cc in permutations(b["c"]):
                    left = b["left"][:3] + list(cc)
                    right = list(common) + b["right"][2:]
                    deck = prefix_deck(left,right)
                    no6 = frozenset(x for x in deck if not x & PIVOT and x.bit_count()==6)
                    assert no6 == frozenset(b["fixed_no_z_rank6"])
                    outcomes.add(no6)
                    candidates += 1
                    all_decks.extend(deck)
            assert len(outcomes) == 1
            all6.update(b["fixed_no_z_rank6"])
        selected_indices = [(t+j) % N for t in range(e,N,3) for j in (-1,0)]
        selected6 = {V[i] for i in selected_indices if V[i].bit_count() == 6}
        fixed.append({"offset": e, "blocks": len(blocks),
                      "valid_blocks": sum(b["valid"] for b in blocks),
                      "invalid_blocks": [b for b in blocks if not b["valid"]],
                      "candidates_checked": candidates,
                      "actual_fixed_no_z_rank6_covered": len(all6),
                      "missing_rank6": sorted(wanted6-all6),
                      "selected_V_rank6_count_without_realizability": len(selected6),
                      "all_choices_union_missing_by_rank":
                          {rank: sum(x.bit_count()==rank and x not in set(all_decks)
                                     for x in range(1024)) for rank in range(11)},
                      "necessary_screen_pass": all(b["valid"] for b in blocks) and all6==wanted6})
    variable = [make_block(t,p,S,U,V) for t in range(N) for p in range(1,6)]
    counts = Counter(V)
    report = {"host": socket.gethostname(), "elapsed_seconds": time.monotonic()-started,
              "scope": "fixed triples plus 630 local variable-length block checks; no partition search or solver",
              "S_unique": len(set(S)), "U_unique": len(set(U)),
              "V_rank_histogram": dict(Counter(x.bit_count() for x in V)),
              "V_distinct_rank6": len(set(V)&wanted6),
              "V_target_multiplicity_histogram": dict(Counter(counts.values())),
              "V_unique_occurrence_indices": [i for i,v in enumerate(V) if counts[v]==1],
              "fixed_triples": fixed,
              "variable_valid_by_p": {p: sum(b["valid"] and b["p"]==p for b in variable) for p in range(1,6)},
              "variable_blocks": variable,
              "V_masks": V}
    Path(sys.argv[2]).write_text(json.dumps(report,indent=2)+"\n")
    summary = dict(report)
    del summary["variable_blocks"]
    del summary["V_masks"]
    print(json.dumps(summary,indent=2))


if __name__ == "__main__":
    main()
