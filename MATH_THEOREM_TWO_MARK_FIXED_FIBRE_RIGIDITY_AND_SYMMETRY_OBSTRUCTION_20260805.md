# Two-mark FIFO refinement: fixed-fibre rigidity and the exact symmetry obstruction

**Date:** 2026-08-05  
**Method:** exact synchronized-chain algebra, group averaging, and a
two-owner diagonal coupling; no computation or search  
**Status:** unconditional obstruction and exact reduction.  The
rank-cycle/vertex-splice kernel of a fresh FIFO endpoint fibre cannot supply
the extra `(r-1)^{-m}` factor in the pre-reserved two-mark cylinder.  At a
fixed endpoint fibre, `(T_2,b_2)` determines `b_1` uniquely.  Full coordinate
symmetry gives the correct **one-point** conditional marginal only; even
exact one-point uniformity can miss the required two-point cylinder by a
factor `r-1`.  Thus (C2) requires a genuinely endpoint-changing, jointly
spread refinement (or an external absorber), not a use of the existing
fixed-fibre chain connectivity theorem.

## 1. The marked level-two state inside one fresh FIFO fibre

Fix pairwise disjoint sets

\[
 C,A,X,B\subseteq[k],\qquad |A|=|X|=|B|=d,
 \qquad |C|=r-2d.
 \tag{1.1}
\]

The harmless change `|B|=d-1` in the punctured duplicate lift leaves all
formulas below through level two unchanged.  Choose orderings

\[
 X=(x_1,\ldots,x_d),\qquad B=(b_1,\ldots,b_d).
 \tag{1.2}
\]

As in the synchronized-chain normal form, the level-two owner is

\[
 T_2=C\cup A\cup\{x_3,\ldots,x_d\}\cup\{b_1,b_2\}.
 \tag{1.3}
\]

The ordered pair `(b_2,b_1)` is exactly the two-mark datum used in
`MATH_THEOREM_PRE_RESERVED_KY_OPTION_TAIL_AND_TWO_MARK_CYLINDER_GATE_20260805.md`.
Call

\[
                 \mathfrak F=(C,A,X,B)                    \tag{1.4}
\]

the unordered endpoint fibre.  Its maximal paths vary the orders in (1.2),
but they do not change any of the four sets in (1.4).

### Theorem 1.1 (fixed-fibre two-mark rigidity)

For every maximal path in `mathfrak F`,

\[
 \boxed{\quad
 b_1\text{ is the unique element of }
       (T_2\cap B)\setminus\{b_2\}.\quad}                 \tag{1.5}
\]

Consequently, among all paths in one endpoint fibre which realize a fixed
one-mark state `(T_2,b_2)`, the second mark `b_1` is constant.

#### Proof

Disjointness in (1.1) and (1.3) gives

\[
                         T_2\cap B=\{b_1,b_2\}.            \tag{1.6}
\]

Removing the specified element `b_2` leaves the singleton `{b_1}`.  The
argument uses only the endpoint sets, not either ordering.  It therefore
holds simultaneously for every maximal path in the fibre.  \(\square\)

There is a stronger support interpretation.  To change `b_1` while fixing
`(T_2,b_2)`, one must change which coordinates belong to the endpoint role
set `B`: the new value must enter `B`, and the old value must leave it.
Thus every such refinement crosses endpoint fibres.

## 2. The synchronized-chain kernel cannot perform that refinement

The exact chain-fibre connectivity theorem has two generators:

1. vertex splices between selected maximal paths; and
2. rank-cycle switches in one synchronized Boolean graph
   `Z_d(X,B)`.

Both preserve the endpoint data `(C,A,X,B)`.

### Corollary 2.1 (no fixed-fibre mark symmetrization)

Every sequence of vertex splices and rank-cycle switches preserves the map

\[
       (\mathfrak F,T_2,b_2)\longmapsto b_1.               \tag{2.1}
\]

In particular, these switches cannot turn a conditional point mass in
`b_1` into the uniform law on `T_2-{b_2}`.

#### Proof

Every intermediate path remains in the same endpoint fibre, while Theorem
1.1 makes (2.1) a deterministic function throughout that fibre.  \(\square\)

At owner load one the obstruction is stronger still.  All maximal paths in
one endpoint fibre share their first and last owner.  Hence an
owner-bijective chronology contains at most one of them.  A nontrivial
rank-cycle switch or vertex splice needs at least two selected paths in the
fibre, so no nontrivial fixed-fibre generator is available at all.

This also identifies the exact limitation of fractional use of the chain
kernel.  It may redistribute path mass **inside** a fixed endpoint fibre,
but (1.5) says that the conditional mark fibre above any fixed
`(T_2,b_2)` still has support one.  Mixing across endpoint fibres is a new
rounding problem not contained in the chain-kernel theorem.

## 3. What full coordinate symmetry does give

Let `mu` be any distribution on feasible marked constructions which is
invariant under the full coordinate group `Sym([k])`.  For a one-mark state

\[
                         s=(T,b_2),\qquad b_2\in T,         \tag{3.1}
\]

write `Y_s` for the event that `s` is selected, and write `X_(s,z)` for the
event that it is selected with second mark `b_1=z`.

