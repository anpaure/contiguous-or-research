#!/usr/bin/env python3
"""Search the first flat D5 router with three strandwise seam collars.

Run on H100 only.  The first factor has token exposures (1,1,2).  Each
prescribed context cut is extended to a canonical three-versus-three C6
seam.  One companion cut from each seam must form the three canonical
P2--Q0 cuts of a single 18-owner router; the remaining cuts are two dummy
identity sockets and the next-router socket on the exposure-two strand.
The search enforces owner and q1 simplicity and exact q1 refill.
"""

from __future__ import annotations

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
from search_d5_rank7_resident_two_channel_cable_router_compatibility_20260814 import (  # noqa:E402
    port_cycle,
)

GROUND = frozenset(range(23))


def edge(a, b):
    return frozenset((a, b))


def q1(e):
    a, b = tuple(e)
    return a & b, a | b


def exact(old, new):
    return all(
        Counter(q1(e)[shore] for e in old) == Counter(q1(e)[shore] for e in new)
        for shore in (0, 1)
    )


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
    edges = []
    for word in words:
        colour = d5.base.bits(word)
        x = old_tail[colour]
        y = next(owner for owner in by_colour[colour] if owner != x)
        edges.append((frozenset(d5.bits_of(x)), frozenset(d5.bits_of(y))))
    appearances = Counter(
        word for factor in flat["factors"] for word in factor
    )
    return words, tuple(edges), tuple(appearances[word] for word in words)


def seam_collars(context_edge):
    x, y = context_edge
    lower = x & y
    x_extra = next(iter(x - lower))
    y_extra = next(iter(y - lower))
    result = {}
    for x0 in lower:
        core = lower - {x0}
        for x2, seam_y in ((x_extra, y_extra), (y_extra, x_extra)):
            for x1 in GROUND - core - {x0, x2, seam_y}:
                active = (x0, x1, x2)
                aa = tuple(
                    frozenset(core | {active[i], active[(i - 1) % 3]})
                    for i in range(3)
                )
                bb = tuple(frozenset(core | {active[i], seam_y}) for i in range(3))
                old = tuple(edge(aa[i], bb[i]) for i in range(3))
                new = tuple(edge(aa[i], bb[(i - 1) % 3]) for i in range(3))
                if edge(x, y) != old[0]:
                    continue
                owners = set(aa) | set(bb)
                if len(owners) != 6 or not exact(old, new):
                    continue
                if any(len(e) != 2 or len(tuple(e)[0] ^ tuple(e)[1]) != 2 for e in old + new):
                    continue
                if any(len({q1(e)[shore] for e in old}) != 3 for shore in (0, 1)):
                    continue
                key = (frozenset(old), frozenset(new))
                result[key] = {
                    "core": core, "seam_y": seam_y, "active": active,
                    "a": aa, "b": bb, "old": old, "new": new,
                }
    return tuple(result.values())


def router_roles(collar):
    roles = []
    # old[0] is context.  Either other seam cut can be the current router.
    for router_index in (1, 2):
        router_edge = collar["old"][router_index]
        auxiliary_edge = collar["old"][3 - router_index]
        for p, q in (tuple(router_edge), tuple(reversed(tuple(router_edge)))):
            lower = p & q
            p_extra = next(iter(p - lower))
            z = next(iter(q - lower))
            for active in lower:
                roles.append({
                    "collar": collar,
                    "router_edge": router_edge,
                    "auxiliary_edge": auxiliary_edge,
                    "p": p, "q": q,
                    "h": lower - {active},
                    "z": z, "active": active, "next_active": p_extra,
                })
    return roles


def cycle_edges(cycle):
    return tuple(edge(owner, cycle[(i + 1) % len(cycle)]) for i, owner in enumerate(cycle))


def encode_set(value):
    return d5.base.bitword(sum(1 << x for x in value), 23)


