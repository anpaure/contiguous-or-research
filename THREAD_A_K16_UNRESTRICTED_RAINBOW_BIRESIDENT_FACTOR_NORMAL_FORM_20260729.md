# The unrestricted K16 rainbow biresident factor: circulation normal form and exact integral gate

Date: 2026-07-29

Status: global theorem and obstruction audit.  The requested spanning
two-factor is neither constructed nor refuted.  This note proves:

1. an exact memory-three circulation formulation equivalent to the full
   unrestricted object;
2. a symmetric fractional solution with exact palette load \(9/8\);
3. every scalar, point-degree, Boolean-star cut, parity, and run-capacity
   ledger is integrally compatible;
4. a complement-quotient reduction to one common Kneser/Johnson edge set;
5. an unconditional construction for the one-sided residence variant from
   the two audited \(k=15\) factors;
6. exact quota-first Hall and Tutte sufficient theorems; and
7. precise reasons ordinary matroid intersection, matroid parity, and one
   fixed pair-cube frame do not close the integral problem.

No finite search, SAT, or heavy computation is used.

## 1. The physical object and its exact local law

Put

\[
\Omega=[16],\qquad
\mathcal V=\binom{\Omega}{8},\qquad
N=|\mathcal V|=\binom{16}{8}=12870.
\tag{1.1}
\]

The Johnson graph

\[
J=J(16,8)
\]

is \(64\)-regular and has

\[
|E(J)|=\frac{12870\cdot64}{2}=411840
\tag{1.2}
\]

edges.  For \(e=XY\), define its two colours and its swap label by

\[
\lambda(e)=X\cap Y\in\binom{\Omega}{7},\qquad
\upsilon(e)=X\cup Y\in\binom{\Omega}{9},\qquad
\sigma(e)=X\triangle Y\in\binom{\Omega}{2}.
\tag{1.3}
\]

There are

\[
C=\binom{16}{7}=\binom{16}{9}=11440
\tag{1.4}
\]

colours on each shore.  For fixed \(R\) of rank seven, its providers are
the \(\binom92=36\) edges of the complete graph on the nine middle
supersets of \(R\).  The same count holds for a fixed rank-nine upper
colour.

Orient every component of a spanning two-factor \(F\), writing

\[
X_{i+1}=X_i-\{a_i\}+\{b_i\},\qquad
\sigma_i=\{a_i,b_i\}.
\tag{1.5}
\]

The strict convention is used: a constant cyclic trace is one run of the
component length.  If an implementation intentionally exempts
coordinate-constant components, the only change below is to omit the
constant-cycle motifs from Section 4; all nonconstant cooldown,
circulation, palette, and Hall statements are unchanged.

### Theorem 1.1 (cooldown, geodesic, and residence equivalence)

The following are equivalent.

1. Every cyclic one-run and every cyclic zero-run of every coordinate has
   length at least four.
2. On every factor component,
   \[
   \sigma_i\cap\sigma_j=\varnothing
   \quad\text{whenever}\quad
   1\le d_{\rm cyc}(i,j)\le3.
   \tag{1.6}
   \]
3. Every four consecutive factor transitions are geodesic:
   \[
   d_J(X_i,X_{i+t})=t\qquad(1\le t\le4).
   \tag{1.7}
   \]

In particular every component has length at least eight.  If its length
\(L\) lies between eight and fifteen, exactly \(L\) coordinates vary on
that component, and each varying coordinate has one one-run and one
zero-run.

#### Proof

A coordinate changes exactly on transitions whose swap label contains it.
Two consecutive changes at cyclic separation \(s\) bound alternately a
one-run and a zero-run of length \(s\).  Thus all such separations are at
least four exactly when (1.6) holds.

Under (1.6), the first \(t\le4\) swaps remove \(t\) distinct currently
present coordinates and insert \(t\) distinct absent coordinates.  Their
net symmetric difference has size \(2t\), proving (1.7).  Conversely,
reusing a coordinate among four consecutive swaps cancels one change and
makes the Johnson distance smaller than the number of transitions.

