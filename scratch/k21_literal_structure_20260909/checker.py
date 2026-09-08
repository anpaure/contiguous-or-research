#!/usr/bin/env python3
"""REVIEW BEFORE RUN. One pinned supplied21 literal; h100 only.

Exactly the 352548/105/63 periods, three copied letters each, and 572-letter
tail. No generation, search, word edits, alternate cuts, flow, or optimisation.
In particular this does not certify the user's weighted-Hall search history.
"""

import argparse
import hashlib
import json
import platform
import resource
import signal
import time
from array import array
from collections import Counter
from math import comb
from pathlib import Path

N = 21
FULL = (1 << N) - 1
WIDTH = 352716
LENGTH = 353297
PERIODS = (352548, 105, 63)
PREFIX_LENGTH = 352725
REPAIR_LENGTH = 572
WORD_SHA = '0b166713d18f9ba4d064b07575c17068008954ac808313359c5fd0bf5dfe24d7'


def dump(path, value, pretty=False):
    with path.open('w') as stream:
        json.dump(value, stream, indent=2 if pretty else None,
                  separators=None if pretty else (',', ':'))
        stream.write('\n')


def rank_census(values):
    return [[rank, count] for rank, count in
            sorted(Counter(x.bit_count() for x in values).items())]


def rot(x):
    return ((x << 1) & FULL) | (x >> (N - 1))


def phi(lower):
    balance = minimum = 0
    first = None
    for bit in range(N):
        balance += 1 if lower & (1 << bit) else -1
        if balance < minimum:
            minimum, first = balance, bit
    assert balance == -1 and first is not None
    return lower | (1 << first)


def ending_states(previous, letter, endpoint):
    """Distinct suffix ORs, decreasing latest-start order.

    ORs of nested suffixes are nested, so duplicates are adjacent. Retaining
    the first occurrence keeps the latest possible start for each OR.
    """
    current = [(letter, endpoint)]
    last = letter
    for mask, start in previous:
        value = mask | letter
        if value != last:
            current.append((value, start))
            last = value
    return current


def make_range_tree(word):
    size = 1
    while size < len(word):
        size *= 2
    tree = array('I', [0]) * (2 * size)
    tree[size:size+len(word)] = array('I', word)
    for i in range(size-1, 0, -1):
        tree[i] = tree[2*i] | tree[2*i+1]
    return size, tree


def range_or(size, tree, left, right):
    value = 0
    left, right = left+size, right+size
    while left < right:
        if left & 1:
            value |= tree[left]
            left += 1
        if right & 1:
            right -= 1
            value |= tree[right]
        left //= 2
        right //= 2
    return value


