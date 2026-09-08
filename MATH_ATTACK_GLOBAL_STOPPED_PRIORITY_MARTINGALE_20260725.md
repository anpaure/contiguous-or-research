# Global stopped compensated degree martingale

Date: 2026-07-25

Method: pure mathematics only.

## 0. Outcome

The per-bite requirement

\[
 \sum_t\eta_t=o(1)
\]

is unnecessary.  For the sequential exact-priority nibble, one global
stopped martingale controls all degree fluctuations.  If the total
weighted predictable quadratic variation is

\[
 \mathcal V_m\le B_mW,
 \qquad B_m=o(1),
\]

then, with the single tolerance

\[
 \eta_m=B_m^{1/4},
\]

fibres of total accounting weight \(o(W)\) may be discarded and every
remaining fibre follows its compensator to multiplicative error
\(1+o(1)\) throughout the whole process.

For the strengthened raw triangle scale

\[
 m^{-1+o(1)}
\]

per anchor, summing all \(Q=m^{1/2+o(1)}\) protected strata and the
effective nibble time gives

\[
 B_m=m^{-1/2+o(1)}.
\]

Then \(\eta_m=m^{-1/8+o(1)}\), martingale-exceptional weight is
\(m^{-1/4+o(1)}W\), and logarithmic-remainder-exceptional weight is
\(m^{-3/8+o(1)}W\).

This closes the **tolerance summation** exactly.  It does not, by itself,
deduce the weighted predictable variation bound from the raw triangle.
The factorial priority weights normalize perfectly as a deletion of
fixed priority decorations, but their later-time distribution may still
concentrate.  Thus the same outer-slice weighted four-walk term remains
the input needed for \(\mathcal V_m\le B_mW\).

---

## 1. Exact priority loss is an ordinary fractional deletion

Expand each base grid \(P\) into all of its fixed priority decorations.
At sequential time \(s\), let

\[
 a_s(P)=\#\{\text{fixed priority decorations of }P
                 \text{ still feasible at time }s\}.
\]

The factorial formula for \(a_s(P)\) is exact, but no factorial weight
larger than one is being assigned to a decoration: \(a_s(P)\) is an
integer count of surviving decorations.  In particular,

\[
 0\le a_{s+1}(P)\le a_s(P).
\]

For any tag or protected-target fibre \(F\), put

\[
 D_s(F)=\sum_{P\in F}a_s(P).
\]

If the accepted chunk at step \(s\) is \(E_s\), define

\[
 h_s(P,E_s)=1-\frac{a_{s+1}(P)}{a_s(P)}\in[0,1]
\]

when \(a_s(P)>0\), with the evident zero convention otherwise.  Owner
collision, target collision, exact deadline reprioritization, and dynamic
quarantine are all included.  Then the exact fractional fibre loss is

\[
 \boxed{
 I_{s,F}
 :=\frac{D_s(F)-D_{s+1}(F)}{D_s(F)}
 =\sum_{P\in F}p_{s,F}(P)h_s(P,E_s),}
 \tag{1.1}
\]

where

\[
 p_{s,F}(P)=a_s(P)/D_s(F).
\]

There is a required lifetime convention.  Let \(\lambda_F\) be the first
step whose accepted decorated edge directly contains the resource vertex
\(F\) (or processes the tag \(F\)).  Track the degree process only for
\(s<\lambda_F\), and omit the terminal jump \(D(F)\to0\).  Direct
consumption means that the target/tag has been successfully handled; it
is not a degree fluctuation.  If these terminal jumps were included, their
squared losses would sum to \(\Theta(KT)=\Theta(W\sqrt m)\).

Consequently

\[
 \boxed{
 \mathbb E[I_{s,F}^2\mid\mathcal F_s]
 =J_s(F),}
 \tag{1.2}
\]

with \(J_s(F)\) the exact weighted common-link square from the priority
bow-tie identity.  There is no missing factorial normalization in
(1.1)--(1.2).

---

## 2. One global stopped theorem

With every fibre stopped strictly before its direct-consumption lifetime,
let

\[
 \bar I_{s,F}=\mathbb E[I_{s,F}\mid\mathcal F_s],
 \qquad
 M_{t,F}=\sum_{s<t}(I_{s,F}-\bar I_{s,F}),
 \tag{2.1}
\]

