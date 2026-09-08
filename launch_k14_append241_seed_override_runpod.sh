#!/usr/bin/env bash
set -euo pipefail

if (( $# != 11 )); then
  echo "usage: $0 solver prefix missing seed242 verify_array verify_suffix output_dir timeout_seconds core branch sat_seed" >&2
  echo "supported construction-led branches: 5 and 36" >&2
  exit 2
fi

solver=$1
prefix=$2
missing=$3
seed242=$4
verify_array=$5
verify_suffix=$6
output_dir=$7
timeout_seconds=$8
core=$9
branch=${10}
sat_seed=${11}

case $branch in
  5)
    x=1
    pattern=5
    f=2
    expected_phase_sha=ef5abe185f628a3bbbbfc70c90f8f74d31281226910c2f4525b21f519201c6a9
    ;;
  36)
    x=2
    pattern=23
    f=2
    expected_phase_sha=692f3c15be148eff0b03554c736b2b601a683861fa8bfc55acd18d9264dceb3a
    ;;
  *)
    echo "branch must be 5 or 36" >&2
    exit 2
    ;;
esac

[[ $timeout_seconds =~ ^[1-9][0-9]*$ ]] || {
  echo "timeout_seconds must be a positive integer" >&2
  exit 2
}
[[ $core =~ ^[0-9]+$ ]] || {
  echo "core must be a nonnegative integer" >&2
  exit 2
}
[[ $sat_seed =~ ^[1-9][0-9]*$ ]] || {
  echo "sat_seed must be a positive integer" >&2
  exit 2
}

for executable in "$solver" "$verify_array" "$verify_suffix"; do
  [[ -x $executable ]] || {
    echo "not executable: $executable" >&2
    exit 2
  }
done

check_sha() {
  local path=$1 expected=$2 actual
  actual=$(sha256sum "$path" | awk '{print $1}')
  if [[ $actual != "$expected" ]]; then
    echo "SHA-256 mismatch for $path: $actual != $expected" >&2
    exit 2
  fi
}

# These hashes bind the exact audited decision problem and the frozen remote
# build.  Use a newly audited launcher instead of weakening a check in place.
check_sha "$solver" 236f3e1597aa9d7590e974915b2cecb73749eded640cae9529d82a173b585231
check_sha "$prefix" 4c71a5e59985ff8d78a4ae80845defd21cebfe240c16ad4604b57e9b9cb999ad
check_sha "$missing" 152e7e9d951e96c0600875d674f78333b634622e4c34262f44de51053fbd64ab
check_sha "$seed242" 41d7028668cde93d6f9347ae881b352dfbc3de446845324a185b21414099d8a8
check_sha "$verify_array" f48f6c33e5ebcd61cc1dbdb4f495712f5b25d573ddfbaafbc41bbfcb56b7de15
check_sha "$verify_suffix" 0c0733359c04afdd7456330b303811a7f4f989b19243aaa7e8cd4c29e473b509

prefix_tokens=$(awk '{n += NF} END {print n + 0}' "$prefix")
seed_tokens=$(awk '{n += NF} END {print n + 0}' "$seed242")
[[ $prefix_tokens == 3434 ]] || {
  echo "prefix has $prefix_tokens tokens, expected 3434" >&2
  exit 2
}
[[ $seed_tokens == 242 ]] || {
  echo "phase seed source has $seed_tokens tokens, expected 242" >&2
  exit 2
}

mkdir -p "$output_dir"
stem="$output_dir/branch_${branch}_x${x}_p${pattern}_f${f}_seed${sat_seed}"
if compgen -G "$stem.*" > /dev/null; then
  echo "refusing to overwrite existing artifacts for $stem" >&2
  exit 73
fi
phase_seed="$stem.phase.txt"

# Phase-only transformations; neither file is constrained by a CNF clause.
# Branch 5 keeps 259/260 exact target phases and prefers its forced crossing.
# Branch 36 keeps 257/260 and prefers both forced crossings.  The deletion at
# one-based position 205 removes the shorter literal witness for 15407.
if (( branch == 5 )); then
  awk '{for (i=1;i<=NF;i++) print $i}' "$seed242" |
    awk 'NR <= 241 {if (NR == 1) $1=1031; print}' > "$phase_seed"
