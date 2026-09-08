# Internal coatom block twists give the full coupled depthwise lattice

Date: 2026-08-01  
Lane: Thread D, enlarged endpoint-planted coatom catalogue  
Status: exact all-`d` packet derivative and saturated full-product catalogue
span.  The fresh-label two-packet isolator has an owner collision, while the
sharp four-column role-swap isolator has no proved compatible packing or
serial order.  Physical reachability and terminal compiler linkage remain
open.

## 0. Outcome

Use the current endpoint-planted coatom schedule with upper transitions

\[
                          \{0,2,4,6,8,10\}.                     \tag{0.1}
\]

The first `Iab` block has omission order

```text
p,f1,...,fd,f0,
```

where `p=f_(d+1)`.  Every other block has standard omission order
`f0,f1,...,fd,p`.

All named roles are disjoint.  The ambient coordinate ground is `Omega`
with `|Omega|=k`, and the fixed packet core has

\[
                              |K|=r-d-4,                         \tag{0.1a}
\]

so every owner has rank `r`.

For any `1<=s<=d-1`, swap the adjacent omissions `f_s,f_(s+1)` only in the
label-attached `Ica` block, in both packet phases.  The modified packet still
preserves the complete safe owner, q1-palette, interval-OR, endpoint,
topology and depth-`d` residence interface.

Its exact extra lower action relative to the common-order packet is sparse
and given in Theorem 2.1.  The decisive consequence is this.  Compare two
such twisted packets which differ only in the extreme label `p` versus a
fresh label `p'`, with opposite signs.  Every depth cancels except

\[
                               q=s+1,                            \tag{0.2}
\]

where the remaining action is one arbitrary Johnson square.  Varying `s`
over `1,...,d-1` and relabelling gives every square independently at every
depth `q=2,...,d`.  Therefore, in the stable range,

\[
 \boxed{
 \operatorname{span}_{\mathbb Z}(\text{common-order packets and
 internal one-block twists})
   =\bigoplus_{q=2}^d\ker_{\mathbb Z}\partial_{r-q}.}           \tag{0.3}
\]

Here `partial_j` is the coordinate-degree map on rank-`j` targets.  The
lattice is saturated.  Thus the new breaker does not merely escape one
quadratic reflection invariant: the enlarged **formal all-depth catalogue**
has no coupled linear or congruence obstruction beyond the separately fixed
point degrees at each depth.

This is not yet physical reachability.  The two packets used to isolate one
depth share unavoidable owner resources, including every common planted
upper screen.  They cannot be installed as two owner-disjoint simultaneous
slots.  A regenerative serial realization, a resource-disjoint triangular
circulation, or another representative-changing macro is still required.

There is a sharper four-column formal isolator which needs no fresh `p'`.
Take the twist correction `C_s=Delta^(s)-Delta^0` and subtract its global
coordinate relabelling by `(p b)`.  All rows except `q=s+1` cancel, leaving
one unit square.  This sharpens the full-product ambient range from
`k>=r+5` to `k>=r+4`; it does not remove the physical resource/ordering
gate.

## 1. The internal adjacent twist is safe

Let `X^0,Y^0` be the two endpoint-planted common-order packet phases.  In
the `Ica` block only, replace the standard omission order by

\[
 f_0,f_1,\ldots,f_{s-1},f_{s+1},f_s,f_{s+2},\ldots,f_d,p.      \tag{1.1}
\]

Call the resulting phases `X^s,Y^s`.

### Lemma 1.1 (safe internal reorder)

For every `d>=2`, `r>=d+4`, and `1<=s<=d-1`, the phases `X^s,Y^s` have:

1. the same distinct rank-`r` owner set and common endpoints;
2. simple Johnson-path topology;
3. equal immediate lower and upper palette multisets;
4. equal pointwise prefix/suffix OR signatures and complete interval-OR
   support;
5. the same clipped residence boundary state; and
6. no internal positive run shorter than `d+1`.

#### Proof

The first and last coatoms of the changed block are fixed.  Reordering all
coatoms of one active block therefore preserves its owner set, endpoints and
both exterior screen attachments.  Any two distinct filler coatoms are
Johnson adjacent.  A singleton block interval is one coatom, while every
longer block interval has the full filler union; hence the block's complete
prefix, suffix and internal OR support is order-independent.

The same reordered `Ica` block occurs once in each packet phase.  Its q1
intersection changes are therefore added identically on the two sides, and
all screen owners remain fixed.  Finally, one adjacent omission swap moves
each of the two affected filler zeros by one position.  Every affected
between-block positive run had canonical margin at least `d+2`, so its new
length is at least `d+1`; all other runs and the clipped boundary state are
unchanged. \(\square\)

## 2. Exact all-depth derivative

Let

