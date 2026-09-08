# The minimal three-cell transverse covariance gadget and its bounded-block limit

Date: 2026-07-26

Method: pure mathematics only. No computation, search, solver, or web input is used.

## 0. Result

Fix one ambient perfect matching of the physical coordinates.  Write the
status of a matching pair as (E,S,F) according as it is empty, split, or
full in a middle orientation cell.

Two distinct orientation cells can have a common lower target cylinder or a
common upper target cylinder, but never both.  Thus a two-cell transverse
gadget cannot service both signs.  The smallest connected common-frame
gadget which has an overlap of each sign consists of three cells.  On three
distinguished pairs (a,b,c) their status words are

\[
 C_0=(S,E,F),\qquad C_1=(E,S,F),\qquad C_2=(E,F,S).       \tag{0.1}
\]

Give all three cells the same (r-1) split reservoir pairs.  Each cell is
then a physical (Q_r).  For every (1\le q<r):

* (C_0,C_1) have one common lower target cylinder and no common upper
  target;
* (C_1,C_2) have one common upper target cylinder and no common lower
  target;
* (C_0,C_2) have no common target of either sign.

Each nonempty common cylinder has exactly

\[
                 U_{r,q}=2^{r-q}\binom{r-1}{q-1}              \tag{0.2}
\]

literal targets.

Let (F) be any isometric (C_{2r})-factor of (Q_r) whose signed traces
are injective through depth (H<r).  Independently conjugate its three
copies by affine cube automorphisms fixing the distinguished abstract
direction.  There is a deterministic triple of conjugates for which the
complete cross-cell collision sum over both signs and all (q\le H\), for
(H\le r/4), is

\[
 \boxed{
 \sum_{q=1}^H\left(K_{01,q}^-+K_{12,q}^+\right)
 \le 2^{r+1}\sum_{q=1}^H {q\over r}
              {2^q\over\binom rq}
 =O\!\left({2^r\over r^2}\right).}                 \tag{0.3}
\]

More precisely, at depth (q) the distinguished-direction trace set has
size

\[
                         M_{r,q}={q\over r}2^r,       \tag{0.4}
\]

its density in (0.2) is exactly

\[
                         p_{r,q}={2^q\over\binom rq}, \tag{0.5}
\]

and the affine balanced overlap is (M_{r,q}p_{r,q}).  The triple in
(0.3) therefore has nonpositive **aggregate** overlap covariance relative
to the exact affine baseline simultaneously over the protected band.  This
is a genuine local cross-cell covariance statement, rather than an owner
codegree or profile-density statement.

It does not close the global Farkas problem.  The only frame-changing
support in (0.1) is the bounded three-pair set ({a,b,c}); the reservoir
is a common product factor.  Consequently every tensoring of this fixed
gadget has a coordinate-axis graph with uniformly bounded components and
is covered by
`MATH_OBSTRUCTION_FINITE_CROSS_CELL_GADGET_BLOCK_PROFILE_DUAL_20260726.md`.
At (q=A\sqrt m+O(1)) its full-block profile gives an explicit
nonnegative Farkas witness with an (Omega_A(W)) deficit.  Thus (0.3)
settles the finite local question positively but also identifies why this
particular gadget cannot be the coefficient-one construction: a successful
atlas must join a growing number of tensor blocks by genuine cross-block
axes.

The qualification in (0.3) is exact.  It gives one deterministic triple
whose **sum** over depths is at most the sum of the depthwise baselines; it
does not assert (K_{01,q}^-\le M_{r,q}p_{r,q}) and
(K_{12,q}^+\le M_{r,q}p_{r,q}) separately for every (q).

## 1. Pairwise two-sign overlap is impossible

An orientation cell in one common pair frame is specified by disjoint sets
((I,F)): the pairs in (I) are split, those in (F) are full, and all
others are empty.  Write it as (mathcal Q(I,F)).

### Lemma 1.1 (lower and upper candidate cells)

Let (T) be a lower depth-(q) target.  Put (S_T,F_T,E_T) for its
split, full, and empty pair sets.  Then (mathcal Q(I,F)) can emit (T)
only if

\[
 F=F_T,\qquad I=S_T\mathbin{\dot\cup}J,qquad
 J\in\binom{E_T}{q}.                                  \tag{1.1}
\]

Let (U) be an upper depth-(q) target.  Then the exact analogous
condition is

