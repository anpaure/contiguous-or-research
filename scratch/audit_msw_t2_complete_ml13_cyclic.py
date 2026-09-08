#!/usr/bin/env python3
"""Complete ML(13) cyclic upper-owner audit for the semilength-6 T2 relay.

The full lifted factor has four literal edge classes:

* the old/new z-free incidences X--Y;
* the unchanged complementary returns
      (z + ([12]\\Y)) -- (z + ([12]\\X));
* the vertical endpoint edges X -- (z + X).

All expensive replays belong on h100 only.
"""

from collections import Counter, defaultdict
from itertools import product

import audit_msw_t0_relay_linear_allwidth as base


M = 6
N = 2 * M
BASE_MASK = (1 << N) - 1
Z = 1 << N
FULL_MASK = (1 << (N + 1)) - 1


def word(x, n=N + 1):
    """Use the project's coordinate order (leftmost printed bit is bit 0)."""
    return format(x, f"0{n}b")[::-1]


def toggle_t2(selected):
    selected = set(selected)
    h1 = [
        ("101010001101", "101011001101", "101010001111"),
        ("100011001101", "100011001111", "101011001101"),
        ("100010001111", "101010001111", "100011001111"),
    ]
    h2 = [
        ("101011000101", "101011010101", "101011001101"),
        ("101001010101", "101001011101", "101011010101"),
        ("101001001101", "101011001101", "101001011101"),
    ]
    for owner, minus, plus in h1 + h2:
        em = (base.bits(owner), base.bits(minus))
        ep = (base.bits(owner), base.bits(plus))
        assert em in selected and ep not in selected
        selected.remove(em)
        selected.add(ep)
    return selected


def endpoint_set(canonical):
    degree = Counter(x for x, _ in canonical)
    endpoints = {x for x, d in degree.items() if d == 1}
    assert len(endpoints) == 2 * 132
    assert all((BASE_MASK ^ x) in endpoints for x in endpoints)
    return endpoints


def full_graph(zfree, canonical, endpoints):
    """Return full ML13 adjacency and edge-type ledger."""
    edges = {}

    def add(a, b, kind):
        assert a != b
        e = tuple(sorted((a, b)))
        assert e not in edges, (word(a), word(b), kind, edges.get(e))
        assert abs(a.bit_count() - b.bit_count()) == 1
        assert (a ^ b).bit_count() == 1
        edges[e] = kind

    for x, y in zfree:
        add(x, y, "free")
    for x, y in canonical:
        # Complement reverses X subset Y; adjoining z restores shores 6,7.
        add(Z | (BASE_MASK ^ y), Z | (BASE_MASK ^ x), "return")
    for x in endpoints:
        # MNW vertical matching {x0,x1}: same 12-bit set, new z bit.
        add(x, Z | x, "vertical")

    adj = defaultdict(list)
    for (a, b), kind in edges.items():
        adj[a].append((b, kind))
        adj[b].append((a, kind))

    assert len(adj) == 2 * 1716
    assert all(len(ns) == 2 for ns in adj.values())
    assert Counter(v.bit_count() for v in adj) == {6: 1716, 7: 1716}
    assert Counter(edges.values()) == {
        "free": 1584,
        "return": 1584,
        "vertical": 264,
    }
    return adj, edges


def cycles(adj, edges):
    """Traverse every component and retain cyclic rank-7 owner order/tags."""
    unseen = set(adj)
    out = []
    while unseen:
        start = min(unseen)
        prev = None
        cur = start
        verts = []
        incoming = []
        while True:
            unseen.discard(cur)
            verts.append(cur)
            opts = [(v, k) for v, k in adj[cur] if v != prev]
            if prev is None:
                # Deterministic gauge; the cyclic support is reversal invariant.
                nxt, kind = min(opts)
            else:
                assert len(opts) == 1
                nxt, kind = opts[0]
            incoming.append(kind)
            prev, cur = cur, nxt
            if cur == start:
                break
        assert len(verts) % 2 == 0
        assert all(verts[i].bit_count() != verts[(i + 1) % len(verts)].bit_count()
                   for i in range(len(verts)))
        uppers = []
        tags = []
        for i, v in enumerate(verts):
            if v.bit_count() != 7:
                continue
            uppers.append(v)
            # A z-free upper Y is a free owner.  A z-present upper z+bar X
            # belongs to the fixed complementary return.
            tags.append("F" if not (v & Z) else "R")
        assert len(uppers) * 2 == len(verts)
        assert len(uppers) == len(tags)
        out.append((uppers, tags, verts, incoming))
    return out


