#!/usr/bin/env python3
"""Hybrid singleton-a variable-tag clock for the complete ML(13) T2 relay.

The exceptional upper owner a is a single lifted owner with payload
{p}+D0.  Every other upper owner uses the forward doubled clock block.
Heavy replays belong on h100 only.
"""

from collections import Counter, defaultdict
import hashlib
import sys

import audit_msw_t0_relay_linear_allwidth as base
import audit_msw_t2_complete_ml13_cyclic as full
import audit_msw_t2_variable_tag_quotient as qbase


A = base.bits("1010110011010")
B = base.bits("1011100011010")
C = base.bits("1011110001010")
D = base.bits("1010011011010")
E = base.bits("1000111011010")


class DSU:
    def __init__(self, values):
        self.p = {v: v for v in values}
        self.sz = {v: 1 for v in values}

    def find(self, v):
        if self.p[v] != v:
            self.p[v] = self.find(self.p[v])
        return self.p[v]

    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b:
            return
        if self.sz[a] < self.sz[b]:
            a, b = b, a
        self.p[b] = a
        self.sz[a] += self.sz[b]


def reconstruct():
    old_orders, new_orders = qbase.reconstruct()
    sold = qbase.successor_map(old_orders)
    snew = qbase.successor_map(new_orders)
    assert sold[A] == B and snew[A] == E
    assert next(v for v in sold if sold[v] == A) == D
    assert next(v for v in snew if snew[v] == A) == C
    return old_orders, new_orders, sold, snew


def quotient_and_coloring(owners, sold, snew, forced_zero_owners=()):
    dsu = DSU(owners)
    # Every normal tail has one literal output tag in both states.
    for v in owners:
        if v == A:
            continue
        dsu.union(sold[v], snew[v])
    # The singleton payload is also the starting payload of both successors.
    dsu.union(A, B)
    dsu.union(A, E)

    classes = sorted({dsu.find(v) for v in owners})
    members = defaultdict(list)
    for v in owners:
        members[dsu.find(v)].append(v)
    conflict = {c: set() for c in classes}
    loops = []
    for v in owners:
        if v == A:
            continue
        x, y = dsu.find(v), dsu.find(sold[v])
        if x == y:
            loops.append(v)
        conflict[x].add(y)
        conflict[y].add(x)
    print("singleton_quotient classes", len(classes),
          "size_hist", dict(sorted(Counter(map(len, members.values())).items())),
          "loops", len(loops),
          "degree_hist", dict(sorted(Counter(map(len, conflict.values())).items())))
    for v in loops:
        print(" SINGLETON_QUOTIENT_LOOP", full.word(v), full.word(sold[v]))
    assert not loops

    # Deterministic DSATUR.  We seek a small constant alphabet, not minimum
    # chromaticity; the graph has maximum degree at most four in this case.
    colour = {}
    for owner in (A, *forced_zero_owners):
        c = dsu.find(owner)
        for other in conflict[c]:
            assert colour.get(other) != 0
        colour[c] = 0
    saturation = {c: set() for c in classes}
    for c in colour:
        for w in conflict[c]:
            saturation[w].add(colour[c])
    while len(colour) < len(classes):
        v = max(
            (c for c in classes if c not in colour),
            key=lambda c: (len(saturation[c]), len(conflict[c]), -c),
        )
        used = {colour[w] for w in conflict[v] if w in colour}
        z = 0
        while z in used:
            z += 1
        colour[v] = z
        for w in conflict[v]:
            if w not in colour:
                saturation[w].add(z)
    tag = {v: colour[dsu.find(v)] for v in owners}
    p = 1 + max(tag.values())
    print("singleton_tag_alphabet", p,
          "tag_hist", dict(sorted(Counter(tag.values()).items())),
          "a_b_e_tags", tag[A], tag[B], tag[E],
          "c_d_tags", tag[C], tag[D])
    tag_certificate = "\n".join(
        f"{full.word(v)} {tag[v]}" for v in sorted(owners)
    ).encode()
    print("singleton_tag_assignment_sha256",
          hashlib.sha256(tag_certificate).hexdigest())
    assert tag[A] == tag[B] == tag[E]
    for v in owners:
        if v == A:
            continue
        assert tag[sold[v]] == tag[snew[v]]
        assert tag[v] != tag[sold[v]]
    return tag, p


