#!/usr/bin/env bash
# Execute only on h100. The caller supplies a unique, existing run directory.
set -uo pipefail

run_dir=$1
shift
source_dir=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
if [[ ! -d "$run_dir" || "$run_dir" != "$source_dir"/run-* ]]; then
    printf 'Refusing non-run output directory: %s\n' "$run_dir" >&2
    exit 2
fi

printf '%s\n' "$$" > "$run_dir/wrapper.pid"
printf '%s\n' "$(date -u +%FT%TZ)" > "$run_dir/started.utc"
printf 'BINARY10_FIXED_MATCHING=%s\nBINARY10_MATCHING_INDEX=%s\nBINARY10_CORE_FIRST_ORDER=%s\nBINARY10_LAST_VARIANT=%s\n' \
    "${BINARY10_FIXED_MATCHING-}" "${BINARY10_MATCHING_INDEX-}" \
    "${BINARY10_CORE_FIRST_ORDER-}" "${BINARY10_LAST_VARIANT-}" > "$run_dir/environment.txt"
cp "$source_dir/binary10_involution_completion_20260907.py" \
    "$source_dir/binary10_involution_matching_core_20260907.py" \
    "$source_dir/binary10_involution_scd_core_20260907.py" \
    "$source_dir/binary10_involution_catalogue_20260907.cpp" "$run_dir/"
sha256sum "$run_dir"/*.py "$run_dir"/*.cpp > "$run_dir/sources.sha256"
printf '%q ' python3 -u "$source_dir/binary10_involution_completion_20260907.py" "$@" > "$run_dir/command.txt"
printf '\n' >> "$run_dir/command.txt"

python3 -u "$source_dir/binary10_involution_completion_20260907.py" "$@" \
    2>&1 | tee "$run_dir/output.log"
run_status=${PIPESTATUS[0]}
printf '%s\n' "$run_status" > "$run_dir/exit.status"
printf '%s\n' "$(date -u +%FT%TZ)" > "$run_dir/finished.utc"
printf 'REMOTE_RUN_EXIT %s\n' "$run_status" | tee -a "$run_dir/output.log"
exit "$run_status"
