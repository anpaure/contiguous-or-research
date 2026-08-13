#!/usr/bin/env python3
"""Exhaustively verify the signed counters used by the D5 selector.

Substantive execution belongs on H100.  Small repeated-literal instances are
checked against Kissat for both the local sequential counter and PySAT's
k-modulo totalizer.  The signed q2 gain-to-absent-gain transformation is also
checked algebraically on every three-variable coefficient vector in
``{-2,-1,0,1,2}^3`` and several old loads.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import subprocess
import tempfile
from pathlib import Path

import pysat
from pysat.card import CardEnc, EncType

from solve_t2_suffix_d5_split_tree_minimum_sdr_20260814 import at_most_k


def sat_with_assignment(kissat, clauses, variables, values):
    units = [
        [index + 1 if value else -(index + 1)]
        for index, value in enumerate(values)
    ]
    all_clauses = clauses + units
    with tempfile.NamedTemporaryFile(mode="w", suffix=".cnf") as handle:
        handle.write(f"p cnf {variables} {len(all_clauses)}\n")
        for clause in all_clauses:
            handle.write(" ".join(map(str, clause)) + " 0\n")
        handle.flush()
        result = subprocess.run(
            [kissat, "--quiet", handle.name],
            check=False,
            capture_output=True,
        )
    assert result.returncode in (10, 20)
    return result.returncode == 10


def literal_value(literal, values):
    value = values[abs(literal) - 1]
    return value if literal > 0 else not value


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--kissat", required=True)
    args = parser.parse_args()
    menus = [
        [1, 2, 3],
        [1, 1, -2, 3, -3],
        [-1, -1, 2, 2, 3],
    ]
    sequential_checks = 0
    modulo_checks = 0
    for literals in menus:
        for bound in range(len(literals) + 1):
            clauses = []
            next_variable = at_most_k(literals, bound, clauses, 4)
            modulo = CardEnc.atmost(
                lits=literals,
                bound=bound,
                top_id=3,
                encoding=EncType.kmtotalizer,
            )
            for values in itertools.product((False, True), repeat=3):
                expected = sum(
                    literal_value(literal, values) for literal in literals
                ) <= bound
                assert sat_with_assignment(
                    args.kissat, clauses, max(3, next_variable - 1), values
                ) == expected
                sequential_checks += 1
                assert sat_with_assignment(
                    args.kissat, modulo.clauses, max(3, modulo.nv), values
                ) == expected
                modulo_checks += 1

    signed_transform_checks = 0
    for changes in itertools.product(range(-2, 3), repeat=3):
        for old_load in range(1, 4):
            gains = sum(max(change, 0) for change in changes)
            literals = []
            for variable, change in enumerate(changes, 1):
                if change < 0:
                    literals.extend([variable] * -change)
                elif change > 0:
                    literals.extend([-variable] * change)
            bound = old_load - 1 + gains
            for values in itertools.product((False, True), repeat=3):
                direct = old_load + sum(
                    change * values[index]
                    for index, change in enumerate(changes)
                ) >= 1
                transformed = sum(
                    literal_value(literal, values) for literal in literals
                ) <= bound
                assert direct == transformed
                signed_transform_checks += 1

    source = Path(
        "solve_t2_suffix_d5_split_tree_minimum_sdr_20260814.py"
    ).read_bytes()
    print(json.dumps({
        "status": "PASS",
        "sequential_counter_assignments": sequential_checks,
        "k_modulo_totalizer_assignments": modulo_checks,
        "signed_q2_transform_assignments": signed_transform_checks,
        "python_sat_version": pysat.__version__,
        "selector_source_sha256": hashlib.sha256(source).hexdigest(),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
