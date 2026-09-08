# Clean and folded incidence-cycle banks under the sparse-edit moment

Date: 2026-07-26

Method: pure mathematics only.

## 0. Outcome

Put

\[
 B=C_s=\operatorname {Cat}_s,\qquad n=2s+1,\qquad W_s=nB,
\]

and let \(F,G\) be anchored exact \(D_s\)-port factors.  The sparse-edit
moment is

\[
 \Xi(F,G)={1\over B}\sum_K b_K\sum_{P\in R_K}d(P),       \tag{0.1}
\]

where \(K\) runs over the full state-and-colour ownership components,
\(b_K=|R_K|\), and \(d(P)\) is the anchored adjacent-transposition
distance between the two cyclic coordinate words at root \(P\).

There are four conclusions.

1. A single clean \(C_6\) or folded \(C_6\) is not an admissible pair for
   (0.1).  Its endpoint monodromy is respectively a three-cycle or a
   transposition.  It must first be closed by a literal internal serial
   packet.  Formal repetition in independent fixed-exterior holes does
   not do this.
2. A disjoint internally closed clean \(C_6\) packet is one three-root
   full \(X/Y\) component.  A closed folded packet is one two-root
   component.  Consequently, if \({\cal A}\) is the set of genuinely
   changed roots, then exactly
   \[
      \Xi_{C_6}={3\over B}\sum_{P\in{\cal A}}d(P),
      \qquad
      \Xi_{C_6^{\rm fold}}={2\over B}\sum_{P\in{\cal A}}d(P).       \tag{0.2}
   \]
3. The audited one-depth MWB plateau demand is \(\kappa B\), where
   \[
          \kappa={1\over2}-{1\over\theta}\ge {1\over4},
          \qquad \theta=B/p\ge4.                     \tag{0.3}
   \]
   Since one row has only one first-insertion carrier, a bank meeting this
   demand must change at least \(\kappa B\) rows.  Thus (0.2) gives only
   \[
       \Xi_{C_6}\ge3\kappa\ge{3\over4},\qquad
       \Xi_{C_6^{\rm fold}}\ge2\kappa\ge{1\over2}.   \tag{0.4}
   \]
   These constant lower bounds are compatible with \(\Xi=o(\sqrt s)\).
   Hence bounded clean or folded banks are **not** ruled out by the
   sparse-edit moment merely because they must cover positive-density
   many rows.
4. The exact remaining condition is edit dispersion.  If a proportion
   \(\alpha\) of all roots is changed and \(\bar d\) is their average
   rooted edit distance, then
   \[
       \Xi_{C_6}=3\alpha\bar d,
       \qquad \Xi_{C_6^{\rm fold}}=2\alpha\bar d.     \tag{0.5}
   \]
   At the MWB density \(\alpha\ge\kappa\), either bank passes the variance
   gate exactly when \(\bar d=o(\sqrt s)\).  No presently proved
   incidence-cycle supply theorem gives a positive-density,
   strand-admissible bank with this distance bound.

The same computation for a clean \(C_{2\ell}\) conveyor gives

\[
                         \Xi=\ell\alpha\bar d.        \tag{0.6}
\]

Therefore positive-density carrier demand forces the necessary conditions

\[
             \ell=o(\sqrt s),\qquad
             \bar d=o(\sqrt s/\ell).                 \tag{0.7}
\]

In particular a conveyor with \(\ell\ge c\sqrt s\) is quantitatively
excluded even at the minimum possible row edit \(d(P)=1\).  Clean
\(C_8\)'s have \(\ell=4\), so, like clean \(C_6\)'s, they are not excluded
by row demand alone.

## 1. Why the open switches have no \(\Xi\)

Orient the rows of an anchored factor from the Dyck root to its
complement.  The exact strand theorem says that a clean coherent
alternating \(C_{2\ell}\) on \(\ell\) distinct rows cyclically permutes
their tails.  For \(\ell=3\), the endpoint operation is a three-cycle.
The folded \(C_6\) of the two-one strand type exchanges the two endpoint
tails and hence acts as a transposition.

