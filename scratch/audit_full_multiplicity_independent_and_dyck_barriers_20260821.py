#!/usr/bin/env python3
import itertools
import math


def is_prime(n):
    return n >= 2 and all(n % d for d in range(2, math.isqrt(n) + 1))


def dyck_words(k):
    def rec(pos, rises, height, word):
        if pos == 2 * k:
            if height == 0:
                yield tuple(word)
            return
        if rises < k:
            word.append(1)
            yield from rec(pos + 1, rises + 1, height + 1, word)
            word.pop()
        if pos - rises < k and height:
            word.append(0)
            yield from rec(pos + 1, rises, height - 1, word)
            word.pop()

    yield from rec(0, 0, 0, [])


def clustered_checks():
    for b in (101, 211, 401, 809, 1601):
        assert is_prime(b)
        qmax = max(1, int(b ** 0.30))
        central_l = (math.sqrt(b) / qmax) ** 0.5
        c = [math.comb(b, j) for j in range(b + 1)]
        worst_endpoint = 0.0
        worst_internal = 0.0
        lower_fractions = []
        for q in range(1, qmax + 1):
            m_q = math.comb(2 * b, b + q)
            miss_weight = 0.0
            for s in range(q, b + 1):
                profile = c[s] * c[s - q]
                lam = []
                lam.append((b - s - q + 1) * c[s] / (b * c[s - q]))
                for z in range(1, q):
                    lam.append(2 * c[s - z] ** 2 / (b * c[s] * c[s - q]))
                lam.append((s - 2 * q + 1) * c[s - q] / (b * c[s]))
                if all(x <= 1 for x in lam):
                    miss_weight += (profile / m_q) * math.prod(1 - x for x in lam)
                x = s - (b + q) / 2
                if abs(x) <= central_l * math.sqrt(b):
                    worst_endpoint = max(
                        worst_endpoint, abs(lam[0] - 0.5), abs(lam[-1] - 0.5)
                    )
                    if len(lam) > 2:
                        worst_internal = max(
                            worst_internal,
                            max(abs(b * y - 2) for y in lam[1:-1]),
                        )
            lower_fractions.append(miss_weight)
        print(
            "clustered PASS",
            b,
            "Q",
            qmax,
            "min coupon lower fraction",
            min(lower_fractions),
            "central endpoint error",
            worst_endpoint,
            "central scaled-interior error",
            worst_internal,
        )


def dyck_checks():
    for k in range(1, 5):
        n = 2 * k + 1
        targets = [
            sum(1 << x for x in subset)
            for subset in itertools.combinations(range(n), k)
        ]
        target_index = {target: i for i, target in enumerate(targets)}
        target_degree = [0] * len(targets)
        pair_ab = 0
        complement_codegree = {}
        mountain_slot_degree = 0
        permutations = list(itertools.permutations(range(k)))
        a_target = sum(1 << x for x in range(1, k + 1))
        b_target = sum(1 << x for x in range(k + 1, 2 * k + 1))
        for word in dyck_words(k):
            rise_positions = [i + 1 for i, bit in enumerate(word) if bit]
            fall_positions = [i + 1 for i, bit in enumerate(word) if not bit]
            mountain = word == (1,) * k + (0,) * k
            for pa in permutations:
                base = [0] * n
                for pos, value in zip(rise_positions, pa):
                    base[pos] = value + 1
                for pb in permutations:
                    pi = base.copy()
                    for pos, value in zip(fall_positions, pb):
                        pi[pos] = k + value + 1
                    deck = []
                    for start in range(n):
                        target = 0
                        for offset in range(k):
                            target |= 1 << pi[(start + offset) % n]
                        deck.append(target)
                        target_degree[target_index[target]] += 1
                    assert len(set(deck)) == n
                    if a_target in deck and b_target in deck:
                        pair_ab += 1
                    deck_set = set(deck)
                    nonzero_mask = ((1 << n) - 1) ^ 1
                    for target in deck:
                        if target & 1:
                            continue
                        complement = nonzero_mask ^ target
                        if target < complement and complement in deck_set:
                            complement_codegree[target] = (
                                complement_codegree.get(target, 0) + 1
                            )
                    if mountain:
                        mountain_slot_degree += 1
        degree = math.factorial(k) ** 2
        assert min(target_degree) == max(target_degree) == degree
        assert mountain_slot_degree == degree
        assert pair_ab == degree
        a_mask = sum(1 << x for x in range(1, k + 1))
        for target, observed in complement_codegree.items():
            a = (target & a_mask).bit_count()
            if a <= k / 2:
                continue
            ballot = math.comb(k, a) - (
                math.comb(k, a + 1) if a + 1 <= k else 0
            )
            predicted = ballot**2 * (math.factorial(a) * math.factorial(k - a)) ** 2
            assert observed == predicted, (k, a, observed, predicted)
        print("Dyck PASS", k, "degree/codegree", degree)


if __name__ == "__main__":
    clustered_checks()
    dyck_checks()
    print("ALL FULL-MULTIPLICITY/DYCK CHECKS PASS")
