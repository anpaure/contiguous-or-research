#!/usr/bin/env python3
"""Repo-owned equivariant carrier + graded one-core pipeline.

This file is intentionally self-contained.  In particular it does not import
the live files under ``~/Downloads/opusproblem/work``.  It implements:

* the composite-safe Z_k quotient catalogue on the two central ranks;
* a CP-SAT strict-spiral carrier model with residence and upper-q1 eager;
* sound CEGAR for lower-q2, the rank-h Hall positive-degree gate, and all
  remaining upper shadows;
* stable explicit selector serialization (IDs are never trusted alone);
* maximal erosion and an equivariant sparse one-core search;
* exact weighted quotient Hall followed by an exact physical matching;
* upper-safe cutting, prefix closure, and exhaustive direct-word checking.

At d=3, lower-q3 is not treated as another frozen carrier row.  Its missing
targets are nevertheless exact zero-degree rank-(r-3) vertices of the graded
Hall graph, so they are checked and CEGARed as a compiler-positive-degree
gate before the more expensive Hall/core search.

Heavy ``search-carrier`` runs belong on the remote CPU host.  ``compile`` and
``verify`` are deterministic audits and are small at k <= 15.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from hashlib import sha256
from itertools import combinations
import json
from math import comb, gcd
from pathlib import Path
import random
import time
from typing import Iterable, Iterator


SCHEMA = "graded-quotient-carrier-v1"


def stable_json(value: object) -> bytes:
    return json.dumps(value, separators=(",", ":"), sort_keys=True).encode()


def mask_from_combination(items: Iterable[int]) -> int:
    value = 0
    for item in items:
        value |= 1 << item
    return value


def derivative(row: list[int]) -> list[int]:
    return [row[i] | row[(i + 1) % len(row)] for i in range(len(row))]


def linear_derivative(row: list[int]) -> list[int]:
    return [row[i] | row[i + 1] for i in range(len(row) - 1)]


def cyclic_runs(bits: list[bool]) -> list[list[int]]:
    """Return the maximal nonempty cyclic 1-runs as ordered position lists."""
    n = len(bits)
    if not any(bits):
        return []
    if all(bits):
        return [list(range(n))]
    zero = bits.index(False)
    runs: list[list[int]] = []
    current: list[int] = []
    for step in range(1, n + 1):
        i = (zero + step) % n
        if bits[i]:
            current.append(i)
        elif current:
            runs.append(current)
            current = []
    if current:
        runs.append(current)
    return runs


def legal_path_cover_patterns(length: int) -> list[tuple[int, ...]]:
    """Vertex covers of a path's edges with both boundary vertices forced."""
    if length <= 0:
        return []
    if length == 1:
        return [(1,)]
    answer = []
    for middle in range(1 << max(0, length - 2)):
        pattern = [1]
        pattern.extend((middle >> j) & 1 for j in range(length - 2))
        pattern.append(1)
        if all(pattern[j] or pattern[j + 1] for j in range(length - 1)):
            answer.append(tuple(pattern))
    answer.sort(key=lambda p: (sum(p), p))
    return answer


def choose_path_cover_pattern(
    length: int, rng: random.Random, randomized: bool
) -> tuple[int, ...]:
    """Choose a minimum legal cover without enumerating Fibonacci-many covers."""
    if length <= 0:
        raise ValueError("positive run length required")
    if length == 1:
        return (1,)
    if not randomized:
        # This is the canonical depth-one erosion core used in the k=11
        # theorem audit: alternating from the first forced endpoint, then
        # force the last endpoint if parity left it out.
        answer = [1 if index % 2 == 0 else 0 for index in range(length)]
        answer[-1] = 1
        return tuple(answer)

    # Dynamic program the minimum suffix weight for each previous bit, then
    # sample uniformly only among tied optimal transitions.  Sparse cores
    # maximize literal flexibility; adding gratuitous protected coordinates
    # can only delete Hall edges.
    infinity = length + 1
    dp = [[infinity, infinity] for _ in range(length + 1)]
    dp[length] = [0, 0]
    for i in range(length - 1, 0, -1):
        for previous in (0, 1):
            choices = []
            for bit in (0, 1):
                if (previous == 0 and bit == 0) or (i == length - 1 and bit == 0):
                    continue
                choices.append(bit + dp[i + 1][bit])
            dp[i][previous] = min(choices)
    answer = [1]
    for i in range(1, length):
        previous = answer[-1]
        candidates = []
        for bit in (0, 1):
            if (previous == 0 and bit == 0) or (i == length - 1 and bit == 0):
                continue
            if bit + dp[i + 1][bit] == dp[i][previous]:
                candidates.append(bit)
        answer.append(rng.choice(candidates))
    if not all(answer[j] or answer[j + 1] for j in range(length - 1)):
        raise AssertionError("random path cover sampler produced an uncovered edge")
    return tuple(answer)


@dataclass(frozen=True)
class Choice:
    lower: int
    a: int
    b: int

    def as_tuple(self) -> tuple[int, int, int]:
        return (self.lower, self.a, self.b)


