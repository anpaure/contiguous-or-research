#!/usr/bin/env bash
set -u
work=/root/three_box_band_opt
program="$work/three_box_band_opt"
mkdir -p "$work/cases"
printf 'a\tD\tstatus\tseconds\n' > "$work/SUMMARY.tsv"
for a in $(seq 1 20); do
  D=$(( (4*a + 2) / 3 ))
  smt="$work/cases/a${a}_D${D}.smt2"
  log="$work/cases/a${a}_D${D}.log"
  stats="$work/cases/a${a}_D${D}.stats"
  "$program" "$a" "$D" "$smt" 2>"$stats"
  started=$(date +%s)
  timeout 310 z3 -T:300 "$smt" >"$log" 2>&1
  rc=$?
  elapsed=$(( $(date +%s)-started ))
  status=$(head -1 "$log" 2>/dev/null || true)
  printf '%s\t%s\t%s\t%s\n' "$a" "$D" "${status:-rc$rc}" "$elapsed" \
    | tee -a "$work/SUMMARY.tsv"
  grep -E 'full_count|gap_sum' "$log" | tail -4 || true
  if (( rc != 0 )); then break; fi
done
