# Tensor associators: exact Boolean transport, the macroblock invariant, and the Hamming-order bottleneck

Date: 2026-07-26

Method: pure mathematics.  No search or solver input is used.

## 0. Outcome

Tensor (r) independent copies of the eight-coordinate pair-frame
associator.  In local block (B_i), let the two shores be denoted by
(\varepsilon_i=0,1), and put

\[
                         \varepsilon=(\varepsilon_1,\ldots,
                         \varepsilon_r)\in\{0,1\}^r.                \tag{0.1}
\]

Each local support has 24 middle owners and is partitioned into six
isometric (4)-cycles on either shore.  The tensor support therefore has

\[
                         S=24^r                                      \tag{0.2}
\]

owners.  Bundling the (2r) local cube directions by a (Q_{2r}) Hamming
cycle factor gives, for every (\varepsilon), a literal long-cycle factor
on the same tensor support.

There are three distinct conclusions.

1.  The exact (\varepsilon)-transport polytope is a Boolean moment
    polytope.  If (A_{q,I}) is the joint depth-(q) action of the local
    associators indexed by (I\subseteq[r]), then

    \[
      \boxed{
      \mu_q^\varepsilon
        =\sum_{I\subseteq[r]}\varepsilon_I A_{q,I},
      \qquad \varepsilon_I:=\prod_{i\in I}\varepsilon_i.}           \tag{0.3}
    \]

    Hence

    \[
      \boxed{
      \operatorname{conv}\{\mu_q^\varepsilon:\varepsilon\in\{0,1\}^r\}
      =\left\{\sum_I y_I A_{q,I}:y\in\operatorname{COR}(r)\right\},} \tag{0.4}
    \]

    where \(\operatorname{COR}(r)\) is the Boolean correlation (moment)
    polytope.  It is not, in general, a zonotope or a product of intervals;
    the higher (A_{q,I})'s record windows meeting several associators.

2.  Every (\varepsilon)-choice preserves the depth-(q) macroblock
    occupancy vector

    \[
      \kappa_q(T)=\bigl(|T\cap B_1|,\ldots,|T\cap B_r|\bigr).         \tag{0.5}
    \]

    Equivalently, if \(\Pi_{\rm mac}\) sums a load vector over equal
    \(\kappa_q\)-cells, then

    \[
      \boxed{\Pi_{\rm mac}\mu_q^\varepsilon
        \text{ is independent of }\varepsilon,
        \qquad
        \Pi_{\rm mac}A_{q,I}=0\ (I\ne\varnothing).}                  \tag{0.6}
    \]

    Thus the (2^r) local choices can overcome the scalar pair-type
    earthmover obstruction once (r=\Omega(\sqrt m)), but they cannot
    repair any deficit already visible in the macroblock projection.

3.  Macroblock conservation **alone does not create a Gaussian-depth
    capacity deficit**.  The quotient inclusion network on macroblock
    occupancy vectors has an explicit perfectly balanced fractional flow,
    and its balanced integer marginal is obtained by ordinary network total
    unimodularity.  Even imposing at most two deletions in any eight-block
    removes only

    \[
                         O(q^3/m^2)=o(1)                              \tag{0.7}
    \]

    of all flags when (q=O(\sqrt m)).  Therefore no analogue of the
    fixed-pair deficit (D_{m,q}=\Theta(W)) follows from (0.6).

What *does* fail is one native Hamming direction order inside one balanced
tensor sector.  When the two directions belonging to each (B_i) are
placed opposite each other in the (2r)-order, a (q\le r) window touches
one of only (r) cyclic (q)-intervals of macroblocks.  The natural
balanced sector has (\binom rq) possible (q)-block deletion profiles.
All (2^r) values of (\varepsilon) have the same support of (r) cells.
Thus a sectorwise quota loses

\[
                         1-{r\over\binom rq}=1-o(1)                   \tag{0.8}
\]

of its macroprofile cells for every (2\le q=o(r)).

Consequently, if \(K\) long-cycle factors are used and each supplies only
one cyclic direction order, sectorwise coverage requires, without any
separation assumption,

\[
                         \boxed{K\ge(1-o(1)){\binom rq\over 2r}.}     \tag{0.9}
\]

For the opposite-pair orders above, each factor exposes only \(r\) cells
and the denominator improves from \(2r\) to \(r\).

A binary hierarchy which creates at most \(2^L\) effective macro-orders
therefore needs