\[
 I=S_U\mathbin{\dot\cup}J,qquad
 F=F_U\setminus J,qquad J\in\binom{F_U}{q}.          \tag{1.2}
\]

#### Proof

A lower window empties precisely its (q) completed split pairs; every
other split pair retains one endpoint, and frozen pairs retain their
statuses.  This is (1.1).  An upper window fills precisely its completed
split pairs, which gives (1.2).  Both converses hold at the geometric-face
level by varying the pairs in (J). (square)

### Proposition 1.2 (two-cell two-sign rigidity)

If two common-frame orientation cells have a common lower target and a
common upper target, at arbitrary positive depths, then the two cells are
equal.

#### Proof

Let the cells be (mathcal Q(I,F)) and
(mathcal Q(I',F')).  A common lower target forces (F=F') by (1.1).
A common upper target gives

\[
                         F\mathbin{\dot\cup}J
                    =F'\mathbin{\dot\cup}J',          \tag{1.3}
\]

where (J,J') are disjoint from (F=F').  Hence (J=J').  Equation
(1.2) now gives (I=S_U\dot\cup J=I').  Thus the cells coincide.
(square)

Therefore two distinct cells cannot supply both colors of overlap.  Any
connected overlap graph containing a lower edge and an upper edge has at
least three vertices.

## 2. The minimal three-cell path

Take three distinguished matching pairs (a,b,c), and (r-1) further
pairs forming a reservoir (R).  Define (C_0,C_1,C_2) by (0.1), with
every pair of (R) split.  The distinguished words all have occupancy
three, while the reservoir has occupancy (r-1); hence all owners have
rank (r+2) on the (r+2) physical pairs.  The three cells are disjoint
middle cells of dimension (r).

### Proposition 2.1 (exact overlap classification)

At every depth (1\le q<r), the only cross-cell signed overlaps are

\[
                         C_0\stackrel{-}{\longleftrightarrow}C_1,
 \qquad                 C_1\stackrel{+}{\longleftrightarrow}C_2. \tag{2.1}
\]

For the lower overlap, (C_0) completes (a), (C_1) completes (b),
and both complete the same ((q-1))-set (J\subseteq R).  Their common
distinguished status is ((E,E,F)).  For the upper overlap, (C_1)
completes (b), (C_2) completes (c), and both complete the same
(J\subseteq R); the common distinguished status is ((E,F,F)).

In either case the target additionally records one endpoint on every pair
of (R\setminus J), proving the count (0.2).  No other overlap is
possible.

#### Proof

The two displayed completions give identical target statuses and hence
the asserted cylinders.  There are (inom{r-1}{q-1}) choices of (J)
and (2^{r-q}) orientations outside (J).

For the converse, compare the distinguished status words coordinate by
coordinate.  In (C_0,C_1), equality on the lower shore forces (a,b)
both to become empty; equality on the upper shore would require the
incompatible words ((F,E,F)) and ((E,F,F)).  The analogous comparison
for (C_1,C_2) works only on the upper shore.  The words of (C_0,C_2)
cannot be made equal on either shore.  Completing reservoir pairs changes
none of these distinguished statuses. (square)

Together with Proposition 1.2 this proves minimality.

## 3. Exact reduced trace sets and Gram matrices

Identify every cell with an abstract (Q_r) by sending its unique split
distinguished pair to coordinate (0), and identify the reservoir pairs
with coordinates (1,\ldots,r-1) in the same order.

For an affine conjugate (gFg^{-1}), let
(B_{g,q}^{\epsilon}) be the set of its signed depth-(q) traces whose
support contains coordinate (0), after deleting that completed
coordinate from the code.  Thus

\[
 B_{g,q}^{\epsilon}\subseteq
 \Omega_{r,q}:={(J,\eta):J\in\tbinom R{q-1},
                    \eta\in Q_{R\setminus J}\}.       \tag{3.1}
\]

The physical identification in Proposition 2.1 gives the exact formulas

\[
 K_{01,q}^-=
 |B_{g_0,q}^-\cap B_{g_1,q}^-|,qquad
 K_{12,q}^+=
 |B_{g_1,q}^+\cap B_{g_2,q}^+|.                    \tag{3.2}
\]

All other cross-cell inner products vanish.  Since every cell trace is
injective and has (2^r) occurrences, the complete target-incidence Gram
matrices are

\[
 G_q^-=
 \begin{pmatrix}
 2^r&K_{01,q}^-&0\\ K_{01,q}^-&2^r&0\\0&0&2^r
 \end{pmatrix},qquad
 G_q^+=
 \begin{pmatrix}
 2^r&0&0\\0&2^r&K_{12,q}^+\\0&K_{12,q}^+&2^r
 \end{pmatrix}.                                      \tag{3.3}
\]

The two signs occupy different target ranks and are orthogonal in their
direct sum.

### Lemma 3.1 (distinguished trace census)

For either sign and every (q<r),

\[
                         |B_{g,q}^{\epsilon}|=M_{r,q}
                         ={q\over r}2^r.             \tag{3.4}
\]

#### Proof

Every component has direction word (pi\pi), with every direction once
in each half.  Coordinate (0) therefore occurs twice per component.
Exactly (q) cyclic starts have a length-(q) window containing each
occurrence, and the two sets of starts are disjoint because (q<r).
There are (2^r/(2r)) components.  Thus the number of occurrences is

\[
                         2q{2^r\over2r}={q\over r}2^r.
\]

Trace injectivity turns this occurrence count into the cardinality of
the reduced trace set. (square)

## 4. Affine averaging and the all-depth aggregate bound

Let (Gamma_0) be the affine subgroup generated by all endpoint
translations and all permutations of the reservoir coordinates, fixing
coordinate (0).  It acts transitively on (Omega_{r,q}).  Hence, for
uniform (g\in\Gamma_0), every reduced trace has inclusion probability

\[
 {M_{r,q}\over U_{r,q}}
 ={(q/r)2^r\over2^{r-q}\binom{r-1}{q-1}}
 ={2^q\over\binom rq}=p_{r,q}.                      \tag{4.1}
\]

For independent uniform (g,g'), therefore,

\[
 \mathbb E|B_{g,q}^{\epsilon}\cap B_{g',q}^{\epsilon}|
                         =M_{r,q}p_{r,q}.            \tag{4.2}
\]

Choose (g_0,g_1,g_2) independently and uniformly.  Equations
(3.2) and (4.2) give

\[
 \mathbb E\sum_{q=1}^H(K_{01,q}^-+K_{12,q}^+)
 =2^{r+1}\sum_{q=1}^H{q\over r}{2^q\over\binom rq}. \tag{4.3}
\]

Some deterministic triple is no worse than this expectation, proving the
first inequality in (0.3).

For the asymptotic bound put

\[
                         a_q={q\over r}{2^q\over\binom rq}.
\]

Then (a_1=2/r^2), and

\[
 {a_{q+1}\over a_q}
 ={2(q+1)^2\over q(r-q)}.                            \tag{4.4}
\]

If (q\le r/4), then

\[
 {a_{q+1}\over a_q}
 \le {2(q+2+1/q)\over3r/4}
 \le {2\over3}+{8\over r}.                         \tag{4.5}
\]

For (r\ge48), this is at most (5/6).  Consequently

\[
                         \sum_{q=1}^{H}a_q
 \le6a_1={12\over r^2},                             \tag{4.6}
\]

and the right side of (4.3) is at most (24\,2^r/r^2).

Subtracting the exact balanced overlaps in (4.2), the chosen triple obeys

\[
 \sum_{q=1}^H
 \bigl[(K_{01,q}^--M_{r,q}p_{r,q})
      +(K_{12,q}^+-M_{r,q}p_{r,q})\bigr]\le0.       \tag{4.7}
\]

This is the promised negative-or-zero aggregate floor-covariance
statement.

## 5. Exact boundary

Proved:

1. A distinct two-cell common-frame gadget cannot overlap both signed
   target families.
2. The path (0.1) is the smallest two-sign overlap gadget.
3. Its literal overlap cylinders and complete signed Gram matrices are
   (0.2) and (3.3).
4. One deterministic common collection of compiler conjugates has the
   all-depth aggregate covariance (4.7), with total collision
   (O(2^r/r^2)) for (H\le r/4).

Not proved:

1. the two inequalities in (4.7) separately at every depth;
2. an integral semigroup saturation theorem for the global status atlas;
3. any escape from the bounded-block Farkas witness; or
4. coefficient one.

The local covariance lane is therefore not empty: the three-cell path is
an explicit exact overlapping-cylinder primitive.  But a tensor of this
fixed primitive remains a bounded-block construction, and the cited
full-block dual rules it out even fractionally.  The next constructive
lemma must replace the fixed three-pair path by a growing connected
cross-axis resolution; improving the finite gadget's internal semigroup
cannot address the surviving dual witness.
