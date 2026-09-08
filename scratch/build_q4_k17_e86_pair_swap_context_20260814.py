#!/usr/bin/env python3
"""Build a compact one-pair-swap scoring context (H100 only)."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from search_q4_k17_z17_reflection_fixed_face_kissat_20260814 import (
    read_instance,
)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--instance", required=True)
    parser.add_argument("--incumbent", required=True)
    parser.add_argument("--context", required=True)
    args = parser.parse_args()

    _, _, self_options, pair_options = read_instance(args.instance)
    with open(args.incumbent, encoding="ascii") as stream:
        state = json.load(stream)
    assert state["energy"] > 0 and state["energy"] % 2 == 0
    assert len(state["self_indices"]) == 35
    assert len(state["pair_indices"]) == 54
    loads = [0] * 680
    for index in state["self_indices"]:
        for row in self_options[index][1]:
            loads[row] += 1
    for index in state["pair_indices"]:
        for row in pair_options[index]:
            loads[row] += 1
    assert set(loads) <= {0, 1, 2}
    assert sum((load - 1) ** 2 for load in loads) == state["energy"]
    assert loads.count(0) == loads.count(2) == state["energy"] // 2

    lines = [f"680 54 {state['energy']}", " ".join(map(str, loads))]
    for index in state["pair_indices"]:
        lines.append(" ".join(map(str, (index,) + pair_options[index])))
    Path(args.context).write_text("\n".join(lines) + "\n", encoding="ascii")
    print(json.dumps({
        "status": "PASS",
        "context": args.context,
        "energy": state["energy"],
        "selected_pairs": len(state["pair_indices"]),
        "load_histogram": {
            str(load): loads.count(load) for load in sorted(set(loads))
        },
        "selected_pair_indices": state["pair_indices"],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