def encode(value):
    if isinstance(value, frozenset):
        if all(isinstance(x, int) for x in value):
            return encode_set(value)
        return sorted(encode(x) for x in value)
    if isinstance(value, (tuple, list, set)):
        return [encode(x) for x in value]
    if isinstance(value, dict):
        return {str(k): encode(v) for k, v in value.items()}
    return value


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("selection")
    parser.add_argument("certificate")
    parser.add_argument("flat")
    parser.add_argument("--max-witnesses", type=int, default=100)
    args = parser.parse_args()
    selection_raw = Path(args.selection).read_bytes()
    certificate_raw = Path(args.certificate).read_bytes()
    flat_raw = Path(args.flat).read_bytes()
    selection = json.loads(selection_raw)
    certificate = json.loads(certificate_raw)
    flat = json.loads(flat_raw)
    words, context_edges, exposures = context(selection, certificate, flat)
    assert exposures == (1, 1, 2)
    collars = tuple(seam_collars(e) for e in context_edges)
    roles = tuple(tuple(r for c in menu for r in router_roles(c)) for menu in collars)

    index = []
    for menu in roles:
        grouped = defaultdict(list)
        for role in menu:
            grouped[(role["h"], role["z"])].append(role)
        index.append(grouped)

    counters = Counter()
    witness = None
    witnesses = []
    # Port order is allowed to permute; boundary action orientation is fixed later.
    for token_permutation in permutations(range(3)):
        menus = [index[token_permutation[i]] for i in range(3)]
        for signature in set(menus[0]) & set(menus[1]) & set(menus[2]):
            h, z = signature
            for triple in product(*(menu[signature] for menu in menus)):
                counters["common_hz_triples"] += 1
                active = tuple(role["active"] for role in triple)
                if len(set(active)) != 3:
                    continue
                if not all(
                    triple[i]["next_active"] == active[(i + 1) % 3]
                    for i in range(3)
                ):
                    continue
                counters["canonical_router_cut_triples"] += 1
                collar_owners = [
                    owner for role in triple
                    for owner in set(role["collar"]["a"]) | set(role["collar"]["b"])
                ]
                if len(collar_owners) != len(set(collar_owners)):
                    continue
                counters["collar_owner_simple"] += 1
                old_collar_edges = tuple(
                    e for role in triple for e in role["collar"]["old"]
                )
                new_collar_edges = tuple(
                    e for role in triple for e in role["collar"]["new"]
                )
                if any(
                    len([q1(e)[shore] for e in old_collar_edges])
                    != len({q1(e)[shore] for e in old_collar_edges})
                    for shore in (0, 1)
                ):
                    continue
                assert exact(old_collar_edges, new_collar_edges)
                counters["collar_q1_simple"] += 1

                x_pool = sorted(GROUND - h - {z} - set(active))
                found_clock = False
                for x1, x2 in permutations(x_pool, 2):
                    for y1, y2 in permutations(sorted(h), 2):
                        k = (h - {y1, y2}) | {x1, x2}
                        cycles = tuple(
                            port_cycle(
                                k, x1, x2, y1, y2, z,
                                active[i], active[(i + 1) % 3],
                            )
                            for i in range(3)
                        )
                        if any(cycles[i][3] != triple[i]["p"] or cycles[i][4] != triple[i]["q"] for i in range(3)):
                            continue
                        router_owners = set().union(*map(set, cycles))
                        if len(router_owners) != 18:
                            continue
                        intended = {role["p"] for role in triple} | {role["q"] for role in triple}
                        if router_owners & set(collar_owners) != intended:
                            continue
                        base_edges = tuple(e for cycle in cycles for e in cycle_edges(cycle))
                        auxiliary_and_context = tuple(
                            role["collar"]["old"][0] for role in triple
                        ) + tuple(role["auxiliary_edge"] for role in triple)
                        before = tuple(base_edges) + auxiliary_and_context
                        removed = {role["router_edge"] for role in triple} | set(auxiliary_and_context)
                        after = tuple(e for e in base_edges if e not in removed) + new_collar_edges
                        if not exact(before, after):
                            continue
                        if any(len([q1(e)[shore] for e in before]) != len({q1(e)[shore] for e in before}) for shore in (0, 1)):
                            continue
                        counters["full_router_q1_simple"] += 1
                        candidate = {
                            "token_permutation": token_permutation,
                            "h": h, "z": z, "active": active,
                            "x1": x1, "x2": x2, "y1": y1, "y2": y2, "k": k,
                            "roles": triple,
                            "router_cycles": cycles,
                            "old_collar_edges": old_collar_edges,
                            "new_collar_edges": new_collar_edges,
                            "before_edges": before,
                            "after_edges": after,
                        }
                        witnesses.append(candidate)
                        if witness is None:
                            witness = candidate
                        found_clock = True
                        break
                    if found_clock:
                        break
                if len(witnesses) >= args.max_witnesses:
                    break
            if len(witnesses) >= args.max_witnesses:
                break
        if len(witnesses) >= args.max_witnesses:
            break

    result = {
        "status": "PASS" if witness else "NO_WITNESS",
        "selection_sha256": hashlib.sha256(selection_raw).hexdigest(),
        "certificate_sha256": hashlib.sha256(certificate_raw).hexdigest(),
        "flat_sha256": hashlib.sha256(flat_raw).hexdigest(),
        "factor_words": words,
        "exposures": exposures,
        "context_edges": context_edges,
        "seam_collars_per_token": tuple(map(len, collars)),
        "router_roles_per_token": tuple(map(len, roles)),
        "counters": dict(counters),
        "witness": witness,
        "witnesses": witnesses,
    }
    print(json.dumps(encode(result), indent=2, sort_keys=True))
    if witness is None:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