\[
 R_q^{(s)}=
  \bigl({\cal L}_q(Y^s)-{\cal L}_q(X^s)\bigr)
 -\bigl({\cal L}_q(Y^0)-{\cal L}_q(X^0)\bigr).                 \tag{2.1}
\]

Put `x=f_s`, `y=f_(s+1)`, and define the Johnson square

\[
 Q_R(u,v;x,y)=
 e_{Rux}+e_{Rvy}-e_{Rvx}-e_{Ruy}.                              \tag{2.2}
\]

Juxtaposition denotes disjoint union.  Empty filler ranges are omitted.

### Theorem 2.1 (adjacent-twist window formula)

For `1<=q<=d`,

\[
\begin{aligned}
 R_q^{(s)}={}&
 \mathbf 1_{\{q=s+1\}}
 Q_{K\infty c\,\{f_{s+2},\ldots,f_d\}}
       (a,p;x,y)\\
 &+\mathbf 1_{\{q=d+1-s\}}
 Q_{K\infty c\,\{f_1,\ldots,f_{s-1}\}}
       (a,f_0;x,y)\\
 &+\sum_{h=1}^{s-1}\mathbf 1_{\{q=d+1-s+h\}}
 Q_{K\infty\,\{f_h,\ldots,f_{s-1}\}}
       (a,c;x,y).
                                                               \tag{2.3}
\end{aligned}
\]

If two displayed depths coincide, their square terms add.  At every other
depth the derivative is zero.

#### Proof

A window of length at most `d+1` crosses at most one screen.  Windows
strictly inside the changed `Ica` block occur with the same active label and
the same reordered filler word in both phases, so they cancel in (2.1).
Every window avoiding one of the two swapped coatoms is also unchanged.

It remains to classify windows which contain exactly one swapped coatom and
one exterior context.  Reading from the left/prefix boundary gives the
first row of (2.3): at width `q=s+1`, the exterior endpoint distinguishes
`a` from `p`, while the coatoms after the swapped pair contribute
`f_(s+2),...,f_d`.  Reading from the right/suffix boundary gives the second row: at
width `q=d+1-s`, the endpoint distinguishes `a` from `f0`, and the coatoms
before the pair contribute `f1,...,f_(s-1)`.

The remaining right/suffix contexts terminate successively after
`f_h,...,f_(s-1)`, for `1<=h<s`.  Their widths are
`d+1-s+h`, and the phase distinction is `a` versus `c`, giving the third
row.  These cases exhaust the one-sided windows; every two-sided or
screen-internal window is common.  Each case has the four signs in (2.2),
which proves (2.3). \(\square\)

For `s=1`, only the first two rows remain.  If `d>=3`, their pair-current
difference between the distinct depths `2` and `d` is exactly

\[
 [f_0f_1]-[f_0f_2]-[pf_1]+[pf_2],                            \tag{2.4}
\]

the previously frozen reflection breaker.  When `d=2`, both rows occur at
the single depth `q=2` and add there; there is no distinct reflected-depth
current, although the pure-depth isolation in Theorem 3.1 still applies.

Formula (2.3) is the authoritative derivative for this endpoint-planted
schedule.  It supersedes the same-schedule planted-action formulas in
`MATH_THEOREM_COATOM_ADJACENT_ORDER_REFLECTION_BREAKERS_20260801.md`;
that earlier note is not used as a dependency here.

## 3. Pure-depth isolation

Let `p'` be fresh.  Construct the same `s`-twisted packet after replacing
only the extreme filler label `p` by `p'`.  Denote its full signed action by
`Delta^(s,p')`.

### Theorem 3.1 (two-breaker pure square)

Assume `k>=r+5`, so the fresh role `p'` exists in addition to the complete
packet template.

The formal opposite difference

