# Ordered-profile QRE and the exact weighted lifting gate

Date: 2026-07-26

Method: pure mathematics only. No computation, solver, or web input is
used.

## 0. Outcome

For the maximal independent-rank-matching graph, the raw all-cuts problem
inside one exact ordered half-rank profile can be solved by the
overlap-stratum method.

Fix a lower target profile

\[
 \tau=((a_j,c_j))_{j\le b},\qquad
 \sum_j(a_j+c_j)=m-q,
\]

and let \(\lambda=((\alpha_j,\gamma_j))_{j\le b}\) be an oriented
allocation, where

\[
 \alpha_j,\gamma_j\ge0,\qquad
 \sum_j(\alpha_j+\gamma_j)=q.                         \tag{0.1}
\]

It leads to the unique ordered source profile

\[
 \kappa(\lambda)=((a_j+\alpha_j,c_j+\gamma_j))_{j\le b}.
\]

For a target \(T\in\tau\), measure its four matching-status counts in
block \(j\) relative to the rank-\((a_j+c_j+\alpha_j+\gamma_j)\)
matching:

\[
 (f_j,p_j,s_j,e_j)
 =(\text{full},A\text{-only},C\text{-only},\text{empty}).
\]

Define the exact allocation score

\[
 R_\lambda^-(T)=
 \prod_j
 {\binom{e_j}{\alpha_j}
  \binom{e_j-\alpha_j}{\gamma_j}
  \over
  \binom{p_j+\alpha_j}{\alpha_j}
  \binom{s_j+\gamma_j}{\gamma_j}}.                    \tag{0.2}
\]

Then every raw family \({\cal A}\subseteq\tau\) satisfies

\[
 \boxed{
 |N^-({\cal A})|
 \ge\sum_{T\in{\cal A}}{\cal R}_\tau^-(T),
 \qquad
 {\cal R}_\tau^-(T):=\sum_\lambda R_\lambda^-(T).}    \tag{0.3}
\]

The sum is over all oriented allocations (0.1).  This is a literal
neighborhood theorem, not a degree or first-moment estimate.

There is an identical upper theorem.  If an upper target has statuses
\((f_j,p_j,s_j,e_j)\) relative to the source-rank matching and the source
removes \(\alpha_j\) \(A\)-endpoints and \(\gamma_j\) \(C\)-endpoints
from full edges, put

\[
 R_\lambda^+(U)=
 \prod_j
 {\binom{f_j}{\alpha_j}
  \binom{f_j-\alpha_j}{\gamma_j}
  \over
  \binom{s_j+\alpha_j}{\alpha_j}
  \binom{p_j+\gamma_j}{\gamma_j}}.                    \tag{0.4}
\]

Then

\[
 \boxed{
 |N^+({\cal A})|
 \ge\sum_{U\in{\cal A}}{\cal R}_\tau^+(U).}           \tag{0.5}
\]

For collision-free allocations, define the one-block scores

\[
\begin{aligned}
 r_j^-(T)
 &=e_j\left({1\over p_j+1}+{1\over s_j+1}\right),\\
 r_j^+(U)
 &=f_j\left({1\over s_j+1}+{1\over p_j+1}\right).
\end{aligned}                                         \tag{0.6}
\]

The full scores dominate the elementary symmetric polynomials

\[
 {\cal R}_\tau^\pm\ge e_q(r_1^\pm,\ldots,r_b^\pm).    \tag{0.7}
\]

On every safe central ordered profile, at least a constant fraction of
the blocks have mean one-block score at least \(4/3\), on the appropriate
sign.  Hypergeometric large deviation then shows that, after deleting an
\(\exp(-\Omega(m))\) fraction of the targets in the profile, at least
\(\rho b\) blocks have actual score at least \(7/6\), where
\(\rho>0\) is absolute.  Since \(q=A\sqrt m=o(b)\),

\[
 \boxed{
 {\cal R}_\tau^\pm(T)
 \ge\binom{\rho b}{q}(7/6)^q\longrightarrow\infty}    \tag{0.8}
\]

