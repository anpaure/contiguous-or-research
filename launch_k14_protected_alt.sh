#!/usr/bin/env bash
set -u -o pipefail

mapfile -t preserved < /root/k14_protected_alt_preserved.args

export SEARCH_CPU=44
export WORK_PREFIX=/root/k14_protected_upper
export MAX_ROUNDS=100
export EARLY_DEFECT_SWAP=1
unset RANK5_FIRST
export TARGET_PICK=last
export INITIAL_RECENT_TARGETS="2826 3352 10514 4881 309"
export TIE_SEED=20260722
export REPAIR_BIN=/root/k14_two_relocations_seeded

/root/k14_core_guided_loop.sh \
    /root/k14_early_exchange_r33_target_309.txt \
    "${preserved[@]}" 2>&1 | tee /root/k14_protected_upper_master.log

status=${PIPESTATUS[0]}
echo "protected_alt_exit=$status at $(date -Is)"
exec bash
