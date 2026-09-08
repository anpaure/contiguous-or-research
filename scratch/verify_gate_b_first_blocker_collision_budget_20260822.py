#!/usr/bin/env python3
"""Exact finite checks for the first-blocker collision-budget theorem."""

from fractions import Fraction as F
from itertools import combinations, permutations
from math import exp, isqrt
import random


def state(rows, targets):
    z = len(rows)
    assert z
    b = len(rows[0])
    assert all(len(w) == b for w in rows)
    x = [sum(t in w for w in rows) for t in targets]
    s = sum(v * v for v in x)
    n = len(targets)
    kappa = F(n * s, b * b * z * z)
    weights = [sum(x[t] for t in w) for w in rows]
    return x, s, kappa, weights


def delete_cell(rows, cell, targets):
    x, s, kappa, weights = state(rows, targets)
    z = len(rows)
    b = len(rows[0])
    m = len(cell)
    y = [sum(t in rows[i] for i in cell) for t in targets]
    rb = sum(a * c for a, c in zip(x, y))
    qb = sum(c * c for c in y)
    assert rb == sum(weights[i] for i in cell)
    eb = F(m * s, z) - rb
    keep = [w for i, w in enumerate(rows) if i not in cell]
    if not keep:
        return None
    xp, sp, kappap, _ = state(keep, targets)
    delta = F(m, z)
    assert sp == s * (1 - 2 * delta) + 2 * eb + qb
    ratio = F(1 - 2 * delta) + F(2 * eb + qb, s)
    ratio /= (1 - delta) ** 2
    assert kappap / kappa == ratio

    nu = [F(c, b * m) for c in y]
    pi = [F(a, b * z) for a in x]
    pip = [F(a, b * len(keep)) for a in xp]
    assert pip == [(p - delta * v) / (1 - delta)
                   for p, v in zip(pi, nu)]
    return keep, (x, s, kappa, rb, qb, eb, delta, y)


def closed_neighborhood(graph, v, active):
    return {u for u in active if u == v or u in graph[v]}


def random_first_blocker_checks():
    rng = random.Random(20260822)
    checked = 0
    for _ in range(800):
        n = rng.randint(4, 9)
        b = rng.randint(1, min(3, n))
        z = rng.randint(5, 13)
        targets = list(range(n))
        rows = [frozenset(rng.sample(targets, b)) for _ in range(z)]

        graph = [set() for _ in range(z)]
        for i, j in combinations(range(z), 2):
            if rng.random() < 0.22:
                graph[i].add(j)
                graph[j].add(i)

        # Greedily choose a pairwise nonadjacent accepted family.
        order = list(range(z))
        rng.shuffle(order)
        accepted = []
        for v in order:
            if all(v not in graph[u] for u in accepted):
                accepted.append(v)
            if len(accepted) >= 3:
                break

        current_ids = list(range(z))
        current_rows = list(rows)
        for g in accepted:
            active = set(current_ids)
            original_cell = closed_neighborhood(graph, g, active)
            local_cell = {i for i, oid in enumerate(current_ids)
                          if oid in original_cell}
            if not local_cell or len(local_cell) == len(current_rows):
                break

            result = delete_cell(current_rows, local_cell, targets)
            assert result is not None
            keep, data = result
            _, _, _, _, qb, _, _, _ = data

            # Q_B is at most the c-weighted mass of all pairs in the
            # current closed neighborhood of the accepted blocker.
            neigh_local = local_cell
            common_mass = 0
            for i in neigh_local:
                for j in neigh_local:
                    common_mass += len(current_rows[i] & current_rows[j])
            assert qb == common_mass

            keep_local = [i for i in range(len(current_rows))
                          if i not in local_cell]
            current_ids = [current_ids[i] for i in keep_local]
            current_rows = keep
            checked += 1
    return checked


