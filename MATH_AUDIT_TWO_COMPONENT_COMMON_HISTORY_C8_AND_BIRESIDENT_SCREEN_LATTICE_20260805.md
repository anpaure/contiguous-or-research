# Independent audit: common-history `C8` and its biresident screen lattice

**Date:** 2026-08-05  
**Method:** literal sliding-window algebra, Boolean palette identities, and
permutation/component calculus; no computation or search  
**Verdict:** **GO after the scope corrections recorded below.**

## 1. Audited artifacts

The audited theorem files, after correction, are

1. `MATH_THEOREM_TWO_COMPONENT_COMMON_HISTORY_C8_CROSSOVER_AND_MINIMALITY_20260805.md`,
   SHA-256
   `f3b14587b0e74d163bb0c28b39ba8beec87fbd5a0cc39b247d3937e70348372f`;
2. `MATH_THEOREM_BIRESIDENT_COMPOUND_C8_SCREEN_LATTICE_20260805.md`,
   SHA-256
   `764937c35bde8b4e621b508889c265391c43eb2c3f52527ef79cc1378b378773`.

The first file was received at SHA
`56fe4c68ce0df64a45510a183e390f4224549058a1ca4408e7aa2ed6bc689ce0`.
The second was received at SHA
`c7d0275fbc8de25bc243a73e8b1db64bf91e480476cee28d43c4981ead85b02a`.

## 2. Corrections to the abstract crossover theorem

### 2.1 Raw reset

The equality

\[
 \delta_d(H,G)=d-\operatorname{ov}(H,G)
\]

is exact in the unrestricted literal order-`d` de Bruijn graph.  The
intermediate appended states need not satisfy the owner-rank, Johnson,
palette, upper, or cap guards.  The theorem now states this explicitly:
the metric is exact before those guards and is a lower bound for a guarded
raw reset.  The PBBS conclusion is unchanged, because the bare lower bound
`d-2` is already unbounded.

The imported rigid braid--residual table proves that no aligned compatible
block has length three.  Therefore `s_*<=2` in all four orientation cases,
including arbitrary legal nonmaximal thinning.  The seam is pointwise
incompatible.  This part is GO.

### 2.2 Cut roles and short-deck transport

The original wording incorrectly spoke of `q` source components, whereas
the sharp `C8` has four cut roles on two components.  The corrected setup is
`q` distinct cut roles distributed among any collection of cyclic source
circuits.

After cutting at the common literal history, all pieces are walks from the
same order-`d` de Bruijn state back to itself.  Reassembling these walks
permutes complete continuations and gives an occurrence bijection for every
source subword of width at most `d+1`.  To infer the unrestricted
strict-lower statement, the theorem must and now does assume a depth-`d`
rank-`r` factor: every width-`d+1` source interval has rank `r`.  Then every
strict-lower interval has width at most `d`, so the same occurrence
bijection transports the complete strict-lower deck and every matching on
it.  Adequate resulting circuit length is also stated in the positive-run
claim.

### 2.3 Minimum support

For support two, the direct/direct and cross/cross palette identifications
force a repeated head or tail.  In the mixed case with lower colours matched
directly, both distinct heads contain two rank-`(r-1)` intersections; those
intersections must coincide.  Writing all four owners as one common core
plus one label, the crosswise upper equality forces the two tails to agree.
Boolean complementation proves the other mixed case.  Thus the support-two
no-go is complete.

For support three, a transposition leaves one occurrence fixed; subtracting
that occurrence from both palette multisets reduces to support two.  A
genuine three-cycle is even, whereas changing the component count from two
to one changes the sign of the cut permutation.  Thus support three is
topologically impossible.  Both arguments are proof-safe on the declared
zero-charge, one-copy Johnson/q1 face.

### 2.4 `C8` identities and history generalization

The literal identities replay exactly:

\[
 L_i=B+b+a_i,\qquad R_i=B+a_{i-1}+a_i,
\]

\[
 L_i\cap R_{i+1}=B+a_i,qquad
 L_i\cup R_{i+1}=B+b+a_i+a_{i+1}.
\]

Hence lower colours are fixed and upper colours are cyclically permuted.
With old cut permutation `(0 2)(1 3)` and head cycle `(0 1 2 3)`, the new
permutation is `(0 3 2 1)`, so the two components fuse.

Disjointness of the history letters is unnecessary.  The proof uses only
their literal ordered equality and union `B`.  The corrected theorem permits
overlapping nonempty `H_j` with union `B`; this is important for prospective
PBBS histories and removes the artificial condition `d<=r-2`.

### 2.5 Long upper interface

Widths at most `d+1` transport exactly.  A longer crossing interval whose
left endpoint lies inside the common history transports with the identical
history suffix until it ends or reaches another selected cut.  If it reaches
another cut, it contains a complete fragment `X_j mathcal H Y_j`; if it
starts before the history, it already contains such a fragment at its first
cut.  Therefore every untransported value contains one old rank-`(r+1)`
hinge union `U_j`, and the stated four-cone localization is correct.  This
is not a bounded casualty theorem.

