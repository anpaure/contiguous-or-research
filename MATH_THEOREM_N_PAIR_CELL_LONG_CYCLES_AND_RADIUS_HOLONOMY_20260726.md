# Pair-cell long cycles, quotient Euler tours, and the Gaussian radius-holonomy obstruction

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
web input is used.

## 0. Outcome

Put

\[
 n=2m,\qquad \mathcal M=\binom{[2m]}m,\qquad
 W=|\mathcal M|.
\]

Fix a partition of the coordinates into pairs

\[
                         M_i=\{x_i,y_i\},\qquad i\in[m].       \tag{0.1}
\]

This note isolates the cycle-count part of the proposed bounded-state
Eulerian realization and obtains one positive theorem and two exact
obstructions.

1. **Cycle economy and the common point margins are simultaneously
   constructible.** If (H=o(m)), there is an (H)-safe partial owner
   permutation on (G=W-o(W)) middle owners, all of whose moves flip the
   chosen element of one singleton pair, such that

   \[
          \kappa\le {W\over T}=o(W/H),\qquad
          T=\lceil4\sqrt{mH}\rceil,                            \tag{0.2}
   \]

   and every coordinate has exactly

   \[
                         R_v={G\over2m}                         \tag{0.3}
   \]

   cyclic membership runs. Consequently, at every (q\le H), the
   lower and upper trace histograms have the exact point margins

   \[
   \sum_{S\ni v}\ell^-_{q,S}={G\over2}-q{G\over2m},\qquad
   \sum_{U\ni v}\ell^+_{q,U}={G\over2}+q{G\over2m}.           \tag{0.4}
   \]

   Thus neither cycle count, suffix safety, nor the common-run point
   ledger is an obstruction inside the pair-cell grammar.

2. **A quotient Euler tour is not a physical Euler tour.** In an
   integral root-transversal (H)-memory circulation, every used
   physical memory state has indegree and outdegree one. Distinct owner
   cycles therefore share no physical memory vertex, so Hierholzer
   splicing at a bounded quotient state is illegal unless the physical
   lift endpoints also agree. In a voltage/cover formulation, the exact
   component count is the number of orbits of the closed-walk holonomy.
   Reset colours act only in an auxiliary label fibre and cannot merge
   distinct physical holonomy orbits.

3. **The natural pair-cell realization is nevertheless ruled out at
   Gaussian depth.** A pair-cell-preserving move leaves the sets of
   double and empty pairs fixed. If (A_d) is the number of middle
   owners with (d) double pairs, and (B_{q,d}) is the number of lower
   rank-(m-q) targets with (d) double pairs, then every such complete
   factor has exactly (A_d) lower occurrences in radius class (d),
   independently of all orientations, de Bruijn states, Euler tours,
   and reset labels. By complementing the upper targets, the same cut
   holds for both signs. Hence

   \[
      M_q^-,M_q^+\ge \sum_d(B_{q,d}-A_d)_+.                     \tag{0.5}
   \]

   For (q=(A+o(1))\sqrt m), (A>0) fixed,

   \[
   \boxed{
     \min\{M_q^-,M_q^+\}\ge
       \left(e^{-A^2}\Phi(A/2)-\Phi(-3A/2)-o(1)\right)W,}      \tag{0.6}
   \]

   and the coefficient is strictly positive. An (o(W)) owner leave
   cannot decrease this literal support-hole lower bound. Thus the positive
   construction in item 1, and every other circulation confined to the
   same pair cells, has Ω_A(W) target holes at Gaussian depth.

The precise surviving gate is therefore not cycle fusion. One needs
physical reset seams which change the double/empty-pair data and whose
closed-walk voltages have long physical orbits, while retaining all-depth
columns. Copy relabelling and pair-radius state alone cannot do this.

## 1. Pair cells

For (X\in\mathcal M), define

\[
\begin{aligned}
 D(X)&=\{i:M_i\subseteq X\},\\
 E(X)&=\{i:M_i\cap X=\varnothing\},\\
 S(X)&=[m]\setminus(D(X)\cup E(X)).
\end{aligned}                                                   \tag{1.1}
\]

Since (|X|=m),

\[
 |D(X)|=|E(X)|=:d(X),\qquad |S(X)|=m-2d(X)=:s(X).              \tag{1.2}
\]

Fix disjoint (D,E\subseteq[m]), (|D|=|E|=d), and put
(S=[m]\setminus(D\cup E)). The owners satisfying

\[
                         D(X)=D,\qquad E(X)=E                  \tag{1.3}
\]

