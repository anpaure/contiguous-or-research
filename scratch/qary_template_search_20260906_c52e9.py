"""Finite q-ary chain-pair covers, checked on actual grid points."""

import argparse
from itertools import combinations, permutations, product
from functools import lru_cache

from qary_tube_compiler_20260906_c52e9 import tube_width_factor


def maximal_chains(q, d):
    def extend(chain):
        last = chain[-1]
        if all(x == q - 1 for x in last):
            yield tuple(chain)
            return
        for i in range(d):
            if last[i] < q - 1:
                following = list(last)
                following[i] += 1
                yield from extend(chain + [tuple(following)])
    yield from extend([(0,) * d])


def grid_chains(q, dimension, kind):
    if kind == "maximal":
        yield from maximal_chains(q, dimension)
        return

    def extend(chain):
        yield tuple(chain)
        last = chain[-1]
        for following in product(*(range(x, q) for x in last)):
            if following == last:
                continue
            if kind == "saturated" and sum(following) != sum(last) + 1:
                continue
            yield from extend(chain + [following])
    for start in product(range(q), repeat=dimension):
        yield from extend([start])


def catalogue(q, kind, dimension=4, all_splits=False, tube_weights=False):
    assert dimension % 2 == 0 and dimension >= 4
    assert dimension == 4 or kind == "maximal"
    shore = dimension // 2
    points = list(product(range(q), repeat=dimension))
    index = {p: i for i, p in enumerate(points)}
    @lru_cache(None)
    def chains(size):
        return list(grid_chains(q, size, kind))

    items = {}
    for size in (range(1, dimension) if all_splits else (shore,)):
        for tail in combinations(range(1, dimension), size - 1):
            left = (0,) + tail
            right = tuple(i for i in range(dimension) if i not in left)
            for c, d in product(chains(size), chains(dimension - size)):
                mask = 0
                for x, y in product(c, d):
                    p = [0] * dimension
                    for i, z in zip(left + right, x + y):
                        p[i] = z
                    mask |= 1 << index[tuple(p)]
                cost = (len(c) * tube_width_factor(d) + len(d) * tube_width_factor(c)
                        if tube_weights else len(c) + len(d))
                if mask not in items or cost < items[mask][0]:
                    items[mask] = (cost, left, c, right, d)
    return points, items


def exact_full_search(q, count):
    points, items = catalogue(q, "maximal")
    keys = list(items)
    full = (1 << len(points)) - 1
    by_point = [[j for j, mask in enumerate(keys) if mask & (1 << i)]
                for i in range(len(points))]
    nodes = 0

    def search(remaining, available, selected):
        nonlocal nodes
        nodes += 1
        if remaining == 0:
            return selected
        slots = count - len(selected)
        if slots == 0:
            return None
        if sum(sorted(((keys[j] & remaining).bit_count() for j in available),
                      reverse=True)[:slots]) < remaining.bit_count():
            return None
        uncovered = [i for i in range(len(points)) if remaining & (1 << i)]
        candidates = min(([j for j in by_point[i] if j in available] for i in uncovered),
                         key=len)
        if not candidates:
            return None
        candidates.sort(key=lambda j: (keys[j] & remaining).bit_count(), reverse=True)
        allowed = available.copy()
        for j in candidates:
            allowed.remove(j)
            found = search(remaining & ~keys[j], allowed, selected + [j])
            if found is not None:
                return found
        return None

    result = search(full, set(range(len(keys))), [])
    print(f"q={q} full-chain products={len(keys)} bound={count} nodes={nodes}")
    if result is None:
        print("No cover in this finite maximal-chain catalogue.")
        return
    union = 0
    for j in result:
        union |= keys[j]
    assert union == full
    print(f"CHECKED cover: cost={sum(items[keys[j]][0] for j in result)}")
    for j in result:
        print(items[keys[j]])