def cyclic_deck(cs, max_width=None):
    if max_width is None:
        max_width = max(len(c[0]) for c in cs)
    support = defaultdict(set)
    witness = {}
    occurrence = defaultdict(Counter)
    for cid, (owners, tags, _, _) in enumerate(cs):
        ell = len(owners)
        for q in range(1, min(max_width, ell) + 1):
            for i in range(ell):
                value = 0
                tagword = []
                for t in range(q):
                    j = (i + t) % ell
                    value |= owners[j]
                    tagword.append(tags[j])
                support[q].add(value)
                occurrence[q][value] += 1
                witness.setdefault((q, value), (cid, i, tuple(tagword), ell))
    return support, occurrence, witness


def boundary_type(tagword):
    if all(t == "F" for t in tagword):
        return "free-internal"
    if all(t == "R" for t in tagword):
        return "return-internal"
    transitions = sum(tagword[i] != tagword[i + 1]
                      for i in range(len(tagword) - 1))
    return f"mixed-{transitions}-internal-transitions"


def component_endpoint_trace(cs, endpoints):
    traces = []
    for owners, tags, verts, incoming in cs:
        trace = []
        for i, v in enumerate(verts):
            if v.bit_count() == 6 and not (v & Z) and v in endpoints:
                trace.append(word(v, N))
        traces.append(trace)
    return traces


def suppressed_edges(cycle, endpoints):
    """Map each suppressed upper-owner edge to its rank-6 connector type."""
    owners, tags, verts, _ = cycle
    start = next(i for i, v in enumerate(verts) if v.bit_count() == 7)
    rot = verts[start:] + verts[:start]
    assert all(rot[2 * i].bit_count() == 7 for i in range(len(owners)))
    out = {}
    for i in range(len(owners)):
        a = rot[2 * i]
        lower = rot[(2 * i + 1) % len(rot)]
        b = rot[(2 * i + 2) % len(rot)]
        e = tuple(sorted((a, b)))
        if lower & Z:
            kind = "return"
        elif lower in endpoints:
            kind = "vertical"
        else:
            kind = "free"
        assert e not in out
        out[e] = (lower, kind)
    return out


def upper_order(cycle):
    """Return one deterministic cyclic upper-owner order from full traversal."""
    owners, _, verts, _ = cycle
    start = next(i for i, v in enumerate(verts) if v.bit_count() == 7)
    rot = verts[start:] + verts[:start]
    order = [rot[2 * i] for i in range(len(owners))]
    assert set(order) == set(owners)
    return order


def solve_z13_orders(oriented_orders):
    equations = defaultdict(list)
    for order in oriented_orders:
        for a, b in zip(order, order[1:] + order[:1]):
            equations[a].append((b, 1))
            equations[b].append((a, -1))
    label = {}
    for start in equations:
        if start in label:
            continue
        label[start] = 0
        stack = [start]
        while stack:
            a = stack.pop()
            for b, delta in equations[a]:
                want = (label[a] + delta) % 13
                if b not in label:
                    label[b] = want
                    stack.append(b)
                elif label[b] != want:
                    return None, (a, b, delta, label[a], label[b], want)
    return label, None


