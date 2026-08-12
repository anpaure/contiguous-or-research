# AD23: common-seed assembly of pairwise top-order couplings

Date: 2026-07-25

Pure mathematics only.  No computation, search, solver, or web input is
used.

## 0. Exact outcome

Let

\[
 W=\binom{2m}{m},\qquad
 H=\min\{h:W/\binom{2m}{m-h}\ge m+h\},
 \qquad M=m+H,
\]

and let

\[
 \mathcal T=\binom{[2m]}M,\qquad
 p=|\mathcal T|=\binom{2m}{m-H},\qquad
 S=Mp=(1-o(1))W.
\tag{0.1}
\]

Put

\[
 Q=\left\lfloor\sqrt{m\log\log m}\right\rfloor,
 \qquad J=2Q+1,
 \qquad h_*=H-Q,
 \qquad B_*=\binom M{h_*}.
\tag{0.2}
\]

For every top \(U\), let \(\mathcal O_U\) be its set of directed cyclic
orders modulo rotation.  Thus

\[
 R:=|\mathcal O_U|=(M-1)!.
\tag{0.3}
\]

Two orders on distinct tops are called compatible when they have no common
cyclic-interval target at any rank

\[
 m-Q,m-Q+1,\ldots,m+Q.
\tag{0.4}
\]

The pair-coupling lemma gives the following symmetric bad-degree bound:
for every two distinct tops and every fixed order on either side, at most

\[
 d\le \eta R,
 \qquad
 \eta={JM^2\over B_*}=o(1)
\tag{0.5}
\]

orders on the other side are incompatible.  In particular every two-top
compatibility graph has a perfect matching.

This report proves the first genuinely multi-top consequence of that
lemma.

> **Multi-top common-seed theorem.**  If \(L\) distinct tops satisfy
>
> \[
>  (L-1)d\le {R\over2},
> \tag{0.6}
> \]
>
> then there are bijections
>
> \[
>  f_U:[R]\longrightarrow\mathcal O_U
> \tag{0.7}
> \]
>
> such that, for every phase \(s\in[R]\), all \(L\) orders
> \(\{f_U(s)}\) are pairwise compatible.  Hence one common uniform phase
> gives uniform order marginals at every top, keeps each complete vertical
> interval column intact, and forbids every within-block common target in
> the whole growing window.

In particular the theorem applies to

\[
 L=L_{\rm Hall}:=1+\left\lfloor {1\over2\eta}\right\rfloor.
\tag{0.8}
\]

The proof is an iterated exact Hall argument, not a fractional coupling.
More generally, if a graph of pair constraints has an ordering for which
the sum of normalized bad degrees into every earlier neighborhood is at
most \(1/2\), the same Hall induction gives a global common-seed
resolution, even when its ordinary degree is unbounded.  This is the
strongest unconditional positive compiler obtained here.

The quantitative audit is also exact.  Partition the calibrated tops into
blocks of size at most \(L_{\rm Hall}\), use the theorem in every block,
and choose the block phases independently.  At rank \(r=M-h\), let

\[
 \rho_r={M\over\binom Mr},\qquad
 b_h={hM\over\binom Mh}.
\tag{0.9}
\]

Relative to independent top orders, the total expected balanced factorial
energy saved over all \(J\) hard ranks is at most

\[
 {p(L_{\rm Hall}-1)Jb_{h_*}\over2}
 \le {ph_*\over4M}=o(W).
\tag{0.10}
\]

Independent orders have \(\Theta(JW)\) aggregate energy.  Thus the
multi-top theorem is positive but its guaranteed block scale removes only
a negligible part of the collision mass.  Pairwise Hall cannot by itself
finish coefficient one.

The exact global consistency condition is now isolated.  For a graph
\(G\) on the tops, form the graph \(\mathfrak B(G)\) whose vertices are all
top-order pairs \((U,\pi)\), whose \(R\) vertices over each fixed top form
a clique, and whose cross-edge \((U,\pi)(V,\sigma)\) is present exactly
when \(UV\in E(G)\) and \(\pi,\sigma\) are incompatible.  Then

\[
 \boxed{
 G\text{ has an }R\text{-phase compatible resolution}
 \quad\Longleftrightarrow\quad
 \chi(\mathfrak B(G))=R.}
\tag{0.11}
\]

Equivalently, if one first fixes safe pair bijections on the edges, their
nonabelian product must be the identity around every cycle.  The two-top
Hall lemma supplies no such holonomy control.

For an edge-accounted construction in which nonedges remain pairwise
independent, flattening even one hard row requires weighted average degree
at least