Every nontrivial component varies in some coordinate, whose one-run and
zero-run have total length \(L\), so \(L\ge8\).  If \(8\le L\le15\), each
varying coordinate has at most \(\lfloor L/8\rfloor=1\) run.  Every
transition changes two coordinates, so if \(r_x\) denotes the number of
nonconstant one-runs of coordinate \(x\),

\[
2\sum_xr_x=2L.
\]

Hence exactly \(L\) coordinates vary.  \(\square\)

The full run-and-gap hypothesis is essential.  Rows excluding only
patterns \(0\,1^\ell\,0\), \(1\le\ell\le3\), enforce positive residence
only.  Full biresidence also needs the complementary patterns
\(1\,0^\ell\,1\).

## 2. The one-sided unrestricted factor is already constructible

Let \(z\) be one coordinate and identify

\[
\Omega=[15]\mathbin{\dot\cup}\{z\}.
\]

The middle layer splits into

\[
\mathcal A=\binom{[15]}8,\qquad
\mathcal B=\{\{z\}\cup R:R\in\binom{[15]}7\}.
\tag{2.1}
\]

Two independently audited \(k=15\) factors are available.

* \(F^+\subset J(15,8)\) has physical cycle lengths \(6390,45\), covers
  both immediate colour palettes, and every coordinate one-run has length
  at least four.
* \(F^-\subset J(15,8)\) has 26 physical components, minimum component
  length sixteen, covers both immediate colour palettes, and every
  coordinate zero-run has length at least four.

The first is the saved all-depth factor

\[
\text{from3\_markov\_s7\_merge.best.json};
\]

the second is the audited seed-seven factor in

\[
\text{MATH\_CERTIFICATE\_K15\_FIXED\_M0\_ZERO\_RESIDENT\_DOUBLE\_SHADOW\_SEED7\_20260729.md}.
\]

### Theorem 2.1 (asymmetric-shore positive-residence construction)

Put \(F^+\) on the \(\mathcal A\) shore.  For every edge \(PQ\in F^-\),
put on the \(\mathcal B\) shore the edge

\[
(\{z\}\cup\bar P)(\{z\}\cup\bar Q),
\tag{2.2}
\]

where complements are inside \([15]\).  Their disjoint union is a spanning
two-factor of \(J(16,8)\) which:

1. covers every rank-seven lower and every rank-nine upper colour; and
2. has every positive coordinate run of length at least four.

#### Proof

The two shores partition all rank-eight owners, and complementation
preserves Johnson adjacency and degree two.

On \(\mathcal A\), the lower and upper colours are those of \(F^+\), hence
cover all targets not containing \(z\).  On \(\mathcal B\),

\[
\begin{aligned}
(\{z\}\cup\bar P)\cap(\{z\}\cup\bar Q)
 &=\{z\}\cup\overline{P\cup Q},\\
(\{z\}\cup\bar P)\cup(\{z\}\cup\bar Q)
 &=\{z\}\cup\overline{P\cap Q}.
\end{aligned}
\tag{2.3}
\]

Upper completeness and lower completeness of \(F^-\) therefore give all
lower and upper colours containing \(z\).

For an old coordinate, the trace on a \(\mathcal B\) component is the
bitwise complement of its trace in \(F^-\).  Its positive runs are exactly
the zero-runs of \(F^-\), hence have length at least four.  The
\(\mathcal A\) traces are positive-resident by the property of \(F^+\).
The \(z\)-trace is constant on every shore component, whose length is at
least sixteen on \(\mathcal B\) and at least 45 on \(\mathcal A\).
\(\square\)

This theorem does not solve the present task.  The \(\mathcal A\) factor
has 2010 short zero-gaps, while \(F^-\) has 855 short positive runs, which
become short zero-gaps on \(\mathcal B\).  It proves a useful scope
correction:

> A dynamic CEGAR system containing only positive-run closures is already
> feasible globally.  Equivalence with the requested run-and-gap object
> requires both signs of every residence motif.

## 3. Exact load, point, parity, and cut ledgers

For a factor \(F\), put

\[
l_R=|\{e\in F:\lambda(e)=R\}|,\qquad
u_U=|\{e\in F:\upsilon(e)=U\}|.
\tag{3.1}
\]

