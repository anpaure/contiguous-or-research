#!/usr/bin/env python3
"""Compare the workspace RP recursion with adjacent-coordinate moves."""

from collections import Counter

from audit_msw_pr_path_common_ports_20260814 import pr_path


for r in (2, 3, 4, 5, 6):
    path = pr_path(r)
    gaps = Counter()
    rows = []
    for left, right in zip(path, path[1:]):
        changed = [i for i, pair in enumerate(zip(left, right)) if pair[0] != pair[1]]
        assert len(changed) == 2
        gaps[changed[1] - changed[0]] += 1
        rows.append((left, right, changed[1] - changed[0]))
    print("PR_PATH_ADJACENCY", r, len(path), dict(gaps), flush=True)
    if r == 4:
        print("PR_PATH_R4", rows, flush=True)
