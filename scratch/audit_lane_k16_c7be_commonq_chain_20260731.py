#!/usr/bin/env python3
"""Independent, literal audit of the c7be true-four-filter compiler lane.

The audit reconstructs the carrier from the SHA-pinned K15 parent, verifies
every carrier interval-OR target and every fixed-depth shadow, rebuilds the
pinned P/Q envelope and lower incidence graph, and runs an independent
Hopcroft--Karp replay.  If a common-Q CNF prefix is supplied, its map and all
clauses are compared line-for-line with an independently generated model.
If a SAT model is supplied, the physical word is reconstructed without
trusting mapped letter variables and all 65,535 masks are replayed literally.

No SAT solver or search is launched by this script.
"""

from __future__ import annotations

import argparse
from collections import Counter, deque
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path
from typing import Iterable, Iterator


ROOT = Path(__file__).resolve().parents[1]
SCRATCH = ROOT / "scratch"
PARENT = SCRATCH / "K15_FOURFILTER_SEED.word"
PARENT_META = SCRATCH / "K15_FOURFILTER_SEED.meta.json"
NATURAL = SCRATCH / "k16_true_fourfilter_natural_targets_20260731.word"
CARRIER = SCRATCH / "k16_true_fourfilter_two_reroot_uppercomplete_targets_20260731.word"
CARRIER_ALIAS = SCRATCH / "k16_true_fourfilter_endpoint_reroot_targets_20260731.word"
CAPACITY_AUDIT = SCRATCH / "r_k16_true_fourfilter_reroot_pin8000_capacity_20260731.audit.json"
HALL_AUDIT = SCRATCH / "r_k16_true_fourfilter_reroot_pin8000_hall_20260731.audit.json"
ARTIFACT_DIR = SCRATCH / "k16_trueff_commoncap_direct_cnf_20260731"
BUILDER_SOURCE = ARTIFACT_DIR / "build_k16_trueff_commoncap_matching_cnf_20260731.cpp"
BUILDER_BINARY = ARTIFACT_DIR / "build"
DECODER_SOURCE = ARTIFACT_DIR / "decode_verify_k16_trueff_commoncap_matching_20260731.py"
REFERENCE_DECODE_AUDIT = ARTIFACT_DIR / "decode.audit.json"
DEFAULT_OUTPUT = SCRATCH / "k16_c7be_commonq_chain_independent_20260731.audit.json"

EXPECTED = {
    "parent": "51f57125ea3e145e08ed9d5f8816d22313a010907588457260c824c6f40217f4",
    "parent_meta": "d1006c375c2cb69f595e7d56ffd0e585d4741ae3d4562bfd9e3d1141f223fea7",
    "natural": "0f6d64e9311ef634169964350baa8f817b17b9d1619970c881f87e7346550a5c",
    "carrier": "c7beccc38489ad0ce4f203fa11e348a9fb04a18418cdc8ac9dce038ddde06906",
    "capacity_audit": "0f75bca6cadef6b243e11c78a320c59bb8b2b29414eb2519b1d57c49fc0661f1",
    "hall_audit": "7dc309006db70c84be5e2065f38045863cefe54270d26c300ad03fa05f79dc15",
    "builder_source": "1cc95858620183305e5b58bf158795ea5174cf22ca0fc9fb2a0cd555aeb2aa7e",
    "builder_binary": "68976fdc15bfd3bedad8030f0271ddb2db9e193c033f9a93899093e8ca38c946",
    "decoder_source": "6395121fca6bbd7a9466ef9e035db5258f4ead7a419ebade011b89a07898a94b",
    "reference_decode_audit": "a7fdc56461c1d25d496853740143badf9a88f06fba0b064d1de2185325c3a700",
    "cnf": "7fc512869e0c525183c4796b746da87a1eb4f7652eebfc6465b839218b7e6e0c",
    "map": "abd76cf89a1b80123e46be3067de8fffa7173710dee2bcc3e39cccd8c398849d",
    "model_meta": "8f67b41a1ac7ee2c582e3927624489351b7289add665d1a1837d68ad7700aab2",
    "solver_model": "2efa5c7b3a73f53d913127e4c6620c56e7828f02fa04a87ae5e5e59242796165",
    "decoded_word": "890ac346ce142f5f9ed564d487ff3e2fb99aea93ae2c104ec13765fa5d3814fe",
}