After either one switch, a row rooted at \(P\) ends at
\(J\setminus\tau(P)\), with \(\tau(P)\ne P\).  It is therefore not an
anchored complement row, and its temporal coordinate sequence need not be
a permutation of the \(2s\) coordinates.  The anchored word distance in
(0.1) is consequently not defined.  Assigning a number to such an open
atom and inserting it into the sparse-edit theorem is invalid.

A clean \(C_6\) may be closed by three coherently transported stages on
the same three root labels; a folded transposition may be closed by two.
This must be a literal internal conveyor, or another boundary-moving
construction whose complete ledgers are proved.  Placing the atoms in
independent Catalan holes applies the twist to independent port
coordinates rather than taking a power on one label.  Placing them in
fixed-exterior serial slabs is also invalid: the fixed-exterior geodesic
theorem forces every such local twist to be pointwise trivial.

All subsequent statements concern an actually constructed closed packet,
not its open constituent switch.

## 2. Exact full-overlay components

### Lemma 2.1 (one clean orbit is one full component)

Let a closed clean \(C_{2\ell}\) packet use the root set
\(R=\{P_0,\ldots,P_{\ell-1}\}\), and suppose every reconnected segment
stays inside these rows.  If its transported tail permutation is the
\(\ell\)-cycle \(\tau=(P_0\cdots P_{\ell-1})\), then the roots in \(R\)
form one component of the full state-and-colour ownership overlay of the
initial and final factors.  No root outside \(R\) belongs to that
component.

#### Proof

Every state and colour outside the packet retains its old owner, and every
state and colour inside the packet is reassigned only among roots in
\(R\).  Hence no ownership edge leaves \(R\).

At a clean alternating-cycle stage, the selected upper incidence token
formerly owned by the row at \(P_i\) is, after reconnection, owned by the
row whose transported label is \(\tau^{\pm1}P_i\).  The corresponding
full-overlay edge joins these two root vertices.  These edges contain the
cycle graph of \(\tau\); hence all roots in its unique orbit \(R\) are
connected.  Both state and colour edges have been included, so this is a
full-overlay statement. \(\square\)

The identical proof gives one two-root component for a nontrivial closed
folded transposition packet.  If packets have disjoint root and token
sets, their components are disjoint.  Thus for disjoint clean \(C_6\)
packets all nontrivial component sizes are three, while for disjoint
folded packets they are two.  Substitution in (0.1) proves (0.2).

More generally, if the final pair retains a cross-owned token for every
generator in an overlapping cycle packet, its components contain the root
orbits generated by those transported cycles.  Such overlap cannot improve
(0.1): if a component of size \(u\) contains only changed rows, its
contribution is at least \(u^2/B\).  In particular a final connected
overlay on \(\alpha B\) changed roots has
\(\Xi\ge\alpha^2B\), and is far outside \(o(\sqrt s)\).  Closing each
bounded orbit internally is therefore the fragmentation-optimal serial
arrangement.

## 3. Exact row-distance bounds

For a fixed root \(P\), both anchored words have the form

\[
 (a_1,\ldots,a_s,b_1,\ldots,b_s,\infty),             \tag{3.1}
\]

where \((a_i)\) orders \(P\) and \((b_i)\) orders \(J\setminus P\).
Therefore

\[
 d(P)=K(a^F,a^G)+K(b^F,b^G),                         \tag{3.2}
\]

where \(K\) is Kendall distance.  In particular

\[
                      1\le d(P)\le s(s-1)             \tag{3.3}
\]

on every genuinely changed row.  Both bounds are best possible for pairs
of rooted coordinate words; cycle geometry alone does not determine where
inside this interval a closed packet lies.

