#!/usr/bin/env python3
"""All-height sample for ungraded singleton-clock masks 0 and {c,d}."""

import sys

import audit_msw_t2_singleton_a_clock as s
import search_msw_t2_singleton_clock_reflections as r


def main():
    hmax = int(sys.argv[1]) if len(sys.argv) > 1 else 12
    old, new, sold, snew = s.reconstruct()
    owners = set(sold)
    head = s.base.bits("0000111011110")
    tag, p = s.quotient_and_coloring(owners, sold, snew, (head,))
    for h in range(2, hmax + 1):
        for mask in (0, 6):
            reflected = {
                r.NEIGHBOURS[j] for j in range(4) if (mask >> j) & 1
            }
            oc = s.expand_orders(old, sold, tag, h, reflected)
            nc = s.expand_orders(new, snew, tag, h, reflected)
            os, ow = r.ungraded(oc)
            ns, nw = r.ungraded(nc)
            rm, _ = s.run_minima(nc, p, h)
            losses = os - ns
            print(
                "TWO_MASK h", h, "mask", mask,
                "old", len(os), "new", len(ns),
                "loss", len(losses), "birth", len(ns - os),
                "run_min", rm,
            )
            for key in sorted(losses):
                print(
                    " LOSS", s.full.word(key[0]),
                    format(key[1], f"0{p}b")[::-1],
                    format(key[2], f"0{2*h}b")[::-1],
                )


if __name__ == "__main__":
    main()
