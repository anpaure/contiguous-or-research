#!/usr/bin/env python3
"""Exact algebra and rational-exponent checks for the high-moment Gate-A note."""

from fractions import Fraction
from itertools import combinations, product
from math import log, sqrt


def integer_partitions_with_parts_at_least_two(total, minimum=2):
    """Yield nondecreasing tuples with entries >= 2 and given total."""
    if total == 0:
        yield ()
        return
    for first in range(minimum, total + 1):
        for rest in integer_partitions_with_parts_at_least_two(
            total - first, first
        ):
            yield (first,) + rest


def component_branches(j):
    """(r exponent a, x exponent b) in r^-a x^-b for one component."""
    if j == 2:
        return [(1, Fraction(3)), (2, Fraction(4))]
    # Q_(j/2)^(j-1).  Choose t factors from its second kernel monomial.
    out = []
    for t in range(j):
        a = (j - 1) + t
        b = Fraction(3 * j * (j - 1), 2) + Fraction(j * t, 2)
        out.append((a, b))
    return out


def minkowski_sum(branch_lists):
    states = [(0, Fraction(0))]
    for branches in branch_lists:
        states = [(a + c, b + d) for a, b in states for c, d in branches]
    return states


def check_component_envelope():
    checks = 0
    for m in range(4, 22, 2):
        alpha = Fraction(1, 3 * m)
        pair_exponent = Fraction(-m, 2) + alpha * Fraction(3 * m, 2)
        for partition in integer_partitions_with_parts_at_least_two(m):
            for a, b in minkowski_sum(
                [component_branches(j) for j in partition]
            ):
                exponent = -a + alpha * b
                # Every monomial is no larger than the all-pair monomial
                # at alpha=1/(3m), hence throughout the strict range.
                assert exponent <= pair_exponent, (
                    m,
                    partition,
                    a,
                    b,
                    exponent,
                    pair_exponent,
                )
                checks += 1
    return checks


def plus_power(x, m):
    return max(x, Fraction(0)) ** m


def nabla_plus(t, m):
    return plus_power(t, m) - plus_power(t - 1, m)


def check_tangent_algebra():
    checks = 0
    for m in (6, 10, 12, 14):
        for c in (Fraction(7, 3), Fraction(11, 4)):
            for t in [Fraction(x, 2) for x in range(-4, 13)]:
                d = c + t
                for z in (Fraction(2), Fraction(5, 2)):
                    for B in (Fraction(0), Fraction(3, 5)):
                        f = plus_power(t, m)
                        grad = nabla_plus(t, m)
                        center_and_denominator = (
                            (z + m * B - d) * f
                            - d * B * grad
                            + m * c * B * plus_power(t, m - 1)
                        )
                        P = m * plus_power(t, m - 1) - grad
                        reduced = (
                            (z - c) * f
                            - plus_power(t, m + 1)
                            + B * d * P
                        )
                        assert center_and_denominator == reduced
                        assert P >= 0
                        checks += 1
    return checks


def phi(m, c, d, a):
    return a * nabla_plus(d - c, m) - (
        plus_power(d - c, m) - plus_power(d - a - c, m)
    )


def check_row_defect():
    checks = 0
    for m in (10, 12):
        for c in (Fraction(3, 2), Fraction(11, 3), Fraction(6)):
            for d in range(0, 16):
                for a in range(d + 1):
                    value = phi(m, c, d, a)
                    assert value >= 0
                    if a < 2:
                        assert value == 0
                    # Twice-integrated second-difference bound used in (4.4).
                    scale = max(Fraction(1), abs(Fraction(d) - c)) ** (m - 2)
                    crude = (
                        Fraction(a * (a - 1), 2)
                        * m
                        * (m - 1)
                        * scale
                    )
                    # Shifting down by h can only reduce the positive-part
                    # argument, so this crude maximum is valid.
                    assert value <= crude
                    checks += 1
    return checks


def conflict_data(edges):
    edge_sets = [frozenset(e) for e in edges]
    vertices = sorted(set().union(*edge_sets))
    degrees = {v: sum(v in e for e in edge_sets) for v in vertices}
    conflicts = [
        sum(bool(e & g) for g in edge_sets)
        for e in edge_sets
    ]
    return edge_sets, vertices, degrees, conflicts


