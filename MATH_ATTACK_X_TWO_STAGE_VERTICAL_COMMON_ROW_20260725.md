# Two-stage vertical contraction and the exact common-row gate

Date: 2026-07-25

## 0. Outcome

This note tests the proposed two-stage use of the proportional tight-atom
hypergraph:

1. resolve the first-order overlap into integral vertical Boolean chains;
2. contract those chains and bundle them into long common tight rows.

There are two positive exact statements.

* The vertical Boolean-chain stage is a totally unimodular Ferrers flow and
  has a zero-leave solution with every proportional floor retained exactly.
* Exact middle wreath factors give genuine common cyclic rows simultaneously
  at ranks \(m\) and \(m+1\).  After a harmless retuning of
  \(b\sim m^{3/4}\), cutting those cycles into \(b\)-start rows loses
  \(o(p/\sqrt m)\) rows.

Moreover, once atoms are genuinely restricted to contain whole compatible
selected chain arms, the adjacent-arm normalized overlap is exactly
\((b-1)/(b\,m(m+1-H))=(1+o(1))/m^2\).  Thus the intended contraction does
produce the desired second-order ratio for a specified compatible neighboring
pair.  A uniform mixed-radius contracted-row bound, and the existence and
expansion of enough aligned common rows, remain unproved.

However, these statements do not compose.  The first-order
\(O(1/m)\) correlation is not a disjoint union of per-start vertical chains.
At the two central ranks it has two cover orientations whose union is one
alternating path on all \(2b\) slots.  Every disjoint-chain contraction leaves
at least \(b-1\) cover pairs of exact normalized codegree

\[
 \frac{2b-1}{b(m+1)}=\frac{2+o(1)}m.
\]

Absorbing both orientations already contracts the whole common row.  Thus a
direct one-chain quotient does **not** expose an \(O(m^{-2})\) residual
hypergraph.  Alternatively, one may first restrict to atoms which are unions
of a preselected chain packing, but then the unrestricted degree calculation
no longer applies and a new common-row Hall theorem is required.  The
\(O(m^{-2})\) cross-slot estimate in the unrestricted atom pool supplies no
such Hall theorem.

The exact surviving gate is therefore an off-central, shift-compatible
common-row theorem.  It must choose \(p-o(p/\sqrt m)\) FIFO rows and, on each
row, synchronize the full radius profile so that all designated Boolean
targets are disjoint.  This note does not prove that theorem and therefore
does not prove the constant-one conjecture.

Throughout,

\[
 n=2m+1,\qquad W=\binom nm,
\]

\[
 H=\left\lceil\alpha\sqrt{m\log m}\right\rceil,
 \qquad \frac1{\sqrt2}<\alpha<\frac{\sqrt3}{2},
\]

and initially

\[
 b=\lfloor m^{3/4}\rfloor,\qquad
 p=\left\lfloor\frac Wb\right\rfloor,\qquad
 b_q=\left\lfloor\frac{N_q}{p}\right\rfloor,
 \qquad N_q=\binom n{m+q}.
\tag{0.1}
\]

All assertions are for sufficiently large (m).  The retuned value
(b^*\sim m^{3/4}) is introduced in Section 6.

## 1. What the (O(m^{-2})) audit says, and what it does not say

For position intervals (P,Q), put

\[
 a=|P\setminus Q|,\qquad c=|Q\setminus P|.
\]

The audited atom overlap calculation proves

\[
 \sum_{a+c\ge2}
 \frac{\operatorname{poly}(a+c)}
 {\binom{|P|}{a}\binom{n-|P|}{c}}
 =O(m^{-2}).
\tag{1.1}
\]

The excluded terms (a+c=1) are exactly Boolean cover pairs.  There are two
such interval orientations:

\[
 [i,i+r-1]\subset[i,i+r],
 \qquad
 [i,i+r-1]\subset[i-1,i+r-1].
\tag{1.2}
\]

The first keeps the left endpoint fixed and the second keeps the right
endpoint fixed.  Calling all of (1.2) “vertical” is correct at the level of
the Boolean poset, but it does not make them a disjoint family of chains.
Every interior interval has both upper covers in (1.2), and the resulting
diamonds are precisely the common-row coupling.

Thus (1.1) has the following exact logical scope:

> After every Boolean cover correlation has been absorbed, all remaining
> slot overlap is (O(m^{-2})).

It does not say that choosing one saturated chain through each target absorbs
every cover correlation.  Sections 2--3 quantify the failure already at the
central seam.

## 2. The exact central cover ladder

### Lemma 2.1 (the two central start counts)

For all sufficiently large (m),

\[
 b_0=b_1=b.
\tag{2.1}
\]

#### Proof

Write

\[
 W=pb+r,\qquad 0\le r<b.
\]

Since (p\gg b), one has (r<p), and hence

\[
 b_0=\left\lfloor\frac Wp\right\rfloor=b.
\]

Binomial symmetry in odd dimension gives (N_1=N_0=W), so (b_1=b) as
well. \(\square\)

Fix a labelled atom word (x).  Put

