# Audit of the buffered diagonal generator for weighted RPRN

Date: 2026-07-27

Scope: constant-one repaired promotion-ring packing only.  This is an
independent audit of the unconditional growing-rank claim in
`MATH_THEOREM_REPAIRED_RING_GROWING_UNIFORMITY_SLOW_BITE_TRAJECTORY_20260726.md`.

## 0. Verdict

The weighted exception criterion is correct.  The multiplicity-aware
intersection variables

\[
 B_X^{\boldsymbol c}(e_1,\ldots,e_j)
 =\sum_{f\ni X}\prod_{i=1}^j\binom{|f\cap e_i|}{c_i}             \tag{0.1}
\]

also correctly encode repeated use of the same selected edge in a
generator power.  Thus the earlier purely algebraic diagonal objection is
repaired.

The unconditional trajectory theorem is nevertheless not proved.  Its
order truncation has a boundary gap.  An energy of total witness order
\(J-1\) can ask for order \(J+1\) after one generator increment.  It does
not acquire \(J\) factors of the small mesh parameter.  Therefore the
tail claimed in the current Lemma 5.1 does not follow from a hierarchy
recorded only through order \(J\).

Taking

\[
 J=\Theta(\log m),\qquad L=\Theta((\log m)^2)                    \tag{0.2}
\]

repairs the distance from the core to the boundary, but it does not by
itself control the energy entering through the top boundary \(L\).  One
must prove either the boundary-flux estimate BF\((J,L)\) in Section 4 or
the diagonal link-energy estimate DLE in Section 5.

Conditional on either estimate, every martingale and predictable-drift
constant closes through

\[
 T=\Theta(m\log m),\qquad z=m^{-1/20}.                            \tag{0.3}
\]

The resulting bad-owner incidence is

\[
 \exp[-\Omega((\log m)^2)]\,rE_t=o(E_t),                         \tag{0.4}
\]

which is exactly weighted RPRN.  No stochastic counterexample to the
actual repaired-ring process is obtained.  The correct status is a sharp
unproved boundary-flux theorem, not an unconditional positive theorem and
not a negative model obstruction.

## 1. Weighted mass is the right target

Let \(E_t\) be the number of active rooted edges.  Then

\[
 \sum_A d_t(A)=E_t,\qquad \sum_Xd_t(X)=rE_t.                     \tag{1.1}
\]

For fixed positive root density, \(E_t=\Theta(N_HR_t)\).  If an owner
set \(\mathcal B_t\) satisfies

\[
                         \sum_{X\in\mathcal B_t}d_t(X)=o(E_t),   \tag{1.2}
\]

then deleting every edge meeting \(\mathcal B_t\) removes at most
\(o(E_t)\) active edges.  Static or literal root-neighbourhood coverage
is irrelevant.

Notice the factor \(r\).  A bad-owner probability merely \(o(1)\) gives
bad incidence \(o(rE_t)\), which need not be \(o(E_t)\).  Weighted RPRN
requires a size-biased bad probability \(o(1/r)=o(1/m)\).

## 2. What the multiplicity hierarchy proves

For pairwise disjoint protected edges \(e_1,\ldots,e_j\), the static
endpoint exposure gives, uniformly for total witness order
\(s=\sum_i c_i=o(m)\),

\[
 {B_X^{\boldsymbol c}(e_1,\ldots,e_j)\over D_X}
 \le\left({Cs^4\over m^2}\right)^s+m^{-H/5}.                     \tag{2.1}
\]

The corresponding power energy is

\[
 \sum_{(e_1,\ldots,e_j)}^*
 \left(B_X^{\boldsymbol c}(e_1,\ldots,e_j)\right)^h
 \le (KD)^jD_X^h
       \left({Cs^4\over m^2}\right)^{hs-j},                     \tag{2.2}
\]

for \(hs=o(m)\).  Equation (2.2) is important: if the next selected edge
is \(g\), the term

\[
             B_X^{\boldsymbol c}(e_1,\ldots,e_j,g)^\ell         \tag{2.3}
\]

