# A rank-two core transplant pairs an entire proper-target chain with disjoint owners

**Date:** 2026-08-07  
**Method:** exchange two core coordinates with the first two rail coordinates  
**Status:** theorem.  This gives the exact local mixed-core actuator missing
from the fixed-core decorated-rectangle circulation: one positive proper-target
chain is reproduced as a negative chain at every depth \(h=2,\ldots,D\), while
the two complete role-owner stars are disjoint.  Global packing of these
transplants into whole rectangles remains open.

## 1. The positive chain

Work in the complemented facet-ring model, with \(r\ge5\).  Fix

\[
                         |S|=r-3
\]

and a point \(a\notin S\).  Let

\[
                         y_1,y_2,\ldots,y_D
\]

be distinct labels outside \(S+a\).  Put

\[
                         Y_h=\{y_1,\ldots,y_h\}
 \qquad(2\le h\le D).                                \tag{1.1}
\]

The chain

\[
                         T_h=S+a+Y_h                 \tag{1.2}
\]

is exactly the complementary proper-target chain emitted at one phase by
the positive shore of a forward rectangle whose opposite leaf cycle contains
\(y_1,y_2,\ldots,y_D\) consecutively in the appropriate orientation.

Let \(F_+\) be the complete leaf set of that positive role.  Thus

\[
 \{y_1,\ldots,y_D\}\subseteq F_+,
 \qquad F_+\cap(S+a)=\varnothing.                    \tag{1.3}
\]

Its complete role-owner star is

\[
                         \mathcal O_+
   =\{S+a+y:y\in F_+\}.                              \tag{1.4}
\]

## 2. The transplant

Choose distinct coordinates

\[
                         x_1,x_2\in S
\]

and define

\[
                         S'=(S-\{x_1,x_2\})
                              +\{y_1,y_2\}.          \tag{2.1}
\]

The negative distinguished point will be

\[
                         b'=x_1.                     \tag{2.2}
\]

Give its opposite leaf cycle the consecutive prefix

\[
                         x_2,a,y_3,y_4,\ldots,y_D.   \tag{2.3}
\]

Equivalently, put

\[
 I_h=\{x_2,a,y_3,\ldots,y_h\}
 \qquad(2\le h\le D).                                \tag{2.4}
\]

The displayed prefix may be extended arbitrarily to a cyclic order on any
leaf set \(F_-\) satisfying

