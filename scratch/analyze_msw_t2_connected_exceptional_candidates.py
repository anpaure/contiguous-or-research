#!/usr/bin/env python3
"""Compare connected singleton-exception candidates around the Z seam.

Heavy runs belong on h100 only.
"""

from collections import Counter
import sys

import audit_msw_t2_singleton_a_clock as one
import search_msw_t2_exceptional_sets as search


def main():
    hmax = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    old, new, sold, snew = one.reconstruct()
    owners = set(sold)
    a = one.A
    f = one.base.bits("1000110011110")
    g = one.base.bits("1000111011010")
    z = f | g
    candidates = {
        "a": frozenset((a,)),
        "a_f": frozenset((a, f)),
        "a_g": frozenset((a, g)),
        "a_f_g": frozenset((a, f, g)),
    }
    print("SEAM", one.full.word(f), "->", one.full.word(g),
          "Z", one.full.word(z), "rank", z.bit_count())
    for name, exc in candidates.items():
        tag, p = search.colour_for(exc, owners, sold, snew)
        if tag is None:
            print("INFEASIBLE", name)
            continue
        print("CANDIDATE", name, "p", p,
              *(one.full.word(v) for v in sorted(exc)))
        for h in range(2, hmax + 1):
            oc = search.expand(old, sold, tag, h, exc)
            nc = search.expand(new, snew, tag, h, exc)
            if oc is None or nc is None:
                print(" BAD_GRAPH", h)
                continue
            so = search.deck(oc)
            sn = search.deck(nc)
            losses = so - sn
            by_base = Counter(k[0] for k in losses)
            by_rank = Counter(k[0].bit_count() for k in losses)
            print(
                " H", h, "loss", len(losses), "birth", len(sn - so),
                "zloss", by_base[z], "basevals", len(by_base),
                "rankhist", dict(sorted(by_rank.items())),
                "run", search.positive_min(nc, p, h),
                "palette", search.palette_max(nc),
            )


if __name__ == "__main__":
    main()