class QuotientCatalogue:
    """Exact quotient catalogue for an odd central-level instance."""

    def __init__(self, k: int):
        if k % 2 != 1:
            raise ValueError("the current quotient carrier model requires odd k")
        self.k = k
        self.full = (1 << k) - 1
        self.r = (k + 1) // 2
        self.m = self.r - 1
        self.W = comb(k, self.r)
        lower_mass = sum(comb(k, j) for j in range(1, self.r))
        d = 0
        while d * self.W + comb(d + 1, 2) < lower_mass:
            d += 1
        self.d = d
        self.h = self.r - d
        self.low = self.orbit_reps(self.m)
        self.mid = self.orbit_reps(self.r)
        self.low_index = {value: i for i, value in enumerate(self.low)}
        self.mid_index = {value: i for i, value in enumerate(self.mid)}
        # Central freeness is gcd(k,m)=gcd(k,r)=1, valid for every odd k.
        if len(self.low) * k != comb(k, self.m):
            raise AssertionError("lower central action unexpectedly non-free")
        if len(self.mid) * k != self.W:
            raise AssertionError("upper central action unexpectedly non-free")
        self.N = len(self.mid)
        self._shadow_state_cache: dict[
            tuple[str, int, int], tuple[list[int], list[tuple[int, int, int, int]]]
        ] = {}
        self._build_choices()

    def rotate(self, value: int, shift: int) -> int:
        shift %= self.k
        if shift == 0:
            return value
        return (
            (value << shift) | (value >> (self.k - shift))
        ) & self.full

    def canonical_shift(self, value: int) -> tuple[int, int]:
        """Return (representative, shift) with value=rotate(rep,shift)."""
        best = value
        best_forward = 0
        current = value
        for forward in range(1, self.k):
            current = self.rotate(current, 1)
            if current < best:
                best = current
                best_forward = forward
        return best, (-best_forward) % self.k

    def canonical(self, value: int) -> int:
        return self.canonical_shift(value)[0]

    def orbit(self, value: int) -> tuple[int, ...]:
        return tuple(sorted({self.rotate(value, s) for s in range(self.k)}))

    def orbit_reps(self, rank: int) -> list[int]:
        return sorted(
            {
                self.canonical(mask_from_combination(items))
                for items in combinations(range(self.k), rank)
            }
        )

    def _build_choices(self) -> None:
        """Use one stable table, excluding quotient self-loop choices."""
        self.choices: list[Choice] = []
        self.choice_index: dict[tuple[int, int, int], int] = {}
        skipped = 0
        for lower in self.low:
            outside = [x for x in range(self.k) if not (lower >> x) & 1]
            for a, b in combinations(outside, 2):
                u, v = lower | (1 << a), lower | (1 << b)
                if self.canonical(u) == self.canonical(v):
                    skipped += 1
                    continue
                choice = Choice(lower, a, b)
                index = len(self.choices)
                self.choices.append(choice)
                self.choice_index[choice.as_tuple()] = index
        self.skipped_self_loops = skipped
        self.choice_table_sha256 = sha256(
            stable_json([choice.as_tuple() for choice in self.choices])
        ).hexdigest()

        self.arc_data: list[tuple[int, int, int, int, int, int]] = []
        self.arcs_by_choice: list[list[int]] = [[] for _ in self.choices]
        self.choices_by_lower: dict[int, list[int]] = defaultdict(list)
        self.upper1_cover: dict[int, list[int]] = defaultdict(list)
        for ci, choice in enumerate(self.choices):
            lower, a, b = choice.as_tuple()
            self.choices_by_lower[lower].append(ci)
            self.upper1_cover[self.canonical(lower | (1 << a) | (1 << b))].append(ci)
            for first, second in ((a, b), (b, a)):
                source_physical = lower | (1 << first)
                target_physical = lower | (1 << second)
                source_rep, source_shift = self.canonical_shift(source_physical)
                target_rep, target_shift = self.canonical_shift(target_physical)
                inv = -source_shift
                source = self.rotate(source_physical, inv)
                target = self.rotate(target_physical, inv)
                if source != source_rep:
                    raise AssertionError("source normalization failed")
                deleted = (source & ~target).bit_length() - 1
                inserted_source_frame = (target & ~source).bit_length() - 1
                shift = (target_shift - source_shift) % self.k
                inserted_target_frame = (inserted_source_frame - shift) % self.k
                arc_index = len(self.arc_data)
                self.arc_data.append(
                    (
                        ci,
                        self.mid_index[source_rep],
                        self.mid_index[target_rep],
                        shift,
                        deleted,
                        inserted_target_frame,
                    )
                )
                self.arcs_by_choice[ci].append(arc_index)

        self.upper1 = self.orbit_reps(self.r + 1)
        if any(not self.upper1_cover[target] for target in self.upper1):
            raise AssertionError("self-loop exclusion destroyed upper-q1 support")

    def explicit_selection(self, ids: Iterable[int]) -> list[tuple[int, int, int]]:
        return [self.choices[index].as_tuple() for index in ids]

    def ids_from_explicit(
        self, choices: Iterable[Iterable[int]]
    ) -> list[int]:
        result = []
        for raw in choices:
            lower, a, b = map(int, raw)
            if a > b:
                a, b = b, a
            key = (lower, a, b)
            if key not in self.choice_index:
                raise ValueError(f"choice absent from stable table: {key}")
            result.append(self.choice_index[key])
        return result

    def edge_choice(self, u: int, v: int) -> int:
        lower = u & v
        lower_rep, shift = self.canonical_shift(lower)
        inv = -shift
        ur, vr = self.rotate(u, inv), self.rotate(v, inv)
        a = (ur & ~lower_rep).bit_length() - 1
        b = (vr & ~lower_rep).bit_length() - 1
        if a > b:
            a, b = b, a
        return self.choice_index[(lower_rep, a, b)]

    def directed_arc(self, u: int, v: int) -> int:
        """Stable quotient arc realizing the oriented physical edge u->v."""
        choice = self.edge_choice(u, v)
        source_rep, source_shift = self.canonical_shift(u)
        target_rep, target_shift = self.canonical_shift(v)
        shift = (target_shift - source_shift) % self.k
        matches = [
            arc
            for arc in self.arcs_by_choice[choice]
            if self.arc_data[arc][1] == self.mid_index[source_rep]
            and self.arc_data[arc][2] == self.mid_index[target_rep]
            and self.arc_data[arc][3] == shift
        ]
        if len(matches) != 1:
            raise ValueError(
                f"oriented edge has {len(matches)} quotient arcs, expected one"
            )
        return matches[0]

    def physical_cycles(self, selected: Iterable[int]) -> list[list[int]]:
        adjacency: dict[int, list[int]] = defaultdict(list)
        for ci in selected:
            choice = self.choices[ci]
            u0 = choice.lower | (1 << choice.a)
            v0 = choice.lower | (1 << choice.b)
            for shift in range(self.k):
                u, v = self.rotate(u0, shift), self.rotate(v0, shift)
                adjacency[u].append(v)
                adjacency[v].append(u)
        if len(adjacency) != self.W:
            raise ValueError(f"selector spans {len(adjacency)} of {self.W} vertices")
        if Counter(map(len, adjacency.values())) != {2: self.W}:
            raise ValueError("selector is not a physical 2-factor")
        seen = set()
        cycles = []
        for start in sorted(adjacency):
            if start in seen:
                continue
            cycle = []
            previous = None
            current = start
            while current not in seen:
                seen.add(current)
                cycle.append(current)
                left, right = sorted(adjacency[current])
                if previous is None:
                    nxt = left
                else:
                    nxt = right if left == previous else left
                previous, current = current, nxt
            cycles.append(cycle)
        return sorted(cycles, key=len, reverse=True)

    def physical_cycle(self, selected: Iterable[int]) -> list[int]:
        cycles = self.physical_cycles(selected)
        if len(cycles) != 1:
            raise ValueError(f"selector has {len(cycles)} physical cycles")
        return cycles[0]

    def strict_spiral_voltage(self, cycle: list[int]) -> int:
        if len(cycle) != self.W:
            return -1
        for voltage in range(self.k):
            if all(
                cycle[i + self.N] == self.rotate(cycle[i], voltage)
                for i in range(self.W - self.N)
            ):
                return voltage
        # The deterministic traversal can run opposite to the quotient order,
        # but the same test already includes all residues, including -v.
        return -1

    def residence_violations(self, cycle: list[int]) -> list[tuple[int, int, int]]:
        result = []
        for coordinate in range(self.k):
            runs = cyclic_runs([bool(value & (1 << coordinate)) for value in cycle])
            for run in runs:
                if len(run) <= self.d:
                    result.append((coordinate, run[0], len(run)))
        return result

    def lower_missing(self, cycle: list[int], q: int) -> list[int]:
        got = set()
        n = len(cycle)
        for i in range(n):
            value = cycle[i]
            for age in range(1, q + 1):
                value &= cycle[(i + age) % n]
            if value.bit_count() == self.r - q:
                got.add(self.canonical(value))
        return [target for target in self.orbit_reps(self.r - q) if target not in got]

    def factor_lower_missing(self, cycles: list[list[int]], q: int) -> list[int]:
        got = set()
        for cycle in cycles:
            n = len(cycle)
            for i in range(n):
                value = cycle[i]
                for age in range(1, q + 1):
                    value &= cycle[(i + age) % n]
                if value.bit_count() == self.r - q:
                    got.add(self.canonical(value))
        return [target for target in self.orbit_reps(self.r - q) if target not in got]

    def upper_missing(self, cycle: list[int]) -> list[int]:
        got = set()
        n = len(cycle)
        for start in range(n):
            value = cycle[start]
            for age in range(1, n):
                old = value
                value |= cycle[(start + age) % n]
                if value != old and value.bit_count() > self.r:
                    got.add(self.canonical(value))
                if value == self.full:
                    break
        need = []
        for rank in range(self.r + 1, self.k + 1):
            need.extend(self.orbit_reps(rank))
        return [target for target in need if target not in got]

    def factor_upper_missing(self, cycles: list[list[int]]) -> list[int]:
        got = {self.full}
        for cycle in cycles:
            n = len(cycle)
            for start in range(n):
                value = cycle[start]
                for age in range(1, n):
                    old = value
                    value |= cycle[(start + age) % n]
                    if value != old and value.bit_count() > self.r:
                        got.add(self.canonical(value))
                    if value == self.full:
                        break
        need = []
        for rank in range(self.r + 1, self.k + 1):
            need.extend(self.orbit_reps(rank))
        return [target for target in need if target not in got]

    def upper_safe_cuts(self, cycle: list[int]) -> list[int]:
        """All cut edges for which every upper target has a noncrossing witness."""
        all_cuts = (1 << self.W) - 1
        allowed: dict[int, int] = defaultdict(int)
        # The full set is always the OR of the complete output word; it does
        # not need a proper nonwrapping carrier-interval witness.
        allowed[self.full] = all_cuts
        for start in range(self.W):
            value = cycle[start]
            crossed = 0
            for age in range(1, self.W):
                crossed |= 1 << ((start + age - 1) % self.W)
                old = value
                value |= cycle[(start + age) % self.W]
                if value != old and self.r < value.bit_count() < self.k:
                    allowed[value] |= all_cuts ^ crossed
                if value == self.full:
                    break
        safe = all_cuts
        for rank in range(self.r + 1, self.k + 1):
            for items in combinations(range(self.k), rank):
                target = mask_from_combination(items)
                safe &= allowed[target]
                if not safe:
                    return []
        result = []
        while safe:
            bit = safe & -safe
            result.append(bit.bit_length() - 1)
            safe ^= bit
        return result

    # ---- motif builders used by sound carrier CEGAR ----

    def cover_lower_q2(self, orbit_rep: int) -> list[list[int]]:
        groups = set()
        outside = [x for x in range(self.k) if not (orbit_rep >> x) & 1]
        for extra in combinations(outside, self.r - orbit_rep.bit_count()):
            middle = orbit_rep | mask_from_combination(extra)
            a, b = extra
            out = [x for x in range(self.k) if not (middle >> x) & 1]
            for deleted_left, deleted_right in ((a, b), (b, a)):
                for inserted_left in out:
                    left = (middle & ~(1 << deleted_left)) | (1 << inserted_left)
                    for inserted_right in out:
                        right = (middle & ~(1 << deleted_right)) | (1 << inserted_right)
                        if (left & middle & right) != orbit_rep:
                            continue
                        try:
                            c1 = self.edge_choice(left, middle)
                            c2 = self.edge_choice(middle, right)
                        except KeyError:
                            continue
                        if c1 != c2:
                            groups.add(tuple(sorted((c1, c2))))
        return [list(group) for group in sorted(groups)]

    def cover_lower_q3(self, orbit_rep: int) -> list[list[int]]:
        """All 3-edge motifs whose four carrier vertices intersect in S.

        This is consumed as the rank-h positive-degree CEGAR gate at d=3,
        not as an additional frozen derivative row in the graded compiler.
        """
        if orbit_rep.bit_count() != self.r - 3:
            raise ValueError("lower-q3 motif requires a rank-(r-3) target")
        groups = set()
        outside_s = [x for x in range(self.k) if not (orbit_rep >> x) & 1]
        for extra in combinations(outside_s, 3):
            first_middle = orbit_rep | mask_from_combination(extra)
            outside_first = [
                x for x in range(self.k) if not (first_middle >> x) & 1
            ]
            for deleted_middle in extra:
                for inserted_middle in outside_first:
                    second_middle = (
                        (first_middle & ~(1 << deleted_middle))
                        | (1 << inserted_middle)
                    )
                    common_extras = [x for x in extra if x != deleted_middle]
                    for deleted_left, deleted_right in (
                        (common_extras[0], common_extras[1]),
                        (common_extras[1], common_extras[0]),
                    ):
                        for inserted_left in outside_first:
                            left = (
                                (first_middle & ~(1 << deleted_left))
                                | (1 << inserted_left)
                            )
                            outside_second = [
                                x
                                for x in range(self.k)
                                if not (second_middle >> x) & 1
                            ]
                            for inserted_right in outside_second:
                                right = (
                                    (second_middle & ~(1 << deleted_right))
                                    | (1 << inserted_right)
                                )
                                if (
                                    left
                                    & first_middle
                                    & second_middle
                                    & right
                                ) != orbit_rep:
                                    continue
                                try:
                                    choices = (
                                        self.edge_choice(left, first_middle),
                                        self.edge_choice(first_middle, second_middle),
                                        self.edge_choice(second_middle, right),
                                    )
                                except KeyError:
                                    continue
                                if len(set(choices)) == 3:
                                    groups.add(tuple(sorted(choices)))
        return [list(group) for group in sorted(groups)]

    def shadow_state_template(
        self, mode: str, q: int, orbit_rep: int
    ) -> tuple[list[int], list[tuple[int, int, int, int]]]:
        """Compact exact state graph for a lower/upper depth-q witness.

        For ``mode='intersection'`` the states are all central supersets of a
        rank-``r-q`` target.  For ``mode='union'`` they are all central subsets
        of a rank-``r+q`` target.  Each table row identifies a physical
        Johnson step with its unique directed quotient arc.
        """
        if q < 1:
            raise ValueError("shadow depth must be positive")
        if mode == "intersection":
            if orbit_rep.bit_count() != self.r - q:
                raise ValueError("lower shadow target has the wrong rank")
        elif mode == "union":
            if orbit_rep.bit_count() != self.r + q:
                raise ValueError("upper shadow target has the wrong rank")
        else:
            raise ValueError("shadow mode must be 'intersection' or 'union'")
        key = (mode, q, orbit_rep)
        cached = self._shadow_state_cache.get(key)
        if cached is not None:
            return cached
        if mode == "intersection":
            outside = [x for x in range(self.k) if not (orbit_rep >> x) & 1]
            states = [
                orbit_rep | mask_from_combination(extra)
                for extra in combinations(outside, q)
            ]
            mandatory = orbit_rep
            allowed = self.full
        else:
            target_bits = [x for x in range(self.k) if orbit_rep >> x & 1]
            states = [mask_from_combination(items) for items in combinations(target_bits, self.r)]
            mandatory = 0
            allowed = orbit_rep
        state_index = {value: index for index, value in enumerate(states)}
        transitions: list[tuple[int, int, int, int]] = []
        for source_index, source in enumerate(states):
            removable = [
                x
                for x in range(self.k)
                if source & (1 << x) and not (mandatory & (1 << x))
            ]
            insertable = [
                x
                for x in range(self.k)
                if allowed & (1 << x) and not (source & (1 << x))
            ]
            for deleted in removable:
                for inserted in insertable:
                    target = (source & ~(1 << deleted)) | (1 << inserted)
                    try:
                        arc = self.directed_arc(source, target)
                    except KeyError:
                        # A quotient self-loop is deliberately absent from
                        # the strict-spiral catalogue.
                        continue
                    # In the lower representation the q-set defect consists
                    # of the extras above S, so a carrier deletion removes a
                    # defect coordinate.  In the upper representation it is
                    # the omitted q-set U\T, so a carrier insertion removes
                    # a defect coordinate.
                    defect_deleted = deleted if mode == "intersection" else inserted
                    transitions.append(
                        (source_index, state_index[target], arc, defect_deleted)
                    )
        result = (states, transitions)
        self._shadow_state_cache[key] = result
        return result

    def upper_reachability_boundary(
        self, orbit_rep: int, selected_arcs: Iterable[int]
    ) -> tuple[bool, list[int]]:
        """Separate exact unrestricted upper-shadow coverage.

        A node is ``(accumulated_union, current_state)``.  Every central
        state inside the target is a legal interval start.  From a reachable
        node, selected quotient arcs advance the physical carrier and update
        the accumulated union.  Reaching the full target is therefore
        equivalent to a contiguous carrier interval with that union.

        If no accepting node is reachable, return the distinct quotient-arc
        labels leaving the reachable set.  Every accepting path must cross
        this boundary, so ``OR(boundary arc variables)`` is a valid exact
        CEGAR cut.  The current selector violates it by construction.

        Unlike ``shadow-state-path``, this permits arbitrary witness length;
        that distinction is necessary for upper depths q >= 3.
        """
        depth = orbit_rep.bit_count() - self.r
        if depth < 1:
            raise ValueError("upper shadow target must lie above the middle rank")
        if orbit_rep != self.canonical(orbit_rep):
            raise ValueError("upper shadow target must be a canonical orbit representative")
        if orbit_rep == self.full:
            # The complete output word always has union [k], so the search
            # loop never needs a carrier-interval cut for this target.
            return True, []

        states, transitions = self.shadow_state_template(
            "union", depth, orbit_rep
        )
        outgoing: list[list[tuple[int, int]]] = [[] for _ in states]
        for source, destination, arc, _token in transitions:
            outgoing[source].append((destination, arc))

        chosen = set(map(int, selected_arcs))
        reachable = {(state, index) for index, state in enumerate(states)}
        queue = deque(reachable)
        while queue:
            accumulated, source = queue.popleft()
            if accumulated == orbit_rep:
                return True, []
            for destination, arc in outgoing[source]:
                if arc not in chosen:
                    continue
                node = (accumulated | states[destination], destination)
                if node not in reachable:
                    reachable.add(node)
                    queue.append(node)

        boundary = set()
        for accumulated, source in reachable:
            for destination, arc in outgoing[source]:
                node = (accumulated | states[destination], destination)
                if node not in reachable:
                    boundary.add(arc)
        if boundary & chosen:
            raise AssertionError("selected arc unexpectedly leaves its reachable set")
        return False, sorted(boundary)

    def lower_q3_state_template(
        self, orbit_rep: int
    ) -> tuple[list[int], list[tuple[int, int, int, int]]]:
        """Backward-compatible diagnostic wrapper for lower depth three."""
        return self.shadow_state_template("intersection", 3, orbit_rep)

    def cover_upper_q2(self, orbit_rep: int) -> list[list[int]]:
        groups = set()
        bits = [x for x in range(self.k) if orbit_rep >> x & 1]
        for middle_items in combinations(bits, self.r):
            middle = mask_from_combination(middle_items)
            missing = [x for x in bits if not (middle >> x) & 1]
            if len(missing) != 2:
                continue
            p, q = missing
            for a in middle_items:
                left = (middle & ~(1 << a)) | (1 << p)
                for b in middle_items:
                    right = (middle & ~(1 << b)) | (1 << q)
                    if (left | middle | right) != orbit_rep:
                        continue
                    try:
                        c1 = self.edge_choice(left, middle)
                        c2 = self.edge_choice(middle, right)
                    except KeyError:
                        continue
                    if c1 != c2:
                        groups.add(tuple(sorted((c1, c2))))
        return [list(group) for group in sorted(groups)]


