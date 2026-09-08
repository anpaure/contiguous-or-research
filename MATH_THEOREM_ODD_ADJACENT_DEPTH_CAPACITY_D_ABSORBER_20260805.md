# Odd adjacent-depth lower absorption uses the new capacity-`D` middle-level bank

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** exact odd-dimensional analogue of the adjacent-depth residual
lower theorem.  Conditional on the residual whole-job configuration LP at
depth `D`, the residual lower ideal in `B_(2r-1)` has a target-once, named,
zero-defect collar realization one depth later.  The result does not prove
the separately priced endpoint/Ferrers bank and does not serialize the
collar forest into one upper-complete resident word.

## 1. The apparent missing maximum socket

Work in the odd Boolean lattice `B_(2r-1)`.  Put

\[
 C_s={2r-1\choose s},\qquad H_s=C_s-C_{s-1},\qquad
 W=C_{r-1}=C_r,
\tag{1.1}
\]

and let the old deadline depth be `D>=1`.  Write

\[
                         t=r-D.
\tag{1.2}
\]

Take a symmetric-chain collar on ranks `t,...,r-1`, with its rank-`r`
continuation regarded as the owner.  A chain born at rank `t+g` consumes
`D-g` lower-collar targets and hence gives one owner socket of capacity
`g`.  In odd dimension no symmetric chain is born at rank `r`: every chain
meets both middle ranks `r-1` and `r`.  Consequently the old exact
capacity multiplicities and tails are

\[
 M_g=H_{t+g}\quad(1\le g\le D-1),
\tag{1.3}
\]

\[
 K_q=\sum_{g=q}^{D-1}H_{t+g}
     =W-C_{t+q-1}\quad(1\le q\le D),
\tag{1.4}
\]

where in particular

\[
                         K_D=W-C_{r-1}=0.
\tag{1.5}
\]

Thus the old odd collar really has no capacity-`D` owner socket.  The one
endpoint-triangular socket of capacity `D` is a separate physical resource;
it is not an exponentially large exceptional bank.

Move one physical position and one deadline depth outward.  Put

\[
 b=t-1,\qquad D^+=D+1.
\tag{1.6}
\]

The new lower collar is `b,...,r-1`.  A chain born at rank `b+g` has
capacity `g`.  Again no chain is born at rank `r`, so now

\[
 M_g^+=H_{b+g}\quad(1\le g\le D),
\tag{1.7}
\]

\[
 K_q^+=\sum_{g=q}^{D}H_{b+g}
      =W-C_{b+q-1}\quad(1\le q\le D),
 \qquad K_{D+1}^+=0.
\tag{1.8}
\]

Therefore

\[
 \boxed{K_q^+-K_q=H_{t+q-1}\quad(1\le q\le D).}
\tag{1.9}
\]

At the last row this says

\[
 \boxed{K_D^+=H_{r-1}
 =C_{r-1}-C_{r-2}={2W\over r+1}.}
\tag{1.10}
\]

These are genuine occurrence counts.  Each of the `H_(r-1)` last-row
sockets is the start of a two-element symmetric chain

\[
                         B^{r-1}\subset T^r.
\tag{1.11}
\]

It consumes the one rank-`r-1` collar target `B` and leaves `D` of the
`D+1` lower cells free.  There is no capacity-`D+1` owner bank, but there is
an exponentially large capacity-`D` bank.

## 2. Why capacity `D` is exactly enough

At old depth `D`, take the canonical nonempty **residual** suffix jobs on
ranks `1,...,t-1`, after removing any separately priced endpoint/Ferrers
bank.  Let `FC_D^odd` denote feasibility of the exact whole-job
configuration LP against the owner tails (1.4).  Since `K_D=0`, every
configuration in the positive support has no piece of length `D`; the last
tail row is identically zero on the feasible support.  Hence an extreme
point leaves at most `D-1` whole jobs nonintegral.  The weaker bound `D`
will also be sufficient below.

Passing to depth `D+1` performs terminal deletion.  Every old rank-`t-1`
singleton job disappears and every other job loses its final cell.  Thus
the new residual ranks are

\[
                         1,\ldots,b-1=t-2.
\tag{2.1}
\]

Transport every uniquely selected ordinary configuration through terminal
deletion.  If `A_q` is its resulting piece tail, then

\[
 A_q\le K_q\quad(1\le q\le D),\qquad A_D=0.
\tag{2.2}
\]