\[
 (1-o(1)){1\over3h}\binom Mh,
\tag{0.12}
\]

whereas (0.8) guarantees only degree

\[
 O\!\left({B_*\over JM^2}\right).
\tag{0.13}
\]

At \(h=h_*\), the ratio between (0.12) and (0.13) tends to infinity like
\(JM^2/h_*\).  Therefore a successful use of the pair couplings must solve
the high-degree coloring/holonomy problem (0.11); disjoint pairs, forests,
or independent Hall blocks cannot carry enough negative covariance.

Even the weighted unbounded-degree Hall compiler has an exact covariance
ceiling.  Two distinct tops can share at most \(J(H+Q)\) hard-window
targets in one pair of orders.  Consequently every graph admitted by that
compiler has total edge-accounted covariance at most

\[
 {pJ(H+Q)\over2}=o(JS),
\tag{0.14}
\]

whereas the independent floor-energy ledger requires \(\Omega(JS)\).
Thus a Hall-compiled common phase can succeed only if its unconstrained
pairs generate almost all of the negative covariance.

Finally, the most natural proposed coherent solution is impossible.  If
one labels every top by a bijection \([M]\to U\) and feeds the same abstract
cyclic order into all labels, then no two tops sharing a hard-rank target
are compatible in every phase.  The obstruction is exact: any two
equal-sized subsets of \([M]\) are simultaneous cyclic intervals in some
cyclic order.  Thus arbitrary order-space bijections, not coordinate
relabelings of one master order, are essential.

## 1. The imported two-top bound

Fix distinct tops \(U,V\).  Let \(D_{UV}\) be the bipartite graph between
\(\mathcal O_U\) and \(\mathcal O_V\) whose edges are the incompatible
pairs.  Write

\[
 d_{UV}=\max\{\Delta_{\mathcal O_U}(D_{UV}),
                    \Delta_{\mathcal O_V}(D_{UV})\},
 \qquad d=\max_{U\ne V}d_{UV}.
\tag{1.1}
\]

The pair lemma proves

\[
 d\le {JM^2R\over B_*}=\eta R.
\tag{1.2}
\]

For completeness, the union-bound scale is transparent.  A fixed order has
\(M\) intervals at a fixed rank.  A prescribed rank-\(r\) subset of the
other top is an interval in a uniform cyclic order with probability

\[
 {M\over\binom Mr}\le {M\over B_*}.
\]

There are \(J\) ranks, giving (1.2).  The estimate is symmetric in the two
tops.  Since \(B_*\) dominates every fixed power of \(m\), \(\eta=o(1)\).

When \(d<R/2\), the compatibility graph between any two order spaces has
minimum degree greater than \(R/2\), and hence a perfect matching.  The
next theorem simultaneously assembles more than two parts.

## 2. Integral common-seed assembly

### Theorem 2.1 (multi-top compatible resolution)

Let \(U_1,\ldots,U_L\) be distinct tops.  Suppose every bipartite
incompatibility graph between two of their order spaces has maximum degree
at most \(d\).  If

\[
 (L-1)d\le {R\over2},
\tag{2.1}
\]

then there are bijections

\[
 f_i:[R]\to\mathcal O_{U_i}
\tag{2.2}
\]

such that \(f_i(s)\) and \(f_j(s)\) are compatible for every phase \(s\)
and every \(i\ne j\).

#### Proof

Choose \(f_1\) arbitrarily.  Suppose \(f_1,\ldots,f_\ell\) have been
constructed, where \(\ell<L\).  Form a balanced bipartite graph
\(A_\ell\) with left side \([R]\) and right side
\(\mathcal O_{U_{\ell+1}}\).  Join phase \(s\) to order \(\sigma\) exactly
when

\[
 \sigma\text{ is compatible with every }f_i(s),
 \qquad1\le i\le\ell.
\tag{2.3}
\]

For fixed \(s\), each of the \(\ell\) previous orders forbids at most
\(d\) right vertices.  Therefore

\[
 \deg_{A_\ell}(s)\ge R-\ell d.
\tag{2.4}
\]

Conversely, fix \(\sigma\) on the right.  For a fixed \(i\), at most
\(d\) orders in \(\mathcal O_{U_i}\) are incompatible with \(\sigma\).
Because \(f_i\) is a bijection, these orders occur at at most \(d\) phases.
Taking the union over \(i\) gives

\[
 \deg_{A_\ell}(\sigma)\ge R-\ell d.
\tag{2.5}
\]