def bite_partition_cap_checks():
    """A whole-bite cap delta implies the same cap in every residual cell."""
    rng = random.Random(31420260822)
    checked = 0
    for z0 in range(8, 161):
        cap = z0 // 8
        for _ in range(20):
            deleted = rng.randint(0, cap)
            remaining = deleted
            prior = 0
            while remaining:
                cell = rng.randint(1, remaining)
                assert F(cell, z0 - prior) <= F(1, 8)
                prior += cell
                remaining -= cell
                checked += 1
            assert prior <= F(z0, 8)
    return checked


def hole_transport_checks():
    targets = list(range(7))
    rows = [frozenset(w) for w in (
        (0, 1), (0, 2), (1, 3), (2, 4),
        (3, 5), (4, 6), (5, 6), (0, 6),
    )]
    holes = {3, 4, 5}
    current = rows
    products = F(1)
    x0, _, _, _ = state(current, targets)
    r0 = sum(F(x0[t], 2 * len(current)) for t in holes)
    for cell in ({0}, {1}):
        # Reindexing makes both literal cells the first current row.
        local = {0}
        x, _, _, _ = state(current, targets)
        r = sum(F(x[t], 2 * len(current)) for t in holes)
        result = delete_cell(current, local, targets)
        assert result is not None
        keep, data = result
        _, _, _, _, _, _, delta, y = data
        nu_h = sum(F(y[t], 2) for t in holes)
        products *= (1 - delta * nu_h / r) / (1 - delta)
        current = keep
    xp, _, _, _ = state(current, targets)
    rp = sum(F(xp[t], 2 * len(current)) for t in holes)
    assert rp / r0 == products
    return rp


def vortex_check():
    n, h, copies = 30, 6, 200
    targets = list(range(n))
    rows = [frozenset((t,)) for t in targets for _ in range(copies)]
    _, _, k0, _ = state(rows, targets)
    assert k0 == 1
    holes = set(range(h))
    keep = [w for w in rows if next(iter(w)) in holes]
    _, sfinal, kfinal, _ = state(keep, targets)
    assert kfinal == F(n, h)
    pi_h = sum(F(copies, len(keep)) for _ in holes)
    assert pi_h == 1
    # Singleton quadratic budget is bounded using the terminal pair-mass
    # floor throughout this particular monotone deletion.
    cells = (n - h) * copies
    assert F(cells, sfinal) <= F(1, F(h, n) * copies)
    return kfinal, F(cells, sfinal)


def weighted_singleton_checks():
    rng = random.Random(8222026)
    checked = 0
    for _ in range(600):
        n = rng.randint(4, 8)
        b = rng.randint(1, min(3, n))
        z = rng.randint(4, 10)
        targets = list(range(n))
        rows = [frozenset(rng.sample(targets, b)) for _ in range(z)]
        graph = [set() for _ in range(z)]
        for i, j in combinations(range(z), 2):
            if rng.random() < 0.28:
                graph[i].add(j)
                graph[j].add(i)

        x, s, _, _ = state(rows, targets)
        raw = [rng.randint(1, 9) for _ in range(z)]
        total = sum(raw)
        lam = [F(v, total) for v in raw]
        cvals, rvals, qvals, gains = [], [], [], []
        for g in range(z):
            cell = {g} | graph[g]
            y = [sum(t in rows[i] for i in cell) for t in targets]
            cg = len(cell)
            rg = sum(a * v for a, v in zip(x, y))
            qg = sum(v * v for v in y)
            gain = F(2 * cg, z) - F(2 * rg - qg, s)
            cvals.append(cg)
            rvals.append(rg)
            qvals.append(qg)
            gains.append(gain)

        zprime = -sum(w * c for w, c in zip(lam, cvals))
        sprime = -sum(w * (2 * r - q)
                      for w, r, q in zip(lam, rvals, qvals))
        logarithmic = sprime / s - 2 * zprime / z
        assert logarithmic == sum(w * g for w, g in zip(lam, gains))

        # Hole-support derivative, with rates restricted to rows avoiding H.
        holes = set(rng.sample(targets, rng.randint(1, n - 1)))
        allowed = [g for g, row in enumerate(rows) if not (row & holes)]
        xh = sum(x[t] for t in holes)
        if allowed and xh:
            raw_h = [rng.randint(1, 7) for _ in allowed]
            total_h = sum(raw_h)
            lam_h = [F(v, total_h) for v in raw_h]
            hvals, mvals, chvals = [], [], []
            for g in allowed:
                cell = {g} | graph[g]
                mg = sum(len(rows[i] & holes) for i in cell)
                cg = len(cell)
                mvals.append(mg)
                chvals.append(cg)
                hvals.append(F(cg, z) - F(mg, xh))
            xprime = -sum(w * m for w, m in zip(lam_h, mvals))
            zhprime = -sum(w * c for w, c in zip(lam_h, chvals))
            assert xprime / xh - zhprime / z == sum(
                w * h for w, h in zip(lam_h, hvals)
            )
        checked += 1
    return checked