Let `L_max<=t-2` be the largest exceptional descendant length.  Split each
exceptional descendant consecutively into pieces of length at most `D`.
Using the sharp `D-1` exceptional-job count requires at most

\[
 h_*=(D-1)\left\lceil{L_{\max}\over D}\right\rceil
\tag{2.3}
\]

pieces.  For notational compatibility one may use the safe bound

\[
 h=D\left\lceil{L_{\max}\over D}\right\rceil<r.
\tag{2.4}
\]

The crucial point is that terminal deletion makes length `D` sufficient.
The absent capacity-`D+1` bank is therefore irrelevant to exceptional
absorption.

## 3. Exact finite occurrence-faithful reserve theorem

For `1<=g<=D`, put

\[
 u_g=b+g,
 \qquad
 d_g={2r-b\choose g+1}.
\tag{3.1}
\]

Here `d_g` is the minimum number of rank-`u_g` containing sets available
to a fragment top of rank at most `b-1`.

### Theorem 3.1 (odd capacity-`D` adjacent absorber)

Assume `FC_D^odd`.  Let `Delta_1,...,Delta_D` be nonnegative integers such
that

\[
 h+\sum_{g=q}^{D}\Delta_g\le H_{t+q-1}
 \qquad(1\le q\le D),
\tag{3.2}
\]

and

\[
 {\Delta_g^2d_g\over C_{u_g}H_{u_g}}
 \ge A_0(2r-1)
 \qquad(1\le g\le D),
\tag{3.3}
\]

where `A_0` is the absolute constant in the MLD--Holder pointwise Hall
union bound.  Then the new residual lower system has a realization in
which:

1. every target of ranks `1,...,b-1` lies in exactly one literal
   inclusion-chain fragment;
2. every ordinary and exceptional fragment is attached to a distinct
   genuine odd-collar occurrence of sufficient capacity;
3. the named top of every fragment is contained in the named bottom of its
   assigned occurrence;
4. no residual target is exceptional or unmatched; and
5. at least `Delta_g` genuine capacity-`g` occurrences remain unused for
   each `g`.

#### Proof

Reserve `h` of the genuine capacity-`D` occurrences and reserve a further
`Delta_g` exact capacity-`g` occurrences.  At threshold `q`, the remaining
new-collar tail is

\[
 K_q^+-h-\sum_{g=q}^{D}\Delta_g.
\tag{3.4}
\]

Equations (1.9), (2.2), and (3.2) give

\[
 A_q\le K_q
 \le K_q^+-h-\sum_{g=q}^{D}\Delta_g
 \qquad(1\le q\le D).
\tag{3.5}
\]

The conjugate-tail matching criterion therefore injects every transported
ordinary piece into the remaining actual capacity multiset.  Put the at
most `h` exceptional pieces on distinct members of the reserved
capacity-`D` bank.  This proves the anonymous occurrence-faithful packing.

All configuration counts, terminal-deletion descendants, exceptional
fragmentations, and capacity types are deterministic before any Boolean
path geometry is exposed.  Uniformly refine each birth/configuration cohort
by these complete marked vectors and then expose the independent augmented
Boolean matchings only through rank `b-1`.  The cohort-stable
multinomial-Laplace theorem preserves MLD.

For a fixed start rank `u_g` and a fixed `u_g`-set, every marked fragment
top family is a union of MLD labels.  Generalized Holder combines the
one-rank binomial Laplace bounds.  Conditions (3.3), followed by the
pointwise-codegree matching theorem, attach all ordinary and exceptional
requests jointly to distinct containing rank-`u_g` starts.  At the top
rank `u_D=r-1`, complete the selected rank-`r-1` starts through any perfect
matching of the two equal middle levels to distinct rank-`r` owners.  The
other starts extend upward by the same augmented-matching/SCD construction.
Thus every selected bottom is an actual collar occurrence and items 1--5
follow.  `square`

### Corollary 3.2 (the reserve exists in the coefficient-one regime)

Suppose `D=Theta(sqrt(r))`.  For a sufficiently large absolute constant
`A`, take

\[
 \Delta_g=
 \left\lceil A\sqrt{rC_{u_g}H_{u_g}/d_g}\right\rceil.
\tag{3.6}
\]

Then (3.2)--(3.3) hold for all sufficiently large `r`.

#### Proof

Condition (3.3) is immediate after enlarging `A`.  Also `h<r`, whereas
uniformly on the odd central collar

\[
 H_s\ge H_{r-1}={2W\over r+1}\gg r.
\tag{3.7}
\]