def optimization(q, kind, target, seconds, dimension, all_splits, tube_weights):
    import numpy as np
    from scipy.optimize import Bounds, LinearConstraint, linprog, milp
    from scipy.sparse import csc_matrix

    points, items = catalogue(q, kind, dimension, all_splits, tube_weights)
    keys = list(items)
    costs = np.array([items[m][0] for m in keys], dtype=float)
    rows, cols = [], []
    for j, mask in enumerate(keys):
        while mask:
            bit = mask & -mask
            rows.append(bit.bit_length() - 1)
            cols.append(j)
            mask ^= bit
    matrix = csc_matrix((np.ones(len(rows)), (rows, cols)), shape=(len(points), len(keys)))
    print(f"q={q} d={dimension} kind={kind} all_splits={all_splits} "
          f"points={len(points)} columns={len(keys)}", flush=True)
    lp = linprog(costs, A_ub=-matrix, b_ub=-np.ones(len(points)),
                 bounds=(0, None), method="highs")
    print(f"LP success={lp.success} cost={lp.fun}", flush=True)
    if target is None:
        return
    if lp.fun > target + 1e-7:
        print("Numerical LP exceeds target.")
        return
    gap = target - lp.fun
    retained = [j for j, reduced in enumerate(lp.lower.marginals) if reduced <= gap + 1e-7]
    costs = costs[retained]
    keys = [keys[j] for j in retained]
    matrix = matrix[:, retained]
    print(f"Retained {len(keys)} reduced-cost columns for target {target}", flush=True)
    result = milp(costs, integrality=np.ones(len(keys)), bounds=Bounds(0, 1),
                  constraints=[LinearConstraint(matrix, 1, np.inf),
                               LinearConstraint(costs, -np.inf, target)],
                  options={"time_limit": seconds, "mip_rel_gap": 0})
    print(f"MILP {result.message}; cost={result.fun}", flush=True)
    if result.x is None:
        return
    assert np.max(np.abs(result.x - np.rint(result.x))) < 1e-5
    selected = [j for j, x in enumerate(result.x) if x > 0.5]
    union = 0
    inventory = [0] * len(points)
    for j in selected:
        union |= keys[j]
        for i in range(len(points)):
            inventory[i] += bool(keys[j] & (1 << i))
    assert union == (1 << len(points)) - 1
    exact_cost = sum(items[keys[j]][0] for j in selected)
    assert exact_cost <= target
    print(f"CHECKED cost={exact_cost}, products={len(selected)}, "
          f"excess={sum(inventory)-len(points)}")
    for j in selected:
        print(items[keys[j]])


