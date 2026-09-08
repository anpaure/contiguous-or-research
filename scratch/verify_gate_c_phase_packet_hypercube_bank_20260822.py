#!/usr/bin/env python3
"""Finite audit for the I.11 phase-packet hypercube bank.

The exhaustive labelled-packet census is run for b=3,5.  The fixed-(u,v)
hypercube bank and its lower-token/endpoint multiplicities are checked for
b=3,5,7,9.  No external package is required.
"""

from collections import Counter, defaultdict, deque
from itertools import combinations, permutations, product
from math import comb, factorial


def packet(u, v, X, Y):
    b = len(X) + 1
    out = [frozenset((u,) + tuple(X))]
    for i in range(1, b):
        out.append(frozenset(tuple(X[i - 1 :]) + tuple(Y[:i])))
    out.append(frozenset((u,) + tuple(Y)))
    return out


def exhaustive_pair_codegrees(b):
    omega = tuple(range(2 * b))
    C = frozenset(range(b))
    degree = 0
    pair_counts = Counter()
    labels = 0
    for p in permutations(omega):
        u, v = p[0], p[1]
        X, Y = p[2 : b + 1], p[b + 1 :]
        edge = packet(u, v, X, Y)
        assert len(edge) == b + 1 and len(set(edge)) == b + 1
        labels += 1
        if C in edge:
            degree += 1
            for D in edge:
                if D != C:
                    pair_counts[D] += 1

    assert labels == factorial(2 * b)
    expected_degree = (b + 1) * factorial(b) ** 2
    assert degree == expected_degree, (b, degree, expected_degree)

    by_distance = defaultdict(set)
    for D in map(frozenset, combinations(omega, b)):
        if D == C:
            continue
        d = b - len(C & D)
        by_distance[d].add(pair_counts[D])

    for d in range(1, b + 1):
        if d <= b - 2:
            expected = (
                2
                * (b + 1 - d)
                * factorial(b) ** 2
                // comb(b, d) ** 2
            )
        elif d == b - 1:
            expected = 6 * factorial(b) ** 2 // (b * b)
        else:
            expected = 0
        assert by_distance[d] == {expected}, (b, d, by_distance[d], expected)