Moreover

\[
 {d_{g+1}\over d_g}={r+D-g\over g+2},
\tag{3.8}
\]

so the reserve tails are geometrically dominated in the square-root
collar.  Here is the uniform estimate explicitly.  Put

\[
 a_g=r-u_g=D+1-g\qquad(1\le g\le D).
\tag{3.9}
\]

For `D=Theta(sqrt(r))`, the local central-binomial estimates give,
uniformly in `g`,

\[
 C_{u_g}=\Theta(W),\qquad
 H_{u_g}={2a_g\over r+a_g}C_{u_g}
         =\Theta(a_gW/r).
\tag{3.10}
\]

If the ceilings in (3.6) are temporarily suppressed, write the resulting
quantity as `X_g`.  Equations (3.6) and (3.10) give

\[
 X_g=\Theta\!\left(W\sqrt{a_g/d_g}\right).
\tag{3.11}
\]

For `g<D`, (3.8), together with the bounded adjacent ratios of `C_(u_g)`
and `H_(u_g)`, implies

\[
 {X_{g+1}\over X_g}=O(r^{-1/4}).
\tag{3.12}
\]

Thus every reserve tail is dominated by its first term.  Moreover

\[
 {a_{g+1}d_{g+1}\over a_gd_g}
 ={a_g-1\over a_g}{r-1+a_g\over D+3-a_g}>1
\tag{3.13}
\]

for all `g<D` and all sufficiently large `r`.  Since
`a_1d_1=Theta(Dr^2)`, (3.10)--(3.13) yield, uniformly in `q`,

\[
 {X_q\over H_{u_q}}
 =O\!\left({r\over\sqrt{a_qd_q}}\right)
 =O(r^{-1/4})=o(1).
\tag{3.14}
\]

Restoring ceilings adds at most `D=O(sqrt(r))` to any tail, whereas
`H_(r-1)=2W/(r+1)` is exponential in `r`.  Consequently

\[
 \sum_{g=q}^{D}\Delta_g=o(H_{u_q})
 =o(H_{t+q-1})
 \qquad(1\le q\le D).
\tag{3.15}
\]

For orientation, at the weakest first row these estimates read

\[
 \Delta_1=O(Wr^{-3/4}),
 \qquad H_t=\Theta(Wr^{-1/2}),
\tag{3.16}
\]

Together with the polynomial bound on `h`, this proves (3.2).  `square`

## 4. Exact no-go and exact positive conclusion

There is a sharp no-go hidden in the indices:

\[
 \boxed{\text{No odd SCD collar has a capacity-}(D+1)
 \text{ owner occurrence at the new depth.}}
\tag{4.1}
\]

Indeed every odd symmetric chain meets rank `r-1`, so every owner chain
uses at least one lower-collar cell.  The endpoint triangle contributes
only one capacity-`D+1` boundary socket.  Therefore the even proof cannot be
copied literally by demanding `h` maximum-new-depth sockets.

Theorem 3.1 is the exact repair: after terminal deletion the unresolved
pieces need capacity only `D`, and the newly exposed rank-`r-1` start bank
has multiplicity `H_(r-1)=2W/(r+1)`.

Let `D=d(2r-1)` and `B(2r-1)=W+D`.  The adjacent-depth physical length is

\[
                       W+D+1=B(2r-1)+1.
\tag{4.2}
\]

Consequently, for all sufficiently large odd dimensions, the conjunction
of

1. `FC_D^odd` for the canonical residual bank;
2. a literal realization of every separately priced endpoint/Ferrers
   target; and
3. a protected serialization of the named odd collar forest into one
   connected, owner-once, depth-`D+1`, upper-complete resident chronology

implies

\[
                         \nu(2r-1)\le B(2r-1)+1.
\tag{4.3}
\]

The residual lower absorber is therefore not an additional odd-parity
obstruction.  The remaining gaps are the all-price fractional
configuration inequality, the separately priced boundary bank, and the
common protected serializer.

## 5. Scope boundary

The new capacity-`D` occurrences are Boolean SCD occurrences.  They are not
automatically suffix occurrences in a separately selected middle-levels or
PBBS chronology.  In particular, the identity (1.10) proves actual collar
supply but not its simultaneous placement with owner connectivity,
coordinate residence, arbitrary-width upper witnesses, pins, or the common
cap.  Those requirements belong to the protected serialization theorem and
must not be inferred from the lower-side matching above.
