#!/usr/bin/env python3
"""Print containment/MM-path templates for the predicted near clones."""

from __future__ import annotations

import argparse

from audit_punctured_near_clone_tail_20260821 import (
    edge,
    path,
    predicted_words,
)


def mm_path_starts(r: int) -> tuple[int, ...]:
    b = 2 * r + 1
    rows = []
    current = r
    while current:
        rows.append(current)
        current = (current + r) % b
    assert len(rows) == 2 * r
    return tuple(rows)


def main(r: int) -> None:
    b = 2 * r + 1
    identity = tuple(range(b))
    base_path = path(identity, r)
    base_index = {vertex: index for index, vertex in enumerate(base_path)}
    base_edge = edge(identity, r)
    psi = mm_path_starts(r)
    mm_rank = {start: rank for rank, start in enumerate(psi)}
    print({"r": r, "psi": psi})
    for word, defect in predicted_words(r).items():
        if defect > 2:
            continue
        actual_path = path(word, r)
        template = tuple(base_index.get(vertex) for vertex in actual_path)
        missing = tuple(index for index, vertex in enumerate(base_path) if vertex not in actual_path)
        new_positions = tuple(index for index, old in enumerate(template) if old is None)
        # Read the shared base-M starts in F's intrinsic disjointness order.
        f_middle_to_base_start = {}
        for f_start in range(1, b):
            old_index = template[2 * (f_start - 1) + 1]
            if old_index is not None:
                assert old_index % 2 == 1
                f_middle_to_base_start[f_start] = (old_index + 1) // 2
        shared_mm_sequence = tuple(
            f_middle_to_base_start[start]
            for start in psi
            if start in f_middle_to_base_start
        )
        seam_steps = tuple(
            (right - left) % b
            for left, right in zip(shared_mm_sequence, shared_mm_sequence[1:])
            if abs(mm_rank[right] - mm_rank[left]) != 1
        )
        print({
            "defect": defect,
            "word": word,
            "missing_path_indices": missing,
            "new_path_positions": new_positions,
            "template": template,
            "shared_mm_sequence": shared_mm_sequence,
            "nonbase_seam_steps": seam_steps,
            "overlap": len(base_edge & edge(word, r)),
        })


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--r", type=int, default=5)
    arguments = parser.parse_args()
    main(arguments.r)
