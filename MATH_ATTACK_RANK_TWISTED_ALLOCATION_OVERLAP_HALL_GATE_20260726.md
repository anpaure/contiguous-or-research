# The allocation-overlap Hall gate for rank-twisted macroblocks

Date: 2026-07-26

Method: pure mathematics only.  No computation, solver, or web input is
used.

## 0. Verdict

Let

\[
 B_j=A_j\mathbin{\dot\cup}C_j,\qquad |A_j|=|C_j|=d,
 \qquad d\asymp\log m,
\]

and, independently for every block \(j\) and local rank \(k\), choose a
uniform bijection

\[
                 \pi_{j,k}:A_j\longrightarrow C_j.              \tag{0.1}
\]

This alteration is legal: the owner partition uses one matching on each
fixed local-rank layer and never compares two ranks.  Its leave remains
\(2^{m+o(m)}\), and every physical axis still crosses the two halves of a
macroblock.

At the maximal-atlas level the exact lower and upper degrees are

\[
 D_q^-(T)=
 \sum_{\sum a_j=q}\prod_j2^{a_j}
     \binom{z_{j,t_j+a_j}(T_j)}{a_j},                         \tag{0.2}
\]

\[
 D_q^+(U)=
 \sum_{\sum a_j=q}\prod_j2^{a_j}
     \binom{v_{j,u_j-a_j}(U_j)}{a_j}.                         \tag{0.3}
\]

Here \(z_{j,k}\) is the number of \(\pi_{j,k}\)-edges empty in the
lower target and \(v_{j,k}\) is the number full in the upper target.
These are incidence counts, not Hall inequalities.

For

\[
                         q=A\sqrt m+O(1),\qquad A>0,             \tag{0.4}
\]

the allocation union does defeat every positive-density Gaussian cut
which is measurable in the macro/half-rank data and the empty/full
carrier profile.  The reason is not the first moment of (0.2).  A typical
owner has, for each bounded carrier correction, far more than \(q\)
one-hit blocks realizing that correction.  Choosing \(q\) distinct such
blocks gives a legal allocation \(a_j\in\{0,1\}\), tunes the target
carrier to any prescribed bounded Gaussian bin, and simultaneously
prescribes the numbers of \(A\)- and \(C\)-side changes.  Quantitatively,
each required local score class occurs

\[
                  \Theta\!\left({m\over d^{3/2}}\right)\gg q   \tag{0.5}
\]

times.  Thus the union over allocations, rather than a frozen allocation
or an averaged degree, supplies the missing profile capacity.  The same
argument works for both signs.  Since the reservoir property holds with
probability \(1-o(1)\), one may fix a deterministic realization of all
the permutations with these conclusions.

This closes only the **coarse profile cut**.  It does not prove raw Hall:
a family hidden inside one profile cell may still reuse a small set of
owners.  The exact remaining maximal-atlas condition is the weighted
dual

\[
 \boxed{
 \sum_T y_T\le
 \sum_X\max_{T\sim X}y_T\quad\hbox{for every }y_T\ge0,}         \tag{0.6}
\]

and its upper analogue.  Neither (0.2), the saddle below, nor the
reservoir lemma proves (0.6) for arbitrary, block-labelled \(y\).

There is a second, logically later failure.  The physical construction
retains only one \(r\)-set \(I(C)\) in a product cell and installs one
compiler chronology on each packet.  Formulae (0.2)--(0.3) precede both
deletions.  Indeed, for a completely legal localized choice of \(I(C)\),
both signs have an explicit Hall cut of size \((1-o(1))N_q=\Omega(W)\),
with fibre ratio

\[
 {\binom n{t+q}\over\binom nt}
 \quad\hbox{or}\quad
 {\binom n{u-q}\over\binom nu}
       \le \exp(-c q^2/r)=o(1),\qquad n=\Theta(r).              \tag{0.7}
\]

Independent rank permutations do not alter this cut.  Consequently the
rank-twisted theorem, as presently stated with an arbitrary deterministic
axis selector, does not prove coefficient one.  A positive continuation
needs both a quenched within-profile expansion theorem and a dispersed,
row-grouped selector/compiler theorem.

