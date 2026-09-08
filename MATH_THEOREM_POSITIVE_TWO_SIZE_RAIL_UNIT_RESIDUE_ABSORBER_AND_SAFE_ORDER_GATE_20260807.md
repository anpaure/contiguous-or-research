# Two consecutive nonmaximal rails give a positive coherent unit-residue absorber

**Date:** 2026-08-07  
**Inputs:** MATH_THEOREM_NONMAXIMAL_PURE_RAIL_LATTICE_BREAKERS_20260807.md
and MATH_THEOREM_CAROUSEL_ADJACENT_TRANSPOSITION_COHERENT_BIRAIL_TRADE_20260807.md  
**Method:** two positive role-swap pairs at consecutive component sizes,
signature-separated owner shores, and cyclic-order avoidance  
**Status:** unconditional positive owner/all-common-width absorber theorem.
The signed Bézout generator is realized by two genuine owner-disjoint
component matchings, not merely by a formal integer combination.  A large
common maximal-carousel background can be added without owner collisions.
What remains open is exact named-target absorption into a global component
factor and safe connectivity under all compiler tickets.

## 1. Pure-rail notation

Put

\[
q=d+1,\qquad c=R-q,\qquad M=k-c=k-R+q.
\tag{1.1}
\]

For any

\[
2(q+1)\le N\le M,
\tag{1.2}
\]

a pure rail consists of a core \(C\), \(|C|=c\), a toggle set \(T\),
\(|T|=N\), and a cyclic order \(\sigma\) of \(T\).  Its owners are

\[
\mathcal O_N(C,T,\sigma)
=\{C\cup I:I\in\mathcal I_q(\sigma)\}.
\tag{1.3}
\]

For every proper width \(1\le\ell<N\), its complete width-\(\ell\) deck is

\[
\mathcal D_{N,\ell}(C,T,\sigma)
=\{C\cup I:I\in\mathcal I_\ell(\sigma)\}.
\tag{1.4}
\]

Each row is simple.  Define its coordinate-incidence vector by

\[
\omega_{N,\ell}(C,T)
=\sum_{S\in\mathcal D_{N,\ell}(C,T,\sigma)}\mathbf1_S.
\tag{1.5}
\]

It is independent of the cyclic order and equals

\[
\boxed{\omega_{N,\ell}(C,T)=N\mathbf1_C+\ell\mathbf1_T.}
\tag{1.6}
\]

The owner vector is the special case \(\ell=q\).

## 2. Explicit positive unit gadget

Assume

\[
M-2\ge2(q+1)
\tag{2.1}
\]

and \(c\ge1\).  Put

\[
N_1=M-1,\qquad N_2=M-2.
\tag{2.2}
\]

Choose distinct coordinates \(x,y,z\), and choose

\[
D\subseteq[k]\setminus\{x,y,z\},
\qquad |D|=c-1.
\tag{2.3}
\]

Define four legal pure-rail role assignments:

\[
\begin{array}{c|c|c|c}
&\text{size}&\text{core}&\text{unused}\\ \hline
Q_1^+&N_1&D\cup\{x\}&\{y\}\\
Q_1^-&N_1&D\cup\{y\}&\{x\}\\
Q_2^+&N_2&D\cup\{y\}&\{x,z\}\\
Q_2^-&N_2&D\cup\{x\}&\{y,z\}.
\end{array}
\tag{2.4}
\]

In every row, the toggle set is the complement of the displayed core and
unused set.  Give each toggle set an arbitrary cyclic order.

Put

\[
\mathcal A^+=\{Q_1^+,Q_2^+\},
\qquad
\mathcal A^-=\{Q_1^-,Q_2^-\}.
\tag{2.5}
\]

### Theorem 2.1 (positive coherent unit-residue absorber)

Each of \(\mathcal A^+,\mathcal A^-\) is an owner matching.  More
strongly, at every common proper width

\[
1\le\ell<N_2,
\tag{2.6}
\]

