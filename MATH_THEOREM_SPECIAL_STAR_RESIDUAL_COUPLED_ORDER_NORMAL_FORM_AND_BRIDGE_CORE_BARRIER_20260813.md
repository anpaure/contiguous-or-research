# The special point-correction star is an exact closed-rail row swap; its only nonfactorable defect is the designated puncture

**Date:** 2026-08-13  
**Input:** `MATH_THEOREM_PURE_RAIL_ONE_OWNER_SIGNED_MACRO_AND_CONFORMAL_ABSORBER_GATE_20260812.md`  
**Status:** unconditional structural theorem for the special residual produced
by Theorem 3.1 of that note.  It gives a coupled-order normal form, an exact
common-reserve ledger, and two positive barriers.  It does **not** construct
the required overlapping-core reserve.

## 1. Setup

Put

\[
 q=d+1,\qquad c=R-q,\qquad N=M-2,
\tag{1.1}
\]

and assume the hypotheses of the point-correction-star theorem.  Thus

\[
 H=C\mathbin{\dot\cup}\Pi,\qquad |C|=c,\quad |\Pi|=q,
 \quad x\in\Pi,
\tag{1.2}
\]

and there is a set (S), disjoint from (C), such that

\[
 \Pi\subset S,\qquad |S|=c+1.
\tag{1.3}
\]

Choose (z\notin C\cup S), and put

\[
 E=[k]\setminus(S\cup\{z\}),\qquad |E|=N.
\tag{1.4}
\]

For (u\in S) and a family \(\mathcal D\subseteq\binom{E\cup\{z\}}q\),
write

\[
 [u,\mathcal D]
 :=\{(S\setminus\{u\})\cup J:J\in\mathcal D\}.
\tag{1.5}
\]

The row label (u) records the unique point of (S) omitted by every
owner in the family.

Let

\[
 L=\Pi\setminus\{x\},\qquad |L|=q-1.
\tag{1.6}
\]

For every (p\in L), choose one cyclic order \(\sigma_p\) of (E) and
one insertion gap for (z).  Write

\[
 \mathcal D_p^0=\mathcal I_q(\sigma_p),\qquad
 \mathcal D_p^1=\mathcal I_q(\sigma_p^z).
\tag{1.7}
\]

The centre orders can be chosen, exactly as in Theorem 3.1, so that the
families \(\mathcal D_p^0\) are pairwise disjoint and the families
\(\mathcal D_p^1\) are pairwise disjoint.  Use the **same** order and gap
for the leaf potential (p) as for its corresponding centre potential
(x).  This coupling costs no extra avoidance: different leaf rows, and
every leaf/centre pair, are separated by their omitted-(S) signatures.

## 2. Coupled-order row-swap normal form

Define two component collections

\[
\begin{aligned}
 \mathcal K^+
 &=\bigsqcup_{p\in L}
   \bigl([x,\mathcal D_p^1]\sqcup[p,\mathcal D_p^0]\bigr),\\
 \mathcal K^-
 &=\bigsqcup_{p\in L}
   \bigl([x,\mathcal D_p^0]\sqcup[p,\mathcal D_p^1]\bigr).
\end{aligned}
\tag{2.1}
\]

Each bracketed family is the complete owner deck of one legal closed pure
rail.  The displayed unions are owner matchings.

### Theorem 2.1 (the star is a deck-preserving row swap)

The point-correction current (K) of Theorem 3.1 may be chosen so that

\[
 \boxed{K={\bf1}_{\mathcal K^+}-{\bf1}_{\mathcal K^-}.}
\tag{2.2}
\]

After forgetting the row label (u), the two states have exactly the same
toggle-deck multiset:

\[
 \bigl\{\mathcal D_p^0,\mathcal D_p^1:p\in L\bigr\}.
\tag{2.3}
\]

The move merely exchanges \(\mathcal D_p^0\) and
\(\mathcal D_p^1\) between rows (x) and (p), independently for every
(p\in L).  Moreover

