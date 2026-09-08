#!/usr/bin/env python3
"""Exact verifier for the fixed-GK leaf/right-head obstruction.

The structural checks are self-contained.  ``--max-m`` performs exhaustive
catalogue and Hopcroft--Karp checks through the requested parameter.  The
optional ``--certificate`` checks a chosen full-leaf simultaneous SDR and its
owner topology; this is used for the finite minimum-reset witness at m=7.

Substantive runs belong on H100, not on the local workstation.
"""

from __future__ import annotations

import argparse
import base64
from collections import Counter, defaultdict, deque
import hashlib
import json
from math import comb
from pathlib import Path
import zlib


# The m=7 minimum-reset certificate, represented by q(U) in increasing integer
# order of the rank-9 uppers.  Encoding the q stream, instead of a JSON option
# list, keeps the verifier self-contained and forces reconstruction of every
# derived endpoint from the structural catalogue.
M7_Q_STREAM_B64 = """
eNo1mAdi5TAIRL96A+5/3H2Ds07iIkuIOoxT1zmn9tJ65bi99Fbv4rru5bnMe2/hb96Zx5i/MWavc9e9+2u1vrUei/rsnUvpZ7Rz
CkJLG+8MiWcOL7VDL3u/9/ob8833RmkPmRzMmZ2RN/hDIq/5XXON11gxfoxr7dha13djfwSuvfbgzMHt2/27m22mzF2b9Z/msbOh
yTlSEv3amJORmjPrsW6IKaX3IiX7Lnme/Oxd2kwlWxrQ2m139C7P3DoXjrm87fvySpN5arwal612z/G1xra9777T0Lu3aXfvYXaX
3L6acW4FLbpZH9bkXyvWDIezt8m9szLUWFSMQzeHybZPyTuzetq2wXLN6TjmbDP2bWa/gx3d2j621uLhXLtIa+zHbO5NGi/jNDo7
lLsLgceTKRl72kUmMzC+si/50VCfbZC4DTcuNqhjGLlyq6E2W9zT2+03k+Gwbqxzz1nWiQOZsS6uOZh/mcR0Xg6JZZ1h8DTEkEJz
o9/mLYZigR0y9CLjYjwPW4lpCreMJL6jr6Wr1+O4rY3Shx+fuNXxJ0oe3hFLJ6S3dlfm9+5bWX6d3LhjkFd3elcZOAo5pzZ98usE
ZTOy/WrHW5z7MS6JR/7J1D24bzuPuh11ruaSooo2WcaO7uXNuscbbW7V35RyemTOKc7xlCnPO6lPHbxF5Z2zC4GlAjpFhgqDP+3E
hfwfr5/2HiNv4wMi8/wtZFBVlWLmStALU520xAZk8qjUfY473m37Pn4623Zs2VmQ716Jp74w4VKej8pg8JVByICDpy1uRWG2OT6I
MzlP9NmiHUWD6Pkk3DOV6BJ6huPnlP+0XVbSdGRJhfOODtIFz28EvrMeTrx3zYMYW3iQ1Edr3Ecab+rFfVtHa3MXqjBBcS8ODLkv
gRz37nUsM27ICtKpORWuGnJ0PSTNaseXK4vc3Dr3hj0SudZ0EsCtdVf5upVl1RFm47cQilTui3klOS/Z5x3x/VJBFKSTAmQNonpn
N3y6cAepzhyEgJ5+TzMcBSJRXB3Eot5UF1erSMJ+JitRU+riGsoAda4NikPDt56OXkya7WwSlZUUDdLxJH5k9qb+eQAEMJ4h81dl
E25BRkW1VZYXzHlGgmHMNNU2IccbgP6uHWQpzY3FD6SyyVnG7mfeDNTs5wEFx95RDRtuePIuqU994CHGm5OnC+NZwcvXHrtjk73H
xlT6MGmIABx1VOPk957DeUm+2OlyCMlGZmDTeej7wEMSVfFQnFOiCXSFRjx014BeoQIVJTRUPnMzqIXUwwSaxNowhjujFuhMYANu
kEcodqrtqfLfo9bBduGA1BY+sohxv7KCeNnAJdyS9Tf1lh1vCXClCvjLNJUCVaKD66PKEcPaJ0fd50fnlycyQxZNxQRlEZrDhHg/
qnqfUMva7RcgconSwM84+m2RBVV0DyBzoU+tFVFu6OBCs9qjhdZTUyNijxgx7x8LoJEVZl0aFsN3rB4aV7eLqF/PY5wZfVVdRs1X
sZTLbLXiRltjslnI62xR5owWtPZIvMwGLtQZPWgAhSQuBR3f550WvBlroD3wQLU+VQg2TtGO2n9qKvXgYBTCY2xNEeGeSaUdlBbH
mO0Vftpb0I/FVfPY4rvqzFLmBXDMy9ixXyQr4UE/q4ufwDcalgBUAxh8gF+G9vxenACuuhQAtN842P5jbKIKUogGywjyix7nba5D
MWEdRRm0PHEkhp6mPl3ShiebceJGeIjlMG8GHAoH0uPkyQgrnMjGoA0GoBR4svQwrF+FIRgRYazwh7UqaU8WlDAFRBU9xQZwLPzB
cr2AvJOaFCrt5CzqEXSkWsAb9mOJ9lx4Eu6naqqKcQQ0wLhB5o6AMtL5l1o8lIbumK+UFoANvrFJ0gLo0hnFrce0gnCqI0yPoh9N
3MEOm6mhMA5zoIhiHkpbSpjAYhyVLAGAYHyM9cDe4oonaBTfcM9pYB3uZra4hVIT3ab9FF8SX8lGANcrP7zU8S9qy0Q82QjR+82k
RqoVcEK6bhkH1RJvAQTIciixcsEaaXcqIMA6wCQsDwwFG9b3AA03PCAeN7+x89IOw5USz73YIRIIpVjR3jl+IiFEbBJSIH3sKyNT
aRt5q7R4UjFEyrjRphrR6XJpimAHhMHCb6sQ0D0BoPrzjN+eAduHaLEB3JW2EkJGE5sPOWCAQRtatuSMoEXrDajHZlcGKCl4kCZK
D7sfQTRVlI5U5jCXhAdElyASre58gkIQjkiLTgpdJQBZ4MsW95MnRBd4Sw2hxpY7QL9Wl3zg4od9C8sAuB11NyCuboqvZ1vpARkT
TaGZkOJFi6i4A/YlXE59AHBxMIW+y6GvGkrXE4J0EGudhj4EWs5U2xYOkkXSAnLgsF108DavmFWLS17eCT+GDhZeYcgWELXtZA46
kqy6B32hKoA1pHAKbrWuiZTmAScgm7/HRF3JuPow4Y33wQw8NcSccnpPmquSuwnsvlmheQI6WJvUgHFdIQ0jagCzMMGjDLAP5Ab/
nygkg5QEe9eSUZwbyoonq9q81m4gEL6xRVf59Smb6OC0fCD8wMe1aqqNg3CeHwUgyRBmqspXUkcqHRK7cGsC5w6RuRAxVVfzU/Wd
dvKTMRSUxoyA7rEX/QH1yDEPffYkcBLwF67EY18sJ3MhnQygfFYELWbpWS1bsL/oPsDXVXugw9L03+9BACJptdbp8xh6mF4WM7jJ
D5LfgdaOJ4hB6AuAT9qn1E1/KYlHfCUQauZoI9OUxXqk2etGvcEVU2pCXQBLiFuo76sBIgYLQzvEEbnGFaizRfsgTvzq4w+aBPtU
LqTVoYusz1t+Sc+W91vDRDFMTFdk02OLLwHqpKEW7o8h/B3xiRmRbCwIcii9XOkhlbBJWPu9hIABPvBnzkN1d3KVC5slhzYEVP8V
lWehHdFU6N7Jghsr/SE6z42rd6QN0kt6KJf55tCDfZrpS3WlsXwyfByL/hWgOXrkNP5SexLm8pH8kSugRUgqU/nOlaG2soa+/zXw
egvlVFKRVUgY8P/9G/BvECqvyrTkQf3mLRWplooH6EkkhOnbMnJeRJaoMjw/yU3fnUQTNvy9uepfTMYhOz8JZKVAO0R5ZSWpnGb9
hdhfRiJDjIKuZr2Igv0FXk7a9j8XeqaHid18CcLPdzf+h3urbLpwH4pKhP3TwdU1JSO3lKyWXaT4t/1LYe0RP7EiCBI8d55UNdP7
73vvUeMki0pbUIvXyQeds+DyJRfjHotV1yn5ZS2riZh0EafmMj91/Hv7OSQ/DeStUBoo+Ertrz9Ct7ViyC3ZBfUPm0RDV59UYW99
/8pyhZuAZKVCZ56eGVDn96SR5JBiIhBJlxxpRrD/rJSErFwRDtyg6P4DXaGvVg==
"""
M7_Q_STREAM_SHA256 = "f5a81c28a57f5eddbd3dadea3d206d3e72644d53959d278bf533529a4125e421"