There is a useful chronology-sensitive lower bound.  Let
\(X_t^F(P),X_t^G(P)\) be the two rank-\(s\) states after \(t\) Johnson
steps, and put

\[
 A_t^e=\{a_1^e,\ldots,a_t^e\},\qquad
 B_t^e=\{b_1^e,\ldots,b_t^e\}.
\]

### Lemma 3.1 (phase-area inequality)

For every changed root,

\[
 \boxed{
 d(P)\ge\sum_{t=1}^{s-1}
             d_J\bigl(X_t^F(P),X_t^G(P)\bigr).}      \tag{3.4}
\]

#### Proof

For two permutations \(u,v\) of one \(s\)-set, let \(U_t,V_t\) be
their first-\(t\) sets and put
\(k_t=|U_t\setminus V_t|\).  Then

\[
 \sum_t k_t={1\over2}\sum_x
       |\operatorname {pos}_u(x)-\operatorname {pos}_v(x)|.
\]

An adjacent swap moves two entries one position, so along a shortest
Kendall path the total endpoint footrule is at most twice the number of
swaps.  Hence \(K(u,v)\ge\sum_tk_t\).

Apply this separately to the deletion and insertion orders.  Since both
rows have root \(P\),

\[
 d_J(X_t^F(P),X_t^G(P))
 =|A_t^F\setminus A_t^G|+|B_t^F\setminus B_t^G|.
\]

Summing and using (3.2) proves (3.4). \(\square\)

Suppose a clean \(\ell\)-stage conveyor switches at phases
\(t_0<\cdots<t_{\ell-1}\) and the transported phase label on the
intervening intervals is successively
\(\tau,\tau^2,\ldots,\tau^{\ell-1}\).  Every nonidentity power of an
\(\ell\)-cycle has no fixed point.  The state partition of \(F\) then
implies that the two states at root \(P\) are distinct throughout the

\[
                         E=t_{\ell-1}-t_0             \tag{3.5}
\]

intermediate phases.  Lemma 3.1 gives

\[
                              d(P)\ge E.              \tag{3.6}
\]

If the packet changes no transition outside this phase hull, its deletion
orders agree outside one position block of length \(E+1\), and the same is
true of its insertion orders.  Therefore

\[
                       d(P)\le2\binom{E+1}{2}=E(E+1). \tag{3.7}
\]

For a dense clean \(C_6\) bank of common exposure \(E\), (0.5) sharpens
to

\[
                    3\alpha E\le\Xi\le3\alpha E(E+1). \tag{3.8}
\]

For a strict two-stage transported transposition packet the analogous
bounds are

\[
                    2\alpha E\le\Xi\le2\alpha E(E+1). \tag{3.9}
\]

A general folded \(C_6\) has mixed cut phases, so one must use (3.4) with
its actual two root traces; the bare strand type supplies no single phase
span.  This is why an edit distance cannot be assigned to the folded
diagram from its endpoint transposition alone.

## 4. The exact audited MWB row demand

At the first charged plateau, the port synthesis audit gives, per aligned
context,

\[
 {B\over2}-p
   =B\left({1\over2}-{1\over\theta}\right)
   =\kappa B,\qquad \theta=B/p.                       \tag{4.1}
\]

The chosen scale has \(\theta\ge4\), hence \(\kappa\ge1/4\).  A row has
one first-insertion target and changing it moves at most one unit out of
the charged class.  Thus a bank which alone supplies (4.1) must contain

\[
                              M\ge\kappa B             \tag{4.2}
\]

changed roots.  Equations (0.4)--(0.7) follow immediately from (4.2) and
\(d(P)\ge1\).

This accounting is deliberately \(\Theta(B)\), not \(\Theta(W_s)\).
Replacing it by an \(\Omega(W_s)\) local carrier hypothesis would be a
stronger, unaudited normalization.

There is a valid conditional statement if some future consumer really
does require that stronger amount.  Put

