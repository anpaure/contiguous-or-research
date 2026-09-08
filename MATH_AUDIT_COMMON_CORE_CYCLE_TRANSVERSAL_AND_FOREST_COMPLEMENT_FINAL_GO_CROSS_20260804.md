# Final independent GO audit: common-core cycle transversal and forest complement

**Date:** 2026-08-04  
**Audited source:**
`MATH_THEOREM_COMMON_CORE_CYCLE_TRANSVERSAL_AND_FOREST_COMPLEMENT_20260804.md`  
**Audited SHA256:**
`a9db5e4ad7d5697ba51e5e9042ccb7be4426df2161eaa5e8b3361f5d95369649`

## Verdict

**PASS / GO in the stated reduction/conditional-fusion scope.**  The
successor preserves the previously audited nullity and fusion arguments,
adds the exact fixed-edge `delta_star` criterion correctly, and repairs the
promotion input wording: a coordinate-containment core is no longer
identified with one common ordered de Bruijn history.

## 1. Core identity

On each cycle component of a two-factor `F`, deleting no `S` edge leaves
one cycle and nullity one; deleting at least one `S` edge leaves only paths
and isolated vertices and nullity zero.  Additivity over components proves

\[
c_S(F)=\beta(F\setminus S).
\]

Thus every component meets `S` exactly when `F\setminus S` is a forest.
The forest-extension and induced-edge rank formulations are exact.

## 2. Fixed-edge extension criterion

Suppose first that a protected factor `F` exists.  With

\[
R_0=F\setminus S,
\]

the core identity makes `R_0` a forest; it lies outside `S union Z` and
contains `D\setminus S`.  Since every edge of `F` lies in `R_0 union S`,
`F` avoids

\[
Z\cup(E\setminus(R_0\cup S)),
\]

so the displayed `delta_star` value is zero.

Conversely, a factor supplied by that zero-deficiency condition contains
`D`, avoids `Z`, and uses outside-`S` edges only from `R_0`.  Hence
`F\setminus S` is a subgraph of a forest and is itself a forest.  This
proves both directions of Corollary 1.3.  The corollary does not assert
that the admissible `R_0` family is a matroid.

## 3. Fusion consequences

If every selected occurrence hinge is jointly all-pairs completed, choose
one in each factor component and apply a cyclic head permutation.  The
completed-hinge theorem turns the component successor permutation into one
cycle with zero added positions.  Joint legality is explicitly retained.

Under the common guarded overlap hypothesis, a linear order of at most
`C` components uses at most `C-1` connectors, giving the exact charge

\[
A+(C-1)K.
\]

Both results remain conditional on their full occurrence-level guard and
product hypotheses.

## 4. Corrected promotion scope

The successor now says only that the promotion atlas supplies a `2H`
coordinate-containment core in each relevant top-dependent word.  It
explicitly states that `2H>d` does not supply one ordered length-`d`
history shared across tops or components.  The still-open assertion is
therefore correctly identified as an occurrence-level common ordered
history and guard-signature bank `S` satisfying the forest-complement
condition while preserving compiler and upper-witness constraints.

The theorem is an exact reduction and conditional fusion theorem, not a
proof of that supply statement or of an additive-constant OR construction.
