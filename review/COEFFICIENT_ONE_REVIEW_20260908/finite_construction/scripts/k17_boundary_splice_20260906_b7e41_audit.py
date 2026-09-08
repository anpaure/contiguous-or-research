#!/usr/bin/env python3
"""Boundary-splice audit; answers/k16.word is the sole word input.

All intervals use zero-based, half-open endpoints. --word optionally retains
the fully verified construction; an existing different body is never replaced.

GENERAL CRITERION
Let C(A) be the nonempty interval ORs of A, and P(A), S(A) its prefix and
suffix ORs, including the empty choice 0. Write F | G for the set of all
f | g, with f in F and g in G. For an old-bit word X, a new bit z, and an
old-bit bridge B, put Y = reverse(X[p:]) + [z] + B + mark(X[q:]). Set
L = P(X[p:]), R = P(X[q:]) - {0}, and b = OR(B). The exact low masks of
marked intervals not wholly inside the marked tail are

    K = (L | P(B)) union ((S(B) - {0}) | R) union (L | {b} | R).

Indeed these are respectively intervals containing z but not the tail,
intervals starting in B and entering the tail, and intervals containing z
and entering the tail. Unmarked intervals lie inside one of the two old-bit
blocks. Thus, for a universal X and D_r = [1, 2**k) minus C(X[r:]), Y is
universal iff D_p <= C(B) and D_q union {0} <= K. Each D_r is contained in
the at most r*k distinct ORs of intervals starting before r. Supplying an
unchanged-tail or boundary witness for those signatures is sufficient;
one need not replay Y or supply it as an additional external witness.

CONCRETE POSITIVE PROOF
Write a,b,c,d = X[:4], u = a|b, v = c|d. Here c <= u in bit inclusion.
The finite ledger below proves every old prefix lost from X[1:] is either
retained elsewhere or equals u or u|v. After index 9, a is absorbed by
OR(X[1:10]). The exceptional one-letter source intervals a and c have
witnesses wholly in X[3:]. For a marked target, choose any source witness
X[i:j]. If i >= 3 use its marked copy; if i == 1 use the reversed left
suffix and z. If i == 2, use the alternate c witness when j == 3, otherwise
v + mark(X[3:j]). If i == 0, use the alternate a witness when j == 1,
z,u when j is 2 or 3, and z,u,v + mark(X[3:j]) when j >= 4. The singleton
z is already present. This proves length 2*12873 - 1 without a new word body.

SCOPE OF THE NEGATIVE RESULT
No strictly shorter word reverse(X[p:])+[z]+B+mark(X[q:]) with len(B)<=2
is universal. This is not an unrestricted lower bound for nu(17).
For p>=2 the five defects D_2 exceed the three interval ORs of B. For
p==1 the two nested defects force len(B)==2 and one letter equal to 50122.
A shorter word then has q>=4. The incomparable tail defects 41833,41834
avoid bit 16384, present in both X[1] and 50122. Their boundary witnesses
would therefore have to come from at most one OR chain, which is impossible.
For p==0, targets avoiding bit 128 cannot meet the reversed left copy.
Outside the marked tail, m bridge letters provide at most m OR chains:
the chain starting at z, and suffix-of-B plus prefix-of-tail chains starting
at B[1],...,B[m-1]. For m==0 the only nonzero low masks already occur in
the tail. The audit checks antichains of sizes 1,2,3 in D_2,D_3,D_4,
respectively, all avoiding bit 128. These rule out the requisite cuts.

The maximum-start recurrence in witnesses() proves the tail-defect ledger:
at each endpoint it keeps the largest start for each suffix OR, then the
largest start over all endpoints. A mask occurs in X[q:] iff this maximum
is at least q. The small self-test checks this and the general criterion
against explicit nonwrapping interval enumeration.
"""

import argparse
from functools import reduce
from hashlib import sha256
import json
from operator import or_
from pathlib import Path
from random import Random


SOURCE_SHA = "890ac346ce142f5f9ed564d487ff3e2fb99aea93ae2c104ec13765fa5d3814fe"
REPLAY_SHA = "ef69969f6f72bc85173c9ccb413b7c111a398e725b956f2a91cbe5decbabca38"


def union(word):
    return reduce(or_, word, 0)


def witnesses(word):
    """One witness with largest possible start for every interval OR."""
    ending, best = {}, {}
    for j, x in enumerate(word):
        new = {x: j}
        for value, start in ending.items():
            value |= x
            new[value] = max(new.get(value, -1), start)
        for value, start in new.items():
            if value not in best or start > best[value][0]:
                best[value] = (start, j + 1)
        ending = new
    return best


def prefixes(word):
    result, value = {0}, 0
    for x in word:
        value |= x
        result.add(value)
    return result


def marked_boundary(left_prefixes, right_prefixes, bridge):
    """Low masks of all marked intervals not wholly in the marked tail."""
    bp = prefixes(bridge)
    bs = prefixes(bridge[::-1]) - {0}
    rp = right_prefixes - {0}
    total = union(bridge)
    return (
        {l | b for l in left_prefixes for b in bp}
        | {b | r for b in bs for r in rp}
        | {l | total | r for l in left_prefixes for r in rp}
    )


