#!/usr/bin/env python3
"""Audit two-copy owner simplicity under every affine Z_17 relabelling.

Run substantively on H100 only.  The first copy is fixed.  The same affine
map x -> a*x+b is applied to both recoupled states of the second copy.
"""

from __future__ import annotations

import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import audit_q4_k17_recoupled_typed_rail_ledgers_20260814 as base  # noqa:E402


def relabel(value, a, b):
    return frozenset((a * item + b) % 17 for item in value)


def owners(rails):
    return {owner for _, cycle in rails for owner in cycle}


def main():
    source_raw = Path(sys.argv[1]).read_bytes()
    states = dict(base.rail_states())
    banks = {name: owners(rails) for name, rails in states.items()}
    histogram = Counter()
    common_owner_simple = []
    for a in range(1, 17):
        for b in range(17):
            overlaps = {
                name: len(bank & {relabel(owner, a, b) for owner in bank})
                for name, bank in banks.items()
            }
            histogram[(overlaps["state_one"], overlaps["state_two"])] += 1
            if all(value == 0 for value in overlaps.values()):
                common_owner_simple.append({"a": a, "b": b})
    print(json.dumps({
        "status": "PASS" if common_owner_simple else "NO_WITNESS",
        "scope": "same affine Z_17 relabelling on the second copy in both states",
        "source_sha256": hashlib.sha256(source_raw).hexdigest(),
        "affine_maps": 272,
        "overlap_pair_histogram": [
            {"state_one_overlap": key[0], "state_two_overlap": key[1], "maps": value}
            for key, value in sorted(histogram.items())
        ],
        "common_owner_simple_maps": common_owner_simple,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