\[
 \boxed{
 L\ge \log_2\binom rq-\log_2(2r)-o(1)
   =q\log_2(r/q)+O(q+\log r).}                                      \tag{0.10}
\]

At (q=x\sqrt m) and (r/\sqrt m\to\infty), this is

\[
 L\ge (x+o(1))\sqrt m\log_2{r\over\sqrt m}-O_x(\sqrt m).            \tag{0.11}
\]

This last lower bound is conditional on **sectorwise** target quotas.  It
does not contradict the macroprofile flow theorem, which routes a target
profile from many different source profiles.  The architecture therefore
has a clean choice:

* use the global cross-sector occupancy flow, leaving coherent cycle
  bundling as the integral gate; or
* insist on tensor-sectorwise quotas, in which case polynomially many
  (\varepsilon)-corners are useless and the hierarchy bound (0.10) is
  unavoidable.

## 1. The local kernels

In one eight-coordinate associator block, measure full-pair type relative
to the original frame

\[
                         ab\mid cd\mid uv\mid wx.                    \tag{1.1}
\]

The 24 middle owners have type enumerator

\[
                         M(z)=16+8z=8(2+z).                          \tag{1.2}
\]

Indeed the local two-set on (a,b,c,d) is one of (ab,cd) for eight
owners and splits the two original special pairs for the other sixteen.

Let (L_d^e(z)) be the aggregate lower-shadow type enumerator when (d)
of the two local cube directions are used and shore (e\in\{0,1\}) is
selected.  For (d=0), no associator action is visible:

\[
                         L_0^0(z)=L_0^1(z)=M(z).                      \tag{1.3}
\]

The explicit associator table gives

\[
                         L_1^0(z)=16+8z,
                         \qquad L_1^1(z)=24.                         \tag{1.4}
\]

The same formula holds for (d=2): on the old shore the four special
orientation cycles give sixteen type-zero intersections and the two
reservoir cycles give eight type-one intersections; on the new shore all
24 intersections have type zero.  Hence

\[
                         L_2^0(z)=16+8z,
                         \qquad L_2^1(z)=24.                         \tag{1.5}
\]

Thus a touched new-shore block deletes one Bernoulli pair-type contribution,
whereas an untouched block is independent of (\varepsilon_i).

The upper-shadow statement is the translated dual: a touched new-shore
block moves the local type from the old (16z+8z^2) distribution to
(24z).

## 2. Exact Boolean expansion

For completeness, (0.3) does not require a synchronization assumption.
Every function from \(\{0,1\}^r\) to a real vector space has the unique
Möbius expansion

\[
 A_{q,I}=\sum_{J\subseteq I}(-1)^{|I|-|J|}\mu_q^{\mathbf1_J},
 \qquad
 \mu_q^\varepsilon=\sum_{I\subseteq\operatorname{supp}\varepsilon}
 A_{q,I}.                                                          \tag{2.0}
\]

Thus (0.3)--(0.4) hold for every coherent choice of the \(2^r\) bundled
factors.  The following sharper formula identifies the coefficients when
the product bundling uses the natural synchronized owner/phase coupling.

Fix such a Hamming-bundled tensor factor.  Index its owners (including
their cycle phase) by \(\omega\).  For the depth-\(q\) window starting at
\(\omega\), let

\[
 d_i(\omega,q)\in\{0,1,2\}                                           \tag{2.1}
\]

be the number of local directions from \(B_i\) used by the window.  Let
\(\delta_i(\omega,q)\in\{0,1\}\) be the indicator that

1. (d_i(\omega,q)>0), and
2. the old-shore local target belongs to the eight type-one occurrences
   in (1.4)--(1.5).

Put (f_0(\omega,q)) for the target's original-frame type when every
shore is zero.  The local table gives the exact pointwise identity

\[
 f_\varepsilon(\omega,q)
   =f_0(\omega,q)-\sum_{i=1}^r\varepsilon_i\delta_i(\omega,q).        \tag{2.2}
\]

Consequently the type generating polynomial is

\[
\begin{aligned}
 G_q^\varepsilon(z)
 &=\sum_\omega z^{f_\varepsilon(\omega,q)}\\
 &=\sum_\omega z^{f_0(\omega,q)}
   \prod_{i=1}^r
     \left[1+\varepsilon_i\delta_i(\omega,q)(z^{-1}-1)\right]\\
 &=\sum_{I\subseteq[r]}\varepsilon_I(z^{-1}-1)^{|I|}
    \sum_\omega z^{f_0(\omega,q)}
       \prod_{i\in I}\delta_i(\omega,q).                            \tag{2.3}
\end{aligned}
\]

