# Trace-two Hall collapse, interval barriers, and a private-reserve theorem

Date: 2026-07-28

Status: pure mathematics.  The Hall collapse and the interval-barrier
characterization below are exact.  The private-reserve theorem is a proved
sufficient theorem for a singleton residual phase.  No general trace-two
residual extension, `k=15` word, or proof of `nu(k)=B(k)` is claimed.

## 0. Outcome

The controller-skeleton formulation in Section 6 of
`THREAD_H_PBBS_CONNECTOR_COBBOUNDARY_AND_SIMULTANEOUS_HYPERSIMPLEX_LIFT_20260728.md`
contains a hidden simplification:

> **After a controller skeleton is fixed, the residual option graph has
> right degree at most one.**

Indeed, the two containments imposed on an edge `(S,c)` say exactly

\[
                         S=\bigcup_{p\in I_c}Q_p.
\]

Thus Hall has no non-singleton content at that stage.  Different residual
labels can never compete for the same cell.  The residual assignment exists
if and only if every residual label occurs at least once as a skeleton-union
on a controller-compatible cell.

This relocates the entire nonlinear gate into construction of the skeleton.
It also says that normalized matching cannot solve the gate *after* the
skeleton has been chosen.

The second exact result is a coordinatewise interval-barrier theorem.  For a
coordinate `x`, private-hit failure is precisely coverage of a required
positive interval by the union of the owner intervals whose labels omit
`x`, together with the positions where the envelope omits `x`.  On a line,
a failure therefore has a finite monotone chain certificate of negative
owner intervals.  This is the sharp cut obstruction special to the actual
Boolean-lattice/interval model; it is absent from arbitrary bipartite Hall.

Finally, a restricted but useful positive result is proved.  If the residual
deep ideal is assigned to singleton source cells, one may reserve mandatory
private witnesses `M_p` inside the fixed cores `C_p`.  The remaining
extension is a Boolean containment matching

\[
                         M_p\subseteq S\subseteq C_p.
\]

A weighted normalized-matching score gives a concrete sufficient condition,
and any such matching automatically has owner meet dimension at most two
provided the unmatched fixed cores do.

## 1. Fixed-skeleton Hall collapses to singleton coverage

Use exactly the notation of the controller-skeleton theorem.  Thus `R` is
the residual label family, `C` the unused cells, `I_c` the source interval of
cell `c`, and an admissible skeleton supplies nonempty traces

\[
 Q_p=E_p\cap\bigcap_{L\in\alpha_p}L,
 \qquad |\alpha_p|\le2.
 \tag{1.1}
\]

For a cell `c`, define its skeleton union

\[
                         \rho_\alpha(c)=\bigcup_{p\in I_c}Q_p.
 \tag{1.2}
\]

Recall that an edge `(S,c)` of `G_alpha` is required to satisfy

\[
 Q_p\subseteq S\quad(p\in I_c),
 \qquad
 S\subseteq\bigcup_{p\in I_c}Q_p,
 \tag{1.3}
\]

as well as base eligibility and the controller-support condition
`P_alpha(S) subseteq I_c`.

### Theorem 1.1 (right-degree-one theorem)

For every admissible skeleton `alpha` and every cell `c`,

\[
                         \deg_{G_\alpha}(c)\le1.
 \tag{1.4}
\]

More precisely, if `c` has a neighbour, that neighbour is
`rho_alpha(c)`.  Consequently the following are equivalent.

1. `G_alpha` has a matching saturating `R`.
2. Every `S in R` has positive degree in `G_alpha`.
3. For every `S in R` there is a cell `c` such that

   \[
   (S,c)\in B,\qquad P_\alpha(S)\subseteq I_c,\qquad
   \rho_\alpha(c)=S.
   \tag{1.5}
   \]

#### Proof

The first containment in (1.3), after union over `p in I_c`, gives
`rho_alpha(c) subseteq S`; the second gives the reverse containment.  Hence
every neighbour of `c` equals `rho_alpha(c)`, proving (1.4).

It follows immediately that neighbour sets of two distinct left labels are
disjoint.  If every left label has a neighbour, choose one arbitrarily for
each label; the chosen cells are automatically distinct.  This is a
matching saturating `R`.  The other implications are immediate, and (1.5)
is the literal edge definition after substituting (1.2).  \(\square\)

### Corollary 1.2 (the true fixed-skeleton gate)