class Dinic:
    def __init__(self, n: int):
        self.graph: list[list[list[int]]] = [[] for _ in range(n)]

    def add(self, u: int, v: int, capacity: int) -> None:
        forward = [v, capacity, len(self.graph[v])]
        backward = [u, 0, len(self.graph[u])]
        self.graph[u].append(forward)
        self.graph[v].append(backward)

    def flow(self, source: int, sink: int) -> int:
        total = 0
        while True:
            level = [-1] * len(self.graph)
            level[source] = 0
            queue = deque([source])
            while queue:
                u = queue.popleft()
                for v, capacity, _ in self.graph[u]:
                    if capacity and level[v] < 0:
                        level[v] = level[u] + 1
                        queue.append(v)
            if level[sink] < 0:
                return total
            cursor = [0] * len(self.graph)

            def send(u: int, amount: int) -> int:
                if u == sink:
                    return amount
                while cursor[u] < len(self.graph[u]):
                    edge = self.graph[u][cursor[u]]
                    v, capacity, reverse = edge
                    if capacity and level[v] == level[u] + 1:
                        pushed = send(v, min(amount, capacity))
                        if pushed:
                            edge[1] -= pushed
                            self.graph[v][reverse][1] += pushed
                            return pushed
                    cursor[u] += 1
                return 0

            while True:
                pushed = send(source, 10**9)
                if not pushed:
                    break
                total += pushed

    def reachable(self, source: int) -> set[int]:
        seen = {source}
        queue = deque([source])
        while queue:
            u = queue.popleft()
            for v, capacity, _ in self.graph[u]:
                if capacity and v not in seen:
                    seen.add(v)
                    queue.append(v)
        return seen


