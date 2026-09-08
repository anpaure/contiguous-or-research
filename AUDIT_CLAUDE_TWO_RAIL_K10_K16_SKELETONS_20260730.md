# Audit of Claude's two-rail construction and the `K=16` rail skeletons

Date: 2026-07-30

Status: the `K=10` theorem witness is genuine, and both marginal `K=16`
quotient path objects exist.  The displayed pair of `K=16` paths is not a
carrier: its seam/residence gauge system is infeasible in every reversal and
relative affine alignment tested.  No optimal `K=16` word is claimed.

## 1. The `K=10` result is fully verified

Claude's two-rail construction produced a length-`254` word.  The repository's
independent `verify_word.py`, which knows nothing about the quotient model,
replayed every contiguous OR and returned

```text
PASS k=10 length=254 covered=1023/1023
D^0: length=254 unique=165 ranks={1: 31, 2: 101, 3: 122}
D^1: length=253 unique=239 ranks={2: 5, 3: 24, 4: 224}
D^2: length=252 unique=252 ranks={5: 252}
central rank=5 exact=True; counting lower bound: d=2, B(10)=252+2=254
```

The word has SHA-256

```text
69eb5acc3bdbf09bef8d0b46023622ba51928fb643fea75bbbc071813cf38efb
```

Thus this is a real second two-rail optimal construction, not merely a carrier
or a quotient-level certificate.

## 2. The two-rail normal form is mathematically sound

For `K=2R`, put `n=K-1` and freeze the top trace to one block of `N/2`
ones and one block of `N/2` zeros.  The middle bijection splits into

* an orbit-transversal path through rank `R-1` subsets of `[n]` (the
  top-containing rail); and
* an orbit-transversal path through rank `R` subsets of `[n]` (the other
  rail).

Within either rail the generalized start/end transversality law is exactly
Johnson adjacency.  Across the two rail boundaries it becomes containment;
the second boundary carries the unit-voltage rotation.  The no-top q1 deck
has one more available edge slot than targets, so the rank-`R` rail is a
near-perfect rainbow path.  The rank-`R-1` rail has more label slack and only
needs coverage.

This reduction is a correct sufficient normal form.  It does not say that
every optimal even word is two-rail; the known `K=14` optimum is not.

## 3. One bug in the exploratory A-rail script

`/Users/amir.nuriyev/Downloads/opusproblem/work/rbcover.py` is not an exact
certificate of label coverage.  For a selected quotient arc it adds that same
arc literal to every label that *some* relative phase could realize.  A single
arc may therefore satisfy several label rows using mutually incompatible
phases.  Its final check deliberately repeats this relaxation (`loose count`).

This is an encoding bug, but it does **not** falsify the existential claim.  A
replacement model was written in

```text
scratch/audit_claude_exact_covering_rail_path_20260729.py
SHA-256 e3cbaea786cb8f171e0c7711aa0e98db87107458514cf60278a4aeff06ebc7ca
```

Every selected arc now chooses exactly one label and an explicit relative
phase witness.  The chosen quotient path is materialized into a physical
Johnson path and its labels are replayed.

At `n=15`, rank seven, the exact model found in `1.50` solver seconds:

```text
429 quotient vertices,
335 required rank-six necklace labels,
335 distinct physical labels,
all 335 labels covered.
```

Artifact:

```text
scratch/claude_exact_arail_n15_20260730.audit.json
SHA-256 22d4df5e375f46269d84ae440d065167387537024a08a17ed8a211f73e6198d0
```

The rank-eight B-rail was independently re-solved with the same exact
one-label-per-arc semantics.  In `23.92` seconds it found a 429-vertex path
whose 428 edges have 428 distinct labels out of 429:

```text
scratch/claude_exact_brail_n15_20260730.audit.json
SHA-256 8a03664ea922357f069b002a9fa69adc447719b09e00a5b792c522e29b26654f
```

Therefore both *marginal* `K=16` skeleton claims are true and cheap.