The quantifier over all Hall shores in the controller-skeleton theorem may
be replaced by the pointwise condition (1.5).  All residual competition is
already resolved by the skeleton-union equality.  The only open choice is a
self-consistent skeleton whose interval unions contain the complete
residual family and whose controller labels occur on intervals containing
the positions they control.

This is a simplification, not a proof of existence.  Constructing such a
skeleton is essentially a bounded-controller interval-union problem.

### Theorem 1.3 (exact controller-word formulation)

A trace-two residual extension exists if and only if there are

* nonempty sets \(Q_p\subseteq E_p\) for all source positions;
* for each residual label \(S\), an eligible cell \(c_S\); and
* for each position \(p\), a controller set \(\Gamma_p\) of at most two
  fixed or residual owner labels;

such that all of the following hold.

1. Every fixed protected pair \((L,J_L)\) has

   \[
                           \bigcup_{p\in J_L}Q_p=L.
   \tag{1.6}
   \]

2. Every residual label has

   \[
                           \bigcup_{p\in I_{c_S}}Q_p=S.
   \tag{1.7}
   \]

3. Every fixed owner active at \(p\), and every residual label \(S\) with
   \(p\in I_{c_S}\), contains \(Q_p\).
4. Every controller in \(\Gamma_p\) is active at \(p\), and

   \[
                 Q_p=E_p\cap\bigcap_{L\in\Gamma_p}L.
   \tag{1.8}
   \]

In particular, if \(S\) is used as a controller at \(p\), then its selected
occurrence satisfies the footprint condition \(p\in I_{c_S}\).

#### Proof

Given an extension, take \(Q_p\) to be its actual meet, take \(c_S\) from
the assignment, and choose at most two active labels generating each meet.
The protected equalities give (1.6)--(1.7), while activity gives conditions
3--4.

Conversely, (1.7) implies \(Q_p\subseteq S\) throughout \(I_{c_S}\), so a
cell cannot be selected for two distinct residual labels: its union has one
value.  Hence the selected cells are automatically distinct.  At position
\(p\), condition 3 says the intersection of all active owners contains
\(Q_p\).  The active controller subfamily in condition 4 has intersection
exactly \(Q_p\), so the intersection of all active owners is also contained
in \(Q_p\).  It is therefore equal to \(Q_p\).  Equations (1.6)--(1.7) give
every protected and residual equality, and nonemptiness is explicit.  This
is the required trace-two extension.  \(\square\)

Theorem 1.3 is the promised word description.  The skeleton is not merely
a list of local controller pairs: it is one nonempty trace word \(Q\), its
short-interval union multiset must cover the residual ideal, and its chosen
controller occurrences must contain their complete controller footprints.
Central-window equalities and private hits are exactly the fixed instances
of (1.6).

### Corollary 1.4 (the \(k=15\) H29 residual consequence)

Keep the 1,489 peeled H29 owners fixed.  In the old residual catalogue there
are 35 labels and six live cells, each old cell having two base-option
neighbours.  For every fixed controller skeleton:

* each of the six cells retains at most one of its two base neighbours;
* at most six residual labels have positive degree; and
* at least 29 residual labels have degree zero.

Consequently any extension preserving the peeled owners must create at
least 29 additional physical cells outside the old six whose skeleton unions
are 29 distinct formerly missing residual labels.

#### Proof

The first two assertions are Theorem 1.1.  There are 35 distinct labels, so
at least \(35-6=29\) have no old-cell occurrence.  In any successful
enlarged catalogue each such label needs a cell whose \(Q\)-union equals
that label by (1.5); those cells are distinct automatically.  \(\square\)

This strengthens the interpretation of the earlier 29-fresh-cell tax.  The
six old collisions are not six ordinary matching choices after a skeleton
is fixed: each skeleton resolves every collision to one literal interval
union and makes the other candidate disappear.

The audited six cells make this literal.  Their two base neighbours are the
following nested rank-six/rank-seven pairs:

\[
\begin{array}{c|c}
\text{cell}&\text{candidate pair}\\ \hline
15899&2420\subset2932\\
16597&4877\subset4909\\
18079&17683\subset21779\\
18088&2676\subset10868\\
18090&9524\subset9588\\
18985&19568\subset27760.
\end{array}
\tag{1.9}
\]

The entries are the decimal subset masks from
`scratch/k15_h29_one_owner_cia_audit.json`.  The rank difference does
not provide a second unit of capacity: one interval union has one rank and
one label.

## 2. The exact coordinatewise interval barrier

Let `P` be the source-position set, let `E_p subseteq Omega` be the maximal
envelope at `p`, and let `phi` be any injective assignment of owner labels
`S` to source intervals `I_S`.  Put

