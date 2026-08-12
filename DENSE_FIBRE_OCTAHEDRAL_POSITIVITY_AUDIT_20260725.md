# Dense-fibre positivity for octahedral moves: a sharp quadratic-rank barrier

Date: 2026-07-25

Pure mathematics only.

## 0. Verdict

Let \(V\) have size \(n\), and consider integer load vectors on
\(\binom Vr\).  The rank-\(r\) octahedral move is

\[
 Q(C;x,y,u,v)
 =e_{C+yu}+e_{C+xv}-e_{C+xu}-e_{C+yv},                 \tag{0.1}
\]

where \(|C|=r-2\).  These moves generate the full integer kernel of the
point-incidence map, as proved in
`TOP_FIBRE_RECTANGLE_TRADE_AUDIT_20260725.md`.

The proposed stronger positivity statement is false:

\[
 \boxed{
 \text{equal point marginals and defect }D
 \not\Longrightarrow O(D)\text{ nonnegative octahedral moves}.}          \tag{0.2}
\]

This remains false after adding one copy of **every** rank-\(r\) set as a
uniform reservoir.  Already on \(2r\) points there are load vectors with
entries only in \(\{1,2\}\), equal point marginals, and defect \(D=2\),
for which every octahedral route has length

\[
 \Omega(r^2)=\Omega(r^2D).                              \tag{0.3}
\]

The obstruction is the rank-two incidence, or pair moment.  One
octahedral move changes exactly four pair coordinates.  Equal point
marginals do not control pair discrepancy.

Conversely, a full all-ones reservoir is sufficient to route arbitrary
equal-point load vectors in

\[
 O(r^2D)                                                 \tag{0.4}
\]

nonnegative octahedral moves.  Thus the \(r^2\) loss is sharp in complete
generality.

For the crossing-scale segment absorber, a route of \(R\) separately
realized moves has word excess \(O((H+Q)R)\).  The universal estimate
\(R=O(r^2D)\) is useful only when

\[
 D=o\!\left(\frac{W}{r^2(H+Q)}\right),                  \tag{0.5}
\]

far smaller than a generic \(o(W)\) shadow defect.  A vanishing reservoir
cannot remove this pair-moment barrier; even a density-one reservoir does
not.

## 1. Point and pair incidence

Let

\[
 A_1:\mathbb Z^{\binom Vr}\to\mathbb Z^V
\]

be the point-incidence map, and let

\[
 A_2:\mathbb Z^{\binom Vr}\to\mathbb Z^{\binom V2}
\]

be the pair-incidence map

\[
 (A_2z)(\{a,b\})=\sum_{S\supset\{a,b\}}z_S.            \tag{1.1}
\]

Every octahedral move lies in \(\ker A_1\).  Its pair image is especially
sparse.

### Lemma 1.1 (one move changes four pair coordinates)

For the move (0.1), all pair incidences involving the core \(C\) cancel,
and

\[
 A_2Q
 =e_{yu}+e_{xv}-e_{xu}-e_{yv}.                        \tag{1.2}
\]

In particular,

\[
 \|A_2Q\|_1=4.                                          \tag{1.3}
\]

#### Proof

A pair inside \(C\) occurs twice with each sign.  A pair consisting of a
core point and one of \(x,y,u,v\) occurs once with each sign.  Among the
four special points, only the four displayed pairs occur. \(\square\)

### Corollary 1.2 (pair-transport lower bound)

If \(\mu\) is transformed into \(\nu\) by \(R\) octahedral moves, then

\[
 \boxed{
 R\ge\frac14\|A_2(\mu-\nu)\|_1.}                       \tag{1.4}
\]

This bound is independent of every common reservoir added to both load
vectors.

## 2. Dense \(\{1,2\}\) counterexamples

Let \(V\) have size \(2r\), with \(r\) even.  Choose two balanced
bipartitions

\[
 V=A_0\sqcup A_1=C_0\sqcup C_1                         \tag{2.1}
\]

such that

\[
 |A_i\cap C_j|=r/2\qquad(i,j\in\{0,1\}).               \tag{2.2}
\]

Put

\[
 \mu=\mathbf1+e_{A_0}+e_{A_1},\qquad
 \nu=\mathbf1+e_{C_0}+e_{C_1},                         \tag{2.3}
\]

