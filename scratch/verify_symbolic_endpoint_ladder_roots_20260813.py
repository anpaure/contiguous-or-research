#!/usr/bin/env python3
"""Root-local verifier for the parity-dependent endpoint-rotation ladder.

This never enumerates the Catalan MSW factor.  It evaluates only the explicit
root families claimed to host the seam paths and lifted repair circuit.  Large
audits belong on h100.
"""

from __future__ import annotations

import argparse
import collections
import json

import audit_msw_inverse_trade_portal_shadow_20260813 as base
import audit_pbbs_portal_compound_coexistence_20260813 as co


def is_dyck(word):
    height = 0
    for bit in word:
        height += 1 if bit == "1" else -1
        if height < 0:
            return False
    return height == 0


def exchanged(v, delete, insert):
    assert delete in v and insert not in v
    return (v - {delete}) | {insert}


def owners_from_row(row, m):
    return [co.cyc_window(row, i, m + 1) for i in range(2 * m + 1)]


def edges_from_row(row, m):
    owners = owners_from_row(row, m)
    return {
        owners[i] & owners[(i + 1) % len(owners)]:
        frozenset((owners[i], owners[(i + 1) % len(owners)]))
        for i in range(len(owners))
    }


def first_aligned_rows(root, m, gap):
    assert len(root) == 2 * m and root[gap:gap + 4] == "1100"
    eligible = [j for j in range(0, 2*m-3, 4)
                if root[j:j+4] in ("1100", "1010")]
    assert eligible and eligible[0] == gap, (root, gap, eligible[:5])
    mate = root[:gap] + "1010" + root[gap + 4:]
    assert is_dyck(root) and is_dyck(mate)
    return base.recover_inverse_trade(base.msw_row(root), base.msw_row(mate), m)


def find_old_edge(root, m, gap, moving, nxt):
    facet = moving & nxt
    assert len(root) == 2*m and is_dyck(root)
    if gap is None:
        eligible = [j for j in range(0, 2*m-3, 4)
                    if root[j:j+4] in ("1100", "1010")]
        assert not eligible, (root, eligible[:5])
        rows = (base.msw_row(root),)
    else:
        rows = first_aligned_rows(root, m, gap)
    hits = []
    for row in rows:
        edge = edges_from_row(row, m).get(facet)
        if edge is not None and moving in edge:
            hits.append((edge, row))
    assert len(hits) == 1, (m, root, facet, len(hits))
    return facet, hits[0][0], hits[0][1]


def path_vertices(m):
    c = co.c_owner(m, 4)
    u = co.height_owner(m, 5)
    f0 = c & u

    p = [c]
    for delete, insert in ((2*m-4, 3), (5, 2), (2*m, 2*m-4),
                           (3, 2*m-3), (2, 2*m)):
        p.append(exchanged(p[-1], delete, insert))

    parity = m & 1
    b = 11 + 2 * parity
    t = (m - 4) // 2
    q = [u, exchanged(u, 2*m-2, b)]
    q.append(exchanged(q[-1], 10, b + 4))
    for j in range(3, t):
        q.append(exchanged(q[-1], b + 4*(j-3), b + 4*(j-1)))
    q.append(exchanged(q[-1], b + 4*(t-3), 2*m-2))

    tail = {15: 2*m-3, 16: 2*m-2, 17: 2*m-1, 18: 2*m}
    fixed = set(range(16, 2*m-2, 2))
    def lift(xs):
        return frozenset(tail.get(x, x) for x in xs) | fixed
    r = [lift(x) for x in (
        {2,6,8,9,10,12,14,15,16,17},
        {2,6,7,8,9,10,12,14,15,16},
        {0,2,6,7,8,9,12,14,15,16},
        {0,1,2,6,7,9,12,14,15,16},
        {0,1,2,6,9,10,12,14,15,16},
        {0,2,6,9,10,12,14,15,16,17},
        {2,6,8,9,10,12,14,15,16,17},
    )]
    return f0, frozenset((c, u)), p, q, r


def p_roots(m):
    return [
        ("101110011100" + "10"*(m-7) + "00", 8),
        ("101111011100" + "10"*(m-8) + "0000", 8),
        ("101100111100" + "10"*(m-8) + "0010", 8),
        ("111001001100" + "10"*(m-6), 8),
        ("111111000001" + "01"*(m-8) + "0010", 4),
    ]


