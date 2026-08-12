# Every owner has a polynomial-support signed rail macro; conformal composition is the first positive gate

**Date:** 2026-08-12
**Inputs:** the nonmaximal pure-rail family, the positive two-size unit
residue macro, and the full named-owner lattice theorem
**Status:** unconditional explicit signed representation of every individual
owner by actual closed-rail replacement currents.  Every elementary current
is a difference of two genuine owner matchings.  The theorem does **not**
assert that all negative sides, or all positive sides, are mutually
owner-disjoint.  That conformal-composition assertion is isolated exactly.

## 1. Notation

Put

\[
 q=d+1,\qquad c=R-q,\qquad M=k-c.
\tag{1.1}
\]

Assume

\[
 d\ge1,\qquad c\ge1,\qquad M-2\ge2(q+1).
\tag{1.2}
\]

For a legal pure rail \(Q=(C,T,\sigma)\), write

\[
 f(Q)=\sum_{I\in\mathcal I_q(\sigma)}e_{C\cup I}
\tag{1.3}
\]

for its named-owner column and \(P_Rf(Q)\) for its point-incidence
vector.

We use three elementary replacement currents.

1. An **insertion current** is the difference between a period-\((N+1)\)
   rail and the period-\(N\) rail obtained by deleting one toggle label.
2. A **unit-role current** is one state minus the other state of the
   positive two-size \((M-1,M-2)\) macro.  Its point image is one prescribed
   unit difference.
3. An **order current** is the difference between two copies of one rail
   which differ by one adjacent transposition of toggle labels.

Each side of each current is a genuine owner matching.  This statement is
local to the current; components belonging to different currents need not
be mutually disjoint.

## 2. The exact insertion current

Choose a core \(C\), an old toggle cycle \(T\) of size

\[
 2(q+1)\le N\le M-1,
\tag{2.1}
\]

and a label \(x\notin C\cup T\).  Insert \(x\) into one cut of the cyclic
order.  Let \(Q^-\) and \(Q^+\) be the old and new rails and put

\[
 \Delta_x=f(Q^+)-f(Q^-).
\tag{2.2}
\]

### Lemma 2.1 (one-more-than-one insertion ledger)

The two owner rows have a common subfamily, and after cancelling it

\[
 \boxed{
 \Delta_x=\sum_{i=0}^{q-1}e_{P_i}
          -\sum_{i=1}^{q-1}e_{O_i},}
\tag{2.3}
\]

where all \(2q-1\) displayed owners are distinct.  Every \(P_i\) contains
\(C\cup\{x\}\), while every \(O_i\) contains \(C\) and omits \(x\).
Moreover

\[
 \boxed{P_R\Delta_x={\bf1}_C+q e_x.}
\tag{2.4}
\]

For every owner

\[
 H=C\cup P,\qquad |P|=q,qquad x\in P,
\tag{2.5}
\]

the cut and local order may be chosen so that \(P_0=H\).

#### Proof

Only the old \(q\)-windows crossing the cut change.  There are \(q-1\)
of them.  After insertion, the changed windows are precisely the \(q\)
windows containing the new label \(x\).  Proper cyclic intervals are
distinct, and an old changed window omits \(x\), so all terms in (2.3) are
distinct.

At point level, a period-\(N\) rail has vector

\[
 N{\bf1}_C+q{\bf1}_T.
\]

Subtracting the old vector from the new one gives (2.4).  Finally, place
the \(q-1\) labels of \(P\setminus\{x\}\) next to the insertion cut in
the desired split between its two sides.  One new \(q\)-window is then
exactly \(P\), proving (2.5).  \(\square\)

The insertion current is already a positive conformal replacement, but it
does not have the point signature of one owner.  This correction is
load-bearing: \({\bf1}_C+qe_x\ne{\bf1}_H\) when \(q>1\).

## 3. Correct the point signature with unit-role macros

For every \(p\in P\setminus\{x\}\), the positive two-size theorem supplies
a current \(U_{p,x}\) such that

\[
 P_RU_{p,x}=e_p-e_x.
\tag{3.1}
\]

Each \(U_{p,x}\) is the difference of two two-component owner matchings;
both sides contain \(2M-3\) owners counted before cross-side cancellation.
Put