\[
 P_i=A_{i,0}(x)=\{x_i,\ldots,x_{i+m-1}\},
\]

\[
 U_j=A_{j,1}(x)=\{x_j,\ldots,x_{j+m}\},
 \qquad 0\le i,j<b.
\tag{2.2}
\]

### Lemma 2.2 (central ladder)

The cover graph induced by the (2b) targets in (2.2) is exactly

\[
 P_0-U_0-P_1-U_1-\cdots-P_{b-1}-U_{b-1}.
\tag{2.3}
\]

In particular, it has (2b-1) edges and is connected.

#### Proof

Because (x) is injective, containment of the target sets is equivalent to
containment of their position intervals.  An interval of length (m) is
contained in an interval of length (m+1) exactly when the latter is obtained
by adding its left or its right neighboring position.  Therefore

\[
 P_i\subset U_j
 \quad\Longleftrightarrow\quad
 j=i\ \text{or}\ j=i-1,
\]

with the evident boundary restrictions.  This is (2.3). \(\square\)

The same-left edges (P_iU_i) are the central covers inside the nominal
start-(i) column.  The edges (P_{i+1}U_i) are equally genuine cover pairs
and connect consecutive columns.

## 3. Exact cover codegree and the disjoint-chain no-go

Let

\[
 L=m+b+H
\]

be the coordinate-word length, and write

\[
 (z)_k=z(z-1)\cdots(z-k+1)
\]

for a falling factorial.

### Theorem 3.1 (exact central normalized codegree)

In the labelled proportional-atom multihypergraph, let

\[
 S\in\binom{[n]}m,\qquad
 T\in\binom{[n]}{m+1},\qquad S\subset T.
\]

Then

\[
 \deg(S)=b\,m!\,(m+1)_{b+H},
\tag{3.1}
\]

\[
 \deg(S,T)=(2b-1)m!\,(m)_{b+H-1},
\tag{3.2}
\]

and consequently

\[
 \boxed{
 \frac{\deg(S,T)}{\deg(S)}
 =\delta_b:=\frac{2b-1}{b(m+1)}}
\tag{3.3}
\]

The same-start and adjacent-start representations contribute respectively

\[
 \frac1{m+1},\qquad
 \frac{b-1}{b(m+1)}.
\tag{3.4}
\]

#### Proof

There are (b) possible middle slots for (S).  Once a slot is fixed, its
(m) positions may be ordered in (m!) ways, and the remaining (L-m=b+H)
positions receive an injective word from the (m+1) complementary
coordinates.  Distinct middle slots cannot both contain (S), so the events
are disjoint and give (3.1).

For the pair (S\subset T), a fixed oriented cover-slot pair fixes the one
coordinate in (T\setminus S).  It has

\[
 m!\,(m)_{b+H-1}
\]

word realizations.  There are (b) same-left pairs and (b-1) same-right
pairs.  No injective word is counted twice: two such representations would
either put (S) in two distinct middle slots or put the unique coordinate
(T\setminus S) in two positions.  This proves (3.2).  Dividing by (3.1)
and using

\[
 (m+1)_{b+H}=(m+1)(m)_{b+H-1}
\]

gives (3.3)--(3.4). \(\square\)

### Lemma 3.2 (exact same-rank contrast)

