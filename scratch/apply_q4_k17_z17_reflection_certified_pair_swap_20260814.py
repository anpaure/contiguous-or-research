#!/usr/bin/env python3
"""Apply one certified reflected-pair swap and replay the load histogram."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path


def read_instance(path: Path) -> tuple[int, list[tuple[int, ...]], list[tuple[int, ...]]]:
    with path.open() as handle:
        row_count, _group_count, self_count, pair_count = map(int, next(handle).split())
        self_rows = []
        for _ in range(self_count):
            fields = tuple(map(int, next(handle).split()))
            self_rows.append(fields[1:])
        pair_rows = [tuple(map(int, next(handle).split())) for _ in range(pair_count)]
        if next(handle, None) is not None:
            raise ValueError("trailing instance data")
    return row_count, self_rows, pair_rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--instance", required=True, type=Path)
    parser.add_argument("--state", required=True, type=Path)
    parser.add_argument("--remove-pair", required=True, type=int)
    parser.add_argument("--add-pair", required=True, type=int)
    parser.add_argument("--output-state", required=True, type=Path)
    parser.add_argument("--expected-energy", type=int)
    args = parser.parse_args()

    row_count, self_rows, pair_rows = read_instance(args.instance)
    state = json.loads(args.state.read_text())
    selected_pairs = list(map(int, state["pair_indices"]))
    selected_self = list(map(int, state["self_indices"]))
    if args.remove_pair not in selected_pairs:
        raise ValueError(f"removed pair {args.remove_pair} is not selected")
    if args.add_pair in selected_pairs:
        raise ValueError(f"added pair {args.add_pair} is already selected")

    selected_pairs[selected_pairs.index(args.remove_pair)] = args.add_pair
    loads = [0] * row_count
    for index in selected_self:
        for row in self_rows[index]:
            loads[row] += 1
    for index in selected_pairs:
        for row in pair_rows[index]:
            loads[row] += 1
    histogram = dict(sorted(Counter(loads).items()))
    energy = sum(abs(load - 1) for load in loads)
    if args.expected_energy is not None and energy != args.expected_energy:
        raise ValueError(f"energy {energy} != expected {args.expected_energy}")

    output = {
        "energy": energy,
        "pair_indices": sorted(selected_pairs),
        "self_indices": selected_self,
        "status": "CERTIFIED_PAIR_SWAP",
    }
    args.output_state.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "add_pair": args.add_pair,
        "energy": energy,
        "histogram": histogram,
        "output_state": str(args.output_state),
        "remove_pair": args.remove_pair,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
