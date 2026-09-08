#!/usr/bin/env python3
"""Exact modular column-span audit for a finite Z17 quotient pool.

Run only on H100.  The input is one of the JSON maps emitted by the
owner-cover generators.  For p in {2,3,5}, this computes the exact rank of
the owner-incidence columns and tests whether the all-one owner target is in
their span.  For a mixed-period pool it also appends the period-11 indicator
row and tests the exact scalar faces b=10t, 0 <= t <= 13.
"""

from __future__ import annotations

import argparse
import json

import numpy as np


PRIMES = (2, 3, 5)


def inverse(value: int, prime: int) -> int:
    return pow(value, prime - 2, prime)


class ModularBasis:
    def __init__(self, dimension: int, prime: int):
        self.dimension = dimension
        self.prime = prime
        self.rows: list[np.ndarray | None] = [None] * dimension
        self.rank = 0

    def reduce(self, vector: np.ndarray) -> np.ndarray:
        p = self.prime
        for pivot, row in enumerate(self.rows):
            coefficient = int(vector[pivot])
            if coefficient and row is not None:
                vector -= coefficient * row
                np.remainder(vector, p, out=vector)
        return vector

    def insert(self, vector: np.ndarray) -> bool:
        self.reduce(vector)
        support = np.flatnonzero(vector)
        if not len(support):
            return False
        pivot = int(support[0])
        vector *= inverse(int(vector[pivot]), self.prime)
        np.remainder(vector, self.prime, out=vector)
        assert self.rows[pivot] is None
        self.rows[pivot] = vector
        self.rank += 1
        return True

    def contains(self, target: np.ndarray) -> bool:
        return not np.any(self.reduce(target.copy()))


def audit(
    candidates: list[dict], owner_orbits: int, prime: int,
    include_period_row: bool, maximum_rank: int,
) -> tuple[ModularBasis, int]:
    dimension = owner_orbits + int(include_period_row)
    basis = ModularBasis(dimension, prime)
    processed = 0
    for candidate in candidates:
        vector = np.zeros(dimension, dtype=np.int16)
        vector[candidate["edge"]] = 1
        if include_period_row:
            vector[-1] = int(candidate.get("period", 10) == 11)
        basis.insert(vector)
        processed += 1
        if basis.rank == maximum_rank:
            break
    return basis, processed


def owner_target(owner_orbits: int, dimension: int, period11: int = 0) -> np.ndarray:
    target = np.ones(dimension, dtype=np.int16)
    if dimension > owner_orbits:
        target[-1] = period11
    return target


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--map", required=True)
    parser.add_argument(
        "--faces", action="store_true",
        help="append the period-11 count row and test b=10t for t=0..13",
    )
    args = parser.parse_args()

    with open(args.map, encoding="utf-8") as stream:
        data = json.load(stream)
    candidates = data["candidates"]
    owner_orbits = int(data["owner_orbits"])
    periods = sorted({int(candidate.get("period", 10)) for candidate in candidates})
    # Mixed generators conventionally store the periods in blocks.  Exact
    # elimination is much faster when they are interleaved: period 11 has
    # odd weight and reaches the owner-row rank immediately over p=2,5,
    # while one early period-10 column breaks the extra augmented-row
    # dependence over p=3.  Reordering does not change the column span.
    if periods == [10, 11]:
        by_period = {
            period: [
                candidate for candidate in candidates
                if candidate.get("period", 10) == period
            ]
            for period in periods
        }
        candidates = []
        for index in range(max(map(len, by_period.values()))):
            for period in (11, 10):
                if index < len(by_period[period]):
                    candidates.append(by_period[period][index])

    report = {
        "map": args.map,
        "candidates": len(candidates),
        "owner_orbits": owner_orbits,
        "periods": periods,
        "elimination_order": "period11_10_interleaved" if periods == [10, 11] else "stored",
        "owner_lattice": {},
    }
    for prime in PRIMES:
        # If every column has one common weight divisible by p, the all-one
        # row is a left-null vector.  Otherwise no scalar left-null relation
        # is forced, so reaching full row rank certifies the exact rank.
        scalar_nullity = int(
            len(periods) == 1 and periods[0] % prime == 0
        )
        maximum_rank = owner_orbits - scalar_nullity
        basis, processed = audit(
            candidates, owner_orbits, prime, False, maximum_rank
        )
        target = owner_target(owner_orbits, owner_orbits)
        report["owner_lattice"][str(prime)] = {
            "rank": basis.rank,
            "consistent": basis.contains(target),
            "processed_until_full_or_exhausted": processed,
        }

    if args.faces:
        assert periods == [10, 11]
        report["period_count_faces"] = {}
        for prime in PRIMES:
            # On the augmented (owner, period-11-count) rows, p=2 or 5
            # has the forced left-null relation
            # sum(owner rows)-11*period11_row=0.  For p=3 there is no
            # nonzero scalar relation because a period-10 column has sum 10.
            scalar_nullity = int(10 % prime == 0)
            maximum_rank = owner_orbits + 1 - scalar_nullity
            basis, processed = audit(
                candidates, owner_orbits, prime, True, maximum_rank
            )
            faces = {}
            for t in range(14):
                b = 10 * t
                target = owner_target(owner_orbits, owner_orbits + 1, b % prime)
                faces[str(t)] = basis.contains(target)
            report["period_count_faces"][str(prime)] = {
                "rank": basis.rank,
                "processed_until_full_or_exhausted": processed,
                "consistent_t": [int(t) for t, ok in faces.items() if ok],
                "inconsistent_t": [int(t) for t, ok in faces.items() if not ok],
            }

    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
