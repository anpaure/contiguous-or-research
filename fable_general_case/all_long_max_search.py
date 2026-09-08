#!/usr/bin/env python3
"""Search for 'all-long-max' orders of the middle hexagon H_a.

Q1: does H_a admit a permutation in which every interior plateau-local-max
of every coordinate (x, y, or z) has plateau length >= a?

Plateau = maximal block of consecutive word positions with constant value of
that coordinate.  Interior = not containing position 1 or M.  Local max =
both neighboring values strictly lower.

DFS with immediate pruning: a violation is created exactly when a plateau
closes downward (xi_t < xi_{t-1}) whose opening was upward (xi_{u-1} < xi_u)
with u >= 2 and length < a.  Symmetry reduction on the first point (group of
order 12: S_3 on coordinates x central negation).
"""
import sys, time, random
from itertools import permutations

def hexpoints(a):
    return [(x, y, -x-y) for x in range(-a, a+1) for y in range(-a, a+1)
            if abs(x+y) <= a]

def orbit_reps(a):
    """Representatives of point-orbits under S_3 x {+-1}."""
    pts = hexpoints(a)
    seen, reps = set(), []
    for p in pts:
        if p in seen: continue
        orb = set()
        for s in (1, -1):
            q = tuple(s*c for c in p)
            for perm in permutations(range(3)):
                orb.add(tuple(q[i] for i in perm))
        orb &= set(pts)
        seen |= orb
        reps.append(p)
    return reps

class Searcher:
    def __init__(self, a, min_len=None, allow_short=0, time_cap=None, rng=None):
        self.a = a
        self.min_len = a if min_len is None else min_len
        self.allow_short = allow_short          # budget of short interior peaks
        self.pts = hexpoints(a)
        self.M = len(self.pts)
        self.time_cap = time_cap
        self.t0 = time.time()
        self.rng = rng
        self.nodes = 0
        self.best_depth = 0
        self.solution = None
        self.timed_out = False

    def run(self, first_points=None):
        firsts = first_points if first_points is not None else orbit_reps(self.a)
        for p0 in firsts:
            used = {p0}
            # plateau state per coord: (value, start_index, opened_up)
            # opened_up: True if plateau began with a strict up-step with a
            # position before it (i.e. can become an interior peak)
            st = [(p0[c], 1, False) for c in range(3)]
            if self.dfs([p0], used, st, self.allow_short):
                return True
            if self.timed_out:
                return None
        return False if not self.timed_out else None

    def dfs(self, word, used, st, budget):
        self.nodes += 1
        if self.time_cap and self.nodes % 4096 == 0:
            if time.time() - self.t0 > self.time_cap:
                self.timed_out = True
                return False
        t = len(word)
        if t > self.best_depth:
            self.best_depth = t
        if t == self.M:
            self.solution = list(word)
            return True
        cands = [p for p in self.pts if p not in used]
        if self.rng:
            self.rng.shuffle(cands)
        last = word[-1]
        for p in cands:
            if p == last:
                continue
            nb = budget
            ok = True
            nst = list(st)
            for c in range(3):
                v, s, up = st[c]
                if p[c] == v:
                    continue  # plateau extends
                if p[c] < v:
                    # plateau [s, t] closes downward at position t (1-indexed)
                    if up:  # interior peak
                        if (t - s + 1) < self.min_len:
                            if nb > 0:
                                nb -= 1
                            else:
                                ok = False
                                break
                    nst[c] = (p[c], t + 1, False)
                else:
                    nst[c] = (p[c], t + 1, True)  # opened upward, has left nbr
            if not ok:
                continue
            word.append(p); used.add(p)
            if self.dfs(word, used, nst, nb):
                return True
            word.pop(); used.discard(p)
            if self.timed_out:
                return False
        return False

def audit_order(word, a, min_len):
    """Independent verification: list all interior plateau-local-maxes."""
    M = len(word)
    bad, peaks = [], []
    for c in range(3):
        vals = [p[c] for p in word]
        i = 0
        while i < M:
            j = i
            while j + 1 < M and vals[j+1] == vals[i]:
                j += 1
            interior = (i > 0 and j < M - 1)
            if interior and vals[i-1] < vals[i] and vals[j+1] < vals[i]:
                L = j - i + 1
                peaks.append((c, i, j, L))
                if L < min_len:
                    bad.append((c, i, j, L))
            i = j + 1
    return peaks, bad

def main():
    for a in [2, 3]:
        M = 3*a*a + 3*a + 1
        print(f"=== a={a} (M={M}), strict min plateau len {a} ===")
        s = Searcher(a, time_cap=600)
        res = s.run()
        print(f" result={res} nodes={s.nodes} best_depth={s.best_depth}/{M}")
        if s.solution:
            peaks, bad = audit_order(s.solution, a, a)
            assert not bad, bad
            print(f" SOLUTION verified. peaks={peaks}")
            print(" word:", s.solution)
        sys.stdout.flush()

if __name__ == '__main__':
    main()
