#!/usr/bin/env bash
set -u
work=/root/three_box_exact
program="$work/three_box_corner"
current="$work/cube2_band_mus_current.txt"
cp "$work/lower_targets_cube2.txt" "$current"
round=0
while true; do
  round=$((round+1)); changed=0
  start="$work/cube2_band_mus_round${round}.txt"
  cp "$current" "$start"
  while read -r mask; do
    candidate="$work/cube2_band_mus_candidate.txt"
    awk -v drop="$mask" '$1 != drop {print $1}' "$current" > "$candidate"
    "$program" gen-band-keep 2 closed 0 1 "$candidate" "$work/cube2_band_mus.cnf" \
      2>"$work/cube2_band_mus.stats"
    timeout 40 kissat --time=30 "$work/cube2_band_mus.cnf" \
      >"$work/cube2_band_mus_solver.log" 2>&1
    rc=$?
    if (( rc == 20 )); then
      mv "$candidate" "$current"; changed=1
      echo "removed=$mask remaining=$(wc -l < "$current")"
    else
      echo "essential=$mask rc=$rc"
    fi
  done < "$start"
  (( changed == 0 )) && break
done
echo FINAL
cat "$current"
