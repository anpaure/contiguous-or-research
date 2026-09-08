#!/usr/bin/env python3
"""Search small lower-complete Johnson Hamilton cycles for mixed-C4 cuts.

Run on H100 only.  The exhaustive m=2 mode fixes one starting vertex and
one orientation representative.  A bounded m=3 randomized mode is also
provided for witness mining; it makes no completeness claim.
"""

from __future__ import annotations

import argparse
import itertools
import json
import random
from collections import Counter, defaultdict


def bits(s):
    return tuple(i for i in range(64) if (s >> i) & 1)


def lower_edge(x, y):
    return x & y


def label_edge(x, y, r):
    return ((x ^ r).bit_length() - 1, (y ^ r).bit_length() - 1)


def cycle_data(cycle, n, m):
    hs = defaultdict(set)
    loads = Counter()
    edge_set = set()
    for i, x in enumerate(cycle):
        y = cycle[(i + 1) % len(cycle)]
        e = tuple(sorted((x, y)))
        edge_set.add(e)
        r = lower_edge(x, y)
        loads[r] += 1
        a, b = label_edge(x, y, r)
        hs[r].add(tuple(sorted((a, b))))
    lowers = [sum(1 << i for i in c) for c in itertools.combinations(range(n), m - 1)]
    if any(loads[r] == 0 for r in lowers):
        return None
    d = {r: loads[r] - 1 for r in lowers}
    point = [sum(v for r, v in d.items() if (r >> i) & 1) for i in range(n)]
    return hs, loads, d, point, edge_set


def mixed_occurrences(cycle, n, m):
    data = cycle_data(cycle, n, m)
    if data is None:
        return None
    hs, loads, d, point, edge_set = data
    occ = []
    legal = []
    pos_in_cycle = []
    full = (1 << n) - 1
    for bset, surplus in d.items():
        if surplus <= 0:
            continue
        for b in bits(bset):
            k = bset ^ (1 << b)
            for uv in hs[bset]:
                for p, a in (uv, uv[::-1]):
                    assert p not in bits(bset) and a not in bits(bset)
                    pset = k | (1 << p)
                    for ac in hs[pset]:
                        if a not in ac:
                            continue
                        c = ac[0] if ac[1] == a else ac[1]
                        if c == b:
                            continue
                        owners = (
                            k | (1 << p) | (1 << a),
                            k | (1 << p) | (1 << c),
                            k | (1 << p) | (1 << b),
                            k | (1 << a) | (1 << b),
                        )
                        neg = {tuple(sorted((owners[0], owners[1]))), tuple(sorted((owners[2], owners[3])))}
                        pos = {tuple(sorted((owners[1], owners[2]))), tuple(sorted((owners[3], owners[0])))}
                        assert neg <= edge_set
                        rec = dict(B=bset, b=b, p=p, a=a, c=c, A=k | (1 << a), owners=owners)
                        occ.append(rec)
                        if pos & edge_set:
                            pos_in_cycle.append(rec)
                            continue
                        # Removing two cycle edges gives two paths.  The new
                        # matching is Hamilton-safe iff its union with the
                        # retained endpoint pairing is a 4-cycle.  Directly
                        # check connectedness of the switched graph.
                        switched = (edge_set - neg) | pos
                        adj = defaultdict(list)
                        for x, y in switched:
                            adj[x].append(y)
                            adj[y].append(x)
                        seen = set()
                        stack = [cycle[0]]
                        while stack:
                            x = stack.pop()
                            if x in seen:
                                continue
                            seen.add(x)
                            stack.extend(adj[x])
                        if len(seen) == len(cycle) and all(len(adj[x]) == 2 for x in cycle):
                            legal.append(rec)
    return dict(hs=hs, loads=loads, d=d, point=point, occ=occ, legal=legal, pos_in_cycle=pos_in_cycle)


def serial_cycle(cycle, data):
    def ss(x):
        return list(bits(x))
    return dict(
        cycle=[ss(x) for x in cycle],
        loads={str(ss(r)): v for r, v in sorted(data["loads"].items())},
        surplus={str(ss(r)): v for r, v in sorted(data["d"].items())},
        point=data["point"],
        occurrence_count=len(data["occ"]),
        legal_count=len(data["legal"]),
    )


