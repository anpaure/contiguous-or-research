#!/usr/bin/env bash
set -u -o pipefail

source_factor=${START_FACTOR:-/root/k14_upper_loop_r4_t11251_factor_2.txt}
output=${OUTPUT_FACTOR:-/root/k14_factor_block_2opt_result.txt}

echo "factor_block_2opt_start=$(date -Is) source=$source_factor"
taskset -c 34 /root/k14_factor_block_2opt 10 < "$source_factor" \
    > "$output" 2> >(tee /root/k14_factor_block_2opt.log >&2)
status=$?
echo "factor_block_2opt_exit=$status at $(date -Is) output=$output"
if (( status == 0 )); then
    /root/verify_or_array 14 < "$output" \
        > /root/k14_factor_block_2opt_verification.txt || true
    head -n 20 /root/k14_factor_block_2opt_verification.txt
fi
exec bash