and

\[
 Q_{t,F}=\sum_{s<t}mathbb E[I_{s,F}^2\mid\mathcal F_s],
 \qquad
 S_{t,F}=\sum_{s<t}I_{s,F}^2.
 \tag{2.2}
\]

Fix the accounting weights \(\operatorname{wt}(F)\), equal to \(g\) on
tag fibres and one on target fibres.  Assume the whole process satisfies

\[
 \boxed{
 \sum_F\operatorname{wt}(F)\,
 \mathbb E Q_{T,F}\le B_mW.}
 \tag{2.3}
\]

### Theorem 2.1 (global stopped degree control)

For any \(0<\eta<1/4\), outside fibres of expected total weight at most

\[
 \boxed{
 4B_mW/\eta^2+B_mW/\eta,}
 \tag{2.4}
\]

one has, simultaneously for every \(t\le T\),

\[
 |M_{t,F}|\le\eta,
 \qquad
 S_{t,F}\le\eta,
 \tag{2.5}
\]

and hence

\[
 \boxed{
 \log\frac{D_t(F)}{D_0(F)}
 =-\sum_{s<t}\bar I_{s,F}+O(\eta).}
 \tag{2.6}
\]

#### Proof

For each fixed \(F\), \(M_{t,F}\) is a martingale and

\[
 \mathbb E M_{T,F}^2
 \le\mathbb E Q_{T,F}.
\]

Doob's \(L^2\) maximal inequality gives

\[
 \Pr\{\max_{t\le T}|M_{t,F}|>\eta\}
 \le4\mathbb EQ_{T,F}/\eta^2.
\]

Also

\[
 \mathbb ES_{T,F}=\mathbb EQ_{T,F},
\]

so Markov gives

\[
 \Pr\{S_{T,F}>\eta\}
 \le\mathbb EQ_{T,F}/\eta.
\]

Multiply by \(\operatorname{wt}(F)\), sum, and use (2.3), proving
(2.4)--(2.5).

On a fibre satisfying (2.5), every \(I_{s,F}\le\sqrt\eta<1/2\).
Therefore

\[
 \log(1-I_{s,F})=-I_{s,F}+O(I_{s,F}^2).
\]

Summing and using

\[
 \sum_{s<t}I_{s,F}
 =\sum_{s<t}\bar I_{s,F}+M_{t,F}
\]

proves (2.6).  \(\square\)

Choose \(\eta=B_m^{1/4}\).  The two terms in (2.4) become

\[
 4B_m^{1/2}W,
 \qquad B_m^{3/4}W,
\]

both \(o(W)\).  Thus a single global tolerance replaces every
per-bite tolerance and there is no requirement to sum tolerances through
the \(R\) bites.

---

## 3. Common mean drift is the only other degree input

Let

\[
 A_{t,F}=\sum_{s<t}\bar I_{s,F}.
\]

If, outside fibres of weighted \(o(W)\), there are stratum reference
compensators \(A_{t,r}\) such that

\[
 \sup_{t\le T}|A_{t,F}-A_{t,r(F)}|=o(1),
 \tag{3.1}
\]

then Theorem 2.1 gives

\[
 \boxed{
 D_t(F)=D_0(F)e^{-A_{t,r(F)}}(1+o(1))}
 \tag{3.2}
\]

uniformly through the whole process.  Affine hash-colour stratification
is one mechanism which makes the degree-one part of (3.1) exact; the
remaining part is a scalar outer-slice mean-dispersal statement.

---

## 4. The numerical coefficient-one ledger

Suppose the strengthened triangle/common-link theorem supplies, after
all protected ranks and effective time are summed,

\[
 \sum_F\operatorname{wt}(F)\,
 \mathbb EQ_{T,F}
 \le m^{-1/2+o(1)}W.
 \tag{4.1}
\]

This is the natural scale: the raw anchored triangle is
\(m^{-1+o(1)}\), there are \(Q=m^{1/2+o(1)}\) protected rank strata,
and logarithmic effective time is absorbed by \(m^{o(1)}\).  Thus

\[
 B_m=m^{-1/2+o(1)},
 \qquad
 \eta=B_m^{1/4}=m^{-1/8+o(1)}.
\]