Taking coefficient vectors in (z) proves (0.3), with

\[
 A_{q,I}=[z^\bullet](z^{-1}-1)^{|I|}
    \sum_\omega z^{f_0(\omega,q)}
       \prod_{i\in I}\delta_i(\omega,q).                            \tag{2.4}
\]

Taking convex hulls proves (0.4).  Formula (2.3) also shows why keeping
only the (r) first-order trade vectors is generally invalid: a single
depth window can meet many local associators, and their joint incidence is
recorded by all (A_{q,I}).

For a fully product-transversal bundling one may package the same statement
more compactly.  If a window touches the macroblock set (J) and
(j=|J\cap\operatorname{supp}\varepsilon|), its aggregate local type
enumerator is

\[
                         24^jM(z)^{r-j}.                              \tag{2.5}
\]

Equation (2.5) is the factorized special case of (2.3), not an assumption
needed for (0.3)--(0.4).

Since every window uses at most (q) macroblocks, (2.2) gives the sharp
order bound

\[
 |f_\varepsilon(\omega,q)-f_0(\omega,q)|\le q.                       \tag{2.6}
\]

Thus Gaussian-depth transport is possible in order of magnitude once
(q=\Theta(\sqrt m)) and (r\ge q/2).  Conversely the two-frame
earthmover theorem implies that (r=\Omega(\sqrt m)) independent local
matching switches are necessary.  The proposed regime
(h=2r\gg\sqrt m) passes this scalar test.

## 3. Macroblock projection is frozen

Both local associator shores use the same middle support in (B_i), and a
local depth-(d) intersection has cardinality (4-d) on either shore.
Therefore, pointwise in (omega),

\[
 |L_q^\varepsilon(\omega)\cap B_i|
     =4-d_i(\omega,q),                                                \tag{3.1}
\]

which is independent of (\varepsilon).  Summing (3.1) over owners proves
(0.6).  In particular no selection, randomization, or convex combination
of the (2^r) tensor corners can change the macroprofile load.

This invariant is strictly stronger than scalar pair-type conservation but
has a different capacity geometry: a lower target profile can be fed by
many larger middle profiles.  It therefore does not automatically yield a
deficit.

## 4. Exact macroprofile flow: no Gaussian marginal obstruction

For this section partition all (2m) coordinates into (b=m/4)
eight-blocks (discard at most seven coordinates into a harmless residual
block when divisibility fails).  A middle macroprofile is

\[
 k=(k_1,\ldots,k_b),\qquad0\le k_i\le8,qquad\sum_i k_i=m,            \tag{4.1}
\]

and a lower target profile is

\[
 \ell=(\ell_1,\ldots,\ell_b),\qquad0\le\ell_i\le8,
 \qquad\sum_i\ell_i=m-q.                                             \tag{4.2}
\]

Their exact cardinalities are

\[
                         V_k=\prod_i\binom8{k_i},
 \qquad                   T_\ell=\prod_i\binom8{\ell_i}.            \tag{4.3}
\]

Define the profile flag flow

\[
 F_{k,\ell}
 ={V_k\over\binom mq}\prod_i\binom{k_i}{\ell_i}                    \tag{4.4}
\]

when (ell_i\le k_i) and (sum_i(k_i-ell_i)=q), and set it to zero
otherwise.

### Theorem 4.1 (perfect macroprofile balance)

The flow (4.4) has source row sums (V_k) and target column sums

\[
                         {W\over N_q}T_\ell.                          \tag{4.5}
\]

Consequently the macroblock occupancy invariant is fractionally compatible
with perfectly constant target loads at every depth.

#### Proof

The row sum is the multivariate Vandermonde identity

\[
 \sum_{\ell\le k,\ |k|-|\ell|=q}
       \prod_i\binom{k_i}{\ell_i}=\binom mq.                         \tag{4.6}
\]

For a column, use

\[
 \binom8{k_i}\binom{k_i}{\ell_i}
   =\binom8{\ell_i}\binom{8-\ell_i}{k_i-\ell_i}.                   \tag{4.7}
\]

Summing the latter factors with total increment (q) gives

\[
 \sum_{k\ge\ell,\ |k|=m}V_k\prod_i\binom{k_i}{\ell_i}
 =T_\ell\binom{m+q}{q}.                                             \tag{4.8}
\]

Finally

\[
 {\binom{m+q}{q}\over\binom mq}={W\over N_q}.                       \tag{4.9}
\]

