# Independent audit: local deep-owner forced-pair separation

**Date:** 2026-08-06  
**Method:** direct event-index and run-length audit; no computation or search  
**Status:** GO at the corrected local scope.  The earlier global reading is
false when a coordinate has several runs; the theorem audited here excludes
only the owner interval and its depth-`d` forward collar.

This note audits
`MATH_THEOREM_DEEP_OWNER_INTERSECTION_FORCED_PAIR_SEPARATION_20260806.md`.

## 1. Index audit

Let

\[
 T_{j+1}=T_j-\{D_j\}+\{I_j\},\qquad
 F_j=\{D_j,I_{j-d-1}\},
\]

and put

\[
 S(i,q)=\bigcap_{h=0}^{q}T_{i+h}.
\]

For `i <= j <= i+q-1`, the deletion on edge `j` makes `D_j` absent
from `T_(j+1)`, hence from `S(i,q)`.  For
`i+d+1 <= j <= i+q+d`, put `e=j-d-1`.  Then
`i <= e <= i+q-1`, and `I_e` is absent from `T_e`, hence from
`S(i,q)`.

When `q>d`, the integer intervals

\[
 [i,i+q-1],\qquad [i+d+1,i+q+d]
\]

overlap or are adjacent and have union `[i,i+q+d]`.  Thus

\[
 F_j\not\subseteq S(i,q)
 \quad (i\le j\le i+q+d).
\]

If a source interval meeting this zone had union `S(i,q)`, every one of
its letters would be a subset of `S(i,q)`, contradicting the mandatory
inclusion `F_j subseteq A_j` at the meeting position.  The local theorem
and its stated collar are therefore exact.

No conclusion is valid outside this zone: another positive run of the same
coordinate labels can furnish a remote forced pair inside the same target.

## 2. Singleton audit

If `A_j={x}`, then nonemptiness and `F_j subseteq A_j` force

\[
 D_j=I_{j-d-1}=x.
\]

The insertion edge `j-d-1` creates the run at owner `j-d`, and deletion
edge `j` removes it after owner `j`.  The run therefore has exactly `d+1`
owner occurrences.  Conversely an exact-`d+1` run has eroded envelope
support at the single position `j`; there `F_j={x}` and the one-position
short-block theorem permits `A_j={x}`.  Thus the iff statement is correct.

This independently agrees with Corollary 7.3 of
`MATH_THEOREM_PBBS_SHORT_GAP_MANDATORY_CORE_LOCALIZATION_AND_BLOCK_TEMPLATE_20260805.md`.

## 3. Width audit

Let `J` be `ell<=d` consecutive source positions whose union is `S`.
The deletion labels `D_j`, `j in J`, are distinct.  If one coordinate were
deleted at two positions `j<j'` of `J`, it would have to be reinserted on
an intervening edge and then have a positive owner run of length at most
`j'-j-1<d+1`, contrary to positive `d`-residence.  Since every
`D_j in F_j subseteq S`, this gives

\[
                         \ell\le |S|.
\]

The proof needs only positive-run residence; zero-gap residence is not
needed.  This is a valid strengthening of the older insertion-label proof.

## 4. Audit verdict

The corrected theorem is proof-safe exactly as follows:

1. a depth-`q>d` owner-intersection target has no literal source occurrence
   in `[i,i+q+d]`;
2. it may still have remote occurrences elsewhere;
3. every singleton requires a minimum positive run of length `d+1`;
4. every width-`ell<=d` witness contains `ell` distinct deletion labels.

Hence the canonical gap-section occurrence SDR cannot be localized.  The
remaining lower theorem must be a global remote occurrence selector, and
must simultaneously engineer minimum runs for all coordinates.
