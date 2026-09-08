# Spread top naming: a pointwise codegree certificate and a random-partition theorem

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional sufficient named-start theorem and unconditional
probabilistic existence of spread **top** names under an explicit
vanishing socket reserve.  The insured one-depth shift can afford that
reserve at every capacity.  This rules out every Hall obstruction,
including compressed stars, on the top-to-collar interface.  It does not
yet prove that the spread top partition extends to one target-once
interval-chain naming.

## 0. Setup

Work in `B_n`, initially with `n=2r`.  Fix a collar rank `u<=n/2`.  Put

\[
 \mathcal B_j=\binom{[n]}j,
 \qquad C_j=|\mathcal B_j|,
 \qquad H_u=C_u-C_{u-1},
\tag{0.1}
\]

and

\[
 \alpha_u={H_u\over C_u}
 ={n-2u+1\over n-u+1}.
\tag{0.2}
\]

Let `mathcal R_u` be occurrence-labelled residual requests assigned to
rank-`u` collar starts.  Request `F` has a named top `S_F` of rank `s_F<u`.
Its number of possible containing starts is

\[
                         d(F)=\binom{n-s_F}{u-s_F}.
\tag{0.3}
\]

For `T in mathcal B_u`, define the normalized top codegree

\[
 \lambda_u(T)=
 \sum_{F\in\mathcal R_u:,S_F\subset T}{1\over d(F)}.
\tag{0.4}
\]

The average of `lambda_u` over `mathcal B_u` is

\[
 {1\over C_u}\sum_T\lambda_u(T)
 ={ |\mathcal R_u|\over C_u}.
\tag{0.5}
\]

The pointwise distribution, not only this average, controls the named
start gate.

## 1. Exact pointwise codegree certificate

### Theorem 1.1 (spread tops imply an exact collar matching)

If

\[
 \boxed{
                         \lambda_u(T)\le\alpha_u
                         \qquad(T\in\mathcal B_u),}
\tag{1.1}
\]

then the augmented inclusion graph has a matching which simultaneously

1. matches every rank-`u-1` set to a distinct containing rank-`u` set; and
2. matches every request `F in mathcal R_u` to a distinct containing
   rank-`u` start.

Equivalently, the request candidate sets have a Rado transversal
independent in the dual Boolean collar-start matroid `mathsf K_u`.

#### Proof

Every continuation vertex `A in mathcal B_(u-1)` sends mass uniformly to
its `n-u+1` containing rank-`u` sets.  Thus it sends total mass one.  A
fixed `T in mathcal B_u` receives continuation mass

\[
 {u\over n-u+1}={C_{u-1}\over C_u}=1-\alpha_u.
\tag{1.2}
\]

Every request `F` sends mass `1/d(F)` to each rank-`u` superset of `S_F`.
It too sends total mass one, and `T` receives request mass exactly
`lambda_u(T)`.  Under (1.1), the total right load is at most one.

This is a fractional matching saturating the entire augmented left shore.
The bipartite matching polytope is integral, so an integral saturating
matching exists.  Deleting the continuation image leaves the request
images as legal collar starts, proving the dual-matroid formulation.
`square`

### Classwise form

If the requests are split into configuration classes `mathcal R_(a,u)` of
common top rank `s_a`, put

\[
 q_{a,u}(T)=
 |\{F\in\mathcal R_{a,u}:S_F\subset T\}|,
 \qquad
 d_{a,u}=\binom{n-s_a}{u-s_a}.
\tag{1.3}
\]

Then (1.1) is exactly

\[
 \boxed{
                         \sum_a{q_{a,u}(T)\over d_{a,u}}
                         \le {H_u\over C_u}
                         \qquad(T\in\mathcal B_u).}
\tag{1.4}
\]

A convenient sufficient budget is

\[
 {q_{a,u}(T)\over d_{a,u}}
 \le {m_{a,u}\over C_u}+\eta_{a,u}
 \quad\text{for all }T,
 \qquad
 \sum_a\eta_{a,u}\le{H_u-m_u\over C_u},
\tag{1.5}
\]

where `m_(a,u)=|mathcal R_(a,u)|` and `m_u=sum_a m_(a,u)`.

The compressed two-star counterexample violates (1.4): all of its request
mass is trapped in one rank-`u` coordinate star.  Theorem 1.1 shows that
(1.4) rules out not only star cuts but every augmented Hall cut.

## 2. Random top partitions are spread when every socket rank has slack

Now specialize to the one-depth setting

\[
 n=2r,
 \qquad D=\Theta(\sqrt r),
 \qquad b=r-D-1.
\tag{2.1}
\]

All positive requests have top rank at most `b-1` and use start ranks

