#!/usr/bin/env python3
"""Exact mod-2/3/5 audit of strong reflection masters (H100 only)."""

from __future__ import annotations

import argparse
import json
import sys

import numpy as np

sys.path.insert(0, "scratch")
from audit_q4_k17_z17_pool_modular_lattice_20260814 import ModularBasis
from build_q4_k17_z17_reflection_stochastic_instance_20260814 import make_instance
from search_q4_k17_z17_quotient_exact_cover_20260814 import owner_orbits
from search_q4_k17_z17_reflection_invariant_owner_cover_20260814 import (
    enumerate_strong_self_columns,
    paired_columns,
    reflection_action,
)


def rank_system(columns, dimension, prime, maximum_rank):
    basis = ModularBasis(dimension, prime)
    processed = 0
    for column in columns:
        vector = np.zeros(dimension, dtype=np.int16)
        vector[list(column)] = 1
        basis.insert(vector)
        processed += 1
        if basis.rank == maximum_rank: break
    target = np.ones(dimension, dtype=np.int16)
    return {
        "rank": basis.rank,
        "consistent": basis.contains(target),
        "processed_until_bound_or_exhausted": processed,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--map", required=True)
    parser.add_argument("--sample", type=int, default=0)
    parser.add_argument("--seed", type=int, default=20260814)
    parser.add_argument("--residual-dlx")
    args = parser.parse_args()
    data = json.load(open(args.map, encoding="utf-8"))
    representatives, orbit_index = owner_orbits()
    reflection = reflection_action(representatives, orbit_index)
    bracelet_reps = sorted(v for v in range(1430) if v <= reflection[v])
    bracelet_index = {v: i for i, v in enumerate(bracelet_reps)}

    self_candidates, _, _ = enumerate_strong_self_columns(orbit_index, reflection)
    full_columns = [
        tuple(sorted({bracelet_index[min(v, reflection[v])] for v in candidate["edge"]}))
        for candidate in self_candidates
    ]
    pair_indices, pool_self = paired_columns(data["candidates"], reflection)
    assert not pool_self
    for left, right in pair_indices:
        union = set(data["candidates"][left]["edge"]) | set(data["candidates"][right]["edge"])
        full_columns.append(tuple(sorted({
            bracelet_index[min(v, reflection[v])] for v in union
        })))
    assert {len(column) for column in full_columns[:len(self_candidates)]} == {6}
    assert {len(column) for column in full_columns[len(self_candidates):]} == {10}

    _, self_options, pairs = make_instance(args.map, args.sample, args.seed)
    fixed_columns = []
    for group, _, rows in self_options:
        fixed_columns.append(tuple([group] + [35 + row for row in rows]))
    for _, rows in pairs:
        fixed_columns.append(tuple(35 + row for row in rows))

    report = {
        "status": "PASS",
        "full_master": {"rows": 750, "columns": len(full_columns), "fields": {}},
        "fixed_matching_face": {"rows": 715, "columns": len(fixed_columns), "fields": {}},
    }
    for prime in (2,3,5):
        full_max = 749 if prime == 2 else 750
        fixed_max = 714 if prime == 5 else 715
        report["full_master"]["fields"][str(prime)] = rank_system(
            full_columns, 750, prime, full_max
        )
        report["fixed_matching_face"]["fields"][str(prime)] = rank_system(
            fixed_columns, 715, prime, fixed_max
        )
    if args.residual_dlx:
        with open(args.residual_dlx, encoding="ascii") as stream:
            row_count, used_count, column_count = map(int, stream.readline().split())
            used = set(map(int, stream.readline().split()))
            assert row_count == 680 and len(used) == used_count
            raw_columns = []
            for _ in range(column_count):
                values = list(map(int, stream.readline().split()))
                assert len(values) == 11
                raw_columns.append(values[1:])
        residual = sorted(set(range(680)) - used)
        residual_index = {row: i for i, row in enumerate(residual)}
        residual_columns = [
            tuple(residual_index[row] for row in column)
            for column in raw_columns
        ]
        report["frozen_residual"] = {
            "rows": len(residual), "columns": len(residual_columns), "fields": {},
        }
        assert len(residual) == 540
        for prime in (2,3,5):
            maximum_rank = 539 if prime in (2,5) else 540
            report["frozen_residual"]["fields"][str(prime)] = rank_system(
                residual_columns, 540, prime, maximum_rank
            )
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__": main()