def search_common_z13(affected_old, merged):
    old_orders = [upper_order(c) for c in affected_old]
    new_order = upper_order(merged)
    answers = []
    for nrev in range(2):
        nn = list(reversed(new_order)) if nrev else new_order
        for mask in range(32):
            orders = []
            for j, order in enumerate(old_orders):
                orders.append(list(reversed(order)) if (mask >> j) & 1 else order)
            label, conflict = solve_z13_orders(orders + [nn])
            if label is not None:
                answers.append((nrev, mask, label))
    print("common_z13_solution_count", len(answers))
    for nrev, mask, label in answers[:16]:
        print(" common_z13_solution new_reverse", nrev, "old_mask", mask,
              "label_hist", dict(sorted(Counter(label.values()).items())))
    return answers


def build_global_tag_orders(old_cycles, new_cycles, affected_old, merged, answer,
                            unchanged_shifts=None):
    """Extend one affected Z13 solution identically over unchanged cycles."""
    nrev, mask, affected_label = answer
    assert nrev == 0  # We use the first printed solution below.
    affected_sets = {frozenset(c[0]) for c in affected_old}
    merged_set = frozenset(merged[0])

    old_orders = []
    new_orders = []
    labels = dict(affected_label)

    for j, cycle in enumerate(affected_old):
        order = upper_order(cycle)
        if (mask >> j) & 1:
            order = list(reversed(order))
        old_orders.append(order)
    new_order = upper_order(merged)
    new_orders.append(new_order)

    new_by_set = {
        frozenset(c[0]): c
        for c in new_cycles
        if frozenset(c[0]) != merged_set
    }
    unchanged_shifts = unchanged_shifts or {}
    unchanged = 0
    for cycle in old_cycles:
        key = frozenset(cycle[0])
        if key in affected_sets:
            continue
        assert key in new_by_set
        order = upper_order(cycle)
        # The component is literal in both states.  Use precisely the same
        # orientation and tag origin rather than the traversal gauge of the
        # separately reconstructed new graph.
        old_orders.append(order)
        new_orders.append(list(order))
        shift = unchanged_shifts.get(unchanged, 0)
        for i, owner in enumerate(order):
            assert owner not in labels
            labels[owner] = (i + shift) % 13
        unchanged += 1
    assert unchanged == 127
    assert len(old_orders) == 132 and len(new_orders) == 128
    assert sum(map(len, old_orders)) == sum(map(len, new_orders)) == 1716
    assert len(labels) == 1716
    for orders in (old_orders, new_orders):
        for order in orders:
            assert all(
                labels[b] == (labels[a] + 1) % 13
                for a, b in zip(order, order[1:] + order[:1])
            )
    return old_orders, new_orders, labels


def private_cycle_shift_matching(losses, old_orders):
    """Match every tagged loss to a distinct unchanged cycle and origin."""
    # old_orders 0..4 are the affected cycles, 5..131 unchanged.  Store
    # local unchanged index 0..126 to make the origin certificate stable.
    candidates = {}
    for loss in losses:
        value, span, tag = loss
        bank = {}
        for cid, order in enumerate(old_orders[5:]):
            ell = len(order)
            assert ell == 13
            for i in range(ell):
                got = 0
                for j in range(span):
                    got |= order[(i + j) % ell]
                if got == value:
                    bank.setdefault(cid, (tag - i) % 13)
        candidates[loss] = bank
    hist = Counter(len(v) for v in candidates.values())
    print("private_shift_candidate_count_hist", dict(sorted(hist.items())))
    for loss in sorted(losses, key=lambda z: (len(candidates[z]), z[1], z[0], z[2])):
        print(" private_shift_candidate_count", word(loss[0]),
              "span", loss[1], "tag", loss[2], "count", len(candidates[loss]))

    zero = [loss for loss in losses if not candidates[loss]]
    if zero:
        print("private_shift_matching_INFEASIBLE zero_candidate_losses", len(zero))
        for loss in zero:
            print(" private_shift_zero", word(loss[0]),
                  "span", loss[1], "tag", loss[2])
        matchable_losses = [loss for loss in losses if candidates[loss]]
    else:
        matchable_losses = list(losses)

    cycle_to_loss = {}

    def augment(loss, seen):
        for cid in candidates[loss]:
            if cid in seen:
                continue
            seen.add(cid)
            if cid not in cycle_to_loss or augment(cycle_to_loss[cid], seen):
                cycle_to_loss[cid] = loss
                return True
        return False

    for loss in sorted(matchable_losses, key=lambda z: len(candidates[z])):
        if not augment(loss, set()):
            print(
                "private_distinct_cycle_matching_INFEASIBLE",
                word(loss[0]), "span", loss[1], "tag", loss[2],
                "candidate_cycles", len(candidates[loss]),
            )
            return None
    loss_to_cycle = {loss: cid for cid, loss in cycle_to_loss.items()}
    assert len(loss_to_cycle) == len(matchable_losses)
    shifts = {
        cid: candidates[loss][cid]
        for loss, cid in loss_to_cycle.items()
    }
    print("private_shift_matching_size", len(shifts))
    for loss in sorted(matchable_losses, key=lambda z: (z[1], z[0], z[2])):
        cid = loss_to_cycle[loss]
        order = old_orders[5 + cid]
        root = min(order)
        print(
            " private_shift_match", word(loss[0]),
            "span", loss[1], "tag", loss[2],
            "unchanged_cycle", cid, "origin_shift", shifts[cid],
            "cycle_min_owner", word(root),
        )
    return None if zero else shifts