\[
                         b+1\le u\le r.
\tag{2.2}
\]

For each pair `(s,u)`, let `m_(s,u)` be a nonnegative integer, interpreted
as the number of distinct rank-`s` top slots assigned to start rank `u`.
Assume

\[
 \sum_u m_{s,u}\le C_s
 \quad(s\le b-1),
\tag{2.3}
\]

and, for one fixed `epsilon>0`,

\[
 m_u:=\sum_{s\le b-1}m_{s,u}
 \le(1-\epsilon)H_u
 \quad(b+1\le u\le r).
\tag{2.4}
\]

### Theorem 2.1 (slackful spread-top partition)

For every fixed `epsilon>0` and all sufficiently large `r`, the complete
rank layers can be partitioned into disjoint families

\[
                         Q_{s,u}\subseteq\mathcal B_s,
 \qquad |Q_{s,u}|=m_{s,u},
\tag{2.5}
\]

such that, simultaneously for every start rank `u` and every
`T in mathcal B_u`,

\[
 \sum_{s\le b-1}
 { |Q_{s,u}\cap\binom Ts|
  \over \binom{2r-s}{u-s}}
 \le {H_u\over C_u}.
\tag{2.6}
\]

Consequently these top slots have an exact named collar matching at every
rank `u`.

#### Proof

Independently for each rank `s`, choose a uniformly random labelled
partition of `mathcal B_s` into bins of sizes `m_(s,u)` and one unused bin.
For fixed `s,u`, the marginal `Q_(s,u)` is a uniform `m_(s,u)`-subset of
`mathcal B_s`.

Fix `u` and `T in mathcal B_u`.  Write

\[
 X_s=|Q_{s,u}\cap\binom Ts|,
 \qquad
 d_{s,u}=\binom{2r-s}{u-s},
 \qquad
 L(T)=\sum_s{X_s\over d_{s,u}}.
\tag{2.7}
\]

The hypergeometric mean and the flag-counting identity give

\[
 \begin{aligned}
 \mathbb E X_s
 &=m_{s,u}{\binom us\over C_s},\\
 {\binom us\over C_s\binom{2r-s}{u-s}}
 &={1\over C_u}.
 \end{aligned}
\tag{2.8}
\]

Therefore

\[
                         \mu:=\mathbb E L(T)={m_u\over C_u}
                         \le(1-\epsilon)\alpha_u.
\tag{2.9}
\]

Sampling without replacement is negatively associated, and the partitions
at different ranks are independent.  The usual weighted Bernstein bound
therefore applies.  With

\[
 d_{\min}(u)=
 \min_{s\le b-1}d_{s,u}
 =\binom{2r-b+1}{u-b+1},
\tag{2.10}
\]

every summand has weight at most `1/d_min(u)` and total variance at most
`mu/d_min(u)`.  Since `alpha_u-mu>=epsilon alpha_u`, Bernstein gives an
absolute `c>0` such that

\[
 \Pr\{L(T)>\alpha_u\}
 \le
 \exp\{-c\epsilon^2\alpha_u d_{\min}(u)\}.
\tag{2.11}
\]

Put `N=r+D+2` and write `u=b+g`, where `1<=g<=D+1`.  Then

\[
 d_{\min}(u)=\binom N{g+1},
 \qquad
 \alpha_u={2D+3-2g\over N-g}.
\tag{2.12}
\]

For `g=1`,

\[
 \alpha_ud_{\min}(u)={(2D+1)N\over2}.
\tag{2.13}
\]

For `g>=2`, eventually `g+1<=N/2`, and hence

\[
 \alpha_ud_{\min}(u)
 \ge {1\over N}\binom N3
 ={(N-1)(N-2)\over6}.
\tag{2.14}
\]

Thus uniformly in `u`,

\[
                         \alpha_ud_{\min}(u)=\Omega(rD)
                         =\Omega(r^{3/2}).
\tag{2.15}
\]

There are at most `(D+1)W=exp(O(r))` pairs `(u,T)`.  The union bound in
(2.11), using (2.15), is strictly below one for all sufficiently large
`r`.  Therefore a deterministic partition satisfying every inequality
(2.6) exists.  Apply Theorem 1.1 independently at each tagged collar rank.
`square`

### Theorem 2.2 (vanishing-slack spread criterion)

Put

\[
                         \Delta_u=H_u-m_u.
\tag{2.16}
\]

There is an absolute constant `A_0` such that the conclusion of Theorem
2.1 still holds whenever every `Delta_u>0` and

\[
 \boxed{
 {\Delta_u^2d_{\min}(u)\over C_uH_u}\ge A_0r
 \qquad(b+1\le u\le r).}
\tag{2.17}
\]

