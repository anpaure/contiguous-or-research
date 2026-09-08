#!/usr/bin/env python3
"""Exact diagnostics for the Dyck tail-seam finite-state matching.

This script is only a finite audit; the proof belongs in MASTER_HANDOFF.md.
It deliberately uses no third-party packages.
"""

from __future__ import annotations

import argparse
from collections import Counter, deque
from itertools import product


SIGMA = ("U", "D", "A", "B")
BITS = {"U": "11", "D": "00", "A": "10", "B": "01"}


def dyck_words(r: int):
    def visit(prefix: str, up: int, down: int):
        if up == down == r:
            yield prefix
            return
        if up < r:
            yield from visit(prefix + "1", up + 1, down)
        if down < up:
            yield from visit(prefix + "0", up, down + 1)

    yield from visit("", 0, 0)


def mu(word: str) -> str:
    return word[::-1].translate(str.maketrans("01", "10"))


def rho(word: str) -> tuple[int, ...]:
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
        + tuple(d - x for x in rho(mu(inside)))
        + (1,)
        + tuple(d + x for x in rho(suffix))
    )


def macro(word: str) -> str:
    r = len(word) // 2
    reverse = {value: key for key, value in BITS.items()}
    assert word[0] == "1" and word[-1] == "0"
    return "".join(reverse[word[1 + 2 * i : 3 + 2 * i]] for i in range(r - 1))


def unmacro(path: str) -> str:
    return "1" + "".join(BITS[x] for x in path) + "0"