\[
 A_p=E_p\cap\bigcap_{S:p\in I_S}S.
 \tag{2.1}
\]

For a coordinate `x in Omega`, define its envelope support, negative owner
barrier, and surviving support by

\[
 E(x)=\{p:x\in E_p\},
 \qquad
 B(x)=\bigcup_{S:x\notin S}I_S,
 \qquad
 Z(x)=E(x)\setminus B(x).
 \tag{2.2}
\]

### Theorem 2.1 (private-hit barrier theorem)

For every coordinate `x` and position `p`,

\[
                         x\in A_p\iff p\in Z(x).
 \tag{2.3}
\]

Hence a protected equality

\[
                         \bigcup_{p\in J_L}A_p=L
 \tag{2.4}
\]

holds if and only if, for every coordinate `x`,

\[
 \begin{cases}
 J_L\cap Z(x)\ne\varnothing,&x\in L,\\
 J_L\cap Z(x)=\varnothing,&x\notin L.
 \end{cases}
 \tag{2.5}
\]

For an assigned owner label `L` on its own interval, the second line is
automatic.  Its positive/private-hit condition is therefore exactly

\[
 \boxed{
 J_L\cap E(x)\not\subseteq
       \bigcup_{S:x\notin S}I_S
 \quad(x\in L).}
 \tag{2.6}
\]

#### Proof

Coordinate `x` belongs to (2.1) precisely when it belongs to `E_p` and no
active owner omits it.  This is (2.3).  Taking the union over `J_L` proves
(2.5).  If `x notin L`, the interval `J_L=I_L` itself is one of the terms in
`B(x)`, so the negative line is automatic for an owner equality.  The
positive line is (2.6).  \(\square\)

This theorem includes central middle-window equalities, spill labels, and
residual labels without treating them as independent matching constraints.
The only difference is that a central equality need not itself be an owner,
so both lines of (2.5) must be checked; in the maximal-erosion model its
negative line is normally forced by `E_p subseteq T_i` on the central
window.

### Proposition 2.2 (monotone barrier-chain certificate)

Assume source positions are linearly ordered and every owner support `I_S`
is an interval.  Fix a required pair `(L,x)` with `x in L`.  If (2.6) fails,
then every interval component `K` of `J_L cap E(x)` is covered by a sequence
of `x`-omitting owner intervals

\[
                         I_1,\ldots,I_t
 \tag{2.7}
\]

which may be chosen so that their left endpoints and right endpoints are
strictly increasing and consecutive intervals overlap (or meet in adjacent
discrete positions).  Conversely any such collection covering
`J_L cap E(x)` certifies failure.

#### Proof

The converse is immediate.  For the forward direction, greedily choose,
among all negative intervals containing the leftmost uncovered point of
`K`, one with maximum right endpoint.  Move to the next uncovered point and
repeat.  Minimality removes any interval whose left endpoint does not
increase, while the greedy maximum makes the right endpoints strictly
increase.  No gap is possible because the intervals cover `K`.  Repeat for
every component of `J_L cap E(x)`.  \(\square\)

Thus private-hit failure has a short, checkable **interval cut**, not an
arbitrary Hall shore.  In particular the complete-graph counterexample in
the abstract controller theorem is the special case in which a chain of
internal two-point cells covers every private marker interval.

## 3. Trace dimension is an omission-cover number

At a fixed position `p`, each active owner `S` omits

\[
                         D_p(S)=E_p\setminus S.
 \tag{3.1}
\]

Let `D_p` be their union.

### Proposition 3.1 (exact local cover formula)

The owner meet dimension at `p` is

\[
 \boxed{
 \kappa_p=\min\left\{|\mathcal H|:
   \mathcal H\subseteq\mathcal O_p,
   \bigcup_{S\in\mathcal H}D_p(S)=D_p\right\}.}
 \tag{3.2}
\]

In particular, trace two holds at `p` if and only if two active owner
omission sets cover every omission made there.

#### Proof

For any subfamily `H`, De Morgan's law gives

\[
 E_p\cap\bigcap_{S\in\mathcal H}S
 =E_p\setminus\bigcup_{S\in\mathcal H}D_p(S).
\]

Equality with the meet of all owners is therefore equivalent to equality of
the two omission unions.  Minimizing proves (3.2).  \(\square\)

### Lemma 3.2 (absorbing controller)

Let the fixed owners at `p` have core

\[
                         C_p=E_p\cap\bigcap_{F\in\mathcal F_p}F.
 \tag{3.3}
\]