### Theorem 3.1 (load and coordinate-run identities)

If both palettes are complete, then

\[
\sum_R(l_R-1)=\sum_U(u_U-1)=12870-11440=1430.
\tag{3.2}
\]

If \(F\) is biresident through four, then

\[
1\le l_R,u_U\le4.
\tag{3.3}
\]

Let \(r_x\) be half the number of selected edges whose swap label contains
\(x\), equivalently the number of nonconstant one-runs of \(x\).  Then

\[
\sum_xr_x=12870
\tag{3.4}
\]

and

\[
\boxed{
\sum_{R\ni x}(l_R-1)=1430-r_x,\qquad
\sum_{U\ni x}(u_U-1)=r_x.}
\tag{3.5}
\]

Consequently

\[
0\le r_x\le1430.
\tag{3.6}
\]

Every palette has at least 10010 singleton-provider colours, and at least

\[
10010+10010-12870=7150
\tag{3.7}
\]

factor edges are simultaneously unique providers of both their lower and
upper colours.

#### Proof

Equation (3.2) is total edge count minus total colour count.

For fixed lower colour \(R\), its 36 providers form a \(K_9\) on the nine
middle supersets of \(R\).  Two selected provider edges sharing a middle
vertex give a local trace \(0,1,0\) in the coordinate missing from \(R\).
Thus the selected providers form a matching and there are at most four.
The upper statement is dual, using a local \(1,0,1\) gap.

Each selected edge changes two coordinates, proving (3.4).  There are
6435 middle vertices containing \(x\).  Orient the factor.  Exactly \(r_x\)
outgoing transitions delete \(x\), so the selected edges whose lower
colour contains \(x\) number \(6435-r_x\).  Likewise the edges whose upper
colour contains \(x\) number \(6435+r_x\).  Subtract the baseline counts

\[
\binom{15}{6}=5005,\qquad\binom{15}{8}=6435
\]

to obtain (3.5).

Since the total excess is 1430, at most 1430 colours on either shore can
have load at least two.  Hence at least \(11440-1430=10010\) are
singletons.  Inclusion-exclusion on the 12870 selected edges gives (3.7).
\(\square\)

For each coordinate, the number of odd one-runs and the number of odd
zero-runs are odd, because each family has total length 6435.  This gives
no contradiction to (3.4)--(3.6).

### Theorem 3.2 (all Boolean-star cut identities)

For \(T\subseteq\Omega\), \(|T|=s\le7\), put

\[
V_T=\{X\in\mathcal V:T\subseteq X\}.
\]

Then

\[
\sum_{R\supseteq T}l_R
=
\binom{16-s}{8-s}-\frac12\delta_F(V_T).
\tag{3.8}
\]

Lower coverage therefore forces

\[
\delta_F(V_T)\le2D_s,\qquad
D_s=\binom{16-s}{8-s}-\binom{16-s}{7-s}.
\tag{3.9}
\]

The same bound holds for the middle vertices avoiding \(T\), by upper
coverage.  Explicitly,

\[
(D_1,\ldots,D_7)=(1430,1001,572,275,110,35,8).
\tag{3.10}
\]

#### Proof

An edge is internal to \(V_T\) exactly when its lower intersection contains
\(T\).  Sum degree two over \(V_T\):

\[
2|V_T|=2e_F(V_T)+\delta_F(V_T).
\]

Substitute \(e_F(V_T)=\sum_{R\supseteq T}l_R\).  Coverage supplies at least
one edge for each of the \(\binom{16-s}{7-s}\) such lower colours, proving
(3.9).  Complementation proves the upper version.  \(\square\)

Every displayed cut is even, as it must be for a two-factor.

### Proposition 3.3 (integer scalar compatibility)

There are integral load and run-length data satisfying all scalar load,
point-degree, parity, and run-capacity identities above, with all colour
loads at most two and all run and gap lengths at least four.

#### Proof

Choose a \(1430\)-element family
\(\mathcal S\subseteq\binom{\Omega}{7}\) whose coordinate degrees differ
by at most one.  Such a family exists: among all \(1430\)-element families,
minimize the sum of squared coordinate degrees.  If
\(d_i\ge d_j+2\), some selected set containing \(i\) but not \(j\) has its
\(i\)-to-\(j\) swap unselected; otherwise the swap bijection would give
\(d_i\le d_j\).  Performing that swap lowers the squared sum, a
contradiction.

