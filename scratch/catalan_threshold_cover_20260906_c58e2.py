"""All-rank threshold-cover audit and an exact finite-column solver.

The archived parameter-four path body is from Proposition 3.4 of
MATH_THEOREM_CATALAN_INDEPENDENT_FILLER_GUARD_FACTORIZATION_20260731.md.
Its previous certificate covered the three central ranks, not all ranks.
"""

import argparse
from collections import Counter
from fractions import Fraction
from itertools import permutations, product
from math import comb, factorial
from random import Random


ARCHIVED4 = (
    (15, 30, 60, 120, 240),
    (29, 89, 90, 114, 226),
    (92, 86, 54, 51, 163),
    (58, 27, 147, 135, 197),
    (23, 71, 78, 204, 232),
    (53, 45, 108, 106, 202),
    (102, 101, 85, 149, 153),
    (77, 141, 142, 170, 178),
    (39, 166, 150, 154, 216),
    (99, 195, 210, 212, 156),
    (116, 180, 184, 169, 139),
    (46, 43, 75, 201, 209),
    (57, 105, 225, 228, 198),
    (83, 113, 177, 165, 172),
)

# Complete all-rank cover, found with at least eleven archived families retained.
# It actually retains twelve: two rail-order changes repair the two holes.
COVER4 = (
    ((0, 4, 6, 1), (5, 7, 2, 3)),
    ((0, 4, 7, 3), (2, 6, 5, 1)),
    ((0, 6, 7, 4), (3, 1, 5, 2)),
    ((0, 7, 2, 6), (1, 4, 3, 5)),
    ((1, 5, 0, 7), (4, 2, 6, 3)),
    ((1, 6, 0, 5), (7, 4, 3, 2)),
    ((2, 1, 0, 4), (6, 3, 7, 5)),
    ((2, 1, 5, 0), (7, 4, 6, 3)),
    ((3, 2, 0, 6), (7, 1, 5, 4)),
    ((3, 2, 1, 0), (4, 5, 6, 7)),
    ((3, 6, 1, 7), (5, 2, 0, 4)),
    ((4, 3, 0, 2), (6, 1, 5, 7)),
    ((5, 0, 3, 4), (6, 7, 2, 1)),
    ((5, 4, 2, 6), (7, 3, 0, 1)),
)


def path_to_pair(path, l):
    leaving, entering = [], []
    for a, b in zip(path, path[1:]):
        x, y = a & ~b, b & ~a
        assert x.bit_count() == y.bit_count() == 1
        leaving.append(x.bit_length() - 1)
        entering.append(y.bit_length() - 1)
    pair = (tuple(reversed(leaving)), tuple(entering))
    assert sorted(pair[0] + pair[1]) == list(range(2 * l))
    assert path[-1] == ((1 << (2 * l)) - 1) ^ path[0]
    assert len(path) == l + 1 and all(x.bit_count() == l for x in path)
    return min(pair, pair[::-1])


def pair_support(pair):
    prefixes = []
    for order in pair:
        current, values = 0, [0]
        for bit in order:
            current |= 1 << bit
            values.append(current)
        prefixes.append(values)
    return frozenset(x | y for x in prefixes[0] for y in prefixes[1])


def verify(l, pairs, label):
    assert len(pairs) == comb(2 * l, l) // (l + 1)
    counts = Counter()
    for pair in pairs:
        assert len(pair) == 2 and all(len(p) == l for p in pair)
        assert sorted(pair[0] + pair[1]) == list(range(2 * l))
        support = pair_support(pair)
        assert len(support) == (l + 1) ** 2
        # An independent membership definition checks every binary pattern.
        alternate = {x for x in range(1 << (2 * l))
                     if all(all((x >> a & 1) >= (x >> b & 1)
                                for a, b in zip(order, order[1:])) for order in pair)}
        assert alternate == support
        counts.update(support)
    missing = [x for x in range(1 << (2 * l)) if not counts[x]]
    ranks = [sum(x.bit_count() == r for x in missing) for r in range(2 * l + 1)]
    hist = [dict(sorted(Counter(counts[x] for x in range(1 << (2 * l))
                               if x.bit_count() == r).items())) for r in range(2 * l + 1)]
    assert all(counts[x] == 1 for x in range(1 << (2 * l))
               if x.bit_count() == l)
    print(label, {"l": l, "families": len(pairs), "missing_count": len(missing),
                  "missing_sample": missing[:24],
                  "rank_holes": ranks, "load_histograms": hist}, flush=True)
    return missing