the two component decks inside either side are disjoint.  Their incidence
vectors obey

\[
\boxed{
\sum_{Q\in\mathcal A^+}\omega_{Q,\ell}
-
\sum_{Q\in\mathcal A^-}\omega_{Q,\ell}
=\mathbf e_x-\mathbf e_y.}
\tag{2.7}
\]

In particular (2.7) holds simultaneously for:

* every lower width through \(d\);
* the owner width \(q=d+1\);
* the immediate upper width \(d+2\); and
* every other protected width below \(M-2\).

Both alternatives contain exactly

\[
N_1+N_2=2M-3
\tag{2.8}
\]

sets in every common width.  Thus this is a positive trade between two
genuine equal-size configurations, not a signed lattice identity.

#### Proof

Every set in every deck of \(Q_1^+\) contains \(x\) and omits \(y\).
Every set in every deck of \(Q_2^+\) contains \(y\) and omits \(x\).
Consequently the two decks are disjoint.  The same argument with signs
reversed proves disjointness in \(\mathcal A^-\).

All coordinates outside \(\{x,y\}\) have the same role on the two sides:
the coordinate \(z\) is a toggle in both size-\(N_1\) components and is
unused in both size-\(N_2\) components; every coordinate of \(D\) is
always core; every other coordinate is always toggle.  By (1.6),

\[
\omega_{Q_1^+,\ell}-\omega_{Q_1^-,\ell}
=N_1(\mathbf e_x-\mathbf e_y),
\tag{2.9}
\]

whereas

\[
\omega_{Q_2^+,\ell}-\omega_{Q_2^-,\ell}
=-N_2(\mathbf e_x-\mathbf e_y).
\tag{2.10}
\]

Since \(N_1-N_2=1\), summing gives (2.7).  The count (2.8) is immediate.
\(\square\)

### Corollary 2.2 (positive realization of the zero-sum lattice)

Every finitely supported

\[
v\in\mathbb Z^k,\qquad \sum_i v_i=0,
\tag{2.11}
\]

is a sum of positive unit gadgets of Theorem 2.1, after writing \(v\) as
a sum of unit differences.  If the number of required unit gadgets is
bounded, their coordinate roles and cyclic orders can be chosen
successively so that every alternative is owner-disjoint, subject to the
local avoidance condition in Section 4.

This corollary concerns the coordinate-incidence lattice.  It does not say
that an arbitrary named set of owner holes has already been absorbed.

### Corollary 2.3 (the \(k=17\) residue is positively broken)

At \(k=17,R=9,d=3\),

\[
q=4,\qquad c=5,\qquad M=12,
\]

so the gadget uses legal component sizes \(11\) and \(10\).  Each state is
an owner matching of \(21\) owners, and switching states changes every
common-width coordinate-incidence vector by exactly
\(\mathbf e_x-\mathbf e_y\).  Thus the earlier mod-\(4\) maximal-carousel
obstruction is broken by one explicit positive local trade.

## 3. A compatible positive maximal background

Assume in this section that \(c\ge2\), so a maximal background core may
contain both signature coordinates.

Let \(\mathcal B\) be any owner-disjoint family of size-\(M\) pure rails
whose cores all contain \(\{x,y\}\).  Every background owner contains both
\(x,y\), whereas every owner in either alternative (2.5) contains exactly
one of them.  Hence

\[
\boxed{
\mathcal B\cup\mathcal A^+
\quad\text{and}\quad
\mathcal B\cup\mathcal A^-
\text{ are both owner matchings}.}
\tag{3.1}
\]

The same remains true after arbitrary adjacent transpositions inside any
of the four absorber carousels.

There are very large such backgrounds.  Fix one \(c\)-core \(C_B\)
containing \(x,y\), and let \(T_B=[k]\setminus C_B\), \(|T_B|=M\).  A
random cyclic order of \(T_B\) contains a fixed \(q\)-subset as a cyclic
block with probability at most