\[
 \{x_2,a,y_3,\ldots,y_D\}\subseteq F_-,
 \qquad F_-\cap(S'+x_1)=\varnothing.                 \tag{2.5}
\]

The corresponding negative role-owner star is

\[
                         \mathcal O_-
   =\{S'+x_1+z:z\in F_-\}.                           \tag{2.6}
\]

## 3. Exact all-depth cancellation

### Theorem 3.1 (rank-two core transplant)

For every \(2\le h\le D\),

\[
 \boxed{
                         S'+x_1+I_h=T_h.}             \tag{3.1}
\]

Moreover,

\[
 \boxed{
                         \mathcal O_+\cap\mathcal O_-
                         =\varnothing.}               \tag{3.2}
\]

Thus one positive proper-target occurrence chain can be canceled, at all
proper widths simultaneously, by one negative occurrence chain belonging to
a different core, without reusing any owner from either complete role star.

#### Proof

Using (2.1)--(2.4),

\[
 \begin{aligned}
 S'+x_1+I_h
   &=(S-\{x_1,x_2\})+\{y_1,y_2\}+x_1
       +\{x_2,a,y_3,\ldots,y_h\}\\
   &=S+a+\{y_1,\ldots,y_h\}
    =T_h,
 \end{aligned}                                       \tag{3.3}
\]

which proves (3.1).

Every owner in \(\mathcal O_+\) contains \(x_2\), because \(x_2\in S\).
The center

\[
                         S'+x_1=S-x_2+y_1+y_2        \tag{3.4}
\]

does not contain \(x_2\).  Hence an owner in \(\mathcal O_-\) can equal an
owner in \(\mathcal O_+\) only if its leaf is \(z=x_2\).  In that case the
negative owner is

\[
                         S+y_1+y_2,                  \tag{3.5}
\]

whereas a positive owner is \(S+a+y\), \(y\in F_+\).  Equality would force
\(\{y_1,y_2\}=\{a,y\}\), impossible because \(a\notin F_+\) and
\(y_1,y_2\in F_+\).  This proves (3.2). \(\square\)

### Theorem 3.2 (the transplant normal form is forced)

Let a positive role have center \(G\), simple cyclic leaf order \(F_+\), and
one phase beginning

\[
                         y_1,y_2,y_3,\ldots,y_D.
\]

Let a negative role have center \(H\), simple cyclic leaf order \(F_-\), and
one phase beginning

\[
                         x_1,x_2,x_3,\ldots,x_D.
\]

Assume their complete role-owner stars are disjoint and their proper targets
agree at every depth:

\[
 G+\{y_1,\ldots,y_h\}
   =H+\{x_1,\ldots,x_h\}
 \qquad(2\le h\le D).                                \tag{3.6}
\]

Then necessarily

\[
 |G-H|=|H-G|=2,
 \quad
 \{y_1,y_2\}=H-G,
 \quad
 \{x_1,x_2\}=G-H,                                   \tag{3.7}
\]

and, after the first two positions,

\[
                         y_h=x_h
 \qquad(3\le h\le D).                                \tag{3.8}
\]

Consequently, two fixed complete roles with disjoint owner stars can pair at
most one phase chain.  A length-\(w\) receiver therefore needs at least
\(w\) distinct donor roles; Theorem 4.3 below meets this lower bound.

#### Proof

The common depth-two target has rank \(r\) and contains both rank-
\((r-2)\) centers, so, writing \(j=|G-H|=|H-G|\),

\[
                         (r-2)+j\le r,
\]

and hence \(j\le2\).

If \(j=0\), equality at depth two gives
\(\{y_1,y_2\}=\{x_1,x_2\}\).  Both roles then use the same two owners
obtained by adjoining those leaf labels to \(G=H\), contrary to
owner-disjointness.

If \(j=1\), write \(G-H=\{a\}\), \(H-G=\{b\}\).  Equality at depth two
forces, for some \(c\),

\[
 \{y_1,y_2\}=\{b,c\},
 \qquad
 \{x_1,x_2\}=\{a,c\}.
\]

The owner \(G+b=H+a\) then lies in both complete role stars, again a
contradiction.  Therefore \(j=2\).  Since \(|G\cup H|=r\), the common
depth-two target is exactly \(G\cup H\), forcing the first three assertions
in (3.7).

For \(h\ge3\), all later leaf labels lie outside \(G\cup H\): on the
positive shore the only elements of \(H-G\) in the leaf order are already
\(y_1,y_2\), and symmetrically on the negative shore.  Canceling
\(G\cup H\) from the two sides of (3.6) gives

\[
                         \{y_3,\ldots,y_h\}
                          =\{x_3,\ldots,x_h\}.
\]

Comparison at successive \(h\)'s proves (3.8).

Finally, a simple cyclic order contains a prescribed unordered adjacent pair
in exactly one phase.  Equation (3.7) fixes that pair on both roles, so the
same pair of complete roles cannot match a second phase. \(\square\)

## 4. Upper-current interpretation

The positive distinguished center is

\[
                         G_+=S+a,
\]

whereas the negative center is

\[
                         G_-=S'+x_1=S-x_2+y_1+y_2.   \tag{4.1}
\]

One paired phase chain transports one immediate-upper occurrence from
\(G_-\) to \(G_+\), i.e. it has upper current

\[
                         [G_+]-[G_-].                 \tag{4.2}
\]

If an assembled bank contains \(w\) such phase transplants with the same
ordered center pair \((G_+,G_-)\), then their aggregate current is

\[
                         w([G_+]-[G_-]).             \tag{4.3}
\]

Thus the transplant converts exact all-depth proper cancellation into a
weighted transport edge on the rank-\((r-2)\) center layer.  A directed
circulation of these transport edges would cancel upper current as well.

The adjacent rectangle sizes in the two-size construction have compatible
phase counts: an \(A\)-role of a size-\(p\) rectangle and a \(B\)-role of a
size-\((p+1)\) rectangle both have \(p+1\) opposite-leaf phases.  This is
why their chains can in principle be bundled without a phase-count sidecar.
The theorem does not claim that all phases of one role transplant to one
other role: the core (2.1) depends on the first two labels of the chosen
phase.  Global assembly must distribute the phase transplants among many
roles and close the resulting unit center-current edges.

There is also a useful canonical equal-length choice.  If the positive leaf
set is \(F_+\), take

\[
                         F_-=(F_+-\{y_1,y_2\})
                                  +\{x_2,a\}.         \tag{4.3a}
\]

Then

\[
 \boxed{
                         G_+\mathbin{\dot\cup}F_+
                         =G_-\mathbin{\dot\cup}F_-.} \tag{4.3b}
\]

Thus an equal-length transplant is a literal two-coordinate exchange between
the center and leaf shores of one fixed support.  Conversely, any such
two-coordinate exchange can be oriented as Theorem 3.1 after choosing one
removed center label as the positive point and one common center label as the
negative point.  The remaining leaf order is chosen with the exchanged pairs
in the displayed prefix positions.

### Corollary 4.1 (every distance-two center edge is a transplant)

Let \(G,G'\in\binom{[n]}{r-2}\) satisfy

\[
                         |G-G'|=|G'-G|=2.            \tag{4.4}
\]

Then either orientation of the formal current

\[
                         [G]-[G']                    \tag{4.5}
\]

has a rank-two core-transplant realization which pairs one complete proper
phase chain and uses disjoint role-owner stars.

#### Proof

Write

\[
                         G-G'=\{a,x_2\},
 \qquad                 G'-G=\{y_1,y_2\}.           \tag{4.6}
\]

Choose any \(x_1\in G\cap G'\), put \(S=G-a\), and apply Theorem 3.1.
Then

\[
 S-x_1-x_2+y_1+y_2=G'-x_1,
\]

so the positive and negative centers are exactly \(G\) and \(G'\).
Reversing their names realizes the other orientation. \(\square\)

### Corollary 4.2 (the abstract upper-current lattice is generated)

Assume \(r\ge5\).  The graph on \(\binom{[n]}{r-2}\) joining pairs at
distance two is connected.  Consequently the unit currents of Corollary 4.1
generate every integral center current \(u\) satisfying

\[
                         \sum_Gu_G=0.                \tag{4.7}
\]

#### Proof

It is enough to simulate one ordinary Johnson swap.  Let

\[
                         T=G-a+b,
\]

where \(a\in G\), \(b\notin G\).  Choose

\[
 c\in G-a,
 \qquad d,e\notin G+b
\]

distinct, and put

\[
                         H=G-\{a,c\}+\{d,e\}.        \tag{4.8}
\]

Then \(G,H\) are at distance two, and so are \(H,T\), because

\[
                         T-H=\{b,c\},
 \qquad                 H-T=\{d,e\}.                \tag{4.9}
\]

The required choices exist since \(|G|=r-2\ge2\) and
\(|[n]-G|=r+1\ge5\).  Ordinary Johnson swaps connect the complete fixed-rank
layer, so the distance-two graph is connected.  Oriented edges of a connected
graph generate its integral zero-sum vertex lattice. \(\square\)

Corollary 4.2 is only a current-lattice statement.  It does not assert that
an arbitrary edge decomposition can be lifted with mutually compatible leaf
cycles or owner resources.  It shows that after the proper chains are paired,
there is no remaining linear or connectivity obstruction in the upper row.

### Theorem 4.3 (one complete receiver cycle can be filled)

Fix a negative role with core \(Q\), distinguished point \(b\), and cyclic
leaf order

\[
                         Z=(z_t)_{t\in\mathbb Z_w},
 \qquad                 w\ge D,                      \tag{4.10}
\]

where \(|Q|=r-3\) and \(Q,b,Z\) are pairwise disjoint.  For each phase
\(t\), choose a two-set

\[
                         Y_t=\{u_t,v_t\}\subset Q
\]

and define a positive donor core and point by

\[
 S_t=Q-Y_t+b+z_t,
 \qquad                 a_t=z_{t+1}.                 \tag{4.11}
\]

Give that donor phase the leaf prefix

\[
                         u_t,v_t,z_{t+2},z_{t+3},\ldots,z_{t+D-1}. \tag{4.12}
\]

It extends canonically to the full length-\(w\) leaf cycle

\[
 F_t=Y_t\mathbin{\dot\cup}(Z-\{z_t,z_{t+1}\}),
 \quad
 (u_t,v_t,z_{t+2},z_{t+3},\ldots,z_{t-1}),           \tag{4.13}
\]

which is disjoint from \(S_t+a_t\).

Then the \(w\) donor phase chains reproduce, with opposite sign, all \(w\)
proper phase chains of the receiver.  Each donor's complete role-owner star
is disjoint from the receiver's complete role-owner star.  If

\[
                         2w\le r-3,                  \tag{4.14}
\]

the pairs \(Y_t\) may be chosen mutually disjoint, in which case the
\(w\) donor role-owner stars are mutually disjoint as well.

#### Proof

At phase \(t\), the receiver's complementary target of interval length
\(h\) is

\[
                         Q+b+\{z_t,z_{t+1},\ldots,z_{t+h-1}\}. \tag{4.15}
\]

The donor target prescribed by (4.11)--(4.12) is

\[
 \begin{aligned}
 &(Q-Y_t+b+z_t)+z_{t+1}
       +\{u_t,v_t,z_{t+2},\ldots,z_{t+h-1}\}\\
 &\hspace{35mm}=Q+b+\{z_t,z_{t+1},\ldots,z_{t+h-1}\},
 \end{aligned}                                       \tag{4.16}
\]

for every \(2\le h\le D\).  This is exactly Theorem 3.1 with

\[
 x_1=b,\quad x_2=z_t,\quad \{y_1,y_2\}=Y_t.
\]

Its owner-disjointness conclusion applies to each donor--receiver pair.
The ordering in (4.13) begins with the required prefix, so every donor phase
belongs to a genuine complete positive role.  Under (4.14), choose the
\(Y_t\)'s pairwise disjoint.  If \(t\ne s\), then

\[
                         Y_s\subseteq G_t-G_s,
 \qquad                 Y_t\subseteq G_s-G_t,        \tag{4.17}
\]

where \(G_t=S_t+a_t\) is the donor center.  Thus two donor centers differ
in at least two coordinates on each shore.  No rank-\((r-1)\) owner can
contain both rank-\((r-2)\) centers, so their complete owner stars are
disjoint.
\(\square\)

Theorem 4.3 removes the cyclic-prefix obstruction on the receiver shore:
one whole negative ring role can accept all of its phase cancellations.
With disjoint \(Y_t\)'s it also removes mutual owner collisions among the
donors, and (4.13) completes every donor phase to a genuine positive role.
It deliberately does not place those \(w\) roles into whole rectangle
blocks or cancel their other \(w-1\) phases.  That regenerative grouping is
now the exact surviving assembly row.

## 5. Exact remaining global gate

Before imposing Boolean labels, even the complete role-incidence skeleton
has an exact solution.

### Theorem 5.1 (optimal two-size phase-role factor)

Use the two-size rectangle counts

\[
                         H_p=p+2,
 \qquad                 H_{p+1}=p.                  \tag{5.1}
\]

Let \(P_q\) denote positive roles of size-\(q\) rectangles and \(N_q\)
negative roles.  There is a simple bipartite graph \(\mathcal P\) between
all positive and negative roles such that every role has degree equal to its
number of proper phase chains:

\[
 \deg(P_q)=q+1,
 \qquad
 \deg(N_q)=q.                                        \tag{5.2}
\]

Moreover, \(\mathcal P\) uses only the two pair types

\[
                         P_p-N_{p+1},
 \qquad                 P_{p+1}-N_p.                \tag{5.3}
\]

Thus it pairs every positive phase with a negative phase, never using the
same ordered role pair twice, exactly as required by Theorem 3.2.

#### Proof

There are

\[
 |P_p|=p(p+2)=|N_{p+1}|.                             \tag{5.4}
\]

Both role types require degree \(p+1\).  On two copies of
\(\mathbb Z_{p(p+2)}\), join \(i\) to

\[
                         i,i+1,\ldots,i+p.
\]

This is a simple \((p+1)\)-regular bipartite graph and supplies the first
pair type.

The remaining counts are

\[
 |P_{p+1}|=p(p+1),
 \qquad
 |N_p|=(p+2)(p+1).                                   \tag{5.5}
\]

Partition them into \(p+1\) groups of sizes \(p\) and \(p+2\), respectively,
and place one complete bipartite graph \(K_{p,p+2}\) on every pair of
groups.  Each \(P_{p+1}\) role then has degree \(p+2\), and each \(N_p\)
role degree \(p\), supplying the second pair type.  All phase degrees in
(5.2) are exhausted. \(\square\)

Theorem 5.1 and Theorem 4.3 meet each other exactly: a receiver of degree
\(w\) has \(w\) distinct donors, and every donor uses one phase on that
receiver.  What remains is to label the vertices of this abstract graph by
whole Boolean roles so that every edge is a rank-two transplant and the
roles incident with each original rectangle share its required core and
opposite leaf cycle.

There is no longer a local incompatibility between:

* all-depth proper-target equality;
* different cores; and
* owner-disjoint role stars.

The surviving theorem is an assembly statement.

> **Rectangle-transplant circulation lemma.**  Group all positive and
> negative role-phase chains of the two-size owner/upper factor into
> rank-two transplants (2.1)--(2.6), so that the resulting roles assemble
> into whole forward rectangles, every owner is used at most once, and the
> weighted center transports (4.3) form a circulation.

The transplant consumes no additional source position and preserves the
literal cyclic-order requirement on the paired chain.  What remains is the
simultaneous consistency of the many prescribed prefixes belonging to one
leaf cycle and the global owner packing across roles not paired to each other.