Since the total degree is \(7\cdot1430=10010\), ten coordinates have degree
626 and six have degree 625.  Put

\[
l_R=1+1_{\{R\in\mathcal S\}},\qquad
u_U=1+1_{\{\bar U\in\mathcal S\}}.
\tag{3.11}
\]

Equations (3.5) then prescribe \(r_x=804\) on the ten coordinates and
\(r_x=805\) on the other six.

For \(r_x=804\), partition 6435 as 803 parts of length eight and one part
of length eleven.  For \(r_x=805\), use 803 parts of length eight, one of
length four, and one of length seven.  Use the same partitions for the zero
gaps.  Every part is at least four and each list has an odd number of
odd-length parts.  \(\square\)

This is a scalar realization, not a Johnson chronology.  It proves that
load integrality, parity, and run capacity cannot refute the object.

## 4. Exact complement and fractional-factor formulations

Let \(\mathcal M\) be the family of every forbidden physical cyclic
residence closure: the edge sets of simple paths, including paths crossing
a chosen cyclic seam, with coordinate patterns

\[
0\,1^\ell\,0\quad\text{or}\quad1\,0^\ell\,1,
\qquad1\le\ell\le3,
\tag{4.1}
\]

together with the full edge set of every ambient cycle of length below four
on which some coordinate is constant.

### Theorem 4.1 (deleted-edge normal form)

A spanning factor \(F\) has both palettes and full residence if and only if
\(D=E(J)\setminus F\) satisfies

\[
d_D(X)=62\qquad(X\in\mathcal V),
\tag{4.2}
\]

\[
|D\cap E_R^-|\le35,\qquad
|D\cap E_U^+|\le35
\tag{4.3}
\]

for every lower and upper colour, and

\[
D\cap M\ne\varnothing\qquad(M\in\mathcal M).
\tag{4.4}
\]

#### Proof

Equation (4.2) is the complement of degree two in a 64-regular graph.
Each colour has 36 providers, so (4.3) is precisely survival of at least
one.  A residence violation persists exactly when all edges of its closure
are selected, which is equivalent to failure of (4.4).  \(\square\)

The two systems (4.3) are partition-matroid capacities on \(D\);
(4.2) is an exact \(62\)-factor constraint; and (4.4) is a rank-at-most-four
transversal system.  Their conjunction is not ordinary matroid
intersection.

### Theorem 4.2 (strict fractional feasibility)

The natural exact-factor, palette, and residence-motif relaxation has a
common fractional point.  Namely,

\[
d_e=\frac{31}{32}\qquad(e\in E(J)).
\tag{4.5}
\]

It has exact degree 62, colour load

\[
36\cdot\frac{31}{32}=34+\frac78<35,
\tag{4.6}
\]

and for every motif of at least two edges,

\[
\sum_{e\in M}d_e\ge\frac{62}{32}>1.
\tag{4.7}
\]

Moreover (4.5) lies in the exact \(62\)-factor polytope.

#### Proof

The numerical assertions are immediate.  Every even-regular graph has a
two-factorization: orient an Euler tour in each component, split each
vertex into an outgoing and incoming copy, decompose the resulting regular
bipartite graph into perfect matchings, and recombine the copies.  Thus
\(J\) is the disjoint union of 32 two-factors.  Averaging their complements
gives (4.5) inside the exact \(62\)-factor polytope.  \(\square\)

Hence no fractional Hall, Tutte, blossom, palette-capacity, or static motif
cut separates the target.

## 5. The exact legal-history circulation

Let \(\mathcal H_3\) be the directed graph whose states are legal directed
three-edge histories

\[
h=(X_0,X_1,X_2,X_3)
\tag{5.1}
\]

whose three swap labels are pairwise disjoint.  There is a state arc

\[
(X_0,X_1,X_2,X_3)\longrightarrow(X_1,X_2,X_3,X_4)
\tag{5.2}
\]

