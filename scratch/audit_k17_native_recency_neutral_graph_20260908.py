#!/usr/bin/env python3
"""One complete canonical k17 native-D^h neutral graph census, h100 only.

No cap, source change, optimization, variant, or search is performed.
All equal-height legal predecessors are covered by the proved rank-eight
containment theorem. Cross-height legal edges cannot lie on a state cycle
and are not claimed to be enumerated here.
"""
import argparse
import csv
import hashlib
import json
import math
import platform
import resource
import signal
import time
from collections import Counter, defaultdict, deque
from functools import reduce
from pathlib import Path


def update(state, letter):
    return (letter,) + tuple(b & ~letter for b in state if b & ~letter)


def coordinate_update(state, letter):
    """Independent physical-coordinate implementation of move-to-front."""
    classes = defaultdict(int)
    for block_index, block in enumerate(state, 1):
        for x in range(17):
            bit = 1 << x
            if block & bit:
                key = 0 if letter & bit else block_index
                classes[key] |= bit
    return tuple(classes[key] for key in sorted(classes))


def prefix_of_rank(state, rank):
    accum = 0
    for block in state:
        assert block and not (block & accum)
        accum |= block
        if accum.bit_count() == rank:
            return accum
        if accum.bit_count() > rank:
            raise AssertionError(("missing rank", rank, state))
    raise AssertionError(("missing rank", rank, state))