def maximum_matching(adjacency: list[list[int]], right_size: int) -> list[int]:
    left = [-1] * len(adjacency)
    right = [-1] * right_size
    distance = [-1] * len(adjacency)

    def bfs() -> bool:
        queue = deque()
        found = False
        for u in range(len(adjacency)):
            if left[u] < 0:
                distance[u] = 0
                queue.append(u)
            else:
                distance[u] = -1
        while queue:
            u = queue.popleft()
            for v in adjacency[u]:
                mate = right[v]
                if mate < 0:
                    found = True
                elif distance[mate] < 0:
                    distance[mate] = distance[u] + 1
                    queue.append(mate)
        return found

    def dfs(u: int) -> bool:
        for v in adjacency[u]:
            mate = right[v]
            if mate < 0 or (
                distance[mate] == distance[u] + 1 and dfs(mate)
            ):
                left[u] = v
                right[v] = u
                return True
        distance[u] = -1
        return False

    while bfs():
        for u in range(len(adjacency)):
            if left[u] < 0:
                dfs(u)
    return left


def maximal_erosion(cycle: list[int], k: int, d: int) -> list[int]:
    full = (1 << k) - 1
    n = len(cycle)
    return [
        full
        & __import__("functools").reduce(
            int.__and__, (cycle[(i - age) % n] for age in range(d + 1))
        )
        for i in range(n)
    ]


def find_spiral_voltage(catalogue: QuotientCatalogue, cycle: list[int]) -> int:
    voltage = catalogue.strict_spiral_voltage(cycle)
    if voltage < 0 or gcd(voltage, catalogue.k) != 1:
        raise ValueError("cycle is not a unit-voltage strict spiral")
    return voltage


def make_equivariant_core(
    catalogue: QuotientCatalogue,
    envelope: list[int],
    voltage: int,
    rng: random.Random,
    randomized: bool,
) -> list[int]:
    """Choose a Z_k-equivariant one-core from coordinate zero's trace."""
    support = [bool(value & 1) for value in envelope]
    runs = cyclic_runs(support)
    if not runs:
        raise ValueError("coordinate zero has empty envelope trace")
    base_selected: set[int] = set()
    for run in runs:
        pattern = choose_path_cover_pattern(len(run), rng, randomized)
        base_selected.update(pos for pos, bit in zip(run, pattern) if bit)

    core = [0] * catalogue.W
    inverse_voltage = pow(voltage, -1, catalogue.k)
    # g^t sends (position,coordinate) -> (position+tN, coordinate+t*v).
    for coordinate in range(catalogue.k):
        t = (coordinate * inverse_voltage) % catalogue.k
        shift = t * catalogue.N
        bit = 1 << coordinate
        for base_position in base_selected:
            core[(base_position + shift) % catalogue.W] |= bit
    if any(core[i] & ~envelope[i] for i in range(catalogue.W)):
        raise AssertionError("constructed core escapes its envelope")
    if derivative(core) != derivative(envelope):
        raise AssertionError("constructed sequence is not a one-core")
    if any(
        core[i + catalogue.N] != catalogue.rotate(core[i], voltage)
        for i in range(catalogue.W - catalogue.N)
    ):
        raise AssertionError("constructed one-core is not equivariant")
    return core


def target_list(k: int, h: int) -> list[int]:
    return [value for value in range(1, 1 << k) if value.bit_count() <= h]


def hall_adjacency(
    envelope: list[int], core: list[int], targets: list[int]
) -> list[list[int]]:
    index = {target: i for i, target in enumerate(targets)}
    adjacency = [[] for _ in targets]
    for position, (low, high) in enumerate(zip(core, envelope)):
        remainder = high & ~low
        subset = remainder
        while True:
            candidate = low | subset
            if candidate and candidate in index:
                adjacency[index[candidate]].append(position)
            if subset == 0:
                break
            subset = (subset - 1) & remainder
    return adjacency


def weighted_quotient_hall(
    catalogue: QuotientCatalogue,
    targets: list[int],
    adjacency: list[list[int]],
) -> tuple[int, int, dict[str, object]]:
    orbit_members: dict[int, set[int]] = defaultdict(set)
    for target in targets:
        orbit_members[catalogue.canonical(target)].add(target)
    orbits = sorted(orbit_members)
    orbit_index = {orbit: i for i, orbit in enumerate(orbits)}
    quotient_adjacency = [set() for _ in orbits]
    for target, neighbours in zip(targets, adjacency):
        quotient_adjacency[orbit_index[catalogue.canonical(target)]].update(
            position % catalogue.N for position in neighbours
        )

    source = 0
    left_base = 1
    right_base = left_base + len(orbits)
    sink = right_base + catalogue.N
    network = Dinic(sink + 1)
    demand = 0
    for oi, orbit in enumerate(orbits):
        weight = len(orbit_members[orbit])
        demand += weight
        network.add(source, left_base + oi, weight)
        for right in quotient_adjacency[oi]:
            network.add(left_base + oi, right_base + right, 10**9)
    for right in range(catalogue.N):
        network.add(right_base + right, sink, catalogue.k)
    value = network.flow(source, sink)
    reachable = network.reachable(source) if value < demand else set()
    deficient_orbits = [
        orbits[oi]
        for oi in range(len(orbits))
        if left_base + oi in reachable
    ]
    deficient_positions = [
        right
        for right in range(catalogue.N)
        if right_base + right in reachable
    ]
    report = {
        "target_orbits": len(orbits),
        "position_orbits": catalogue.N,
        "orbit_size_histogram": dict(
            sorted(Counter(len(members) for members in orbit_members.values()).items())
        ),
        "flow": value,
        "demand": demand,
        "deficiency": demand - value,
        "deficient_target_orbits": deficient_orbits,
        "deficient_position_orbits": deficient_positions,
    }
    return value, demand, report


