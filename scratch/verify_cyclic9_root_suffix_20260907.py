"""Independent H100-only cyclic-word certificate check by suffix recurrence.

This imports neither the tree-bank search nor its verifier. All mathematical
execution is to be performed on ssh h100, not on the local workstation.
"""
import hashlib
import json
from math import comb
from pathlib import Path
import resource
import signal
import sys


def require(test, reason):
    if not test:
        raise AssertionError(reason)


def rotate(mask, step, dimension):
    result = 0
    for bit in range(dimension):
        if mask & (1 << bit):
            result |= 1 << ((bit + step) % dimension)
    return result


def main():
    require(sys.platform.startswith("linux"), "Run explicitly on H100/Linux")
    resource.setrlimit(resource.RLIMIT_AS, (256 << 20, 256 << 20))
    resource.setrlimit(resource.RLIMIT_CPU, (10, 10))
    signal.alarm(10)
    require(len(sys.argv) == 2, "supply one literal word file")
    raw = Path(sys.argv[1]).read_bytes()
    word = [int(x) for x in raw.split()]
    k, n = 9, len(word)
    full = (1 << k) - 1
    require(n == comb(k, k // 2) == 126, "not the width-length candidate")
    require(all(0 < mask <= full for mask in word), "invalid alphabet")

    # For each current OR value retain its LATEST eligible start. Equal
    # values have identical future extensions, and the latest start lasts
    # longest under the one-period length bound. Starts lie in period one.
    # Appending all but the last letter of period two suffices for every
    # legal cyclic interval starting in that first period.
    ending = {}
    witnesses = {}
    max_ending_chain = 0
    for end, letter in enumerate(word + word[:-1]):
        next_ending = {letter: end} if end < n else {}
        for value, start in ending.items():
            if end - start + 1 <= n:
                union = value | letter
                next_ending[union] = max(start, next_ending.get(union, -1))
        ending = next_ending
        max_ending_chain = max(max_ending_chain, len(ending))
        require(len(ending) <= k, "suffix unions should form a nonempty chain")
        for value, start in ending.items():
            length = end - start + 1
            require(0 <= start < n and 1 <= length <= n, "illegal cyclic witness")
            witnesses.setdefault(value, (start, length))
    require(set(witnesses) == set(range(1, full + 1)), "missing a nonempty target")

    # Replay each returned witness directly, independently of the recurrence.
    for value, (start, length) in witnesses.items():
        replay = 0
        for offset in range(length):
            replay |= word[(start + offset) % n]
        require(replay == value, "witness replay failed")

    rank_counts = {str(rank): sum(mask.bit_count() == rank for mask in witnesses)
                   for rank in range(1, k + 1)}
    require(all(rank_counts[str(rank)] == comb(k, rank) for rank in range(1, k + 1)),
            "rank inventory mismatch")
    voltages = [step for step in range(1, k)
                if all(word[(i + 14) % n] == rotate(word[i], step, k) for i in range(n))]
    require(len(voltages) == 1 and voltages[0] % 3 != 0, "missing unit development voltage")
    canonical = lambda mask: min(rotate(mask, step, k) for step in range(k))
    orbit_witnesses = {}
    for value, (start, length) in witnesses.items():
        base_start = start % 14
        base_value = 0
        for offset in range(length):
            base_value |= word[(base_start + offset) % n]
        representative = canonical(value)
        require(canonical(base_value) == representative, "normalized orbit witness mismatch")
        proposal = (length, base_start, base_value)
        if representative not in orbit_witnesses or proposal < orbit_witnesses[representative]:
            orbit_witnesses[representative] = proposal
    expected_orbits = {canonical(mask) for mask in range(1, full + 1)}
    require(set(orbit_witnesses) == expected_orbits, "missing rotation orbit")
    orbit_table = [{"representative": representative, "rank": representative.bit_count(),
                    "start": value[1], "length": value[0], "window_union": value[2],
                    "orbit_size": len({rotate(representative, step, k) for step in range(k)})}
                   for representative, value in sorted(orbit_witnesses.items())]
    central = {}
    for length in (3, 4):
        values = []
        for start in range(n):
            value = 0
            for offset in range(length):
                value |= word[(start + offset) % n]
            values.append(value)
        central[str(length)] = {"distinct": len(set(values)),
                                "ranks": sorted({v.bit_count() for v in values})}

    report = {"status": "ROOT_SUFFIX_RECURRENCE_ALL_511_PASS", "k": k,
              "length": n, "lower_bound": comb(k, k // 2),
              "sha256": hashlib.sha256(raw).hexdigest(),
              "rank_counts": rank_counts, "base_seed": word[:14],
              "rotation_voltages": voltages, "central_windows": central,
              "orbit_count": len(orbit_table), "orbit_witnesses": orbit_table,
              "max_suffix_chain_size": max_ending_chain,
              "method": "latest-start suffix-union recurrence plus replay of every target"}
    print(json.dumps(report, sort_keys=True))


if __name__ == "__main__":
    main()