K, RANK, WIDTH, HEIGHT = 16, 8, 12870, 3
LENGTH = WIDTH + HEIGHT
FULL = (1 << K) - 1
PIN = 0x8000
PIN_POSITION = 6389
START_HOLES = (12870, 12871, 12872)
DEADLINE_HOLES = (0, 1, 6388)


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def stable(value: object) -> str:
    return sha256(json.dumps(
        value, sort_keys=True, separators=(",", ":")
    ).encode()).hexdigest()


def canonical(values: Iterable[int]) -> bytes:
    return (" ".join(map(str, values)) + "\n").encode()


def load_word(path: Path) -> list[int]:
    return [int(token, 0) for token in path.read_text().split()]


def derivative(values: list[int]) -> list[int]:
    return [a | b for a, b in zip(values, values[1:])]


def rank_universe(rank: int) -> set[int]:
    return {
        sum(1 << bit for bit in subset)
        for subset in combinations(range(K), rank)
    }


def all_interval_ors(values: list[int]) -> set[int]:
    """All distinct interval ORs, maintained by right endpoint."""
    seen: set[int] = set()
    ending: set[int] = set()
    for value in values:
        ending = {value} | {old | value for old in ending}
        seen.update(ending)
    return seen


def fixed_depth_decks(values: list[int]) -> dict[str, object]:
    upper: dict[str, object] = {}
    lower: dict[str, object] = {}
    for depth in range(1, RANK + 1):
        unions: set[int] = set()
        intersections: set[int] = set()
        for left in range(len(values) - depth):
            union = 0
            intersection = FULL
            for value in values[left:left + depth + 1]:
                union |= value
                intersection &= value
            if union.bit_count() == RANK + depth:
                unions.add(union)
            if intersection.bit_count() == RANK - depth:
                intersections.add(intersection)
        upper_missing = rank_universe(RANK + depth) - unions
        lower_missing = rank_universe(RANK - depth) - intersections
        assert not upper_missing and not lower_missing
        upper[str(depth)] = len(unions)
        lower[str(depth)] = len(intersections)
    return {"upper_distinct": upper, "lower_distinct": lower}


def reconstruct_lineage() -> tuple[list[int], dict[str, object]]:
    assert digest(PARENT) == EXPECTED["parent"]
    assert digest(PARENT_META) == EXPECTED["parent_meta"]
    assert digest(NATURAL) == EXPECTED["natural"]
    assert digest(CARRIER) == EXPECTED["carrier"]
    assert digest(CARRIER_ALIAS) == EXPECTED["carrier"]
    assert digest(CAPACITY_AUDIT) == EXPECTED["capacity_audit"]
    assert digest(HALL_AUDIT) == EXPECTED["hall_audit"]

    metadata = json.loads(PARENT_META.read_text())
    assert metadata["opening"] == [5134, 0, 5, 1, 0]
    assert metadata["dir"] == "fwd"
    parent = load_word(PARENT)
    assert len(parent) == 6438
    d2 = derivative(derivative(parent))
    d3 = derivative(d2)
    assert len(d2) == 6436 and len(set(d2)) == 6436
    assert len(d3) == 6435 and len(set(d3)) == 6435
    assert [(i, x) for i, x in enumerate(d2) if x.bit_count() != 7] == [
        (6390, 0x13C8)
    ]
    assert all(value.bit_count() == RANK for value in d3)

    natural = (
        list(reversed([PIN | value for value in d2[:6390]]))
        + d3
        + list(reversed([PIN | value for value in d2[6391:6436]]))
    )
    assert canonical(natural) == NATURAL.read_bytes()
    prefix = list(reversed(natural[:6389])) + natural[6389:]
    reroot = prefix[:12826] + list(reversed(prefix[12826:]))
    assert canonical(reroot) == CARRIER.read_bytes() == CARRIER_ALIAS.read_bytes()
    assert len(reroot) == len(set(reroot)) == WIDTH
    assert all(value.bit_count() == RANK for value in reroot)
    assert set(reroot) == rank_universe(RANK)

    adjacent = Counter(a | b for a, b in zip(reroot, reroot[1:]))
    assert rank_universe(9) <= set(adjacent)
    all_ors = all_interval_ors(reroot)
    required = {
        mask for mask in range(1, 1 << K) if mask.bit_count() >= RANK
    }
    assert required <= all_ors
    decks = fixed_depth_decks(reroot)

    return reroot, {
        "parent": str(PARENT.relative_to(ROOT)),
        "parent_sha256": EXPECTED["parent"],
        "parent_metadata": str(PARENT_META.relative_to(ROOT)),
        "parent_metadata_sha256": EXPECTED["parent_meta"],
        "opening": metadata["opening"],
        "direction": metadata["dir"],
        "d2_unique_exception": {"index": 6390, "value": "0x13c8"},
        "natural": str(NATURAL.relative_to(ROOT)),
        "natural_sha256": EXPECTED["natural"],
        "formula": (
            "reverse(0x8000|D2[:6390]) + D3 + "
            "reverse(0x8000|D2[6391:6436])"
        ),
        "reroot_operations_zero_based_inclusive": [[0, 6388], [12826, 12869]],
        "carrier": str(CARRIER.relative_to(ROOT)),
        "carrier_alias": str(CARRIER_ALIAS.relative_to(ROOT)),
        "carrier_sha256": EXPECTED["carrier"],
        "middle_count": len(reroot),
        "middle_universe_missing": 0,
        "q1_universe_covered": len(rank_universe(9)),
        "all_rank_ge_8_interval_or_masks_covered": len(required),
        "fixed_depth_decks": decks,
    }