form a Boolean cube (Q_S\): one chooses (x_i) or (y_i) for each
(i\in S). Flipping one cube coordinate is exactly one Johnson move,
because it replaces (x_i) by (y_i), or conversely.

We call (1.3) a pair cell. Every move inside it preserves (D,E,S).

## 2. A long-cycle partial factor

We use the standard dyadic cube fact in the exact form needed here.

### Lemma 2.1 (dyadic isometric cube factor)

If (r\) is a power of two, (Q_r) has a factor into cycles of length
(2r), and on every cycle the cyclic direction word is ππ for some
permutation π of the (r) directions.

This is the recursive (C_{2r})-factor of the dyadic cube. In particular,
every cyclic interval of fewer than (r) moves uses distinct directions.

The result is used only for powers of two; the divisibility
(2r\mid2^r) is then automatic.

#### Proof

Define a neighbour permutation (F_r) recursively. Let (F_1) toggle
its only coordinate. If (r=2h), write a cube vertex as
((u,v)\in Q_h\times Q_h), and set

\[
 F_{2h}(u,v)=
 \begin{cases}
  (F_hu,v),&|u|+|v|\equiv0\pmod2,\\
  (u,F_hv),&|u|+|v|\equiv1\pmod2.
 \end{cases}                                                   \tag{2.0}
\]

Two successive moves make one child move in each half, so

\[
                         F_{2h}^{,2a}(u,v)=(F_h^au,F_h^av).   \tag{2.0a}
\]

Inductively (F_h^{2h}=\mathrm{id}). Equation (2.0a) gives
(F_{2h}^{4h}=\mathrm{id}), so (F_{2h}) is indeed a permutation and
every point returns after (4h=2r) moves. An earlier even return would give an
earlier return in both children. At an odd time the two child move counts
differ by one, so they cannot both be multiples of (2h). Thus every
orbit has length (2r). During its first (r=2h) moves, each child
makes (h) moves and, by induction, uses every direction in its half
exactly once; the second (r) moves repeat the order. The cyclic
direction word is therefore ππ, as claimed. □

### Theorem 2.2 (pair-cell long-cycle skeleton)

Let (H=H(m)\ge1) and (H=o(m)). For all sufficiently large (m), there
are a retained owner set (mathcal G\subseteq\mathcal M) and a
permutation (P) of (mathcal G) such that:

1. every (X,PX) are Johnson neighbours and lie in the same pair cell;
2. every cyclic window of at most (H) moves is geodesic;
3. (G:=|\mathcal G|=W-o(W));
4. the number of cycles of (P) is at most (W/T), where
   (T=\lceil4\sqrt{mH}\rceil), and hence is (o(W/H));
5. the factor is invariant under the cyclic permutation of the (m)
   coordinate pairs;
6. every physical coordinate has exactly (G/(2m)) membership runs.

#### Proof

Let τ cyclically permute the (m) coordinate pairs. Discard two kinds of
pair cells:

* cells with (s<T);
* cells whose ordered status word in {(D,E,S)} has nontrivial
  stabilizer under ⟨τ⟩.

Every remaining cell lies in a free τ-orbit and has (s\ge T). On one
representative of each cell orbit choose

\[
                         r=2^{\lfloor\log_2s\rfloor};          \tag{2.1}
\]

thus (s/2<r\le s). Choose any (r)-subset (A\subseteq S). Propagate
this choice equivariantly around the free τ-orbit. For every fixed
orientation of (S\setminus A), Lemma 2.1 factors the remaining
(Q_A\) into isometric (C_{2r})'s; propagate the chosen factors around
the τ-orbit as well.

Because (s\ge T),

\[
                         r>{s\over2}\ge {T\over2}>H            \tag{2.2}
\]

for all sufficiently large (m). A length-(H) interval of a direction
word ππ therefore uses distinct pair directions. The corresponding
Johnson moves remove (H) distinct physical coordinates and insert
(H) distinct physical coordinates. This proves the cyclic (H)-safety.

A retained cell of dimension (s) contributes

\[
       2^{s-r}{2^r\over2r}={2^s\over2r}<{2^s\over s}          \tag{2.3}
\]

cycles. Summing (2.3) over retained cells gives

\[
                         \kappa(P)\le {G\over T}\le {W\over T}.\tag{2.4}
\]

Since (T/H\to\infty), (2.4) is (o(W/H)).

It remains to bound the leave. The number of owners with exactly (s)
singleton pairs is at most

\[
                         2^m\binom ms.                         \tag{2.5}
\]

Indeed choose the singleton pairs, their orientations, and then choose
which remaining pairs are double rather than empty; the last two factors
are at most (2^s2^{m-s}=2^m). Since (T=o(m)),