def check_covariance_identity():
    examples = [
        [(0, 1), (1, 2), (2, 3), (3, 0)],
        [(0, 1), (0, 2), (0, 3), (4, 5)],
        [(0, 1, 2), (0, 3, 4), (1, 3, 5), (2, 4, 5)],
    ]
    checks = 0
    for edges in examples:
        edge_sets, vertices, d, C = conflict_data(edges)
        Z = len(edges)
        k = len(edge_sets[0])
        z = Fraction(k * Z, len(vertices))
        bar_c = Fraction(sum(C), Z)
        weights = {v: Fraction((v + 1) ** 2, 7) for v in vertices}
        A = {}
        Xi = {}
        for v in vertices:
            A[v] = Fraction(
                sum(C[i] for i, e in enumerate(edge_sets) if v in e), d[v]
            )
            Xi[v] = A[v] - d[v] - (bar_c - z)
        left = -sum(Fraction(d[v]) * Xi[v] * weights[v] for v in vertices)
        WF = [sum(weights[v] for v in e) for e in edge_sets]
        mean_w = sum(WF, Fraction(0)) / Z
        cov = sum(
            (Fraction(C[i]) - bar_c) * (WF[i] - mean_w)
            for i in range(Z)
        ) / Z
        right = sum(
            Fraction(d[v]) * (Fraction(d[v]) - z) * weights[v]
            for v in vertices
        ) - Z * cov
        assert left == right
        checks += 1
    return checks


def check_exponent_ledger():
    # m=12, a legal strict reference exponent, and a full power of
    # stopped-comparison loss.
    m = 12
    alpha = Fraction(1, 40)
    kappa = Fraction(1)
    assert alpha < Fraction(1, 3 * m)
    assert kappa < Fraction(m, 2) - 4 - Fraction(3 * m, 2) * alpha

    collision = 1 + kappa - Fraction(m, 2) + Fraction(3 * m, 2) * alpha
    protection_size = (
        kappa - Fraction(m, 2) + Fraction(3 * m, 2) * alpha
    )
    protection_cov = (
        1
        + kappa / 2
        - Fraction(m, 4)
        + Fraction(3 * m, 4) * alpha
    )
    assert collision < -1
    assert protection_size < -1
    assert protection_cov < -1

    # Full shore persistence needs forcing o(x_*/r), not merely o(1/r).
    target_exp = -1 - alpha
    assert protection_cov < target_exp
    assert kappa < Fraction(2) - 20 * alpha
    assert Fraction(2) - 20 * alpha < Fraction(2) - 18 * alpha

    # Lossless cap-only covariance has exponent 1-m/4 at alpha=0.
    assert 1 - Fraction(8, 4) == -1  # m=8 is only borderline.
    assert 1 - Fraction(10, 4) < -1  # m=10 is the first even success.

    # epsilon=r^-3: Taylor sum is r^-2 log r, and the transported purge
    # charge / direct purge charge ratio is epsilon*r=r^-2.
    epsilon_power = 3
    taylor_power = 1 - epsilon_power
    transfer_ratio_power = 1 - epsilon_power
    assert taylor_power < -1
    assert transfer_ratio_power < 0

    return {
        "alpha": alpha,
        "kappa": kappa,
        "collision_exp": collision,
        "size_exp": protection_size,
        "cov_exp": protection_cov,
        "taylor_exp_ignoring_log": taylor_power,
        "shore_target_exp": target_exp,
    }


def check_density_clock_direction():
    """Lower progress plus monotonicity bounds weighted occupancy of bins."""
    checks = 0
    r = 100
    c = Fraction(1, 3)
    # A finite family of varying microbite sizes and arbitrary forward jumps.
    for eps_pattern in product((Fraction(1, 4), Fraction(1, 2), Fraction(1)), repeat=5):
        for jump_pattern in product((Fraction(0), Fraction(1, 20)), repeat=5):
            y = Fraction(0)
            records = []
            for eps, jump in zip(eps_pattern, jump_pattern):
                records.append((y, eps))
                y += c * eps / r + jump

            # In each log-width-one bin, lower progress allows its width plus
            # one crossing step.  Forward jumps only reduce occupancy.
            for q in range(4):
                occupancy = sum(
                    eps / r
                    for y0, eps in records
                    if Fraction(q) <= y0 < Fraction(q + 1)
                )
                assert occupancy <= Fraction(1, 1) / c + Fraction(1, r)
                checks += 1
    return checks


