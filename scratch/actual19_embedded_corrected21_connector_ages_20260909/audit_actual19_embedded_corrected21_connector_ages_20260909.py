#!/usr/bin/env python3
"""REVIEW BEFORE RUN: fixed actual19 -> corrected21 incoming-age supply.

The ONLY input carrier is the pinned optimal19 literal. Enumerate every
P=00D1, D Dyck of semilength 8, without rotations or alternative histories.
No search, matching, word modification, or spanning21 assertion.
Mathematical execution is allowed only on h100 after source approval.
"""

import argparse
import hashlib
import json
import math
import resource
import signal
import socket
import time
from collections import Counter
from pathlib import Path


PARENT_K = 19
PARENT_R = 9
WIDTH = 92378
LENGTH = 92381
FULL = (1 << PARENT_K) - 1
EXPECTED_SHA = '1d0e7595dc72c6f1b7590e9565d5c0d3c30d70138e993d074e7d90d778d4e414'
CHILD_K = PARENT_K + 2
PARENT_A = 1 << 18
PARENT_FIRST_D = 1 << 2
CHILD_A = 1 << 19
CHILD_B = 1 << 20
D_LENGTH = 16
D_SEMILENGTH = 8
CAPS = dict(cpu_seconds=30, wall_seconds=45,
            address_space_bytes=1024**3, file_bytes=128*1024**2)


def write_json(path, value):
    path.write_text(json.dumps(value, sort_keys=True, indent=2) + '\n')


def phi(mask, dimension):
    """Add the zero at the first global prefix minimum, bit0 first."""
    height = minimum = 0
    first_minimum_coordinate = None
    for coordinate in range(dimension):
        height += 1 if mask & (1 << coordinate) else -1
        if height < minimum:
            minimum = height
            first_minimum_coordinate = coordinate
    assert height == -1 and first_minimum_coordinate is not None
    bit = 1 << first_minimum_coordinate
    assert not mask & bit
    return mask | bit


def inverse_phi(upper, dimension):
    """Delete the up-step after the last minimum, including empty prefix."""
    height = minimum = 0
    last_minimum_prefix_length = 0
    for coordinate in range(dimension):
        height += 1 if upper & (1 << coordinate) else -1
        if height <= minimum:
            minimum = height
            last_minimum_prefix_length = coordinate + 1
    assert height == 1 and last_minimum_prefix_length < dimension
    bit = 1 << last_minimum_prefix_length
    assert upper & bit
    lower = upper & ~bit
    assert phi(lower, dimension) == upper
    return lower


def is_dyck(mask, length):
    height = 0
    for coordinate in range(length):
        height += 1 if mask & (1 << coordinate) else -1
        if height < 0:
            return False
    return height == 0


def dyck_masks(semilength):
    """Every fixed-root Dyck word once; no quotient or phase selection."""
    def visit(position, ones, zeros, mask):
        if position == 2 * semilength:
            yield mask
            return
        if ones < semilength:
            yield from visit(position + 1, ones + 1, zeros,
                             mask | (1 << position))
        if zeros < ones:
            yield from visit(position + 1, ones, zeros + 1, mask)
    yield from visit(0, 0, 0, 0)


def embed(parent):
    """Child physical word 0 P 1: u=bit0, a=bit19, b=bit20."""
    return (parent << 1) | CHILD_B


def cyclic_ages(states, bit):
    """Exact finite ages at every present state of this one cyclic bank."""
    v = len(states)
    zero = next(i for i, state in enumerate(states) if not state & bit)
    ages = [0] * v
    age = 0
    for distance in range(1, v + 1):
        i = (zero + distance) % v
        age = age + 1 if states[i] & bit else 0
        ages[i] = age
    assert all(ages[i] == (ages[(i-1) % v] + 1 if states[i] & bit else 0)
               for i in range(v))
    return ages


def direct_cyclic_age(states, position, bit):
    """Independent backward replay of a reported port age, through its zero."""
    v = len(states)
    age = 0
    while age < v and states[(position-age) % v] & bit:
        age += 1
    assert 0 < age < v
    assert not states[(position-age) % v] & bit
    return age