def tagged_base_signatures(orders, labels, max_span=13):
    support = set()
    witness = {}
    for cid, order in enumerate(orders):
        ell = len(order)
        for s in range(1, min(max_span, ell) + 1):
            for i in range(ell):
                value = 0
                for j in range(s):
                    value |= order[(i + j) % ell]
                key = (value, s, labels[order[i]])
                support.add(key)
                witness.setdefault(key, (cid, i, ell))
    return support, witness


def doubled_tag_clock_support(orders, labels, h, max_base_span=13):
    """Literal support of the cyclic 13-tag, doubled-clock expansion.

    A tag-t base owner V is expanded to
      V+t+D0,...,V+t+Dh,V+(t+1)+Dh,...,V+(t+1)+D0.
    The final state joins the next base owner, whose input tag is t+1.
    For comparison with the old cycles we only need physical intervals of
    length at most 13 complete block lengths; this already includes every
    old cyclic interval width.
    """
    block_len = 2 * h + 2
    max_width = max_base_span * block_len

    def dset(t):
        return sum(1 << ((t + j) % (2 * h)) for j in range(h))

    support = set()
    witness = {}
    for cid, order in enumerate(orders):
        lifted = []
        for block, owner in enumerate(order):
            t = labels[owner]
            for j in range(h + 1):
                lifted.append((owner, 1 << t, dset(j), block, j))
            for step, j in enumerate(range(h, 2 * h + 1)):
                lifted.append((owner, 1 << ((t + 1) % 13), dset(j), block,
                               h + 1 + step))
        ell = len(lifted)
        for i in range(ell):
            base_or = tag_or = clock_or = 0
            for width in range(1, min(max_width, ell) + 1):
                owner, tag, clock, block, offset = lifted[(i + width - 1) % ell]
                base_or |= owner
                tag_or |= tag
                clock_or |= clock
                key = (base_or, width, tag_or, clock_or)
                support.add(key)
                witness.setdefault(
                    key,
                    (cid, i, width, block, offset, ell),
                )
    return support, witness


def bipartite_after_deleting(edge_sets, deleted):
    adj = defaultdict(set)
    for edges in edge_sets:
        for a, b in edges:
            if (a, b) in deleted:
                continue
            adj[a].add(b)
            adj[b].add(a)
    phase = {}
    for start in adj:
        if start in phase:
            continue
        phase[start] = 0
        stack = [start]
        while stack:
            a = stack.pop()
            for b in adj[a]:
                if b not in phase:
                    phase[b] = phase[a] ^ 1
                    stack.append(b)
                elif phase[b] == phase[a]:
                    return None
    return phase


