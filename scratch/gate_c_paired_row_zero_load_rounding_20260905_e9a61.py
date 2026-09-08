"""Exact checks for paired-position, zero-load row rounding (e9a61)."""

from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb
from random import Random


def decks(row, ranks):
    n = len(row)
    answer = {}
    for s in ranks:
        targets = set()
        for a in range(n):
            mask = 0
            for j in range(s):
                mask |= 1 << row[(a + j) % n]
            targets.add(mask)
        assert len(targets) == n
        answer[s] = targets
    return answer


def oriented(row, bits):
    return tuple(row[2 * i + (j ^ bits[i])] for i in range(len(bits)) for j in (0, 1))


def window_forms(row, ranks):
    n, b = len(row), len(row) // 2
    forms = []
    seen = set()
    for s in ranks:
        for a in range(n):
            positions = {(a + j) % n for j in range(s)}
            partial = tuple(i for i in range(b) if len(positions & {2 * i, 2 * i + 1}) == 1)
            assert len(partial) <= 2
            base = sum(1 << row[j] for j in positions)
            variants = {}
            for values in product((0, 1), repeat=len(partial)):
                target = base
                for i, value in zip(partial, values):
                    if value:
                        target ^= (1 << row[2 * i]) | (1 << row[2 * i + 1])
                assert target not in seen
                seen.add(target)
                variants[values] = target
            forms.append((s, a, partial, base, variants))
    return forms


def compiled(row, h):
    n, low = len(row), len(row) // 2 - h
    result = []
    for j in range(n + 2 * h):
        mask = 0
        for r in range(low):
            mask |= 1 << row[(j + r) % n]
        result.append(mask)
    return result


def literal_targets(word):
    suffixes, answer = set(), set()
    for letter in word:
        assert letter
        suffixes = {letter} | {target | letter for target in suffixes}
        answer.update(suffixes)
    return answer


def row_counts(rows, ranks):
    return Counter(target for row in rows for bank in decks(row, ranks).values() for target in bank)


def protection(forms, external, caps):
    pins = set()
    for s, _, partial, target, _ in forms:
        if external[target] < caps[s]:
            pins.update(partial)
    return pins


def useful_patterns(forms, external, caps, pins):
    patterns = []
    for s, _, partial, base, variants in forms:
        for values, target in variants.items():
            if target == base or external[target] >= caps[s]:
                continue
            if any(value for i, value in zip(partial, values) if i in pins):
                continue
            required = {i: value for i, value in zip(partial, values) if i not in pins}
            assert 1 <= len(required) <= 2
            patterns.append((target, required))
    assert len({target for target, _ in patterns}) == len(patterns)
    return patterns


def conditional_augmentation(b, pins, patterns):
    fixed = dict.fromkeys(pins, 0)

    def expectation(assignment):
        total = Fraction(0)
        for _, required in patterns:
            if any(i in assignment and assignment[i] != value for i, value in required.items()):
                continue
            missing = sum(i not in assignment for i in required)
            total += Fraction(1, 1 << missing)
        return total

    initial = expectation(fixed)
    previous = initial
    for i in range(b):
        if i in fixed:
            continue
        scores = [expectation(fixed | {i: value}) for value in (0, 1)]
        assert sum(scores) / 2 == previous
        value = int(scores[1] > scores[0])
        fixed[i] = value
        previous = scores[value]
    assert previous >= initial
    return tuple(fixed[i] for i in range(b)), initial


def conditional_cost(row, ranks, external, caps):
    return -sum(
        external[target] < caps[s]
        for s, targets in decks(row, ranks).items()
        for target in targets
    )


