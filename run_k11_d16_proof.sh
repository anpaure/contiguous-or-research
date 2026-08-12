#!/usr/bin/env bash
set -u
cd /root/or_k11 || exit 1

kissat --seed=61616 corrected_allinc16.cnf corrected_allinc16.drat \
    > corrected_allinc16_kissat.log 2>&1
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
' corrected_allinc16.cnf > corrected_allinc16_dimacs_audit.log

/root/drat-trim corrected_allinc16.cnf corrected_allinc16.drat \
    > corrected_allinc16_dratcheck.log 2>&1

sha256sum \
    corrected_allinc16.cnf \
    corrected_allinc16.drat \
    corrected_allinc16_kissat.log \
    corrected_allinc16_dratcheck.log \
    recombine_paths_sat_support.cpp \
    k11_lower956_upper549.txt \
    > corrected_allinc16.sha256
