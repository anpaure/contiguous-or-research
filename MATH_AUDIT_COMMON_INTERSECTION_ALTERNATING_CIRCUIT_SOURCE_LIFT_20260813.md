# Hostile audit of the common-intersection alternating-circuit source lift

**Date:** 2026-08-13  
**Audited file:**
`MATH_THEOREM_COMMON_INTERSECTION_ALTERNATING_CIRCUIT_SOURCE_LIFT_20260813.md`  
**Audited SHA256:**
`9d08b28b364fde7ef371ddc2fc88b81d49a5fa4eb14ba608b6b20297f7e3fa29`  
**Verdict:** **PASS after the cut-separation premise and prior-art/scope
corrections were incorporated in the audited bytes.**  The result is a
prospective local source lift.  It is not an occurrence theorem inside an
already fixed PBBS source chronology.

## 1. Arbitrary permutations and several cuts on one component

Cutting a cyclic source component immediately before all of its tagged
`Y` occurrences decomposes it into disjoint residual paths, one beginning
at every cut.  The new predecessor role of the path beginning at `Y_j` is
the unique `i` with `pi(i)=j`.  Thus an arbitrary permutation `pi`, not
only one cycle, gives a well-defined reattachment of all path heads.

The load-bearing physical hypothesis is cut separation: no tagged `Y` cut
may occur strictly inside another displayed left block

\[
                 X_h,C_1,\ldots,C_d.                 \tag{1.1}
\]

Under this premise, a residual path ending at the cut before `Y_h` contains
the complete block (1.1).  Consequently an interval traversing two changed
seams contains

\[
                 H\cup X_h=A_h,                     \tag{1.2}
\]

and has rank at least `R`.  Without cut separation this inference is false:
an intervening cut can truncate (1.1).  The theorem now states the premise
explicitly; occurrence-disjoint displayed fragments are a sufficient
implementation.

## 2. Strict-lower occurrence bijection

Consider a new seam whose transported right path begins at `Y_j`.  A
strict-lower interval crossing that seam cannot reach its left screen
`X_i`, because then it contains `H union X_i=A_i` of rank `R`.  It is
therefore exactly a suffix of the literal common history followed by a
prefix of the tagged path beginning at `Y_j`.  The old seam before the
same tagged path has the identical history suffix and identical right-path
prefix.  Sending the new occurrence there preserves its width and OR value.

By Section 1, a strict-lower interval crosses at most one changed seam.
Every remaining occurrence is internal to one residual path and stays
literal.  Applying the inverse permutation gives the inverse map, including
when one old component was cut several times.  This proves an actual
occurrence bijection, rather than only equality of value supports.

For clarity, every width-`d+1` window crossing a changed seam is handled by
the same seam map, even if its rank is not below `R`; the two distinguished
internal windows are the displayed owners `A_i` and `B_j`.  Hence the
owner-row interpretation is consistent with the local proof.  No analogous
claim is made for arbitrary longer exterior upper intervals.

## 3. Internal deck and residence

An internal fragment has length `d+2`.  Widths at most `d` are one-sided.
At width `d+1`, the multisets are the fixed `A` bank and the permuted `B`
bank.  At width `d+2`, the values are the old and new immediate unions,
whose multisets agree by hypothesis.  These cases exhaust the complete
internal deck.

For any cyclic source word, one occurrence of a coordinate belongs to
`d+1` consecutive length-`d+1` owner windows.  The positive trace is a
union of such cyclic intervals; every proper nonempty component therefore
has length at least `d+1`.  Permuting complete residual paths changes no
source length.  This proves exactly positive residence and zero length
charge.  It supplies no lower bound on zero gaps.

## 4. Short-support corollary and exact scope

Along an `ell`-edge Johnson walk, at most one coordinate is deleted per
transition, so the intersection of all walk owners has rank at least
`R-ell`.  If all auxiliary owners retain that intersection and
`ell<=R-d`, a `d`-element common history can be selected and partitioned
into nonempty source letters.  Theorem 2.1 then applies to every
palette-neutral alternating trade after cut-separated prospective
fragments are installed.  This proves Corollary 3.1 at its local scope; it
does not plant the fragments in a frozen factor.

The construction generalizes the rank-three five-head argument in
`MATH_THEOREM_PBBS_PENTAGON_THREE_SCREEN_COMMON_HISTORY_AND_UPPER_CURRENT_GATE_20260805.md`.
It does not supersede that note's Section 6: the complete exterior-current
tensor is still the exact ledger for all longer crossing upper intervals.
In particular, common intersection, palette neutrality, and positive
residence alone do not imply exterior upper transparency, zero-gap safety,
socket neutrality, or typed-cap functoriality.

