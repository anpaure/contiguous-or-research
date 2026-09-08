#!/usr/bin/env python3
"""Variable-successor tag quotient audit for the complete ML(13) T2 relay.

Heavy runs belong on h100 only.
"""

from collections import Counter

import audit_msw_t0_relay_linear_allwidth as base
import audit_msw_t2_complete_ml13_cyclic as full


class DSU:
    def __init__(self, values):
        self.parent = {v: v for v in values}
        self.size = {v: 1 for v in values}

    def find(self, v):
        while self.parent[v] != v:
            self.parent[v] = self.parent[self.parent[v]]
            v = self.parent[v]
        return v

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.parent[b] = a
        self.size[a] += self.size[b]


def successor_map(orders):
    out = {}
    for order in orders:
        for a, b in zip(order, order[1:] + order[:1]):
            assert a not in out
            out[a] = b
    return out


def full_word_signatures(orders, succ, cls, max_span=13):
    support = set()
    witness = {}
    for cid, order in enumerate(orders):
        ell = len(order)
        for s in range(1, min(max_span, ell) + 1):
            for i in range(ell):
                value = 0
                tau = []
                for j in range(s):
                    v = order[(i + j) % ell]
                    value |= v
                    tau.append((cls[v], cls[succ[v]]))
                key = (value, s, tuple(tau))
                support.add(key)
                witness.setdefault(key, (cid, i, ell))
    return support, witness


def cyclic_run_minima(orders):
    positive = []
    zero = []
    witnesses = []
    for cid, order in enumerate(orders):
        ell = len(order)
        for bit in range(13):
            seq = [bool(v >> bit & 1) for v in order]
            if all(seq) or not any(seq):
                continue
            # Cyclic run lengths from transition points.
            runs = []
            for i in range(ell):
                if seq[i] == seq[i - 1]:
                    continue
                val = seq[i]
                length = 1
                while length < ell and seq[(i + length) % ell] == val:
                    length += 1
                runs.append((val, length, i))
            for val, length, i in runs:
                (positive if val else zero).append(length)
                witnesses.append((length, val, cid, bit, i, ell, order[i]))
    return min(positive), min(zero), sorted(witnesses)


def reconstruct():
    canonical = base.canonical_edges(full.M)
    new_zfree = full.toggle_t2(canonical)
    endpoints = full.endpoint_set(canonical)
    old_adj, old_edges = full.full_graph(canonical, canonical, endpoints)
    new_adj, new_edges = full.full_graph(new_zfree, canonical, endpoints)
    old_cycles = full.cycles(old_adj, old_edges)
    new_cycles = full.cycles(new_adj, new_edges)
    merged = next(c for c in new_cycles if len(c[0]) == 65)
    merged_set = set(merged[0])
    affected_old = [c for c in old_cycles if set(c[0]) <= merged_set]
    answers = full.search_common_z13(affected_old, merged)
    assert len(answers) == 2
    old_orders, new_orders, _ = full.build_global_tag_orders(
        old_cycles, new_cycles, affected_old, merged, answers[0]
    )
    return old_orders, new_orders


def main():
    old_orders, new_orders = reconstruct()
    owners = {v for order in old_orders for v in order}
    assert owners == {v for order in new_orders for v in order}
    sold = successor_map(old_orders)
    snew = successor_map(new_orders)

    dsu = DSU(owners)
    changed = []
    for v in owners:
        dsu.union(sold[v], snew[v])
        if sold[v] != snew[v]:
            changed.append(v)
    cls = {v: dsu.find(v) for v in owners}
    classes = Counter(cls.values())
    loops = sorted(v for v in owners if cls[v] == cls[sold[v]])
    print("successor_changed_tails", len(changed))
    print("base_successor_quotient_classes", len(classes),
          "size_hist", dict(sorted(Counter(classes.values()).items())),
          "required_tag_change_loops", len(loops))
    for v in loops[:30]:
        print(" LOOP", full.word(v), "succ", full.word(sold[v]))

    so, wo = full_word_signatures(old_orders, sold, cls)
    sn, wn = full_word_signatures(new_orders, snew, cls)
    losses = sorted(so - sn, key=lambda z: (z[1], z[0], z[2]))
    print("private_successor_class_signature",
          "old", len(so), "new", len(sn),
          "loss", len(losses), "birth", len(sn - so))
    for key in losses[:120]:
        print(" LOSS", full.word(key[0]), "span", key[1],
              "tau", key[2], "old", wo[key])

    pmin, zmin, run_w = cyclic_run_minima(new_orders)
    print("new_complete_owner_run_min positive", pmin, "zero", zmin)
    for row in run_w[:20]:
        length, val, cid, bit, i, ell, owner = row
        print(" RUN_MIN", "positive" if val else "zero", "length", length,
              "cycle", cid, "coord", bit, "start", i,
              "cycle_length", ell, "owner", full.word(owner))


if __name__ == "__main__":
    main()