\[
 P_RK=\sum_{p\in L}(e_p-e_x).
\tag{2.4}
\]

#### Proof

With the coupled order,

\[
 \Phi_x^{(p)}=[x,\mathcal D_p^1]-[x,\mathcal D_p^0],
 \qquad
 \Phi_p=[p,\mathcal D_p^1]-[p,\mathcal D_p^0].
\]

Substitution in

\[
 K=\sum_{p\in L}(\Phi_x^{(p)}-\Phi_p)
\]

gives (2.1)--(2.2).  For (p\ne p'), every owner in row (p)
contains (p') and omits (p), while every owner in row (p') has the
opposite signature.  A centre owner omits (x) and contains every leaf,
whereas a leaf owner contains (x) and omits that leaf.  Hence the only
possible same-state collision is between two centre decks.  Those were
chosen pairwise disjoint separately in state zero and state one.  This
proves the matching assertion.  Equation (2.3) is immediate, and (2.4)
is the insertion-potential point ledger. \(\square\)

Thus the special star is much more rigid than a general pair of equal
degree hypergraphs: it is a transportation-fibre trade in which the
column objects are whole cyclic decks and only their omitted-core rows
change.

## 3. The exact reduced reserve

For every (p\in L), put

\[
 \mathcal G_p=\mathcal D_p^0\cap\mathcal D_p^1,
 \quad
 \mathcal A_p=\mathcal D_p^1\setminus\mathcal D_p^0,
 \quad
 \mathcal B_p=\mathcal D_p^0\setminus\mathcal D_p^1.
\tag{3.1}
\]

The insertion identity gives

\[
 |\mathcal G_p|=N-q+1,\qquad
 |\mathcal A_p|=q,\qquad
 |\mathcal B_p|=q-1.
\tag{3.2}
\]

Every member of \(\mathcal A_p\) contains (z), while no member of
\(\mathcal B_p\) contains (z).

Choose the original insertion current \(\Delta_x\) with old period (N).
Write its two full rail decks as \(\mathcal Q^+\) and
\(\mathcal Q^-\), where \(|\mathcal Q^+|=N+1\),
\(|\mathcal Q^-|=N\), and (H\in\mathcal Q^+\).  Put

\[
 \mathcal G_\Delta=\mathcal Q^+\cap\mathcal Q^-,\quad
 \mathcal A_\Delta=\mathcal Q^+\setminus\mathcal Q^-,\quad
 \mathcal B_\Delta=\mathcal Q^-\setminus\mathcal Q^+.
\tag{3.3}
\]

Then

\[
 |\mathcal G_\Delta|=N-q+1,\quad
 |\mathcal A_\Delta|=q,\quad
 |\mathcal B_\Delta|=q-1,\quad H\in\mathcal A_\Delta.
\tag{3.4}
\]

The full two states of the conformal point-correction macro are

\[
 \mathcal Y^+=\mathcal Q^+\sqcup\mathcal K^+,\qquad
 \mathcal Y^-=\mathcal Q^-\sqcup\mathcal K^-.
\tag{3.5}
\]

They are closed-rail packings, (H) occurs only in \(\mathcal Y^+\), and

\[
 P_R({\bf1}_{\mathcal Y^+}-{\bf1}_{\mathcal Y^-})={\bf1}_H.
\tag{3.6}
\]

The residual pair in Theorem 3.1 is therefore exactly

\[
 \boxed{
 \mathcal B^+=\mathcal Y^-,\qquad
 \mathcal B^-=\mathcal Y^+\setminus\{H\}.}
\tag{3.7}
\]

In particular, \(\mathcal B^+\) is already a union of closed rails, while
\(\mathcal B^-\) is a union of closed rails with exactly one named owner
deleted.

For the cancellation-reduced form, define

\[
 \mathcal R=
 \mathcal G_\Delta\sqcup
 \bigsqcup_{p\in L}
 \bigl([x,\mathcal G_p]\sqcup[p,\mathcal G_p]\bigr),
\tag{3.8}
\]

and

\[
\begin{aligned}
 \widehat{\mathcal B}^+
 &=\mathcal B_\Delta\sqcup
   \bigsqcup_{p\in L}
   \bigl([x,\mathcal B_p]\sqcup[p,\mathcal A_p]\bigr),\\
 \widehat{\mathcal B}^-
 &=(\mathcal A_\Delta\setminus\{H\})\sqcup
   \bigsqcup_{p\in L}
   \bigl([x,\mathcal A_p]\sqcup[p,\mathcal B_p]\bigr).
\end{aligned}
\tag{3.9}
\]

### Theorem 3.1 (punctured common-reserve identity)

All families in (3.8)--(3.9) are owner matchings, and

\[
\boxed{
\begin{aligned}
 \mathcal R\sqcup\widehat{\mathcal B}^+&=\mathcal Y^-,\\
 \mathcal R\sqcup\widehat{\mathcal B}^-\sqcup\{H\}&=\mathcal Y^+.
\end{aligned}}
\tag{3.10}
\]

Their exact sizes are

\[
 \boxed{
 |\mathcal R|=(2q-1)(N-q+1),\qquad
 |\widehat{\mathcal B}^+|
 =|\widehat{\mathcal B}^-|=2q(q-1).}
\tag{3.11}
\]

#### Proof

Equations (3.10) follow by splitting every insertion pair into its common,
new-only, and old-only decks.  The centre common families are pairwise
disjoint because each is contained in both a state-zero centre deck and a
state-one centre deck, and those decks are pairwise disjoint within their
respective states.  All other disjointness follows from the row signatures
and the (C)-core/star-core separation already used in Theorem 3.1 of the
input note.  Finally,

\[
 (q-1)+(q-1)(q+(q-1))=2q(q-1),
\]

and there are (1+2(q-1)=2q-1) common insertion decks, proving (3.11).
\(\square\)

This is the strongest literal telescoping available from merely coupling
the cyclic orders: all common decks factor out exactly, but the designated
owner remains as one puncture.  Nothing is lost in an abstract
point-kernel reduction.

### Corollary 3.2 (the owner gate reduces to one insertion puncture)

Suppose there is an owner reserve \(\mathcal R_0\), disjoint from both star
states, such that each of

\[
 \mathcal R_0\sqcup\mathcal Q^-,
 \qquad
 \mathcal R_0\sqcup(\mathcal Q^+\setminus\{H\})
\tag{3.12}
\]

admits a closed-pure-rail factorization.  Then the complete special
residual pair \(\mathcal B^+,\mathcal B^-\) admits a common-reserve
closed-rail factorization.

#### Proof

Append the already-factorized star state \(\mathcal K^-\) to the first
factorization in (3.12), and append \(\mathcal K^+\) to the second.  By
(3.7), the resulting owner sets are respectively
\(\mathcal R_0\sqcup\mathcal B^+\) and
\(\mathcal R_0\sqcup\mathcal B^-\). \(\square\)

Thus one sufficient positive theorem is universal and one-row:
absorb the difference between an old period-\(N\) rail and a
period-\((N+1)\) rail with one designated new-only owner removed.  The
star is already positively closed and need not participate in that
absorber.  The later context-flow formulation records the more flexible
alternative in which the star does participate and supplies the
point-balanced return commodities.

## 4. A rigid (z)-layer prevents total star telescoping

Let

\[
 \mathscr Z_x=
 \{A\in\tbinom{[k]}R:A\cap S=S\setminus\{x\},\ z\in A\}.
\tag{4.1}
\]

### Proposition 4.1 (uncancellable centre (z)-layer)

For every conformal choice of the (q-1) centre potentials,

\[
 \left.K\right|_{\mathscr Z_x}
\]

is the positive sum of exactly (q(q-1)) distinct owners.  In particular,
no coupling of the cyclic orders can telescope the complete star current
to (O(q)), let alone bounded, named support.

#### Proof

Every enlarged centre rail has exactly (q) owner windows containing
(z), while no small centre rail contains (z).  The enlarged centre
decks are pairwise disjoint because the positive centre shore is an owner
matching.  Leaf rows have a different omitted-(S) signature and therefore
do not meet \(\mathscr Z_x\).  Hence all (q(q-1)) owners survive with
positive sign. \(\square\)

There is a symmetric negative (z)-layer of the same size on the leaf
rows.  Thus the common-reserve identity (3.10), rather than cancellation
of the entire star, is the correct positive normal form.

## 5. The punctured shore is not itself rail-factorable

For a (c)-set (D), write

\[
 \mathscr F_D=\{A\in\tbinom{[k]}R:D\subseteq A\}.
\tag{5.1}
\]

All owners of the original insertion rail lie in \(\mathscr F_C\).  All
star owners lie in

\[
 \mathscr F_S=\bigcup_{u\in\{x\}\cup L}\mathscr F_{S\setminus\{u\}}.
\tag{5.2}
\]

### Lemma 5.1 (sector separation)

If (c>q), then \(\mathscr F_C\cap\mathscr F_S=\varnothing\).  If
(c>2q), an owner in \(\mathscr F_C\) and an owner in
\(\mathscr F_S\) have intersection smaller than (c).

#### Proof

The cores (C) and (S\setminus\{u\}) are disjoint and both have size
(c).  An (R=c+q) set cannot contain both when (c>q).  More generally,
if

\[
 A=C\cup I,\qquad B=(S\setminus\{u\})\cup J,\qquad |I|=|J|=q,
\]

then every point of (A\cap B) is supplied by one of the two (q)-sets
(I,J), so \(|A\cap B|\le2q<c\). \(\square\)

### Theorem 5.2 (direct refactorization no-go)

Assume (c>2q).  The punctured residual shore \(\mathcal B^-\) in (3.7)
cannot be partitioned into legal closed pure rails, even if arbitrary new
cores and cyclic orders are allowed.

#### Proof

Every two owners in one pure rail share its (c)-set core.  Lemma 5.1
therefore says that no rail in a hypothetical factorization can mix the
(C)-sector and the star sector.

Consider a rail lying wholly in the (C)-sector.  The intersection of all
owners of a legal period-(n) pure rail is exactly its core: the intersection
of all cyclic (q)-windows is empty because (n\ge2(q+1)>q).  Since all
its owners contain (C), its core contains (C), and equality of their
sizes forces its core to be (C).

Hence the (C)-sector

\[
 \mathcal Q^+\setminus\{H\}
\tag{5.3}
\]

would have to be a union of (C)-core rails.  In any union of (C)-core
rails, every point outside (C) has degree divisible by (q).  In
\(\mathcal Q^+\), every toggle point has degree (q).  Removing (H)
changes the degree of each (p\in H\setminus C=\Pi) to (q-1), a
contradiction modulo (q). \(\square\)

Thus the one puncture in (3.10) is not a notational nuisance.  A genuine
auxiliary reserve is necessary.

## 6. Natural cores cannot support the reserve

Let

\[
 \mathfrak C_{\rm nat}
 =\{C\}\cup\{S\setminus\{u\}:u\in\{x\}\cup L\}.
\tag{6.1}
\]

### Theorem 6.1 (natural-core common-reserve barrier)

Assume (c>q).  There is no signed closed-rail representation

\[
 {\bf1}_{\widehat{\mathcal B}^+}
 -{\bf1}_{\widehat{\mathcal B}^-}
 =\sum_i f(Q_i^+)-\sum_jf(Q_j^-)
\tag{6.2}
\]

in which every component core belongs to \(\mathfrak C_{\rm nat}\).
Consequently, no common-reserve factorization of the reduced pair using
only the original insertion core and the star cores can exist.

#### Proof

Restrict (6.2) to the owner sector \(\mathscr F_C\).  By Lemma 5.1, a
rail with a star core contributes no owner there.  A rail with core (C)
has, outside (C), point degrees divisible by (q).  Therefore the point
projection of the restricted right side is coordinatewise divisible by
(q) outside (C).

The restricted left side is the insertion residual

\[
 {\bf1}_{\mathcal B_\Delta}
 -{\bf1}_{\mathcal A_\Delta\setminus\{H\}}
 =e_H-\Delta_x.
\tag{6.3}
\]

Its point image is

\[
 P_R(e_H-\Delta_x)
 =\sum_{p\in\Pi\setminus\{x\}}e_p-(q-1)e_x.
\tag{6.4}
\]

Every coordinate in \(\Pi\) is congruent to (1\pmod q), contradicting
the divisibility of the right side. \(\square\)

The theorem is stronger than the one-fixed-core obstruction: adjoining
all (q) natural star cores still cannot repair the designated puncture.
At least one genuinely overlapping, nonnatural core is forced.

## 7. The bridge must have growing core depth

For (c)-sets (D,D'), let

\[
 \operatorname{dist}(D,D')=c-|D\cap D'|
\tag{7.1}
\]

be Johnson distance.

### Lemma 7.1 (support-overlap metric)

\[
 \boxed{
 \mathscr F_D\cap\mathscr F_{D'}\ne\varnothing
 \quad\Longleftrightarrow\quad
 \operatorname{dist}(D,D')\le q.}
\tag{7.2}
\]

#### Proof

A rank-(R=c+q) owner contains both cores exactly when

\[
 |D\cup D'|=c+\operatorname{dist}(D,D')\le c+q.
\]

This is (7.2). \(\square\)

### Corollary 7.2 (core-depth lower bound)

Any chain of rail supports linking the original core (C) to a star core
(S\setminus\{u\}), where consecutive supports share an owner, has at
least

\[
 \boxed{\left\lceil\frac cq\right\rceil}
\tag{7.3}
\]

overlap steps.

#### Proof

The endpoint cores are disjoint, so their Johnson distance is (c).
Each overlap step changes core distance by at most (q), by Lemma 7.1.
The triangle inequality gives (7.3). \(\square\)

For the central parameters, (c/q\to\infty).  Hence a successful positive
absorber cannot be a bounded-depth interaction among the natural rail
cores.  It must use a growing overlapping-core bridge, a compound reserve
whose cancellation graph is not confined to the natural sectors, or a
different global factorization which never isolates this puncture.

## 8. Exact remaining target

The special residual is now reduced to the following positive problem.

> **Overlapping-core puncture absorber.**  Starting from the two literal
> closed-rail packings \(\mathcal Y^-\) and \(\mathcal Y^+\), refactor
> \(\mathcal Y^+\setminus\{H\}\) after adjoining one common owner reserve,
> while keeping both aggregate owner shores simple.  The reserve must use
> at least one nonnatural core; any literal support-overlap route from the
> insertion sector to a star sector has depth at least \(\lceil c/q\rceil\).

No cyclic-order choice inside the existing star can remove that gate: the
star already has the exact row-swap form (2.1), its common part has already
been extracted in (3.10), and Proposition 4.1 leaves a rigid quadratic
(z)-layer.  The remaining theorem is genuinely an overlapping-core
positive-semigroup theorem, not another signed-lattice or order-coupling
calculation.

## 9. Exact coordinate-pair context-flow normal form

The residual admits a finer decomposition which is absent for a generic
equal-degree pair.

For distinct \(x,p\) and an \((R-1)\)-set \(A\) avoiding them, put

\[
 \delta_{xp}(A)=e_{A\cup\{x\}}-e_{A\cup\{p\}}.
\tag{9.1}
\]

Choose the insertion order for \(\Delta_x\) so that \(H\) is an endpoint
of the path of \(q\) new-only owners.  Order the other petals as
\(\Pi\setminus\{x\}=\{p_1,\ldots,p_{q-1}\}\).  The \(q-1\) old-only
owners and the \(q-1\) non-\(H\) new-only owners can then be paired as

\[
 O_p=A_p^\Delta\cup\{p\},\qquad
 P_p=A_p^\Delta\cup\{x\},
\tag{9.2}
\]

one pair for every \(p\in L\).  Here \(A_p^\Delta\) is an
\((R-1)\)-context avoiding \(x,p\).  Hence

\[
 e_H-\Delta_x=-\sum_{p\in L}\delta_{xp}(A_p^\Delta).
\tag{9.3}
\]

For \(J\in\binom{E\cup\{z\}}q\), define the star context

\[
 B_{p,J}=(S\setminus\{x,p\})\cup J.
\tag{9.4}
\]

Then

\[
 \delta_{xp}(B_{p,J})
 =e_{[p,\{J\}]}-e_{[x,\{J\}]}.
\tag{9.5}
\]

After cancelling \(\mathcal G_p\), the \(p\)-th row swap is therefore

\[
 K_p=
 \sum_{J\in\mathcal B_p}\delta_{xp}(B_{p,J})
 -
 \sum_{J\in\mathcal A_p}\delta_{xp}(B_{p,J}).
\tag{9.6}
\]

Put

\[
\begin{aligned}
 \mathcal U_p&=\{B_{p,J}:J\in\mathcal A_p\},\\
 \mathcal V_p&=\{A_p^\Delta\}
 \cup\{B_{p,J}:J\in\mathcal B_p\}.
\end{aligned}
\tag{9.7}
\]

Both families have size \(q\).

### Theorem 9.1 (balanced multicommodity context form)

The complete special residual decomposes as

\[
 \boxed{
 Z_H=e_H-\Delta_x-K
 =\sum_{p\in L}
 \left(
 \sum_{U\in\mathcal U_p}\delta_{xp}(U)
 -
 \sum_{V\in\mathcal V_p}\delta_{xp}(V)
 \right).}
\tag{9.8}
\]

Each summand indexed by \(p\) separately has zero point image: it contains
exactly \(q\) positive and \(q\) negative contexts for the same coordinate
pair \(x,p\).

#### Proof

Equation (9.3) is the endpoint insertion ledger.  Equation (9.6) follows
from (2.1): on a fixed toggle set \(J\), row \(p\) contains \(x\), row
\(x\) contains \(p\), and their common context is (9.4).  Substitute
(9.3) and (9.6) in \(Z_H=e_H-\Delta_x-\sum_pK_p\).  This gives (9.8).
Since \(P_R\delta_{xp}(A)=e_x-e_p\), the equal context counts make every
\(p\)-summand point-zero. \(\square\)

Thus the special pair does not require a generic degree-sequence
transformation.  It requires \(q-1\) labelled transportation linkages,
each routing \(q\) source contexts to \(q\) sink contexts in one explicit
exact-distance context graph.

### Proposition 9.2 (exact compound-path lifting criterion)

For fixed \(p\), let \(G_{xp}\) have vertex set

\[
 \binom{[k]\setminus\{x,p\}}{R-1}
\]

and join \(A,B\) when \(|A\cap B|=c\).  Suppose that:

1. \(\mathcal U_p\) can be linked bijectively to \(\mathcal V_p\) by
   pairwise vertex-disjoint paths in \(G_{xp}\), for every \(p\in L\);
2. across different \(p\), the lifted owner pairs
   \(A\cup\{x\},A\cup\{p\}\) are occurrence-disjoint on each aggregate
   shore; and
3. the adjacent-transposition rails realizing all path edges can be
   chosen with mutually disjoint common decks, disjoint also from every
   lifted endpoint/internal owner outside their own edge and from the
   protected exterior.

Then \(Z_H\) has an owner-conformal closed-rail representation.  Equivalently,
the special pair \(\mathcal B^+,\mathcal B^-\) has a literal common-reserve
closed-rail factorization.

#### Proof

For an edge \(A B\) of \(G_{xp}\), the restricted carousel identity gives
one adjacent-transposition current

\[
 \delta_{xp}(A)-\delta_{xp}(B).
\tag{9.9}
\]

Sum (9.9) along an oriented path from \(U\) to \(V\).  All internal
\(\delta\)-contexts telescope, leaving
\(\delta_{xp}(U)-\delta_{xp}(V)\).  More importantly, in the two positive
component collections, each internal context contributes its \(x\)-owner
and \(p\)-owner once on each shore; it is therefore a literal common-reserve
pair, not merely an algebraic cancellation.  Conditions 1--3 make the
aggregate shores owner matchings.  Sum over the bijections and then over
\(p\), and apply (9.8). \(\square\)

This criterion isolates the remaining positive theorem as a protected
multicommodity linkage plus common-deck packing problem.  It avoids the
false generic claim that arbitrary simple uniform-hypergraph realizations
are serially connected by \(2\)-switches: the intermediate contexts here
are installed simultaneously as a common reserve.

### Proposition 9.3 (the disjoint-core construction forces long routes)

For every \(p\in L\), every insertion context \(A_p^\Delta\) and every
star context \(B_{p,J}\) obey

\[
 |A_p^\Delta\cap B_{p,J}|\le2q-1.
\tag{9.10}
\]

Consequently, any path in \(G_{xp}\) from a member of \(\mathcal U_p\)
to the distinguished sink \(A_p^\Delta\in\mathcal V_p\) has length at
least

\[
 \boxed{
 \left\lceil\frac{c-q}{q-1}\right\rceil.}
\tag{9.11}
\]

#### Proof

The delta context consists of \(C\) and \(q-1\) further points.  The star
context consists of the disjoint \((c-1)\)-set
\(S\setminus\{x,p\}\) and \(q\) further points.  Any common point is
supplied by one of the two small exterior parts, giving (9.10).

Both contexts have size \(R-1=c+q-1\), so their Johnson distance is at
least \(c-q\).  Every edge of \(G_{xp}\) changes exactly

\[
 (R-1)-c=q-1
\]

points.  The triangle inequality gives (9.11). \(\square\)

Therefore even the specially balanced context flow cannot be closed by a
bounded number of local switches when \(c/q\to\infty\).  The correct next
positive statement is a **growing, protected, vertex-disjoint linkage
theorem** for the \(q(q-1)\) context demands, together with simultaneous
avoidance of the full rail common decks.  This is substantially narrower
than arbitrary point-kernel conformalization and preserves the exact
special structure of \(\mathcal B^\pm\).

## 10. The context linkage itself is asymptotically automatic

Only the full-rail common decks, not the abstract context paths, remain a
serious obstruction.  We first record a robust diameter lemma.

Let \(J_d(n,r)\) be the graph on \(\binom{[n]}r\) in which two vertices
are adjacent when their Johnson distance is exactly \(d\).

### Lemma 10.1 (short paths avoiding a polynomial forbidden bank)

Assume

\[
 r\ge3d,\qquad n-r\ge d+2.
\tag{10.1}
\]

Let \(A,B\in\binom{[n]}r\), and let \(\mathcal F\) be a forbidden vertex
family avoiding \(A,B\).  If

\[
 |\mathcal F|+\frac rd+3<2^{d/2},
\tag{10.2}
\]

then \(J_d(n,r)-\mathcal F\) contains an \(A\)-to-\(B\) path of length at
most

\[
 \left\lceil\frac{\operatorname{dist}(A,B)}d\right\rceil+1.
\tag{10.3}
\]

#### Proof

Put \(t=\operatorname{dist}(A,B)\).  While \(t>2d\), choose \(d\) points
of \(A\setminus B\) and \(d\) points of \(B\setminus A\), and exchange
them.  This gives an adjacent vertex whose distance to \(B\) is \(t-d\).
There are

\[
 \binom td^2\ge\binom{2d+1}d^2>2^{d}
\tag{10.4}
\]

such choices, so one avoids the current forbidden family.  Add the chosen
vertex to that family and continue.

It remains to handle \(0<t\le2d\).  If \(t=d\), use the edge \(AB\).
If \(t<d\), write

\[
 I=A\cap B,\quad X=A\setminus B,\quad Y=B\setminus A.
\]

Choose a common neighbour \(Z\) by taking all \(t\) points from each of
\(X,Y\), omitting \(d\) points from \(I\), and adding \(d-t\) points
outside \(A\cup B\).  The number of choices is at least

\[
 \binom{r-t}{d}\binom{n-r-t}{d-t}\ge2^d.
\tag{10.5}
\]

The last inequality uses (10.1).  If \(d<t\le2d\), take \(d\) points
from each of \(X,Y\), no outside points, and \(r-2d\) points from \(I\).
The number of resulting common neighbours is

\[
 \binom td^2\binom{r-t}{r-2d}.
\tag{10.6}
\]

Writing \(t=d+u\), either \(u\ge d/2\), in which case the first factor
in (10.6) is at least \(2^{d/2}\), or \(u<d/2\), in which case

\[
 \binom{r-t}{r-2d}
 =\binom{r-d-u}{d-u}\ge2^{d/2}
\]

by \(r\ge3d\).  Thus a common neighbour outside the current forbidden
family exists in every case.  The construction uses at most one edge per
full \(d\)-step and two edges at the end, giving (10.3); the allowance
in (10.2) covers the vertices added during the construction. \(\square\)

The crude powers of two are inessential.  What matters is the exponential
choice at every stage versus a polynomial forbidden bank.

### Theorem 10.2 (all special context commodities admit owner-separated linkages)

For the central parameters and all sufficiently large \(k\), conditions
1 and 2 of Proposition 9.2 can always be satisfied.  More explicitly,
all \(q(q-1)\) source-to-sink demands in (9.8) have context paths such
that:

* paths for one coordinate pair \(x,p\) are vertex-disjoint;
* every internal lifted owner \(A\cup\{x\}\) or \(A\cup\{p\}\) is distinct
  from every lifted owner already used by another path; and
* every path has \(O(R/q)\) edges.

#### Proof

For \(G_{xp}\), take

\[
 n=k-2,\qquad r=R-1,\qquad d=q-1.
\tag{10.7}
\]

The standing parameter inequalities give

\[
 n-r=k-R-1\ge d+2,
\]

and \(c>2q\) gives \(r=c+d\ge3d\).

Route the demands one at a time.  Before routing a demand, forbid every
context already used by a path, every other reserved terminal context,
every context whose \(x\)- or \(p\)-lift equals a reserved terminal owner,
and every context whose lift equals a lifted owner used earlier.  The
endpoint residual is an owner matching, so the two endpoints of the
current demand survive these prohibitions.  A fixed rank-\(R\) owner
determines at most one such context for the pair \(x,p\).  Hence the
forbidden count is linear in the number of reserved terminals, previously
used contexts, and previously used owners.

There are \(q(q-1)\) demands.  By Lemma 10.1, each path uses at most
\(O(R/q)\) contexts, so throughout the construction the forbidden count
is

\[
 O(q^2R/q)=O(qR).
\tag{10.8}
\]

For the central deadline, \(q=\Theta(\sqrt{k})\) and \(R=\Theta(k)\);
therefore (10.8) is polynomial in \(q\), while
\(2^{(q-1)/2}\) is exponential.  Condition (10.2) holds for all
sufficiently large \(k\).  Sequential application of Lemma 10.1 proves
the theorem. \(\square\)

Combining Theorem 10.2 with Proposition 9.2 leaves one exact owner-level
row:

> **Protected common-deck packing.**  Realize the edges of the linked
> exact-distance context paths by adjacent-transposition rails so that all
> unchanged carousel owners form a simple common reserve and avoid the
> compulsory exterior.

The generic context connectivity and the occurrence-level endpoint
collisions are no longer part of that row.  A proof may plant these
component decks prospectively before completing the exterior factor, or
must establish a sufficiently strong safe-order avoidance theorem if the
exterior is fixed first.
