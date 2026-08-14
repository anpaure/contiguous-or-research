#!/usr/bin/env python3
"""Independent replay of the quotient-twisted owner edge-axis no-go.

Substantive execution belongs on H100.  This does not import the search
enumerator.  It independently normalizes the core by translation, builds
all adjacent reflected boundary words, pairs disjoint halves, and checks
all five owner relations for the involution i -> 1-i.
"""

from __future__ import annotations

import itertools
import json
import multiprocessing as mp
from collections import Counter

from search_q4_k17_z17_quotient_exact_cover_20260814 import (
    K,
    canonical_orbit_mask,
    deck_masks,
    subset_mask,
)


def negate(mask):
    return subset_mask((-value) % K for value in range(K) if mask >> value & 1)


def reflected_representative(mask):
    return canonical_orbit_mask(negate(mask))


def canonical_cores():
    return [
        core for core in itertools.combinations(range(K), 5)
        if canonical_orbit_mask(subset_mask(core)) == subset_mask(core)
    ]


def boundary_bank(core):
    complement = tuple(value for value in range(K) if value not in core)
    core_mask = subset_mask(core)
    rows = []
    for word in itertools.permutations(complement, 5):
        left = core_mask | subset_mask(word[:4])
        right = core_mask | subset_mask(word[1:])
        if canonical_orbit_mask(right) == reflected_representative(left):
            rows.append(word)
    return rows


def audit_cores(cores):
    counts = Counter()
    relation_histogram = Counter()
    for core in cores:
        bank = boundary_bank(core)
        counts["boundary_words"] += len(bank)
        rows = [(word, frozenset(word)) for word in bank]
        for left, left_set in rows:
            for right, right_set in rows:
                if left_set & right_set:
                    continue
                counts["disjoint_boundary_pairs"] += 1
                order = left + right
                owners = tuple(map(canonical_orbit_mask, deck_masks(core, order)))
                if len(set(owners)) != 10:
                    counts["owner_nonsimple"] += 1
                    continue
                counts["owner_simple"] += 1
                assert reflected_representative(owners[0]) == owners[1]
                assert reflected_representative(owners[1]) == owners[0]
                assert reflected_representative(owners[5]) == owners[6]
                assert reflected_representative(owners[6]) == owners[5]
                relations = (
                    reflected_representative(owners[2]) == owners[9],
                    reflected_representative(owners[3]) == owners[8],
                    reflected_representative(owners[4]) == owners[7],
                )
                relation_histogram["".join(map(lambda value: "1" if value else "0", relations))] += 1
                if all(relations):
                    counts["owner_edge_axis_columns"] += 1
    return counts, relation_histogram


def chunks(values, number):
    result = [[] for _ in range(number)]
    for index, value in enumerate(values):
        result[index % number].append(value)
    return [row for row in result if row]


def main():
    cores = canonical_cores()
    assert len(cores) == 364
    work = chunks(cores, 64)
    with mp.get_context("fork").Pool(processes=len(work)) as pool:
        reports = pool.map(audit_cores, work)
    counts = Counter()
    relation_histogram = Counter()
    for partial_counts, partial_histogram in reports:
        counts.update(partial_counts)
        relation_histogram.update(partial_histogram)

    assert counts == Counter({
        "boundary_words": 188160,
        "disjoint_boundary_pairs": 2115072,
        "owner_nonsimple": 173440,
        "owner_simple": 1941632,
    })
    assert relation_histogram.get("111", 0) == 0
    print(json.dumps({
        "status": "PASS",
        "canonical_core_necklaces": len(cores),
        "counts": dict(sorted(counts.items())),
        "remaining_three_pair_relation_histogram": dict(sorted(relation_histogram.items())),
        "normalization_proof_interface": (
            "translate the five-core to its unique necklace representative; "
            "rotate any odd-axis involution i->a-i to i->1-i; the two fixed "
            "owner-cycle edges split the support order into disjoint boundary "
            "words s0..s4 and s5..s9"
        ),
        "conclusion": (
            "no quotient-simple q4 period-10 column has induced owner "
            "reflection action i->1-i, even with row-dependent translating lifts"
        ),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