def search_reset_transversal(affected_old, merged, endpoints):
    old_maps = [suppressed_edges(c, endpoints) for c in affected_old]
    new_map = suppressed_edges(merged, endpoints)
    common = [sorted(set(mp) & set(new_map)) for mp in old_maps]
    print("reset_common_candidate_counts", [len(c) for c in common])
    vertical = [
        [e for e in bank if mp[e][1] == "vertical"]
        for bank, mp in zip(common, old_maps)
    ]
    print("reset_vertical_candidate_counts", [len(c) for c in vertical])
    old_edge_sets = [set(mp) for mp in old_maps]
    new_edge_set = set(new_map)

    def try_banks(banks, label):
        checked = 0
        for choice in product(*banks):
            checked += 1
            deleted = set(choice)
            phase = bipartite_after_deleting(old_edge_sets + [new_edge_set], deleted)
            if phase is not None:
                print("reset_transversal", label, "checked", checked)
                for j, e in enumerate(choice):
                    lower, kind = old_maps[j][e]
                    print(
                        " reset", j,
                        "owners", word(e[0]), word(e[1]),
                        "connector", word(lower), "kind", kind,
                        "phases", phase[e[0]], phase[e[1]],
                    )
                return choice, phase
        print("reset_transversal", label, "NONE checked", checked)
        return None, None

    if all(vertical):
        answer = try_banks(vertical, "vertical-only")
        if answer[0] is not None:
            return answer
    return try_banks(common, "all-common")


