#!/usr/bin/env bash
set -u -o pipefail

mapfile -t preserved < /root/k14_rank5_altcore_preserved.args

export SEARCH_CPU=47
export WORK_PREFIX=/root/k14_rank5_altcore
export MAX_ROUNDS=100
export EARLY_DEFECT_SWAP=1
export RANK5_FIRST=1
export TARGET_PICK=last
export INITIAL_RECENT_TARGETS="3589 3624 6185 6200 8476"
export TIE_SEED=20260724
export REPAIR_BIN=/root/k14_two_relocations_seeded

/root/k14_core_guided_loop.sh \
    /root/k14_rank5_early_r22_target_8476.txt \
    "${preserved[@]}" 2>&1 | tee /root/k14_rank5_altcore_master.log

status=${PIPESTATUS[0]}
echo "rank5_altcore_exit=$status at $(date -Is)"
exec bash