where \(\mathbf1\) is the all-ones load vector on \(\binom Vr\).

### Theorem 2.1 (quadratic-rank move lower bound)

The vectors \(\mu,\nu\) have the following properties.

1. Every entry belongs to \(\{1,2\}\).
2. Each vector is itself floor/ceiling balanced (two entries are two and
   all remaining entries are one), and their point marginals agree.
3. Their transportation defect is
   \[
      D:=\frac12\|\mu-\nu\|_1=2.                        \tag{2.4}
   \]
4. Every nonnegative octahedral route from \(\mu\) to \(\nu\) has length
   at least
   \[
      \boxed{
      \frac{r^2}4
      =\Omega(r^2D).}                                    \tag{2.5}
   \]

#### Proof

Every point lies in one \(A\)-part and one \(C\)-part, so the extra point
marginals agree.  The four parts are distinct, giving (2.4).

The extra pair incidence of \(\mu\) is supported on pairs lying in one
\(A\)-part, and that of \(\nu\) on pairs lying in one \(C\)-part.  Each
side contains

\[
 2\binom r2=r(r-1)
\]

pair units.  Their common support consists of pairs lying in one of the
four cells \(A_i\cap C_j\), and has size

\[
 4\binom{r/2}{2}=\frac{r^2}{2}-r.
\]

Therefore

\[
 \|A_2(\mu-\nu)\|_1
 =2\left[r(r-1)-\left(\frac{r^2}{2}-r\right)\right]
 =r^2.                                                    \tag{2.6}
\]

Apply Corollary 1.2. \(\square\)

### Consequence

No hypothesis of the following form can prove an \(O(D)\) route:

* entries in \(\{0,1,2\}\), or within bounded distance of a balanced
  vector;
* exact equality of point marginals;
* a common positive reservoir, even the complete all-ones layer; and
* total defect \(D=o(W)\).

The pair discrepancy must also be controlled, or higher-order moves must be
allowed.

This does not rule out choosing, for a *given* packet load \(\mu\), a
balanced target \(\nu\) specifically to minimize pair discrepancy.  It
rules out a theorem uniform over all balanced targets using only point
marginals and \(L^1\) defect.

The obstruction is not confined to the exact middle rank.

### Proposition 2.2 (central-window version)

Let \(n=2m\), and let

\[
 m/3\le r\le m.
\]

For all sufficiently large \(m\), there are two load vectors
\(\mu,\nu\in\{1,2\}^{\binom{[n]}r}\) with equal point marginals and

\[
 D=\frac12\|\mu-\nu\|_1=n,                              \tag{2.7}
\]

such that every octahedral route between them has length

\[
 \Omega(n^2r)=\Omega(r^2D).                              \tag{2.8}
\]

#### Proof

For an oriented cyclic order \(\pi\) on \([n]\), let

\[
 {cal W}_r(\pi)=\{I_\pi(j,r):j\in\mathbb Z_n\}.
\]

Every point lies in exactly \(r\) members of \({\cal W}_r(\pi)\).  Thus

\[
 \mu=\mathbf1+\mathbf1_{{\cal W}_r(\pi)},\qquad
 \nu=\mathbf1+\mathbf1_{{\cal W}_r(\sigma)}             \tag{2.9}
\]

have equal point marginals for all \(\pi,\sigma\).

For a pair at cyclic distance \(d\le m\), its number of occurrences in
\({\cal W}_r(\pi)\) is

\[
 w_r(d)=(r-d)_+.                                         \tag{2.10}
\]

Fix \(\pi\) and choose \(\sigma\) uniformly.  The cyclic distance of each
fixed coordinate pair in \(\sigma\) has the usual distribution on
\(1,\ldots,m\).  Two independent samples from this distribution have

\[
 \mathbb E|w_r(D_1)-w_r(D_2)|=\Omega(r)                 \tag{2.11}
\]

uniformly for \(m/3\le r\le m\): with constant probability one distance is
at most \(r/4\), while the other is at least \(3r/4\).  Averaging (2.11)
over the \(\binom n2\) coordinate pairs gives