exactly when the fourth swap label is disjoint from the preceding three.
The projected physical transition of this state arc is \(X_3X_4\).

### Lemma 5.1 (regularity)

Every state has exactly 25 successors and 25 predecessors.  There are

\[
(8)_3^2=64\cdot49\cdot36
\tag{5.3}
\]

states ending at each owner \(X\).

#### Proof

After three disjoint swaps, the three inserted coordinates are distinct
members of \(X_3\), while the three deleted coordinates are distinct
members of its complement.  The next deletion has five legal current
choices and the next insertion has five legal absent choices.  Reversal
gives the predecessor count.

Working backwards from \(X_3\), an ordered choice of three distinct current
and three distinct absent coordinates uniquely reconstructs the history,
giving (5.3).  \(\square\)

### Theorem 5.2 (IRRC16 equivalence)

The requested unrestricted factor exists if and only if there is a binary
circulation \(y\) on \(\mathcal H_3\) satisfying

\[
\sum_{a\in\delta^+(h)}y_a
=
\sum_{a\in\delta^-(h)}y_a
\qquad(h\in V(\mathcal H_3)),
\tag{5.4}
\]

\[
\sum_{\substack{a:\ {\rm terminal}({\rm tail}(a))=X}}y_a=1
\qquad(X\in\mathcal V),
\tag{5.5}
\]

and

\[
\sum_{a:\lambda(\pi(a))=R}y_a\ge1,\qquad
\sum_{a:\upsilon(\pi(a))=U}y_a\ge1
\tag{5.6}
\]

for every rank-seven \(R\) and rank-nine \(U\), where \(\pi(a)\) is the
projected transition.

#### Proof

Orient a required factor and slide a three-edge window around each
component.  Theorem 1.1 makes every resulting state and state arc legal.
Every state has one selected predecessor and successor along its lifted
component, giving (5.4), while each physical owner is the terminal owner of
exactly one selected transition, giving (5.5).  The palette conditions give
(5.6).

Conversely, an integral circulation decomposes into directed state cycles.
Equation (5.5) permits exactly one selected outgoing state arc over all
histories ending at each owner.  Flow conservation supplies exactly one
incoming transition there.  Hence the projection is a spanning directed
cycle cover of the physical owners.  The legal memory-three transitions
give Theorem 1.1, including across the wraparound of every projected state
cycle; in particular every projected component has length at least eight.
Condition (5.6) gives both palettes.  Immediate reversal is illegal, so no
undirected edge is used twice.  \(\square\)

### Theorem 5.3 (chronology-aware fractional point)

Assign every state arc the weight

\[
y_a=\frac1{25(8)_3^2}.
\tag{5.7}
\]

Then (5.4)--(5.5) hold exactly.  Every oriented Johnson transition has
projected weight \(1/64\), every undirected edge has weight \(1/32\), and
every lower and upper colour has load

\[
36\cdot\frac1{32}=\frac98.
\tag{5.8}
\]

#### Proof

Regularity proves flow conservation and (5.5).  Fix an oriented transition
\(X\to Y\).  Compatible preceding histories choose ordered triples from
the seven current coordinates not deleted and the seven absent coordinates
not inserted.  Their number is \((7)_3^2\).  Therefore its projected weight
is

\[
\frac{(7)_3^2}{25(8)_3^2}
=\frac{(5/8)^2}{25}
=\frac1{64}.
\]

There are two orientations per undirected edge and 36 providers per
colour.  \(\square\)

This is stronger than Theorem 4.2: even the exact chronology-aware
circulation has uniform palette slack \(1/8\).  The missing phenomenon is
integral owner-fibre and palette rounding.

## 6. The complement-quotient common-edge reduction

Complementation \(\kappa(X)=\bar X\) acts freely on the middle vertices and
edges.  Let

\[
Q=J(16,8)/\langle\kappa\rangle.
\]

It has 6435 vertices and is 64-regular.

Let

\[
K=KG(16,7)
\]

be the Kneser graph on rank-seven sets, joining disjoint pairs.  It has
11440 vertices and is 36-regular.

### Theorem 6.1 (canonical common edge set)

There is a canonical bijection