\[
                         \Delta^{(s,p)}-\Delta^{(s,p')}         \tag{3.1}
\]

vanishes at every depth except `q=s+1`.  At that depth it is

\[
 Q_{K\infty c\,\{f_{s+2},\ldots,f_d\}}
             (p',p;f_s,f_{s+1}).                               \tag{3.2}
\]

#### Proof

The common-order packet action depends only on the internal filler flag
`f1,...,fd`, so it is independent of `p`.  In (2.3), every term except the
first is also independent of `p`.  Subtracting the `p'` copy therefore
cancels all those terms.  In the first term,

\[
 Q_R(a,p;x,y)-Q_R(a,p';x,y)=Q_R(p',p;x,y),                     \tag{3.3}
\]

which proves (3.2). \(\square\)

There is a dual isolation using `f0` versus a fresh `f0'`, which isolates
the second row of (2.3) at depth `d+1-s`.

### Corollary 3.2 (sharp role-swap isolator)

No fresh role is needed if common-order packets are included.  Put
`C_s=Delta^(s)-Delta^0`, and let `tau=(p b)` act by global coordinate
relabelling on the whole packet template.  Then the four-column expression

\[
 C_s-\tau C_s
   =\Delta^{(s)}-\Delta^0-\tau\Delta^{(s)}+\tau\Delta^0       \tag{3.4}
\]

vanishes at every depth except `q=s+1`, where it equals

\[
 Q_{K\infty c\,\{f_{s+2},\ldots,f_d\}}
             (b,p;f_s,f_{s+1}).                                \tag{3.5}
\]

#### Proof

In (2.3), the role `b` occurs in no row and `p` occurs only in the first
row, at depth `s+1`.  Thus every other row is fixed by `tau`.  On the first
row,

\[
 Q_R(a,p;x,y)-Q_R(a,b;x,y)=Q_R(b,p;x,y),                       \tag{3.6}
\]

which proves the claim.  Each term of (3.4) is a full relabelled canonical
or twisted packet action, so this is an identity in the stated catalogue
lattice. \(\square\)

## 4. Saturated full-product span

For a coordinate ground `Omega` and rank `j`, let

\[
 \partial_j:\mathbb Z^{\binom{\Omega}{j}}\to\mathbb Z^\Omega,
 \qquad e_S\longmapsto\sum_{x\in S}e_x.                       \tag{4.1}
\]

### Lemma 4.0 (integral Johnson-square generation)

If `2<=j<=|Omega|-2`, then `ker_Z(partial_j)` is generated over the
integers by the unit squares

\[
 e_{Rux}+e_{Rvy}-e_{Rvx}-e_{Ruy},
 \qquad |R|=j-2,                                               \tag{4.1a}
\]

with `R,u,v,x,y` pairwise disjoint in the displayed roles.

#### Proof

Induct on `n=|Omega|`.  Fix `w in Omega` and restrict a kernel vector `z`
to the `j`-sets containing `w`; after deleting `w` this is an integer
vector `z_w` on the `(j-1)`-sets of `Omega-{w}`.  Its coefficient sum is
zero, because the `w`-coordinate of `partial_j z` is zero.

The Johnson graph on these `(j-1)`-sets is connected.  If two adjacent
vertices are `R+x` and `R+y`, choose
`v notin R union {w,x,y}`; this is possible because `j<=n-2`.  The square

\[
 e_{Rwx}+e_{Rvy}-e_{Rvx}-e_{Rwy}                              \tag{4.1b}
\]

restricts on the `w`-containing sets to exactly
`e_(R+x)-e_(R+y)`.  Integer edge differences of a connected graph generate
the complete zero-sum lattice, so an integral sum of squares kills `z_w`.
The residual kernel vector is supported on `Omega-{w}`.  Repeat until the
ground has size `j+1`; there the `j`-set incidence matrix is the complement
matrix `J-I`, whose determinant has absolute value `j`, so its integer
kernel is zero.  This proves the claim without division and hence with
coefficient-one integral generators. \(\square\)

### Theorem 4.1 (complete coupled catalogue lattice)

Assume

\[
                 r\ge d+4,qquad k\ge r+4,                    \tag{4.2}
\]

and every target rank `r-q`, `2<=q<=d`, lies between `2` and `k-2`.
Let `L_twist` be the integer span of all relabelled common-order packets and
all relabelled internal one-block twists (1.1), with both orientations.
Then

\[
 \boxed{
 L_{twist}=\bigoplus_{q=2}^d\ker_{\mathbb Z}\partial_{r-q}.}   \tag{4.3}
\]

In particular `L_twist` is saturated.

With the sharp ambient range, the common-order columns occur in the
four-column isolator (3.4).  If `k>=r+5`, the two-twist fresh-label isolator
(3.2) shows that they are redundant for the span.

#### Proof

Every common-order action is a sum of rankwise rectangles.  Formula (2.3)
shows the same for every twist derivative.  Hence every packet action has
zero coordinate degree at each depth, proving the inclusion from left to
right in (4.3).

Fix `q` and put `s=q-1`.  Corollary 3.2 gives a pure depth-`q` Johnson square.
Its common core has size `r-q-2`.  Under (4.2), any prescribed core and four
outside square labels can be assigned respectively to

```text
K + infinity + c + {f_(s+2),...,f_d}
and
b,p,f_s,f_(s+1),
```

while the `s+3` unused roles are filled by
`f0,f1,...,f_(s-1),a,e,delta`.  Thus every rank-`(r-q)` Johnson square is
a relabelled instance of (3.5).  The complete template uses exactly `r+4`
distinct roles.

Lemma 4.0 says that the Johnson squares generate
`ker_Z(partial_(r-q))` integrally.  Since (3.5)
has zero action at all other depths, these generators are independent across
`q=2,...,d`.  This proves the reverse inclusion and saturation. \(\square\)

The theorem closes the formal coupled-span problem completely.  The
common-order reflected-pair fibre was an artefact of the common block order,
not an invariant of the safe enlarged catalogue.

## 5. Exact physical obstruction to the isolator

Theorem 3.1 is a signed catalogue difference, not a two-slot construction.
The `p` and `p'` packets have identical active roles, internal fillers and
screen schedule.  Every planted upper screen omits both extreme filler
roles, so its owner is identical in the two packets.  Coatom owners which
omit the changed extreme also collide.  Therefore the two old packet words
cannot occur as owner-disjoint simultaneous slots in one exact owner deck.

Equivalently, if `A` is the full action matrix of a finite prepared atlas,
with the two packet columns indexed by `u,v`, then the coefficient vector
`e_u-e_v` lies in `ker(A_rest)` after `rest` removes the isolated depth,
and `A_J(e_u-e_v)` is the square (3.2) on the retained depth `J`.  But the
two columns violate one or more stable-set rows of the owner/collar conflict
graph `K_conf`,

\[
                              x_u+x_v\le1.                       \tag{5.1}
\]

This is the exact surviving distinction:

```text
formal full product: proved;
resource-disjoint two-slot lift: false for the canonical isolator;
regenerative serial or triangular lift: open.
```

The sharp role-swap isolator (3.4) uses four signed columns from two
labellings.  Within each labelling, the twisted and common-order phases have
the same owner set, so there is no simultaneous owner-disjoint four-slot
lift; no serial lift is proved.  Its better ambient corank does not weaken
this physical gate.

A positive physical theorem may take either of two forms.

1. A safe route transforms the first packet slot into a state containing the
   second and then permits the inverse route to be replayed without undoing
   the square action.
2. A three- or four-packet resource-disjoint circulation cancels the shared
   owners while retaining the pure depth square, analogous to the existing
   zero-action triangle/twisted-cube absorbers.

Neither follows from (4.3).

## 6. Exact compiler linkage after a physical lift

Suppose a physical realization `T->T'` of one enlarged-catalogue action has
been obtained and identify the target and cell shores at its two endpoints.
Fix a **carryable guard schema** `rho`: one endpoint-relative
boundary/pin/trace policy which instantiates a co-selectable incidence graph
`H_rho(U)` on both endpoint carriers.  Write

\[
 \delta_\rho(U)=|L|-\nu(H_\rho(U)).
\]

Let `M` be a maximum matching of `H_rho(T)`, delete its `ell` edges absent
from `H_rho(T')`, and let `alpha` be the maximum number of pairwise
vertex-disjoint augmenting paths from the surviving matching in
`H_rho(T')`.  Then

\[
             \delta_\rho(T')-\delta_\rho(T)=\ell-\alpha.       \tag{6.1}
\]

Thus the twist improves this **fixed-schema deficiency** exactly when
`alpha>ell`.  This is not automatically an improvement of the global
terminal deletion number, which optimizes over complete cap states and may
change schema.  Full formal span (4.3) removes every linear coupled-depth
obstruction to choosing a desired signed occurrence action, but it neither
supplies the physical lift nor makes the maximal common-cap equations
linear.  A complete terminal proof still needs a co-selectable guarded
return bank or the exact nonlinear cap-conflict system.

## 7. Audit

The replay

```text
scratch/audit_threadD_coatom_internal_twist_full_product_span_20260801.py
scratch/threadD_coatom_internal_twist_full_product_span_20260801.audit.json
```

checks every internal adjacent twist for `2<=d<=10`, including all safe
packet rows and the exact formula (2.3), verifies pure-depth cancellation
both by the fresh-role two-column difference and by the sharp `(p b)`
four-column commutator, replays the coefficient-one integral peeling
schema, and checks the expected Johnson-square kernel ranks on small
grounds.  It does not claim a physical packing or serial lift.

Dependencies:

* `MATH_THEOREM_COATOM_SINGLE_BLOCK_ORDER_REFLECTION_BREAKER_20260801.md`;
* `MATH_THEOREM_COATOM_FLAG_SIGNATURE_AND_PLUCKER_LATTICE_20260801.md`;
* `MATH_THEOREM_COATOM_ENDPOINT_PLANTING_FIXED_SLOT_HALL_CORRECTION_20260801.md`;
* `MATH_THEOREM_INDEPENDENT_COATOM_TWO_CHAIN_PROVIDER_SWITCH_AND_SERIAL_LAMBDA_GATE_20260801.md`; and
* `MATH_THEOREM_GUARDED_CONVEX_LAMINAR_COMMON_CAP_COMPILER_20260731.md`.
