#!/usr/bin/env python3
"""Lift the verified K=16 optimum to an explicit K=17 upper bound.

For any universal word X=(x_0,...,x_{L-1}) on k-1 coordinates and a new
bit z, the word

    X, z, (x_0|z), ..., (x_{L-2}|z)

is universal on k coordinates.  An unmarked target is served in the first
copy.  For a marked target S+z, take an X-interval for S: if it avoids the
last X-cell, use its marked copy; otherwise extend that suffix by the bare-z
cell.  The bare target z is the central singleton.
"""

from __future__ import annotations

from collections import Counter
from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "scratch/k16_optimal_12873_20260731.word"
OUTPUT = ROOT / "scratch/k17_explicit_upper25746_from_k16_20260731.word"
AUDIT = ROOT / "scratch/k17_explicit_upper25746_from_k16_20260731.audit.json"
SOURCE_SHA256 = "890ac346ce142f5f9ed564d487ff3e2fb99aea93ae2c104ec13765fa5d3814fe"
OLD_K = 16
NEW_BIT = 1 << OLD_K
NEW_K = OLD_K + 1


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def interval_or_spectrum(word: list[int]) -> tuple[set[int], int]:
    """Return all interval ORs using the nested suffix-frontier recurrence."""

    seen: set[int] = set()
    endings: list[int] = []
    maximum_frontier = 0
    for value in word:
        following = [value]
        for old in endings:
            joined = old | value
            if joined != following[-1]:
                following.append(joined)
        endings = following
        maximum_frontier = max(maximum_frontier, len(endings))
        seen.update(endings)
    return seen, maximum_frontier


def main() -> int:
    assert digest(SOURCE) == SOURCE_SHA256
    parent = list(map(int, SOURCE.read_text().split()))
    assert len(parent) == 12873
    assert all(0 < value < NEW_BIT for value in parent)

    child = [*parent, NEW_BIT, *(value | NEW_BIT for value in parent[:-1])]
    assert len(child) == 2 * len(parent) == 25746
    assert all(0 < value < (1 << NEW_K) for value in child)
    OUTPUT.write_text(" ".join(map(str, child)) + "\n")

    parent_seen, parent_frontier = interval_or_spectrum(parent)
    child_seen, child_frontier = interval_or_spectrum(child)
    parent_universe = set(range(1, 1 << OLD_K))
    child_universe = set(range(1, 1 << NEW_K))
    assert parent_seen == parent_universe
    assert child_seen == child_universe

    core = {
        "status": "PASS_LITERAL_UNIVERSAL_WORD",
        "claim": "nu(17) <= 25746",
        "construction": "X + [z] + ((X without its last cell) OR z)",
        "source": str(SOURCE.relative_to(ROOT)),
        "source_sha256": digest(SOURCE),
        "source_length": len(parent),
        "source_covered": len(parent_seen),
        "source_required": len(parent_universe),
        "source_maximum_suffix_frontier": parent_frontier,
        "word": str(OUTPUT.relative_to(ROOT)),
        "word_sha256": digest(OUTPUT),
        "word_length": len(child),
        "covered": len(child_seen),
        "required": len(child_universe),
        "missing": [],
        "maximum_suffix_frontier": child_frontier,
        "letter_rank_histogram": dict(sorted(Counter(map(int.bit_count, child)).items())),
        "scope": "explicit upper bound only; does not claim the conjectured optimum B(17)=24313",
    }
    payload = dict(core)
    payload["payload_sha256"] = sha256(
        json.dumps(core, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()
    AUDIT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps(payload, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
