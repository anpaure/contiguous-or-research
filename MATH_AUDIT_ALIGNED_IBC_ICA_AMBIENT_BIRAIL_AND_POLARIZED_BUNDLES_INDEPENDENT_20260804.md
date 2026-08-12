# Independent audit: aligned `Ibc/Ica` ambient birail and polarized bundles

**Date:** 2026-08-04  
**Method:** independent pure-mathematical proof audit; no computation,
search, or solver  
**Audited theorem:**
`MATH_THEOREM_ALIGNED_IBC_ICA_AMBIENT_BIRAIL_AND_POLARIZED_BUNDLES_20260804.md`  
**Audited SHA-256:**
`7906b08d7d7953b2d8a22730fa6cd79f637f2f2e732890696155e3e1b0d3770e`  
**Verdict:** `GO` within the theorem's explicit local-to-ambient scope.

## 1. Correct active pair

The authenticated phases place `Ibc,Ica` at macro positions `5,6` in
phase `P` and `Ica,Ibc` there in phase `Q`.  With

\[
 J=K\cup\{\infty,c\},\qquad
 (x_0,y_0)=(b,a),\qquad (x_1,y_1)=(a,b),
\]

the first block has active set `J+{x_epsilon}` and the second has stable
core `K+{infinity,y_epsilon}` with pivot `c`.  The claimed phase table is
therefore the genuine aligned `a/b` birail action, not the superseded
`Cd/Ic` surrogate.

## 2. Guard and filler addresses

For internal filler `f_i`, the unique zero owner forces occurrences at

\[
 t+i-1,\qquad t+i+d+1
\]

and excludes the whole interval `[t+i,t+i+d]`.  On the first block the
right-side ray range excludes both guard fillers by the lower/upper screen
pattern; on the second block the left-side ray range excludes them by the
upper/lower pattern.  These are one-sided assertions only, exactly matching
the ray intervals actually used.

The stable-core and pivot pins all lie in their permissible source ranges.
Across the middle screen their gaps are at most `d+1`, so the coordinatewise
extension lemma produces one exact antecedent in each phase.  Nonempty
`K`, present in every local owner and screen, gives nonempty source letters.

## 3. Exact rays and the `d=2` boundary

The forced post-zero occurrence of `f_i` belongs to the prefix interval
`X_j` exactly when `i<=j`; the forced pre-zero occurrence belongs to the
suffix interval `Y_j` exactly when `i>j`.  The pins supply the advertised
stable core and pivot, while the screen zeros exclude guards and opposite
active labels.  Hence the literal values are

\[
 (J+b+P_j,J+a+S_j)\longleftrightarrow
 (J+a+P_j,J+b+S_j).
\]

For `d=2`, the only ticket is `j=1`; both ray intervals are singletons at
the forced/pinned addresses, and the endpoint port cases `i=0,2` are met by
the displayed active pins.  No exceptional endpoint case is hidden.

## 4. Native diamonds and occurrence capacity

For each native port, the two omitted fillers are excluded by their zero
intervals and every other filler is supplied by a forced occurrence.
The active pins meet every port, including both endpoint ports.  Thus the
port, owner, and q1 values are exactly the claimed intersection, owner, and
union values.

Across the `d-1` tickets, the addressed ray, port, owner, and q1 interval
occurrences are injective in their respective roles and distinguished by
interval length where roles meet.  This proves pairwise occurrence
disjointness **inside the displayed bundle bank**.

## 5. Two essential scope cautions

1. The phase-specific words `A^0,A^1` are exact antecedents.  Their
   pointwise union is only a source-letter **containment cap**.  In general
   it is not an exact antecedent for either phase and does not prove one
   common terminal cap state.
2. Bundle occurrences are disjoint from one another, not automatically
   from the transported background compiler.  State-aware polarized type
   acceptance and simultaneous background coexistence remain hypotheses.

Accordingly, the theorem materializes the true aligned rays and native
socket multiplicity, but it does not close terminal common-cap feasibility,
global packet planting, or regeneration.  With those exclusions retained,
the proof is sound.
