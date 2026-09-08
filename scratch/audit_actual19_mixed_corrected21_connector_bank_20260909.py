#!/usr/bin/env python3
"""REVIEW BEFORE RUN: deterministic mixed corrected21 connector bank.

The ONLY input carrier is the pinned optimal19 literal. Enumerate every
P=00D1, D Dyck of semilength 8, without rotations or alternative histories.
Use the original route when parent a-age>=2; swap its last two deletions
when parent a-age=1. Prior source/report/bad-list are pinned but not executed.
No search, matching, parent modification, or spanning21 assertion.
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
PRIOR_SOURCE_SHA = '27388f115066d5f6270a8d8957bc3503d81ddf231aa5e65d989afeef0663a6dd'
PRIOR_REPORT_SHA = 'fe798b2a6dbc55c4307ed252f91ca4b53c02b88dd442e3c10d8eba90360aeecc'
PRIOR_BAD_SHA = 'd177285f9e8fad4f6db5e45cb9a0b82cec6775b65f6303c143304a1add11f151'
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
    parser.add_argument('--prior-source', type=Path, required=True)
    parser.add_argument('--prior-report', type=Path, required=True)
    parser.add_argument('--prior-bad', type=Path, required=True)
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
        scope='One pinned actual19 carrier; one age-dependent route at every fixed P=00D1 port.'))
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
    prior_source_raw = args.prior_source.read_bytes()
    prior_report_raw = args.prior_report.read_bytes()
    prior_bad_raw = args.prior_bad.read_bytes()
    require('pinned_prior_source',
            hashlib.sha256(prior_source_raw).hexdigest() == PRIOR_SOURCE_SHA)
    require('pinned_prior_report',
            hashlib.sha256(prior_report_raw).hexdigest() == PRIOR_REPORT_SHA)
    require('pinned_prior_bad_list',
            hashlib.sha256(prior_bad_raw).hexdigest() == PRIOR_BAD_SHA)
    (args.out / 'prior_checker.py').write_bytes(prior_source_raw)
    (args.out / 'prior_diagnostic_report.json').write_bytes(prior_report_raw)
    (args.out / 'prior_bad_age_one_ports.json').write_bytes(prior_bad_raw)
    prior_report = json.loads(prior_report_raw)
    prior_bad = json.loads(prior_bad_raw)
    require('prior_report_identity_and_status',
            prior_report['status'] == 'PASS_FIXED_ACTUAL19_CONNECTOR_AGE_DIAGNOSTIC' and
            prior_report['input_sha256'] == EXPECTED_SHA and
            prior_report['source_sha256'] == PRIOR_SOURCE_SHA and
            all(prior_report['all_checks'].values()))
    prior_bad_by_position = {row['parent_position']: row for row in prior_bad}
    require('prior_bad_list_unique_and_reported',
            len(prior_bad_by_position) == len(prior_bad) == prior_report['bad_age_one_count'])
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
    original_route_records = []
    swapped_route_records = []
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
        predecessors_without_a = []
        for coordinate in range(PARENT_K):
            extra = 1 << coordinate
            if P & extra:
                continue
            incoming_upper = P | extra
            candidate_predecessor = inverse_phi(incoming_upper, PARENT_K)
            if candidate_predecessor == P:
                continue
            if not candidate_predecessor & PARENT_A:
                predecessors_without_a.append(candidate_predecessor)
        require('only_strict_inverse_arrival_without_a_is_10D0',
                predecessors_without_a == [predicted_bad_predecessor])

        require('same_prior_bad_set_membership_at_each_port',
                bad == (i in prior_bad_by_position))
        if bad:
            old = prior_bad_by_position[i]
            require('same_named_prior_bad_record',
                    old['parent_state'] == P and old['D_mask'] == D and
                    old['actual_parent_predecessor'] == predecessor and
                    old['parent_history_last_three'] ==
                    [R[(i-2) % WIDTH], predecessor, P] and
                    old['parent_a_exact_age'] == a_age and
                    old['parent_first_D_bit_exact_age'] == d_age)
            require('bad_branch_first_D_bit_already_present_in_predecessor',
                    bool(predecessor & PARENT_FIRST_D) and d_age >= 2)

        A = embed(P)
        B = (A | (1 << 2)) & ~CHILD_B
        V = (B | (1 << 1)) & ~((1 << 3) if bad else CHILD_A)
        H = (V | 1) & ~(CHILD_A if bad else (1 << 3))
        states = [A, B, V, H]
        require('literal_connector_bit_patterns',
                A == ((D << 3) | CHILD_A | CHILD_B) and
                B == ((D << 3) | (1 << 2) | CHILD_A) and
                V == ((((D & ~1) << 3) | 6 | CHILD_A) if bad else
                      ((D << 3) | 6)) and
                H == (((D & ~1) << 3) | 7))
        require('all_four_child_states_distinct_rank10',
                len(set(states)) == 4 and all(x.bit_count() == 10 for x in states))
        parent_history = [R[(i-2) % WIDTH], R[(i-1) % WIDTH], P]
        history = [embed(x) for x in parent_history]
        additions = [1 << 2, 1 << 1, 1]
        removals = ([CHILD_B, 1 << 3, CHILD_A] if bad else
                    [CHILD_B, CHILD_A, 1 << 3])
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
        exact_second_age = (d_age if bad else a_age) + 1
        exact_third_age = (a_age if bad else d_age) + 2
        require('three_state_history_replays_every_mixed_route_as_legal',
                edge_legality == [True, True, True] and
                replayed_ages[1] == min(d_age if bad else a_age, 3)+1 and
                replayed_ages[2] == min(a_age if bad else d_age, 3)+2 and
                exact_second_age >= 3 and exact_third_age >= 3)
        if bad:
            require('swapped_branch_final_a_deletion_has_exact_age_three',
                    exact_third_age == replayed_ages[2] == 3)
        require('same_endpoint_as_original_route_at_every_port',
                H == ((((D << 3) | 6) | 1) & ~(1 << 3)))
        require('identical_prefix_output_ages_one_two_three',
                [history_age(history, 1 << coordinate) for coordinate in (0, 1, 2)]
                == [1, 2, 3])
        require('all_surviving_D_coordinates_gain_three_states', all(
                history_age(history, 1 << coordinate) ==
                history_age(history[:3], 1 << coordinate) + 3
                for coordinate in range(4, 19) if H & (1 << coordinate)))
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
            original_route_bad_age_one=bad,
            selected_route='swap_b_d_a' if bad else 'original_b_a_d',
            connector_residence_three_legal=True,
            child_states=states, child_history_last_three_then_connector=history,
            child_deletion_coordinates=[remove.bit_length()-1 for remove in removals],
            child_deletion_exact_ages=['infinite_in_embedded_periodic_history',
                                       exact_second_age, exact_third_age],
            child_deletion_ages_from_three_parent_states=replayed_ages,
            child_edge_legality=edge_legality)
        all_records.append(record)
        (swapped_route_records if bad else original_route_records).append(record)

    port_count = len(positions)
    require('all_fixed_ports_recorded_and_partitioned',
            len(all_records) == len(original_route_records)+len(swapped_route_records) == port_count)
    require('same_complete_prior_bad_set',
            {row['parent_position'] for row in swapped_route_records} ==
            set(prior_bad_by_position))
    require('same_independently_derived_prior_counts_and_histogram',
            port_count == prior_report['enumerated_port_count'] and
            len(original_route_records) == prior_report['good_connector_count'] and
            len(swapped_route_records) == prior_report['bad_age_one_count'] and
            {str(age): count for age, count in age_histogram.items()} ==
            prior_report['parent_a_exact_age_histogram'])
    require('each_connector_lower_bank_injective',
            all(len(bank) == port_count for bank in child_banks))
    require('four_connector_lower_banks_disjoint',
            len(set().union(*child_banks)) == 4*port_count)
    require('three_connector_outgoing_upper_banks_disjoint',
            len(set().union(*outgoing_banks)) == 3*port_count)
    require('all_three_new_lower_banks_outside_embedded_parent',
            all(not state & CHILD_B for bank in child_banks[1:] for state in bank))
    write_json(args.out / 'all_mixed_connector_ports.json', all_records)
    write_json(args.out / 'all_unchanged_original_routes.json', original_route_records)
    write_json(args.out / 'all_swapped_bad_port_routes.json', swapped_route_records)
    report = dict(
        status='PASS_FIXED_ACTUAL19_MIXED_LOCAL_CONNECTOR_BANK',
        input_sha256=raw_sha, source_sha256=source_sha, resource_caps=CAPS,
        prior_source_sha256=PRIOR_SOURCE_SHA, prior_report_sha256=PRIOR_REPORT_SHA,
        prior_bad_list_sha256=PRIOR_BAD_SHA,
        parent_dimension=PARENT_K, child_dimension=CHILD_K, residence=3,
        parent_width=WIDTH, parent_literal_length=LENGTH,
        child_embedding='(parent_mask << 1) | (1 << 20)',
        child_u_coordinate=0, child_a_coordinate=19, child_b_coordinate=20,
        fixed_parent_family='00D1; D Dyck semilength 8; bit0 first',
        enumerated_port_count=port_count, derived_catalan_count=expected_catalan,
        quoted_1430_count_matches=(port_count == 1430),
        original_route_count=len(original_route_records),
        swapped_bad_port_route_count=len(swapped_route_records),
        locally_legal_connector_count=len(all_records),
        parent_a_exact_age_histogram=dict(sorted(age_histogram.items())),
        all_fixed_ports_have_legal_selected_route=True,
        all_bad_predecessors_exactly_10D0=True,
        all_mixed_route_records_complete=True,
        four_lower_bank_sizes=[len(bank) for bank in child_banks],
        three_consumed_upper_bank_sizes=[len(bank) for bank in outgoing_banks],
        all_checks=checks,
        elapsed_cpu_seconds=time.process_time()-began_cpu,
        elapsed_wall_seconds=time.monotonic()-began_wall,
        scope=('One deterministic mixed local connector bank on the SAME fixed '
               'actual19 parent: old route when a-age>=2, swapped b,d,a route '
               'only when a-age=1. Every incoming history is the ORIGINAL '
               'embedded parent history. All local routes, mixed-bank '
               'injectivity and common output ages are replayed. This does '
               'not glue the cut parent paths, repair parent matching degrees, '
               'preserve arbitrary all-rank targets, or construct a spanning '
               'child factor/word. No alternative parent, rotation, cut, '
               'matching, optimization or search was attempted.'))
    write_json(args.out / 'actual19_mixed_corrected21_connector_bank_certificate.json', report)
    print(json.dumps({key: report[key] for key in (
        'status', 'enumerated_port_count', 'original_route_count',
        'swapped_bad_port_route_count', 'locally_legal_connector_count',
        'all_fixed_ports_have_legal_selected_route', 'elapsed_cpu_seconds',
        'elapsed_wall_seconds')}, sort_keys=True), flush=True)


if __name__ == '__main__':
    main()