\[
 Y_H=\Delta_x+
      \sum_{p\in P\setminus\{x\}}U_{p,x}.
\tag{3.2}
\]

Then

\[
 \boxed{P_RY_H={\bf1}_H.}
\tag{3.3}
\]

Indeed, (2.4) and (3.1) give

\[
 {\bf1}_C+qe_x+
 \sum_{p\in P\setminus\{x\}}(e_p-e_x)
 ={\bf1}_C+\sum_{p\in P}e_p={\bf1}_H.
\]

Consequently

\[
 Z_H=e_H-Y_H
\tag{3.4}
\]

belongs to \(\ker_{\mathbb Z}P_R\).

### Theorem 3.1 (the whole point-correction star is conformal)

Assume in addition that

\[
 M\ge c+2,\qquad c>q,\qquad
 {N\choose q}>2q(N+1)^2,\quad N=M-2.
\tag{3.5}
\]

The currents \(U_{p,x}\) in (3.2) can be chosen jointly so that the
positive component collection of \(Y_H\) is an owner matching, the
negative component collection is an owner matching, and neither collection
collides with the corresponding side of \(\Delta_x\).  Moreover \(H\)
occurs on the positive side of \(\Delta_x\) and nowhere else.  Consequently

\[
 Z_H=\mathcal B^+-\mathcal B^-
\tag{3.6}
\]

for two genuine equal-size owner matchings \(\mathcal B^+,\mathcal B^-\).

#### Proof

Choose a \((c+1)\)-set

\[
 P\subseteq S\subseteq[k]\setminus C
\tag{3.7}
\]

and choose \(z\notin C\cup S\).  This is possible by the first inequality
in (3.5).  Put

\[
 E=[k]\setminus(S\cup\{z\}),qquad |E|=N=M-2.
\tag{3.8}
\]

For \(u\in S\), choose a cyclic order \(\sigma\) of \(E\) and a gap in
which to insert \(z\).  Write \(\sigma^+\) for the resulting order on
\(E\cup\{z\}\), and define the **insertion potential**

\[
 \Phi_u(\sigma)
 =f(S\setminus\{u\},E\cup\{z\},\sigma^+)
  -f(S\setminus\{u\},E,\sigma).
\tag{3.9}
\]

Its point image is

\[
 P_R\Phi_u={\bf1}_{S\setminus\{u\}}+qe_z
           ={\bf1}_S-e_u+qe_z.
\tag{3.10}
\]

Hence any difference \(\Phi_x-\Phi_p\) has point image \(e_p-e_x\)
and is exactly a four-rail two-size role current, even when the two
insertion potentials use unrelated cyclic orders.

We need \(q-1\) copies of the state \(u=x\).  They may be chosen so that
their period-\(N\) decks are pairwise disjoint and their
period-\((N+1)\) decks are pairwise disjoint.  Indeed, after \(j<q-1\)
copies have been chosen, take a uniformly random cyclic order of \(E\)
and a uniformly random insertion gap.  The small order is uniform on
\(E\), and the enlarged order is uniform on \(E\cup\{z\}\).  The union
bound gives collision probability at most

\[
 \frac{jN^2}{\binom Nq}
 +\frac{j(N+1)^2}{\binom{N+1}q}<1
\tag{3.11}
\]

by (3.5).  Thus the greedy packing continues.  Denote the resulting
potentials by \(\Phi_x^{(p)}\), one for each
\(p\in P\setminus\{x\}\), and choose one arbitrary potential \(\Phi_p\)
for every such \(p\).  Put

\[
 K=\sum_{p\in P\setminus\{x\}}
       \bigl(\Phi_x^{(p)}-\Phi_p\bigr).
\tag{3.12}
\]

Equation (3.10) gives

\[
 P_RK=\sum_{p\in P\setminus\{x\}}(e_p-e_x).
\tag{3.13}
\]

It remains to check positivity.  Every owner in a \(u\)-potential contains
\(S\setminus\{u\}\) and omits \(u\).  If \(u\ne v\), every owner in a
\(v\)-potential contains \(u\), so the two owner shores are disjoint.
Thus different leaf potentials and every leaf/centre pair are automatically
disjoint.  The only repeated shore is \(u=x\), and its big decks and small
decks were packed separately above.  Therefore each sign of \(K\) is an
owner matching.

