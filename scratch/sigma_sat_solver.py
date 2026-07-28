#!/usr/bin/env python3
"""Exact SAT solver for the depth-one sigma formulation.

The primary mode quotients by translations of Z_k (for prime k).  A Boolean
variable chooses one of C(r,2) upper extensions for every orbit of
(r-1)-sets.  The CNF enforces

  * exactly one extension per lower orbit;
  * middle degree at most two (hence exactly two by total degree);
  * upper coverage, optionally upper load at most two;
  * optionally, coverage of every depth-two upper orbit.

Connectedness is imposed by lazy subtour cuts.  A connected quotient cycle
is accepted only when its voltage is non-zero, so its lift is one Hamilton
cycle rather than k disjoint cycles.  Short-residence violations can also be
cut lazily.

The non-equivariant mode uses the same encoding without quotienting and is
useful for validating small composite k.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import os
import subprocess
import sys
import time
from collections import Counter
from dataclasses import dataclass
from pathlib import Path


def masks_of_size(n: int, size: int):
    for comb in itertools.combinations(range(n), size):
        mask = 0
        for x in comb:
            mask |= 1 << x
        yield mask


def rotate(mask: int, shift: int, n: int) -> int:
    shift %= n
    if not shift:
        return mask
    full = (1 << n) - 1
    return ((mask << shift) | (mask >> (n - shift))) & full


def canonical(mask: int, n: int, equivariant: bool) -> tuple[int, int]:
    """Return (canonical representative, s) with rot(mask,s)=representative."""
    if not equivariant:
        return mask, 0
    best = mask
    best_s = 0
    for s in range(1, n):
        candidate = rotate(mask, s, n)
        if candidate < best:
            best = candidate
            best_s = s
    return best, best_s


def orbit_representatives(n: int, size: int, equivariant: bool) -> list[int]:
    if not equivariant:
        return list(masks_of_size(n, size))
    return sorted({canonical(mask, n, True)[0] for mask in masks_of_size(n, size)})


class CNF:
    def __init__(self):
        self.nvars = 0
        self.clauses: list[list[int]] = []

    def var(self) -> int:
        self.nvars += 1
        return self.nvars

    def add(self, *lits: int):
        clause = [int(x) for x in lits]
        if not clause:
            raise ValueError("empty clause")
        self.clauses.append(clause)

    def at_most_k(self, lits: list[int], k: int):
        """Compact forward sequential counter; equisatisfiable at-most-k."""
        # Repeated literals are intentional for weighted degree constraints.
        n = len(lits)
        if n <= k:
            return
        if k == 0:
            for x in lits:
                self.add(-x)
            return
        threshold = k + 1
        state: dict[tuple[int, int], int] = {}
        for i in range(1, n + 1):
            for j in range(1, min(i, threshold) + 1):
                state[i, j] = self.var()
            x = lits[i - 1]
            self.add(-x, state[i, 1])
            if i > 1:
                self.add(-state[i - 1, 1], state[i, 1])
            for j in range(2, min(i, threshold) + 1):
                if (i - 1, j) in state:
                    self.add(-state[i - 1, j], state[i, j])
                if (i - 1, j - 1) in state:
                    self.add(-x, -state[i - 1, j - 1], state[i, j])
        self.add(-state[n, threshold])

    def exactly_one(self, lits: list[int]):
        self.add(*lits)
        # Pairwise clauses are stronger and small in the intended instances.
        for i, x in enumerate(lits):
            for y in lits[i + 1 :]:
                self.add(-x, -y)

    def write(self, path: Path):
        with path.open("w", encoding="ascii") as out:
            out.write(f"p cnf {self.nvars} {len(self.clauses)}\n")
            for clause in self.clauses:
                out.write(" ".join(map(str, clause)))
                out.write(" 0\n")


@dataclass(frozen=True)
class Incidence:
    choice: int
    side: int
    aligned_upper: int
    aligned_lower: int


@dataclass
class Choice:
    var: int
    lower_idx: int
    lower: int
    add_a: int
    add_b: int
    upper_idx: int
    upper: int
    endpoint: tuple[int, int]
    endpoint_phase: tuple[int, int]
    voltage: int


class SigmaInstance:
    def __init__(
        self,
        k: int,
        equivariant: bool,
        cap2: bool,
        q2: bool,
        cover_upper: bool = True,
        upper_q1_masks: tuple[int, ...] = (),
        upper_q2_masks: tuple[int, ...] = (),
        upper_q1_hole_budget: int | None = None,
        upper_q2_hole_budget: int | None = None,
        lower_q2: bool = False,
        lower_q2_masks: tuple[int, ...] = (),
        lower_q3: bool = False,
        direct_residence: int = 0,
        automaton_residence: int = 0,
        residence_budget: int | None = None,
        automaton_lower_q3: bool = False,
        automaton_coresidence: int = 0,
        automaton_upper_q3: bool = False,
        automaton_compiler_depth: int = 0,
        compiler_target_ranks: tuple[int, ...] = (),
        compiler_target_masks: tuple[int, ...] = (),
        compiler_pointwise_d2: bool = False,
        compiler_d2_budget: int | None = None,
        direct_connectivity: bool = False,
        compact_connectivity: bool = False,
        oriented_lazy_connectivity: bool = False,
    ):
        if k % 2 != 1 or k < 5:
            raise ValueError("k must be odd and at least 5")
        if equivariant and not self._is_prime(k):
            raise ValueError("translation quotient currently requires prime k")
        self.k = k
        self.r = (k + 1) // 2
        self.equivariant = equivariant
        self.cap2 = cap2
        self.cover_upper = cover_upper
        self.upper_q1_hole_budget = upper_q1_hole_budget
        self.upper_q2_hole_budget = upper_q2_hole_budget
        self.upper_q1_masks = tuple(
            sorted({canonical(mask, k, equivariant)[0] for mask in upper_q1_masks})
        )
        self.q2 = q2
        self.lower_q2 = lower_q2
        self.lower_q3 = lower_q3
        self.group_order = k if equivariant else 1
        self.cnf = CNF()

        self.lower = orbit_representatives(k, self.r - 1, equivariant)
        self.middle = orbit_representatives(k, self.r, equivariant)
        self.upper = orbit_representatives(k, self.r + 1, equivariant)
        if upper_q2_masks:
            requested_upper2 = []
            for mask in upper_q2_masks:
                if mask.bit_count() != self.r + 2:
                    raise ValueError(
                        f"forced upper-q2 mask {mask} has rank {mask.bit_count()}, "
                        f"expected {self.r + 2}"
                    )
                requested_upper2.append(canonical(mask, k, equivariant)[0])
            self.upper2 = sorted(set(requested_upper2))
        else:
            self.upper2 = orbit_representatives(k, self.r + 2, equivariant) if q2 else []
        self.lower2 = (
            orbit_representatives(k, self.r - 2, equivariant) if lower_q2 else []
        )
        if lower_q2_masks and not lower_q2:
            requested = []
            for mask in lower_q2_masks:
                if mask.bit_count() != self.r - 2:
                    raise ValueError(
                        f"forced lower-q2 mask {mask} has rank {mask.bit_count()}, "
                        f"expected {self.r - 2}"
                    )
                requested.append(canonical(mask, k, equivariant)[0])
            self.lower2 = sorted(set(requested))
        self.lower3 = (
            orbit_representatives(k, self.r - 3, equivariant)
            if lower_q3 or automaton_lower_q3
            else []
        )
        self.upper3 = (
            orbit_representatives(k, self.r + 3, equivariant)
            if automaton_upper_q3
            else []
        )
        self.mid_index = {mask: i for i, mask in enumerate(self.middle)}
        self.upper_index = {mask: i for i, mask in enumerate(self.upper)}
        self.upper2_index = {mask: i for i, mask in enumerate(self.upper2)}
        self.lower2_index = {mask: i for i, mask in enumerate(self.lower2)}
        self.lower3_index = {mask: i for i, mask in enumerate(self.lower3)}
        self.upper3_index = {mask: i for i, mask in enumerate(self.upper3)}
        self.upper_q2_witnesses: list[list[int]] = []
        self.lower_q2_witnesses: list[list[int]] = []

        self.choices: list[Choice] = []
        self.choice_by_var: dict[int, Choice] = {}
        self.by_lower: list[list[int]] = [[] for _ in self.lower]
        self.by_middle: list[list[Incidence]] = [[] for _ in self.middle]
        self.by_upper: list[list[int]] = [[] for _ in self.upper]
        self.cross_cache: dict[tuple[int, ...], list[int]] = {}
        self.and_cache: dict[tuple[int, ...], int] = {}
        self.base_clause_count = 0
        self._build_choices()
        self._build_core_cnf()
        if q2 or upper_q2_masks or lower_q2 or lower_q2_masks:
            self._build_q2_cnf(
                upper=q2 or bool(upper_q2_masks),
                lower=lower_q2 or bool(lower_q2_masks),
            )
        if lower_q3:
            self._build_lower_q3_cnf()
        self.residence_clause_counts: dict[int, int] = {}
        if direct_residence:
            self._build_residence_cnf(direct_residence)
        self.direct_connectivity = direct_connectivity
        self.compact_connectivity = compact_connectivity
        self.oriented_lazy_connectivity = oriented_lazy_connectivity
        self.directed_arcs: list[tuple[int, int, int, int]] = []
        if direct_connectivity:
            self._build_hamilton_cnf()
        elif compact_connectivity:
            self._build_compact_hamilton_cnf()
        elif oriented_lazy_connectivity:
            self._build_oriented_lazy_cnf()
        if automaton_residence:
            if not (compact_connectivity or oriented_lazy_connectivity):
                raise ValueError("automaton residence requires directed connectivity mode")
            self._build_residence_automaton_cnf(
                automaton_residence, residence_budget
            )
        if automaton_lower_q3:
            if automaton_residence < 3:
                raise ValueError("automaton lower q3 requires automaton residence depth >= 3")
            self._build_automaton_lower_q3_cnf()
        if automaton_coresidence or automaton_upper_q3:
            co_depth = max(automaton_coresidence, 3 if automaton_upper_q3 else 0)
            self._build_coresidence_automaton_cnf(
                co_depth, automaton_coresidence
            )
        if automaton_upper_q3:
            self._build_automaton_upper_q3_cnf()
        if automaton_compiler_depth:
            self._build_compiler_automaton_cnf(
                automaton_compiler_depth,
                compiler_target_ranks,
                compiler_target_masks,
                compiler_pointwise_d2,
                compiler_d2_budget,
                lower_q2,
            )
        self.base_clause_count = len(self.cnf.clauses)

    @staticmethod
    def _is_prime(n: int) -> bool:
        return n >= 2 and all(n % d for d in range(2, int(math.sqrt(n)) + 1))

    def _build_choices(self):
        full = (1 << self.k) - 1
        for li, lower in enumerate(self.lower):
            outside = [x for x in range(self.k) if not (lower >> x) & 1]
            for a, b in itertools.combinations(outside, 2):
                upper = lower | (1 << a) | (1 << b)
                urep, _ = canonical(upper, self.k, self.equivariant)
                ui = self.upper_index[urep]

                actual_endpoints = (lower | (1 << a), lower | (1 << b))
                ep_idx = []
                ep_phase = []
                aligned_upper = []
                aligned_lower = []
                for endpoint in actual_endpoints:
                    rep, shift_to_rep = canonical(endpoint, self.k, self.equivariant)
                    ep_idx.append(self.mid_index[rep])
                    # actual endpoint = rotate(rep, phase).
                    phase = (-shift_to_rep) % self.k if self.equivariant else 0
                    ep_phase.append(phase)
                    aligned_upper.append(rotate(upper, -phase, self.k))
                    aligned_lower.append(rotate(lower, -phase, self.k))

                var = self.cnf.var()
                choice = Choice(
                    var=var,
                    lower_idx=li,
                    lower=lower,
                    add_a=a,
                    add_b=b,
                    upper_idx=ui,
                    upper=upper,
                    endpoint=(ep_idx[0], ep_idx[1]),
                    endpoint_phase=(ep_phase[0], ep_phase[1]),
                    voltage=(ep_phase[1] - ep_phase[0]) % self.k if self.equivariant else 0,
                )
                ci = len(self.choices)
                self.choices.append(choice)
                self.choice_by_var[var] = choice
                self.by_lower[li].append(var)
                self.by_upper[ui].append(var)
                self.by_middle[ep_idx[0]].append(
                    Incidence(ci, 0, aligned_upper[0], aligned_lower[0])
                )
                self.by_middle[ep_idx[1]].append(
                    Incidence(ci, 1, aligned_upper[1], aligned_lower[1])
                )

        expected = math.comb(self.r, 2)
        if any(len(vs) != expected for vs in self.by_lower):
            raise AssertionError("wrong number of choices at a lower orbit")

    def _build_core_cnf(self):
        for vars_ in self.by_lower:
            self.cnf.exactly_one(vars_)

        # Every selected quotient edge contributes one incidence at each end;
        # a loop appears twice.  There are |V| selected edges and |V| middle
        # vertices, so at-most-two everywhere forces degree exactly two.
        for incidences in self.by_middle:
            self.cnf.at_most_k([self.choices[inc.choice].var for inc in incidences], 2)

        self.upper_q1_hole_vars = []
        if self.upper_q1_hole_budget is not None:
            if self.upper_q1_hole_budget < 0 or self.upper_q1_hole_budget > len(self.upper):
                raise ValueError("upper-q1 hole budget is out of range")
            self.upper_q1_hole_vars = [self.cnf.var() for _ in self.upper]
            for vars_, hole in zip(self.by_upper, self.upper_q1_hole_vars):
                self.cnf.add(*vars_, hole)
                if self.cap2:
                    self.cnf.at_most_k(vars_, 2)
            self.cnf.at_most_k(
                self.upper_q1_hole_vars, self.upper_q1_hole_budget
            )
        elif self.cover_upper:
            for vars_ in self.by_upper:
                self.cnf.add(*vars_)
                if self.cap2:
                    self.cnf.at_most_k(vars_, 2)
        elif self.upper_q1_masks:
            for mask in self.upper_q1_masks:
                if mask not in self.upper_index:
                    raise ValueError(f"upper-q1 target {mask} is not a rank-{self.r + 1} orbit")
                vars_ = self.by_upper[self.upper_index[mask]]
                self.cnf.add(*vars_)

        # A loop is already a whole component in a 2-regular quotient graph.
        # Since all intended instances have more than one quotient vertex,
        # connectedness forbids it.  Adding the unit clauses up front removes
        # a large family of useless subtours.
        if len(self.middle) > 1:
            for choice in self.choices:
                if choice.endpoint[0] == choice.endpoint[1]:
                    self.cnf.add(-choice.var)

    def _and_literal(self, variables: tuple[int, ...]) -> int:
        uniq = tuple(sorted(set(variables)))
        if len(uniq) == 1:
            return uniq[0]
        if uniq in self.and_cache:
            return self.and_cache[uniq]
        y = self.cnf.var()
        for x in uniq:
            self.cnf.add(-y, x)
        self.cnf.add(*[-x for x in uniq], y)
        self.and_cache[uniq] = y
        return y

    def _build_q2_cnf(self, upper: bool, lower: bool):
        upper_witnesses: list[list[int]] = [[] for _ in self.upper2]
        upper_seen: list[set[tuple[int, ...]]] = [set() for _ in self.upper2]
        lower_witnesses: list[list[int]] = [[] for _ in self.lower2]
        lower_seen: list[set[tuple[int, ...]]] = [set() for _ in self.lower2]
        for incidences in self.by_middle:
            for ia in range(len(incidences)):
                for ib in range(ia + 1, len(incidences)):
                    a = incidences[ia]
                    b = incidences[ib]
                    key = tuple(sorted({self.choices[a.choice].var, self.choices[b.choice].var}))
                    if upper:
                        union = a.aligned_upper | b.aligned_upper
                        if union.bit_count() == self.r + 2:
                            rep, _ = canonical(union, self.k, self.equivariant)
                            if rep not in self.upper2_index:
                                continue
                            target = self.upper2_index[rep]
                            if key not in upper_seen[target]:
                                upper_seen[target].add(key)
                                upper_witnesses[target].append(self._and_literal(key))
                    if lower:
                        intersection = a.aligned_lower & b.aligned_lower
                        if intersection.bit_count() == self.r - 2:
                            rep, _ = canonical(intersection, self.k, self.equivariant)
                            if rep not in self.lower2_index:
                                continue
                            target = self.lower2_index[rep]
                            if key not in lower_seen[target]:
                                lower_seen[target].add(key)
                                lower_witnesses[target].append(self._and_literal(key))
        self.upper_q2_hole_vars = []
        if upper and self.upper_q2_hole_budget is not None:
            if self.upper_q2_hole_budget < 0 or self.upper_q2_hole_budget > len(upper_witnesses):
                raise ValueError("upper-q2 hole budget is out of range")
            self.upper_q2_hole_vars = [self.cnf.var() for _ in upper_witnesses]
        for kind, witnesses in (("upper", upper_witnesses), ("lower", lower_witnesses)):
            for target, lits in enumerate(witnesses):
                if not lits:
                    raise RuntimeError(f"depth-two {kind} target {target} has no witness")
                if kind == "upper" and self.upper_q2_hole_vars:
                    self.cnf.add(*lits, self.upper_q2_hole_vars[target])
                else:
                    self.cnf.add(*lits)
        if self.upper_q2_hole_vars:
            self.cnf.at_most_k(
                self.upper_q2_hole_vars, self.upper_q2_hole_budget
            )
        self.upper_q2_witnesses = upper_witnesses
        self.lower_q2_witnesses = lower_witnesses

    def _build_lower_q3_cnf(self):
        """Require every rank-(r-3) orbit in a four-middle-set intersection."""
        witnesses: list[list[int]] = [[] for _ in self.lower3]
        seen: list[set[tuple[int, ...]]] = [set() for _ in self.lower3]

        # Oriented incidences carry the lower colour aligned to the current
        # canonical middle representative.
        arcs: list[list[tuple[int, int, int, int, int]]] = [
            [] for _ in self.middle
        ]
        for vertex, incidences in enumerate(self.by_middle):
            for inc in incidences:
                choice = self.choices[inc.choice]
                other = choice.endpoint[1 - inc.side]
                delta = (
                    choice.voltage
                    if inc.side == 0
                    else (-choice.voltage) % self.k
                )
                arcs[vertex].append(
                    (inc.choice, other, delta, choice.lower_idx, inc.aligned_lower)
                )

        for start in range(len(self.middle)):
            for ci, v1, d1, l1, low1 in arcs[start]:
                phase1 = d1 % self.k if self.equivariant else 0
                for cj, v2, d2, l2, low2_local in arcs[v1]:
                    if cj == ci or l2 == l1:
                        continue
                    phase2 = (phase1 + d2) % self.k if self.equivariant else 0
                    low2 = rotate(low2_local, phase1, self.k)
                    partial = low1 & low2
                    # A valid q3 intersection can lose only one further point.
                    if partial.bit_count() < self.r - 3:
                        continue
                    for ck, _, _, l3, low3_local in arcs[v2]:
                        if ck in (ci, cj) or l3 in (l1, l2):
                            continue
                        low3 = rotate(low3_local, phase2, self.k)
                        intersection = partial & low3
                        if intersection.bit_count() != self.r - 3:
                            continue
                        rep, _ = canonical(intersection, self.k, self.equivariant)
                        target = self.lower3_index[rep]
                        key = tuple(
                            sorted(
                                {
                                    self.choices[ci].var,
                                    self.choices[cj].var,
                                    self.choices[ck].var,
                                }
                            )
                        )
                        if len(key) != 3 or key in seen[target]:
                            continue
                        seen[target].add(key)
                        witnesses[target].append(self._and_literal(key))

        for target, lits in enumerate(witnesses):
            if not lits:
                raise RuntimeError(f"depth-three lower target {target} has no witness")
            self.cnf.add(*lits)

    def _build_residence_cnf(self, depth: int):
        """Forbid every quotient path producing a one-run of length <= depth.

        A violation beginning on edge e_0 and ending on edge e_h is a path of
        h+1 selected quotient edges.  We enumerate only *minimal* violations:
        the inserted coordinate stays present on intermediate vertices and is
        deleted by the final edge.  Non-minimal violations contain one of
        these clauses already.
        """
        if depth <= 0:
            return

        # (choice index, next vertex, phase increment, lower-choice index)
        arcs: list[list[tuple[int, int, int, int]]] = [[] for _ in self.middle]
        for ci, choice in enumerate(self.choices):
            u, v = choice.endpoint
            if u == v:
                continue
            arcs[u].append((ci, v, choice.voltage, choice.lower_idx))
            arcs[v].append((ci, u, (-choice.voltage) % self.k, choice.lower_idx))

        clauses_by_h: list[set[tuple[int, ...]]] = [set() for _ in range(depth + 1)]

        for start_vertex in range(len(self.middle)):
            start_mask = self.middle[start_vertex]
            for ci, nxt, delta, lower_idx in arcs[start_vertex]:
                choice = self.choices[ci]
                next_phase = delta % self.k if self.equivariant else 0
                next_mask = rotate(self.middle[nxt], next_phase, self.k)
                inserted = next_mask & ~start_mask
                if inserted.bit_count() != 1:
                    raise AssertionError("oriented quotient edge is not a Johnson step")
                inserted_bit = inserted.bit_length() - 1
                used_choices = {ci}
                used_lowers = {lower_idx}
                path_vars = [choice.var]

                def extend(
                    current_vertex: int,
                    current_phase: int,
                    current_mask: int,
                    h: int,
                ):
                    # h is the desired run length; the path currently contains
                    # h edges before choosing its final deleting edge.
                    for cj, following, phase_delta, lower_j in arcs[current_vertex]:
                        if cj in used_choices or lower_j in used_lowers:
                            continue
                        following_phase = (
                            (current_phase + phase_delta) % self.k
                            if self.equivariant
                            else 0
                        )
                        following_mask = rotate(
                            self.middle[following], following_phase, self.k
                        )
                        has_now = (current_mask >> inserted_bit) & 1
                        has_next = (following_mask >> inserted_bit) & 1
                        if not has_now:
                            continue
                        if h == target_h:
                            if has_next:
                                continue
                            key = tuple(sorted(path_vars + [self.choices[cj].var]))
                            clauses_by_h[target_h].add(key)
                            continue
                        if not has_next:
                            # This shorter run is handled at its own depth.
                            continue
                        used_choices.add(cj)
                        used_lowers.add(lower_j)
                        path_vars.append(self.choices[cj].var)
                        extend(following, following_phase, following_mask, h + 1)
                        path_vars.pop()
                        used_lowers.remove(lower_j)
                        used_choices.remove(cj)

                for target_h in range(1, depth + 1):
                    extend(nxt, next_phase, next_mask, 1)

        for h in range(1, depth + 1):
            for key in clauses_by_h[h]:
                self.cnf.add(*[-x for x in key])
            self.residence_clause_counts[h] = len(clauses_by_h[h])

    def _build_hamilton_cnf(self):
        """Encode one quotient Hamilton cycle with oriented edges and positions."""
        n = len(self.middle)
        if n <= 1:
            return

        outgoing: list[list[int]] = [[] for _ in self.middle]
        incoming: list[list[int]] = [[] for _ in self.middle]
        directed: list[tuple[int, int, int]] = []  # (arc variable, u, v)
        for choice in self.choices:
            u, v = choice.endpoint
            if u == v:
                continue
            uv = self.cnf.var()
            vu = self.cnf.var()
            # Exactly one orientation iff this quotient edge is selected.
            self.cnf.add(-uv, choice.var)
            self.cnf.add(-vu, choice.var)
            self.cnf.add(-choice.var, uv, vu)
            self.cnf.add(-uv, -vu)
            outgoing[u].append(uv)
            incoming[v].append(uv)
            outgoing[v].append(vu)
            incoming[u].append(vu)
            directed.append((uv, u, v))
            directed.append((vu, v, u))

        for v in range(n):
            self.cnf.exactly_one(outgoing[v])
            self.cnf.exactly_one(incoming[v])

        position = [[self.cnf.var() for _ in range(n)] for _ in range(n)]
        for v in range(n):
            self.cnf.exactly_one(position[v])
        for t in range(n):
            self.cnf.exactly_one([position[v][t] for v in range(n)])
        self.cnf.add(position[0][0])

        for arc, u, v in directed:
            for t in range(n):
                self.cnf.add(-arc, -position[u][t], position[v][(t + 1) % n])

    def _build_compact_hamilton_cnf(self):
        """Connected directed 2-factor via unary MTZ ranks.

        Every selected undirected edge gets one orientation, and every vertex
        gets one incoming and one outgoing arc.  Along every arc not entering
        root 0, the unary rank strictly increases.  Thus no directed cycle can
        avoid the root, so the 2-factor has one component.  Unlike the one-hot
        position encoding, ranks need not be all-different; strictness along
        arcs is enough.
        """
        n = len(self.middle)
        if n <= 1:
            return
        outgoing: list[list[int]] = [[] for _ in self.middle]
        incoming: list[list[int]] = [[] for _ in self.middle]
        directed: list[tuple[int, int, int]] = []
        for choice in self.choices:
            u, v = choice.endpoint
            if u == v:
                continue
            uv = self.cnf.var()
            vu = self.cnf.var()
            self.cnf.add(-uv, choice.var)
            self.cnf.add(-vu, choice.var)
            self.cnf.add(-choice.var, uv, vu)
            self.cnf.add(-uv, -vu)
            outgoing[u].append(uv)
            incoming[v].append(uv)
            outgoing[v].append(vu)
            incoming[u].append(vu)
            directed.append((uv, u, v))
            directed.append((vu, v, u))
            self.directed_arcs.append((uv, u, v, choice.voltage % self.k))
            self.directed_arcs.append(
                (vu, v, u, (-choice.voltage) % self.k)
            )
        for v in range(n):
            self.cnf.exactly_one(outgoing[v])
            self.cnf.exactly_one(incoming[v])

        # rank_ge[v][t-1] means rank(v) >= t, 1 <= t <= n-1.
        rank_ge = [[self.cnf.var() for _ in range(n - 1)] for _ in range(n)]
        for t in range(n - 1):
            self.cnf.add(-rank_ge[0][t])
        for v in range(1, n):
            for t in range(n - 2):
                self.cnf.add(-rank_ge[v][t + 1], rank_ge[v][t])
        for arc, u, v in directed:
            if v == 0:
                continue
            self.cnf.add(-arc, rank_ge[v][0])
            for t in range(n - 2):
                self.cnf.add(-arc, -rank_ge[u][t], rank_ge[v][t + 1])
            self.cnf.add(-arc, -rank_ge[u][n - 2])

    def _build_oriented_lazy_cnf(self):
        """Orient the selected 2-factor but leave connectivity to lazy cuts."""
        n = len(self.middle)
        if n <= 1:
            return
        outgoing: list[list[int]] = [[] for _ in self.middle]
        incoming: list[list[int]] = [[] for _ in self.middle]
        for choice in self.choices:
            u, v = choice.endpoint
            if u == v:
                continue
            uv = self.cnf.var()
            vu = self.cnf.var()
            self.cnf.add(-uv, choice.var)
            self.cnf.add(-vu, choice.var)
            self.cnf.add(-choice.var, uv, vu)
            self.cnf.add(-uv, -vu)
            outgoing[u].append(uv)
            incoming[v].append(uv)
            outgoing[v].append(vu)
            incoming[u].append(vu)
            self.directed_arcs.append((uv, u, v, choice.voltage % self.k))
            self.directed_arcs.append(
                (vu, v, u, (-choice.voltage) % self.k)
            )
        for v in range(n):
            self.cnf.exactly_one(outgoing[v])
            self.cnf.exactly_one(incoming[v])

    def _build_residence_automaton_cnf(
        self, depth: int, final_age_budget: int | None = None
    ):
        """Compact exact short-residence encoding on the directed cycle.

        ``recent[t,v,x]`` records that coordinate ``x`` (in the canonical
        phase of quotient vertex ``v``) was inserted ``t`` transitions ago.
        Selected arcs force the new age-zero state, propagate older states
        with the arc voltage, and may not delete any state of age below
        ``depth``.  Implications suffice: every genuine recent insertion is
        forced along the unique selected predecessor chain; unsupported true
        states can only strengthen the formula.
        """
        if depth <= 0:
            return
        if not self.directed_arcs:
            raise ValueError("residence automaton has no directed arcs")

        recent: list[list[dict[int, int]]] = []
        for _ in range(depth):
            layer = []
            for mask in self.middle:
                layer.append(
                    {x: self.cnf.var() for x in range(self.k) if (mask >> x) & 1}
                )
            recent.append(layer)

        clauses_before = len(self.cnf.clauses)
        # Only one directed arc leaves each quotient vertex.  Therefore the
        # final-age budget needs one indicator per *vertex*, not one per
        # possible directed arc.  The older arc-wise encoding used thousands
        # of indicators (and a correspondingly huge sequential counter) even
        # though at most one of them could ever fire at a vertex.
        final_age_bad: list[int] = []
        final_age_bad_by_vertex: list[int] = []
        if final_age_budget is not None:
            final_age_bad_by_vertex = [self.cnf.var() for _ in self.middle]
            final_age_bad = list(final_age_bad_by_vertex)
        for arc, u, v, delta in self.directed_arcs:
            source = self.middle[u]
            target_aligned = rotate(self.middle[v], delta, self.k)
            deleted = source & ~target_aligned
            inserted = target_aligned & ~source
            if deleted.bit_count() != 1 or inserted.bit_count() != 1:
                raise AssertionError("directed quotient arc is not a Johnson step")
            deleted_x = deleted.bit_length() - 1
            inserted_actual = inserted.bit_length() - 1
            inserted_v = (inserted_actual - delta) % self.k

            # Exact age-zero state under the selected predecessor arc.
            for x, state in recent[0][v].items():
                self.cnf.add(-arc, state if x == inserted_v else -state)
            for age in range(depth):
                state = recent[age][u][deleted_x]
                if age == depth - 1 and final_age_budget is not None:
                    bad = final_age_bad_by_vertex[u]
                    # arc & state <=> this vertex is bad.  The reverse
                    # implication is conditioned on the arc; exactly one
                    # outgoing arc is selected at u, so these clauses make
                    # bad exact without introducing arc/state conjunctions.
                    self.cnf.add(-arc, -state, bad)
                    self.cnf.add(-bad, -arc, state)
                else:
                    self.cnf.add(-arc, -state)
            for age in range(depth - 1):
                # The coordinate inserted by this arc cannot simultaneously
                # be an older insertion at the target vertex.
                self.cnf.add(-arc, -recent[age + 1][v][inserted_v])
                for x, state in recent[age][u].items():
                    if x == deleted_x:
                        continue
                    y = (x - delta) % self.k
                    if y not in recent[age + 1][v]:
                        raise AssertionError("surviving coordinate missing after phase alignment")
                    self.cnf.add(-arc, -state, recent[age + 1][v][y])
                    self.cnf.add(-arc, -recent[age + 1][v][y], state)
        self.recent_states = recent
        self.residence_automaton_depth = depth
        if final_age_budget is not None:
            self.cnf.at_most_k(final_age_bad, final_age_budget)
        self.residence_budget_literals = final_age_bad
        self.residence_clause_counts = {
            **self.residence_clause_counts,
            "automaton_depth": depth,
            "automaton_clauses": len(self.cnf.clauses) - clauses_before,
            "final_age_budget": final_age_budget,
            "final_age_indicators": len(final_age_bad),
        }

    def _build_automaton_lower_q3_cnf(self):
        """Cover every rank-(r-3) orbit using exact recent-insertion states.

        At the end of a residence-3-safe four-vertex window, the intersection
        is the current middle set with the three most recent insertions
        removed.  The automaton states make those three coordinates exact, so
        only O(|V| r^3) conjunction witnesses are needed instead of enumerating
        every possible three-edge path.
        """
        if getattr(self, "residence_automaton_depth", 0) < 3:
            raise ValueError("lower-q3 automaton needs three recent layers")
        witnesses: list[list[int]] = [[] for _ in self.lower3]
        seen: list[set[tuple[int, int, int, int]]] = [set() for _ in self.lower3]
        for v, mask in enumerate(self.middle):
            elements = [x for x in range(self.k) if (mask >> x) & 1]
            for x0, x1, x2 in itertools.permutations(elements, 3):
                target_mask = mask ^ (1 << x0) ^ (1 << x1) ^ (1 << x2)
                rep, _ = canonical(target_mask, self.k, self.equivariant)
                target = self.lower3_index[rep]
                key = (v, x0, x1, x2)
                if key in seen[target]:
                    continue
                seen[target].add(key)
                witness = self._and_literal(
                    tuple(
                        sorted(
                            (
                                self.recent_states[0][v][x0],
                                self.recent_states[1][v][x1],
                                self.recent_states[2][v][x2],
                            )
                        )
                    )
                )
                witnesses[target].append(witness)
        for target, lits in enumerate(witnesses):
            if not lits:
                raise RuntimeError(f"automaton lower-q3 target {target} has no witness")
            self.cnf.add(*lits)

    def _build_coresidence_automaton_cnf(
        self, depth: int, enforce_depth: int = 0
    ):
        """Track recent deletions exactly, optionally forbidding quick returns.

        These are the complement-dual states to ``recent_states``.  A deleted
        coordinate starts at age zero in the target vertex and propagates
        while it remains absent.  If ``enforce_depth`` is positive, a selected
        arc may not reinsert a coordinate of age below that threshold.
        Tracking alone is enough for compact upper-q3 coverage: three surviving
        deletion states identify a valid four-vertex union.
        """
        if depth <= 0 or not self.directed_arcs:
            raise ValueError("co-residence automaton requires directed arcs")
        full = (1 << self.k) - 1
        recent: list[list[dict[int, int]]] = []
        for _ in range(depth):
            layer = []
            for mask in self.middle:
                layer.append(
                    {x: self.cnf.var() for x in range(self.k) if not (mask >> x) & 1}
                )
            recent.append(layer)

        clauses_before = len(self.cnf.clauses)
        for arc, u, v, delta in self.directed_arcs:
            source = self.middle[u]
            target_aligned = rotate(self.middle[v], delta, self.k)
            deleted = source & ~target_aligned
            inserted = target_aligned & ~source
            deleted_actual = deleted.bit_length() - 1
            inserted_u = inserted.bit_length() - 1
            deleted_v = (deleted_actual - delta) % self.k

            for x, state in recent[0][v].items():
                self.cnf.add(-arc, state if x == deleted_v else -state)
            for age in range(min(enforce_depth, depth)):
                self.cnf.add(-arc, -recent[age][u][inserted_u])
            for age in range(depth - 1):
                # The freshly deleted coordinate was present at the source,
                # so it cannot also represent an older still-absent deletion.
                self.cnf.add(-arc, -recent[age + 1][v][deleted_v])
                for x, state in recent[age][u].items():
                    if x == inserted_u:
                        continue
                    y = (x - delta) % self.k
                    if y not in recent[age + 1][v]:
                        raise AssertionError("absent coordinate missing after phase alignment")
                    self.cnf.add(-arc, -state, recent[age + 1][v][y])
                    self.cnf.add(-arc, -recent[age + 1][v][y], state)
        self.recent_deleted_states = recent
        self.coresidence_automaton_depth = depth
        self.residence_clause_counts = {
            **self.residence_clause_counts,
            "coresidence_depth": enforce_depth,
            "coresidence_tracking_depth": depth,
            "coresidence_clauses": len(self.cnf.clauses) - clauses_before,
        }

    def _build_automaton_upper_q3_cnf(self):
        """Cover rank-(r+3) orbits from three exact recent deletions."""
        if getattr(self, "coresidence_automaton_depth", 0) < 3:
            raise ValueError("upper-q3 automaton needs three recent-deletion layers")
        full = (1 << self.k) - 1
        witnesses: list[list[int]] = [[] for _ in self.upper3]
        for v, mask in enumerate(self.middle):
            elements = [x for x in range(self.k) if not (mask >> x) & 1]
            for x0, x1, x2 in itertools.permutations(elements, 3):
                target_mask = mask | (1 << x0) | (1 << x1) | (1 << x2)
                rep, _ = canonical(target_mask, self.k, self.equivariant)
                target = self.upper3_index[rep]
                witness = self._and_literal(
                    tuple(
                        sorted(
                            (
                                self.recent_deleted_states[0][v][x0],
                                self.recent_deleted_states[1][v][x1],
                                self.recent_deleted_states[2][v][x2],
                            )
                        )
                    )
                )
                witnesses[target].append(witness)
        for target, lits in enumerate(witnesses):
            if not lits:
                raise RuntimeError(f"automaton upper-q3 target {target} has no witness")
            self.cnf.add(*lits)

    def _build_compiler_automaton_cnf(
        self,
        depth: int,
        target_ranks: tuple[int, ...] = (),
        target_masks: tuple[int, ...] = (),
        pointwise_d2: bool = False,
        d2_budget: int | None = None,
        native_lower_q2: bool = False,
    ):
        """Jointly choose an equivariant depth-``depth`` OR--Pascal preimage.

        ``entry[v,x]`` is an entry attached to the current middle vertex and
        is indexed so that the middle mask at time i equals the union of the
        current entry and the previous ``depth`` entries.  Entry-history
        states propagate exactly along the selected directed arcs, including
        voltage alignment.  Forbidding a live entry coordinate from being
        deleted before its final history age enforces the opposite inclusion,
        so the union is *exactly* the prescribed middle mask.

        Finally every nonempty lower mask orbit must occur as the union of
        one, two, or three consecutive entries.  For the only currently used
        case depth=3 these are precisely the rows below the middle row.
        """
        if depth != 3:
            raise ValueError("joint compiler currently supports exactly depth 3")
        if not self.directed_arcs:
            raise ValueError("joint compiler requires directed arcs")
        if not self.equivariant:
            raise ValueError("joint compiler currently requires quotient symmetry")

        clauses_before = len(self.cnf.clauses)
        entry: list[dict[int, int]] = []
        for mask in self.middle:
            local = {x: self.cnf.var() for x in range(self.k) if (mask >> x) & 1}
            self.cnf.add(*local.values())  # normalized nonzero entry
            entry.append(local)

        history: list[list[dict[int, int]]] = [entry]
        for _ in range(depth):
            layer = []
            for mask in self.middle:
                layer.append(
                    {x: self.cnf.var() for x in range(self.k) if (mask >> x) & 1}
                )
            history.append(layer)

        d2_bad = []
        if pointwise_d2 and d2_budget is not None:
            if d2_budget < 0 or d2_budget > len(self.middle):
                raise ValueError(
                    f"compiler D2 budget {d2_budget} must lie in [0,{len(self.middle)}]"
                )
            d2_bad = [self.cnf.var() for _ in self.middle]

        for arc, u, v, delta in self.directed_arcs:
            source = self.middle[u]
            target_aligned = rotate(self.middle[v], delta, self.k)
            deleted = source & ~target_aligned
            inserted = target_aligned & ~source
            if deleted.bit_count() != 1 or inserted.bit_count() != 1:
                raise AssertionError("compiler arc is not a Johnson step")
            deleted_x = deleted.bit_length() - 1
            inserted_actual = inserted.bit_length() - 1
            inserted_v = (inserted_actual - delta) % self.k

            for age in range(depth):
                # An entry coordinate must survive until it has contributed
                # to all depth+1 middle windows containing that entry.
                self.cnf.add(-arc, -history[age][u][deleted_x])
                # A newly inserted middle coordinate cannot be an older entry.
                self.cnf.add(-arc, -history[age + 1][v][inserted_v])
                for x, state in history[age][u].items():
                    if x == deleted_x:
                        continue
                    y = (x - delta) % self.k
                    target_state = history[age + 1][v][y]
                    self.cnf.add(-arc, -state, target_state)
                    self.cnf.add(-arc, -target_state, state)

            if pointwise_d2:
                # Redundant nested-rainbow consequence of a full compiler:
                # exact D^3 reconstruction makes every entry envelope rank 4,
                # so rank-(r-1) masks can occur only in the W D2 cells.  Full
                # lower coverage therefore forces those cells to equal the W
                # outgoing lower colours bijectively.  Encoding it explicitly
                # is a powerful propagation lemma.  The state convention attaches entry
                # E_i=A_{i+3} to T_i, hence ages 0,1,2 at T_i form
                # A_{i+1}|A_{i+2}|A_{i+3}=T_i cap T_{i+1}.
                lower_u = source & target_aligned
                if lower_u.bit_count() != self.r - 1:
                    raise AssertionError("outgoing compiler lower colour has wrong rank")
                for x in range(self.k):
                    if not (source >> x) & 1:
                        continue
                    states = [history[age][u][x] for age in range(3)]
                    if (lower_u >> x) & 1:
                        if d2_bad:
                            self.cnf.add(-arc, d2_bad[u], *states)
                        else:
                            self.cnf.add(-arc, *states)
                    else:
                        for state in states:
                            self.cnf.add(-arc, -state)

        if d2_bad:
            self.cnf.at_most_k(d2_bad, d2_budget)

        # Every prescribed middle coordinate must be supplied by one of the
        # current/three previous entries.  All history variables live inside
        # the current middle mask, giving the reverse containment for free.
        for v, mask in enumerate(self.middle):
            for x in range(self.k):
                if (mask >> x) & 1:
                    self.cnf.add(*(history[age][v][x] for age in range(depth + 1)))

        ranks = set(target_ranks or range(1, self.r))
        if target_masks and not target_ranks:
            # A nonempty explicit target list is allowed to stand on its own.
            ranks = set()
        if any(rank <= 0 or rank >= self.r for rank in ranks):
            raise ValueError(f"invalid compiler target ranks {sorted(ranks)}")
        witness_ranks = set(ranks)
        if pointwise_d2:
            witness_ranks.discard(self.r - 1)
        lower_reps = {
            canonical(mask, self.k, True)[0]
            for mask in range(1, 1 << self.k)
            if mask.bit_count() in witness_ranks
        }
        explicit_reps = set()
        for mask in target_masks:
            if mask <= 0 or mask >= (1 << self.k):
                raise ValueError(f"invalid compiler target mask {mask}")
            if mask.bit_count() >= self.r:
                raise ValueError(
                    f"compiler target {mask} has rank {mask.bit_count()}, "
                    f"expected below {self.r}"
                )
            explicit_reps.add(canonical(mask, self.k, True)[0])
        lower_reps.update(explicit_reps)
        lower_reps = sorted(lower_reps)
        rep_index = {mask: i for i, mask in enumerate(lower_reps)}
        witnesses: list[list[int]] = [[] for _ in lower_reps]
        witness_count = 0
        for v, middle_mask in enumerate(self.middle):
            elements = [x for x in range(self.k) if (middle_mask >> x) & 1]
            # Every physical target contained in this canonical middle mask.
            target_sizes = sorted(witness_ranks | {mask.bit_count() for mask in explicit_reps})
            for size in target_sizes:
                for subset in itertools.combinations(elements, size):
                    target = sum(1 << x for x in subset)
                    rep, _ = canonical(target, self.k, True)
                    if rep not in rep_index:
                        continue
                    target_index = rep_index[rep]
                    for row_depth in range(depth):
                        witness = self.cnf.var()
                        witness_count += 1
                        witnesses[target_index].append(witness)
                        for x in elements:
                            states = [
                                history[age][v][x]
                                for age in range(row_depth + 1)
                            ]
                            if (target >> x) & 1:
                                self.cnf.add(-witness, *states)
                            else:
                                for state in states:
                                    self.cnf.add(-witness, -state)
        for target, lits in zip(lower_reps, witnesses):
            if not lits:
                raise RuntimeError(f"compiler lower orbit {target} has no witness")
            self.cnf.add(*lits)

        self.compiler_entry_vars = entry
        self.compiler_history_vars = history
        self.compiler_depth = depth
        self.compiler_d2_bad_vars = d2_bad
        self.compiler_report = {
            "depth": depth,
            "entry_variables": sum(map(len, entry)),
            "history_variables": sum(
                len(local) for layer in history[1:] for local in layer
            ),
            "lower_orbits": len(lower_reps),
            "target_ranks": sorted(ranks),
            "target_masks": sorted(explicit_reps),
            "witness_target_ranks": sorted(witness_ranks),
            "pointwise_d2": pointwise_d2,
            "d2_budget": d2_budget,
            "native_lower_q2": native_lower_q2,
            "witnesses": witness_count,
            "clauses": len(self.cnf.clauses) - clauses_before,
        }

    def selected_choices(self, model: set[int]) -> list[Choice]:
        return [choice for choice in self.choices if choice.var in model]

    def components(self, selected: list[Choice]) -> list[set[int]]:
        adjacency: list[list[tuple[int, int]]] = [[] for _ in self.middle]
        for edge_id, choice in enumerate(selected):
            u, v = choice.endpoint
            adjacency[u].append((v, edge_id))
            adjacency[v].append((u, edge_id))
        if any(len(adj) != 2 for adj in adjacency):
            raise AssertionError(f"decoded graph is not degree two: {[len(a) for a in adjacency]}")
        unseen = set(range(len(self.middle)))
        comps = []
        while unseen:
            root = next(iter(unseen))
            stack = [root]
            comp = set()
            while stack:
                v = stack.pop()
                if v in comp:
                    continue
                comp.add(v)
                unseen.discard(v)
                stack.extend(w for w, _ in adjacency[v] if w not in comp)
            comps.append(comp)
        return comps

    def add_component_cuts(self, components: list[set[int]]) -> int:
        if len(components) <= 1:
            return 0
        all_vertices = set(range(len(self.middle)))
        added = 0
        canonical_sides = set()
        for comp in components:
            other = all_vertices - comp
            side = tuple(sorted(comp if len(comp) <= len(other) else other))
            if side in canonical_sides:
                continue
            canonical_sides.add(side)
            key = side
            if key not in self.cross_cache:
                side_set = set(side)
                crossing = [
                    choice.var
                    for choice in self.choices
                    if (choice.endpoint[0] in side_set) != (choice.endpoint[1] in side_set)
                ]
                self.cross_cache[key] = crossing
            crossing = self.cross_cache[key]
            if not crossing:
                raise RuntimeError("component cut has no crossing choice")
            self.cnf.add(*crossing)
            added += 1
        return added

    def traverse_cycle(self, selected: list[Choice]):
        adjacency: list[list[tuple[int, int, int]]] = [[] for _ in self.middle]
        for eid, choice in enumerate(selected):
            u, v = choice.endpoint
            adjacency[u].append((v, eid, choice.voltage))
            adjacency[v].append((u, eid, (-choice.voltage) % self.k if self.equivariant else 0))
        start = 0
        current = start
        previous_edge = -1
        vertices = [start]
        phases = [0]
        edges = []
        phase = 0
        for _ in range(len(selected)):
            options = [item for item in adjacency[current] if item[1] != previous_edge]
            if not options:
                raise AssertionError("cycle traversal stuck")
            nxt, eid, delta = options[0]
            edges.append(eid)
            phase = (phase + delta) % self.k if self.equivariant else 0
            previous_edge = eid
            current = nxt
            vertices.append(current)
            phases.append(phase)
        if current != start or len(set(edges)) != len(selected):
            raise AssertionError("not one quotient cycle")
        return vertices[:-1], phases[:-1], edges, phase

    def lift_middle_cycle(self, selected: list[Choice]):
        qvertices, qphases, _, voltage = self.traverse_cycle(selected)
        if not self.equivariant:
            return [self.middle[v] for v in qvertices], voltage
        if voltage == 0:
            return [], voltage
        result = []
        offset = 0
        for _ in range(self.k):
            for vertex, phase in zip(qvertices, qphases):
                result.append(rotate(self.middle[vertex], phase + offset, self.k))
            offset = (offset + voltage) % self.k
        return result, voltage

    def residence_violations(self, middle_cycle: list[int], depth: int):
        n = len(middle_cycle)
        if depth <= 0:
            return []
        deleted = []
        inserted = []
        for i in range(n):
            a = middle_cycle[i]
            b = middle_cycle[(i + 1) % n]
            dm = a & ~b
            im = b & ~a
            if dm.bit_count() != 1 or im.bit_count() != 1:
                raise AssertionError("lift is not a Johnson cycle")
            deleted.append(dm.bit_length() - 1)
            inserted.append(im.bit_length() - 1)
        bad = []
        for i, x in enumerate(inserted):
            for t in range(1, depth + 1):
                if deleted[(i + t) % n] == x:
                    bad.append((i, t))
                    break
        return bad

    def coresidence_violations(self, middle_cycle: list[int], depth: int):
        """Deleted coordinates reinserted within ``depth`` later steps."""
        n = len(middle_cycle)
        if depth <= 0:
            return []
        deleted = []
        inserted = []
        for i in range(n):
            a = middle_cycle[i]
            b = middle_cycle[(i + 1) % n]
            deleted.append((a & ~b).bit_length() - 1)
            inserted.append((b & ~a).bit_length() - 1)
        bad = []
        for i, x in enumerate(deleted):
            for t in range(1, depth + 1):
                if inserted[(i + t) % n] == x:
                    bad.append((i, t))
                    break
        return bad

    def verify(self, selected: list[Choice], residence: int):
        upper_load = [0] * len(self.upper)
        middle_degree = [0] * len(self.middle)
        for choice in selected:
            upper_load[choice.upper_idx] += 1
            middle_degree[choice.endpoint[0]] += 1
            middle_degree[choice.endpoint[1]] += 1
        comps = self.components(selected)
        cycle, voltage = ([], 0)
        if len(comps) == 1:
            cycle, voltage = self.lift_middle_cycle(selected)
        report = {
            "selected": len(selected),
            "components": [len(c) for c in comps],
            "upper_load_histogram": {
                str(x): upper_load.count(x) for x in sorted(set(upper_load))
            },
            "middle_degree_histogram": {
                str(x): middle_degree.count(x) for x in sorted(set(middle_degree))
            },
            "voltage": voltage,
            "lift_length": len(cycle),
        }
        if cycle:
            n = len(cycle)
            report["unique_middle"] = len(set(cycle))
            lower = [cycle[i] & cycle[(i + 1) % n] for i in range(n)]
            upper = [cycle[i] | cycle[(i + 1) % n] for i in range(n)]
            report["unique_lower_q1"] = len(set(lower))
            report["unique_upper_q1"] = len(set(upper))
            report["upper_q1_target"] = math.comb(self.k, self.r + 1)
            upper2 = [
                cycle[i] | cycle[(i + 1) % n] | cycle[(i + 2) % n]
                for i in range(n)
            ]
            upper2_good = {x for x in upper2 if x.bit_count() == self.r + 2}
            lower2 = [
                cycle[i] & cycle[(i + 1) % n] & cycle[(i + 2) % n]
                for i in range(n)
            ]
            lower2_good = {x for x in lower2 if x.bit_count() == self.r - 2}
            report["unique_lower_q2"] = len(lower2_good)
            report["lower_q2_target"] = math.comb(self.k, self.r - 2)
            report["unique_upper_q2"] = len(upper2_good)
            report["upper_q2_target"] = math.comb(self.k, self.r + 2)
            lower3 = []
            upper3 = []
            for i in range(n):
                lo = (1 << self.k) - 1
                hi = 0
                for h in range(4):
                    lo &= cycle[(i + h) % n]
                    hi |= cycle[(i + h) % n]
                if lo.bit_count() == self.r - 3:
                    lower3.append(lo)
                if hi.bit_count() == self.r + 3:
                    upper3.append(hi)
            report["unique_lower_q3"] = len(set(lower3))
            report["lower_q3_target"] = math.comb(self.k, self.r - 3)
            report["unique_upper_q3"] = len(set(upper3))
            report["upper_q3_target"] = math.comb(self.k, self.r + 3)
            violations = self.residence_violations(cycle, residence)
            coviolations = self.coresidence_violations(cycle, residence)
            report["residence_depth"] = residence
            report["residence_violations"] = len(violations)
            report["residence_examples"] = violations[:20]
            report["coresidence_violations"] = len(coviolations)
            report["coresidence_examples"] = coviolations[:20]
        return report

    def add_zero_voltage_block(self, selected: list[Choice]):
        self.cnf.add(*[-choice.var for choice in selected])

    def selected_path_vars_for_lift_indices(
        self, selected: list[Choice], bad_indices: list[tuple[int, int]]
    ) -> list[list[int]]:
        """Map short lifted-cycle violations to quotient-edge nogoods."""
        _, _, qedges, _ = self.traverse_cycle(selected)
        qlen = len(qedges)
        cuts = []
        seen = set()
        for i, distance in bad_indices:
            vars_ = []
            for t in range(distance + 1):
                eid = qedges[(i + t) % qlen]
                vars_.append(selected[eid].var)
            key = tuple(sorted(set(vars_)))
            if key and key not in seen:
                seen.add(key)
                cuts.append([-x for x in key])
        return cuts


def parse_model(text: str) -> tuple[str, set[int]]:
    status = "UNKNOWN"
    model: set[int] = set()
    for line in text.splitlines():
        if line.startswith("s "):
            if "UNSATISFIABLE" in line:
                status = "UNSAT"
            elif "SATISFIABLE" in line:
                status = "SAT"
        elif line.startswith("v "):
            for token in line.split()[1:]:
                value = int(token)
                if value > 0:
                    model.add(value)
    return status, model


def solve_once(
    cnf: CNF,
    cnf_path: Path,
    out_path: Path,
    seed: int,
    limit: int,
    walk_initially: bool = False,
):
    cnf.write(cnf_path)
    # Keep the desktop default, but make every CNF driver cloud-portable.
    # Example: KISSAT=/dev/shm/k15_sat/kissat/build/kissat python3 driver.py ...
    cmd = [
        os.environ.get("KISSAT", "/opt/homebrew/bin/kissat"),
        "--sat",
        f"--seed={seed}",
        f"--time={limit}",
    ]
    if walk_initially:
        cmd.append("--walkinitially")
    cmd.append(str(cnf_path))
    started = time.time()
    proc = subprocess.run(cmd, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out_path.write_text(proc.stdout, encoding="utf-8")
    status, model = parse_model(proc.stdout)
    return status, model, time.time() - started, proc.returncode


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--k", type=int, required=True)
    parser.add_argument("--full", action="store_true", help="do not quotient by translations")
    parser.add_argument("--no-cap2", action="store_true")
    parser.add_argument(
        "--no-upper-q1",
        action="store_true",
        help="relax rank-(r+1) coverage (seed/diagnostic mode only)",
    )
    parser.add_argument(
        "--upper-q1-target",
        type=int,
        action="append",
        default=[],
        help=(
            "with --no-upper-q1, require one physical rank-(r+1) mask "
            "(and, in quotient mode, its translation orbit); repeatable"
        ),
    )
    parser.add_argument(
        "--upper-q1-hole-budget",
        type=int,
        help="allow at most this many uncovered rank-(r+1) quotient orbits",
    )
    parser.add_argument("--q2", action="store_true")
    parser.add_argument(
        "--upper-q2-target",
        type=int,
        action="append",
        default=[],
        help=(
            "require one physical rank-(r+2) mask (and, in quotient mode, "
            "its translation orbit) as an upper-q2 shadow; repeatable"
        ),
    )
    parser.add_argument(
        "--upper-q2-hole-budget",
        type=int,
        help="allow at most this many uncovered rank-(r+2) quotient orbits",
    )
    parser.add_argument("--lower-q2", action="store_true")
    parser.add_argument(
        "--lower-q2-target",
        type=int,
        action="append",
        default=[],
        help=(
            "require one physical rank-(r-2) mask (and, in quotient mode, "
            "its translation orbit) as a lower-q2 shadow; repeatable"
        ),
    )
    parser.add_argument("--lower-q3", action="store_true")
    parser.add_argument("--residence", type=int, default=0)
    parser.add_argument(
        "--direct-residence",
        action="store_true",
        help="compile all short-residence path clauses up front instead of lazy cuts",
    )
    parser.add_argument(
        "--automaton-residence",
        action="store_true",
        help="encode short residence by propagating recent coordinates on directed arcs",
    )
    parser.add_argument(
        "--automaton-lower-q3",
        action="store_true",
        help="cover lower q3 using exact recent-coordinate automaton states",
    )
    parser.add_argument(
        "--residence-budget",
        type=int,
        help="allow at most this many quotient violations at the final automaton age",
    )
    parser.add_argument(
        "--automaton-coresidence",
        action="store_true",
        help="also forbid deleted coordinates returning within the residence depth",
    )
    parser.add_argument(
        "--automaton-upper-q3",
        action="store_true",
        help="cover upper q3 using exact recent-deletion automaton states",
    )
    parser.add_argument(
        "--automaton-compiler-depth",
        type=int,
        default=0,
        help="jointly encode an equivariant OR--Pascal preimage (currently depth 3)",
    )
    parser.add_argument(
        "--compiler-target-ranks",
        type=int,
        nargs="+",
        default=[],
        help="restrict joint compiler coverage to these ranks (diagnostic/seed mode)",
    )
    parser.add_argument(
        "--compiler-target-mask",
        type=int,
        action="append",
        default=[],
        help=(
            "require one physical lower mask (and, in quotient mode, its "
            "translation orbit) in the joint compiler; repeatable"
        ),
    )
    parser.add_argument(
        "--compiler-pointwise-d2",
        action="store_true",
        help=(
            "redundant full-compiler strengthening: force every cyclic D2 "
            "entry cell to equal its outgoing lower colour"
        ),
    )
    parser.add_argument(
        "--compiler-flat-d2",
        action="store_true",
        help="alias for --compiler-pointwise-d2",
    )
    parser.add_argument(
        "--compiler-d2-budget",
        type=int,
        help=(
            "with pointwise/flat D2, allow this many quotient vertices to "
            "miss coordinates from their outgoing lower colour"
        ),
    )
    parser.add_argument(
        "--direct-connectivity",
        action="store_true",
        help="encode a directed Hamilton cycle with one-hot vertex positions",
    )
    parser.add_argument(
        "--compact-connectivity",
        action="store_true",
        help="encode connectivity with directed arcs and unary MTZ ranks",
    )
    parser.add_argument(
        "--oriented-lazy-connectivity",
        action="store_true",
        help="orient the 2-factor for automata; impose connectivity by lazy cuts",
    )
    parser.add_argument("--max-rounds", type=int, default=200)
    parser.add_argument("--time-per-round", type=int, default=120)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument(
        "--kissat-walkinitially",
        action="store_true",
        help="enable Kissat's initial local-search walk before CDCL",
    )
    parser.add_argument(
        "--build-only",
        action="store_true",
        help="write the constructed CNF and exit without invoking Kissat",
    )
    parser.add_argument(
        "--hint-certificate",
        type=Path,
        help="freeze choices away from residence defects of an existing certificate",
    )
    parser.add_argument(
        "--fix-certificate",
        type=Path,
        help="fix every sigma choice to an existing decoded certificate",
    )
    parser.add_argument(
        "--lns-free",
        type=int,
        default=0,
        help="with --hint-certificate, number of nearest quotient choices left free",
    )
    parser.add_argument(
        "--lns-center-residue",
        type=int,
        help="center connected-hint LNS on one quotient residence-defect residue",
    )
    parser.add_argument(
        "--lns-center-position",
        type=int,
        help="center connected-hint LNS on an arbitrary quotient cycle position",
    )
    parser.add_argument(
        "--lns-defect-aware",
        action="store_true",
        help=(
            "for a disconnected hint, free every selected lower choice on a "
            "short-residence defect window before filling by component-crossing score"
        ),
    )
    parser.add_argument(
        "--lns-include-lower-index",
        type=int,
        action="append",
        default=[],
        help="always leave this lower-orbit index free in an LNS neighbourhood",
    )
    parser.add_argument(
        "--lns-extra-changes",
        type=int,
        default=0,
        help=(
            "with --hint-certificate, allow this many additional changed "
            "lower-orbit choices outside the ordinary LNS free set"
        ),
    )
    parser.add_argument(
        "--hint-q2-near-target",
        type=int,
        action="append",
        default=[],
        help=(
            "with --hint-certificate, require this upper-q2 orbit to be "
            "covered by a witness differing from the hint in exactly one "
            "compatible lower choice; repeatable"
        ),
    )
    parser.add_argument(
        "--hint-q2-near-side",
        choices=("upper", "lower"),
        default="upper",
        help="shadow side used by --hint-q2-near-target",
    )
    parser.add_argument(
        "--hint-q2-near-max-q1-delta",
        type=int,
        default=1,
        help="maximum isolated q1-hole increase allowed in a near-q2 witness",
    )
    parser.add_argument(
        "--hint-q2-near-min-endpoint-overlap",
        type=int,
        default=0,
        help="minimum old/new endpoint overlap for a near-q2 witness",
    )
    parser.add_argument(
        "--hint-q2-near-max-cycle-distance",
        type=int,
        help="maximum hint-cycle distance between the two q2 witness choices",
    )
    parser.add_argument(
        "--hint-preserve-covered-upper-q1",
        action="store_true",
        help=(
            "with --hint-certificate, forbid relocation of existing upper-q1 "
            "holes by preserving every orbit currently covered by the hint"
        ),
    )
    parser.add_argument(
        "--block-hint",
        action="store_true",
        help="require the selected sigma assignment to differ from the hint",
    )
    parser.add_argument(
        "--block-certificate",
        type=Path,
        action="append",
        default=[],
        help="block an exact selected sigma assignment from a certificate (repeatable)",
    )
    parser.add_argument(
        "--gap-min",
        type=int,
        help="minimum selected choices in each cyclic endpoint-gap class",
    )
    parser.add_argument(
        "--gap-max",
        type=int,
        help="maximum selected choices in each cyclic endpoint-gap class",
    )
    parser.add_argument(
        "--parallel-min",
        type=int,
        help=(
            "require at least this many selected sigma choices to have a "
            "same-quotient-endpoints parallel alternative"
        ),
    )
    parser.add_argument(
        "--lower-q2-min2-orbit",
        type=int,
        action="append",
        default=[],
        help=(
            "require at least two distinct selected q2-lower witnesses for "
            "this canonical orbit mask (repeatable; requires --lower-q2)"
        ),
    )
    parser.add_argument(
        "--force-choice",
        type=int,
        nargs=3,
        action="append",
        default=[],
        metavar=("LOWER", "ADD_A", "ADD_B"),
        help="force a selected sigma choice (repeatable)",
    )
    parser.add_argument("--prefix", default=None)
    args = parser.parse_args()
    if sum(
        map(
            bool,
            (
                args.direct_connectivity,
                args.compact_connectivity,
                args.oriented_lazy_connectivity,
            ),
        )
    ) > 1:
        parser.error("choose at most one connectivity/orientation encoding")
    if args.direct_residence and args.automaton_residence:
        parser.error("choose at most one direct residence encoding")
    if args.automaton_residence and not (
        args.compact_connectivity or args.oriented_lazy_connectivity
    ):
        parser.error("--automaton-residence requires a directed connectivity mode")
    if args.automaton_lower_q3 and (
        not args.automaton_residence or args.residence < 3
    ):
        parser.error("--automaton-lower-q3 requires residence >=3 automaton mode")
    if args.residence_budget is not None and not args.automaton_residence:
        parser.error("--residence-budget requires --automaton-residence")
    if (args.automaton_coresidence or args.automaton_upper_q3) and (
        not (args.compact_connectivity or args.oriented_lazy_connectivity)
        or args.residence < 3
    ):
        parser.error("co-residence/upper-q3 automata require directed mode and depth >=3")
    if args.automaton_compiler_depth and not (
        args.compact_connectivity or args.oriented_lazy_connectivity
    ):
        parser.error("--automaton-compiler-depth requires a directed connectivity mode")
    if args.lower_q2_min2_orbit and not args.lower_q2:
        parser.error("--lower-q2-min2-orbit requires --lower-q2")
    if args.upper_q2_hole_budget is not None and not args.q2:
        parser.error("--upper-q2-hole-budget requires --q2")
    if args.compiler_d2_budget is not None and not (
        args.compiler_pointwise_d2 or args.compiler_flat_d2
    ):
        parser.error("--compiler-d2-budget requires --compiler-pointwise-d2/--compiler-flat-d2")

    equivariant = not args.full
    prefix = Path(
        args.prefix
        or f"scratch/sigma_sat_k{args.k}_{'quot' if equivariant else 'full'}"
    )
    prefix.parent.mkdir(parents=True, exist_ok=True)
    cnf_path = prefix.with_suffix(".cnf")
    out_path = prefix.with_suffix(".kissat.out")
    cert_path = prefix.with_suffix(".certificate.json")

    instance = SigmaInstance(
        args.k,
        equivariant=equivariant,
        cap2=not args.no_cap2,
        cover_upper=not args.no_upper_q1,
        q2=args.q2,
        lower_q2=args.lower_q2,
        upper_q1_masks=tuple(args.upper_q1_target),
        upper_q2_masks=tuple(args.upper_q2_target),
        upper_q1_hole_budget=args.upper_q1_hole_budget,
        upper_q2_hole_budget=args.upper_q2_hole_budget,
        lower_q2_masks=tuple(args.lower_q2_target),
        lower_q3=args.lower_q3,
        direct_residence=args.residence if args.direct_residence else 0,
        automaton_residence=args.residence if args.automaton_residence else 0,
        residence_budget=args.residence_budget,
        automaton_lower_q3=args.automaton_lower_q3,
        automaton_coresidence=args.residence if args.automaton_coresidence else 0,
        automaton_upper_q3=args.automaton_upper_q3,
        automaton_compiler_depth=args.automaton_compiler_depth,
        compiler_target_ranks=tuple(args.compiler_target_ranks),
        compiler_target_masks=tuple(args.compiler_target_mask),
        compiler_pointwise_d2=(
            args.compiler_pointwise_d2 or args.compiler_flat_d2
        ),
        compiler_d2_budget=args.compiler_d2_budget,
        direct_connectivity=args.direct_connectivity,
        compact_connectivity=args.compact_connectivity,
        oriented_lazy_connectivity=args.oriented_lazy_connectivity,
    )
    lns_report = None
    if args.fix_certificate:
        fixed_hint = json.loads(args.fix_certificate.read_text())
        fixed_keys = {
            (item["lower"], tuple(sorted(item["add"])))
            for item in fixed_hint.get("selected_options", [])
        }
        fixed_choices = [
            choice
            for choice in instance.choices
            if (choice.lower, tuple(sorted((choice.add_a, choice.add_b))))
            in fixed_keys
        ]
        if len(fixed_choices) != len(instance.lower):
            parser.error("could not decode every selected choice from --fix-certificate")
        for choice in fixed_choices:
            instance.cnf.add(choice.var)
    if args.hint_certificate:
        if args.lns_free <= 0:
            parser.error("--hint-certificate requires positive --lns-free")
        if args.lns_extra_changes < 0:
            parser.error("--lns-extra-changes must be nonnegative")
        hint = json.loads(args.hint_certificate.read_text())
        hint_status = str(hint.get("status", ""))
        if not (
            hint_status.startswith("SAT")
            or hint_status in (
                "AFFINE_SEED",
                "NEAR_SAT_LOWER_Q2_MINUS_ONE_ORBIT",
                "K13_MATERIALIZED_SELECTION",
            )
        ) or hint.get("k", hint.get("p")) != args.k:
            parser.error(
                "hint certificate must be a decoded SAT/seed with requested k"
            )
        selected_keys = {
            (item["lower"], tuple(sorted(item["add"])))
            for item in hint["selected_options"]
        }
        selected = [
            choice
            for choice in instance.choices
            if (choice.lower, tuple(sorted((choice.add_a, choice.add_b))))
            in selected_keys
        ]
        if len(selected) != len(instance.lower):
            parser.error("could not decode every selected choice from hint certificate")

        preserved_upper_q1 = 0
        if args.hint_preserve_covered_upper_q1:
            selected_vars = {choice.var for choice in selected}
            for variables in instance.by_upper:
                if any(variable in selected_vars for variable in variables):
                    instance.cnf.add(*variables)
                    preserved_upper_q1 += 1

        near_q2_report = []
        if args.hint_q2_near_target:
            selected_vars = {choice.var for choice in selected}
            selected_by_lower = {choice.lower_idx: choice for choice in selected}
            selected_upper_load = Counter(choice.upper_idx for choice in selected)
            inverse_and = {
                literal: key for key, literal in instance.and_cache.items()
            }
            cycle_position = None
            if args.hint_q2_near_max_cycle_distance is not None:
                try:
                    _, _, quotient_edges, _ = instance.traverse_cycle(selected)
                except AssertionError:
                    parser.error(
                        "--hint-q2-near-max-cycle-distance requires a connected hint"
                    )
                cycle_position = {
                    selected[edge_id].lower_idx: position
                    for position, edge_id in enumerate(quotient_edges)
                }
            for physical_target in args.hint_q2_near_target:
                representative = canonical(physical_target, args.k, equivariant)[0]
                q2_index = (
                    instance.upper2_index
                    if args.hint_q2_near_side == "upper"
                    else instance.lower2_index
                )
                q2_witnesses = (
                    instance.upper_q2_witnesses
                    if args.hint_q2_near_side == "upper"
                    else instance.lower_q2_witnesses
                )
                if representative not in q2_index:
                    parser.error(
                        "--hint-q2-near-target must also be present in the "
                        f"encoded {args.hint_q2_near_side}-q2 target set"
                    )
                target = q2_index[representative]
                allowed = []
                incompatible = 0
                for literal in q2_witnesses[target]:
                    key = inverse_and.get(literal, (literal,))
                    chosen = [var for var in key if var in selected_vars]
                    unchosen = [var for var in key if var not in selected_vars]
                    if len(chosen) != 1 or len(unchosen) != 1:
                        continue
                    a = instance.choice_by_var[chosen[0]]
                    b = instance.choice_by_var[unchosen[0]]
                    if a.lower_idx == b.lower_idx:
                        incompatible += 1
                        continue
                    current = selected_by_lower[b.lower_idx]
                    fills_q1_hole = int(selected_upper_load[b.upper_idx] == 0)
                    creates_q1_hole = int(
                        selected_upper_load[current.upper_idx] == 1
                        and current.upper_idx != b.upper_idx
                    )
                    q1_delta = creates_q1_hole - fills_q1_hole
                    if q1_delta > args.hint_q2_near_max_q1_delta:
                        continue
                    endpoint_overlap = len(set(current.endpoint) & set(b.endpoint))
                    if endpoint_overlap < args.hint_q2_near_min_endpoint_overlap:
                        continue
                    if cycle_position is not None:
                        pa = cycle_position[a.lower_idx]
                        pb = cycle_position[b.lower_idx]
                        distance = min(
                            (pa - pb) % len(selected),
                            (pb - pa) % len(selected),
                        )
                        if distance > args.hint_q2_near_max_cycle_distance:
                            continue
                    allowed.append(literal)
                if not allowed:
                    parser.error(
                        f"upper-q2 target {representative} has no compatible "
                        "one-flip witness around the hint"
                    )
                instance.cnf.add(*allowed)
                near_q2_report.append(
                    {
                        "target": representative,
                        "side": args.hint_q2_near_side,
                        "compatible_one_flip_witnesses": len(allowed),
                        "incompatible_same_lower": incompatible,
                        "max_q1_delta": args.hint_q2_near_max_q1_delta,
                        "min_endpoint_overlap": (
                            args.hint_q2_near_min_endpoint_overlap
                        ),
                        "max_cycle_distance": (
                            args.hint_q2_near_max_cycle_distance
                        ),
                    }
                )

        components = instance.components(selected)
        if len(components) == 1:
            if args.residence <= 0:
                parser.error("connected hint LNS currently needs positive residence")
            hint_cycle, hint_voltage = instance.lift_middle_cycle(selected)
            if not hint_cycle:
                # A connected zero-voltage quotient is still a valuable LNS
                # seed.  Its single quotient cycle closes in one period; only
                # the final lift into one k-fold Hamilton cycle is missing.
                qvertices, qphases, _, hint_voltage = instance.traverse_cycle(selected)
                hint_cycle = [
                    rotate(instance.middle[v], phase, instance.k)
                    for v, phase in zip(qvertices, qphases)
                ]
            violations = instance.residence_violations(hint_cycle, args.residence)
            _, _, qedges, _ = instance.traverse_cycle(selected)
            qlen = len(qedges)
            center_residue = None
            center_position = None
            if args.lns_center_position is not None:
                center_position = args.lns_center_position % qlen
                violations = [(center_position, 3)]
            elif args.lns_center_residue is not None:
                defect_residues = sorted({position % qlen for position, _ in violations})
                center_residue = args.lns_center_residue % qlen
                if center_residue not in defect_residues:
                    parser.error(
                        f"--lns-center-residue must be one of {defect_residues}"
                    )
                violations = [
                    item for item in violations if item[0] % qlen == center_residue
                ]
            bad_positions = set()
            for position, distance in violations:
                for offset in range(distance + 1):
                    bad_positions.add((position + offset) % qlen)
            if not bad_positions:
                parser.error("hint already has no requested residence violations")

            def cyclic_distance(position: int) -> int:
                return min(
                    min((position - bad) % qlen, (bad - position) % qlen)
                    for bad in bad_positions
                )

            ordered_positions = sorted(
                range(qlen), key=lambda p: (cyclic_distance(p), p)
            )
            free_positions = set(ordered_positions[: min(args.lns_free, qlen)])
            free_lower = {selected[qedges[p]].lower_idx for p in free_positions}
            free_lower.update(args.lns_include_lower_index)
            lns_report = {
                "hint": str(args.hint_certificate),
                "mode": "residence",
                "hint_residence_violations": len(violations),
                "quotient_bad_positions": len(bad_positions),
                "free_lower_orbits": len(free_lower),
                "fixed_lower_orbits": len(instance.lower) - len(free_lower),
                "max_free_distance": max(
                    (cyclic_distance(p) for p in free_positions), default=0
                ),
                "center_residue": center_residue,
                "center_position": center_position,
            }
        else:
            # Break an H-equivariant seed asymmetrically while preserving the
            # base translation quotient.  Free selected lower colours whose
            # alternative sigma choices cross the most current components.
            component_of = {
                vertex: ci for ci, component in enumerate(components) for vertex in component
            }
            choice_by_lower = {choice.lower_idx: choice for choice in selected}
            scored = []
            for lower_idx, current in choice_by_lower.items():
                current_component = component_of[current.endpoint[0]]
                crossing = 0
                touched = set()
                for var in instance.by_lower[lower_idx]:
                    alternative = instance.choice_by_var[var]
                    a = component_of[alternative.endpoint[0]]
                    b = component_of[alternative.endpoint[1]]
                    if a != b:
                        crossing += 1
                        touched.update((a, b))
                scored.append((crossing, len(touched), lower_idx, current_component))
            # First expose the best edge from every component, then fill the
            # remaining budget globally by cross-component option count.
            ordered = []
            for component_id in range(len(components)):
                local = [x for x in scored if x[3] == component_id]
                if local:
                    ordered.append(max(local))
            used = {x[2] for x in ordered}
            ordered.extend(
                x for x in sorted(scored, reverse=True) if x[2] not in used
            )
            defect_lower: set[int] = set()
            defect_windows = 0
            if args.lns_defect_aware:
                if args.residence <= 0:
                    parser.error("--lns-defect-aware requires positive --residence")
                # Traverse every current component separately.  A physical
                # zero-voltage quotient seed expands into translated cycles;
                # the generic component-break score sees only possible joins
                # and can freeze all actual residence repairs.  Put the lower
                # choices on every bad path window into the free set first.
                adjacency: list[list[tuple[int, int, int]]] = [
                    [] for _ in instance.middle
                ]
                for edge_id, choice in enumerate(selected):
                    u, v = choice.endpoint
                    adjacency[u].append((v, edge_id, choice.voltage))
                    adjacency[v].append(
                        (
                            u,
                            edge_id,
                            (-choice.voltage) % instance.k
                            if instance.equivariant
                            else 0,
                        )
                    )
                for component in components:
                    start = min(component)
                    current = start
                    previous_edge = -1
                    phase = 0
                    vertices = []
                    phases = []
                    edge_order = []
                    for _ in range(len(component)):
                        vertices.append(current)
                        phases.append(phase)
                        options = [
                            item
                            for item in adjacency[current]
                            if item[1] != previous_edge
                        ]
                        if not options:
                            raise AssertionError("component traversal stuck")
                        nxt, edge_id, delta = options[0]
                        edge_order.append(edge_id)
                        phase = (
                            (phase + delta) % instance.k
                            if instance.equivariant
                            else 0
                        )
                        previous_edge = edge_id
                        current = nxt
                    if current != start or len(set(edge_order)) != len(component):
                        raise AssertionError("failed to traverse hint component")
                    # A nonzero-voltage quotient component does not close
                    # after one quotient lap: it lifts to k/gcd(k,v) laps.
                    # Expand those laps before asking the physical Johnson-
                    # cycle residence checker.  (The old one-lap code raised
                    # "lift is not a Johnson cycle" on precisely the useful
                    # disconnected exact-shadow models.)
                    component_voltage = phase % instance.k if instance.equivariant else 0
                    repeats = (
                        instance.k // math.gcd(instance.k, component_voltage)
                        if instance.equivariant and component_voltage
                        else 1
                    )
                    lifted_vertices = []
                    lifted_phases = []
                    lifted_edges = []
                    for lap in range(repeats):
                        shift = (lap * component_voltage) % instance.k
                        lifted_vertices.extend(vertices)
                        lifted_phases.extend(
                            (p + shift) % instance.k for p in phases
                        )
                        lifted_edges.extend(edge_order)
                    cycle = [
                        rotate(instance.middle[v], p, instance.k)
                        for v, p in zip(lifted_vertices, lifted_phases)
                    ]
                    violations = instance.residence_violations(
                        cycle, args.residence
                    )
                    defect_windows += len(violations)
                    for position, distance in violations:
                        for offset in range(distance + 1):
                            edge_id = lifted_edges[
                                (position + offset) % len(lifted_edges)
                            ]
                            defect_lower.add(selected[edge_id].lower_idx)

            # Preserve all defect-window variables when the requested budget
            # permits it, then expose high-scoring joins.  If the window set is
            # larger than the budget, deterministic lower-index order keeps
            # runs reproducible; the report makes the truncation explicit.
            free_order = sorted(defect_lower)
            free_seen = set(free_order)
            free_order.extend(x[2] for x in ordered if x[2] not in free_seen)
            free_lower = set(
                free_order[: min(args.lns_free, len(instance.lower))]
            )
            free_lower.update(args.lns_include_lower_index)
            lns_report = {
                "hint": str(args.hint_certificate),
                "mode": (
                    "defect_aware_component_break"
                    if args.lns_defect_aware
                    else "component_break"
                ),
                "hint_components": sorted(map(len, components), reverse=True),
                "hint_component_count": len(components),
                "hint_residence_defect_windows": defect_windows,
                "defect_window_lower_orbits": len(defect_lower),
                "defect_window_lower_orbits_freed": len(defect_lower & free_lower),
                "free_lower_orbits": len(free_lower),
                "fixed_lower_orbits": len(instance.lower) - len(free_lower),
                "total_crossing_alternatives": sum(
                    x[0] for x in scored if x[2] in free_lower
                ),
            }
        fixed_choices = [
            choice for choice in selected if choice.lower_idx not in free_lower
        ]
        if args.lns_extra_changes:
            # Exactly one option is selected at every lower orbit.  Thus
            # ``-choice.var`` is an exact indicator that this otherwise-fixed
            # hint choice changed.  A single cardinality constraint searches
            # all sparse nonlocal helpers without enumerating one CNF per
            # possible helper orbit.
            instance.cnf.at_most_k(
                [-choice.var for choice in fixed_choices],
                args.lns_extra_changes,
            )
            lns_report["extra_changes"] = args.lns_extra_changes
            lns_report["extra_change_candidates"] = len(fixed_choices)
        else:
            for choice in fixed_choices:
                instance.cnf.add(choice.var)
        if near_q2_report:
            lns_report["near_q2_targets"] = near_q2_report
        if args.hint_preserve_covered_upper_q1:
            lns_report["preserved_upper_q1_orbits"] = preserved_upper_q1
        if args.block_hint:
            instance.cnf.add(*[-choice.var for choice in selected])
    for block_path in args.block_certificate:
        blocked = json.loads(block_path.read_text())
        blocked_keys = {
            (item["lower"], tuple(sorted(item["add"])))
            for item in blocked.get("selected_options", [])
        }
        blocked_choices = [
            choice
            for choice in instance.choices
            if (choice.lower, tuple(sorted((choice.add_a, choice.add_b))))
            in blocked_keys
        ]
        if len(blocked_choices) != len(instance.lower):
            parser.error(f"could not decode all choices from --block-certificate {block_path}")
        instance.cnf.add(*[-choice.var for choice in blocked_choices])
    parallel_flexible_vars = []
    if args.parallel_min is not None:
        for lower_idx in range(len(instance.lower)):
            endpoint_groups = {}
            for variable in instance.by_lower[lower_idx]:
                choice = instance.choice_by_var[variable]
                endpoint_groups.setdefault(tuple(sorted(choice.endpoint)), []).append(variable)
            for group in endpoint_groups.values():
                if len(group) > 1:
                    parallel_flexible_vars.extend(group)
        if args.parallel_min < 0:
            parser.error("--parallel-min must be nonnegative")
        if args.parallel_min > len(parallel_flexible_vars):
            parser.error("--parallel-min exceeds the flexible choice catalogue")
        instance.cnf.at_most_k(
            [-variable for variable in parallel_flexible_vars],
            len(parallel_flexible_vars) - args.parallel_min,
        )
    for orbit_mask in args.lower_q2_min2_orbit:
        representative, _ = canonical(orbit_mask, args.k, equivariant)
        if representative not in instance.lower2_index:
            parser.error(
                f"--lower-q2-min2-orbit {orbit_mask} is not a lower-q2 target"
            )
        witnesses = instance.lower_q2_witnesses[
            instance.lower2_index[representative]
        ]
        if len(witnesses) < 2:
            parser.error(
                f"lower-q2 orbit {representative} has fewer than two catalogue witnesses"
            )
        instance.cnf.at_most_k(
            [-literal for literal in witnesses], len(witnesses) - 2
        )
    for lower, add_a, add_b in args.force_choice:
        forced = [
            choice
            for choice in instance.choices
            if choice.lower == lower and {choice.add_a, choice.add_b} == {add_a, add_b}
        ]
        if len(forced) != 1:
            parser.error(f"--force-choice did not identify one choice: {lower} {add_a} {add_b}")
        instance.cnf.add(forced[0].var)
    if args.gap_min is not None or args.gap_max is not None:
        for gap in range(1, (args.k - 1) // 2 + 1):
            group = []
            for lower_idx in range(len(instance.lower)):
                local = [
                    var
                    for var in instance.by_lower[lower_idx]
                    if min(
                        (
                            instance.choice_by_var[var].add_a
                            - instance.choice_by_var[var].add_b
                        )
                        % args.k,
                        (
                            instance.choice_by_var[var].add_b
                            - instance.choice_by_var[var].add_a
                        )
                        % args.k,
                    )
                    == gap
                ]
                indicator = instance.cnf.var()
                for var in local:
                    instance.cnf.add(-var, indicator)
                instance.cnf.add(-indicator, *local)
                group.append(indicator)
            if args.gap_max is not None:
                instance.cnf.at_most_k(group, args.gap_max)
            if args.gap_min is not None:
                instance.cnf.at_most_k([-var for var in group], len(group) - args.gap_min)
    print(
        json.dumps(
            {
                "k": args.k,
                "equivariant": equivariant,
                "lower": len(instance.lower),
                "middle": len(instance.middle),
                "upper": len(instance.upper),
                "choices": len(instance.choices),
                "variables": instance.cnf.nvars,
                "clauses": len(instance.cnf.clauses),
                "cap2": not args.no_cap2,
                "q2": args.q2,
                "upper_q1_targets": args.upper_q1_target,
                "upper_q2_targets": args.upper_q2_target,
                "upper_q1_hole_budget": args.upper_q1_hole_budget,
                "upper_q2_hole_budget": args.upper_q2_hole_budget,
                "lower_q2": args.lower_q2,
                "lower_q3": args.lower_q3,
                "residence_clause_counts": instance.residence_clause_counts,
                "direct_connectivity": args.direct_connectivity,
                "compact_connectivity": args.compact_connectivity,
                "oriented_lazy_connectivity": args.oriented_lazy_connectivity,
                "automaton_residence": args.automaton_residence,
                "automaton_lower_q3": args.automaton_lower_q3,
                "residence_budget": args.residence_budget,
                "automaton_coresidence": args.automaton_coresidence,
                "automaton_upper_q3": args.automaton_upper_q3,
                "automaton_compiler": getattr(instance, "compiler_report", None),
                "lns": lns_report,
                "parallel_min": args.parallel_min,
                "parallel_flexible_choice_count": len(parallel_flexible_vars),
                "lower_q2_min2_orbits": args.lower_q2_min2_orbit,
                "compiler_target_masks": args.compiler_target_mask,
                "compiler_d2_budget": args.compiler_d2_budget,
            },
            sort_keys=True,
        ),
        flush=True,
    )

    if args.build_only:
        instance.cnf.write(cnf_path)
        print(f"wrote {cnf_path}", flush=True)
        return 0

    total_started = time.time()
    for round_no in range(args.max_rounds):
        status, model, elapsed, code = solve_once(
            instance.cnf,
            cnf_path,
            out_path,
            seed=args.seed + round_no,
            limit=args.time_per_round,
            walk_initially=args.kissat_walkinitially,
        )
        print(
            f"round={round_no} status={status} seconds={elapsed:.3f} "
            f"vars={instance.cnf.nvars} clauses={len(instance.cnf.clauses)}",
            flush=True,
        )
        if status != "SAT":
            result = {
                "status": status,
                "returncode": code,
                "round": round_no,
                "elapsed_total": time.time() - total_started,
                "lns": lns_report,
                "variables": instance.cnf.nvars,
                "clauses": len(instance.cnf.clauses),
            }
            cert_path.write_text(json.dumps(result, indent=2), encoding="utf-8")
            return 20 if status == "UNSAT" else 1

        selected = instance.selected_choices(model)
        components = instance.components(selected)
        if len(components) > 1:
            # Preserve every feasible disconnected round before the next
            # solver call overwrites ``out_path``.  These models are valuable
            # LNS seeds and make a lazy-connectivity frontier reproducible.
            round_stem = prefix.parent / f"{prefix.name}.round{round_no}"
            Path(f"{round_stem}.sat.out").write_text(
                out_path.read_text(encoding="utf-8", errors="replace"),
                encoding="utf-8",
            )
            Path(f"{round_stem}.disconnected.json").write_text(
                json.dumps(
                    {
                        "status": "SAT_DISCONNECTED",
                        "k": args.k,
                        "round": round_no,
                        "components": [sorted(component) for component in components],
                        "component_sizes": list(map(len, components)),
                        "selected_options": [
                            {
                                "lower": choice.lower,
                                "add": [choice.add_a, choice.add_b],
                                "upper": choice.upper,
                                "endpoints": list(choice.endpoint),
                                "voltage": choice.voltage,
                            }
                            for choice in selected
                        ],
                    },
                    indent=2,
                ),
                encoding="utf-8",
            )
            added = instance.add_component_cuts(components)
            print(f"  subtours={list(map(len, components))} cuts_added={added}", flush=True)
            continue

        cycle, voltage = instance.lift_middle_cycle(selected)
        if instance.equivariant and voltage == 0:
            instance.add_zero_voltage_block(selected)
            print("  connected quotient has voltage zero; exact assignment blocked", flush=True)
            continue

        report = instance.verify(selected, args.residence)
        if (
            args.residence
            and not args.direct_residence
            and not args.automaton_residence
            and report.get("residence_violations", 0)
        ):
            bad = instance.residence_violations(cycle, args.residence)
            # Preserve connected exact-shadow models before adding lazy
            # residence cuts.  These near misses are valuable diagnostics for
            # native bridge searches; without this snapshot the next solver
            # round overwrites the only model containing their changed lower
            # choices.
            round_stem = prefix.parent / f"{prefix.name}.round{round_no}"
            Path(f"{round_stem}.sat.out").write_text(
                out_path.read_text(encoding="utf-8", errors="replace"),
                encoding="utf-8",
            )
            Path(f"{round_stem}.residence.json").write_text(
                json.dumps(
                    {
                        "status": "SAT_RESIDENCE_DEFECT",
                        "k": args.k,
                        "round": round_no,
                        "voltage": voltage,
                        "residence_violations": len(bad),
                        "residence_examples": bad[:100],
                        "selected_options": [
                            {
                                "lower": choice.lower,
                                "add": [choice.add_a, choice.add_b],
                                "upper": choice.upper,
                                "endpoints": list(choice.endpoint),
                                "voltage": choice.voltage,
                            }
                            for choice in selected
                        ],
                    },
                    indent=2,
                ),
                encoding="utf-8",
            )
            cuts = instance.selected_path_vars_for_lift_indices(selected, bad)
            for clause in cuts:
                instance.cnf.add(*clause)
            print(
                f"  residence_violations={len(bad)} local_cuts_added={len(cuts)}",
                flush=True,
            )
            continue

        report.update(
            {
                "status": "SAT",
                "k": args.k,
                "r": instance.r,
                "equivariant": equivariant,
                "cap2": not args.no_cap2,
                "q2_encoded": args.q2,
                "lower_q2_encoded": args.lower_q2,
                "lower_q2_targets_encoded": sorted(
                    {canonical(x, args.k, equivariant)[0] for x in args.lower_q2_target}
                ),
                "automaton_compiler": getattr(instance, "compiler_report", None),
                "round": round_no,
                "variables": instance.cnf.nvars,
                "clauses": len(instance.cnf.clauses),
                "base_clauses": instance.base_clause_count,
                "elapsed_total": time.time() - total_started,
                "lns": lns_report,
                "selected_options": [
                    {
                        "lower": choice.lower,
                        "add": [choice.add_a, choice.add_b],
                        "upper": choice.upper,
                        "endpoints": list(choice.endpoint),
                        "voltage": choice.voltage,
                    }
                    for choice in selected
                ],
                "middle_cycle": cycle,
            }
        )
        if getattr(instance, "compiler_depth", 0):
            outgoing = {}
            for arc, u, v, delta in instance.directed_arcs:
                if arc in model:
                    if u in outgoing:
                        raise AssertionError("multiple selected directed compiler arcs")
                    outgoing[u] = (v, delta)
            if len(outgoing) != len(instance.middle):
                raise AssertionError("missing selected directed compiler arc")
            qvertices = []
            qphases = []
            current = 0
            phase = 0
            for _ in range(len(instance.middle)):
                qvertices.append(current)
                qphases.append(phase)
                current, delta = outgoing[current]
                phase = (phase + delta) % instance.k
            if current != 0:
                raise AssertionError("directed compiler traversal is not one cycle")
            directed_voltage = phase
            canonical_entries = []
            for local in instance.compiler_entry_vars:
                value = sum(1 << x for x, variable in local.items() if variable in model)
                if not value:
                    raise AssertionError("decoded compiler entry is empty")
                canonical_entries.append(value)
            compiler_word = []
            compiler_middle = []
            offset = 0
            for _ in range(instance.k):
                for vertex, local_phase in zip(qvertices, qphases):
                    compiler_word.append(
                        rotate(canonical_entries[vertex], local_phase + offset, instance.k)
                    )
                    compiler_middle.append(
                        rotate(instance.middle[vertex], local_phase + offset, instance.k)
                    )
                offset = (offset + directed_voltage) % instance.k
            for i, target in enumerate(compiler_middle):
                value = 0
                for age in range(instance.compiler_depth + 1):
                    value |= compiler_word[(i - age) % len(compiler_word)]
                if value != target:
                    raise AssertionError("decoded compiler word does not reconstruct middle")
            d2_rank_histogram = Counter()
            for i in range(len(compiler_word)):
                d2_value = (
                    compiler_word[i]
                    | compiler_word[(i - 1) % len(compiler_word)]
                    | compiler_word[(i - 2) % len(compiler_word)]
                )
                d2_rank_histogram[d2_value.bit_count()] += 1
            d2_actual_bad_vertices = sorted(
                {
                    qvertices[i]
                    for i in range(len(qvertices))
                    if (
                        compiler_word[i]
                        | compiler_word[(i - 1) % len(compiler_word)]
                        | compiler_word[(i - 2) % len(compiler_word)]
                    ).bit_count()
                    < instance.r - 1
                }
            )
            lower_seen = set()
            for row_depth in range(instance.compiler_depth):
                for i in range(len(compiler_word)):
                    value = 0
                    for age in range(row_depth + 1):
                        value |= compiler_word[(i - age) % len(compiler_word)]
                    lower_seen.add(value)
            reported_lower = {
                value
                for value in range(1, 1 << instance.k)
                if (
                    value.bit_count() in set(instance.compiler_report["target_ranks"])
                    or canonical(value, instance.k, True)[0]
                    in set(instance.compiler_report.get("target_masks", []))
                )
            }
            expected_lower = reported_lower
            if instance.compiler_report.get("d2_budget"):
                expected_lower = {
                    value
                    for value in expected_lower
                    if value.bit_count() != instance.r - 1
                }
            if not expected_lower <= lower_seen:
                raise AssertionError(
                    f"decoded compiler misses {len(expected_lower - lower_seen)} lower masks"
                )
            report.update(
                {
                    "compiler_directed_voltage": directed_voltage,
                    "compiler_cyclic_entries": compiler_word,
                    "compiler_middle_cycle_oriented": compiler_middle,
                    "compiler_lower_seen": len(reported_lower & lower_seen),
                    "compiler_lower_target": len(reported_lower),
                    "compiler_d2_bad_selected": sum(
                        variable in model
                        for variable in getattr(instance, "compiler_d2_bad_vars", [])
                    ),
                    "compiler_d2_bad_vertices": [
                        vertex
                        for vertex, variable in enumerate(
                            getattr(instance, "compiler_d2_bad_vars", [])
                        )
                        if variable in model
                    ],
                    "compiler_d2_actual_bad_vertices": d2_actual_bad_vertices,
                    "compiler_d2_rank_histogram": dict(d2_rank_histogram),
                }
            )
        cert_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
        print(json.dumps(report, sort_keys=True), flush=True)
        return 0

    cert_path.write_text(
        json.dumps(
            {
                "status": "ROUND_LIMIT",
                "rounds": args.max_rounds,
                "elapsed_total": time.time() - total_started,
                "lns": lns_report,
                "variables": instance.cnf.nvars,
                "clauses": len(instance.cnf.clauses),
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
