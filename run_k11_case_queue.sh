#!/usr/bin/env bash
set -u

queue_id="$1"
queue_count="$2"
solver_seed="$3"
root_dir="${4:-/root}"

mkdir -p "$root_dir/k11_case13"
index=0
while read -r upper; do
    if (( index % queue_count != queue_id )); then
        ((index += 1))
        continue
    fi
    log="$root_dir/k11_case13/case_${upper}.log"
    out="$root_dir/k11_case13/case_${upper}.txt"
    if [[ -s "$out" ]]; then
        exit 0
    fi
    RECOMBINE_EXTRA_UPPER="$upper" \
    RECOMBINE_TARGETS="$root_dir/k11_initial_targets.txt" \
        "$root_dir/recombine_paths_sat_new" \
        11 6 \
        "$root_dir/k11_lower956_upper549.txt" \
        "$root_dir/k11_lower956_upper549.txt" \
        "caseinc13:$((solver_seed + index))" >"$out" 2>"$log"
    status=$?
    if (( status == 0 )) && [[ -s "$out" ]]; then
        printf 'SAT upper=%s output=%s\n' "$upper" "$out" \
            >"$root_dir/k11_case13/SAT_FOUND.txt"
        exit 0
    fi
    rm -f "$out"
    ((index += 1))
done <"$root_dir/k11_rank7_masks.txt"