for every retained target.  Equations (0.3), (0.5) therefore prove:

> **Ordered-profile QRE.** Outside an \(\exp(-\Omega(m))\) quarantine
> in each safe exact ordered profile, every raw target subset has
> neighborhood at least \((1+\delta)|{\cal A}|\), for either sign and
> any fixed \(\delta>0\).

This closes the arbitrary-subset gate inside one ordered profile.

It does not by itself prove global QRE.  Source profiles reached from
different target profiles overlap.  The exact global lifting statement
is weighted.  If \(c_{\tau\kappa}\) is the amount of capacity of each
raw source in profile \(\kappa\) reserved for targets in profile \(\tau\),
define

\[
 {\cal R}_{\tau,c}^\pm(T)
 =\sum_\lambda
 c_{\tau,\kappa(\lambda)}R_\lambda^\pm(T).            \tag{0.9}
\]

If

\[
 \sum_\tau c_{\tau\kappa}\le1
 \quad(\kappa\text{ fixed}),                          \tag{0.10}
\]

and, outside an \(o(W)\) quarantine,

\[
                         {\cal R}_{\tau,c}^\pm(T)\ge1, \tag{0.11}
\]

then a fractional matching saturating every retained raw target exists;
bipartite integrality gives a raw injection.

Any ordered-profile refinement of the already proved quotient flow
supplies capacities satisfying (0.10) with constant average slack.  The
existence of a refinement with the required raw support, and the
pointwise weighted score bound (0.11), are not yet proved.  The
unweighted theorem (0.8) cannot replace (0.11), because a profile flow
may assign exponentially small capacity to each of exponentially many
allocations.

Thus the requested layer-cake argument proves ordered-profile QRE on both
signs and reduces full QRE to the explicit weighted score inequality
(0.11).  A claim that the coarse profile flow alone implies (0.11) would
reuse source capacity and is not valid.

## 1. Exact lower overlap components

Fix \(\tau\) and one oriented allocation \(\lambda\).  In block \(j\),
the target matching statuses are

\[
 (f_j,p_j,s_j,e_j).
\]

Completing \(\alpha_j\) empty edges with their \(A\)-endpoints and
\(\gamma_j\) further empty edges with their \(C\)-endpoints changes the
source statuses to

\[
 (f_j,\ p_j+\alpha_j,\ s_j+\gamma_j,\
  e_j-\alpha_j-\gamma_j).                            \tag{1.1}
\]

The target degree inside this exact status component is

\[
 d_{T,j}
 =\binom{e_j}{\alpha_j}
  \binom{e_j-\alpha_j}{\gamma_j}.                     \tag{1.2}
\]

The reverse source degree is

\[
 d_{X,j}
 =\binom{p_j+\alpha_j}{\alpha_j}
  \binom{s_j+\gamma_j}{\gamma_j}.                     \tag{1.3}
\]

Tensoring the blocks gives a biregular bipartite component with
source/target size ratio

\[
                         {d_T\over d_X}=R_\lambda^-(T).\tag{1.4}
\]

The value in (1.4) is constant on the complete vector of local status
strata for this allocation.

Let \({\cal A}_{\lambda,\mathbf f}\) be the part of a raw family
\({\cal A}\subseteq\tau\) in one such status vector.  Biregularity gives

\[
 |N_{\kappa(\lambda)}
       ({\cal A}_{\lambda,\mathbf f})|
 \ge R_\lambda^-(\mathbf f)
       |{\cal A}_{\lambda,\mathbf f}|.                \tag{1.5}
\]

Different status vectors have disjoint source status vectors.  Hence

\[
 |N_{\kappa(\lambda)}({\cal A})|
 \ge\sum_{T\in{\cal A}}R_\lambda^-(T).                \tag{1.6}
\]

Different oriented allocations \(\lambda\) give different ordered source
profiles \(\kappa(\lambda)\), so their source shores are disjoint.
Summing (1.6) over \(\lambda\) proves (0.3).

This disjointness is the decisive reason the layer-cake sum is legal
inside one exact target profile.

## 2. Exact upper overlap components