def build_schedule(targets: list[int]) -> tuple[
        list[int], list[int], list[int], list[int], list[int]]:
    starts = [p for p in range(LENGTH) if p not in START_HOLES]
    deadlines = [p for p in range(LENGTH) if p not in DEADLINE_HOLES]
    assert len(starts) == len(deadlines) == WIDTH
    depths = [right - left for left, right in zip(starts, deadlines)]
    assert all(0 <= depth <= HEIGHT for depth in depths)
    assert sum(depths) == 32224

    envelope = [FULL] * LENGTH
    for target, left, right in zip(targets, starts, deadlines):
        for position in range(left, right + 1):
            envelope[position] &= target
    assert all(envelope)
    before_pin = envelope[:]
    assert before_pin[PIN_POSITION] == 0xC304
    envelope[PIN_POSITION] = PIN
    assert all(envelope)
    for target, left, right in zip(targets, starts, deadlines):
        realized = 0
        for position in range(left, right + 1):
            realized |= envelope[position]
        assert realized == target
    return starts, deadlines, depths, before_pin, envelope


def build_cells(starts: list[int], depths: list[int]) -> tuple[
        list[tuple[int, int, str]], dict[tuple[int, int], int], int]:
    specs: list[tuple[int, int, str]] = []
    lookup: dict[tuple[int, int], int] = {}
    for left, depth in zip(starts, depths):
        for length in range(1, depth + 1):
            assert (left, length) not in lookup
            lookup[left, length] = len(specs)
            specs.append((left, length, "selected"))
    assert len(specs) == 32224
    for left in START_HOLES:
        for length in range(1, min(HEIGHT, LENGTH - left) + 1):
            assert (left, length) not in lookup
            lookup[left, length] = len(specs)
            specs.append((left, length, "omitted-start physical"))
    assert len(specs) == 32230
    reserved = lookup[PIN_POSITION, 1]
    assert reserved == 12781
    return specs, lookup, reserved


def build_graph(
    targets: list[int], starts: list[int], deadlines: list[int],
    envelope: list[int], specs: list[tuple[int, int, str]],
    lookup: dict[tuple[int, int], int], reserved: int,
) -> tuple[list[tuple[int, int]], list[list[int]], list[list[int]],
           list[int], list[int], int]:
    mandatory = [0] * len(specs)
    for target, row_left, row_right in zip(targets, starts, deadlines):
        bits = target
        while bits:
            bit_value = bits & -bits
            bits -= bit_value
            possible = [
                p for p in range(row_left, row_right + 1)
                if envelope[p] & bit_value
            ]
            assert possible
            lo, hi = possible[0], possible[-1]
            for length in range(1, HEIGHT + 1):
                for left in range(max(0, hi - length + 1), lo + 1):
                    cell = lookup.get((left, length))
                    if cell is not None:
                        mandatory[cell] |= bit_value

    allowed: list[int] = []
    for left, length, _kind in specs:
        value = 0
        for position in range(left, left + length):
            value |= envelope[position]
        allowed.append(value)

    edges: list[tuple[int, int]] = []
    by_target: list[list[int]] = [[] for _ in range(1 << K)]
    by_cell: list[list[int]] = [[] for _ in specs]
    raw_incidences = 0
    for cell, (left, length, _kind) in enumerate(specs):
        subset = allowed[cell]
        while subset:
            if (subset.bit_count() < RANK
                    and not (mandatory[cell] & ~subset)
                    and all(envelope[p] & subset
                            for p in range(left, left + length))):
                raw_incidences += 1
                if cell != reserved and subset != PIN:
                    variable = len(edges) + 1
                    edges.append((subset, cell))
                    by_target[subset].append(variable)
                    by_cell[cell].append(variable)
            subset = (subset - 1) & allowed[cell]

    # The cap turns the reserved cell into the sole 0x8000 incidence.  Thus
    # the post-pin graph has 347,678 edges before fixing that singleton and
    # the exact residual direct model has 347,677.
    assert raw_incidences == 347678, raw_incidences
    assert len(edges) == 347677
    remaining = [
        mask for mask in range(1, 1 << K)
        if mask.bit_count() < RANK and mask != PIN
    ]
    assert len(remaining) == 26331
    assert all(by_target[target] for target in remaining)
    return edges, by_target, by_cell, allowed, mandatory, raw_incidences


