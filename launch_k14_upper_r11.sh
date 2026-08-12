#!/usr/bin/env bash
set -u -o pipefail

cpu=32
target=10175
prefix=/root/k14_upper10175_candidate_
source_path=/root/k14_rank5_seeded_r10_target_6405.txt

rm -f "${prefix}"*.txt /root/k14_upper10175_factor_*.txt

echo "upper_repair_start=$(date -Is) target=$target source=$source_path"
env DUMP_PREFIX="$prefix" TOP_K=64 \
    taskset -c "$cpu" /root/k14_upper_relocate "$target" \
    < "$source_path" > /root/k14_upper10175_best.txt \
    2> >(tee /root/k14_upper10175_relocate.log >&2)
repair_status=$?
echo "upper_repair_exit=$repair_status at $(date -Is)"

if (( repair_status != 0 )); then
    exec bash
fi

for i in $(seq 0 63); do
    candidate="${prefix}${i}.txt"
    [[ -f "$candidate" ]] || continue
    factor="/root/k14_upper10175_factor_${i}.txt"
    log="/root/k14_upper10175_factor_${i}.log"
    echo "factor_candidate=$i start=$(date -Is)"
    taskset -c "$cpu" /root/pinnable_factor_sat_core 14 2 "$factor" \
        < "$candidate" > /root/k14_upper10175_factor_${i}.stdout \
        2> >(tee "$log" >&2)
    status=$?
    echo "factor_candidate=$i exit=$status at $(date -Is)"
    if (( status == 0 )); then
        echo "PINNABLE_UPPER_REPAIR_FOUND candidate=$candidate factor=$factor"
        /root/verify_k14_live_path < "$candidate" \
            > /root/k14_upper10175_central_verification.txt
        /root/verify_or_array 14 < "$factor" \
            > /root/k14_upper10175_factor_verification.txt || true
        cat /root/k14_upper10175_central_verification.txt
        head -n 18 /root/k14_upper10175_factor_verification.txt
        exec bash
    fi
done

echo "UPPER_REPAIR_FACTOR_FRONTIER target=$target tested=64"
exec bash
