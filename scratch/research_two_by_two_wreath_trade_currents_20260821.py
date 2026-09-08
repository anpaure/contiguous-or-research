#!/usr/bin/env python3
"""Symbolic interval currents of the all-rank 2<->2 wreath trade.

Run only on H100.  The rows are
  abPcdQ, caPdbQ  <->  acPbdQ, baPdcQ,
with |P|=r-1 and |Q|=r-2.
"""

from __future__ import annotations

from collections import Counter


def deck(row, ell):
    n = len(row)
    return Counter(
        frozenset(row[(i + j) % n] for j in range(ell)) for i in range(n)
    )


def fmt(s):
    return '{' + ','.join(sorted(s)) + '}'


def one(r):
    p = [f'p{i}' for i in range(1, r)]
    q = [f'q{i}' for i in range(1, r - 1)]
    old = [tuple(['a', 'b', *p, 'c', 'd', *q]), tuple(['c', 'a', *p, 'd', 'b', *q])]
    new = [tuple(['a', 'c', *p, 'b', 'd', *q]), tuple(['b', 'a', *p, 'd', 'c', *q])]
    assert all(len(x) == 2 * r + 1 for x in old + new)
    print('R', r)
    for ell in range(r - 3, r + 4):
        if not 1 <= ell <= 2 * r:
            continue
        oo = sum((deck(x, ell) for x in old), Counter())
        nn = sum((deck(x, ell) for x in new), Counter())
        delta = nn.copy()
        delta.subtract(oo)
        plus = sorted((fmt(s), v) for s, v in delta.items() if v > 0)
        minus = sorted((fmt(s), -v) for s, v in delta.items() if v < 0)
        print('ELL', ell, 'PLUS', plus, 'MINUS', minus)
        if ell == r:
            assert not plus and not minus


if __name__ == '__main__':
    for rr in (4, 5, 6):
        one(rr)
