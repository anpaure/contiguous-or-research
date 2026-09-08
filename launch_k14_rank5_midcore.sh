#!/usr/bin/env bash
set -u -o pipefail

mapfile -t preserved < /root/k14_rank5_altcore_preserved.args

export SEARCH_CPU=46
export WORK_PREFIX=/root/k14_rank5_midcore
export MAX_ROUNDS=100
export EARLY_DEFECT_SWAP=1
export RANK5_FIRST=1
unset IGNORE_SECONDARY
unset TARGET_MULTIPLICITY_SECOND
export TARGET_MULTIPLICITY_FIRST=1
export TARGET_PICK=middle
export INITIAL_RECENT_TARGETS="3589 3624 6185 6200 8476"
export TIE_SEED=20260725
export REPAIR_BIN=/root/k14_two_relocations_seeded

/root/k14_core_guided_loop.sh \
    /root/k14_rank5_early_r22_target_8476.txt \
    "${preserved[@]}" 2>&1 | tee /root/k14_rank5_midcore_master.log

status=${PIPESTATUS[0]}
echo "rank5_midcore_exit=$status at $(date -Is)"
exec bash