def folded_oracle(row, h, ranks, external, caps, pins=frozenset()):
    n = len(row)
    assert n % 4 == 0
    m = n // 4
    radius = min(m, (h + 1) // 2 + 1)
    unary = [[0] * 4 for _ in range(m)]
    edges = {}
    constant = 0
    forms = window_forms(row, ranks)
    for s, _, partial, base, variants in forms:
        scope = tuple(sorted({i % m for i in partial}))

        def cost(states):
            values = tuple((states[i % m] >> (i // m)) & 1 for i in partial)
            return -int(external[variants[values]] < caps[s])

        if not scope:
            constant += -int(external[base] < caps[s])
        elif len(scope) == 1:
            i = scope[0]
            for value in range(4):
                unary[i][value] += cost({i: value})
        else:
            i, j = scope
            assert min(j - i, m - (j - i)) <= radius
            table = edges.setdefault((i, j), [[0] * 4 for _ in range(4)])
            for first, second in product(range(4), repeat=2):
                table[first][second] += cost({i: first, j: second})

    allowed = [
        tuple(
            state for state in range(4)
            if not (i in pins and state & 1) and not (i + m in pins and state & 2)
        )
        for i in range(m)
    ]
    incoming = [[] for _ in range(m)]
    for (i, j), table in edges.items():
        incoming[j].append((i, table))
    best = None
    for prefix in product(*allowed[:radius]):
        start_cost = constant + sum(unary[i][prefix[i]] for i in range(radius))
        start_cost += sum(
            table[prefix[i]][prefix[j]]
            for (i, j), table in edges.items() if j < radius
        )
        states = {prefix: (start_cost, prefix)}
        for j in range(radius, m):
            following = {}
            for tail, (old_cost, path) in states.items():
                for value in allowed[j]:
                    new_cost = old_cost + unary[j][value]
                    for i, table in incoming[j]:
                        if i < radius:
                            previous = prefix[i]
                        else:
                            assert i >= j - radius
                            previous = tail[i - (j - len(tail))]
                        new_cost += table[previous][value]
                    key = (tail + (value,))[-radius:]
                    candidate = (new_cost, path + (value,))
                    if key not in following or candidate < following[key]:
                        following[key] = candidate
            states = following
        candidate = min(states.values())
        if best is None or candidate < best:
            best = candidate
    value, path = best
    bits = tuple((path[i % m] >> (i // m)) & 1 for i in range(2 * m))
    result = oriented(row, bits)
    assert conditional_cost(result, ranks, external, caps) == value
    assert all(bits[i] == 0 for i in pins)
    return result, value, bits


def check_geometry_and_rounding():
    rng = Random(0xE9A61)
    face_cases = oracle_cases = 0
    for n in (8, 12, 16, 20):
        b = n // 2
        for h in (1, 2):
            ranks = tuple(range(b - h, b + h + 1))
            for trial in range(4):
                row = list(range(n))
                rng.shuffle(row)
                row = tuple(row)
                forms = window_forms(row, ranks)
                if trial == 0:
                    others = [row]
                else:
                    others = []
                    for _ in range(2):
                        other = list(range(n))
                        rng.shuffle(other)
                        others.append(tuple(other))
                external = row_counts(others, ranks)
                caps = {s: 1 + int(trial == 3 and s % 2 == 0) for s in ranks}
                pins = protection(forms, external, caps)
                old = row_counts([row], ranks)
                oracle_row, optimum, _ = folded_oracle(row, h, ranks, external, caps)
                brute = None
                for bits in product((0, 1), repeat=b):
                    variant = oriented(row, bits)
                    cost = conditional_cost(variant, ranks, external, caps)
                    brute = cost if brute is None else min(brute, cost)
                    if n <= 12:
                        new = row_counts([variant], ranks)
                        no_loss = all(
                            min(external[target] + new[target], caps[target.bit_count()])
                            >= min(external[target] + old[target], caps[target.bit_count()])
                            for target in old
                        )
                        assert no_loss == all(bits[i] == 0 for i in pins)
                        face_cases += 1
                assert optimum == brute
                assert optimum <= conditional_cost(row, ranks, external, caps)
                patterns = useful_patterns(forms, external, caps, pins)
                bits, expectation = conditional_augmentation(b, pins, patterns)
                update = oriented(row, bits)
                gain = conditional_cost(row, ranks, external, caps) - conditional_cost(update, ranks, external, caps)
                assert gain >= expectation >= Fraction(len(patterns), 4)
                protected_row, protected_cost, _ = folded_oracle(row, h, ranks, external, caps, pins)
                assert protected_cost <= conditional_cost(update, ranks, external, caps)
                updated = row_counts([protected_row], ranks)
                assert all(
                    min(external[target] + updated[target], caps[target.bit_count()])
                    >= min(external[target] + old[target], caps[target.bit_count()])
                    for target in old
                )
                all_mask = (1 << n) - 1
                support = decks(oracle_row, ranks)
                for s in ranks:
                    assert {all_mask ^ target for target in support[s]} == support[n - s]
                blocks = [compiled(current, h) for current in (row, oracle_row)]
                word = [letter for block in blocks for letter in block]
                actual = literal_targets(word)
                designated = set(row_counts([row, oracle_row], ranks))
                assert designated <= actual
                for s in ranks:
                    extra = len({target for target in actual - designated if target.bit_count() == s})
                    assert extra <= s - (b - h) + 1
                oracle_cases += 1
    print(f"Unique forms, exact cap faces: {face_cases} exhaustive orientations passed")
    print(f"Folded optimum vs brute force, augmentation, complements, literal joins: {oracle_cases} cases passed")


def check_parallel_protection():
    n, h = 8, 1
    ranks = (3, 4, 5)
    rows = [tuple(range(n))] * 3
    old = row_counts(rows, ranks)
    forms = [window_forms(row, ranks) for row in rows]
    caps = {s: 1 for s in ranks}
    pins = [set() for _ in rows]
    for target in old:
        owner = next(i for i, bank in enumerate(forms) if any(base == target for _, _, _, base, _ in bank))
        partial = next(partial for _, _, partial, base, _ in forms[owner] if base == target)
        pins[owner].update(partial)
    choices = [
        [bits for bits in product((0, 1), repeat=n // 2) if all(bits[i] == 0 for i in bank)]
        for bank in pins
    ]
    candidates = {}
    requirements = {}
    for i, bank in enumerate(forms):
        for _, _, partial, _, variants in bank:
            for values, target in variants.items():
                if target in old or any(value for bit, value in zip(partial, values) if bit in pins[i]):
                    continue
                free = sum(bit not in pins[i] for bit in partial)
                assert 1 <= free <= 2
                candidates.setdefault(target, {})[i] = Fraction(1, 1 << free)
                requirements.setdefault(target, {})[i] = {
                    bit: value for bit, value in zip(partial, values) if bit not in pins[i]
                }
    expected_gain = sum(
        1 - product_fraction(1 - p for p in available.values())
        for available in candidates.values()
    )
    actual_total, runs = 0, 0
    for assignments in product(*choices):
        new_rows = [oriented(row, bits) for row, bits in zip(rows, assignments)]
        new = row_counts(new_rows, ranks)
        assert set(old) <= set(new)
        actual_total += len(set(new) - set(old))
        runs += 1
    assert Fraction(actual_total, runs) == expected_gain
    fixed = [dict.fromkeys(bank, 0) for bank in pins]

    def expected_misses():
        value = Fraction(0)
        for banks in requirements.values():
            miss = Fraction(1)
            for i, required in banks.items():
                if any(bit in fixed[i] and fixed[i][bit] != wanted for bit, wanted in required.items()):
                    continue
                remaining = sum(bit not in fixed[i] for bit in required)
                miss *= 1 - Fraction(1, 1 << remaining)
            value += miss
        return value

    previous = expected_misses()
    assert previous == len(candidates) - expected_gain
    for i, row in enumerate(rows):
        for bit in range(n // 2):
            if bit in fixed[i]:
                continue
            scores = []
            for value in (0, 1):
                fixed[i][bit] = value
                scores.append(expected_misses())
            assert sum(scores) / 2 == previous
            value = int(scores[1] < scores[0])
            fixed[i][bit] = value
            previous = scores[value]
    new_rows = [
        oriented(row, tuple(assignment[i] for i in range(n // 2)))
        for row, assignment in zip(rows, fixed)
    ]
    new = row_counts(new_rows, ranks)
    assert set(old) <= set(new)
    gain = len(set(new) - set(old))
    assert gain >= expected_gain
    print(
        f"Protected parallel product formula: {runs} assignments, "
        f"expected gain={expected_gain}, deterministic gain={gain}"
    )


def product_fraction(values):
    answer = Fraction(1)
    for value in values:
        answer *= value
    return answer


def check_explicit_and_large_updates():
    row = tuple(range(16))
    ranks = (6, 7, 8, 9, 10)
    external = row_counts([row], ranks)
    caps = dict.fromkeys(ranks, 1)
    forms = window_forms(row, ranks)
    pins = protection(forms, external, caps)
    assert not pins
    patterns = useful_patterns(forms, external, caps, pins)
    assert Counter(len(required) for _, required in patterns) == {1: 32, 2: 72}
    new, cost, _ = folded_oracle(row, 2, ranks, external, caps)
    gain = conditional_cost(row, ranks, external, caps) - cost
    assert gain == 56
    assert len(row_counts([row, new], ranks)) == 136
    assert len(compiled(row, 2)) + len(compiled(new, 2)) == 40
    print("Explicit no-loss update: 80 -> 136 band targets, unchanged length 40")

    rng = Random(0x64E9A61)
    row = tuple(range(64))
    ranks = tuple(range(30, 35))
    caps = dict.fromkeys(ranks, 1)
    others = [oriented(row, tuple(rng.randrange(2) for _ in range(32))) for _ in range(3)]
    external = row_counts(others, ranks)
    new, cost, bits = folded_oracle(row, 2, ranks, external, caps)
    gain = conditional_cost(row, ranks, external, caps) - cost
    assert gain >= 0
    for i in range(32):
        neighbor = bits[:i] + (1 - bits[i],) + bits[i + 1 :]
        assert conditional_cost(oriented(row, neighbor), ranks, external, caps) >= cost
    print(f"64-coordinate folded oracle over 2^32 row variants: zero-load gain={gain}")


def fixed_budget_experiment():
    rng = Random(0xBADA55)
    n, h = 12, 2
    b = n // 2
    ranks = tuple(range(b - h, b + h + 1))
    caps = dict.fromkeys(ranks, 1)
    width = comb(n, b)
    count = width // (n + 2 * h)
    rows = []
    for _ in range(count):
        row = list(range(n))
        rng.shuffle(row)
        rows.append(tuple(row))
    loads = row_counts(rows, ranks)
    total = sum(comb(n, s) for s in ranks)
    history = [total - len(loads)]
    for sweep in range(12):
        for i, row in enumerate(rows):
            old_deck = set(row_counts([row], ranks))
            for target in old_deck:
                loads[target] -= 1
                if not loads[target]:
                    del loads[target]
            frame = row[sweep % 2 :] + row[: sweep % 2]
            new, value, _ = folded_oracle(frame, h, ranks, loads, caps)
            old_value = conditional_cost(row, ranks, loads, caps)
            assert value <= old_value
            rows[i] = new
            loads.update(set(row_counts([new], ranks)))
        history.append(total - len(loads))
        assert history[-1] <= history[-2]
    word = [letter for row in rows for letter in compiled(row, h)]
    actual_holes = (1 << n) - 1 - len(literal_targets(word))
    assert len(word) == count * (n + 2 * h) <= width
    print(
        f"Fixed-budget oracle experiment: n={n}, rows={count}, "
        f"length={len(word)}, width={width}, band-hole history={history}, "
        f"final actual nonempty holes={actual_holes}"
    )


if __name__ == "__main__":
    check_geometry_and_rounding()
    check_parallel_protection()
    check_explicit_and_large_updates()
    fixed_budget_experiment()