def balanced_two_edge_obstruction_check():
    # In either shore: common-target loads are lambda+mu and private loads
    # are lambda and mu.  Equality plus normalization is impossible.
    for den in range(1, 31):
        for num in range(den + 1):
            lam = F(num, den)
            mu = 1 - lam
            assert not (lam + mu == lam == mu)
    return True


def gibbs_switch_checks():
    rng = random.Random(17720260822)
    checked = 0
    for _ in range(500):
        z = rng.randint(2, 12)
        base_raw = [rng.randint(1, 20) for _ in range(z)]
        base_total = sum(base_raw)
        base = [v / base_total for v in base_raw]
        gain = [rng.uniform(-3, 3) for _ in range(z)]
        previous = None
        for theta in (0.0, 0.05, 0.2, 0.7, 2.0, 8.0):
            raw = [p * exp(theta * g) for p, g in zip(base, gain)]
            total = sum(raw)
            law = [v / total for v in raw]
            objective = sum(p * g for p, g in zip(law, gain))
            if previous is not None:
                assert objective + 1e-12 >= previous
            previous = objective
        checked += 1
    return checked


def compensated_gibbs_checks():
    rng = random.Random(73120260822)
    checked = 0
    for _ in range(400):
        groups = rng.randint(2, 6)
        sizes = [rng.randint(2, 5) for _ in range(groups)]
        raw = [[rng.randint(1, 12) for _ in range(s)] for s in sizes]
        grand = sum(sum(v) for v in raw)
        base = [[F(v, grand) for v in part] for part in raw]
        gain = [[F(rng.randint(-20, 20), 7) for _ in part]
                for part in raw]

        # The constraints preserve the total baseline mass of every group.
        dot = []
        lhs = F(0)
        rhs = F(0)
        for ppart, gpart in zip(base, gain):
            mass = sum(ppart)
            avg = sum(p * g for p, g in zip(ppart, gpart)) / mass
            dpart = [p * (g - avg) for p, g in zip(ppart, gpart)]
            dot.append(dpart)
            lhs += sum(d * g for d, g in zip(dpart, gpart))
            rhs += sum(d * d / p for d, p in zip(dpart, ppart))
            assert sum(dpart) == 0
        assert lhs == rhs and rhs >= 0

        previous = None
        for theta in (0.0, 0.1, 0.5, 2.0, 7.0):
            objective = 0.0
            for ppart, gpart in zip(base, gain):
                mass = float(sum(ppart))
                vals = [float(p) * exp(theta * float(g))
                        for p, g in zip(ppart, gpart)]
                scale = mass / sum(vals)
                objective += sum(scale * v * float(g)
                                 for v, g in zip(vals, gpart))
            if previous is not None:
                assert objective + 1e-11 >= previous
            previous = objective
        checked += 1
    return checked


