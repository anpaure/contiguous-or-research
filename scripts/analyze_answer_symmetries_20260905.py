#!/usr/bin/env python3
"""Fresh, answer-only symmetry and cross-dimensional chronology checks.

Coordinates and positions are zero based. A symmetry (sign, shift, perm)
means perm(word[i]) == word[(shift + sign*i) % len(word)]. Approximation
minimizes differing incidence bits, not the number of differing masks.
Only numpy is needed, and only for the optional exhaustive FFT comparison.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from hashlib import sha256
from itertools import permutations, product
from math import comb
from pathlib import Path
import json
import re
import time


ROOT = Path(__file__).resolve().parents[1]


def columns(word, k):
    return [bytes((x >> b) & 1 for x in word) for b in range(k)]


def relabel(x, perm):
    result = 0
    while x:
        bit = x & -x
        result |= 1 << perm[bit.bit_length() - 1]
        x ^= bit
    return result


def cycles(perm):
    seen, result = set(), []
    for start in range(len(perm)):
        if start in seen:
            continue
        cycle, b = [], start
        while b not in seen:
            seen.add(b)
            cycle.append(b)
            b = perm[b]
        if len(cycle) > 1:
            result.append(cycle)
    return result


def column_mapping(source, target):
    """One exact coordinate map, or None; repeated columns are allowed."""
    lookup = defaultdict(list)
    for b, col in enumerate(target):
        lookup[col].append(b)
    result = []
    for col in source:
        if not lookup[col]:
            return None
        result.append(lookup[col].pop())
    return result


def exact_equivalences(source, target, k, cyclic=True):
    if len(source) != len(target):
        return []
    n = len(source)
    if not n:
        return []
    left = columns(source, k)
    # An anchor-column match is necessary; byte-string search avoids n^2
    # pairwise mask comparisons. Every surviving candidate is checked exactly.
    anchor = max(left, key=lambda col: sum(a != b for a, b in zip(col, col[1:])))
    result = []
    for sign in (1, -1):
        right = columns(target if sign == 1 else target[::-1], k)
        offsets = {0}
        if cyclic:
            offsets = set()
            for col in right:
                doubled = col + col[:-1]
                position = doubled.find(anchor)
                while position >= 0:
                    offsets.add(position)
                    position = doubled.find(anchor, position + 1)
        for offset in sorted(offsets):
            perm = column_mapping(left, [col[offset:] + col[:offset] for col in right])
            if perm is not None:
                shift = offset if sign == 1 else n - 1 - offset
                assert all(relabel(x, perm) == target[(shift + sign * i) % n]
                           for i, x in enumerate(source))
                result.append({"sign": sign, "shift": shift, "perm": perm,
                               "cycles": cycles(perm)})
    return result


def extract_middle(word, k):
    """First occurrences of middle ORs, ordered by their right endpoints."""
    seen, middle, previous = set(), [], []
    rank = (k + 1) // 2
    for x in word:
        current = [x]
        for value in previous:
            value |= x
            if value != current[-1]:
                current.append(value)
        for value in current:
            if value not in seen and value.bit_count() == rank:
                middle.append(value)
            seen.add(value)
        previous = current
    assert len(seen) == (1 << k) - 1, (k, "not universal")
    assert len(middle) == comb(k, rank)
    # Independent moving-window extraction: stop at the first middle-rank
    # endpoint for each start. This is also O(k*n), without witness profiles.
    counts, mask, right, independent, used = [0] * k, 0, 0, [], set()
    for x in word:
        while right < len(word) and mask.bit_count() < rank:
            value = word[right]
            while value:
                bit = value & -value
                counts[bit.bit_length() - 1] += 1
                mask |= bit
                value ^= bit
            right += 1
        if mask.bit_count() == rank and mask not in used:
            independent.append(mask)
            used.add(mask)
        while x:
            bit = x & -x
            counts[bit.bit_length() - 1] -= 1
            if not counts[bit.bit_length() - 1]:
                mask ^= bit
            x ^= bit
    assert middle == independent
    return middle


def assignment(cost):
    """Integer Hungarian algorithm; at most 16 coordinates in this audit."""
    n = len(cost)
    u, v, p, way = [0] * (n + 1), [0] * (n + 1), [0] * (n + 1), [0] * (n + 1)
    for i in range(1, n + 1):
        p[0] = i
        j0 = 0
        minimum, used = [10**30] * (n + 1), [False] * (n + 1)
        while True:
            used[j0] = True
            i0, delta, j1 = p[j0], 10**30, 0
            row = cost[i0 - 1]
            for j in range(1, n + 1):
                if not used[j]:
                    value = row[j - 1] - u[i0] - v[j]
                    if value < minimum[j]:
                        minimum[j], way[j] = value, j0
                    if minimum[j] < delta:
                        delta, j1 = minimum[j], j
            for j in range(n + 1):
                if used[j]:
                    u[p[j]] += delta
                    v[j] -= delta
                else:
                    minimum[j] -= delta
            j0 = j1
            if not p[j0]:
                break
        while j0:
            j1 = way[j0]
            p[j0] = p[j1]
            j0 = j1
    perm = [0] * n
    for j in range(1, n + 1):
        perm[p[j] - 1] = j - 1
    return -v[0], perm


def approximate_symmetries(word, k):
    import numpy as np

    n = len(word)
    x = np.array([list(col) for col in columns(word, k)], dtype=np.float64)
    xf = np.fft.rfft(x, axis=1)
    totals = x.sum(axis=1).astype(np.int32)
    result = {}
    for sign in (1, -1):
        yf = xf if sign == 1 else np.fft.rfft(x[:, ::-1], axis=1)
        costs = np.empty((n, k, k), dtype=np.int32)
        for b in range(k):
            raw = np.fft.irfft(xf.conj() * yf[b], n=n, axis=1)
            rounded = np.rint(raw)
            assert np.max(np.abs(raw - rounded)) < 1e-6
            costs[:, :, b] = (totals[:, None] + totals[b] - 2 * rounded).T
        best = None
        best_nonidentity = None
        linear = None
        for offset in range(n):
            if sign == 1 and offset == 0:
                continue
            value, perm = assignment(costs[offset].tolist())
            shift = offset if sign == 1 else n - 1 - offset
            candidate = (value, shift, perm)
            if sign == -1 and offset == 0:
                linear = candidate
            if best is None or candidate[:2] < best[:2]:
                best = candidate
            if perm != list(range(k)) and (
                best_nonidentity is None or candidate[:2] < best_nonidentity[:2]
            ):
                best_nonidentity = candidate
        reports = {}
        comparisons = [("best", best), ("best_with_nonidentity_optimal_map", best_nonidentity)]
        if sign == -1:
            comparisons.append(("linear_reversal", linear))
        for name, found in comparisons:
            if found is None:
                reports[name] = None
                continue
            value, shift, perm = found
            mismatches = [i for i, a in enumerate(word)
                          if relabel(a, perm) != word[(shift + sign * i) % n]]
            direct = sum((relabel(a, perm) ^ word[(shift + sign * i) % n]).bit_count()
                         for i, a in enumerate(word))
            assert direct == value
            reports[name] = {"sign": sign, "shift": shift, "perm": perm,
                             "cycles": cycles(perm), "bit_errors": value,
                             "mask_errors": len(mismatches),
                             "mismatch_positions_first20": mismatches[:20]}
            flags = runs([relabel(a, perm) != word[(shift + sign * i) % n]
                          for i, a in enumerate(word)])
            if len(flags) <= 16:
                reports[name]["mismatch_runs"] = flags
        result["rotation" if sign == 1 else "reflection"] = reports
    return result


def delete_coordinate(x, b):
    return (x & ((1 << b) - 1)) | ((x >> (b + 1)) << b)


def longest_prefix(source, target, lower_k, pin):
    """Inject old coordinates, with the extra coordinate constantly pin."""
    size = min(len(source), len(target))
    a = columns(source[:size], lower_k) + [bytes([pin]) * size]
    b = columns(target[:size], lower_k + 1)
    lo, hi = 0, size + 1
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if Counter(col[:mid] for col in a) == Counter(col[:mid] for col in b):
            lo = mid
        else:
            hi = mid
    perm = column_mapping([col[:lo] for col in a], [col[:lo] for col in b])
    assert perm is not None
    for i in range(lo):
        assert relabel(source[i] | (pin << lower_k), perm) == target[i]
    return {"length": lo, "perm": perm, "pin": pin}


def prefix_inheritance(source, target, lower_k):
    result = []
    for reverse_source, reverse_target, pin in product((False, True), repeat=3):
        report = longest_prefix(source[::-1] if reverse_source else source,
                                target[::-1] if reverse_target else target,
                                lower_k, int(pin))
        report.update(reverse_source=reverse_source, reverse_target=reverse_target)
        result.append(report)
    return sorted(result, key=lambda row: -row["length"])


def segment_embeddings(source, target, k):
    """All full contiguous copies under relabeling and source reversal."""
    length = len(source)
    target_cols = columns(target, k)
    result = []
    for reverse in (False, True):
        oriented = source[::-1] if reverse else source
        source_cols = columns(oriented, k)
        anchor = max(source_cols, key=lambda col: sum(a != b for a, b in zip(col, col[1:])))
        starts = set()
        for col in target_cols:
            start = col.find(anchor)
            while start >= 0:
                starts.add(start)
                start = col.find(anchor, start + 1)
        for start in sorted(starts):
            perm = column_mapping(source_cols, [col[start:start + length] for col in target_cols])
            if perm is not None:
                assert [relabel(x, perm) for x in oriented] == target[start:start + length]
                result.append({"start": start, "reverse": reverse, "perm": perm})
    return result


def runs(values):
    result = []
    for value in values:
        if result and result[-1][0] == value:
            result[-1][1] += 1
        else:
            result.append([value, 1])
    return result


def developed_chunks(middle, best, k):
    if best is None or not best["cycles"] or best["mask_errors"] * 3 > len(middle):
        return []
    shift, perm = best["shift"], best["perm"]
    if shift > len(middle) // 2:
        return []
    matches = [relabel(middle[i], perm) == middle[i + shift]
               for i in range(len(middle) - shift)]
    position, boundaries = 0, {0, len(middle)}
    for value, length in runs(matches):
        if value and length >= 2 * shift:
            boundaries.update((position, position + length + shift))
        position += length
    if k > 5:
        for b in range(k):
            membership = runs([(x >> b) & 1 for x in middle])
            if len(membership) <= 4:
                position = 0
                for _, length in membership:
                    position += length
                    boundaries.add(position)
    boundaries = sorted(boundaries)
    result = []
    for start, end in zip(boundaries, boundaries[1:]):
        chunk = middle[start:end]
        syms = exact_equivalences(chunk, chunk, k)
        rotations = [s for s in syms if s["sign"] == 1 and s["shift"] > 0]
        first = min(rotations, key=lambda s: s["shift"]) if rotations else None
        result.append({"start": start, "end": end, "length": end - start,
                       "rotation_order": len(rotations) + 1, "generator": first,
                       "reflection_count": sum(s["sign"] == -1 for s in syms),
                       "cyclic_non_johnson_edges": sum((a ^ b).bit_count() != 2
                                                       for a, b in zip(chunk, chunk[1:] + chunk[:1]))})
    return result


def edge_lift_checks(lower, higher, lower_chunks, k):
    """Compare a visible lift section with cyclic edge intersections."""
    result = []
    for b in range(k):
        flags = [(x >> b) & 1 for x in higher]
        membership = runs(flags)
        if len(membership) > 8:
            continue
        position = 0
        for present, length in membership:
            if present:
                section = [delete_coordinate(x, b) for x in higher[position:position + length]]
                for chunk in lower_chunks:
                    if chunk["length"] != length:
                        continue
                    cycle = lower[chunk["start"]:chunk["end"]]
                    edges = [a & c for a, c in zip(cycle, cycle[1:] + cycle[:1])]
                    result.append({"coordinate": b, "higher_start": position, "length": length,
                                   "lower_start": chunk["start"],
                                   "edge_equivalences": exact_equivalences(edges, section, k - 1)})
            position += length
    return result


def reconstruct_two_cycle_lift(lower, higher, lower_chunks, sections):
    """Try a full finite identity, not an induction or a compiler theorem."""
    if len(lower_chunks) != 2:
        return []
    first = lower[lower_chunks[0]["start"]:lower_chunks[0]["end"]]
    second = lower[lower_chunks[1]["start"]:lower_chunks[1]["end"]]
    forward_edges = [a & b for a, b in zip(first, first[1:] + first[:1])]
    backward_edges = [a & b for a, b in zip(second, second[-1:] + second[:-1])]
    reports = []
    for section in sections:
        if section["present"]:
            continue
        b = section["coordinate"]
        for match in section["exact_lower_equivalences"]:
            if match["sign"] != 1 or match["shift"] != 0:
                continue
            injection = [j if j < b else j + 1 for j in match["perm"]]
            reconstructed = ([relabel(x, injection) | (1 << b) for x in forward_edges]
                             + [relabel(x, injection) for x in lower]
                             + [relabel(x, injection) | (1 << b) for x in backward_edges])
            reports.append({"coordinate": b, "injection": injection,
                            "first_cycle_size": len(first), "second_cycle_size": len(second),
                            "literal_equal": reconstructed == higher,
                            "first_edge_example": [first[0], first[1], first[0] & first[1], higher[0]]})
    return reports


def seed_lift_checks(lower, higher, lower_chunks, higher_chunks, k):
    """Same-parity seed inheritance with one new 1-column and one 0-column."""
    result = []
    for old in lower_chunks:
        if not old["generator"]:
            continue
        length = old["generator"]["shift"]
        seed = [x | (1 << (k - 2)) for x in lower[old["start"]:old["start"] + length]]
        for new in higher_chunks:
            if not new["generator"]:
                continue
            cycle = higher[new["start"]:new["end"]]
            if len(seed) > len(cycle):
                continue
            target_seed = cycle[:new["generator"]["shift"]]
            prefixes = prefix_inheritance(seed, target_seed, k - 1)
            result.append({"source_start": old["start"], "source_seed_size": length,
                           "target_start": new["start"], "target_seed_size": len(target_seed),
                           "best_seed_prefix": next(p for p in prefixes if p["pin"] == 0),
                           "cyclic_full_seed_embeddings": segment_embeddings(seed, cycle + cycle[:length - 1], k)})
    return result


def folded_anchor(section, lower, k, anchor_length=32):
    """Recover maps from a 32-mask anchor, then certify every piece exactly.

    This is an anchor-based search, not an exhaustive optimum over all
    possible piecewise foldings. Full-word equivalence is exhaustive above.
    """
    n = len(lower)
    length = min(anchor_length, n)
    source_cols = columns(section[:length], k)
    source_signatures = [int.from_bytes(col, "little") for col in source_cols]
    wanted = Counter(source_signatures)
    mask = (1 << (8 * length)) - 1
    lower_index = {x: i for i, x in enumerate(lower)}
    candidates = {}
    for sign in (1, -1):
        target = lower if sign == 1 else lower[::-1]
        doubled = target + target[:length - 1]
        cols = columns(doubled, k)
        signatures = [int.from_bytes(col[:length], "little") for col in cols]
        for start in range(n):
            if Counter(signatures) == wanted:
                source_groups, target_groups = defaultdict(list), defaultdict(list)
                for b, value in enumerate(source_signatures):
                    source_groups[value].append(b)
                for b, value in enumerate(signatures):
                    target_groups[value].append(b)
                possibilities = 1
                for group in source_groups.values():
                    for factor in range(2, len(group) + 1):
                        possibilities *= factor
                if possibilities <= 720:
                    keys = list(source_groups)
                    for choices in product(*(permutations(target_groups[value]) for value in keys)):
                        perm = [0] * k
                        for value, choice in zip(keys, choices):
                            for a, b in zip(source_groups[value], choice):
                                perm[a] = b
                        candidates[tuple(perm)] = perm
            if start + 1 < n:
                for b in range(k):
                    signatures[b] = ((signatures[b] >> 8) |
                                     (cols[b][start + length] << (8 * (length - 1)))) & mask
    best = None
    for perm in candidates.values():
        indices = [lower_index[relabel(x, perm)] for x in section]
        pieces, start = [], 0
        while start < n:
            end = start + 1
            direction = 0
            if end < n and abs(indices[end] - indices[start]) == 1:
                direction = indices[end] - indices[start]
                end += 1
                while end < n and indices[end] - indices[end - 1] == direction:
                    end += 1
            pieces.append({"section_start": start, "length": end - start,
                           "lower_start": indices[start], "lower_end": indices[end - 1],
                           "direction": direction})
            start = end
        report = {"pieces": pieces, "piece_count": len(pieces), "perm": perm,
                  "anchor_length": length, "candidate_maps": len(candidates)}
        if best is None or len(pieces) < best["piece_count"]:
            best = report
    return best


def chronology_sections(middle, lower, k):
    reports = []
    for b in range(k):
        flags = [(x >> b) & 1 for x in middle]
        section_types = (0, 1) if k % 2 == 0 else (1,)
        for present in section_types:
            section = [delete_coordinate(x, b) for x in middle if ((x >> b) & 1) == present]
            dual = k % 2 == 0 and present == 1
            if dual:
                section = [((1 << (k - 1)) - 1) ^ x for x in section]
            assert len(section) == len(lower)
            bad_edges = [i for i, (a, c) in enumerate(zip(section, section[1:]))
                         if (a ^ c).bit_count() != 2]
            exact = exact_equivalences(lower, section, k - 1)
            membership = runs(flags)
            components = [end - start for start, end in zip(
                [0] + [i + 1 for i in bad_edges], [i + 1 for i in bad_edges] + [len(section)])]
            reports.append({"coordinate": b, "present": present, "dual": dual,
                            "membership_run_count": len(membership),
                            "membership_runs": membership if len(membership) <= 32 else None,
                            "non_johnson_edges": len(bad_edges),
                            "johnson_component_lengths": components if len(components) <= 32 else None,
                            "exact_lower_equivalences": exact,
                            "anchor_fold": folded_anchor(section, lower, k - 1)})
    return reports


def developed_blocks(word, middle_symmetries, k):
    """Test raw linear inheritance of exact cyclic middle development."""
    result = []
    for sym in middle_symmetries:
        if sym["sign"] != 1 or sym["shift"] == 0:
            continue
        shift, perm = sym["shift"], sym["perm"]
        mismatches = [i for i in range(len(word) - shift)
                      if relabel(word[i], perm) != word[i + shift]]
        result.append({"shift": shift, "perm": perm, "cycles": cycles(perm),
                       "linear_comparisons": len(word) - shift,
                       "mask_errors": len(mismatches),
                       "mismatch_positions_first20": mismatches[:20]})
    return result


def self_test(use_fft=False):
    import random

    rng = random.Random(20260905)
    for k in range(1, 6):
        for _ in range(12):
            cost = [[rng.randrange(20) for _ in range(k)] for _ in range(k)]
            actual, perm = assignment(cost)
            expected = min(sum(cost[i][p[i]] for i in range(k)) for p in permutations(range(k)))
            assert actual == expected == sum(cost[i][perm[i]] for i in range(k))
    for k in range(1, 5):
        word = [1 << b for b in range(k)] + [rng.randrange(1, 1 << k) for _ in range(4)]
        actual = {(s["sign"], s["shift"], tuple(s["perm"]))
                  for s in exact_equivalences(word, word, k)}
        expected = {(sign, shift, perm) for sign in (1, -1) for shift in range(len(word))
                    for perm in permutations(range(k))
                    if all(relabel(x, perm) == word[(shift + sign * i) % len(word)]
                           for i, x in enumerate(word))}
        assert actual == expected
        if use_fft:
            approximate = approximate_symmetries(word, k)
            for sign, name in ((1, "rotation"), (-1, "reflection")):
                expected_cost = min(
                    sum((relabel(x, perm) ^ word[(shift + sign * i) % len(word)]).bit_count()
                        for i, x in enumerate(word))
                    for shift in range(len(word)) if sign == -1 or shift != 0
                    for perm in permutations(range(k)))
                assert approximate[name]["best"]["bit_errors"] == expected_cost


def summarize(reports):
    print("\nEXACT SYMMETRIES: k | word rotations; reflections | middle rotations; reflections")
    for row in reports:
        def show(items):
            return ([s["shift"] for s in items if s["sign"] == 1],
                    [s["shift"] for s in items if s["sign"] == -1])
        print(row["k"], show(row["word_symmetries"]), show(row["middle_symmetries"]))
    if "word_approximate" in reports[0]:
        for kind in ("word", "middle"):
            print(f"\nAPPROXIMATE {kind}: k | rotation (bits,masks,shift,cycles) | reflection likewise")
            for row in reports:
                values = []
                for orientation in ("rotation", "reflection"):
                    value = row[f"{kind}_approximate"][orientation]["best"]
                    values.append(None if value is None else (
                        value["bit_errors"], value["mask_errors"], value["shift"], value["cycles"]))
                print(row["k"], *values)
    print("\nDELETIONS: k | size-compatible coordinates | exact matches (coord,sign,shift,perm)")
    for previous, row in zip(reports, reports[1:]):
        deletions = row["coordinate_deletions"]
        compatible = [d["coordinate"] for d in deletions if d["filtered_size"] == previous["word_size"]]
        matches = [(d["coordinate"], s["sign"], s["shift"], s["perm"])
                   for d in deletions for s in d["matches"]]
        print(row["k"], compatible, matches)
    print("\nPREFIX/LIFT: k | best per pin (length, reverse_lower, reverse_higher, coordinate_map)")
    for row in reports[1:]:
        best = [next(p for p in row["word_prefix_inheritance"] if p["pin"] == pin) for pin in (0, 1)]
        print(row["k"], [(p["length"], p["reverse_source"], p["reverse_target"], p["perm"]) for p in best])
        print("  full raw embeddings", row["whole_lower_word_embeddings"])
        print("  middle max prefix", row["middle_prefix_inheritance"][0])
    print("\nMIDDLE SECTIONS: k | min membership runs (coord) | min components (coord,present)")
    for row in reports[1:]:
        sections = row["middle_sections"]
        minimum_runs = min(s["membership_run_count"] for s in sections)
        minimum_components = 1 + min(s["non_johnson_edges"] for s in sections)
        print(row["k"], minimum_runs,
              sorted({s["coordinate"] for s in sections if s["membership_run_count"] == minimum_runs}),
              minimum_components,
              [(s["coordinate"], s["present"]) for s in sections
               if s["non_johnson_edges"] + 1 == minimum_components])
        for s in sections:
            if row["k"] >= 5 and s["exact_lower_equivalences"]:
                print("  exact", s["coordinate"], s["present"], s["exact_lower_equivalences"][0])
            fold = s["anchor_fold"]
            if row["k"] >= 6 and fold and fold["piece_count"] <= 10:
                print("  fold", s["coordinate"], s["present"], fold)
            if row["k"] >= 11 and s["membership_run_count"] <= 16:
                print("  special", s["coordinate"], s["present"], "runs", s["membership_runs"],
                      "components", s["johnson_component_lengths"])
                if not s["present"]:
                    print("  raw deletion size", row["coordinate_deletions"][s["coordinate"]]["filtered_size"])
    print("\nRAW WORD DEVELOPMENT FROM EXACT MIDDLE SYMMETRIES")
    for row in reports:
        for value in row["word_development_from_middle_symmetry"][:1]:
            print(row["k"], value)
    print("\nEXACT DEVELOPED CHUNKS IN MIDDLE CHRONOLOGY")
    for row in reports:
        for chunk in row.get("middle_developed_chunks", []):
            print(row["k"], chunk)
        for lift in row.get("edge_lift_checks", []):
            print("edge lift", row["k"], {name: value for name, value in lift.items()
                                        if name != "edge_equivalences"},
                  "maps", len(lift["edge_equivalences"]), lift["edge_equivalences"][:1])
        for lift in row.get("whole_middle_two_cycle_lift", []):
            print("FULL MIDDLE LIFT", row["k"], lift)
        if "cycle_intersection_matching" in row:
            print("intersection matching", row["k"], row["cycle_intersection_matching"])
        for seed in row.get("same_parity_seed_lift", []):
            print("seed lift", row["k"] - 2, row["k"], seed)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--approximate", action="store_true", help="all shifts, FFT plus assignment")
    parser.add_argument("--summary", action="store_true", help="print compact computed tables")
    parser.add_argument("--output", type=Path, help="optional reproducible JSON report")
    args = parser.parse_args()
    self_test(args.approximate)
    hashes = {int(k): digest for k, digest in re.findall(
        r"\|\s*(\d+)\s*\|\s*\d+\s*\|\s*`([0-9a-f]{64})`",
        (ROOT / "answers/README.md").read_text())}
    words, middles, reports = {}, {}, []
    for k in range(1, 17):
        start = time.monotonic()
        raw = (ROOT / f"answers/k{k:02d}.word").read_bytes()
        digest = sha256(raw).hexdigest()
        assert digest == hashes[k], (k, "SHA-256 mismatch")
        word = list(map(int, raw.split()))
        assert all(0 < x < 1 << k for x in word)
        words[k] = word
        middle = middles[k] = extract_middle(word, k)
        ws = exact_equivalences(word, word, k)
        ms = exact_equivalences(middle, middle, k)
        report = {"k": k, "sha256": digest, "word_size": len(word),
                  "middle_size": len(middle), "word_symmetries": ws, "middle_symmetries": ms,
                  "middle_non_johnson_edges": sum((a ^ b).bit_count() != 2
                                                  for a, b in zip(middle, middle[1:])),
                  "middle_closure_hamming": (middle[0] ^ middle[-1]).bit_count(),
                  "word_development_from_middle_symmetry": developed_blocks(word, ms, k)}
        positive_shifts = [s["shift"] for s in ms if s["sign"] == 1 and s["shift"] > 0]
        if positive_shifts:
            report["middle_developed_seed"] = middle[:min(positive_shifts)]
        if k > 1:
            lower = words[k - 1]
            deletions = []
            for b in range(k):
                filtered = [delete_coordinate(x, b) for x in word if not (x & (1 << b))]
                matches = exact_equivalences(lower, filtered, k - 1)
                deletions.append({"coordinate": b, "filtered_size": len(filtered), "matches": matches})
            report["coordinate_deletions"] = deletions
            report["word_prefix_inheritance"] = prefix_inheritance(lower, word, k - 1)
            report["middle_prefix_inheritance"] = prefix_inheritance(middles[k - 1], middle, k - 1)
            report["whole_lower_word_embeddings"] = [
                {"pin": pin, "embeddings": segment_embeddings([x | (pin << (k - 1)) for x in lower], word, k)}
                for pin in (0, 1)]
            report["middle_sections"] = chronology_sections(middle, middles[k - 1], k)
        if args.approximate:
            report["word_approximate"] = approximate_symmetries(word, k)
            report["middle_approximate"] = approximate_symmetries(middle, k)
            report["middle_developed_chunks"] = developed_chunks(
                middle, report["middle_approximate"]["rotation"]["best"], k)
            chunks = report["middle_developed_chunks"]
            if k % 2 and chunks and all(c["cyclic_non_johnson_edges"] == 0 for c in chunks):
                intersections = []
                for chunk in chunks:
                    cycle = middle[chunk["start"]:chunk["end"]]
                    intersections.extend(a & b for a, b in zip(cycle, cycle[1:] + cycle[:1]))
                expected = comb(k, (k - 1) // 2)
                report["cycle_intersection_matching"] = {
                    "distinct_intersections": len(set(intersections)), "expected": expected,
                    "perfect": len(set(intersections)) == expected}
            if k >= 13 and k % 2:
                report["same_parity_seed_lift"] = seed_lift_checks(
                    middles[k - 2], middle, reports[k - 3].get("middle_developed_chunks", []), chunks, k)
            if k > 2 and k % 2 == 0:
                report["edge_lift_checks"] = edge_lift_checks(
                    middles[k - 1], middle, reports[-1].get("middle_developed_chunks", []), k)
                report["whole_middle_two_cycle_lift"] = reconstruct_two_cycle_lift(
                    middles[k - 1], middle, reports[-1].get("middle_developed_chunks", []),
                    report["middle_sections"])
        reports.append(report)
        rotations = [x["shift"] for x in ms if x["sign"] == 1]
        reflections = [x["shift"] for x in ms if x["sign"] == -1]
        print(f"k={k:2} word_sym={len(ws):2} middle_rot={rotations} "
              f"middle_ref={reflections} elapsed={time.monotonic() - start:.2f}s", flush=True)
    result = {"convention": "perm(A[i]) = A[(shift + sign*i) % n]; zero-based coordinates/positions",
              "middle": "distinct rank-ceil(k/2) interval ORs in first-right-endpoint chronology",
              "approximate_objective": "sum of bit Hamming distances; mask errors only measured afterward",
              "reports": reports}
    if args.output:
        args.output.write_text(json.dumps(result, indent=2) + "\n")
    if args.summary:
        summarize(reports)
    elif not args.output:
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
