# Two-coordinate side forests as turn braids, and the first physical capacity cut

Date: 2026-07-31  
Lane: R, integral `a=1` balanced-subcube recursion  
Status: exact all-parameter reformulation, an all-parameter canonical-BTK
obstruction, a smallest-parameter literal child/common-basis counterexample
to "incidence implies physical degree," and a literal smallest-parameter
obstruction to arbitrary prescribed anchor pairings.  No all-parameter
side-forest existence theorem is claimed.

## 0. Scope after the automatic common-basis theorem

Fix `n>=3`, a `2n`-set `Omega`, and a Catalan linear matching `F` on the
rank-`n` layer.  Orient every path of `F`.  For an edge `e` write

\[
 t(e),h(e)\in\binom\Omega n,\qquad
 \ell(e)=t(e)\cap h(e),\qquad u(e)=t(e)\cup h(e).
\]

The maps

\[
 \ell:E(F)\longrightarrow\binom\Omega{n-1},\qquad
 u:E(F)\longrightarrow\binom\Omega{n+1}
\]

are bijections.  Put

\[
\begin{aligned}
 K&=\operatorname {Cat}_n,&
 N&=|E(F)|=\binom{2n}{n-1},\\
 P&=\binom{2n}{n-2},&
 C&=\operatorname {Cat}_{n+1}=\binom{2n}{n}-P.
\end{aligned}
\]

Let `Q subset E(F)` be a common deletion basis of order `C`, whose
existence for `n>=4` is supplied by the automatic common-basis theorem.
The two punctured middle banks are

\[
 D^- =\binom\Omega n\setminus t(Q),\qquad
 D^+ =\binom\Omega n\setminus h(Q),                  \tag{0.1}
\]

and both have order `P`.  The side-anchor banks are `u(Q)` and `ell(Q)`.
Incidence existence is now closed; this note concerns only physical degree
and forest topology.

## 1. Exact turn-forest equivalence

Define the **upper turn graph** `T^-_F` on vertex set `E(F)` by joining
distinct `e,f` exactly when `u(e),u(f)` are Johnson adjacent.  Give such an
edge its two turn colours

\[
 \lambda^-(ef)=u(e)\cap u(f)\in\binom\Omega n,
 \qquad
 \upsilon^-(ef)=u(e)\cup u(f)\in\binom\Omega{n+2}.    \tag{1.1}
\]

Define the **lower turn graph** `T^+_F` analogously, joining `e,f` when
`ell(e),ell(f)` are Johnson adjacent, with colours

\[
 \lambda^+(ef)=\ell(e)\cap\ell(f)\in\binom\Omega{n-2},
 \qquad
 \upsilon^+(ef)=\ell(e)\cup\ell(f)\in\binom\Omega n. \tag{1.2}
\]

### Theorem 1.1 (anchored two-colour turn-forest normal form)

For fixed `F,Q`, an upper punctured diagonal side forest exists if and
only if `T^-_F` contains a spanning linear forest `H^-` such that

1. `lambda^-` maps `E(H^-)` bijectively onto `D^-`;
2. `upsilon^-` maps `E(H^-)` bijectively onto
   `binom(Omega,n+2)`; and
3. `deg_(H^-)(q)<=1` for every `q in Q`.

The lower punctured diagonal side forest exists if and only if `T^+_F`
contains a spanning linear forest `H^+` such that

1. `lambda^+` maps `E(H^+)` bijectively onto
   `binom(Omega,n-2)`;
2. `upsilon^+` maps `E(H^+)` bijectively onto `D^+`; and
3. `deg_(H^+)(q)<=1` for every `q in Q`.

Each forest necessarily has

\[
        P\text{ edges and }N-P=C-K\text{ components}. \tag{1.3}
\]

#### Proof

Consider the upper shore.  A diagonal incidence `d subset V`, with
`|d|=n` and `|V|=n+2`, has precisely two intermediate rank-`n+1` sets,
say `X,Y`.  Its physical realization is the Johnson edge `XY`, and

\[
                  X\cap Y=d,\qquad X\cup Y=V.         \tag{1.4}
\]