def gk_matching(x: int, n: int) -> tuple[dict[int, int], list[int]]:
    stack: list[int] = []
    mate: dict[int, int] = {}
    for i in range(n):
        if (x >> i) & 1:
            stack.append(i)
        elif stack:
            j = stack.pop()
            mate[i] = j
            mate[j] = i
    return mate, [i for i in range(n) if i not in mate]


def catalogue(m: int) -> list[dict[str, int]]:
    n = 2 * m + 1
    records: list[dict[str, int]] = []
    for upper in range(1 << n):
        if upper.bit_count() != m + 2:
            continue
        _mate_u, free_u = gk_matching(upper, n)
        free_one_u = [i for i in free_u if (upper >> i) & 1]
        p = free_one_u[0]
        a = upper ^ (1 << p)
        mate_a, free_a = gk_matching(a, n)
        for q in range(n):
            if not ((a >> q) & 1):
                continue
            leaf = q in free_a or mate_a.get(q) == q + 1
            if not leaf:
                continue
            lower = a ^ (1 << q)
            b = lower | (1 << p)
            _mate_l, free_l = gk_matching(lower, n)
            free_zero_l = [i for i in free_l if not ((lower >> i) & 1)]
            assert p in free_zero_l
            chart = len(free_zero_l) - 1 - free_zero_l.index(p)
            records.append(
                dict(upper=upper, p=p, q=q, a=a, lower=lower, b=b, chart=chart)
            )
    return records