By (2.1), both sides of \(A_\ell\) have minimum degree at least \(R/2\).
Every balanced bipartite graph on \(R+R\) vertices with minimum degree at
least \(R/2\) has a perfect matching.  Indeed, if a left set \(X\) has
\(|X|\le R/2\), then its neighborhood has size at least \(R/2\); if
\(|X|>R/2\), a right vertex outside its neighborhood would have all its
neighbors in a set of size \(R-|X|<R/2\), a contradiction.  Thus Hall's
condition holds.

Use a perfect matching of \(A_\ell\) to define \(f_{\ell+1}\).  It is a
bijection, and (2.3) preserves every earlier pairwise compatibility.
Induction completes the construction. \(\square\)

### Corollary 2.2 (the calibrated growing window)

For all sufficiently large \(m\), every collection of

\[
 L\le1+\left\lfloor{1\over2\eta}\right\rfloor
\tag{2.6}
\]

calibrated tops has a common-seed resolution compatible throughout all
\(J=2Q+1\) hard ranks.

#### Proof

Equations (1.2) and (2.6) give
\((L-1)d\le(L-1)\eta R\le R/2\).  Apply Theorem 2.1. \(\square\)

The conclusion is stronger than choosing one favorable tuple.  Every one
of the \(R\) phases is favorable, and every order of every top occurs
exactly once over the phases.  Hence choosing a uniform phase preserves
all one-top marginals exactly.

The same proof has a weighted graph form which permits unbounded ordinary
degree.

### Theorem 2.3 (weighted-degeneracy common-seed compiler)

Let \(G\) be a graph on a set of calibrated tops.  For \(UV\in E(G)\),
let \(d_{UV}\) be the maximum bad degree between
\(\mathcal O_U,\mathcal O_V\), in either direction, and put

\[
 \delta_{UV}={d_{UV}\over R}.
\tag{2.7}
\]

Suppose the vertices can be ordered \(U_1,\ldots,U_n\) so that

\[
 \sum_{i<j:\,U_iU_j\in E(G)}\delta_{U_iU_j}\le {1\over2}
 \qquad(1\le j\le n).
\tag{2.8}
\]

Then \(G\) has an exact \(R\)-phase compatible resolution.

#### Proof

Repeat the induction in Theorem 2.1, but when adding \(U_j\) impose
compatibility only with its earlier neighbors.  For a fixed phase, the
union of forbidden orders has size at most

\[
 \sum_{i<j:\,U_iU_j\in E(G)}d_{U_iU_j}\le R/2.
\]

For a fixed order on \(U_j\), bijectivity of every earlier phase map gives
the same bound on the number of forbidden phases.  The resulting balanced
bipartite graph has minimum degree at least \(R/2\), so Hall supplies the
next phase bijection. \(\square\)

Thus pair Hall does compile globally on every graph of weighted degeneracy
at most \(1/2\).  Section 6 proves that even this unbounded-degree compiler
cannot account for the needed covariance: a distinct-top incompatibility
can bundle only \(O(JH)\), rather than \(JM\), common hard-window targets.

## 3. Exact block covariance and factorial energy

Partition \(\mathcal T\) into blocks \(\mathcal P\), each of size at most
the bound in Corollary 2.2.  Fix a compatible resolution in each block and
choose one uniform phase independently in every block.

Fix a hard rank \(r\), put

\[
 N_r=\binom{2m}r,
 \qquad
 \rho_r={M\over\binom Mr},
 \qquad
 K_r=\binom{2m-r}{M-r},
 \qquad
 \mu_r=K_r\rho_r={S\over N_r},
\tag{3.1}
\]

and write

\[
 \mu_r=k_r+\theta_r,
 \qquad k_r=\lfloor\mu_r\rfloor,
 \qquad0\le\theta_r<1.
\tag{3.2}
\]

For a target \(T\in\binom{[2m]}r\) and a block \(B\in\mathcal P\), let

\[
 a_{B,T}=|\{U\in B:T\subset U\}|.
\tag{3.3}
\]

### Proposition 3.1 (Poisson-binomial block law)

Let \(Z_T\) be the number of selected packets containing \(T\).  Then

\[
 Z_T=\sum_{B\in\mathcal P}Y_{B,T},
\tag{3.4}
\]

where the \(Y_{B,T}\) are independent Bernoulli variables with

\[
 \Pr(Y_{B,T}=1)=a_{B,T}\rho_r.
\tag{3.5}
\]

In particular

