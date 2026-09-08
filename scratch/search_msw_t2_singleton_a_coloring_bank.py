#!/usr/bin/env python3
"""Search legal three-colour singleton-a clocks and global reversals.

The objective is exact support of the union of parallel copies at h=2.
Heavy search belongs on h100 only.
"""

from collections import defaultdict
import random
import sys

import audit_msw_t2_singleton_a_clock as one


def quotient_graph(owners, sold, snew):
    dsu = one.DSU(owners)
    for v in owners:
        if v != one.A:
            dsu.union(sold[v], snew[v])
    dsu.union(one.A, sold[one.A])
    dsu.union(one.A, snew[one.A])
    classes = sorted({dsu.find(v) for v in owners})
    adj = {c: set() for c in classes}
    for v in owners:
        if v == one.A:
            continue
        a, b = dsu.find(v), dsu.find(sold[v])
        assert a != b
        adj[a].add(b)
        adj[b].add(a)
    return dsu, classes, adj


def random_dsatur(dsu, classes, adj, owners, seed):
    rng = random.Random(seed)
    colour = {}
    saturation = {c: set() for c in classes}
    while len(colour) < len(classes):
        score = max(
            (len(saturation[c]), len(adj[c]))
            for c in classes if c not in colour
        )
        bank = [
            c for c in classes if c not in colour
            and (len(saturation[c]), len(adj[c])) == score
        ]
        v = rng.choice(bank)
        available = [z for z in range(3)
                     if z not in {colour[w] for w in adj[v] if w in colour}]
        if not available:
            return None
        z = rng.choice(available)
        colour[v] = z
        for w in adj[v]:
            if w not in colour:
                saturation[w].add(z)

    central = colour[dsu.find(one.A)]
    if central != 0:
        # Normalize the literal singleton payload to tag 0.
        for c in colour:
            if colour[c] == 0:
                colour[c] = central
            elif colour[c] == central:
                colour[c] = 0
    tag = {v: colour[dsu.find(v)] for v in owners}
    assert tag[one.A] == 0
    return tag


def support(cycles):
    out = set()
    for cycle in cycles:
        ell = len(cycle)
        for i in range(ell):
            bo = to = co = 0
            for width in range(1, ell + 1):
                x = cycle[(i + width - 1) % ell]
                bo |= x[0]
                to |= x[1]
                co |= x[2]
                out.add((bo, width, to, co))
    return out


def scheme(old_orders, new_orders, sold, snew, tag, h=2):
    so = support(one.expand_orders(old_orders, sold, tag, h))
    sn = support(one.expand_orders(new_orders, snew, tag, h))
    return so, sn


def main():
    trials = int(sys.argv[1]) if len(sys.argv) > 1 else 64
    old0, new0, sold0, snew0 = one.reconstruct()
    owners = set(sold0)
    base_tag, _ = one.quotient_and_coloring(owners, sold0, snew0)
    base_so, base_sn = scheme(old0, new0, sold0, snew0, base_tag)
    base_loss = base_so - base_sn
    print("baseline", len(base_so), len(base_sn), len(base_loss))

    best = None
    seen = set()
    top = []
    for reverse in (0, 1):
        old = [list(reversed(o)) for o in old0] if reverse else old0
        new = [list(reversed(o)) for o in new0] if reverse else new0
        sold = one.qbase.successor_map(old)
        snew = one.qbase.successor_map(new)
        dsu, classes, adj = quotient_graph(owners, sold, snew)
        print("orientation", reverse,
              "classes", len(classes),
              "degree_hist", {
                  z: sum(len(adj[c]) == z for c in classes)
                  for z in sorted({len(adj[c]) for c in classes})
              })
        legal = 0
        for seed in range(trials):
            tag = random_dsatur(dsu, classes, adj, owners,
                                seed + reverse * 10_000_000)
            if tag is None:
                continue
            fingerprint = tuple(tag[v] for v in sorted(owners))
            if fingerprint in seen:
                continue
            seen.add(fingerprint)
            legal += 1
            so, sn = scheme(old, new, sold, snew, tag)
            individual = len(so - sn)
            base_covered = len(base_loss & sn)
            union_loss_set = (base_so | so) - (base_sn | sn)
            row = (
                len(union_loss_set), individual, -base_covered,
                reverse, seed, tag, so, sn,
            )
            if best is None or row[:5] < best[:5]:
                best = row
                print(
                    "BEST_PAIR",
                    "union_loss", row[0],
                    "individual", individual,
                    "baseline_loss_covered", base_covered,
                    "reverse", reverse, "seed", seed,
                    "tag_hist", {
                        z: sum(t == z for t in tag.values()) for z in range(3)
                    },
                )
            top.append(row)
        print("orientation_legal_unique", reverse, legal)

    top.sort(key=lambda r: r[:5])
    print("TOP_PAIRS")
    for row in top[:20]:
        print(row[:5], "covered", -row[2])

    # Greedily test banks of up to four schemes, starting with baseline and
    # repeatedly choosing the candidate with smallest exact union loss.
    union_old = set(base_so)
    union_new = set(base_sn)
    used = []
    for step in range(1, 5):
        choice = None
        for row in top:
            if (row[3], row[4]) in used:
                continue
            loss = len((union_old | row[6]) - (union_new | row[7]))
            score = (loss, row[0], row[1], row[3], row[4])
            if choice is None or score < choice[0]:
                choice = (score, row)
        assert choice is not None
        row = choice[1]
        used.append((row[3], row[4]))
        union_old |= row[6]
        union_new |= row[7]
        print("GREEDY_BANK", step + 1,
              "added_reverse_seed", used[-1],
              "union_old", len(union_old), "union_new", len(union_new),
              "loss", len(union_old - union_new),
              "birth", len(union_new - union_old))
        if not union_old - union_new:
            break


if __name__ == "__main__":
    main()
