#!/usr/bin/env python3
"""Identify canonical MSW roots/row positions for the parity-ladder candidate.

Substantive runs belong on H100.  This script is diagnostic: a theorem still needs
to prove the displayed root/rho identities symbolically.
"""

from __future__ import annotations

import json
import sys

import audit_pbbs_portal_compound_coexistence_20260813 as co
import audit_msw_inverse_trade_portal_shadow_20260813 as base
import test_uniform_endpoint_trade_formula_20260813 as cand


def described_factor(m):
    roots, original = base.build_factor(m)
    paired = set()
    removed = set()
    result = {}
    for w in roots:
        if w in paired:
            continue
        mate = None
        gap = None
        for j in range(0, 2 * m - 3, 4):
            block = w[j:j + 4]
            if block == "1100":
                mate = w[:j] + "1010" + w[j + 4:]
                gap = j
                break
            if block == "1010":
                mate = w[:j] + "1100" + w[j + 4:]
                gap = j
                break
        if mate is None:
            continue
        paired.update((w, mate))
        neg = (original[w], original[mate])
        pos = base.recover_inverse_trade(*neg, m)
        removed.update(neg)
        for idx, row in enumerate(pos):
            result[row] = {"kind": "positive", "root": w,
                           "mate": mate, "gap": gap,
                           "positive_index": idx}
    for w, row in original.items():
        if row not in removed:
            result[row] = {"kind": "original", "root": w}
    return result


def edge_map(desc, m):
    ans = {}
    for row, info in desc.items():
        owners = [co.cyc_window(row, i, m + 1) for i in range(2 * m + 1)]
        for i in range(2 * m + 1):
            edge = frozenset((owners[i], owners[(i + 1) % (2 * m + 1)]))
            facet = frozenset.intersection(*edge)
            ans[facet] = (edge, row, i, info)
    return ans


def audit(m):
    _, _, circuits = cand.candidate(m)
    desc = described_factor(m)
    emap = edge_map(desc, m)
    out = []
    for ci, vertices in enumerate(circuits):
        for si, (a, b) in enumerate(zip(vertices, vertices[1:])):
            facet = a & b
            edge, row, pos, info = emap[facet]
            out.append({"circuit": ci, "step": si,
                        "from": sorted(a), "to": sorted(b),
                        "facet": sorted(facet), "edge": [sorted(x) for x in edge],
                        "row": list(row), "position": pos, **info})
    return out


if __name__ == "__main__":
    m = int(sys.argv[1])
    print(json.dumps({"m": m, "steps": audit(m)}, indent=2, sort_keys=True))