def exhaustive_missing(word: list[int], k: int) -> set[int]:
    got = set()
    full = (1 << k) - 1
    for start in range(len(word)):
        value = 0
        for end in range(start, len(word)):
            value |= word[end]
            got.add(value)
            if value == full:
                break
    return set(range(1, 1 << k)) - got


def validate_carrier(
    catalogue: QuotientCatalogue, selected: list[int]
) -> tuple[list[int], dict[str, object]]:
    if len(selected) != catalogue.N or len(set(selected)) != catalogue.N:
        raise ValueError("selector must contain exactly N distinct choices")
    used_lower = [catalogue.choices[index].lower for index in selected]
    if len(set(used_lower)) != len(catalogue.low):
        raise ValueError("selector is not a perfect lower-q1 rainbow")
    cycle = catalogue.physical_cycle(selected)
    voltage = find_spiral_voltage(catalogue, cycle)
    residence = catalogue.residence_violations(cycle)
    lower_q2 = catalogue.lower_missing(cycle, 2)
    lower_q3 = catalogue.lower_missing(cycle, 3) if catalogue.d >= 3 else []
    upper = catalogue.upper_missing(cycle)
    report = {
        "physical_cycle_length": len(cycle),
        "physical_cycle_sha256": sha256(stable_json(cycle)).hexdigest(),
        "voltage": voltage,
        "residence_violations": residence,
        "lower_q2_missing": lower_q2,
        "lower_q3_positive_degree_missing": lower_q3,
        "upper_missing": upper,
        "carrier_pass": not residence and not lower_q2 and not lower_q3 and not upper,
    }
    return cycle, report


def validate_cycle_cover(
    catalogue: QuotientCatalogue, selected: list[int]
) -> tuple[list[list[int]], dict[str, object]]:
    """Audit a connectivity-free equivariant physical 2-factor."""
    if len(selected) != catalogue.N or len(set(selected)) != catalogue.N:
        raise ValueError("selector must contain exactly N distinct choices")
    used_lower = [catalogue.choices[index].lower for index in selected]
    if len(set(used_lower)) != len(catalogue.low):
        raise ValueError("selector is not a perfect lower-q1 rainbow")
    cycles = catalogue.physical_cycles(selected)
    residence = []
    for component, cycle in enumerate(cycles):
        residence.extend(
            (component, coordinate, start, length)
            for coordinate, start, length in catalogue.residence_violations(cycle)
        )
    lower_q2 = catalogue.factor_lower_missing(cycles, 2)
    lower_q3 = (
        catalogue.factor_lower_missing(cycles, 3) if catalogue.d >= 3 else []
    )
    upper = catalogue.factor_upper_missing(cycles)
    report = {
        "physical_cycle_count": len(cycles),
        "physical_cycle_lengths": list(map(len, cycles)),
        "residence_violations": residence,
        "lower_q2_missing": lower_q2,
        "lower_q3_positive_degree_missing": lower_q3,
        "upper_missing": upper,
        "carrier_pass": not residence and not lower_q2 and not lower_q3 and not upper,
        "connectivity_pending": len(cycles) != 1,
    }
    return cycles, report


def serialize_carrier(
    catalogue: QuotientCatalogue,
    selected: list[int],
    report: dict[str, object],
) -> dict[str, object]:
    return {
        "schema": SCHEMA,
        "k": catalogue.k,
        "r": catalogue.r,
        "d": catalogue.d,
        "W": catalogue.W,
        "N": catalogue.N,
        "choice_table_sha256": catalogue.choice_table_sha256,
        "choice_ids": selected,
        "choices": catalogue.explicit_selection(selected),
        **report,
    }


def load_carrier(path: Path) -> tuple[QuotientCatalogue, list[int], dict[str, object]]:
    data = json.loads(path.read_text())
    catalogue = QuotientCatalogue(int(data["k"]))
    selected = catalogue.ids_from_explicit(data["choices"])
    if "choice_table_sha256" in data:
        expected = data["choice_table_sha256"]
        if expected != catalogue.choice_table_sha256:
            raise ValueError("stable choice table digest mismatch")
    if "choice_ids" in data and list(map(int, data["choice_ids"])) != selected:
        raise ValueError("serialized IDs disagree with explicit choices")
    cycle, report = validate_carrier(catalogue, selected)
    report["cycle"] = cycle
    return catalogue, selected, report


def load_cp_sat_hint(
    catalogue: QuotientCatalogue, path: Path | None
) -> tuple[list[int] | None, list[int] | None]:
    """Load stable explicit choice hints and, when possible, arc directions."""
    if path is None:
        return None, None
    data = json.loads(path.read_text())
    if "choices" not in data:
        raise ValueError("hint requires explicit choices; bare foreign IDs are unsafe")
    selected = catalogue.ids_from_explicit(data["choices"])
    if len(selected) != catalogue.N or len(set(selected)) != catalogue.N:
        raise ValueError("hint must select exactly one central lower-orbit choice")
    if len({catalogue.choices[index].lower for index in selected}) != catalogue.N:
        raise ValueError("hint does not select every lower central orbit exactly once")

    cycle = data.get("physical_cycle", data.get("cycle"))
    if cycle is None:
        try:
            cycle = catalogue.physical_cycle(selected)
        except ValueError:
            # A disconnected or non-degree-two selection is still useful as
            # a choice-level hint, but has no coherent arc orientation.
            return selected, None
    cycle = list(map(int, cycle))
    if len(cycle) != catalogue.W or len(set(cycle)) != catalogue.W:
        raise ValueError("hint cycle is not a central Hamilton cycle")
    arcs_by_choice = {}
    for i, u in enumerate(cycle):
        v = cycle[(i + 1) % catalogue.W]
        arc = catalogue.directed_arc(u, v)
        choice = catalogue.arc_data[arc][0]
        old = arcs_by_choice.setdefault(choice, arc)
        if old != arc:
            raise ValueError("physical hint orientation is not quotient-equivariant")
    if set(arcs_by_choice) != set(selected):
        raise ValueError("hint cycle and explicit selector disagree")
    return selected, sorted(arcs_by_choice.values())


