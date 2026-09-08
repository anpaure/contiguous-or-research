#!/usr/bin/env python3
"""Audit lower triple-intersection support of the resident C8.

Run substantively on H100 only.  This independently rebuilds the four
complementary-square owner cycles and compares the old four-cycle bank with
the switched concatenation.
"""

from collections import Counter


def insert_fixed(base, fixed, length):
    out = []
    it = iter(base)
    for pos in range(1, length + 1):
        out.append(fixed[pos] if pos in fixed else next(it))
    try:
        next(it)
        raise AssertionError("unused base entry")
    except StopIteration:
        return out


def build_paths(m, q):
    assert q >= 5 and m >= max(q + 8, 2 * q + 2)
    C = [("c", i) for i in range(m - 3)]
    Q = [("q", i) for i in range(4)]
    Z = [("z", i) for i in range(m - 3)]
    a = ("a", 0)
    ground = set(C + Q + [a] + Z)
    n = m - 1
    w = n - q
    paths = []
    t_values = []

    for j in range(4):
        p = C[j]
        t = C[j + q]
        d = Z[m - 4 - j]
        t_values.append(t)
        U = set(C + [a, Q[j], Q[(j + 1) % 4]])
        missing = [Q[(j + 2) % 4], Q[(j + 3) % 4]]
        alpha = next(x for x in missing if x[1] % 2 == 0)
        beta = next(x for x in missing if x[1] % 2 == 1)
        gamma = [C[(j + s) % len(C)] for s in range(1, len(C))]
        assert gamma[q - 1] == t
        f_dep = gamma + [a, Q[j], Q[(j + 1) % 4]]
        f_arr = Z + [alpha, beta]
        forward = [U]
        for x, y in zip(f_dep, f_arr):
            forward.append((forward[-1] - {x}) | {y})

        B = {p} | (ground - U)
        assert forward[-1] == B
        rho_base = [x for x in gamma if x != t]
        if j < 3:
            rho = insert_fixed(rho_base, {w: Q[j]}, n - 3)
        else:
            rho_base = [x for x in rho_base if x not in {C[1], C[2]}]
            rho = insert_fixed(
                rho_base, {w: Q[j], w + 1: C[1], w + 2: C[2]}, n - 3
            )
        r_dep = [x for x in Z if x != d] + [
            Q[(j + 3) % 4], d, Q[(j + 2) % 4]
        ]
        r_arr = rho + [Q[(j + 1) % 4], t, a]
        ret = [B]
        for x, y in zip(r_dep, r_arr):
            ret.append((ret[-1] - {x}) | {y})
        R = set(C + [Q[j], Q[(j + 1) % 4], Q[(j + 2) % 4]])
        assert ret[-2] == R and ret[-1] == U
        path = forward + ret[1:-1]
        assert path[0] == U and path[-1] == R and len(path) == 2 * n
        paths.append(path)
    return ground, C, Q, paths, t_values


def triple_intersections(cycles):
    result = Counter()
    for cycle in cycles:
        length = len(cycle)
        for index in range(length):
            value = cycle[index] & cycle[(index + 1) % length]
            value &= cycle[(index + 2) % length]
            result[frozenset(value)] += 1
    return result


def palettes(cycles):
    owners = set()
    lowers = set()
    uppers = set()
    for cycle in cycles:
        length = len(cycle)
        for index, owner in enumerate(cycle):
            nxt = cycle[(index + 1) % length]
            owners.add(frozenset(owner))
            lowers.add(frozenset(owner & nxt))
            uppers.add(frozenset(owner | nxt))
    return owners, lowers, uppers


def backup_cycle(target, anchor, outside):
    assert anchor in target and len(outside) == 6
    core = set(target) - {anchor}
    toggles = [anchor] + list(outside)
    return [
        core | {
            toggles[index],
            toggles[(index + 1) % 7],
            toggles[(index + 2) % 7],
        }
        for index in range(7)
    ]


