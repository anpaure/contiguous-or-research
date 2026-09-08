"""Exact small-graph audit of cap-free isolated-mark variance bounds.

Research checker only. Closed degrees weight the total deletion envelope.
The analytic proof, not this finite audit, establishes the general bounds.
"""

from fractions import Fraction
from itertools import combinations


def check_graph(n, edge_bits, p):
    pairs = list(combinations(range(n), 2))
    neighbours = [0] * n
    for bit, (u, v) in enumerate(pairs):
        if edge_bits & (1 << bit):
            neighbours[u] |= 1 << v
            neighbours[v] |= 1 << u
    degrees = [mask.bit_count() for mask in neighbours]
    closed = [degree + 1 for degree in degrees]
    first = [Fraction(0), Fraction(0)]
    second = [Fraction(0), Fraction(0)]
    for marks in range(1 << n):
        size = marks.bit_count()
        probability = p**size * (1 - p) ** (n - size)
        isolated = [
            v for v in range(n)
            if marks & (1 << v) and not marks & neighbours[v]
        ]
        values = [len(isolated), sum(closed[v] for v in isolated)]
        for index, value in enumerate(values):
            first[index] += probability * value
            second[index] += probability * value**2
    variances = [second[i] - first[i] ** 2 for i in range(2)]
    square_sum = sum(degree**2 for degree in degrees)
    assert variances[0] <= n * p + p**3 * square_sum
    assert variances[1] <= sum(closed) + p * square_sum
    assert first[1] <= p * sum(closed)
    closed_masks = [neighbours[v] | (1 << v) for v in range(n)]
    triangle_trace = sum(
        bool(closed_masks[u] & (1 << v))
        * (closed_masks[u] & closed_masks[v]).bit_count()
        for u in range(n) for v in range(n)
    )
    child_mass_sum = 0
    for chosen in range(n):
        kept = ((1 << n) - 1) ^ closed_masks[chosen]
        child_mass_sum += sum(
            (closed_masks[v] & kept).bit_count()
            for v in range(n) if kept & (1 << v)
        )
    assert child_mass_sum == (
        n * sum(closed) - 2 * sum(c**2 for c in closed) + triangle_trace
    )


def check_hypergraph(n, edges):
    q = max(map(len, edges))
    closed = [sum(bool(e & f) for f in edges) for e in edges]
    assert max(closed) ** 2 <= q * sum(closed)
    degrees = [sum(v in e for e in edges) for v in range(n)]
    moment = sum(d**2 for d in degrees)
    expected_numerator = 0
    collision_square = 0
    companion = 0
    for i, chosen in enumerate(edges):
        remaining = [e for e in edges if not e & chosen]
        expected_numerator += sum(
            sum(v in e for e in remaining) ** 2
            for v in range(n) if v not in chosen
        )
        companion += closed[i] * sum(degrees[v] for v in chosen)
        collision_square += sum(
            sum(v in e and bool(e & chosen) for e in edges) ** 2
            for v in range(n) if v not in chosen
        )
    assert expected_numerator == (
        len(edges) * moment + sum(d**3 for d in degrees)
        - 2 * companion + collision_square
    )


if __name__ == "__main__":
    graph_checks = 0
    for n in range(1, 6):
        for edge_bits in range(1 << (n * (n - 1) // 2)):
            for p in (Fraction(1, 5), Fraction(1, 2), Fraction(4, 5)):
                check_graph(n, edge_bits, p)
                graph_checks += 1
    hypergraph_checks = 0
    for n in range(2, 6):
        for q in range(1, min(3, n) + 1):
            possible = [frozenset(e) for e in combinations(range(n), q)]
            for selected in range(1, 1 << len(possible)):
                edges = [e for i, e in enumerate(possible) if selected & (1 << i)]
                check_hypergraph(n, edges)
                hypergraph_checks += 1
    print(f"Exact graph/mark-law checks passed: {graph_checks}")
    print(f"Exact hypergraph clique/drift checks passed: {hypergraph_checks}")
