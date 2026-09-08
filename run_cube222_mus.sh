#!/usr/bin/env bash
set -u
work=/root/three_box_exact
program="$work/three_box_mus"
current="$work/cube222_mus_current.txt"
printf '%s\n' 1 3 4 5 7 12 13 15 16 17 19 20 21 23 28 29 31 48 49 51 52 53 55 60 61 63 > "$current"

round=0
while true; do
  round=$((round+1))
  changed=0
  cp "$current" "$work/cube222_mus_round${round}_start.txt"
  while read -r mask; do
    candidate="$work/cube222_mus_candidate.txt"
    awk -v drop="$mask" '$1 != drop {print $1}' "$current" > "$candidate"
    cnf="$work/cube222_mus_test.cnf"
    log="$work/cube222_mus_test.log"
    "$program" gen-keep 2 2 2 9 "$candidate" "$cnf" 2>"$work/cube222_mus_test.stats"
    timeout 40 kissat --time=30 "$cnf" >"$log" 2>&1
    rc=$?
    if (( rc == 20 )); then
      mv "$candidate" "$current"
      changed=1
      echo "round=$round removed=$mask remaining=$(wc -l < "$current")"
    elif (( rc == 10 )); then
      echo "round=$round essential=$mask"
    else
      echo "round=$round unknown=$mask rc=$rc"
    fi
  done < "$work/cube222_mus_round${round}_start.txt"
  if (( changed == 0 )); then break; fi
done

echo FINAL
cat "$current"