def block(owner, output_tag, tag, h, reflected=False):
    def dset(j):
        return sum(1 << ((j + k) % (2 * h)) for k in range(h))

    if owner == A:
        assert tag[owner] == output_tag
        return [(owner, 1 << tag[owner], dset(0), 0, "singleton")]
    out = []
    for j in range(h + 1):
        clock_j = (-j) % (2 * h) if reflected else j
        out.append((owner, 1 << tag[owner], dset(clock_j), j, "first"))
    for step, j in enumerate(range(h, 2 * h + 1)):
        clock_j = (-j) % (2 * h) if reflected else j
        out.append((owner, 1 << output_tag, dset(clock_j), h + 1 + step, "second"))
    return out


def expand_orders(orders, succ, tag, h, reflected_owners=frozenset()):
    cycles = []
    occurrence_count = 0
    for cid, order in enumerate(orders):
        lifted = []
        for owner in order:
            output_tag = tag[succ[owner]]
            lifted.extend(block(
                owner, output_tag, tag, h,
                reflected=owner in reflected_owners,
            ))
            occurrence_count += 1
        # Literal Johnson adjacency in the disjoint base/tag/clock product.
        for x, y in zip(lifted, lifted[1:] + lifted[:1]):
            base_delta = (x[0] ^ y[0]).bit_count()
            tag_delta = (x[1] ^ y[1]).bit_count()
            clock_delta = (x[2] ^ y[2]).bit_count()
            assert base_delta + tag_delta + clock_delta == 2, (
                cid, x, y, base_delta, tag_delta, clock_delta
            )
            assert (x[0].bit_count() + x[1].bit_count() + x[2].bit_count()
                    == 7 + 1 + h)
        cycles.append(lifted)
    assert occurrence_count == 1716
    return cycles


def deck(cycles):
    support = set()
    witness = {}
    by_width = defaultdict(set)
    for cid, cycle in enumerate(cycles):
        ell = len(cycle)
        for i in range(ell):
            base_or = tag_or = clock_or = 0
            first = cycle[i]
            previous_owner = None
            base_span = 0
            contains_a = False
            for width in range(1, ell + 1):
                owner, t, clock, _, kind = cycle[(i + width - 1) % ell]
                if owner != previous_owner:
                    base_span += 1
                    previous_owner = owner
                contains_a |= owner == A
                base_or |= owner
                tag_or |= t
                clock_or |= clock
                key = (base_or, width, tag_or, clock_or)
                support.add(key)
                by_width[width].add((base_or, tag_or, clock_or))
                witness.setdefault(
                    key,
                    (
                        cid, i, ell,
                        first[4], kind,
                        first[3], cycle[(i + width - 1) % ell][3],
                        base_span, contains_a,
                        first[0], owner,
                    ),
                )
    return support, witness, by_width


def palettes(cycles):
    owners = Counter()
    lower = Counter()
    upper = Counter()
    for cycle in cycles:
        for x in cycle:
            key = (x[0], x[1], x[2])
            owners[key] += 1
        for x, y in zip(cycle, cycle[1:] + cycle[:1]):
            # Base/tag/clock grounds are disjoint, so componentwise AND/OR
            # are the literal lower and upper tickets after adjoining core.
            lower[(x[0] & y[0], x[1] & y[1], x[2] & y[2])] += 1
            upper[(x[0] | y[0], x[1] | y[1], x[2] | y[2])] += 1
    return owners, lower, upper


def run_minima(cycles, p, h):
    # Ground coordinates: 13 base, p tags, 2h clocks.  Ignore constants.
    result = {"base": [10**9, 10**9],
              "tag": [10**9, 10**9],
              "clock": [10**9, 10**9]}
    witness = {}
    for cid, cycle in enumerate(cycles):
        layers = [
            ("base", 13, lambda x: x[0]),
            ("tag", p, lambda x: x[1]),
            ("clock", 2 * h, lambda x: x[2]),
        ]
        for layer, n, getter in layers:
            ell = len(cycle)
            for bit in range(n):
                seq = [bool(getter(x) >> bit & 1) for x in cycle]
                if all(seq) or not any(seq):
                    continue
                for i in range(ell):
                    if seq[i] == seq[i - 1]:
                        continue
                    val = int(seq[i])
                    length = 1
                    while length < ell and seq[(i + length) % ell] == seq[i]:
                        length += 1
                    if length < result[layer][val]:
                        result[layer][val] = length
                        witness[(layer, val)] = (cid, bit, i, ell, cycle[i])
    return result, witness


def target_seams(cycles, target):
    out = []
    for cid, cycle in enumerate(cycles):
        ell = len(cycle)
        for i, x in enumerate(cycle):
            y = cycle[(i + 1) % ell]
            if x[0] | y[0] == target:
                out.append((cid, i, ell, x, y,
                            x[1] | y[1], x[2] | y[2]))
    return out