Because `u` is a bijection, write uniquely `X=u(e),Y=u(f)`.  Equation
(1.4) says exactly that `ef` is an edge of `T^-_F` with turn colours
`(d,V)`.  Thus a perfect diagonal incidence selection is the same as an
edge set whose two turn-colour maps have the stated images.  Physical
maximum degree two and acyclicity say exactly that this edge set is a
linear forest.  A side vertex `u(q)`, `q in Q`, receives one additional
cross-sector seam, so its side degree must be at most one; under the
bijection `u` this is condition 3.  This proves both directions.

The lower statement is the complemented argument with (1.2).  Finally a
forest on `N` vertices with `P` edges has `N-P` components. `square`

Equivalently, each side is a collection of sequences of child-edge
occurrences.  Consecutive occurrences must be adjacent in the relevant
turn graph, their two turn-colour streams must be rainbow with the exact
prescribed images, and every deleted occurrence `q in Q` may occur only at
a sequence endpoint (or as a singleton).  This is the exact symbolic
**path/ear braid** left after common-basis incidence is removed.

There is an equivalent two-SDR form which is sometimes better suited to an
SCD recursion.

### Corollary 1.2 (oriented two-SDR/strict-potential form)

The lower side forest is equivalent to maps

\[
 t,h:\binom\Omega{n-2}\longrightarrow\binom\Omega{n-1}             \tag{1.5}
\]

such that, for every `A`,

\[
 A=t(A)\cap h(A),\qquad e(A):=t(A)\cup h(A)\in D^+,               \tag{1.6}
\]

and all of the following hold:

1. `t`, `h`, and `e` are injective (so `e` is a bijection onto `D^+`);
2. the directed graph with arcs `t(A)->h(A)` is acyclic; and
3. the lower anchor bank `ell(Q)` is disjoint from
   `im(t) intersect im(h)`.

The upper side has the complemented form.  In particular, acyclicity in
condition 2 follows from any strict potential `phi` on the rank-`(n-1)`
vertices satisfying

\[
                         \phi(t(A))<\phi(h(A))\quad\hbox{for all }A. \tag{1.7}
\]

#### Proof

Orient every path component of a lower side forest.  Index its edges by
their distinct rank-`(n-2)` intersection colours `A`, and let `t(A),h(A)`
be the directed endpoints.  Outdegree and indegree at most one are exactly
the injectivity of `t` and `h`; upper-colour bijectivity is exactly the
injectivity and prescribed image of `e`; the forest condition is exactly
directed acyclicity.  An anchor has side degree two exactly when it lies in
both images, proving condition 3.  Conversely these conditions give a
maximum-degree-two acyclic physical support with both palettes exact and
every anchor of degree at most one.  A strict potential excludes directed
cycles. `square`

## 2. Socket count and the guarded capacity cut

### Lemma 2.1 (socket count)

Let `H` be a spanning linear forest on `N` vertices with `P` edges, hence
`h=N-P=C-K` components, and let `i` be its number of isolated vertices.
Then the number of vertices of degree at most one is

\[
                         2h-i.                         \tag{2.1}
\]

Consequently an arbitrarily relabelled bank of `C` distinct anchors can be
placed only if

\[
                         i\le C-2K.                    \tag{2.2}
\]

For a fixed anchor bank, of course every anchor itself must belong to this
socket set.

#### Proof

Every nonisolated path component supplies two degree-one vertices, while
an isolate supplies one degree-zero vertex.  Thus the count is
`2(h-i)+i=2h-i`.  Requiring at least `C` sockets and using `h=C-K` gives
(2.2). `square`

The next cut remains valid after arbitrary forced-row propagation in a
diagonal matching problem.

### Lemma 2.2 (residual endpoint-capacity cut)

Fix a partial diagonal matching `mu_0` and delete its used lower and upper
colours.  Let `W` be a set of residual upper targets.  Suppose every
remaining candidate for every target in `W` has both physical intermediate
vertices in a set `S`.  Give a side vertex capacity

\[
 b_X=1\quad(X\text{ is an anchor}),\qquad
 b_X=2\quad(X\text{ is not an anchor}).               \tag{2.3}
\]

