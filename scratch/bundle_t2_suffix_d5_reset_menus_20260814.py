#!/usr/bin/env python3
"""Bundle the exact D5 candidate menus used by the topology CEGAR.

Substantive execution belongs on H100.  The bundle keeps the parsed JSON and
the SHA-256 of every original menu while avoiding hundreds of tiny frozen
certificate files.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


P1_EXACT = [6, 7, 11, 13, 22, 23, 27, 28, 29, 33, 35, 37, 38, 39, 40]
P1_CAPPED = [0, 2, 3, 4, 8, 9, 10, 12, 14, 16, 17, 18, 20, 21, 24, 31, 32, 34]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", nargs="?", default=".")
    args = parser.parse_args()
    directory = Path(args.directory)
    groups = {
        "all_prefix_global_minimum": [
            f"d5_minimum_candidates_{index}.out" for index in range(41)
        ],
        "reset_phase_p0": [
            f"d5_thirdphase_all_{index}.out" for index in range(41)
        ],
        "reset_phase_p1_exact": [
            f"d5_fourthphase_{index}.out" for index in P1_EXACT
        ],
        "reset_phase_p1_capped": [
            f"d5_fourthphase_cap512_{index}.out" for index in P1_CAPPED
        ],
    }
    assert sum(map(len, groups.values())) == 115
    files = {}
    for name in [name for group in groups.values() for name in group]:
        path = directory / name
        raw = path.read_bytes()
        assert raw
        files[name] = {
            "sha256": hashlib.sha256(raw).hexdigest(),
            "data": json.loads(raw),
        }
    print(json.dumps({
        "status": "PASS",
        "menu_files": len(files),
        "groups": groups,
        "files": files,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
