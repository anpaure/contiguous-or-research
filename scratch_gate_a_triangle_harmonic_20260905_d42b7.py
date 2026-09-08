"""Research checks for triangle surplus and adaptive first harmonics.

No master/index changes. The companion note contains the general proofs.
"""

from fractions import Fraction as F
from itertools import combinations, permutations
from math import comb, factorial
from random import Random


def graph_checks():
    count = 0
    for size in range(1, 6):
        pairs = list(combinations(range(size), 2))
        for bits in range(1 << len(pairs)):
            base = [1 << i for i in range(size)]
            for j, (u, v) in enumerate(pairs):
                if bits & (1 << j):
                    base[u] |= 1 << v
                    base[v] |= 1 << u
            masks = [mask << (copy * size) for copy in range(3) for mask in base]
            z = len(masks)
            closed = [mask.bit_count() for mask in masks]
            total = sum(closed)
            trace = sum(
                (masks[u] & masks[v]).bit_count()
                for u in range(z) for v in range(z) if masks[u] & (1 << v)
            )
            child_totals = []
            for mask in masks:
                kept = ((1 << z) - 1) ^ mask
                child_totals.append(sum(
                    (masks[v] & kept).bit_count()
                    for v in range(z) if kept & (1 << v)
                ))
            assert sum(child_totals) == z * total - 2 * sum(c * c for c in closed) + trace
            mean = F(total, z)
            variance = sum((c - mean) ** 2 for c in closed) / z
            delta = F(max(closed), z)
            beta = F(total, z * z)
            rho = F(1, 31)
            surplus = max(F(0), F(trace, z * total) - 2 * variance / total - rho)
            ratio = sum(
                F(child_totals[i] * z * z, total * (z - closed[i]) ** 2)
                for i in range(z)
            ) / z / (1 + rho)
            assert delta <= F(1, 2)
            assert ratio <= 1 + surplus + 8 * delta * beta
            count += 1
    return count


def catalogue(r):
    b = 2 * r + 1
    layers = [list(combinations(range(b), k)) for k in (r, r - 1)]
    targets = [[sum(1 << i for i in a) for a in layer] for layer in layers]
    indexes = [{a: i for i, a in enumerate(layer)} for layer in targets]
    rows = []
    dirty = []
    for word in permutations(range(b)):
        shore_rows = []
        omissions = []
        for k, index in zip((r, r - 1), indexes):
            windows = [sum(1 << word[(start + j) % b] for j in range(k)) for start in range(b)]
            shore_rows.append(tuple(index[a] for a in windows[1:]))
            omissions.append(windows[0])
        rows.append(tuple(shore_rows))
        dirty.append(tuple(omissions))
    return targets, rows, dirty


def punctured_trace_check(r, targets, rows):
    offset = len(targets[0])
    flat_targets = targets[0] + targets[1]
    edges = [tuple(row[0]) + tuple(offset + v for v in row[1]) for row in rows]
    stars = [0] * len(flat_targets)
    degree = [0] * len(flat_targets)
    pair = [[0] * len(flat_targets) for _ in flat_targets]
    for edge_id, edge in enumerate(edges):
        bit = 1 << edge_id
        for v in edge:
            stars[v] |= bit
            degree[v] += 1
        for u, v in combinations(edge, 2):
            pair[u][v] += 1
            pair[v][u] += 1
    masks = []
    for edge in edges:
        mask = 0
        for v in edge:
            mask |= stars[v]
        masks.append(mask)
    closed = [mask.bit_count() for mask in masks]
    assert len(set(closed)) == 1
    z = len(edges)
    trace = z * sum(
        (masks[0] & masks[v]).bit_count()
        for v in range(z) if masks[0] & (1 << v)
    )
    star_cubes = sum(d ** 3 for d in degree)
    pair_cubes = sum(pair[u][v] ** 3 for u in range(len(pair)) for v in range(u))
    target_trace = sum(
        pair[u][v] * pair[v][w] * pair[w][u]
        for u in range(len(pair)) for v in range(len(pair)) for w in range(len(pair))
    )
    assert star_cubes - pair_cubes <= trace <= star_cubes + target_trace
    high = [[False] * len(pair) for _ in pair]
    for u, v in combinations(range(len(pair)), 2):
        a, b = flat_targets[u], flat_targets[v]
        is_high = ((u < offset and v < offset and not a & b)
                   or (u < offset <= v and a & b == b))
        high[u][v] = high[v][u] = is_high
    assert not any(
        high[u][v] and high[v][w] and high[w][u]
        for u, v, w in combinations(range(len(pair)), 3)
    )
    sh = sum(pair[u][v] for u, v in combinations(edges[0], 2) if high[u][v])
    sall = sum(pair[u][v] for u, v in combinations(edges[0], 2))
    duplicate = sum(degree[v] for v in edges[0]) - closed[0]
    assert F(sh, 4) <= duplicate <= sall
    return z, closed[0], F(trace, z)