def main():
    canonical = base.canonical_edges(M)
    new_zfree = toggle_t2(canonical)
    endpoints = endpoint_set(canonical)

    old_adj, old_edges = full_graph(canonical, canonical, endpoints)
    new_adj, new_edges = full_graph(new_zfree, canonical, endpoints)
    old_cycles = cycles(old_adj, old_edges)
    new_cycles = cycles(new_adj, new_edges)

    old_hist = Counter(len(c[0]) for c in old_cycles)
    new_hist = Counter(len(c[0]) for c in new_cycles)
    print("upper_owner_cycle_hist old=", dict(sorted(old_hist.items())),
          "new=", dict(sorted(new_hist.items())))
    assert old_hist == {13: 132}
    assert new_hist == {13: 127, 65: 1}

    old_trace = component_endpoint_trace(old_cycles, endpoints)
    new_trace = component_endpoint_trace(new_cycles, endpoints)
    changed_new = [t for t in new_trace if len(t) > 2]
    print("merged_endpoint_trace_count=", len(changed_new))
    for t in changed_new:
        print("merged_endpoint_trace", t)
    assert len(changed_new) == 1 and len(changed_new[0]) == 10

    old_s, old_c, old_w = cyclic_deck(old_cycles, 13)
    new_s, new_c, new_w = cyclic_deck(new_cycles, 13)
    all_losses = []
    for q in range(1, 14):
        losses = sorted(old_s[q] - new_s[q])
        births = sorted(new_s[q] - old_s[q])
        print(
            f"q={q:2d} old_support={len(old_s[q]):4d} "
            f"new_support={len(new_s[q]):4d} "
            f"loss={len(losses):3d} birth={len(births):3d}"
        )
        hist = Counter(boundary_type(old_w[(q, v)][2]) for v in losses)
        if losses:
            print("  loss_boundary_hist", dict(sorted(hist.items())))
        for v in losses[:30]:
            cid, i, tags, ell = old_w[(q, v)]
            all_losses.append((q, v))
            print("  LOSS", word(v), "old_witness", (cid, i, "".join(tags), ell),
                  "old_load", old_c[q][v])
        for v in births[:12]:
            cid, i, tags, ell = new_w[(q, v)]
            print("  BIRTH", word(v), "new_witness", (cid, i, "".join(tags), ell),
                  "new_load", new_c[q][v])

    # Topological localization: compare the complete five old cycles with
    # the one new merged cycle.  Unaffected cycles are literal.
    merged = next(c for c in new_cycles if len(c[0]) == 65)
    merged_owners = merged[0]
    merged_owner_set = set(merged_owners)
    affected_old = [c for c in old_cycles if set(c[0]) <= merged_owner_set]
    assert len(affected_old) == 5
    aff_old_s, _, aff_old_w = cyclic_deck(affected_old, 13)
    aff_new_s, _, aff_new_w = cyclic_deck(
        [merged], 13
    )
    print("affected_only")
    for q in range(1, 14):
        losses = sorted(aff_old_s[q] - aff_new_s[q])
        print(f" q={q:2d} old={len(aff_old_s[q]):3d} new={len(aff_new_s[q]):3d} "
              f"loss={len(losses):3d} birth={len(aff_new_s[q]-aff_old_s[q]):3d}")
        if losses:
            hist = Counter(boundary_type(aff_old_w[(q, v)][2]) for v in losses)
            print("   local_loss_boundary_hist", dict(sorted(hist.items())))
        for v in losses:
            ocid, oi, otags, oell = aff_old_w[(q, v)]
            ncid, ni, ntags, nell = new_w[(q, v)]
            print(
                "   LOCAL_LOSS_GLOBAL_MATE",
                word(v),
                "old_affected_witness", (ocid, oi, "".join(otags), oell),
                "new_global_witness", (ncid, ni, "".join(ntags), nell),
            )

    choice, reset_phase = search_reset_transversal(
        affected_old, merged, endpoints
    )
    assert choice is not None
    z13_answers = search_common_z13(affected_old, merged)
    assert z13_answers

    old_orders, new_orders, tag_label = build_global_tag_orders(
        old_cycles, new_cycles, affected_old, merged, z13_answers[0]
    )
    sig_old, sig_ow = tagged_base_signatures(old_orders, tag_label)
    sig_new, sig_nw = tagged_base_signatures(new_orders, tag_label)
    sig_loss = sorted(sig_old - sig_new, key=lambda x: (x[1], x[0], x[2]))
    print(
        "tagged_base_signature",
        "old", len(sig_old), "new", len(sig_new),
        "loss", len(sig_loss), "birth", len(sig_new - sig_old),
    )
    for key in sig_loss[:80]:
        print(" TAGGED_BASE_LOSS", word(key[0]), "span", key[1], "tag", key[2],
              "old", sig_ow[key])

    private_shifts = private_cycle_shift_matching(sig_loss, old_orders)
    if private_shifts is not None:
        old_orders, new_orders, tag_label = build_global_tag_orders(
            old_cycles, new_cycles, affected_old, merged, z13_answers[0],
            private_shifts,
        )
        sig_old, sig_ow = tagged_base_signatures(old_orders, tag_label)
        sig_new, sig_nw = tagged_base_signatures(new_orders, tag_label)
        sig_loss = sorted(sig_old - sig_new, key=lambda x: (x[1], x[0], x[2]))
        print(
            "shifted_tagged_base_signature",
            "old", len(sig_old), "new", len(sig_new),
            "loss", len(sig_loss), "birth", len(sig_new - sig_old),
        )

    for h in (2, 3, 4):
        ls_old, lw_old = doubled_tag_clock_support(old_orders, tag_label, h)
        ls_new, lw_new = doubled_tag_clock_support(new_orders, tag_label, h)
        loss = sorted(ls_old - ls_new, key=lambda x: (x[1], x[0], x[2], x[3]))
        print(
            "doubled_tag_clock_support h", h,
            "old", len(ls_old), "new", len(ls_new),
            "loss", len(loss), "birth", len(ls_new - ls_old),
        )
        for key in loss[:40]:
            print(
                " TAG_CLOCK_LOSS", word(key[0]), "width", key[1],
                "tags", format(key[2], "013b")[::-1],
                "clock", format(key[3], f"0{2*h}b")[::-1],
                "old", lw_old[key],
            )

    # Odd base owner cycles have length 13.  Their Johnson adjacency graph
    # cannot carry an alternating {0,1} phase around the complete closure.
    print("complete_cycle_phase_obstruction=odd_upper_owner_length_13")


if __name__ == "__main__":
    main()
