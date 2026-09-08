#!/usr/bin/env python3
"""Test whether the b=9 five-row trade tensors inside Dyck contexts."""

from __future__ import annotations

import argparse
from itertools import product

from ortools.sat.python import cp_model


REMOVED_ORDERS = [
    (1, 3, 4, 2, 9, 7, 5, 6, 8),
    (1, 4, 3, 7, 2, 6, 5, 8, 9),
    (1, 4, 5, 3, 2, 8, 6, 7, 9),
    (1, 5, 3, 2, 9, 7, 6, 4, 8),
    (1, 6, 4, 3, 2, 8, 7, 5, 9),
]

ADDED_ORDERS = [
    (1, 3, 5, 2, 9, 7, 4, 6, 8),
    (1, 4, 3, 2, 5, 8, 6, 9, 7),
    (1, 4, 3, 8, 2, 6, 7, 9, 5),
    (1, 4, 9, 3, 2, 7, 6, 5, 8),
    (1, 6, 4, 3, 2, 7, 8, 5, 9),
]


def dyck_words(m: int):
    def rec(pos: int, ones: int, word: list[str]):
        if pos == 2 * m:
            yield "".join(word)
            return
        if ones < m:
            word.append("1")
            yield from rec(pos + 1, ones + 1, word)
            word.pop()
        if pos - ones < ones:
            word.append("0")
            yield from rec(pos + 1, ones, word)
            word.pop()

    yield from rec(0, 0, [])


def mu(word: str) -> str:
    return word[::-1].translate(str.maketrans("01", "10"))


def rho(word: str) -> list[int]:
    if not word:
        return []
    h = 0
    close = None
    for i, bit in enumerate(word):
        h += 1 if bit == "1" else -1
        if h == 0:
            close = i
            break
    assert close is not None
    u, v = word[1:close], word[close + 1 :]
    d = len(u) + 2
    return [d] + [d - x for x in rho(mu(u))] + [1] + [d + x for x in rho(v)]


def canonical(order):
    order = tuple(order)
    rots = [order[i:] + order[:i] for i in range(len(order))]
    rev = tuple(reversed(order))
    rots.extend(rev[i:] + rev[:i] for i in range(len(order)))
    return min(rots)


def msw_order(word: str):
    m = len(word) // 2
    b = 2 * m + 1
    q = rho(word) + [b]
    return canonical(tuple(q[(-1 - 2 * j) % b] for j in range(b)))


def omitted_forms(order, distinguished):
    b = len(order)
    answers = []
    for base in (tuple(order), tuple(reversed(order))):
        for shift in range(b):
            c = base[shift:] + base[:shift]
            q = [None] * b
            for j, value in enumerate(c):
                q[(-1 - 2 * j) % b] = value
            if q[-1] == distinguished:
                answers.append(tuple(q[:-1]))
    return tuple(sorted(set(answers)))


def vertex_deck_from_q(q, rank):
    b = len(q)
    return frozenset(
        frozenset(q[(i + 1 + 2 * j) % b] for j in range(rank))
        for i in range(b)
    )


def lower_deck_from_q(q, rank):
    b = len(q)
    return frozenset(
        frozenset(q[(i + 1 + 2 * j) % b] for j in range(rank - 1))
        for i in range(b)
    )


def find_block(seq, label_set):
    positions = [i for i, x in enumerate(seq) if x in label_set]
    if positions != list(range(min(positions), max(positions) + 1)):
        return None
    return min(positions), max(positions) + 1


