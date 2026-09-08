#!/usr/bin/env python3
"""Independent replay of the first-flat-factor bare-router q1 obstruction.

Run on H100 only.  This imports none of the subject search code.  It rebuilds
the three literal old D5 context edges, enumerates every oriented cross-legal
central-cut pair, joins the three ports by the router signature, and checks
aggregate lower/upper q1 refill.
"""

import argparse
import hashlib
import json
import sys
from collections import Counter, defaultdict
from itertools import permutations, product
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import solve_d5_tapped_c6_212_coinstantiation_20260814 as d5  # noqa:E402

GROUND = frozenset(range(23))


def edge(a, b):
    return frozenset((a, b))


def q1(e):
    a, b = tuple(e)
    return a & b, a | b


def exact(removed, added):
    return all(
        Counter(q1(e)[shore] for e in removed)
        == Counter(q1(e)[shore] for e in added)
        for shore in (0, 1)
    )


def records(context):
    x, y = context
    answer = []
    for orientation, (left, right) in enumerate(((x, y), (y, x))):
        for remove_left in left:
            for add_left in GROUND - left:
                p = frozenset((left - {remove_left}) | {add_left})
                for remove_right in right:
                    for add_right in GROUND - right:
                        q = frozenset((right - {remove_right}) | {add_right})
                        if len(p ^ q) != 2:
                            continue
                        lower = p & q
                        answer.append((
                            p, q, lower, next(iter(p - lower)),
                            next(iter(q - lower)), orientation, left, right,
                        ))
    return answer


def context(selection, certificate, flat):
    _, old, _ = d5.extract_rows(selection, certificate)
    _, by_colour = d5.base.factor_maps(old)
    old_tail = {}
    for item in selection["selection"]:
        owners = [d5.base.bits(word) for word in item["candidate"]["owners"]]
        colours = [d5.base.bits(word) for word in item["candidate"]["new_colours"]]
        for i, owner in enumerate(owners):
            old_tail[colours[i - 1]] = owner
    words = tuple(flat["factors"][0])
    result = []
    for word in words:
        colour = d5.base.bits(word)
        x = old_tail[colour]
        y = next(owner for owner in by_colour[colour] if owner != x)
        result.append((frozenset(d5.bits_of(x)), frozenset(d5.bits_of(y))))
    return words, tuple(result)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("selection")
    parser.add_argument("certificate")
    parser.add_argument("flat")
    args = parser.parse_args()
    selection_raw = Path(args.selection).read_bytes()
    certificate_raw = Path(args.certificate).read_bytes()
    flat_raw = Path(args.flat).read_bytes()
    selection = json.loads(selection_raw)
    certificate = json.loads(certificate_raw)
    flat = json.loads(flat_raw)
    words, context_edges = context(selection, certificate, flat)
    raw = tuple(records(e) for e in context_edges)
    four = tuple([
        r for r in port
        if len({context_edges[i][0], context_edges[i][1], r[0], r[1]}) == 4
    ] for i, port in enumerate(raw))
    unique = []
    for port in four:
        unique.append(len({
            (edge(r[0], r[1]), frozenset((edge(r[6], r[0]), edge(r[7], r[1]))))
            for r in port
        }))

    central = aggregate = q1_simple = endpoint_simple = both = 0
    distinct_histogram = Counter()
    context_cuts = {edge(*e) for e in context_edges}
    boundary = set().union(*(set(e) for e in context_edges))
    for perm in permutations(range(3)):
        ports = [four[perm[i]] for i in range(3)]
        by_z = []
        for port in ports:
            grouped = defaultdict(list)
            for r in port:
                grouped[r[4]].append(r)
            by_z.append(grouped)
        for z in set(by_z[0]) & set(by_z[1]) & set(by_z[2]):
            for triple in product(*(group[z] for group in by_z)):
                h = triple[0][2] & triple[1][2] & triple[2][2]
                if len(h) != 9:
                    continue
                aa = [tuple(r[2] - h) for r in triple]
                if any(len(a) != 1 for a in aa):
                    continue
                active = [a[0] for a in aa]
                if len(set(active)) != 3 or z in active:
                    continue
                if not all(triple[i][3] == active[(i + 1) % 3] for i in range(3)):
                    continue
                central += 1
                cuts = {edge(r[0], r[1]) for r in triple}
                crosses = {edge(r[6], r[0]) for r in triple} | {
                    edge(r[7], r[1]) for r in triple
                }
                if not exact(context_cuts | cuts, crosses):
                    continue
                aggregate += 1
                distinct = tuple(
                    len({q1(e)[shore] for e in context_cuts | cuts})
                    for shore in (0, 1)
                )
                distinct_histogram[distinct] += 1
                simple = distinct == (6, 6)
                owners = {owner for r in triple for owner in (r[0], r[1])}
                owner_ok = len(owners) == 6 and not (owners & boundary)
                q1_simple += simple
                endpoint_simple += owner_ok
                both += simple and owner_ok

    assert list(map(len, raw)) == [2026, 2026, 2026]
    assert list(map(len, four)) == [1500, 1500, 1500]
    assert unique == [750, 750, 750]
    assert (central, aggregate, q1_simple, endpoint_simple, both) == (255, 0, 0, 0, 0)
    print(json.dumps({
        "status": "PASS",
        "selection_sha256": hashlib.sha256(selection_raw).hexdigest(),
        "certificate_sha256": hashlib.sha256(certificate_raw).hexdigest(),
        "flat_sha256": hashlib.sha256(flat_raw).hexdigest(),
        "factor_words": words,
        "raw_oriented_pairs": list(map(len, raw)),
        "four_owner_oriented_pairs": list(map(len, four)),
        "four_owner_unoriented_pairs": unique,
        "central_router_patterns": central,
        "aggregate_q1_exact": aggregate,
        "q1_simple": q1_simple,
        "endpoint_owner_simple": endpoint_simple,
        "q1_and_owner_simple": both,
        "distinct_histogram": {f"{a},{b}": n for (a, b), n in distinct_histogram.items()},
        "compiler_exists_in_scope": False,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
