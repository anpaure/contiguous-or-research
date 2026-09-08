#!/usr/bin/env python3
"""Census the maximal source deck of the full rigid PBBS C6 orbit.

Substantial instances belong on h100, not on the local Mac.  The script
builds the directed standard/complement-GK PBBS owner 2-factor on rank
m+1 of [2m+1], applies every rotated rigid C6 switch in its literal
orientation, forms the maximal depth-d antecedent, and counts the source
interval values at widths 1,...,d.  It also audits the reverse orientation
of every terminal component and reports the union of the two decks.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import time
from collections import Counter, defaultdict


def masks(n: int, rank: int):
    for cc in itertools.combinations(range(n), rank):
        z = 0
        for i in cc:
            z |= 1 << i
        yield z


def unmatched_linear(word: int, n: int):
    stack = []
    free_ones = []
    for i in range(n):
        if (word >> i) & 1:
            if stack:
                stack.pop()
            else:
                free_ones.append(i)
        else:
            stack.append(i)
    return free_ones, stack


def gk_up(word: int, n: int) -> int:
    return word | (1 << unmatched_linear(word, n)[1][0])


def gk_down(word: int, n: int) -> int:
    return word ^ (1 << unmatched_linear(word, n)[0][-1])


def complement_up(word: int, n: int) -> int:
    full = (1 << n) - 1
    return full ^ gk_down(full ^ word, n)


def pbbs_inverse(word: int, n: int) -> int:
    """The inverse cyclic-parenthesis/PBBS map on rank-(n-1)/2 sets."""
    full = (1 << n) - 1
    return full ^ complement_up(word, n)


def rotate(mask: int, shift: int, n: int) -> int:
    shift %= n
    full = (1 << n) - 1
    return ((mask << shift) | (mask >> (n - shift))) & full


def rank_deadline(n: int) -> int:
    r = (n + 1) // 2
    w = math.comb(n, r)
    lower = sum(math.comb(n, s) for s in range(1, r))
    d = 0
    while d * w + d * (d + 1) // 2 < lower:
        d += 1
    return d


def canonical_successor(m: int):
    n = 2 * m + 1
    succ = {}
    for owner in masks(n, m):
        head = pbbs_inverse(pbbs_inverse(owner, n), n)
        if (owner ^ head).bit_count() != 2:
            raise AssertionError((owner, head))
        succ[owner] = head
    if len(set(succ.values())) != len(succ):
        raise AssertionError("PBBS successor is not a permutation")
    return succ


def rigid_terminal_successor(m: int):
    n = 2 * m + 1
    succ = canonical_successor(m)
    K = sum(1 << x for x in range(1, m - 1))
    active = (m - 1, m, m + 1)
    P = [K | (1 << active[i]) | (1 << active[(i + 1) % 3])
         for i in range(3)]
    Q = [K | (1 << active[i]) | 1 for i in range(3)]
    touched = set()
    for t in range(n):
        for i in range(3):
            tail = rotate(P[i], t, n)
            old_head = rotate(Q[i], t, n)
            new_head = rotate(Q[(i + 1) % 3], t, n)
            if succ[tail] != old_head:
                raise AssertionError(("rigid old arc absent", t, i))
            succ[tail] = new_head
            touched.add(tail)
    if len(touched) != 3 * n or len(set(succ.values())) != len(succ):
        raise AssertionError((len(touched), len(set(succ.values())), len(succ)))
    # Complement to the rank-(m+1) physical owner chronology used by the
    # universal-word central row, retaining the literal direction.
    full = (1 << n) - 1
    physical_succ = {full ^ a: full ^ b for a, b in succ.items()}
    physical_touched = {full ^ a for a in touched}
    return physical_succ, physical_touched


def cycles_from_successor(succ):
    cycles = []
    seen = set()
    for start in succ:
        if start in seen:
            continue
        cyc = []
        cur = start
        while cur not in seen:
            seen.add(cur)
            cyc.append(cur)
            cur = succ[cur]
        if cur != start:
            raise AssertionError("component traversal failed")
        cycles.append(cyc)
    return cycles


def maximal_antecedent(cycle, d: int, full: int, verify=True):
    L = len(cycle)
    out = []
    for i in range(L):
        z = full
        for a in range(d + 1):
            z &= cycle[(i - a) % L]
        if z == 0:
            raise AssertionError(("empty maximal letter", i, L))
        out.append(z)
    # Verify D^d P equals the chosen orientation when residence is claimed.
    mismatches = 0
    for i in range(L):
        z = 0
        for a in range(d + 1):
            z |= out[(i + a) % L]
        if z != cycle[i]:
            mismatches += 1
            if verify:
                raise AssertionError(("antecedent derivative mismatch", i, L))
    return out, mismatches


def deck(cycles, d: int, full: int, R: int, verify=True,
         detailed=True, expected_min_rank=None):
    by_rank = [set() for _ in range(R)]
    occurrence_hist = Counter()
    width_rank_hist = Counter()
    letter_rank_hist = Counter()
    derivative_mismatches = 0
    for cyc in cycles:
        P, bad = maximal_antecedent(cyc, d, full, verify=verify)
        derivative_mismatches += bad
        letter_rank_hist.update(z.bit_count() for z in P)
        L = len(P)
        if detailed:
            for start in range(L):
                z = 0
                for width in range(1, d + 1):
                    z |= P[(start + width - 1) % L]
                    rank = z.bit_count()
                    width_rank_hist[(width, rank)] += 1
                    if 0 < rank < R:
                        by_rank[rank].add(z)
                        occurrence_hist[z] += 1
        else:
            if expected_min_rank is None:
                raise AssertionError("expected_min_rank required for light deck")
            min_seen = R
            deep_count = 0
            for start in range(L):
                z = 0
                for width in range(1, d + 1):
                    z |= P[(start + width - 1) % L]
                    rank = z.bit_count()
                    min_seen = min(min_seen, rank)
                    if rank < expected_min_rank:
                        deep_count += 1
                    width_rank_hist[(width, rank)] += 1
    return (by_rank, occurrence_hist, width_rank_hist, letter_rank_hist,
            derivative_mismatches)


def rank_rows(by_rank, n: int, R: int):
    out = {}
    for rank in range(1, R):
        total = math.comb(n, rank)
        covered = len(by_rank[rank])
        out[str(rank)] = {
            "covered": covered,
            "total": total,
            "missing": total - covered,
        }
    return out


def canonical_components(succ):
    return cycles_from_successor(succ)


def census(m: int):
    started = time.time()
    n = 2 * m + 1
    R = m + 1
    d = rank_deadline(n)
    full = (1 << n) - 1
    succ, touched = rigid_terminal_successor(m)
    cycles = cycles_from_successor(succ)
    sector_cycles = [cyc for cyc in cycles if any(x in touched for x in cyc)]
    if not sector_cycles or sum(any(x in touched for x in cyc) for cyc in cycles) != len(sector_cycles):
        raise AssertionError("sector extraction failed")
    (by_rank, occurrence_hist, width_rank_hist, letter_rank_hist,
     derivative_mismatches) = deck(cycles, d, full, R, verify=False)
    (sector_by_rank, sector_occurrence_hist, sector_width_rank_hist,
     sector_letter_rank_hist, sector_derivative_mismatches) = deck(
        sector_cycles, d, full, R, verify=True)
    reverse_cycles = [list(reversed(cyc)) for cyc in cycles]
    (rev_by_rank, _, _, rev_letter_rank_hist,
     reverse_derivative_mismatches) = deck(
        reverse_cycles, d, full, R, verify=False)
    either_by_rank = [a | b for a, b in zip(by_rank, rev_by_rank)]
    rows = rank_rows(by_rank, n, R)
    rev_rows = rank_rows(rev_by_rank, n, R)
    either_rows = rank_rows(either_by_rank, n, R)
    deep_cut = R - d
    if min(letter_rank_hist) < deep_cut or min(rev_letter_rank_hist) < deep_cut:
        raise AssertionError((letter_rank_hist, rev_letter_rank_hist, deep_cut))
    if set(sector_letter_rank_hist) != {deep_cut}:
        raise AssertionError((sector_letter_rank_hist, deep_cut))
    if any(by_rank[r] or rev_by_rank[r] or sector_by_rank[r]
           for r in range(1, deep_cut)):
        raise AssertionError("maximal deck unexpectedly reaches below its letter rank")
    bottom_missing = set(masks(n, R - 1)) - by_rank[R - 1]
    old_components = canonical_components(canonical_successor(m))
    missing_old_component_lengths = sorted(
        len(cyc) for cyc in old_components if set(cyc) <= bottom_missing)
    bottom_missing_rotation_invariant = all(
        rotate(x, 1, n) in bottom_missing for x in bottom_missing)
    return {
        "m": m,
        "n": n,
        "R": R,
        "d": d,
        "owners": math.comb(n, R),
        "terminal_components": len(cycles),
        "terminal_component_lengths": sorted(map(len, cycles)),
        "rigid_sector_components": len(sector_cycles),
        "rigid_sector_component_lengths": sorted(map(len, sector_cycles)),
        "maximal_letter_rank": deep_cut,
        "full_factor_letter_rank_hist": dict(sorted(letter_rank_hist.items())),
        "full_factor_derivative_mismatches": derivative_mismatches,
        "reverse_factor_derivative_mismatches": reverse_derivative_mismatches,
        "rank_rows_directed": rows,
        "rank_rows_reversed": rev_rows,
        "rank_rows_either_orientation": either_rows,
        "top_d_complete_directed": all(
            rows[str(r)]["missing"] == 0 for r in range(deep_cut, R)),
        "deep_values_directed": sum(len(by_rank[r]) for r in range(1, deep_cut)),
        "bottom_row_missing": len(bottom_missing),
        "bottom_missing_rotation_invariant": bottom_missing_rotation_invariant,
        "canonical_components_wholly_bottom_missing": missing_old_component_lengths,
        "rigid_sector_rank_rows": rank_rows(sector_by_rank, n, R),
        "rigid_sector_derivative_mismatches": sector_derivative_mismatches,
        "rigid_sector_distinct_lower_values": sum(len(x) for x in sector_by_rank),
        "rigid_sector_lower_occurrences": sum(sector_occurrence_hist.values()),
        "rigid_sector_width_rank_hist": {
            f"{w},{r}": c for (w, r), c in sorted(sector_width_rank_hist.items())},
        "distinct_lower_values": sum(len(x) for x in by_rank),
        "lower_occurrences": sum(occurrence_hist.values()),
        "multiplicity_hist": dict(sorted(Counter(occurrence_hist.values()).items())),
        "width_rank_hist": {f"{w},{r}": c for (w, r), c in sorted(width_rank_hist.items())},
        "seconds": time.time() - started,
    }


def sector_census(m: int):
    """Lightweight touched-sector audit, suitable for larger m."""
    started = time.time()
    n = 2 * m + 1
    R = m + 1
    d = rank_deadline(n)
    deep_cut = R - d
    full = (1 << n) - 1
    # Literal closed formulas for the touched terminal sector.  This avoids
    # enumerating the exponential ambient PBBS factor.
    def setmask(items):
        return sum(1 << (x % n) for x in items)

    def rotset(items, shift):
        return rotate(setmask(items), shift, n)

    def aa(j, root):
        return rotset(list(range(1, m)) + [m + j], root)

    def bb(j, root):
        return rotset(list(range(1, j + 1))
                      + list(range(j + 2, m + 2)), root)

    p0 = list(range(1, m + 1))
    braid = [rotset(p0, -h) if h % 2 == 0 else aa(1, -h)
             for h in range(2 * n)]
    residual = []
    seen = set()
    for seed in range(n):
        if seed in seen:
            continue
        cyc = []
        phase = seed
        while phase not in seen:
            seen.add(phase)
            cyc.append(bb(m - 2, phase))
            cyc.extend(aa(j, phase - j + 1) for j in range(2, m))
            cyc.extend(bb(j, phase - m - j) for j in range(1, m - 2))
            phase = (phase + 3) % n
        residual.append(cyc)
    # The closed rigid formulas are on the rank-m PBBS shore.  Complement
    # to the rank-(m+1) physical owner shore used by the universal word.
    sector_cycles = [[full ^ x for x in cyc] for cyc in [braid] + residual]
    for cyc in sector_cycles:
        if any((cyc[i] ^ cyc[(i + 1) % len(cyc)]).bit_count() != 2
               for i in range(len(cyc))):
            raise AssertionError("closed sector formula is not Johnson")
    (_, _, width_rank_hist, letter_rank_hist,
     derivative_mismatches) = deck(
        sector_cycles, d, full, R, verify=True, detailed=False,
        expected_min_rank=deep_cut)
    return {
        "m": m,
        "n": n,
        "R": R,
        "d": d,
        "maximal_letter_rank": deep_cut,
        "rigid_sector_components": len(sector_cycles),
        "rigid_sector_component_lengths": sorted(map(len, sector_cycles)),
        "rigid_sector_derivative_mismatches": derivative_mismatches,
        "rigid_sector_letter_rank_hist": dict(sorted(letter_rank_hist.items())),
        "rigid_sector_width_rank_hist": {
            f"{w},{r}": c for (w, r), c in sorted(width_rank_hist.items())},
        "deep_value_occurrences": sum(
            c for (w, r), c in width_rank_hist.items() if r < deep_cut),
        "seconds": time.time() - started,
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("m", type=int, nargs="+")
    ap.add_argument("--json")
    ap.add_argument("--sector-only", action="store_true")
    args = ap.parse_args()
    results = [(sector_census(m) if args.sector_only else census(m))
               for m in args.m]
    payload = json.dumps(results, indent=2, sort_keys=True)
    print(payload)
    if args.json:
        with open(args.json, "w", encoding="utf-8") as out:
            out.write(payload + "\n")


if __name__ == "__main__":
    main()
