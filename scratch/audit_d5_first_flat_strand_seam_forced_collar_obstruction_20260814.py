#!/usr/bin/env python3
"""Replay the forced fixed-side collar obstruction for all q1 witnesses.

Run on H100 only.  The failing three-support window lies wholly on the
context/router side of the auxiliary cut, so it rules out every possible
dummy completion, not just the searched central/direct resident C6 rails.
"""

import argparse
import hashlib
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import solve_d5_tapped_c6_212_coinstantiation_20260814 as d5  # noqa:E402


def decode(word):
    return frozenset(i for i, c in enumerate(word) if c == "1")


def decode_edge(value):
    return frozenset(decode(word) for word in value)


def edge(a, b):
    return frozenset((a, b))


def cycle_edges(cycle):
    return {edge(owner, cycle[(i + 1) % len(cycle)]) for i, owner in enumerate(cycle)}


def router_edges(cycles, switched):
    result = set().union(*(cycle_edges(cycle) for cycle in cycles))
    if switched:
        for i, cycle in enumerate(cycles):
            result.remove(edge(cycle[0], cycle[1]))
            result.add(edge(cycle[0], cycles[(i - 1) % 3][1]))
    return result


def adjacency(edges):
    result = defaultdict(set)
    for e in edges:
        a, b = tuple(e)
        result[a].add(b)
        result[b].add(a)
    return result


def q1(e):
    a, b = tuple(e)
    return a & b, a | b


def context_collar_edges(selection, certificate, context_edges):
    _, raw_old, _ = d5.extract_rows(selection, certificate)
    canonical = set(d5.base.canonical_edges(11))
    integer_adj, _ = d5.factor_adjacency(d5.lifted_edges(raw_old, canonical))

    def integer(owner):
        return sum(1 << x for x in owner)

    result = set()
    for cut in context_edges:
        x, y = tuple(cut)
        for endpoint, other in ((x, y), (y, x)):
            endpoint_i, other_i = integer(endpoint), integer(other)
            one_i = next(value for value in integer_adj[endpoint_i] if value != other_i)
            two_i = next(value for value in integer_adj[one_i] if value != endpoint_i)
            one = frozenset(d5.bits_of(one_i))
            two = frozenset(d5.bits_of(two_i))
            result.add(edge(endpoint, one))
            result.add(edge(one, two))
    return result


def encode_set(value):
    return d5.base.bitword(sum(1 << x for x in value), 23)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("selection")
    parser.add_argument("certificate")
    parser.add_argument("q1_witnesses")
    args = parser.parse_args()
    selection_raw = Path(args.selection).read_bytes()
    certificate_raw = Path(args.certificate).read_bytes()
    q1_raw = Path(args.q1_witnesses).read_bytes()
    selection = json.loads(selection_raw)
    certificate = json.loads(certificate_raw)
    report = json.loads(q1_raw)
    witnesses = report["witnesses"]
    assert len(witnesses) == 21
    context_edges = {
        decode_edge(role["collar"]["old"][0])
        for role in witnesses[0]["roles"]
    }
    context_collars = context_collar_edges(selection, certificate, context_edges)
    audits = []
    repeated_histogram = Counter()

    for index, witness in enumerate(witnesses):
        router = tuple(tuple(decode(owner) for owner in cycle) for cycle in witness["router_cycles"])
        roles = witness["roles"]
        permutation = witness["token_permutation"]
        token_zero_port = permutation.index(0)
        role = roles[token_zero_port]
        auxiliary = decode_edge(role["auxiliary_edge"])
        router_cuts = {decode_edge(item["router_edge"]) for item in roles}
        seam_edges = {decode_edge(e) for item in roles for e in item["collar"]["new"]}

        # Hostile q1 replay of the complete finite bank stated by the witness.
        before = [decode_edge(e) for e in witness["before_edges"]]
        after = [decode_edge(e) for e in witness["after_edges"]]
        assert all(Counter(q1(e)[s] for e in before) == Counter(q1(e)[s] for e in after) for s in (0, 1))
        assert all(len({q1(e)[s] for e in before}) == len(before) for s in (0, 1))

        phase_reports = []
        for switched in (False, True):
            fixed = (router_edges(router, switched) - router_cuts) | seam_edges | context_collars
            adj = adjacency(fixed)
            endpoint_reports = []
            for auxiliary_endpoint in auxiliary:
                join = next(e for e in seam_edges if auxiliary_endpoint in e)
                other = next(owner for owner in join if owner != auxiliary_endpoint)
                one = next(owner for owner in adj[other] if owner != auxiliary_endpoint)
                two = next(owner for owner in adj[one] if owner != other)
                supports = (auxiliary_endpoint ^ other, other ^ one, one ^ two)
                repeated = (supports[0] & supports[1]) | (supports[0] & supports[2]) | (supports[1] & supports[2])
                endpoint_reports.append({
                    "auxiliary_endpoint": encode_set(auxiliary_endpoint),
                    "other": encode_set(other),
                    "one": encode_set(one),
                    "two": encode_set(two),
                    "supports": [sorted(s) for s in supports],
                    "union_size": len(set().union(*supports)),
                    "repeated": sorted(repeated),
                })
            failures = [item for item in endpoint_reports if item["union_size"] < 6]
            assert len(failures) == 1
            repeated_histogram.update(failures[0]["repeated"])
            phase_reports.append(endpoint_reports)
        # The fixed obstruction is copied exactly between router phases.
        assert phase_reports[0] == phase_reports[1]
        audits.append({
            "witness": index,
            "token_permutation": permutation,
            "token_zero_port": token_zero_port,
            "endpoints": phase_reports[0],
        })

    assert all(
        sorted(item["union_size"] for item in audit["endpoints"]) == [5, 6]
        for audit in audits
    )
    print(json.dumps({
        "status": "PASS",
        "selection_sha256": hashlib.sha256(selection_raw).hexdigest(),
        "certificate_sha256": hashlib.sha256(certificate_raw).hexdigest(),
        "q1_witnesses_sha256": hashlib.sha256(q1_raw).hexdigest(),
        "q1_witnesses": len(witnesses),
        "all_q1_exact_and_simple": True,
        "all_fail_same_logical_token": True,
        "failing_logical_token": 0,
        "fixed_side_union_size_histogram": {"5": 21, "6": 21},
        "repeated_coordinate_histogram_over_both_phases": dict(sorted(repeated_histogram.items())),
        "phase_independent": True,
        "dummy_completion_can_repair": False,
        "audits": audits,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
