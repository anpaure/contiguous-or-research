#!/usr/bin/env python3
"""Shard runner for the m=4 protected-wreath pair audit (H100 only)."""

import argparse
import json
import time

import audit_protected_wreath_extension_20260813 as w


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--shard", type=int, required=True)
    ap.add_argument("--shards", type=int, required=True)
    ap.add_argument("--time-limit", type=float, default=60.0)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()

    inst = w.build_instance(4)
    canonical = inst["ci"][tuple(range(9))]
    c_mask = inst["masks"][canonical]
    compatible = [z for z, mask in enumerate(inst["masks"])
                  if z != canonical and not (mask & c_mask)]
    group = w.dihedral_group(9)
    reps = {}
    for z in compatible:
        key = w.orbit_key_tuple(inst, (canonical, z), group)
        reps.setdefault(key, z)
    jobs = [(i, key, z) for i, (key, z) in enumerate(sorted(reps.items()))
            if i % args.shards == args.shard]
    with open(args.output, "w") as f:
        for num, (global_index, key, z) in enumerate(jobs):
            ok, sol, status, sec = w.exact_cover(
                inst, (canonical, z), args.time_limit, 1)
            rec = {
                "global_index": global_index,
                "orbit_key": list(key),
                "representative": z,
                "cycle": list(inst["cycles"][z]),
                "extendable": ok,
                "status": status,
                "seconds": sec,
                "completion": list(sol) if sol else None,
            }
            f.write(json.dumps(rec, sort_keys=True) + "\n")
            f.flush()
            print(args.shard, num + 1, len(jobs), global_index, status, sec,
                  flush=True)


if __name__ == "__main__":
    main()