The same missing exactly-one link occurs in Claude's `railpair.py`: option
variables imply their arc and a selected arc requires at least one option,
but one arc may select several incompatible `(intersection,union)` pairs.
Results from that script likewise require an exact replacement before they
can certify a coupled palette.  By contrast, `rbexact.py` is sound for the
zero-slack rainbow case used at `n=15`: extra selected labels can simply be
pruned to one per arc.  Its `--slack>0` mode remains too strong because the
global per-label `AtMostOne` still forbids the repeats that slack was meant to
allow.

## 4. Marginal paths are not a compatible pair

The paths must still admit one common choice of class phases satisfying

1. all interior Johnson steps;
2. both containment seams and unit-voltage wrap; and
3. positive residence four.

Claude's `gauges.py` is an exact model of those three conditions for a fixed
pair of quotient paths.  The independently certified A/B pair above is
`INFEASIBLE` in all four path-orientation combinations.  Applying every unit
multiplier of `Z_15` to the A path relative to B and again trying both
orientations gives 32 cases, all `INFEASIBLE` in about one second each.

```text
scratch/claude_exact_pair_affine_gauge_20260730.txt
SHA-256 0934ee0ec0a891228067741c1e6651fe06734897d70ad0acd5b823a0668af684
```

Translations do not add cases because the gauge variables already absorb
them.  This is not a no-go for the two-rail architecture: different A and B
paths may be compatible.  It does show that finding the two paths separately
does not discharge the coupled gate.

The failure is stronger than seam incompatibility.  An exact *open-rail*
phase audit drops both A/B seams and leaves endpoint runs unconstrained.  It
asks only whether the fixed quotient chronology can be phased into a physical
Johnson path whose internal positive runs have length at least four.  Both
paths are infeasible in both orientations:

```text
A forward  INFEASIBLE   A reverse  INFEASIBLE
B forward  INFEASIBLE   B reverse  INFEASIBLE
```

The checker is

```text
scratch/audit_k16_rail_path_phase_residence_20260730.py
SHA-256 a73ef80179b88aea4463b533168b56ffc7058d1492fad1ad465a8e7404fba54f
```

with the four result artifacts named
`scratch/claude_open_{a,b}_rail_residence_rev{0,1}_20260730.audit.json`.
Hence a portfolio of paths generated without phase-residence constraints is
poorly targeted; residence must enter the quotient path generator itself (or
at least be used as an immediate exact filter) before pairing endpoints.

Operationally, `gauges.py`, `rbcover.py`, and `rbexact.py` return a Boolean
from `main` but do not pass it to `SystemExit`.  An infeasible run therefore
has shell exit status zero.  Monitors must parse the printed solver status or
a structured artifact; exit code zero is not a SAT verdict.

## 5. The rail-prescribed CNF is sound but not yet lean

The new `cnf16.py --rails` mode correctly constrains each class to a rotation
of its prescribed necklace and retains the residence and palette rows.  A SAT
output, followed by the independent carrier/word replay, would be valid.

However, the current implementation still emits the original full middle,
q1, q2, and upper selector catalogues.  Fixing the rail representatives does
not project those redundant selectors away.  Thus the semantic search space
is only `15^858`, but the present CNF is not yet the compact phase-only model
suggested by that count.  No `K=16 --rails` verdict or emitted instance was
present at audit time.

Also, the upper-width catalogue is sufficient for a SAT witness but not proved
complete for an UNSAT theorem.  Negative results must keep that scope label.

## 6. Verdict

Claude found a real and valuable normal form:

```text
two orbit-transversal quotient paths + common phase gauge + two seams.
```

The `K=10` success and both exact `K=16` marginal path certificates validate
the first half strongly.  The remaining half—choosing the paths and gauge
*jointly* so that residence and every palette coexist—is still the hard
problem.  Therefore “the skeletons exist and are cheap” is correct if
`skeletons` means the two marginal paths; it is too strong if read as a
nearly-complete `K=16` carrier.
