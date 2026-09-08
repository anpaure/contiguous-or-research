# What the coefficient-one manuscript constructs

2026-09-08. Companion to `COEFFICIENT_ONE_PROOF_20260908.md`.

The manuscript specifies a finite deterministic construction of ordinary
interval-union words. Its new proposed theorem concerns their asymptotic
length. An executable implementation of this PBBS construction has not
been delivered in this continuation, and no improved k=17 word has been
produced from it. The proof has internal AI-agent reviews, not independent
external review or formal verification.

## 1. Finite recipe in odd dimension

Given n=2r+1, try every positive integer H with 2H<=r+1. Fix a
lexicographic order to resolve arbitrary choices.

1. Enumerate the rank-r states of the canonical parenthesis-matching
   PBBS permutation. Take their complements and traverse by two steps,
   obtaining rank-(r+1) owner cycles X_i. The map and conventions are in
   `PBBS_RESIDENCE_PACKING_REDUCTION_20260725.md`, Sections 1, 8, and 9,
   and `PBBS_COORDINATE_HOMOMESY_AUDIT_20260724.md`.

2. List positive coordinate runs of at most H owners. Their repair
   intervals include the insertion edge, internal edges, and removal
   edge. On each cycle with such intervals, choose an edge in one
   interval and cut there. Hit the remaining line intervals by the
   greedy right-endpoint algorithm. This uses at most twice the maximum
   number of disjoint repair intervals on that active cycle.

3. On each resulting path X_0,...,X_(v-1), extend X constantly beyond
   both endpoints. Output the v+H nonempty subset letters

       D_i = intersection_(j=0)^H X_tilde_(i+j),  -H<=i<=v-1.

   On a cycle needing no cuts, output the cyclic version and repeat
   its first 2H letters. This is the endpoint-capped erosion construction
   in Section 22 of the residence note.

4. At each cut use the ORIGINAL cyclic owners to form

       P_(s,t) = intersection_(i=-s)^(t-1) X_i,  1<=s,t<=H.

   Record the capped positive extents (u_x,v_x) of each coordinate
   present on both sides. Join their Pareto-minimal points by the
   east-before-south unit path from (1,H) to (H,1), and emit P_(s,t)
   at its 2H-1 vertices. Then emit X_(-H),...,X_(H-1). These two words
   restore crossing lower and upper targets. Section 24 and
   `MATH_ATTACK_H_PBBS_DOMINANCE_STAIRCASE_SEAM_20260725.md` give the
   formulas and proof.

5. Append the product symmetric-chain tail word. On two r-coordinate
   halves, take standard symmetric-chain decompositions. For each
   chain pair C,D with minimum ranks a+b<=r-H, concatenate C's reversed
   increment word and D's forward increment word. Lift this tail word
   to 2r+1 coordinates by the rule below. The complete recipe is in
   `MATH_THEOREM_O_PRODUCT_SCD_TAIL_MIXED_CYCLE_INTERFACE_20260726.md`,
   Sections 1 and 2.

6. Concatenate all blocks and retain the shortest output among the
   finitely many H candidates. Each witness stays inside its block.

For small dimensions with no admissible H, use a direct complete word,
for example listing all nonempty subsets. No running-time claim is made.

Trying every H avoids needing the nonexplicit thresholds in the
asymptotic proof: the shortest candidate is no longer than the one chosen
by its slow diagonal. This is a finite selection rule, not a rate estimate.

## 2. Even dimensions

For a complete word Q_1,...,Q_N on the preceding odd dimension, add a
new coordinate z and output

    Q_1,...,Q_N, {z}, Q_1 union {z},...,Q_(N-1) union {z}.

This has 2N letters. Old witnesses remain in the first copy. Witnesses
with z use the last block or an old suffix followed by {z}.

## 3. The actual construction at k=17

`answers/k17_upper25745.word` is a retained 25,745-letter word. Its saved
independent exhaustive verification reports all 131,071 nonempty targets
covered, zero missing. It is an earlier boundary splice, not an output
of the new coefficient-one PBBS analysis.

Using `answers/k16.word` as the Python list X, its exact recipe is

```python
Y = X[1:][::-1] + [65536, 50122, 33642] + [x | 65536 for x in X[3:]]
```

Each integer encodes a subset; bit j represents coordinate j+1. Targets
are bitwise ORs of nonempty contiguous, nonwrapping intervals. The
generator and source-only proof are in
`scripts/k17_boundary_splice_20260906_b7e41_audit.py`.

The review package includes both words, the generator, independent
verifier, and saved verification in its `finite_construction` directory.

At r=8, the PBBS ledger has four admissible H choices. Even dropping
its nonnegative packing term, the right-hand sides are 97,786; 94,374;
81,106; and 62,910. Thus that ledger cannot certify a better k=17 word.
These figures do NOT lower-bound all words or exclude a more economical
implementation. See `scratch/PBBS_K17_FINITE_COMPILER_LEDGER_20260908.md`
for the exact remote calculation and its scope.

The recorded finite bounds remain 24,313 <= nu(17) <= 25,745.

## 4. Comparison with the user's new coefficient 1.15325

The user's endpoint-partition argument claims
nu(k)<=(1.15325+o(1))W(k). This is the same full-cube leading coefficient
as our proposed nu(k)=(1+o(1))W(k). If the coefficient-one proof is
correct, it is asymptotically stronger and optimal in its leading
coefficient. It does not imply exact equality nu(k)=W(k), or replace a
verified finite word at k=17.

The new 1.15325 argument has not been independently audited here.
The supplied labels for its proof and verifier contained no accessible
paths or URLs; no claim is made to have run that external verifier.
