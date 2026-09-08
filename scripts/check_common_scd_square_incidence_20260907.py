"""Finite literal checks for the prescribed-chain square incidence law."""

from math import comb


def square_pair(b, ell):
    fsize = b-ell+1
    f = (1 << fsize)-1
    x = list(range(2*fsize, 2*fsize+ell-1))
    y = list(range(2*fsize+ell-1, 2*b))
    xp, yp = [0], [0]
    for bit in x:
        xp.append(xp[-1] | (1 << bit))
    for bit in y:
        yp.append(yp[-1] | (1 << bit))
    first = {f | a | c for a in xp for c in yp}
    full = (1 << (2*b))-1
    second = {full ^ a for a in first}
    assert not first & second
    return first | second


cases = 0
for b in range(2, 9):
    for ell in range(2, b+1):
        support = square_pair(b, ell)
        middle = [x for x in support if x.bit_count() == b]
        assert len(middle) == 2*ell
        for h in range(1, ell+1):
            down = {x: 1 for x in middle}
            up = down.copy()
            # Count paths separately for each central set, to retain the
            # common midpoint when multiplying lower and upper counts.
            total = 0
            for center in middle:
                below, above = {center: 1}, {center: 1}
                for _ in range(h):
                    next_below, next_above = {}, {}
                    for x, count in below.items():
                        for bit in range(2*b):
                            y = x & ~(1 << bit)
                            if y != x and y in support:
                                next_below[y] = next_below.get(y, 0)+count
                    for x, count in above.items():
                        for bit in range(2*b):
                            y = x | (1 << bit)
                            if y != x and y in support:
                                next_above[y] = next_above.get(y, 0)+count
                    below, above = next_below, next_above
                total += sum(below.values())*sum(above.values())
            expected = 2*sum(
                sum(comb(h, r)
                    for r in range(max(0, h-(ell-1-i)), min(h, i)+1))**2
                for i in range(ell)
            )
            assert total == expected
            assert total <= 2*ell*4**h
            if h == 1:
                assert total == 8*ell-12
            cases += 1
print(f"PASS {cases} literal prescribed-chain incidence counts")
