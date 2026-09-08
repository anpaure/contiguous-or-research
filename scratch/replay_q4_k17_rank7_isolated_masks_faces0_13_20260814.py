#!/usr/bin/env python3
"""Independent replay for the canonical 3-separated rank-seven mark schedules.

Substantive execution is intended for H100 only.  This file deliberately
does not import the search program.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import sys
from collections import Counter
from pathlib import Path


CORE = frozenset(range(5))
TYPES = (
    (1, 5, 2, 1), (1, 6, 1, 1), (2, 5, 1, 1),
    (3, 3, 2, 1), (3, 4, 1, 1), (4, 3, 1, 1),
    (5, 1, 2, 1), (5, 2, 1, 1), (6, 1, 1, 1),
)
TYPE_COUNTS = (139, 297, 8, 20, 20, 140, 127, 237, 442)
UNMARKED = frozenset((0, 3, 6))


def partitions(sizes):
    for middle in itertools.combinations(CORE, sizes[1]):
        middle = frozenset(middle)
        rest = CORE - middle
        for old in itertools.combinations(rest, sizes[2]):
            old = frozenset(old)
            yield CORE - middle - old, middle, old


def catalogue():
    states = []
    for type_id, kind in enumerate(TYPES):
        for parts in partitions(tuple(value - 1 for value in kind[:3])):
            states.append((type_id, parts))
    arcs = frozenset(
        (i, j) for i, (_, old) in enumerate(states)
        for j, (_, new) in enumerate(states)
        if new[1] <= old[0] and new[2] <= old[1]
    )
    assert len(states) == 72 and len(arcs) == 793
    return states, arcs


def canonical_masks(t):
    lengths = [10] * (143 - 11 * t) + [11] * (10 * t)
    extras = 2 * t
    masks = []
    for cycle_id, length in enumerate(lengths):
        word = [0] * length
        word[0] = word[3] = 1
        if cycle_id < extras:
            word[6] = 1
        masks.append(tuple(word))
    assert sum(map(sum, masks)) == 286
    return masks


def cyclic_distance(i, j, n):
    delta = (i - j) % n
    return min(delta, n - delta)


def main():
    if len(sys.argv) != 3:
        raise SystemExit("usage: replay.py SEARCH_SOURCE CERTIFICATE")
    search_path = Path(sys.argv[1])
    certificate_path = Path(sys.argv[2])
    certificate = json.loads(certificate_path.read_text())
    assert certificate["summary"] == "PASS"
    assert certificate["source_sha256"] == hashlib.sha256(search_path.read_bytes()).hexdigest()
    states, arcs = catalogue()
    reports = certificate["reports"]
    assert [report["t"] for report in reports] == list(range(14))
    face_hashes = []
    for report in reports:
        t = report["t"]
        assert report["mode"] == "isolated3"
        assert report["status"] in ("OPTIMAL", "FEASIBLE")
        masks = canonical_masks(t)
        words = report["state_words"]
        assert len(words) == len(masks) == 143 - t
        assert sum(len(word) == 10 for word in words) == 143 - 11 * t
        assert sum(len(word) == 11 for word in words) == 10 * t
        assert report["cycles"] == 143 - t
        assert report["mask_multiset_sha256"] == hashlib.sha256(json.dumps(
            sorted("".join(map(str, mask)) for mask in masks),
                   separators=(",", ":")
        ).encode()).hexdigest()
        assert report["state_words_sha256"] == hashlib.sha256(json.dumps(
            words, separators=(",", ":")
        ).encode()).hexdigest()
        counts = Counter()
        for mask, word in zip(masks, words):
            assert len(mask) == len(word)
            unmarked_positions = [i for i, bit in enumerate(mask) if bit]
            assert len(unmarked_positions) in (2, 3)
            assert all(cyclic_distance(i, j, len(mask)) >= 3
                       for p, i in enumerate(unmarked_positions)
                       for j in unmarked_positions[p + 1:])
            for i, state_id in enumerate(word):
                assert 0 <= state_id < 72
                type_id = states[state_id][0]
                counts[type_id] += 1
                assert int(type_id in UNMARKED) == mask[i]
                assert (state_id, word[(i + 1) % len(word)]) in arcs
        assert tuple(counts[i] for i in range(9)) == TYPE_COUNTS
        assert report["type_counts"] == list(TYPE_COUNTS)
        face_hashes.append((t, report["state_words_sha256"]))
    print(json.dumps({
        "status": "PASS",
        "faces": 14,
        "positions_per_face": 1430,
        "unmarked_per_face": 286,
        "type_counts": TYPE_COUNTS,
        "states": len(states),
        "arcs": len(arcs),
        "search_source_sha256": certificate["source_sha256"],
        "certificate_sha256": hashlib.sha256(certificate_path.read_bytes()).hexdigest(),
        "replay_source_sha256": hashlib.sha256(Path(sys.argv[0]).read_bytes()).hexdigest(),
        "face_state_word_hashes": face_hashes,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