def file_sha(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    assert platform.node().split(".")[0] == "arboghast", "h100 only"
    resource.setrlimit(resource.RLIMIT_CPU, (120, 120))
    resource.setrlimit(resource.RLIMIT_AS, (2 * 1024**3, 2 * 1024**3))
    signal.alarm(150)
    started = time.monotonic()
    args.out.mkdir(parents=True, exist_ok=True)
    raw = args.input.read_bytes()
    source_sha = hashlib.sha256(raw).hexdigest()
    assert source_sha == "fed20c313c639740b089428c1d2b8b572fc7138de4c11c2203be554e4acfa2a3"
    cycles = json.loads(raw)
    full = (1 << 17) - 1
    records = []
    rank8_index = {}
    rank9_index = {}
    cycle_first = {}
    owner_seen = set()
    source_checks = state_checks = 0

    for cycle in cycles:
        cid = cycle["cycle"]
        assert cid == len(cycle_first)
        lower = cycle["lower_owners"]
        v, h = cycle["length"], cycle["height"]
        assert len(lower) == v and v % 17 == 0 and 1 <= h <= 8
        assert all(a.bit_count() == 8 for a in lower)
        assert not owner_seen.intersection(lower)
        owner_seen.update(lower)
        owners = [full ^ a for a in lower]
        word = []
        for i in range(v):
            mask = full
            for j in range(h + 1):
                mask &= owners[(i + j) % v]
            assert mask and mask.bit_count() == 9 - h
            word.append(mask)
            source_checks += 1
        assert word == cycle["source_period"]
        assert reduce(int.__or__, word, 0) == full

        # One full warm-up determines all last occurrences. The next period
        # supplies the actual cyclic steady states, not empty-start states.
        state = ()
        last = [-1] * 17
        for i, letter in enumerate(word):
            state = update(state, letter)
            for x in range(17):
                if letter & (1 << x):
                    last[x] = i
        assert min(last) >= 0
        steady_initial = state
        cycle_first[cid] = len(records)
        for i, letter in enumerate(word):
            state = update(state, letter)
            for x in range(17):
                if letter & (1 << x):
                    last[x] = v + i
            by_time = defaultdict(int)
            for x, timestamp in enumerate(last):
                by_time[timestamp] |= 1 << x
            direct = tuple(by_time[t] for t in sorted(by_time, reverse=True))
            assert direct == state
            assert state[0] == letter
            assert state[0].bit_count() == 9 - h
            assert all(block.bit_count() == 1 for block in state[1:h + 1])
            prefix8 = prefix_of_rank(state, 8)
            prefix9 = prefix_of_rank(state, 9)
            assert prefix9 == owners[i]
            assert prefix8 == owners[i] & owners[(i + 1) % v]
            accum = 0
            below9 = 0
            for block in state:
                accum |= block
                below9 += accum.bit_count() < 9
            assert accum == full and below9 == h
            gid = len(records)
            assert prefix8 not in rank8_index and prefix9 not in rank9_index
            rank8_index[prefix8] = gid
            rank9_index[prefix9] = gid
            records.append(dict(id=gid, cycle=cid, position=i, period=v,
                                height=h, blocks=list(state), rank8=prefix8,
                                rank9=prefix9, first=letter))
            state_checks += 1
        assert state == steady_initial

    assert len(records) == math.comb(17, 8) == 24310
    assert len(cycles) == 146
    assert len(rank8_index) == len(rank9_index) == len(records)
    assert len({tuple(r["blocks"]) for r in records}) == len(records)
    assert len(owner_seen) == len(records)
    for rec in records:
        nxt = cycle_first[rec["cycle"]] + (rec["position"] + 1) % rec["period"]
        assert update(tuple(rec["blocks"]), records[nxt]["first"]) == tuple(records[nxt]["blocks"])

    states_path = args.out / "native_periodic_states.json"
    states_path.write_text(json.dumps(records, separators=(",", ":")) + "\n")
    candidates_path = args.out / "complete_neutral_candidates.csv"
    legal_path = args.out / "complete_neutral_legal_edges.csv"
    count = Counter()
    cross = []
    extra_internal = []
    self_by_cycle = Counter()
    native_by_cycle = Counter()
    with candidates_path.open("w", newline="") as cf, legal_path.open("w", newline="") as ef:
        cw, ew = csv.writer(cf), csv.writer(ef)
        header = ["source_state", "destination_state", "source_cycle", "destination_cycle",
                  "height", "legal", "kind"]
        cw.writerow(header)
        ew.writerow(header)
        for dst in records:
            rest = dst["rank9"]
            seen = set()
            while rest:
                bit = rest & -rest
                rest ^= bit
                src = records[rank8_index[dst["rank9"] ^ bit]]
                assert src["id"] not in seen
                seen.add(src["id"])
                count["all_rank8_subset_candidates"] += 1
                if src["height"] != dst["height"]:
                    count["discarded_unequal_height_candidates"] += 1
                    continue
                count["complete_neutral_candidates"] += 1
                got = update(tuple(src["blocks"]), dst["first"])
                direct = coordinate_update(tuple(src["blocks"]), dst["first"])
                assert got == direct
                legal = got == tuple(dst["blocks"])
                if src["id"] == dst["id"]:
                    kind = "self"
                elif src["cycle"] == dst["cycle"] and dst["position"] == (src["position"] + 1) % src["period"]:
                    kind = "native"
                elif src["cycle"] == dst["cycle"]:
                    kind = "extra_internal"
                else:
                    kind = "cross_component"
                row = [src["id"], dst["id"], src["cycle"], dst["cycle"], src["height"], int(legal), kind]
                cw.writerow(row)
                if not legal:
                    count["rejected_neutral_candidates"] += 1
                    continue
                ew.writerow(row)
                count["legal_neutral_edges"] += 1
                count[kind] += 1
                if kind == "self":
                    self_by_cycle[src["cycle"]] += 1
                elif kind == "native":
                    native_by_cycle[src["cycle"]] += 1
                elif kind == "extra_internal":
                    extra_internal.append(row)
                else:
                    cross.append(dict(source_state=src["id"], destination_state=dst["id"],
                                      source_cycle=src["cycle"], destination_cycle=dst["cycle"],
                                      source_position=src["position"], destination_position=dst["position"],
                                      source_period=src["period"], destination_period=dst["period"],
                                      height=src["height"], emitted_letter=dst["first"]))
            assert len(seen) == 9 and dst["id"] in seen

    # The quotient is over SAME-HEIGHT edges only. All other legal edges
    # strictly decrease height and so cannot occur in a directed cycle.
    multiplicity = Counter((e["source_cycle"], e["destination_cycle"]) for e in cross)
    adjacency = {c["cycle"]: set() for c in cycles}
    indegree = {c["cycle"]: 0 for c in cycles}
    for u, v in multiplicity:
        adjacency[u].add(v)
        indegree[v] += 1
    queue = deque(sorted(c for c, degree in indegree.items() if not degree))
    topological = []
    while queue:
        u = queue.popleft()
        topological.append(u)
        for v in sorted(adjacency[u]):
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
    graph = dict(scope="complete same-height nonnative component quotient",
                 vertices=[dict(cycle=c["cycle"], period=c["length"], height=c["height"]) for c in cycles],
                 edges=[dict(source_cycle=u, destination_cycle=v, multiplicity=multiplicity[u, v])
                        for u, v in sorted(multiplicity)],
                 topological_order=topological, acyclic=len(topological) == len(cycles),
                 complete_cross_edges=cross)
    graph_path = args.out / "native_neutral_component_quotient.json"
    graph_path.write_text(json.dumps(graph, indent=2) + "\n")
    claims = dict(all24310_native_states_and_both_middle_bijections=True,
                  every_state_has_exactly_one_self_and_native_edge=(count["self"] == count["native"] == len(records)),
                  no_extra_internal_edges=not extra_internal,
                  exactly17_cross_edges=(len(cross) == 17),
                  one_cross_component_pair=(len(multiplicity) == 1),
                  all_cross_height3_from153_to85=all(e["height"] == 3 and e["source_period"] == 153
                                                   and e["destination_period"] == 85 for e in cross),
                  quotient_acyclic=graph["acyclic"])
    report = dict(status="PASS" if all(claims.values()) else "CLAIM_MISMATCH", host=platform.node(),
                  input_sha256=source_sha, cycle_count=len(cycles), state_count=len(records),
                  native_erosion_letters_reconstructed=source_checks,
                  periodic_states_independently_last_occurrence_replayed=state_checks,
                  counts=dict(count), claims=claims, extra_internal_edges=extra_internal,
                  component_edges=graph["edges"],
                  scope="All same-height legal edges are enumerated. Unequal-height edges are excluded from cycle covers by the separately proved monotonicity theorem, not by a claimed full edge census.",
                  resources=dict(cpu_seconds=120, wall_seconds=150, address_space_bytes=2*1024**3),
                  elapsed_seconds=time.monotonic()-started,
                  artifacts={p.name: dict(bytes=p.stat().st_size, sha256=file_sha(p))
                             for p in [states_path, candidates_path, legal_path, graph_path]})
    (args.out / "native_recency_routing_certificate.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2), flush=True)
    assert all(claims.values()), "User claim mismatch; certificate retained"


if __name__ == "__main__":
    main()
