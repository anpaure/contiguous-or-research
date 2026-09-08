#!/usr/bin/env python3
"""Exhaustive audit of the reverse first-UHD two-seam proposal.

For every Dyck root through the requested semilength, this checker:

* forms the first-UHD A/B mate;
* verifies the local rho normal form;
* constructs the two reverse asymmetric hybrids;
* verifies their exact flip streams and their one-duplicate/one-hole ledger;
* proves computationally that each hybrid contains a Johnson triangle and
  is therefore not a phase packet; and
* audits the global Catalan occurrence, collision, and hole counts.

The enumeration is evidence only.  The accompanying obstruction note gives
the dimension-independent proof.
"""

from __future__ import annotations

import argparse
from collections import Counter
from math import comb


BITS = {"U": "11", "D": "00", "A": "10", "B": "01"}


def catalan(n: int) -> int:
    return comb(2 * n, n) // (n + 1)


def dyck_words(b: int):
    def visit(prefix: str, ones: int, zeros: int):
        if ones == zeros == b:
            yield prefix
            return
        if ones < b:
            yield from visit(prefix + "1", ones + 1, zeros)
        if zeros < ones:
            yield from visit(prefix + "0", ones, zeros + 1)

    yield from visit("", 0, 0)


def reverse_complement(word: str) -> str:
    return word[::-1].translate(str.maketrans("01", "10"))


def rho(word: str) -> tuple[int, ...]:
    """The recursive Chung--Feller flip permutation."""
    if not word:
        return ()
    height = 0
    close = None
    for index, bit in enumerate(word):
        height += 1 if bit == "1" else -1
        if height == 0:
            close = index
            break
    assert close is not None
    inside, suffix = word[1:close], word[close + 1 :]
    d = len(inside) + 2
    return (
        (d,)
        + tuple(d - x for x in rho(reverse_complement(inside)))
        + (1,)
        + tuple(d + x for x in rho(suffix))
    )


def macro(word: str) -> str:
    reverse = {bits: symbol for symbol, bits in BITS.items()}
    b = len(word) // 2
    assert word[0] == "1" and word[-1] == "0"
    return "".join(reverse[word[1 + 2 * i : 3 + 2 * i]] for i in range(b - 1))


def unmacro(path: str) -> str:
    return "1" + "".join(BITS[symbol] for symbol in path) + "0"


def first_uhd(path: str) -> int | None:
    """Zero-based location of the U in the first U(A/B)D factor."""
    return next(
        (
            i
            for i in range(len(path) - 2)
            if path[i] == "U" and path[i + 1] in {"A", "B"} and path[i + 2] == "D"
        ),
        None,
    )


def canonical_path(word: str) -> tuple[frozenset[int], ...]:
    b = len(word) // 2
    current = {i + 1 for i, bit in enumerate(word) if bit == "1"}
    answer = [frozenset(current)]
    order = rho(word)
    for phase in range(b):
        current ^= {order[2 * phase], order[2 * phase + 1]}
        answer.append(frozenset(current))
    return tuple(answer)


def transition_stream(path: tuple[frozenset[int], ...]) -> tuple[int, ...]:
    stream: list[int] = []
    for left, right in zip(path, path[1:]):
        added, removed = right - left, left - right
        assert len(added) == len(removed) == 1
        stream.extend((next(iter(added)), next(iter(removed))))
    return tuple(stream)


def unique_middle_window_word(
    path: tuple[frozenset[int], ...],
) -> tuple[int, ...]:
    """Recover the unique word whose consecutive length-b windows are path."""
    stream = transition_stream(path)
    additions, removals = stream[::2], stream[1::2]
    assert len(set(removals)) == len(removals)
    assert frozenset(removals) == path[0]
    word = removals + additions
    b = len(path) - 1
    assert tuple(
        frozenset(word[start : start + b]) for start in range(b + 1)
    ) == path
    return word


def johnson_distance(left: frozenset[int], right: frozenset[int]) -> int:
    assert len(left) == len(right)
    return len(left - right)


def distance_one_edges(path: tuple[frozenset[int], ...]) -> set[frozenset[int]]:
    return {
        frozenset((i, j))
        for i in range(len(path))
        for j in range(i + 1, len(path))
        if johnson_distance(path[i], path[j]) == 1
    }


def is_ordered_phase_packet(path: tuple[frozenset[int], ...], ground: set[int]) -> bool:
    """Exact test for (C_0,...,C_b) in the labelled packet definition."""
    b = len(ground) // 2
    if len(path) != b + 1 or len(set(path)) != b + 1:
        return False
    if any(len(vertex) != b or not vertex <= ground for vertex in path):
        return False
    try:
        stream = transition_stream(path)
    except AssertionError:
        return False
    loads = Counter(stream)
    repeated = [label for label in ground if loads[label] == 2]
    omitted = [label for label in ground if loads[label] == 0]
    if len(repeated) != 1 or len(omitted) != 1:
        return False
    if any(loads[label] != 1 for label in ground - set(repeated) - set(omitted)):
        return False
    pivot = repeated[0]
    additions, removals = stream[::2], stream[1::2]
    return removals[0] == pivot and additions[-1] == pivot


def sample_phase_packet(b: int) -> tuple[frozenset[int], ...]:
    ground = list(range(1, 2 * b + 1))
    pivot, omitted = ground[:2]
    x = ground[2 : b + 1]
    y = ground[b + 1 :]
    path = [frozenset({pivot, *x})]
    for i in range(1, b):
        path.append(frozenset(x[i - 1 :] + y[:i]))
    path.append(frozenset({pivot, *y}))
    assert omitted not in set().union(*path)
    return tuple(path)