#### Proof

For fixed `(u,T)`, the gap between the pointwise capacity and the mean is

\[
                         \tau_u={\Delta_u\over C_u}.
\tag{2.18}
\]

The variance bound in Theorem 2.1 is at most

\[
 {\mu\over d_{\min}(u)}
 \le {H_u\over C_ud_{\min}(u)},
\]

and every summand is at most `1/d_min(u)`.  Weighted Bernstein now gives

\[
 \Pr\{L(T)>\alpha_u\}
 \le
 \exp\left\{-c
 {\Delta_u^2d_{\min}(u)\over C_uH_u}\right\}
\tag{2.19}
\]

for an absolute `c>0`; here `tau_u<=alpha_u` absorbs the linear Bernstein
term into the same denominator.  Choose `A_0` larger than the exponential
growth constant of `(D+1)W`, divided by `c`, and take the union bound.
`square`

Thus fixed relative slack is far stronger than necessary.  The sufficient
absolute reserve is only

\[
 \Delta_u\ge
 \sqrt{A_0rC_uH_u/d_{\min}(u)}.
\tag{2.20}
\]

## 2A. The one-depth shift can afford the vanishing reserve

The socket-insurance theorem supplies more than the fewer-than-`r`
exceptional occurrences used by the named small-bank theorem.  Its entire
new interval-piece multiset can be reassigned while leaving the reserve
(2.20) empty at every capacity.

Keep the old notation

\[
 t=r-D,
 \qquad b=t-1=r-D-1,
 \qquad
 h=D\left\lceil{t-2\over D+1}\right\rceil.
\tag{2A.1}
\]

For `1<=g<=D+1`, put

\[
 u_g=b+g,
 \qquad
 d_g=\binom{r+D+2}{g+1},
\tag{2A.2}
\]

and choose

\[
 \Delta_g=\left\lceil
 A\sqrt{\,rC_{u_g}H_{u_g}/d_g\,}
 \right\rceil,
\tag{2A.3}
\]

where `A` is any fixed constant with `A^2>=A_0`.

### Theorem 2.3 (tail-faithful empty-socket reserve)

Assume the old depth-`D` configuration LP is feasible and the hypotheses
of the vanishing-singleton insurance theorem hold.  For all sufficiently
large `r`, its new depth-`D+1` interval-piece multiset can be injected into
the genuine collar occurrences while leaving at least `Delta_g` unused
occurrences of every capacity `g`.

Consequently its abstract chunk-top slots admit a disjoint literal top
partition satisfying the pointwise spread inequalities (2.6) at every
collar rank.

#### Proof

Let

\[
 K_q=W-C_{t+q-1}
 \quad(1\le q\le D),
 \qquad
 K_q^+=W-C_{b+q-1}
 \quad(1\le q\le D+1)
\tag{2A.4}
\]

be the old and new socket tails.  Let `A_q^+` count new pieces of length at
least `q` in the insured construction.  Let `p<=h` be the actual number of
exceptional pieces, let `E_q` be their length-at-least-`q` tail, and put

\[
                         B_q=A_q^+-E_q
\tag{2A.4a}
\]

for the transported bulk tail.

The insurance operation replaces a piece of length `ell` by `ell`
singletons.  It can increase only the `q=1` piece count.  Its crude total
increase is at most

\[
 R_{\rm ins}=hD+{D(D+1)\over2}.
\tag{2A.5}
\]

Terminal deletion never increases a piece tail.  Before the exceptional
pieces are reinserted, the transported bulk therefore satisfies

\[
 \begin{aligned}
 B_1&\le K_1+R_{\rm ins},\\
 B_q&\le K_q &&(2\le q\le D),\\
 B_{D+1}&=0.
 \end{aligned}
\tag{2A.6}
\]

The adjacent-depth identities are

