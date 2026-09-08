#!/usr/bin/env bash
set -euo pipefail

if (( $# != 7 )); then
  echo "usage: $0 solver prefix missing seed output_dir timeout_seconds cores_csv" >&2
  echo "example cores_csv: 5,26,35,39" >&2
  exit 2
fi

solver=$1
prefix=$2
missing=$3
seed=$4
output_dir=$5
timeout_seconds=$6
cores_csv=$7

mkdir -p "$output_dir"
IFS=',' read -r -a cores <<< "$cores_csv"
if (( ${#cores[@]} == 0 )); then
  echo "no cores supplied" >&2
  exit 2
fi

mapfile -t branches < <(
  "$solver" --list "$prefix" "$missing" | sed -n '/^branch=/p'
)
if (( ${#branches[@]} != 52 )); then
  echo "expected 52 exact branches, got ${#branches[@]}" >&2
  exit 2
fi
printf '%s\n' "${branches[@]}" > "$output_dir/branch_manifest.txt"

run_worker() {
  local worker=$1 core=$2
  local index line branch x pattern f h stem rc proof_path
  for ((index=worker; index<${#branches[@]}; index+=${#cores[@]})); do
    line=${branches[index]}
    if [[ ! $line =~ branch=([0-9]+)\ x=([0-9]+)\ pattern=([0-9]+)\ f=([0-9]+)\ h=([0-9]+) ]]; then
      echo "cannot parse manifest line: $line" >&2
      exit 2
    fi
    branch=${BASH_REMATCH[1]}
    x=${BASH_REMATCH[2]}
    pattern=${BASH_REMATCH[3]}
    f=${BASH_REMATCH[4]}
    h=${BASH_REMATCH[5]}
    stem="$output_dir/branch_${branch}_x${x}_p${pattern}_f${f}_h${h}"
    proof_path=
    if [[ -n ${K14_APPEND241_PROOF_DIR:-} ]]; then
      mkdir -p "$K14_APPEND241_PROOF_DIR"
      proof_path="$K14_APPEND241_PROOF_DIR/$(basename "$stem").drat"
    fi
    echo "START $(date -Is) core=$core $line" > "$stem.status"
    set +e
    if [[ -n $proof_path ]]; then
      K14_APPEND241_PROOF=$proof_path \
        timeout "${timeout_seconds}s" taskset -c "$core" \
        "$solver" "$prefix" "$missing" "$seed" "$stem.append.txt" \
        "$((branch + 1))" "$x" "$pattern" "$f" \
        > "$stem.stdout" 2> "$stem.stderr"
    else
      timeout "${timeout_seconds}s" taskset -c "$core" \
        "$solver" "$prefix" "$missing" "$seed" "$stem.append.txt" \
        "$((branch + 1))" "$x" "$pattern" "$f" \
        > "$stem.stdout" 2> "$stem.stderr"
    fi
    rc=$?
    set -e
    case $rc in
      0) status=SAT ;;
      20) status=UNSAT_UNCHECKED ;;
      124|137) status=TIMEOUT ;;
      *) status="EXIT_$rc" ;;
    esac
    echo "END $(date -Is) core=$core branch=$branch status=$status rc=$rc" \
      >> "$stem.status"
  done
}

pids=()
for ((worker=0; worker<${#cores[@]}; ++worker)); do
  run_worker "$worker" "${cores[worker]}" &
  pids+=("$!")
done
for pid in "${pids[@]}"; do
  wait "$pid"
done

echo "All 52 branches terminated.  A solver exit 20 is not a proved global"
echo "UNSAT until every branch proof is independently checked."