\[
 {1\over W}\sum_{s<T}2^m\binom ms
 \le (2m+1)2^{-m}\left({em\over T}\right)^T=o(1),             \tag{2.6}
\]

where (W\ge4^m/(2m+1)).

If a cell has nontrivial τ-stabilizer, its status word is fixed by some
τ^j\ne1), hence has period at most (m/2). There are at most
(m3^{m/2}) such status words, and each cell has at most (2^m) owners.
Thus the second discarded family has size at most

\[
                         m(2\sqrt3)^m=o(W).                    \tag{2.7}
\]

This proves (G=W-o(W)).

The construction is τ-invariant. In one installed isometric cycle, an
active pair direction occurs twice, so each of its two physical
coordinates has one cyclic membership run; an inactive pair contributes
zero runs. Hence the two coordinates within every pair have equal run
counts, and τ-invariance makes this integer common to all pairs. The sum
of all coordinate run counts equals the total number (G) of cycle
vertices: each (C_{2r}) contributes (2r) coordinate runs. Therefore
every coordinate has (G/(2m)) runs. □

### Corollary 2.3 (exact point margins at all depths)

Let ℓ(^{\pm}_{q}) be the two signed trace histograms of the factor in
Theorem 2.2. Then (0.4) holds for every (q\le H).

#### Proof

The retained owner set is invariant under τ and under interchanging the
two coordinates of any one pair. This group is transitive on the (2m)
physical coordinates. Hence exactly (G/2) retained owners contain a
fixed coordinate (v).

In a cyclic (q)-window, (v) is absent from the lower intersection
precisely when it is absent initially or is deleted during the window.
By (H)-safety, the window contains at most one transition of (v).
Every cyclic deletion of (v) lies in exactly (q) rooted (q)-windows.
Thus

\[
 \sum_{S\ni v}\ell^-_{q,S}={G\over2}-qR_v.
\]

The same argument with insertions and unions gives

\[
 \sum_{U\ni v}\ell^+_{q,U}={G\over2}+qR_v.
\]

Substitute (R_v=G/(2m)). □

This proves exact common-run compatibility, not targetwise balance.

## 3. Why bounded-state Eulerization does not reduce physical cycles

Let Γ_H be the directed graph whose arcs are safe physical paths

\[
                         \gamma=(X_0,\ldots,X_H),              \tag{3.1}
\]

from the prefix memory ((X_0,\ldots,X_{H-1})) to the suffix memory
((X_1,\ldots,X_H)). Let (z_\gamma\in\{0,1\}) satisfy root
transversality and memory balance:

\[
 \sum_{\gamma:X_0=X}z_\gamma\le1,\qquad
 \deg_z^+(\sigma)=\deg_z^-(\sigma).                           \tag{3.2}
\]

### Proposition 3.1 (root-transversal Euler rigidity)

Every used physical memory state in (3.2) has indegree and outdegree one.
Consequently the selected support is a vertex-disjoint union of directed
cycles, and two different cycles cannot be joined by choosing a different
Euler transition at a used state.

#### Proof

All arcs leaving a memory state σ have the same root, namely the first
owner of σ. The root row in (3.2) therefore gives
(\deg_z^+(\sigma)\le1). Memory balance gives
(\deg_z^-(\sigma)=\deg_z^+(\sigma)\le1). Every used state has both
degrees one, proving the claim. □

Thus Hierholzer's theorem is useful only before root transversality has
collapsed the physical support to degree one. A quotient of physical
memories by pair radius, quota level, copy label, or a bounded deletion
word may have large quotient degree, but pairing quotient half-edges does
not make unequal physical memories equal.

The exact general language is a graph cover.

### Proposition 3.2 (holonomy component formula)

Let (B) be a directed base graph. Over each base vertex (u) let there
be a physical fibre (F_u), and let every directed base arc
(e:u\to v) carry a bijection (g_e:F_u\to F_v). If

\[
                         C=e_1e_2\cdots e_b                 \tag{3.3}
\]

is a closed base Euler tour rooted at (u), put

\[
                         g_C=g_{e_b}\cdots g_{e_1}:F_u\to F_u.\tag{3.4}
\]

Then the lift of repeated traversals of (C) has exactly

\[
                         \operatorname{cyc}(g_C)               \tag{3.5}
\]

physical cycles. If an orbit of (g_C) has length (a), its lifted
physical cycle has length (ab).

#### Proof

Starting above (x\in F_u), one traversal of (C) returns above
(g_Cx). The lift closes after exactly the orbit length of (x) under
(g_C). Distinct orbits give disjoint lifted cycles, and every fibre
point occurs in one of them. □