Every owner in \(\Delta_x\) contains \(C\), while every owner in \(K\)
contains one of the \(c\)-sets \(S\setminus\{u\}\).  These two cores are
disjoint, and \(2c>R\), so no rank-\(R\) owner can contain both.  Hence
the corresponding signs of \(\Delta_x\) and \(K\) are disjoint.  Taking
\(U_{p,x}=\Phi_x^{(p)}-\Phi_p\) proves the first assertion.

Finally, \(H\) is the designated owner \(P_0\) in \(\Delta_x\).  It
cannot occur in \(K\), because \(|H\cap S|=|P|=q<c\).  Since \(Y_H\)
has one more owner on its positive side and \(P_RY_H={\bf1}_H\), removing
this copy of \(H\) leaves two equal-size owner matchings whose point
incidences agree.  This is (3.6).  \(\square\)

## 4. Constructive point-kernel lifting

We record a support-conscious version of the point-kernel theorem.

### Lemma 4.1 (matrix switches followed by rail trades)

Let \(z\in\ker_{\mathbb Z}P_R\), and write

\[
 \|z\|_1=2s.
\]

Then \(z\) is a sum of at most

\[
 2sR(R-1)
\tag{4.1}
\]

adjacent-transposition rail currents.

#### Proof

Expand the positive and negative parts of \(z\) into \(s\) labelled owner
occurrences.  Regard each side as the incidence matrix of a bipartite graph
with \(s\) row vertices and \(k\) coordinate vertices.  Every row has
degree \(R\), and \(P_Rz=0\) says that the two matrices have the same
column degrees.

The standard alternating-cycle proof for bipartite degree sequences
transforms one matrix into the other through at most \(sR\) binary
\(2\times2\) switches.  Explicitly, the symmetric difference decomposes
into alternating cycles; resolving a chordless alternating cycle of length
\(2t\) uses at most \(t-1\) switches and shortens the symmetric difference.

One matrix switch replaces two rank-\(R\) rows

\[
 A,B
 \quad\hbox{by}\quad
 A-a+b,\ B-b+a,
\tag{4.2}
\]

where \(a\in A\setminus B\) and \(b\in B\setminus A\).  Its current is

\[
 \delta_{ab}(A-a)-\delta_{ab}(B-b).
\tag{4.3}
\]

In the exact-distance context graph from the full owner-lattice theorem,
each ordinary Johnson adjacency may be replaced by a two-edge
distance-\(d\) path.  Its diameter is therefore at most
\(2(R-1)\).  Telescoping (4.3) along such a path writes one matrix switch
as at most \(2(R-1)\) adjacent-transposition rail currents.  Multiplying
the two bounds gives (4.1).  \(\square\)

### Theorem 4.2 (polynomial-support signed one-owner macro)

For every named owner \(H\), there is an exact identity

\[
 \boxed{
 e_H=\Delta_x+
      \sum_{p\in P\setminus\{x\}}U_{p,x}
      +\sum_{j=1}^{t}T_j,}
\tag{4.4}
\]


where every \(T_j\) is an adjacent-transposition rail current and

\[
 t<4qMR(R-1).
\tag{4.5}
\]

Thus \(e_H\) is a signed sum of fewer than \(8qMR^2+4q+2\) legal closed
pure-rail component columns.  Every summand current in (4.4) is separately
a difference of two genuine owner matchings.

#### Proof

Apply Lemma 4.1 to \(Z_H\) in (3.4).  From (2.3),

\[
 \|\Delta_x\|_1=2q-1.
\]

A unit-role current is a difference of alternatives containing
\(2M-3\) owners each, so

\[
 \|U_{p,x}\|_1\le4M-6.
\]

Therefore

\[
 \|Z_H\|_1
 \le1+(2q-1)+(q-1)(4M-6)<4qM.
\tag{4.6}
\]

Writing \(\|Z_H\|_1=2s\), Lemma 4.1 gives

\[
 t\le2sR(R-1)<4qMR(R-1).
\]

The component-column count follows because an insertion or order current
uses two columns and each unit-role current uses four.  \(\square\)