\[
 \mathbb EZ_T=\mu_r,
 \qquad
 \operatorname{Var}(Z_T)
 =\mu_r-\rho_r^2\sum_{B\in\mathcal P}a_{B,T}^2.
\tag{3.6}
\]

#### Proof

Every top containing \(T\) hits it in a uniform order with probability
\(\rho_r\).  Within one compatible block, two different selected orders
cannot both contain \(T\).  Hence the sum of the relevant indicators in
that block lies in \(\{0,1\}\), and its mean is
\(a_{B,T}\rho_r\).  This proves (3.5).  Different blocks use independent
phases.  Summing their Bernoulli means and variances proves (3.6).
\(\square\)

Define the balanced factorial potential

\[
 \Psi_r
 ={1\over2}\sum_T(Z_T-\mu_r)^2
 -{N_r\over2}\theta_r(1-\theta_r).
\tag{3.7}
\]

It is the nonnegative integer excess of
\(\sum_T\binom{Z_T}{2}\) over its minimum at fixed total \(S\).

### Corollary 3.2 (exact expected energy)

The independent-block construction satisfies

\[
 \boxed{
 \mathbb E\Psi_r
 ={1\over2}\left[
 S-\rho_r^2\sum_T\sum_{B\in\mathcal P}a_{B,T}^2
 -N_r\theta_r(1-\theta_r)
 \right].}
\tag{3.8}
\]

Relative to fully independent orders at the tops, the exact energy saving
is

\[
 \boxed{
 \rho_r^2
 \sum_{B\in\mathcal P}
 \sum_{\{U,V\}\subset B}
 \binom{|U\cap V|}{r}.}
\tag{3.9}
\]

#### Proof

Sum (3.6) over all targets and use \(N_r\mu_r=S\).  This proves (3.8).
Also

\[
 \sum_T a_{B,T}^2
 =\sum_{U\in B}\binom Mr
 +2\sum_{\{U,V\}\subset B}\binom{|U\cap V|}{r}.
\]

The diagonal term gives \(S\rho_r\) after summing blocks, exactly the
diagonal Bernoulli correction for independent orders.  The remaining term
gives (3.9). \(\square\)

This identity keeps the whole vertical cyclic order intact.  No rankwise
random variable has been introduced.

## 4. Quantitative limit of the guaranteed Hall blocks

Put \(h=M-r\).  For two distinct tops, \(|U\cap V|\le M-1\), and hence

\[
 \rho_r^2\binom{|U\cap V|}{r}
 \le \rho_r^2\binom{M-1}{r}
 ={hM\over\binom Mh}
 =:b_h.
\tag{4.1}
\]

Moreover

\[
 {b_{h+1}\over b_h}
 ={(h+1)^2\over h(M-h)}<1
\tag{4.2}
\]

uniformly for \(H-Q\le h\le H+Q\) and all sufficiently large \(m\).
Thus

\[
 b_h\le b_{h_*}={h_*M\over B_*}.
\tag{4.3}
\]

If every block has size at most \(L\), then

\[
 \sum_{B\in\mathcal P}\binom{|B|}{2}
 \le {p(L-1)\over2}.
\tag{4.4}
\]

Equations (3.9), (4.1), and (4.4) show that the aggregate energy saving in
all \(J\) rows is at most

\[
 {p(L-1)Jb_{h_*}\over2}.
\tag{4.5}
\]

For the unconditional Hall choice (0.8),

\[
 L-1\le {1\over2\eta}={B_*\over2JM^2}.
\]

Therefore

\[
 {p(L-1)Jb_{h_*}\over2}
 \le {p\over2}{B_*\over2JM^2}J{h_*M\over B_*}
 ={ph_*\over4M}.
\tag{4.6}
\]

Since \(p=(1+o(1))W/m\) and \(h_*=o(M)\), the right side is not merely
\(o(W)\), but \(o(W/m)\).

On the other hand, fully independent top orders satisfy, uniformly in the
hard window,

\[
 \mathbb E\Psi_r
 ={S\over2}(1-\rho_r)
 -{N_r\over2}\theta_r(1-\theta_r)
 \ge(3/8-o(1))W.
\tag{4.7}
\]

Indeed \(S=(1-o(1))W\), \(N_r\le W\),
\(\theta_r(1-\theta_r)\le1/4\), and \(\rho_r=o(1)\).  Combining
(4.6) and (4.7) gives

\[
 \sum_{|r-m|\le Q}\mathbb E\Psi_r=\Theta(JW)
\tag{4.8}
\]

for the independently phased Hall-block construction.  It therefore does
not approach the required \(o(W)\) aggregate energy.

