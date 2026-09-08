#!/usr/bin/env python3
"""REVIEW BEFORE RUN: one supplied literal19 reconstruction, h100 only.

No generator, search, switch, relabelling trial, word edit, or optimisation.
The canonical comparison uses only the separately pinned existing file.
Coverage of the complete nineteen-cube is audited independently elsewhere.
Here all rank<=8 targets are checked by explicit literal/pair witnesses.
"""

import argparse
import hashlib
import json
import platform
import resource
import signal
import time
from collections import Counter
from math import comb
from pathlib import Path

N = 19
FULL = (1 << N) - 1
WIDTH = 92378
LENGTH = 92381
CANONICAL_SHA = '5e44113db3152b216af7761766f69a7b389db54b5c1f5dce9ac227ba6e6e71cd'


def union_masks(values):
    out = 0
    for value in values:
        out |= value
    return out


def intersection_masks(values):
    out = FULL
    for value in values:
        out &= value
    return out


def rotate(value):
    return ((value << 1) & FULL) | (value >> (N - 1))


def rotate_back(value, amount):
    if amount == 0:
        return value
    return ((value >> amount) | (value << (N - amount))) & FULL


def phi(lower):
    """Add the first global prefix-minimum zero, in positive site order."""
    balance = minimum = 0
    root = None
    for coordinate in range(N):
        balance += 1 if (lower >> coordinate) & 1 else -1
        if balance < minimum:
            minimum = balance
            root = coordinate
    assert balance == -1 and root is not None
    assert not (lower >> root) & 1
    return lower | (1 << root)


def write_json(path, value, *, pretty=False):
    with path.open('w') as stream:
        json.dump(value, stream, indent=2 if pretty else None,
                  separators=None if pretty else (',', ':'))
        stream.write('\n')


