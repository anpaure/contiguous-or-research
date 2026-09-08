# Octahedral \(H\)-collars: a bounded-overlap capacity obstruction and the exact conjugated-router boundary

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

There is an exact signed-depth-one-invisible three-edge trade on the
octahedron \(J(4,2)\), and the already proved two-type rail construction
lifts one copy of it to a literal signed-\(H\)-invisible trade.  This note
settles the packing scale of that certified local atom.

Let \(W\) be the number of middle owners and let a family of
context-separated matching trades have **collar participation at most
\(\kappa\)**, meaning that every owner lies in the full two-sided
\(H\)-collar of at most \(\kappa\) trades.  If the \(i\)-th trade replaces
\(a_i\) matching edges and has joining rank \(r_i\), then

\[
 \boxed{
   \sum_i r_i\le {\kappa W\over 2H}.}
 \tag{0.1}
\]

For the three-edge octahedral atom this sharpens to

\[
 \boxed{
   \sum_i r_i\le {\kappa W\over 3H}.}
 \tag{0.2}
\]

The two-colour product-SCD diagonal cover has

\[
 p=\left({2\over\sqrt\pi}+o(1)\right){W\over\sqrt m}
 \tag{0.3}
\]

components.  Reducing this to \(o(W/H)\) components therefore requires

\[
 \kappa\ge
 \left({4\over\sqrt\pi}-o(1)\right){H\over\sqrt m}
 \tag{0.4}
\]

for arbitrary-arity context-separated trades, and

\[
 \boxed{
 \kappa\ge
 \left({6\over\sqrt\pi}-o(1)\right){H\over\sqrt m}}
 \tag{0.5}
\]

for octahedral trades.  In particular, when
\(H/\sqrt m\to\infty\), no owner-disjoint or bounded-overlap packing of
the certified local atoms can have the required joining rank.

Thus a surviving octahedral construction must reuse the same owner
collars an unbounded number of times.  It is necessarily a close-packed
multi-seam construction, and independent port signatures are then no
longer sufficient.

For that escape there is an exact replacement for the independent-port
criterion.  Encode the actual before/after successors by their
length-\(H\) safe-path columns.  The aggregate switch is invisible through
depth \(H\) exactly when its signed column vector lies simultaneously in

\[
 \ker A\cap\ker M\cap\ker D\cap
 \bigcap_{q\le H,\,\epsilon\in\{-,+\}}\ker S_q^\epsilon.
 \tag{0.6}
\]

Equivalently, a reduced close-packed routing grammar makes *every* closed
route invisible precisely when each meet/join target cochain is a
coboundary on the full two-queue state graph.  This is the exact
multi-seam identity; it is not implied by the one-seam octahedral
identity.

Finally, a genuinely conjugated crossing \(S\mapsto RSR^{-1}\) does exist
at the abstract cycle-label level.  An exact normalizer criterion is
proved below.  If the exit is required to use the original switch
direction, one two-direction plane retains exactly ten of the sixteen
pair-bit states.  If the exit direction is allowed to be the conjugated
direction, all sixteen plane states close: the other six leave in
direction \(\delta+\gamma\).  For overlapping coordinate transpositions
this is again a physical two-coordinate direction.
However, any such construction confined to one split-pair packet is
trace-invisible only when its final edge set is unchanged.  Hence its
joining rank is zero.  The conjugated-router escape must be cross-packet
and must satisfy the coboundary condition (0.6); no existing braid theorem
proves this last statement.

## 1. Full \(H\)-collars cost \(2aH\) owners

Consider a matching trade

\[
                       M_0\longrightarrow M_1
 \tag{1.1}
\]

on the same \(2a\) exposed ports, where both matchings have \(a\) edges.
Assume that every port has a retained outward collar of \(H-1\) edges and
that these collars are context-separated: collars issuing from distinct
ports do not meet before depth \(H\).  This is exactly the local regime in
which the independent seam signatures

\[
 \Sigma_q^\pm(v,w),\qquad 1\le q\le H,
 \tag{1.2}
\]

give a sufficient switch test.

### Lemma 1.1 (collar support)