The conclusion of this section is scope-exact.  It does not say that a
larger coherent resolution is impossible.  It says that the resolution
which follows solely from the two-top bad-degree bound, assembled in
independent complete blocks, is quantitatively negligible.

## 5. Exact consistency: coloring and holonomy

Let \(G\) be any simple graph on the calibrated tops.  Define
\(\mathfrak B(G)\) as follows.

* Its vertices are \((U,\pi)\) with \(U\in\mathcal T\) and
  \(\pi\in\mathcal O_U\).
* For each fixed \(U\), all \(R\) vertices \((U,\pi)\) form a clique.
* If \(UV\in E(G)\), join \((U,\pi)\) and \((V,\sigma)\) exactly when
  \(\pi,\sigma\) are incompatible.

### Theorem 5.1 (the exact phase-resolution criterion)

There are bijections \(f_U:[R]\to\mathcal O_U\) such that

\[
 f_U(s)\text{ and }f_V(s)\text{ are compatible}
 \quad(UV\in E(G),\ s\in[R])
\tag{5.1}
\]

if and only if

\[
 \boxed{\chi(\mathfrak B(G))=R.}
\tag{5.2}
\]

#### Proof

Given the bijections, color \((U,f_U(s))\) by \(s\).  The top cliques are
properly colored because every \(f_U\) is bijective; the cross-edges are
properly colored by (5.1).  Hence \(\chi(\mathfrak B(G))\le R\).  Every
top clique has size \(R\), so equality holds.

Conversely, in a proper \(R\)-coloring, every top clique uses all \(R\)
colors exactly once.  Let \(f_U(s)\) be its unique order of color \(s\).
A cross-edge cannot be monochromatic, proving (5.1). \(\square\)

There is also an exact targetwise necessary condition.  Fix a hard-rank
target \(T\), let

\[
 \mathcal A_T=\{U\in\mathcal T:T\subset U\},
\]

and retain the notation \(\rho_r=M/\binom Mr\).

### Proposition 5.2 (stable-set capacity at every target)

If \(G\) has an \(R\)-phase compatible resolution, then

\[
 \rho_r{\bf1}_{\mathcal A_T}
 \in\operatorname{STAB}\bigl(G[\mathcal A_T]\bigr),
\tag{5.3}
\]

where \(\operatorname{STAB}\) is the convex hull of independent-set
incidence vectors.  In particular, for every \(B\subseteq\mathcal A_T\),

\[
 \boxed{
 \alpha(G[B])\ge\rho_r|B|.}
\tag{5.4}
\]

Equivalently,

\[
 \chi_f\bigl(G[\mathcal A_T]\bigr)\le {1\over\rho_r}.
\tag{5.5}
\]

#### Proof

At phase \(s\), let \(I_s(T)\) be the set of tops whose selected order
contains \(T\) as an interval.  It is independent in
\(G[\mathcal A_T]\), because two adjacent hits would be a forbidden common
target.  Every top in \(\mathcal A_T\) hits \(T\) in exactly \(\rho_rR\)
of the \(R\) phases.  Hence

\[
 {1\over R}\sum_{s=1}^{R}{\bf1}_{I_s(T)}
 =\rho_r{\bf1}_{\mathcal A_T},
\]

which proves (5.3).  Restriction to \(B\) and summation of coordinates
gives (5.4).  Scaling the phase weights by \(1/\rho_r\) gives the
fractional coloring in (5.5). \(\square\)

For ranks with \(\mu_r=|\mathcal A_T|\rho_r>1\), this rules out taking
\(G[\mathcal A_T]\) complete.  A high-degree compatible graph must retain
independent-set capacity at least \(\mu_r\) in every target fibre,
simultaneously for all hard ranks.

There is an equivalent nonabelian condition if safe pair bijections are
chosen in advance.  Orient every edge and choose

\[
 \phi_{UV}:\mathcal O_U\to\mathcal O_V,
 \qquad \phi_{VU}=\phi_{UV}^{-1},
\tag{5.6}
\]

with every pair \((\pi,\phi_{UV}(\pi))\) compatible.

### Proposition 5.3 (holonomy criterion for prescribed pair couplings)

There are phase bijections \(f_U\) satisfying

\[
 \phi_{UV}=f_V\circ f_U^{-1}
\tag{5.7}
\]

on every edge if and only if, in every connected component, the ordered
product of the \(\phi\)'s around every closed walk is the identity.

#### Proof