def hopcroft_karp(by_target: list[list[int]], edges: list[tuple[int, int]],
                  right_count: int) -> tuple[int, list[int], list[int]]:
    lefts = [
        mask for mask in range(1, 1 << K)
        if mask.bit_count() < RANK and mask != PIN
    ]
    pair_left = [-1] * (1 << K)
    pair_right = [-1] * right_count
    distance = [-1] * (1 << K)

    def bfs() -> bool:
        queue: deque[int] = deque()
        found = False
        for left in lefts:
            if pair_left[left] < 0:
                distance[left] = 0
                queue.append(left)
            else:
                distance[left] = -1
        while queue:
            left = queue.popleft()
            for variable in by_target[left]:
                cell = edges[variable - 1][1]
                mate = pair_right[cell]
                if mate < 0:
                    found = True
                elif distance[mate] < 0:
                    distance[mate] = distance[left] + 1
                    queue.append(mate)
        return found

    def dfs(left: int) -> bool:
        for variable in by_target[left]:
            cell = edges[variable - 1][1]
            mate = pair_right[cell]
            if mate < 0 or (
                    distance[mate] == distance[left] + 1 and dfs(mate)):
                pair_left[left] = cell
                pair_right[cell] = left
                return True
        distance[left] = -1
        return False

    size = 0
    while bfs():
        for left in lefts:
            if pair_left[left] < 0 and dfs(left):
                size += 1
    return size, pair_left, pair_right


def build_letter_variables(envelope: list[int], edge_count: int) -> tuple[
        list[list[int]], list[tuple[int, int]]]:
    next_variable = edge_count + 1
    avar = [[0] * K for _ in range(LENGTH)]
    avec: list[tuple[int, int]] = []
    for position in range(LENGTH):
        for bit in range(K):
            if envelope[position] & (1 << bit):
                avar[position][bit] = next_variable
                next_variable += 1
                avec.append((position, bit))
    assert len(avec) == 70759
    return avar, avec


def build_blockers(
    edges: list[tuple[int, int]], specs: list[tuple[int, int, str]],
    envelope: list[int], avar: list[list[int]], avec: list[tuple[int, int]],
) -> list[list[int]]:
    a0 = len(edges) + 1
    blockers: list[list[int]] = [[] for _ in avec]
    for variable, (target, cell) in enumerate(edges, 1):
        left, length, _kind = specs[cell]
        for position in range(left, left + length):
            blocked = envelope[position] & ~target & FULL
            while blocked:
                bit_value = blocked & -blocked
                blocked -= bit_value
                bit = bit_value.bit_length() - 1
                blockers[avar[position][bit] - a0].append(variable)
    assert sum(map(len, blockers)) == 941437
    return blockers


def amo_clauses(xs: list[int], aux0: int) -> Iterator[list[int]]:
    n = len(xs)
    if n < 2:
        return
    yield [-xs[0], aux0]
    for i in range(1, n - 1):
        previous, current = aux0 + i - 1, aux0 + i
        yield [-xs[i], current]
        yield [-previous, current]
        yield [-xs[i], -previous]
    yield [-xs[-1], -(aux0 + n - 2)]


