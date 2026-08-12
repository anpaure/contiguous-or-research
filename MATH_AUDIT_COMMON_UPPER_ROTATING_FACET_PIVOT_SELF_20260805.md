# Self-audit: common-upper rotating-facet pivot

**Date:** 2026-08-05  
**Audited file:**
`MATH_THEOREM_COMMON_UPPER_ROTATING_FACET_PIVOT_AND_EXACT_INTERFACES_20260805.md`  
**Method:** independent symbolic recount of indices, ranks, interval cells,
run lengths, and Catalan excess; no computation or search  
**Verdict:** GO with the scope boundaries recorded below

## 1. Index and owner replay

For the interval

\[
 J_j=[-(h-j),-1]\cup\{0\}\cup[1,j]
\]

the left labels are `c_(j+1),...,c_h`, the right labels are
`c_0,...,c_(j-1)`, and all letters contain `X`.  Its union is therefore
`R-c_j`.  Consecutive owners exchange `c_(j+1)` for `c_j`.  Their
intersection is `R-{c_j,c_(j+1)}` and their union is `R`.  This validates
all formulas in Section 1 and proves that the upper collision is real, not
an indexing artefact.

The old crossing length-`h` interval with `h-j` left and `j` right letters
has the same union `R-c_j`, for `1<=j<h`.  These are exactly the `h-1`
escaped cells.  A pivot-ended interval with `t` nearest left letters has
union `X+{c_(h-t+1),...,c_h}`; the right formula is dual.  This verifies
the complete band ledger.

## 2. Compiler scope

The zero-deficiency conclusion is conditional in exactly the same way as
the audited sharp monotone-pivot theorem.

* `X` must be a new target identity, or else its singleton is only a second
  occurrence of an old target.
* The old target occurrences equal to the two ray values must be released
  before the new ray edges are inserted.
* Strict-lower matching edges cannot use an escaped cell because every
  escaped value has rank `r`.
* Cell disjointness follows from the exact interval transport theorem, not
  merely from distinct masks.
* One simultaneous cap/maximal-word state is still required; local literal
  feasibility cannot be unioned with an independently chosen exterior cap.

No stronger compiler conclusion is stated.

## 3. Cap replay

A left source position `-i` lies in owner windows `M_0,...,M_(h-i)`, whose
intersection is

\[
 X+\{c_(h-i+1),...,c_h\}.
\]

The right formula is its reversal.  Their cumulative maximal letters keep
all owner and ray unions unchanged.  Hence Section 4 is an exact local cap
description.  It is not a proof that exterior rows leave those caps
nonempty.

## 4. Residence replay

The trace of `c_i` on `M_0,...,M_h` is all ones except at `M_i`.  The two
positive-run lengths are `i` and `h-i`.  Extending the first by `h+1-i`
and the second by `i+1` gives exactly `h+1` in both cases.  The abstract
halos have rank

\[
 (r-h)+(h+1-a)+(a-1)=r
\]

and consecutive terms differ by one exchange.  Their label count is

\[
 (r-h)+(h+1)+2+2(h-1)=r+2h+1.
\]

The halos are deliberately called abstract.  They cannot be pasted onto
the fixed source word because the old endpoint source states are already
rank-saturated; Section 6 proves that obstruction separately.  Filler and
seam-label residence remains clipped.  The one-owner zero gap at `M_i`
also correctly excludes any bi-resident interpretation.

## 5. Endpoint stutter replay

The union of the `h` left old letters is exactly `M_0`; adding any preceding
letter yields either `M_0` again or a strict superset of rank above `r`.
The right statement is identical.  Therefore an internal embedding creates
two distinct exceptional depth windows.  When the deadline is `h`, a word
of length `B+1=W+h+1` has `W+1` depth-`(h+1)` windows.  Two exceptional
windows leave at most `W-1` distinct owner windows and cannot cover the
`W`-element middle layer.  At a global source endpoint one adjacent window
does not exist, leaving exactly one possible exception.  This validates the
physical-length conclusion.

## 6. Upper excess and cap two

The central block contributes `h` occurrences of one upper colour, hence
`h-1` repetition excess.  An upper-complete owner path has excess

\[
 (W-1)-U=\operatorname {Cat}_r-1.
\]

Thus `H(h-1)<=Cat_r-1` is necessary.  The cap-two profile separately
forbids one colour from having `h>=3` occurrences.  Smoothing is a legal
Johnson shortcut because `M_0,M_h` are distinct facets of `R`, but it
deletes exactly `M_1,...,M_(h-1)` and cannot be treated as owner-free.

These statements do not claim that one fixed common-upper block obstructs
an unrestricted upper-complete word.  For fixed `H` the scalar repeat
budget has abundant slack.  The no-go concerns cap two, the `Cat_r-1`
balanced-collar bank, and an internal literal `B+1` placement.

## 7. Relation to prior results

With `Q=X`, `lambda_i=c_i`, and `rho_i=c_(i-1)`, the owner sequence is the
sharp aperture sequence with overlap
`{c_1,...,c_(h-1)}`.  The audited equality-case correction says precisely
that this overlap destroys geodesicity.  The forced endpoint-stutter
conclusion agrees with the existing strict-stutter-sidecar theorem.  The
upper multiplicity conclusion agrees with the Catalan cap-two theorem,
whose blocks have length at most two.

Therefore the new theorem duplicates none of the positive claims and
contradicts none of the audited scope boundaries.  Its new content is the
closed-form common-upper specialization and the exact combination of its
lower positive with its residence, source-stutter, and Catalan-excess
interfaces.