Necessity follows by telescoping (5.7) around the walk.  For sufficiency,
choose a root \(U_0\), choose \(f_{U_0}\) arbitrarily, and transport it
along a path from \(U_0\) to each vertex using the \(\phi\)'s.  Trivial
closed-walk products make the result path-independent, and (5.7) follows.
\(\square\)

On a forest there is no holonomy condition, which is why arbitrary pair
bijections assemble there.  A forest has fewer than \(p\) edges and hence
average degree below two.  The collision ledger below requires a degree
which tends to infinity superpolynomially.  Thus the decisive issue is the
simultaneous choice of safe bijections on a huge cycle space, not the
existence of any individual safe bijection.

## 6. The exact weighted high-degree requirement

For a hard rank \(r=M-h\), define the independent common-target weight of
a top pair by

\[
 w_r(U,V)=\rho_r^2\binom{|U\cap V|}{r}.
\tag{6.1}
\]

This is exactly the expected number of common rank-\(r\) interval targets
of two independent uniform orders.  Put

\[
 \omega_r(G)=\sum_{UV\in E(G)}w_r(U,V).
\tag{6.2}
\]

The relation between compatibility cost and covariance value has an exact
geometric ceiling.  Let

\[
 t(U,V)=|U\setminus V|=|V\setminus U|\ge1
\]

and retain \(\delta_{UV}=d_{UV}/R\) from (2.7).

### Lemma 6.1 (distinct-top collision-bundle ceiling)

For every two distinct tops,

\[
 \boxed{
 \sum_{|r-m|\le Q}w_r(U,V)
 \le A_{t(U,V)}\delta_{UV},}
\tag{6.3}
\]

where

\[
 A_t=\sum_{h=H-Q}^{H+Q}(h-t+1)_+
 \le J(H+Q).
\tag{6.4}
\]

#### Proof

Choose the two top orders independently and uniformly, and let \(X\) be
their number of common hard-window interval targets.  Then

\[
 \mathbb EX=\sum_{|r-m|\le Q}w_r(U,V).
\tag{6.5}
\]

Fix one realization and one rank \(r=M-h\).  Put \(D=U\setminus V\), so
\(|D|=t\).  If a rank-\(r\) interval \(T\) of the order on \(U\) is also
contained in \(V\), then its complementary cyclic \(h\)-interval
\(U\setminus T\) contains \(D\).

There are at most \((h-t+1)_+\) cyclic \(h\)-intervals containing a fixed
\(t\)-set when \(h<M/2\).  To see this, a containing interval exists only
if the complementary \((M-h)\)-interval lies inside one gap between
successive elements of \(D\).  Because \(M-h>M/2\), at most one such gap
is long enough.  Its length is at most \(M-t\), so the number of possible
complements, and hence of containing \(h\)-intervals, is at most

\[
 (M-t)-(M-h)+1=h-t+1.
\]

Thus pointwise \(X\le A_t\).  Also

\[
 \Pr(X>0)={|E(D_{UV})|\over R^2}
 \le {Rd_{UV}\over R^2}=\delta_{UV}.
\]

Therefore \(\mathbb EX\le A_t\Pr(X>0)\le A_t\delta_{UV}\), proving
(6.3). \(\square\)

### Corollary 6.2 (weighted Hall compilation cannot pay the ledger)

Let \(G\) satisfy the weighted-degeneracy hypothesis (2.8).  Then

\[
 \boxed{
 \sum_{|r-m|\le Q}\omega_r(G)
 \le {pJ(H+Q)\over2}.}
\tag{6.6}
\]

#### Proof

Orient every edge toward its later endpoint in the ordering (2.8).
Summing (2.8) over vertices gives

\[
 \sum_{UV\in E(G)}\delta_{UV}\le {p\over2}.
\]

Now sum Lemma 6.1 over the edges. \(\square\)

The right side of (6.6) is smaller than the aggregate covariance required
by a factor tending to zero:

\[
 {pJ(H+Q)/2\over JS/6}
 ={3(H+Q)\over M}=o(1).
\tag{6.7}
\]

Thus even the unbounded-degree compiler in Theorem 2.3 cannot finish in an
edge-accounted model.  Reaching coefficient one through such a common
phase would require the unconstrained pairs to supply essentially all of
the negative covariance.

Suppose a marginal-uniform law makes every edge of \(G\) compatible and
makes every nonedge pair independent.  Let

\[
 F_r=\sum_T(Z_T-k_r)(Z_T-k_r-1)=2\Psi_r.
\tag{6.8}
\]

The exact covariance identity gives