Then every degree-feasible completion satisfies

\[
                    2|W|\le\sum_{X\in S}b_X.          \tag{2.4}
\]

#### Proof

Each selected diagonal for a target of `W` contributes two distinct
physical endpoint incidences, both in `S`.  The degree constraints bound
their total by the right side of (2.4). `square`

This is a physical cut, not an inclusion-Hall cut: it can fail even when a
containment perfect matching exists.

There is also a cut which depends only on the anchor bank.

### Corollary 2.3 (complete-target anchor-shadow cut)

Let `B subset binom(Omega,n+1)` be the upper anchor bank and let

\[
 \mathcal A(B)=\{V\in\tbinom\Omega{n+2}:
                  \tbinom V{n+1}\subseteq B\}.        \tag{2.5}
\]

Every anchor-capped upper side satisfies

\[
                         2|\mathcal A(B)|\le |B|.      \tag{2.6}
\]

#### Proof

Both physical intermediate endpoints of every realization of a target
`V in A(B)` are rank-`(n+1)` facets of `V`, hence belong to `B`.  Each such
target consumes two distinct anchor incidences, while every anchor has
capacity one. `square`

For example, at `n=7` let `B` be the first
`C=Cat_8=1430` rank-eight sets in colex order on `[14]`.  Its Macaulay
decomposition is

\[
1430=\binom{13}8+\binom{10}7+\binom76+\binom65+
     \binom54+\binom43+\binom22.                       \tag{2.7}
\]

The clique transform for an initial colex segment therefore gives

\[
 |\mathcal A(B)|=
 \binom{13}9+\binom{10}8+\binom77+\binom66+
 \binom55+\binom44=764.                                \tag{2.8}
\]

Thus `1528>1430`, and no side forest can use this prescribed anchor bank,
independently of its lower palette or forest cycles.  For the analogous
colex banks at `n=3,4,5,6`, the clique counts are respectively
`4,14,54,204`, so this particular inequality first fails at `n=7`.
This is an obstruction to arbitrary prescribed anchor banks; the displayed
colex bank is not asserted to come from a favorable common basis of a
literal child forest.

## 3. The smallest strict physical obstruction

Work at `n=3` on `Omega={0,1,2,3,4,5}` and write subsets as hexadecimal
bitmasks.  Let

```text
D = {07,0b,0d,0e,13,23},
B = binom(Omega,4) minus {0f}.
```

Thus every rank-four physical vertex except `0f` is an anchor.  There is a
perfect containment matching from `D` to all six rank-five targets:

```text
0d->3d, 0e->3e, 07->37, 0b->3b, 13->1f, 23->2f.
```

### Theorem 3.1 (incidence-perfect but degree-impossible)

No containment perfect matching from `D` to the rank-five targets has a
physical lift satisfying the anchor degree caps (2.3).  In particular no
side forest exists for these one-shore data.

#### Proof

Target `3d` contains only `0d` from `D`, and target `3e` contains only
`0e`; those two assignments are forced.  Remove their rows and columns.
The residual lower bank and target bank are

```text
{07,0b,13,23},             {1f,2f,37,3b}.
```

Every physical intermediate endpoint of every residual candidate lies in

```text
S={0f,17,1b,27,2b,33}.
```

Indeed the complete residual table is

```text
1f: 07->{0f,17}, 0b->{0f,1b}, 13->{17,1b};
2f: 07->{0f,27}, 0b->{0f,2b}, 23->{27,2b};
37: 07->{17,27}, 13->{17,33}, 23->{27,33};
3b: 0b->{1b,2b}, 13->{1b,33}, 23->{2b,33}.
```

Only `0f` is not an anchor, so the total capacity of `S` is

\[
                        2+5=7.
\]

Four residual physical edges require eight incidences.  Lemma 2.2 gives
the contradiction. `square`

This is not merely abstract one-shore data.  It is induced by the following
literal child Catalan forest, with every path oriented left to right:

```text
34-15-07-0b
16-26-2a-29-19-13
2c-25-23
38-1c-0d
31-32-1a-0e.
```

Its fifteen `(lower colour, upper colour, physical edge)` records are