def dyck_words(l):
    def visit(word, up, down):
        if up == down == l:
            yield word
        if up < l:
            yield from visit(word + (1,), up + 1, down)
        if down < up:
            yield from visit(word + (0,), up, down + 1)
    yield from visit((), 0, 0)


def msw_permutation(word):
    if not word:
        return ()
    height = 0
    for i, bit in enumerate(word):
        height += 2 * bit - 1
        if height == 0:
            break
    inside, after = word[1:i], word[i + 1:]
    mirrored = tuple(1 - x for x in reversed(inside))
    return ((i,) + tuple(i - 1 - j for j in msw_permutation(mirrored))
            + (0,) + tuple(i + 1 + j for j in msw_permutation(after)))


def canonical_pairs(l):
    result = []
    for word in dyck_words(l):
        order = msw_permutation(word)
        state = sum(x << i for i, x in enumerate(word))
        path = [state]
        for j, bit in enumerate(order):
            state ^= 1 << bit
            if j % 2:
                path.append(state)
        result.append(path_to_pair(path, l))
    return result


def hereditary_msw_check():
    cases = 0
    for l in range(3, 9):
        for tail in dyck_words(l - 3):
            paths = []
            for prefix in ((1, 1, 1, 0, 0, 0), (1, 1, 0, 1, 0, 0)):
                word = prefix + tail
                state = sum(x << i for i, x in enumerate(word))
                path = [state]
                for j, bit in enumerate(msw_permutation(word)):
                    state ^= 1 << bit
                    if j % 2:
                        path.append(state)
                paths.append(path)
            spectator = sum(x << (6 + i) for i, x in enumerate(tail))
            assert paths[0][:3] == [7 | spectator, 37 | spectator, 41 | spectator]
            assert paths[1][:3] == [11 | spectator, 35 | spectator, 49 | spectator]
            assert paths[0][1] & paths[0][2] == paths[1][1] & paths[1][2] == 33 | spectator
            cases += 1
    print("HEREDITARY_MSW_COLLISION_PASS", cases, flush=True)


def menu(l):
    result = []
    for order in permutations(range(2 * l)):
        left, right = order[:l], order[l:]
        if left > right:
            continue
        pair = left, right
        result.append((pair, pair_support(pair)))
    assert len(result) == factorial(2 * l) // 2
    return result


def noncrossing_matchings(vertices):
    if not vertices:
        yield ()
        return
    for j in range(1, len(vertices), 2):
        for inside in noncrossing_matchings(vertices[1:j]):
            for outside in noncrossing_matchings(vertices[j + 1:]):
                yield ((vertices[0], vertices[j]),) + inside + outside


def noncrossing_menu(l):
    result, owners = [], []
    for owner, matching in enumerate(noncrossing_matchings(tuple(range(2 * l)))):
        for orientation in product((0, 1), repeat=l):
            for order in permutations(range(l)):
                leaving = tuple(matching[i][orientation[i]] for i in order)
                entering = tuple(matching[i][1 - orientation[i]] for i in order)
                pair = tuple(reversed(leaving)), entering
                if pair[0] > pair[1]:
                    continue
                result.append((pair, pair_support(pair)))
                owners.append(owner)
    assert len(result) == comb(2 * l, l) // (l + 1) * 2 ** (l - 1) * factorial(l)
    assert len({pair for pair, _ in result}) == len(result)
    return result, owners


