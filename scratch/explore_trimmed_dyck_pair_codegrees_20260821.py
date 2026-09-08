#!/usr/bin/env python3
"""Exact small-k census for the Dyck-typed wreath slot hypergraph.

Research-only diagnostic.  All executions used for claims are run on H100.
"""

from collections import defaultdict
import itertools
import math


def dyck_words(k):
    def rec(pos, rises, height, word):
        if pos == 2 * k:
            if height == 0:
                yield tuple(word)
            return
        if rises < k:
            word.append(1)
            yield from rec(pos + 1, rises + 1, height + 1, word)
            word.pop()
        if pos - rises < k and height:
            word.append(0)
            yield from rec(pos + 1, rises, height - 1, word)
            word.pop()

    yield from rec(0, 0, 0, [])


def masks_of_size(n, k):
    return [sum(1 << x for x in ss) for ss in itertools.combinations(range(n), k)]


def profile(mask, k):
    # A={1,...,k}; record presence of 0 and A-count.
    return ((mask & 1) != 0, (mask & (((1 << (k + 1)) - 1) ^ 1)).bit_count())


def census(k):
    n = 2 * k + 1
    targets = masks_of_size(n, k)
    tid = {x: i for i, x in enumerate(targets)}
    profiles = [profile(x, k) for x in targets]
    perms = list(itertools.permutations(range(k)))
    degree = math.factorial(k) ** 2

    pair_count = defaultdict(int)
    slot_target_max = defaultdict(int)
    slot_target_global = 0

    for slot_id, word in enumerate(dyck_words(k)):
        rises = [i + 1 for i, bit in enumerate(word) if bit]
        falls = [i + 1 for i, bit in enumerate(word) if not bit]
        slot_counts = defaultdict(int)
        for pa in perms:
            base = [0] * n
            for pos, value in zip(rises, pa):
                base[pos] = value + 1
            for pb in perms:
                pi = base.copy()
                for pos, value in zip(falls, pb):
                    pi[pos] = k + value + 1
                deck = []
                for start in range(n):
                    mask = 0
                    for off in range(k):
                        mask |= 1 << pi[(start + off) % n]
                    deck.append(tid[mask])
                assert len(set(deck)) == n
                for u in deck:
                    slot_counts[u] += 1
                for i, u in enumerate(deck):
                    for v in deck[i + 1 :]:
                        lo, hi = (u, v) if u < v else (v, u)
                        pair_count[(lo, hi)] += 1
        for u, value in slot_counts.items():
            slot_target_max[profiles[u]] = max(slot_target_max[profiles[u]], value)
            slot_target_global = max(slot_target_global, value)

    by_pair_profile = defaultdict(int)
    by_distance = defaultdict(int)
    global_pair = 0
    central_pair = 0
    for (u, v), value in pair_count.items():
        pu, pv = profiles[u], profiles[v]
        dist = k - (targets[u] & targets[v]).bit_count()
        key = tuple(sorted((pu, pv))) + (dist,)
        by_pair_profile[key] = max(by_pair_profile[key], value)
        by_distance[dist] = max(by_distance[dist], value)
        global_pair = max(global_pair, value)
        # A crude central trim: A-count is within one of k/2 for both targets.
        if abs(pu[1] - k / 2) <= 1 and abs(pv[1] - k / 2) <= 1:
            central_pair = max(central_pair, value)

    print(f"k={k} degree={degree} slots={math.comb(2*k,k)//(k+1)} targets={len(targets)}")
    print("  max slot-target ratio", slot_target_global / degree)
    print("  max target-pair ratio", global_pair / degree)
    print("  crude-central target-pair ratio", central_pair / degree)
    print("  distance maxima", {j: v / degree for j, v in sorted(by_distance.items())})
    print("  slot-target profile maxima", {p: v / degree for p, v in sorted(slot_target_max.items())})
    top = sorted(by_pair_profile.items(), key=lambda kv: kv[1], reverse=True)[:20]
    print("  top pair-profile maxima")
    for key, value in top:
        print("   ", key, value / degree)


if __name__ == "__main__":
    for k in range(2, 6):
        census(k)
