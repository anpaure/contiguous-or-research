# Independent hostile audit: the two-suffix q2-safe C16 switches

**Date:** 2026-08-13  
**Audited source:** `MATH_THEOREM_T2_TWO_SUFFIX_C16_Q2_SAFE_SWITCH_AND_C8_C10_OBSTRUCTION_20260813.md`  
**Audited SHA-256:** `407f7728eb6541bac1b98850ce143c044774f9f31e5437f794370d7ddf0ff50a`  
**Verifier SHA-256:** `3b668ef31f46fa05c4fc6ab450a5d7c8225e3d01f408142b46884427daa474ae`  
**H100 output SHA-256:** `57f5e72e435923d26754830486fa35d4298e182e52d4ff2a96a249922c75b9e7`  
**Verdict:** **PASS after two incorporated scope corrections.**

## Corrections incorporated during audit

1. The original distance replay excluded degree-one owner endpoints.  Its
   lower bounds \(22,16,16,20,16,16\) therefore apply only to alternating
   cycles whose owner vertices are internal in the open MSW forest.
   Allowing endpoint owners changes the exact directed-distance sums to
   lower bounds \(18,14,14,18,14,14\).  Literal label-simple cycles of
   these lengths exist.  Both tables still exclude C8 and C10.
2. A directed owner cycle is an alternating incidence cycle only when its
   arc-colour labels are pairwise distinct.  The rebound source now uses
   directed cycles only as necessary projections for the distance lower
   bound and checks label distinctness for the explicit C16s.

## Checks

1. In each of the two displayed instances the eight owners have rank eight,
   the eight colours have rank nine, and every old/new colour contains its
   owner.  The old incidences are selected and the new incidences are
   unselected in the exact post-T2 semilength-eight factor.  Owner and
   colour sets are disjoint across the two C16s, so simultaneous toggling
   preserves both exact degree ledgers.
2. The complete q2 ledger was recomputed from each owner's unchanged mate.
   Every negatively charged value retains load at least one, separately and
   simultaneously.  This is support monotonicity, correctly not claimed as
   multiplicity preservation.
3. Concatenation of MSW insertion/deletion orders under a Dyck suffix leaves
   every selected/unselected prefix incidence unchanged.  Every old backup
   occurrence tensors by the same \(U(W)\), so its base load lower bound
   survives.  Distinct Dyck words have distinct up-step sets; suffix
   projection therefore separates all owners and colours of different
   copies.
4. The verifier was rerun on H100 and reproduced the advertised final
   artifact hash exactly.

## Scope

The theorem supplies a Catalan-tensorable owner/q1-exact, q2-support-safe
cross-phase switch bank for aligned suffix pairs \(1100W/1010W\).  It does
not prove residence, a desired socket multiplier, that the two named T2
arcs lie in one resulting chronology, or coverage of arbitrary adjacent
Dyck suffixes.
