#!/usr/bin/env python3
"""Audit fixed-GK p with q chosen among free 1s of the predecessor A."""

from __future__ import annotations

import argparse
import collections
import itertools


def masks(n, r):
    for c in itertools.combinations(range(n), r):
        x = 0
        for i in c:
            x |= 1 << i
        yield x


def free(mask, n):
    stack = []
    paired = set()
    for i in range(n):
        if (mask >> i) & 1:
            stack.append(i)
        elif stack:
            paired.add(i)
            paired.add(stack.pop())
    return [i for i in range(n) if i not in paired]


def audit(m):
    n = 2*m+1
    us = list(masks(n, m+2))
    for from_right in (False, True):
        for index in range(m+1):
            ls = collections.Counter(); bs = collections.Counter(); joint = collections.Counter()
            bad = 0
            for u in us:
                fu = [i for i in free(u,n) if (u>>i)&1]
                p = fu[0]
                a = u ^ (1<<p)
                qa = [i for i in free(a,n) if (a>>i)&1]
                if from_right: qa.reverse()
                if index >= len(qa):
                    bad += 1
                    continue
                q = qa[index]
                l = a ^ (1<<q); b = u ^ (1<<q)
                ls[l] += 1; bs[b] += 1; joint[a] += 1; joint[b] += 1
            print("m",m,"right",int(from_right),"idx",index,"bad",bad,
                  "Lmax",max(ls.values(),default=0),"Ldup",sum(v-1 for v in ls.values()),
                  "Bmax",max(bs.values(),default=0),"Bdup",sum(v-1 for v in bs.values()),
                  "Omax",max(joint.values(),default=0))


if __name__ == '__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('m',nargs='+',type=int); a=ap.parse_args()
    for m in a.m: audit(m)