def history_age(history, bit):
    age = 0
    for state in reversed(history):
        if not state & bit:
            break
        age += 1
    return age


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--word', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    assert socket.gethostname().split('.')[0] == 'arboghast', 'h100 only'
    resource.setrlimit(resource.RLIMIT_CPU, (CAPS['cpu_seconds'],)*2)
    resource.setrlimit(resource.RLIMIT_AS, (CAPS['address_space_bytes'],)*2)
    resource.setrlimit(resource.RLIMIT_FSIZE, (CAPS['file_bytes'],)*2)
    signal.alarm(CAPS['wall_seconds'])
    began_cpu = time.process_time()
    began_wall = time.monotonic()
    args.out.mkdir(parents=True, exist_ok=False)
    source = Path(__file__).read_bytes()
    source_sha = hashlib.sha256(source).hexdigest()
    (args.out / 'checker.py').write_bytes(source)
    write_json(args.out / 'run_started.json', dict(
        status='RUNNING_NOT_CERTIFIED', source_sha256=source_sha,
        resource_caps=CAPS,
        scope='One pinned actual19 carrier and all fixed P=00D1 ports only.'))
    checks = {}

    def require(name, condition, detail=None):
        checks[name] = bool(condition)
        if not condition:
            write_json(args.out / 'failure.json', dict(
                status='FAILED_INPUT_OR_INTERFACE', failed_check=name,
                detail=detail, checks=checks))
            raise AssertionError(name)

    raw = args.word.read_bytes()
    raw_sha = hashlib.sha256(raw).hexdigest()
    require('pinned_raw_sha', raw_sha == EXPECTED_SHA, raw_sha)
    (args.out / 'k19_optimal92381.word').write_bytes(raw)
    tokens = raw.split()
    require('decimal_input_tokens', all(token.isdigit() for token in tokens))
    word = [int(token) for token in tokens]
    require('literal_length_and_nonempty_masks', len(word) == LENGTH and
            all(0 < mask <= FULL for mask in word))
    require('width_arithmetic', WIDTH == math.comb(PARENT_K, PARENT_R) ==
            math.comb(PARENT_K, PARENT_R+1))
    C = word[:WIDTH]
    require('actual_one_period_plus_three', word == C + C[:3])
    R = [C[i] | C[(i+1) % WIDTH] | C[(i+2) % WIDTH]
         for i in range(WIDTH)]
    U = [R[i] | C[(i+3) % WIDTH] for i in range(WIDTH)]
    require('complete_lower_rank9_deck', len(set(R)) == WIDTH and
            all(mask.bit_count() == PARENT_R for mask in R))
    require('complete_upper_rank10_deck', len(set(U)) == WIDTH and
            all(mask.bit_count() == PARENT_R+1 for mask in U))
    require('correct_adjacent_lower_union_phase', all(
        R[i] | R[(i+1) % WIDTH] == U[i] for i in range(WIDTH)))
    require('correct_adjacent_upper_intersection_phase', all(
        U[(i-1) % WIDTH] & U[i] == R[i] for i in range(WIDTH)))
    require('canonical_parent_outgoing_phi', all(
        phi(R[i], PARENT_K) == U[i] for i in range(WIDTH)))
    inserted = [R[(i+1) % WIDTH] & ~R[i] for i in range(WIDTH)]
    deleted = [R[i] & ~R[(i+1) % WIDTH] for i in range(WIDTH)]
    require('strict_parent_johnson_cycle', all(
        add.bit_count() == remove.bit_count() == 1
        for add, remove in zip(inserted, deleted)))
    require('parent_residence_at_least_three', all(
        inserted[i] not in (deleted[(i+1) % WIDTH], deleted[(i+2) % WIDTH])
        for i in range(WIDTH)))
    require('entire_fixed_embedding_retains_canonical_phi', all(
        phi(embed(R[i]), CHILD_K) == embed(U[i]) for i in range(WIDTH)))
    require('entire_fixed_embedding_retains_parent_edges', all(
        embed(R[i]) | embed(R[(i+1) % WIDTH]) == embed(U[i])
        for i in range(WIDTH)))

    ages_a = cyclic_ages(R, PARENT_A)
    ages_first_d = cyclic_ages(R, PARENT_FIRST_D)
    generated_d = list(dyck_masks(D_SEMILENGTH))
    expected_catalan = math.comb(D_LENGTH, D_SEMILENGTH) // (D_SEMILENGTH+1)
    require('independent_dyck_generation_complete',
            len(generated_d) == len(set(generated_d)) == expected_catalan and
            all(is_dyck(d, D_LENGTH) for d in generated_d))
    generated_ports = {(d << 2) | PARENT_A for d in generated_d}
    # Independently identify the same physical family by scanning the full deck.
    positions = [i for i, mask in enumerate(R) if
                 not mask & 3 and mask & PARENT_A and
                 is_dyck((mask >> 2) & ((1 << D_LENGTH)-1), D_LENGTH)]
    require('fixed_port_inventory_exact',
            {R[i] for i in positions} == generated_ports and
            len(positions) == len(generated_d))

    all_records = []
    good_records = []
    bad_records = []
    age_histogram = Counter()
    child_banks = [set() for _ in range(4)]
    outgoing_banks = [set() for _ in range(3)]
    for i in positions:
        P = R[i]
        predecessor = R[(i-1) % WIDTH]
        D = (P >> 2) & ((1 << D_LENGTH)-1)
        require('fixed_port_shape_and_nonempty_dyck_first_bit',
                P == ((D << 2) | PARENT_A) and bool(D & 1))
        a_age = ages_a[i]
        d_age = ages_first_d[i]
        require('reported_parent_ages_independently_replayed',
                a_age == direct_cyclic_age(R, i, PARENT_A) and
                d_age == direct_cyclic_age(R, i, PARENT_FIRST_D))
        age_histogram[a_age] += 1
        predicted_bad_predecessor = (D << 2) | 1  # physical 10D0
        bad = a_age == 1
        require('bad_age_iff_final_parent_bit_just_inserted',
                bad == (inserted[(i-1) % WIDTH] == PARENT_A))
        require('bad_age_iff_actual_predecessor_10D0',
                bad == (predecessor == predicted_bad_predecessor))

        # Independently audit ALL strict inverse incidences at this fixed port;
        # no incoming matching is changed or searched for by this enumeration.
        first_d_excluded = []
        for coordinate in range(PARENT_K):
            extra = 1 << coordinate
            if P & extra:
                continue
            incoming_upper = P | extra
            candidate_predecessor = inverse_phi(incoming_upper, PARENT_K)
            if candidate_predecessor == P:
                continue
            if not candidate_predecessor & PARENT_A:
                first_d_excluded.append(candidate_predecessor)
        require('only_strict_inverse_arrival_without_a_is_10D0',
                first_d_excluded == [predicted_bad_predecessor])

        A = embed(P)
        B = (A | (1 << 2)) & ~CHILD_B
        V = (B | (1 << 1)) & ~CHILD_A
        H = (V | 1) & ~(1 << 3)
        states = [A, B, V, H]
        require('literal_connector_bit_patterns',
                A == ((D << 3) | CHILD_A | CHILD_B) and
                B == ((D << 3) | (1 << 2) | CHILD_A) and
                V == ((D << 3) | (1 << 1) | (1 << 2)) and
                H == (((D & ~1) << 3) | 7))
        require('all_four_child_states_distinct_rank10',
                len(set(states)) == 4 and all(x.bit_count() == 10 for x in states))
        parent_history = [R[(i-2) % WIDTH], R[(i-1) % WIDTH], P]
        history = [embed(x) for x in parent_history]
        additions = [1 << 2, 1 << 1, 1]
        removals = [CHILD_B, CHILD_A, 1 << 3]
        replayed_ages = []
        edge_legality = []
        for step, (add, remove) in enumerate(zip(additions, removals)):
            upper = phi(states[step], CHILD_K)
            require('each_connector_edge_uses_actual_child_phi',
                    upper == (states[step] | add) and
                    states[step+1] == (upper & ~remove) and
                    bool(states[step] & remove) and
                    states[step+1] != states[step])
            require('connector_history_has_correct_current_state',
                    history[-1] == states[step])
            age = history_age(history, remove)
            replayed_ages.append(age)
            edge_legality.append(age >= 3)
            outgoing_banks[step].add(upper)
            history.append(states[step+1])
        exact_second_age = a_age + 1
        exact_third_age = d_age + 2
        require('three_state_history_replays_exact_legal_criterion',
                edge_legality == [True, not bad, True] and
                replayed_ages[1] == min(a_age, 3)+1 and
                replayed_ages[2] == min(d_age, 3)+2 and
                (all(edge_legality) == (a_age >= 2)))
        for bank, state in zip(child_banks, states):
            bank.add(state)
        record = dict(
            parent_position=i, parent_state=P, D_mask=D,
            D_bit0_first=''.join('1' if D & (1 << j) else '0'
                                for j in range(D_LENGTH)),
            actual_parent_predecessor=predecessor,
            parent_history_last_three=parent_history,
            parent_a_exact_age=a_age,
            parent_first_D_bit_exact_age=d_age,
            parent_a_last_absent_position=(i-a_age) % WIDTH,
            predicted_bad_predecessor_10D0=predicted_bad_predecessor,
            bad_age_one=bad, connector_residence_three_legal=not bad,
            child_states=states, child_history_last_three_then_connector=history,
            child_deletion_exact_ages=['infinite_in_embedded_periodic_history',
                                       exact_second_age, exact_third_age],
            child_deletion_ages_from_three_parent_states=replayed_ages,
            child_edge_legality=edge_legality)
        all_records.append(record)
        (bad_records if bad else good_records).append(record)

    port_count = len(positions)
    require('all_fixed_ports_recorded_and_partitioned',
            len(all_records) == len(good_records)+len(bad_records) == port_count)
    require('each_connector_lower_bank_injective',
            all(len(bank) == port_count for bank in child_banks))
    require('four_connector_lower_banks_disjoint',
            len(set().union(*child_banks)) == 4*port_count)
    require('three_connector_outgoing_upper_banks_disjoint',
            len(set().union(*outgoing_banks)) == 3*port_count)
    require('all_three_new_lower_banks_outside_embedded_parent',
            all(not state & CHILD_B for bank in child_banks[1:] for state in bank))
    write_json(args.out / 'all_fixed_connector_ports.json', all_records)
    write_json(args.out / 'all_good_connectors.json', good_records)
    write_json(args.out / 'all_bad_age_one_ports.json', bad_records)
    report = dict(
        status='PASS_FIXED_ACTUAL19_CONNECTOR_AGE_DIAGNOSTIC',
        input_sha256=raw_sha, source_sha256=source_sha, resource_caps=CAPS,
        parent_dimension=PARENT_K, child_dimension=CHILD_K, residence=3,
        parent_width=WIDTH, parent_literal_length=LENGTH,
        child_embedding='(parent_mask << 1) | (1 << 20)',
        child_u_coordinate=0, child_a_coordinate=19, child_b_coordinate=20,
        fixed_parent_family='00D1; D Dyck semilength 8; bit0 first',
        enumerated_port_count=port_count, derived_catalan_count=expected_catalan,
        quoted_1430_count_matches=(port_count == 1430),
        good_connector_count=len(good_records), bad_age_one_count=len(bad_records),
        parent_a_exact_age_histogram=dict(sorted(age_histogram.items())),
        all_fixed_ports_have_legal_connector=not bad_records,
        all_bad_predecessors_exactly_10D0=True,
        literal_good_and_bad_records_complete=True, all_checks=checks,
        elapsed_cpu_seconds=time.process_time()-began_cpu,
        elapsed_wall_seconds=time.monotonic()-began_wall,
        scope=('Conditional incoming-age supply from ONE fixed verified actual19 '
               'carrier, embedded as physical 0 P 1. All good connectors and all '
               'bad ports are listed; a nonzero bad count is a diagnostic result, '
               'not an input failure. This does not splice the excursions into '
               'a child factor, resolve matching degrees or output ages, prove '
               'spanning21 coverage, or search alternative parents/ports/cuts.'))
    write_json(args.out / 'actual19_corrected21_connector_age_certificate.json', report)
    print(json.dumps({key: report[key] for key in (
        'status', 'enumerated_port_count', 'good_connector_count',
        'bad_age_one_count', 'parent_a_exact_age_histogram',
        'all_fixed_ports_have_legal_connector', 'elapsed_cpu_seconds',
        'elapsed_wall_seconds')}, sort_keys=True), flush=True)


if __name__ == '__main__':
    main()