\[
 \begin{aligned}
 K_1^+-K_1&=H_t,\\
 K_q^+-K_q&=H_{t+q-1} &&(2\le q\le D),\\
 K_{D+1}^+&=H_r.
 \end{aligned}
\tag{2A.7}

Assign the `p` exceptional pieces first to their `p` insured old-maximum,
new-capacity-`D+1` occurrences.  Removing those occurrences leaves the bulk
capacity tail `K_q^+-p` at every `q`.  Hence the available bulk tail margins
in (2A.6) are respectively

\[
 H_t-R_{\rm ins}-p,
 \qquad
 H_{t+q-1}-p,
 \qquad
 H_r-p.
\tag{2A.8}

We next check the cost of (2A.3).  Uniformly for `u_g` in the collar,
`C_(u_g)=Theta(W)` and `H_(u_g)>=cW/r` for an absolute `c>0`; at the first
rank, more sharply,

\[
                         H_t=\Theta(WD/r)=\Theta(W/\sqrt r).
\tag{2A.9}

Since `rH_(u_g)/C_(u_g)<=2D+3`, equation (2A.3) gives

\[
                         \Delta_g
 =O\left(W\sqrt{D/d_g}\right)+1.
\tag{2A.10}

At `g=1`, this is

\[
                         \Delta_1=O(W\sqrt D/r)=o(H_t).
\tag{2A.11}

For `g>=2`, the ratio

\[
 {d_{g+1}\over d_g}={r+D+1-g\over g+2}
\tag{2A.12}

is `Omega(sqrt(r))` throughout the collar.  Thus every reserve tail is
dominated by its first term, and for `q>=2`,

\[
 \sum_{g=q}^{D+1}\Delta_g
 =O\left(W\sqrt{D/d_q}\right)+O(D)
 =O\left(W{\sqrt D\over r^{3/2}}\right)+O(D)
 =o(W/r)
 =o(H_{b+q}).
\tag{2A.13}

Together with (2A.11),

\[
                         \sum_{g=q}^{D+1}\Delta_g
                         =o(H_{b+q})
                         \qquad(1\le q\le D+1).
\tag{2A.14}

The polynomial quantities `R_ins` and `p<=h` are also `o(H_(b+q))`
uniformly.  Comparing (2A.14) with (2A.8), for every `q`,

\[
 B_q
 \le K_q^+-p-\sum_{g=q}^{D+1}\Delta_g.
\tag{2A.15}

The sorted-tail matching criterion now injects every transported bulk
piece into the capacity multiset after deleting the `p` insured maximum
occurrences and `Delta_g` further capacity-`g` occurrences.  Restore the
exceptional pieces on their insured occurrences.

Let `m_(s,u)` count the resulting abstract piece slots by top rank and
assigned collar rank.  Distinct pieces at rank `s` use at most the retained
rank-`s` inventory `n_s<=C_s`, while (2A.15) gives

\[
                         m_{u_g}\le H_{u_g}-\Delta_g.
\tag{2A.16}

Equations (2A.2)--(2A.3) verify (2.17).  Theorem 2.2 therefore supplies a
disjoint spread literal top partition and Theorem 1.1 supplies the exact
top-to-collar matching.  `square`

Theorem 2.3 removes the saturated-partial-class arithmetic obstruction:
one does not need a fixed relative reserve or an exact orbit design.  The
required empty bank is `O(W/r^(3/4))` in total, while the depth shift creates
much larger tail margins.  It still does not solve the downward
target-once interval-chain extension.

## 3. Orbit-core hybrid

The same proof allows an exactly balanced deterministic core.  Suppose at
rank `u` a collection of complete-orbit request batches contributes the
constant pointwise load

\[
                         \beta_u={B_u\over C_u}
\tag{3.1}
\]

under the uniform edge weighting of the joint-start orbit theorem.  If the
remaining partial top slots satisfy

\[
 m_u^{\rm rem}\le
 (1-\epsilon)(H_u-B_u)
\tag{3.2}
\]

and `H_u-B_u` is a fixed positive proportion of `H_u`, Theorem 2.1 applies
with residual capacity `(H_u-B_u)/C_u`.  Adding the orbit-core and random
residual fractional matchings gives total right load at most one, and one
integral matching rounds them simultaneously.

Thus saturation is harmless when it is carried by an exact symmetric
orbit core.  What remains outside the theorem is a saturated **partial**
class with no exact balancing identity.

## 4. Exact remaining bridge

Theorem 2.1 chooses distinct literal **tops** for every abstract chunk slot.
It does not assert that these prescribed tops can be extended downward to
pairwise target-disjoint inclusion chains realizing the entire interval
histogram.  The interval Boolean lift proves existence when the top sets
are co-chosen by its upward matchings; it is not presently
extension-surjective onto an arbitrary prescribed spread top partition.

Accordingly, a sufficient final bulk theorem is now:

> **Spread extension theorem.**  Choose the interval-histogram Boolean lift
> from a distribution, or by a deterministic balanced construction, whose
> induced top partition satisfies (2.6) at every socket rank.

The insured one-depth shift supplies enough vanishing per-rank slack for
the probabilistic part of that statement once such a random top-partition
marginal is available.  The surviving correlation is precisely between
those spread top names and the lower target-once chain matching.  Arbitrary
fixed naming is false by the compressed two-star theorem; scalar capacity,
zero-slack arithmetic, and all top-to-collar Hall cuts are no longer
additional obstructions.
