# Runbook: exact global q369 sparse-factor SAT

## Build and tiny local checks

```bash
g++ -std=c++20 -O3 -Wall -Wextra -Wpedantic \
  k11_q369_global_factor_cnf.cpp -o /tmp/k11_q369_global_factor_cnf
g++ -std=c++20 -O3 -Wall -Wextra -Wpedantic \
  k11_q369_global_factor_verify.cpp -o /tmp/k11_q369_global_factor_verify
/tmp/k11_q369_global_factor_cnf --self-test
/tmp/k11_q369_global_factor_cnf --count k11_lower956_upper549.txt
```

Expected self-test:

```text
PASS factor_vars=5115 central=369x3+93x4 short=1392-369=1023 caps=10,31,87,213,465
```

Expected lower-only inventory for `k11_lower956_upper549.txt`:

```text
factor_variables=5115 selectors=3248 variables=8363 clauses=22843 literals=47587
central_empty_pins=0 empty_targets=0 missing_upper_targets=13 encoded_upper_targets=0
rank=1 targets=11 selectors=49
rank=2 targets=55 selectors=551
rank=3 targets=165 selectors=1099
rank=4 targets=330 selectors=1061
rank=5 targets=462 selectors=488
```

No local SAT run is required.

## Generate DIMACS

Lower-complete factor gate:

```bash
./k11_q369_global_factor_cnf --build \
  k11_lower956_upper549.txt q369_lower956_upper549_lower.cnf
```

Optional universal formula, including the thirteen missing upper masks:

```bash
./k11_q369_global_factor_cnf --build \
  k11_lower956_upper549.txt q369_lower956_upper549_universal.cnf --universal
```

For this row the universal inventory reports thirteen empty targets and the
CNF contains thirteen empty clauses.  The meaningful first run is the
lower-only formula.

Independent DIMACS inventory:

```bash
awk 'NR==1{v=$3;c=$4;next}{for(i=1;i<=NF;i++){if($i==0)z++;else{x=$i<0?-$i:$i;if(x>m)m=x}}}
     END{print "maxvar="m,"clauses="z,"header_vars="v,"header_clauses="c;
         exit !(m<=v&&z==c)}' \
  q369_lower956_upper549_lower.cnf
```

## Remote proof-producing run

Compile/generate on the remote host from the frozen source, then:

```bash
set +e
/root/kissat/build/kissat --seed=369549 \
  q369_lower956_upper549_lower.cnf \
  q369_lower956_upper549_lower.drat \
  > q369_lower956_upper549_lower.kissat.log 2>&1
rc=$?
set -e
echo "KISSAT_EXIT=$rc" >> q369_lower956_upper549_lower.kissat.log
```

### If `rc=10` (SAT)

Decode the first 5115 variables and independently check the lower factor:

```bash
./k11_q369_global_factor_cnf --decode \
  k11_lower956_upper549.txt \
  q369_lower956_upper549_lower.kissat.log \
  q369_lower956_upper549_lower.factor

./k11_q369_global_factor_verify \
  k11_lower956_upper549.txt \
  q369_lower956_upper549_lower.factor
```

This proves exact central realization and all 1023 lower masks for the fixed
row, but not full universality: the row has thirteen unrecoverable upper holes.
The factor is nevertheless a valuable seed/certificate for changing the
central row while preserving global lower labelability.

### If `rc=20` (UNSAT)

Check the proof independently:

```bash
/root/drat-trim/drat-trim \
  q369_lower956_upper549_lower.cnf \
  q369_lower956_upper549_lower.drat \
  > q369_lower956_upper549_lower.drat-trim.log 2>&1
echo "DRAT_TRIM_EXIT=$?" >> q369_lower956_upper549_lower.drat-trim.log
```

Only `s VERIFIED` together with exit zero promotes fixed-row UNSAT to a
checked theorem.

## Universal certification for a future row

For a row with a complete upper consecutive-union triangle, lower mode is
already universal.  Verify its decoded factor with:

```bash
./k11_q369_global_factor_verify ROW FACTOR --universal
```

For a row with upper holes but nonempty upper witness candidate sets, build
and solve with `--universal`, decode with `--universal`, and require the same
independent universal verifier PASS.

SAT or UNSAT is always local to the supplied fixed row.  Neither outcome by
itself decides unrestricted `nu(11)`.