\[
\frac{M}{{M\choose q}}.
\tag{3.2}
\]

After \(b\) owner-disjoint background carousels have been chosen, at most
\(bM\) \(q\)-blocks are forbidden.  Therefore another order exists whenever

\[
\boxed{bM^2<{M\choose q}.}
\tag{3.3}
\]

Greedy iteration gives at least

\[
\left\lfloor\frac{{M\choose q}-1}{M^2}\right\rfloor
\tag{3.4}
\]

pairwise owner-disjoint maximal background carousels, all compatible with
both absorber states.  This is a genuinely positive common background;
its incidence cancels from the difference (2.7).

## 4. Exact local avoidance and extension conditions

Fix one pure-rail role assignment \((C,T)\), \(|T|=N\), and let
\(\mathcal F_\ell\) be forbidden rank-\((c+\ell)\) ticket values at proper
width \(\ell\).  Only forbidden sets of the form \(C\cup J\), \(J\in
{T\choose\ell}\), can collide with this component.

### Proposition 4.1 (one-order extension)

A cyclic order of \(T\) avoiding every forbidden value at every protected
width exists under the explicit sufficient condition

\[
\boxed{
\sum_{\ell\in\mathcal W}
\frac{N\,|\{J\in{T\choose\ell}:C\cup J\in\mathcal F_\ell\}|}
{{N\choose\ell}}
<1.}
\tag{4.1}
\]

#### Proof

Choose a uniformly random cyclic order.  For fixed \(J\in{T\choose\ell}\),
the expected number of cyclic \(\ell\)-blocks equal to \(J\) is
\(N/{N\choose\ell}\).  The probability of at least one such block is at
most this expectation.  Sum over all forbidden tickets and use the union
bound.  If the sum is below one, some order has no forbidden block.
\(\square\)

For the owner row alone, (4.1) is simply

\[
|\mathcal F_q(C,T)|\,N<{N\choose q}.
\tag{4.2}
\]

Because the two components of either absorber state lie in the disjoint
signature shores \(x\bar y\) and \(\bar x y\), they may be extended
independently using (4.1).  This gives an exact, checkable local
extendability condition against a previously selected background.

## 5. Adjacent transpositions supply the internal router, not the residue

For fixed roles \((C,T)\), adjacent transpositions generate all cyclic
orders of \(T\).  At every width \(\ell\), one transposition replaces
exactly two old values by two new values on the coherent left/right rays.
It leaves (1.6) unchanged.

### Lemma 5.1 (exact named-owner \(2\)-switch port)

Let \(P,Q\subseteq T\) be disjoint \(q\)-sets, choose \(y\in P\) and
\(x\in Q\), and assume \(N\ge2q+2\).  There is a cyclic toggle order whose
one adjacent transposition replaces exactly the owner pair

\[
\boxed{
C\cup(P-\{y\})\cup\{x\},
\qquad
C\cup(Q-\{x\})\cup\{y\}}
\tag{5.1}
\]

by

\[
\boxed{C\cup P,\qquad C\cup Q.}
\tag{5.2}
\]

Every other owner is fixed.  At every other proper width the same move is
the coherent two-ray trade.

#### Proof

Place the labels cyclically in the local order

\[
P-\{y\},\ x,\ y,\ Q-\{x\},
\tag{5.3}
\]

with arbitrary orders inside the two displayed \((q-1)\)-sets.  Put the
at least two remaining toggle labels in the exterior gap.  Thus the
\((q-1)\) labels immediately left of \(x\) are \(P-\{y\}\), and those
immediately right of \(y\) are \(Q-\{x\}\).  Apply the adjacent-
transposition formula at owner width \(q\). \(\square\)

Lemma 5.1 is an actual named-vertex absorber port: if the crossed pair
(5.1) lies in the reserve and (5.2) is the desired pair of holes, one
adjacent toggle trade absorbs those holes.  It is moment-neutral because
the sums of the two owner incidence vectors in (5.1) and (5.2) agree.
Hence it complements, rather than replaces, the unit-moment macro of
Theorem 2.1.

