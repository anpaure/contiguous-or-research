#!/usr/bin/env python3
"""Exact small-b census of complement-aligned clustered product banks.

The script first finds tight-cycle factors independently at ranks r<=b/2,
uses the same oriented orders at complementary ranks, and then enumerates all
product atoms and all upper windows.  Research diagnostic; execute on H100.
"""

from collections import Counter
import itertools
import math


def canonical_cycle(order):
    """Canonicalize up to rotation and reversal."""
    n = len(order)
    seqs = []
    for base in (order, tuple(reversed(order))):
        for j in range(n):
            seqs.append(base[j:] + base[:j])
    return min(seqs)


def masks_of_size(n, r):
    return [sum(1 << x for x in ss) for ss in itertools.combinations(range(n), r)]


def deck(order, r):
    n = len(order)
    out = []
    for i in range(n):
        mask = 0
        for j in range(r):
            mask |= 1 << order[(i + j) % n]
        out.append(mask)
    return tuple(out)


def tight_factor(b, r):
    if r == 0 or r == b:
        return []
    if r > b // 2:
        return tight_factor(b, b - r)
    targets = masks_of_size(b, r)
    tid = {x: i for i, x in enumerate(targets)}
    cycles = set()
    for tail in itertools.permutations(range(1, b)):
        cycles.add(canonical_cycle((0,) + tail))
    candidates = []
    through = [[] for _ in targets]
    for order in sorted(cycles):
        ds = deck(order, r)
        if len(set(ds)) != b:
            continue
        bits = 0
        for x in ds:
            bits |= 1 << tid[x]
        idx = len(candidates)
        candidates.append((order, bits))
        for x in ds:
            through[tid[x]].append(idx)

    full = (1 << len(targets)) - 1
    need = len(targets) // b

    def search(covered, chosen):
        if covered == full:
            return chosen
        if len(chosen) >= need:
            return None
        # Minimum remaining branching target.
        best = None
        opts = None
        for t in range(len(targets)):
            if (covered >> t) & 1:
                continue
            avail = [i for i in through[t] if candidates[i][1] & covered == 0]
            if not avail:
                return None
            if opts is None or len(avail) < len(opts):
                best, opts = t, avail
                if len(opts) == 1:
                    break
        assert best is not None
        for i in opts:
            ans = search(covered | candidates[i][1], chosen + [i])
            if ans is not None:
                return ans
        return None

    answer = search(0, [])
    assert answer is not None and len(answer) == need
    factor = [candidates[i][0] for i in answer]
    seen = Counter(x for order in factor for x in deck(order, r))
    assert len(seen) == len(targets) and set(seen.values()) == {1}
    return factor


def clustered_word(alpha, beta, r):
    b = len(alpha)
    types = (0,) * r + (1,) * (b - r)  # 0=A, 1=B
    ia = ib = 0
    out = []
    for t in range(b * b + 2 * b):
        if types[t % b] == 0:
            out.append(alpha[ia % b])
            ia += 1
        else:
            out.append(b + beta[ib % b])
            ib += 1
    return out


def window_mask(word, start, length):
    mask = 0
    for x in word[start : start + length]:
        mask |= 1 << x
    return mask


def census(b):
    factors = {}
    for r in range(1, b // 2 + 1):
        factors[r] = tight_factor(b, r)
        factors[b - r] = factors[r]
        print("factor", b, r, "orders", len(factors[r]))

    ranks = range(1, b)
    counters = {q: Counter() for q in range(0, b // 2 + 1)}
    middle_seen = Counter()
    atom_count = 0
    for r in ranks:
        for alpha in factors[r]:
            for beta in factors[b - r]:
                word = clustered_word(alpha, beta, r)
                atom_count += 1
                for t in range(b * b):
                    mid = window_mask(word, t, b)
                    middle_seen[mid] += 1
                    for q in counters:
                        counters[q][window_mask(word, t, b + q)] += 1

    central_scale = math.comb(2 * b, b)
    expected_middle = sum(math.comb(b, r) ** 2 for r in ranks)
    assert atom_count * b * b == expected_middle
    assert len(middle_seen) == expected_middle and set(middle_seen.values()) == {1}
    print("b", b, "atoms", atom_count, "middle exact", expected_middle)
    for q, count in counters.items():
        target_total = math.comb(2 * b, b + q)
        holes = target_total - len(count)
        repeats = expected_middle - len(count)
        mult_hist = Counter(count.values())
        print(
            " q", q,
            "target", target_total,
            "covered", len(count),
            "holes", holes,
            "holes/W", holes / central_scale,
            "repeat/W", repeats / central_scale,
            "maxmult", max(count.values()),
            "hist", dict(sorted(mult_hist.items())),
        )


if __name__ == "__main__":
    for b in (5, 7):
        census(b)
