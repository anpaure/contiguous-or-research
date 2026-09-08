#!/usr/bin/env bash
set -u
work=/root/three_box_band_opt
program="$work/three_box_band_opt_v3"
printf 'a\tD\tstatus\tseconds\n' > "$work/SECTOR.tsv"
for a in $(seq 1 10); do
  D=$(( (4*a + 2) / 3 ))
  smt="$work/cases/sector_a${a}_D${D}.smt2"
  log="$work/cases/sector_a${a}_D${D}.log"
  "$program" "$a" "$D" "$smt" sector 2>"$work/cases/sector_a${a}_D${D}.stats"
  started=$(date +%s)
  timeout 310 z3 -T:300 "$smt" >"$log" 2>&1
  rc=$?; elapsed=$(( $(date +%s)-started ))
  status=$(head -1 "$log" 2>/dev/null || true)
  printf '%s\t%s\t%s\t%s\n' "$a" "$D" "${status:-rc$rc}" "$elapsed" \
    | tee -a "$work/SECTOR.tsv"
  grep -E 'full_count|gap_sum' "$log" | tail -4 || true
  (( rc == 0 )) || break
done