One such \(a\)-edge trade occupies at least

\[
                            2aH
 \tag{1.3}
\]

distinct owner vertices in its complete port collars.

#### Proof

Each of the \(2a\) ports contributes itself and the next \(H-1\) retained
vertices on its outward ray.  Opposite rays from one deleted edge are
disjoint.  Context separation makes rays belonging to different cut
edges disjoint through the displayed depth.  Hence there are at least
\(2aH\) distinct owners.  \(\square\)

The explicit two-type lift of the octahedral trade attains this count:
it has six ports and six rails of \(H-1\) further vertices, hence exactly
\(6H\) owner positions before any ambient completion.

### Lemma 1.2 (joining rank)

The component decrease caused by an \(a\)-edge matching trade is at most

\[
                              a-1.
 \tag{1.4}
\]

#### Proof

Only components containing one of the \(a\) deleted edges can be joined.
There are at most \(a\) such old components.  Their replacement has at
least one component.  Thus their component count can fall by at most
\(a-1\).  \(\square\)

### Theorem 1.3 (bounded-overlap collar capacity)

Let \({\cal T}\) be a family of full-collar, context-separated trades and
suppose every owner belongs to the collar support of at most \(\kappa\)
members of \({\cal T}\).  Then (0.1) holds.  If every member is a
three-edge octahedral trade, then (0.2) holds.

#### Proof

Double count owner--trade collar incidences.  Lemma 1.1 gives

\[
                 \sum_{i\in{\cal T}}2a_iH\le\kappa W.
 \tag{1.5}
\]

By Lemma 1.2,

\[
 \sum_i r_i\le\sum_i(a_i-1)<\sum_i a_i
              \le {\kappa W\over2H},
 \tag{1.6}
\]

which proves (0.1).  For octahedral trades, \(a_i=3\) and \(r_i\le2\).
If their number is \(t\), then \(6Ht\le\kappa W\), so

\[
                  \sum_i r_i\le2t\le{\kappa W\over3H}.
 \tag{1.7}
\]

This is (0.2).  \(\square\)

### Corollary 1.4 (the isolated-octahedron lane is too small)

Suppose \(H/\sqrt m\to\infty\).  No bounded-overlap family of certified
two-rail octahedral trades reduces the product-SCD component count from
(0.3) to \(o(W/H)\).

#### Proof

The required joining rank is

\[
 p-o(W/H)=\left({2\over\sqrt\pi}+o(1)\right){W\over\sqrt m}.
 \tag{1.8}
\]

Combine this with (0.1), or with (0.2) in the octahedral case.  This gives
(0.4) and (0.5).  Both lower bounds tend to infinity.  \(\square\)

This is a capacity obstruction, not a nonexistence theorem for sequential
reuse.  It says exactly what sequential reuse must accomplish: average
collar participation must grow at least on the scale
\(H/\sqrt m\).  At that density, many protected windows meet several
active seams, so the one-seam context criterion cannot be applied
independently.

## 2. Exact close-packed condition in the two-queue state space

Let \(\Gamma_H\) be the set of safe owner paths

\[
                 \gamma=(X_0,X_1,\ldots,X_H).
 \tag{2.1}
\]

Recall the matrices

* \(A\): root-owner incidence;
* \(M\): prefix-minus-suffix incidence on length-\((H-1)\) memory states;
* \(D\): first-deletion incidence, recording the common run vector;
* \(S_q^-\): the lower meet target of the first \(q\) edges;
* \(S_q^+\): the upper join target of the first \(q\) edges.

The memory state is equivalently the ordered pair of cooldown queues of
the last \(H-1\) deleted and inserted labels.  Thus it retains exactly the
information needed to decide every window crossing a later seam.

