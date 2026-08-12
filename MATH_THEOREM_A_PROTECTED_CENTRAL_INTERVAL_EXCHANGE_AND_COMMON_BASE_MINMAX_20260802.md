# Protected central interval exchange, atlas connectivity, and common-base min--max

**Date:** 2026-08-02  
**Lane:** A, central complementary bi-packing / fixed-core common base  
**Status:** exact conditional absorber theorem and exact scoped obstruction.
No central interval-replacement supply, matroidal lift, Boolean normality,
reset ticket, or contiguous-OR word is asserted.

## 0. Outcome

Let a complementary pair of central interval banks be fixed.  Its physical
Johnson union has maximum degree two, so its graphic nullity is exactly its
number of alternating cycle components.  There are four proof-safe facts.

1. For every equal-size interval trade, cycle reduction has the exact
   contracted-rank test

   \[
    \beta(B-R+A)-\beta(B)
      =\rho_{B-R}(R)-\rho_{B-R}(A).                 \tag{0.1}
   \]

   Thus a proposed third replacement circuit is useful precisely when its
   new half has larger graphic rank than its old half after the untouched
   support is contracted.  Palette neutrality alone does not imply this.

2. For any supplied protected atlas, there is an exact connected-exchange
   criterion.  Retain only moves that do not lower graphic rank and contract
   its equal-rank strongly connected classes.  The atlas is a monotone
   cycle-complete absorber exactly when every sink class has full graphic
   rank.  A sub-full-rank sink is a rigorous no-go for that atlas, but not
   for the full Boolean problem.

3. A literal bounded-load inequality supplies an escaping circuit from
   every nonterminal class.  It is the exact analogue of the protected
   circuit load lemma in the skip-port theorem.

4. If, in addition, the non-graphic table family has an **exact matroidal
   lift**, Edmonds' matroid-intersection min--max theorem gives the sharp
   cut criterion

   \[
      r_M(X)+r_G(E-X)\ge q\qquad(X\subseteq E).      \tag{0.2}
   \]

   Under (0.2), an ordinary matroid-intersection augmenting path raises a
   common forest subset by one; extending it to a new resource base lowers
   the graphic deficit by at least one.  This becomes a literal interval
   absorber only when the supplied atlas realizes those base changes.

The qualification in Item 4 is essential.  On the natural diamond ground,
lower, upper, and the two bank-middle matching rows are several simultaneous
partition constraints, not one matroid.  The known five-cycle fixture even
rules out an exact two-matroid representation on the natural oriented-
diamond ground.  Neither the Dong--Mao theorem nor the five-coordinate
three-quarter bank supplies the missing lift.

## 1. Literal protected two-bank states

Put

\[
 \mathcal L={ [2m]\choose m-1},\qquad
 \mathcal M={ [2m]\choose m},\qquad
 \mathcal U={ [2m]\choose m+1},\qquad
 N=|\mathcal L|=|\mathcal U|.                       \tag{1.1}
\]

Let \(\mathcal Q=\mathcal Q_0\mathbin{\dot\cup}\mathcal Q_1\) be the
bank-labelled central diamonds.  An element

\[
 q=(\epsilon,L,\{a,b\}),\qquad \epsilon\in\{0,1\}, \tag{1.2}
\]

has upper endpoint \(U=L+a+b\), middle endpoints
\(L+a,L+b\), and physical Johnson edge

\[
                         e(q)=\{L+a,L+b\}.            \tag{1.3}
\]

A **two-bank table** is a set \(B\subseteq\mathcal Q\) of size \(N\)
such that

* every lower and every upper endpoint occurs once; and
* for each \((\epsilon,M)\in\{0,1\}\times\mathcal M\), at most one
  member of \(B\cap\mathcal Q_\epsilon\) uses \(M\).

Thus \(B\cap\mathcal Q_0\) and \(B\cap\mathcal Q_1\) are interval banks
with complementary outer palettes.  Let \(G_B\) be their uncoloured
physical union on \(\mathcal M\).  Each bank is a matching, so
\(\Delta(G_B)\le2\).  The outer rows prevent two selected bank copies of
the same physical edge.  Hence \(G_B\) is a simple disjoint union of paths,
even cycles, and isolated vertices.

Let \(G\) denote the graphic matroid on the bank-labelled physical edge
copies, and put

\[
       \beta(B)=|B|-r_G(B).                           \tag{1.4}
\]

