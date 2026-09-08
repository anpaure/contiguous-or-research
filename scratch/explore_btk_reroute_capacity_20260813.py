#!/usr/bin/env python3
"""Exact BTK forest degree and fresh-lower reroute capacity census."""

from collections import Counter
from itertools import combinations


def sets(n, w):
    for cc in combinations(range(n), w):
        x = 0
        for i in cc:
            x |= 1 << i
        yield x


def scd_down(x, n):
    stack = []
    free_ones = []
    for i in range(n):
        if ((x >> i) & 1) == 0:
            stack.append(i)
        elif stack:
            stack.pop()
        else:
            free_ones.append(i)
    if not free_ones:
        return None
    return x ^ (1 << free_ones[-1])


def main():
    for r in range(2, 10):
        n = 2 * r - 1
        all_lowers = set(sets(n, r - 1))
        used_lowers = set()
        edge_of_upper = {}
        for u in sets(n, r + 1):
            a = scd_down(u, n)
            lo = scd_down(a, n)
            y = u ^ a
            b = lo | y
            assert a & b == lo and a | b == u
            used_lowers.add(lo)
            edge_of_upper[u] = (a, b, lo)
        fresh = all_lowers - used_lowers
        deg = Counter(z for a, b, lo in edge_of_upper.values() for z in (a, b))
        excess = sum(max(0, d - 2) for d in deg.values())
        overloaded = [a for a, d in deg.items() if d > 2]
        # For each overloaded incidence U-A, count fresh L' subset U avoiding A.
        caps = []
        for a in overloaded:
            for u, (x, y, lo) in edge_of_upper.items():
                if a not in (x, y):
                    continue
                opts = []
                bits = [i for i in range(n) if (u >> i) & 1]
                for cc in combinations(bits, r - 1):
                    ll = 0
                    for i in cc:
                        ll |= 1 << i
                    if ll in fresh and ll != lo and ll & a != ll:
                        opts.append(ll)
                caps.append(len(opts))
        print(r, "W", len(all_lowers), "U", len(edge_of_upper),
              "fresh", len(fresh), "over", len(overloaded), "excess", excess,
              "reroute_min", min(caps, default=0), "reroute_avg", round(sum(caps)/len(caps),2) if caps else 0,
              "hist", dict(sorted(Counter(deg.values()).items())))


if __name__ == "__main__":
    main()
