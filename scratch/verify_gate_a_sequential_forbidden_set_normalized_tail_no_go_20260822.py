#!/usr/bin/env python3
"""Exact m=12 normalized-tail no-go for the forbidden-set representation."""

from fractions import Fraction
from itertools import permutations
from math import comb


ORDER = 12
CUTOFF = 11


def falling(n, k):
    if n < k:
        return 0
    output = 1
    for j in range(k):
        output *= n - j
    return output


def phi(d):
    if d < ORDER:
        return Fraction(0)
    return Fraction(max(d - CUTOFF, 0) ** ORDER, falling(d, ORDER))


def binomial_distribution(number, probability):
    return {
        successes: Fraction(comb(number, successes))
        * probability**successes
        * (1 - probability) ** (number - successes)
        for successes in range(number + 1)
    }


def convolve(left, right):
    output = {}
    for a, pa in left.items():
        for b, pb in right.items():
            output[a + b] = output.get(a + b, Fraction(0)) + pa * pb
    return output


def extra_degree_distribution(carrier_type):
    k = carrier_type
    if k == 0:
        output = {0: Fraction(1, 2)}
        for extra, probability in binomial_distribution(
            12, Fraction(1, 2)
        ).items():
            output[extra] = output.get(extra, Fraction(0)) + probability / 2
        return output
    if k == 12:
        output = {0: Fraction(1, 2)}
        for extra, probability in binomial_distribution(
            12, Fraction(1, 4)
        ).items():
            output[extra] = output.get(extra, Fraction(0)) + probability / 2
        return output
    return convolve(
        binomial_distribution(k, Fraction(1, 4)),
        binomial_distribution(12 - k, Fraction(1, 2)),
    )


def exact_small_priority_check():
    # Exhaust the d=5,c=2,m=2 version of the priority construction.
    # Higher integer parameters follow from the identical symmetry count.
    rows = range(5)
    carrier = (0, 1)
    success = 0
    total = 0
    for priority_order in permutations(rows):
        rank = {row: index for index, row in enumerate(priority_order)}
        alive = set(rows)
        good = True
        for j, row in enumerate(carrier):
            forbidden_size = 2 - j
            forbidden = set(
                sorted(alive, key=lambda item: rank[item], reverse=True)[
                    :forbidden_size
                ]
            )
            if row in forbidden:
                good = False
                break
            alive.remove(row)
        total += 1
        success += int(good)
    assert Fraction(success, total) == Fraction(3**2, falling(5, 2))

    # Literal m=12 product formula.
    for d in range(12, 40):
        sequential = Fraction(1)
        for j in range(ORDER):
            sequential *= Fraction(d - CUTOFF, d - j)
        assert sequential == phi(d)


def main():
    exact_small_priority_check()

    types = []
    for k in range(13):
        forced_targets = (
            1 + int(k > 0) + int(k < 12) + k + 2 * (12 - k)
        )
        weight = Fraction(comb(12, k) ** 2, 2**forced_targets)
        distribution = extra_degree_distribution(k)
        assert sum(distribution.values()) == 1
        tail_likelihood = sum(
            probability * phi(12 + extra)
            for extra, probability in distribution.items()
        )
        mean_degree = 12 + sum(
            extra * probability for extra, probability in distribution.items()
        )
        degree_tail_product = sum(
            probability * (12 + extra) * phi(12 + extra)
            for extra, probability in distribution.items()
        )
        fixed_covariance = degree_tail_product - mean_degree * tail_likelihood
        assert fixed_covariance >= 0
        types.append(
            {
                "k": Fraction(k),
                "weight": weight,
                "p": tail_likelihood,
                "mu": mean_degree,
                "within": fixed_covariance,
            }
        )

    total_weight = sum(item["weight"] for item in types)
    assert total_weight == Fraction(125800033, 67108864)

    def expectation(key):
        return sum(item["weight"] * item[key] for item in types) / total_weight

    mean_k = expectation("k")
    mean_p = expectation("p")
    mean_mu = expectation("mu")
    covariance_k_p = sum(
        item["weight"]
        * (item["k"] - mean_k)
        * (item["p"] - mean_p)
        for item in types
    ) / total_weight
    covariance_mu_p = sum(
        item["weight"]
        * (item["mu"] - mean_mu)
        * (item["p"] - mean_p)
        for item in types
    ) / total_weight
    within = expectation("within")
    base = within + covariance_mu_p

    assert mean_p == Fraction(
        60887760922742269, 82272825462856089600
    )
    assert covariance_k_p == Fraction(
        -103531504816623590706626628809,
        499782312714715254340487007436800,
    )
    assert covariance_mu_p == Fraction(
        580109326576358854794581638963,
        11195123804809621697226908966584320,
    )
    assert within == Fraction(
        124405554636853845816229,
        88991421844934028731351040,
    )
    assert base == Fraction(
        600199552291948973160317,
        413996966329221453837238272,
    )

    def full_covariance(external_multiplicity):
        return base + Fraction(external_multiplicity, 2) * covariance_k_p

    assert full_covariance(13) == Fraction(
        5908152554165649057718189,
        57209513818076379846667468800,
    )
    assert full_covariance(14) == Fraction(
        -304263390241370370174430601,
        999564625429430508680974014873600,
    )
    assert all(full_covariance(multiplicity) >= 0 for multiplicity in range(14))
    assert full_covariance(14) < 0

    print("PASS: sequential forbidden-set normalized-tail no-go")
    print("mean acceptance", mean_p)
    print("within-carrier covariance", within)
    print("between k/acceptance covariance", covariance_k_p)
    print("M=13 full covariance", full_covariance(13))
    print("M=14 full covariance", full_covariance(14))


if __name__ == "__main__":
    main()