If a residual owner `S` is active only at `p` and satisfies
`S subseteq C_p`, then the full meet at `p` is `S`, and `kappa_p<=1`.

#### Proof

Every fixed owner contains `C_p` and hence contains `S`.  Intersecting all
fixed owners and `S` therefore gives `S`, which is generated by the one
owner `S`.  \(\square\)

This is the basic reason singleton deep owners are particularly valuable:
they absorb every spill cut at their position rather than adding another
independent controller.

### Proposition 3.3 (unit-spill colour-depth theorem)

Suppose every non-natural fixed owner is a one-rank spill: for its cell
interval \(I\), with maximal union-envelope \(H_I\), its label is

\[
                         S_I=H_I\setminus\{z_I\}.
\tag{3.4}
\]

At a position \(p\), let

\[
 \chi(p)=\#\{z_I:z_I\in E_p,\ p\in I\}
\tag{3.5}
\]

count distinct active spill colours.  If no other effective owner is active
at \(p\), then

\[
                         \kappa_p=\chi(p).
\tag{3.6}
\]

If a singleton residual owner \(S\subseteq C_p\) is placed at \(p\), then
\(\kappa_p\le1\), regardless of \(\chi(p)\).  Consequently a unit-spill
assignment is trace two whenever every position with \(\chi(p)>2\) is
absorbed by such a singleton residual owner.

#### Proof

For \(p\in I\), one has \(E_p\subseteq H_I\), so the omission set of this
owner at \(p\) is either empty or the singleton \(\{z_I\}\).  The union of
all omissions has exactly \(\chi(p)\) elements, and each active owner covers
at most one of them.  Formula (3.2) gives (3.6).  The absorbing assertion is
Lemma 3.2.  \(\square\)

This is the bounded-overlap theorem for the most important spill regime.
It turns trace two into a coloured interval-depth condition.  High
uncoloured overlap is harmless; only three *different deleted coordinates*
at one unabsorbed position are forbidden.  The private-reserve matching in
Section 4 can therefore be aimed first at the hot set
\(\{p:\chi(p)>2\}\).

## 4. A private-reserve theorem for a singleton residual phase

We now give a positive theorem which combines private witnesses with a
Boolean containment matching.  It applies whenever the remaining residual
labels are assigned to unused source (length-one) cells.  Fixed natural and
spill owners may have arbitrary interval lengths.

Let `U subseteq P` be the unused singleton positions and let `R` be the
remaining nonempty residual labels.  Let `C_p` be the fixed-owner core (3.3),
assumed nonempty.  Let `P_0` be the already protected pairs `(L,J_L)`.

A **private reserve** is a family `M_p subseteq C_p` such that

\[
 M_p\ne\varnothing\quad(p\in P),
 \qquad
 \bigcup_{p\in J_L}M_p=L\quad((L,J_L)\in P_0).
 \tag{4.1}
\]

For `p in U`, declare a residual label `S` compatible when

\[
                         M_p\subseteq S\subseteq C_p.
 \tag{4.2}
\]

### Theorem 4.1 (private-reserve extension)

Assume:

1. for every protected \((L,J_L)\) and every \(p\in J_L\), one has
   \(C_p\subseteq L\);
2. the compatibility graph (4.2) has a matching saturating `R` such
   that, at every position not used by that matching, the fixed owners
   defining \(C_p\) have meet dimension at most two.

Assign each matched residual label `S` to the singleton cell `{p}` supplied
by the matching.  Then all residual and protected equalities hold, every
source position remains nonempty, and the resulting owner meet dimension is
at most two everywhere.

#### Proof

At a matched position, Lemma 3.2 and (4.2) show that the full source entry is
exactly `S`; it is nonempty, realizes its singleton residual cell, contains
`M_p`, and has meet dimension one.  At an unmatched position the source
entry is the fixed meet, which contains `M_p`, is nonempty, and has meet
dimension at most two by assumption 2.

All entries in a protected interval are contained in its label by assumption
1 (and by \(S\subseteq C_p\) at a matched position).  Their union
contains `union M_p=L` by (4.1), so it equals
`L`.  This proves all protected equalities and the theorem.  \(\square\)

The theorem separates the two genuinely different resources:

* `M_p` reserves positive witnesses against the interval barriers of
  Section 2;
* the containment matching places the deep ideal without destroying those
  witnesses.

Let

\[
 H=\{p\in U:\text{the fixed-owner meet dimension at }p\text{ exceeds }2\}
\tag{4.3}
\]