def q_roots(m):
    parity = m & 1
    t = (m - 4) // 2
    roots = [("101111000110" + "10"*(m-7) + "00", 4)]
    if parity == 0:
        roots.append(("10111100010110" + "10"*(m-8) + "00", 4))
    else:
        roots.append(("1011110001100110" + "10"*(m-9) + "00", 4))
    for r in range(2, t):
        root = ("101111000111" + "01"*(2*r-4+parity)
                + "000110" + "10"*(m-2*r-6-parity) + "00")
        roots.append((root, 4))
    assert len(roots) == t
    return roots


def repair_roots(m):
    return [
        ("110111010001" + "01"*(m-8) + "0010", None),
        ("110111000011" + "01"*(m-8) + "0010", 4),
        ("111111000001" + "01"*(m-8) + "0010", 4),
        ("111001110001" + "01"*(m-8) + "0010", None),
        ("111001011001" + "01"*(m-8) + "0010", None),
        ("110111011001" + "01"*(m-8) + "0000", None),
    ]


def seam_root(m):
    return ("101111000111" + "01"*(m-8) + "0000", 4)


def upper_backup_roots(m):
    """Explicit untouched-row witnesses for every potentially negative term.

    Keys identify the source circuit/step (``s`` is the seam).  Each value is
    a root and either its first-aligned gap or ``None`` for an unchanged row.
    """
    p = {
        (0, 0): ("101110011011" + "01"*(m-8) + "0000", None),
        (0, 1): ("101111111100" + "10"*(m-9) + "000000", 8),
        (0, 2): ("111100111100" + "10"*(m-8) + "0000", 8),
    }
    q = {
        (1, 0): ("1011110101101100" + "10"*(m-10) + "0000", 12),
    }
    if m & 1:
        q[(1, 1)] = ("1011110001010110" + "10"*(m-9) + "00", 4)
    else:
        q[(1, 1)] = ("1011110100011100" + "10"*(m-10) + "1000", 12)
    parity = m & 1
    t = (m - 4) // 2
    for r in range(2, t):
        a = 2*r - 4 + parity
        c = m - 2*r - 6 - parity
        if a == 0:
            root = "101111000110010110" + "10"*c + "00"
        else:
            root = ("101111000111" + "01"*(a-1)
                    + "00010110" + "10"*c + "00")
        q[(1, r)] = (root, 4)
    repair = {
        (2, 0): ("111111010001" + "01"*(m-8) + "0000", None),
        (2, 1): ("11011100001111" + "01"*(m-9) + "0000", 4),
        (2, 2): ("111110001001" + "01"*(m-8) + "0010", None),
        (2, 4): ("111100100101" + "01"*(m-8) + "0010", None),
        (2, 5): ("110011011001" + "01"*(m-8) + "0100", 0),
    }
    seam = {
        ("seam", 0): ("101111000111" + "01"*(m-9) + "000100", 4),
    }
    return p | q | repair | seam


def selected_portal_facets(m, d):
    ans = set()
    tasks = [(a, q) for q in range(2, d) for a in range(q + 1, d + 1)
             if a <= m-q]
    if d + 1 <= m-d:
        tasks.append((d + 1, d))
    for a, q in tasks:
        _, cpos, dpos, _, _ = co.explicit_positive_rows(m, a, q)
        for row in (cpos, dpos):
            ans.update(edges_from_row(row, m))
    return ans