def compile_carrier(
    carrier_path: Path,
    output_word: Path,
    output_audit: Path,
    core_trials: int,
    seed: int,
) -> dict[str, object]:
    catalogue, selected, carrier_report = load_carrier(carrier_path)
    cycle = carrier_report.pop("cycle")
    if not carrier_report["carrier_pass"]:
        raise ValueError("carrier fails residence, lower-q2, or upper coverage")
    envelope = maximal_erosion(cycle, catalogue.k, catalogue.d)
    rows = [envelope]
    for _ in range(catalogue.d):
        rows.append(derivative(rows[-1]))
    if rows[-1] != cycle:
        raise AssertionError("maximal erosion does not differentiate to carrier")
    expected_ranks = [catalogue.h + j for j in range(catalogue.d + 1)]
    for row, rank in zip(rows, expected_ranks):
        if any(value.bit_count() != rank for value in row):
            raise AssertionError(f"graded row is not uniformly rank {rank}")
    if len(set(rows[1])) != comb(catalogue.k, catalogue.h + 1):
        raise AssertionError("DP does not cover rank h+1 (the lower-q2 gate)")
    if len(set(rows[-2])) != comb(catalogue.k, catalogue.r - 1):
        raise AssertionError("top lower row is not a perfect rainbow")

    voltage = int(carrier_report["voltage"])
    targets = target_list(catalogue.k, catalogue.h)
    envelope_values = set(envelope)
    missing_top_literals = [
        mask_from_combination(items)
        for items in combinations(range(catalogue.k), catalogue.h)
        if mask_from_combination(items) not in envelope_values
    ]
    if missing_top_literals:
        # This is not an eager carrier gate.  It is the exact positive-degree
        # test for the rank-h vertices of the literal Hall graph: since both
        # S and P_i have rank h, S <= P_i iff S=P_i.  No choice of one-core can
        # repair a missing envelope value.
        missing_orbits = sorted(
            {catalogue.canonical(target) for target in missing_top_literals}
        )
        report = {
            "status": "NO_CORE_POSITIVE_DEGREE",
            "carrier": str(carrier_path),
            "k": catalogue.k,
            "rank_h": catalogue.h,
            "missing_rank_h_targets": len(missing_top_literals),
            "missing_rank_h_orbits": missing_orbits,
            "missing_rank_h_orbit_count": len(missing_orbits),
        }
        output_audit.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
        return report
    rng = random.Random(seed)
    best: dict[str, object] | None = None
    winner = None
    for trial in range(max(1, core_trials)):
        core = make_equivariant_core(
            catalogue,
            envelope,
            voltage,
            rng,
            randomized=trial > 0,
        )
        adjacency = hall_adjacency(envelope, core, targets)
        zero_degree = sum(not neighbours for neighbours in adjacency)
        flow, demand, quotient_report = weighted_quotient_hall(
            catalogue, targets, adjacency
        )
        score = (flow, -zero_degree, -sum(value.bit_count() for value in core))
        if best is None or score > best["score"]:
            best = {
                "score": score,
                "trial": trial,
                "core": core,
                "adjacency": adjacency,
                "quotient": quotient_report,
                "zero_degree": zero_degree,
            }
        if flow == demand:
            matching = maximum_matching(adjacency, catalogue.W)
            matched = sum(position >= 0 for position in matching)
            if matched != demand:
                raise AssertionError(
                    "weighted quotient Hall passed but physical matching failed"
                )
            winner = (trial, core, adjacency, matching, quotient_report)
            break
    if winner is None:
        assert best is not None
        report = {
            "status": "NO_CORE_PASS",
            "carrier": str(carrier_path),
            "k": catalogue.k,
            "trials": max(1, core_trials),
            "best_trial": best["trial"],
            "best_zero_degree": best["zero_degree"],
            "best_weighted_quotient": best["quotient"],
        }
        output_audit.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
        return report

    trial, core, adjacency, matching, quotient_report = winner
    cyclic_word = envelope[:]
    for target, position in zip(targets, matching):
        cyclic_word[position] = target
    if derivative(cyclic_word) != derivative(envelope):
        raise AssertionError("matched word does not preserve DA=DP")

    safe_cuts = catalogue.upper_safe_cuts(cycle)
    if not safe_cuts:
        report = {
            "status": "NO_UPPER_SAFE_CUT",
            "carrier": str(carrier_path),
            "k": catalogue.k,
            "winning_core_trial": trial,
            "weighted_quotient": quotient_report,
        }
        output_audit.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
        return report

    output = None
    used_cut = None
    final_missing: set[int] | None = None
    for cut in safe_cuts:
        start = (cut + 1) % catalogue.W
        candidate = [
            cyclic_word[(start + i) % catalogue.W] for i in range(catalogue.W)
        ]
        candidate.extend(candidate[: catalogue.d])
        missing = exhaustive_missing(candidate, catalogue.k)
        if not missing:
            output, used_cut, final_missing = candidate, cut, missing
            break
        if final_missing is None or len(missing) < len(final_missing):
            final_missing = missing
    if output is None:
        report = {
            "status": "DIRECT_VERIFY_FAILED",
            "carrier": str(carrier_path),
            "k": catalogue.k,
            "winning_core_trial": trial,
            "safe_cut_count": len(safe_cuts),
            "best_full_missing": len(final_missing or ()),
            "weighted_quotient": quotient_report,
        }
        output_audit.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
        return report

    payload = " ".join(map(str, output)) + "\n"
    output_word.write_text(payload)
    report = {
        "status": "VERIFIED_OPTIMAL",
        "carrier": str(carrier_path),
        "k": catalogue.k,
        "r": catalogue.r,
        "d": catalogue.d,
        "h": catalogue.h,
        "W": catalogue.W,
        "N": catalogue.N,
        "carrier_report": carrier_report,
        "graded_row_rank_histograms": [
            dict(sorted(Counter(value.bit_count() for value in row).items()))
            for row in rows
        ],
        "graded_row_distinct_counts": [len(set(row)) for row in rows],
        "core_trial": trial,
        "core_rank_histogram": dict(
            sorted(Counter(value.bit_count() for value in core).items())
        ),
        "core_incidences": sum(value.bit_count() for value in core),
        "DC_equals_DP": derivative(core) == derivative(envelope),
        "physical_targets": len(targets),
        "physical_matching": sum(position >= 0 for position in matching),
        "candidate_degree_histogram": dict(
            sorted(Counter(map(len, adjacency)).items())
        ),
        "weighted_quotient": quotient_report,
        "safe_cut_count": len(safe_cuts),
        "used_cut": used_cut,
        "output_length": len(output),
        "output_word": str(output_word),
        "output_sha256": sha256(payload.encode()).hexdigest(),
        "full_missing": 0,
    }
    output_audit.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    return report


