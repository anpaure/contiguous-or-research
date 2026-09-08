#!/usr/bin/env bash
set -u
work=/root/three_box_exact
program="$work/three_box_mus"
for n in 14 15 16 17; do
  cnf="$work/cases/cube_3_n${n}.cnf"
  log="$work/cases/cube_3_n${n}.log"
  word="$work/cases/cube_3_n${n}.word"
  "$program" gen 3 3 3 "$n" "$cnf" 2>"$work/cases/cube_3_n${n}.stats"
  echo "cube3 trying n=$n"
  timeout 610 kissat --time=600 "$cnf" >"$log" 2>&1
  rc=$?
  if (( rc == 10 )); then
    "$program" decode 3 3 3 "$n" "$log" "$word"
    "$program" verify 3 3 3 "$word"
    echo "cube3 SAT n=$n"
    exit 0
  elif (( rc == 20 )); then
    echo "cube3 UNSAT n=$n"
  else
    echo "cube3 UNKNOWN n=$n rc=$rc"
    exit 1
  fi
done
