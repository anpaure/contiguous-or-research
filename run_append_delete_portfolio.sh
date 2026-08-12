#!/usr/bin/env bash
set -u

if [[ $# -ne 3 ]]; then
    echo "usage: $0 core worker workers" >&2
    exit 2
fi

core=$1
worker=$2
workers=$3
root=/root
run_dir=$root/append_delete_runs
mkdir -p "$run_dir"

mapfile -t candidates < <(
    awk '{
        split($1, s, "=");
        split($3, m, "=");
        print m[2], s[2];
    }' "$root/prefix_delete_profiles.txt" |
    sort -n -k1,1 -k2,2 |
    awk '$2 != 102 && $2 != 313 {print $2}'
)

for ((index=worker; index<${#candidates[@]}; index+=workers)); do
    if [[ -e "$run_dir/FOUND" ]]; then
        exit 0
    fi
    skip=${candidates[index]}
    log="$run_dir/skip_${skip}.log"
    out="$run_dir/skip_${skip}.append"
    {
        echo "START skip=$skip core=$core worker=$worker index=$index"
        start=$(date +%s)
        APPEND_SKIP_INDEX="$skip" timeout 300 \
            taskset -c "$core" nice -n 15 \
            "$root/append_completion_sat_skip" 11 12 \
            "$root/k11_upper549_natural_array.txt" "$out" "$((1000+skip))"
        result=$?
        stop=$(date +%s)
        echo "RESULT skip=$skip exit=$result seconds=$((stop-start))"
        if [[ $result -eq 0 ]]; then
            printf 'skip=%s append=%s\n' "$skip" "$out" > "$run_dir/FOUND"
            exit 0
        fi
    } >"$log" 2>&1
done