def row_hazard_compensation_checks():
    rng = random.Random(71120260822)
    checked = 0
    for z in range(5, 15):
        n = z + 3
        b = 2
        targets = list(range(n))
        rows = [frozenset(rng.sample(targets, b)) for _ in range(z)]
        x, s, kappa, _ = state(rows, targets)
        # Closed neighborhoods in a cycle have common size three.
        cells = [{(g - 1) % z, g, (g + 1) % z} for g in range(z)]
        c = F(3, z)
        yrows = []
        sprimes = []
        zprimes = []
        for cell in cells:
            y = [sum(t in rows[i] for i in cell) for t in targets]
            yrows.append(y)
            keep = [w for i, w in enumerate(rows) if i not in cell]
            _, sp, _, _ = state(keep, targets)
            sprimes.append(sp)
            zprimes.append(len(keep))
        assert F(sum(zprimes), z) == z * (1 - c)
        means = [F(sum(y[t] for y in yrows), z) for t in targets]
        assert means == [c * value for value in x]
        variances = [F(sum(y[t] * y[t] for y in yrows), z)
                      - means[t] * means[t] for t in targets]
        esp = F(sum(sprimes), z)
        assert esp == s * (1 - c) ** 2 + sum(variances)
        ratio_means = F(n) * esp / (b * b * (z * (1 - c)) ** 2)
        assert ratio_means >= kappa
        checked += 1
    return checked


def balanced_duplicate_cancellation_check():
    """Audit Proposition 7.2a on a nontrivial two-shore hypergraph."""
    left = [("M", i) for i in range(4)]
    right = [("L", i) for i in range(4)]
    rows = [frozenset(a + b)
            for a in combinations(left, 2)
            for b in combinations(right, 2)]
    z = len(rows)
    assert z == 36
    vertices = left + right
    degree = {v: sum(v in row for row in rows) for v in vertices}
    assert set(degree.values()) == {18}

    # An arbitrary constant-size external deck and a nontrivial support.
    external = [frozenset((index % 11, (index + 4) % 11))
                for index in range(z)]
    holes = {0, 3, 7}
    score = [len(deck & holes) for deck in external]
    x_holes = sum(score)
    assert x_holes

    # A checkerboard perturbation of the product law preserves every
    # central target load but makes the audited drift nonzero.
    rate = [F(1, z) for _ in rows]
    epsilon = F(1, 100)
    for index, sign in ((0, 1), (7, 1), (1, -1), (6, -1)):
        rate[index] += sign * epsilon
    assert min(rate) > 0 and sum(rate) == 1

    lhs = F(0)
    rhs = F(0)
    for g_index, g in enumerate(rows):
        cell = [f_index for f_index, f in enumerate(rows) if f & g]
        c_g = len(cell)
        m_g = sum(score[f_index] for f_index in cell)
        duplicate = [max(len(f & g) - 1, 0) for f in rows]
        d_zero = sum(duplicate)
        d_holes = sum(weight * value
                      for weight, value in zip(score, duplicate))
        lhs += rate[g_index] * (F(c_g, z) - F(m_g, x_holes))
        rhs += rate[g_index] * (F(d_holes, x_holes) - F(d_zero, z))

    # The perturbed rates still have the required load 2/4 on every target.
    for vertex in vertices:
        assert sum(rate[index] for index, row in enumerate(rows)
                   if vertex in row) == F(1, 2)
    assert lhs == rhs == F(-1, 950)
    return lhs


def modular_column_rank(columns, prime=1_000_003):
    """Exact column rank over F_prime; full rank certifies Q-column rank."""
    assert all(prime % divisor for divisor in range(2, isqrt(prime) + 1))
    basis = {}
    for column in columns:
        value = [entry % prime for entry in column]
        while True:
            pivot = next((i for i, entry in enumerate(value) if entry), None)
            if pivot is None:
                break
            if pivot not in basis:
                inverse = pow(value[pivot], prime - 2, prime)
                basis[pivot] = [(entry * inverse) % prime
                                for entry in value]
                break
            coefficient = value[pivot]
            old = basis[pivot]
            value = [(entry - coefficient * old_entry) % prime
                     for entry, old_entry in zip(value, old)]
    return len(basis)


