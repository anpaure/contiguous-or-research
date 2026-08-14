#!/usr/bin/env python3
"""Dump every literal q1/q2 occurrence in a frozen splice witness.

Run on H100 only.  This is a presentation companion to the independent
verifier; it performs no search.
"""

import argparse
import json
from collections import Counter
from pathlib import Path

import verify_d5_complete_owner_disjoint_three_splice_reset_20260814 as verify


NAMES = ("owner", "lower_q1", "upper_q1", "lower_q2", "upper_q2")


def encode(value):
    return [sorted(owner) for owner in value]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("witness")
    args = parser.parse_args()
    raw = json.loads(Path(args.witness).read_text())
    assert raw["status"] == "SAT"
    witness = raw["witness"]
    old = tuple(verify.fs_cycle(cycle) for cycle in witness["old_cycles"])
    new = tuple(verify.fs_cycle(cycle) for cycle in witness["new_cycles"])
    old_palettes = verify.palettes(old)
    new_palettes = verify.palettes(new)
    assert all(Counter(old_palettes[k]) == Counter(new_palettes[k]) for k in range(5))
    print(json.dumps({
        "status": "PASS",
        "old_component_lengths": sorted(map(len, old)),
        "new_component_lengths": sorted(map(len, new)),
        "old": {name: encode(old_palettes[k]) for k, name in enumerate(NAMES)},
        "new": {name: encode(new_palettes[k]) for k, name in enumerate(NAMES)},
        "old_distinct_counts": {
            name: len(set(old_palettes[k])) for k, name in enumerate(NAMES)
        },
        "new_distinct_counts": {
            name: len(set(new_palettes[k])) for k, name in enumerate(NAMES)
        },
        "occurrence_multisets_equal": {
            name: Counter(old_palettes[k]) == Counter(new_palettes[k])
            for k, name in enumerate(NAMES)
        },
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
