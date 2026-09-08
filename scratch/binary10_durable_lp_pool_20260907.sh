#!/usr/bin/env bash
# Run only on h100; persist output and terminal status independently of SSH.
set -uo pipefail
run_dir=$1
shift
source_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
[[ -d "$run_dir" && "$run_dir" == "$source_dir"/run-* ]] || exit 2
printf '%s\n' "$$" > "$run_dir/wrapper.pid"
printf '%s\n' "$(date -u +%FT%TZ)" > "$run_dir/started.utc"
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3 -u \
    "$source_dir/binary10_lp_guided_pool_20260907.py" --output "$run_dir" "$@" \
    2>&1 | tee "$run_dir/output.log"
run_status=${PIPESTATUS[0]}
printf '%s\n' "$run_status" > "$run_dir/exit.status"
printf '%s\n' "$(date -u +%FT%TZ)" > "$run_dir/finished.utc"
printf 'REMOTE_POOL_EXIT %s\n' "$run_status" | tee -a "$run_dir/output.log"
exit "$run_status"