For a two-bank table, \(\beta(B)\) is exactly the number of cyclic
components of \(G_B\).  In particular,

\[
                 B\text{ is a central linear forest}
                 \quad\Longleftrightarrow\quad
                 r_G(B)=N.                           \tag{1.5}
\]

Now fix a protected selected set \(P\subseteq B\), a forbidden literal
resource set \(F\), and any extra exact resource/guard incidence map

\[
                         \gamma:\mathcal Q\longrightarrow\mathbb Z^Z.
                                                               \tag{1.6}
\]

The coordinates of \(\gamma\) may include lower and upper colours,
bank-middle uses, owner and payload labels, oriented tail/head labels,
residence guards, reset type, and collar resources.  Which coordinates are
included must be stated literally; an orbit count is not a substitute.
If \(P\) is not graphic-independent, then no forest table containing it can
exist.  Thus every positive protected-forest statement below implicitly
requires \(P\) itself to be a forest; failure is already an exact protected
no-go.

An interval replacement

\[
                  C=(R,A),\qquad R\subseteq B-P,\quad
                  A\subseteq\mathcal Q-B,             \tag{1.7}
\]

is **protected resource-zero** at \(B\) when

\[
 |R|=|A|,\qquad \gamma(R)=\gamma(A),                 \tag{1.8}
\]

every member of its complete old/new footprint avoids \(F\), and

\[
                         B'=(B-R)\mathbin{\dot\cup}A \tag{1.9}
\]

is again a literal two-bank table containing \(P\).  If bank-middle rows
are included in \(\gamma\), (1.8) preserves their complete occupancy
vector.  If they are not included, the last requirement in (1.9) must be
checked directly.  This distinction permits capacity-safe trades that move
unused middle slots, while never deriving capacity from palette neutrality.

If orientations are chosen only after the final physical forest, oriented
tail/head rows are omitted during the atlas descent and installed at the
end by coherently orienting each path.  If the table has already been
inserted into a fixed owner/state master, then orientation and all four
central labels must instead occur in \(\gamma\) and be preserved by every
trade.

## 2. The exact graphic test for one replacement circuit

For a fixed trade (1.7), put \(T=B-R\).  For any edge set \(X\), define
its graphic rank relative to the untouched support by

\[
       \rho_T(X)=r_G(T\cup X)-r_G(T).                 \tag{2.1}
\]

Equivalently, contract every connected component of \(G_T\), keep loops
and parallel copies, and take the graphic rank of the image of \(X\).

### Theorem 2.1 (protected interval rank-transfer identity)

Every protected equal-size replacement (1.7)--(1.9) satisfies