def allocate_auxiliaries(
    by_target: list[list[int]], by_cell: list[list[int]], avec: list[tuple[int, int]],
) -> tuple[list[int], list[int], int]:
    next_variable = 347677 + len(avec) + 1
    target_aux = [-1] * (1 << K)
    for target in range(1, 1 << K):
        if target.bit_count() < RANK and target != PIN and len(by_target[target]) >= 2:
            target_aux[target] = next_variable
            next_variable += len(by_target[target]) - 1
    cell_aux = [-1] * len(by_cell)
    for cell, group in enumerate(by_cell):
        if len(group) >= 2:
            cell_aux[cell] = next_variable
            next_variable += len(group) - 1
    assert next_variable - 1 == 1055230
    return target_aux, cell_aux, next_variable - 1


class ClauseReader:
    def __init__(self, path: Path, variables: int, clauses: int):
        self.path = path
        self.stream = path.open()
        header = self.stream.readline().split()
        assert header == ["p", "cnf", str(variables), str(clauses)]
        self.count = 0

    def check(self, expected: Iterable[int]) -> None:
        line = self.stream.readline()
        assert line, f"CNF ended at clause {self.count}"
        actual = [int(token) for token in line.split()]
        assert actual and actual[-1] == 0
        actual.pop()
        expected_list = list(expected)
        assert actual == expected_list, (
            f"clause {self.count + 1} mismatch: "
            f"{actual[:12]} != {expected_list[:12]}"
        )
        self.count += 1

    def finish(self, expected_count: int) -> None:
        assert self.count == expected_count
        assert not self.stream.readline()
        self.stream.close()


def audit_map(
    path: Path, edges: list[tuple[int, int]], specs: list[tuple[int, int, str]],
    avec: list[tuple[int, int]],
) -> None:
    with path.open() as stream:
        assert next(stream).rstrip("\n") == (
            "kind\tvar\ttarget\tcell\tstart\tlength\tposition\tbit"
        )
        for variable, (target, cell) in enumerate(edges, 1):
            left, length, _kind = specs[cell]
            expected = [
                "y", str(variable), str(target), str(cell), str(left),
                str(length), "-1", "-1",
            ]
            assert next(stream).split() == expected
        a0 = len(edges) + 1
        for offset, (position, bit) in enumerate(avec):
            expected = [
                "a", str(a0 + offset), "-1", "-1", "-1", "-1",
                str(position), str(bit),
            ]
            assert next(stream).split() == expected
        assert not stream.readline()


def audit_cnf(
    path: Path, targets: list[int], starts: list[int], deadlines: list[int],
    edges: list[tuple[int, int]], by_target: list[list[int]],
    by_cell: list[list[int]], specs: list[tuple[int, int, str]],
    avar: list[list[int]], avec: list[tuple[int, int]], blockers: list[list[int]],
) -> tuple[int, int]:
    target_aux, cell_aux, variables = allocate_auxiliaries(by_target, by_cell, avec)
    clauses = 4513893
    reader = ClauseReader(path, variables, clauses)

    for target in range(1, 1 << K):
        if target.bit_count() < RANK and target != PIN:
            reader.check(by_target[target])
            for clause in amo_clauses(by_target[target], target_aux[target]):
                reader.check(clause)
    for cell, group in enumerate(by_cell):
        for clause in amo_clauses(group, cell_aux[cell]):
            reader.check(clause)

    a0 = len(edges) + 1
    for offset, group in enumerate(blockers):
        a = a0 + offset
        for y in group:
            reader.check([-a, -y])
        reader.check([a, *group])

    for position in range(LENGTH):
        reader.check(avar[position][bit] for bit in range(K) if avar[position][bit])
    for target, left, right in zip(targets, starts, deadlines):
        for bit in range(K):
            if target & (1 << bit):
                reader.check(
                    avar[position][bit]
                    for position in range(left, right + 1)
                    if avar[position][bit]
                )
    for variable, (target, cell) in enumerate(edges, 1):
        left, length, _kind = specs[cell]
        for bit in range(K):
            if target & (1 << bit):
                reader.check([
                    -variable,
                    *(avar[position][bit]
                      for position in range(left, left + length)
                      if avar[position][bit]),
                ])
    reader.finish(clauses)
    return variables, clauses


def read_model(path: Path) -> tuple[str, dict[int, bool]]:
    status = "UNKNOWN"
    assignment: dict[int, bool] = {}
    for line in path.read_text(errors="replace").splitlines():
        if line.startswith("s "):
            status = line[2:].strip()
        if line.startswith("v "):
            for token in line[2:].split():
                literal = int(token)
                if literal:
                    assignment[abs(literal)] = literal > 0
    return status, assignment


