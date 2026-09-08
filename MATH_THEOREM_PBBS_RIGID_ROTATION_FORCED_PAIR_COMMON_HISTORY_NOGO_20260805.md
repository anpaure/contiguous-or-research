# No braid--residual common `d`-history exists even after nonmaximal thinning

**Date:** 2026-08-05  
**Method:** exact forced-pair/envelope inclusions on the braid and residual
event rails; no computation or search  
**Status:** unconditional for `m>=6` and the optimal deadline
`d=d(2m+1)`.  Arbitrary nonmaximal thinning of at most `d` consecutive
maximal source letters cannot create a literal common history between the
terminal braid and a residual component.  Thus the zero-position de Bruijn
fusion criterion fails before any Johnson/q1/upper guard is imposed.

## 1. Deadline range

Put

\[
                         n=2m+1,\qquad L=2m-4.
\]

The residual residence theorem gives

\[
                         d\le m-3\qquad(m\ge6).    \tag{1.1}
\]

Also `d>=3`.  Indeed, at `m=6`,

\[
                         2{13\choose6}+4<4^6,
\]

and both `W_m/4^m` and `4/4^m` decrease with `m`.  Hence
`2W_m+3<4^m-1=Lambda_m`, so deadline two is inadmissible for every
`m>=6`.

Put

\[
                         R=m-d\ge3.               \tag{1.2}
\]

## 2. Braid envelopes and forced pairs

At a braid source position choose the phase base `y`.  According to its
parity, the maximal letter and forced pair are

\[
 \begin{array}{c|c|c}
 &P^{\rm br}&F^{\rm br}\\ \hline
 \text{even}
 &[y+d+1,y+m]
 &\{y+d+1,y+m-1\}\\[1mm]
 \text{odd}
 &[y+d+1,y+m-1]\cup\{y+m+1\}
 &\{y+d+1,y+m+1\}.
 \end{array}                                      \tag{2.1}
\]

As consecutive source positions are traversed, `y` changes by `-1` in the
forward orientation and by `+1` in the reverse orientation.  The parity
alternates in either orientation.

## 3. Residual envelopes and forced pairs

Index a residual source position by edge `e` in the block of phase `t`,
`0<=e<L`.  Intersections of the preceding `d` q1 rows and the event formulas
give the following complete list.

### 3.1 The seam position `e=0`

\[
 P_0=[t+d+1,t+m+1]\setminus\{t+m-1\},
 \qquad
 F_0=\{t+d+1,t+m\}.                              \tag{3.1}
\]

This single position is checked separately in Lemma 4.1.

### 3.2 The `A`-type band

For

\[
                         1\le e\le m+d-1,
\]

put `x=t-e`.  Then

\[
 P_e=[x+d+1,x+m-1]\cup\{t+m+1\},
 \qquad
 F_e=\{x+d+1,x+m-1\}.                            \tag{3.2}
\]

This one formula includes the `B|A` crossing band, the `A` interior, the
`A|B` crossing band, and the first full `B` window.  In all four cases the
moving interval and the fixed `A` singleton are the displayed sets.

### 3.3 The terminal `B`-type band

For

\[
                         m+d\le e<L,
\]

put `x=t-e-2`.  Then

\[
 P_e=[x+d+1,x+m+1]\setminus\{t+m+2\},
 \qquad
 F_e=\{x+d+1,x+m+1\}.                            \tag{3.3}
\]

Empty index ranges are interpreted literally.

#### Derivation

The forced pair is always

\[
                         F_e=\{D_e,I_{e-d-1}\}.   \tag{3.4}
\]

Substitute the residual insertion/deletion schedule.  For `e<=m+d-1`, the
earlier insertion lies on the `A` branch (or the preceding block's terminal
`B` branch with the same residue), giving the endpoints in (3.2).  Later it
lies on the `B` branch, giving (3.3).  Intersecting the corresponding `d`
q1 rows yields the stated interval plus fixed singleton, or interval minus
fixed hole.  At `e=0`, the last `d` rows of the preceding block give (3.1).

## 4. Pointwise compatibility is parity-rigid

Align one braid position with one residual position.  On a standard band,
write

\[
                         y=x+\delta.              \tag{4.1}
\]

The nonmaximal common-history criterion requires

\[
 F^{\rm br}\cup F^{\rm res}
       \subseteq P^{\rm br}\cap P^{\rm res}.     \tag{4.2}
\]

### Lemma 4.1 (local compatibility table)

For the standard positions, together with the seam position:

1. an `A`-type residual position satisfies (4.2) iff the braid position is
   even and `delta=0`, except that the terminal `A` position
   `e=m+d-1` also admits an odd braid position with `delta=-2` when
   `R>=4`;
2. a `B`-type residual position satisfies (4.2) iff the braid position is
   odd and `delta=0`;
3. the seam position `e=0` is incompatible with either braid parity.

#### Proof

