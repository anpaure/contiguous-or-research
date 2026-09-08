#!/usr/bin/env python3
"""Classify losses for exceptional owners a and f. Heavy runs: h100 only."""

from collections import Counter
import gc
import sys

import audit_msw_t2_singleton_a_clock as one
import search_msw_t2_exceptional_sets as search


def main():
    hmax = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    old, new, sold, snew = one.reconstruct()
    owners = set(sold)
    a = one.A
    f = one.base.bits("1000110011110")
    z = one.base.bits("1000111011110")
    exc = frozenset((a, f))
    tag, p = search.colour_for(exc, owners, sold, snew)
    assert tag is not None
    for h in range(2, hmax + 1):
        oc = search.expand(old, sold, tag, h, exc)
        nc = search.expand(new, snew, tag, h, exc)
        so = search.deck(oc)
        sn = search.deck(nc)
        losses = so - sn
        by_base = Counter(k[0] for k in losses)
        by_rank = Counter(k[0].bit_count() for k in losses)
        rank8_base = Counter(k[0] for k in losses if k[0].bit_count() == 8)
        print(
            "SUMMARY", h, "loss", len(losses), "birth", len(sn - so),
            "zloss", by_base[z], "basevals", len(by_base),
            "rankhist", dict(sorted(by_rank.items())),
            "run", search.positive_min(nc, p, h),
            "palette", search.palette_max(nc),
        )
        print("RANK8", *(f"{one.full.word(v)}:{n}" for v, n in rank8_base.items()))
        del oc, nc, so, sn, losses, by_base, by_rank, rank8_base
        gc.collect()


if __name__ == "__main__":
    main()