No claim of optimality is made for the polynomial bound.  Its purpose is
to exclude a hidden requirement for exponentially supported signed
correction.

## 5. Protected supply for the insertion stage

The insertion packet itself has abundant copies even after a small owner
bank is protected.

### Proposition 5.1 (small forbidden-bank avoidance)

Fix \(H\), and choose the core \(C\) uniformly from
\(\binom Hc\).  For any other owner \(G\ne H\), the event that \(G\)
occurs anywhere in either the old or new insertion rail implies
\(C\subseteq G\), and hence has probability at most

\[
 \frac{\binom{R-1}c}{\binom Rc}
 =\frac{R-c}{R}=\frac qR.
\tag{5.1}
\]

Consequently, for every forbidden owner family \(\mathcal F\) with

\[
 |\mathcal F|<R/q,
\tag{5.2}
\]

there is a choice of \(C\) for which neither insertion rail meets
\(\mathcal F\).  Subject to that core, one may then choose \(x\in H-C\),
the exterior labels, and the local order as in Lemma 2.1.

#### Proof

Every owner of either rail contains its common core \(C\).  If it equals
\(G\), then \(C\subseteq H\cap G\).  Since \(G\ne H\),
\(|H\cap G|\le R-1\), giving (5.1).  A union bound over
\(\mathcal F\) proves (5.2).  \(\square\)

This supplies a protected first step for any fixed number of owner tasks.
It does not protect the entire polynomial list of correction currents in
Theorem 4.2.

## 6. Exact conformality gate

An **owner absorber for \(H\)** is a pair of component collections
\((\mathcal A^-,\mathcal A^+)\) such that

* the owner sets within each collection are pairwise disjoint; and
* their incidence vectors obey

  \[
  \sum_{Q\in\mathcal A^+}f(Q)
  -\sum_{Q\in\mathcal A^-}f(Q)=e_H.
  \tag{6.1}
  \]

Theorem 3.1 proves that the insertion and all point-correction role currents
already satisfy the first bullet jointly.  It leaves a difference
\(Z_H=\mathcal B^+-\mathcal B^-\) between two equal-size owner matchings
with identical point degrees.  Theorem 4.2 then proves (6.1) only after
dropping the first bullet for the point-kernel lift: its adjacent-order
currents may reuse an owner on one sign.  Algebraic cancellation says that
the final signed multiplicities agree; it does not bound either multiplicity
by one.

There is a genuine reason the role-changing stages cannot be omitted.
If every component on both sides has one fixed core \(C\), then every
toggle coordinate has degree divisible by \(q\) on each side, while a
single owner changes its \(q\) petal-coordinate degrees by one.  Thus no
single-owner absorber exists inside one fixed-core fibre when \(q>1\).
The insertion current escapes this obstruction through the additional
core-degree term in (2.4), and the two-size role macros remove the resulting
point imbalance.

The first positive theorem needed after the signed lattice is therefore:

> **Protected conformal point-kernel lemma.**  Any two sparse equal-size
> owner matchings with the same point-incidence vector, in particular the
> pair \(\mathcal B^+,\mathcal B^-\) of Theorem 3.1, can be connected by
> adjacent-order rail currents whose two aggregate signs remain owner
> matchings; moreover the two states retain the compulsory palette, upper,
> socket, and common-cap tickets.

If only owner matching is required, Theorem 3.1 closes the complete point
correction, while Proposition 5.1 supplies additional protection for its
first insertion stage.  The unresolved owner-level issue is conformal
composition of the \(O(qMR^2)\) *point-kernel* currents, not a remaining
lattice, point-moment, or support-size obstruction.

## 7. The minimal two-size role gadget has unavoidable linear collateral

The positive unit-role gadget cannot itself be retuned into a one-owner
replacement.  This is an exact positive obstruction, not a failure of the
particular coupled orders used in its construction.

### Lemma 7.1 (one-toggle deck-intersection bound)

Let \(E\) have size \(N\), let \(z\notin E\), and give \(E\) and
\(E\cup\{z\}\) arbitrary, unrelated cyclic orders.  Their cyclic
\(q\)-window families obey