\[
E(K)\longleftrightarrow E(Q).
\tag{6.1}
\]

If \(R,S\) are disjoint rank-seven sets and

\[
\Omega\setminus(R\cup S)=\{a,b\},
\tag{6.2}
\]

the corresponding quotient edge joins

\[
[R\cup\{a\}]\quad\text{to}\quad[R\cup\{b\}].
\tag{6.3}
\]

For \(H\) in this common edge set, its physical lift is a
complement-invariant spanning two-factor if and only if

\[
d_Q(v)=2\qquad(v\in V(Q)).
\tag{6.4}
\]

It covers both physical palettes if and only if

\[
d_K(R)\ge1\qquad(R\in V(K)).
\tag{6.5}
\]

Finally it is biresident through four if and only if, along every actual
physical lift component of every \(Q\)-cycle, consecutive selected edges
whose leftover pair (6.2) contains the same coordinate have cyclic
separation at least four.  (A quotient cycle can lift to two physical
cycles or to one cycle of twice the quotient length.)

#### Proof

The physical Johnson edge

\[
(R+a)(R+b)
\]

has lower colour \(R\) and upper colour \(\bar S\).  Its complement is

\[
(S+a)(S+b),
\]

with lower colour \(S\) and upper colour \(\bar R\).  This constructs
(6.1), and reversing the construction proves bijectivity.

Quotient degree two lifts to degree two at each of the two complementary
physical owners, proving (6.4).  An incident \(K\)-edge supplies lower
colour \(R\) and, on its complementary lift, upper colour \(\bar R\).
Thus (6.5) is exactly simultaneous palette coverage.

The two physical lift edges change precisely the coordinates \(a,b\).
Theorem 1.1 therefore becomes the stated cooldown rule.  \(\square\)

The direct PBBS even-factor theorem supplies an integral \(H\) satisfying
(6.4)--(6.5), so the static common-edge problem is already solved.  Its old
coordinate traces do not satisfy cooldown.

The exact surviving complement-invariant sufficient lemma is:

> **CQC16.**  The common edge set \(E(K)=E(Q)\) contains a subgraph with
> \(d_Q=2\), \(d_K\ge1\), and leftover-pair cooldown four on every quotient
> cycle.

CQC16 would prove the requested unrestricted factor.  It is a sufficient
symmetry subclass, whereas Theorem 5.2 is equivalent to the unrestricted
problem.

The uniform common-edge weight \(1/32\) gives

\[
d_Q=2,\qquad d_K=\frac{36}{32}=\frac98,
\tag{6.6}
\]

so this symmetry-reduced problem also has no fractional degree or palette
cut.

Every change between two solutions of \(d_Q=2\) is a degree-balanced
integer circulation in \(Q\), hence is a signed sum of alternating circuits.
Thus the exact switch version of CQC16 is: find such a circuit sum from the
PBBS scaffold which keeps every \(K\)-degree positive and destroys every
distance-one, -two, and -three leftover-pair collision.  This is an exact
statement, not a claim that bounded circuits suffice.

## 7. Why standard matroid methods stop

### Proposition 7.1 (colour rows destroy two-factor integrality)

Let \(P_1,P_2,P_3\) be the three perfect matchings of \(K_4\), treated as
three colour classes.  Every spanning two-factor of \(K_4\) is

\[
E(K_4)\setminus P_i
\]

for one \(i\), and therefore misses one colour.  The fractional point

\[
x_e=\frac23
\]

has degree two and load \(4/3\) on every colour.

Thus even the exact two-factor polytope need not remain integral after
colour-cover rows.

### Proposition 7.2 (residence-safe partial sets are not a matroid)

Let

\[
\begin{aligned}
X_0&=\{1,3,5,6,7,8,9,10\},\\
X_1&=\{2,3,5,6,7,8,9,10\},\\
X_2&=\{3,4,5,6,7,8,9,10\},\\
X_3&=\{3,5,6,7,8,9,10,11\},
\end{aligned}
\]

and \(e_i=X_{i-1}X_i\).  Their swap labels are

\[
\{1,2\},\qquad\{2,4\},\qquad\{4,11\}.
\tag{7.1}
\]