else
  awk '{for (i=1;i<=NF;i++) print $i}' "$seed242" |
    awk 'NR == 205 {next} {if (NR == 1) $1=1031; if (NR == 2) $1=7182; print}' \
      > "$phase_seed"
fi

phase_tokens=$(awk '{n += NF} END {print n + 0}' "$phase_seed")
[[ $phase_tokens == 241 ]] || {
  echo "generated phase seed has $phase_tokens tokens, expected 241" >&2
  exit 2
}
if ! awk '($1 <= 0 || $1 >= 16384) {bad=1} END {exit bad}' "$phase_seed"; then
  echo "generated phase seed contains an invalid mask" >&2
  exit 2
fi
check_sha "$phase_seed" "$expected_phase_sha"

# A successful taskset probe proves that the requested CPU is in this
# process's allowed affinity mask.  The separate occupancy test prevents an
# accidental launch on a core already carrying a CPU-bound worker.
if ! taskset -c "$core" true 2>/dev/null; then
  echo "core $core is not available in this process's CPU affinity mask" >&2
  exit 75
fi
busy_core=$(
  ps -eLo pid=,tid=,psr=,pcpu=,comm= |
    awk -v core="$core" -v self="$$" \
      '$3 == core && $1 != self && ($4 + 0) >= 1.0 {print; found=1} END {exit !found}' || true
)
if [[ -n $busy_core ]]; then
  echo "core $core is not idle (threads at or above 1% CPU):" >&2
  printf '%s\n' "$busy_core" >&2
  exit 75
fi

# Two concurrent searches need this check to pass independently.  The 5 GiB
# default is per launch; the 4 GiB virtual-memory ceiling below is per solver.
min_headroom_bytes=${K14_MIN_HEADROOM_BYTES:-5368709120}
if [[ -r /sys/fs/cgroup/memory/memory.usage_in_bytes &&
      -r /sys/fs/cgroup/memory/memory.limit_in_bytes ]]; then
  used=$(< /sys/fs/cgroup/memory/memory.usage_in_bytes)
  limit=$(< /sys/fs/cgroup/memory/memory.limit_in_bytes)
  headroom=$((limit - used))
elif [[ -r /sys/fs/cgroup/memory.current &&
        -r /sys/fs/cgroup/memory.max &&
        $(< /sys/fs/cgroup/memory.max) != max ]]; then
  used=$(< /sys/fs/cgroup/memory.current)
  limit=$(< /sys/fs/cgroup/memory.max)
  headroom=$((limit - used))
else
  headroom=$(awk '/^MemAvailable:/ {printf "%.0f\n", $2 * 1024}' /proc/meminfo)
fi
if (( headroom < min_headroom_bytes )); then
  echo "insufficient memory headroom: $headroom < $min_headroom_bytes" >&2
  exit 75
fi

free_bytes=$(df -PB1 "$output_dir" | awk 'NR==2 {print $4}')
min_free_bytes=${K14_MIN_FREE_BYTES:-1073741824}
if (( free_bytes < min_free_bytes )); then
  echo "insufficient output-disk headroom: $free_bytes < $min_free_bytes" >&2
  exit 75
fi

proof_path=
if [[ -n ${K14_APPEND241_PROOF_DIR:-} ]]; then
  mkdir -p "$K14_APPEND241_PROOF_DIR"
  proof_free=$(df -PB1 "$K14_APPEND241_PROOF_DIR" | awk 'NR==2 {print $4}')
  proof_min=${K14_PROOF_MIN_FREE_BYTES:-53687091200}
  if (( proof_free < proof_min )); then
    echo "proof tracing requires $proof_min free bytes; found $proof_free" >&2
    exit 75
  fi
  proof_path="$K14_APPEND241_PROOF_DIR/$(basename "$stem").drat"
fi

{
  echo "START $(date -Is) host=$(hostname) core=$core branch=$branch x=$x pattern=$pattern f=$f sat_seed=$sat_seed"
  echo "solver_sha=$(sha256sum "$solver" | awk '{print $1}')"
  echo "prefix_sha=$(sha256sum "$prefix" | awk '{print $1}')"
  echo "missing_sha=$(sha256sum "$missing" | awk '{print $1}')"
  echo "seed242_sha=$(sha256sum "$seed242" | awk '{print $1}')"
  echo "phase_sha=$(sha256sum "$phase_seed" | awk '{print $1}')"
  echo "verify_array_sha=$(sha256sum "$verify_array" | awk '{print $1}')"
  echo "verify_suffix_sha=$(sha256sum "$verify_suffix" | awk '{print $1}')"
  echo "headroom_bytes=$headroom free_bytes=$free_bytes proof_path=${proof_path:-none}"
} > "$stem.status"