def two_row_trade_checks():
    rng = Random(906584)
    for l in range(2, 8):
        for _ in range(20):
            f = list(range(4, l + 2))
            z = list(range(l + 2, 2 * l))
            ff, zz = f[:], z[:]
            rng.shuffle(f)
            rng.shuffle(z)
            rng.shuffle(ff)
            rng.shuffle(zz)
            f, z, ff, zz = map(tuple, (f, z, ff, zz))
            old = (((0, 1) + f, z + (2, 3)), ((3, 0) + ff, zz + (1, 2)))
            new = (((1, 0) + f, z + (3, 2)), ((0, 3) + ff, zz + (2, 1)))
            a = Counter(x for pair in old for x in pair_support(pair)
                        if abs(x.bit_count() - l) <= 1)
            b = Counter(x for pair in new for x in pair_support(pair)
                        if abs(x.bit_count() - l) <= 1)
            assert a == b
    print("GENERAL_TWO_ROW_TRADE_PASS", 120, flush=True)


def cyclic_eight():
    def shift(pair):
        following = tuple(tuple((x + 1) % 7 if x < 7 else 7 for x in order)
                          for order in pair)
        return min(following, following[::-1])

    columns = menu(4)
    support = dict(columns)
    seen, banks = set(), []
    central = sum(1 << x for x in range(256) if 3 <= x.bit_count() <= 5)
    full = (1 << 256) - 1
    for pair, _ in columns:
        if pair in seen:
            continue
        orbit, current = [], pair
        while current not in orbit:
            orbit.append(current)
            seen.add(current)
            current = shift(current)
        assert len(orbit) == 7
        count = Counter(x for item in orbit for x in support[item])
        if any(count[x] > 1 for x in count if abs(x.bit_count() - 4) <= 1):
            continue
        mask = sum(1 << x for x in count)
        position = next(order.index(7) + 1 for order in pair if 7 in order)
        banks.append((mask, tuple(orbit), position))
    endings = {}
    for mask, orbit, position in banks:
        if position == 4:
            endings.setdefault(mask & central, []).append((mask, orbit))
    tested = 0
    for mask, orbit, position in banks:
        if position != 1:
            continue
        for other, rest in endings.get(central ^ (mask & central), []):
            tested += 1
            if mask | other == full:
                answer = orbit + rest
                assert not verify(4, answer, "CYCLIC_EIGHT_COMPLETE")
                print("CYCLIC_BASES", (orbit[0], rest[0]), flush=True)
                return
    print("CYCLIC_EIGHT_EXHAUSTED", {"orbits": 2880, "central_simple_banks": len(banks),
                                     "endpoint_compatible_central_pairs": tested}, flush=True)


def noncrossing_fractional(l):
    import numpy as np
    from scipy.optimize import linprog

    columns, owners = noncrossing_menu(l)
    count = comb(2 * l, l) // (l + 1)
    resources = [x for x in range(1 << (2 * l)) if abs(x.bit_count() - l) <= 1]
    index = {x: i for i, x in enumerate(resources)}
    matrix = np.zeros((len(resources) + count, len(columns)))
    footprints = []
    for j, (_, support) in enumerate(columns):
        rows = [index[x] for x in support if x in index]
        rows.append(len(resources) + owners[j])
        footprints.append(rows)
        matrix[rows, j] = 1
    answer = linprog(-np.ones(len(columns)), A_ub=matrix,
                     b_ub=np.ones(len(matrix)), bounds=(0, None), method="highs")
    assert answer.success
    weights = [Fraction(float(-x)).limit_denominator(1000000)
               for x in answer.ineqlin.marginals]
    checked = (all(x >= 0 for x in weights)
               and all(sum(weights[i] for i in rows) >= 1 for rows in footprints))
    print("NONCROSSING_FRACTIONAL", {"l": l, "floating_value": -answer.fun,
                                     "dual_exactly_verified": checked,
                                     "dual_sum": str(sum(weights)), "required": count}, flush=True)
    if checked and sum(weights) < count:
        print("EXACT_DUAL", [(('target', resources[i]) if i < len(resources)
                               else ('pairing', i - len(resources)), str(x))
                              for i, x in enumerate(weights) if x], flush=True)


