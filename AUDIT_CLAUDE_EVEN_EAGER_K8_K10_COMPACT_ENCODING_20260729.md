# Audit of the even eager claims and a compact equivalent encoding

Date: 2026-07-29

Scope: the local snapshot in
`/Users/amir.nuriyev/Downloads/opusproblem/work`.  No remote solver was
launched for this audit.

## 1. Exact finite conclusions

The retained certificates still prove

\[
\nu(8)=72,\qquad \nu(10)=254.
\]

An independent literal replay enumerated every contiguous-subarray OR:

| artifact | length | required masks | missing | SHA-256 |
|---|---:|---:|---:|---|
| `answers/k08.word` | 72 | 255 | 0 | `df6d76b468bd816fd014d9b6f5259ba60e5f1ea06e4c4313901fe6155c8780eb` |
| `answers/k10.word` | 254 | 1023 | 0 | `24b6fc4f4c054e46ef54553ca37eded126150542d51a61256a837d666e0c74fd` |
| Claude `k10_flat.word` | 254 | 1023 | 0 | `b71ef0cfba9642b793a09323bb53839e2d4649901c3c78a156ae6d3c1d913f48` |

Together with the proved monotone-deadline lower bound, these are exact
optimality certificates.

The generic `K=10` finish chain is also independently calibrated.  Taking
`T=D^2(k10_flat.word)` gives all 252 distinct rank-five sets, no Johnson-path
defect, complete cyclic q1 coverage, and all 386 upper targets.  Its cyclic
closure has one short run.  Exactly two cuts make that run a boundary run;
one cut (`p=251` in `cutscan16.py`'s convention) has soft score at most two,
and a direct literal recount after the cut has zero q1 holes and zero upper
holes.  Thus the positive

```text
carrier -> cut scan -> exact d=2 compiler -> literal verifier
```

chain is sound at `K=10`.

## 2. What the local snapshot does not certify

The stronger claim that the eager model produced *new equivariant* witnesses
at `K=8` and `K=10` is not locally reproducible.  The following claimed
artifacts or dependencies are absent from the searched Downloads, Documents,
temporary, and Codex directories:

```text
k8_equivariant.word
the K=8 eager carrier/PASS JSON
the K=10 eager carrier/PASS JSON
the corresponding solver logs
beloop.py
biword2.py
```

In particular, the present `bieager.py` fails at import time because it
imports the absent `biword2.py`.  The local `k10_flat.word` predates
`bieager.py` by about nineteen hours, and its derived carrier is not a strict
equivariant spiral (it has 160 distinct rotation jumps).  The retained `K=8`
answer is also non-equivariant.  These words verify optimality and the generic
finisher, not the new eager provenance.

Static inspection finds no false-positive path in `bieager.py`: if its
dependency has the audited `BiWord` semantics, a printed positive PASS is a
sound cyclic-carrier certificate because the physical audit rechecks middle
coverage, Johnson adjacency, residence, q1, q2 when applicable, and upper
coverage.  The missing PASS artifacts are therefore a provenance gap, not a
counterexample to the construction claim.

Two negative claims require narrower wording:

1. `UNSAT_EAGER_GENUINE` is exact only for the encoded width catalogue
   `(2,3,4,6,9,13)`.  A valid carrier can in principle realize an upper target
   first at another width.  Without a width-completeness theorem, UNSAT is not
   nonexistence of the full equivariant class.
2. `sandwich2.py` has sound positive output and performs a final literal
   verification, but its higher derivative rows enumerate only the envelope
   and masks obtained by at most two deletions.  Its negative output is not a
   universal compiler obstruction.  This qualification matters at `K=16`;
   `sandwich.py` at `d=2` is exact for the `K=10` calibration above.

## 3. Why the current eager encoding exhausts memory

Write `K=2r`, `n=K-1`, `W=binom(K,r)`, and `N=W/n`.  At `K=16`,

```text
n = 15, W = 12870, N = 858.
```

The current middle channel introduces one `x[j,o]` variable per quotient
column and middle necklace, then one rotation selector for every triple
`(j,o,s)`.  This gives

```text
x variables                  N^2 =       736,164
rotation selectors         n N^2 =    11,042,460
selector-to-bit implications n^2 N^2 = 165,636,900.
```

That is only the middle gate.  Exact static counts for the rest of
`bieager.py` at `K=16` are:

| gate | selector variables | principal generated rows |
|---|---:|---:|
| q1 | 9,815,520 | 137,417,280 implications |
| q2 | 6,870,864 | 123,675,552 implications + 68,708,640 OR rows |
| upper catalogue | 122,731,752 | 4,914,827,346 implications + 1,203,359,586 OR rows |

The upper rows contain about 19 billion literal references before the target
coverage disjunctions are counted.  Consequently the reported 33.5 GB after
building the 165.6-million middle implications is not the full `K=16` model;
the target-by-witness Cartesian products are the dominant eventual blow-up.

## 4. Canonical-ID encoding

The Cartesian products are unnecessary.  Encode each physical quotient
object once, canonicalize it under rotation, and let each target choose one
witness index.

For a low-coordinate mask `S subseteq Z_n`, define its binary code and orbit
identifier by

\[
 \operatorname{code}(S)=\sum_{x\in S}2^x,
 \qquad
 \operatorname{cid}(S)=\min_{s\in\mathbb Z_n}
       \operatorname{code}(\rho^s S).
\]

The fixed top bit, when present, is included with coefficient `2^n` and is
unchanged by rotation.  In CP-SAT, each identifier is one integer variable
with an `AddMinEquality` over the `n` rotated linear codes.  If the installed
OR-Tools version does not accept affine expressions in `AddMinEquality`, use
`n` auxiliary integer rotation-code variables; the count remains small.

### Middle gate

For every quotient column `j`, form `mid_id[j]=cid(T_j)` and impose

```text
AddAllDifferent(mid_id).
```

This is exactly equivalent to the current `x/y` channeling.  Indeed, the
class sums and `sum(t)=N/2` give `N/2` rank-`r` low columns and `N/2`
rank-`(r-1)` low columns.  Rotation is free on both layers because

\[
\gcd(2r-1,r)=\gcd(2r-1,r-1)=1.
\]

Each layer therefore has exactly `N/2` necklace orbits.  Pairwise distinct
canonical IDs imply an injection from `N/2` columns into `N/2` orbits in
each layer, hence a bijection.  Conversely, the old bijection plainly makes
the IDs pairwise distinct.

### q1 and q2 gates

Create the actual intersection bits once for each quotient start:

```text
q1_id[j] = cid(T_j & T_(j+1))
q2_id[j] = cid(T_j & T_(j+1) & T_(j+2)).
```

For every required target orbit with canonical integer `q`, introduce one
witness index `w_q` and impose

```text
AddElement(w_q, q1_id, q)
```

or the analogous q2 row.  Different target constants cannot use one window
unless their IDs agree, so no all-different condition on witness indices is
needed.  This is exactly the old OR over all starts and phases, with phase
removed by canonicalization.

### Upper catalogue

For every encoded pair `(j,width)` compute the actual window union once,

```text
up_id[j,width] = cid(T_j | ... | T_(j+width-1)).
```

Flatten these IDs into one list.  Each required upper orbit `q` receives a
single witness-index variable and one `AddElement(index_q, up_ids, q)` row.
Using exactly `(2,3,4,6,9,13)` gives a model equivalent, on its `(c,t)`
projection, to the present eager catalogue.  Enlarging the list enlarges the
scope monotonically.  This transformation does not by itself make a
catalogue-restricted UNSAT a full arbitrary-width theorem.

### Equivalence proof

Given a solution of the old model, take the canonical ID of every selected
column or window and set each new witness index to the old selector's start
and width.  All new constraints hold.

Conversely, middle `AllDifferent` gives the two old orbit bijections by the
count above.  Each element constraint identifies a concrete window whose
canonical ID is the requested target; therefore some rotation of that window
equals the target, so the corresponding old phase selector can be set true.
Thus the old and new encodings have exactly the same feasible `(c,t)` pairs
for the same width catalogue.

## 5. Size at `K=16`

With direct Boolean variables for q1/q2 intersection bits and the six
catalogue-width union masks, the compact model needs approximately:

```text
base c/t and exact start/end variables       41,184
middle canonical IDs                           858
q1 bits + IDs                               14,586
q2 bits + IDs                               14,586
upper-window bits + IDs                     87,516
coverage witness indices                     3,063
---------------------------------------------------
total variables                            161,793
```

Its dominant compact rows are about 10.2 million `Element` list references,
1.85 million canonical-min linear-term references, and roughly one million
window-AND/OR references.  This replaces about 151 million selector variables
and billions of generated implication/OR rows.  Native `Element`,
`MinEquality`, and `AllDifferent` propagation must still be benchmarked, but
the serialized model and Python builder should be smaller by orders of
magnitude.

## 6. Consequence for `K=16`

No numerical bound changes: currently

\[
12873\le \nu(16)\le12909.
\]

The compact encoding makes the equivariant carrier search materially more
credible, but a cyclic-carrier PASS is still intermediate.  An optimality
certificate requires a safe linear cut, a positive exact compiler/COMP3
result, and an independent literal verification of a 12,873-letter word.

## 7. Implementation and bounded validation

The encoding above is implemented independently of Claude's missing
`biword2.py` in

```text
scratch/search_even_eager_canonical_id_20260729.py
SHA-256 f53b255842ced36a120757862bbe64528ae7d3b6112a0ef0552c127a89ba12b1
```

The script has four fail-closed modes: analytical count only, model build
only, solve, and independent audit of a saved `(c,t)` artifact.  Positive
artifacts explicitly say that a carrier does not authorize the compiler;
negative solve status is `UNSAT_CATALOGUE_RESTRICTED`.

At `K=8` the compact model solved from scratch in 0.18 seconds.  The physical
audit passed every middle, Johnson, residence, q1, catalogue-upper, and
arbitrary-upper gate.  A cut-scanned exact `d=2` compile then produced

```text
scratch/compact_even_k8_canonical_20260729.word
SHA-256 f89e6337428e2fb8dafe62b1d68458b21616b9d16181c4cce07256ddcd74c361
```

and the repository verifier independently reported all 255 masks covered at
length 72.

At `K=10` the unrestricted compact model builds in about 0.05 seconds with
3,094 variables and 15,501 constraints.  It returned `UNKNOWN` at the bounded
300-second local solve limit.  Eighteen logged top-word layouts, including
the reported run histograms and an optional exact redundant-table propagator,
also returned `UNKNOWN` under short bounded slices.  Thus the implementation
has an exact logical equivalence proof and a complete `K=8` positive replay,
but it has not yet regenerated the missing equivariant `K=10` artifact.
Small serialized size is not being claimed as a search-time theorem.

At `K=16`, build-only validation—no solve—completed in 9.77 seconds with:

```text
161,793 variables
823,314 constraints
1,525,907,456 bytes maximum RSS
0 swaps
model.Validate() == ""
```

The build artifact is
`scratch/compact_even_k16_final_20260729_BUILD_ONLY.json`, SHA-256
`0bc3540504f5607722f07e689845d04b9727a31349ff42c896ec135a1bcf0c64`.

One existence-preserving symmetry is safe at `K=16`: cyclically shift the
carrier so the fixed no-top rank-eight state `{0,...,7}` is `T_0`.  No further
orientation or top-run symmetry is assumed.  Redundant domain tables are
exact but unsafe for memory at `K=16`; the implementation rejects them above
`K=12`.

A prepared, unlaunched, hard-capped run is recorded in
`scratch/compact_even_k16_capped_launch_manifest_20260729.json` and
`scratch/launch_compact_even_k16_capped_20260729.sh`.  It requires explicit
host-stability checks and retirement of the old eager process, and places a
hard 12-GiB address-space ceiling around the new process.  It must not be
started while the H100 freeze remains in force.