def build_cp_sat_model(
    catalogue: QuotientCatalogue,
    lazy: list[tuple[str, object]],
    hint_choices: list[int] | None = None,
    hint_arcs: list[int] | None = None,
    max_choice_changes: int | None = None,
    allow_cycle_cover: bool = False,
    partial_arc_hint: bool = False,
):
    """Build the repo-owned strict carrier model; import OR-Tools lazily."""
    from ortools.sat.python import cp_model

    model = cp_model.CpModel()
    arc_vars = [model.NewBoolVar(f"a{index}") for index in range(len(catalogue.arc_data))]
    if allow_cycle_cover:
        outgoing: dict[int, list[object]] = defaultdict(list)
        incoming: dict[int, list[object]] = defaultdict(list)
        for index, (_, source, target, _, _, _) in enumerate(catalogue.arc_data):
            outgoing[source].append(arc_vars[index])
            incoming[target].append(arc_vars[index])
        for vertex in range(catalogue.N):
            model.AddExactlyOne(outgoing[vertex])
            model.AddExactlyOne(incoming[vertex])
    else:
        model.AddCircuit(
            [
                (source, target, arc_vars[index])
                for index, (_, source, target, _, _, _) in enumerate(catalogue.arc_data)
            ]
        )
    choice_vars = [model.NewBoolVar(f"c{index}") for index in range(len(catalogue.choices))]
    for ci, arcs in enumerate(catalogue.arcs_by_choice):
        model.AddMaxEquality(choice_vars[ci], [arc_vars[index] for index in arcs])
        model.AddAtMostOne([arc_vars[index] for index in arcs])
    for lower, ids in catalogue.choices_by_lower.items():
        model.AddExactlyOne([choice_vars[index] for index in ids])

    if not allow_cycle_cover:
        total = model.NewIntVar(
            0, catalogue.k * len(catalogue.arc_data), "total_voltage"
        )
        model.Add(
            total
            == sum(
                catalogue.arc_data[index][3] * arc_vars[index]
                for index in range(len(catalogue.arc_data))
            )
        )
        voltage = model.NewIntVar(0, catalogue.k - 1, "voltage")
        model.AddModuloEquality(voltage, total, catalogue.k)
        model.AddAllowedAssignments(
            [voltage],
            [
                (value,)
                for value in range(catalogue.k)
                if gcd(value, catalogue.k) == 1
            ],
        )

    # Exact age automaton for minimum positive run d+1.
    ages = {}
    for mi, representative in enumerate(catalogue.mid):
        for coordinate in range(catalogue.k):
            if representative & (1 << coordinate):
                for age in range(1, catalogue.d + 1):
                    ages[(mi, coordinate, age)] = model.NewBoolVar(
                        f"g{mi}_{coordinate}_{age}"
                    )
    for arc_index, (_, source_i, target_i, shift, deleted, inserted) in enumerate(
        catalogue.arc_data
    ):
        arc = arc_vars[arc_index]
        model.AddImplication(arc, ages[(target_i, inserted, 1)])
        shared = catalogue.mid[source_i] & ~(1 << deleted)
        for coordinate in range(catalogue.k):
            if not (shared & (1 << coordinate)):
                continue
            target_coordinate = (coordinate - shift) % catalogue.k
            for age in range(1, catalogue.d):
                model.AddBoolOr(
                    [
                        arc.Not(),
                        ages[(source_i, coordinate, age)].Not(),
                        ages[(target_i, target_coordinate, age + 1)],
                    ]
                )
        for age in range(1, catalogue.d + 1):
            model.AddBoolOr([arc.Not(), ages[(source_i, deleted, age)].Not()])

    for target in catalogue.upper1:
        model.AddBoolOr(
            [choice_vars[index] for index in catalogue.upper1_cover[target]]
        )

    for constraint_index, (kind, payload) in enumerate(lazy):
        if kind == "or-of-ands":
            alternatives = []
            for group in payload:
                flag = model.NewBoolVar("")
                alternatives.append(flag)
                for choice in group:
                    model.AddImplication(flag, choice_vars[choice])
            if alternatives:
                model.AddBoolOr(alternatives)
            else:
                model.AddBoolOr([])
        elif kind == "shadow-state-path":
            mode, q, target = payload
            mode, q, target = str(mode), int(q), int(target)
            states, transitions = catalogue.shadow_state_template(mode, q, target)
            state_vars = [
                model.NewIntVar(
                    0,
                    len(states) - 1,
                    f"shs{constraint_index}_{step}",
                )
                for step in range(q + 1)
            ]
            selected_arc_vars = [
                model.NewIntVar(
                    0,
                    len(catalogue.arc_data) - 1,
                    f"she{constraint_index}_{step}",
                )
                for step in range(q)
            ]
            deleted_defect_vars = [
                model.NewIntVar(0, catalogue.k - 1, f"shd{constraint_index}_{step}")
                for step in range(q)
            ]
            for step in range(q):
                model.AddAllowedAssignments(
                    [
                        state_vars[step],
                        state_vars[step + 1],
                        selected_arc_vars[step],
                        deleted_defect_vars[step],
                    ],
                    transitions,
                )
                # The chosen physical transition must be the lift of an arc
                # selected by the quotient Hamilton circuit.
                model.AddElement(selected_arc_vars[step], arc_vars, 1)
            model.AddAllDifferent(deleted_defect_vars)
            initial_defect = []
            for state_index, state in enumerate(states):
                defect = (state & ~target) if mode == "intersection" else (target & ~state)
                for coordinate in range(catalogue.k):
                    if defect & (1 << coordinate):
                        initial_defect.append((state_index, coordinate))
            for deleted in deleted_defect_vars:
                model.AddAllowedAssignments([state_vars[0], deleted], initial_defect)
        elif kind == "upper-reachability-boundary":
            _target, boundary = payload
            model.AddBoolOr([arc_vars[int(index)] for index in boundary])
        elif kind == "nogood":
            model.AddBoolOr([choice_vars[index].Not() for index in payload])
        else:
            raise ValueError(f"unknown lazy constraint {kind}")
    if hint_choices is not None:
        chosen = set(hint_choices)
        for index, variable in enumerate(choice_vars):
            model.AddHint(variable, int(index in chosen))
        if max_choice_changes is not None:
            if not 0 <= max_choice_changes <= catalogue.N:
                raise ValueError("max choice changes must lie in [0,N]")
            # Both the hint and every feasible selector contain exactly N
            # choices, one per lower orbit.  Hence overlap >= N-R is exactly
            # Hamming distance (changed lower-orbit choices) <= R.
            model.Add(
                sum(choice_vars[index] for index in chosen)
                >= catalogue.N - max_choice_changes
            )
    elif max_choice_changes is not None:
        raise ValueError("a Hamming-radius constraint requires --hint")
    if hint_arcs is not None:
        chosen_arcs = set(hint_arcs)
        if partial_arc_hint:
            for index in sorted(chosen_arcs):
                model.AddHint(arc_vars[index], 1)
        else:
            for index, variable in enumerate(arc_vars):
                model.AddHint(variable, int(index in chosen_arcs))
    return model, arc_vars, choice_vars


def search_carrier(
    k: int,
    workers: int,
    timeout: float,
    max_rounds: int,
    seed: int,
    output: Path,
    hint: Path | None,
    max_choice_changes: int | None,
    seed_shadow_cuts: bool,
    shadow_seed: Path | None,
    allow_cycle_cover: bool,
    arc_hint: Path | None,
    base_only: bool,
) -> dict[str, object]:
    from ortools.sat.python import cp_model

    catalogue = QuotientCatalogue(k)
    hint_choices, hint_arcs = load_cp_sat_hint(catalogue, hint)
    # Keep the coherent orientation supplied by --hint separate from a
    # possibly partial --arc-hint used only for branching guidance.  Exact
    # seeded reachability cuts require a complete selected-arc set.
    shadow_hint_arcs = hint_arcs
    partial_arc_hint = False
    if arc_hint is not None:
        _arc_choices, external_arcs = load_cp_sat_hint(catalogue, arc_hint)
        if external_arcs is None:
            raise ValueError("--arc-hint must encode a valid quotient cycle")
        if hint_choices is not None:
            selected_hint = set(hint_choices)
            external_arcs = [
                arc
                for arc in external_arcs
                if catalogue.arc_data[arc][0] in selected_hint
            ]
        hint_arcs = external_arcs
        partial_arc_hint = True
    lazy: list[tuple[str, object]] = []
    shadow_keys: set[tuple[str, int, int]] = set()
    upper_boundary_keys: set[tuple[int, tuple[int, ...]]] = set()

    def add_shadow(mode: str, depth: int, target: int) -> bool:
        key = (mode, int(depth), int(target))
        if key in shadow_keys:
            return False
        shadow_keys.add(key)
        lazy.append(("shadow-state-path", key))
        return True

    def add_upper_boundary(target: int, selected_arcs: Iterable[int]) -> bool:
        covered, boundary = catalogue.upper_reachability_boundary(
            int(target), selected_arcs
        )
        if covered:
            raise AssertionError(
                f"upper target {target} is audit-missing but automaton-reachable"
            )
        key = (int(target), tuple(boundary))
        if key in upper_boundary_keys:
            return False
        upper_boundary_keys.add(key)
        lazy.append(("upper-reachability-boundary", key))
        return True

    if seed_shadow_cuts or shadow_seed is not None:
        shadow_choices = hint_choices
        shadow_arcs = shadow_hint_arcs
        if shadow_seed is not None:
            shadow_choices, shadow_arcs = load_cp_sat_hint(catalogue, shadow_seed)
            if shadow_arcs is None:
                raise ValueError("--shadow-seed must encode a valid quotient cycle")
        if shadow_choices is None or shadow_arcs is None:
            raise ValueError("seeded shadow cuts require a valid cycle hint")
        try:
            _hint_cycle, hint_report = validate_carrier(catalogue, shadow_choices)
        except ValueError as error:
            raise ValueError(
                "--seed-shadow-cuts requires a degree-two Hamilton cycle hint"
            ) from error
        for target in hint_report["lower_q2_missing"]:
            add_shadow("intersection", 2, int(target))
        for target in hint_report["lower_q3_positive_degree_missing"]:
            add_shadow("intersection", 3, int(target))
        for target in hint_report["upper_missing"]:
            depth = int(target).bit_count() - catalogue.r
            if depth == 2:
                add_shadow("union", depth, int(target))
            elif depth >= 3:
                add_upper_boundary(int(target), shadow_arcs)
        print(
            "seeded "
            f"{len(shadow_keys) + len(upper_boundary_keys)} exact shadow "
            "constraints from hint",
            flush=True,
        )
    started = time.time()
    for round_index in range(max_rounds):
        model, arc_vars, choice_vars = build_cp_sat_model(
            catalogue,
            lazy,
            hint_choices,
            hint_arcs,
            max_choice_changes,
            allow_cycle_cover,
            partial_arc_hint,
        )
        solver = cp_model.CpSolver()
        solver.parameters.num_search_workers = workers
        solver.parameters.max_time_in_seconds = timeout
        solver.parameters.random_seed = seed + round_index
        status = solver.Solve(model)
        status_name = solver.StatusName(status)
        if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
            report = {
                "schema": SCHEMA,
                "k": k,
                "status": status_name,
                "round": round_index,
                "lazy_constraints": len(lazy),
                "elapsed": time.time() - started,
                "hint": str(hint) if hint else None,
                "max_choice_changes": max_choice_changes,
                "seed_shadow_cuts": seed_shadow_cuts,
                "shadow_seed": str(shadow_seed) if shadow_seed else None,
                "allow_cycle_cover": allow_cycle_cover,
                "arc_hint": str(arc_hint) if arc_hint else None,
                "base_only": base_only,
            }
            output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
            print(json.dumps(report, sort_keys=True), flush=True)
            return report
        selected = [
            index for index, variable in enumerate(choice_vars) if solver.Value(variable)
        ]
        selected_arcs = [
            index for index, variable in enumerate(arc_vars) if solver.Value(variable)
        ]
        try:
            if allow_cycle_cover:
                cycles, report = validate_cycle_cover(catalogue, selected)
                cycle = cycles[0] if len(cycles) == 1 else []
            else:
                cycle, report = validate_carrier(catalogue, selected)
        except ValueError as error:
            lazy.append(("nogood", selected))
            print(f"round={round_index} invalid={error}; +nogood", flush=True)
            continue
        print(
            f"round={round_index} residence={len(report['residence_violations'])} "
            f"lower_q2={len(report['lower_q2_missing'])} "
            f"lower_q3_positive={len(report['lower_q3_positive_degree_missing'])} "
            f"upper={len(report['upper_missing'])} lazy={len(lazy)}",
            flush=True,
        )
        if base_only:
            upper_q1_missing = [
                target
                for target in report["upper_missing"]
                if int(target).bit_count() == catalogue.r + 1
            ]
            if report["residence_violations"] or upper_q1_missing:
                # Both conditions are eager in the master model.  Keep this
                # independent endpoint audit as a soundness backstop.
                lazy.append(("nogood", selected))
                print(
                    "base-model audit mismatch; +nogood "
                    f"residence={len(report['residence_violations'])} "
                    f"upper_q1={len(upper_q1_missing)}",
                    flush=True,
                )
                continue
            result = serialize_carrier(catalogue, selected, report)
            result["schema"] = (
                "graded-quotient-cycle-cover-base-v1"
                if allow_cycle_cover
                else "graded-quotient-strict-base-v1"
            )
            result["status"] = "BASE_FEASIBLE"
            result["base_only"] = True
            result["round"] = round_index
            result["lazy_constraints"] = len(lazy)
            result["elapsed"] = time.time() - started
            result["hint"] = str(hint) if hint else None
            result["max_choice_changes"] = max_choice_changes
            result["allow_cycle_cover"] = allow_cycle_cover
            result["arc_hint"] = str(arc_hint) if arc_hint else None
            output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
            return result
        if report["carrier_pass"]:
            result = serialize_carrier(catalogue, selected, report)
            if allow_cycle_cover:
                result["schema"] = "graded-quotient-cycle-cover-v1"
            result["round"] = round_index
            result["lazy_constraints"] = len(lazy)
            result["elapsed"] = time.time() - started
            result["hint"] = str(hint) if hint else None
            result["max_choice_changes"] = max_choice_changes
            result["seed_shadow_cuts"] = seed_shadow_cuts
            result["shadow_seed"] = str(shadow_seed) if shadow_seed else None
            result["allow_cycle_cover"] = allow_cycle_cover
            result["arc_hint"] = str(arc_hint) if arc_hint else None
            output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
            return result
        added = 0
        for target in report["lower_q2_missing"]:
            added += int(add_shadow("intersection", 2, int(target)))
        for target in report["lower_q3_positive_degree_missing"]:
            added += int(add_shadow("intersection", 3, int(target)))
        for target in report["upper_missing"]:
            depth = int(target).bit_count() - catalogue.r
            if depth == 2:
                added += int(add_shadow("union", depth, int(target)))
            elif depth >= 3:
                added += int(add_upper_boundary(int(target), selected_arcs))
        # Deeper upper shadows currently receive a sound whole-selection
        # no-good.  This is slower than a specialized motif, but exact.
        if added == 0:
            lazy.append(("nogood", selected))
    report = {
        "schema": SCHEMA,
        "k": k,
        "status": "MAX_ROUNDS",
        "round": max_rounds,
        "lazy_constraints": len(lazy),
        "elapsed": time.time() - started,
        "hint": str(hint) if hint else None,
        "max_choice_changes": max_choice_changes,
        "seed_shadow_cuts": seed_shadow_cuts,
        "shadow_seed": str(shadow_seed) if shadow_seed else None,
        "allow_cycle_cover": allow_cycle_cover,
        "arc_hint": str(arc_hint) if arc_hint else None,
        "base_only": base_only,
    }
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    return report


