#!/usr/bin/env python3
"""Isolated h100-only partial compilation, bounded repair, and independent audit.

No existing search, pipeline, answer, or handoff file is modified. A retained
universal word longer than 25744 is a diagnostic, not a new record.
"""

import argparse
from collections import Counter, defaultdict, deque
import csv
from hashlib import sha256
import json
from pathlib import Path
import os
import shlex
import shutil
import socket
import subprocess
import time


STEM = "k17_partial_compile_20260906_c83a1"
K, FULL, W, DEMAND = 17, 131071, 24310, 21777


def check(condition, message):
    if not condition:
        raise ValueError(message)


def write_json(path, value):
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n")


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def read_word(path):
    result = [int(x) for x in path.read_bytes().split()]
    check(result and all(0 < x <= FULL for x in result), f"invalid word {path}")
    return result


def suffix_audit(word):
    """All literal intervals, retaining exact multiplicities without a width cap."""
    counts = [0] * (FULL + 1)
    suffix = {}
    for x in word:
        new = {x: 1}
        for mask, count in suffix.items():
            union = mask | x
            new[union] = new.get(union, 0) + count
        for mask, count in new.items():
            counts[mask] += count
        suffix = new
    check(sum(counts) == len(word) * (len(word) + 1) // 2, "interval multiplicity total")
    return counts


def missing_hist(counts):
    result = [0] * (K + 1)
    for x in range(1, FULL + 1):
        if not counts[x]:
            result[x.bit_count()] += 1
    return result


def next_occurrence_audit(word):
    """Independent forward event scan; even hundred-letter zero gaps are exact."""
    next_at = [len(word)] * K
    seen = bytearray(FULL + 1)
    events = 0
    max_first_full_width = 0
    for start in range(len(word) - 1, -1, -1):
        bits = word[start]
        while bits:
            bit = bits & -bits
            next_at[bit.bit_length() - 1] = start
            bits ^= bit
        ordered = sorted((pos, 1 << bit) for bit, pos in enumerate(next_at) if pos < len(word))
        union, previous_pos = 0, -1
        for pos, bit in ordered:
            if pos != previous_pos and union:
                seen[union] = 1
                events += 1
            union |= bit
            previous_pos = pos
        if union:
            seen[union] = 1
            events += 1
        if union == FULL:
            max_first_full_width = max(max_first_full_width, previous_pos - start + 1)
    return seen, events, max_first_full_width


def factor_cycles(json_path, body_path):
    data = json.loads(json_path.read_text())
    check(tuple(data[key] for key in ("k", "r", "d", "N", "W")) == (17, 9, 3, 1430, W), "factor JSON header")
    lines = body_path.read_text().splitlines()
    check(lines[0] == "K17QF1 17 1430 24310 3" and len(lines) == 1431, "factor body header")
    rows = [tuple(map(int, line.split())) for line in lines[1:]]
    check(all(len(row) == 3 for row in rows), "body triples")
    choices = sorted((low, min(a, b), max(a, b)) for low, a, b in rows)
    check(choices == sorted(tuple(row) for row in data["choices"]), "JSON/body disagreement")
    adjacency = defaultdict(list)
    facets = Counter()
    for low, a, b in choices:
        check(low.bit_count() == 8 and 0 <= a < b < K and not low & ((1 << a) | (1 << b)), "factor choice")
        u0, v0 = low | (1 << a), low | (1 << b)
        for shift in range(K):
            u = ((u0 << shift) | (u0 >> (K - shift))) & FULL
            v = ((v0 << shift) | (v0 >> (K - shift))) & FULL
            adjacency[u].append(v)
            adjacency[v].append(u)
            facets[u & v] += 1
    check(len(adjacency) == W and all(x.bit_count() == 9 and len(set(v)) == len(v) == 2 for x, v in adjacency.items()), "degree two")
    check(len(facets) == W and set(facets.values()) == {1}, "rank-eight rainbow")
    seen, cycles = set(), []
    for start in sorted(adjacency):
        if start in seen:
            continue
        previous, current, cycle = None, start, []
        while current not in seen:
            seen.add(current)
            cycle.append(current)
            left, right = sorted(adjacency[current])
            previous, current = current, left if previous is None or left != previous else right
        check(current == start, "cycle traversal")
        cycles.append(cycle)
    cycles.sort(key=lambda c: (-len(c), c[0]))
    check(list(map(len, cycles)) == data["physical_audit"]["physical_cycle_lengths"], "saved component sizes")
    return cycles


def audit(prefix, factor_json, factor_body):
    report = json.loads(Path(str(prefix) + ".best.json").read_text())
    carrier = factor_cycles(factor_json, factor_body)
    with Path(str(prefix) + ".best.state.tsv").open() as stream:
        rows = list(csv.DictReader(stream, delimiter="\t"))
    check(len(rows) == W, "state row count")
    p, core, letters, assigned = [], [], [], []
    matched = {}
    offset = 0
    cyclic_seen = bytearray(FULL + 1)
    layer_seen = [set() for _ in range(4)]
    for c, cycle in enumerate(carrier):
        component = rows[offset:offset + len(cycle)]
        this_word = []
        for i, row in enumerate(component):
            check((int(row["cycle"]), int(row["position"]), int(row["T"])) == (c, i, cycle[i]), "physical state replay")
            expected_p = FULL
            for age in range(4):
                expected_p &= cycle[(i - age) % len(cycle)]
            high, low, x, owner = (int(row[key]) for key in ("P", "C", "S", "assigned"))
            check(high == expected_p and high.bit_count() == 6 and not low & ~high, "envelope/core containment")
            check(0 < x <= FULL and not low & ~x and not x & ~high, "letter/core containment")
            if owner:
                check(owner == x and x not in matched, "matching duplicate or assignment mismatch")
                matched[x] = offset + i
            p.append(high)
            core.append(low)
            letters.append(x)
            assigned.append(owner)
            this_word.append(x)
        pp, cc, ww = p[offset:], core[offset:], this_word
        check(all((cc[i] | cc[(i + 1) % len(cc)]) == (pp[i] | pp[(i + 1) % len(pp)]) for i in range(len(pp))), "DC != DP")
        envelope_row, word_row = pp, ww
        for depth in range(4):
            check(all(x.bit_count() == 6 + depth for x in envelope_row), "graded envelope rank")
            layer_seen[depth].update(envelope_row)
            if depth:
                check(word_row == envelope_row, "higher word derivative differs from P")
            if depth == 3:
                check(envelope_row == cycle, "D^3 P != T")
            envelope_row = [envelope_row[i] | envelope_row[(i + 1) % len(pp)] for i in range(len(pp))]
            word_row = [word_row[i] | word_row[(i + 1) % len(pp)] for i in range(len(pp))]
        counts = suffix_audit(ww + ww)
        for x in range(1, FULL + 1):
            cyclic_seen[x] |= bool(counts[x])
        offset += len(cycle)
    check(len(matched) == report["matched"], "matching cardinality")
    targets = [x for x in range(1, FULL + 1) if x.bit_count() <= 6]
    adjacency = {x: [] for x in targets}
    for pos, (low, high) in enumerate(zip(core, p)):
        free = high & ~low
        s = free
        while True:
            x = low | s
            if x:
                adjacency[x].append(pos)
            if not s:
                break
            s = (s - 1) & free
    unmatched = set(targets) - matched.keys()
    reachable_left, reachable_right = set(unmatched), set()
    queue = deque(unmatched)
    while queue:
        x = queue.popleft()
        for pos in adjacency[x]:
            if pos in reachable_right:
                continue
            reachable_right.add(pos)
            mate = assigned[pos]
            check(mate != 0, "augmenting path: matching is not maximum")
            if mate not in reachable_left:
                reachable_left.add(mate)
                queue.append(mate)
    cover_size = DEMAND - len(reachable_left) + len(reachable_right)
    check(cover_size == len(matched) == report["matching_cover_size"], "Konig certificate size")
    for x, neighbours in adjacency.items():
        check(x not in reachable_left or all(pos in reachable_right for pos in neighbours), "vertex cover misses an edge")
    unmatched_hist, zero_hist = [0] * 18, [0] * 18
    for x in targets:
        unmatched_hist[x.bit_count()] += x in unmatched
        zero_hist[x.bit_count()] += not adjacency[x]
    check(unmatched_hist == report["unmatched_by_rank"] and zero_hist == report["zero_degree_by_rank"], "matching ledger")
    check(missing_hist(cyclic_seen) == report["cyclic_missing_by_rank"], "cyclic missing census")
    offsets = [0]
    for cycle in carrier:
        offsets.append(offsets[-1] + len(cycle))
    replay = []
    check(sorted(report["cycle_order"]) == list(range(len(carrier))) and report["closure_per_cycle"] == 3, "cycle opening recipe")
    for c, cut, reverse in zip(report["cycle_order"], report["cuts"], report["reverse"]):
        part = letters[offsets[c]:offsets[c + 1]]
        replay.extend(part[(cut + (-i if reverse else i)) % len(part)] for i in range(len(part) + 3))
    base_path = Path(str(prefix) + ".best.partial.word")
    word_path = Path(str(prefix) + ".best.word")
    repair_path = Path(str(prefix) + ".best.repair.word")
    base, word, repair_word = read_word(base_path), read_word(word_path), read_word(repair_path)
    check(base == replay and word == base + repair_word, "literal opening/repair replay")
    check((len(word), len(base), len(repair_word)) == (report["length"], report["base_length"], report["repair_length"]), "word lengths")
    base_counts, final_counts = suffix_audit(base), suffix_audit(word)
    check(missing_hist(base_counts) == report["base_missing_by_rank"], "linear cut census")
    check(not any(missing_hist(final_counts)), "retained word is not universal")
    check(report["final_missing_by_rank"] == [0] * 18, "reported final missing ledger")
    masks = [x for x in range(1, FULL + 1) if not base_counts[x]]
    check(masks == read_word(Path(str(prefix) + ".best.missing.txt")), "literal missing body")
    forward, event_count, max_width = next_occurrence_audit(word)
    check(all(forward[1:]), "independent next-occurrence verification failed")
    cut_lost = [x for x in range(1, FULL + 1) if cyclic_seen[x] and not base_counts[x]]
    cut_gained = [x for x in range(1, FULL + 1) if not cyclic_seen[x] and base_counts[x]]
    result = dict(
        status="VERIFIED_IMPROVEMENT" if len(word) < 25745 else "VERIFIED_UNIVERSAL_DIAGNOSTIC_NOT_IMPROVEMENT",
        length=len(word), covered_nonempty_masks=FULL, missing_masks=0,
        base_length=len(base), repair_length=len(repair_word), base_missing_by_rank=missing_hist(base_counts),
        cyclic_missing_by_rank=missing_hist(cyclic_seen), final_missing_by_rank=missing_hist(final_counts),
        matched=len(matched), matching_demand=DEMAND, matching_deficiency=DEMAND - len(matched),
        matching_min_vertex_cover=cover_size, unmatched_by_rank=unmatched_hist, zero_degree_by_rank=zero_hist,
        graded_envelope_distinct_counts=list(map(len, layer_seen)), physical_cycle_lengths=list(map(len, carrier)),
        cut_lost_masks=cut_lost, cut_gained_masks=cut_gained, forward_union_events=event_count,
        maximum_first_full_witness_width=max_width, word=str(word_path), word_sha256=digest(word_path),
        partial_sha256=digest(base_path), repair_sha256=digest(repair_path),
        state_sha256=digest(Path(str(prefix) + ".best.state.tsv")),
        missing_body_sha256=digest(Path(str(prefix) + ".best.missing.txt")),
        factor_json_sha256=digest(factor_json), factor_body_sha256=digest(factor_body),
    )
    write_json(Path(str(prefix) + ".independent_audit.json"), result)
    print(json.dumps({key: result[key] for key in ("status", "length", "matching_deficiency", "base_missing_by_rank", "word_sha256")}), flush=True)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("preflight", "run", "audit"))
    parser.add_argument("--directory", type=Path, required=True)
    parser.add_argument("--factor", type=Path, action="append", default=[])
    parser.add_argument("--seconds", type=int, default=300)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--seed-base", type=int, default=17090680)
    parser.add_argument("--max-trials", type=int, default=1000)
    args = parser.parse_args()
    check(socket.gethostname().split(".")[0] in ("h100", "arboghast"), "heavy work is restricted to h100")
    check(1 <= args.workers <= 4 and 1 <= args.seconds <= 330, "worker/time bounds")
    directory = args.directory.resolve(strict=True)
    binary = directory / STEM
    if args.mode == "preflight":
        inputs = directory / "inputs"
        inputs.mkdir(exist_ok=True)
        factors = []
        for source in args.factor:
            source = source.resolve(strict=True)
            destination = inputs / source.name
            for original, snapshot in ((source, destination), (source.with_suffix(".txt"), destination.with_suffix(".txt"))):
                if snapshot.exists():
                    check(digest(original) == digest(snapshot), "refuse to replace a different factor snapshot")
                else:
                    shutil.copyfile(original, snapshot)
            cycles = factor_cycles(destination, destination.with_suffix(".txt"))
            factors.append(dict(json=str(destination), body=str(destination.with_suffix(".txt")),
                                source=str(source), json_sha256=digest(destination),
                                body_sha256=digest(destination.with_suffix(".txt")), cycles=list(map(len, cycles))))
        check(factors, "at least one factor required")
        command = ["g++", "-O3", "-DNDEBUG", "-std=c++17", "-Wall", "-Wextra", str(directory / (STEM + ".cpp")), "-o", str(binary)]
        subprocess.run(command, check=True, timeout=60)
        tested = subprocess.run([str(binary), "--self-test"], check=True, capture_output=True, text=True, timeout=40)
        print(tested.stdout, end="", flush=True)
        sources = {path.name: digest(path) for path in directory.iterdir() if path.suffix in (".py", ".cpp")}
        preflight = dict(status="PREFLIGHT_PASS", host=socket.gethostname(), factors=factors,
                         compile_command=shlex.join(command), tests=tested.stdout, sources_sha256=sources,
                         binary_sha256=digest(binary), max_workers=4, existing_processes_untouched=True)
        write_json(directory / "preflight.json", preflight)
        print(json.dumps(preflight, indent=2), flush=True)
        return
    preflight = json.loads((directory / "preflight.json").read_text())
    if args.mode == "run":
        check(digest(binary) == preflight["binary_sha256"], "binary changed after preflight")
        for name, expected in preflight["sources_sha256"].items():
            check(digest(directory / name) == expected, "source changed after preflight")
        run = directory / "run"
        run.mkdir(exist_ok=False)
        env = dict(os.environ, OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1", MKL_NUM_THREADS="1")
        jobs, children = [], []
        started = time.monotonic()
        try:
            for i in range(args.workers):
                # Three independent cores on the better L2 factor, one on the
                # two-cycle factor with the smaller intrinsic rank-six deficit.
                factor = preflight["factors"][min(i // 3, len(preflight["factors"]) - 1)]
                check(digest(Path(factor["body"])) == factor["body_sha256"], "factor snapshot changed")
                prefix = run / f"worker{i}"
                command = [str(binary), factor["body"], str(prefix), str(args.seconds), str(args.seed_base + i), str(args.max_trials)]
                log = Path(str(prefix) + ".log").open("w")
                process = subprocess.Popen(command, stdout=log, stderr=subprocess.STDOUT, env=env)
                children.append((process, log))
                jobs.append(dict(worker=i, pid=process.pid, command=command, shell_command=shlex.join(command),
                                 prefix=str(prefix), factor=factor))
                print(f"START worker={i} pid={process.pid}", flush=True)
            write_json(directory / "commands.json", jobs)
            while any(process.poll() is None for process, _ in children):
                if time.monotonic() - started > args.seconds + 8:
                    raise TimeoutError("owned compiler batch exceeded watchdog")
                time.sleep(0.2)
        finally:
            for job, (process, log) in zip(jobs, children):
                if process.poll() is None:
                    process.terminate()
                    try:
                        process.wait(timeout=2)
                    except subprocess.TimeoutExpired:
                        process.kill()
                        process.wait()
                job["returncode"] = process.returncode
                log.close()
            write_json(directory / "finished.json", dict(jobs=jobs, worker_wall_seconds=time.monotonic() - started))
        check(all(job["returncode"] == 0 for job in jobs), "worker failure; inspect isolated logs")
    jobs = json.loads((directory / "commands.json").read_text())
    audit_start = time.monotonic()
    results = [audit(Path(job["prefix"]), Path(job["factor"]["json"]), Path(job["factor"]["body"])) for job in jobs]
    best = min(results, key=lambda result: result["length"])
    retained = directory / (f"verified_k17_length{best['length']}.word" if best["length"] < 25745 else f"diagnostic_k17_length{best['length']}.word")
    shutil.copyfile(best["word"], retained)
    check(digest(retained) == best["word_sha256"], "retained copy hash mismatch")
    summary = dict(status=best["status"], best=best, candidates=results, retained_word=str(retained),
                   audit_wall_seconds=time.monotonic() - audit_start, preflight=preflight,
                   finished=json.loads((directory / "finished.json").read_text()))
    write_json(directory / "summary.json", summary)
    print(json.dumps(dict(status=summary["status"], length=best["length"], missing=0, retained=str(retained), sha256=digest(retained))), flush=True)


if __name__ == "__main__":
    main()
