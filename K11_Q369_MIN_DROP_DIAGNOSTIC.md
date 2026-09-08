# Exact minimum-drop diagnostic for a fixed q369 row

## Result

For the fixed row

`scratch/d3best_rose_conflict38.txt`

the minimum possible number of uncovered masks of ranks 1 through 5 among
nonzero 465-entry factors of the q369 central schedule is exactly **2**.

An explicit factor misses exactly the masks

```text
710  (rank 5)
1185 (rank 4)
```

and no factor of this row can miss at most one lower mask.  The upper union
shadow of this row is still incomplete (the independent verifier reports 46
missing masks of ranks 7 through 11), so this is not a 465-entry universal
array and does not decide `nu(11)`.

The previous heuristic score `conflict=38` was therefore not the true
factorization distance.  Exact factorization is much closer: two lower masks.

A later refined row improves the heuristic statistics to conflict 10, complete
bulk D3, and 44 missing upper masks:

`scratch/q369_two_refined_conflict10_d3_330.txt`

Its exact lower-factor distance is **also 2**.  A semantic factor misses exactly

```text
4     (rank 1)
1553  (rank 4)
```

while its q=1 CNF is UNSAT.  The 480 MiB binary DRAT proof was independently
verified and is stored zstd-compressed in
`scratch/certificates/q369_min_drop_refined10/`.  This second result reinforces
that the matching conflict score is not a calibrated distance, even though it
remains useful for finding better rows.

## Encoding

`k11_q369_global_factor_cnf.cpp` now has two additional modes:

```text
--build-drops ROW Q OUTPUT.cnf OUTPUT.dropmap.tsv
--decode-drops ROW Q MODEL OUTPUT.factor OUTPUT.dropped.tsv
```

For every lower target `S` (rank at most 5), the generator creates one fresh
variable `drop[S]`.  If `w[S,I]` is the exact-OR selector for candidate short
interval `I`, the ordinary target clause

```text
OR_I w[S,I]
```

is replaced by

```text
drop[S] OR OR_I w[S,I].
```

A monotone sequential counter enforces

```text
sum_S drop[S] <= Q.
```

All factor-bit variables, nonzero-entry clauses, q369 central equations, and
selector-to-exact-OR implications are unchanged.

### Soundness

In a satisfying assignment, every target with `drop[S]=false` has a selected
witness.  The conditional clauses make every bit of its interval OR equal to
`S`.  The sequential counter allows at most `Q` relaxed targets.  Therefore
the decoded factor misses at most `Q` lower masks.

### Completeness

Every interval of length at least four contains one designated q369 rank-six
central window: for a start before 369 it contains the corresponding triple,
and thereafter it contains the corresponding quadruple.  Hence an interval
whose OR has rank at most five necessarily has length at most three.

Given a nonzero factor of the fixed row missing at most `Q` lower masks, choose
a short witness selector for every covered lower target and set `drop[S]` only
for missing targets.  Every candidate prefilter in the generator is necessary
for a genuine witness (envelope containment, nonzero intersection, no
containing incompatible central window, and survival of every central pin).
Thus the chosen witnesses are present, and the sequential counter has an
extension.  The CNF is satisfiable.

Consequently,

```text
CNF(Q) is SAT  <=>  the fixed row has a factor missing at most Q lower masks.
```

The sequential-counter implementation is also exhaustively self-tested on all
assignments of a five-input, at-most-two instance.

## Exact target-core mode

The same generator also provides:

```text
--build-target-core ROW OUTPUT.cnf OUTPUT.assumptions OUTPUT.guardmap.tsv
```

It creates one positive assumption guard `g[S]` for every lower target.  The
literal `-g[S]` is prepended to the target support clause **and to every
selector-to-exact-OR clause for that target**.  Thus dropping assumption
`g[S]` removes the whole target constraint rather than leaving hidden
contamination clauses behind.  The central row, position envelopes, and
nonzero constraints remain hard background.

The assumptions file has a DIMACS-style line

```text
a g[1] g[2] ... g[1023] 0
```

and the TSV maps each guard variable back to its mask and rank.  Failed
assumption cores are therefore sound target cores for the fixed row.  Because
candidate pre-pruning retains consequences of the complete central row, these
cores should not be interpreted as faithful *central-window removal* cores.
For row-search feedback, map recurring core targets back onto their compatible
selector intervals; aggregate several solver seeds rather than relying on one
noncanonical core.

## Certificates

The directory

`scratch/certificates/q369_min_drop_conflict38/`

contains:

- `conflict38_q2.factor`: semantic SAT certificate;
- `conflict38_q2.dropped.tsv`: the two missing masks;
- `conflict38_q2.cnf`, model, and drop-variable map;
- `conflict38_q1.cnf` and `conflict38_q1.drat`: UNSAT certificate;
- `conflict38_q1_dratcheck.log`: independent `drat-trim` verification.

The independent semantic verifier is

`k11_q369_min_drop_verify.cpp`.

It checks the rank-six permutation, all 462 mixed-width central equations, all
factor entries for nonzeroness/range, and every subarray OR using the distinct
suffix-OR recurrence.  It confirms exactly two lower omissions:

```text
PASS q369 central=462 lower_missing=2 upper_missing=46 masks 710 1185
```

The q=1 proof check ends with:

```text
s VERIFIED
```

The refined-row proof check also ends with `s VERIFIED`; it checks 2,832,989
core lemmas using 839,436,511 resolution steps.

The q=1 DIMACS has 10,458 variables and 26,186 clauses.  Its SHA-256 is

```text
2a016111f8615b2f55a26e881ec721cb279d5e6d24327dc29bf9c8d478e04b31
```

and the DRAT SHA-256 is

```text
5059b311e6b4c0a85995697a36e2089153291935597f282145b388cd12621a8b
```

## Reproduction

Lightweight local semantic verification:

```bash
g++ -std=c++20 -O2 -Wall -Wextra -pedantic \
  k11_q369_min_drop_verify.cpp -o /tmp/q369_min_drop_verify
/tmp/q369_min_drop_verify \
  scratch/d3best_rose_conflict38.txt \
  scratch/certificates/q369_min_drop_conflict38/conflict38_q2.factor \
  710 1185
```

Build and solve on a remote machine (use `-std=c++2a` on the current RunPod
compiler):

```bash
g++ -std=c++2a -O3 -DNDEBUG k11_q369_global_factor_cnf.cpp -o q369_factor
./q369_factor --self-test
./q369_factor --build-drops d3best_rose_conflict38.txt 2 \
  conflict38_q2.cnf conflict38_q2.dropmap.tsv
kissat --seed=2 conflict38_q2.cnf > conflict38_q2.model
./q369_factor --decode-drops d3best_rose_conflict38.txt 2 \
  conflict38_q2.model conflict38_q2.factor conflict38_q2.dropped.tsv

./q369_factor --build-drops d3best_rose_conflict38.txt 1 \
  conflict38_q1.cnf conflict38_q1.dropmap.tsv
kissat --seed=101 --no-binary conflict38_q1.cnf conflict38_q1.drat \
  > conflict38_q1_proof.log
drat-trim conflict38_q1.cnf conflict38_q1.drat
```

## Interpretation and next use

This diagnostic distinguishes two issues that the old matching score mixed:

1. the fixed row has an unavoidable two-mask lower pin obstruction;
2. independently, its upper row-union shadow misses 46 masks.

Therefore a useful row move must change the central envelopes enough to remove
the two-mask lower obstruction while also improving the upper shadow.  Merely
optimizing the old conflict count is not a faithful proxy for either task.