The sets \(\{e_2\}\) and \(\{e_1,e_3\}\) contain no forbidden consecutive
pair.  Adding either edge of the latter to the former creates a
length-one run, in coordinate two or four.  Hence augmentation fails.
\(\square\)

Ordinary matroid parity also does not apply: a physical edge simultaneously
uses its two owner incidences and one incidence on each colour shore, a
four-resource block rather than a pair.

### Proposition 7.3 (uniform duplicate regularization is impossible)

Suppose one tries to use each lower colour once, duplicate exactly 1430
lower colours, and require every middle owner to lie in exactly one
duplicated lower star.  If \(e_R\in\{0,1\}\) records the duplicated colours,
the required equations are

\[
\sum_{R\subset X}e_R=1\qquad
\left(X\in\binom{\Omega}{8}\right),
\qquad
\sum_Re_R=1430.
\tag{7.2}
\]

This system has no integral solution.

#### Proof

Fix a coordinate \(x\), and put

\[
d_x=\sum_{R\ni x}e_R.
\]

Sum the first equations in (7.2) over the 6435 middle sets containing
\(x\).  A selected \(R\) containing \(x\) occurs in all nine of its middle
supersets, whereas a selected \(R\) avoiding \(x\) occurs in exactly one
such superset.  Hence

\[
6435=9d_x+(1430-d_x)=1430+8d_x,
\]

which would give \(d_x=5005/8\).  \(\square\)

Thus a direct regular duplication followed by a regular-graph
factorization cannot prove the theorem; owner loads must be nonuniform or
the palette witnesses must be chosen jointly with the completion.

### Proposition 7.4 (one fixed pair frame is impossible)

Partition \(\Omega\) into eight fixed pairs and allow only swaps inside one
pair.  Let \(X\) be a transversal owner, containing one point of every
pair.  For each pair \(p\), put

\[
R_p=X\setminus\{x_p\}.
\]

Within this restricted edge set, \(R_p\) has exactly one provider: the
pair-\(p\) flip incident with \(X\).  Covering all eight colours \(R_p\)
forces all eight restricted edges incident with \(X\), contradicting
degree two.  Globally, the 256 transversal owners determine 1024 distinct
colours of this form, and their 1024 unique providers are exactly all edges
of the transversal \(Q_8\); a two-factor on those owners could use only 256
of them.  Thus at least 768 of these colours require providers outside the
fixed-pair cell, and any cube construction needs genuinely mixed frames.

## 8. Quota-first global sufficient theorems

Form the 36-regular bipartite flag graph

\[
\mathcal B:
\binom{\Omega}{7}\longleftrightarrow\binom{\Omega}{9},
\qquad R\sim U\iff R\subset U.
\tag{8.1}
\]

The flag \(R\subset U\), with \(|U\setminus R|=2\), corresponds to the
unique Johnson edge between its two rank-eight intermediate sets.

Regular bipartite Hall gives a perfect matching of \(\mathcal B\), hence
an abstract choice of exactly one physical provider of every lower and
every upper colour.  The first unresolved rounding condition is whether
such a perfect matching can satisfy

\[
\sum_{R\subset X\subset U}p_{R,U}\le2
\qquad(X\in\mathcal V).
\tag{8.2}
\]

The symmetric fractional matching \(p_{R,U}=1/36\) has middle load

\[
\frac{64}{36}=\frac{16}{9}<2.
\tag{8.3}
\]

No integral capacity-two rounding theorem is known.

### Theorem 8.1 (P9 rainbow-forest Hall theorem)

Suppose a perfect matching of \(\mathcal B\) has a Johnson image \(P\)
which partitions the 12870 middle vertices into 1430 oriented paths, each
with eight edges, and suppose that within each path any two internal swap
labels at edge distance at most three are disjoint.

Build a bipartite directed connector graph with a left copy of the path
terminals and a right copy of the path initials.  Retain a connector from
the terminal of one path to the initial of a path (possibly the same path)
precisely when it is a Johnson edge and all nine cross-seam label
comparisons are disjoint:

1. the connector against the previous three and next three labels;
2. the last old label against the first and second new labels; and
3. the penultimate old label against the first new label.