For the upper sign, start from an upper target status vector
\((f_j,p_j,s_j,e_j)\).  Remove the \(A\)-endpoint from
\(\alpha_j\) full edges and the \(C\)-endpoint from \(\gamma_j\) further
full edges.  The source statuses become

\[
 (f_j-\alpha_j-\gamma_j,\
  p_j+\gamma_j,\ s_j+\alpha_j,\ e_j).                 \tag{2.1}
\]

The target and reverse source degrees are

\[
\begin{aligned}
 d_{U,j}
 &=\binom{f_j}{\alpha_j}
   \binom{f_j-\alpha_j}{\gamma_j},\\
 d_{X,j}
 &=\binom{s_j+\alpha_j}{\alpha_j}
   \binom{p_j+\gamma_j}{\gamma_j}.
\end{aligned}                                         \tag{2.2}
\]

This proves (0.4).  The status vectors and ordered source profiles are
again disjoint, so the proof of (0.5) is identical to Section 1.

No relation such as
\(\pi_{j,k}=\pi_{j,2d-k}\) is needed.  Lower and upper use their own
source-rank matching and the same local biregularity argument.

## 3. Collision-free score reservoir

Restrict (0.3) to allocations with
\(\alpha_j+\gamma_j\in\{0,1\}\) in every block.  If block \(j\) is used,
summing its two possible endpoint sides gives exactly \(r_j^-\) in
(0.6).  Summing over all \(q\)-subsets of blocks gives

\[
 \sum_{\substack{\lambda\text{ collision-free}}}
 R_\lambda^-(T)
 =e_q(r_1^-(T),\ldots,r_b^-(T)).                      \tag{3.1}
\]

All other allocations have nonnegative ratios, proving the lower version
of (0.7).  The upper proof is identical.

Suppose \(g\) blocks satisfy \(r_j^\pm\ge c\).  The elementary symmetric
polynomial contains all \(q\)-subsets of these blocks, hence

\[
                         {\cal R}_\tau^\pm
 \ge\binom gq c^q.                                    \tag{3.2}
\]

This is a pointwise lower bound.  It does not average over targets or
over matching realizations.

## 4. Deterministic supply of favorable half-rank blocks

Write

\[
                         x_j={a_j\over d},\qquad
                         y_j={c_j\over d}.
\]

For a uniform target in the ordered profile, the full-edge count in the
relevant one-promotion matching is hypergeometric with mean

\[
                         \overline f_j=x_jy_jd.
\]

At this mean, the lower one-block score, ignoring \(O(d^{-1})\)
denominator corrections, is

\[
 \overline r_j^-
 ={1-x_j\over x_j}+{1-y_j\over y_j},                 \tag{4.1}
\]

whereas the upper score is

\[
 \overline r_j^+
 ={x_j\over1-x_j}+{y_j\over1-y_j}.                   \tag{4.2}
\]

For the lower target layer,

\[
 {1\over b}\sum_j(x_j+y_j)=1-o(1).
\]

At least \((1/6-o(1))b\) blocks satisfy

\[
                         x_j+y_j\le {6\over5}.         \tag{4.3}
\]

Indeed, if a fraction \(\theta\) satisfies (4.3), the smallest possible
average with all other blocks above \(6/5\) is
\((1-\theta)6/5\), so an average \(1-o(1)\) forces
\(\theta\ge1/6-o(1)\).

By the harmonic-mean inequality, (4.3) gives

\[
 {1\over x_j}+{1\over y_j}
 \ge {4\over x_j+y_j}\ge {10\over3},
\]

and therefore

\[
                         \overline r_j^-\ge {4\over3}. \tag{4.4}
\]

For the upper target layer the average of \(x_j+y_j\) is \(1+o(1)\).
At least \((1/6-o(1))b\) blocks satisfy

\[
                         x_j+y_j\ge {4\over5}.         \tag{4.5}
\]

Apply the preceding argument to
\((1-x_j,1-y_j)\).  Equation (4.5) gives

\[
                         \overline r_j^+\ge {4\over3}. \tag{4.6}
\]

On the safe half-rank core