## 1. The three graphs and the exact kernels

Let \(b=\lfloor m/d\rfloor\); residual coordinates contribute only
\(O(d)=o(\sqrt m)\) coordinates and will be suppressed.  For a lower
target \(T\), put

\[
 T_j=T\cap B_j,\qquad t_j=|T_j|,
\]

and define

\[
 z_{j,k}(T_j)=
 |\{a\in A_j:a\notin T_j,\ \pi_{j,k}(a)\notin T_j\}|.          \tag{1.1}
\]

If \(a_j\) elements are added in block \(j\), the source rank is
\(k_j=t_j+a_j\).  Choose \(a_j\) empty matching edges and one of two
endpoints on every chosen edge.  This proves (0.2) exactly.  Distinct
allocations cannot duplicate a source--target pair, because the pair
itself determines every \(a_j=|(X\setminus T)\cap B_j|\).

For an upper target \(U\), put \(u_j=|U\cap B_j|\) and

\[
 v_{j,k}(U_j)=
 |\{a\in A_j:a\in U_j,\ \pi_{j,k}(a)\in U_j\}|.                \tag{1.2}
\]

The source rank is \(u_j-a_j\); choosing \(a_j\) full edges and the
endpoint absent from the source proves (0.3).

It is essential to distinguish:

1. the maximal graph \(G_q^\pm\), counted by (0.2)--(0.3);
2. the selected-axis graph, which also requires every touched edge to
   lie in the retained set \(I(C)\); and
3. the literal factor graph, which additionally requires those axes,
   with their endpoint signs, to be the consecutive depth-\(q\) trace of
   the one compiler installed on the packet.

Every assertion in Sections 2--6 concerns the first graph only.

## 2. Exact random-permutation law

Fix \(R\subseteq A\dot\cup C\), and write

\[
                 \alpha=|R\cap A|,\qquad \gamma=|R\cap C|.
\]

For a uniform bijection \(\pi:A\to C\), the full-edge count is

\[
 F\sim\operatorname{Hyp}(d,\gamma,\alpha),\qquad
 \mathbb EF={\alpha\gamma\over d},                              \tag{2.1}
\]

\[
 \operatorname{Var}F=
 {\alpha\gamma(d-\alpha)(d-\gamma)\over d^2(d-1)}.             \tag{2.2}
\]

The empty-edge count is \(E=d-\alpha-\gamma+F\), with mean

\[
                         \mu^-(R)={(d-\alpha)(d-\gamma)\over d},\tag{2.3}
\]

whereas the full-edge mean is

\[
                         \mu^+(R)={\alpha\gamma\over d}.        \tag{2.4}
\]

