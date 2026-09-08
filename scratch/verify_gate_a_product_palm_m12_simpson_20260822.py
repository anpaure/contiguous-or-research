#!/usr/bin/env python3
"""Exact type calculation for the non-punctured m=12 product Simpson no-go."""

from fractions import Fraction
from math import comb


ORDER = 12


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
        # The common B-target is retained with probability 1/2; conditional
        # on it, the twelve B-row private targets are independent fair bits.
        output = {0: Fraction(1, 2)}
        for extra, probability in binomial_distribution(12, Fraction(1, 2)).items():
            output[extra] = output.get(extra, Fraction(0)) + probability / 2
        return output
    if k == 12:
        # The common A-target is a fair bit; conditional on it, each A-row
        # needs two independent private fair bits.
        output = {0: Fraction(1, 2)}
        for extra, probability in binomial_distribution(12, Fraction(1, 4)).items():
            output[extra] = output.get(extra, Fraction(0)) + probability / 2
        return output
    return convolve(
        binomial_distribution(k, Fraction(1, 4)),
        binomial_distribution(12 - k, Fraction(1, 2)),
    )


def main():
    types = []
    for k in range(13):
        forced_targets = (
            1 + int(k > 0) + int(k < 12) + k + 2 * (12 - k)
        )
        weight = Fraction(comb(12, k) ** 2, 2**forced_targets)
        distribution = extra_degree_distribution(k)
        assert sum(distribution.values()) == 1
        tail_probability = 1 - distribution[0]
        mean_degree = 12 + sum(extra * p for extra, p in distribution.items())
        fixed_covariance = sum(
            p * (12 + extra) * int(extra >= 1)
            for extra, p in distribution.items()
        ) - mean_degree * tail_probability
        assert fixed_covariance == (1 - tail_probability) * (mean_degree - 12)
        assert fixed_covariance >= 0
        types.append(
            {
                "k": Fraction(k),
                "weight": weight,
                "p": tail_probability,
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

    assert covariance_k_p == Fraction(
        -48859110891261717, 16205463862068315136
    )
    assert covariance_mu_p == Fraction(
        201910008730439973, 259287421793093042176
    )
    assert within == Fraction(40946898723, 2061107740672)

    base = within + covariance_mu_p
    assert base == Fraction(669128902416437229, 32410927724136630272)

    def full_covariance(external_multiplicity):
        return base + Fraction(external_multiplicity, 2) * covariance_k_p

    assert full_covariance(13) == Fraction(
        33960460830034908, 32410927724136630272
    )
    assert full_covariance(14) == Fraction(
        -14898650061226809, 32410927724136630272
    )
    assert all(full_covariance(m) >= 0 for m in range(14))
    assert full_covariance(14) < 0

    print("PASS: exact non-punctured m=12 product Palm Simpson obstruction")
    print("within-carrier covariance", within)
    print("between k/tail covariance", covariance_k_p)
    print("M=13 full covariance", full_covariance(13))
    print("M=14 full covariance", full_covariance(14))


if __name__ == "__main__":
    main()
