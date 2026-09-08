#!/usr/bin/env python3
"""Falsification test for Lemma B (fan-capped avoidance inequality).

Lemma B: for any word A_1..A_N of nonzero closed triples covering the box
[0,p]x[0,q]x[0,r] by contiguous componentwise maxima, any selection of one
witnessing interval per middle-rank target (m* = floor((p+q+r)/2)), and any
h>=1:   |S_h| <= sum_i min(w_i, h) + h*D
where S_h = covered points with rank in [m*-h, m*-1] (rank>=1 only),
w_i = r_i - ell_i for the sorted witness intervals, D = N - M.
"""
import itertools, random, sys

def joins_of_word(word):
    """All (interval -> join). Returns dict {(x,y): join} 1-indexed inclusive."""
    N = len(word)
    out = {}
    for x in range(N):
        cur = (0,0,0)
        for y in range(x, N):
            w = word[y]
            cur = (max(cur[0],w[0]), max(cur[1],w[1]), max(cur[2],w[2]))
            out[(x+1,y+1)] = cur
    return out

def covered_targets(word, box):
    J = joins_of_word(word)
    cov = set(J.values())
    p,q,r = box
    allpts = {(a,b,c) for a in range(p+1) for b in range(q+1) for c in range(r+1)} - {(0,0,0)}
    return cov & allpts, J

def check_word(word, box, max_selections=20000, rng=None, verbose=False):
    """Returns list of violations (empty if none)."""
    p,q,r = box
    mstar = (p+q+r)//2
    cov, J = covered_targets(word, box)
    N = len(word)
    # middle targets
    mid = sorted(t for t in cov if sum(t) == mstar)
    M = len(mid)
    D = N - M
    if D < 0:
        return [("D<0 impossible", word, box)]
    # witness lists per middle target
    wit = {t: sorted([iv for iv,j in J.items() if j == t]) for t in mid}
    for t in mid:
        if not wit[t]:
            return [("uncovered middle target", t, word)]
    # S_h sizes for each h (covered points only, rank >= 1)
    ranks_below = {}
    for t in cov:
        s = sum(t)
        if 1 <= s <= mstar-1:
            ranks_below.setdefault(s, set()).add(t)
    violations = []
    # selection generator
    sizes = [len(wit[t]) for t in mid]
    total = 1
    for s in sizes:
        total *= s
        if total > max_selections: break
    def selections():
        if total <= max_selections:
            for combo in itertools.product(*(wit[t] for t in mid)):
                yield combo
        else:
            # extremal + random
            yield tuple(wit[t][0] for t in mid)            # leftmost
            yield tuple(wit[t][-1] for t in mid)           # rightmost
            yield tuple(min(wit[t], key=lambda iv: iv[1]-iv[0]) for t in mid)  # shortest
            yield tuple(max(wit[t], key=lambda iv: iv[1]-iv[0]) for t in mid)  # longest
            for _ in range(max_selections):
                yield tuple(rng.choice(wit[t]) for t in mid)
    for combo in selections():
        ivs = sorted(combo)
        # sanity: strictly increasing endpoints (theory says automatic)
        ls = [iv[0] for iv in ivs]; rs = [iv[1] for iv in ivs]
        if len(set(ls)) != M or any(rs[i] >= rs[i+1] for i in range(M-1)):
            violations.append(("normal form broken", combo, word))
            continue
        ws = [iv[1]-iv[0] for iv in ivs]
        for h in range(1, mstar):
            Sh = sum(len(ranks_below.get(s, ())) for s in range(max(1, mstar-h), mstar))
            bound = sum(min(w, h) for w in ws) + h*D
            if Sh > bound:
                violations.append(("VIOLATION", box, word, combo, h, Sh, bound))
    return violations

def closure_decode(v):
    """Decode 6-bit mask: bits (1,2)=chain A, (4,8)=chain B, (16,32)=chain C.
    Closure: level = 2 if high bit set else 1 if low bit set else 0."""
    def lev(lo, hi): return 2 if v & hi else (1 if v & lo else 0)
    return (lev(1,2), lev(4,8), lev(16,32))

def main():
    rng = random.Random(20260722)
    # --- Test 1: the exact cube_2 certificate ---
    raw = open('/Users/amir.nuriyev/Documents/problem/three_box_certificates/cube_2/2_2_2_n10.word').read().split()
    word = [closure_decode(int(x)) for x in raw]
    box = (2,2,2)
    cov, _ = covered_targets(word, box)
    need = 26
    print(f"cube_2 word decoded: {word}")
    print(f"coverage: {len(cov)}/{need}")
    assert len(cov) == need, "decode/coverage failed -- wrong bit convention?"
    v = check_word(word, box, rng=rng)
    print(f"cube_2 certificate: {'NO violations' if not v else v[:3]}")

    # --- Test 2: randomized covering words on small boxes ---
    boxes = [(1,1,1),(2,1,1),(2,2,1),(2,2,2),(3,2,2),(2,2,3),(3,3,2),(3,1,1)]
    grand = 0
    for box in boxes:
        p,q,r = box
        pts = [(a,b,c) for a in range(p+1) for b in range(q+1) for c in range(r+1) if (a,b,c)!=(0,0,0)]
        allpts = set(pts)
        # width for reference
        from collections import Counter
        cnt = Counter(sum(t) for t in allpts | {(0,0,0)})
        width = max(cnt.values())
        tested = 0
        tries = 0
        while tested < 60 and tries < 30000:
            tries += 1
            L = width + rng.randint(1, 8)
            word = [rng.choice(pts) for _ in range(L)]
            cov, _ = covered_targets(word, box)
            if cov != allpts:
                continue
            tested += 1
            v = check_word(word, box, max_selections=3000, rng=rng)
            if v:
                print("!!!", v[:2]); grand += len(v)
        print(f"box {box}: {tested} random covering words tested, violations so far: {grand}")
    print("TOTAL violations:", grand)

if __name__ == '__main__':
    main()