\[
 \varepsilon\le x_j,y_j\le1-\varepsilon              \tag{4.7}
\]

for a fixed \(\varepsilon>0\).  The score is a smooth increasing function
of the hypergeometric full-edge count.  A drop from \(4/3+O(d^{-1})\)
to \(7/6\) requires a downward deviation \(\Omega_\varepsilon(d)\).
The elementary hypergeometric Chernoff bound therefore gives

\[
 \Pr\{r_j^\pm<7/6\}\le e^{-c_\varepsilon d}           \tag{4.8}
\]

on every favorable block.

Blocks outside (4.7) can be separated into the existing macro/half-rank
quarantine.  Alternatively their one-sided score can be bounded directly;
the fixed safe core is sufficient for the present theorem.

## 5. Exact quarantine count

Fix an exact ordered profile \(\tau\) in the safe core.  The raw target
choices in different macroblocks are independent under the uniform
measure on \(\tau\).  For a fixed realized perfect matching, the
hypergeometric count and bound (4.8) are exact; randomness of the atlas
only permutes the local target states.

Let \(J_\tau^\pm\) be the favorable block set from Section 4, with

\[
                         |J_\tau^\pm|\ge(1/6-o(1))b.
\]

The number of blocks in \(J_\tau^\pm\) whose actual score is below
\(7/6\) is stochastically bounded by

\[
                         \operatorname {Bin}
 (|J_\tau^\pm|,e^{-c_\varepsilon d}).                 \tag{5.1}
\]

The probability that fewer than

\[
                         \rho b,\qquad \rho=1/13,
\]

blocks remain good is

\[
                         \exp[-\Omega_\varepsilon(bd)]
 =\exp[-\Omega_\varepsilon(m)].                       \tag{5.2}
\]

Delete these exceptional targets from \(\tau\).  For every retained
target, (3.2) with \(g=\rho b\), \(c=7/6\) proves (0.8).  Substitution
in (0.3) or (0.5) proves ordered-profile QRE for every raw subset of the
retained profile.

This quarantine is much smaller than the
\(\exp[-\Omega(\sqrt m\log m)]\) one obtained by counting only locally
Hall-deficient blocks.  The stronger estimate is available because the
full allocation union may choose any \(q\) of a linear reservoir of good
blocks.

## 6. Weighted layer-cake lifting

The global source shore is shared by different target profiles.  To state
the exact lifting condition, reserve a uniform capacity

\[
                         c_{\tau\kappa}\ge0
\]

on every raw source in ordered profile \(\kappa\) for targets from
profile \(\tau\).  The source capacity condition is (0.10).

For an allocation \(\lambda\) from \(\tau\) to \(\kappa(\lambda)\),
multiply the biregular inequality (1.6) or its upper analogue by
\(c_{\tau,\kappa(\lambda)}\).  Because capacities are uniform within the
source profile, the same edge double count gives, for every
\({\cal A}\subseteq\tau\),

\[
 \operatorname {cap}
 N^\pm({\cal A})
 \ge
 \sum_{T\in{\cal A}}{\cal R}_{\tau,c}^\pm(T).         \tag{6.1}
\]

If (0.11) holds, the capacitated Hall inequality follows for every raw
subset of \(\tau\).  Max-flow gives a fractional matching from the
retained targets in \(\tau\) into their reserved source capacities.

Summing these fractional matchings over \(\tau\) is legal by (0.10).
It saturates every retained target and uses every raw source by at most
one.  Bipartite integrality then produces a raw injection.

This proves the weighted lifting theorem (0.9)--(0.11).

## 7. Why the existing profile flow is not yet enough

Let \(F_{\tau\kappa}\) be a profile-flow mass and put

\[
 c_{\tau\kappa}={F_{\tau\kappa}\over|\kappa|}.
\]

Then (0.10) is exactly the owner-capacity constraint of the quotient
flow.  There is one eligibility correction in averaging the weighted
score.  For an arc \((\tau,\kappa)\), let

\[
 E_{\tau\kappa}
 =\sum_{T\in\tau}R_{\tau\kappa}^\pm(T)\le |\kappa|.
\]

