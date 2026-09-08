#!/usr/bin/env bash
set -u

distance="$1"
support_cap="$2"
solver_seed="$3"
cd /root/or_k11 || exit 1

prefix="corrected_allinc${distance}"

env \
    RECOMBINE_EXTRA_SUPPORT="$support_cap" \
    RECOMBINE_DUMP_CNF="${prefix}.cnf" \
    RECOMBINE_DUMP_ONLY=1 \
    ./recombine_paths_sat_support \
        11 6 \
        k11_allbase_r7full.txt \
        k11_lower956_upper549.txt \
        "allinc${distance}:${solver_seed}" \
        >"${prefix}_dump.out" 2>"${prefix}_dump.log"

kissat --seed="$solver_seed" "${prefix}.cnf" "${prefix}.drat" \
    >"${prefix}_kissat.log" 2>&1
kissat_status=$?
if [[ "$kissat_status" -ne 20 ]]; then
    echo "unexpected kissat status $kissat_status" >&2
    exit "$kissat_status"
fi

awk '
    NR == 1 { header_vars=$3; header_clauses=$4; next }
    {
        if ($NF != 0) { print "bad_terminator", NR; exit 2 }
        ++actual_clauses
        for (i=1; i<NF; ++i) {
            value=$i < 0 ? -$i : $i
            if (value > max_variable) max_variable=value
        }
    }
    END {
        print "header_vars", header_vars,
              "header_clauses", header_clauses,
              "actual_maxvar", max_variable,
              "actual_clauses", actual_clauses
        if (header_vars != max_variable || header_clauses != actual_clauses)
            exit 3
    }
' "${prefix}.cnf" >"${prefix}_dimacs_audit.log"

/root/drat-trim "${prefix}.cnf" "${prefix}.drat" \
    >"${prefix}_dratcheck.log" 2>&1

sha256sum \
    "${prefix}.cnf" \
    "${prefix}.drat" \
    "${prefix}_kissat.log" \
    "${prefix}_dratcheck.log" \
    recombine_paths_sat_support.cpp \
    k11_lower956_upper549.txt \
    >"${prefix}.sha256"