def choose_backups(ground, C, Q, paths, t_values, targets):
    used_owner, used_lower, used_upper = palettes(paths)
    backups = []
    choices = []
    for index in range(4):
        target = frozenset(
            (set(C) - {t_values[index]})
            | {Q[index], Q[(index + 1) % 4]}
        )
        assert target in targets
        anchor = C[0]
        outside = (
            ("a", 0), Q[(index + 2) % 4], Q[(index + 3) % 4],
            ("z", 0), ("z", 1), ("z", 2),
        )
        assert anchor in target and set(outside) <= ground - set(target)
        cycle = backup_cycle(set(target), anchor, outside)
        owners, lowers, uppers = palettes([cycle])
        assert len(owners) == len(lowers) == len(uppers) == 7
        assert not owners & used_owner
        assert not lowers & used_lower
        assert not uppers & used_upper
        assert triple_intersections([cycle])[target] == 1
        used_owner |= owners
        used_lower |= lowers
        used_upper |= uppers
        backups.append(cycle)
        choices.append((anchor, outside))

    # Every trace is two-sided depth-two resident.  Core/noncore constant
    # coordinates are ignored in the usual residence convention.
    for cycle in backups:
        lower = [
            cycle[index] & cycle[(index + 1) % 7] for index in range(7)
        ]
        upper = [
            cycle[index] | cycle[(index + 1) % 7] for index in range(7)
        ]
        for trace, expected in ((cycle, (3, 4)), (lower, (2, 5)), (upper, (4, 3))):
            for coordinate in ground:
                bits = [coordinate in value for value in trace]
                if all(bits) or not any(bits):
                    continue
                positive = max_run(bits, True)
                zero = max_run(bits, False)
                assert sorted((positive, zero)) == sorted(expected)
    return backups, choices


def max_run(bits, value):
    doubled = bits + bits
    best = current = 0
    for bit in doubled:
        if bit == value:
            current += 1
            best = max(best, current)
        else:
            current = 0
    return min(best, len(bits))


def audit(m, q):
    ground, C, Q, paths, t_values = build_paths(m, q)
    old = triple_intersections(paths)
    switched = triple_intersections([sum(paths, [])])
    losses = {x: old[x] - switched[x] for x in old if old[x] > switched[x]}
    births = {x: switched[x] - old[x] for x in switched if switched[x] > old[x]}

    predicted_losses = {
        frozenset((set(C) - {t_values[j]}) | {Q[j], Q[(j + 1) % 4]})
        for j in range(4)
    }
    predicted_births = {
        frozenset((set(C) - {t_values[j]}) | {Q[(j + 1) % 4], Q[(j + 2) % 4]})
        for j in range(4)
    }
    assert set(losses) == predicted_losses
    assert set(births) == predicted_births
    assert set(losses.values()) == {1} and set(births.values()) == {1}
    assert all(switched[x] == 0 for x in losses)
    backups, choices = choose_backups(
        ground, C, Q, paths, t_values, predicted_losses
    )
    combined_old = old + triple_intersections(backups)
    combined_new = switched + triple_intersections(backups)
    assert all(combined_new[target] >= 1 for target in old)
    return {
        "m": m,
        "q": q,
        "old_support": len(old),
        "new_support": len(switched),
        "losses": len(losses),
        "births": len(births),
        "lost_loads_after": sorted(switched[x] for x in losses),
        "backup_cycles": len(backups),
        "backup_owners": sum(len(cycle) for cycle in backups),
        "backup_choices": choices,
        "combined_support_losses": sum(
            1 for target in combined_old if combined_new[target] == 0
        ),
        "formula": "four predecessor-side singleton losses and four births",
    }


if __name__ == "__main__":
    cases = []
    for m in range(18, 81):
        q = max(5, int(m**0.5) + 1)
        if m >= max(q + 8, 2 * q + 2):
            cases.append(audit(m, q))
    print({"status": "PASS", "cases": len(cases), "first": cases[0], "last": cases[-1]})