This is the number of source states in \(\kappa\) having enough correctly
oriented singleton edges to reverse the allocation.  Thus the exact
identity is

\[
 {1\over|\tau|}
 \sum_{T\in\tau}{\cal R}_{\tau,c}^\pm(T)
 ={1\over|\tau|}\sum_\kappa
       F_{\tau\kappa}{E_{\tau\kappa}\over|\kappa|}.   \tag{7.1}
\]

On the safe at-most-two-promotion arcs used by the quotient flow,
\(E_{\tau\kappa}=(1-o(1))|\kappa|\) uniformly, because failure in one
touched block has probability \(e^{-\Omega(d)}\) and there are at most
\(q\) touched blocks.  Hence (7.1) is \(1-o(1)\), not exactly one.

If the quotient flow uses only the fraction
\(\rho_A=e^{-A^2}+o(1)\) of each owner profile, one may scale all
capacities by \(\rho_A^{-1}\), preserving (0.10), and make the average
weighted score

\[
                         e^{A^2}+o(1)>1.              \tag{7.2}
\]

But an average lower bound does not imply the pointwise bound (0.11).
The fixed-allocation overlap cuts show that allocation scores can have
large lower tails.  The unweighted reservoir estimate (0.8) says only
that many alternative source profiles are available; it does not say
that the quotient flow reserves appreciable capacity on those profiles.

What remains is therefore the following precise statement.

### Weighted allocation-score theorem

Choose the slack profile flow so that, for both signs,

\[
 \sum_\lambda
 c_{\tau,\kappa(\lambda)}R_\lambda^\pm(T)
 \ge1                                                   \tag{7.3}
\]

for every target outside an \(o(W)\) quarantine.

By Section 6, (7.3) is equivalent to the desired raw fractional matching
after the profile capacities have been fixed.  It is stronger than the
proved profile flow and weaker than a product cut-norm theorem.  It
preserves coordinate cylinders and all other one-sided inclusion
structure.

## 8. Exact asymptotics at Gaussian depth

For \(d=\Theta(\log m)\), \(b=m/d+O(1)\), and
\(q=A\sqrt m+O(1)\),

\[
 {q\over b}=O(d/\sqrt m)=o(1).                        \tag{8.1}
\]

The collision-free reservoir in (0.8) has logarithm

\[
\begin{aligned}
 \log\left[\binom{\rho b}q(7/6)^q\right]
 &=q\log{\rho b\over q}+q\log(7/6)+O(q+q^2/b)\\
 &=\left({1\over2}+o(1)\right)A\sqrt m\log m.         \tag{8.2}
\end{aligned}
\]

Thus ordered-profile expansion is

\[
 \exp\left[\left({A\over2}+o(1)\right)
                 \sqrt m\log m\right],               \tag{8.3}
\]

far larger than the constant expansion required by QRE.

The per-profile quarantine in (5.2) is
\(\exp[-\Omega(m)]|\tau|\).  Summing it over all exact ordered profiles
preserves an \(\exp[-\Omega(m)]N_q=o(W)\) global quarantine, because the
profiles partition the target layer.  The same estimates hold for the
upper sign.

The only remaining loss is therefore not within-profile raw expansion.
It is the weighted source-capacity allocation (7.3).

## 9. Certified boundary

Proved:

1. exact all-cuts inequalities (0.3) and (0.5);
2. ordered-profile QRE after an exponentially small quarantine;
3. both lower and upper signs at \(q=A\sqrt m\);
4. the Gaussian expansion exponent (8.3); and
5. the exact weighted lifting theorem (0.9)--(0.11).

Not proved:

1. the weighted allocation-score theorem (7.3) for the existing profile
   flow;
2. global QRE across all ordered profiles;
3. a raw injection; or
4. selected-axis and chronological grouping.

The overlap-stratum method therefore solves the arbitrary-subset problem
inside every ordered profile.  Full QRE is now equivalent to choosing the
profile-flow capacities so that their weighted allocation score has no
nonquarantined lower tail.
