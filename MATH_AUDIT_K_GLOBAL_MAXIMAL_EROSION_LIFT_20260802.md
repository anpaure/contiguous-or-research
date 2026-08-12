# Audit of the global maximal-erosion lift

**Date:** 2026-08-02  
**Object audited:**
`MATH_THEOREM_K_GLOBAL_MAXIMAL_EROSION_LIFT_AND_COARSENED_HISTORY_GATE_20260802.md`  
**Verdict:** PASS for the fixed full-depth-chronology post-insertion source lift, with
the temporal/preword and terminal rows explicitly outside scope.

## 1. Independent derivation

Fix a full depth word `T_0,...,T_(N-1)` and a putative source address
`j`.  If a source coordinate `x` occurs at `j`, then `x` occurs in every
depth window using `j`, namely all

\[
               i\in [\max(0,j-d),\min(N-1,j)].
\]

It must also lie in the address cap.  Therefore every feasible source letter
is contained in the envelope `E_j` of (1.5).  This proves necessity of all
three rows (1.7): pins lie in the envelope, the source letter cannot be
empty, and each depth-row coordinate needs an envelope occurrence in its
window.

Choosing the whole envelope at each address cannot add an unwanted depth-row
coordinate: `E_j` is contained in every depth window using `j`.  The
coverage row then prevents a missing depth-row coordinate.  Hence `A_j=E_j`
is sufficient and is pointwise maximal.  No matching or integrality theorem
is hidden here.

The same argument does not use consecutiveness.  For any prescribed family
of source-position sets `H` with required unions `R_H`, every letter at `j`
lies in the intersection of all `R_H` containing `j`; choosing the resulting
maximal envelope works exactly when it covers each `R_H`.  This confirms
Theorem 1.2 and its simultaneous use for post-insertion windows, deleted
crossing windows, chosen preword upper occurrences, and literal compiler
intervals.

If a source address occurs in no prescribed row, its maximal envelope is
just its cap.  The nonempty-envelope row remains necessary because the word
model forbids empty source letters.  This causes no hidden issue in PCPS,
where every source address lies in a post-insertion depth window.

For one coordinate, an internal full-depth-row run `[a,b]` allows exactly source
positions `[a+d,b]`.  Its backward length-`d` dilation is `[a,b]` exactly
when `b-a+1>=d+1`.  Left and right boundary runs have the clipped envelopes
shown in (2.2) and impose no minimum length.  This independently confirms
Corollary 2.2.

Finally,

\[
 \bigcup_{i=p}^{q}\bigcup_{j=i}^{i+d}A_j
      =\bigcup_{j=p}^{q+d}A_j,
\]

because the union of those index intervals is `[p,q+d]`.  The all-width
post-insertion identity is exact.

For the intended Johnson host, envelope nonemptiness is automatic before
caps.  Any `d+1` consecutive rank-`m` owners have intersection rank at least
`m-d`.  A block containing the outer rank-`m-1` ticket starts with that
ticket, loses nothing at its containment step, and loses at most `d-1`
elements afterward, again leaving `m-d`.  Thus the uncapped global lift is
equivalent to residence of the **full** depth row, not merely of the owner
subsequence.  The distinction is load-bearing: the boundary ticket can turn
a formerly clipped owner run into an internal short run.

If caps differ from `U` only on an address set `H`, every envelope outside
`H` is unchanged.  A depth coverage union `[i,i+d]` is unchanged whenever
it avoids `H`, proving the sparse-halo bound `(d+1)|H|`.  This verifies
Corollary 2.5 and shows that an `O(d)` literal collar has only an `O(d^2)`
source-lift halo.  It does not localize independently selected long upper
occurrences.

## 2. Short-component audit

On the full-overlap face, component starts advance by at least one.  A
source address can consequently lie in at most `d+1` component images.
Three one-owner components at `d=2` attain the first nonadjacent overlap.
The cap triple

\[
                         \{a\},\ \{a,b\},\ \{b\}
\]

has two nonempty adjacent intersections and empty total intersection.  This
validates the warning against edgewise existential seam projection.  With
complete exact middle-block states, letter equality is transitively bound;
the independent remaining failure is collision of two nonadjacent named
physical pins.  The theorem now distinguishes these two cases.

If a coarse intervening block contributes at least `d` new depth cells, the
preceding block's source interval ends before the following block begins.
Thus only adjacent coarse blocks overlap.  Greedy groups have at most `d`
components, except a last remainder merged into its predecessor, which has
at most `2d-1`.  Lemma 5.1 is therefore correct, but it is a bounded-width
dynamic-programming reduction rather than an original-component Hall
theorem.

For a fixed source fragment `B` with `D^d(B)=P`, an interior source address
`u in [d,n-1]` is used only by depth cells of `P`, so its exact fixed letter
is automatically compatible with the global envelope.  Only the first and
last `d` source letters are exposed to exterior depth cells.  Likewise,
only the `d` depth windows immediately before and after `P` can have their
coverage changed.  This independently confirms the four `d`-row families
in Theorem 5.2.  For the `3d+1`-owner split-core collar, the full literal
embedding audit is therefore bounded, even though the ambient owner path is
Catalan-scale.

## 3. Exact scope boundary

The theorem closes only the following implication:

\[
 \begin{array}{c}
 \text{fixed rooted post-insertion full depth chronology}\ +
 \text{caps/pins}\ +
 \text{residence and nonempty envelopes}
 \end{array}
 \Longrightarrow
 \text{one global source antecedent}.                 \tag{3.1}
\]

It does not prove:

1. the rooted upper-exact full chronology and its Hamilton owner subsequence;
2. the corrected omitted-root endpoint aperture unless imposed;
3. that deleting a designated star from the antecedent gives the required
   pre-insertion crossing ranks, unless the exact crossing sets have first
   been selected and included in Theorem 1.2;
4. upper completeness of that deleted preword;
5. common-cap/compiler feasibility; or
6. regeneration.

In particular, monotone upper preservation is one-directional.  The fact
that the post-insertion full depth word is upper-complete does not imply that the
word obtained by deleting the star was upper-complete.  Selecting one
preword interval per target converts this residual into the exact closure
test (1.11), but existence of such a selection is still open.  This scope is
explicit in Sections 0, 1, 6, and 7 of the theorem note.

The reported K17 one-hole mask `32058` remains unauthenticated here and is
not used as evidence for (3.1).  Even after its owner-layer replay, all six
rows above require separate checks.