def self_test():
    rng = Random(20260906)
    for _ in range(1000):
        k, n = rng.randrange(1, 5), rng.randrange(1, 9)
        z = 1 << k
        x = [rng.randrange(1, z) for _ in range(n)]
        p, q = rng.randrange(n + 1), rng.randrange(n + 1)
        bridge = [rng.randrange(1, z) for _ in range(rng.randrange(3))]
        brute = {}
        for i in range(n):
            for j in range(i + 1, n + 1):
                mask = union(x[i:j])
                brute[mask] = max(brute.get(mask, -1), i)
        assert {mask: i for mask, (i, _) in witnesses(x).items()} == brute
        y = x[p:][::-1] + [z] + bridge + [a | z for a in x[q:]]
        actual = {union(y[i:j]) for i in range(len(y)) for j in range(i + 1, len(y) + 1)}
        low = set(witnesses(x[p:])) | set(witnesses(bridge))
        high = set(witnesses(x[q:])) | marked_boundary(prefixes(x[p:]), prefixes(x[q:]), bridge)
        assert actual == low | {z | a for a in high}
    print("PASS: 1000 small maximum-start and boundary-formula checks")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", nargs="?", type=Path,
                         default=Path(__file__).resolve().parents[1] / "answers/k16.word")
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--word", type=Path, help="retain the verified 25745-letter word")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return
    raw = args.source.read_bytes()
    assert sha256(raw).hexdigest() == SOURCE_SHA
    x = [int(token) for token in raw.split()]
    assert len(x) == 12873 and all(0 < a < 65536 for a in x)
    best = witnesses(x)
    assert set(best) == set(range(1, 65536))
    defects = {p: sorted(mask for mask, (i, _) in best.items() if i < p)
               for p in range(5)}
    bridge = [50122, 33642]
    assert x[:4] == [50120, 49994, 33610, 33640]
    assert bridge == [x[0] | x[1], x[2] | x[3]]
    assert x[2] | bridge[0] == bridge[0]

    # These seven identities and absorption suffice for the positive proof.
    source_ledger = {
        50120: (1715, 1717),
        58346: (165, 170),
        58347: (5931, 5937),
        58351: (6389, 6397),
        62447: (6389, 6399),
        63471: (1, 10),
        33610: (4489, 4490),
    }
    for mask, (i, j) in source_ledger.items():
        assert 1 <= i < j <= len(x) and union(x[i:j]) == mask
    assert all(source_ledger[a][0] >= 3 for a in (x[0], x[2]))
    assert x[0] | union(x[1:10]) == union(x[1:10]) == 63471
    running, boundary = 0, {}
    for j, a in enumerate(x[:9]):
        running |= a
        boundary.setdefault(running, [0, j + 1])
    assert set(boundary) <= set(source_ledger) | set(witnesses(bridge))

    assert set(defects[1]) <= set(witnesses(bridge))
    assert set(defects[3]) | {0} <= marked_boundary(prefixes(x[1:]), prefixes(x[3:]), bridge)
    y = x[1:][::-1] + [65536] + bridge + [a | 65536 for a in x[3:]]
    assert len(y) == 25745
    assert sha256((" ".join(map(str, y)) + "\n").encode()).hexdigest() == REPLAY_SHA
    assert set(witnesses(y)) == set(range(1, 131072))

    assert defects[1] == [50122, 50154]
    assert defects[2] == [49994, 50026, 50122, 50154, 58218]
    antichains = [(2, [49994]), (3, [33642, 49994]), (4, [41833, 41834, 50026])]
    for q, masks in antichains:
        assert all(best[a][0] < q and not a & 128 for a in masks)
        assert all((a | b) not in (a, b) for a in masks for b in masks if a != b)
    assert x[0] & 128 and x[1] & 16384 and bridge[0] & 16384
    assert all(best[a][0] < 4 and not a & 16384 for a in (41833, 41834))

    # The two unmarked defects force B=(u,t) or (t,u), t<=50154, t&32.
    profiles = {p: prefixes(x[p:]) for p in range(5)}
    accepted, trials, t = {3: [], 4: []}, 0, 50154
    while t:
        if t & 32:
            for b in ((50122, t), (t, 50122)):
                trials += 1
                for q in accepted:
                    if set(defects[q]) <= marked_boundary(profiles[1], profiles[q], b):
                        accepted[q].append(b)
        t = (t - 1) & 50154
    assert trials == 512 and len(accepted[3]) == 32 and not accepted[4]
    assert all(u == 50122 and t & 34 == 34 and t | 33642 == 33642 for u, t in accepted[3])
    lean = x[1:][::-1] + [65536, 50122, 34] + [a | 65536 for a in x[3:]]
    assert set(witnesses(lean)) == set(range(1, 131072))

    if args.word is not None:
        payload = (" ".join(map(str, y)) + "\n").encode()
        if args.word.exists():
            assert args.word.read_bytes() == payload, "refuse to replace a different word"
        else:
            with args.word.open("xb") as output:
                output.write(payload)

    print(json.dumps({
        "status": "PASS", "source_sha256": SOURCE_SHA,
        "replay_sha256": REPLAY_SHA, "length": len(y),
        "source_first_16": x[:16], "source_last_16": x[-16:],
        "prefix_absorption_index": 9,
        "unmarked_prefix_ledger": boundary,
        "source_interval_ledger": {
            mask: {"interval": [i, j], "letters": x[i:j]}
            for mask, (i, j) in source_ledger.items()
        },
        "suffix_defects": defects,
        "negative_maximum_start_ledger": {
            a: best[a] for a in sorted({*defects[2], 33642, 41833, 41834})
        },
        "boundary_only_pairs_checked": trials,
        "accepted_pairs_at_q3": len(accepted[3]),
        "accepted_pairs_at_q4": len(accepted[4]),
        "same_length_lean_bridge": [50122, 34],
        "further_length_improvement": False,
        "negative_scope": "Only reverse(X[p:])+[z]+B+mark(X[q:]), len(B)<=2",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