Equation (2.4) gives exceptional weights

\[
 m^{-1/4+o(1)}W
 \quad\text{and}\quad
 m^{-3/8+o(1)}W.
 \tag{4.2}
\]

Both are coefficient-safe.  This is strictly stronger and cleaner than
choosing \(R\) separate tolerances whose sum must tend to zero.

---

## 5. Can the pair-square aggregate itself be stopped?

Yes, but only **after** its total predictable budget is bounded.
For any \(v>0\), stop protecting fibre \(F\) when

\[
 Q_{t,F}>v.
\]

Equation (2.3) then charges all such fibres by

\[
 \boxed{B_mW/v.}
 \tag{5.1}
\]

This is useful because no pointwise hereditary pair-square theorem is
needed: an aggregate weighted bound on \(\sum_F\operatorname{wt}(F)Q_{T,F}\)
is enough.

However, stopping is not a proof of that aggregate bound.  The raw
triangle controls (1.2) only under the raw uniform catalogue measure.
At later times

\[
 p_{s,F}(P)=a_s(P)/D_s(F)
\]

may concentrate on outer schedule slices whose physical target-pair
labels collide.  In exact form the missing input is

\[
 \boxed{
 \sum_F\operatorname{wt}(F)
 \mathbb E\sum_sJ_s(F)\le B_mW.}
 \tag{5.2}
\]

This is precisely (2.3), by (1.2).  Doob stopping cannot manufacture
(5.2): using (5.1) without first knowing (5.2) is circular.

The dense-down-set theorem removes the within-switch-cube part of this
problem.  After replacing each dense feasible down-set by its scalar
slice density \(\rho_\omega\), the unproved contribution to (5.2) is the
outer scalar-slice weighted four-walk.  Thus the current exact division
of labour is:

1. global stopped martingale: proved here;
2. factorial priority normalization: exact by (1.1)--(1.2);
3. per-bite tolerance summation: eliminated;
4. aggregate outer-slice pair-square budget (5.2): still unproved;
5. common compensator drift (3.1): still unproved beyond the closed
   hash-colour mode.

No coefficient-one conclusion is claimed without (5.2) and (3.1).

---

## 6. Audit of the tempting codegree-monotonicity bootstrap

Expanding every priority as a fixed decorated edge is valid.  The current
catalogue is a literal subhypergraph of the raw decorated catalogue, so

\[
 d_t(x,y)\le d_0(x,y).
 \tag{6.1}
\]

However, this does **not** make the desired \(z^{-2}\) hereditary
pair-square bound automatic.  The reason is a density distinction.

In the pair-square statement, \(z\ge1/\log m\) is the density of unused
tags/resources.  A fixed decorated chunk contains

\[
 K=\Theta(g\sqrt m)=m^{1+o(1)}
\]

protected resources.  Even in an ideal independent model, the survival
density of a fixed decorated edge is on the scale

\[
 \rho_t\asymp z^K,
 \tag{6.2}
\]

not on the scale \(z\).  Priority adaptation leaves an exponentially
large absolute catalogue, but it does not turn the fraction of surviving
fixed priority decorations into \(z\).

Degree stopping can therefore guarantee only a bound of the form

\[
 d_t(x)\ge(1-\eta)\rho_td_0(x).
 \tag{6.3}
\]

Combining (6.1) and (6.3) gives the true monotonicity estimate

\[
 K_t(x,y)le((1-\eta)\rho_t)^{-1}K_0(x,y),
 \tag{6.4}
\]

whose square/triangle inflation is \(\rho_t^{-2}\) or
\(\rho_t^{-3}\).  This is astronomically larger than the required
\(z^{-2}\) scale and is useless for the coefficient-one ledger.

The nontrivial content of the hereditary pair-square theorem is exactly
that pair-codegree numerators shrink in concert with the very small
decorated-edge degrees, leaving only the resource-density inflation
\(z^{-2}\).  Raw numerator monotonicity discards that cancellation.

Thus the binary expansion proves the exact normalization (1.1)--(1.2),
but it does not close (5.2).  The global stopped martingale removes the
roundwise tolerance loss **conditional on** (5.2); it cannot derive
(5.2) from (6.1).