```text
(03,0f,07-0b) (05,17,07-15) (21,27,23-25)
(11,1b,13-19) (28,2b,29-2a) (30,33,31-32)
(0c,1d,0d-1c) (24,2d,25-2c) (14,35,15-34)
(09,39,19-29) (0a,1e,0e-1a) (22,2e,26-2a)
(06,36,16-26) (12,3a,1a-32) (18,3c,1c-38).
```

The lower entries are all fifteen rank-two masks, the upper entries all
fifteen rank-four masks, and the support is visibly five vertex-disjoint
paths spanning all twenty rank-three masks.  Hence it is a literal
parameter-three Catalan linear matching.

Let `q_0=(03,0f,07-0b)` and `Q=E(F) minus {q_0}`.  The tails of `Q` are
exactly the fourteen rank-three masks outside `D`, so (0.1) gives the
displayed `D^-`.  Likewise `u(Q)` is every rank-four mask except `0f`, so
it gives the displayed anchor bank `B`.  The opposite punctured bank is

```text
D^+={0b,16,2c,31,34,38}.
```

It has the explicit downward containment matching

```text
01->31, 02->16, 04->34, 08->0b, 10->38, 20->2c.
```

Thus `Q` is a genuine two-sided common deletion basis, while its upper
side has no degree-capped physical representative.  Even a literal child,
a synchronized common basis, and both incidence matchings do not force the
side-degree row.  This does **not** prove that the child forest lacks some
other, physically favorable common basis.

## 4. Canonical BTK branches in every later parameter

Use the LSB scan convention: scan coordinates `0,1,...,2n-1`, treat `0`
as an opening symbol, and pair each `1` with the latest unmatched `0`.
The canonical BTK diagonal matches the rank-`n` and rank-`n+2` members of
every chain that reaches both ranks; its physical edge joins the two
rank-`n+1` intermediates.

Let the scan word

\[
                       X_n=1110(10)^{n-2}.             \tag{4.1}
\]

It has rank `n+1`.

### Theorem 4.1 (uniform canonical-BTK degree obstruction)

For every `n>=3`, the upper canonical-BTK diagonal has

\[
                         \deg(X_n)\ge n-1.             \tag{4.2}
\]

Consequently it is not a side linear forest for every `n>=4`.  Every
coordinate conjugate has the same obstruction.

#### Proof

In (4.1), the paired positions are

\[
 (3,4),(5,6),\ldots,(2n-3,2n-2),                     \tag{4.3}
\]

and the free positions are `0,1,2,2n-1`.

First fix any pair `(a,b)` in (4.3).  Delete the `1` at `b` from `X_n`.
The resulting rank-`n` word has the same bracket pairs except `(a,b)`;
its free positions are

\[
                         0,1,2,a,b,2n-1.
\]

At rank `n` the first three free positions are occupied, so its next two
BTK free zeros are `a,b`.  The canonical two-rank diagonal therefore has
physical endpoints `X_n` and `X_n-b+a`.  The `n-2` choices in (4.3) give
`n-2` distinct edges incident with `X_n`.

Second, in the BTK chain containing `X_n` itself, the rank-`n` member has
free positions `0,1` occupied.  The next two free zeros are `2` and
`2n-1`, giving the additional edge from `X_n` to
`X_n-2+(2n-1)`.  It is distinct from the preceding edges.  This proves
(4.2).  Relabelling coordinates conjugates the physical graph and
preserves degrees. `square`

At `n=3`, (4.2) gives only degree two.  The separate socket count is sharp:
the canonical support has thirteen degree-at-most-one vertices but the
side requires fourteen anchors.  This is the finite `n=3` obstruction
already recorded in the canonical audit.  Thus the canonical BTK diagonal
fails for every `n>=3`, but for two different reasons at the first and later
parameters.

## 5. Endpoint-distance budget: arbitrary pairing is false

For two vertices \(X,Y\in\binom{\Omega}{n+1}\), write

\[
                  d_J(X,Y)=(n+1)-|X\cap Y|
                           ={1\over2}|X\mathbin\triangle Y|.
                                                                  \tag{5.1}
\]

