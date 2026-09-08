#!/usr/bin/env python3
"""Exact rational regression checks for the one-step-lag absorption theorem."""

from fractions import Fraction as F
import hashlib
import random
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "MATH_THEOREM_GATE_A_ONE_STEP_LAG_EROSION_ABSORPTION_20260822.md"
RNG = random.Random(20260822)


def mean(mu, vals):
    return sum((mu[x] * vals[x] for x in mu), F(0))


def cov(mu, u, v):
    return mean(mu, {x: u[x] * v[x] for x in mu}) - mean(mu, u) * mean(mu, v)


def one_trial(depth):
    # A state name is its complete path, so its labelled parent is unique.
    mu = {(): F(1)}
    phi = {(): F(RNG.randrange(0, 20), 5)}
    ancestor_phi = {(): phi[()]}
    layers = []

    for j in range(depth):
        s = {}
        rem = {}
        kernels = {}
        child_phi = {}
        child_ancestor_phi = {}
        for x in mu:
            s[x] = F(RNG.randrange(0, 13), 60)  # at most 1/5
            rem[x] = F(RNG.randrange(0, int(s[x] * 120) + 1), 240)
            if rem[x] > s[x] / 2:
                rem[x] = s[x] / 2
            a = 1 - s[x] + rem[x]
            split = F(RNG.randrange(1, 10), 10)
            y0, y1 = x + (0,), x + (1,)
            kernels[x] = {y0: a * split, y1: a * (1 - split)}
            for y in (y0, y1):
                loss_steps = RNG.randrange(0, 6)
                loss = min(phi[x], F(loss_steps, 10))
                child_phi[y] = phi[x] - loss
                child_ancestor_phi[y] = phi[x]

        abar = mean(mu, {x: sum(kernels[x].values(), F(0)) for x in mu})
        mu_child = {}
        for x in mu:
            for y, kxy in kernels[x].items():
                mu_child[y] = mu_child.get(y, F(0)) + mu[x] * kxy / abar

        A = mean(mu, phi)
        A_child = mean(mu_child, child_phi)
        a_vals = {x: sum(kernels[x].values(), F(0)) for x in mu}
        erosion_num = F(0)
        for x in mu:
            for y, kxy in kernels[x].items():
                erosion_num += mu[x] * kxy * (phi[x] - child_phi[y])
        erosion = erosion_num / abar

        exact_rhs = A + cov(mu, a_vals, phi) / abar - erosion
        assert A_child == exact_rhs

        eps = max(rem.values(), default=F(0))
        L = max(s.values(), default=F(0))
        g = 1 + eps / abar
        lam = L / abar
        if j == 0:
            B = max(F(0), -cov(mu, s, phi)) / abar
            previous_erosion = F(0)
        else:
            B = max(F(0), -cov(mu, s, ancestor_phi)) / abar
            previous_erosion = layers[-1]["erosion"]
        one_step_rhs = g * A + B + lam * previous_erosion - erosion
        assert A_child <= one_step_rhs
        assert lam <= g

        layers.append(
            dict(A=A, A_child=A_child, g=g, lam=lam, B=B, erosion=erosion)
        )
        mu, phi, ancestor_phi = mu_child, child_phi, child_ancestor_phi

    # Verify the fully unrolled inequality (2.6).
    rhs = layers[0]["A"]
    for layer in layers:
        rhs = layer["g"] * rhs + layer["B"]
    assert layers[-1]["A_child"] <= rhs
    return sum(len(layer) if isinstance(layer, dict) else 0 for layer in layers)


def deterministic_edge_cases():
    # Complete erosion of the tail is allowed and causes no division by A_j.
    mu = {0: F(1, 2), 1: F(1, 2)}
    phi = {0: F(0), 1: F(1)}
    s = {0: F(1, 10), 1: F(1, 5)}
    rem = {0: F(0), 1: F(0)}
    a = {x: 1 - s[x] + rem[x] for x in mu}
    abar = mean(mu, a)
    # Both surviving children have zero test value.
    A0 = mean(mu, phi)
    erosion = (sum(mu[x] * a[x] * phi[x] for x in mu)) / abar
    A1 = F(0)
    assert A1 == A0 + cov(mu, a, phi) / abar - erosion
    eps = F(0)
    g = 1 + eps / abar
    B = max(F(0), -cov(mu, s, phi)) / abar
    assert A1 <= g * A0 + B - erosion


def main():
    assert NOTE.exists()
    required = [
        "A_{j+1}=A_j+",
        "one-step-lag",
        "ancestor-row predictable-rate regression",
        "No child-degree column ratio occurs",
    ]
    text = NOTE.read_text()
    for token in required:
        assert token in text, token

    deterministic_edge_cases()
    checks = 0
    for depth in range(1, 7):
        for _ in range(120):
            checks += one_trial(depth)

    digest = hashlib.sha256(NOTE.read_bytes()).hexdigest()
    print(
        "GATE_A_ONE_STEP_LAG_EROSION_ABSORPTION_PASS",
        f"trials={6 * 120}",
        f"layer_checks={checks}",
        f"note_sha256={digest}",
    )


if __name__ == "__main__":
    main()

