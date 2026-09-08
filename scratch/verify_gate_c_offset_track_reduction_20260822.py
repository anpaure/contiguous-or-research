#!/usr/bin/env python3
"""Finite audit for MATH_REDUCTION_GATE_C_OFFSET_TRACK_MATCHING_20260822.md."""

from collections import Counter, defaultdict, deque
from fractions import Fraction
from itertools import combinations, permutations, product
from math import comb, factorial, floor, ceil, log, sqrt


def falling(n, k):
    ans = 1
    for i in range(k):
        ans *= n - i
    return ans


def atom_word(b, rho):
    h = (b - 1) // 2
    A = list(range(b))
    B = list(range(b, 2 * b))
    types = ["B", "A"] * h + ["B"]
    ia, ib = rho % b, 0
    out = []
    for t in range(b * b):
        if types[t % b] == "A":
            out.append(A[ia % b])
            ia += 1
        else:
            out.append(B[ib % b])
            ib += 1
    return out


def cyclic_set(w, start, length):
    n = len(w)
    return frozenset(w[(start + j) % n] for j in range(length))


def check_atoms():
    cases = 0
    for b in (5, 7, 9, 11):
        n = b * b
        H = min(4, b - 2)
        for rho in range(b):
            w = atom_word(b, rho)
            cells = [cyclic_set(w, t, b) for t in range(n)]
            assert len(set(cells)) == n
            for x in range(2 * b):
                pos = [i for i, y in enumerate(w) if y == x]
                gaps = [(pos[(j + 1) % len(pos)] - pos[j]) % n
                        for j in range(len(pos))]
                assert min(gaps) >= 2 * b - 2
            for t in range(n):
                for q in range(1, H + 1):
                    low = cyclic_set(w, t, b - q)
                    high = cyclic_set(w, t, b + q)
                    assert low == cells[(t - q) % n] & cells[t]
                    assert high == cells[t] | cells[(t + q) % n]
                    assert len(cells[t] - cells[(t + q) % n]) == q
            cases += 1
    return cases


def flags_through(C, universe, H):
    C = frozenset(C)
    outside = frozenset(universe) - C
    ans = []
    for deleted in permutations(C, H):
        R = C - frozenset(deleted)
        # u is ordered from farthest lower addition to the central boundary.
        u = tuple(reversed(deleted))
        for v in permutations(outside, H):
            low = {}
            high = {}
            for q in range(H + 1):
                low[q] = R | frozenset(u[:H - q])
                high[q] = C | frozenset(v[:q])
            ans.append((R, u, v, low, high))
    return ans


def check_flag_collisions():
    b, H = 5, 2
    U = frozenset(range(2 * b))
    C = frozenset(range(b))
    F = flags_through(C, U, H)
    assert len(F) == falling(b, H) ** 2
    tests = 0
    for d in range(0, H + 1):
        Cp = frozenset(range(b - d)) | frozenset(range(b, b + d))
        G = flags_through(Cp, U, H)
        for q in range(1, H + 1):
            for side_index in (3, 4):
                cf = Counter(f[side_index][q] for f in F)
                cg = Counter(g[side_index][q] for g in G)
                equal_pairs = sum(cf[x] * cg[x] for x in cf.keys() & cg.keys())
                numerator = comb(b - d, q - d) if d <= q else 0
                expected = Fraction(numerator, comb(b, q) ** 2)
                assert Fraction(equal_pairs, len(F) * len(G)) == expected
                if d == 0:
                    assert expected <= Fraction(1, b)
                else:
                    assert expected <= Fraction(1, b * b)
                tests += 1
    return tests


