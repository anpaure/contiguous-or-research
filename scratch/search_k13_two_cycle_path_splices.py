#!/usr/bin/env python3
"""Join the two perfect k=13 carrier cycles by one Johnson seam.

The input is a disconnected sigma selection.  Unlike the endpoint-circuit
search, the final object sought here is a *linear* middle path, so one cross
edge is sufficient: delete one edge from each physical cycle and concatenate
the resulting paths through a Johnson edge.  Cyclic shadow loads are updated
locally at the two cuts and the seam, making exhaustive enumeration cheap.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scratch"))

from sigma_sat_solver import SigmaInstance, rotate
from k13_quotient_endpoint_cycle_search import load_selected
from audit_k13_disconnected_selection import traverse_component
from sigma_multirow_linear_compiler import derive, linear_erosion


FULL = (1 << 13) - 1


def physical_cycles(instance: SigmaInstance, selected_by_lower: dict) -> list[list[int]]:
    selected = [selected_by_lower[x] for x in sorted(selected_by_lower)]
    answer: list[list[int]] = []
    for component in instance.components(selected):
        local = [choice for choice in selected if choice.endpoint[0] in component]
        vertices, phases, _, voltage = traverse_component(instance, local, component)
        if voltage:
            cycle: list[int] = []
            offset = 0
            for _ in range(instance.k):
                cycle.extend(
                    rotate(instance.middle[v], phase + offset, instance.k)
                    for v, phase in zip(vertices, phases)
                )
                offset = (offset + voltage) % instance.k
            answer.append(cycle)
        else:
            for offset in range(instance.k):
                answer.append(
                    [
                        rotate(instance.middle[v], phase + offset, instance.k)
                        for v, phase in zip(vertices, phases)
                    ]
                )
    return answer


def oriented_path(cycle: list[int], end: int, direction: int) -> list[int]:
    """Path ending at cycle[end], after deleting its edge in ``direction``."""
    n = len(cycle)
    assert direction in (-1, 1)
    start = (end + direction) % n
    return [cycle[(start + direction * t) % n] for t in range(n)]


def shadow_value(block: list[int]) -> tuple[int, int]:
    lo, hi = FULL, 0
    for value in block:
        lo &= value
        hi |= value
    return lo, hi


def cyclic_loads(cycles: list[list[int]]) -> dict[int, dict[str, Counter]]:
    result: dict[int, dict[str, Counter]] = {}
    for q in range(1, 7):
        lower, upper = Counter(), Counter()
        for cycle in cycles:
            n = len(cycle)
            for start in range(n):
                block = [cycle[(start + j) % n] for j in range(q + 1)]
                lo, hi = shadow_value(block)
                if lo.bit_count() == 7 - q:
                    lower[lo] += 1
                if hi.bit_count() == 7 + q:
                    upper[hi] += 1
        result[q] = {"lower": lower, "upper": upper}
    return result


def boundary_windows(path: list[int], q: int) -> list[list[int]]:
    """The q cyclic windows removed when ``path`` is treated linearly."""
    n = len(path)
    return [
        [path[(n - t + j) % n] for j in range(q + 1)]
        for t in range(1, q + 1)
    ]


def local_counter(blocks: list[list[int]], q: int, side: str) -> Counter:
    answer = Counter()
    target_rank = 7 - q if side == "lower" else 7 + q
    for block in blocks:
        lo, hi = shadow_value(block)
        value = lo if side == "lower" else hi
        if value.bit_count() == target_rank:
            answer[value] += 1
    return answer


def structural_failures(path: list[int], depth: int = 3) -> int:
    allowed = linear_erosion(path, 13, depth)
    maximal = derive(allowed[:], depth)
    return sum(a != b for a, b in zip(path, maximal))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--keep", type=int, default=200)
    parser.add_argument(
        "--max-shadow-holes-for-residence",
        type=int,
        default=2,
        help="run the linear residence audit on splices with at most this many holes",
    )
    parser.add_argument(
        "--write-path-prefix",
        type=Path,
        help="write middle_path JSON files for all exact-shadow residence-safe splices",
    )
    args = parser.parse_args()

    instance = SigmaInstance(13, True, cap2=False, q2=False, cover_upper=False)
    _, selected = load_selected(instance, args.source)
    cycles = sorted(physical_cycles(instance, selected), key=len, reverse=True)
    if len(cycles) != 2:
        raise SystemExit(f"expected exactly two physical cycles, got {list(map(len, cycles))}")
    base = cyclic_loads(cycles)
    for q in range(1, 7):
        for side in ("lower", "upper"):
            if not base[q][side]:
                raise AssertionError("empty baseline load")

    # Cache both orientations for every cut.  The second cycle is indexed by
    # its starting mask so only genuine Johnson seams are considered.
    descriptors: list[list[dict]] = [[], []]
    starts2: dict[int, list[dict]] = defaultdict(list)
    for ci, cycle in enumerate(cycles):
        for end in range(len(cycle)):
            for direction in (-1, 1):
                path = oriented_path(cycle, end, direction)
                removed = {
                    q: {
                        side: local_counter(boundary_windows(path, q), q, side)
                        for side in ("lower", "upper")
                    }
                    for q in range(1, 7)
                }
                row = {
                    "cycle": ci,
                    "end_index": end,
                    "direction": direction,
                    "start": path[0],
                    "end": path[-1],
                    "head": path[:7],
                    "tail": path[-7:],
                    "removed": removed,
                }
                descriptors[ci].append(row)
                if ci == 1:
                    starts2[path[0]].append(row)

    candidates = 0
    exact_shadow = 0
    residence_safe = 0
    rows: list[dict] = []
    written = 0
    for left in descriptors[0]:
        x = left["end"]
        # Every Johnson neighbour differs by deleting one of seven elements
        # and inserting one of six absent elements.
        neighbours = []
        for deleted in range(13):
            if not (x >> deleted) & 1:
                continue
            for inserted in range(13):
                if (x >> inserted) & 1:
                    continue
                neighbours.append(x ^ (1 << deleted) ^ (1 << inserted))
        for start_mask in neighbours:
            for right in starts2.get(start_mask, []):
                candidates += 1
                added: dict[int, dict[str, Counter]] = {}
                holes: dict[str, dict[str, int]] = {}
                all_holes = 0
                for q in range(1, 7):
                    seam_blocks = [
                        left["tail"][-t:] + right["head"][: q + 1 - t]
                        for t in range(1, q + 1)
                    ]
                    added[q] = {
                        side: local_counter(seam_blocks, q, side)
                        for side in ("lower", "upper")
                    }
                    holes[str(q)] = {}
                    for side in ("lower", "upper"):
                        delta = Counter(added[q][side])
                        delta.subtract(left["removed"][q][side])
                        delta.subtract(right["removed"][q][side])
                        count = sum(
                            1
                            for mask, change in delta.items()
                            if base[q][side][mask] + change <= 0
                        )
                        holes[str(q)][side] = count
                        all_holes += count

                # A linear depth-three compiler has two boundary cells beyond
                # the W-1 internal adjacent intersections, so one or two lower
                # q1 holes can still be recoverable by Hall.  Audit residence
                # on this small near-exact collar, not only at zero holes.
                failures = None
                path = None
                if all_holes <= args.max_shadow_holes_for_residence:
                    if all_holes == 0:
                        exact_shadow += 1
                    p0 = oriented_path(cycles[0], left["end_index"], left["direction"])
                    p1 = oriented_path(cycles[1], right["end_index"], right["direction"])
                    path = p0 + p1
                    failures = structural_failures(path)
                    if failures == 0:
                        residence_safe += 1

                row = {
                    "left_end_index": left["end_index"],
                    "left_direction": left["direction"],
                    "right_end_index": right["end_index"],
                    "right_direction": right["direction"],
                    "seam_left": x,
                    "seam_right": start_mask,
                    "all_shadow_holes": all_holes,
                    "holes": holes,
                    "structural_residence_failures": failures,
                }
                rows.append(row)
                rows.sort(
                    key=lambda item: (
                        item["all_shadow_holes"],
                        10**9
                        if item["structural_residence_failures"] is None
                        else item["structural_residence_failures"],
                    )
                )
                del rows[args.keep :]

                if failures == 0 and args.write_path_prefix:
                    assert path is not None
                    out = Path(f"{args.write_path_prefix}.{written}.json")
                    out.write_text(
                        json.dumps(
                            {
                                "status": "K13_TWO_CYCLE_ONE_SEAM_PATH",
                                "source": str(args.source),
                                "splice": row,
                                "middle_path": path,
                            },
                            indent=2,
                            sort_keys=True,
                        )
                        + "\n"
                    )
                    row["path_file"] = str(out)
                    written += 1

    report = {
        "source": str(args.source),
        "physical_cycle_lengths": list(map(len, cycles)),
        "candidate_splices": candidates,
        "exact_shadow_splices": exact_shadow,
        "exact_shadow_residence_safe_splices": residence_safe,
        "written_paths": written,
        "best": rows,
    }
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({key: value for key, value in report.items() if key != "best"}, indent=2, sort_keys=True))
    if rows:
        print(json.dumps({"best": rows[0]}, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
