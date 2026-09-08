#!/usr/bin/env python3
"""Inspect the invariant/noninvariant cyclic decomposition of central decks."""

from __future__ import annotations

import argparse
from fractions import Fraction

from research_w2_hahn_venn_exact_20260822 import (
    gram_entry, interval_mask, masks_of_size, superset_sums, zeta,
)


def run(r: int) -> None:
    b = 2*r+1
    ranks = (r, r-1, r-2)
    masks = {s:masks_of_size(b,s) for s in ranks}
    vec = {}
    for s in ranks:
        full = {interval_mask(b,a,s) for a in range(b)}
        vec[(s,'Q')] = [int(x in full) for x in masks[s]]
        missing = interval_mask(b,0,s)
        vec[(s,'d')] = [int(x == missing) for x in masks[s]]
    tr = {(s,n):superset_sums(b,masks[s],v) for (s,n),v in vec.items()}
    for j in range(2,r-1):
        def ge(sa,na,sb,nb):
            return gram_entry(b,sa,sb,j,tr[(sa,na)],tr[(sb,nb)])
        Ug=[]
        for sa in (r,r-1):
            row=[]
            for sb in (r,r-1):
                row.append(ge(sa,'d',sb,'d')-ge(sa,'Q',sb,'Q')/b**2)
            Ug.append(row)
        det=Ug[0][0]*Ug[1][1]-Ug[0][1]**2
        corr=float(Ug[0][1]/(Ug[0][0]*Ug[1][1])**Fraction(1,2))
        rel=float(det/(Ug[0][0]*Ug[1][1]))
        # normalized lower eigenvalue of D^{-1/2}UD^{-1/2} is 1-|corr|.
        print(f"r={r} j={j} Ucorr={corr:.12g} Udelta={rel:.12g} "
              f"1-corr={1-abs(corr):.12g}")


if __name__ == '__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('r',type=int); ns=ap.parse_args()
    run(ns.r)