### Theorem 3.1 (exact one-point orbit symmetrization)

If `Pr(Y_s)>0`, then for every `z in T-{b_2}`,

\[
 \boxed{
  \Pr(X_{(s,z)}=1\mid Y_s=1)={1\over r-1}.}
 \tag{3.2}
\]

#### Proof

The stabilizer of `(T,b_2)` in `Sym([k])` acts transitively on
`T-{b_2}`.  Invariance of `mu` therefore makes all conditional probabilities
in (3.2) equal.  Exactly one second mark is present whenever `Y_s=1`, so
their sum is one.  \(\square\)

This theorem is useful but has two exact scope restrictions.

* The two role banks `(B_0,B_1)` are fixed in condition (C2).  Conditioning
  on a realized bank pair replaces the full stabilizer above by the
  stabilizer of `(T,b_2,B_0,B_1)`, which need not act transitively on
  `T-{b_2}` and may be trivial.
* Even without bank conditioning, one-point uniformity does not imply the
  joint cylinder needed for `m=O(d)`.

The second failure is sharp already at `m=2`.

## 4. A sharp two-owner diagonal obstruction

Let `A` be an `(r-1)`-set and take distinct `x,y` outside `A`.  Put

\[
 T_x=A\cup\{x\},\quad b_2^x=x,
 \qquad
 T_y=A\cup\{y\},\quad b_2^y=y.                              \tag{4.1}
\]

These are distinct compatible one-mark owners, and both second-mark
candidate sets are the same set `A`.  Choose one random `Z`, uniformly from
`A`, and put

\[
                         b_1^x=b_1^y=Z.                     \tag{4.2}
\]

### Proposition 4.1 (marginal symmetry misses the cylinder by `r-1`)

Each of `b_1^x,b_1^y` is exactly uniform on its `(r-1)` candidates, and the
coupling is invariant under the full stabilizer of the configuration
(4.1).  Nevertheless, for every `z in A`,

\[
 \Pr(b_1^x=z,b_1^y=z)={1\over r-1}
       =(r-1){1\over(r-1)^2}.                               \tag{4.3}
\]

Thus exact conditional one-point symmetry can violate the desired
two-mark product cylinder by the full factor `r-1`.

#### Proof

Uniformity and invariance follow from the uniform choice of `Z`.  Equation
(4.3) is immediate.  \(\square\)

The pair (4.1) is precisely why global random relabelling is not a substitute
for independent endpoint-role refinement: the two stabilizer orbits share
one latent mark.  Repeating the same construction over a family of owners
with a common candidate core gives analogous failures at every higher
cylinder order.

## 5. Exact disintegration of the remaining requirement

Let `mathcal F_s` be the endpoint fibres which can realize a fixed one-mark
state `s=(T,b_2)`.  Theorem 1.1 defines a deterministic map

\[
 \phi_s:\mathcal F_s\longrightarrow T-\{b_2\},
 \qquad \phi_s(\mathfrak F)=b_1.                            \tag{5.1}
\]

For any physical construction law, let `F_s` be its random endpoint fibre
conditional on selecting `s`.  Then exactly

\[
 \Pr(b_1=z\mid s,B_0,B_1)
   =\Pr(\phi_s(F_s)=z\mid s,B_0,B_1).                       \tag{5.2}
\]

For distinct one-mark states `s_1,...,s_m`, the factor needed to upgrade
the proved one-mark cylinder to (C2) is therefore the endpoint-fibre kernel
bound

\[
 \boxed{
 \Pr\bigl(\phi_{s_i}(F_{s_i})=z_i\ (1\le i\le m)
       \mid s_1,\ldots,s_m\text{ selected},B_0,B_1\bigr)
       \le(r-1)^{-m}.}                                     \tag{5.3}
\]

Only orders `m=O(d)` are required.  If (5.3) holds, multiplying it by the
one-mark cylinder at scale

\[
                         {(1+o(1))H\over Wr}               \tag{5.4}
\]

gives (C2) at scale

\[
                         {(1+o(1))H\over W(r)_2}.           \tag{5.5}
\]

Conversely, the diagonal construction in Section 4 shows that neither
one-mark spread nor all one-point instances of (5.2) imply (5.3).

## 6. Proof-safe conclusion

The proposed fixed-fibre route is closed negatively:

\[
 \boxed{
 \text{chain-fibre connectivity cannot symmetrize the second mark at fixed
 `(T,b_2)`, because that mark is an endpoint-fibre invariant.}}
 \tag{6.1}
\]

The correct positive target is an **endpoint-changing mark-spread lemma**.
It must jointly randomize the role sets `B` (or use an external compound
absorber which exchanges endpoint roles), remain valid after conditioning on
the pre-reserved owner banks, and satisfy the order-`O(d)` kernel bound
(5.3).  An unconditioned group average, a one-point uniform refinement, or
the existing rank-cycle/vertex-splice connectivity theorem is insufficient.

This result does not disprove the pre-reserved two-mark spread SDR.  It
proves that the specific proposed source of its missing `(r-1)^{-m}` factor
has the wrong invariant and identifies exactly which additional
endpoint-changing randomness must be constructed.