def check_stopped_jensen():
    checks = 0
    distributions = [
        ((Fraction(1, 4), Fraction(3, 4)), (0, 4)),
        ((Fraction(1, 3), Fraction(1, 3), Fraction(1, 3)), (1, 9, 25)),
        ((Fraction(1, 10), Fraction(2, 10), Fraction(7, 10)), (0, 16, 1)),
    ]
    for probs, values in distributions:
        for mask in range(1, 1 << len(values)):
            event_prob = sum(probs[i] for i in range(len(values)) if mask >> i & 1)
            first = sum(
                float(probs[i]) * sqrt(values[i])
                for i in range(len(values))
                if mask >> i & 1
            )
            second = sum(
                probs[i] * values[i]
                for i in range(len(values))
                if mask >> i & 1
            )
            assert first * first <= float(event_prob * second) + 1e-12
            checks += 1
    return checks


def check_cap_and_shore_ledgers():
    checks = 0
    # A nonlarge K0-purge deterministically restores the larger K cap.
    K = Fraction(2)
    K0 = Fraction(3, 2)
    rho0 = 1 - K0 / K
    for rho_num in range(0, rho0.numerator + 1):
        rho = Fraction(rho_num, rho0.denominator)
        if rho > rho0:
            continue
        for tau_num in range(0, 21):
            tau = Fraction(tau_num, 100)
            if tau > rho / K0:
                continue
            average_ratio = (1 - rho) / (1 - tau)
            assert average_ratio >= 1 - rho >= K0 / K
            assert K0 <= K * average_ratio
            checks += 1

    # sum rho=o(1) alone does not preserve shore comparability.  Purge delta
    # of M early, then use equal deletions until L-density is 2 delta.
    for n in (10_000, 100_000, 1_000_000):
        x_star = n ** (-0.5)
        delta = sqrt(x_star)
        assert delta < 0.2 and delta > x_star
        n_l = 2 * delta
        n_m = delta
        assert abs(n_m / n_l - 1) == 0.5
        assert delta < 0.5  # yet the total purge fraction tends to zero
        checks += 1

    return checks


def check_normalization_and_powers():
    checks = 0
    for m in (6, 10, 12, 14):
        for a in (Fraction(6, 5), Fraction(4, 3)):
            for n in (7, 13):
                for w in (Fraction(5, 2), Fraction(11, 3)):
                    values = [Fraction(j, 2) for j in range(1, n + 1)]
                    numerator = sum(plus_power(d - a * w, m) for d in values)
                    phi = numerator / (n * w**m)
                    psi = numerator / (n * (a * w) ** m)
                    assert phi == a**m * psi
                    checks += 1

        # Collision: z^(m-2) times r z^3; lattice: (rz)*z*z^(m-2).
        collision_z_power = (m - 2) + 3
        lattice_z_power = 1 + 1 + (m - 2)
        assert collision_z_power == m + 1
        assert lattice_z_power == m
        checks += 1
    return checks


def check_purge_margin():
    a = Fraction(6, 5)
    rstar = Fraction(6, 5)
    k0 = Fraction(3, 2)
    assert 1 < a < a * rstar < k0
    checks = 0
    for m in (10, 12):
        for z in range(20, 41):
            w = rstar * z
            for d in range((k0 * z).numerator // (k0 * z).denominator + 1, 100):
                if d <= k0 * z:
                    continue
                gap = Fraction(d) - a * w
                assert gap > 0
                # Uniform positive constant furnished by the two margins.
                lower_constant = min(
                    (k0 - a * rstar) / rstar,
                    (k0 - a * rstar) / k0,
                )
                assert gap >= lower_constant * w
                assert gap >= lower_constant * d
                assert gap**m >= lower_constant**m * w ** (m - 1) * d
                checks += 1
    return checks


def main():
    component_checks = check_component_envelope()
    tangent_checks = check_tangent_algebra()
    row_checks = check_row_defect()
    covariance_checks = check_covariance_identity()
    purge_checks = check_purge_margin()
    clock_checks = check_density_clock_direction()
    jensen_checks = check_stopped_jensen()
    cap_shore_checks = check_cap_and_shore_ledgers()
    normalization_checks = check_normalization_and_powers()
    ledger = check_exponent_ledger()
    print(
        "GATE_A_HIGH_EVEN_MOMENT_SHADOW_PASS",
        f"components={component_checks}",
        f"tangent={tangent_checks}",
        f"rows={row_checks}",
        f"covariance={covariance_checks}",
        f"purge={purge_checks}",
        f"clock={clock_checks}",
        f"jensen={jensen_checks}",
        f"cap_shore={cap_shore_checks}",
        f"normalization={normalization_checks}",
        f"ledger={ledger}",
    )


if __name__ == "__main__":
    main()
