# Audit: pairwise conformal MSW portals for internal PBBS height-spine targets

**Date:** 2026-08-13  
**Audited source:**
`MATH_THEOREM_PBBS_INTERNAL_HEIGHT_SPINE_TARGETS_HAVE_PAIRWISE_CONFORMAL_MSW_PORTALS_20260813.md`  
**Source SHA-256:**
`153a8043a116d879ea898f2549fb80cf783d1a1195bf062b0d6ec5a0f5de09eb`  
**Verdict:** **PASS**, at the source's stated set-valued and
componentwise scope.

## 1. Height-spine normalization

For

\[
 U_h=\{0\}\dot\cup[h+1,2h]
       \dot\cup\{2h+2,2h+4,\ldots,2m\},
\]

direct intersection over `h=A,...,A+q` gives

\[
 \bigcap_{t=A}^{A+q}U_t
 =\{0\}\dot\cup[A+q+1,2A]
       \dot\cup\{2A+2,2A+4,\ldots,2m\}.
\]

When `A>=q`, its size is

\[
                         1+(A-q)+(m-A)=m+1-q.
\]

When `A<q`, the ordinary interval vanishes and the rank is too large.
The equality `S_(q,q)=S_(q+1,q)` is literal: the latter description moves
the coordinate `2q+2` from the even tail into the one-point ordinary
interval.  Restricting normal forms to `A>=q+1` therefore removes exactly
the one boundary duplication.

The upper bound `A<=m-q` is exactly the requirement that all `q+1` owners
remain on the displayed spine.  No exterior-return target is silently
included.

## 2. Flip-list recurrence and parity

Write

\[
 a=2q-3,\quad b=A-q,\quad c=m-A-q+1,
 \quad V=1^b0^b(10)^c,
 \quad W_j=1^jV0^j.
\]

The hypotheses give `a` positive odd and `b,c>=1`.  The two-shell MSW
recurrence is

\[
 \rho(W_{j+2})=
 (2M_j+4,2,\rho(W_j)+2,2M_j+3,1),
\]

and taking odd list positions yields exactly

\[
 \mathsf O(W_{j+2})=
 (2M_j+4,\mathsf O(W_j)+2,2M_j+3).
\]

There is no parity reversal error here.  At the base shell `q=2`, the
retained part of `mathsf O(W_1)` is the reversal of
`mathsf O(V)+1`, whose set is

\[
 [A+q-2,2A-3]\dot\cup
 \{2A-1,2A+1,\ldots,2m-5\}.
\]

Increasing `(A,q,m)` to `(A+1,q+1,m+2)` holds `b,c` fixed.  The new leading
entry enlarges the discarded prefix by one; the old retained entries
translate by two; and the new terminal odd-position entry is `2m-1`, the
new largest required value.  This proves the induction for every odd
shell `a=2q-3`.

## 3. Literal portal and row-disjointness

In the positive row `(3,4,E,1,2,O)`, the suffix of `E` beginning at the
`q`-th odd-list entry, followed by one-based label `1`, is consecutive.
After subtracting one, its set is exactly

\[
 \{0\}\cup[A+q+1,2A]
 \cup\{2A+2,2A+4,\ldots,2m\}=S_{A,q}.
\]

Its length is `m+1-q`, so the cited interval-to-clean-package theorem
applies with the correct rank and pointing.

The initial positive and zero runs of `z_(A,q)` have lengths
`A+q-3` and `A-q`; they recover `(A,q)`.  Thus all selected Dyck roots are
distinct.  Injectivity of the canonical MSW root-row indexing then makes
their negative rows pairwise distinct.  Each pair is an actual applicable
inverse-triple trade, and conformal simultaneous substitution gives an
exact factor.  Exactness makes the positive middle-window decks pairwise
disjoint and disjoint from untouched rows.  Complementation gives the
rank-`R` owner statement.

This verifies **middle owners and immediate-lower resources**.  It does not
upgrade the theorem to pairwise disjoint nonmiddle halo tickets; the source
does not make that upgrade.

## 4. Whole-packet host and casualty census

Every selected root begins with `1100` or `1010`, so the eligible block at
positions `0,1,2,3` is automatically its first aligned block.  Hence every
selected trade belongs to the offset-zero first-aligned involution packet.
Applying the whole packet is valid because that packet has row-disjoint
negative pairs.  Other packet trades cannot collide at middle rank with a
selected positive row, by the same conformal-support identity.

For deleted edges `U_hU_(h+1)`, `4<=h<=d`, an internal `q`-edge interval
has literal start `A<=d`.  Correct rank forces `A>=q`; the value at `A=q`
normalizes to `A=q+1`.  Thus for `2<=q<d` there are at most `d-q` distinct
normal forms and `q=d` contributes the one boundary representative
`A=d+1`.  The displayed total

\[
 \sum_{q=2}^{d-1}(d-q)+1
 =\frac{(d-2)(d-1)}2+1
\]

is correct.  It is a census of distinct values, not an
occurrence-labelled casualty multiset.

## 5. Residence scope

In a cyclic wreath row, a coordinate occurs in one owner run of length
`m+1` and one gap of length `m`.  Since the theorem assumes
`m>=3d+2`, both exceed the deadline.  Therefore every component is
positive- and zero-resident, and the pointed portal survives in that
component's maximal antecedent.

This proves only componentwise residence.  It does not fuse the wreath
components, place an independently frozen PBBS module in the same factor,
or cover exterior-return casualties.  Those exclusions in the source are
mathematically necessary and correctly stated.

## 6. Audit conclusion

No flaw was found in the rank normalization, the shell recurrence, the
portal pointing, the negative-row-disjoint packet argument, the quadratic
distinct-value census, or the full-wreath residence claim.  The theorem is
safe to cite at its literal scope:

\[
 \boxed{\text{distinct internal correct-rank target set}
 \Longrightarrow\text{one componentwise resident exact MSW host}.}
\]