def hopcroft_karp(adjacency: dict[int, set[int]]) -> tuple[dict[int, int], dict[int, int]]:
    pair_u: dict[int, int] = {}
    pair_v: dict[int, int] = {}
    inf = 1 << 60
    while True:
        distance: dict[int, int] = {}
        queue: deque[int] = deque()
        for u in adjacency:
            if u not in pair_u:
                distance[u] = 0
                queue.append(u)
            else:
                distance[u] = inf
        found = False
        while queue:
            u = queue.popleft()
            for v in adjacency[u]:
                if v not in pair_v:
                    found = True
                else:
                    u2 = pair_v[v]
                    if distance[u2] == inf:
                        distance[u2] = distance[u] + 1
                        queue.append(u2)
        if not found:
            return pair_u, pair_v

        def augment(u: int) -> bool:
            for v in adjacency[u]:
                if v not in pair_v or (
                    distance[pair_v[v]] == distance[u] + 1 and augment(pair_v[v])
                ):
                    pair_u[u] = v
                    pair_v[v] = u
                    return True
            distance[u] = inf
            return False

        for u in adjacency:
            if u not in pair_u:
                augment(u)


def projection_components(
    uppers: set[int], records: list[dict[str, int]], shore: str
) -> list[tuple[set[int], set[int]]]:
    ua: dict[int, set[int]] = {u: set() for u in uppers}
    va: dict[int, set[int]] = defaultdict(set)
    for record in records:
        u, v = record["upper"], record[shore]
        ua[u].add(v)
        va[v].add(u)
    seen_u: set[int] = set()
    seen_v: set[int] = set()
    result: list[tuple[set[int], set[int]]] = []
    for seed in sorted(uppers):
        if seed in seen_u:
            continue
        cu, cv = {seed}, set()
        seen_u.add(seed)
        queue: deque[tuple[str, int]] = deque([("u", seed)])
        while queue:
            side, x = queue.popleft()
            if side == "u":
                for v in ua[x]:
                    if v not in seen_v:
                        seen_v.add(v)
                        cv.add(v)
                        queue.append(("v", v))
            else:
                for u in va[x]:
                    if u not in seen_u:
                        seen_u.add(u)
                        cu.add(u)
                        queue.append(("u", u))
        result.append((cu, cv))
    return result


