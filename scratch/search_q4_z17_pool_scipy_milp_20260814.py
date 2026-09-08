#!/usr/bin/env python3
"""Run SciPy/HiGHS set-partitioning on a frozen q4 Z17 candidate pool."""

from __future__ import annotations

import argparse
import json

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp
from scipy.sparse import coo_array


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("pool")
    parser.add_argument("--time-limit", type=float, default=600.0)
    parser.add_argument("--seed", type=int, default=20260814)
    args = parser.parse_args()

    data = json.load(open(args.pool))
    candidates = data["candidates"]
    n = data["owner_orbits"]
    rows = []
    cols = []
    for col, candidate in enumerate(candidates):
        edge = candidate["edge"]
        if len(edge) != len(set(edge)):
            raise ValueError("nonsimple candidate")
        rows.extend(edge)
        cols.extend([col] * len(edge))
    matrix = coo_array(
        (np.ones(len(rows)), (np.array(rows), np.array(cols))),
        shape=(n, len(candidates)),
    ).tocsc()

    rng = np.random.default_rng(args.seed)
    # A tiny deterministic perturbation prevents a completely flat branch
    # order while every feasible solution remains acceptable.
    objective = rng.random(len(candidates)) * 1.0e-8
    result = milp(
        c=objective,
        integrality=np.ones(len(candidates), dtype=np.uint8),
        bounds=Bounds(0.0, 1.0),
        constraints=LinearConstraint(matrix, 1.0, 1.0),
        options={
            "time_limit": args.time_limit,
            "mip_rel_gap": 0.0,
            "presolve": True,
        },
    )
    report = {
        "success": bool(result.success),
        "status": int(result.status),
        "message": str(result.message),
        "fun": None if result.fun is None else float(result.fun),
        "mip_node_count": getattr(result, "mip_node_count", None),
        "mip_gap": getattr(result, "mip_gap", None),
        "pool": len(candidates),
        "owner_orbits": n,
    }
    if result.x is not None:
        selected = np.flatnonzero(result.x > 0.5).tolist()
        load = np.asarray(matrix[:, selected].sum(axis=1)).ravel()
        report["selected"] = selected
        report["selected_count"] = len(selected)
        report["load_histogram"] = {
            str(int(value)): int(np.count_nonzero(load == value))
            for value in np.unique(load)
        }
        if result.success:
            assert np.all(load == 1)
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