def main():
    old_orders, new_orders, sold, snew = reconstruct()
    owners = set(sold)
    force_backup = "--force-z-backup" in sys.argv
    backup_head = base.bits("0000111011110")
    tag, p = quotient_and_coloring(
        owners, sold, snew,
        (backup_head,) if force_backup else (),
    )
    print("force_z_backup", force_backup,
          "backup_head_tag", tag[backup_head])
    numeric = [a for a in sys.argv[1:] if not a.startswith("--")]
    hmax = int(numeric[0]) if numeric else 12
    for h in range(2, hmax + 1):
        old_cycles = expand_orders(old_orders, sold, tag, h)
        new_cycles = expand_orders(new_orders, snew, tag, h)
        oh = Counter(map(len, old_cycles))
        nh = Counter(map(len, new_cycles))
        so, wo, bow = deck(old_cycles)
        sn, wn, bnw = deck(new_cycles)
        losses = sorted(so - sn, key=lambda z: (z[1], z[0], z[2], z[3]))
        po = palettes(old_cycles)
        pn = palettes(new_cycles)
        old_simple = tuple(max(c.values()) for c in po)
        new_simple = tuple(max(c.values()) for c in pn)
        rmin, rw = run_minima(new_cycles, p, h)
        print(
            "singleton_clock h", h,
            "cycle_hist_old", dict(sorted(oh.items())),
            "cycle_hist_new", dict(sorted(nh.items())),
            "old", len(so), "new", len(sn),
            "loss", len(losses), "birth", len(sn - so),
            "palette_max_old", old_simple,
            "palette_max_new", new_simple,
            "run_min_new", rmin,
        )
        if losses:
            print(
                " singleton_loss_width_hist",
                dict(sorted(Counter(key[1] for key in losses).items())),
            )
            print(
                " singleton_loss_base_span_hist",
                dict(sorted(Counter(wo[key][7] for key in losses).items())),
            )
            print(
                " singleton_loss_base_rank_hist",
                dict(sorted(Counter(key[0].bit_count() for key in losses).items())),
            )
            print(
                " singleton_loss_target_rank_excess_hist",
                dict(sorted(Counter(
                    key[0].bit_count()
                    + key[2].bit_count()
                    + key[3].bit_count()
                    - (8 + h)
                    for key in losses
                ).items())),
            )
            print(
                " singleton_loss_endpoint_kind_hist",
                dict(sorted(Counter((wo[key][3], wo[key][4])
                                    for key in losses).items())),
            )
            print(
                " singleton_loss_contains_a_hist",
                dict(sorted(Counter(wo[key][8] for key in losses).items())),
            )
            print(
                " singleton_loss_span_rank_hist",
                dict(sorted(Counter((wo[key][7], key[0].bit_count())
                                    for key in losses).items())),
            )
            for key in losses:
                w = wo[key]
                rank_excess = (
                    key[0].bit_count()
                    + key[2].bit_count()
                    + key[3].bit_count()
                    - (8 + h)
                )
                print(
                    " LOSS_RECORD",
                    "h", h,
                    "base", full.word(key[0]),
                    "base_span", w[7],
                    "base_rank", key[0].bit_count(),
                    "target_rank_excess", rank_excess,
                    "physical_width", key[1],
                    "contains_a", int(w[8]),
                    "start", w[3], w[5],
                    "end", w[4], w[6],
                    "tag_mask", format(key[2], f"0{p}b")[::-1],
                    "clock_mask", format(key[3], f"0{2*h}b")[::-1],
                    "old_cycle_start_length", w[0], w[1], w[2],
                )
        for key in losses[:30]:
            print(
                " SINGLETON_LOSS", full.word(key[0]), "width", key[1],
                "tags", format(key[2], f"0{p}b")[::-1],
                "clock", format(key[3], f"0{2*h}b")[::-1],
                "old", wo[key],
            )
        for name, target in (
            ("T0", base.bits("1100110011110")),
            ("B", base.bits("1011110011010")),
            ("C", base.bits("1010111011010")),
        ):
            old_seams = target_seams(old_cycles, target)
            new_seams = target_seams(new_cycles, target)
            print(" target", name, "old_seams", len(old_seams),
                  "new_seams", len(new_seams))
            for row in new_seams[:8]:
                cid, i, ell, x, y, tu, cu = row
                print("  NEW_TARGET", name, cid, i, ell,
                      full.word(x[0]), x[4], "->", full.word(y[0]), y[4],
                      "tags", format(tu, f"0{p}b")[::-1],
                      "clock", format(cu, f"0{2*h}b")[::-1])


if __name__ == "__main__":
    main()
