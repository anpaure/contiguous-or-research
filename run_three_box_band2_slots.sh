#!/usr/bin/env bash
set -u
work=/root/three_box_exact
program="$work/three_box_band_full"
for extra in 0 1 2 3 4 5; do
  for ((pre=0; pre<=extra; ++pre)); do
    post=$((extra-pre))
    tag="cube_2_band_e${extra}_pre${pre}"
    "$program" gen-band 2 closed "$pre" "$post" "$work/cases/${tag}.cnf" \
      2>"$work/cases/${tag}.stats"
    timeout 90 kissat --sat --time=80 "$work/cases/${tag}.cnf" \
      >"$work/cases/${tag}.log" 2>&1
    rc=$?
    echo "extra=$extra pre=$pre post=$post rc=$rc"
    if (( rc == 10 )); then
      n=$((9+extra))
      "$program" decode 2 2 2 "$n" "$work/cases/${tag}.log" "$work/cases/${tag}.word"
      "$program" verify 2 2 2 "$work/cases/${tag}.word"
      exit 0
    fi
  done
done