repeats \(g\), and (2.2), rather than a distinct-\(g\) marginal product,
is the correct static object.  D's revised hierarchy therefore repairs
the local repeated-edge algebra.

The issue is temporal.  Formula (2.2) is a time-zero estimate.  At a
later stopping time its scaled version is itself one of the quantities
which must be regenerated.

## 3. The exact failure of the unbuffered truncation

Let \(A\) be a protected mesh count of total witness order \(q\), and let
\(B(g)\) be its decrement when \(g\) is selected.  For a power \(h\),

\[
 (A-B(g))^h-A^h
 =\sum_{\ell=1}^h(-1)^\ell\binom h\ell
       A^{h-\ell}B(g)^\ell.                                    \tag{3.1}
\]

After summing over \(g\), (2.3) places the \(\ell\)-term at a higher
total witness order.  If the starting energy has order \(J-1\), the
\(\ell=2\) term may already require order \(J+1\).  Hence leaving a
hierarchy truncated at \(J\) may cost only one order-raising generator
factor.

For the parameters claimed in the growing-rank trajectory,

\[
 \varepsilon_*={C(\log m)^4\over m^2z^2},\qquad
 T=\Theta(m\log m),\qquad z=m^{-1/20},                            \tag{3.2}
\]

and therefore

\[
                         T\varepsilon_*
 =O(m^{-9/10}(\log m)^5).                                      \tag{3.3}
\]

This tends to zero, but it is not \(o(1/m)\).  If it were the only bound
on the bad owner fraction, its incidence cost after multiplication by
\(r\sim m\) would be

\[
                         rT\varepsilon_*
 =O(m^{1/10}(\log m)^5),                                       \tag{3.4}
\]

which is not harmless.  Thus the weighted reformulation does not make the
unbuffered exit error disappear.

## 4. The exact buffered boundary-flux estimate

Put

\[
 J=C_0\log m,\qquad L=C_1(\log m)^2.                            \tag{4.1}
\]

