#!/usr/bin/env bash
set -u -o pipefail

cpu=32
current_path=${START_PATH:-/root/k14_upper10175_candidate_0.txt}
current_factor=${START_FACTOR:-/root/k14_upper10175_factor_0.txt}
work=${WORK_PREFIX:-/root/k14_upper_loop}
max_rounds=400

for ((round=1; round<=max_rounds; ++round)); do
    missing_file="${work}_r${round}_missing.txt"
    /root/list_missing_k14_upper < "$current_path" > "$missing_file"
    current_missing=$(wc -l < "$missing_file")
    echo
    echo "UPPER_ROUND=$round path=$current_path missing=$current_missing start=$(date -Is)"
    if (( current_missing == 0 )); then
        echo "UPPER_COMPLETE path=$current_path factor=$current_factor"
        /root/verify_k14_live_path < "$current_path" > "${work}_complete_central_verification.txt"
        /root/verify_or_array 14 < "$current_factor" > "${work}_complete_factor_verification.txt"
        cat "${work}_complete_central_verification.txt"
        head -n 20 "${work}_complete_factor_verification.txt"
        exec bash
    fi

    accepted=0
    while read -r target; do
        prefix="${work}_r${round}_t${target}_candidate_"
        relocate_log="${work}_r${round}_t${target}_relocate.log"
        rm -f "${prefix}"*.txt
        echo "upper_target=$target relocate_start=$(date -Is)"
        env DUMP_PREFIX="$prefix" TOP_K=24 \
            taskset -c "$cpu" /root/k14_upper_relocate "$target" \
            < "$current_path" > "${work}_r${round}_t${target}_best.txt" \
            2> >(tee "$relocate_log" >&2)
        relocate_status=$?
        echo "upper_target=$target relocate_exit=$relocate_status at $(date -Is)"
        (( relocate_status == 0 )) || continue

        for i in $(seq 0 23); do
            candidate="${prefix}${i}.txt"
            [[ -f "$candidate" ]] || continue
            candidate_missing_file="${work}_r${round}_t${target}_candidate_${i}_missing.txt"
            /root/list_missing_k14_upper < "$candidate" > "$candidate_missing_file"
            candidate_missing=$(wc -l < "$candidate_missing_file")
            if (( candidate_missing >= current_missing )); then
                echo "upper_target=$target factor_candidate=$i skipped_nonimproving candidate_missing=$candidate_missing"
                continue
            fi
            factor="${work}_r${round}_t${target}_factor_${i}.txt"
            factor_log="${work}_r${round}_t${target}_factor_${i}.log"
            echo "upper_target=$target factor_candidate=$i start=$(date -Is)"
            taskset -c "$cpu" /root/pinnable_factor_sat_core 14 2 "$factor" \
                < "$candidate" > "${factor}.stdout" \
                2> >(tee "$factor_log" >&2)
            factor_status=$?
            echo "upper_target=$target factor_candidate=$i exit=$factor_status at $(date -Is)"
            (( factor_status == 0 )) || continue

            echo "upper_target=$target factor_candidate=$i candidate_missing=$candidate_missing"
            if (( candidate_missing < current_missing )); then
                current_path=$candidate
                current_factor=$factor
                accepted=1
                echo "UPPER_ACCEPT round=$round target=$target candidate=$i missing=$candidate_missing path=$current_path factor=$current_factor"
                break 2
            fi
        done
    done < "$missing_file"

    if (( ! accepted )); then
        echo "UPPER_LOCAL_FRONTIER round=$round missing=$current_missing path=$current_path factor=$current_factor"
        exec bash
    fi
done

echo "UPPER_MAX_ROUNDS path=$current_path factor=$current_factor"
exec bash