For one fixed desired pair \(C\cup P,C\cup Q\), the number of oriented
swap incidences supplied by this construction is exactly

\[
\boxed{
q^2\,((q-1)!)^2\,(N-2q)!.}
\tag{5.4}
\]

Indeed choose \(y\in P,x\in Q\), order the two \((q-1)\)-rays, and order
the \(N-2q\) exterior labels.  Rooting the cyclic order at the active
label \(x\) removes rotational overcount.  This factorial port supply is
available before any background exclusions are imposed.

Define the **safe-order graph**

\[
\mathfrak S(C,T;\mathcal F)
\tag{5.5}
\]

whose vertices are cyclic orders satisfying all protected ticket
constraints and whose edges are adjacent transpositions for which the two
new ticket values at every protected width are free (or are the prescribed
next vertices of an alternating augmentation).

### Proposition 5.2 (exact reconfiguration condition)

Two safe incarnations of one carousel are connected by literal coherent
birail trades if and only if their cyclic orders lie in the same connected
component of \(\mathfrak S(C,T;\mathcal F)\).

For one step, owner-disjointness is equivalent to the two entering owners
being outside the fixed background and outside every other selected
component after the two departing owners are removed.  The corresponding
condition at each designated lower/upper/compiler row is the identical
two-ray test from the adjacent-transposition theorem.

This is tautologically exact but useful: no global compiler matching must
survive intermediate orders; only the listed entering ports must be free
or augmentable.

Adjacent transpositions alone cannot create (2.7), because they preserve
the role partition \(C\dot\cup T\dot\cup U_{\rm unused}\) and hence every
coordinate-incidence vector (1.6).  The two-size role-swap macro is
therefore indispensable.  The transpositions provide its internal
named-target router after the lattice residue has been created.

## 6. Iterative-absorption readiness and remaining obstruction

The catalogue

\[
\boxed{\{M-2,M-1,M\}}
\tag{6.1}
\]

now has the following positive features:

1. \(M-1,M-2\) realize every unit coordinate difference by two positive,
   equal-size, owner-disjoint alternatives.
2. The same unit difference occurs coherently at every common proper
   interval width, including owner and both q1 rows.
3. A large common \(M\)-carousel background can coexist with both
   alternatives.
4. Exact cyclic-order avoidance is supplied by (4.1).
5. Lemma 5.1 absorbs any prepared pair of disjoint-petal owner holes by
   one literal two-owner switch.
6. Adjacent transpositions give a two-ray-per-width generator for routing
   named holes without changing the lattice residue.

What is not yet proved is the robust absorber property required by an
iterative-absorption theorem:

> for every sufficiently small *named* owner/target leave satisfying the
> global lattice conditions, choose disjoint unit gadgets and safe-order
> paths so that one state covers the reference reserve and the other state
> covers the reserve plus the leave, while preserving the upper/compiler
> tickets.

The possible obstruction is now topological rather than arithmetic:
\(\mathfrak S(C,T;\mathcal F)\) may be disconnected by structured forbidden
ticket families even when (4.1) supplies many isolated safe orders.
Neither the nonmaximal lattice theorem nor adjacent-transposition
generation without forbidden states proves this connectivity.

Also, the size-\(M-2\) components reach only universe rank \(k-2\).  The
top two upper ranks must be carried by the common maximal background or a
separate full-ground reserve; they are not part of the unit macro's common
proper-width guarantee.

Thus the exact next lemma is a **safe-order expansion/absorption theorem**
for the four-carousel gadget under the occurrence-labelled owner,
lower/upper, and common-cap forbidden sets.  The positive lattice and
owner-disjointness rows themselves are now closed.

This note does not prove the global named-target absorber,
\(\nu(k)\le B(k)+O(1)\), or exact equality.
