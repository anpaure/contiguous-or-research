#!/usr/bin/env python3
"""Finite audit for the fixed-order three-rank Cayley bank."""

from verify_gate_c_all_pairing_coherent_tour_orbit_20260822 import natural_tour


def rank_targets(b, state):
    middle, _, lower, upper = natural_tour(b, state)
    return {
        b - 1: tuple(lower),
        b: tuple(mask for _, mask in middle),
        b + 1: tuple(upper),
    }


def forbidden_differences(b):
    targets = [rank_targets(b, x) for x in range(1 << b)]
    bad = set()
    for h in range(1, 1 << b):
        collision = False
        # Translation invariance says checking every x is redundant, but
        # exhausting it independently audits the affine claim.
        for x in range(1 << b):
            y = x ^ h
            for rank in (b - 1, b, b + 1):
                if set(targets[x][rank]) & set(targets[y][rank]):
                    collision = True
                    break
            if collision:
                break
        if collision:
            bad.add(h)
    return targets, bad


def greedy_bank(b, bad):
    remaining = set(range(1 << b))
    bank = []
    while remaining:
        x = min(remaining)
        bank.append(x)
        remaining.remove(x)
        remaining.difference_update(x ^ h for h in bad)
    return bank


def audit_b(b):
    targets, bad = forbidden_differences(b)
    bound = 2 * b ** 3 + 8 * b ** 2 - 16 * b
    assert len(bad) <= bound

    bank = greedy_bank(b, bad)
    assert len(bank) * (bound + 1) >= 1 << b
    for rank in (b - 1, b, b + 1):
        seen = set()
        for x in bank:
            row = targets[x][rank]
            assert len(row) == len(set(row)) == b * (b - 1)
            assert not (seen & set(row))
            seen.update(row)
    print(
        f"PASS: b={b} forbidden={len(bad)} bound={bound} "
        f"greedy_bank={len(bank)}"
    )


def audit():
    for b in (3, 5, 7):
        audit_b(b)


if __name__ == "__main__":
    audit()