This proves (4.5). \(\square\)

There is also no integral marginal obstruction.  Put

\[
 c_q=\lfloor W/N_q\rfloor.                                          \tag{4.10}
\]

Give every source profile supply (V_k), every target profile lower
capacity (c_qT_\ell), and upper capacity ((c_q+1)T_\ell).  Flow
(4.4) is feasible.  The profile graph is bipartite, so its network matrix
is totally unimodular; it has an integral feasible flow.  Thus exact
floor/ceiling macroprofile quotas can be met.

### Proposition 4.2 (two deletions per block suffice at Gaussian scale)

Delete from (4.4) every flag using at least three deleted coordinates in
one eight-block.  The removed fraction of all flags is at most

\[
 {m\over4}\binom83{(q)_3\over(2m)_3}
       =O(q^3/m^2).                                                     \tag{4.11}
\]

In particular it is (o(1)) for (q=O(\sqrt m)).

#### Proof

Under the uniform flag flow, the deleted (q)-set is uniform in
(\binom{[2m]}q).  For a prescribed block and a prescribed triple in it,
the probability that the triple is deleted is ((q)_3/(2m)_3).  Union
bound over the (m/4) blocks and their (\binom83) triples gives (4.11).
\(\square\)

Give every original deletion flag weight \(1/\binom mq\).  Its source
degree is one and every target degree is \(W/N_q\ge1\).  After deleting
the bad flags in Proposition 4.2, the total removed flow mass is
\[
                         O(Wq^3/m^2)=o(W).                            \tag{4.12}
\]
If \(r_T\) is the removed load at target \(T\), then
\[
 \left(1-\left({W\over N_q}-r_T\right)\right)_+\le r_T.
                                                                          \tag{4.13}
\]
Summing (4.13) proves that the restricted two-deletions-per-block flag
system has total fractional covering deficit \(o(W)\) at Gaussian depth.

The proposition does not construct one coherent Hamming cycle factor.  It
proves the narrower and important claim that the macroblock invariant
itself has no \(\Theta(W)\) Gaussian orbit-capacity defect.

## 5. The native Hamming-order obstruction inside the balanced tensor sector

Return to the tensor support (mathcal V^r), where every middle owner has
exactly four coordinates in every (B_i).  Place the two Hamming directions
belonging to (B_i) at cyclic distance (r) in the (2r)-direction word.
For (q\le r), every (q)-window then touches (q) distinct macroblocks.
Its lower macroprofile is

\[
 \kappa^J_i=
 \begin{cases}3,&i\in J,\\4,&i\notin J,
 \end{cases}                                                        \tag{5.1}
\]

where (J) is one cyclic interval of length (q) in \(\mathbb Z_r\).
There are only (r) such profiles.  Equation (3.1) shows that the set of
profiles is identical for all (2^r) values of (\varepsilon).

Suppose a sectorwise marginal allocation asks the (S=24^r) occurrences
to be balanced over the (\binom rq) symmetric cells (5.1).  Every cell
has quota (S/\binom rq) fractionally.  A native order is zero off its
(r) cyclic cells.  Hence its missing quota mass is at least

\[
 S\left(1-{r\over\binom rq}\right).                                 \tag{5.2}
\]

This proves (0.8).

An arbitrary cyclic order on the \(2r\) labelled directions has only
\(2r\) starting positions, hence exposes at most \(2r\) macroprofile
cells.  Thus \(K\) possibly different orders expose at most \(2rK\)
cells, proving (0.9).  Opposite-pair orders expose only \(rK\), giving
the stronger denominator \(r\).  If a binary hierarchy of \(L\)
macroblock recouplings creates at most \(2^L\) effective orders, (0.10)
follows.  For \(q=o(r)\), Stirling gives

\[
 \log_2\binom rq=q\log_2(r/q)+O(q),                                  \tag{5.3}
\]

which proves (0.11).

This obstruction is not a contradiction to Theorem 4.1.  Equation (5.2)
forces each target cell to be supplied from the balanced source sector
itself.  Theorem 4.1 uses the essential extra freedom of sending other
middle macroprofiles into the same target cell.  Therefore the rigorous
remaining alternatives are:

1. prove a coherent long-cycle rounding of the cross-sector flow (4.4), or
2. build a macroblock hierarchy with enough effective profile support to
   evade (0.10).

The (2^r) local associator corners solve neither task: all their nonempty
Boolean moments lie in the kernel of (Pi_{\rm mac}).