\[
 \mathbb EF_r
 =N_r\bigl(k_r+\theta_r^2-\mu_r\rho_r\bigr)
 -2\omega_r(G).
\tag{6.9}
\]

Uniformly in the hard window, the first term is at least \(S/3\) for all
sufficiently large \(m\).  Indeed, if \(k_r=0\), then
\(N_r\theta_r^2=S\theta_r\ge S/2\); if \(k_r\ge1\), then
\(N_rk_r\ge S/2\); and \(S\rho_r=o(S)\).

In particular, if \(G\) also satisfies (2.8), then Corollary 6.2 gives the
aggregate lower bound

\[
 \sum_{|r-m|\le Q}\mathbb EF_r
 \ge {JS\over3}-pJ(H+Q)
 =\left({1\over3}-o(1)\right)JS.
\tag{6.9a}
\]

Thus the weighted-degeneracy Hall compiler plus independent nonedges fails
by a factor \(\Theta(J)\) even against the desired \(o(W)\) aggregate.

Therefore \(\mathbb EF_r=o(W)\) forces

\[
 \omega_r(G)\ge {S\over6}-o(W).
\tag{6.10}
\]

By (4.1), every edge has weight at most \(b_h\).  Consequently

\[
 |E(G)|\ge(1-o(1)){S\over6b_h},
\tag{6.11}
\]

and its average degree satisfies

\[
 \boxed{
 {2|E(G)|\over p}
 \ge(1-o(1)){M\over3b_h}
 =(1-o(1)){1\over3h}\binom Mh.}
\tag{6.12}
\]

At \(h=h_*\), compare (6.12) with the complete-block degree guaranteed by
Corollary 2.2:

\[
 {\binom M{h_*}/(3h_*)
  \over B_*/(2JM^2)}
 ={2JM^2\over3h_*}\longrightarrow\infty.
\tag{6.13}
\]

This proves the advertised high-degree consistency gap.

The nonedge-independence clause in (6.9) is essential.  A single global
phase makes all top variables dependent, and unconstrained pairs may add
either sign of covariance.  For such a law, the exact sufficient condition
is the direct phase ledger

\[
 {1\over R}\sum_{s=1}^{R}
 \sum_{|r-m|\le Q}\Psi_r\bigl(f(s)\bigr)=o(W).
\tag{6.14}
\]

Equation (5.2) is the exact feasibility condition for the pairwise-zero
part of that ledger; (6.14) is the additional quantitative condition.  Pair
Hall alone proves neither at the required high degree.

## 7. Why one master cyclic order cannot synchronize the tops

A tempting common-seed construction is to choose, for every top \(U\), a
fixed labeling

\[
 \ell_U:[M]\to U
\]

and set

\[
 f_U(\pi)=\ell_U(\pi)
\tag{7.1}
\]

for the same abstract cyclic order \(\pi\) of \([M]\).  Every \(f_U\) is
a bijection, so all marginals are perfect.  It cannot make even one
overlapping top pair compatible in every phase.

### Lemma 7.1 (simultaneous-interval lemma)

Let \(A,B\subset[M]\) satisfy

\[
 0<|A|=|B|<M.
\]

There is a cyclic order of \([M]\) in which both \(A\) and \(B\) are
cyclic intervals.

#### Proof

Arrange the four disjoint blocks

\[
 [M]\setminus(A\cup B),\quad A\setminus B,
 \quad A\cap B,
 \quad B\setminus A
\tag{7.2}
\]

consecutively around a circle, omitting empty blocks and ordering elements
inside each block arbitrarily.  Then \(A=(A\setminus B)\cup(A\cap B)\)
and \(B=(A\cap B)\cup(B\setminus A)\) are each consecutive. \(\square\)

### Corollary 7.2 (coordinate-relabeling obstruction)

Suppose distinct tops \(U,V\) share a proper rank-\(r\) target \(T\).  For
arbitrary fixed labelings \(\ell_U,\ell_V\), the common-seed maps (7.1)
have an incompatible phase.

#### Proof

Apply Lemma 7.1 to

\[
 A=\ell_U^{-1}(T),\qquad B=\ell_V^{-1}(T).
\]

In the resulting phase, \(T\) is a cyclic interval in both selected top
orders. \(\square\)

Thus the required safe bijections of order spaces are necessarily highly
non-geometric permutations of the \((M-1)!\) cyclic orders.  Coordinate
permutations, fixed phase shifts, and one master abstract cycle do not
solve the holonomy problem.

## 8. Pairwise density alone cannot give a larger complete block

The scale \(1/\eta\) is an intrinsic limit of what can follow from only a
pairwise bad-degree hypothesis.

