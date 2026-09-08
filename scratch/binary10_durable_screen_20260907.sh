#!/usr/bin/env bash
# Remote-only durable launcher for the labelled-matching LP screen.
set -uo pipefail
run_dir=$1
shift
source_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
[[ -d "$run_dir" && "$run_dir" == "$source_dir"/run-* ]] || exit 2
printf '%s\n' "$$" > "$run_dir/wrapper.pid"
printf '%s\n' "$(date -u +%FT%TZ)" > "$run_dir/started.utc"
python3 -u "$source_dir/binary10_all_matching_screen_20260907.py" \
    --output "$run_dir" --parallel 4 --seconds 30 "$@" 2>&1 | tee "$run_dir/output.log"
run_status=${PIPESTATUS[0]}
printf '%s\n' "$run_status" > "$run_dir/exit.status"
printf '%s\n' "$(date -u +%FT%TZ)" > "$run_dir/finished.utc"
printf 'REMOTE_SCREEN_EXIT %s\n' "$run_status" | tee -a "$run_dir/output.log"
exit "$run_status"
