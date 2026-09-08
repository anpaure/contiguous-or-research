#!/usr/bin/env python3
"""One canonical k17 D^min(h,3) neutral/matching graph census, h100 only.

One deterministic SCC/cycle diagnostic; no frame variants or optimization.
This changes source aperture but makes no subsequent entrywise letter caps.
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


def strongly_connected(adjacency):
    """Iterative Kosaraju, including isolated vertices."""
    n = len(adjacency)
    reverse = [[] for _ in range(n)]
    for u, neighbors in enumerate(adjacency):
        for v in neighbors:
            reverse[v].append(u)
    seen = bytearray(n)
    finish = []
    for root in range(n):
        if seen[root]:
            continue
        seen[root] = 1
        stack = [(root, 0)]
        while stack:
            u, index = stack[-1]
            if index == len(adjacency[u]):
                finish.append(u)
                stack.pop()
                continue
            stack[-1] = (u, index + 1)
            v = adjacency[u][index]
            if not seen[v]:
                seen[v] = 1
                stack.append((v, 0))
    assigned = bytearray(n)
    components = []
    for root in reversed(finish):
        if assigned[root]:
            continue
        assigned[root] = 1
        block = []
        stack = [root]
        while stack:
            u = stack.pop()
            block.append(u)
            for v in reverse[u]:
                if not assigned[v]:
                    assigned[v] = 1
                    stack.append(v)
        components.append(sorted(block))
    components.sort(key=lambda c: c[0])
    return components


def chosen_cycle(adjacency, components):
    """Shortest return at the minimum vertex of the first nontrivial SCC.

    Sorted neighbors give a deterministic lexicographic breadth-first choice.
    There is no search over alternative cap/source configurations.
    """
    nontrivial = next((c for c in components if len(c) > 1), None)
    if nontrivial is None:
        return []
    allowed = set(nontrivial)
    start = nontrivial[0]
    parent = {start: None}
    queue = deque([start])
    while queue:
        u = queue.popleft()
        for v in adjacency[u]:
            if v not in allowed or v == u:
                continue
            if v == start and u != start:
                path = [u]
                while path[-1] != start:
                    path.append(parent[path[-1]])
                return list(reversed(path))
            if v not in parent:
                parent[v] = u
                queue.append(v)
    raise AssertionError("nontrivial SCC has no return cycle")


def audit_sccs(adjacency, components):
    """Separate certificate check: mutual reachability + acyclic quotient."""
    n = len(adjacency)
    label = [-1] * n
    reverse = [[] for _ in range(n)]
    for cid, block in enumerate(components):
        for u in block:
            assert label[u] == -1
            label[u] = cid
    assert min(label) >= 0
    quotient = [set() for _ in components]
    indegree = [0] * len(components)
    for u, neighbors in enumerate(adjacency):
        for v in neighbors:
            reverse[v].append(u)
            if label[u] != label[v]:
                quotient[label[u]].add(label[v])
    for cid, block in enumerate(components):
        for graph in (adjacency, reverse):
            reached = {block[0]}
            stack = [block[0]]
            while stack:
                u = stack.pop()
                for v in graph[u]:
                    if label[v] == cid and v not in reached:
                        reached.add(v)
                        stack.append(v)
            assert len(reached) == len(block)
        for dest in quotient[cid]:
            indegree[dest] += 1
    queue = deque(i for i, degree in enumerate(indegree) if not degree)
    processed = 0
    while queue:
        u = queue.popleft()
        processed += 1
        for v in quotient[u]:
            indegree[v] -= 1
            if not indegree[v]:
                queue.append(v)
    assert processed == len(components)


def permutation_cycles(successor):
    n = len(successor)
    assert sorted(successor) == list(range(n))
    seen = bytearray(n)
    result = []
    for start in range(n):
        if seen[start]:
            continue
        cycle = []
        u = start
        while not seen[u]:
            seen[u] = 1
            cycle.append(u)
            u = successor[u]
        assert u == start
        result.append(cycle)
    return result


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
        v, native_h = cycle["length"], cycle["height"]
        h = min(native_h, 3)
        assert len(lower) == v and v % 17 == 0 and 1 <= native_h <= 8
        assert all(a.bit_count() == 8 for a in lower)
        assert not owner_seen.intersection(lower)
        owner_seen.update(lower)
        owners = [full ^ a for a in lower]
        word, native_word = [], []
        for i in range(v):
            mask = native_mask = full
            for j in range(native_h + 1):
                native_mask &= owners[(i + j) % v]
                if j <= h:
                    mask &= owners[(i + j) % v]
            assert mask and mask.bit_count() == 9 - h
            assert native_mask and native_mask & ~mask == 0
            word.append(mask)
            native_word.append(native_mask)
            source_checks += 1
        assert native_word == cycle["source_period"]
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
                                height=h, native_height=native_h, blocks=list(state), rank8=prefix8,
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

    native_successor = [cycle_first[rec["cycle"]] + (rec["position"] + 1) % rec["period"]
                        for rec in records]
    native_predecessor = [cycle_first[rec["cycle"]] + (rec["position"] - 1) % rec["period"]
                          for rec in records]
    states_path = args.out / "capped_periodic_states.json"
    states_path.write_text(json.dumps(records, separators=(",", ":")) + "\n")
    candidates_path = args.out / "complete_neutral_candidates.csv"
    legal_path = args.out / "complete_neutral_legal_edges.csv"
    count = Counter()
    cross = []
    extra_internal = []
    self_by_cycle = Counter()
    native_by_cycle = Counter()
    source_adjacency = [set() for _ in records]
    source_arc_witness = {}
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
                # The physical self-loop is NOT a permissible splice edge.
                # Original successor edges become matching-graph identities.
                if src["id"] != dst["id"]:
                    cut_target = native_predecessor[dst["id"]]
                    source_adjacency[src["id"]].add(cut_target)
                    source_arc_witness[(src["id"], cut_target)] = dst["id"]
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

    # The quotient alone is not a permutation certificate. Build it, then
    # separately analyze the source matching graph and replay one cycle.
    multiplicity = Counter((e["source_cycle"], e["destination_cycle"]) for e in cross)
    adjacency = {c["cycle"]: set() for c in cycles}
    indegree = {c["cycle"]: 0 for c in cycles}
    for u, v in multiplicity:
        adjacency[u].add(v)
        indegree[v] += 1
    component_adjacency = [sorted(adjacency[i]) for i in range(len(cycles))]
    component_sccs = strongly_connected(component_adjacency)
    audit_sccs(component_adjacency, component_sccs)
    component_cycle = chosen_cycle(component_adjacency, component_sccs)
    cross_by_pair = {}
    for e in cross:
        key = (e["source_cycle"], e["destination_cycle"])
        cross_by_pair.setdefault(key, e)
    component_cycle_witness = [cross_by_pair[(u, component_cycle[(i + 1) % len(component_cycle)])]
                               for i, u in enumerate(component_cycle)] if component_cycle else []
    graph = dict(scope="complete same-H nonnative component quotient for D^min(h,3)",
                 vertices=[dict(cycle=c["cycle"], period=c["length"],
                                height=min(c["height"],3), native_height=c["height"]) for c in cycles],
                 edges=[dict(source_cycle=u, destination_cycle=v, multiplicity=multiplicity[u, v])
                        for u, v in sorted(multiplicity)],
                 sccs=component_sccs, chosen_component_cycle=component_cycle,
                 chosen_component_cycle_edge_witnesses=component_cycle_witness,
                 acyclic=all(len(c) == 1 for c in component_sccs),
                 complete_cross_edges=cross)
    graph_path = args.out / "capped_neutral_component_quotient.json"
    graph_path.write_text(json.dumps(graph, indent=2) + "\n")
    source_adjacency = [sorted(neighbors) for neighbors in source_adjacency]
    source_sccs = strongly_connected(source_adjacency)
    audit_sccs(source_adjacency, source_sccs)
    cut_cycle = chosen_cycle(source_adjacency, source_sccs)
    source_path = args.out / "complete_alternative_matching_arcs.csv"
    with source_path.open("w", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(["source_cut_state", "target_cut_state", "legal_destination_state",
                         "source_component", "target_component"])
        for u, neighbors in enumerate(source_adjacency):
            for v in neighbors:
                writer.writerow([u,v,source_arc_witness[u,v],records[u]["cycle"],records[v]["cycle"]])
    source_report = dict(scope="P -> native_pred(Q) for every legal same-H P->Q except physical self-loops",
                         source_sccs=source_sccs, chosen_cut_cycle=cut_cycle,
                         all_cut_components_distinct=(len({records[u]["cycle"] for u in cut_cycle})==len(cut_cycle)) if cut_cycle else None)
    new_cycles = None
    if cut_cycle:
        successor = native_successor.copy()
        reassignment = []
        for i,u in enumerate(cut_cycle):
            v = cut_cycle[(i+1)%len(cut_cycle)]
            q = native_successor[v]
            assert source_arc_witness[u,v] == q and u != q
            assert update(tuple(records[u]["blocks"]),records[q]["first"]) == tuple(records[q]["blocks"])
            successor[u] = q
            reassignment.append(dict(source=u,old_destination=native_successor[u],new_destination=q,
                                     source_component=records[u]["cycle"],target_cut=v,
                                     target_component=records[v]["cycle"]))
        new_cycles = permutation_cycles(successor)
        faithful = []
        for chain in new_cycles:
            word = [records[u]["first"] for u in chain]
            union = reduce(int.__or__,word,0)
            state = ()
            for letter in word:
                state = update(state,letter)
            ok = union == full
            for u,letter in zip(chain,word):
                state = update(state,letter)
                ok = ok and state == tuple(records[u]["blocks"])
            faithful.append(ok)
        source_report.update(reassignment=reassignment,new_cycle_count=len(new_cycles),
                             new_cycle_lengths=[len(c) for c in new_cycles],
                             net_component_saving=len(cycles)-len(new_cycles),
                             every_new_cycle_is_actual_full_ground_periodic_state_walk=all(faithful),
                             nonfaithful_cycle_indices=[i for i,ok in enumerate(faithful) if not ok])
        (args.out / "reassigned_state_cycles.json").write_text(json.dumps(new_cycles,separators=(",",":"))+"\n")
        (args.out / "reassigned_literal_cycles.json").write_text(json.dumps([[records[u]["first"] for u in c] for c in new_cycles],separators=(",",":"))+"\n")
    matching_path = args.out / "capped_alternative_matching_scc_and_cycle.json"
    matching_path.write_text(json.dumps(source_report,indent=2)+"\n")
    report = dict(status="PASS", host=platform.node(),
                  input_sha256=source_sha, cycle_count=len(cycles), state_count=len(records),
                  capped_erosion_letters_reconstructed=source_checks,
                  periodic_states_independently_last_occurrence_replayed=state_checks,
                  counts=dict(count), extra_internal_edge_count=len(extra_internal),
                  component_edges=graph["edges"],
                  nontrivial_component_sccs=[c for c in component_sccs if len(c)>1],
                  source_scc_size_census=dict(Counter(len(c) for c in source_sccs)),
                  nontrivial_source_scc_count=sum(len(c)>1 for c in source_sccs),
                  sccs_independently_verified_by_reachability_and_acyclic_condensation=True,
                  chosen_cut_cycle=cut_cycle,
                  reassignment_summary={k:v for k,v in source_report.items() if k not in ("source_sccs","scope")},
                  scope="Exactly D^min(h,3), without any further entrywise caps. All neutral legal edges tested; one deterministic SCC/cycle diagnostic, no variants.",
                  resources=dict(cpu_seconds=120, wall_seconds=150, address_space_bytes=2*1024**3),
                  elapsed_seconds=time.monotonic()-started,
                  artifacts={p.name: dict(bytes=p.stat().st_size, sha256=file_sha(p))
                             for p in [states_path, candidates_path, legal_path, graph_path,source_path,matching_path]})
    (args.out / "capped_recency_matching_certificate.json").write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({k:v for k,v in report.items() if k not in ("component_edges","reassignment_summary","chosen_cut_cycle")}, indent=2), flush=True)
    print("REASSIGNMENT", json.dumps(dict(cut_cycle_length=len(cut_cycle),
           cut_cycle=cut_cycle if len(cut_cycle)<=30 else cut_cycle[:30],
           new_cycle_count=source_report.get("new_cycle_count"),
           net_component_saving=source_report.get("net_component_saving"),
           faithful=source_report.get("every_new_cycle_is_actual_full_ground_periodic_state_walk"))), flush=True)


if __name__ == "__main__":
    main()
