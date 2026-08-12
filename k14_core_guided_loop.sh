#!/usr/bin/env bash
set -u -o pipefail

# Remote-only orchestration for the k=14 delay-two central-row search.
# Heavy work is done by the C++ binaries; this script only chains exact cores.

if (( $# < 2 )); then
    echo "usage: $0 START_PATH PRESERVED_MASK..." >&2
    exit 2
fi

current_path=$1
shift
preserved=("$@")

repair_bin=${REPAIR_BIN:-/root/k14_two_relocations}
factor_bin=${FACTOR_BIN:-/root/pinnable_factor_sat_core}
has_triple_bin=${HAS_TRIPLE_BIN:-/root/has_triple}
cpu=${SEARCH_CPU:-40}
work_prefix=${WORK_PREFIX:-/root/k14_autocore}
max_rounds=${MAX_ROUNDS:-100}
early_defect_swap=${EARLY_DEFECT_SWAP:-0}
target_pick=${TARGET_PICK:-first}
recent_targets=()
if [[ -n "${INITIAL_RECENT_TARGETS:-}" ]]; then
    read -r -a recent_targets <<< "$INITIAL_RECENT_TARGETS"
fi

missing_minimal_member() {
    local path=$1
    shift
    local values=("$@")
    local x y has_smaller
    local candidates=()
    for x in "${values[@]}"; do
        has_smaller=0
        for y in "${values[@]}"; do
            if (( y != x && (y & ~x) == 0 )); then
                has_smaller=1
                break
            fi
        done
        if (( ! has_smaller )); then
            if ! "$has_triple_bin" "$x" < "$path" > /dev/null; then
                candidates+=("$x")
            fi
        fi
    done
    if (( ${#candidates[@]} == 0 )); then
        return 1
    fi
    case "$target_pick" in
        first) echo "${candidates[0]}" ;;
        last) echo "${candidates[${#candidates[@]}-1]}" ;;
        middle) echo "${candidates[${#candidates[@]}/2]}" ;;
        *)
            echo "Unknown TARGET_PICK=$target_pick (expected first, middle, or last)" >&2
            return 2
            ;;
    esac
}

for ((round=1; round<=max_rounds; ++round)); do
    stem="${work_prefix}_r${round}"
    factor_path="${stem}_factor.txt"
    factor_stdout="${stem}_factor.stdout"
    factor_log="${stem}_factor.log"

    echo
    echo "=== CORE ROUND $round ==="
    echo "path=$current_path"
    echo "preserved_count=${#preserved[@]}"
    echo "target_pick=$target_pick recent_protected=${recent_targets[*]}"
    echo "factor_start=$(date -Is)"

    env PIN_CORE=1 taskset -c "$cpu" "$factor_bin" 14 2 "$factor_path" \
        < "$current_path" > "$factor_stdout" 2> >(tee "$factor_log" >&2)
    factor_status=$?
    echo "factor_exit=$factor_status at $(date -Is)"

    if (( factor_status == 0 )); then
        echo "PINNABLE_FACTOR_FOUND path=$current_path factor=$factor_path"
        exit 0
    fi

    core_line=$(sed -n 's/^failed_targets //p' "$factor_log" | tail -n 1)
    if [[ -z "$core_line" ]]; then
        echo "No failed-target core was emitted; stopping." >&2
        exit 4
    fi
    read -r -a core <<< "$core_line"
    target=$(missing_minimal_member "$current_path" "${core[@]}") || {
        echo "Every minimal core member is already a triple; this core needs positional rerouting." >&2
        exit 5
    }

    next_path="${stem}_target_${target}.txt"
    repair_log="${stem}_target_${target}.log"
    echo "core=$core_line"
    echo "promote_target=$target"
    echo "repair_start=$(date -Is) mode=two-relocation"

    taskset -c "$cpu" "$repair_bin" "$target" "${preserved[@]}" \
        < "$current_path" > "$next_path" 2> >(tee "$repair_log" >&2)
    repair_status=$?
    echo "repair_exit=$repair_status at $(date -Is)"

    if grep -q 'best_rank5=0' "$repair_log"; then
        echo "No run-free two-relocation repair; escalating to a third healing relocation."
        if (( early_defect_swap )); then
            env THIRD_REPAIR=1 ALLOW_DEFECT_SWAP=1 \
                PROTECTED_MASKS="${recent_targets[*]}" taskset -c "$cpu" \
                "$repair_bin" "$target" "${preserved[@]}" < "$current_path" \
                > "$next_path" 2> >(tee "$repair_log" >&2)
        else
            env THIRD_REPAIR=1 taskset -c "$cpu" "$repair_bin" \
                "$target" "${preserved[@]}" < "$current_path" \
                > "$next_path" 2> >(tee "$repair_log" >&2)
        fi
        repair_status=$?
        echo "depth3_exit=$repair_status at $(date -Is)"
    fi

    if grep -q 'best_rank5=0' "$repair_log"; then
        echo "Standard depth three failed; allowing a temporary first-move run defect."
        env ALLOW_FIRST_BAD_RUN=1 THIRD_REPAIR=1 taskset -c "$cpu" \
            "$repair_bin" "$target" "${preserved[@]}" < "$current_path" \
            > "$next_path" 2> >(tee "$repair_log" >&2)
        repair_status=$?
        echo "extended_depth3_exit=$repair_status at $(date -Is)"
    fi

    if grep -q 'best_rank5=0' "$repair_log"; then
        echo "Depth three failed; retaining minimum-defect seeds for a fourth relocation."
        env THIRD_REPAIR=1 FOURTH_REPAIR=1 taskset -c "$cpu" \
            "$repair_bin" "$target" "${preserved[@]}" < "$current_path" \
            > "$next_path" 2> >(tee "$repair_log" >&2)
        repair_status=$?
        echo "depth4_exit=$repair_status at $(date -Is)"
    fi

    if grep -q 'best_rank5=0' "$repair_log"; then
        echo "Standard depth four failed; enlarging its first-move neighborhood."
        env ALLOW_FIRST_BAD_RUN=1 THIRD_REPAIR=1 FOURTH_REPAIR=1 \
            taskset -c "$cpu" "$repair_bin" "$target" "${preserved[@]}" \
            < "$current_path" > "$next_path" \
            2> >(tee "$repair_log" >&2)
        repair_status=$?
        echo "extended_depth4_exit=$repair_status at $(date -Is)"
    fi

    if grep -q 'best_rank5=0' "$repair_log"; then
        echo "Zero-defect neighborhood exhausted; permitting a minimum-defect triple exchange."
        env THIRD_REPAIR=1 FOURTH_REPAIR=1 FIFTH_REPAIR=1 \
            ALLOW_DEFECT_SWAP=1 taskset -c "$cpu" "$repair_bin" \
            "$target" "${preserved[@]}" < "$current_path" > "$next_path" \
            2> >(tee "$repair_log" >&2)
        repair_status=$?
        echo "defect_swap_exit=$repair_status at $(date -Is)"
    fi

    if (( repair_status != 0 )) || grep -q 'best_rank5=0' "$repair_log"; then
        echo "REPAIR_FRONTIER target=$target path=$current_path log=$repair_log" >&2
        exit 6
    fi

    surviving=()
    for old_target in "${preserved[@]}"; do
        if "$has_triple_bin" "$old_target" < "$next_path" > /dev/null; then
            surviving+=("$old_target")
        else
            echo "released_promoted_target=$old_target"
        fi
    done
    preserved=("${surviving[@]}" "$target")
    recent_targets+=("$target")
    if (( ${#recent_targets[@]} > 5 )); then
        recent_targets=("${recent_targets[@]:${#recent_targets[@]}-5}")
    fi
    current_path=$next_path
done

echo "Reached MAX_ROUNDS=$max_rounds without a pinnable factor." >&2
exit 7