def verify_word(path: Path, k: int) -> dict[str, object]:
    word = [int(token) for token in path.read_text().split()]
    missing = exhaustive_missing(word, k)
    report = {
        "word": str(path),
        "k": k,
        "length": len(word),
        "nonempty_letters": all(word),
        "in_range_letters": all(0 < value < (1 << k) for value in word),
        "missing_count": len(missing),
        "missing": sorted(missing),
        "sha256": sha256(path.read_bytes()).hexdigest(),
        "status": "PASS" if not missing and all(word) else "FAIL",
    }
    return report


def command_fixture(args: argparse.Namespace) -> None:
    catalogue = QuotientCatalogue(args.k)
    raw = json.loads(args.input.read_text())
    if "choices" in raw:
        selected = catalogue.ids_from_explicit(raw["choices"])
    else:
        raise ValueError("fixture import requires explicit choices, never bare foreign IDs")
    _, report = validate_carrier(catalogue, selected)
    result = serialize_carrier(catalogue, selected, report)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, indent=2, sort_keys=True))


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)

    search = sub.add_parser("search-carrier")
    search.add_argument("--k", type=int, required=True)
    search.add_argument("--workers", type=int, default=8)
    search.add_argument("--timeout", type=float, default=3600)
    search.add_argument("--max-rounds", type=int, default=500)
    search.add_argument("--seed", type=int, default=0)
    search.add_argument("--output", type=Path, required=True)
    search.add_argument(
        "--hint",
        type=Path,
        help="explicit stable carrier JSON; choices are hinted and a valid cycle also hints arcs",
    )
    search.add_argument(
        "--max-choice-changes",
        type=int,
        help="exact LNS radius: require overlap with hint >= N-radius",
    )
    search.add_argument(
        "--seed-shadow-cuts",
        action="store_true",
        help="eagerly add compact q2/q3 cuts for shadows missing from the cycle hint",
    )
    search.add_argument(
        "--shadow-seed",
        type=Path,
        help="valid cycle used only to seed compact q2/q3 shadow constraints",
    )
    search.add_argument(
        "--allow-cycle-cover",
        action="store_true",
        help="allow several quotient/physical cycles; splice connectivity later",
    )
    search.add_argument(
        "--arc-hint",
        type=Path,
        help="valid cycle supplying positive partial arc-orientation hints",
    )
    search.add_argument(
        "--base-only",
        action="store_true",
        help="stop after degree/connectivity, residence, and both q1 rainbows",
    )

    compile_parser = sub.add_parser("compile")
    compile_parser.add_argument("carrier", type=Path)
    compile_parser.add_argument("--word", type=Path, required=True)
    compile_parser.add_argument("--audit", type=Path, required=True)
    compile_parser.add_argument("--core-trials", type=int, default=1000)
    compile_parser.add_argument("--seed", type=int, default=0)

    verify = sub.add_parser("verify")
    verify.add_argument("word", type=Path)
    verify.add_argument("--k", type=int, required=True)

    fixture = sub.add_parser("import-fixture")
    fixture.add_argument("input", type=Path)
    fixture.add_argument("--k", type=int, required=True)
    fixture.add_argument("--output", type=Path, required=True)

    args = parser.parse_args()
    if args.command == "search-carrier":
        result = search_carrier(
            args.k,
            args.workers,
            args.timeout,
            args.max_rounds,
            args.seed,
            args.output,
            args.hint,
            args.max_choice_changes,
            args.seed_shadow_cuts,
            args.shadow_seed,
            args.allow_cycle_cover,
            args.arc_hint,
            args.base_only,
        )
    elif args.command == "compile":
        result = compile_carrier(
            args.carrier,
            args.word,
            args.audit,
            args.core_trials,
            args.seed,
        )
    elif args.command == "verify":
        result = verify_word(args.word, args.k)
    elif args.command == "import-fixture":
        # command_fixture performs its own stable serialization and print.
        command_fixture(args)
        return
    else:
        raise AssertionError(args.command)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
