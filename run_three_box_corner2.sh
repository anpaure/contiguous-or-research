#!/usr/bin/env bash
set -u
work=/root/three_box_exact
program="$work/three_box_corner"
for reverse in 0 1; do
  for phase in 0 1 2 3 4 5; do
    for omit in 0 1 2 3 4 5 6; do
      tag="cube_2_corner_p${phase}_r${reverse}_o${omit}"
      "$program" gen-corner 2 "$phase" "$reverse" "$omit" "$work/cases/${tag}.cnf" \
        2>"$work/cases/${tag}.stats"
      timeout 90 kissat --sat --time=80 "$work/cases/${tag}.cnf" \
        >"$work/cases/${tag}.log" 2>&1
      rc=$?
      echo "phase=$phase reverse=$reverse omit=$omit rc=$rc"
      if (( rc == 10 )); then
        "$program" decode 2 2 2 10 "$work/cases/${tag}.log" "$work/cases/${tag}.word"
        "$program" verify 2 2 2 "$work/cases/${tag}.word"
        cat "$work/cases/${tag}.word"
      fi
    done
  done
done