def nonzero_difference(left: Counter, right: Counter) -> dict[frozenset[int], int]:
    keys = set(left) | set(right)
    return {key: left[key] - right[key] for key in keys if left[key] != right[key]}


def audit_dimension(b: int) -> dict[str, object]:
    assert b >= 4
    ground = set(range(1, 2 * b + 1))
    phase_example = sample_phase_packet(b)
    assert is_ordered_phase_packet(phase_example, ground)
    assert distance_one_edges(phase_example) == {
        frozenset((i, i + 1)) for i in range(b)
    }

    roots = tuple(dyck_words(b))
    assert len(roots) == catalan(b)
    root_set = set(roots)
    canonical_occurrences: Counter = Counter()
    reverse_occurrences: Counter = Counter()
    pairs = 0
    residual = 0
    first_example = None

    for peak in roots:
        peak_path = canonical_path(peak)
        canonical_occurrences.update(peak_path)
        encoded = macro(peak)
        location = first_uhd(encoded)
        if location is None:
            residual += 1
            continue
        if encoded[location + 1] == "B":
            continue

        pairs += 1
        mate_code = encoded[: location + 1] + "B" + encoded[location + 2 :]
        valley = unmacro(mate_code)
        assert first_uhd(mate_code) == location
        assert valley in root_set
        valley_path = canonical_path(valley)

        changed = [
            i + 1 for i, (left, right) in enumerate(zip(peak, valley)) if left != right
        ]
        assert len(changed) == 2 and changed[1] == changed[0] + 1
        u, v = changed
        order_p, order_q = rho(peak), rho(valley)
        s = (order_p.index(u) + 1) // 2
        assert 1 <= s <= b - 1
        gamma = order_p[: 2 * (s - 1)]
        c, seen_u, seen_v, d = order_p[2 * (s - 1) : 2 * (s + 1)]
        delta = order_p[2 * (s + 1) :]
        assert (seen_u, seen_v) == (u, v)
        assert len({c, u, v, d}) == 4
        assert order_q == gamma + (u, d, c, v) + delta

        common = peak_path[s] - {c, d}
        assert len(common) == b - 2
        assert peak_path[s - 1] == common | {u, d}
        assert peak_path[s] == common | {c, d}
        assert peak_path[s + 1] == common | {c, v}
        assert valley_path[s - 1] == common | {v, d}
        assert valley_path[s] == common | {u, v}
        assert valley_path[s + 1] == common | {u, c}

        reverse_x = valley_path[:s] + peak_path[s:]
        reverse_y = peak_path[: s + 1] + valley_path[s + 1 :]
        assert transition_stream(reverse_x) == gamma + (c, v, v, d) + delta
        assert transition_stream(reverse_y) == gamma + (c, u, u, d) + delta
        assert len(set(reverse_x)) == len(set(reverse_y)) == b + 1
        word_x = unique_middle_window_word(reverse_x)
        word_y = unique_middle_window_word(reverse_y)
        assert word_x[s - 1] == word_x[b + s] == v
        assert word_y[s - 1] == word_y[b + s] == u
        assert len(set(word_x[s - 1 : s + b + 1])) == b + 1
        assert len(set(word_y[s - 1 : s + b + 1])) == b + 1

        original_pair = Counter(peak_path + valley_path)
        reverse_pair = Counter(reverse_x + reverse_y)
        assert nonzero_difference(reverse_pair, original_pair) == {
            peak_path[s]: 1,
            valley_path[s]: -1,
        }

        edges_x, edges_y = distance_one_edges(reverse_x), distance_one_edges(reverse_y)
        assert all(
            frozenset(edge) in edges_x
            for edge in ((s - 1, s), (s, s + 1), (s - 1, s + 1))
        )
        assert all(
            frozenset(edge) in edges_y
            for edge in ((s - 1, s), (s, s + 1), (s - 1, s + 1))
        )
        assert not is_ordered_phase_packet(reverse_x, ground)
        assert not is_ordered_phase_packet(reverse_y, ground)

        reverse_occurrences.update(reverse_x)
        reverse_occurrences.update(reverse_y)
        if first_example is None:
            first_example = {
                "P": peak,
                "Q": valley,
                "s": s,
                "rho_P": order_p,
                "rho_Q": order_q,
            }

    total = comb(2 * b, b)
    assert 2 * pairs + residual == catalan(b)
    assert len(canonical_occurrences) == total
    assert set(canonical_occurrences.values()) == {1}

    occurrence_count = sum(reverse_occurrences.values())
    collision_excess = sum(max(0, load - 1) for load in reverse_occurrences.values())
    holes = total - len(reverse_occurrences)
    assert occurrence_count == 2 * pairs * (b + 1)
    assert collision_excess == pairs
    assert holes == pairs + (b + 1) * residual
    assert max(reverse_occurrences.values(), default=0) <= 2

    n = b - 1
    quotient, remainder = divmod(n, 3)
    unrestricted_residual_bound = 62**quotient * 4**remainder
    assert residual <= unrestricted_residual_bound

    return {
        "b": b,
        "Catalan": catalan(b),
        "pairs": pairs,
        "residual_roots": residual,
        "middle_vertices": total,
        "reverse_occurrences": occurrence_count,
        "collision_excess": collision_excess,
        "holes": holes,
        "residual_bound": unrestricted_residual_bound,
        "first_example": first_example,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--min-b", type=int, default=4)
    parser.add_argument("--max-b", type=int, default=10)
    args = parser.parse_args()
    for b in range(args.min_b, args.max_b + 1):
        print("REVERSE_UHD_TWO_SEAM_NO_GO_PASS", audit_dimension(b), flush=True)


if __name__ == "__main__":
    main()