def symmetric_pricing(q, dimension, rounds, all_splits, integer_seconds, tube_weights):
    """Price every chain pair, using the coordinate-symmetric quotient LP."""
    import numpy as np
    from scipy.optimize import linprog

    assert dimension % 2 == 0
    assert not tube_weights or ((q, dimension) == (3, 6) and not integer_seconds)
    half = dimension // 2
    points = list(product(range(q), repeat=dimension))

    def orbit(p):
        count = tuple(p.count(i) for i in range(q))
        return min(count, count[::-1])

    types = sorted({orbit(p) for p in points})
    type_index = {p: i for i, p in enumerate(types)}
    populations = np.zeros(len(types))
    for p in points:
        populations[type_index[orbit(p)]] += 1
    structures = []
    for size in (range(1, half + 1) if all_splits else (half,)):
        left = list(product(range(q), repeat=size))
        right = list(product(range(q), repeat=dimension - size))
        left_index = {p: i for i, p in enumerate(left)}
        chains = [tuple(left_index[p] for p in c) for c in grid_chains(q, size, "all")]
        incidence = np.zeros((len(chains), len(left)))
        for i, chain in enumerate(chains):
            incidence[i, list(chain)] = 1
        lengths = incidence.sum(axis=1)
        cell_type = np.array([[type_index[orbit(x + y)] for y in right] for x in left])
        predecessors = [[j for j, y in enumerate(right[:i]) if all(a <= b for a, b in zip(y, x))]
                        for i, x in enumerate(right)]
        structures.append((left, right, chains, incidence, lengths, cell_type, predecessors))
    # Singleton columns make the initial quotient feasible.
    columns = {tuple(int(i == j) for i in range(len(types))): (2, None)
               for j in range(len(types))}
    print(f"Pricing q={q} d={dimension}: {len(types)} target orbits, "
          f"shore catalogues={[len(s[2]) for s in structures]}", flush=True)
    for step in range(rounds):
        keys = list(columns)
        matrix = np.array(keys, dtype=float).T
        costs = np.array([columns[key][0] for key in keys], dtype=float)
        lp = linprog(costs, A_ub=-matrix, b_ub=-populations,
                     bounds=(0, None), method="highs")
        assert lp.success
        dual = -lp.ineqlin.marginals
        most, candidates = 0.0, []
        for left, right, chains, incidence, lengths, cell_type, predecessors in structures:
            if tube_weights and len(left[0]) == len(right[0]) == 3:
                assert q <= 3
                factors = np.array([float(tube_width_factor(tuple(left[x] for x in c)))
                                    for c in chains])
                weighted = incidence @ dual[cell_type]
                for start in range(0, len(chains), 256):
                    stop = min(len(chains), start + 256)
                    scores = (weighted @ incidence[start:stop].T
                              - lengths[:, None] * factors[None, start:stop]
                              - factors[:, None] * lengths[None, start:stop])
                    most = max(most, float(np.max(scores)))
                    flat = scores.ravel()
                    take = min(150, len(flat))
                    for location in np.argpartition(-flat, take - 1)[:take]:
                        if flat[location] < 1e-7:
                            continue
                        ci, dj = divmod(int(location), stop - start)
                        c, d = chains[ci], chains[start + dj]
                        census = [0] * len(types)
                        for x, y in product(c, d):
                            census[cell_type[x, y]] += 1
                        cc, dd = tuple(left[x] for x in c), tuple(right[y] for y in d)
                        exact_cost = len(c) * tube_width_factor(dd) + len(d) * tube_width_factor(cc)
                        candidates.append((tuple(census), exact_cost, (cc, dd)))
                continue
            dp = incidence @ dual[cell_type] - 1
            for i, pred in enumerate(predecessors):
                if pred:
                    dp[:, i] += np.maximum(0, np.max(dp[:, pred], axis=1))
            end = np.argmax(dp, axis=1)
            reduced = dp[np.arange(len(chains)), end] - lengths
            most = max(most, float(np.max(reduced)))
            for j in np.argsort(-reduced)[: min(len(chains), 1000)]:
                if reduced[j] < 1e-7:
                    break
                d = []
                i = int(end[j])
                while True:
                    d.append(i)
                    pred = predecessors[i]
                    if not pred:
                        break
                    previous = max(pred, key=lambda x: dp[j, x])
                    if dp[j, previous] <= 0:
                        break
                    i = previous
                d.reverse()
                c = chains[j]
                census = [0] * len(types)
                for x, y in product(c, d):
                    census[cell_type[x, y]] += 1
                candidates.append((tuple(census), len(c) + len(d),
                                   (tuple(left[x] for x in c), tuple(right[y] for y in d))))
        print(f"  step={step} columns={len(columns)} LP={lp.fun:.12f} "
              f"max_violation={most:.9g}", flush=True)
        if most < 1e-7:
            print("All chain pairs priced. Numerical optimum and symmetric dual:")
            print([(kind, float(value)) for kind, value in zip(types, dual)])
            print("Positive quotient columns:")
            for key, weight in zip(keys, lp.x):
                if weight > 1e-7:
                    print(float(weight), columns[key])
            if integer_seconds:
                orbit_integer_cover(q, dimension,
                                    [columns[key][1] for key, weight in zip(keys, lp.x)
                                     if weight > 1e-7 and columns[key][1] is not None],
                                    integer_seconds)
            return
        added = 0
        for key, cost, pair in candidates:
            old = columns.get(key)
            if old is None or cost < old[0]:
                columns[key] = (cost, pair)
                added += 1
        assert added
    print("Round limit; no optimum claim.")