def rank_map(word: str) -> dict[int, int]:
    return {label: index // 2 + 1 for index, label in enumerate(rho(word))}


def canonical_path(word: str) -> tuple[frozenset[int], ...]:
    r = len(word) // 2
    current = {i + 1 for i, bit in enumerate(word) if bit == "1"}
    answer = [frozenset(current)]
    order = rho(word)
    for phase in range(r):
        current ^= {order[2 * phase], order[2 * phase + 1]}
        answer.append(frozenset(current))
    return tuple(answer)


def defect(path: tuple[frozenset[int], ...]) -> int | None:
    multiplicity = Counter()
    for left, right in zip(path, path[1:]):
        if len(left ^ right) != 2:
            return None
        multiplicity.update(left ^ right)
    return sum(max(0, count - 1) for count in multiplicity.values())


def safe_seams(peak: str, valley: str) -> tuple[int, ...]:
    assert len(peak) == len(valley)
    changed = [i + 1 for i, (x, y) in enumerate(zip(peak, valley)) if x != y]
    assert len(changed) == 2 and peak[changed[0] - 1 : changed[1]] == "10"
    left, right = canonical_path(peak), canonical_path(valley)
    answer = []
    for seam in range(1, len(left)):
        first = left[:seam] + right[seam:]
        second = right[:seam] + left[seam:]
        if defect(first) == defect(second) == 1:
            answer.append(seam)
    return tuple(answer)


def sufficient_macro_edge(left: str, right: str) -> bool:
    """The two local edge families used by the proved matching."""
    changed = [i for i, (x, y) in enumerate(zip(left, right)) if x != y]
    if len(changed) == 1:
        i = changed[0]
        if {left[i], right[i]} != {"A", "B"}:
            return False
        peak = left if left[i] == "A" else right
        before = peak[i - 1] if i else "S"
        after = peak[i + 1] if i + 1 < len(peak) else "E"
        return not (before in {"A", "D"} and after in {"A", "U"})
    if len(changed) == 2 and changed[1] == changed[0] + 1:
        i = changed[0]
        return {left[i : i + 2], right[i : i + 2]} == {"AA", "UD"}
    return False


def local_sweep(paths: set[str]) -> tuple[set[str], tuple[int, ...]]:
    if not paths:
        return set(), ()
    n = len(next(iter(paths)))
    residual = set(paths)
    rounds = []
    for i in range(n):
        pairs = set()
        for path in tuple(residual):
            if path[i] not in {"A", "B"}:
                continue
            mate = path[:i] + ("B" if path[i] == "A" else "A") + path[i + 1 :]
            if mate in residual and sufficient_macro_edge(path, mate):
                pairs.add(frozenset((path, mate)))
        used = set().union(*pairs) if pairs else set()
        residual -= used
        rounds.append(len(pairs))

        if i + 1 == n:
            continue
        pairs = set()
        for path in tuple(residual):
            block = path[i : i + 2]
            if block not in {"AA", "UD"}:
                continue
            mate_block = "UD" if block == "AA" else "AA"
            mate = path[:i] + mate_block + path[i + 2 :]
            if mate in residual:
                pairs.add(frozenset((path, mate)))
        used = set().union(*pairs) if pairs else set()
        residual -= used
        rounds.append(len(pairs))
    return residual, tuple(rounds)


def first_uh_matching(paths: set[str]) -> tuple[int, set[str]]:
    """Pair at the first factor U(A or B), toggling its horizontal colour."""
    pairs = set()
    residual = set()
    for path in paths:
        location = next(
            (
                i + 1
                for i in range(len(path) - 1)
                if path[i] == "U" and path[i + 1] in {"A", "B"}
            ),
            None,
        )
        if location is None:
            residual.add(path)
            continue
        mate = (
            path[:location]
            + ("B" if path[location] == "A" else "A")
            + path[location + 1 :]
        )
        assert mate in paths
        mate_location = next(
            i + 1
            for i in range(len(mate) - 1)
            if mate[i] == "U" and mate[i + 1] in {"A", "B"}
        )
        assert mate_location == location
        assert sufficient_macro_edge(path, mate)
        pairs.add(frozenset((path, mate)))
    assert 2 * len(pairs) + len(residual) == len(paths)
    return len(pairs), residual


def transition(state: tuple[str, tuple[int, int, int, int]]):
    """One nonterminal sweep step in the prefix-status automaton."""
    before, raw = state
    live = dict(zip(SIGMA, raw))

    def after_flip(current: str, following: str) -> bool:
        safe = not (before in {"A", "D"} and following in {"A", "U"})
        if current not in {"A", "B"} or not safe:
            return bool(live[current])
        mate = "B" if current == "A" else "A"
        return bool(live[current] and not live[mate])

    answer = []
    for current in SIGMA:
        next_vector = []
        for following in SIGMA:
            value = after_flip(current, following)
            if (current, following) == ("A", "A"):
                value = value and not after_flip("U", "D")
            elif (current, following) == ("U", "D"):
                value = value and not after_flip("A", "A")
            next_vector.append(int(value))
        if any(next_vector):
            answer.append((current, tuple(next_vector)))
    return tuple(answer)


def final_weight(state: tuple[str, tuple[int, int, int, int]]) -> int:
    _, raw = state
    live = dict(zip(SIGMA, raw))
    return (
        live["U"]
        + live["D"]
        + int(live["A"] and not live["B"])
        + int(live["B"] and not live["A"])
    )


def automaton():
    start = ("S", (1, 1, 1, 1))
    states = [start]
    index = {start: 0}
    queue = deque([start])
    while queue:
        state = queue.popleft()
        for following in transition(state):
            if following not in index:
                index[following] = len(states)
                states.append(following)
                queue.append(following)
    matrix = [[0] * len(states) for _ in states]
    for i, state in enumerate(states):
        for following in transition(state):
            matrix[i][index[following]] += 1
    square = [
        [sum(matrix[i][k] * matrix[k][j] for k in range(len(states)))
         for j in range(len(states))]
        for i in range(len(states))
    ]
    return states, matrix, square


def unrestricted_counts(limit: int):
    states, matrix, square = automaton()
    vector = [0] * len(states)
    vector[0] = 1
    counts = []
    for n in range(1, limit + 1):
        if n > 1:
            vector = [
                sum(vector[i] * matrix[i][j] for i in range(len(states)))
                for j in range(len(states))
            ]
        counts.append(sum(vector[i] * final_weight(states[i]) for i in range(len(states))))
    assert max(map(sum, square)) == 8
    return counts, states, matrix, square


def audit(max_r: int):
    counts, states, matrix, square = unrestricted_counts(max_r - 1)
    rows = []
    for r in range(2, max_r + 1):
        words = tuple(dyck_words(r))
        word_set = set(words)
        paths = {macro(word) for word in words}
        assert all(unmacro(path) in word_set for path in paths)
        residual, rounds = local_sweep(paths)
        first_uh_pairs, first_uh_residual = first_uh_matching(paths)

        # Every selected local rule really has a canonical defect-one seam.
        checked_edges = set()
        for path in paths:
            for i in range(len(path)):
                if path[i] in {"A", "B"}:
                    mate = path[:i] + ("B" if path[i] == "A" else "A") + path[i + 1 :]
                    if mate in paths and sufficient_macro_edge(path, mate):
                        checked_edges.add(frozenset((path, mate)))
                if i + 1 < len(path) and path[i : i + 2] in {"AA", "UD"}:
                    block = "UD" if path[i : i + 2] == "AA" else "AA"
                    mate = path[:i] + block + path[i + 2 :]
                    if mate in paths:
                        checked_edges.add(frozenset((path, mate)))
        for edge in checked_edges:
            left, right = map(unmacro, edge)
            changed = [i for i, (x, y) in enumerate(zip(left, right)) if x != y]
            assert len(changed) == 2
            if left[changed[0] : changed[1] + 1] == "10":
                peak, valley = left, right
            else:
                peak, valley = right, left
            assert safe_seams(peak, valley)

        # The unrestricted finite-state residual is an upper bound.
        assert len(residual) <= counts[r - 2]
        rows.append(
            {
                "r": r,
                "Catalan": len(paths),
                "selected_rule_edges": len(checked_edges),
                "rounds": rounds,
                "leave": len(residual),
                "first_UH_pairs": first_uh_pairs,
                "first_UH_leave": len(first_uh_residual),
                "unrestricted_bound": counts[r - 2],
            }
        )
    return {
        "states": states,
        "matrix": matrix,
        "square_row_sums": tuple(map(sum, square)),
        "unrestricted_counts": counts,
        "rows": rows,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-r", type=int, default=10)
    args = parser.parse_args()
    print("DYCK_TAIL_SEAM_AUTOMATON", audit(args.max_r), flush=True)


if __name__ == "__main__":
    main()
