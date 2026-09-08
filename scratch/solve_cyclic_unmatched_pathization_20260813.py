#!/usr/bin/env python3
"""SAT test: choose one of three cyclic-unmatched diamonds per upper colour."""

import argparse
import subprocess
import tempfile
from collections import defaultdict, Counter
from itertools import combinations
from pathlib import Path


def sets(n, w):
    for cc in combinations(range(n), w):
        yield sum(1 << i for i in cc)


def free_ones(x, n):
    h = 0
    vals = [0]
    for i in range(n):
        h += 1 if (x >> i) & 1 else -1
        vals.append(h)
    start = max(i for i, v in enumerate(vals[:-1]) if v == max(vals[:-1])) % n
    stack = []
    free = []
    for jj in range(n):
        i = (start + jj) % n
        if ((x >> i) & 1) == 0:
            stack.append(i)
        elif stack:
            stack.pop()
        else:
            free.append(i)
    assert not stack and len(free) == 3
    return free


def options(r):
    n = 2 * r - 1
    ret = []
    for ui, u in enumerate(sets(n, r + 1)):
        ff = free_ones(u, n)
        for rule in range(3):
            drop = [ff[(rule + j) % 3] for j in range(2)]
            lo = u ^ (1 << drop[0]) ^ (1 << drop[1])
            a = lo | (1 << drop[0])
            b = lo | (1 << drop[1])
            ret.append((ui, rule, lo, a, b))
    return ret


def cycles(selected, opts):
    adj = defaultdict(list)
    for oi in selected:
        a, b = opts[oi][3:]
        adj[a].append((b, oi)); adj[b].append((a, oi))
    seen = set(); found = []
    for v in list(adj):
        if v in seen:
            continue
        comp_v = set(); comp_e = set(); stack = [v]; seen.add(v)
        while stack:
            x = stack.pop(); comp_v.add(x)
            for y, oi in adj[x]:
                comp_e.add(oi)
                if y not in seen:
                    seen.add(y); stack.append(y)
        if len(comp_e) == len(comp_v):
            found.append(sorted(comp_e))
    return found


def solve(r):
    opts = options(r)
    by_u = defaultdict(list); by_l = defaultdict(list); by_m = defaultdict(list)
    for oi, (u, rule, lo, a, b) in enumerate(opts):
        lit = oi + 1
        by_u[u].append(lit); by_l[lo].append(lit)
        by_m[a].append(lit); by_m[b].append(lit)
    clauses = []
    for vv in by_u.values():
        clauses.append(vv)
        for a, b in combinations(vv, 2): clauses.append([-a, -b])
    for vv in by_l.values():
        for a, b in combinations(vv, 2): clauses.append([-a, -b])
    for vv in by_m.values():
        for abc in combinations(vv, 3): clauses.append([-x for x in abc])
    for rnd in range(100):
        with tempfile.TemporaryDirectory() as td:
            cnf = Path(td) / "x.cnf"; out = Path(td) / "x.out"
            with cnf.open("w") as f:
                f.write(f"p cnf {len(opts)} {len(clauses)}\n")
                for cc in clauses: f.write(" ".join(map(str, cc)) + " 0\n")
            proc = subprocess.run(["kissat", str(cnf)], capture_output=True, text=True)
            if proc.returncode == 20:
                return None, rnd, len(clauses)
            vals = []
            for line in proc.stdout.splitlines():
                if line.startswith("v "):
                    vals.extend(int(x) for x in line.split()[1:] if x != "0")
            selected = {x - 1 for x in vals if x > 0 and x <= len(opts)}
        bad = cycles(selected, opts)
        if not bad:
            return selected, rnd, len(clauses)
        clauses.extend([[-(oi + 1) for oi in cc] for cc in bad])
    raise RuntimeError("round limit")


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("r", type=int); args = ap.parse_args()
    opts = options(args.r)
    sol, rounds, nc = solve(args.r)
    if sol is None:
        print("UNSAT", args.r, rounds, nc); return
    hist = Counter(opts[oi][1] for oi in sol)
    print("SAT", args.r, "rounds", rounds, "clauses", nc, "rules", dict(hist))


if __name__ == "__main__": main()
