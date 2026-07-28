# Fast sigma SAT search, the exact `k=11` certificate, and the `k=13` probe

Date: 2026-07-27

## Result

The translation-quotient search found a length-465 nonzero set word on
`[11]` whose contiguous ORs contain all `2^11-1=2047` nonempty masks.
Together with the audited deadline lower bound, this proves

\[
\nu(11)=B(11)=\binom{11}{6}+3=465.
\]

The final word is `scratch/sigma_sat_k11_465.word`, with SHA-256

```text
746b469af108558b14e7f6af0e3f76f9b6f39f70b3561e0258cc976650761850
```

## Search encoding

For each of the 42 translation orbits of five-sets, one of its 15 two-point
extensions is selected.  The CNF enforces:

1. one extension per lower orbit;
2. degree two at every one of the 42 middle orbits;
3. all 30 upper-q1 orbits covered, with load at most two;
4. all 15 upper-q2 and all 30 lower-q2 orbits covered;
5. all quotient paths creating residence 1, 2, or 3 forbidden;
6. one quotient Hamilton cycle, via directed arcs and one-hot positions.

The final CNF has 27,103 variables and 1,728,029 clauses.  Kissat found the
model in 13.95 seconds; construction plus solving took 19.68 seconds on the
development machine.  The quotient voltage is two, so the lift is one
462-cycle.  An independent audit gives zero residence violations and complete
lower and upper shadows at every depth.

The exact interval/Hall compiler then chose cut 1 and the boundary flag

```text
155 superset 154 superset 152
```

and found a 231/231 matching for all masks of ranks one through three.  It
finished in 0.05 seconds.  The resulting derivative tableau is

| row | length | distinct | rank histogram |
|---|---:|---:|---|
| `D^0` | 465 | 231 | `1:11, 2:55, 3:399` |
| `D^1` | 464 | 332 | `2:1, 3:1, 4:462` |
| `D^2` | 463 | 462 | `5:463` |
| `D^3` | 462 | 462 | `6:462` |

## Reproduction

Generate the central certificate:

```sh
python3 scratch/sigma_sat_solver.py \
  --k 11 --q2 --lower-q2 \
  --residence 3 --direct-residence --direct-connectivity \
  --time-per-round 600 --max-rounds 30 \
  --prefix scratch/sigma_sat_k11_allcentral_cap2
```

Compile and independently audit the central certificate:

```sh
python3 scratch/sigma_sat_verify_certificate.py \
  scratch/sigma_sat_k11_allcentral_cap2.certificate.json \
  --compiled-word scratch/sigma_sat_k11_465.word \
  --report scratch/sigma_sat_k11_allcentral_verify.json
```

Run the minimal exhaustive verifier, which trusts neither SAT auxiliaries nor
the compiler's claimed coverage:

```sh
python3 scratch/sigma_sat_verify_word.py \
  --k 11 scratch/sigma_sat_k11_465.word
shasum -a 256 scratch/sigma_sat_k11_465.word
```

Expected headline:

```text
PASS k=11 length=465 covered=2047/2047
```

## Smaller-instance calibration

The exact final-word verifier passes the stored known optima:

| `k` | `B(k)` | final artifact | exhaustive result |
|---:|---:|---|---|
| 3 | 4 | `scratch/sigma_sat_known_k3.word` | `7/7` |
| 4 | 7 | `scratch/sigma_calibration_k4.txt` | `15/15` |
| 5 | 12 | `scratch/sigma_sat_known_k5.word` | `31/31` |
| 6 | 21 | `k6_honest_generated.txt` | `63/63` |
| 7 | 37 | `k7_published_rank_exact.txt` | `127/127` |
| 8 | 72 | `k8_optimal.txt` | `255/255` |
| 9 | 128 | `k9_optimal.txt` | `511/511` |
| 10 | 254 | `k10_optimal_nonzero.txt` | `1023/1023` |
| 11 | 465 | `scratch/sigma_sat_k11_465.word` | `2047/2047` |
| 12 | 926 | `k12_optimal_nonzero.txt` | `4095/4095` |

The same central SAT modules were calibrated separately before `k=11`:

| `k` | symmetry | central constraints | SAT time | artifact |
|---:|---|---|---:|---|
| 5 | `Z_5` quotient | both q2 sides, connected | 0.0029 s | `scratch/sigma_sat_bench_k5.certificate.json` |
| 7 | `Z_7` quotient | both q2 sides, connected | 0.0036 s | `scratch/sigma_sat_bench_k7.certificate.json` |
| 9 | full, no quotient | both q2 sides, connected | 4.20 s | `scratch/sigma_sat_test_k9_bothq2.certificate.json` |
| 11 | `Z_11` quotient | both q2 sides, residence 3, connected | 14.44 s solver loop | `scratch/sigma_sat_k11_allcentral_cap2.certificate.json` |

For `k=3` the prime quotient is degenerate because its top target is the full
set and has non-free stabilizer.  For `k=5,7`, cyclic equivariant residence is
stronger than what their positive-slack optimal linear words require, so the
central calibration and final-word calibration are deliberately reported as
separate tests.  The `k=11` row is the first end-to-end run of this exact
quotient-central-plus-Hall pipeline.

Commands for the smaller exact checks:

```sh
python3 scratch/sigma_sat_verify_word.py --k 3 scratch/sigma_sat_known_k3.word
python3 scratch/sigma_sat_verify_word.py --k 4 scratch/sigma_calibration_k4.txt
python3 scratch/sigma_sat_verify_word.py --k 5 scratch/sigma_sat_known_k5.word
python3 scratch/sigma_sat_verify_word.py --k 6 k6_honest_generated.txt
python3 scratch/sigma_sat_verify_word.py --k 7 k7_published_rank_exact.txt
python3 scratch/sigma_sat_verify_word.py --k 8 k8_optimal.txt
python3 scratch/sigma_sat_verify_word.py --k 9 k9_optimal.txt
python3 scratch/sigma_sat_verify_word.py --k 10 k10_optimal_nonzero.txt
python3 scratch/sigma_sat_verify_word.py --k 11 scratch/sigma_sat_k11_465.word
python3 scratch/sigma_sat_verify_word.py --k 12 k12_optimal_nonzero.txt
```

## Bounded `k=13` next-case probe

Here `r=7`, `W=1716`, and the translation quotient has 132 lower/middle
orbits with 21 choices per lower orbit.  The compact Hamilton encoding uses
oriented selected edges and unary MTZ ranks.  It is much smaller than the
one-hot position encoding.

The exact stages reached were:

| stage | result | time | artifact |
|---|---|---:|---|
| q1 cap2, lazy connectivity | SAT | 20.68 s | `scratch/sigma_sat_k13_q1.certificate.json` |
| q1 + both q2 + compact connectivity | SAT | 144.97 s solve | `scratch/sigma_sat_k13_bothq2_compact.certificate.json` |
| add direct residence 2 globally | UNKNOWN | 300.06 s | `scratch/sigma_sat_k13_bothq2_h2_compact.certificate.json` |
| residence-2 LNS, 30 free / 102 fixed | UNSAT in this neighborhood | 0.18 s | `scratch/sigma_sat_k13_h2_lns30.certificate.json` |
| residence-2 LNS, 60 free / 72 fixed | UNSAT in this neighborhood | 0.47 s | `scratch/sigma_sat_k13_h2_lns60.certificate.json` |
| residence-2 LNS, 90 free / 42 fixed | SAT | 21.88 s solve | `scratch/sigma_sat_k13_h2_lns90.certificate.json` |

The both-q2 certificate has one quotient 132-cycle of voltage 11, hence one
lifted 1716-cycle.  Independent enumeration found complete q1 and q2 shadows
on both sides.  In fact all upper shadows q1 through q6 and lower shadows
q1, q2, q4, q5, q6 are complete; the only missing central shadow is lower q3,
with 611/715 targets covered.  It has 117 residence-2 and 559 residence-3
violations.

The LNS residence-2 certificate has voltage one and exactly preserves q1/q2
coverage while eliminating every residence-1/2 violation.  Its remaining
central defects are 442 residence-3 violations, lower q3 coverage 650/715,
upper q3 coverage 273/286, and lower q4 coverage 273/286.  Upper q4 and both
sides at q5/q6 are complete.

