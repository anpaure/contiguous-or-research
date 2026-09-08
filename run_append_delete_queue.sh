#!/usr/bin/env bash
set -u

if [[ $# -ne 1 ]]; then
    echo "usage: $0 core" >&2
    exit 2
fi

core=$1
root=/root
run_dir=$root/append_delete_runs

mapfile -t candidates < <(
    awk '{
        split($1, s, "=");
        split($3, m, "=");
        print m[2], s[2];
    }' "$root/prefix_delete_profiles.txt" |
    sort -n -k1,1 -k2,2 |
    awk '$2 != 102 && $2 != 313 {print $2}'
)

for skip in "${candidates[@]}"; do
    [[ -e "$run_dir/FOUND" ]] && exit 0
    log="$run_dir/skip_${skip}.log"
    [[ -e "$log" ]] && continue
    lock="$run_dir/lock_${skip}"
    mkdir "$lock" 2>/dev/null || continue
    out="$run_dir/skip_${skip}.append"
    {
        echo "START skip=$skip core=$core queue=1"
        start=$(date +%s)
        APPEND_SKIP_INDEX="$skip" timeout 300 \
            taskset -c "$core" nice -n 15 \
            "$root/append_completion_sat_skip" 11 12 \
            "$root/k11_upper549_natural_array.txt" "$out" "$((2000+skip))"
        result=$?
        stop=$(date +%s)
        echo "RESULT skip=$skip exit=$result seconds=$((stop-start))"
        if [[ $result -eq 0 ]]; then
            printf 'skip=%s append=%s\n' "$skip" "$out" > "$run_dir/FOUND"
            exit 0
        fi
    } >"$log" 2>&1
done