def check_successors():
    for b, H in ((5, 2), (7, 2), (7, 3)):
        U = frozenset(range(2 * b))
        C = frozenset(range(b))
        R = frozenset(range(b - H))
        u = tuple(range(b - H, b))
        v = tuple(range(b, b + H))
        outside_top = sorted(U - (C | frozenset(v)))
        succ = []
        for z in R:
            for y in outside_top:
                Cp = (C - {z}) | {v[0]}
                Rp = (R - {z}) | {u[0]}
                up = u[1:] + (v[0],)
                vp = v[1:] + (y,)
                assert len(Cp) == b and len(Rp) == b - H
                assert set(up).issubset(Cp) and not (set(vp) & set(Cp))
                succ.append((Cp, Rp, up, vp))
        assert len(set(succ)) == (b - H) ** 2
        by_middle = Counter(x[0] for x in succ)
        assert len(by_middle) == b - H
        assert set(by_middle.values()) == {b - H}
    return 3


class Dinic:
    def __init__(self, n):
        self.g = [[] for _ in range(n)]

    def add(self, u, v, c):
        ui, vi = len(self.g[u]), len(self.g[v])
        self.g[u].append([v, c, vi])
        self.g[v].append([u, 0, ui])
        return ui

    def maxflow(self, s, t):
        total = 0
        n = len(self.g)
        while True:
            level = [-1] * n
            level[s] = 0
            q = deque([s])
            while q:
                u = q.popleft()
                for v, c, _ in self.g[u]:
                    if c and level[v] < 0:
                        level[v] = level[u] + 1
                        q.append(v)
            if level[t] < 0:
                return total
            it = [0] * n

            def dfs(u, f):
                if u == t:
                    return f
                while it[u] < len(self.g[u]):
                    e = self.g[u][it[u]]
                    v, c, rev = e
                    if c and level[v] == level[u] + 1:
                        z = dfs(v, min(f, c))
                        if z:
                            e[1] -= z
                            self.g[v][rev][1] += z
                            return z
                    it[u] += 1
                return 0

            while True:
                z = dfs(s, 10 ** 18)
                if not z:
                    break
                total += z


def feasible_circulation(n, edge_specs):
    """Return realized flows for integer lower/upper bounded circulation."""
    ss, tt = n, n + 1
    din = Dinic(n + 2)
    bal = [0] * n
    refs = []
    for u, v, lo, hi, tag in edge_specs:
        idx = din.add(u, v, hi - lo)
        refs.append((u, idx, lo, hi - lo, tag))
        bal[u] -= lo
        bal[v] += lo
    need = 0
    for v, d in enumerate(bal):
        if d > 0:
            din.add(ss, v, d)
            need += d
        elif d < 0:
            din.add(v, tt, -d)
    assert din.maxflow(ss, tt) == need
    got = {}
    for u, idx, lo, residual_initial, tag in refs:
        residual_now = din.g[u][idx][1]
        got[tag] = lo + residual_initial - residual_now
    return got


def balanced_half(n, b, H, direction):
    ranks = list(range(b, b - H - 1, -1)) if direction == -1 \
        else list(range(b, b + H + 1))
    subsets = {s: list(map(frozenset, combinations(range(n), s))) for s in ranks}
    next_id = 0
    ids = {}
    for s in ranks:
        for S in subsets[s]:
            ids[(s, S, 0)] = next_id
            next_id += 1
            ids[(s, S, 1)] = next_id
            next_id += 1
    src, sink = next_id, next_id + 1
    next_id += 2
    W = comb(n, b)
    specs = []
    for s in ranks:
        mu = Fraction(W, comb(n, s))
        lo, hi = floor(mu), ceil(mu)
        for S in subsets[s]:
            specs.append((ids[(s, S, 0)], ids[(s, S, 1)],
                          lo, hi, ("node", s, S)))
    for C in subsets[b]:
        specs.append((src, ids[(b, C, 0)], 1, 1, ("source", C)))
    for s, sp in zip(ranks, ranks[1:]):
        for S in subsets[s]:
            if direction == -1:
                neighbors = (S - {x} for x in S)
            else:
                neighbors = (S | {x} for x in range(n) if x not in S)
            for T in neighbors:
                specs.append((ids[(s, S, 1)], ids[(sp, T, 0)],
                              0, W, ("arc", s, S, T)))
    last = ranks[-1]
    for S in subsets[last]:
        specs.append((ids[(last, S, 1)], sink, 0, W, ("sink", S)))
    specs.append((sink, src, W, W, ("return",)))
    flow = feasible_circulation(next_id, specs)
    for s in ranks:
        mu = Fraction(W, comb(n, s))
        loads = [flow[("node", s, S)] for S in subsets[s]]
        assert sum(loads) == W
        assert set(loads).issubset({floor(mu), ceil(mu)})
    return sum(len(subsets[s]) for s in ranks)