Let \(S,S'\in\binom{[n]}m\) be Johnson adjacent:

\[
 |S\setminus S'|=|S'\setminus S|=1.
\]

Then their exact normalized codegree in the labelled atom pool is

\[
 \boxed{
 \frac{\deg(S,S')}{\deg(S)}
 =\frac{2(b-1)}{b\,m(m+1)}
 =\Theta(m^{-2})}
\tag{3.5}
\]

#### Proof

The two sets can occupy consecutive middle slots in either orientation.
There are \(2(b-1)\) oriented slot pairs.  For a fixed orientation, the
departing coordinate in \(S\setminus S'\) and the arriving coordinate in
\(S'\setminus S\) are fixed.  The remaining positions have

\[
 (m-1)!\,(m)_{b+H-1}
\]

realizations.  Divide

\[
 2(b-1)(m-1)!\,(m)_{b+H-1}
\]

by (3.1). \(\square\)

Lemma 3.2 is the genuine cross-column second-order estimate: a middle-row
transition fixes both a departure and an arrival.  A central cover pair
fixes only the arrival, giving Theorem 3.1.  Importing Lemma 3.2 after an
arbitrary one-chain contraction therefore loses one constraint.

### Theorem 3.3 (one-chain contraction leaves first-order correlation)

Partition the (2b) central targets of one atom into blocks, each of which
is totally ordered by Boolean inclusion.  Then at most (b) edges of the
central ladder (2.3) have both endpoints in one block.  At least (b-1)
ladder edges join distinct blocks.

Consequently the average, over the (b) lower central targets, of the
normalized codegree contributed by cross-block central cover pairs is at
least

\[
 \boxed{
 \frac{b-1}{b}\,\delta_b
 =\frac{(b-1)(2b-1)}{b^2(m+1)}
 =\frac{2+o(1)}m}
\tag{3.6}
\]

In particular it is not (O(m^{-2})).

#### Proof

A chain block contains at most one rank-(m) target and at most one
rank-(m+1) target.  It therefore contains at most one edge of (2.3).  There
are at most (b) nontrivial two-rank blocks, whereas (2.3) has (2b-1)
edges.  The number of cross-block edges is at least (b-1).  Every one has
the exact normalized codegree (3.3), which gives (3.6). \(\square\)

The path (2.3) has a unique perfect matching, namely

\[
 \{P_iU_i:0\le i<b\}.
\]

Thus even the optimal disjoint two-rank chain contraction absorbs one cover
orientation and leaves the other.  If an equivalence relation is instead
required to absorb **every** ladder edge, connectedness of (2.3) puts all
(2b) slots in one equivalence class.  That class is not a Boolean chain;
it is already the common alternating row.

### Corollary 3.4 (aggregate incidence ledger)

Suppose (p-t) pairwise target-disjoint atoms are chosen, where

\[
 t=o(p/\sqrt m).
\]

Under any disjoint-chain partition of their central targets, at least

\[
 (p-t)(b-1)=W-o(W/\sqrt m)
\tag{3.7}
\]

distinct central ladder incidences remain cross-chain.

#### Proof

The atoms are target-disjoint, so their ladder pairs are distinct.  Apply
Theorem 3.3 in every atom.  Also

\[
 pb=W+O(b),\qquad p=O(W/b)=o(W/\sqrt m),
\]

and

\[
 tb=o(W/\sqrt m).
\]

These identities give (3.7). \(\square\)

### Scope of the no-go

Theorem 3.3 closes a direct quotient argument: one cannot take the full atom
pool, contract a disjoint vertical chain system, and then cite (1.1) as an
(O(m^{-2})) bound between distinct contracted columns.

There is a logically different operation.  One may first choose a disjoint
Boolean-chain packing and then **discard every atom which is not a union of
those selected chain segments**.  The surviving row hypergraph can have very
different degrees and codegrees.  Theorem 3.3 does not say that this
restricted hypergraph has no large matching.  It says that the unrestricted
atom overlap calculation does not prove that it does.  Establishing adequate
degrees, Hall expansion, and long FIFO paths after this restriction is
exactly the new common-row theorem.

The restriction really can recover the second-order scale at the central
seam.  The following exact count separates it from the invalid raw quotient.

### Lemma 3.5 (aligned dominoes restore the second anchor)

Fix

\[
 A\in\binom{[n]}m,\qquad
 a\in A,\qquad c,d\notin A,\qquad c\ne d,
\]

and the two oriented central dominoes

\[
 C=(A\subset A\cup\{c\}),
\]

\[
 D=(A-\{a\}+\{d\}\subset A\cup\{d\}).
\tag{3.8}
\]

Require \(C\) to occupy one same-start column and \(D\) the immediately
preceding same-start column of the same labelled atom.  Conditioned on a
fixed eligible slot for \(C\), the exact ratio of the joint event to the
\(C\)-event is

\[
 \frac1{m^2}.
\tag{3.9}
\]

After pooling over the \(b\) possible slots of \(C\), the exact ratio is

\[
 \boxed{\frac{b-1}{b\,m^2}}
\tag{3.10}
\]

#### Proof

At a fixed slot, the domino \(C\) has

\[
 m!\,(m)_{b+H-1}
\]

labelled word realizations.  Adding the predecessor domino \(D\) fixes the
departing coordinate \(d\), the location of \(a\) at the opposite end of
the middle window, and leaves

\[
 (m-1)!\,(m-1)_{b+H-2}
\]

realizations.  Their ratio is

\[
 \frac{(m-1)!}{m!}\,
 \frac{(m-1)_{b+H-2}}{(m)_{b+H-1}}
 =\frac1{m^2}.
\]

There are \(b\) possible slots for \(C\) and \(b-1\) with an eligible
predecessor, proving (3.10). \(\square\)

Thus a restriction to atoms containing whole selected dominoes introduces
the missing departure constraint and genuinely changes \(1/m\) to
\(1/m^2\).  What remains unproved is that a selected integral chain system
retains enough mutually compatible dominoes, and higher flags, to support
the required long rows.  Codegree improves only after the common-row
support itself has been shown to exist.

The same gain survives a growing vertical arm.

### Lemma 3.6 (exact aligned \(H\)-arm count)

Fix one compatible right-oriented chain arm

\[
 C=(A_{i,0}\subset A_{i,1}\subset\cdots\subset A_{i,H})
\]

at a specified start.  Its labelled slot degree is

\[
 d_{\rm slot}(C)=m!\,(m+1-H)_b.
\tag{3.11}
\]

Fix also the compatible right-oriented arm \(D\) at the immediately
preceding start.  Then

\[
 d_{\rm slot}(C,D)=(m-1)!\,(m-H)_{b-1},
\tag{3.12}
\]

and hence

\[
 \boxed{
 \frac{d_{\rm slot}(C,D)}{d_{\rm slot}(C)}
 =\frac1{m(m+1-H)}}
\tag{3.13}
\]

Pooling over all starts gives

\[
 \boxed{
 \frac{b-1}{b\,m(m+1-H)}
 =\frac{1+o(1)}{m^2}}
\tag{3.14}
\]

#### Proof

The arm \(C\) fixes an unordered \(m\)-set in its middle window and the
ordered \(H\) coordinates added on its right.  Of the \(L=m+b+H\) word
positions, \(b\) remain, and they receive an injective word from
\(m+1-H\) unused coordinates.  This proves (3.11).

The predecessor arm shares \(H-1\) of the ordered right additions with
\(C\).  Relative to \(C\), it fixes one departing middle coordinate and one
new left coordinate.  Thus there are \((m-1)!\) orders of the middle core
and \(b-1\) free positions chosen from \(m-H\) unused coordinates, proving
(3.12).  Finally,

\[
 (m+1-H)_b=(m+1-H)(m-H)_{b-1},
\]

which gives (3.13); only \(b-1\) of the \(b\) pooled current starts have a
predecessor. \(\square\)

The left-oriented equal-depth arm has the symmetric count.  Lemma 3.6
verifies the desired \(m^{-2}\) conditional ratio for this specified
neighboring pair even for \(H\to\infty\), because \(H=o(m)\).  It does not
give a uniform maximum codegree or row-sum bound for every mixed-radius pair,
nor a lower bound on the number of arms from an independently chosen SCD
which participate in one long shift-compatible row.

If one could prove a comparable \(O(m^{-2})\) bound uniformly for all
\(O(b^2)\) relevant arm pairs in a contracted row, the prospective
union-bound scale would be

\[
 b^2\frac1{m(m+1-H)}
 =(1+o(1))m^{-1/2}.
\tag{3.15}
\]

That uniform premise is **UNPROVED**.  Even under it, a bare pair count lands
at the required square-root boundary, not at its necessary little-\(o\)
improvement.  The gain beyond (3.15) would still have to come from common-row
expansion, a structured absorber, or an exact factorization.

## 4. The exact integral vertical stage is totally unimodular

Define the proportional radius counts

\[
 a_d=b_{-d}-b_{-(d+1)}\quad(0\le d<H),
 \qquad a_H=b_{-H}.
\tag{4.1}
\]

Then

\[
 b_q=\sum_{d\ge\rho(q)}a_d,
 \qquad \rho(q)=\max\{-q,q-1\}.
\tag{4.2}
\]

Fix any symmetric-chain decomposition \(\mathscr C\) of \(B_{2m+1}\).  A
chain has radius (r) when its endpoint ranks are (m-r) and (m+r+1).

### Theorem 4.1 (exact TU vertical contraction)

There is an integral choice of (pa_d) distinct SCD chains for every
(0\le d\le H), each chosen chain having radius at least (d).  Truncating
such a chain to its central radius-(d) segment gives pairwise
vertex-disjoint vertical segments whose occupancy at rank (m+q) is exactly

\[
 p b_q.
\tag{4.3}
\]

The unused rank-(m+q) capacity is exactly

\[
 R_q=N_q-pb_q,\qquad 0\le R_q<p.
\tag{4.4}
\]

#### Proof

Make a bipartite network with radius-demand nodes \(d=0,\ldots,H\) and one
capacity-one node for every chain \(C\in\mathscr C\).  Join \(d\) to \(C\)
when the radius of (C) is at least (d), and give node (d) demand
(pa_d).

The neighborhoods of the demand nodes are nested.  An SCD chain has radius
at least (d) exactly when it meets rank (m-d); every such chain meets that
rank once.  Hence

\[
 \#\{C\in\mathscr C:\operatorname{rad}(C)\ge d\}=N_{-d}.
\tag{4.5}
\]

The only threshold Hall inequalities are

\[
 p\sum_{e=d}^H a_e
 =p b_{-d}
 \le N_{-d}.
\tag{4.6}
\]

They hold by the definition of (b_{-d}).  The bipartite incidence matrix,
with source and sink rows appended, is a network matrix and is totally
unimodular.  Thus the feasible fractional flow has an integral realization.

The retained segment of type (d) meets rank (m+q) exactly when
(d\ge\rho(q)).  Equations (4.2) and (4.6) therefore give (4.3), and (4.4)
is the defining floor remainder. \(\square\)

Theorem 4.1 proves the complete vertical capacity statement with zero bundle
loss.  Arbitrarily partitioning each radius class into (p) groups of size
(a_d) gives (p) abstract proportional bundles.  It does not order those
segments into physical rows.

## 5. Exact formulation of the common-row theorem

### 5.1 The central matching quotient

Every full SCD determines a perfect matching (M) from rank (m) to rank
(m+1): (M(S)) is the next member of the SCD chain through (S).
Define a directed graph (D_M) on (inom{[n]}m) by

\[
 S\longrightarrow T
 \quad\Longleftrightarrow\quad
 T\subset M(S),\qquad T\ne S.
\tag{5.1}
\]

### Lemma 5.1 (exact regularity)

(D_M) is loopless and has indegree and outdegree exactly (m) at every
vertex.

#### Proof

The ((m+1))-set (M(S)) contains (m+1) middle sets, one of which is
(S).  This gives (m) outgoing arcs.

For a fixed (T), there are (m+1) upper sets containing it.  Exactly one
is (M(T)).  Every other such upper set (U) has a unique predecessor
(S=M^{-1}(U)\ne T), and (5.1) gives the arc (S\to T).  Thus there are
exactly (m) incoming arcs. \(\square\)

A directed path in (D_M) is an alternating path of selected vertical
matching edges and the second cover orientation.  Regularity is only a
one-seam fact; it does not imply the required long simple FIFO path factor.

### 5.2 Exact FIFO criterion at the middle rank

Let

\[
 T_{i+1}=T_i-\{z_i\}+\{y_i\},
 \qquad 0\le i<\ell-1,
\tag{5.2}
\]

be a tight Johnson path of (m)-sets.

### Lemma 5.2 (FIFO word criterion)

Assume \(\ell\le m+1\).  There is an injective coordinate word

\[
 x_0,x_1,\ldots,x_{m+\ell-2}
\]

such that

\[
 T_i=\{x_i,\ldots,x_{i+m-1}\}
\tag{5.3}
\]

for every (i) if and only if all symbols

\[
 z_0,\ldots,z_{\ell-2},y_0,\ldots,y_{\ell-2}
\tag{5.4}
\]

are pairwise distinct.

#### Proof

Necessity follows from (5.3): (z_i=x_i) and (y_i=x_{m+i}).

Conversely, repeated use of (5.2) gives

\[
 T_i=
 \left(T_0\setminus\{z_0,\ldots,z_{i-1}\}\right)
 \mathbin{\dot\cup}
 \{y_0,\ldots,y_{i-1}\}.
\tag{5.5}
\]

Pairwise distinctness implies that every (z_i) is an as-yet undeleted
member of (T_0), while every (y_i) lies outside (T_0).  Order (T_0)
with \(z_0,\ldots,z_{\ell-2}\) first, followed by its remaining elements,
and append \(y_0,\ldots,y_{\ell-2}\).  The resulting word is injective and
its successive length-(m) windows are (5.5). \(\square\)

For a path in (D_M), one has

\[
 y_i=M(T_i)\setminus T_i,\qquad
 z_i=M(T_i)\setminus T_{i+1}.
\tag{5.6}
\]

Thus Lemma 5.2 is the exact no-return condition which an alternating path
must satisfy before it is a physical tight row.

### 5.3 Full radius flags

Let a selected radius-(d_i) segment through (T_i) be

\[
 C_i^{-d_i}\subset C_i^{-d_i+1}\subset\cdots
 \subset C_i^{d_i+1},
 \qquad |C_i^q|=m+q,\qquad C_i^0=T_i.
\tag{5.7}
\]

For \(-d_i\le r\le d_i\), let \(\lambda_{i,r}\) be the unique coordinate
added in

\[
 C_i^r\subset C_i^{r+1}.
\tag{5.8}
\]

If these segments are columns of one proportional atom, there is one
coordinate sequence

\[
 y_{-H},y_{-H+1},\ldots,y_{b+H-1}
\tag{5.9}
\]

such that

\[
 \boxed{\lambda_{i,r}=y_{i+r}
 \quad(-d_i\le r\le d_i)}
\tag{5.10}
\]

In particular adjacent addition words obey the exact overlap law

\[
 \lambda_{i,r}=\lambda_{i+1,r-1}
\tag{5.11}
\]

whenever both sides are defined.

For the converse, the boundary data must also be retained; shift overlap
alone is not enough.  Suppose, in addition to the middle FIFO criterion and
(5.10), that

\[
 y_{-H},\ldots,y_{-1}
\]

are distinct members of (T_0), disjoint from all departures
(z_0,\ldots,z_{b-2}), and that

\[
 y_0,\ldots,y_{b+H-1}
\]

are distinct coordinates outside (T_0), disjoint from every preceding
symbol.  Order the coordinate word as follows:

\[
 x_i=z_i\quad(0\le i<b-1),
\]

fill positions \(b-1,\ldots,m-H-1\) with the remaining elements of \(T_0\),
put

\[
 x_{m+j}=y_j\quad(-H\le j\le b+H-1).
\tag{5.12}
\]

The counts are exact because

\[
 |T_0\setminus
   (\{z_0,\ldots,z_{b-2}\}\cup\{y_{-H},\ldots,y_{-1}\})|
 =m-b-H+1.
\]

This reconstructs an injective word of length

\[
 m+b+H.
\tag{5.13}
\]

It is the word used in the proportional-atom reduction.  Equation (5.10)
then gives, for every window present in the word and after the standard
cyclic tight completion at the left boundary,

\[
 C_i^{-q}=\bigcap_{j=0}^qT_{i-j},
 \qquad
 C_i^q=\bigcup_{j=0}^qT_{i+j},
\qquad
 0\le q\le d_i\ \text{on the left},\quad
 0\le q\le d_i+1\ \text{on the right}
\tag{5.14}
\]

The negative-index middle windows in the first intersection are interpreted
through the standard cyclic tight completion.  The designated targets
themselves remain the literal finite-word intervals specified by (5.7)--(5.12).

This is the exact extra condition absent from Theorem 4.1.  Nested chains
which are independently integral need not satisfy (5.11).

### 5.4 Necessary Hall hierarchy

Let \(\Gamma\) be a family of \(V\) contracted chain instances and let
\(\mathcal R\) be any directed compatibility relation whose simple
\(b\)-vertex paths are valid common rows.  Suppose \(k\) vertex-disjoint
rows cover \(kb\) instances, and put

\[
 L=V-kb.
\]

### Proposition 5.3 (one-step and multistep Hall deficiencies)

Let \(\operatorname{def}(\mathcal R)\) be the maximum Hall deficiency in
the bipartite graph formed from a left and a right copy of \(\Gamma\).  Then

\[
 \operatorname{def}(\mathcal R)\le L+k.
\tag{5.15}
\]

More generally, let \(\mathcal R_r\) join the endpoints of every admissible
\(r\)-transition row fragment.  For \(1\le r<b\),

\[
 \operatorname{def}(\mathcal R_r)\le L+kr.
\tag{5.16}
\]

#### Proof

The (b-1) consecutive arcs in each selected row form a bipartite matching,
and the rows are vertex-disjoint.  Its size is (k(b-1)=V-L-k).  The
deficiency form of Hall's theorem gives (5.15).

Likewise, the pairs of positions at distance (r) give a bipartite matching
of size (k(b-r)=V-L-kr), proving (5.16). \(\square\)

At the target scale

\[
 V=pb,\qquad k=p-t,\qquad t=o(p/\sqrt m),
\]

one has

\[
 L=tb=o(W/\sqrt m),\qquad k=o(W/\sqrt m).
\tag{5.17}
\]

Consequently (5.15) requires deficiency (o(W/\sqrt m)).  Equation
(5.16) requires the same for every

\[
 r=o(b/\sqrt m)=o(m^{1/4}).
\tag{5.18}
\]

For a preassigned (p)-by-(b) layered system, each individual seam must
have deficiency at most

\[
 t=o(p/\sqrt m).
\tag{5.19}
\]

An (O(m^{-2})) normalized codegree estimate is not a Hall-deficiency
bound and does not imply any of (5.15)--(5.19).

Even zero one-step Hall deficiency is insufficient: a disjoint union of
directed cycles of length (b-1) has a perfect one-step matching but contains
no simple (b)-vertex path.  If weak components have sizes (s_j), every
component-confined (b)-path packing leaves at least

\[
 \sum_j(s_j\bmod b)
\tag{5.20}
\]

vertices.  A valid common-row theorem must therefore supply higher-order
FIFO expansion or an equivalent global chronology, not just independent
seam matchings.

## 6. Positive common rows at the two central ranks

This section uses the frozen theorem that exact middle wreath factors
exist.  Let

\[
 \operatorname{Cat}_m=\frac Wn.
\tag{6.1}
\]

An exact factor consists of \(\operatorname{Cat}_m\) cyclic coordinate
orders, and their cyclic intervals of length (m) partition
(inom{[n]}m).

### Theorem 6.1 (exact two-rank common-row factor)

For each wreath (pi=(x_0,\ldots,x_{n-1})), with indices modulo (n), put

\[
 P_{\pi,j}=\{x_j,\ldots,x_{j+m-1}\},
\]

\[
 U_{\pi,j}=\{x_j,\ldots,x_{j+m}\}.
\tag{6.2}
\]

Over all factor rows and all (j), the (P_{\pi,j}) partition rank (m),
the (U_{\pi,j}) partition rank (m+1), and

\[
 P_{\pi,j}-U_{\pi,j}-P_{\pi,j+1}
\tag{6.3}
\]

forms a vertex-disjoint union of alternating cycles (C_{2n}).

#### Proof

The rank-(m) assertion is exact middle-factor ownership.  Also

\[
 U_{\pi,j}^{\,c}
 =P_{\pi,j+m+1}.
\tag{6.4}
\]

Complementation is a bijection from rank (m+1) to rank (m), so (6.4)
proves the rank-(m+1) partition.  Both containments in (6.3) are literal.
Distinctness of the interval owners gives the disjoint (C_{2n}) components.
\(\square\)

Thus the two central cover orientations can be integrated, but only as
whole common wreath rows rather than independent chains.

### 6.1 Exact cutting ledger for the frozen value of (b)

Write

\[
 n=qb+r,\qquad 0\le r<b.
\tag{6.5}
\]

Cut every wreath cycle into \(q\) disjoint \(b\)-start segments.  Since
\(m+b+H<n\), each segment and its Gaussian-band lookahead use distinct
coordinates and hence define a valid labelled atom candidate.  At the two
central ranks these candidates are target-disjoint.

In fact all candidates cut from one wreath are mutually target-disjoint
through the full Gaussian band.  At a fixed rank, two of their designated
targets are cyclic intervals of the same proper length with different
starts.  Two such intervals cannot have the same coordinate set: a proper
nonempty cyclic arc is determined by its two boundary edges.  Targets at
different ranks have different cardinalities.  Therefore every collision
among the cut candidates comes from two different wreath parents.

The number of row-confined candidates is exactly

\[
 s_{\rm cut}=\operatorname{Cat}_m q.
\tag{6.6}
\]

Since (W=n\operatorname{Cat}_m),

\[
 p=\left\lfloor\frac Wb\right\rfloor
 =\operatorname{Cat}_m q
  +\left\lfloor\frac{\operatorname{Cat}_m r}{b}\right\rfloor.
\]

Hence the exact row deficit is

\[
 \boxed{
 t_{\rm cut}
 =p-s_{\rm cut}
 =\left\lfloor\frac{\operatorname{Cat}_m r}{b}\right\rfloor}
\tag{6.7}
\]

As (m\to\infty),

\[
 \frac{t_{\rm cut}}{p/\sqrt m}
 =\frac{r\sqrt m}{n}+o(1).
\tag{6.8}
\]

Therefore independent cutting of the exact wreaths attains the target
(t=o(p/\sqrt m)) exactly when

\[
 n\bmod b=o(\sqrt m).
\tag{6.9}
\]

This is not uniform for \(b=\lfloor m^{3/4}\rfloor\).  For example, take

\[
 m=t^4+t^3.
\tag{6.10}
\]

The binomial expansion gives

\[
 b=t^3+\tfrac34t^2+O(t),\qquad
 q=2t,\qquad
 r=\tfrac12t^3+O(t^2)=(\tfrac12+o(1))b.
\tag{6.11}
\]

Thus the ratio in (6.8) is

\[
 (\tfrac14+o(1))m^{1/4}\longrightarrow\infty.
\tag{6.12}
\]

By contrast, \(m=t^4\) gives \(b=t^3\) and \(r=1\).  The frozen cutting
loss is arithmetic, not geometric.

### 6.2 Retuning (b) removes the arithmetic loss

Put

\[
 Q=\left\lceil\frac{n}{m^{3/4}}\right\rceil,
 \qquad
 b^*=\left\lfloor\frac nQ\right\rfloor.
\tag{6.13}
\]

Then

\[
 b^*\sim m^{3/4},\qquad Q=O(m^{1/4}).
\tag{6.14}
\]

Write

\[
 n=Qb^*+r^*,\qquad 0\le r^*<Q.
\tag{6.15}
\]

For large \(m\), \(Q<b^*\), so \(\lfloor n/b^*\rfloor=Q\).  Repeating
(6.7) with

\[
 p^*=\left\lfloor\frac W{b^*}\right\rfloor
\]

gives

\[
 t^*_{\rm cut}
 =\left\lfloor\frac{\operatorname{Cat}_m r^*}{b^*}\right\rfloor
 =O(\operatorname{Cat}_m m^{-1/2}).
\tag{6.16}
\]

On the other hand,

\[
 \frac{p^*}{\sqrt m}
 =(2+o(1))\operatorname{Cat}_m m^{-1/4}.
\tag{6.17}
\]

Consequently

\[
 \boxed{t^*_{\rm cut}=o(p^*/\sqrt m)}
\tag{6.18}
\]

The proportional-atom Gaussian reduction is unchanged by this retuning.
Indeed,

\[
 b^*\sim m^{3/4},\qquad b^*+H<m,
\]

\[
 \min_q b_q=m^{3/4-\alpha^2+o(1)}\to\infty,
\]

and

\[
 \frac{H}{b^*}=o(1).
\]

All floor, overlap, literal-length, repair, and Gaussian-tail estimates use
only these properties.  Thus the two central ranks and independent-cycle
cutting arithmetic can both be solved at the required scale.

### 6.3 Exact limitation

Theorem 6.1 says nothing about distinct ownership at ranks

\[
 m+q,\qquad q\notin\{0,1\}.
\]

Within one wreath, the row-induced radius-\(d\) chains are target-disjoint,
as proved above.  Chains belonging to different wreaths may share
off-central targets.  Thus the retuned construction reduces the remaining
problem to a genuinely cross-parent selection or switching theorem: retain
all but \(o(p^*/\sqrt m)\) of the cut rows while eliminating every
cross-wreath off-central collision and preserving the common coordinate
rows.  This is precisely the missing labelled common-row synchronization
theorem.  It is strictly stronger than the abstract TU packing in
Theorem 4.1.

## 7. Consequence for the four-cube cross-parent construction

The verified four-cube shell and macro-packet words are literal MTF/OR
chronologies.  They are not injective coordinate words of the form required
by Lemma 5.2, and their seams have not been proved to obey (5.10).  In
particular, an MTF state reset or a reversal of a chain coordinate is not a
tight-row connector.

There is an exact local reason that mere regrouping inside compact product
parents cannot repair this.

### Proposition 7.1 (FIFO run bound in a product parent)

Let (P) be an affine product of saturated Boolean chain segments on
disjoint coordinate supports, with side heights

\[
 h_1,\ldots,h_d,
 \qquad S=\sum_{j=1}^d h_j.
\]

If

\[
 T_0,T_1,\ldots,T_{\ell-1}
\]

is a consecutive run of middle windows from one injective tight row and all
of them lie in (P), then

\[
 \boxed{\ell\le\left\lfloor\frac S2\right\rfloor+1}
\tag{7.1}
\]

#### Proof

In product coordinates, a tight same-rank Boolean transition decreases one
chain coordinate by one and increases another by one.  Its
\(\ell_1\)-variation is therefore two.

No chain coordinate can reverse direction during a FIFO row.  If a
coordinate first decreases and later increases across the same saturated
chain edge, the later step reintroduces the Boolean coordinate previously
removed.  If it first increases and later decreases, the later step removes
a coordinate which entered during the row.  Both contradict Lemma 5.2.

Thus every product coordinate is monotone, and the total coordinate
variation is at most \(S\).  The \(\ell-1\) transitions have total variation
\(2(\ell-1)\), proving (7.1). \(\square\)

For an equal four-cube parent of side height (R), this gives

\[
 \ell\le2R+1.
\tag{7.2}
\]

For compact Boolean SCD parents with total active height (O(\sqrt m)), one
parent supplies only (O(\sqrt m)) consecutive windows, whereas a
proportional row requires

\[
 b\asymp m^{3/4}.
\]

Thus every such row must cross many parent seams.  If all selected middle
targets lie in parents with (S\le C\sqrt m), the number (J) of genuine
parent changes among (k) disjoint (b)-window rows satisfies the exact
run count

\[
 J\ge
 \frac{kb}{\lfloor C\sqrt m/2\rfloor+1}-k.
\tag{7.3}
\]

At (k=p-o(p/\sqrt m)), this is

\[
 J\ge\left(\frac2C-o(1)\right)\frac W{\sqrt m}.
\tag{7.4}
\]

If only a compact sector is used, the same count applies to its maximal
same-parent runs, with entries and exits of that sector charged as seams.

The prior four-cube words prove neither the FIFO seam criterion nor the
short-range Hall hierarchy (5.15)--(5.19) for these
\(\Theta(W/\sqrt m)\) passages.  Their exact OR coverage therefore cannot be
relabelled as a proportional-atom common-row factor.

## 8. Final proved and conditional boundary

### Proved

1. The complete proportional radius profile admits an exact zero-leave
   integral vertical-chain packing by the TU flow of Theorem 4.1.
2. Every \(O(1/m)\) atom overlap is a Boolean cover correlation, but those
   correlations have two orientations.  At the central ranks they form the
   connected ladder (2.3).
3. Every central cover pair has exact normalized labelled codegree
   \((2b-1)/(b(m+1))\).
4. Any disjoint-chain contraction leaves at least \(b-1\) first-order cover
   pairs per atom.  Absorbing all of them contracts the whole common row.
5. For a specified compatible pair of neighboring aligned dominoes, or
   equal-depth right \(H\)-arms, restriction to whole chains gives an exact
   \((1+o(1))m^{-2}\) conditional ratio.  A uniform mixed-radius contracted
   row-sum theorem and survival of enough rows remain unproved.
6. Exact middle wreath factors solve the two central ranks in common cyclic
   rows.
7. The frozen-\(b\) independent cutting loss is exactly (6.7), and it is not
   uniformly below \(p/\sqrt m\).
8. Retuning \(b\sim m^{3/4}\) by (6.13) makes the central cutting loss
   \(o(p/\sqrt m)\) without changing any proportional-reduction asymptotic.
9. Any full common-row factor must satisfy the FIFO law, the shifted flag
   overlap (5.10), and the multistep Hall hierarchy (5.15)--(5.20).
10. A compact product parent supplies only \(O(\sqrt m)\) consecutive windows
   of a FIFO row, so the four-cube route needs a genuinely global seam
   theorem.

### Unproved lemma

> **Shift-compatible proportional common-row theorem — UNPROVED.**  For the
> retuned \(b^*\sim m^{3/4}\), select \(p^*-o(p^*/\sqrt m)\) pairwise
> target-disjoint families of vertical segments, each family containing
> exactly \(a_d\) radius-\(d\) segments for every \(d\le H\), such that every
> family satisfies one injective FIFO word, uses the prescribed start classes
> \(J_d\), and obeys the exact shifted identities (5.10)--(5.14).

This theorem is equivalent to the needed proportional-atom matching after
the harmless retuning of \(b\).  The TU vertical theorem and the central
wreath-row theorem verify its two separate projections, but no argument here
couples them.

### Implication scope

If the unproved theorem held, the exact literal length and repair ledger of
`PROPORTIONAL_TIGHT_ATOM_GAUSSIAN_REDUCTION_20260725.md` would give

\[
 \nu(2m+1)\le(1+o(1))W.
\]

Nothing proved in this note establishes that theorem, MWB, labelled
common-owner synchronization, or the constant-one conjecture.  The sharp
new obstruction is architectural: independent vertical chains do not
remove the first-order correlation, while removing it completely already
requires the common rows one hoped to construct in the second stage.
