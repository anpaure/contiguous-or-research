# Audit: residual Ore versus safe-pull component connectivity

**Date:** 2026-08-02  
**Audited note:**
`MATH_THEOREM_K_RESIDUAL_ORE_VERSUS_SAFE_PULL_COMPONENT_CONNECTIVITY_20260802.md`  
**Verdict:** PASS, with the scope qualifications below.

## 1. Projection check

Ore--Ryser and the two opposite LKK branches in the direct-new-phase
residual theorem use only the projected rank-`(m-1)`/rank-`m` incidence
table, its residual demands and same-shore codegrees.  Adding a component
tag to occurrence states and rejecting every mixed-tag circuit leaves all
of those quantities unchanged.  It removes every intercomponent safe pull.
Hence projected expansion cannot imply component-circuit connectivity.

This is a logical nonimplication, not a claim that the canonical Boolean
history table contains arbitrary component tags.

## 2. Fusion check

A binary pull lowers the component count by one; a ternary Boolean hex on
three distinct current components lowers it by two.  In a loose
`{2,3}`-hypertree each successive footprint meets the accumulated component
once and introduces exactly `|footprint|-1` new components.  Therefore

\[
             \sum_p(|\kappa(p)|-1)=c(F)-1
\]

leaves exactly one component.  Pairwise support disjointness makes the
switches commute.  The stated hereditary alternative is exactly what is
needed when supports overlap.

The warning about ordinary connectivity is necessary: two individually
safe pull labels can share one old occurrence/private token, so the
two-edge auxiliary path on three components need not be selectable or
serially executable.

## 3. Transversal check

For a component shore `S`, a protected bank kills every crossing
certificate exactly when it is a hitting set of their hazard sets.  Thus
robust survival against every bank of size at most `h` is equivalent to
minimum transversal greater than `h`.  If one resource blocks at most
`lambda_S` candidates, an `h`-bank blocks at most `h lambda_S`, proving the
count/load corollary.

This criterion certifies hypergraph connectivity only.  A compatible loose
spanning hypertree still requires private supports or a serial-hereditary
catalogue.

The cut certificate is exact for the frozen candidate catalogue.  It is not
a global no-go against preparatory moves which create new crossing circuits,
unless closure of the catalogue under within-side switches has separately
been proved.  In the dynamic setting the exact descending potential is the
component count, conditional on a safe coarsening switch at every reachable
nonterminal factor.

## 4. Exact scope

The note proves:

* LKK/Ore supplies marginal residual factor existence only;
* the sharp protected component-cut statistic;
* the exact additional compatibility needed for a pull/hex spanning tree;
  and
* the minimal strengthened joint theorem sufficient for topology.

It does not prove the intended Boolean host satisfies the cutwise
transversal bound, does not construct a compatible circuit basis, and does
not close upper, residence, charge or compiler rows.
