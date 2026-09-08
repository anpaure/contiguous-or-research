#!/usr/bin/env python3
"""Test the 0/1 lexical pair between ranks r and r+1 of B_(2r-1)."""

from collections import Counter, defaultdict
from itertools import combinations


def upper_words(n, w):
    for ones in combinations(range(n), w):
        x = 0
        for i in ones:
            x |= 1 << i
        yield x


def lexical_down(x, n, p):
    height = 0
    ups = []
    for i in range(n):
        if (x >> i) & 1:
            ups.append((height, i))
            height += 1
        else:
            height -= 1
    ups.sort(key=lambda z: (-z[0], z[1]))
    return x ^ (1 << ups[p][1])


def scd_down(x, n):
    stack = []
    unmatched_ones = []
    for i in range(n):
        if ((x >> i) & 1) == 0:
            stack.append(i)
        elif stack:
            stack.pop()
        else:
            unmatched_ones.append(i)
    return x ^ (1 << unmatched_ones[-1])


def unmatched_count(x, n):
    stack = []
    free = 0
    for i in range(n):
        if ((x >> i) & 1) == 0:
            stack.append(i)
        elif stack:
            stack.pop()
        else:
            free += 1
    return free + len(stack)


def components(vertices, edges):
    adj = defaultdict(list)
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    seen = set()
    out = []
    for v in vertices:
        if v in seen:
            continue
        stack = [v]
        seen.add(v)
        vs = []
        es = 0
        while stack:
            u = stack.pop()
            vs.append(u)
            es += len(adj[u])
            for z in adj[u]:
                if z not in seen:
                    seen.add(z)
                    stack.append(z)
        out.append((len(vs), es // 2))
    return out


def main():
    for r in range(2, 10):
        n = 2 * r - 1
        uppers = list(upper_words(n, r + 1))
        mids = list(upper_words(n, r))
        edges = []
        lows = []
        phase0 = []
        phase1 = []
        bad_same = 0
        for u in uppers:
            assert lexical_down(u, n, 0) == scd_down(u, n)
            a = lexical_down(u, n, 0)
            b = lexical_down(u, n, 1)
            phase0.append(a)
            phase1.append(b)
            if a == b:
                bad_same += 1
            edges.append((a, b))
            lows.append(a & b)
        deg = Counter(z for e in edges for z in e)
        comps = components(mids, edges)
        cycles = sum(1 for v, e in comps if e == v and e)
        low_hist = Counter(Counter(lows).values())
        print(
            r,
            "U", len(uppers),
            "phase", len(set(phase0)), len(set(phase1)),
            "lower", len(set(lows)),
            "lowhist", dict(sorted(low_hist.items())),
            "same", bad_same,
            "maxdeg", max(deg.values(), default=0),
            "components", len(comps),
            "cycles", cycles,
        )
        if r <= 4:
            lc = Counter(lows)
            print(" duplicated", [format(z, f"0{n}b") for z, v in lc.items() if v == 2])
        if r <= 8:
            for pp in ((0, 2), (1, 2)):
                if r + 1 <= max(pp):
                    continue
                es = []
                ls = []
                ph = [[], []]
                for u in uppers:
                    a = lexical_down(u, n, pp[0])
                    b = lexical_down(u, n, pp[1])
                    es.append((a, b))
                    ls.append(a & b)
                    ph[0].append(a)
                    ph[1].append(b)
                co = components(mids, es)
                print(" pair", pp, "ph", len(set(ph[0])), len(set(ph[1])),
                      "lowhist", dict(sorted(Counter(Counter(ls).values()).items())),
                      "maxdeg", max(Counter(z for e in es for z in e).values()),
                      "cycles", sum(1 for v, e in co if e == v and e))
        if r <= 8:
            # Choose one of the adjacent lexical pairs (0,1) or (1,2) per U.
            # Brute-force the natural rule by chain-bottom/height statistics.
            candidates = []
            for u in uppers:
                e01 = (lexical_down(u, n, 0), lexical_down(u, n, 1))
                e12 = (lexical_down(u, n, 1), lexical_down(u, n, 2))
                candidates.append((u, e01, e12))
            rules = {
                "firstbit": lambda u: (u & 1) != 0,
                "lastbit": lambda u: ((u >> (n - 1)) & 1) != 0,
                "scdfree_parity": lambda u: unmatched_count(u, n) % 4 == 1,
            }
            for name, rule in rules.items():
                es = [e12 if rule(u) else e01 for u, e01, e12 in candidates]
                ls = [a & b for a, b in es]
                co = components(mids, es)
                print(" rule", name, "low", len(set(ls)),
                      "maxdeg", max(Counter(z for e in es for z in e).values()),
                      "cycles", sum(1 for v, e in co if e == v and e))
            # Greedy retain phase-1 neighbor and choose the other lexical phase.
            chosen = []
            used_lower = set()
            used_other = set()
            for u in sorted(uppers):
                b = lexical_down(u, n, 1)
                opts = []
                for p in range(n - r):
                    if p == 1:
                        continue
                    a = lexical_down(u, n, p)
                    opts.append((a & b in used_lower, a in used_other, p, a))
                _, _, p, a = min(opts)
                chosen.append((a, b))
                used_lower.add(a & b)
                used_other.add(a)
            lc = Counter(a & b for a, b in chosen)
            dg = Counter(z for e in chosen for z in e)
            co = components(mids, chosen)
            print(" greedy fixed1", "low", len(lc), "hist", dict(sorted(Counter(lc.values()).items())),
                  "maxdeg", max(dg.values()), "cycles", sum(1 for v, e in co if e == v and e))
            # Exact-cover test: choose one adjacent lexical pair (p,p+1) per U,
            # with all lower colours distinct. This ignores owner degree for now.
            if r <= 6:
                rows = []
                options = []
                lower_index = {}
                for ui, u in enumerate(uppers):
                    for p in range(r):
                        a = lexical_down(u, n, p)
                        b = lexical_down(u, n, p + 1)
                        lo = a & b
                        li = lower_index.setdefault(lo, len(lower_index))
                        options.append((ui, p, li))
                # Backtracking with MRV; each U exactly once, lower at most once.
                by_u = [[] for _ in uppers]
                for oi, (ui, p, li) in enumerate(options):
                    by_u[ui].append((p, li, oi))
                order = sorted(range(len(uppers)), key=lambda ui: len(by_u[ui]))
                used = set()
                sol = [-1] * len(uppers)

                def dfs(pos):
                    if pos == len(order):
                        return True
                    # Dynamic MRV among remaining U.
                    best_j = None
                    best_opts = None
                    for j in range(pos, len(order)):
                        ui = order[j]
                        av = [x for x in by_u[ui] if x[1] not in used]
                        if best_opts is None or len(av) < len(best_opts):
                            best_j, best_opts = j, av
                            if not av:
                                break
                    if not best_opts:
                        return False
                    order[pos], order[best_j] = order[best_j], order[pos]
                    ui = order[pos]
                    for p, li, oi in best_opts:
                        used.add(li)
                        sol[ui] = p
                        if dfs(pos + 1):
                            return True
                        used.remove(li)
                    sol[ui] = -1
                    order[pos], order[best_j] = order[best_j], order[pos]
                    return False

                ok = dfs(0)
                print(" exact lexical adjacent lower", ok,
                      "phases", Counter(sol) if ok else {})
                if ok:
                    es = []
                    for ui, u in enumerate(uppers):
                        p = sol[ui]
                        es.append((lexical_down(u, n, p), lexical_down(u, n, p + 1)))
                    dg = Counter(z for e in es for z in e)
                    co = components(mids, es)
                    print(" exact lexical geometry", "maxdeg", max(dg.values()),
                          "cycles", sum(1 for v, e in co if e == v and e),
                          "components", len(co))
                    if r <= 4:
                        print(" lexical assignment", [
                            (format(u, f"0{n}b"), sol[ui]) for ui, u in enumerate(uppers)
                        ])


if __name__ == "__main__":
    main()