\[
 {\cal A}_H(F,G)=\sum_{q\le H}{1\over2c_q}
                 \|\mu_q^F-\mu_q^G\|_1,
 \qquad S_H=\sum_{q\le H}{1\over c_q}.                \tag{4.3}
\]

The adjacent-edit lemma gives

\[
                 {\cal A}_H(F,G)\le2S_H\sum_Pd(P).    \tag{4.4}
\]

For uniform component size \(b\), (0.1) and (4.4) imply

\[
                 {\cal A}_H(F,G)\le{2S_HB\over b}\Xi. \tag{4.5}
\]

Consequently the additional hypothesis
\({\cal A}_H\ge\gamma W_s\) would force

\[
                     \Xi\ge{\gamma b(2s+1)\over2S_H}
                     =\Omega_{A,\gamma}(b\sqrt s)     \tag{4.6}
\]

at \(H=A\sqrt s\), and would close every fixed-length cycle bank.  This
is a rigorous conditional obstruction, but (4.1), not the stronger
hypothesis, is the currently audited MWB plateau demand.

## 5. Serial repetition

Let \(F^0,F^1,\ldots,F^q\) be anchored factors obtained by \(q\) closed
packets on the same root orbit \(R\), of size \(b\).  Rootwise triangle
inequality gives

\[
 d(F^0_P,F^q_P)\le\sum_{j=1}^q
                      d(F^{j-1}_P,F^j_P).             \tag{5.1}
\]

If the final full overlay remains inside \(R\), then

\[
 \Xi(F^0,F^q)
 \le {b\over B}\sum_{P\in R}\sum_{j=1}^q
                   d(F^{j-1}_P,F^j_P).                \tag{5.2}
\]

Thus a positive-density disjoint bank of packets, each with row distance
at most \(d_0\), has the sufficient estimate

\[
                              \Xi\le b\alpha qd_0.     \tag{5.3}
\]

For phase-hull exposure \(E\), (3.7) gives the still more explicit

\[
                              \Xi\le b\alpha qE(E+1). \tag{5.4}
\]

Hence \(qE(E+1)=o(\sqrt s/b)\) is sufficient for the variance gate.
There is no converse linear in \(q\): later packets can undo earlier word
edits.  The correct lower bound always uses the final distance or the
final phase-area (3.4).

Serial packets on fresh disjoint root orbits add exactly in (0.1).
Serial packets with overlapping root sets can merge the full overlay into
larger generated orbits; then \(b\) in (5.2)--(5.4) must be replaced by
the actual orbit size, and the size-square obstruction of Section 2
applies.

## 6. Precise proved boundary

The sparse-edit calculation does not eliminate bounded alternating-cycle
banks.  A positive-density clean \(C_6\), folded \(C_6\), or clean
\(C_8\) bank is compatible with \(\Xi=o(\sqrt s)\) provided its final
average rooted word distance is \(o(\sqrt s)\).  A clean
\(C_{2\ell}\) bank additionally requires \(\ell=o(\sqrt s)\) and
\(\bar d=o(\sqrt s/\ell)\).

What is not proved is the existence of such a bank.  The ballot-forced
incidence-cycle theorem certifies merely a lower bound of order \(B/s\)
on the number of edge-disjoint cycle certificates; it gives no
positive-density lower bound, and their lengths and phase/strand patterns
are uncontrolled.  It does not supply \(\Theta(B)\) clean \(C_6\)'s,
folded routers, or closed conveyors, and it supplies no final rooted edit
bound.  The exact next
constructive lemma is therefore:

> Construct \(\kappa B\) root-disjoint, internally monodromy-closed
> bounded-cycle packets whose final full-overlay components have bounded
> size, whose charged first-insertion carriers have a common favourable
> sign, and whose average final rooted edit distance is \(o(\sqrt s)\).

Without the favourable signed carrier clause, (0.2) is only a rounding
estimate and says nothing about midpoint descent.