def reconstruct(args, started, checks):
    out = args.out

    def require(name, condition, detail=None):
        checks[name] = bool(condition)
        if not condition:
            dump(out / 'failure_report.json', dict(
                status='ARCHITECTURE_OR_INPUT_MISMATCH', failed_check=name,
                detail=detail, checks=checks,
                elapsed_seconds=time.monotonic()-started), True)
            raise AssertionError(name)

    raw = args.word.read_bytes()
    actual_sha = hashlib.sha256(raw).hexdigest()
    require('pinned_supplied21_sha', actual_sha == WORD_SHA, actual_sha)
    word = [int(line) for line in raw.decode('ascii').splitlines() if line.strip()]
    require('literal_length_nonempty_masks', len(word) == LENGTH and
            all(0 < x <= FULL for x in word))
    require('width_and_length_arithmetic',
            comb(N, 10) == WIDTH == comb(N, 11) == sum(PERIODS) and
            WIDTH+9 == PREFIX_LENGTH and PREFIX_LENGTH+REPAIR_LENGTH == LENGTH)
    cycles = []
    offset = 0
    for cid, v in enumerate(PERIODS):
        C = word[offset:offset+v]
        require('literal_three_letter_collar_'+str(cid),
                word[offset+v:offset+v+3] == C[:3])
        cycles.append(dict(cycle=cid, length=v, offset=offset, letters=C))
        offset += v+3
    require('exact_three_period_block_boundary', offset == PREFIX_LENGTH)
    repairs = word[PREFIX_LENGTH:]
    dump(out / 'literal_three_periods_and_572_repairs.json', dict(
        cycles=cycles, repair_offset=PREFIX_LENGTH, repair_letters=repairs))

    position = {}
    uppers_seen = set()
    phi_bad, residence_bad = [], []
    for cycle in cycles:
        cid, v, C = cycle['cycle'], cycle['length'], cycle['letters']
        R = [C[i] | C[(i+1) % v] | C[(i+2) % v] for i in range(v)]
        U = [R[i] | C[(i+3) % v] for i in range(v)]
        require('literal_middle_ranks_'+str(cid),
                all(x.bit_count() == 10 for x in R) and
                all(x.bit_count() == 11 for x in U))
        for i, lower in enumerate(R):
            require('global_lower_owner_no_repeat', lower not in position,
                    dict(cycle=cid, position=i, lower=lower))
            require('global_upper_owner_no_repeat', U[i] not in uppers_seen,
                    dict(cycle=cid, position=i, upper=U[i]))
            position[lower] = (cid, i)
            uppers_seen.add(U[i])
        require('adjacent_middle_incidence_'+str(cid), all(
            R[i] | R[(i+1) % v] == U[i] and
            U[(i-1) % v] & U[i] == R[i] for i in range(v)))
        E = [U[(i-3) % v] & U[(i-2) % v] & U[(i-1) % v] & U[i]
             for i in range(v)]
        require('causal_envelope_contains_same_index_literal_'+str(cid),
                all(C[i] & ~E[i] == 0 for i in range(v)))
        require('exact_envelope_future_window_phase_'+str(cid), all(
            E[i] | E[(i+1) % v] | E[(i+2) % v] == R[i] and
            E[i] | E[(i+1) % v] | E[(i+2) % v] | E[(i+3) % v] == U[i]
            for i in range(v)))
        inserted = [R[(i+1) % v] & ~R[i] for i in range(v)]
        deleted = [R[i] & ~R[(i+1) % v] for i in range(v)]
        require('single_insert_delete_'+str(cid), all(
            a.bit_count() == d.bit_count() == 1 for a, d in zip(inserted, deleted)))
        for i in range(v):
            expected = phi(R[i])
            if expected != U[i]:
                phi_bad.append([cid, i, R[i], U[i], expected])
            for delay in (1, 2):
                if inserted[i] == deleted[(i+delay) % v]:
                    residence_bad.append([cid, i, delay, inserted[i]])
        pins = [
            (R[(i-2) % v] & ~(E[(i-2) % v] | E[(i-1) % v])) |
            (R[(i-1) % v] & ~(E[(i-1) % v] | E[(i+1) % v])) |
            (R[i] & ~(E[(i+1) % v] | E[(i+2) % v]))
            for i in range(v)]
        require('actual_caps_contain_individual_triple_pins_'+str(cid),
                all(pins[i] & ~C[i] == 0 for i in range(v)))
        cycle.update(lower=R, upper=U, envelope=E, pins=pins)
    dump(out / 'fixed_phi_violations.json', phi_bad)
    dump(out / 'two_step_residence_violations.json', residence_bad)
    require('both_complete_middle_bijections', len(position) == WIDTH == len(uppers_seen))
    require('both_delayed_deletion_exclusions', not residence_bad,
            dict(count=len(residence_bad), first=residence_bad[:10]))
    # Fixed Phi is reported, never silently imposed as a premise.

    literal_sets = {rank: set() for rank in range(1, 10)}
    pair_sets = {rank: set() for rank in range(1, 10)}
    low_witness = {}
    cycle_statistics = []
    for cycle in cycles:
        v, off = cycle['length'], cycle['offset']
        C, E, pins = cycle['letters'], cycle['envelope'], cycle['pins']
        pairs = [C[i] | C[(i+1) % v] for i in range(v)]
        old_pairs = [E[i] | E[(i+1) % v] for i in range(v)]
        for i, (letter, pair) in enumerate(zip(C, pairs)):
            if letter.bit_count() <= 9:
                literal_sets[letter.bit_count()].add(letter)
                low_witness.setdefault(letter, (off+i, off+i+1))
            if pair.bit_count() <= 9:
                pair_sets[pair.bit_count()].add(pair)
                low_witness.setdefault(pair, (off+i, off+i+2))
        changed = [pairs[i] for i in range(v) if pairs[i] != old_pairs[i]]
        cycle_statistics.append(dict(
            cycle=cycle['cycle'], length=v, offset=off,
            literal_rank_occurrences=rank_census(C),
            envelope_rank_occurrences=rank_census(E),
            literal_pair_rank_occurrences=rank_census(pairs),
            envelope_pair_rank_occurrences=rank_census(old_pairs),
            pin_rank_occurrences=rank_census(pins),
            changed_literal_positions=sum(C[i] != E[i] for i in range(v)),
            changed_pair_positions=len(changed), changed_pair_ranks=rank_census(changed)))
    require('all_short_witnesses_replay_in_actual_opened_blocks', all(
        0 <= left < right <= PREFIX_LENGTH and
        ((word[left] if right-left == 1 else word[left] | word[left+1]) == target)
        for target, (left, right) in low_witness.items()))
    low_holes = [mask for mask in range(1, FULL+1)
                 if mask.bit_count() <= 9 and mask not in low_witness]
    low_table = []
    for rank in range(1, 10):
        literals, pairs = literal_sets[rank], pair_sets[rank]
        low_table.append(dict(rank=rank, possible=comb(N, rank),
                              literals=len(literals), pairs=len(pairs),
                              overlap=len(literals & pairs), covered=len(literals | pairs),
                              pair_only=len(pairs-literals)))
    dump(out / 'rank1_through9_short_masks_and_holes.json', dict(
        literal={r: sorted(s) for r, s in literal_sets.items()},
        pair={r: sorted(s) for r, s in pair_sets.items()}, holes=low_holes))
    dump(out / 'all_lower_short_interval_witnesses.json',
         [[mask, *low_witness[mask]] for mask in sorted(low_witness)])

    # The named carrier is phase-independent. Equivariance is a diagnostic for
    # each field separately: a quotient does not certify an unprovided generator.
    fields = ('successor', 'outgoing', 'incoming', 'envelope', 'pins', 'literal')

    def row(lower):
        cid, i = position[lower]
        cycle = cycles[cid]
        v = cycle['length']
        return (cycle['lower'][(i+1) % v], cycle['upper'][i],
                cycle['upper'][(i-1) % v], cycle['envelope'][i],
                cycle['pins'][i], cycle['letters'][i])

    equiv_bad = {field: [] for field in fields}
    orbit_seen = bytearray(FULL+1)
    representatives = []
    orbit_sizes = Counter()
    with (out / 'complete_named_middle_carrier.jsonl').open('w') as stream:
        for lower in sorted(position):
            cid, i = position[lower]
            values = row(lower)
            stream.write(json.dumps([lower, cid, i, *values], separators=(',', ':'))+'\n')
            rotated = rot(lower)
            require('rotation_stays_in_named_middle_layer', rotated in position)
            rotated_values = row(rotated)
            for field, value, other in zip(fields, values, rotated_values):
                if rot(value) != other:
                    equiv_bad[field].append([lower, value, other])
            if not orbit_seen[lower]:
                orbit = []
                current = lower
                while not orbit_seen[current]:
                    orbit_seen[current] = 1
                    orbit.append(current)
                    current = rot(current)
                require('coordinate_orbit_closure', current == lower)
                orbit_sizes[len(orbit)] += 1
                representatives.append([lower, cid, i, *values])
    require('all_middle_rotation_orbits_have_length21',
            dict(orbit_sizes) == {21: WIDTH//21} and WIDTH//21 == 16796)
    dump(out / 'rotation_quotient_rows.json', dict(
        row_fields=['lower', 'cycle', 'position', *fields], rows=representatives,
        equivariant_fields={f: not equiv_bad[f] for f in fields},
        scope='Only an equivariant field is reconstructed by rotating its representative values.'))
    dump(out / 'rotation_equivariance_violations.json', equiv_bad)

    # Exact cyclic coverage of these three periods, with each start/end legal
    # and length at most its own period. No joins are counted as cyclic witnesses.
    bank_seen = bytearray(FULL+1)
    for cycle in cycles:
        v, C = cycle['length'], cycle['letters']
        states = []
        for endpoint in range(2*v):
            states = ending_states(states, C[endpoint % v], endpoint)
            lower = endpoint-v+1
            states = [(mask, start) for mask, start in states if start >= lower]
            if endpoint >= v:
                for mask, _ in states:
                    bank_seen[mask] = 1
    bank_holes = [mask for mask in range(1, FULL+1) if not bank_seen[mask]]
    require('cyclic_low_inventory_matches_complete_cyclic_enumeration', all(
        bool(bank_seen[mask]) == (mask in low_witness)
        for mask in range(1, FULL+1) if mask.bit_count() <= 9))

    # Exact ending-OR enumeration of the three opened blocks including their
    # physical joins. Continue its actual boundary states through the fixed tail.
    prefix_seen = bytearray(FULL+1)
    states = []
    for endpoint, letter in enumerate(word[:PREFIX_LENGTH]):
        states = ending_states(states, letter, endpoint)
        for mask, _ in states:
            prefix_seen[mask] = 1
    prefix_holes = [mask for mask in range(1, FULL+1) if not prefix_seen[mask]]
    opening_losses = [mask for mask in prefix_holes if bank_seen[mask]]
    cross_join_gains = [mask for mask in bank_holes if prefix_seen[mask]]
    tail_witnesses = {}
    for endpoint in range(PREFIX_LENGTH, LENGTH):
        states = ending_states(states, word[endpoint], endpoint)
        for mask, start in states:
            if not prefix_seen[mask]:
                prefix_seen[mask] = 1
                tail_witnesses[mask] = (start, endpoint+1)
    final_holes = [mask for mask in prefix_holes if not prefix_seen[mask]]
    size, tree = make_range_tree(word)
    require('every_new_tail_witness_independent_range_tree_replay', all(
        0 <= left < right <= LENGTH and right > PREFIX_LENGTH and
        range_or(size, tree, left, right) == mask
        for mask, (left, right) in tail_witnesses.items()))
    dump(out / 'cyclic_bank_opened_prefix_and_repair_holes.json', dict(
        cyclic_bank_holes=bank_holes, opened_prefix_holes=prefix_holes,
        cyclic_covered_but_opening_lost=opening_losses,
        cyclic_missing_but_cross_join_gained=cross_join_gains,
        repair_literal_set=sorted(set(repairs)), final_holes=final_holes,
        new_tail_witnesses=[[mask, *tail_witnesses[mask]] for mask in sorted(tail_witnesses)]))
    # The exact supplied file is expected universal. If a premise is wrong, keep
    # all diagnostics and do not label the run successful.
    require('all_opened_prefix_holes_repaired_by_actual_tail', not final_holes,
            dict(count=len(final_holes), first=final_holes[:20]))

    report = dict(
        status='PASS_FIXED_LITERAL_STRUCTURE_AND_REPAIR_REPLAY',
        scope='One supplied three-cycle literal. No search, Hall-flow, compact-generator, or all-dimension proof.',
        word_sha256=actual_sha,
        checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        coordinate_count=N, total_length=LENGTH, period_lengths=list(PERIODS),
        total_period_width=WIDTH, opened_prefix_length=PREFIX_LENGTH,
        repair_length=REPAIR_LENGTH, checks=checks,
        fixed_phi_agrees=not phi_bad, fixed_phi_violation_count=len(phi_bad),
        residence_violation_count=len(residence_bad), cycles=cycle_statistics,
        middle_lower_count=len(position), middle_upper_count=len(uppers_seen),
        lower_literal_pair_inventory=low_table, lower_short_holes=len(low_holes),
        orbit_sizes=sorted(orbit_sizes.items()),
        rotation_equivariance_violation_counts={f: len(equiv_bad[f]) for f in fields},
        cyclic_bank_target_count=FULL-len(bank_holes), cyclic_bank_holes=len(bank_holes),
        cyclic_bank_hole_ranks=rank_census(bank_holes),
        opened_prefix_target_count=FULL-len(prefix_holes),
        opened_prefix_holes=len(prefix_holes), opened_prefix_hole_ranks=rank_census(prefix_holes),
        opening_losses=len(opening_losses), cross_join_gains=len(cross_join_gains),
        repair_distinct_literals=len(set(repairs)),
        repair_literal_set_equals_prefix_holes=set(repairs) == set(prefix_holes),
        newly_repaired_targets=len(tail_witnesses), final_target_count=FULL-len(final_holes),
        all_new_tail_witnesses_independently_range_replayed=True,
        elapsed_seconds=time.monotonic()-started)
    dump(out / 'k21_three_cycle_structure_and_repairs_certificate.json', report, True)
    manifest = {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                for p in sorted(out.iterdir()) if p.is_file()}
    dump(out / 'artifact_sha256_manifest.json', manifest, True)
    print(json.dumps(report, separators=(',', ':')), flush=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--word', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    assert platform.node().split('.')[0] == 'arboghast', 'h100 only'
    resource.setrlimit(resource.RLIMIT_CPU, (60, 60))
    resource.setrlimit(resource.RLIMIT_AS, (2*1024**3, 2*1024**3))
    resource.setrlimit(resource.RLIMIT_FSIZE, (512*1024**2, 512*1024**2))
    args.out.mkdir(parents=True, exist_ok=False)
    started, checks = time.monotonic(), {}

    def timeout(signum, frame):
        raise TimeoutError('90 second wall cap')

    signal.signal(signal.SIGALRM, timeout)
    signal.alarm(90)
    try:
        reconstruct(args, started, checks)
    except BaseException as error:
        if not (args.out / 'failure_report.json').exists():
            dump(args.out / 'failure_report.json', dict(
                status='INCONCLUSIVE_OR_RUNTIME_FAILURE', exception=type(error).__name__,
                detail=str(error), checks=checks,
                elapsed_seconds=time.monotonic()-started), True)
        raise
    finally:
        signal.alarm(0)


if __name__ == '__main__':
    main()