def rank_census(values):
    return [[rank, count] for rank, count in
            sorted(Counter(value.bit_count() for value in values).items())]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--word', type=Path, required=True)
    parser.add_argument('--word-sha', required=True,
                        help='Root-pinned supplied literal SHA, not inferred by this checker.')
    parser.add_argument('--canonical', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    assert platform.node().split('.')[0] == 'arboghast', 'h100 only'
    resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
    resource.setrlimit(resource.RLIMIT_AS, (2 * 1024**3, 2 * 1024**3))
    resource.setrlimit(resource.RLIMIT_FSIZE, (1024**3, 1024**3))
    signal.alarm(90)
    started = time.monotonic()
    args.out.mkdir(parents=True, exist_ok=False)
    checks = {}

    def require(name, condition, detail=None):
        checks[name] = bool(condition)
        if not condition:
            failure = dict(status='ARCHITECTURE_OR_INPUT_MISMATCH', failed_check=name,
                           detail=detail, checks=checks,
                           elapsed_seconds=time.monotonic() - started)
            write_json(args.out / 'failure_report.json', failure, pretty=True)
            raise AssertionError(name)

    raw = args.word.read_bytes()
    canonical_raw = args.canonical.read_bytes()
    require('word_hash_argument_format', len(args.word_sha) == 64 and
            all(c in '0123456789abcdef' for c in args.word_sha))
    actual_sha = hashlib.sha256(raw).hexdigest()
    require('pinned_literal_hash', actual_sha == args.word_sha, actual_sha)
    require('pinned_existing_canonical_hash',
            hashlib.sha256(canonical_raw).hexdigest() == CANONICAL_SHA)
    word = [int(line) for line in raw.decode('ascii').splitlines() if line.strip()]
    require('literal_length_and_nonempty_masks', len(word) == LENGTH and
            all(0 < value <= FULL for value in word))
    require('width_arithmetic', comb(N, 9) == WIDTH == comb(N, 10))
    C = word[:WIDTH]
    require('one_period_plus_three_literal_letters', word == C + C[:3])

    # Future-window convention is derived directly from the supplied word.
    R = [C[i] | C[(i+1) % WIDTH] | C[(i+2) % WIDTH] for i in range(WIDTH)]
    U = [R[i] | C[(i+3) % WIDTH] for i in range(WIDTH)]
    require('all_literal_triples_rank9', all(x.bit_count() == 9 for x in R))
    require('all_literal_four_windows_rank10', all(x.bit_count() == 10 for x in U))
    require('rank9_window_bijection', len(set(R)) == WIDTH)
    require('rank10_window_bijection', len(set(U)) == WIDTH)
    position = {lower: i for i, lower in enumerate(R)}
    require('consecutive_lower_union_is_outgoing_upper',
            all(R[i] | R[(i+1) % WIDTH] == U[i] for i in range(WIDTH)))
    require('incoming_outgoing_intersection_is_current_lower',
            all(U[(i-1) % WIDTH] & U[i] == R[i] for i in range(WIDTH)))

    E = [U[(i-3) % WIDTH] & U[(i-2) % WIDTH] & U[(i-1) % WIDTH] & U[i]
         for i in range(WIDTH)]
    require('causal_envelope_contains_literal_same_index',
            all(C[i] & ~E[i] == 0 for i in range(WIDTH)))
    envelope_triples = [E[i] | E[(i+1) % WIDTH] | E[(i+2) % WIDTH]
                        for i in range(WIDTH)]
    require('envelope_triples_have_exact_R_i_phase', envelope_triples == R)
    require('envelope_four_windows_have_exact_U_i_phase',
            all(envelope_triples[i] | E[(i+3) % WIDTH] == U[i]
                for i in range(WIDTH)))

    inserted = [R[(i+1) % WIDTH] & ~R[i] for i in range(WIDTH)]
    deleted = [R[i] & ~R[(i+1) % WIDTH] for i in range(WIDTH)]
    require('one_coordinate_insertions_and_deletions',
            all(a.bit_count() == b.bit_count() == 1 for a, b in zip(inserted, deleted)))
    phi_bad = [dict(position=i, lower=R[i], actual_upper=U[i], phi_upper=phi(R[i]))
               for i in range(WIDTH) if phi(R[i]) != U[i]]
    residence_bad = [dict(position=i, lower=R[i], inserted=inserted[i],
                          delays=[j for j in (1, 2) if inserted[i] == deleted[(i+j) % WIDTH]])
                     for i in range(WIDTH)
                     if inserted[i] in (deleted[(i+1) % WIDTH], deleted[(i+2) % WIDTH])]
    write_json(args.out / 'fixed_phi_violations.json', phi_bad)
    write_json(args.out / 'two_step_residence_violations.json', residence_bad)
    # Fixed Phi is a diagnostic, not a premise of the supplied construction.
    # A valid literal carrier may change BOTH canonical matchings.
    fixed_phi_agrees = not phi_bad
    require('both_delayed_deletion_exclusions', not residence_bad,
            dict(count=len(residence_bad), first=residence_bad[:5]))

    literal_pairs = [C[i] | C[(i+1) % WIDTH] for i in range(WIDTH)]
    envelope_pairs = [E[i] | E[(i+1) % WIDTH] for i in range(WIDTH)]
    pins = []
    for i in range(WIDTH):
        pin = ((R[(i-2) % WIDTH] & ~(E[(i-2) % WIDTH] | E[(i-1) % WIDTH])) |
               (R[(i-1) % WIDTH] & ~(E[(i-1) % WIDTH] | E[(i+1) % WIDTH])) |
               (R[i] & ~(E[(i+1) % WIDTH] | E[(i+2) % WIDTH])))
        pins.append(pin)
    require('actual_caps_contain_all_individual_triple_deficit_pins',
            all(pins[i] & ~C[i] == 0 for i in range(WIDTH)))

    # Full low-rank inventory and actual ordinary witnesses in A=C+C[:3].
    # No >=3-letter interval can have rank<=8, since every triple has rank9.
    literal_by_rank = {rank: set() for rank in range(1, 9)}
    pair_by_rank = {rank: set() for rank in range(1, 9)}
    low_witnesses = {}
    for i in range(WIDTH):
        if C[i].bit_count() <= 8:
            literal_by_rank[C[i].bit_count()].add(C[i])
            low_witnesses.setdefault(C[i], (i, i+1))
        if literal_pairs[i].bit_count() <= 8:
            pair_by_rank[literal_pairs[i].bit_count()].add(literal_pairs[i])
            low_witnesses.setdefault(literal_pairs[i], (i, i+2))
    expected_low = {mask for mask in range(1, FULL+1) if mask.bit_count() <= 8}
    holes = sorted(expected_low - low_witnesses.keys())
    write_json(args.out / 'rank1_through8_literal_and_pair_masks.json', dict(
        literal={rank: sorted(values) for rank, values in literal_by_rank.items()},
        pair={rank: sorted(values) for rank, values in pair_by_rank.items()},
        holes=holes))
    require('all_rank1_through8_targets_have_literal_or_pair_witness', not holes,
            dict(count=len(holes), first=holes[:20]))
    for target, (left, right) in low_witnesses.items():
        require('low_witness_range_inside_actual_linear_word',
                0 <= left < right <= len(word) and right-left in (1, 2))
        require('low_witness_direct_literal_replay', union_masks(word[left:right]) == target)
    write_json(args.out / 'all_lower_short_interval_witnesses.json',
               [[mask, *low_witnesses[mask]] for mask in sorted(low_witnesses)])

    # Existing canonical data only. No new native factor is generated.
    canonical = json.loads(canonical_raw)
    native = {}
    for cycle in canonical:
        base = cycle['lower_owners']
        v = cycle['length']
        require('canonical_cycle_literal_lengths', len(base) == v)
        require('canonical_original_owner_ranks', all(b.bit_count() == 9 for b in base))
        uppers = [FULL ^ b for b in base]
        for j in range(v):
            lower = uppers[j] & uppers[(j+1) % v]
            require('canonical_named_lower_no_repeat', lower not in native)
            require('canonical_named_lower_rank', lower.bit_count() == 9)
            native[lower] = dict(incoming=uppers[j], outgoing=uppers[(j+1) % v],
                                 cycle=cycle['cycle'], height=cycle['height'])
    require('canonical_same_complete_named_lower_layer', set(native) == set(position))
    require('canonical_incoming_upper_bijection',
            len({row['incoming'] for row in native.values()}) == WIDTH)
    require('canonical_outgoing_is_same_phi',
            all(row['outgoing'] == phi(lower) for lower, row in native.items()))
    inverse_native_in = {row['incoming']: lower for lower, row in native.items()}
    theta = {lower: inverse_native_in[U[(i-1) % WIDTH]]
             for lower, i in position.items()}
    require('incoming_matching_difference_is_permutation', set(theta) == set(theta.values()))
    seen = set()
    circuits = []
    lengths = Counter()
    unchanged = 0
    for start in sorted(theta):
        if start in seen:
            continue
        circuit = []
        lower = start
        while lower not in seen:
            seen.add(lower)
            circuit.append(lower)
            lower = theta[lower]
        require('matching_difference_cycle_closure', lower == start)
        if len(circuit) == 1:
            unchanged += 1
            continue
        old = [native[L]['incoming'] for L in circuit]
        new = [U[(position[L]-1) % WIDTH] for L in circuit]
        require('matching_difference_cyclic_transport', new == old[1:] + old[:1])
        core = intersection_masks(circuit)
        active = union_masks(old+new) & ~core
        lengths[len(circuit)] += 1
        circuits.append(dict(lower_cycle=circuit, old_incoming=old, new_incoming=new,
                             common_core=core, active_coordinates=active,
                             native_components=sorted({native[L]['cycle'] for L in circuit}),
                             native_heights=sorted({native[L]['height'] for L in circuit})))
    write_json(args.out / 'incoming_matching_alternating_circuits.json', circuits)
    changed_by_height = Counter()
    outgoing_changed_by_height = Counter()
    shared_incidence = Counter()
    for lower, i in position.items():
        native_row = native[lower]
        if native_row['incoming'] != U[(i-1) % WIDTH]:
            changed_by_height[native_row['height']] += 1
        if native_row['outgoing'] != U[i]:
            outgoing_changed_by_height[native_row['height']] += 1
        shared_incidence[len({native_row['incoming'], native_row['outgoing']} &
                             {U[(i-1) % WIDTH], U[i]})] += 1

    # Derive all physical rotation orbits. Fields may be compressed to
    # one representative only if their equivariance check actually passes.
    orbit = {}
    reps = []
    for lower in sorted(position):
        if lower in orbit:
            continue
        oi = len(reps)
        reps.append(lower)
        mask = lower
        for shift in range(N):
            require('rotation_orbit_has_nineteen_distinct_named_labels',
                    mask in position and mask not in orbit)
            orbit[mask] = (oi, shift)
            mask = rotate(mask)
        require('rotation_orbit_closes_after_nineteen', mask == lower)
    require('4862_rotation_orbits', len(reps) == 4862 and len(reps) * N == WIDTH)
    fields = dict(successor=[R[(i+1) % WIDTH] for i in range(WIDTH)],
                  outgoing=U, incoming=[U[(i-1) % WIDTH] for i in range(WIDTH)],
                  literal=C, envelope=E, triple_pins=pins)
    equivariance = {}
    for field, values in fields.items():
        bad = [i for i in range(WIDTH)
               if values[position[rotate(R[i])]] != rotate(values[i])]
        equivariance[field] = dict(violations=len(bad), first_positions=bad[:20])
    quotient = []
    for oi, lower in enumerate(reps):
        i = position[lower]
        orbit_positions = []
        normalised_letters = []
        mask = lower
        for shift in range(N):
            j = position[mask]
            orbit_positions.append(j)
            normalised_letters.append(rotate_back(C[j], shift))
            mask = rotate(mask)
        successor_row, successor_shift = orbit[R[(i+1) % WIDTH]]
        quotient.append(dict(row=oi, lower=lower, period_position=i,
                             outgoing=U[i], incoming=U[(i-1) % WIDTH],
                             insertion=inserted[i], deletion=deleted[i],
                             successor_row=successor_row, successor_shift=successor_shift,
                             literal=C[i], envelope=E[i], triple_pins=pins[i],
                             original_period_positions=orbit_positions,
                             rotation_normalised_literal_values=normalised_letters))
    write_json(args.out / 'recovered_4862_rotation_rows.json', quotient)
    write_json(args.out / 'complete_named_literal_carrier.json', [
        dict(lower=R[i], position=i, outgoing=U[i], incoming=U[(i-1) % WIDTH],
             successor=R[(i+1) % WIDTH], insertion=inserted[i], deletion=deleted[i],
             literal=C[i], envelope=E[i], triple_pins=pins[i],
             literal_pair=literal_pairs[i], envelope_pair=envelope_pairs[i],
             canonical_incoming=native[R[i]]['incoming'],
             canonical_component=native[R[i]]['cycle'], canonical_height=native[R[i]]['height'])
        for i in range(WIDTH)])

    changed_pairs = [i for i in range(WIDTH) if literal_pairs[i] != envelope_pairs[i]]
    write_json(args.out / 'changed_pair_positions.json', changed_pairs)
    low_census = []
    for rank in range(1, 9):
        literals = literal_by_rank[rank]
        pairs = pair_by_rank[rank]
        low_census.append(dict(rank=rank, literal_distinct=len(literals),
                               pair_distinct=len(pairs), overlap=len(literals & pairs),
                               total_distinct=len(literals | pairs), expected=comb(N, rank),
                               pair_only=len(pairs - literals)))
    report = dict(
        status='PASS_LITERAL19_STRUCTURAL_RECONSTRUCTION',
        scope='One pinned literal19 and one pinned existing canonical19 file; no generator or search replay.',
        word19_sha256=actual_sha, canonical_sha256=CANONICAL_SHA,
        checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        checks=checks, actual_period_length=WIDTH, linear_length=LENGTH,
        lower_layer_rank=9, upper_layer_rank=10,
        phase=dict(lower='R_i=OR C_i,C_(i+1),C_(i+2)',
                   upper='U_i=OR C_i,...,C_(i+3)',
                   envelope='E_i=INTERSECTION U_(i-3),...,U_i',
                   exact_triple_identity='OR E_i,E_(i+1),E_(i+2)=R_i',
                   exact_four_identity='OR E_i,...,E_(i+3)=U_i'),
        literal_rank_occurrences=rank_census(C), envelope_rank_occurrences=rank_census(E),
        literal_pair_rank_occurrences=rank_census(literal_pairs),
        envelope_pair_rank_occurrences=rank_census(envelope_pairs),
        triple_pin_rank_occurrences=rank_census(pins),
        distinct_literal_targets=len(set(C)), distinct_pair_targets=len(set(literal_pairs)),
        changed_pair_positions=len(changed_pairs), lower_short_target_count=len(low_witnesses),
        lower_rank_census=low_census, ordinary_short_witness_replays=len(low_witnesses),
        rotation_equivariance=equivariance, quotient_rows=len(quotient),
        quotient_scope='One row determines a field on its orbit only when that field has zero equivariance violations; the full named carrier is also retained.',
        canonical_components=len(canonical),
        fixed_phi_agrees=fixed_phi_agrees, fixed_phi_violations=len(phi_bad),
        native_outgoing_changed=sum(outgoing_changed_by_height.values()),
        native_outgoing_unchanged=WIDTH-sum(outgoing_changed_by_height.values()),
        outgoing_changed_by_native_height=sorted(outgoing_changed_by_height.items()),
        native_incoming_unchanged=unchanged, native_incoming_changed=WIDTH-unchanged,
        incoming_difference_nontrivial_circuits=len(circuits),
        incoming_difference_circuit_lengths=sorted(lengths.items()),
        incoming_changed_by_native_height=sorted(changed_by_height.items()),
        shared_unoriented_middle_incidences=sorted(shared_incidence.items()),
        resource_caps=dict(cpu_seconds=60, wall_seconds=90, address_space_bytes=2*1024**3,
                           per_file_size_bytes=1024**3),
        host=platform.node(), elapsed_seconds=time.monotonic()-started)
    write_json(args.out / 'literal19_structural_reconstruction_certificate.json', report, pretty=True)
    print(json.dumps(report, indent=2), flush=True)


if __name__ == '__main__':
    main()