def weak_compositions(total, n):
    if n == 1:
        yield (total,)
    else:
        for x in range(total + 1):
            for tail in weak_compositions(total - x, n - 1):
                yield (x,) + tail


def check_hole_lemma():
    cases = 0
    for N in range(1, 7):
        for M in range(0, 9):
            base, rem = divmod(M, N)
            for high in combinations(range(N), rem):
                q = [base] * N
                for i in high:
                    q[i] += 1
                for a in weak_compositions(M, N):
                    V = sum(max(x - y, 0) for x, y in zip(a, q))
                    holes = sum(x == 0 for x in a)
                    assert holes <= max(N - M, 0) + V
                    cases += 1
    return cases


def check_embedding():
    cases = 0
    for b, H in ((7, 2), (9, 3), (11, 4)):
        h = (b - 1) // 2
        types = (["B", "A"] * h + ["B"])
        desired = list(range(b + H))
        events = [types[i % b] for i in range(b + H)]
        assert Counter(events)["A"] <= b and Counter(events)["B"] <= b
        shore = {"A": [], "B": []}
        for x, typ in zip(desired, events):
            shore[typ].append(x)
        unused = iter(range(b + H, 2 * b))
        for typ in ("A", "B"):
            while len(shore[typ]) < b:
                shore[typ].append(next(unused))
        ia = ib = 0
        made = []
        for typ in events:
            if typ == "A":
                made.append(shore["A"][ia])
                ia += 1
            else:
                made.append(shore["B"][ib])
                ib += 1
        assert made == desired
        for q in range(H + 1):
            assert frozenset(made[:b-q]) == frozenset(desired[:b-q])
            assert frozenset(made[:b+q]) == frozenset(desired[:b+q])
        cases += 1
    return cases


def check_arithmetic():
    for b in range(5, 61, 2):
        W = comb(2 * b, b)
        Dhat = b * factorial(b) ** 2
        assert W * Dhat == b * factorial(2 * b)
        for q in range(1, b + 1):
            ratio = Fraction(comb(2 * b, b + q), W)
            prod_ratio = Fraction(1, 1)
            for i in range(q):
                prod_ratio *= Fraction(b - i, b + i + 1)
            assert ratio == prod_ratio
            assert float(ratio) <= pow(2.718281828459045, -q * q / (2 * b)) + 1e-15
    return 28


def main():
    atom_cases = check_atoms()
    collision_cases = check_flag_collisions()
    successor_cases = check_successors()
    flow_nodes = balanced_half(10, 5, 2, -1)
    flow_nodes += balanced_half(10, 5, 2, +1)
    hole_cases = check_hole_lemma()
    embedding_cases = check_embedding()
    arithmetic_cases = check_arithmetic()
    print("PASS gate-C offset-track reduction")
    print("atom phase cases:", atom_cases)
    print("collision marginal cases:", collision_cases)
    print("successor cases:", successor_cases)
    print("balanced-flow rank vertices:", flow_nodes)
    print("hole-lemma exhaustive cases:", hole_cases)
    print("embedding cases:", embedding_cases)
    print("arithmetic b-cases:", arithmetic_cases)


if __name__ == "__main__":
    main()