def audit(m, d):
    assert m >= 10
    f0, seam_pair, p, q, r = path_vertices(m)
    families = [(p, p_roots(m)), (q, q_roots(m)),
                (r, repair_roots(m))]
    changed = {f0: seam_pair}
    old_edges = {}
    root_records = []
    for ci, (vertices, roots) in enumerate(families):
        assert len(vertices) - 1 == len(roots)
        for i, ((x, y), (root, gap)) in enumerate(zip(zip(vertices, vertices[1:]), roots)):
            facet, edge, row = find_old_edge(root, m, gap, x, y)
            assert facet not in changed and facet not in old_edges
            stationary = next(iter(edge - {x}))
            old_edges[facet] = edge
            changed[facet] = frozenset((stationary, y))
            root_records.append({"circuit": ci, "step": i,
                                 "root": root, "gap": gap,
                                 "facet": sorted(facet),
                                 "moving": sorted(x),
                                 "stationary": sorted(stationary),
                                 "to": sorted(y),
                                 "old_upper": sorted(frozenset().union(*edge)),
                                 "new_upper": sorted(stationary | y),
                                 "row": list(row)})

    # Seam old endpoints are the terminal moving owners of the two paths.
    sroot, sgap = seam_root(m)
    sfacet, sedge, srow = find_old_edge(sroot, m, sgap, p[-1], q[-1])
    assert sfacet == f0 and sedge == frozenset((p[-1], q[-1]))
    old_edges[f0] = sedge
    root_records.append({"circuit": "seam", "step": 0,
                         "root": sroot, "gap": sgap,
                         "facet": sorted(f0),
                         "moving": [sorted(p[-1]), sorted(q[-1])],
                         "stationary": None,
                         "to": [sorted(x) for x in seam_pair],
                         "old_upper": sorted(p[-1] | q[-1]),
                         "new_upper": sorted(frozenset().union(*seam_pair)),
                         "row": list(srow)})
    old_deg = collections.Counter(v for edge in old_edges.values() for v in edge)
    new_deg = collections.Counter(v for edge in changed.values() for v in edge)
    portals = selected_portal_facets(m, d)
    old_u = collections.Counter(frozenset().union(*e) for e in old_edges.values())
    new_u = collections.Counter(frozenset().union(*e) for e in changed.values())
    net_removed = old_u - new_u
    net_added = new_u - old_u
    host_rows = {base.canonical_cycle(x["row"]) for x in root_records}
    by_key = {(x["circuit"], x["step"]): frozenset(x["old_upper"])
              for x in root_records}
    new_by_key = {(x["circuit"], x["step"]): frozenset(x["new_upper"])
                  for x in root_records}
    assert by_key[(0, 3)] == new_by_key[(0, 2)]
    assert by_key[(0, 4)] == new_by_key[(2, 0)]
    assert by_key[(2, 3)] == new_by_key[(0, 3)]
    backup_records = []
    backed_targets = set()
    for key, (root, gap) in upper_backup_roots(m).items():
        target = by_key[key]
        if gap is None:
            eligible = [j for j in range(0, 2*m-3, 4)
                        if root[j:j+4] in ("1100", "1010")]
            assert not eligible, (m, key, root, eligible[:5])
            rows = (base.msw_row(root),)
        else:
            rows = first_aligned_rows(root, m, gap)
        witnesses = []
        for row in rows:
            for i in range(2*m+1):
                if co.cyc_window(row, i, m+2) == target:
                    witnesses.append((row, i))
        assert witnesses, (m, key, root)
        # At least one full row carrying the backup is untouched by the trade.
        row, index = next((row, index) for row, index in witnesses
                          if base.canonical_cycle(row) not in host_rows)
        backed_targets.add(target)
        backup_records.append({"source": list(key), "root": root, "gap": gap,
                               "target": sorted(target), "row": list(row),
                               "index": index})
    assert set(net_removed) <= backed_targets
    return {
        "m": m, "d": d, "p_steps": len(p)-1, "q_steps": len(q)-1,
        "repair_steps": len(r)-1, "changed_facets": len(changed),
        "owner_exact": old_deg == new_deg,
        "portal_facet_hits": len(portals & set(changed)),
        "net_removed": [{"target": sorted(x), "multiplicity": c}
                        for x, c in net_removed.items()],
        "net_added": [{"target": sorted(x), "multiplicity": c}
                      for x, c in net_added.items()],
        "upper_support_backups": backup_records,
        "upper_support_monotone": set(net_removed) <= backed_targets,
        "roots": root_records,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pairs", nargs="+", help="m:d")
    ap.add_argument("--json")
    args = ap.parse_args()
    result = [audit(*map(int, x.split(":"))) for x in args.pairs]
    payload = json.dumps(result, indent=2, sort_keys=True)
    print(payload)
    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            f.write(payload + "\n")


if __name__ == "__main__":
    main()