\[
 \boxed{\ \beta(B')-\beta(B)=\rho_T(R)-\rho_T(A).\ } \tag{2.2}
\]

Consequently it strictly reduces the number of alternating cycles exactly
when

\[
                         \rho_T(A)>\rho_T(R),         \tag{2.3}
\]

and the exact number removed, net of cycles recreated elsewhere, is the
difference in (2.3).

#### Proof

By (2.1),

\[
 r_G(B)=r_G(T)+\rho_T(R),\qquad
 r_G(B')=r_G(T)+\rho_T(A).                           \tag{2.4}
\]

Subtract these identities in (1.4) and use \(|B|=|B'|\).  Both terminal
sets are two-bank tables, so their nullities equal their cycle-component
counts.  This proves every assertion. \(\square\)

### Corollary 2.2 (complete local cycle-breaker certificate)

Suppose \(|R|=t\), and \(R\) meets exactly \(h\) cyclic components of
the maximum-degree-two graph \(G_B\).  Then

\[
                         \rho_T(R)=t-h.               \tag{2.5}
\]

If the image of \(A\) after contracting \(T\) is independent, so that
\(\rho_T(A)=t\), then the trade removes exactly those \(h\) cycles and
creates none:

\[
                         \beta(B')=\beta(B)-h.        \tag{2.6}
\]

In particular, a proposed third interval-replacement circuit that cuts one
old alternating cycle is a one-unit breaker exactly when its new half has
full rank in the quotient by the untouched support.

#### Proof

Every removed edge in a path component is a bridge.  In a cyclic component,
the first removed edge destroys the unique cycle without increasing the
component count, while each further removed edge is a bridge in what
remains.  Thus each cyclic component met saves one unit from the relative
rank, giving (2.5).  Substitute \(\rho_T(A)=t\) in (2.2). \(\square\)

The word "independent" in this corollary is global: the contraction uses
the complete untouched central and protected support.  Checking the new
half only inside its five-coordinate fibre is insufficient.

## 3. The exact connected-atlas criterion

Let \(\mathfrak B_P\) be any finite family of protected two-bank tables
with the same exact resources and guards.  A supplied interval atlas
\(\mathscr A\) gives a directed state graph \(D_{\mathscr A}\) on
\(\mathfrak B_P\): put an arc \(B\to B'\) precisely when one listed
literal replacement is legal at \(B\) and produces \(B'\).  Reversible
signed circuits give arcs in both directions, but reversibility is not
assumed.

Write \(g(B)=r_G(B)\), and let \(D_{\mathscr A}^{\uparrow}\) retain only
arcs with \(g(B')\ge g(B)\).  Every strongly connected component of
\(D_{\mathscr A}^{\uparrow}\) has one common rank: a strict increase could
not be followed by a nondecreasing return.

### Theorem 3.1 (protected atlas reachability and plateau traps)

The following statements are exact.

1. A forest table is reachable from a specified \(B_0\) by arbitrary atlas
   moves if and only if the forward-reachable set of \(B_0\) in
   \(D_{\mathscr A}\) contains a rank-\(N\) state.
2. Every state has some atlas path to a forest if and only if every sink
   strongly connected component of \(D_{\mathscr A}\) contains a forest.
3. Every state has a **nondecreasing-graphic-rank** atlas path to a forest
   if and only if every sink strongly connected component of
   \(D_{\mathscr A}^{\uparrow}\) has rank \(N\).

A sink component of \(D_{\mathscr A}^{\uparrow}\) of rank below \(N\) is
called a **plateau trap**.  It is an exact obstruction to every monotone
absorber using this atlas.  A sink component of the full graph containing
no forest is the stronger obstruction to every absorber using this atlas,
even one allowed to make rank-decreasing detours.

#### Proof

Item 1 is the definition of reachability.  In any finite directed graph,
every vertex reaches a sink strongly connected component.  Therefore all
vertices reach a member of a specified target set exactly when every sink
component meets that target set, proving Item 2.  Apply the same statement
to \(D_{\mathscr A}^{\uparrow}\).  Its sink components have constant
graphic rank, and its target states have rank \(N\), proving Item 3.
\(\square\)

For a reversible atlas, the equal-rank strongly connected components are
ordinary connected components of the rank plateau.  Item 3 then says:
every sub-full plateau component must have an atlas edge to a higher-rank
table.  This is the promised connected exchange theorem; it makes no
unproved assertion that the supplied atlas has the property.

### Corollary 3.2 (finite descent)

If the condition in Theorem 3.1(3) holds, then from a table with \(c\)
alternating cycles there is a monotone atlas path having at most \(c\)
strictly rank-increasing moves.  Neutral moves inside a plateau may also be
needed.

#### Proof

Leave each sub-full sink plateau through a strict rank increase.  Graphic
rank is integral and bounded by \(N\).  Its initial deficit is
\(N-r_G(B)=c\). \(\square\)

## 4. A protected bounded-load escape theorem

For a literal trade \(C\), let \(\operatorname{foot}(C)\) contain every
old and new physical resource whose use, availability, guard, menu, or
reset status is inspected by that trade.  Omitting a changed resource from
the footprint invalidates the following count.

### Theorem 4.1 (bounded-load exclusion of plateau traps)

Consider a rank-\(s<N\) strongly connected component \(K\) of
\(D_{\mathscr A}^{\uparrow}\).  Suppose a state \(B_K\in K\) has a bank
\(\mathcal C_K\) of ambient resource-zero candidate trades, before
forbidden-set filtering, such that:

1. every \(C\in\mathcal C_K\), if legal, satisfies the strict rank test
   \(\rho_{B_K-R_C}(A_C)>\rho_{B_K-R_C}(R_C)\);
2. avoiding the current forbidden set \(F_K\) is sufficient for \(C\) to
   be a literal legal atlas move at \(B_K\);
3. every \(f\in F_K\) lies in at most \(\Delta_K\) footprints; and
4. \(|\mathcal C_K|>\Delta_K|F_K|\).

Then \(K\) is not a plateau trap.  If these hypotheses hold for every
sub-full-rank component, the atlas is a monotone circuit-complete absorber.

#### Proof

At most \(\Delta_K|F_K|\) members of \(\mathcal C_K\) meet the forbidden
set, by the union bound over a first forbidden resource.  Hence some trade
avoids \(F_K\).  Item 2 makes it legal, and Item 1 gives an outgoing arc
from \(B_K\), hence from \(K\), to a higher rank.  Apply Theorem 3.1(3) to
all plateau components. \(\square\)

This theorem counts literal complete trades, not orbit types.  The
inequality is strict because equality allows every candidate to be hit.
It also gives no candidates: proving the size and load assertions is the
missing Boolean interval-circuit supply theorem.

## 5. Conditional matroid--graphic min--max and augmentation

There is a stronger structural route, but it has an additional hypothesis.
Assume the protected selected set is graphic-independent.  After
contracting it and deleting every forbidden or conflicting option, suppose
there is a finite lifted ground set \(E\)
with:

1. a rank-\(q\) matroid \(M\) whose bases decode, through a
   network-integral and payload-transparent fibre, to exactly the admissible
   residual resource tables under consideration; and
2. a graphic matroid \(G\), truncated to rank \(q\), such that for every
   lifted \(M\)-base \(\widehat B\),
   \[
      q-r_G(\widehat B)
       =\beta(\operatorname{decode}(\widehat B));     \tag{5.0}
   \]
   in particular, a decoded table completes the protected physical forest
   exactly when its lift is independent in \(G\).

Call this an **exact protected matroidal lift**.  Exactness of Item 1 in
both directions is needed to turn a negative cut into an impossibility
theorem for the stated table family.  A one-way lift gives only a
sufficient positive route.

### Theorem 5.1 (protected common-base min--max)

For an exact protected matroidal lift,

\[
 \begin{aligned}
 \mu
  &:=\max\{|I|: I\in\mathcal I(M)\cap\mathcal I(G)\}\\
  &=\min_{X\subseteq E}\bigl(r_M(X)+r_G(E-X)\bigr). \tag{5.1}
 \end{aligned}
\]

Consequently a protected forest resource base exists if and only if

\[
              r_M(X)+r_G(E-X)\ge q
              \qquad\text{for every }X\subseteq E.  \tag{5.2}
\]

If (5.2) fails at \(X\), then

\[
        q-r_M(X)-r_G(E-X)>0                          \tag{5.3}
\]

is an exact common-base deficiency certificate for this lift.

#### Proof

Equation (5.1) is the matroid-intersection min--max theorem.  A common
independent set of size \(q\) is a base of \(M\); after decoding it is an
admissible resource table, and graphic independence gives the protected
forest.  Conversely every decoded protected forest base has a common
independent lift of size \(q\).  Thus \(\mu=q\) is equivalent to (5.2),
and (5.3) is its separating cut. \(\square\)

The constructive certificate is equally exact.  For a common independent
set \(I\), form the usual exchange digraph on \(E\).  For
\(x\in I,y\notin I\), put

\[
 \begin{array}{ll}
 x\longrightarrow y,& I-x+y\in\mathcal I(M),\\
 y\longrightarrow x,& I-x+y\in\mathcal I(G).
 \end{array}                                         \tag{5.4}
\]

Its sources and sinks are

\[
 S_I=\{y\notin I:I+y\in\mathcal I(M)\},\qquad
 T_I=\{y\notin I:I+y\in\mathcal I(G)\}.             \tag{5.5}
\]

The matroid-intersection augmenting-path theorem says that \(I\) is not
maximum exactly when (5.4) has a directed \(S_I\)-to-\(T_I\) path.  The
symmetric difference with a shortest such path is a common independent set
of size \(|I|+1\).

### Theorem 5.2 (one-unit base deficit descent)

Assume (5.2).  Write \(B\) for any lifted \(M\)-base and put

\[
                         d=q-r_G(B).                  \tag{5.6}
\]

If \(d>0\), then there is another \(M\)-base \(B^+\) with

\[
                         q-r_G(B^+)\le d-1.           \tag{5.7}
\]

Starting from any base, at most its initial graphic deficit many repetitions
produce a common forest base.

#### Proof

Choose a maximal graphic-independent subset \(I\subseteq B\).  Since
\(B\) is an \(M\)-base, \(I\) is common independent, and

\[
                         |I|=r_G(B)=q-d.              \tag{5.8}
\]

By (5.2), the maximum common-independent size is \(q\), so the exchange
digraph (5.4) has an augmenting path.  Let \(I^+\) be the resulting common
independent set of size \(q-d+1\).  Extend \(I^+\) to an \(M\)-base
\(B^+\).  Since \(I^+\subseteq B^+\) is graphic-independent,

\[
             r_G(B^+)\ge |I^+|=q-d+1,
\]

which is (5.7).  Iterate. \(\square\)

### Corollary 5.3 (when min--max becomes an interval absorber)

Under Theorem 5.2, either of the following extra atlas hypotheses is
sufficient.

1. If the protected atlas connects all decoded \(M\)-bases, then every
   initial decoded table has some atlas path to a forest table.
2. If, for every step in Theorem 5.2, the atlas contains the aggregate
   resource-zero replacement
   \((B-B^+,B^+-B)\), or realizes it by a path never dropping below
   \(r_G(B)\), then the atlas is a monotone absorber with at most the
   initial graphic deficit many strict steps.

#### Proof

Theorem 5.2 supplies a forest base in the same decoded base family.  Base
connectivity gives Item 1.  The stronger realization in Item 2 gives an
escape from every sub-full plateau; apply Theorem 3.1(3). \(\square\)

The abstract basis-exchange graph of \(M\) is connected, but this does not
by itself prove either item: a matroid basis exchange may fail to be a
listed literal interval replacement, may touch a protected collar, or may
lose a payload/state guard.  Those facts belong to the atlas hypothesis.

### Proposition 5.4 (why the lift is a genuine extra theorem)

The natural central selection problem does not meet the premise of
Theorem 5.1 merely by naming its resource rows.  Before the graphic row,
it simultaneously intersects lower-, upper-, and two bank-middle partition
constraints; in the oriented form it has the four lower/upper/tail/head
partition matroids.  These constraints do not combine into one matroid on
the natural diamond ground.  Indeed the explicit induced-five-cycle
fixture in
`MATH_THEOREM_CATALAN_FOUR_TRANSVERSAL_MATROID_AND_TURN_AUGMENTATION_20260731.md`
is not even the intersection of two matroids there.

Therefore (5.2) is available only after proving a genuine exact lifted
representation, for example a network-integral fibre of the kind required
in Corollary 2.2 of the skip-port common-base theorem.  The three-quarter
five-fibre bank is a large collection of intervals, not such a
representation.

## 6. Exact interface with the skip-port and Hoffman rows

The central graphic cycle and the later directed transition-cycle topology
are different constraints.  A central forest does not produce a skip-port
cycle cover, and a skip-port perfect transition matching does not make the
central Johnson support acyclic.

There are two safe orders of composition.

1. Perform the interval-atlas descent on the undecorated two-bank table,
   orient the final physical paths, then embed those roles in one exact
   residual owner--named-payload table and apply the skip-port theorem.
2. Work inside a fully decorated atlas in which every replacement is zero
   on the complete skip-port/resource incidence and transparent to the
   protected state menus.  Then every intermediate table remains on the
   same protected face.

The second order has an exact Hoffman test.  For a table \(B\), let its free
roles have Cartesian menus \(A_i\times H_i\) on the rotor-state set
\(V_{\rm rot}\), and let its protected boundary be \(\eta_B\), with
\(\eta_B(V_{\rm rot})=0\).  Recall

\[
 \ell_B(X)=|\{i:A_i\subseteq X\}|,\qquad
 r_B(X)=|\{i:H_i\cap X\ne\varnothing\}|.             \tag{6.1}
\]

### Lemma 6.1 (Hoffman-transparent interval exchange)

Suppose a protected interval exchange \(B\to B'\) has a bijection
\(\theta\) between the old and new free roles such that

\[
 A'_{\theta(i)}=A_i,qquad H'_{\theta(i)}=H_i
 \quad\text{for every }i,\qquad
 \eta_{B'}=\eta_B.                                  \tag{6.2}
\]

Assume also that owner, named payload, all four central labels, flag/reset
mode, and every intended guard are constant under \(\theta\).  Then

\[
  \ell_{B'}(X)-r_{B'}(X)\le\eta_{B'}(X)\quad
 \text{for all }X\subseteq V_{\rm rot}              \tag{6.3}
\]

holds if and only if it holds for \(B\).  Hence the exact integral Hoffman
state completion and its declared reset ledger survive the exchange.

#### Proof

The bijection and (6.2) make both counts in (6.1) identical for every
\(X\), and the boundary is identical.  Thus every inequality in (6.3) is
the same inequality.  The exact common-table Hoffman theorem then supplies
the integral one-copy completion.  Constancy of the listed labels makes
that completion payload- and reset-transparent. \(\square\)

If either a menu or \(\eta\) changes, Lemma 6.1 gives no conclusion: all
Hoffman cuts must be rebuilt and rechecked on the new common table.  Merely
preserving lower/upper palettes or the four scalar central counts is not
enough.  If fixed Johnson tail/head labels are variable rotor coordinates,
their injectivity must also be carried as literal matching rows or forced
by singleton menus.

## 7. Conditional circuit-complete absorber and scoped no-go

### Theorem 7.1 (protected complementary-bi-packing absorber)

Let \(B_0\) be a complementary central bi-packing with \(c\) alternating
cycle components.  Suppose a finite literal atlas is supplied such that:

1. every atlas move is a protected resource-zero or directly verified
   capacity-safe replacement in the sense of Section 1;
2. every move intended to occur after common-table insertion satisfies
   Lemma 6.1 (otherwise absorption is completed before insertion); and
3. either
   * the atlas has no sub-full plateau trap as in Theorem 3.1;
   * the bounded-load hypotheses of Theorem 4.1 hold at every such
     plateau; or
   * an exact protected matroidal lift satisfies (5.2) and the atlas has
     one of the realization properties in Corollary 5.3.

Then the atlas carries \(B_0\) to a complementary two-bank table whose
physical Johnson union is a forest.  Lower and upper palettes, all declared
middle capacities, every protected selected interval, and every resource
and reset guard included in the hypotheses survive.  The path uses at most
\(c\) strict graphic-rank improvements in the first two branches and in
the rank-filtered realization branch of Corollary 5.3(2).  The merely
connected branch of Corollary 5.3(1) guarantees a path, but not a monotone
one or this strict-step bound.

#### Proof

The first two alternatives in Item 3 exclude sub-full plateau traps.
Theorem 3.1 and Corollary 3.2 then give a final rank-\(N\) table with the
stated strict-step bound.  In the matroidal branch, Theorem 5.2 supplies a
forest base.  Corollary 5.3(1) connects to it by an arbitrary atlas path,
while Corollary 5.3(2) gives the monotone path and the same bound.  Item 1
preserves the literal static face.  Item 2 and Lemma 6.1 preserve the fixed
common-table/Hoffman face when that order of composition is used.  Finally
(1.5) identifies rank \(N\) with a central linear forest. \(\square\)

### Corollary 7.2 (proof-safe failure certificates)

Each of the following is a rigorous but scoped impossibility result.

* A full-atlas sink component without a forest proves that no sequence of
  the listed interval replacements absorbs every cycle from that component.
* A sub-full sink of the nondecreasing-rank graph proves that no monotone
  sequence of the listed replacements does so.
* A violated cut (5.3) proves that no protected forest base exists in the
  exact matroidal lift.

None is a no-go for the Catalan Linear Matching assertion unless the atlas
or lift has separately been proved complete for every literal central
table.  In particular, failure of a five-coordinate atlas proves only a
frozen-fibre obstruction.  Fixed coordinate parity is not used: the
component bipartition may be chosen from each selected two-bank graph, in
accord with the fixed-ground-bipartition obstruction.

## 8. Exact remaining construction target

To turn Theorem 7.1 into an unconditional central reset theorem, one must
supply at least one of the following, literally and uniformly in \(m\).

1. A protected interval atlas and a proof that every sub-full plateau has
   an escaping trade passing (2.3), preferably through Theorem 4.1.
2. An exact protected matroidal/network lift satisfying all cuts (5.2),
   together with an atlas realization of its augmenting base changes.
3. A complete finite-atlas obstruction: a certified sink component and a
   proof that the atlas exhausts every permitted interval replacement in
   the stated scope.

The five-coordinate Dong--Mao bank supplies none of these three facts by
itself.  Its value is as a large initial bank and as a possible source of
literal circuit candidates.  The missing theorem is precisely their
protected contracted-rank connectivity, not additional capacity
arithmetic.
