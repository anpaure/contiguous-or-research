#!/usr/bin/env python3
"""Find a smallest row trade from the canonical b=9 MSW factor to M1=0."""

from __future__ import annotations

import argparse
from itertools import combinations, permutations

from ortools.sat.python import cp_model


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
    height = 0
    close = None
    for i, bit in enumerate(word):
        height += 1 if bit == "1" else -1
        if height == 0:
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


def msw_row(word: str):
    m = len(word) // 2
    n = 2 * m + 1
    q = [x - 1 for x in rho(word)] + [2 * m]
    return canonical(tuple(q[(-1 - 2 * j) % n] for j in range(n)))


def windows(order, k):
    b = len(order)
    return tuple(
        sorted(
            sum(1 << order[(i + j) % b] for j in range(k))
            for i in range(b)
        )
    )


def ribbon_map(order, k):
    b = len(order)
    return {
        sum(1 << order[(i + j) % b] for j in range(k)):
        sum(1 << order[(i + j) % b] for j in range(k - 1))
        for i in range(b)
    }


def main(
    seconds: float,
    workers: int,
    max_shadow_multiplicity: int | None,
    optimize_ribbon: bool,
    joint_ribbon: bool,
):
    b, m = 9, 4
    rank4 = [sum(1 << q for q in c) for c in combinations(range(b), m)]
    rank3 = [sum(1 << q for q in c) for c in combinations(range(b), m - 1)]
    id4 = {x: i for i, x in enumerate(rank4)}
    id3 = {x: i for i, x in enumerate(rank3)}

    rows = []
    for tail in permutations(range(1, b)):
        order = (0,) + tail
        if order[1] > order[-1]:
            continue
        rows.append((order, tuple(id4[x] for x in windows(order, m)), tuple(id3[x] for x in windows(order, m - 1))))
    assert len(rows) == 20160
    row_id = {canonical(order): i for i, (order, _, _) in enumerate(rows)}
    msw = {row_id[msw_row(word)] for word in dyck_words(m)}
    assert len(msw) == 14

    by4 = [[] for _ in rank4]
    by3 = [[] for _ in rank3]
    for i, (_, ww4, ww3) in enumerate(rows):
        for x in ww4:
            by4[x].append(i)
        for x in ww3:
            by3[x].append(i)

    model = cp_model.CpModel()
    take = [model.new_bool_var(f"take_{i}") for i in range(len(rows))]
    orientation = None
    ribbon_score = None
    if optimize_ribbon or joint_ribbon:
        orientation = [
            (model.new_bool_var(f"ori0_{i}"), model.new_bool_var(f"ori1_{i}"))
            for i in range(len(rows))
        ]
        for i in range(len(rows)):
            model.add(take[i] == orientation[i][0] + orientation[i][1])
    for support in by4:
        model.add(sum(take[i] for i in support) == 1)
    for support in by3:
        model.add(sum(take[i] for i in support) >= 1)
        if max_shadow_multiplicity is not None:
            model.add(sum(take[i] for i in support) <= max_shadow_multiplicity)
    old_orientation = None
    if optimize_ribbon and not joint_ribbon:
        reference = {}
        for i in msw:
            reference.update(ribbon_map(rows[i][0], m))
        assert len(reference) == len(rank4)
        scores = []
        for i, (order, _, _) in enumerate(rows):
            for bit, oriented in enumerate((order, tuple(reversed(order)))):
                score = sum(reference[x] == y for x, y in ribbon_map(oriented, m).items())
                scores.append(score * orientation[i][bit])
        ribbon_score = sum(scores)
        model.maximize(1000 * sum(take[i] for i in msw) + ribbon_score)
    elif joint_ribbon:
        old_orientation = [
            (model.new_bool_var(f"oldori0_{j}"), model.new_bool_var(f"oldori1_{j}"))
            for j in range(len(msw))
        ]
        msw_list = sorted(msw)
        old_position = {row: j for j, row in enumerate(msw_list)}
        owner = {}
        old_ribbon = {}
        for j, row_id_value in enumerate(msw_list):
            model.add(sum(old_orientation[j]) == 1)
            order = rows[row_id_value][0]
            old_ribbon[(j, 0)] = ribbon_map(order, m)
            old_ribbon[(j, 1)] = ribbon_map(tuple(reversed(order)), m)
            for x in rows[row_id_value][1]:
                owner[x] = j
        assert len(owner) == len(rank4)
        terms = []
        for i, (order, ww4, _) in enumerate(rows):
            for bit, oriented in enumerate((order, tuple(reversed(order)))):
                attached = ribbon_map(oriented, m)
                counts = {}
                for x in ww4:
                    j = owner[x]
                    mask = rank4[x]
                    for old_bit in (0, 1):
                        if attached[mask] == old_ribbon[(j, old_bit)][mask]:
                            counts[(j, old_bit)] = counts.get((j, old_bit), 0) + 1
                for (j, old_bit), coefficient in counts.items():
                    z = model.new_bool_var(f"match_{i}_{bit}_{j}_{old_bit}")
                    model.add(z <= orientation[i][bit])
                    model.add(z <= old_orientation[j][old_bit])
                    model.add(z >= orientation[i][bit] + old_orientation[j][old_bit] - 1)
                    terms.append(coefficient * z)
        ribbon_score = sum(terms)
        model.maximize(1000 * sum(take[i] for i in msw) + ribbon_score)
    else:
        model.maximize(sum(take[i] for i in msw))

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = seconds
    solver.parameters.num_search_workers = workers
    solver.parameters.log_search_progress = False
    status = solver.solve(model)
    chosen = [i for i, v in enumerate(take) if solver.value(v)] if status in (cp_model.OPTIMAL, cp_model.FEASIBLE) else []
    kept = sorted(msw & set(chosen))
    removed = sorted(msw - set(chosen))
    added = sorted(set(chosen) - msw)
    realized_ribbon_score = solver.value(ribbon_score) if chosen and ribbon_score is not None else None
    print(
        {
            "status": solver.status_name(status),
            "objective_kept": len(kept) if chosen else None,
            "solver_objective": solver.objective_value if chosen else None,
            "best_bound": solver.best_objective_bound,
            "wall": solver.wall_time,
            "kept": len(kept),
            "removed": len(removed),
            "added": len(added),
            "ribbon_score": realized_ribbon_score,
        },
        flush=True,
    )
    for label, indices in (("REMOVE", removed), ("ADD", added)):
        for i in indices:
            bit = None
            if orientation is not None and i in chosen:
                bit = int(solver.value(orientation[i][1]))
            print(label, " ".join(str(q + 1) for q in rows[i][0]), "orientation", bit, flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--seconds", type=float, default=600)
    parser.add_argument("--workers", type=int, default=64)
    parser.add_argument("--max-shadow-multiplicity", type=int)
    parser.add_argument("--optimize-ribbon", action="store_true")
    parser.add_argument("--joint-ribbon", action="store_true")
    args = parser.parse_args()
    main(
        args.seconds,
        args.workers,
        args.max_shadow_multiplicity,
        args.optimize_ribbon,
        args.joint_ribbon,
    )
