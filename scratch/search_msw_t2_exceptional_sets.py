#!/usr/bin/env python3
"""Search small undilated-owner sets in the complete T2 clock.

Heavy runs belong on h100 only.
"""

from collections import Counter, defaultdict, deque
from itertools import combinations
import sys

import audit_msw_t2_singleton_a_clock as one


class DSU:
    def __init__(self, values):
        self.p = {v: v for v in values}
        self.sz = {v: 1 for v in values}

    def find(self, v):
        if self.p[v] != v:
            self.p[v] = self.find(self.p[v])
        return self.p[v]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.sz[x] < self.sz[y]:
            x, y = y, x
        self.p[y] = x
        self.sz[x] += self.sz[y]


def colour_for(exceptions, owners, sold, snew):
    dsu = DSU(owners)
    for v in owners:
        dsu.union(sold[v], snew[v])
        if v in exceptions:
            dsu.union(v, sold[v])
    classes = sorted({dsu.find(v) for v in owners})
    graph = {c: set() for c in classes}
    for v in owners:
        if v in exceptions:
            continue
        x, y = dsu.find(v), dsu.find(sold[v])
        if x == y:
            return None, None
        graph[x].add(y)
        graph[y].add(x)
    # Deterministic DSATUR greedy.  Any constant number of colours is okay;
    # report it rather than asserting optimality.
    col = {}
    sat = {c: set() for c in classes}
    while len(col) < len(classes):
        v = max(
            (c for c in classes if c not in col),
            key=lambda c: (len(sat[c]), len(graph[c]), -c),
        )
        used = {col[w] for w in graph[v] if w in col}
        z = 0
        while z in used:
            z += 1
        col[v] = z
        for w in graph[v]:
            if w not in col:
                sat[w].add(z)
    tag = {v: col[dsu.find(v)] for v in owners}
    return tag, 1 + max(col.values())


def dset(j, h):
    return sum(1 << ((j + k) % (2 * h)) for k in range(h))


def block(v, output_tag, tag, h, exceptions):
    if v in exceptions:
        assert tag[v] == output_tag
        return [(v, 1 << tag[v], dset(0, h), 0, "exception")]
    out = []
    for j in range(h + 1):
        out.append((v, 1 << tag[v], dset(j, h), j, "first"))
    for step, j in enumerate(range(h, 2 * h + 1)):
        out.append((v, 1 << output_tag, dset(j, h), h + 1 + step, "second"))
    return out


def expand(orders, succ, tag, h, exceptions):
    cycles = []
    for order in orders:
        cycle = []
        for v in order:
            cycle.extend(block(v, tag[succ[v]], tag, h, exceptions))
        for x, y in zip(cycle, cycle[1:] + cycle[:1]):
            if (x[0] ^ y[0]).bit_count() + (x[1] ^ y[1]).bit_count() + (x[2] ^ y[2]).bit_count() != 2:
                return None
        cycles.append(cycle)
    return cycles


def deck(cycles):
    support = set()
    for cycle in cycles:
        ell = len(cycle)
        for i in range(ell):
            bo = to = co = 0
            for width in range(1, ell + 1):
                x = cycle[(i + width - 1) % ell]
                bo |= x[0]
                to |= x[1]
                co |= x[2]
                support.add((bo, width, to, co))
    return support


def positive_min(cycles, p, h):
    ans = 10**9
    for cycle in cycles:
        ell = len(cycle)
        layers = [(13, 0), (p, 1), (2 * h, 2)]
        for n, layer in layers:
            for bit in range(n):
                seq = [bool(x[layer] >> bit & 1) for x in cycle]
                if not any(seq) or all(seq):
                    continue
                for i in range(ell):
                    if not seq[i] or seq[i - 1]:
                        continue
                    run = 1
                    while run < ell and seq[(i + run) % ell]:
                        run += 1
                    ans = min(ans, run)
    return ans


def palette_max(cycles):
    out = [Counter(), Counter(), Counter()]
    for cyc in cycles:
        for x in cyc:
            out[0][x[:3]] += 1
        for x, y in zip(cyc, cyc[1:] + cyc[:1]):
            out[1][(x[0] & y[0], x[1] & y[1], x[2] & y[2])] += 1
            out[2][(x[0] | y[0], x[1] | y[1], x[2] | y[2])] += 1
    return tuple(max(c.values()) for c in out)


def neighbourhood(a, sold, snew, radius):
    pred_old = {w: v for v, w in sold.items()}
    pred_new = {w: v for v, w in snew.items()}
    seen = {a}
    front = {a}
    for _ in range(radius):
        nxt = set()
        for v in front:
            nxt.update((sold[v], snew[v], pred_old[v], pred_new[v]))
        nxt -= seen
        seen |= nxt
        front = nxt
    return seen


def main():
    radius = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    max_size = int(sys.argv[2]) if len(sys.argv) > 2 else 3
    height = int(sys.argv[3]) if len(sys.argv) > 3 else 2
    old, new, sold, snew = one.reconstruct()
    owners = set(sold)
    a = one.A
    pool = sorted(neighbourhood(a, sold, snew, radius))
    print("POOL", len(pool), *(one.full.word(v) for v in pool))
    rows = []
    for size in range(1, max_size + 1):
        for extra in combinations([v for v in pool if v != a], size - 1):
            exc = frozenset((a,) + extra)
            tag, p = colour_for(exc, owners, sold, snew)
            if tag is None:
                continue
            oc = expand(old, sold, tag, height, exc)
            nc = expand(new, snew, tag, height, exc)
            if oc is None or nc is None:
                continue
            run = positive_min(nc, p, height)
            if run < height:
                continue
            so = deck(oc)
            sn = deck(nc)
            loss = len(so - sn)
            rows.append((loss, size, p, run, palette_max(nc), exc, len(sn - so)))
            print(
                "ROW", loss, "size", size, "p", p, "run", run,
                "palette", palette_max(nc), "birth", len(sn - so),
                *(one.full.word(v) for v in sorted(exc)),
            )
    print("BEST")
    for row in sorted(rows)[:30]:
        loss, size, p, run, pal, exc, birth = row
        print(loss, size, p, run, pal, birth, *(one.full.word(v) for v in sorted(exc)))


if __name__ == "__main__":
    main()