### Theorem 5.1 (pairing metric budget)

Let \(H\) be any upper side linear forest with \(P\) edges.  Suppose
\(\Pi\) is the matching of anchor pairs whose endpoints lie in the same
two-anchor component of \(H\).  Then

\[
                         \sum_{\{X,Y\}\in\Pi}d_J(X,Y)\le P.        \tag{5.2}
\]

The dual lower shore obeys the same inequality.

#### Proof

The unique \(X\)-to-\(Y\) path in their common component has at least
\(d_J(X,Y)\) Johnson edges.  Distinct pairs in \(\Pi\) lie in distinct
components, so these paths are edge-disjoint.  Their total number of edges
is at most \(|E(H)|=P\).  \(\square\)

Thus the prescribed-pair theorem in
MATH_THEOREM_CATALAN_SIDE_ANCHOR_PAIRING_TOPOLOGY_DECOUPLING_20260731.md
cannot hold for *every* \(K\)-matching without a distance hypothesis.
This failure already occurs on the literal positive \(n=3\) prefix
interface of Section 7 in
MATH_THEOREM_R_CATALAN_A1_INTEGRAL_FIVE_SECTOR_BRAID_AND_DIAGONAL_GATE_20260731.md.
There the upper anchor bank is

\[
             \mathcal A=\binom{[6]}4\setminus\{\mathtt{3a}\},
\]

because the sole retained child edge is
\(\mathtt{1a}\!-\!\mathtt{2a}\), of upper colour \(\mathtt{3a}\).
All ten anchors in

\[
(\mathtt{3c},\mathtt{33}),\ 
(\mathtt{36},\mathtt{1d}),\ 
(\mathtt{2e},\mathtt{1b}),\ 
(\mathtt{1e},\mathtt{35}),\ 
(\mathtt{39},\mathtt{27})
                                                                  \tag{5.3}
\]

belong to \(\mathcal A\), are pairwise distinct, and each displayed pair
has Johnson distance two.  They form a requested matching of order
\(K=\operatorname{Cat}_3=5\), but its distance sum is \(10\), whereas the
side has only

\[
                         P=\binom 61=6
\]

edges.  Theorem 5.1 forbids this pairing.  The same literal interface does
admit the different side pairing in the positive certificate, so this is
an obstruction to **pairing universality**, not to side-forest existence.

Consequently the topology-decoupling theorem must be used through a rich
realizable family, not through all matchings.  For a fixed common basis
\(Q\), let \(\mathcal R^-\) and \(\mathcal R^+\) be the matchings induced
by no-anchor-free side forests satisfying Theorem 1.1 on the two shores,
and let \(P_0\) be the central partial matching.  The exact remaining
pairing condition is

\[
 \boxed{\ \exists\,P_-\in\mathcal R^-,\ P_+\in\mathcal R^+
          \text{ such that }P_0\cup P_-\cup P_+\text{ is a forest.}\ }       \tag{5.4}
\]

The abstract greedy theorem proves that the accepting set of \(P_+\) is
nonempty in the space of all \(K\)-matchings; it does not prove that this
set meets \(\mathcal R^+\).

## 6. Exact surviving all-parameter lemma

After common-basis incidence, the all-parameter side problem is neither an
ordinary matching problem nor an SCD problem by itself.  Its exact positive
form is:

> **Anchored double-turn braid.**  Choose the guaranteed common basis \(Q\)
> so that both turn graphs \(T^-_F,T^+_F\) admit the two rainbow linear
> forests of Theorem 1.1, and so that their induced anchor pairings satisfy
> (5.4).  It is enough to prove that one shore supplies some realizable
> pairing and the other shore's realizable family meets the greedy
> cross-component extension relation; arbitrary prescribed-pair
> universality is false by Theorem 5.1.

Theorem 1.1 is an equivalence, not an extra hypothesis hidden in a physical
lift.  Lemma 2.2 is the first checkable obstruction after incidence Hall,
and Theorem 4.1 rules out the unmodified canonical BTK representative in
every parameter.  A noncanonical turn/ear rethread, or a symbolic family of
such forests, is still required.
