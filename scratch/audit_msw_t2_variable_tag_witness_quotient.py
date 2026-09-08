#!/usr/bin/env python3
"""Select a loop-free base-arc witness quotient for the complete T2 relay.

This is the finite gate in the variable-successor tag theorem.  Heavy runs
belong on h100 only.
"""

from collections import Counter, defaultdict

import audit_msw_t2_variable_tag_quotient as q
import audit_msw_t2_complete_ml13_cyclic as full


class RollbackDSU:
    def __init__(self, values):
        self.parent = {v: v for v in values}
        self.size = {v: 1 for v in values}
        self.stack = []

    def find(self, v):
        while self.parent[v] != v:
            v = self.parent[v]
        return v

    def checkpoint(self):
        return len(self.stack)

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            self.stack.append(None)
            return False
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.stack.append((b, a, self.size[a]))
        self.parent[b] = a
        self.size[a] += self.size[b]
        return True

    def rollback(self, mark):
        while len(self.stack) > mark:
            item = self.stack.pop()
            if item is None:
                continue
            b, a, old_size = item
            self.parent[b] = b
            self.size[a] = old_size


def arcs(orders, max_span=13):
    out = []
    for cid, order in enumerate(orders):
        ell = len(order)
        for s in range(1, min(max_span, ell) + 1):
            for i in range(ell):
                seq = tuple(order[(i + j) % ell] for j in range(s))
                value = 0
                for v in seq:
                    value |= v
                out.append((value, s, seq, cid, i, ell))
    return out


def constraints(old_arc, new_arc, sold, snew):
    pairs = []
    for v, w in zip(old_arc[2], new_arc[2]):
        pairs.append((v, w))
        pairs.append((sold[v], snew[w]))
    return pairs


def has_loop(dsu, forbidden):
    return any(dsu.find(a) == dsu.find(b) for a, b in forbidden)


def try_candidate(dsu, pairs, forbidden, commit=False):
    mark = dsu.checkpoint()
    merges = 0
    for a, b in pairs:
        merges += dsu.union(a, b)
    bad = has_loop(dsu, forbidden)
    if bad or not commit:
        dsu.rollback(mark)
    return (not bad), merges


def signature_support(orders, succ, cls, max_span=13):
    support = set()
    for value, s, seq, _, _, _ in arcs(orders, max_span):
        tau = tuple((cls[v], cls[succ[v]]) for v in seq)
        support.add((value, s, tau))
    return support


def main():
    old_orders, new_orders = q.reconstruct()
    owners = {v for order in old_orders for v in order}
    sold = q.successor_map(old_orders)
    snew = q.successor_map(new_orders)
    forbidden = list(sold.items())

    dsu = RollbackDSU(owners)
    for v in owners:
        dsu.union(sold[v], snew[v])
    assert not has_loop(dsu, forbidden)

    old_arcs = arcs(old_orders)
    new_arcs = arcs(new_orders)
    new_by_key = defaultdict(list)
    new_sequences = set()
    for arc in new_arcs:
        new_by_key[arc[:2]].append(arc)
        new_sequences.add(arc[2])

    nonliteral = [arc for arc in old_arcs if arc[2] not in new_sequences]
    print("old_arc_occurrences", len(old_arcs),
          "new_arc_occurrences", len(new_arcs),
          "nonliteral_old_arcs", len(nonliteral))
    print("nonliteral_candidate_hist",
          dict(sorted(Counter(len(new_by_key[a[:2]]) for a in nonliteral).items())))

    # Fail-first ordering; within ties, short arcs first and lexicographic
    # occurrence names make the certificate deterministic.
    nonliteral.sort(key=lambda a: (len(new_by_key[a[:2]]), a[1], a[2]))
    chosen = []
    for step, old_arc in enumerate(nonliteral):
        ranked = []
        for new_arc in new_by_key[old_arc[:2]]:
            pairs = constraints(old_arc, new_arc, sold, snew)
            good, merges = try_candidate(dsu, pairs, forbidden, commit=False)
            if not good:
                continue
            same = sum(v == w for v, w in zip(old_arc[2], new_arc[2]))
            unaffected = new_arc[5] == 13
            ranked.append((merges, -same, not unaffected, new_arc, pairs))
        if not ranked:
            print("GREEDY_STUCK", step,
                  "value", full.word(old_arc[0]), "span", old_arc[1],
                  "old", old_arc[3:])
            raise SystemExit(2)
        ranked.sort(key=lambda x: (x[0], x[1], x[2], x[3][2]))
        merges, _, _, new_arc, pairs = ranked[0]
        good, actual = try_candidate(dsu, pairs, forbidden, commit=True)
        assert good and actual == merges
        chosen.append((old_arc, new_arc, merges, len(ranked)))
        if step < 40 or step % 50 == 49:
            print("CHOOSE", step, "value", full.word(old_arc[0]),
                  "span", old_arc[1], "old", old_arc[3:5],
                  "new", new_arc[3:5], "new_cycle_len", new_arc[5],
                  "merges", merges, "safe_options", len(ranked))

    assert not has_loop(dsu, forbidden)
    cls = {v: dsu.find(v) for v in owners}
    class_sizes = Counter(cls.values())
    so = signature_support(old_orders, sold, cls)
    sn = signature_support(new_orders, snew, cls)
    losses = so - sn
    print("final_quotient_classes", len(class_sizes),
          "size_hist", dict(sorted(Counter(class_sizes.values()).items())))
    print("final_full_word_signature old", len(so), "new", len(sn),
          "loss", len(losses), "birth", len(sn - so))
    assert not losses

    print("NONLITERAL_WITNESS_TABLE_BEGIN")
    for old_arc, new_arc, merges, safe in chosen:
        print(
            full.word(old_arc[0]), old_arc[1],
            old_arc[3], old_arc[4],
            new_arc[3], new_arc[4], new_arc[5],
            merges, safe,
            ":",
            ",".join(full.word(v) for v in old_arc[2]),
            "=>",
            ",".join(full.word(v) for v in new_arc[2]),
        )
    print("NONLITERAL_WITNESS_TABLE_END")


if __name__ == "__main__":
    main()