vm_limit_kib=${K14_VM_LIMIT_KIB:-4194304}
time_prefix=()
if [[ -x /usr/bin/time ]]; then
  time_prefix=(/usr/bin/time -v)
fi
set +e
(
  ulimit -v "$vm_limit_kib"
  if [[ -n $proof_path ]]; then
    K14_APPEND241_PROOF=$proof_path \
      "${time_prefix[@]}" timeout --kill-after=30s "${timeout_seconds}s" \
      taskset -c "$core" "$solver" "$prefix" "$missing" "$phase_seed" \
      "$stem.append.txt" "$sat_seed" "$x" "$pattern" "$f"
  else
    "${time_prefix[@]}" timeout --kill-after=30s "${timeout_seconds}s" \
      taskset -c "$core" "$solver" "$prefix" "$missing" "$phase_seed" \
      "$stem.append.txt" "$sat_seed" "$x" "$pattern" "$f"
  fi
) > "$stem.stdout" 2> "$stem.stderr"
rc=$?
set -e

status=
case $rc in
  0)
    [[ -s $stem.append.txt ]] || {
      echo "solver returned SAT without a nonempty append file" >&2
      exit 3
    }
    append_tokens=$(awk '{n += NF} END {print n + 0}' "$stem.append.txt")
    [[ $append_tokens == 241 ]] || {
      echo "SAT output has $append_tokens tokens, expected 241" >&2
      exit 3
    }
    if ! awk '($1 <= 0 || $1 >= 16384) {bad=1} END {exit bad}' "$stem.append.txt"; then
      echo "SAT output contains an invalid mask" >&2
      exit 3
    fi
    full=$(mktemp "$output_dir/k14_3675.XXXXXX.txt")
    trap 'rm -f "${full:-}"' EXIT
    awk '{for (i=1;i<=NF;i++) print $i}' "$prefix" > "$full"
    awk '{for (i=1;i<=NF;i++) print $i}' "$stem.append.txt" >> "$full"
    full_tokens=$(awk '{n += NF} END {print n + 0}' "$full")
    [[ $full_tokens == 3675 ]] || {
      echo "combined candidate has $full_tokens tokens, expected 3675" >&2
      exit 3
    }
    if ! "$verify_array" 14 < "$full" > "$stem.verify_array.txt"; then
      echo "END $(date -Is) branch=$branch sat_seed=$sat_seed status=SAT_REJECTED_ARRAY rc=3" >> "$stem.status"
      exit 3
    fi
    if ! "$verify_suffix" 14 "$full" > "$stem.verify_suffix.txt"; then
      echo "END $(date -Is) branch=$branch sat_seed=$sat_seed status=SAT_REJECTED_SUFFIX rc=3" >> "$stem.status"
      exit 3
    fi
    mv "$full" "$stem.VERIFIED.full.txt"
    trap - EXIT
    cp "$stem.append.txt" "$stem.VERIFIED.append.txt"
    sha256sum "$stem.VERIFIED.append.txt" "$stem.VERIFIED.full.txt" \
      > "$stem.VERIFIED.sha256"
    status=SAT_VERIFIED
    ;;
  20)
    if [[ -n $proof_path && -s $proof_path ]]; then
      status=UNSAT_TRACE_UNCHECKED
    else
      status=UNSAT_UNCHECKED
    fi
    ;;
  124) status=TIMEOUT ;;
  137) status=KILLED_137_UNCLASSIFIED ;;
  *) status="EXIT_$rc" ;;
esac

if [[ -n $proof_path && $rc != 20 && -e $proof_path ]]; then
  mv "$proof_path" "$proof_path.INCOMPLETE"
fi
echo "END $(date -Is) branch=$branch sat_seed=$sat_seed status=$status rc=$rc" \
  >> "$stem.status"
echo "$status"