Let \(z,z'\in\{0,1\}^{\Gamma_H}\) encode two integral safe successors and
put

\[
                              \delta=z'-z.
 \tag{2.2}
\]

### Theorem 2.1 (multi-seam meet/join kernel)

The two successors have the same owner roots, the same cyclic
\(H\)-chronology, the same coordinate run vector, and identical complete
signed trace multisets through depth \(H\) if and only if

\[
 \boxed{
 A\delta=M\delta=D\delta=0,
 \qquad
 S_q^-\delta=S_q^+\delta=0\quad(1\le q\le H).}
 \tag{2.3}
\]

If every protected window is also required to be literal, both \(z\) and
\(z'\) must be supported on safe columns, as assumed above.

#### Proof

\(A\delta=0\) is equality of the root-owner ledgers.  \(M\delta=0\) is
equality of prefix and suffix flow at every memory state, hence equality
of the cyclic \(H\)-chronology.  \(D\delta=0\) is equality of the common
coordinate run vector.  (It is redundant once the complete signed
depth-one histogram and the root ledger are both fixed, but it is useful
to retain explicitly.)  The rows of \(S_q^\pm\) are precisely the
indicator rows of the meet/join target carried by a length-\(q\) window.
Therefore \(S_q^\pm\delta=0\) is exactly equality of the corresponding
target multiset.  These conditions are separately necessary and jointly
sufficient.  \(\square\)

The importance of (2.3) is that it remains valid when a protected window
meets arbitrarily many seams.  No sum of fixed one-seam collar formulas is
being used: \(z'\) records the actual final windows.

### Theorem 2.2 (telescoping and the cocycle criterion)

Let

\[
                    z_0,z_1,\ldots,z_t
 \tag{2.4}
\]

be a sequence of exact \(H\)-safe successors and put
\(\delta_i=z_i-z_{i-1}\).  Then

\[
 S_q^\pm(z_t-z_0)=\sum_{i=1}^tS_q^\pm\delta_i.
 \tag{2.5}
\]

Now let \({\cal G}\) be a reduced reversible directed grammar of
close-packed switch states (every trade arc is present with its reverse).
An arc \(e:x\to y\) must include the full two-queue context, so
that its target derivative

\[
 \omega_{q,T}^\pm(e)
  =\#\{\hbox{new \(q\)-windows with target \(T\)}\}
   -\#\{\hbox{old \(q\)-windows with target \(T\)}\}
 \tag{2.6}
\]

is well defined.  Every integer state circulation in \({\cal G}\)
(equivalently, every closed route, because the grammar is reversible) is
trace-invisible through depth \(H\) if and only if, for every
\((q,\pm,T)\), there is a potential
\(F_{q,T}^\pm:V({\cal G})\to\mathbb Z\) such that

\[
 \boxed{
 \omega_{q,T}^\pm(e)
   =F_{q,T}^\pm(y)-F_{q,T}^\pm(x).}
 \tag{2.7}
\]

#### Proof

Equation (2.5) is linear telescoping.  For the second statement, a
cochain on a finite reversible directed graph is a coboundary exactly
when it annihilates the integer cycle space.  Applying this
coordinatewise to all protected meet/join targets proves the
equivalence.  \(\square\)

There is an equivalent matrix formulation useful for a proposed switch
library.  Let \(B\) denote its augmented constraint matrix: the
state-boundary rows together with every root/run row not already built
into the arc catalogue.  If \(C\) is the matrix of all protected target
derivatives, then every admissible state circulation is invisible exactly
when

\[
                       \ker B\subseteq\ker C,
 \tag{2.8}
\]

or, over \(\mathbb Q\), exactly when

\[
                       \operatorname{row}(C)
                       \subseteq\operatorname{row}(B).
 \tag{2.9}
\]

This is the promised meet/join cocycle identity.  A local octahedral
identity proves (2.6) is zero for one isolated arc with specially matched
collars.  It does not prove (2.7) after the collars overlap.  Conversely,
a genuine close-packed proof may allow large nonzero local derivatives as
long as (2.7) makes them telescope.

### Corollary 2.3 (exact three-stage octahedral telescope)

Suppose three serial octahedral stages act on the same transported
three-port shore by one 3-cycle \(R\), and let

\[
                         \omega_0,\omega_1,\omega_2
 \tag{2.10}
\]

be their complete vector-valued meet/join derivatives, computed in the
actual successive two-queue states.  The three stages restore the port
labels because \(R^3=1\).  They preserve every protected trace through
depth \(H\) if and only if

\[
 \boxed{
                         \omega_0+\omega_1+\omega_2=0.}
 \tag{2.11}
\]

Equivalently, there are potentials on the three phase states with

\[
 \omega_j=F(j+1)-F(j)\qquad(j\in\mathbb Z_3).
 \tag{2.12}
\]

#### Proof

Port restoration is \(R^3=1\).  Equation (2.5) makes (2.11) necessary
and sufficient for trace restoration.  On a directed 3-cycle, (2.11) is
equivalent to (2.12): take
\(F(0)=0,F(1)=\omega_0,F(2)=\omega_0+\omega_1\).  \(\square\)

The qualification “actual successive two-queue states” is essential.
Computing all three \(\omega_j\)'s against one frozen exterior collar
misses windows crossing two stages and does not prove (2.11).

## 3. Exact conjugation of two cycle-label switches

Let \(V\) be a binary label space and let \(\delta,\gamma\in V\) be
linearly independent.  Put

\[
 S(x)=x+\epsilon(x)\delta,\qquad
 \epsilon(x)=\epsilon(x+\delta),
 \tag{3.1}
\]

and

\[
 R(x)=x+\zeta(x)\gamma,\qquad
 \zeta(x)=\zeta(x+\gamma).
 \tag{3.2}
\]

Both are involutive matching switches.

### Theorem 3.1 (exact normalizer criterion)

The conjugate \(T=RSR^{-1}=RSR\) is again a \(\delta\)-matching switch if
and only if

\[
 \boxed{
 \epsilon(y)=1
 \quad\Longrightarrow\quad
 \zeta(y+\delta)=\zeta(y)
 \qquad(y\in V).}
 \tag{3.3}
\]

When (3.3) holds,

\[
 T(x)=x+\eta(x)\delta,\qquad
 \eta(x)=\epsilon(Rx),\qquad
 \eta(x)=\eta(x+\delta).
 \tag{3.4}
\]

Thus \(R\) may transport the active \(\delta\)-matching to a different
support, but it must map every active \(\delta\)-edge to another
\(\delta\)-edge.

#### Proof

Since \(R^{-1}=R\), put \(y=Rx=x+\zeta(x)\gamma\).  Direct substitution
gives

\[
 RSR(x)
 =x+\epsilon(y)\delta
  +\bigl(\zeta(x)+\zeta(y+\epsilon(y)\delta)\bigr)\gamma.
 \tag{3.5}
\]

If \(\epsilon(y)=0\), the \(\gamma\)-coefficient vanishes because
\(\zeta(y)=\zeta(x)\).  If \(\epsilon(y)=1\), it vanishes exactly under
(3.3).  Hence (3.3) is necessary and sufficient for every displacement
to lie in \(\{0,\delta\}\).

Under (3.3), let \(\eta(x)=\epsilon(Rx)\).  If \(\eta(x)=1\), (3.3) and
\(\gamma\)-invariance give \(\zeta(x+\delta)=\zeta(x)\), so
\(R(x+\delta)=Rx+\delta\) and
\(\eta(x+\delta)=\epsilon(Rx+\delta)=\epsilon(Rx)=1\).  Applying the
same argument from \(x+\delta\) excludes the pattern
\(\eta(x)=0,\eta(x+\delta)=1\).  Thus \(\eta\) is
\(\delta\)-invariant, proving (3.4).  \(\square\)

### Corollary 3.2 (the exact ten-state plane)

On one affine \(\langle\delta,\gamma\rangle\)-plane there are sixteen
pairs of matching fields \((\epsilon,\zeta)\).  Exactly ten satisfy
(3.3).

#### Proof

\(\epsilon\) has two values, one on each \(\delta\)-edge, and \(\zeta\)
has two values, one on each \(\gamma\)-edge.  If \(\epsilon=0\), all four
choices of \(\zeta\) work.  For each of the other three choices of
\(\epsilon\), (3.3) forces the two values of \(\zeta\) to agree, giving
two choices.  Hence \(4+3\cdot2=10\).  \(\square\)

The legal states include genuine transport.  For example, let
\(\epsilon\) activate exactly one \(\delta\)-edge and take
\(\zeta\equiv1\).  Then \(R\) translates that active edge by \(\gamma\),
and \(RSR^{-1}\ne S\).

Thus noncommuting conjugated closure is not algebraically impossible.
It is, however, highly correlated: an arbitrary second matching field
does not normalize the active first field.

### Theorem 3.3 (routed exit direction)

For \(c\in\mathbb F_2\), put

\[
                         \theta_c=\delta+c\gamma.
 \tag{3.6}
\]

Then \(T=RSR^{-1}\) is a \(\theta_c\)-matching switch if and only if

\[
 \boxed{
 \epsilon(y)=1
 \quad\Longrightarrow\quad
 \zeta(y+\delta)+\zeta(y)=c
 \qquad(y\in V).}
 \tag{3.7}
\]

When this holds,

\[
 T(x)=x+\eta(x)\theta_c,\qquad
 \eta(x)=\epsilon(Rx),\qquad
 \eta(x)=\eta(x+\theta_c).
 \tag{3.8}
\]

#### Proof

Formula (3.5) shows that at an active point the displacement is exactly

\[
                  \delta+
                  \bigl(\zeta(y+\delta)+\zeta(y)\bigr)\gamma.
 \tag{3.9}
\]

Thus it is the fixed vector \(\theta_c\) on every active edge exactly
under (3.7).  The conjugate \(T\) is an involution.  Any involution of the
form \(x\mapsto x+\eta(x)\theta_c\) has
\(\eta(x)=\eta(x+\theta_c)\), proving (3.8).  \(\square\)

### Corollary 3.4 (all sixteen states route on one plane)

On one affine \(\langle\delta,\gamma\rangle\)-plane, every one of the
sixteen pairs \((\epsilon,\zeta)\) closes as a matching switch if the exit
direction may be chosen from

\[
                         \{\delta,\delta+\gamma\}.
 \tag{3.10}
\]

The ten states in Corollary 3.2 exit in direction \(\delta\).  For each
nonzero \(\epsilon\), the two nonconstant choices of \(\zeta\) exit in
direction \(\delta+\gamma\), giving the remaining six states.

If \(\delta=e_a+e_b\) and \(\gamma=e_b+e_c\) come from overlapping
coordinate transpositions, then

\[
                         \delta+\gamma=e_a+e_c
 \tag{3.11}
\]

is again a legal physical transposition direction.  Hence the
\(S\mapsto RSR^{-1}\) mechanism really does realize one abstract
noncommuting routed crossing.  Across many affine planes, however, the
derivative in (3.7) may take both values.  A single fixed-direction exit
then fails unless those plane values are synchronized; allowing a mixed
exit produces a more general matching bank which still requires a
literal whole-owner and shadow-cocycle proof.

### Corollary 3.5 (abstract open--route--close identity)

If \(S\) and \(R\) are actual reversible factor transformations and the
transported exit switch \(T=RSR^{-1}\) is available, then chronological
opening by \(S\), routing by \(R\), and closing by \(T\) has net action
\(R\):

\[
                         T\,R\,S
             =(RSR^{-1})RS=R.
 \tag{3.12}
\]

Thus conjugation is exactly the algebra needed to carry an open switch
through a noncommuting router.  The assertion is only useful physically
when \(T\) is again a literal owner trade and the resulting successor
passes (2.3).  Theorems 3.1 and 3.3 decide the first issue in the binary
label model; they do not decide the second.

### Lemma 3.6 (the octahedron itself is a conjugated shore rotation)

Use the six octahedral ports

\[
 {\cal V}_0=\{ab,ac,bc\},\qquad
 {\cal V}_1=\{ad,bd,cd\},
 \tag{3.13}
\]

and the two matchings

\[
\begin{aligned}
 M_0&=\{ac-ad,\ ab-bd,\ bc-cd\},\\
 M_1&=\{ab-ad,\ ac-cd,\ bc-bd\}.
\end{aligned}
 \tag{3.14}
\]

Let \(R\) fix \({\cal V}_0\) pointwise and act on the other shore by

\[
                         bd\mapsto ad\mapsto cd\mapsto bd.
 \tag{3.15}
\]

Then

\[
                         M_1=RM_0R^{-1}.
 \tag{3.16}
\]

#### Proof

The three old assignments from \({\cal V}_0\) to \({\cal V}_1\) are

\[
 ab\mapsto bd,\qquad ac\mapsto ad,\qquad bc\mapsto cd.
\]

Applying (3.15) gives respectively

\[
 ab\mapsto ad,\qquad ac\mapsto cd,\qquad bc\mapsto bd,
\]

which are exactly the edges of \(M_1\).  \(\square\)

This is more than a formal coincidence.  In the certified two-type
\(H\)-lift, all three ports on one shore carry the same ordered rail
directions.  Hence the abstract shore rotation (3.15) preserves the
collar *template*, and the octahedral identity is exactly a three-port
conjugated matching identity.  What remains missing is a literal owner
router realizing \(R\) inside the ambient factor without paying a fresh
disjoint \(H\)-collar.  Since \(R\) is a 3-cycle, it is the first case in
which two noncommuting routed transpositions could in principle do so.

## 4. Why the existing conjugated braid is not yet a useful invisible trade

The syndrome \(Q_4\) braid and its nested-invariance extension prove
literal owner exactness for many noncommuting layers.  They do not prove
equality of protected shadow decks.  There is an exact reason that no
intrapacket specialization can do so nontrivially.

### Theorem 4.1 (intrapacket trace-invisible conjugation is inert)

Let all intermediate and final successor edges lie in one physical
split-pair packet \(Q_R\).  If the final lower depth-one multiset equals
the initial lower depth-one multiset, then the final edge set equals the
initial edge set.  In particular, every trace-invisible conjugated-router
word supported in one packet has joining rank zero.

#### Proof

Inside a split-pair packet, the lower target of a Johnson edge recovers
the changed pair direction and every spectator bit.  Hence the map

\[
                         e\longmapsto\ell(e)
 \tag{4.1}
\]

is injective.  Equality of lower-target multisets therefore gives equality
of edge multisets.  Equal successor edge sets have the same components,
so the joining rank is zero.  \(\square\)

Coordinate conjugation of a packet does not change the argument; it only
relabels the injective target map.  Therefore the positive ten-state
normalizer calculation and the linear-entropy nested braid solve only the
owner-composition layer.  To affect component count while returning all
protected traces, the router must exchange edges between different
physical packets or different exterior frames.

## 5. Exact surviving theorem

The remaining close-packed route can now be stated without ambiguity.

> **Cross-packet conjugated \(H\)-cocycle theorem (open).**  Construct a
> two-queue state grammar of literal cross-packet Johnson trades such that:
>
> 1. every crossing transports an active matching by the normalizer law
>    \(S\mapsto RSR^{-1}\) and preserves exact middle ownership;
> 2. the aggregate protected meet/join derivative satisfies the
>    coboundary identity (2.7) at every depth \(q\le H\) and both signs;
> 3. the routed words are return-free, so all selected columns lie in
>    \(\Gamma_H\);
> 4. the total joining rank is
>    \[
>      \left({2\over\sqrt\pi}+o(1)\right){W\over\sqrt m};
>    \]
> 5. its collar participation is necessarily at least the lower bound
>    (0.4), and the construction remains cap-safe under that dense reuse.
>
> By Theorems 2.1--2.2 and the invisible-trade packing lemma, this theorem
> would collapse the product-SCD components while preserving every signed
> trace through depth \(H\), and hence would close the chronology gate.

What is now ruled out:

* owner-disjoint certified octahedral \(H\)-atoms;
* every bounded-overlap family of context-separated \(H\)-atoms; and
* every intrapacket \(S\mapsto RSR^{-1}\) braid, even though nontrivial
  fixed- or routed-direction conjugated matching transport exists
  abstractly.

What remains open is genuinely narrower: a dense, cross-packet,
noncommuting meet/join coboundary.  Neither the octahedral local identity
nor the existing nested-invariance braid supplies it.