The final bounded residence-3 experiments did **not** establish SAT or
UNSAT globally:

* freeing 90 choices around the defect set became UNSAT only for that fixed
  neighborhood after lazy cuts;
* freeing 120 choices returned UNKNOWN at 60 s and 90 s;
* freeing 110 choices ran five lazy rounds (base solutions with 403, 312,
  403, and 442 residence-3 violations, plus one zero-voltage solution) and
  ended at the round limit after 236.7 s.

Thus the exact `k=13` residual is residence 3 plus q3 shadow completion,
followed by the interval/Hall compiler.  No claim about `nu(13)` follows from
the bounded UNKNOWN or neighborhood-UNSAT outcomes.

### Compact residence and q3 automata

The later version of the solver contains a substantially smaller exact
encoding of this residual:

* `--automaton-residence` orients the selected quotient Hamilton cycle and
  propagates the last `h` inserted coordinates in the canonical phase of each
  quotient vertex.  A selected arc may not delete one of those coordinates.
  At `k=13,h=3` this adds 88,512 implication clauses in the forward-only
  version (199,152 after making the states exact in both directions), rather
  than enumerating all forbidden four-edge paths.
* `--automaton-lower-q3` uses the exact last-three-insertion states.  The
  four-window intersection ending at a middle set `Y` is exactly `Y` minus
  those three coordinates.  All 55 lower-q3 quotient targets therefore need
  only 27,720 ordered-triple witnesses.
* `--automaton-upper-q3` is the exact dual.  It tracks recent deletions among
  the coordinates absent from `Y`; three deletions that remain absent identify
  the union `Y` plus those coordinates.  It does **not** assume that forward
  residence controls short zero-gaps.  `--automaton-coresidence` optionally
  imposes that stronger dual residence condition, but upper-q3 coverage does
  not require it.

The complete `k=13` both-q2 + residence-3 + both-q3 CNF has 211,755 variables
and 1,923,877 clauses and builds locally in about 1.2 seconds:

```sh
python3 scratch/sigma_sat_solver.py \
  --k 13 --q2 --lower-q2 \
  --residence 3 --automaton-residence \
  --automaton-lower-q3 --automaton-upper-q3 \
  --compact-connectivity --time-per-round 300 --max-rounds 1 \
  --prefix scratch/sigma_sat_k13_h3_bothq3_auto
```

The construction was calibrated by fixing the exact `k=11` central
certificate: the full forward-residence plus lower/upper-q3 automaton CNF was
SAT in 0.03 seconds.  A fresh unfixed `k=11` forward residence automaton also
produced a residence-3-clean Hamilton certificate.  Local `k=13` attempts at
zero h3 defect, and a MaxSAT-style budget of at most 20 quotient h3 defects,
returned UNKNOWN at their stated 120--300 second limits; these are timing
results only, not mathematical obstructions.

The two stored `k=13` certificates give a concrete defect tradeoff at quotient
scale (divide physical counts by 13):

| certificate | forward residence 2 | additional forward residence 3 | lower-q3 holes | upper-q3 holes | valid lower/upper q3 windows |
|---|---:|---:|---:|---:|---:|
| both-q2 base | 9 | 34 | 8 | 0 | 123 / 94 |
| residence-2 LNS | 0 | 34 | 5 | 1 | 132 / 94 |

The LNS changed 74 of the 132 sigma choices.  Thus eliminating the nine
depth-two run defects also removed three lower-q3 holes, but displaced one
hole to the upper side; it did not change the 34 additional depth-three run
defects.  This is why the final CNF couples forward residence and both q3
coverages rather than optimizing them in separate passes.

The successful residence-2 LNS run is reproducible with:

```sh
python3 scratch/sigma_sat_solver.py \
  --k 13 --q2 --lower-q2 \
  --residence 2 --direct-residence --compact-connectivity \
  --hint-certificate scratch/sigma_sat_k13_bothq2_compact.certificate.json \
  --lns-free 90 --time-per-round 180 --max-rounds 1 \
  --prefix scratch/sigma_sat_k13_h2_lns90
```