\[
 \mathbb E_\sigma
 \|A_2(\mathbf1_{{\cal W}_r(\pi)}-
          \mathbf1_{{\cal W}_r(\sigma)})\|_1
 =\Omega(n^2r).                                          \tag{2.12}
\]

On the other hand, the expected number of common rank-\(r\) windows is

\[
 \frac{n^2}{\binom nr}=o(1).                             \tag{2.13}
\]

The pair discrepancy is always \(O(n^2r)\).  Hence (2.12), (2.13), and a
simple averaging argument give a choice of \(\sigma\) for which the two
window families are disjoint and the pair discrepancy is \(\Omega(n^2r)\).
Then (2.7) holds, and Corollary 1.2 proves (2.8). \(\square\)

Thus the \(r^2\) loss persists throughout the lower central band used by
the crossing-packet construction.

## 3. A matching \(O(r^2D)\) positive theorem

The lower bound above has the correct order in full generality.

### Lemma 3.1 (one general exchange from local squares)

Let \(A,B\in\binom Vr\), choose \(a\in A-B\), \(b\in B-A\), and put

\[
 A'=A-a+b,qquad B'=B-b+a.                              \tag{3.1}
\]

Let

\[
 d=|A-B|.
\]

After adding one reservoir copy of every \(r\)-set, the positive exchange

\[
 e_A+e_B\longmapsto e_{A'}+e_{B'}                     \tag{3.2}
\]

can be performed by exactly \(d-1\) nonnegative octahedral moves.  Every
reservoir set has its original load again at the end.

#### Proof

Write

\[
 A-B=\{a,p_1,\ldots,p_{d-1}\},\qquad
 B-A=\{b,q_1,\ldots,q_{d-1}\}.                          \tag{3.3}
\]

Put

\[
 G_k=A-\{p_1,\ldots,p_k\}+\{q_1,\ldots,q_k\},          \tag{3.4}
\]

and

\[
 E_k=G_k-a+b.                                           \tag{3.5}
\]

Thus \(G_0=A\), \(E_0=A'\), \(G_{d-1}=B'\), and
\(E_{d-1}=B\).

For \(1\le k\le d-1\), the local square with common core

\[
 G_{k-1}-\{a,p_k\}
\]

performs

\[
 e_{G_{k-1}}+e_{E_k}
 \longmapsto
 e_{E_{k-1}}+e_{G_k}.                                  \tag{3.6}
\]