If \(k\ne k'\), the statistics measured by \(\pi_{j,k}\) and
\(\pi_{j,k'}\) are conditionally independent given \(R\).

There is also an exact inclusion probability.  If \(T_j\subset X_j\),

\[
 p=|(X_j\setminus T_j)\cap A_j|,\qquad
 s=|(X_j\setminus T_j)\cap C_j|,
\]

and \(\alpha=|X_j\cap A_j|,\gamma=|X_j\cap C_j|\), then

\[
 \Pr(T_j\sim X_j)=
 { (d-\gamma)_{\underline p}(d-\alpha)_{\underline s}
       \over d_{\underline{p+s}}}.                              \tag{2.5}
\]

For \(X_j\subset U_j\), the upper probability is

\[
 \Pr(X_j\sim U_j)=
 { \gamma_{\underline p}\alpha_{\underline s}
       \over d_{\underline{p+s}}}.                              \tag{2.6}
\]

On a central half profile the leading factor is \(2^{-p-s}\), but the
relative error is \(\exp(O((p+s)^2/d))\).  Thus the frequently used
\(2^{-p-s}e^{o(1)}\) statement requires \(p+s=o(\sqrt d)\), not merely
\(o(d^{2/3})\).

## 3. The multivariate coefficient saddle

For the lower sign write the local polynomial

\[
 P_j^-(w)=\sum_{a=0}^d
       2^a\binom{z_{j,t_j+a}(T_j)}a w^a.                        \tag{3.1}
\]

The upper polynomial is defined with \(v_{j,u_j-a}\).  On central
profiles,

\[
                         w_*={2A\over\sqrt m}(1+o(1)).           \tag{3.2}
\]

At this saddle

\[
 {q^2\over b}=\Theta(d),\qquad {q^3\over b^2}=o(1).            \tag{3.3}
\]

Consequently \(q-O(d)\) occupied blocks have allocation one,
\(O(d)\) have allocation two, and allocations at least three contribute
\(o(1)\) to the logarithm.  One must not discard the two-hit term: in

\[
 \log P_j^-(w)=2z_{j,t_j+1}w+
 \left(4\binom{z_{j,t_j+2}}2-2z_{j,t_j+1}^2\right)w^2
 +O(d^3w^3),                                                     \tag{3.4}
\]

the sum of the quadratic terms is \(\Theta(1)\).  Its random fluctuation
is \(o(1)\), but its deterministic contribution is part of the Gaussian
constant.

Define the centered first-coefficient carriers

\[
 Z^-(T)={4\over\sqrt m}\sum_j
 \bigl(z_{j,t_j+1}(T_j)-\mu^-(T_j)\bigr),                       \tag{3.5}
\]

\[
 Z^+(U)={4\over\sqrt m}\sum_j
 \bigl(v_{j,u_j-1}(U_j)-\mu^+(U_j)\bigr).                       \tag{3.6}
\]

Stirling's formula in (2.1), followed by Lindeberg's elementary
triangular-array argument, gives

\[
                         Z^\pm\Longrightarrow N(0,1).           \tag{3.7}
\]

The matching-dependent part of the coefficient saddle is

\[
 \log D_q^\pm=C_q^\pm(\text{macro/half profile})
                         +A Z^\pm+o(1).                          \tag{3.8}
\]

Indeed, the linear perturbation of \(\log P\) is

\[
 w_*\,2\sum_j(z_{j,t_j+1}-\mu_j)=AZ^-+o(1),                    \tag{3.9}
\]

and the centered fluctuation of the quadratic term in (3.4) is bounded
by \(O(d/\sqrt m)=o(1)\).  The upper calculation is identical after
replacing empty by full edges.  Equation (3.8) is an exact use of the
allocation sum at Gaussian order.  It is still only a degree statement.

## 4. A hidden carrier and why the annealed kernel is insufficient

For a middle owner \(X\), put \(k_j=|X\cap B_j|\) and define its lower
look-ahead and upper look-behind carriers

\[
 L^-(X)={4\over\sqrt m}\sum_j
 \bigl(z_{j,k_j+1}(X_j)-\mu^-(X_j)\bigr),                       \tag{4.1}
\]

\[
 L^+(X)={4\over\sqrt m}\sum_j
 \bigl(v_{j,k_j-1}(X_j)-\mu^+(X_j)\bigr).                       \tag{4.2}
\]

Both converge to \(N(0,1)\).  They are independent, to first order, of
the owner's intrinsic split-count fluctuation because the latter uses
\(\pi_{j,k_j}\).

Uniform edge sampling does not make the target carrier independent of
\(L^\pm\).  On every block not touched by an allocation, the corresponding
summands in \(Z^\pm\) and \(L^\pm\) are literally equal.  A uniform
one-hit allocation changes only \(q=o(b)\) blocks.  Thus the edge kernel
augmented by \(L^\pm\) is nearly diagonal.  Forgetting \(L^\pm\) and
retaining only the intrinsic owner status produces an apparently
rank-one kernel, but that projection cannot prove a neighborhood union.

This identifies the precise first-moment gap in an annealed profile
argument.  The next section shows that the allocation **choice**, rather
than the uniform edge law, nevertheless breaks the hidden carrier.

## 5. Exact carrier-edit identities

Consider a lower one-hit block.  Let \(e\) be a split edge of
\(\pi_{j,k_j}\), let \(\xi\in e\cap X_j\), and put
\(T_j=X_j\setminus\{\xi\}\).  The chosen split edge becomes empty, so

\[
                         z_{j,k_j}(T_j)=z_{j,k_j}(X_j)+1.         \tag{5.1}
\]

Define its exact lower edit score

\[
 R^-_{j,\xi}(X)=
 \bigl(z_{j,k_j}(X_j)+1-\mu^-(T_j)\bigr)
 -\bigl(z_{j,k_j+1}(X_j)-\mu^-(X_j)\bigr).                     \tag{5.2}
\]

If \(J\) is a set of \(q\) distinct blocks and one occupied endpoint of
an intrinsic split edge is deleted in every \(j\in J\), then the resulting
target is compatible with \(X\), has allocation \(a_j=1_J(j)\), and

\[
 \boxed{
 Z^-(T)=L^-(X)+{4\over\sqrt m}
                  \sum_{j\in J}R^-_{j,\xi_j}(X)+o(1).}          \tag{5.3}
\]

The \(o(1)\) is only the residual-coordinate normalization; on the
macroblocks the identity is exact.

For the upper sign choose the absent endpoint \(\eta\) of a split edge,
put \(U_j=X_j\cup\{\eta\}\), and define

\[
 R^+_{j,\eta}(X)=
 \bigl(v_{j,k_j}(X_j)+1-\mu^+(U_j)\bigr)
 -\bigl(v_{j,k_j-1}(X_j)-\mu^+(X_j)\bigr).                     \tag{5.4}
\]

Then

\[
 \boxed{
 Z^+(U)=L^+(X)+{4\over\sqrt m}
                  \sum_{j\in J}R^+_{j,\eta_j}(X)+o(1).}         \tag{5.5}
\]

Conditional on central half-ranks, each score is the difference of two
independent hypergeometric variables of variance \(d/16+o(d)\),
plus \(1/2+O(d^{-1/2})\).  In particular its variance is
\(d/8+o(d)\).

## 6. The allocation reservoir lemma

### Lemma 6.1 (two-sided score reservoir)

Fix \(K<\infty\).  With probability \(1-o(1)\) over the independent
rank matchings, all but \(o(W)\) middle owners have the following
property, simultaneously for both signs.

For every integer \(h\) with \(|h|\le K+2\), and for each choice of the
occupied endpoint side \(A\) or \(C\), there are

\[
                 \Theta\!\left({m\over d^{3/2}}\right)          \tag{6.1}
\]

distinct central macroblocks whose one-hit score is

\[
                         h+{1\over2}+O(d^{-1/2}),                \tag{6.2}
\]

and which contain \(\Theta(d)\) intrinsic split edges with the required
occupied endpoint side.

#### Proof

Restrict to the positive-probability block event
\(\alpha,\gamma=d/2+O(\sqrt d)\).  Then (2.1) gives

\[
 \Pr(F=s)=
 {\binom\gamma s\binom{d-\gamma}{\alpha-s}
       \over\binom d\alpha}.                                   \tag{6.3}
\]

Apply Stirling's formula uniformly for
\(s=\alpha\gamma/d+O(\sqrt d)\).  Adjacent central probabilities
have ratio bounded above and below, the central interval has
\(\Theta(\sqrt d)\) points, and its total probability is bounded away
from zero.  Hence every fixed central value has probability
\(\Theta(d^{-1/2})\).  Convolving two independent copies proves the same
bound for every fixed value of their difference.

Given the intrinsic full count \(F\), the numbers of split edges occupied
on the \(A\)- and \(C\)-sides are respectively

\[
                         \alpha-F,\qquad\gamma-F.                \tag{6.4}
\]

Both are \(\Theta(d)\) throughout the central event.  Equations
(5.2) and (5.4) differ from the hypergeometric difference by
\(1/2+O(d^{-1/2})\), proving the one-block probability
\(\Theta(d^{-1/2})\) for every score/side class.

There are \(b\sim m/d\) independent blocks.  The mean number in one
class is therefore \(\Theta(m/d^{3/2})\).  A direct exponential-moment
bound for a sum of independent indicators gives failure probability

\[
                         \exp(-\Theta(m/d^{3/2})).                \tag{6.5}
\]

Conditioning on total rank \(m\) costs only the reciprocal of a central
binomial probability, \(O(\sqrt m)\), and does not affect (6.5).
There are only \(O(K)\) classes.  Averaging first over the atlas and the
owner and then applying Markov's inequality proves the quenched
\(1-o(1)\) assertion.  The upper proof is the complement of the lower
calculation.  \(\square\)

Because

\[
 {m/d^{3/2}\over q}={\sqrt m\over A d^{3/2}}\longrightarrow\infty,\tag{6.6}
\]

the reservoir is much larger than the number of blocks which must be
touched.

### Theorem 6.2 (Gaussian profile reachability)

Fix bounded \(z\) and suppose \(|L^-(X)|\le K\).  Put

\[
                         c={z-L^-(X)\over4A}.                     \tag{6.7}
\]

Invoke Lemma 6.1 with a score cutoff larger than
\((|z|+K)/(4A)+2\).  Choose the two adjacent score classes whose convex
hull contains \(c\),
and take the appropriate integral mixture of \(q\) blocks from those
classes.  The rounding error in the average is \(O(1/q)\), while the
\(O(d^{-1/2})\) offsets in (6.2) are \(o(1)\).  Equations (5.3) and (0.4)
give

\[
                              Z^-(T)=z+o(1).                      \tag{6.8}
\]

The selected axes are intrinsic split edges, so \(T\sim X\) in the exact
maximal graph.  By splitting the reservoir simultaneously by endpoint
side, one may prescribe exactly how many of the \(q\) deletions occur in
\(A\) and how many in \(C\).  The upper construction using (5.5) is
identical.

Let \(K=K_m\to\infty\) sufficiently slowly.  The local Stirling estimate
and the union bound above remain uniform for \(|h|\le K_m\), while

\[
                         \Pr(|L^\pm|>K_m)=o(1).                  \tag{6.9}
\]

Therefore every bounded-width Gaussian carrier bin has, on both signs,
all but \(o(W)\) typical owners as potential neighbors, subject only to
the ordinary half-rank compatibility.  This is a union-of-allocations
statement; a uniformly sampled allocation would not prove it.

The same proof permits finitely many central macro-rank/half-rank
categories.  Split the reservoirs by category.  A fixed central
\((\alpha,\gamma)\)-type and score class still occurs

\[
                         \Theta(m/d^{5/2})\gg q                  \tag{6.10}
\]

times.  Hence every prescribed Gaussian empirical allocation whose
category demands stay below these reservoirs can be realized.  An exact
block-labelled target family is not covered by this statement.

## 7. Profile capacity and the max-flow boundary

The reservoir theorem gives an actual neighborhood statement for whole
profile cells.  To see the capacity explicitly, fix a lower half-rank
profile and let \(\mathcal A\) be the full family of rank-\(m-q\) targets
in it.  Every target has

\[
                         \binom{m+q}q                              \tag{7.1}
\]

ordinary middle supersets.  A middle set contains at most

\[
                         \binom mq                                  \tag{7.2}
\]

rank-\(m-q\) subsets in \(\mathcal A\).  Double counting gives

\[
 |N_{\rm inc}(\mathcal A)|
 \ge {\binom{m+q}q\over\binom mq}|\mathcal A|
 ={W\over N_q}|\mathcal A|
 =(e^{A^2}+o(1))|\mathcal A|.                                  \tag{7.3}
\]

The side-resolved reservoir construction supplies, for almost every
source in this ordinary neighborhood, a safe target in any prescribed
bounded carrier bin contained in the profile.  Thus every admissible
positive-density Gaussian macro/half/carrier cell \(\mathcal C\) covered
by the empirical reservoir conditions of Theorem 6.2 obeys

\[
                         |N_{G_q^\pm}(\mathcal C)|
                              \ge(1-o(1))|\mathcal C|.           \tag{7.4}
\]

In fact its neighborhood contains the whole typical ordinary source
profile made available by (7.3).  The statement is uniform over any
fixed finite union of such cells.  This proves that the fixed-frame
ratio \(e^{-A^2}\) does not survive the allocation union at the coarse
Gaussian level.

Equation (7.4) must not be extended to arbitrary subfamilies of a cell.
For the raw graph, max-flow/min-cut is equivalent to (0.6).  To verify
this, give each target demand one and each owner capacity one.  Separating
the product of owner simplices gives (0.6); indicator weights recover
ordinary Hall.  The kernels (0.2)--(0.3) test only singleton weights, and
Theorem 6.2 tests weights constant on the retained profiles.  A weight
which depends on the exact block labels is not controlled.

The missing statement can be written as the quenched expansion estimate

\[
 |N(\mathcal B)|\ge(1+\varepsilon_A)|\mathcal B|
\quad\hbox{for every retained }
\mathcal B\subseteq\binom{[2m]}{m\mp q},                         \tag{7.5}
\]

after deleting \(o(W)\) vertices.  A cut-norm theorem for products of the
random permutation kernels, or a compression theorem forcing a minimum
cut to be a profile union, would prove (7.5).  The present calculation
does neither.

## 8. Exact owner/selector/compiler constraints

Let \(C\cong Q_S\) be one product status cell.  A physical tiling chooses
one retained set \(I(C)\in\binom{[S]}r\) and freezes the other axes in all
orientations.  For a lower target, allocation \(a\), and chosen empty-edge
set \(D\), the corresponding maximal incidence survives precisely when

\[
                         D\subseteq I(C^-(T;a,D)).                \tag{8.1}
\]

The upper condition is the same with full edges.  Thus the selected
degrees are

\[
 p_q^-(T)=\sum_{a,D}
 \mathbf1_{\{D\subseteq I(C^-(T;a,D))\}},\qquad
 p_q^+(U)=\sum_{a,D}
 \mathbf1_{\{D\subseteq I(C^+(U;a,D))\}},                       \tag{8.2}
\]

apart from the already negligible cells of dimension below \(r\).

After the split, one compiler conjugate \(g_P\) is chosen for the whole
packet, not separately at every owner.  Let

\[
 \tau_{P,g,q}^{\epsilon}
 \subseteq\binom{[2m]}{m+\epsilon q}                             \tag{8.3}
\]

be its literal signed traces.  A fractional all-depth choice exists only
if, for every nonnegative target weight array,

\[
 \boxed{
 \sum_{q,\epsilon,T}y_{q,\epsilon,T}
 \le\sum_P\max_g
       \sum_{q,\epsilon}
       \sum_{T\in\tau_{P,g,q}^{\epsilon}}y_{q,\epsilon,T}.}     \tag{8.4}
\]

This is the exact grouped outer Hall dual.  It forces lower and upper
signs and all protected depths to use one common row \(g_P\).  Solving
(0.6) separately for the two signs would not imply (8.4).

Equivalently, in the selector-fibre refinement let a row be
\(R=(C,z)\), let an option \(\omega=(I,g)\) contain both the retained
axis set and compiler conjugate, and let
\(b^\epsilon_{R,\omega,q}(T)\in\{0,1\}\) be literal incidence.  The exact
integral owner/compiler system is

\[
 x_{R,\omega}\in\{0,1\},\qquad
 \sum_\omega x_{R,\omega}=1,\qquad
 \sum_{R,\omega}x_{R,\omega}
 b^\epsilon_{R,\omega,q}(T)\ge1.                               \tag{8.5}
\]

The first equality is the owner grouping constraint.  Replacing each row
by its average over \(\omega\) proves only balanced marginals and is not a
relaxation which can automatically be rounded row by row.

The allocation reservoir survives a genuinely dispersed selected set:
if the \(r\) retained axes sample the score classes proportionally and

\[
                         r\gg q\sqrt d,                            \tag{8.6}
\]

then each required score class contributes much more than \(q\) retained
axes.  The proposed \(r=m^{3/5+o(1)}\) satisfies (8.6).  But neither an
arbitrary deterministic selector nor aggregate complete-design marginals
imply this rowwise property, and (8.5) still does not make the selected
axes consecutive in one compiler word.

## 9. The explicit physical Hall cut

The unspecified selector admits the following legal failure.  Let \(E\)
be the union of the first complete macroblocks with

\[
                         n=|E|\in[16r,16r+2d).                    \tag{9.1}
\]

All but \(o(W)\) owners have at least \(r\) intrinsic split axes in \(E\).
For those product cells choose all retained axes inside \(E\); choose
arbitrarily on the exceptional cells.  This is an exact parallel-\(Q_r\)
owner partition for every realization of the rank permutations.

For the lower sign, take targets satisfying

\[
 \left||T\cap E|-{n(m-q)\over2m}\right|\le q/10.                \tag{9.2}
\]

They form \((1-o(1))N_q\) targets because their hypergeometric variance is
at most \(n/4=o(q^2)\).  Fix their exterior set and write
\(t=|T\cap E|\).  A localized packet preserves the exterior and its source
has \(t+q\) coordinates in \(E\).  Hence the exact source/target capacity
ratio in this fibre is

\[
                         {\binom n{t+q}\over\binom nt}
                         \le\exp(-c q^2/n)=o(1).                 \tag{9.3}
\]

The last inequality is the elementary product comparison of binomial
coefficients on opposite sides of \(n/2\), and uses
\(q^2/n\asymp q^2/r\to\infty\).  Exceptional packets contribute only
\(o(W)=o(N_q)\) targets.

For the upper sign use the corresponding central window about
\(n(m+q)/(2m)\).  At fixed exterior set the ratio is

\[
                         {\binom n{u-q}\over\binom nu}
                         \le\exp(-c q^2/n)=o(1).                 \tag{9.4}
\]

The cut is independent of the identities of the local matchings and of
the compiler: every possible trace of a localized packet preserves the
exterior.  Therefore both literal signed target layers have
\((1-o(1))N_q=\Omega(W)\) holes for this legal selector.

This is not a universal obstruction to a dispersed selector.  It is a
sharp obstruction to claiming a physical Hall theorem from the owner
tiling, the kernel (0.2), or independent rank permutations alone.

## 10. Certified boundary

Proved here:

1. the exact lower and upper allocation kernels for independent rank
   permutations;
2. the Gaussian coefficient saddle, including the non-negligible
   two-hit term;
3. the hidden look-ahead carrier which an annealed first moment forgets;
4. the two-sided score-reservoir theorem, showing that the allocation
   union removes every positive-density Gaussian profile cut;
5. the exact raw and grouped max-flow duals; and
6. an explicit \(\Omega(W)\) physical Hall cut for a legal localized
   selector, valid for both signs and every compiler.

Not proved:

1. quenched Hall expansion inside one exact profile cell;
2. a deterministic dispersed \(r\)-axis selector satisfying the raw dual;
3. an integral choice of one compiler row per packet; or
4. simultaneous lower/upper, all-depth coefficient-one coverage.

The correct next gate is therefore not another degree calculation.  It is
a block-labelled cut-norm/compression theorem followed by the grouped
selector/compiler inequality (8.4).

The direction-level selector part is advanced in
MATH_THEOREM_TRANSVERSAL_AXIS_SELECTOR_AND_COMPILER_HALL_GATE_20260726.md:
an exact nonparallel product-of-matchings \(Q_r\)-tiling satisfies the
sharp anti-localization law
\[
 \nu_q(D\subseteq E)\le(1+o(1))
       (|E|/(S-o(S)))^q
\]
for the actual lower and upper compiler occurrences.  It removes the
specific localized-\(E\) cut but leaves the arbitrary literal
configuration inequality open.
