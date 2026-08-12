#!/usr/bin/env bash
set -u
work=/root/three_box_exact
program="$work/three_box_drop"
summary="$work/cube222_drop.tsv"
printf 'mask\tstatus\tseconds\n' > "$summary"
targets=(1 3 4 5 7 12 13 15 16 17 19 20 21 23 28 29 31 48 49 51 52 53 55 60 61 63)
for mask in "${targets[@]}"; do
  cnf="$work/cases/cube222_drop_${mask}.cnf"
  log="$work/cases/cube222_drop_${mask}.log"
  started=$(date +%s)
  "$program" gen-drop 2 2 2 9 "$mask" "$cnf" 2>"$work/cases/cube222_drop_${mask}.stats"
  timeout 70 kissat --time=60 "$cnf" >"$log" 2>&1
  rc=$?
  elapsed=$(( $(date +%s) - started ))
  if (( rc == 10 )); then status=SAT;
  elif (( rc == 20 )); then status=UNSAT;
  else status=UNKNOWN; fi
  printf '%s\t%s\t%s\n' "$mask" "$status" "$elapsed" | tee -a "$summary"
done
