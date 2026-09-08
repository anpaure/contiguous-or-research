#!/usr/bin/env python3
"""Classify the first-aligned MSW factor on pair-transversal facets.

Substantive runs belong on h100.  For every cyclic sentinel/pair alignment,
the script records whether the two old endpoints at each transversal facet
use the sentinel port or cube-edge ports, and the induced degrees of those
cube-edge owners.
"""

from __future__ import annotations

import collections
import itertools
import json
import sys

import cpsat_relative_incidence_trade_compound_seam_20260813 as cp


def structure(m, sentinel):
    n = 2 * m + 1
    rest = [(sentinel + j) % n for j in range(1, n)]
    return [(rest[2 * i], rest[2 * i + 1]) for i in range(m)]


def audit_alignment(m, sentinel, old):
    pairs = structure(m, sentinel)
    pair_of = {}
    for i, (a, b) in enumerate(pairs):
        pair_of[a] = (i, b)
        pair_of[b] = (i, a)
    port_degree = collections.Counter()
    sentinel_endpoints = 0
    bad_endpoints = 0
    repeated_ports_at_vertex = 0
    for bits in itertools.product((0, 1), repeat=m):
        L = frozenset(pairs[i][bits[i]] for i in range(m))
        ports = []
        for T in old[L]:
            extra = next(iter(T - L))
            if extra == sentinel:
                sentinel_endpoints += 1
                ports.append(("z",))
            else:
                i, mate = pair_of[extra]
                if mate not in L:
                    bad_endpoints += 1
                    ports.append(("bad", extra))
                else:
                    # The owner is the lift of the cube edge in direction i.
                    y = tuple(bits[j] for j in range(m) if j != i)
                    key = (i, y)
                    port_degree[key] += 1
                    ports.append(key)
        if ports[0] == ports[1]:
            repeated_ports_at_vertex += 1
    hist = collections.Counter(port_degree.values())
    all_ports = m * (1 << (m - 1))
    hist[0] = all_ports - len(port_degree)
    return {
        "sentinel": sentinel,
        "sentinel_endpoints": sentinel_endpoints,
        "bad_endpoints": bad_endpoints,
        "repeated_ports_at_vertex": repeated_ports_at_vertex,
        "cube_port_degree_histogram": dict(sorted(hist.items())),
        "cube_ports_degree_two_or_zero": all(d == 2 for d in port_degree.values()),
        "selected_cube_ports": len(port_degree),
    }


def main():
    m = int(sys.argv[1])
    _, old, _, _ = cp.old_factor_data(m)
    ans = [audit_alignment(m, s, old) for s in range(2 * m + 1)]
    print(json.dumps({"m": m, "alignments": ans}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
