#!/usr/bin/env bash
set -u

if [[ $# -ne 3 ]]; then
    echo "usage: $0 JOB_INDEX JOB_COUNT CPU" >&2
    exit 2
fi

job_index=$1
job_count=$2
cpu=$3
root=${K11_CASE13_ROOT:-/root/or_k11}
out_dir="$root/case13_job_${job_index}"
mkdir -p "$out_dir"

ordinal=0
for ((upper=1; upper<2048; ++upper)); do
    x=$upper
    bits=0
    while (( x )); do
        ((bits += x & 1))
        ((x >>= 1))
    done
    if [[ $bits -ne 7 ]]; then
        continue
    fi
    if (( ordinal % job_count != job_index )); then
        ((ordinal+=1))
        continue
    fi

    log="$out_dir/$upper.log"
    path="$out_dir/$upper.path"
    if [[ -s $path ]] || grep -q '^UNSAT' "$log" 2>/dev/null; then
        ((ordinal+=1))
        continue
    fi

    timeout 300s env RECOMBINE_EXTRA_UPPER="$upper" \
        taskset -c "$cpu" nice -n 10 "$root/recombine_paths_case13" \
        11 6 "$root/k11_allbase_r7full.txt" \
        "$root/k11_lower956_upper549.txt" "caseinc13:$((130000+upper))" \
        > "$path" 2> "$log"
    code=$?
    printf 'upper=%d code=%d ' "$upper" "$code" >> "$out_dir/summary.log"
    tail -1 "$log" >> "$out_dir/summary.log"
    if [[ -s $path ]]; then
        cp "$path" "$root/k11_case13_solution.txt"
        echo "SAT upper=$upper path=$path" > "$root/k11_case13_solution.status"
        exit 0
    fi
    ((ordinal+=1))
done

echo "job=$job_index complete" >> "$out_dir/summary.log"
