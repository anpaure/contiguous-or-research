#!/usr/bin/env python3
"""Resident no-new-label edge halos for the reflected singleton T2 clock.

At an unreflected/reflected cut, use the unused half-clock arc, swap the
base owner at its far endpoint, and return along the same arc.  Heavy runs
belong on h100 only.
"""

from collections import Counter
import sys

import audit_msw_t2_singleton_a_clock as s
import search_msw_t2_singleton_clock_reflections as r


REFLECTED = {s.C, s.D}


def dset(h, j):
    return sum(1 << ((j + k) % (2 * h)) for k in range(h))


def expand_halo(orders, succ, tag, h):
    cycles = []
    for order in orders:
        lifted = []
        ell = len(order)
        for i, v in enumerate(order):
            w = order[(i + 1) % ell]
            assert succ[v] == w
            lifted.extend(s.block(
                v, tag[w], tag, h, reflected=v in REFLECTED
            ))
            if (v in REFLECTED) == (w in REFLECTED):
                continue
            sign = -1 if v in REFLECTED else 1
            p = tag[w]
            # Endpoints v+p+D0 and w+p+D0 are already supplied by the
            # adjacent blocks.  Insert only the simple internal bounce.
            for k in range(1, h):
                lifted.append((v, 1 << p, dset(h, sign * k),
                               k, "halo_tail"))
            for k in range(h - 1, 0, -1):
                lifted.append((w, 1 << p, dset(h, sign * k),
                               2 * h - k, "halo_head"))

        # Exact graph and owner simplicity.
        keys = [(x[0], x[1], x[2]) for x in lifted]
        assert len(keys) == len(set(keys)), "owner repeat within component"
        for x, y in zip(lifted, lifted[1:] + lifted[:1]):
            delta = ((x[0] ^ y[0]).bit_count()
                     + (x[1] ^ y[1]).bit_count()
                     + (x[2] ^ y[2]).bit_count())
            assert delta == 2, (x, y, delta)
        cycles.append(lifted)
    all_keys = [(x[0], x[1], x[2]) for c in cycles for x in c]
    assert len(all_keys) == len(set(all_keys)), "owner repeat across components"
    return cycles


def expand_full_halo(orders, succ, tag, h, halo_tag):
    cycles = []
    for order in orders:
        lifted = []
        ell = len(order)
        for i, v in enumerate(order):
            w = order[(i + 1) % ell]
            assert succ[v] == w
            lifted.extend(s.block(
                v, tag[w], tag, h, reflected=v in REFLECTED
            ))
            if (v in REFLECTED) == (w in REFLECTED):
                continue
            q = halo_tag[(v, w)]
            # The adjacent p+D0 endpoints are already in the normal blocks.
            # A private-q full bounce leaves D0 in the tail orientation,
            # swaps the base owner at the opposite cut, and returns to D0
            # in the head orientation.  This is the chronology-changing
            # halo; a single forward clock turn would retain the old
            # orientation and leave a run-two bounce at its far boundary.
            sign = 1 if v not in REFLECTED else -1
            js = [(sign * j) % (2 * h) for j in range(0, 2 * h)]
            for step, j in enumerate(js):
                lifted.append((v, 1 << q, dset(h, j), step,
                               "full_halo_tail"))
            for step, j in enumerate(reversed(js)):
                lifted.append((w, 1 << q, dset(h, j), 2 * h + step,
                               "full_halo_head"))

        keys = [(x[0], x[1], x[2]) for x in lifted]
        assert len(keys) == len(set(keys)), "full halo owner repeat"
        for x, y in zip(lifted, lifted[1:] + lifted[:1]):
            delta = ((x[0] ^ y[0]).bit_count()
                     + (x[1] ^ y[1]).bit_count()
                     + (x[2] ^ y[2]).bit_count())
            assert delta == 2, (x, y, delta)
        cycles.append(lifted)
    all_keys = [(x[0], x[1], x[2]) for c in cycles for x in c]
    assert len(all_keys) == len(set(all_keys)), "full halo global repeat"
    return cycles


def owner_support(cycles):
    return {(x[0], x[1], x[2]) for c in cycles for x in c}


def main():
    hmax = int(sys.argv[1]) if len(sys.argv) > 1 else 8
    old, new, sold, snew = s.reconstruct()
    owners = set(sold)
    head = s.base.bits("0000111011110")
    tag, p = s.quotient_and_coloring(owners, sold, snew, (head,))
    union_cut_edges = sorted({
        (v, w)
        for succ in (sold, snew)
        for v, w in succ.items()
        if (v in REFLECTED) != (w in REFLECTED)
    })
    halo_tag = {edge: p + j for j, edge in enumerate(union_cut_edges)}
    print("full_halo_edge_count", len(union_cut_edges))
    for edge, z in halo_tag.items():
        print(" full_halo_tag", z, s.full.word(edge[0]), s.full.word(edge[1]))
    for h in range(2, hmax + 1):
        oc = expand_halo(old, sold, tag, h)
        nc = expand_halo(new, snew, tag, h)
        os = owner_support(oc)
        ns = owner_support(nc)
        od, ow = r.ungraded(oc)
        nd, nw = r.ungraded(nc)
        rm, rw = s.run_minima(nc, p, h)
        po = s.palettes(oc)
        pn = s.palettes(nc)
        print(
            "EDGE_HALO h", h,
            "cycle_hist_old", dict(sorted(Counter(map(len, oc)).items())),
            "cycle_hist_new", dict(sorted(Counter(map(len, nc)).items())),
            "owner_old", len(os), "owner_new", len(ns),
            "owner_loss", len(os - ns), "owner_birth", len(ns - os),
            "deck_old", len(od), "deck_new", len(nd),
            "deck_loss", len(od - nd), "deck_birth", len(nd - od),
            "run_min", rm,
            "palette_old", tuple(max(c.values()) for c in po),
            "palette_new", tuple(max(c.values()) for c in pn),
        )
        for key in sorted(od - nd):
            print(
                " DECK_LOSS", s.full.word(key[0]),
                format(key[1], f"0{p}b")[::-1],
                format(key[2], f"0{2*h}b")[::-1],
            )
        for key in sorted(os - ns):
            print(
                " OWNER_LOSS", s.full.word(key[0]),
                format(key[1], f"0{p}b")[::-1],
                format(key[2], f"0{2*h}b")[::-1],
            )
        for key in sorted(ns - os):
            print(
                " OWNER_BIRTH", s.full.word(key[0]),
                format(key[1], f"0{p}b")[::-1],
                format(key[2], f"0{2*h}b")[::-1],
            )

        of = expand_full_halo(old, sold, tag, h, halo_tag)
        nf = expand_full_halo(new, snew, tag, h, halo_tag)
        ofs = owner_support(of)
        nfs = owner_support(nf)
        ofd, ofw = r.ungraded(of)
        nfd, nfw = r.ungraded(nf)
        frm, _ = s.run_minima(nf, p + len(union_cut_edges), h)
        fpo = s.palettes(of)
        fpn = s.palettes(nf)
        print(
            "FULL_EDGE_HALO h", h,
            "owner_old", len(ofs), "owner_new", len(nfs),
            "owner_loss", len(ofs - nfs), "owner_birth", len(nfs - ofs),
            "deck_old", len(ofd), "deck_new", len(nfd),
            "deck_loss", len(ofd - nfd), "deck_birth", len(nfd - ofd),
            "run_min", frm,
            "palette_old", tuple(max(c.values()) for c in fpo),
            "palette_new", tuple(max(c.values()) for c in fpn),
        )


if __name__ == "__main__":
    main()
