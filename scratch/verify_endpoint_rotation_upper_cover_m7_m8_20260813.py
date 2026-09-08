#!/usr/bin/env python3
"""Exact finite verifier for endpoint-rotation seam trades at m=7,8.

Substantive replay belongs on h100.  It reconstructs the complete
first-aligned packet factor, checks each old colored edge, portal-row
avoidance, owner/lower exactness, desired seam, and final upper coverage.
"""

from __future__ import annotations

import collections
import json

import cpsat_relative_incidence_trade_compound_seam_20260813 as cp
import audit_pbbs_portal_compound_coexistence_20260813 as co
import search_relative_inverse_trade_for_compound_seam_20260813 as rel


TABLES = {
    7: [
        ([0,3,6,8,9,11,14], [4,5], [4,12]),
        ([0,5,6,7,8,9,14], [3,12], [3,11]),
        ([0,5,6,8,9,11,14], [7,10], [3,10]),
        ([0,6,7,8,9,12,14], [10,11], [5,10]),
        ([0,6,8,9,11,12,14], [3,13], [7,13]),
    ],
    8: [
        ([0,5,6,7,8,9,12,16], [3,14], [3,4]),
        ([0,4,6,7,8,9,12,16], [5,14], [3,14]),
        ([0,3,6,7,8,9,12,16], [4,5], [5,11]),
        ([0,6,7,8,9,11,12,16], [3,10], [10,14]),
        ([0,6,7,8,9,10,12,16], [3,14], [3,13]),
        ([0,6,7,8,9,12,13,16], [10,11], [11,14]),
        ([0,6,7,8,9,12,14,16], [11,13], [5,10]),
    ],
}


def pair(facet, extras):
    return frozenset(facet | {x} for x in extras)


def audit(m):
    rows, old, loads, _ = cp.old_factor_data(m)
    protected = set()
    for row in rel.selected_portal_rows(m, 4):
        owners = [co.cyc_window(row, t, m + 1) for t in range(2 * m + 1)]
        protected.update(
            owners[t] & owners[(t + 1) % (2 * m + 1)]
            for t in range(2 * m + 1)
        )
    neg = {}
    pos = {}
    for f0, old_extra, new_extra in TABLES[m]:
        f = frozenset(f0)
        assert len(f) == m and f not in protected
        neg[f] = pair(f, old_extra)
        pos[f] = pair(f, new_extra)
        assert old[f] == neg[f]
    old_degree = collections.Counter(v for e in neg.values() for v in e)
    new_degree = collections.Counter(v for e in pos.values() for v in e)
    assert old_degree == new_degree
    F = co.c_owner(m, 4) & co.height_owner(m, 5)
    assert pos[F] == frozenset((co.c_owner(m, 4), co.height_owner(m, 5)))
    old_u = collections.Counter(frozenset().union(*e) for e in neg.values())
    new_u = collections.Counter(frozenset().union(*e) for e in pos.values())
    removed = old_u - new_u
    added = new_u - old_u
    assert all(loads[T] - count >= 1 for T, count in removed.items())
    return {
        "m": m,
        "changed_facets": len(neg),
        "protected_facets": len(protected),
        "upper_removed": [
            {"target": sorted(T), "count": c, "old_load": loads[T]}
            for T, c in removed.items()
        ],
        "upper_added": [
            {"target": sorted(T), "count": c, "old_load": loads[T]}
            for T, c in added.items()
        ],
        "minimum_final_removed_load": min(
            (loads[T] - c for T, c in removed.items()), default=None
        ),
    }


if __name__ == "__main__":
    print(json.dumps([audit(7), audit(8)], indent=2, sort_keys=True))