If this \(1430\) by \(1430\) connector graph satisfies Hall, then the
desired unrestricted spanning two-factor exists.

#### Proof

The perfect colour matching gives one permanent witness of every lower and
upper colour.  The path arithmetic is exact:

\[
12870=9\cdot1430,\qquad11440=8\cdot1430.
\tag{8.4}
\]

A connector perfect matching gives every terminal one successor and every
initial one predecessor, hence closes the paths into a spanning two-factor.
There are exactly eight internal path edges between consecutive connectors,
so no four-edge residence window contains two connectors.  Internal windows
are safe by hypothesis, and every remaining window is one of the nine seam
tests.  \(\square\)

The nine set-disjointness tests are the same as the eighteen directed
deletion/insertion inequalities.

### Theorem 8.2 (quota-first Tutte completion)

More generally, let \(P\) cover every lower and upper colour and satisfy
\(d_P(v)\le2\).  Let \(A\supseteq P\) be an edge support containing no
complete forbidden cyclic residence closure (including the constant-cycle
closures of Section 4), put

\[
H=A\setminus P,\qquad b(v)=2-d_P(v),
\]

so that \(b:V(H)\to\{0,1,2\}\) is integral,

and for disjoint \(S,T\subseteq\mathcal V\), let \(q_b(S,T)\) count the
components \(C\) of \(H-(S\cup T)\) for which

\[
b(C)+e_H(C,T)
\]

is odd.  If

\[
b(S)+\sum_{v\in T}\bigl(d_{H-S}(v)-b(v)\bigr)
-q_b(S,T)\ge0
\tag{8.5}
\]

for every disjoint \(S,T\), then a desired factor exists.

#### Proof

Equation (8.5) is the exact Tutte \(b\)-factor criterion.  It supplies
\(N\subseteq H\) with \(d_N(v)=b(v)\).  Thus \(P\cup N\) has degree two,
retains every quota witness in \(P\), and is resident because it lies in
the motif-free support \(A\).  \(\square\)

Theorem 8.2 isolates the totally integral final stage.  The non-Tutte step
is selecting the common colour witnesses and a sufficiently rich
motif-free support simultaneously.

## 9. Exact remaining lemma

There is no proved existence theorem and no counting/parity obstruction.
The exact unrestricted missing statement is:

> **IRRC16.**  The 25-regular legal history graph \(\mathcal H_3\) has a
> binary circulation satisfying one unit in every terminal-owner fibre and
> positive projected load on all 11440 lower and all 11440 upper colours.

By Theorem 5.2, IRRC16 is equivalent to the requested spanning two-factor.
It has the strict symmetric fractional solution (5.7), with palette load
\(9/8\), so no proof based only on fractional Hall, ordinary blossom cuts,
point degrees, or local motif capacity can close it.

Within the quota-first route, the earliest independent sublemma is the
capacity-two perfect matching (8.2).  Within the complement-invariant
route, it is CQC16.  Neither is known.

Accordingly the current \(407675/411840\)-edge UNKNOWN result has no
mathematical force in either direction.  The global barrier is integral
history-colour rounding, not the stale failed-literal count and not a
bounded repair of one scaffold.

## 10. Adversarial boundary audit

The exact equivalence in Theorem 5.2 uses all three ingredients:
statewise flow conservation, one unit in every terminal-owner fibre, and
both projected palette inequalities.  Dropping any one of them permits,
respectively, broken chronology, repeated or omitted owners, or colour
holes.  The uniform point in Theorem 5.3 proves only fractional feasibility;
the \(K_4\) example in Proposition 7.1 shows why it cannot be rounded merely
by invoking the ordinary two-factor polytope.

Proposition 3.3 is deliberately only a scalar compatibility result; it
does not realize the Boolean-star cuts by a Johnson chronology.  CQC16 is
only a complement-invariant sufficient subclass, not an equivalent
reduction.  Theorems 8.1 and 8.2 are conditional sufficient theorems:
neither asserts existence of its rainbow forest or motif-free support.
Finally, the \(407675\)-edge retained finite catalogue is not used as a
global bound and no conclusion is inferred from its current UNKNOWN
status.
