#!/usr/bin/env python3
"""Replay one explicit defect-cover removal and solve its exact patch."""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, "scratch")
from search_q4_k17_z17_reflection_fixed_face_kissat_20260814 import read_instance
from search_q4_k17_z17_reflection_vertex_cover_patch_benders_20260814 import (
    selected_vertices,
)
from search_q4_k17_z17_reflection_sampled_root_direct_patch_20260814 import (
    direct_patch,
    row_mask,
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--instance", required=True)
    parser.add_argument("--incumbent", required=True)
    parser.add_argument("--removal-mask", required=True)
    parser.add_argument("--solution", required=True)
    parser.add_argument("--report", required=True)
    parser.add_argument("--seconds", type=float, default=10.0)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument("--seed", type=int, default=20260814)
    args = parser.parse_args()
    started = time.time()

    _, _, self_options, pair_options = read_instance(args.instance)
    incumbent = json.loads(Path(args.incumbent).read_text())
    vertices = selected_vertices(self_options, pair_options, incumbent)
    removal = int(args.removal_mask, 0)
    if removal >> len(vertices):
        raise ValueError("removal mask has bits outside selected vertices")
    self_masks = [row_mask(rows) for _, rows in self_options]
    pair_masks = [row_mask(rows) for rows in pair_options]
    summary, solution, free_rows = direct_patch(
        self_options, pair_options, self_masks, pair_masks, vertices, removal,
        args.seconds, args.workers, args.seed,
    )
    if solution is not None:
        Path(args.solution).write_text(json.dumps(solution, indent=2,
                                                  sort_keys=True) + "\n")
    report = {
        "status": "PASS" if solution is not None else summary["status"],
        "scope": "one exact explicit removal-mask patch",
        "instance": args.instance,
        "incumbent": args.incumbent,
        "removal_mask_hex": hex(removal),
        "removal_vertices": [position for position in range(len(vertices))
                             if removal >> position & 1],
        "free_rows_list": free_rows,
        "patch_summary": summary,
        "solution": args.solution if solution is not None else None,
        "elapsed_seconds": time.time() - started,
    }
    Path(args.report).write_text(json.dumps(report, indent=2,
                                           sort_keys=True) + "\n")
    print(json.dumps({key: value for key, value in report.items()
                      if key != "free_rows_list"}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