### 2.6 PBBS and pivot no-go scopes

The rigid theorem excludes a common length-`d` history only when both the
braid and residual hinge neighbourhoods are left unchanged.  It does not
exclude a prospectively rebuilt endpoint.

The canonical split-core pivot output has `d-1` singleton rho letters.
Every rigid braid/residual forced set has two distinct coordinates for
`m>=6`, `d<=m-3`, so that displayed canonical state cannot equal an
unchanged rigid history.  This does not exclude legal enlargement of the
pivot rail or a different compound pivot.  The corrected theorem retains
exactly this narrow scope.

## 3. Audit of the biresident screen lattice

### 3.1 Coordinate supply and source-window rank

Each core block must contain two distinct removable coordinates.  The
construction now explicitly requires `|C_j|>=2`; `|B|>=2d` is the
corresponding sufficient supply.  The `2d` fresh `y` coordinates and nine
active coordinates give the stated outside supply `2d+9`.

Screens occur once every `d+1` source positions.  A width-`d+1` window
therefore contains exactly one screen and, for every block index `j`,
exactly one of `C_j` and `C_j^s`.  These chosen core blocks remain disjoint
and have total rank `r-2`; the active screen is disjoint and has rank two.
Every owner consequently has rank `r`.

Sliding one step either swaps the unique differing pair
`x_(s,j)<->y_(s,j)` or exchanges the noncommon coordinates of consecutive
screens in

\[
 A_i,D_i,P_i,Q_i,A_{i+2}.
\]

Each step is therefore a loopless Johnson step.

### 3.2 Owner and immediate-palette simplicity

The intersection of an owner with the active bank is exactly its screen.
All sixteen screen values are distinct, so different screen runs cannot
collide.  Within one run, the prefix/suffix of its private `y` bank recovers
the stage.

On a core-swap edge, the lower and upper active trace has size two and the
changed block/profile recovers the edge.  On a screen-swap edge, the lower
active trace has size one and the upper active trace has size three.  The
four screen-swap families are distinguished by the common active coordinate
and by core state `B`, `B^1`, or `B^2`; private `c_i` coordinates separate
ports.  Hence owners and both immediate palettes are globally simple in the
local bank, before and after rethreading.

### 3.3 Topology and short cells

From the cut after role `i`, the unchanged continuation reaches role
`i+2`; after assigning the head beginning at `D_(i+1)`, it reaches role
`i+3`.  Thus the old next-role permutation has two cycles and the new one is
one four-cycle.  The common-state Euler argument transports every source
subword through width `d+1`; the rank-`r` owner law then transports every
strict-lower occurrence and its matching.

### 3.4 Biresidence

Screens have source residue zero modulo `d+1`; the `j`th old or changed core
block has residue `j`.  Every occurrence of every coordinate therefore lies
in one residue class.  Each continuation segment permuted by the crossover
has length `4(d+1)`, so this phase property survives the rethread.

A source occurrence covers an owner-start arc of length `d+1`.  Consecutive
occurrences are separated by `t(d+1)`.  Their positive arcs concatenate if
`t=1`; otherwise the intervening zero gap is `(t-1)(d+1)`.  Hence every
nonconstant positive run and nonempty zero gap is a positive multiple of
`d+1` in both phases.

### 3.5 Internal upper damage

Each old cycle has length `L=8(d+1)`, so its complete cyclic interval deck
has at most `L^2` based occurrences.  The two-cycle old internal deck has at
most `2L^2=128(d+1)^2` values.  Every untransported value contains an old
rank-`(r+1)` hinge union.  A value of exactly that rank equals the hinge
union, which still has a new immediate-upper witness.  Thus every actual
internal casualty has rank at least `r+2`.

This polynomial statement applies only to the isolated cyclic collar deck.
After the cycles are opened and grafted into external PBBS bodies, longer
crossing intervals can carry arbitrary exterior coordinates; the audit
patched the text so it no longer treats the `O(d^2)` internal bank as a
global exterior bound.

### 3.6 Protected-factor corollary

There are `16(d+1)` projected owner transitions and hence `32(d+1)`
middle-level incidence edges.  Owner and lower-colour simplicity makes the
protected incidence bank 2-bounded.  After specializing `r=m` on `[2m-1]`,
the small protected-factor theorem applies under

\[
                       32(d+1)\le m-2.
\]

The two protected old cycles are saturated components of every such
extension.  Replacing the four hinge incidence pairs preserves every owner
and lower degree and turns those two cycles into one, so the switched graph
is again an exact q1 two-factor with one fewer component.

This does not attach the collar to named PBBS components, enforce the
unprotected upper deck, or supply the typed cap/opening.  Those scope lines
are necessary and correctly retained.

## 4. Final verdict

The abstract `C8` crossover and the literal biresident screen lattice are
both **GO** at their corrected scopes.  The new collar closes the local
source-factorization, owner/q1, topology, and two-sided residence rows.  It
does not close the global protected graft, exterior long-upper witness, or
typed cap/opening rows.

