#!/usr/bin/env bash
set -u

j="$1"
source_file="/root/or_search_logs/q9_${j}.txt"
cnf_file="/tmp/fq9_${j}.cnf"
model_file="/tmp/fq9_${j}.model"
done_file="/root/or_search_logs/q9_test_${j}.done"

tested=0
while IFS= read -r q; do
    tested=$((tested + 1))
    printf '%s\n' "$q" | /root/fixed_q_sat generate "$cnf_file" low 9 >/dev/null 2>&1
    /root/kissat/build/kissat --quiet "$cnf_file" > "$model_file"
    if grep -q '^s SATISFIABLE' "$model_file"; then
        printf '%s\n' "$q" > "/root/or_search_logs/Q9_SAT_${j}"
        printf '%s\n' "$q" |
            /root/fixed_q_sat decode "$model_file" low 9 > "/root/or_search_logs/A9_SAT_${j}"
        printf 'FOUND %d\n' "$tested" > "$done_file"
        exit 0
    fi
done < "$source_file"

printf 'NONE %d\n' "$tested" > "$done_file"
