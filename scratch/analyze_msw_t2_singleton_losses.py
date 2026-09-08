#!/usr/bin/env python3
"""Classify singleton-a T2 clock losses.  Heavy runs belong on h100."""

from collections import Counter, defaultdict
import sys

import audit_msw_t2_singleton_a_clock as s


def word(x):
    return s.full.word(x)


def base_arc(interval):
    out = []
    for x in interval:
        if not out or out[-1] != x[0]:
            out.append(x[0])
    return tuple(out)


def main():
    hmax = int(sys.argv[1]) if len(sys.argv) > 1 else 12
    old, new, sold, snew = s.reconstruct()
    tag, p = s.quotient_and_coloring(set(sold), sold, snew)
    changed = {v for v in sold if sold[v] != snew[v]}
    print("changed", len(changed), *(word(v) for v in sorted(changed)))
    for h in range(2, hmax + 1):
        oc = s.expand_orders(old, sold, tag, h)
        nc = s.expand_orders(new, snew, tag, h)
        so, wo, _ = s.deck(oc)
        sn, _, _ = s.deck(nc)
        losses = sorted(so - sn, key=lambda z: (z[1], z[0], z[2], z[3]))
        by_base = Counter()
        by_crossings = Counter()
        by_arc = Counter()
        by_clock_size = Counter()
        by_tag_size = Counter()
        rows = []
        for key in losses:
            cid, start, ell = wo[key][:3]
            width = key[1]
            interval = [oc[cid][(start + j) % ell] for j in range(width)]
            arc = base_arc(interval)
            # Count changed base joins met in the actual lifted interval.
            crossed = []
            for x, y in zip(interval, interval[1:]):
                if x[0] != y[0] and x[0] in changed:
                    crossed.append(x[0])
            by_base[key[0]] += 1
            by_crossings[len(crossed)] += 1
            by_arc[arc] += 1
            by_clock_size[key[3].bit_count()] += 1
            by_tag_size[key[2].bit_count()] += 1
            rows.append((key, arc, tuple(crossed), cid, start, ell))
        print(
            "SUMMARY", h, len(losses), "basevals", len(by_base),
            "arcs", len(by_arc), "crossings", dict(sorted(by_crossings.items())),
            "clock_sizes", dict(sorted(by_clock_size.items())),
            "tag_sizes", dict(sorted(by_tag_size.items())),
        )
        print("BASE", *(f"{word(v)}:{n}" for v, n in by_base.most_common()))
        print("ARCS")
        for arc, n in by_arc.most_common():
            print(n, "->".join(word(v) for v in arc))
        if h == hmax:
            print("ROWS")
            for key, arc, crossed, cid, start, ell in rows:
                print(
                    word(key[0]), key[1],
                    format(key[2], f"0{p}b")[::-1],
                    format(key[3], f"0{2*h}b")[::-1],
                    "arc", "->".join(word(v) for v in arc),
                    "changed", ",".join(word(v) for v in crossed),
                    "at", cid, start, ell,
                )


if __name__ == "__main__":
    main()
