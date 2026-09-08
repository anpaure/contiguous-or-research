#!/usr/bin/env python3
"""Verifier for floored multi-rank covering witnesses.

Usage: python3 verify_witness.py <witness_file>

Witness file format: first line "n GAP k1,k2,..."; second line the
cyclic word as space-separated integers.  Checks: (i) every cyclic
letter-gap >= GAP; (ii) for each k in the list, the k-windows (as
sets; windows with a repeated letter are skipped) cover ALL
C(n,k) k-subsets of {0..n-1}.  Exits 0 and prints PASS iff all
checks hold.
"""
import itertools
import sys


def main():
    path = sys.argv[1]
    with open(path) as f:
        header = f.readline().split()
        n, gap = int(header[0]), int(header[1])
        ks = [int(x) for x in header[2].split(",")]
        w = [int(x) for x in f.readline().split()]
    L = len(w)
    print(f"n={n} GAP={gap} ks={ks} L={L}")
    ok = True
    for x in range(n):
        ps = [i for i, y in enumerate(w) if y == x]
        if not ps:
            print(f"FAIL: letter {x} absent")
            ok = False
            continue
        gaps = [b - a for a, b in zip(ps, ps[1:] + [ps[0] + L])]
        if min(gaps) < gap:
            print(f"FAIL: letter {x} has gap {min(gaps)} < {gap}")
            ok = False
    for k in ks:
        seen = set()
        for p in range(L):
            s = frozenset(w[(p + t) % L] for t in range(k))
            if len(s) == k:
                seen.add(s)
        total = len(list(itertools.combinations(range(n), k)))
        print(f"  k={k}: {len(seen)}/{total} covered")
        if len(seen) != total:
            ok = False
    print("PASS" if ok else "FAIL")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