def verify_model_clauses(cnf: Path, assignment: dict[int, bool], variables: int) -> None:
    assert all(variable in assignment for variable in range(1, variables + 1))
    with cnf.open() as stream:
        header = stream.readline().split()
        assert header[:2] == ["p", "cnf"]
        for number, line in enumerate(stream, 1):
            literals = [int(token) for token in line.split()][:-1]
            assert any(
                assignment[abs(literal)] == (literal > 0)
                for literal in literals
            ), f"model falsifies clause {number}"


def decode_model(
    model: Path, cnf: Path, targets: list[int], starts: list[int],
    deadlines: list[int], envelope: list[int], edges: list[tuple[int, int]],
    by_target: list[list[int]], specs: list[tuple[int, int, str]],
    reserved: int, avar: list[list[int]], variables: int,
    decoded_word: Path | None,
) -> dict[str, object]:
    status, assignment = read_model(model)
    assert "SATISFIABLE" in status and "UNSATISFIABLE" not in status
    verify_model_clauses(cnf, assignment, variables)
    selected = [
        (variable, *edges[variable - 1])
        for variable in range(1, len(edges) + 1) if assignment[variable]
    ]
    assert len(selected) == 26331
    assert all(sum(assignment[v] for v in by_target[target]) == 1
               for target in range(1, 1 << K)
               if target.bit_count() < RANK and target != PIN)
    cells = [cell for _variable, _target, cell in selected]
    assert len(cells) == len(set(cells)) and reserved not in cells

    word = envelope[:]
    for _variable, target, cell in selected:
        left, length, _kind = specs[cell]
        for position in range(left, left + length):
            word[position] &= target
    assert all(word) and word[PIN_POSITION] == PIN
    for position in range(LENGTH):
        for bit in range(K):
            variable = avar[position][bit]
            if variable:
                assert assignment[variable] == bool(word[position] & (1 << bit))
    for target, left, right in zip(targets, starts, deadlines):
        realized = 0
        for position in range(left, right + 1):
            realized |= word[position]
        assert realized == target
    for _variable, target, cell in selected:
        left, length, _kind = specs[cell]
        realized = 0
        for position in range(left, left + length):
            realized |= word[position]
        assert realized == target

    covered = all_interval_ors(word)
    missing = [mask for mask in range(1, 1 << K) if mask not in covered]
    assert not missing
    if decoded_word is not None:
        decoded_word.write_bytes(canonical(word))
    return {
        "model": str(model),
        "model_sha256": digest(model),
        "selected_lower_incidences": len(selected),
        "literal_word_length": len(word),
        "literal_nonempty_masks_covered": 65535,
        "missing_masks": 0,
        "word_sha256": sha256(canonical(word)).hexdigest(),
        "word_output": str(decoded_word) if decoded_word is not None else None,
        "letter_rank_histogram": dict(sorted(Counter(
            value.bit_count() for value in word
        ).items())),
    }


