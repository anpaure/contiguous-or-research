#!/usr/bin/env python3
"""Census alternate upper occurrences for the endpoint ladder (H100 only)."""

from __future__ import annotations

import argparse
import collections
import json

import cpsat_relative_incidence_trade_compound_seam_20260813 as cp
import identify_first_aligned_rows_for_endpoint_trade_20260813 as ident
import verify_symbolic_endpoint_ladder_roots_20260813 as sym


def audit(m, d):
    # Formula old/new current from root-local verifier.
    rec = sym.audit(m, d)
    removed = [frozenset(x["target"]) for x in rec["net_removed"]]

    desc = ident.described_factor(m)
    emap = ident.edge_map(desc, m)
    by_upper = collections.defaultdict(list)
    for facet, (edge, row, index, info) in emap.items():
        by_upper[frozenset().union(*edge)].append((facet, edge, row, index, info))
    out = []
    ground = frozenset(range(2*m+1))
    for upper in removed:
        occs = []
        for facet, edge, row, index, info in by_upper[upper]:
            occs.append({
                "facet": sorted(facet),
                "facet_complement_in_upper": sorted(upper - facet),
                "global_complement": sorted(ground - upper),
                "owners": [sorted(x) for x in edge],
                "row": list(row), "index": index, **info,
            })
        sources = [{"circuit": x["circuit"], "step": x["step"],
                    "root": x["root"]}
                   for x in rec["roots"]
                   if frozenset(x["old_upper"]) == upper]
        out.append({"target": sorted(upper), "load": len(occs),
                    "sources": sources,
                    "occurrences": occs})
    return {"m": m, "d": d, "removed": out}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pairs", nargs="+")
    ap.add_argument("--json")
    args = ap.parse_args()
    ans = [audit(*map(int, x.split(":"))) for x in args.pairs]
    payload = json.dumps(ans, indent=2, sort_keys=True)
    print(payload)
    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            f.write(payload + "\n")


if __name__ == "__main__":
    main()