At \(k=1\), \(G_0=A\) is a source unit and \(E_1\) is supplied by the
reservoir.  The move creates \(E_0=A'\) and \(G_1\).  At the next step the
new \(G_1\) is used, while \(E_2\) comes from the reservoir and \(E_1\) is
restored.  Continue.  At the last step \(E_{d-1}=B\) is the second source
unit, and the move creates \(G_{d-1}=B'\) while restoring
\(E_{d-2}\).  All temporary reservoir units are restored and no load ever
becomes negative. \(\square\)

### Theorem 3.2 (full-reservoir positive routing)

Let \(\mu_0,\nu_0\) be nonnegative integer rank-\(r\) load vectors with

\[
 A_1\mu_0=A_1\nu_0,
\]

and put

\[
 D=\frac12\|\mu_0-\nu_0\|_1.
\]

Then \(\mathbf1+\mu_0\) can be transformed into
\(\mathbf1+\nu_0\) by at most

\[
 \boxed{r(r-1)D}                                         \tag{3.7}
\]

nonnegative octahedral moves, with the all-ones reservoir restored.

#### Proof

Cancel common units of \(\mu_0,\nu_0\), leaving \(D\) source and \(D\)
target hyperedges.  Label their edge slots.  Their bipartite incidence
matrices have the same row sums \(r\) and the same column sums because the
point marginals agree.

The symmetric difference of the two matrices decomposes into alternating
even cycles.  Standard \(2\times2\) switches along those cycles transform
one incidence matrix into the other using at most \(rD\) switches.  Each
switch is a general exchange (3.2), with \(d\le r\), and Lemma 3.1 realizes
it in at most \(r-1\) octahedral moves.  This proves (3.7). \(\square\)

Together, Theorems 2.1 and 3.2 show that, with a common all-ones reservoir,
the worst-case positive routing complexity is \(\Theta(r^2D)\).

## 4. A vanishing reservoir cannot prove the requested theorem

Suppose a common reservoir \(\rho\) is added to two load vectors.  The
pair-transport difference is unchanged:

\[
 A_2((\mu+\rho)-(\nu+\rho))=A_2(\mu-\nu).              \tag{4.1}
\]

Therefore no choice of reservoir density \(\varepsilon\), uniformity, or
spread can improve the lower bound (1.4).  A reservoir helps only with
nonnegativity; it cannot shorten the required pair transport.

In particular, Theorem 2.1 already has the maximal density-one reservoir.
Hence there is no \(\varepsilon>0\), even \(\varepsilon=1\), for which the
requested universal \(O(D)\) theorem is true.

For a *particular* pair \(\mu,\nu\), a sparse reservoir may suffice if it
contains every temporary set \(E_k\) in a chosen decomposition.  This is a
path-dependent exchange-completeness condition, not a consequence of
point-marginal uniformity alone.

## 5. Segment-absorber toll

Return to the crossing packet scale

\[
 M=m+H,qquad H=(1+o(1))\sqrt{m\log m},qquad
 N_H=(1+o(1))W/m.                                       \tag{5.1}
\]

The bounded-segment rectangle theorem in
`TOP_FIBRE_RECTANGLE_TRADE_AUDIT_20260725.md` realizes one rank-isolating
octahedral move over a hard band \(m-Q,\ldots,m+Q\) with

* at most four promotion paths;
* at most \(2Q+2\) extra state occurrences; and
* word excess \(O(H+Q)\) over one baseline top packet.

If \(R\) moves are realized independently in this way, the proved ledger is

\[
 \operatorname{excess}=O((H+Q)R).                       \tag{5.2}
\]

Thus an \(o(W)\) absorber requires

\[
 R=o\!\left(\frac W{H+Q}\right).                        \tag{5.3}
\]

Combining this with Theorem 3.2 gives the sufficient but very strong
condition

\[
 D=o\!\left(\frac W{r^2(H+Q)}\right).                  \tag{5.4}
\]

The balanced-bipartition example proves that the \(r^2\) cannot be removed from a universal
statement based only on point marginals and \(D\).

For central ranks \(r\asymp m\) and \(Q\le H\), (5.4) is approximately

\[
 D=o\!\left(\frac{W}{m^2\sqrt{m\log m}}\right),         \tag{5.5}
\]

much smaller than the desired generic \(o(W)\) defect.

The bound (5.2) does not rule out a nonlocal gadget which amortizes many
octahedral moves inside a bounded number of paths.  No such composition
theorem is presently proved.

## 6. Top support and congestion

A rank-\(r\) octahedral move uses exactly the \(r+2\) coordinates

\[
 C+\{x,y,u,v\}.
\]

At the crossing scale it can be embedded in exactly

\[
 \boxed{
 g_r=\binom{2m-r-2}{M-r-2}}                             \tag{6.1}
\]

tops of size \(M\), provided \(r\le M-2\).  This counts *potential*
embeddings before cyclic orders are fixed.  The bounded-segment gadget also
requires the baseline order on the chosen top to place the core and four
special points in the pattern of Theorem 1.2.  Thus a pre-existing packet
selection may have fewer accessible tops; (6.1) is an ambient capacity, not
an automatic absorber degree.

For the lower depth \(q\), \(r=m-q\), this is

\[
 g^-_q=\binom{m+q-2}{H+q-2}.                            \tag{6.2}
\]

For upper depth \(q\le H-2\), \(r=m+q\), it is

\[
 g^+_q=\binom{m-q-2}{H-q-2}.                            \tag{6.3}
\]

The upper depth \(H-2\) has a unique containing top; upper depth \(H-1\)
has no nontrivial point-kernel and was already automatic in the packet
construction.

Given a multiset \({\cal S}\) of required octahedral moves and a permitted
capacity \(\kappa\) per top, assigning moves to compatible top/order slots
is exactly a bipartite \(b\)-matching.  Its necessary and sufficient Hall
condition is

\[
 \boxed{
 |{\cal A}|\le\kappa|N({\cal A})|
 \quad\text{for every submultiset }{\cal A}\subseteq{\cal S}.}            \tag{6.4}
\]

The large values (6.2) remove raw top scarcity in the lower/shallow band.
They do not control a move multiset concentrated repeatedly on the same
\((r+2)\)-support.  Near the upper boundary, (6.3) shows that genuine top
congestion is possible.

At the crossing scale there are \(N_H\sim W/m\) tops.  A total of
\(R=o(W/H)\) independently realized moves has average congestion

\[
 \frac R{N_H}=o(m/H)=o\!\left(\sqrt{m/\log m}\right).    \tag{6.5}
\]

This is compatible with moderate per-top capacity, but Hall condition
(6.4), not the average alone, is the exact integral requirement.

## 7. Correct replacement gate

The failed \(O(D)\) theorem should be replaced by a statement controlling
at least the pair discrepancy

\[
 \mathcal P_2(\mu,\nu)
 :=\frac14\|A_2(\mu-\nu)\|_1.                           \tag{7.1}
\]

Every octahedral route has length at least \(\mathcal P_2\).  A useful
absorber theorem would need, for the actual packet-generated load vectors,

\[
 \mathcal P_2=o(W/H)                                    \tag{7.2}
\]

together with a positive routing theorem of comparable length and the top
Hall condition (6.4).

Neither equal point marginals, bounded loads, nor \(D=o(W)\) implies
(7.2).  The packet construction must therefore control second-order
incidence as part of the main design, or use higher-order nonlocal trades
which move many pair incidences per unit word cost.

## 8. Pair balance is fractionally easy for top packets

The pair obstruction is not an arithmetic obstruction to the packet family
itself.  It becomes difficult only when coupled to middle disjointness.

Choose one cyclic order independently and uniformly inside every top
\(U\in\binom{[2m]}M\), without imposing middle-owner disjointness.  Fix an
interval length \(r<M\) and a coordinate pair \(e=\{x,y\}\).  The number
of tops containing \(e\) is

\[
 L=\binom{2m-2}{M-2}.                                    \tag{8.1}
\]

Inside one such top, let \(Z_U(e,r)\) be the number of cyclic
rank-\(r\) intervals containing \(e\).  Double counting pair--interval
incidences gives

\[
 \mathbb E Z_U(e,r)=\frac{r(r-1)}{M-1},                 \tag{8.2}
\]

and always \(0\le Z_U(e,r)\le r\).

### Proposition 8.1 (simultaneous packet pair concentration)

There is a one-order-per-top family such that, simultaneously for every
controlled rank \(r\in[m-H,m+H-1]\) and every coordinate pair \(e\),

\[
 \left|
 \sum_{U\supset e}Z_U(e,r)
 -L\frac{r(r-1)}{M-1}
 \right|
 =O\!\left(r\sqrt{L\log m}\right).                      \tag{8.3}
\]

Consequently the aggregate rank-\(r\) pair-incidence discrepancy from the
uniform mean is

\[
 O\!\left(m^2r\sqrt{L\log m}\right)=o(W/H)             \tag{8.4}
\]

at the crossing scale.

#### Proof

For fixed \(e,r\), the variables \(Z_U(e,r)\), over tops containing
\(e\), are independent and lie in an interval of length \(r\).  Hoeffding's
inequality gives

\[
 \Pr\left(
 \left|\sum Z_U-\mathbb E\sum Z_U\right|>t
 \right)
 \le2\exp\left(-\frac{2t^2}{Lr^2}\right).               \tag{8.5}
\]

Take \(t=C r\sqrt{L\log m}\) with a sufficiently large absolute \(C\),
and union bound over fewer than \(2Hm^2\) choices of \((r,e)\).  This proves
(8.3).

At the crossing scale,

\[
 L
 =N_H\frac{M(M-1)}{2m(2m-1)}
 =\Theta(W/m).                                           \tag{8.6}
\]

Substitution into the sum over \(O(m^2)\) pair coordinates proves (8.4),
because \(W\) is exponential while all remaining factors are polynomial.
\(\square\)

Every packet family already has exact uniform point marginals.  Proposition
8.1 shows that it can also have essentially uniform pair marginals before
middle matching.  What remains unproved is a correlated choice which keeps
(8.3) while making the middle packet supports disjoint and the target loads
nearly balanced.  This is a more precise version of the packet-selection
gate: second-order pseudorandomness must survive the integral near-factor.
