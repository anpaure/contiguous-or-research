#!/usr/bin/env bash
set -u

work=/root/three_box_exact
solver=/usr/local/bin/kissat
program="$work/three_box_exact_sat"
summary="$work/SUMMARY.tsv"

mkdir -p "$work/cases"
printf 'p\tq\tr\twidth\taxes\toptimum\tstatus\tseconds\n' > "$summary"

cases=(
  '1 1 1'
  '1 1 2'
  '1 1 3'
  '1 1 4'
  '1 2 2'
  '1 2 3'
  '1 2 4'
  '1 3 3'
  '2 2 2'
  '2 2 3'
  '2 2 4'
  '2 3 3'
  '3 3 3'
)

for triple in "${cases[@]}"; do
  read -r p q r <<< "$triple"
  tag="${p}_${q}_${r}"
  info=$($program info "$p" "$q" "$r")
  width=$(sed -n 's/.*width=\([0-9][0-9]*\).*/\1/p' <<< "$info")
  axes=$(sed -n 's/.*axes=\([0-9][0-9]*\).*/\1/p' <<< "$info")
  lower=$width
  if (( axes > lower )); then lower=$axes; fi
  started=$(date +%s)
  status=LIMIT
  optimum=-1
  echo "CASE $tag info=[$info] lower=$lower"

  for ((n=lower; n<=lower+8; ++n)); do
    cnf="$work/cases/${tag}_n${n}.cnf"
    log="$work/cases/${tag}_n${n}.log"
    word="$work/cases/${tag}_n${n}.word"
    "$program" gen "$p" "$q" "$r" "$n" "$cnf" 2> "$work/cases/${tag}_n${n}.stats"
    echo "  trying n=$n"
    timeout 180 "$solver" --time=170 "$cnf" > "$log" 2>&1
    rc=$?
    if (( rc == 10 )); then
      "$program" decode "$p" "$q" "$r" "$n" "$log" "$word"
      "$program" verify "$p" "$q" "$r" "$word"
      optimum=$n
      status=EXACT
      break
    elif (( rc == 20 )); then
      echo "  UNSAT n=$n"
    else
      echo "  solver limit/error n=$n rc=$rc"
      status=UNKNOWN
      break
    fi
  done

  elapsed=$(( $(date +%s) - started ))
  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
    "$p" "$q" "$r" "$width" "$axes" "$optimum" "$status" "$elapsed" \
    | tee -a "$summary"
done

echo DONE