be the hot positions which must be absorbed by Lemma 3.2.

### Proposition 4.2 (exact hot-position cuts)

Let \(G\) be the compatibility graph between \(R\) and \(U\), with
\(|U|\ge |R|\).  There is a matching which saturates every target in \(R\)
and also uses every position in \(H\) if and only if, for every
\(X\subseteq R\),

\[
 |N(X)|\ge |X|
\tag{4.4}
\]

and

\[
 |N(X)\cap H|\ge |X|+|H|-|R|.
\tag{4.5}
\]

#### Proof

Add \(|U|-|R|\) dummy left vertices, each adjacent to every vertex of
\(U\setminus H\) and to no vertex of \(H\).  A perfect matching in the
resulting balanced graph is exactly a matching of the original graph which
saturates \(R\) and leaves no hot position for a dummy.

Apply Hall to a left shore consisting of \(X\subseteq R\) and a dummy
subset.  With no dummy, Hall is (4.4).  With at least one dummy, the largest
right-hand demand occurs when all dummies are included, and Hall becomes

\[
 |N(X)\cup(U\setminus H)|
 \ge |X|+|U|-|R|.
\]

Since the left side is \(|U|-|H\setminus N(X)|\), this rearranges to
(4.5).  These exhaust all augmented Hall shores.  \(\square\)

Thus the only extra cut created by trace two in the singleton absorption
phase is the explicit hot-position inequality (4.5).  It is not an
unstructured private-hit constraint.

### Corollary 4.3 (weighted normalized-matching certificate)

Partition `R` by rank.  For `p in U` and a rank `t`, put

\[
 n_{p,t}=\#\{S\in R:|S|=t,\ M_p\subseteq S\subseteq C_p\}.
 \tag{4.6}
\]

Suppose there are numbers `lambda_(p,t)>=0`, with `lambda_(p,t)=0` when
`n_(p,t)=0`, such that

\[
                         \sum_t\lambda_{p,t}\le1
 \quad(p\in U),                                      \tag{4.7}
\]

and for every `S in R` of rank `t`,

\[
 \boxed{
 \sum_{p:\,M_p\subseteq S\subseteq C_p}
       \frac{\lambda_{p,t}}{n_{p,t}}\ge1.}
 \tag{4.8}
\]

Then the compatibility graph has a matching saturating `R`, so Theorem 4.1
applies whenever the fixed-owner meet dimension is already at most two at
every position.  More generally, one must additionally choose the matching
to cover every position where that fixed dimension exceeds two, as required
in Theorem 4.1.

#### Proof

Give an eligible edge `(S,p)`, with `|S|=t`, fractional weight
`lambda_(p,t)/n_(p,t)`.  The total weight at `p` is
`sum_t lambda_(p,t)<=1`; (4.8) says every target receives weight at least
one.  Trimming excess target weight gives a fractional matching saturating
`R`.  The bipartite matching polytope is integral, so an integral saturating
matching exists.  \(\square\)

When `R` contains every rank-`t` set in a Boolean interval, (4.6) becomes
the explicit normalized-matching denominator

\[
 n_{p,t}
 =\binom{|C_p|-|M_p|}{t-|M_p|}.
 \tag{4.9}
\]

Thus (4.8) is the precise place where Boolean-lattice normalized matching is
useful.  It is useful *before* the controller skeleton is fixed, in a
restricted absorption phase; it is vacuous after a full skeleton is fixed,
by Theorem 1.1.

## 5. The revised open target

The general residual intervals are not all singletons, so Theorem 4.1 does
not close the Pascal-package compiler.  The proved reductions identify the
remaining target more sharply:

> Construct nonempty traces `Q_p subseteq E_p`, each generated by at most
> two active owner labels, such that every fixed and residual lower target
> is the union of the `Q_p` on one eligible short interval, every controller
> label controls only positions inside its chosen occurrence, and no
> required positive interval is crossed by a complete negative barrier
> chain.

There is no additional matching theorem after this construction.  The
interval-union equality automatically separates cell ownership.  Any future
attack should therefore target one of two concrete structures:

1. a recursive two-controller trace word whose interval unions enumerate
   the lower ideal; or
2. a decomposition of the residual phase into singleton absorption rounds,
   each certified by Theorem 4.1 and Corollary 4.2.

The second route is the cleanest possible normalized-matching approach.  A
proof that every Pascal flag package admits enough such rounds would prove
the trace-two residual extension lemma; that decomposition is presently
open.
