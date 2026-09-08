"""Exact balanced-only fractional optimum 1248; NOT an integral cover."""

from collections import Counter
from itertools import product


DATA = [
    (1744, '000 001 011 021 022 122 123 223 323 333', '000 001 002 003 013 023 033 133 233 333'),
    (1196, '000 100 110 111 211 221 231 232 233 333', '000 001 002 003 013 023 033 133 233 333'),
    (476, '110 111 211 212 222 232', '011 111 112 122 222 223'),
    (476, '001 011 111 112 113 123 133 233', '001 011 111 112 113 123 133 233'),
    (306, '100 200 300 301 302 312 322 323', '001 002 012 022 122 222 223 233'),
    (402, '100 200 300 301 302 312 322 332 333', '001 002 012 022 122 222 223 233'),
    (380, '001 002 102 202 302 312 313 323', '001 011 012 013 023 123 223 233'),
    (172, '000 010 020 120 130 230 231 331 332 333', '001 002 012 013 023 123 133 233'),
    (530, '000 010 020 120 130 131 132 232', '011 012 022 023 123 133 233'),
    (268, '001 002 012 013 023 033 133 233', '001 011 012 022 023 123 133 233'),
    (184, '110 120 121 221 222 322', '011 012 013 113 123 223'),
    (894, '001 011 021 121 221 222 232', '011 012 013 113 123 223 233 333'),
    (1064, '101 102 202 302 312 322 323', '000 001 011 111 112 122 123 223'),
    (238, '000 100 101 111 121 131 132 232 332', '001 011 111 112 113 123 223 233'),
    (476, '100 101 102 112 113 123 223 233', '001 011 012 022 122 123 223 233'),
]


def rows():
    return [(weight, tuple(tuple(map(int, p)) for p in c.split()),
             tuple(tuple(map(int, p)) for p in d.split())) for weight, c, d in DATA]


def check():
    def orbit(p):
        c = tuple(p.count(i) for i in range(4))
        return min(c, c[::-1])
    populations = Counter(orbit(p) for p in product(range(4), repeat=6))
    coverage, cost, volume = Counter(), 0, 0
    for weight, c, d in rows():
        for chain in (c, d):
            assert all(len(p) == 3 and all(0 <= x < 4 for x in p) for p in chain)
            assert all(a != b and all(x <= y for x, y in zip(a, b)) for a, b in zip(chain, chain[1:]))
        for x, y in product(c, d):
            coverage[orbit(x+y)] += weight
        cost += weight*(len(c)+len(d))
        volume += weight*len(c)*len(d)
    assert all(coverage[p] >= 119*n for p, n in populations.items())
    assert cost == 119*1248
    print('PASS exact balanced-only FRACTIONAL cover; cost', cost, '/119=1248;',
          'volume', volume, '/119;', '15 orbit types;', 'not an integral cover')


if __name__ == '__main__':
    check()
