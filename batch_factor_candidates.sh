#!/usr/bin/env bash
set -u

candidate_dir=${1:?candidate directory required}
count=${2:?candidate count required}
output_dir=${3:?output directory required}
parallelism=${4:-8}

mkdir -p "$output_dir"
: > "$output_dir/status.txt"

run_one() {
    local index=$1
    local candidate_stem=${CANDIDATE_STEM:-cand_}
    local cpu_list=${CPU_LIST:-34,35,36,38,39,40,43,44}
    local cpus
    IFS=',' read -r -a cpus <<< "$cpu_list"
    local cpu=${cpus[$(((index - 1) % ${#cpus[@]}))]}
    env PIN_CORE=1 taskset -c "$cpu" /root/pinnable_factor_sat_core 14 2 \
        "$output_dir/factor_${index}.txt" \
        < "$candidate_dir/${candidate_stem}${index}.txt" \
        > "$output_dir/factor_${index}.stdout" \
        2> "$output_dir/factor_${index}.log"
    local result=$?
    printf '%s %s\n' "$index" "$result" >> "$output_dir/status.txt"
}

export candidate_dir output_dir parallelism CPU_LIST CANDIDATE_STEM
export -f run_one
seq 1 "$count" | xargs -P "$parallelism" -n 1 bash -c 'run_one "$1"' _