def c8_exposure_detection_checks():
    """Exact r=4 C8 orbit obstruction in the complete punctured catalogue."""
    n, r = 9, 4
    middle = list(combinations(range(n), r))
    lower = list(combinations(range(n), r - 1))
    pairs = list(combinations(range(n), r - 2))
    targets = middle + lower
    target_index = {frozenset(target): i
                    for i, target in enumerate(targets)}
    pair_index = {frozenset(target): i
                  for i, target in enumerate(pairs)}

    def windows(word, length, omit_origin):
        first = 1 if omit_origin else 0
        return [frozenset(word[(start + offset) % n]
                          for offset in range(length))
                for start in range(first, n)]

    def configuration_mask(word):
        retained = windows(word, r, True) + windows(word, r - 1, True)
        return sum(1 << target_index[target] for target in retained)

    # Compute one column of the unnormalised rooted-exposure matrix from
    # its definition.  Every other column is a label translate of this one.
    identity = tuple(range(n))
    identity_mask = configuration_mask(identity)
    base_exposure = [0] * len(targets)
    degrees = [0] * len(targets)
    for word in permutations(range(n)):
        current = configuration_mask(word)
        duplicate = max((current & identity_mask).bit_count() - 1, 0)
        bits = current
        while bits:
            low_bit = bits & -bits
            index = low_bit.bit_length() - 1
            degrees[index] += 1
            base_exposure[index] += duplicate
            bits -= low_bit
    assert set(degrees[:len(middle)]) == {23040}
    assert set(degrees[len(middle):]) == {34560}

    a, b, c, d = 0, 1, 2, 3
    pword, qword = (4, 5, 6), (7, 8)
    negative = [
        (a, b) + pword + (c, d) + qword,
        (c, a) + pword + (d, b) + qword,
    ]
    positive = [
        (a, c) + pword + (b, d) + qword,
        (b, a) + pword + (d, c) + qword,
    ]
    reversal = {pword[0]: pword[-1], pword[-1]: pword[0]}

    def reverse_p(word):
        return tuple(reversal.get(label, label) for label in word)

    signed_words = [(-1, word) for word in negative]
    signed_words += [(1, word) for word in positive]
    signed_words += [(-1, reverse_p(word)) for word in negative]
    signed_words += [(1, reverse_p(word)) for word in positive]

    central_current = [0] * len(targets)
    shallow_current = [0] * len(pairs)
    exposure_current = [0] * len(targets)
    bank_columns_a = []
    bank_columns_ap = []
    directed_words = []
    for sign, cyclic_word in signed_words:
        # Its full rank-two deck is independent of the puncture origin.
        for target in windows(cyclic_word, r - 2, False):
            shallow_current[pair_index[target]] += n * sign

        for origin in range(n):
            word = cyclic_word[origin:] + cyclic_word[:origin]
            directed_words.append(word)
            incidence = [0] * len(targets)
            for target in windows(word, r, True) + windows(word, r - 1, True):
                incidence[target_index[target]] = 1
            translated_exposure = [0] * len(targets)
            for index, target in enumerate(targets):
                image = frozenset(word[label] for label in target)
                translated_exposure[target_index[image]] = base_exposure[index]
            for index in range(len(targets)):
                central_current[index] += sign * incidence[index]
                exposure_current[index] += sign * translated_exposure[index]
            bank_columns_a.append(incidence)
            bank_columns_ap.append(incidence + translated_exposure)

    assert len(directed_words) == 72
    assert len(set(directed_words)) == 72
    assert central_current == [0] * len(targets)
    expected = {
        frozenset((b, qword[0])): -18,
        frozenset((b, qword[1])): 18,
        frozenset((c, qword[0])): 18,
        frozenset((c, qword[1])): -18,
    }
    assert {
        frozenset(pairs[index]): value
        for index, value in enumerate(shallow_current) if value
    } == expected

    down_middle = []
    down_lower = []
    for pair in pairs:
        pair_set = set(pair)
        down_middle.append(sum(
            exposure_current[index]
            for index, target in enumerate(middle)
            if pair_set <= set(target)
        ))
        down_lower.append(sum(
            exposure_current[len(middle) + index]
            for index, target in enumerate(lower)
            if pair_set <= set(target)
        ))
    assert all(9 * value == 425 * current
               for value, current in zip(down_middle, shallow_current))
    assert all(3 * value == 2944 * current
               for value, current in zip(down_lower, shallow_current))

    rank_a = modular_column_rank(bank_columns_a)
    rank_ap = modular_column_rank(bank_columns_ap)
    assert rank_a == 35
    assert rank_ap == 72
    return rank_a, rank_ap


