# The repeated-child profile diagonal has exact coefficient \(O(1/r)\)

Date: 2026-07-27

> **AUDIT CORRECTION.** Equation (0.4) below is an exact raw,
> hereditary reverse-sum identity.  The claims (0.5)--(0.6) are **not proved
> in the natural child-profile normalization**.  Passing from the parent
> denominator to the child denominator inserts
> \((\mu_{S\cup a}/\mu_S)^2\), potentially as large as \(u^{-2}\) for a
> rare fibre.  A valid cutoff still needs an incidence-averaged weighting or
> the centered variance norm.  Read (0.5)--(0.6) only as the favorable value
> conditional on that normalization compatibility.

## 0. Theorem

Let \({\cal H}_t\) be any current vertex-induced \(r\)-uniform residual,
let

\[
 \Delta_t=\max_x d_t(x),
 \qquad
 \nu_t=\frac1{r\Delta_t},
\tag{0.1}
\]

and let the compensation deletion clock of every physical resource satisfy

\[
 \chi_t(a)\le\frac1r.
\tag{0.2}
\]

Fix an active physical profile \(S\).  Put

\[
 A_a=d_t(S\cup\{a\}).
\tag{0.3}
\]

The repeated-child diagonal in the selected-edge and compensation
carr\'e-du-champ satisfies

\[
\boxed{
 \nu_t\sum_{g\in{\cal H}_t}\sum_{a\in g}A_a^2
 +\sum_a\chi_t(a)A_a^2
 \le \frac2r\sum_aA_a^2.}
\tag{0.4}
\]

Consequently, in the equality-resolved compensated profile generator, the
physical \(+1\) repeated-child coefficient obeys

\[
\boxed{\delta_{k+1}\le 2/r=O(1/m)}
\tag{0.5}
\]

at every profile order.  The assertion is pathwise and hereditary: it holds
in every induced residual and requires no codegree hypothesis.

For the finite cutoff

\[
 {cal T}=\Theta(m\log m),qquad
 \theta=\Theta(\sqrt{m\log m}),
\]

its integrated weighted coefficient is

\[
\boxed{
 \frac{{\cal T}}\theta\max_k\delta_k
 =O\!\left(\sqrt{\frac{\log m}{m}}\right)=o(1).}
\tag{0.6}
\]

Thus the repeated-child orbit which invalidates the literal \(+2\)-only
generator does not obstruct the compensated \((\log m)^2\) cutoff.

## 1. Proof

Reverse the selected-edge sum:

\[
\begin{aligned}
 \nu_t\sum_g\sum_{a\in g}A_a^2
 &=\nu_t\sum_a d_t(a)A_a^2\\
 &\le\frac1{r\Delta_t}\sum_a\Delta_tA_a^2\\
 &=\frac1r\sum_aA_a^2.
\end{aligned}
\tag{1.1}
\]

The compensation part follows directly from (0.2):

\[
 \sum_a\chi_t(a)A_a^2\le\frac1r\sum_aA_a^2.
\tag{1.2}
\]

Adding (1.1) and (1.2) proves (0.4).

In a square or exponential Taylor generator, the term \(A_a^2\) is the
physical diagonal in which two algebraic witnesses are the same resource
\(a\).  It raises physical profile order by one, so (0.4) is exactly the
coefficient \(\delta_{k+1}\) in the corrected generator
(CG'\(_J\)).  This proves (0.5).

Finally,

\[
 \frac{{\cal T}}\theta\frac2r
 =O\!\left(
 {m\log m\over\sqrt{m\log m}}{1\over m}
 \right)
 =O\!\left(\sqrt{\frac{\log m}{m}}\right),
\]

which proves (0.6).

## 2. Higher repeated powers

For a positive exponential Taylor remainder, a single physical child may be
repeated \(\ell\ge3\) times.  Before the profile/jump stop, write \(b_*) for
the maximum normalized one-child decrement.  Then

\[
 A_a^\ell\le (b_*A)^{\ell-2}A_a^2
\tag{2.1}
\]

after restoring the observable normalization \(A\).  Hence all repeated
powers are dominated by (0.4) times the convergent Taylor series in \(b_*\).
In the polylogarithmic cutoff range the existing child-profile stop gives
\(b_*=m^{-1+o(1)}u^{-1}=o(1)\) down to the stated square-root density.
They therefore change (0.5) only by a factor \(1+o(1)\).

Mixed patterns with at least two **distinct** new resources are not part of
the repeated-child diagonal.  They remain the distinct-child
\(\ell\ge2\) census in the compensated cutoff theorem.

## 3. Remaining boundary

The finite compensated cutoff now has no unbounded \(+1\) coefficient.  Its
only unresolved generator input is the equality-resolved distinct-child
bound through total order \(J=(\log m)^2\), together with a direct aggregate
terminal type count.  The post-collar consecutive spine and the compensation
coin diagonal are both discharged by (0.4).
