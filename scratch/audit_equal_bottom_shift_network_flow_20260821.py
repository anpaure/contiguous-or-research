#!/usr/bin/env python3
import random
from math import comb

import networkx as nx
import numpy as np
from scipy.optimize import linprog
from scipy.sparse import lil_matrix


def direct_instance(b, q, kept, residual):
    h = (b - 1) // 2
    multiplicities = [
        (comb(b, d) - (comb(b, d - 1) if d else 0)) ** 2
        for d in range(h + 1)
    ]
    variables = []
    for d in range(h + 1):
        for z in range(q + 1):
            ranks = tuple(
                r for r in kept if d + q - z <= r <= b - d - z
            )
            if ranks:
                variables.append((d, z, ranks, len(ranks)))

    rows = [("s", d) for d in range(h + 1)]
    rows += [("c", r, z) for z in range(q + 1) for r in kept]
    row_index = {row: i for i, row in enumerate(rows)}
    matrix = lil_matrix((len(rows), len(variables)), dtype=float)
    upper = []
    for d in range(h + 1):
        upper.append(multiplicities[d])
    for z in range(q + 1):
        for r in kept:
            upper.append(residual[r, z])
    objective = []
    for j, (d, z, ranks, weight) in enumerate(variables):
        matrix[row_index["s", d], j] = 1
        for r in ranks:
            matrix[row_index["c", r, z], j] = 1
        objective.append(-weight)
    return multiplicities, variables, matrix.tocsr(), np.array(upper), np.array(objective)


def network_optimum(b, q, kept, residual, multiplicities, variables):
    h = (b - 1) // 2
    total = sum(multiplicities)
    graph = nx.DiGraph()
    graph.add_node("source", demand=-total)
    graph.add_node("sink", demand=total)

    eligible = {(d, z): weight for d, z, _, weight in variables}
    for d, supply in enumerate(multiplicities):
        node = ("D", d)
        graph.add_edge("source", node, capacity=supply, weight=0)
        graph.add_edge(node, "sink", capacity=supply, weight=0)
        for z in range(q + 1):
            if (d, z) in eligible:
                graph.add_edge(
                    node,
                    ("Z", z, d),
                    capacity=supply,
                    weight=-eligible[d, z],
                )

    for z in range(q + 1):
        bounds = [total] * (h + 1)
        for r in kept:
            prefix = min(r - q + z, b - r - z)
            if prefix >= 0:
                prefix = min(h, prefix)
                bounds[prefix] = min(bounds[prefix], residual[r, z])
        for level in range(h + 1):
            graph.add_edge(
                ("Z", z, level),
                ("Z", z, level + 1),
                capacity=bounds[level],
                weight=0,
            )
        graph.add_edge(("Z", z, h + 1), "sink", capacity=total, weight=0)

    flow = nx.min_cost_flow(graph)
    value = 0
    for d, z, _, weight in variables:
        value += weight * flow[("D", d)][("Z", z, d)]
    return value, flow


def audit():
    rng = random.Random(20260821)
    for b in (5, 7, 9, 11, 13):
        for q in range(1, min(4, b // 2) + 1):
            kept = tuple(range(q, b - q + 1))
            for trial in range(8):
                residual = {
                    (r, z): rng.randrange(0, comb(b, min(r, b - r)) ** 2 + 1)
                    for z in range(q + 1)
                    for r in kept
                }
                multiplicities, variables, matrix, upper, objective = direct_instance(
                    b, q, kept, residual
                )
                lp = linprog(
                    objective,
                    A_ub=matrix,
                    b_ub=upper,
                    bounds=(0, None),
                    method="highs",
                )
                assert lp.success
                flow_value, flow = network_optimum(
                    b, q, kept, residual, multiplicities, variables
                )
                assert abs((-lp.fun) - flow_value) < 1e-6
                for d, z, _, _ in variables:
                    assert isinstance(flow[("D", d)][("Z", z, d)], int)
            print("network/LP PASS", b, q)
    print("ALL EQUAL-BOTTOM SHIFT FLOW CHECKS PASS")


if __name__ == "__main__":
    audit()
