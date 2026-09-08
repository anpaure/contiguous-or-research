#!/usr/bin/env python3
"""Finite audit for MATH_THEOREM_GATE_CQ_ORDERED_PORT_CROSS_JOIN_20260822.md."""

from itertools import permutations
from math import factorial


def windows(word, b):
    return [frozenset(word[i : i + b]) for i in range(b + 1)]


def legal_arc(A, B):
    b = len(A)
    return (
        len(B) == b
        and len(set(A)) == b
        and len(set(B)) == b
        and set(A).intersection(B) == {A[0]}
        and A[0] == B[-1]
    )


def triangular_clean(A, C, H):
    b = len(A)
    return all(
        A[r] != C[s]
        for s in range(max(0, H - 1))
        for r in range(b - H + 1 + s, b)
    )


def brute_clean(A, B, C, H):
    word = A + B + C
    g = len(A) + H
    for length in range(1, g + 1):
        for start in range(len(word) - length + 1):
            block = word[start : start + length]
            if len(set(block)) != length:
                return False
    return True


def falling(x, h):
    ans = 1
    for j in range(h):
        ans *= x - j
    return ans


def audit_b(b):
    omega = tuple(range(2 * b))
    A = tuple(range(b))
    B = tuple(range(b, 2 * b - 1)) + (0,)
    assert legal_arc(A, B)
    omitted = next(iter(set(omega) - set(A) - set(B)))

    # Lemma 1.1: reversal has the same middle path in reverse, and changing
    # the puncture pivot preserves all internal middle sets.
    support = windows(A + B, b)
    reverse_support = windows(tuple(reversed(B)) + tuple(reversed(A)), b)
    assert reverse_support == list(reversed(support))
    A_swap = (omitted,) + A[1:]
    B_swap = B[:-1] + (omitted,)
    assert legal_arc(A_swap, B_swap)
    assert windows(A_swap + B_swap, b)[1:-1] == support[1:-1]

    # Theorem 5.3: canonical continuation has orbit 2b-1 and the first
    # and third packets share exactly b-2 internal targets.
    canonical_arcs = []
    current_A, current_B = A, B
    seen_arcs = set()
    while (current_A, current_B) not in seen_arcs:
        seen_arcs.add((current_A, current_B))
        canonical_arcs.append((current_A, current_B))
        current_C = current_A[1:] + (current_B[0],)
        current_A, current_B = current_B, current_C
    assert (current_A, current_B) == (A, B)
    assert len(canonical_arcs) == 2 * b - 1
    internal = [set(windows(X + Y, b)[1:-1]) for X, Y in canonical_arcs]
    assert internal[0].isdisjoint(internal[1])
    assert len(internal[0].intersection(internal[2])) == b - 2
    for j in range(len(internal)):
        assert len(internal[j].intersection(internal[(j + 2) % len(internal)])) == b - 2

    pool = tuple(sorted(set(omega) - set(B)))
    legal_outputs = set()
    for perm in permutations(pool):
        C = perm[:-1] + (B[0],)
        assert legal_arc(B, C)
        legal_outputs.add(C)
    assert len(legal_outputs) == factorial(b)

    # Theorem 5.1: canonical local transition is a clean bijection.
    canonical_outputs = set()
    incoming_queues = set()
    for perm in permutations(pool):
        incoming = (B[-1],) + perm[:-1]
        outgoing = perm[:-1] + (B[0],)
        assert legal_arc(incoming, B)
        assert legal_arc(B, outgoing)
        incoming_queues.add(incoming)
        canonical_outputs.add(outgoing)
        for H in range(1, b - 1):
            assert triangular_clean(incoming, outgoing, H)
            assert brute_clean(incoming, B, outgoing, H)
    assert len(incoming_queues) == factorial(b)
    assert canonical_outputs == legal_outputs

    for H in range(1, b - 1):
        clean_count = 0
        for C in legal_outputs:
            criterion = triangular_clean(A, C, H)
            brute = brute_clean(A, B, C, H)
            assert criterion == brute
            if not criterion:
                continue
            clean_count += 1

            # Lemma 4.2: the exact triple-queue cross-collar windows.
            cross_count = 0
            word = A + B + C
            for q in range(2, H + 1):
                for t in range(1, q):
                    target = (
                        set(A[b - t :])
                        | set(B)
                        | set(C[: q - t])
                    )
                    actual = set(word[b - t : b - t + b + q])
                    assert target == actual
                    assert len(target) == b + q
                    cross_count += 1
            assert cross_count == H * (H - 1) // 2

        h = H - 1
        if 2 * h <= b:
            lower_bound = falling(b - h, h) * factorial(b - h)
            assert clean_count >= lower_bound

    return factorial(b)


def main():
    totals = []
    for b in range(3, 8):
        totals.append((b, audit_b(b)))
    print("PASS gate-C_Q ordered-port/cross-join audit", totals)


if __name__ == "__main__":
    main()