For an `A` position, its forced pair is the two endpoints of the moving
interval in (3.2).  An even braid interval can contain both only for
`delta in {-1,0}`; requiring the braid forced pair to lie back in (3.2)
eliminates `delta=-1`, leaving `delta=0`.  An odd braid envelope can contain
the residual endpoints only for `delta=0` or `-2`.  At `delta=-2` its forced
left endpoint lies outside the moving interval.  It can equal the fixed
residual singleton only at the terminal position `e=m+d-1`; there the
other containments hold when `R>=4`, giving the stated exception.  At
`delta=0` its forced far singleton
`x+m+1` lies outside the moving interval and equals the fixed residual
singleton only at the excluded seam phase `e=0`.  Thus no standard `A`
position has another odd compatibility.

For a `B` position, the residual forced endpoints span the full
`R+1`-point interval before its one hole.  An even braid interval has only
`R` points and cannot contain both endpoints.  At an odd braid position and
`delta=0`, the braid moving interval contains the left endpoint and its far
singleton is the right endpoint; conversely both braid forced coordinates
are residual interval endpoints.  The fixed residual hole is interior and
is neither endpoint.  Any nonzero shift loses one of these four endpoint
containments.

At `e=0`, the two residual forced points are the endpoints of an `R`-point
span.  An even braid interval contains both only at `delta=0`, where its
second forced coordinate is precisely the deleted residual hole `t+m-1`.
An odd braid can contain both only by using its far singleton, forcing
`delta=-1`; its forced left coordinate then lies one step before the
residual envelope.  Hence neither parity is compatible.  This proves the
table.  `square`

All interval comparisons use arcs of length at most `R+1<n/2`; hence there
is no second wraparound containment.

## 5. No length-`d` aligned block

Along one residual block the standard type word is

\[
                         A\cdots A\ B\cdots B,     \tag{5.1}
\]

with the sole wildcard `e=0` between the terminal `B` band of one block and
the initial `A` band of the next.

Within either standard band, `x` changes by one per source step.  At the
`A->B` transition it changes by three, whereas the braid base changes by
one.  Thus:

* two consecutive positions in one band would require the alternating
  braid parity to be simultaneously the same parity, impossible by
  Lemma 4.1.  The terminal odd-`A` exception does not help: within the
  `A` band `delta` is constant, while a neighbouring regular `A` position
  requires `delta=0` and the exception requires `delta=-2`;
* the standard `A->B` pair would require `delta=0` on both sides, but the
  jump changes `delta` by two, also impossible.  If the terminal `A`
  exception is used instead, the following braid parity is even whereas a
  `B` position requires odd parity.

No aligned block can meet `e=0` at all, by Lemma 4.1(3).

This proves the forward-forward orientation no-go.

Reversing a component reverses its cyclic list of pairs `(P_j,F_j)`; the
forced-pair theorem is invariant under this reindexing.  If both components
are reversed, the preceding parity/type proof is unchanged.  If exactly one
is reversed, the two phase bases move in opposite directions, so `delta`
changes by two at every pair of consecutive standard positions.  Two
consecutive regular positions cannot both have the required `delta=0`.
The only possible two-position exception is a regular `A` position next to
the terminal odd-`A` exception, using `delta=0,-2` in the appropriate order.
But every length at least three containing that pair also contains either a
second regular `A` adjacency or the following `B` position; the former has
two incompatible regular deltas and the latter has the wrong braid parity.
The seam position remains pointwise incompatible after reversal because
reversal merely reindexes the same pair `(P_0,F_0)`.

### Theorem 5.1 (forced-pair common-history no-go)

For `m>=6`, no choices of cyclic cuts, component orientations, or nonmaximal
antecedent letters produce a common literal length-`d` history between the
terminal braid and any residual component.

#### Proof

The optimal deadline satisfies `d>=3`.  Any aligned `d`-block is excluded by
the standard-band, transition, or wildcard argument above in each of the
four orientation choices.  By the exact common-history criterion, no other
nonmaximal thinning can evade the failed containments.  `square`

## 6. Consequence and guard scope

The bare order-`d` de Bruijn source circuits of the fixed terminal factor
cannot be fused at zero positional charge.  Since the obstruction occurs
before the cross screens are typed, adding Johnson adjacency, q1/upper
palette, residence, compiler, or common-cap guards cannot repair it.

Thus the rigid full-rotation endpoint has now exhausted both direct source
joins:

1. maximal antecedents have overlap zero and cost `d`;
2. arbitrary nonmaximal thinning has no common length-`d` de Bruijn vertex.

Any additive-constant completion must change the owner endpoint itself (for
example by reversing a sparse subset of rotation switches), or use a compound
boundary packet whose source state is not an antecedent of the two fixed
components separately.

## 7. Dependencies

The exact common-history criterion is

`MATH_THEOREM_RESIDENT_JOHNSON_FORCED_PAIRS_AND_COMMON_HISTORY_CRITERION_20260805.md`.

The braid and residual event/envelope formulas come from

* `MATH_THEOREM_PBBS_RIGID_ROTATION_BRAID_EXACT_BIRESIDENCE_20260805.md`,
* `MATH_THEOREM_PBBS_RIGID_ROTATION_RESIDUAL_EXACT_RESIDENCE_20260805.md`, and
* `MATH_THEOREM_PBBS_RIGID_ROTATION_MAXIMAL_ANTECEDENT_OVERLAP_NOGO_20260805.md`.
