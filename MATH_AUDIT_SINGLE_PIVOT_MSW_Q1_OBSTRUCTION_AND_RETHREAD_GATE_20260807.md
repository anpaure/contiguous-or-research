# Audit of the single-pivot MSW upper-q1 obstruction and rethread gate

**Date:** 2026-08-07  
**Audited theorem:**
`MATH_THEOREM_SINGLE_PIVOT_MSW_HAMILTON_HOST_Q1_OBSTRUCTION_AND_RETHREAD_GATE_20260807.md`  
**Method:** proof and parameter audit; no search or solver  
**Verdict:** `GO` with the scope stated in the theorem.

## 1. Parameter alignment

The endpoint-preserving MSW/MNW theorem uses a ground set `Omega` of size
`2r`, canonical rank-`r` paths

\[
 X_0,Y_0,X_1,\ldots,Y_{r-1},X_r,
 \qquad |X_i|=r, |Y_i|=r+1,
\]

and lifts them to `ML_(r+1)` after adjoining `z`.  The audited theorem sets
`r=m`.  Therefore its `z`-free owners are exactly the rank-`(m+1)` sets
`Y_i`, and

\[
 Y_i\cup Y_{i+1}=X_i\cup X_{i+1}\cup X_{i+2}
\]

is exactly the canonical MSW upper-`q2` map.  No rank shift is missing.

## 2. Transfer of the missing family

The canonical obstruction theorem gives `Cat_(m-6)` distinct missing
rank-`(m+2)` subsets of `Omega` for every `m>=6`.  The identity
`F_z(H)=P_m` fixes every `z`-free MSW path inside the Hamilton cycle.
Every owner window not wholly in that half contains `z`; hence it cannot
represent one of these subsets of `Omega`.  The transfer to the full
Hamilton cycle is therefore exact.

A coordinate permutation of `Omega` maps both witnesses and targets
bijectively, preserving the missing count.  The protected-pivot embedding
uses only such a permutation on one canonical component, so it does not
invalidate the obstruction.

The local-repair lower bound is correctly scoped to packets changing at
most `b` turn values.  It makes no claim against one global
Catalan-support move.

## 3. One-coordinate cut ledger

Write

\[
 W={2m\choose m},\qquad V={2m\choose m+1},\qquad
 C=\operatorname {Cat}_m={W\over m+1}.
\]

Then

\[
 W-V=C,\qquad W-(V-C)=2C.                            \tag{3.1}
\]

Cutting a Hamilton cycle at the vertical `z`-edges leaves two spanning
path forests.  All their endpoints are rank-`m` sets.  Each path in either
forest has one more rank-`m` vertex than the opposite shore, so (3.1)
forces exactly `C` components and `2C` common endpoints.  Conversely, two
such forests with the same endpoint set and connected vertical union give
a connected spanning 2-regular graph, hence a Hamilton cycle.  The stated
equivalence is exact.

Suppressing the internal rank-`m` vertices of the `z`-free forest leaves
`V-C` Johnson edges.  Pairwise-distinct intersection colours use `V-C`
rank-`m` sets, and (3.1) leaves exactly `2C` sets for the endpoint
occurrence matching.  Thus no endpoint slot is omitted or counted twice.

## 4. Residence scope

The cited free-repeat theorem gives the exact two-sided core conditions at
MSW seams.  The audited theorem correctly says that the published MNW join
does not certify them.  It does not claim that the join fails residence,
only that global residence remains unproved.  For a non-MSW rethread, the
correct requirement is depth-`h` residence; bi-core safety is only its
MSW-geodesic specialization.

## 5. Scope conclusion

The theorem proves a no-go only for the endpoint-preserved canonical MSW
half and bounded-turn repairs of it.  It does not rule out:

* a Catalan-scale rethread;
* a noncanonical owner forest;
* another distinguished coordinate;
* or the protected doubly-coloured common-endpoint forest isolated in its
  Section 5.

It also does not promote immediate upper-q1 coverage to the deeper upper
deck or to a global literal compiler.  Those qualifications are present in
the theorem, so no correction is required.