def verify_decoded_word(
    path: Path, targets: list[int], starts: list[int], deadlines: list[int],
    envelope: list[int], specs: list[tuple[int, int, str]],
) -> dict[str, object]:
    word = load_word(path)
    assert len(word) == LENGTH
    assert all(0 < value <= FULL for value in word)
    assert all(not (value & ~cap) for value, cap in zip(word, envelope))
    assert word[PIN_POSITION] == PIN

    for target, left, right in zip(targets, starts, deadlines):
        realized = 0
        for position in range(left, right + 1):
            realized |= word[position]
        assert realized == target

    short_seen: set[int] = set()
    for left, length, _kind in specs:
        realized = 0
        for position in range(left, left + length):
            realized |= word[position]
        if realized.bit_count() < RANK:
            short_seen.add(realized)
    required_lower = {
        mask for mask in range(1, 1 << K) if mask.bit_count() < RANK
    }
    assert required_lower <= short_seen

    all_seen = all_interval_ors(word)
    missing = [mask for mask in range(1, 1 << K) if mask not in all_seen]
    assert not missing
    return {
        "word": str(path),
        "word_sha256": digest(path),
        "canonical_bytes": path.read_bytes() == canonical(word),
        "word_length": len(word),
        "nonempty_letters": len(word),
        "letters_outside_pinned_envelope": 0,
        "middle_replay_failures": 0,
        "physical_short_cell_lower_masks_covered": len(required_lower),
        "nonempty_interval_or_masks_covered": 65535,
        "missing_masks": 0,
        "letter_rank_histogram": dict(sorted(Counter(
            value.bit_count() for value in word
        ).items())),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cnf-prefix", type=Path)
    parser.add_argument("--model", type=Path)
    parser.add_argument("--word", type=Path)
    parser.add_argument("--decoded-word", type=Path)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    if args.model is not None:
        assert args.cnf_prefix is not None

    targets, lineage = reconstruct_lineage()
    starts, deadlines, depths, before_pin, envelope = build_schedule(targets)
    specs, lookup, reserved = build_cells(starts, depths)
    edges, by_target, by_cell, allowed, mandatory, raw_incidences = build_graph(
        targets, starts, deadlines, envelope, specs, lookup, reserved
    )
    matching_size, pair_left, _pair_right = hopcroft_karp(
        by_target, edges, len(specs)
    )
    assert matching_size == 26331
    avar, avec = build_letter_variables(envelope, len(edges))
    blockers = build_blockers(edges, specs, envelope, avar, avec)

    source_hash = digest(BUILDER_SOURCE)
    binary_hash = digest(BUILDER_BINARY)
    decoder_hash = digest(DECODER_SOURCE)
    assert source_hash == EXPECTED["builder_source"]
    assert binary_hash == EXPECTED["builder_binary"]
    assert decoder_hash == EXPECTED["decoder_source"]
    assert digest(REFERENCE_DECODE_AUDIT) == EXPECTED["reference_decode_audit"]
    builder_text = BUILDER_SOURCE.read_text()
    decoder_text = DECODER_SOURCE.read_text()
    assert "edges.size()!=347677" in builder_text
    assert "assert len(y_rows) == 347677" in decoder_text

    model_output: dict[str, object] | None = None
    literal_word_output: dict[str, object] | None = None
    cnf_output: dict[str, object] | None = None
    variables = 1055230
    if args.cnf_prefix is not None:
        cnf = Path(str(args.cnf_prefix) + ".cnf")
        mapping = Path(str(args.cnf_prefix) + ".map.tsv")
        metadata = Path(str(args.cnf_prefix) + ".meta.json")
        audit_map(mapping, edges, specs, avec)
        variables, clauses = audit_cnf(
            cnf, targets, starts, deadlines, edges, by_target, by_cell,
            specs, avar, avec, blockers
        )
        meta = json.loads(metadata.read_text())
        assert digest(cnf) == EXPECTED["cnf"]
        assert digest(mapping) == EXPECTED["map"]
        assert digest(metadata) == EXPECTED["model_meta"]
        assert meta["schema"] == "k16.trueff.commoncap-direct-cnf.v1"
        assert meta["target"] == "k16_true_fourfilter_endpoint_reroot_targets_20260731.word"
        assert meta["target_sha256"] == EXPECTED["carrier"]
        assert meta["variables"] == variables
        assert meta["clauses"] == clauses
        assert meta["incidence_variables"] == len(edges)
        assert meta["letter_bit_variables"] == len(avec)
        assert meta["remaining_lower_targets"] == 26331
        assert meta["physical_cells"] == len(specs)
        assert meta["reserved_singleton"] == {
            "target": PIN, "position": PIN_POSITION, "cell": reserved,
        }
        cnf_output = {
            "prefix": str(args.cnf_prefix),
            "cnf_sha256": digest(cnf),
            "map_sha256": digest(mapping),
            "meta_sha256": digest(metadata),
            "variables": variables,
            "clauses": clauses,
            "map_rows": len(edges) + len(avec),
            "all_map_rows_exact": True,
            "all_clauses_exact": True,
        }
        if args.model is not None:
            assert digest(args.model) == EXPECTED["solver_model"]
            model_output = decode_model(
                args.model, cnf, targets, starts, deadlines, envelope, edges,
                by_target, specs, reserved, avar, variables, args.decoded_word
            )

    if args.word is not None:
        assert digest(args.word) == EXPECTED["decoded_word"]
        literal_word_output = verify_decoded_word(
            args.word, targets, starts, deadlines, envelope, specs
        )
        if model_output is not None:
            assert literal_word_output["word_sha256"] == model_output["word_sha256"]

    remaining = [
        mask for mask in range(1, 1 << K)
        if mask.bit_count() < RANK and mask != PIN
    ]
    matching_pairs = [
        [target, pair_left[target]] for target in remaining
    ]
    core: dict[str, object] = {
        "schema": "k16.c7be.commonq-chain-independent.v1",
        "status": (
            "PASS_LITERAL_UNIVERSAL_WORD" if literal_word_output is not None else
            "PASS_CARRIER_PIN_HALL_AND_EXACT_CNF_NO_MODEL"
            if cnf_output is not None else
            "PASS_CARRIER_PIN_AND_MARGINAL_HALL_NO_CNF"
        ),
        "lineage_and_literal_carrier": lineage,
        "authenticated_prior_audits": {
            "capacity_audit": str(CAPACITY_AUDIT.relative_to(ROOT)),
            "capacity_audit_sha256": EXPECTED["capacity_audit"],
            "hall_audit": str(HALL_AUDIT.relative_to(ROOT)),
            "hall_audit_sha256": EXPECTED["hall_audit"],
            "note": "Hashes only; every carrier/schedule/Hall fact above was recomputed.",
        },
        "pinned_schedule": {
            "start_holes": list(START_HOLES),
            "deadline_holes": list(DEADLINE_HOLES),
            "selected_area": sum(depths),
            "physical_cells": len(specs),
            "reserved_cell": reserved,
            "pin_target": "0x8000",
            "pin_position": PIN_POSITION,
            "before_pin": f"0x{before_pin[PIN_POSITION]:04x}",
            "after_pin": f"0x{envelope[PIN_POSITION]:04x}",
            "middle_replay_failures": 0,
            "envelope_rank_histogram": dict(sorted(Counter(
                value.bit_count() for value in envelope
            ).items())),
        },
        "independent_marginal_hall": {
            "post_pin_incidences_before_singleton_reservation": raw_incidences,
            "residual_incidence_count": len(edges),
            "remaining_target_count": len(remaining),
            "zero_host_count": sum(not by_target[target] for target in remaining),
            "matching_size": matching_size,
            "deficiency": len(remaining) - matching_size,
            "matching_pairs_sha256": stable(matching_pairs),
            "allowed_rank_histogram": dict(sorted(Counter(
                value.bit_count() for value in allowed
            ).items())),
            "mandatory_rank_histogram": dict(sorted(Counter(
                value.bit_count() for value in mandatory
            ).items())),
        },
        "common_q_model": {
            "builder_source": str(BUILDER_SOURCE.relative_to(ROOT)),
            "builder_source_sha256": source_hash,
            "landed_builder_binary": str(BUILDER_BINARY.relative_to(ROOT)),
            "landed_builder_binary_sha256": binary_hash,
            "decoder_source": str(DECODER_SOURCE.relative_to(ROOT)),
            "decoder_source_sha256": decoder_hash,
            "reference_decode_audit": str(REFERENCE_DECODE_AUDIT.relative_to(ROOT)),
            "reference_decode_audit_sha256": EXPECTED["reference_decode_audit"],
            "model_semantics": {
                "exactly_one_cell_per_lower_target": True,
                "at_most_one_target_per_cell": True,
                "letter_bit_iff_no_selected_blocker": True,
                "nonempty_physical_letters": True,
                "every_middle_bit_supplied": True,
                "every_selected_lower_bit_supplied": True,
            },
            "independent_counts": {
                "incidence_variables": len(edges),
                "letter_bit_variables": len(avec),
                "blocker_occurrences": sum(map(len, blockers)),
                "variables": variables,
                "clauses": 4513893,
            },
            "source_authentication_gap": (
                "The C++ source prints the constant expected carrier SHA into metadata "
                "but does not compute the input file SHA; this audit computes it first."
            ),
            "artifact_compatibility": {
                "corrected_source_residual_y_count": 347677,
                "decoder_asserted_y_count": 347677,
                "decoder_compatible_with_corrected_map": True,
            },
            "generated_output": cnf_output,
            "decoded_model": model_output,
            "literal_decoded_word": literal_word_output,
        },
        "scope": [
            "No artifact status field is used as evidence.",
            "No SAT solver or carrier search is launched.",
            "The decoded word is checked directly against the pinned envelope, physical lower cells, middle schedule, and all 65,535 interval-OR masks.",
            "When a SAT model is supplied, every variable and every CNF clause are additionally checked and the independently reconstructed model word must equal the decoded word.",
        ],
    }
    payload = dict(core)
    payload["checker_sha256"] = digest(Path(__file__))
    payload["payload_sha256"] = stable(core)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": payload["status"],
        "output": str(args.output),
        "checker_sha256": payload["checker_sha256"],
        "payload_sha256": payload["payload_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
