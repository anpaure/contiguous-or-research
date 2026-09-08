#!/usr/bin/env python3
"""Audit the four-insertion near-core curl under one master cyclic order.

All heavy parameter scans belong on h100.  The common (c-1)-core is
suppressed.  Labels a,p,x are the three possible last core roles; a
maximal rail with core role r uses the induced cyclic order Omega-r.
"""

from collections import Counter
from itertools import combinations
import argparse


def induced(order, deleted):
    deleted = set(deleted)
    return tuple(v for v in order if v not in deleted)


def deck(core_role, order, q):
    n = len(order)
    out = Counter()
    for i in range(n):
        w = frozenset(order[(i+j) % n] for j in range(q))
        assert len(w) == q
        out[frozenset((core_role,)) | w] += 1
    assert all(v == 1 for v in out.values())
    return out


def add(dst, src, coef):
    for key, val in src.items():
        dst[key] += coef * val
        if dst[key] == 0:
            del dst[key]


def delta(master, core_role, inserted, q):
    big_order = induced(master, (core_role,))
    small_order = induced(master, (core_role, inserted))
    ans = Counter()
    add(ans, deck(core_role, big_order, q), +1)
    add(ans, deck(core_role, small_order, q), -1)
    return ans


def curl(master, q):
    # (Delta_x^{D_p}-Delta_x^C)-(Delta_p^{D_x}-Delta_p^C)
    ans = Counter()
    add(ans, delta(master, "p", "x", q), +1)
    add(ans, delta(master, "a", "x", q), -1)
    add(ans, delta(master, "x", "p", q), -1)
    add(ans, delta(master, "a", "p", q), +1)
    return ans


def state_shores(master, q):
    """Whole-rail positive and negative owner multiplicities before cancellation."""
    pos = Counter()
    neg = Counter()
    terms = [
        (+1, "p", "x"), (-1, "a", "x"),
        (-1, "x", "p"), (+1, "a", "p"),
    ]
    for sign, core, ins in terms:
        big = deck(core, induced(master, (core,)), q)
        small = deck(core, induced(master, (core, ins)), q)
        if sign > 0:
            add(pos, big, +1); add(neg, small, +1)
        else:
            add(pos, small, +1); add(neg, big, +1)
    return pos, neg


def reduced_shores(master, q):
    """Cancel the identical two appearances of the core-a big rail."""
    pos = Counter()
    neg = Counter()
    # Positive: big(core p), small(core a, insert x),
    # small(core x, insert p).  Negative is the complementary three.
    for core, deleted in (("p", ("p",)),
                          ("a", ("a", "x")),
                          ("x", ("x", "p"))):
        add(pos, deck(core, induced(master, deleted), q), +1)
    for core, deleted in (("p", ("p", "x")),
                          ("x", ("x",)),
                          ("a", ("a", "p"))):
        add(neg, deck(core, induced(master, deleted), q), +1)
    return pos, neg


def audit(q, M):
    # |Omega|=M+1: common (c-1)-core has this complement.
    n = M + 1
    assert M >= q + 1
    fillers = [f"e{i}" for i in range(n - 3)]
    best = None
    hist = Counter()
    simple_count = 0
    whole_simple_count = 0
    reduced_simple_count = 0
    examples = []
    # Fix a at cyclic position zero.  Choose positions of p,x; fillers keep
    # their relative order, which exhausts structural role patterns.
    for pp, xp in combinations(range(1, n), 2):
        for ppos, xpos in ((pp, xp), (xp, pp)):
            order = []
            fi = 0
            for i in range(n):
                if i == 0: order.append("a")
                elif i == ppos: order.append("p")
                elif i == xpos: order.append("x")
                else:
                    order.append(fillers[fi]); fi += 1
            order = tuple(order)
            u = curl(order, q)
            lp = sum(v for v in u.values() if v > 0)
            ln = -sum(v for v in u.values() if v < 0)
            maxmult = max((abs(v) for v in u.values()), default=0)
            key = (lp, ln, len(u), maxmult)
            hist[key] += 1
            simple = maxmult <= 1
            simple_count += simple
            pos, neg = state_shores(order, q)
            whole_simple = max(pos.values(), default=0) <= 1 and max(neg.values(), default=0) <= 1
            whole_simple_count += whole_simple
            rpos, rneg = reduced_shores(order, q)
            reduced_simple = max(rpos.values(), default=0) <= 1 and max(rneg.values(), default=0) <= 1
            reduced_simple_count += reduced_simple
            score = (maxmult, lp + ln, len(u), not reduced_simple, not whole_simple)
            if best is None or score < best[0]:
                best = (score, order, dict(u), max(pos.values()), max(neg.values()))
            if simple and whole_simple and len(examples) < 5:
                examples.append((order, lp, ln, len(u)))
    print("CURL", "q", q, "M", M, "patterns", (n-1)*(n-2),
          "simple_currents", simple_count,
          "whole_shore_simple", whole_simple_count,
          "reduced_shore_simple", reduced_simple_count)
    print(" hist")
    for key, count in sorted(hist.items()):
        print("  ", key, count)
    score, order, u, pm, nm = best
    print(" best_score", score, "order", order,
          "whole_maxmult", pm, nm, "current", sorted((sorted(k), v) for k, v in u.items()))
    print(" simple_whole_examples", examples)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pairs", nargs="+", type=int, help="q M pairs")
    ns = ap.parse_args()
    assert len(ns.pairs) % 2 == 0
    for i in range(0, len(ns.pairs), 2):
        audit(ns.pairs[i], ns.pairs[i+1])


if __name__ == "__main__":
    main()