def fixed_uv_bank(b):
    """Check the even-start antipodal-geodesic bank on m=b-1 pairs."""
    m = b - 1
    assert m % 2 == 0

    # Pair i is represented by symbols (i,0),(i,1).  A bit vector is a
    # transversal.  The union of the endpoints of a cube edge is a unique
    # (m+1)-set with exactly one doubled pair and no empty pair.
    interior = Counter()
    lower = Counter()
    upper_internal = Counter()
    upper_boundary = Counter()
    endpoints = Counter()
    endpoint_edges = Counter()

    even_starts = [x for x in product((0, 1), repeat=m) if sum(x) % 2 == 0]
    for x in even_starts:
        cur = list(x)
        start = tuple(cur)
        endpoint_sets = []
        for i in range(m):
            lower[tuple(cur)] += 1
            nxt = list(cur)
            nxt[i] ^= 1
            edge_union = frozenset(
                [(j, cur[j]) for j in range(m)] + [(i, nxt[i])]
            )
            interior[edge_union] += 1
            if i + 1 < m:
                upper = set(edge_union)
                upper.add((i + 1, 1 - cur[i + 1]))
                upper_internal[frozenset(upper)] += 1
            else:
                upper = set(edge_union)
                upper.add(("u", 0))
                upper_boundary[frozenset(upper)] += 1
            cur = nxt
        finish = tuple(cur)
        assert finish == tuple(1 - z for z in start)
        endpoints[start] += 1
        endpoints[finish] += 1
        endpoint_edges[tuple(sorted((start, finish)))] += 1

    eligible = set()
    for doubled in range(m):
        for choices in product((0, 1), repeat=m - 1):
            S = {(doubled, 0), (doubled, 1)}
            q = 0
            for j in range(m):
                if j == doubled:
                    continue
                S.add((j, choices[q]))
                q += 1
            eligible.add(frozenset(S))

    assert set(interior) == eligible
    assert set(interior.values()) == {1}
    assert len(interior) == m * 2 ** (m - 1)
    assert set(lower) == set(product((0, 1), repeat=m))
    assert set(lower.values()) == {m // 2}
    assert len(upper_internal) == (m - 1) * 2 ** (m - 2)
    assert set(upper_internal.values()) == {2}
    assert len(upper_boundary) == 2 ** (m - 1)
    assert set(upper_boundary.values()) == {1}
    assert len(endpoints) == 2 ** (m - 1)
    assert set(endpoints.values()) == {2}
    assert len(endpoint_edges) == 2 ** (m - 2)
    assert set(endpoint_edges.values()) == {2}

    # Fractional bank census from Corollary 2.2.
    R = tuple(range(2 * m))

    def pairings(items):
        if not items:
            yield ()
            return
        a = items[0]
        for q in range(1, len(items)):
            c = items[q]
            rest = items[1:q] + items[q + 1 :]
            for tail in pairings(rest):
                yield ((a, c),) + tail

    # Exhaustive pairing enumeration is kept to m<=6; larger bank checks
    # above do not need it.
    if m <= 6:
        all_pairings = list(pairings(R))
        middle_counts = Counter()
        lower_counts = Counter()
        for P in all_pairings:
            for doubled in range(m):
                other = [j for j in range(m) if j != doubled]
                for bits in product((0, 1), repeat=m - 1):
                    S = set(P[doubled])
                    for t, j in enumerate(other):
                        S.add(P[j][bits[t]])
                    middle_counts[frozenset(S)] += 1
            for bits in product((0, 1), repeat=m):
                lower_counts[
                    frozenset(P[j][bits[j]] for j in range(m))
                ] += 1
        rho = factorial(m + 1) // 2
        assert set(middle_counts) == set(map(frozenset, combinations(R, m + 1)))
        assert set(middle_counts.values()) == {rho}
        assert set(lower_counts) == set(map(frozenset, combinations(R, m)))
        assert set(lower_counts.values()) == {factorial(m)}


def global_endpoint_components(b):
    """Underlying fixed-pairing endpoint graph with u-bit fixed to zero."""
    assert b % 2 == 1
    vertices = [x for x in product((0, 1), repeat=b) if sum(x) % 2 == 0]
    adjacency = {x: set() for x in vertices}
    for x in vertices:
        for j in range(b):
            if x[j] != 0:
                continue
            y = tuple(x[k] if k == j else 1 - x[k] for k in range(b))
            assert sum(y) % 2 == 0
            adjacency[x].add(y)
            adjacency[y].add(x)

    seen = set()
    weight_profiles = []
    for root in vertices:
        if root in seen:
            continue
        q = deque([root])
        seen.add(root)
        comp = []
        while q:
            x = q.popleft()
            comp.append(x)
            for y in adjacency[x]:
                if y not in seen:
                    seen.add(y)
                    q.append(y)
        weights = tuple(sorted({sum(x) for x in comp}))
        weight_profiles.append(weights)

    expected = sorted(
        {
            tuple(sorted({s, b - 1 - s}))
            for s in range(0, b, 2)
        }
    )
    assert sorted(weight_profiles) == expected, (b, weight_profiles, expected)


def selector_rank_obstruction(b):
    """Rank of the fixed-order simultaneous parity-selector equations."""
    # Linear parts are ell_j(x)=sum_{k!=j} x_k.  Their span over F_2 has
    # rank b-1: differences give x_i+x_j, the even-weight dual subspace.
    rows = []
    for j in range(b):
        rows.append(sum(1 << k for k in range(b) if k != j))

    rank = 0
    basis = {}
    for row in rows:
        x = row
        while x:
            p = x.bit_length() - 1
            if p in basis:
                x ^= basis[p]
            else:
                basis[p] = x
                rank += 1
                break
    assert rank == b - 1
    # Any common affine fibre has at most 2 points, whereas a simultaneous
    # packet-bank selector would need 2^(b-2) starts.
    if b >= 5:
        assert 2 ** (b - rank) < 2 ** (b - 2)


def coherent_cycle_targets(b, rho, initial):
    """Defect-one targets in one fixed-order coherent FIFO packet cycle."""
    x = list(initial)
    targets = []
    for t in range(b):
        j = rho[t]
        for s in range(1, b):
            i = rho[(t + s) % b]
            targets.append(
                (j, i, tuple((k, x[k]) for k in range(b) if k not in (j, i)))
            )
            x[i] ^= 1
    assert x == list(initial)
    assert len(targets) == b * (b - 1) == len(set(targets))
    return frozenset(targets)


def fixed_order_code_obstruction(b):
    rho = tuple(range(b))
    states = list(product((0, 1), repeat=b))
    edges = {x: coherent_cycle_targets(b, rho, x) for x in states}
    for q, x in enumerate(states):
        for y in states[q + 1 :]:
            disjoint = edges[x].isdisjoint(edges[y])
            distance = sum(a != c for a, c in zip(x, y))
            assert disjoint == (distance >= 3)


def main():
    for b in (3, 5):
        exhaustive_pair_codegrees(b)
    for b in (3, 5, 7, 9):
        fixed_uv_bank(b)
        global_endpoint_components(b)
        selector_rank_obstruction(b)
        fixed_order_code_obstruction(b)
    print(
        "GATE_C_PHASE_PACKET_HYPERCUBE_BANK_PASS "
        "pair_codegrees=b3,b5 banks=b3,b5,b7,b9 "
        "adjacent_literal_multiplicities=PASS endpoint_components=PASS selector_rank=PASS "
        "fixed_order_code=PASS"
    )


if __name__ == "__main__":
    main()