### Corollary 3.3 (reset labels cannot improve physical holonomy)

Suppose an auxiliary reset colour is added to the fibre and every reset
operation projects to the identity on the physical fibre. Then every
labelled lifted cycle projects inside one orbit of (g_C). Reset colours
may split a physical orbit, but cannot merge two different physical
orbits. In particular, base-state connectedness or the existence of one
labelled Euler tour gives no physical cycle-count bound without a bound
on ​(\operatorname{cyc}(g_C)).

This is the cycle-count version of the reset-state projection theorem.
The sufficient positive condition is equally exact: the selected closed
base tours must have physical holonomies whose average orbit length tends
to infinity faster than the required (H/b) scale. Merely enlarging the
state alphabet does not create such holonomy.

## 4. The stable pair-radius obstruction

Theorem 2.2 solves the cycle and point ledgers, but its preservation of
pair cells imposes an all-depth target invariant.

Let

\[
 A_d={m!\over d!^2(m-2d)!},2^{m-2d}                           \tag{4.1}
\]

be the number of middle owners with (d) double and (d) empty pairs.
At lower depth (q), let

\[
 B_{q,d}={m!\over d!(d+q)!(m-q-2d)!},2^{m-q-2d}              \tag{4.2}
\]

be the number of ((m-q))-targets with (d) double pairs. Terms with
invalid factorials are zero.

### Lemma 4.1 (radius conservation)

In every (H)-safe pair-cell-preserving owner factor, every rooted
(q)-window beginning at an owner of radius (d) has a lower target of
radius (d) and an upper target of radius (d+q). Consequently a
complete factor has exactly (A_d) lower occurrences in radius class
(d), and an owner leave of size (L) changes the aggregate radius
counts by total variation at most (L).

#### Proof

During a safe (q)-window, (q) distinct singleton pairs are flipped.
Every original double pair remains double in the lower intersection.
Every flipped singleton pair contributes no coordinate to the lower
intersection, and every unflipped singleton contributes one. Thus the
lower target has exactly the original (d) double pairs. In the upper
union, each flipped singleton becomes a double pair, giving (d+q).
There is one rooted occurrence per retained owner. □

### Corollary 4.2 (exact two-sided radial support cut)

For every complete pair-cell-preserving factor,

\[
             M_q^-,M_q^+\ge\sum_d(B_{q,d}-A_d)_+.              \tag{4.3}
\]

The same lower bound holds for a partial pair-cell-preserving factor.

#### Proof

There are (B_{q,d}) lower targets in class (d), but only (A_d)
occurrences available to hit them. Hence at most
(\min\{A_d,B_{q,d}\}) distinct targets in that class can be hit. Sum
over (d). For the upper sign, classify an upper target by its number of
empty pairs. Complementation identifies this class with the lower class
of size (B_{q,d}), while Lemma 4.1 again gives (A_d) occurrences.
Deleting an owner can only delete an occurrence, so it cannot
increase the number of distinct targets hit. □

The classwise likelihood ratio is

\[
 \Lambda_{q,m}(d):={A_d\over B_{q,d}}
 =2^q{(d+1)(d+2)\cdots(d+q)
       \over(m-2d-q+1)\cdots(m-2d)}.                          \tag{4.4}
\]

It is strictly increasing on its support. Formula (4.3) is

\[
 {M_q^-\over N_q}\ge
 \mathbb E_{q}\bigl(1-\Lambda_{q,m}(D)\bigr)_+,              \tag{4.5}
\]

where (D) is the number of double pairs in a uniform
((m-q))-subset and (N_q=\binom{2m}{m-q}).

### Theorem 4.3 (Gaussian radius-holonomy obstruction)

Fix (A>0), let (q=(A+o(1))\sqrt m), and assume (q\le H). Then

\[
 {D-(m/4-q/2)\over\sqrt m}\ \Longrightarrow\
                         N(0,1/16),                             \tag{4.6}
\]

and

\[
 \log\Lambda_{q,m}(D)\ \Longrightarrow\
                         N(-A^2,4A^2).                          \tag{4.7}
\]

Consequently

\[
 \liminf_{m\to\infty}{\min\{M_q^-,M_q^+\}\over W}
 \ge e^{-A^2}\Phi(A/2)-\Phi(-3A/2)>0.                         \tag{4.8}
\]

The same bound holds for every partial pair-cell-preserving factor.

#### Proof

For one coordinate pair in a uniformly random unrestricted subset, let
(Z\in\{0,1,2\}) be its occupancy and let (Y=\mathbf1_{\{Z=2\}}).
Under independent fair coordinate bits,