Let \(\mathscr E_q(t)\) denote the sum of all normalized multiplicity
power energies of total witness order (q), weighted by their base owner
incidences.  Let \(\mathcal K_{q,q'}(t)\) be the positive generator
kernel taking order (q) to order (q'>q) after the reference drift is
subtracted.  This kernel is defined literally by expanding (3.1), applying
binomial inversion in every selected-edge intersection, and collecting
terms by total witness order.

For (q_0\le J), define the chronological flux through level (L) by

\[
\begin{aligned}
 \operatorname {Flux}_{q_0,L}(T)
 :=\sum_{n\ge1}
 \int_{0<t_1<\cdots<t_n<T}
 \sum_{\substack{q_0<q_1<\cdots<q_n\\
                  q_{n-1}\le L<q_n}}
 \prod_{i=1}^n\mathcal K_{q_{i-1},q_i}(t_i)
 \,\mathscr E_{q_n}(t_n)\,dt_1\cdots dt_n .                    \tag{4.2}
\end{aligned}
\]

The exact missing buffered theorem is

\[
 \boxed{
 \sum_{q_0\le J}\operatorname {Flux}_{q_0,L}(T)
 \le \beta_m E_0,
 \qquad \beta_m=o(1/m).}                                      \tag{BF}
\]

This is not automatic from the distance \(L-J\).  A distant boundary
gives many small factors only after the energy entering from orders
greater than \(L\) is controlled.  BF is precisely that top-boundary
control.

The static hierarchy (2.2) suggests the stronger numerical bound

\[
                         \beta_m
 \le \exp[-c(\log m)^2],                                       \tag{4.3}
\]

because a chronological chain advancing from core order \(J\) to level
\(L\) has at least \(\Omega((L-J)/J)=\Omega(\log m)\) effective
order-raising blocks, while

\[
 {TCL^4\over m^2z^2}
 =O(m^{-9/10}(\log m)^9).                                      \tag{4.4}
\]

But (4.3) is a consequence of BF, not a proof of BF.

## 5. Equivalent diagonal link-energy formulation

A stronger, local sufficient condition avoids the top-boundary notation.
For a protected cluster

\[
 C=(X;e_1,\ldots,e_j),\qquad
 A_C=a_{X,t}(e_1,\ldots,e_j),
\]

put \(A_C(g)=a_{X,t}(e_1,\ldots,e_j,g)\).  Outside owners of total
incidence \(o(E_t)\), require throughout the full available witness range
\(j+\ell\le r\),

\[
 \boxed{
 \sum_g^*A_C(g)^\ell
 \le(1+o(1))KR_tA_C^\ell
 \left({C_L(j+\ell)^4\over m^2u_t^2}\right)^{\ell-1}.}          \tag{DLE}
\]

The power \(u_t^{-2}\) is a safe master normalization for multiplicity
energies; using the sharper witness-dependent power only improves the
bound.  This global DLE supplies every repeated-edge power in (3.1), so
there is no finite top boundary, and it implies BF.  A statement restricted
to \(j+\ell\le L\) would still need a separate overflow estimate and would
not by itself imply BF.

It is enough to prove an incidence-averaged version: owners for which DLE
fails may be quarantined provided

\[
                         \sum_{X\in\mathcal B_t}d_t(X)=o(E_t).   \tag{5.1}
\]

## 6. Conditional completion and the full constants

Assume BF, or global DLE, together with the exact
first-moment reference drift.  Put

\[
 \eta=m^{-1/10},\qquad J=C_0\log m,qquad
 L=C_1(\log m)^2.                                               \tag{6.1}
\]

The normalized predictable quadratic variation of every core owner
degree or core mesh martingale is at most

\[
 T{CL^4\over m^2z^2}
 =O(m^{-9/10}(\log m)^9).                                      \tag{6.2}
\]

Freedman's exponent is therefore

\[
 {\eta^2\over TCL^4/(m^2z^2)}
 \ge {c m^{7/10}\over(\log m)^9}.                              \tag{6.3}
\]

For the growing-order tail, choose a moment order
\(s=c_0\log m\).  The ratio entering weighted Markov is at most

\[
 \left(
  {C(\log m)^{O(1)}T\over m^2z^2\eta^2}
 \right)^s
 \le\exp[-c(\log m)^2].                                       \tag{6.4}
\]

The predictable reference drift also closes.  The multiplicity-\(s\)
owner-cluster reference has the form

\[
 D_Xx u^{r-1}\varepsilon_s(u)^s,
 \qquad \varepsilon_s(u)={Cs^4\over m^2u},                      \tag{6.5}
\]

and its logarithmic derivative agrees with the exact first generator
moment.  Pair-overcount and multiple-intersection errors have relative
size

\[
 O\!\left({L^6\over m^2z}+{1\over m^2z}\right).                 \tag{6.6}
\]

After multiplication by \(T/K=\Theta(\log m)\), (6.6) is
\(o(m^{-1/10})\).  Thus the cumulative predictable drift fits inside the
same tolerance \(\eta\).

Equations (6.3)--(6.4), averaged with owner-incidence weight, give bad
owner incidence at most

\[
 \beta_m rE_t,
 \qquad \beta_m\le\exp[-c(\log m)^2].                            \tag{6.7}
\]

Since \(r\beta_m=o(1)\), this is \(o(E_t)\).  Roots and internal-pair
energies obey the analogous calculation.  Weighted quarantine then
removes only \(o(E_t)\) options, and integration of

\[
                         {dx\over dt}=-(1+o(1)){x\over K}        \tag{6.8}
\]

to time \(T=(K/20)\log m\) gives

\[
                         x(T)=m^{-1/20}(1+o(1)).                 \tag{6.9}
\]

The exact owner ledger then yields an \(o(W)\) owner leave.

This proves the full weighted RPRN conclusion **conditional on BF/DLE**.

## 7. Independent audit of D's unconditional claim

The unconditional claim has three distinct layers.

1. **Static multiplicity mesh:** valid at the stated scale, and extendible
   from \(O(\log m)\) to \(O((\log m)^2)\) because the endpoint proof only
   uses \(s=o(m)\).

2. **Repeated-edge generator algebra:** repaired by the power energies
   (2.2).  The same selected edge is not being replaced by independent
   copies.

3. **Temporal truncation:** not proved.  The argument bounds a chain which
   advances by \(J\) levels from its starting order, but the stopped state
   includes energies already near its top recorded order.  Those energies
   can exit in one step.  No estimate for the resulting top-boundary flux
   is supplied.

Therefore D's Theorem 0.1 cannot currently be cited as unconditional.
The finite-density wasteful-bite note is correctly more cautious: it
states its trajectory conclusion conditionally on regenerated bridge
energies and cumulative degree control.

No actual stochastic counterexample is proved.  The audit identifies the
minimal theorem which distinguishes a valid completion from an invalid
finite-order truncation: BF, or equivalently the incidence-weighted DLE
hierarchy.

## 8. Infinite order: the compensated generator closes algebraically

There are two different infinite-norm questions.  They must not be
conflated.

* In the **compensated** hierarchy the exact first-order reference drift
  has already been removed.  Its positive upward remainder starts with a
  \(+2\) term.
* An absolute-value majorant which puts the first-order drift back has a
  \(+1\) term.  That stronger majorant has a genuine high-order
  obstruction.

The first model, not the second one, is the proposed alternative to the
finite buffer.  Let

\[
 w_s={\theta^s\over(s!)^a},\qquad
 \mathfrak F_{a,\theta}=\sum_{s=0}^r w_s\mathscr E_s,
 \qquad
 \kappa_s=\min\left\{1,{Cs^4\over m^2}\right\}.                \tag{8.1}
\]

Here \(\mathscr E_s\ge0\) is an order-\(s\) multiplicity energy after
division by its owner-link and free-edge normalizations.  The upper limit
is \(r\), since a physical repaired path has only \(r\) owner positions.
The moment power is itself exponentially normalized, so the binomial
coefficients from expanding \((A-B)^h\) are absorbed into an absolute
factor \(A^\ell\).  Without that power normalization, (8.2) would not be
the correct all-order generator inequality.

### Proposition 8.1 (boundary-free compensated shift)

Let \({\cal T}\ge1\) be the time horizon.  Suppose the positive upward
part of the compensated generator satisfies the all-order coefficient
inequality

\[
 (\mathcal G\mathscr E)_s^+
 \le \sum_{\ell=2}^{r-s}
 A^\ell\kappa_{s+\ell}^{\,\ell-1}\mathscr E_{s+\ell}             \tag{8.2}
\]

for an absolute \(A\).  Then the choice

\[
                         a=0,\qquad
                         \theta=2A\sqrt{\mathcal T}             \tag{8.3}
\]

absorbs every \(+2,+3,\ldots\) jump with no terminal order.  More
precisely, the time-integrated upward operator has norm at most \(1/2\)
on \(\mathfrak F_{0,\theta}\).

#### Proof

After putting \(t=s+\ell\), the coefficient of
\(w_t\mathscr E_t\) entering from an \(\ell\)-jump is

\[
 {\cal T}A^\ell\kappa_t^{\ell-1}{w_{t-\ell}\over w_t}.
                                                                    \tag{8.4}
\]

For (8.3), this is at most

\[
                  2^{-\ell}{\cal T}^{1-\ell/2}.                 \tag{8.5}
\]

The sum of (8.5) over \(\ell\ge2\) is at most
\(\sum_{\ell\ge2}2^{-\ell}=1/2\).  This proves the assertion.
\(\square\)

The exponent \(\ell-1\) in (8.2) is deliberately the weaker of the two
natural diagonal bounds.  If the exact generator supplies
\(\kappa^{\ell}\), the conclusion only improves.  Thus the algebra works
both for a checkpoint of length \(O(m)\), where
\(\theta=O(\sqrt m)\), and for the entire slow-greedy trajectory
\({\cal T}=\Theta(m\log m)\), where

\[
                         \theta=\Theta(\sqrt{m\log m})=\Theta(H).
                                                                    \tag{8.6}
\]

Positive factorial damping gives no advantage.  If \(a\ge0\), taking
\(\theta=2A\sqrt{\mathcal T}\,r^a\) also proves (8.4), since
\((t)_\ell\le r^\ell\).  But then

\[
 {\theta^s\over(s!)^a}
 =(2A\sqrt{\mathcal T})^s\left({r^s\over s!}\right)^a
 \ge(2A\sqrt{\mathcal T})^s.                                  \tag{8.7}
\]

It makes every initial coefficient at least as large as the coefficient
for \(a=0\).  The optimal member of the proposed inverse-factorial class
is therefore the plain geometric norm.

### 8.1 The exact initial-catalogue condition

Proposition 8.1 is an operator statement.  To use it one must still show
that the initial all-order physical catalogue has a small value in that
norm.  This condition has an exact, non-marginal form.  For pairwise
disjoint protected edges \(e_1,\ldots,e_j\) avoiding \(X\), put

\[
 z_i(f)=|f\cap e_i|.
\]

Directly from (0.1),

\[
\boxed{
 \sum_{c_1,\ldots,c_j\ge1}
 \theta^{c_1+\cdots+c_j}
 B_X^{\boldsymbol c}(e_1,\ldots,e_j)
 =\sum_{f\ni X}\prod_{i=1}^j
       \big((1+\theta)^{z_i(f)}-1\big).}                       \tag{8.8}
\]

This is the complete physical overlap transform.  If the aggregate
energy contains the additional exponential-composition factors
\(1/\prod_i c_i!\), its generating function is bounded above by the
right side of (8.8), so (8.8) is a safe common target.

For \(j=1\), the missing initialization estimate is already

\[
 {1\over D_X}\sum_{f\ni X}
       \big((1+\theta)^{|f\cap e|}-1\big)                       \tag{8.9}
\]

at \(\theta\asymp\sqrt{\mathcal T}\), together with its
incidence-weighted multi-edge versions (8.8).  Equations (2.1)--(2.2)
prove the required bound through
\(s\le L=\Theta((\log m)^2)\): indeed, for the full horizon,

\[
 \theta{CL^4\over m^2}
 =m^{-3/2+o(1)}.                                                \tag{8.10}
\]

They do not prove the tail \(L<s\le r\).  Nor does the audited
all-order codegree bound

\[
 {\Delta_{s+1}\over D_X}\le\left({CH\over m}\right)^s          \tag{8.11}
\]

do so.  Expanding (8.9) and bounding every prescribed witness set by
\(\Delta_{s+1}\) gives only

\[
 {\theta^s B_X^{(s)}(e)\over D_X}
 \le \theta^s\binom rs\left({CH\over m}\right)^s,              \tag{8.12}
\]

which is larger than one already in the mesoscopic range.  Formula
(8.12) is only an upper bound, so it is not a counterexample.  It proves
that static maximum codegrees are insufficient to initialize the
boundary-free norm.

To state the exact new static statement, let \(D\) be the root degree and
define the safely dominating first-moment transform

\[
 \mathcal I_\theta(X)
 :=\sum_{j=1}^r{1\over j!(KD)^jD_X}
 \sum_{(e_1,\ldots,e_j)}^*
 \sum_{f\ni X}\prod_{i=1}^j
       \big((1+\theta)^{|f\cap e_i|}-1\big).                    \tag{8.13}
\]

The star has the same disjointness and avoidance meaning as in (2.2).
The factorial composition weights in the actual aggregate only reduce
(8.13).  Repeated-edge powers require the positive exponential lift

\[
 \mathcal P_{\theta,\lambda}(X)
 :=\sum_{j=1}^r{1\over j!(KD)^j}
 \sum_{(e_1,\ldots,e_j)}^*
 \left[
  \exp\left({\lambda\over D_X}
    \sum_{f\ni X}\prod_{i=1}^j
       \big((1+\theta)^{|f\cap e_i|}-1\big)\right)-1
 \right].                                                       \tag{8.14}
\]

Indeed,
\(\partial_\lambda\mathcal P_{\theta,\lambda}(X)|_{\lambda=0}
=\mathcal I_\theta(X)\), and every coefficient of (8.14) is
nonnegative.  Thus (8.14) dominates all mixed powers generated from the
all-order multiplicity transform.  The exact new static statement which
would close initialization is:

\[
\boxed{
 {1\over rE_0}\sum_Xd_0(X)\mathcal P_{\theta,\lambda}(X)
 \le \exp(o(\Xi_m)),qquad
 \theta=2A\sqrt{\mathcal T},\qquad
 \Xi_m={m^{7/10}\over(\log m)^9},\quad
 0\le\lambda\le c\log m.}                                     \tag{IEGF}
\]

An \(O(1)\) bound is the natural reference prediction; the weaker IEGF
display is already sufficient for the Section 6 martingale budget.  The
present catalogue does not prove even its first derivative (8.13) in the
mesoscopic range.

### Lemma 8.2 (private-star mesh)

Fix a repaired catalogue edge \(f\), write \(O(f)\) for its \(r\) owner
vertices, and fix \(X\in O(f)\).  There are
\(s=r-1\) pairwise vertex-disjoint repaired edges

\[
                         e_Y\qquad(Y\in O(f)\setminus\{X\})
\tag{8.15}
\]

which avoid \(X\) and satisfy

\[
                         e_Y\cap f=\{Y\}.                       \tag{8.16}
\]

Consequently, for the all-one multiplicity vector
\(\boldsymbol 1=(1,\ldots,1)\),

 \[
 B_X^{\boldsymbol1}((e_Y)_{Y\in O(f)\setminus\{X\}})\ge1.       \tag{8.17}
\]

#### Proof

Order the owners of \(O(f)\setminus\{X\}\) as
\(Y_1,\ldots,Y_s\), and choose
the edges greedily.  Suppose \(e_1,\ldots,e_{i-1}\) have been chosen.
The number of options through \(Y_i\) meeting one of the earlier edges is
at most

\[
 \sum_{h<i}a_{Y_i}(e_h)
 \le {20+o(1)\over m^2}(i-1)D_X
 =O(D_X/m).                                         \tag{8.18}
\]

The number meeting \(f\setminus\{Y_i\}\) is at most the corresponding
internal owner-pair sum, hence is \(O(D_X/m)\); the common-root
contribution is superpolynomially smaller.  This restriction also
excludes \(X\).  Since the full link of \(Y_i\) has size \(D_X\), an
available edge \(e_i\) exists.  It is disjoint from every earlier
\(e_h\), avoids \(X\), and meets \(f\) exactly at \(Y_i\).

The link option \(f\) is counted once in the left side of (8.17), proving
the assertion. \(\square\)

This is a genuinely transverse high-total-order atom.  It does not use
the adjacent-deletion construction with a common root.  But it is **not**
an obstruction to Proposition 8.1.  With
\(n=r-1=(1+o(1))m\) and \(\theta=O(\sqrt{m\log m})\).  The exact
degree formula, with \(u=(k-H+1)_+\), gives

\[
 D_X=\rho {M!\over2u!},\qquad \log D_X=n\log m+O(m).             \tag{8.19}
\]

Thus its contribution to the pointwise catalogue energy normalized by
\(D_X\) is only

\[
 {\theta^n\over D_X}
=\exp\left[-\left({1\over2}+o(1)\right)m\log m\right].          \tag{8.20}
\]

The exact consecutive-path spine is harmless for the same reason.  Up to
order \(H\), its normalized term is
\(O(((m-s)!/m!)^2)\), so multiplication by \(\theta^s\), with
\(\theta=O(H)\), is already geometrically decreasing.  Above \(H\), put
\(q=m-s\).  If \(q+1\ge\theta\), then

\[
 \theta^s{(m-s)!(m-H)!\over(m!)^2}
 \le { (m-H)!\over m!}=m^{-H+o(H)}.                            \tag{8.21}
\]

If \(q+1<\theta\), then \(q!=\exp(o(m\log m))\) and direct Stirling
gives

\[
 \log\left(
 \theta^s{q!(m-H)!\over(m!)^2}
 \right)
 \le-\left({1\over2}+o(1)\right)m\log m.                       \tag{8.22}
\]

Thus the entire exact consecutive spine is harmless.  No known physical
high-order atom disproves IEGF.

### 8.2 What happens if a \(+1\) term survives

If compensation is not used, or absolute values restore an upward term
\(A\kappa_{s+1}\mathscr E_{s+1}\), absorption requires

\[
 {\cal T}A\kappa_{s+1}{w_s\over w_{s+1}}=O(1).                  \tag{8.23}
\]

Put \(s_*:=\min\{m,r-1\}=m-o(m)\).  At this order
\(\kappa_{s_*}=1\), so (8.23) forces, for every fixed real \(a\),

\[
                         \theta\ge c{\cal T}s_*^a.               \tag{8.24}
\]

The exact consecutive spine \(\Gamma_{s_*}\) satisfies, directly from
the two factorial formulas audited in Section 4,

\[
                         \log\Gamma_{s_*}
                         =-s_*\log m+O(m).                       \tag{8.25}
\]

Stirling and (8.24) therefore give

\[
\begin{aligned}
 \log\left({\theta^{s_*}\over(s_*!)^a}\Gamma_{s_*}\right)
 &\ge s_*\log({\cal T}/m)+O_a(m)\\
 &=(1+o(1))m\log\log m                                      \tag{8.26}
\end{aligned}
\]

on the full trajectory \({\cal T}=\Theta(m\log m)\).  This is the exact
consecutive-spine obstruction to an **uncompensated** scalar norm.  For
a single horizon \({\cal T}=O(m)\), the logarithmic excess in (8.26)
disappears, so this argument alone gives no statewise no-go.

### 8.3 The dynamic all-order gate

There is also an exact power-diagonal formulation.  If \(A_C\) is a
protected count, \(A_C(g)\) its decrement on selecting \(g\), and
\(P_C(y)\) its compensation-coin decrement at \(y\), then the positive
exponential majorant of the remainder after subtracting first-order drift
is

\[
\begin{aligned}
 \mathsf R^+_\vartheta(C)
 &=\nu_t\sum_g
 \left(e^{\vartheta A_C(g)/A_C}-1
             -\vartheta {A_C(g)\over A_C}\right)\\
 &\quad+
 \sum_y\chi_t(y)
 \left(e^{\vartheta P_C(y)/A_C}-1
             -\vartheta {P_C(y)\over A_C}\right).              \tag{8.27}
\end{aligned}
\]

Its Taylor series has nonnegative coefficients and starts at
\(\ell=2\).  It dominates the absolute Taylor remainder of the actual
decrement generator.  Proposition 8.1 sums that
series without a finite boundary **if** its coefficients satisfy (8.2).
The current static catalogue proves this only through order \(L\).  The
required all-order, incidence-weighted assertion is precisely the
following.  For every monitored cluster class \(\mathcal C_t\), with
its base-incidence weights \(w_C\),

\[
 \sum_{C\in\mathcal C_t}w_C\mathsf R^+_\vartheta(C)
 \le C\vartheta^2\varepsilon_*
       \sum_{C\in\mathcal C_t}w_C
 \qquad(0\le\vartheta\le c\log m),                            \tag{EMDLE}
\]

outside owner incidence \(o(E_t)\).  The clock rates \(\nu_t,\chi_t\)
are already present in (8.26), so EMDLE has the same per-time
normalization as DLE.  Taylor expansion of EMDLE displays every positive
diagonal moment; coefficientwise global DLE sums to EMDLE.

Hence the infinite-order proposal has a precise status.  It **does**
remove the artificial finite boundary at the level of the compensated
triangular operator.  It does **not yet** prove weighted RPRN, because
IEGF and its hereditary dynamic version EMDLE are unproved in the
mesoscopic range.  No initial private-star, consecutive-spine, or
high-order-diagonal counterexample to the compensated norm is presently
known.