### Proposition 8.1 (abstract sharpness example)

Let \(R=td\) with integers \(t\ge2\), \(d\ge1\).  There is a family of
arbitrarily many \(R\)-element order spaces such that:

1. every fixed order is incompatible with exactly \(d\) orders in every
   other part;
2. every two-part compatibility graph has a perfect matching; but
3. no phase can select pairwise compatible orders from more than \(t=R/d\)
   parts.

#### Proof

Partition each part into \(t\) labeled classes of size \(d\).  Declare two
orders in different parts incompatible exactly when their class labels
agree.  This gives bad degree \(d\).  A cyclic shift of the class labels,
together with arbitrary bijections inside classes, gives a compatible
perfect matching between any two parts.  But a pairwise compatible tuple
must use distinct class labels, so it has size at most \(t\). \(\square\)

Theorem 2.1 reaches half this general upper scale.  Special structure of
cyclic intervals might permit much larger non-clique constraint graphs,
but that would be a new theorem about (5.2), not a consequence of the
two-top matchings.

## 9. Proved and unproved boundary

### Proved

1. Up to \(1+\lfloor1/(2\eta)\rfloor\) arbitrary calibrated tops admit an
   exact common-seed resolution whose complete vertical columns are
   pairwise compatible in every hard rank.
2. Independent use of these resolutions in blocks has the exact
   Poisson-binomial load law (3.4)--(3.6) and exact factorial-energy ledger
   (3.8)--(3.9).
3. At the guaranteed Hall scale, the total possible energy saving is at
   most \(ph_*/(4M)=o(W)\), while the starting aggregate energy is
   \(\Theta(QW)\).
4. A global graph of pair constraints has a common-seed resolution exactly
   when its order incompatibility graph is \(R\)-colorable.
5. Prescribed pair bijections synchronize exactly when every cycle has
   trivial holonomy.
6. In the edge-accounted/nonedge-independent model, one hard row already
   needs weighted average degree \((1-o(1))\binom Mh/(3h)\).
7. A master cyclic order transported by fixed coordinate labelings cannot
   satisfy even one overlapping pair constraint for every phase.
8. Pairwise bad degree alone cannot guarantee all-pairs-compatible blocks
   larger than order \(1/\eta\).
9. Every constraint graph of normalized bad-degree degeneracy at most
   \(1/2\) has an integral common-seed resolution, even at unbounded
   ordinary degree.
10. Such a weighted Hall compiler can account for at most
    \(pJ(H+Q)/2=o(JS)\) aggregate negative covariance, by the exact
    distinct-top collision-bundle ceiling.
11. Every target fibre obeys the stable-set condition
    \(\rho_r\mathbf1\in\operatorname{STAB}(G[\mathcal A_T])\), hence
    \(\alpha(G[B])\ge\rho_r|B|\) for every induced subgraph.

### Unproved

1. An \(R\)-coloring of \(\mathfrak B(G)\) for any graph \(G\) carrying
   the weights required in (6.10) simultaneously through all hard ranks.
2. A coherent choice of safe edge bijections with trivial holonomy on such
   a high-degree graph.
3. Direct phase balance (6.14) when nonedge covariances are allowed to be
   global.

Hence the pair-coupling lemma does have a rigorous integral multi-top
consequence, but it stops far before coefficient one.  The remaining gate
is no longer pair coupling: it is a high-degree, vertically coherent
\(R\)-coloring (equivalently a nonabelian synchronization) whose weighted
negative covariance is linear in \(W\) at every shallow rank.

## 10. Independent audit

The decisive constants were checked independently.

1. In Theorem 2.1, both sides of the stage-\(\ell\) Hall graph have degree
   at least \(R-\ell d\); the right-side estimate genuinely uses the
   bijectivity of every earlier phase map.
2. In (3.9), the factor \(1/2\) in the variance potential cancels the
   factor two from ordered expansion of \(a_{B,T}^2\); no factor two is
   missing.
3. Equations (4.5)--(4.6) give exactly \(ph_*/(4M)\).
4. The circular-gap proof of Lemma 6.1 gives exactly
   \((h-t+1)_+\), including the zero case \(t>h\).
5. Summing the incoming normalized bad-degree budgets gives exactly
   \(\sum_e\delta_e\le p/2\), and the covariance identity then gives
   \(JS/3-pJ(H+Q)\) in (6.9a).
6. The nonedge-independence scope in Section 6 is essential and has not
   been suppressed: (6.6) controls only covariance explicitly accounted
   for by compatible edges.