def exhaustive_m2(stop_first):
    n, m = 5, 2
    verts = [sum(1 << i for i in c) for c in itertools.combinations(range(n), m)]
    adj = {x: [y for y in verts if (x ^ y).bit_count() == 2] for x in verts}
    start = verts[0]
    second = min(adj[start])
    path = [start, second]
    used = {start, second}
    counts = Counter()
    witnesses = {}

    def visit():
        if len(path) == len(verts):
            if start not in adj[path[-1]]:
                return False
            data = mixed_occurrences(tuple(path), n, m)
            if data is None:
                return False
            counts["lower_complete"] += 1
            regular = len(set(data["point"])) == 1
            if not regular:
                counts["point_nonregular"] += 1
                old = counts.get("min_occ", 10**18)
                if len(data["occ"]) < old:
                    counts["min_occ"] = len(data["occ"])
                    witnesses["min_occ"] = serial_cycle(path, data)
                old = counts.get("min_legal", 10**18)
                if len(data["legal"]) < old:
                    counts["min_legal"] = len(data["legal"])
                    witnesses["min_legal"] = serial_cycle(path, data)
                if not data["occ"]:
                    counts["nonregular_zero_occ"] += 1
                    witnesses.setdefault("nonregular_zero_occ", serial_cycle(path, data))
                if not data["legal"]:
                    counts["nonregular_zero_legal"] += 1
                    witnesses.setdefault("nonregular_zero_legal", serial_cycle(path, data))
            return stop_first and "nonregular_zero_occ" in witnesses
        prev = path[-1]
        for nxt in adj[prev]:
            if nxt in used:
                continue
            used.add(nxt)
            path.append(nxt)
            if visit():
                return True
            path.pop()
            used.remove(nxt)
        return False

    visit()
    return counts, witnesses


def randomized_m3(trials, seed):
    n, m = 7, 3
    rng = random.Random(seed)
    verts = [sum(1 << i for i in c) for c in itertools.combinations(range(n), m)]
    adj = {x: [y for y in verts if (x ^ y).bit_count() == 2] for x in verts}
    counts = Counter()
    witnesses = {}
    for _ in range(trials):
        start = rng.choice(verts)
        path = [start]
        used = {start}
        # Warnsdorff-style randomized Hamilton DFS, bounded restarts.
        while len(path) < len(verts):
            cand = [y for y in adj[path[-1]] if y not in used]
            if len(path) == len(verts) - 1:
                cand = [y for y in cand if start in adj[y]]
            if not cand:
                break
            rng.shuffle(cand)
            cand.sort(key=lambda y: sum(z not in used for z in adj[y]))
            y = cand[0]
            path.append(y)
            used.add(y)
        if len(path) != len(verts) or start not in adj[path[-1]]:
            continue
        counts["hamilton"] += 1
        data = mixed_occurrences(tuple(path), n, m)
        if data is None:
            continue
        counts["lower_complete"] += 1
        regular = len(set(data["point"])) == 1
        if not regular:
            counts["point_nonregular"] += 1
            old = counts.get("min_occ", 10**18)
            if len(data["occ"]) < old:
                counts["min_occ"] = len(data["occ"])
                witnesses["min_occ"] = serial_cycle(path, data)
            old = counts.get("min_legal", 10**18)
            if len(data["legal"]) < old:
                counts["min_legal"] = len(data["legal"])
                witnesses["min_legal"] = serial_cycle(path, data)
            if not data["occ"]:
                counts["nonregular_zero_occ"] += 1
                witnesses.setdefault("nonregular_zero_occ", serial_cycle(path, data))
            if not data["legal"]:
                counts["nonregular_zero_legal"] += 1
                witnesses.setdefault("nonregular_zero_legal", serial_cycle(path, data))
    return counts, witnesses


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--m", type=int, choices=(2, 3), required=True)
    ap.add_argument("--trials", type=int, default=100000)
    ap.add_argument("--seed", type=int, default=20260814)
    ap.add_argument("--stop-first", action="store_true")
    ap.add_argument("--output")
    args = ap.parse_args()
    if args.m == 2:
        counts, witnesses = exhaustive_m2(args.stop_first)
    else:
        counts, witnesses = randomized_m3(args.trials, args.seed)
    result = dict(m=args.m, counts=dict(counts), witnesses=witnesses)
    blob = json.dumps(result, sort_keys=True, indent=2)
    print(blob)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(blob + "\n")


if __name__ == "__main__":
    main()
