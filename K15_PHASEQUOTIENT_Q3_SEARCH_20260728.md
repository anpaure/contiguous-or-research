# k=15 phase-quotient upper-shadow search (2026-07-28)

## Exact model

The replacement catalogue acts on the 5,295 middle vertices belonging to
carrier cycles 1 and 12.  Translation by `Z_15` leaves 353 vertex orbits and
7,609 admissible edge orbits.  The SAT model selects exactly 353 edge orbits
and enforces:

1. exactly one selected edge orbit for each old lower-colour orbit;
2. quotient degree two at every middle-vertex orbit;
3. exact global upper-q1 coverage after retaining the other 15 carrier
   cycles;
4. exact global upper-q2 coverage, using exact selected-wedge variables.

This q1+q2 model is SAT (`k15_phasequotient_upperq2_orbit.factor.json`) and
its full audit has zero upper holes at q1 and q2.  Its only q3 deficit is the
15 translates of orbit representative 6139.

## Lazy q3 separation

An eager exact q3 encoding contains 6,185,178 triple conjunctions, 6,461,238
variables, and 25,586,519 clauses.  The lazy encoder adds path witnesses only
for q3 orbits missed by the current exact factor.

Round 1 enforced orbit 6139:

- 346,435 variables;
- 1,127,263 clauses;
- 70,387 triple-conjunction variables;
- 20 MB DIMACS.

Kissat seed 17000 found SAT.  Exact decoding preserved q1 and q2 and moved
the q3 deficit to two orbits, 4031 and 8111 (30 physical holes).  The next
lazy instance therefore enforces `4031,6139,8111`:

- 617,719 variables;
- 2,212,401 clauses;
- 341,671 triple-conjunction variables;
- 40 MB DIMACS.

For portfolio diversity, the two one-new-orbit residence-depth-1 branches
are also materialized:

| branch | q3 keys | variables | clauses | size |
|---|---|---:|---:|---:|
| lazy2a-res1 | 4031, 6139 | 495,014 | 1,761,756 | 31 MB |
| lazy2b-res1 | 6139, 8111 | 469,197 | 1,658,488 | 30 MB |

Each has the same 40,176 exact eager residence-depth-1 clauses.  A 16-seed
portfolio on the direct three-key residence-1 instance produced no answer
within its bounded runs; this is a timeout, not evidence of UNSAT.

No conclusion about full q3 feasibility is claimed until the separation loop
terminates with no missed q3 orbit.

## Reproducible commands

Build or solve one exact lazy instance:

```sh
python3 scratch/search_k15_phasequotient_upperq2.py \
  --upper-depth 3 \
  --q3-keys 4031,6139,8111 \
  --prefix scratch/k15_phasequotient_upperq3_lazy3 \
  --seconds 1800
```

Run the complete separator (one new q3 orbit per round):

```sh
python3 scratch/run_k15_upperq3_lazy.py \
  --prefix scratch/k15_phasequotient_upperq3_exact \
  --initial-keys 4031,6139,8111 \
  --seconds 1800
```

On the Linux/H100 host, prefix Python commands with

```sh
KISSAT_BIN=/dev/shm/k15_sat/kissat/build/kissat
```

so the portable runner uses the remote Kissat binary.

Once q3 is feasible, add exact eager residence depths in order:

```sh
# residence depth 1
python3 scratch/run_k15_upperq3_lazy.py \
  --prefix scratch/k15_phasequotient_upperq3_res1 \
  --initial-keys 4031,6139,8111 \
  --eager-residence-depth 1 --seconds 1800

# residence depth 2
python3 scratch/run_k15_upperq3_lazy.py \
  --prefix scratch/k15_phasequotient_upperq3_res2 \
  --initial-keys 4031,6139,8111 \
  --eager-residence-depth 2 --seconds 1800

# depth 1+2 eager, depth 3 exact lazy, plus physical subtour separation
python3 scratch/run_k15_upperq3_lazy.py \
  --prefix scratch/k15_phasequotient_upperq3_res3_connected \
  --initial-keys 4031,6139,8111 \
  --eager-residence-depth 2 \
  --lazy-residence-depth 3 \
  --connected --seconds 1800
```

The lazy residence clauses are exact forbidden selected-edge motifs, and the
connectivity clauses are standard exact physical subtour cuts.  Edge-orbit
indices are stable under the deterministic catalogue construction.

## Current audited SAT factor

The first q3-separated factor has 18 components of sizes

```text
30, 33 (fifteen times), 1170, 3600.
```

Its exact lazy audit finds 97 residence-at-most-3 forbidden motifs and four
distinct physical component cuts.  These are small separation sets; they do
not establish that the combined model is SAT.