def main(max_outer):
    removed_words = {}
    for word in dyck_words(4):
        order = msw_order(word)
        if order in {canonical(x) for x in REMOVED_ORDERS}:
            removed_words[order] = word
    assert len(removed_words) == 5
    base_old = sorted((word, tuple(rho(word))) for word in removed_words.values())
    base_added_forms = [omitted_forms(canonical(x), 9) for x in ADDED_ORDERS]
    assert all(len(x) == 2 for x in base_added_forms)

    # The base equality is independent of the chosen omitted-word orientation.
    base_old_deck = set().union(
        *(vertex_deck_from_q(p + (9,), 4) for _, p in base_old)
    )
    for choices in product((0, 1), repeat=5):
        deck = set().union(
            *(
                vertex_deck_from_q(base_added_forms[i][choices[i]] + (9,), 4)
                for i in range(5)
            )
        )
        assert deck == base_old_deck

    results = []
    for outer_m in range(max_outer + 1):
        for outer in dyck_words(outer_m):
            for gap in range(len(outer) + 1):
                local_labels = set(range(gap + 1, gap + 9))
                old_qs = []
                contexts = []
                valid_context = True
                for word, local_rho in base_old:
                    expanded = outer[:gap] + word + outer[gap:]
                    q = tuple(rho(expanded) + [2 * (outer_m + 4) + 1])
                    block = find_block(q[:-1], local_labels)
                    if block is None:
                        valid_context = False
                        break
                    lo, hi = block
                    actual = q[lo:hi]
                    identity = tuple(gap + x for x in local_rho)
                    reverse = tuple(gap + 9 - x for x in local_rho)
                    if actual == identity:
                        sign = 1
                    elif actual == reverse:
                        sign = -1
                    else:
                        valid_context = False
                        break
                    contexts.append((q[:lo], q[hi:-1], q[-1], sign))
                    old_qs.append(q)
                if not valid_context or len(set(contexts)) != 1:
                    results.append((outer_m, outer, gap, "nonuniform-context", None))
                    continue
                prefix, suffix, infinity, sign = contexts[0]
                rank = outer_m + 4
                old_deck = set().union(*(vertex_deck_from_q(q, rank) for q in old_qs))
                successes = []
                for choices in product((0, 1), repeat=5):
                    new_qs = []
                    for i in range(5):
                        local = base_added_forms[i][choices[i]]
                        mapped = tuple(
                            gap + x if sign == 1 else gap + 9 - x for x in local
                        )
                        new_qs.append(prefix + mapped + suffix + (infinity,))
                    new_deck = set().union(
                        *(vertex_deck_from_q(q, rank) for q in new_qs)
                    )
                    if new_deck == old_deck:
                        old_lower = set().union(
                            *(lower_deck_from_q(q, rank) for q in old_qs)
                        )
                        new_lower = set().union(
                            *(lower_deck_from_q(q, rank) for q in new_qs)
                        )
                        successes.append(
                            (choices, len(old_lower - new_lower), len(new_lower - old_lower))
                        )
                results.append((outer_m, outer, gap, "ok", successes))

    summary = {}
    for outer_m, outer, gap, status, successes in results:
        key = (outer_m, status, bool(successes))
        summary[key] = summary.get(key, 0) + 1
        if successes:
            print(
                "SUCCESS",
                {"outer_m": outer_m, "outer": outer, "gap": gap, "solutions": successes[:4], "number": len(successes)},
                flush=True,
            )
    print("summary", sorted(summary.items()), flush=True)

    # A weaker bundled test: replace all five D-block rows simultaneously for
    # every outer root, allowing cancellations between different outer roots.
    for outer_m in range(1, max_outer + 1):
        for side in ("prefix", "suffix"):
            outers = list(dyck_words(outer_m))
            rank = outer_m + 4
            infinity = 2 * rank + 1
            old_rows = []
            candidates = []
            groups = []
            for outer_index, outer in enumerate(outers):
                for word, _ in base_old:
                    expanded = word + outer if side == "prefix" else outer + word
                    old_rows.append(tuple(rho(expanded) + [infinity]))
                outside = tuple(8 + x for x in rho(outer))
                for i in range(5):
                    group = []
                    for choice in (0, 1):
                        local = base_added_forms[i][choice]
                        if side == "prefix":
                            q = local + outside + (infinity,)
                        else:
                            shifted_local = tuple(2 * outer_m + x for x in local)
                            q = tuple(rho(outer)) + shifted_local + (infinity,)
                        group.append(len(candidates))
                        candidates.append(vertex_deck_from_q(q, rank))
                    groups.append(group)
            universe = set().union(*(vertex_deck_from_q(q, rank) for q in old_rows))
            assert len(universe) == len(old_rows) * (2 * rank + 1)
            model = cp_model.CpModel()
            take = [model.new_bool_var(f"x_{i}") for i in range(len(candidates))]
            for group in groups:
                model.add(sum(take[i] for i in group) == 1)
            by_target = {x: [] for x in universe}
            outside_candidate = 0
            for i, deck in enumerate(candidates):
                if not deck <= universe:
                    model.add(take[i] == 0)
                    outside_candidate += 1
                    continue
                for x in deck:
                    by_target[x].append(i)
            for support in by_target.values():
                model.add(sum(take[i] for i in support) == 1)
            solver = cp_model.CpSolver()
            solver.parameters.max_time_in_seconds = 120
            solver.parameters.num_search_workers = 32
            status = solver.solve(model)
            print(
                "BUNDLED",
                {
                    "outer_m": outer_m,
                    "side": side,
                    "outer_roots": len(outers),
                    "old_rows": len(old_rows),
                    "candidates_forced_out": outside_candidate,
                    "status": solver.status_name(status),
                },
                flush=True,
            )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-outer", type=int, default=4)
    args = parser.parse_args()
    main(args.max_outer)
