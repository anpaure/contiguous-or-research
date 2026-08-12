#!/usr/bin/env bash
set -u -o pipefail

mapfile -t preserved < /root/k14_rank5_seeded_preserved.args

export SEARCH_CPU=40
export WORK_PREFIX=/root/k14_rank5_seeded
export MAX_ROUNDS=100
export EARLY_DEFECT_SWAP=1
export RANK5_FIRST=1
export TARGET_PICK=first
export INITIAL_RECENT_TARGETS="2571 2698 5139 10912 651"
export TIE_SEED=20260723
export REPAIR_BIN=/root/k14_two_relocations_seeded

/root/k14_core_guided_loop.sh \
    /root/k14_rank5_early_r16_target_651.txt \
    "${preserved[@]}" 2>&1 | tee /root/k14_rank5_seeded_master.log

status=${PIPESTATUS[0]}
echo "rank5_seeded_exit=$status at $(date -Is)"
exec bash
