#!/usr/bin/env python3
"""Exact/arbitrary-precision checks for the growing-rank paired-wreath audit.

Run on H100.  This checks finite identities and the signs of all asymptotic
comparisons used in the audit; it does not claim the open restricted-P nibble.
"""

from __future__ import annotations

from math import comb, exp, factorial, lgamma, log, sqrt


def exact_profile(r: int) -> None:
    n0 = comb(2 * r + 1, r)
    n_j = (r + 1) * n0 // 2
    degree = r * factorial(r) ** 2
    codegree = (r - 1) * factorial(r - 1) ** 2

    assert 2 * n_j == (r + 1) * n0
    assert codegree * r**3 == degree * (r - 1)

    # Endpoint-disjoint full-J matchings cover at most this many J vertices.
    cover_cap = r * (n0 // (2 * r))
    assert cover_cap <= n0 // 2
    assert 2 * cover_cap <= n0

    # Vizing: a largest colour class in an (r+2)-edge-colouring.
    edge_count = n_j
    vizing_size_floor = edge_count // (r + 2)
    assert 2 * vizing_size_floor >= n0 * (r + 1) // (r + 2) - 2

    for t in range(2, r + 1):
        high = (r - t + 1) * factorial(r - t + 1) ** 2
        assert 1 <= high <= codegree


def log_profile(r: int) -> dict[str, float]:
    log_d = log(r) + 2 * lgamma(r + 1)
    log_c = log(r - 1) + 2 * lgamma(r)
    log_ratio = log_c - log_d

    # Log of e^(2r) C log(D) / D: must diverge to +infinity.
    log_abkv_hyp_ratio = 2 * r + log_ratio + log(log_d)

    # Log of r * (C log(1+C)/D)^(1/(r-1)).  Since C is huge,
    # log(log(1+C)) = log(log C) up to an exponentially tiny error.
    log_leave_coeff = log(r) + (log_ratio + log(log_c)) / (r - 1)

    eps_max = -log_ratio / log_d
    glock_exponent = eps_max**3 * log_d
    log_n_j = log(r + 1) - log(2) + (
        lgamma(2 * r + 2) - lgamma(r + 1) - lgamma(r + 2)
    )

    b_pair = sqrt(exp(-log_ratio))
    grable_parameter = r * exp(log_ratio) * log_n_j
    return {
        "r": float(r),
        "log_D": log_d,
        "log_N": log_n_j,
        "C_over_D": exp(log_ratio),
        "rC_over_D": r * exp(log_ratio),
        "log_ABKV_hyp_ratio": log_abkv_hyp_ratio,
        "ABKV_leave_coefficient": exp(log_leave_coeff),
        "eps_max": eps_max,
        "eps3_logD": glock_exponent,
        "B_pair": b_pair,
        "B_pair_over_logD": b_pair / log_d,
        "rC_logN_over_D": grable_parameter,
    }


def main() -> None:
    for r in range(2, 31):
        exact_profile(r)

    rows = [log_profile(r) for r in (8, 16, 32, 64, 128, 256, 512)]
    for a, b in zip(rows, rows[1:]):
        assert b["log_ABKV_hyp_ratio"] > a["log_ABKV_hyp_ratio"]
        assert b["ABKV_leave_coefficient"] > a["ABKV_leave_coefficient"]
        assert b["eps3_logD"] < a["eps3_logD"]
        assert b["B_pair_over_logD"] < a["B_pair_over_logD"]

    assert rows[-1]["log_ABKV_hyp_ratio"] > 100
    assert rows[-1]["ABKV_leave_coefficient"] > 100
    assert rows[-1]["eps3_logD"] < 0.01
    assert rows[-1]["B_pair_over_logD"] < 0.1
    assert abs(rows[-1]["rC_logN_over_D"] - log(4)) < 0.02
    assert all(1.2 < row["rC_logN_over_D"] < 1.5 for row in rows)

    print("PASS")
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