def audit_parameter(m: int) -> dict[str, object]:
    records = catalogue(m)
    uppers = {r["upper"] for r in records}
    expected_u = comb(2 * m + 1, m + 2)
    assert len(uppers) == expected_u
    assert {r["chart"] for r in records} <= {0, 1, 2}
    left = [r for r in records if r["q"] < r["p"]]
    right = [r for r in records if r["q"] > r["p"]]
    # Exact form of the only topology-breaking atom.
    assert all(r["chart"] == 0 and r["a"] >> r["q"] & 3 == 1 for r in left)

    match_size = {}
    for shore in ("lower", "b"):
        adjacency = {u: set() for u in uppers}
        for r in right:
            adjacency[r["upper"]].add(r[shore])
        pair_u, pair_v = hopcroft_karp(adjacency)
        assert len(pair_u) == len(pair_v)
        match_size[shore] = len(pair_u)

    components = projection_components(uppers, right, "b")
    monotone_upper = (1 << (m + 2)) - 1
    monotone_component = next(c for c in components if monotone_upper in c[0])
    result = {
        "m": m,
        "uppers": len(uppers),
        "left_options": len(left),
        "right_lower_matching": match_size["lower"],
        "right_head_matching": match_size["b"],
        "right_head_deficiency": len(uppers) - match_size["b"],
        "head_component_count": len(components),
        "head_component_balances": sorted(Counter(len(u) - len(v) for u, v in components).items()),
        "monotone_component": [len(monotone_component[0]), len(monotone_component[1])],
    }
    if m == 7:
        assert result["right_lower_matching"] == 5005
        assert result["right_head_matching"] == 4950
        assert result["head_component_count"] == 66
        assert result["monotone_component"] == [2705, 2650]
        assert sum(1 for u, v in components if len(u) > len(v)) == 1
    return result


def audit_selection(m: int, chosen: list[dict[str, int]], source: str) -> dict[str, object]:
    n = 2 * m + 1
    records = catalogue(m)
    legal = {
        (r["upper"], r["p"], r["q"], r["lower"], r["b"]): r for r in records
    }
    normalized = []
    for r in chosen:
        key = (r["upper"], r["p"], r["q"], r["lower"], r["b"])
        assert key in legal
        normalized.append(legal[key])
    assert len(normalized) == comb(n, m + 2)
    assert len({r["upper"] for r in normalized}) == len(normalized)
    assert len({r["lower"] for r in normalized}) == len(normalized)
    assert len({r["b"] for r in normalized}) == len(normalized)
    resets = [r for r in normalized if r["q"] < r["p"]]

    owner_adj: dict[int, list[tuple[int, int]]] = defaultdict(list)
    for i, r in enumerate(normalized):
        owner_adj[r["a"]].append((r["b"], i))
        owner_adj[r["b"]].append((r["a"], i))
    assert max(map(len, owner_adj.values())) <= 2
    seen: set[int] = set()
    owner_components = []
    reset_indices = {i for i, r in enumerate(normalized) if r["q"] < r["p"]}
    for seed in owner_adj:
        if seed in seen:
            continue
        seen.add(seed)
        queue = deque([seed])
        vertices, edges = set(), set()
        while queue:
            x = queue.popleft()
            vertices.add(x)
            for y, i in owner_adj[x]:
                edges.add(i)
                if y not in seen:
                    seen.add(y)
                    queue.append(y)
        owner_components.append((vertices, edges))
    cycle_rank = sum(len(e) - len(v) + 1 for v, e in owner_components)
    reset_component_hist = Counter(
        len(e & reset_indices) for v, e in owner_components if e & reset_indices
    )
    result = {
        "certificate": source,
        "m": m,
        "selected": len(normalized),
        "resets": len(resets),
        "owner_components": len(owner_components),
        "cycle_rank": cycle_rank,
        "reset_component_histogram": sorted(reset_component_hist.items()),
    }
    if m == 7 and len(resets) == 55:
        assert len(owner_components) == 1430
        assert cycle_rank == 0
        assert result["reset_component_histogram"] == [(1, 46), (2, 3), (3, 1)]
    return result


def check_certificate(path: Path) -> dict[str, object]:
    raw = path.read_bytes()
    data = json.loads(raw)
    m = data["m"]
    chosen = data.get("chosen", data.get("records"))
    assert chosen is not None
    result = audit_selection(m, chosen, str(path))
    result["sha256"] = hashlib.sha256(raw).hexdigest()
    return result


def check_embedded_m7() -> dict[str, object]:
    q_stream = zlib.decompress(base64.b64decode(M7_Q_STREAM_B64))
    assert hashlib.sha256(q_stream).hexdigest() == M7_Q_STREAM_SHA256
    records = catalogue(7)
    uppers = sorted({r["upper"] for r in records})
    assert len(q_stream) == len(uppers) == 5005
    by_upper_q = {(r["upper"], r["q"]): r for r in records}
    chosen = [by_upper_q[(u, q)] for u, q in zip(uppers, q_stream)]
    result = audit_selection(7, chosen, "embedded-m7-q-stream")
    result["q_stream_sha256"] = M7_Q_STREAM_SHA256
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-m", type=int, default=7)
    parser.add_argument("--certificate", type=Path)
    args = parser.parse_args()
    output = {"parameters": [audit_parameter(m) for m in range(2, args.max_m + 1)]}
    output["embedded_m7_certificate"] = check_embedded_m7()
    if args.certificate:
        output["certificate"] = check_certificate(args.certificate)
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