\[
 \left|
 \mathcal I_q(E)\cap\mathcal I_q(E\cup\{z\})
 \right|
 \le N+1-q.
\tag{7.1}
\]

Consequently the larger deck has at least \(q\) values absent from the
smaller deck, and the smaller deck has at least \(q-1\) values absent from
the larger deck.  Both bounds are attained by inserting \(z\) into an
order of \(E\).

#### Proof

The period-\((N+1)\) cyclic order has exactly \(q\) cyclic
\(q\)-windows containing \(z\).  Hence only \(N+1-q\) of its windows are
subsets of \(E\), and only those can occur in the period-\(N\) deck.  This
proves (7.1).  Subtracting the bound from the two deck sizes gives \(q\)
and \(q-1\), respectively.  If the smaller order is obtained by deleting
\(z\) from the larger one, precisely the \(q-1\) old windows crossing the
deletion cut change, so equality holds.  \(\square\)

### Theorem 7.2 (sharp collateral floor for the four-rail unit macro)

Take the two-size role pattern of the positive unit-residue gadget, but
allow all four cyclic orders to be chosen independently.  Thus one
signature shore has a period-\((N+1)\) rail in the positive state and a
period-\(N\) rail in the negative state, while the other signature shore
has the reverse assignment.  Then the named-owner current has at least

\[
 2q-1
\tag{7.2}
\]

positive-only owners and at least \(2q-1\) negative-only owners.  Equivalently,
its named-owner \(\ell_1\)-norm is at least \(4q-2\).

The coupled insertion orders used in the positive two-size theorem attain
this lower bound exactly.

#### Proof

The two signature shores are disjoint: every owner in one contains the
first role coordinate and omits the second, and every owner in the other
has the opposite signature.  Apply Lemma 7.1 in the first shore.  It
contributes at least \(q\) large-only owners and \(q-1\) small-only owners.
The roles of the two states are reversed in the second shore, which
contributes at least \(q-1\) positive-only and \(q\) negative-only owners.
No cross-shore cancellation is possible.  Adding the two bounds proves
(7.2).  Equality follows from the equality case of Lemma 7.1 in both
shores.  \(\square\)

In particular, for \(q>1\) no four-rail gadget with this role pattern has
named current \(e_A-e_B\), even though its point-incidence current can be
the unit vector \(e_x-e_y\).  A positive single-owner absorber must couple
several role gadgets through their collateral owners, introduce additional
periods, or serialize them through a larger reserve.  The first obstruction
after lattice saturation is therefore already visible at the named-owner
semigroup level: point-unit positivity does not imply bounded named support.

## 8. Generic two-switch serialization is false

There is a second exact boundary on the remaining point-kernel step.  An
adjacent-order current replaces two owners by two owners with the same point
degrees.  If it is applied serially while the owner set remains simple, it
is a \(2\)-switch in the standard uniform-hypergraph terminology.

Behrens--Erbes--Ferrara--Hartke--Reiniger--Spinoza--Tomlinson prove the
following sharp obstruction: for every uniformity \(r\ge3\), there is a
degree sequence with two simple \(r\)-uniform realizations such that neither
realization admits an \(i\)-switch for any \(i<r\).  At the same time, if
temporary multiplicities are allowed, arbitrary realizations with the same
degree sequence are connected by \(2\)-**exchanges**.  See *New Results on
Degree Sequences of Uniform Hypergraphs*, Electron. J. Combin. 20(4)
(2013), P14, DOI 10.37236/3414.

Therefore Lemma 4.1 has exactly the strength its wording claims.  It gives a
signed \(2\)-exchange decomposition, but it cannot be upgraded by a generic
argument to a path through simple owner matchings.  More quantitatively,
there is no universal conformal Markov basis of support bounded independently
of \(R\) for all simple rank-\(R\) degree fibres: in the worst case a
nontrivial move needs at least \(R\) owners on a side.

This does not refute the structured residual pair
\(\mathcal B^+,\mathcal B^-\) produced by Theorem 3.1.  It proves that the
next positive theorem must use that structure, a simultaneous compound rail
trade, or an auxiliary reserve.  Plain duplicate-avoiding serialization of
the matrix switches in Lemma 4.1 is not a valid general route.
