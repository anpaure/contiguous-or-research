#!/usr/bin/env bash
set -u

work=/root/three_box_exact
program="$work/three_box_exact_sat_pruned"
solver=/usr/local/bin/kissat

run_cube() {
  local side=$1 first=$2 last=$3 limit=$4
  local tag="cube_${side}"
  local summary="$work/${tag}.tsv"
  printf 'side\tn\tstatus\tseconds\n' > "$summary"
  for ((n=first; n<=last; ++n)); do
    local cnf="$work/cases/${tag}_n${n}.cnf"
    local log="$work/cases/${tag}_n${n}.log"
    local word="$work/cases/${tag}_n${n}.word"
    local started=$(date +%s)
    "$program" gen "$side" "$side" "$side" "$n" "$cnf" \
      2> "$work/cases/${tag}_n${n}.stats"
    echo "CUBE side=$side trying n=$n"
    timeout "$((limit+10))" "$solver" --time="$limit" "$cnf" > "$log" 2>&1
    local rc=$?
    local elapsed=$(( $(date +%s) - started ))
    if (( rc == 10 )); then
      "$program" decode "$side" "$side" "$side" "$n" "$log" "$word"
      "$program" verify "$side" "$side" "$side" "$word"
      printf '%s\t%s\tSAT\t%s\n' "$side" "$n" "$elapsed" | tee -a "$summary"
      return 0
    elif (( rc == 20 )); then
      printf '%s\t%s\tUNSAT\t%s\n' "$side" "$n" "$elapsed" | tee -a "$summary"
    else
      printf '%s\t%s\tUNKNOWN\t%s\n' "$side" "$n" "$elapsed" | tee -a "$summary"
      return 1
    fi
  done
  return 1
}

case "${1:-}" in
  4) run_cube 4 22 28 900 ;;
  6) run_cube 6 41 46 1800 ;;
  *) echo 'usage: run_three_box_cubes.sh 4|6' >&2; exit 2 ;;
esac
