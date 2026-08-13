# Independent hostile audit: the three private singleton-T2 backup rails

**Date:** 2026-08-13  
**Audited source:** `MATH_THEOREM_T2_SINGLETON_THREE_PRIVATE_BACKUP_RAILS_AND_CATALAN_FACTOR_GATE_20260813.md`  
**Audited SHA-256:** `2749ab43838f487b3167a7c9c24650ca9567848c1957e4e5f52b66e2017c7f36`  
**Verdict:** **PASS at its final stated scope.**

## Corrections incorporated before this verdict

The frozen source now incorporates three issues found during hostile audit:

1. the staircase identities are
   \(\bigcup_{i=0}^jK_i=P_j\) and
   \(\bigcup_{i=0}^j\rho K_i=D_0\cup\cdots\cup D_{-j}\) for
   \(j\ge1\), with \(K_0=D_1\) exceptional;
2. the naive old-suffix tensor has owner rank \(r+h+2\), whereas the
   literal lifted MSW owner rank is \(r+1\), an overshoot of \(h+1\);
3. the \(H\)-rail is not wholly monotone: clock coordinate zero has the
   pattern \(1,0,\ldots,0,1\), but its bounded zero gap has length
   \(h+3\).  Global residence consequently requires endpoint-compatible
   collars, not merely collars described as monotone.

## Checks

1. All displayed prefix masks have the stated ranks.  Each consecutive
   pair in \(R_B,R_C,R_H\) differs by exactly one deletion and one
   insertion.  The rail sizes are respectively \(h+1,h+1,h+5\), hence
   \(3h+7\) owners and \(3h+4\) selected lower facets.

2. The forward staircase produces exactly
   \[
   B\cup\{p_0\}\cup(D_0\cup\cdots\cup D_j),
   \qquad 1\le j<h,
   \]
   and reflection by \(t\mapsto h-1-t\pmod{2h}\) produces exactly the
   corresponding \(C\)-family with \(D_{-j}\).  The \(H\)-path spans all
   of \(H\), both tags, and all \(2h\) clock labels.  These are precisely
   the \(2h-1\) ungraded casualties in the cited frozen residual theorem.

3. The symbolic path intersections imply that an arbitrary unused lower
   facet lies below at most two rail owners and an arbitrary owner contains
   at most two selected rail facets.  A separate full-facet replay on H100
   for \(2\le h\le20\) returned \((\alpha,\beta)=(2,2)\) throughout.  This
   agrees with, but is stronger than, the verifier's narrower within-bank
   statistic.

4. Internally bounded coordinate runs/gaps have length at least \(h\).
   The bare paths are clipped; the note correctly leaves the two-sided
   endpoint compatibility of resident collars as a premise.

5. The corrected fixed-rank calculation is decisive.  Appending the old
   constant Dyck suffix does **not** yield the literal T0V family.  Embedding
   tag and clock labels inside \(U(V)\) makes the residual core vary along
   the rail, so suffix-projection disjointness is unavailable.  No Catalan
   tensor count follows.

6. Collision freedom of the local paths does not balance their incidence
   current in a spanning factor.  The source correctly leaves as an open
   gate either a conformal alternating replacement or a new fixed-rank,
   varying-core protected-factor theorem.

## Exact scope

This is an unconditional local all-height provider theorem for the
ungraded singleton-T2 residual.  It is not yet a literal all-suffix repair,
a Catalan-scale factor insertion, or a globally resident completion.