def harmonic_checks(r, targets, rows, dirty):
    rng = Random(190507 + r)
    b = 2 * r + 1
    s = b - 1
    count = 0
    for trial in range(80):
        retained = [set(range(len(layer))) for layer in targets]
        selected = []
        alive = list(range(len(rows)))
        for _ in range(trial % 4):
            if not alive:
                break
            chosen = rng.choice(alive)
            child_retained = [retained[shore] - set(rows[chosen][shore]) for shore in range(2)]
            child_alive = [
                j for j in alive
                if all(set(rows[j][shore]) <= child_retained[shore] for shore in range(2))
            ]
            if not child_alive:
                break
            retained, alive = child_retained, child_alive
            selected.append(chosen)
        current = rng.sample(alive, min(len(alive), 1 + rng.randrange(120)))
        z_rows = len(current)
        for shore, k in enumerate((r, r - 1)):
            n_all = len(targets[shore])
            n = len(retained[shore])
            assert n == n_all - s * len(selected)
            z = F(s * z_rows, n)
            degree = [0] * n_all
            for j in current:
                for v in rows[j][shore]:
                    degree[v] += 1
            u = [F(degree[v], 1) / z - 1 if v in retained[shore] else F(0) for v in range(n_all)]
            assert sum(u) == 0
            q = []
            for label in range(b):
                p = F(sum(bool(dirty[j][shore] & (1 << label)) for j in current), z_rows)
                m = sum(bool(dirty[j][shore] & (1 << label)) for j in selected)
                q.append(F(n, n_all) * p + F(s * m, n_all))
            assert sum(q) == k and all(0 <= value <= 1 for value in q)
            coefficients = [F(b, k * (b - k)) * (F(k, b) - value) for value in q]
            projected = [sum(coefficients[i] for i in range(b) if a & (1 << i)) for a in targets[shore]]
            for label in range(b):
                moment = sum(u[v] for v, a in enumerate(targets[shore]) if a & (1 << label))
                assert moment / n_all == (F(k, b) - q[label]) / s
                assert sum(
                    u[v] - projected[v] for v, a in enumerate(targets[shore]) if a & (1 << label)
                ) == 0
            second = sum(value ** 2 for value in projected) / n_all
            fourth = sum(value ** 4 for value in projected) / n_all
            assert second <= F(1, s)
            assert all(-1 <= value <= F(k, b - k) for value in projected)
            a2 = sum(value ** 2 for value in coefficients)
            a4 = sum(value ** 4 for value in coefficients)
            probs = [F(comb(k, j), comb(b, j)) if j <= k else F(0) for j in range(1, 5)]
            p1, p2, p3, p4 = probs
            assert fourth == (p1 - 7 * p2 + 12 * p3 - 6 * p4) * a4 + 3 * (p2 - 2 * p3 + p4) * a2 ** 2
            extreme_a2 = F(b, k * (b - k))
            extreme_a4 = F(1, k ** 3) + F(1, (b - k) ** 3)
            extreme_fourth = (p1 - 7 * p2 + 12 * p3 - 6 * p4) * extreme_a4 + 3 * (p2 - 2 * p3 + p4) * extreme_a2 ** 2
            assert fourth <= extreme_fourth
            if r >= 3:
                assert fourth <= F(2048, s * s)
            count += 1
    return count


def inventory_surplus_bound(r):
    d = 2 * r * factorial(r) * factorial(r + 1)
    sh = F((2 * r - 1) ** 2, r * (r + 1)) + F((4 * r - 1) ** 2, 2 * r * r)
    total = F(0)
    for a in range(r):
        codegree = (4 * r - 2) * factorial(a) * factorial(r - a) ** 2 * factorial(a + 1)
        total += F((2 * r - 1) * codegree, d)
    for a in range(r - 1):
        mult = 4 * r - 2 if a == 0 else 2 * r - 1
        codegree = ((8 * r - 4) * factorial(r - 1) ** 2 * factorial(3) if a == 0
                    else (4 * r - 2) * factorial(a) * factorial(r - 1 - a) ** 2 * factorial(a + 3))
        total += F(mult * codegree, d)
    for a in range(r):
        if a == 0:
            mult = 6 * r - 3
            codegree = mult * factorial(r) * factorial(r - 1) * factorial(2)
        elif a == r - 1:
            mult = 4 * r - 1
            codegree = mult * factorial(r - 1) * factorial(r + 1)
        else:
            mult = 4 * r - 2
            codegree = mult * factorial(a) * factorial(r - a) * factorial(r - 1 - a) * factorial(a + 2)
        total += F(mult * codegree, d)
    dl = F(r + 2, r)
    zeta = (1 + dl * dl) / (1 + dl)
    delta2 = F(4 * r - 1, 2 * r * r)
    lower = zeta * sh / 4 - delta2 * total
    assert total >= sh
    s = 2 * r
    nm, nl = comb(2 * r + 1, r), comb(2 * r + 1, r - 1)
    dz = F(s, nm)
    a0 = s * (1 + dl)
    shore_ratio = F((nm - s) * (nl - s) * (nm + nl), nm * nl * (nm + nl - 2 * s))
    drift_lower = shore_ratio * (zeta * dz + lower * dz / a0) - (1 - shore_ratio) - (a0 * dz) ** 2
    assert a0 * dz < 1
    if r >= 24:
        assert drift_lower > 0
    return lower, total - sh, drift_lower


if __name__ == "__main__":
    print("Exact finite-jump graph checks:", graph_checks())
    total_harmonic = 0
    for r in (2, 3):
        data = catalogue(r)
        print(f"Punctured r={r} (Z, closed conflict, trace/Z):", punctured_trace_check(r, *data[:2]))
        total_harmonic += harmonic_checks(r, *data)
    print("Exact matching-residual harmonic checks:", total_harmonic)
    for r in (12, 24, 48, 96, 192):
        lower, low_mass, drift_lower = inventory_surplus_bound(r)
        assert lower > 0
        print(f"r={r}: certified (trace-T*zeta)/(Z*D^2) >= {float(lower):.8f}; S_low/D={float(low_mass):.8f}")
        if r >= 24:
            print(f"  Exact-rational certificate: E[chi']/chi - 1 >= {float(drift_lower):.8e} > 0")