def c8_all_r_shadow_checks():
    """Check the dimension-free q=1 cancellation and q=2 current."""
    checked = 0
    for r in range(4, 17):
        n = 2 * r + 1
        a, b, c, d = 0, 1, 2, 3
        pword = tuple(range(4, r + 3))
        qword = tuple(range(r + 3, n))
        assert len(pword) == r - 1 and len(qword) == r - 2
        negative = [
            (a, b) + pword + (c, d) + qword,
            (c, a) + pword + (d, b) + qword,
        ]
        positive = [
            (a, c) + pword + (b, d) + qword,
            (b, a) + pword + (d, c) + qword,
        ]
        reversal = {pword[i]: pword[-1 - i]
                    for i in range(len(pword))}
        reverse_p = lambda word: tuple(reversal.get(x, x) for x in word)
        signed = [(-1, word) for word in negative]
        signed += [(1, word) for word in positive]
        signed += [(-1, reverse_p(word)) for word in negative]
        signed += [(1, reverse_p(word)) for word in positive]

        def deck(word, length):
            return [frozenset(word[(start + offset) % n]
                              for offset in range(length))
                    for start in range(n)]

        ledgers = {}
        for length in (r, r - 1, r - 2):
            ledger = {}
            for sign, word in signed:
                for target in deck(word, length):
                    ledger[target] = ledger.get(target, 0) + sign
            ledgers[length] = {target: value
                               for target, value in ledger.items() if value}
        assert not ledgers[r] and not ledgers[r - 1]
        prefix = frozenset(qword[:r - 3])
        suffix = frozenset(qword[-(r - 3):])
        expected = {
            frozenset({b} | prefix): -2,
            frozenset({c} | suffix): -2,
            frozenset({c} | prefix): 2,
            frozenset({b} | suffix): 2,
        }
        assert ledgers[r - 2] == expected
        checked += 1
    return checked


def main():
    checked = random_first_blocker_checks()
    partitions = bite_partition_cap_checks()
    rp = hole_transport_checks()
    kfinal, qbudget = vortex_check()
    weighted = weighted_singleton_checks()
    gibbs = gibbs_switch_checks()
    compensated = compensated_gibbs_checks()
    hazard = row_hazard_compensation_checks()
    duplicate_cancellation = balanced_duplicate_cancellation_check()
    c8_rank_a, c8_rank_ap = c8_exposure_detection_checks()
    c8_dimensions = c8_all_r_shadow_checks()
    balanced_two_edge_obstruction_check()
    print(
        "GATE_B_FIRST_BLOCKER_COLLISION_BUDGET_PASS",
        f"random_cells={checked}",
        f"bite_partition_cells={partitions}",
        f"weighted_tangents={weighted}",
        f"gibbs_switches={gibbs}",
        f"compensated_switches={compensated}",
        f"hazard_compensation={hazard}",
        f"duplicate_cancellation={duplicate_cancellation}",
        f"c8_rank_A={c8_rank_a}",
        f"c8_rank_AP={c8_rank_ap}",
        f"c8_dimensions={c8_dimensions}",
        f"hole_mass={rp}",
        f"vortex_K={kfinal}",
        f"vortex_Q_bound={qbudget}",
    )


if __name__ == "__main__":
    main()