def orbit_integer_cover(q, dimension, seeds, seconds):
    import highspy
    import numpy as np
    from scipy.sparse import csc_matrix

    assert (q, dimension) == (4, 6)
    full = (1 << (q ** dimension)) - 1
    items = {}

    def insert(left, c, right, d):
        mask = 0
        for x, y in product(c, d):
            point = [0] * dimension
            for i, value in zip(left + right, x + y):
                point[i] = value
            index = 0
            for value in point:
                index = q * index + value
            mask |= 1 << index
        cost = len(c) + len(d)
        if mask not in items or cost < items[mask][0]:
            items[mask] = (cost, tuple(left), tuple(c), tuple(right), tuple(d))
        return mask

    for c, d in seeds:
        for perm in permutations(range(dimension)):
            size = len(c[0])
            for reflected in (False, True):
                cc = tuple(tuple(q - 1 - x for x in p) for p in reversed(c)) if reflected else c
                dd = tuple(tuple(q - 1 - x for x in p) for p in reversed(d)) if reflected else d
                insert(perm[:size], cc, perm[size:], dd)
    staircase = [tuple((x,) for x in range(4))]
    for _ in range(2):
        following = []
        for c in staircase:
            for j in range(2):
                last = len(c) - 1 - j
                following.append(tuple([c[i] + (j,) for i in range(last + 1)]
                                       + [c[last] + (y,) for y in range(j + 1, 4)]))
        staircase = following
    rows6 = [((0, 1, 2), (3, 4, 5)), ((1, 2, 4), (3, 5, 0)),
             ((1, 4, 3), (5, 2, 0)), ((0, 4, 1), (2, 3, 5)),
             ((4, 2, 3), (5, 0, 1))]
    baseline = []
    union = 0
    for left, right in rows6:
        for c, d in product(staircase, repeat=2):
            mask = insert(left, c, right, d)
            baseline.append(mask)
            union |= mask
    assert union == full
    assert sum(items[mask][0] for mask in baseline) == 1280
    keys = list(items)
    if seconds < 0:
        key_index = {key: i for i, key in enumerate(keys)}
        by_point = [0] * (q ** dimension)
        costs = [items[key][0] for key in keys]
        for j, key in enumerate(keys):
            while key:
                bit = key & -key
                by_point[bit.bit_length() - 1] |= 1 << j
                key ^= bit
        price_masks = [sum(1 << j for j, cost in enumerate(costs) if cost <= limit)
                       for limit in range(41)]
        selected = [key_index[key] for key in baseline]
        moves = 0
        while True:
            owners = [0] * (q ** dimension)
            for j, index in enumerate(selected):
                key = keys[index]
                while key:
                    bit = key & -key
                    owners[bit.bit_length() - 1] |= 1 << j
                    key ^= bit
            private = [0] * len(selected)
            paired = {}
            for p, owner in enumerate(owners):
                if owner.bit_count() == 1:
                    private[owner.bit_length() - 1] |= 1 << p
                elif owner.bit_count() == 2:
                    paired[owner] = paired.get(owner, 0) | (1 << p)
            change = None
            for i, j in combinations(range(len(selected)), 2):
                required = private[i] | private[j] | paired.get((1 << i) | (1 << j), 0)
                budget = costs[selected[i]] + costs[selected[j]]
                bits, positions = required, []
                while bits:
                    bit = bits & -bits
                    positions.append(bit.bit_length() - 1)
                    bits ^= bit
                if not positions:
                    change = (i, j, [])
                    break
                anchor = min(positions, key=lambda p: by_point[p].bit_count())
                first = by_point[anchor]
                while first:
                    bit = first & -first
                    f = bit.bit_length() - 1
                    first ^= bit
                    limit = budget - 1 - costs[f]
                    if limit < 0:
                        continue
                    remaining = required & ~keys[f]
                    if not remaining:
                        change = (i, j, [f])
                        break
                    possible = price_masks[min(40, limit)]
                    while remaining and possible:
                        bit = remaining & -remaining
                        possible &= by_point[bit.bit_length() - 1]
                        remaining ^= bit
                    if possible:
                        g = (possible & -possible).bit_length() - 1
                        change = (i, j, [f, g])
                        break
                if change is not None:
                    break
            if change is None:
                break
            i, j, replacement = change
            selected = [x for h, x in enumerate(selected) if h not in (i, j)] + replacement
            moves += 1
            print(f"Exact two-exchange move {moves}: cost={sum(costs[x] for x in selected)}", flush=True)
        union = 0
        for index in selected:
            union |= keys[index]
        assert union == full
        total = sum(costs[x] for x in selected)
        print(f"CHECKED two-exchange cover: cost={total}, pieces={len(selected)}, moves={moves}")
        if total < 1280:
            for index in selected:
                print(items[keys[index]])
        return
    rows, cols = [], []
    for j, mask in enumerate(keys):
        while mask:
            bit = mask & -mask
            rows.append(bit.bit_length() - 1)
            cols.append(j)
            mask ^= bit
    matrix = csc_matrix((np.ones(len(rows)), (rows, cols)), shape=(q ** dimension, len(keys)))
    lp = highspy.HighsLp()
    lp.num_col_ = len(keys)
    lp.num_row_ = q ** dimension
    lp.col_cost_ = np.array([items[key][0] for key in keys], dtype=float)
    lp.col_lower_ = np.zeros(len(keys))
    lp.col_upper_ = np.ones(len(keys))
    lp.row_lower_ = np.ones(q ** dimension)
    lp.row_upper_ = np.full(q ** dimension, highspy.kHighsInf)
    lp.a_matrix_.format_ = highspy.MatrixFormat.kColwise
    lp.a_matrix_.start_ = matrix.indptr
    lp.a_matrix_.index_ = matrix.indices
    lp.a_matrix_.value_ = matrix.data
    lp.integrality_ = [highspy.HighsVarType.kInteger] * len(keys)
    solver = highspy.Highs()
    solver.setOptionValue("time_limit", float(seconds))
    solver.setOptionValue("mip_rel_gap", 0.0)
    solver.setOptionValue("threads", 2)
    solver.setOptionValue("presolve", "off")
    solver.setOptionValue("output_flag", False)
    solver.passModel(lp)
    baseline_set = set(baseline)
    solution = highspy.HighsSolution()
    solution.col_value = [float(key in baseline_set) for key in keys]
    solution.value_valid = True
    solver.setSolution(solution)
    print(f"Integral orbit pool: {len(keys)} rectangles, baseline=1280", flush=True)
    solver.run()
    info = solver.getInfo()
    print(f"HiGHS: {solver.modelStatusToString(solver.getModelStatus())}; "
          f"cost={info.objective_function_value}, lower={info.mip_dual_bound}", flush=True)
    values = solver.getSolution().col_value
    selected = [i for i, value in enumerate(values) if value > 0.5]
    assert all(abs(value - round(value)) < 1e-5 for value in values)
    union = 0
    for i in selected:
        union |= keys[i]
    assert union == full
    cost = sum(items[keys[i]][0] for i in selected)
    print(f"CHECKED integral cover cost={cost}, pieces={len(selected)}")
    if cost < 1280:
        for i in selected:
            print(items[keys[i]])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("q", type=int)
    parser.add_argument("--kind", choices=("maximal", "saturated", "all"), default="maximal")
    parser.add_argument("--full-count", type=int)
    parser.add_argument("--target", type=int)
    parser.add_argument("--seconds", type=float, default=30)
    parser.add_argument("--dimension", type=int, default=4)
    parser.add_argument("--all-splits", action="store_true")
    parser.add_argument("--price", action="store_true")
    parser.add_argument("--rounds", type=int, default=40)
    parser.add_argument("--integer-seconds", type=float, default=0)
    parser.add_argument("--tube-weights", action="store_true")
    args = parser.parse_args()
    if args.price:
        symmetric_pricing(args.q, args.dimension, args.rounds, args.all_splits, args.integer_seconds,
                          args.tube_weights)
    elif args.full_count:
        exact_full_search(args.q, args.full_count)
    else:
        optimization(args.q, args.kind, args.target, args.seconds, args.dimension, args.all_splits,
                     args.tube_weights)