\[
 \mathbb EZ=1,\quad \operatorname{Var}Z={1\over2},\quad
 \mathbb EY={1\over4},\quad \operatorname{Var}Y={3\over16},
 \quad \operatorname{Cov}(Y,Z)={1\over4}.                    \tag{4.9}
\]

Conditioning Σ(Z_i=m-q) makes the subset uniform on rank (m-q).
The bivariate local central limit theorem, or equivalently Stirling's
formula applied uniformly to (4.2), gives the conditional mean shift

\[
 {\operatorname{Cov}(Y,Z)\over\operatorname{Var}Z}(-q)
                         =-{q\over2}                            \tag{4.10}
\]

and conditional variance

\[
 m\left({3\over16}-{(1/4)^2\over1/2}\right)={m\over16}.       \tag{4.11}
\]

This proves (4.6).

Write (d=m/4+y\sqrt m). Uniformly for bounded (y), expansion of (4.4)
gives

\[
\begin{aligned}
 \log\Lambda_{q,m}(d)
 &=\sum_{i=1}^q
 \log {2(d+i)\over m-2d-q+i}\\
 &=8Ay+3A^2+o(1).                                              \tag{4.12}
\end{aligned}
\]

By (4.6), (y=-A/2+Z/4+o_{\mathbb P}(1)), where (Z\sim N(0,1)).
Substitution in (4.12) gives

\[
                         -A^2+2AZ,                              \tag{4.13}
\]

which proves (4.7). The likelihood ratios in (4.4) have mean

\[
 \mathbb E_q\Lambda_{q,m}(D)={W\over N_q}\longrightarrow e^{A^2}.\tag{4.14}
\]

Truncation at one makes the function ((1-e^z)_+) bounded and continuous,
so (4.7) and (4.5) yield

\[
 \liminf {M_q^-\over N_q}
 \ge \Phi(A/2)-e^{A^2}\Phi(-3A/2).                            \tag{4.15}
\]

Also (N_q/W\to e^{-A^2}), proving (4.8). Positivity follows already
from the fact that the nondegenerate normal variable in (4.7) has
positive probability below zero and ((1-e^z)_+>0) there. Finally apply
Corollary 4.2. □

The word “holonomy” here is literal: the pair-cell datum ((D,E)) is
conserved around every physical cycle of this grammar, and its lower
radius is then conserved through every suffix window. The obstruction is
unchanged by:

* changing the isometric cube factor;
* changing its direction orders;
* choosing a different bounded de Bruijn state;
* taking a different Euler tour in the quotient;
* adding quota, copy, pair-radius, or reset colours.

Only a physical pair-breaking move which changes the pair-cell datum can
alter (4.3); its scalar owner radius need not change on that single move.

## 5. Exact proved boundary

The following are proved here.

1. There is an (H)-safe owner circulation on (W-o(W)) owners with
   (o(W/H)) cycles, for every (H=o(m)).
2. It has one exactly balanced integer run vector and exact two-sided
   point margins simultaneously at all (q\le H).
3. Root transversality makes the physical memory support 1-regular;
   quotient Euler connectivity cannot fuse its cycles.
4. The exact additional datum controlling a cover lift is closed-walk
   physical holonomy, and reset colours cannot improve it.
5. Every pair-cell-preserving realization has the radial support cut
   (4.3), which is Ω_A(W) at (q=A\sqrt m).

What is not proved is an integral realization of the rounded all-depth
target tables. The present positive factor deliberately remains inside
pair cells and is therefore excluded by Theorem 4.3. A successful
pair-radius/reset construction must include physical pair-breaking,
pair-cell-changing seams,
arrange those seams in the same (H)-memory circulation, and show that
their physical holonomies have sufficiently long orbits. The support cut
alone does not quantify the seam density.

For the particular smallest-radius floor/ceiling tables, the companion
radius-moment theorem in
`MATH_LEMMA_N_PAIR_RADIUS_RESET_DENSITY_OBSTRUCTION_20260726.md` does:
if the aggregate all-depth multiplicity-table discrepancy is (o(W)) and
(H=\Omega(\sqrt m)), then the number of physical pair-breaking seams is

\[
                         E_\Pi\ge(1/2-o(1))W.                   \tag{5.1}
\]

For a partial circulation the displayed error term gives the sufficient
leave condition (L=o(WH/m)); the companion statement uses the stronger
(L=o(W/H)). This density conclusion is scoped to
multiplicity-table approximation; it does not follow merely from
(o(W)) literal support holes. No bounded-state or reset-label argument
supplies the required dense physical chronology automatically.