def solve(l, seconds, freeze, keep, noncrossing):
    from ortools.sat.python import cp_model

    columns, owners = noncrossing_menu(l) if noncrossing else (menu(l), None)
    index = {pair: i for i, (pair, _) in enumerate(columns)}
    count = comb(2 * l, l) // (l + 1)
    model = cp_model.CpModel()
    selected = [model.new_bool_var(f"x{i}") for i in range(len(columns))]
    rows = [[] for _ in range(1 << (2 * l))]
    for i, (_, support) in enumerate(columns):
        for target in support:
            rows[target].append(selected[i])
    model.add(sum(selected) == count)
    if owners is not None:
        for owner in range(count):
            model.add_exactly_one(selected[i] for i, x in enumerate(owners) if x == owner)
    for target, row in enumerate(rows):
        if abs(target.bit_count() - l) <= 1:
            model.add_exactly_one(row)
        else:
            model.add(sum(row) >= 1)
    archived = [path_to_pair(path, 4) for path in ARCHIVED4] if l == 4 and not noncrossing else []
    assert not (freeze or keep) or archived
    for pair in archived[:freeze]:
        model.add(selected[index[pair]] == 1)
    if keep:
        assert archived
        model.add(sum(selected[index[pair]] for pair in archived) >= keep)
    if archived:
        chosen = {index[pair] for pair in archived}
        for i, variable in enumerate(selected):
            model.add_hint(variable, int(i in chosen))
    elif not noncrossing:
        model.add(selected[0] == 1)
    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = seconds
    solver.parameters.num_search_workers = 8
    solver.parameters.random_seed = 906582
    print("MODEL", {"l": l, "columns": len(columns), "targets": len(rows),
                    "families": count, "frozen": freeze, "keep_at_least": keep,
                    "one_per_noncrossing_swap_pairing": noncrossing}, flush=True)
    status = solver.solve(model)
    print("SOLVER_STATUS", solver.status_name(status), "seconds", solver.wall_time, flush=True)
    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        answer = [pair for i, (pair, _) in enumerate(columns) if solver.value(selected[i])]
        assert not verify(l, answer, "EXACT_ALL_RANK_COVER")
        print("WITNESS", answer, flush=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--solve", action="store_true")
    parser.add_argument("--cyclic-eight", action="store_true")
    parser.add_argument("--l", type=int, default=4)
    parser.add_argument("--seconds", type=int, default=120)
    parser.add_argument("--freeze", type=int, default=0)
    parser.add_argument("--keep-at-least", type=int, default=0)
    parser.add_argument("--noncrossing", action="store_true")
    parser.add_argument("--noncrossing-lp", action="store_true")
    args = parser.parse_args()
    if args.noncrossing_lp:
        noncrossing_fractional(args.l)
    elif args.cyclic_eight:
        cyclic_eight()
    elif args.solve:
        solve(args.l, args.seconds, args.freeze, args.keep_at_least, args.noncrossing)
    else:
        pairs = [path_to_pair(path, 4) for path in ARCHIVED4]
        verify(4, pairs, "ARCHIVED4_FULL_INVENTORY")
        print("ARCHIVED4_ORDERS", pairs, flush=True)
        assert not verify(4, COVER4, "CERTIFIED8_ALL_RANK")
        assert len(set(pairs) & set(COVER4)) == 12
        print("TWO_ROW_TRADE", {"old": sorted(set(pairs) - set(COVER4)),
                                "new": sorted(set(COVER4) - set(pairs))}, flush=True)
        before = Counter(x for pair in pairs for x in pair_support(pair))
        after = Counter(x for pair in COVER4 for x in pair_support(pair))
        delta = {x: after[x] - before[x] for x in range(256) if after[x] != before[x]}
        assert delta == {4: 1, 64: -1, 132: 1, 190: -1, 191: -1,
                         192: -1, 215: -1, 219: 1, 246: 1, 251: 1}
        assert all(before[x] >= 2 for x, change in delta.items() if change < 0)
        print("EXACT_TRADE_DELTA", {"delta": delta,
                                    "old_loads_on_removed": {x: before[x] for x in delta
                                                               if delta[x] < 0}}, flush=True)
        two_row_trade_checks()
        hereditary_msw_check()
        for l in range(2, 7):
            verify(l, canonical_pairs(l), "CANONICAL_MSW")
