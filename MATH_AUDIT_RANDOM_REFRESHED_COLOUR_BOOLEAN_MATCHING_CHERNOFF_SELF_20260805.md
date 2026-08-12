# Self-audit: randomly refreshed Boolean colours

**Date:** 2026-08-05  
**Audited theorem:**
`MATH_THEOREM_RANDOM_REFRESHED_COLOUR_BOOLEAN_MATCHING_CHERNOFF_20260805.md`  
**Method:** pure mathematical replay; no computation, search, or solver  
**Verdict:** GO after four corrections: the occupancy exponent is `1/20`
rather than `1/18`, one display delimiter was restored, the simultaneous
and refresh statements were made quantifier-exact, and the independently
refreshed dummy shore was added so the theorem covers the complete colour
contribution claimed in its status.

## 1. Strong-Rayleigh dependency

The dependency theorem applies to exactly the law used here:

* `M` is uniform over all perfect matchings of `J_q`;
* its old image set `I` has generating polynomial proportional to the top
  homogeneous part of the restricted Heilmann--Lieb polynomial;
* hence `I` is Strong Rayleigh;
* coordinate symmetry gives

\[
 \Pr(T\in I)={m\over N}
 ={q+1\over n-q}.
\]

Therefore, for `R_U=binom(U,q+1)`,

\[
 \mathbb E|I\cap R_U|
 ={m\over N}\binom v{q+1}=\mu_U,
\]

and negative association supplies the usual Bernoulli upper and lower
tails.  No edge-coordinate Strong-Rayleigh statement is being imported.

The complement `R\setminus I` is Strong Rayleigh by homogeneous duality.
Its owner count has exact mean

\[
 \nu_U={N-m\over N}\binom v{q+1}.
\]

This supplies the dummy-occupancy Bernstein bound at its own mean, which
can be much smaller than `mu_U` near the middle layer.

## 2. Conditional hypergeometric law

Condition on the complete matching `M`.  Its old restriction is a
bijection `L -> I`, so

\[
 P_U=M^{-1}(I\cap R_U)
\]

is a fixed `Y_U`-subset of the `m` old vertices.  In a uniformly random
labelled partition with prescribed class sizes, the marginal class `A_j`
is a uniform `m_j`-subset of `L`.  Thus

\[
 X_{j,U}=|A_j\cap P_U|
\]

is hypergeometric with mean

\[
 {m_jY_U\over m}=p_jY_U.
\]

Joint independence among different colour classes is neither true nor
used; the final simultaneous result uses only a union bound.

Unconditionally,

\[
 \mathbb E X_{j,U}=p_j\mu_U
 ={m_j\over N}\binom v{q+1},
\]

so every displayed mean is exact.

The dummy matching is a bijection from the `h=N-m` labelled dummies to
`R\setminus I`.  An independent uniform dummy class `B_j` of size `h_j`
therefore gives, conditional on `M`, a hypergeometric count with mean

\[
 s_j(K_U-Y_U),
 \qquad s_j={h_j\over h},
 \qquad K_U=\binom v{q+1}.
\]

The old and dummy counts are conditionally independent because their two
partitions were sampled independently.  Their complete colour sum has
conditional mean

\[
 \theta_Y=p_jY_U+s_j(K_U-Y_U).
\]

## 3. Occupancy constant

Let `t=delta mu/3`.  The Strong-Rayleigh Bernoulli Bernstein bounds give

\[
 \Pr(Y_U-\mu\ge t)
 \le
 \exp\left(-{t^2\over2(\mu+t/3)}\right)
 \le e^{-\delta^2\mu/20}
\]

for `delta<=1`, because `2(mu+t/3)<=20mu/9`.  The lower tail is at most
`e^{-delta^2 mu/18}`.  Thus the corrected two-sided exponent `1/20` is
valid.  The original `1/18` did not follow for the upper tail.

Weakening by `p_j<=1` gives the corresponding exponent in
`delta^2 p_j mu`.

## 4. Hypergeometric constant

On the good event,

\[
 Y_U\le {4\mu\over3},
 \qquad
 \nu:=pY_U\le {4p\mu\over3},
 \qquad
 t:={2\delta p\mu\over3}.
\]

Sampling without replacement has the Bernoulli Bernstein upper tail and a
stronger lower tail.  Hence

\[
 \Pr(|X-\nu|\ge t\mid M)
 \le2\exp\left(-{t^2\over2(\nu+t/3)}\right).
\]

For `delta<=1`,

\[
 2(\nu+t/3)
 \le {28p\mu\over9},
 \qquad
 t^2={4\delta^2p^2\mu^2\over9},
\]

so the exponent is actually at least `delta^2 p mu/7`.  The theorem's
weaker `1/24` is therefore safe.  Combining it with the corrected occupancy
bound proves

\[
 \Pr(|X-p\mu|\ge\delta p\mu)
 \le4e^{-\delta^2p\mu/24}.
\]

## 5. Edge cases

* If `m_j=0`, then `p_j=0`, `X_(j,U)=mu_(j,U)=0`; the event is empty.
* If `m_j=m`, the conditional hypergeometric fluctuation is zero and only
  the already valid occupancy tail remains.
* Since `q<r` and `n=2r`, one has `h=N-m>0`.  Since `v>=q+1`, both
  `mu_U>0` and `nu_U>0`; no division by a zero occupancy mean occurs.
* Dummy classes of size zero or `h` cause no problem, for the same reason
  as old classes of size zero or `m`.
* For the complete statistic, `theta=0` forces `p=s=0`, so the variable is
  identically zero.  When `p=s`, its conditional mean is exactly constant
  and the occupancy stage is unnecessary.
* Means below one merely make the displayed bound possibly larger than
  one; the inequality remains true.
* Dependence among tests and among colour classes is irrelevant to the
  union bound.

## 6. Complete old-plus-dummy constant replay

Write

\[
 \theta=p\mu+s\nu,
 \qquad \rho=\min(\mu,\nu),
 \qquad d=|p-s|.
\]

The conditional mean is

\[
 \theta_Y=\theta+(p-s)(Y_U-\mu).
\]

The theorem uses only the following elementary inequality:

\[
                         \theta\ge d^2\rho.
\]

Indeed, if `p>=s`, then `d^2<=p` and
`theta>=p mu>=d^2 rho`; the other case follows by swapping the shores.
The old image and its complement are both Strong Rayleigh.  For either
sign of `Y_U-mu`, use the stronger of the old-shore and complementary-shore
Bernstein bounds.  This gives the common variance proxy `rho`.

At

\[
                         t={\delta\theta\over3d}
\]

when `d>0`, if `t<=3rho` the Bernstein exponent is at least

\[
 {t^2\over4\rho}\ge {\delta^2\theta\over36};
\]

if `t>3rho`, it is at least

\[
 {3t\over4}={\delta\theta\over4d}
             \ge {\delta^2\theta\over4}.
\]

Thus the conditional mean differs from `theta` by at most
`delta theta/3` except with probability
`2 exp(-delta^2 theta/36)`.  On that event it is at most `4theta/3`.
Conditioned on `M`, the old and dummy hypergeometric indicator families
are independent and negatively associated.  Their union is negatively
associated, so Bernstein at threshold `2delta theta/3` has exponent at
least

\[
 {4\delta^2\theta^2/9\over
  2(4\theta/3+2\delta\theta/9)}
 \ge {\delta^2\theta\over7}.
\]

Combining the stages proves the advertised complete-colour constant
`1/36`.  This also audits the cases `p=0`, `s=0`, and `p=s`; no division by
`d` is made in the last case.

## 7. Simultaneous constants

For a nonempty family of at most `e^(Cr)` tests, Theorem 3.1 gives total
failure probability at most

\[
 4\exp\left(Cr-{1\over24}\min_{(j,U)}
                 \delta_{j,U}^2\mu_{j,U}\right).
\]

The corrected hypothesis

\[
 \delta_{j,U}^2\mu_{j,U}\ge48(Cr+\log4)
\]

makes this strictly below one for every `C,r>=0`.  The empty-family case
is trivial.  This avoids the former informal appeal to finitely many small
dimensions.

For complete old-plus-dummy tests, the corresponding sufficient condition
is

\[
 \delta_{j,U}^2\theta_{j,U}\ge72(Cr+\log4),
\]

because the audited exponent is `1/36`.

## 8. Remaining refresh gate

The one-interface theorem is unconditional.  Its multi-interface use is
conditional on a much stronger object than arbitrary relabelling:

1. conditional on the protected past, the complete future-role labels on
   both the old and labelled-dummy shores must be exactly uniformly
   partitionable with the required fixed counts;
2. those two partitions must be mutually independent, and the next uniform
   `J_q` matching must be physically legal and independent of both;
3. all past literal targets, residence prefixes, boundaries, sockets, and
   compiler tickets must remain unchanged;
4. every transferred future role must remain legal; and
5. the same refresh capability must regenerate after the step.

The revised theorem states all five requirements.  It does not infer this
serial kernel from abstract role symmetry, marginal counts, or the
Strong-Rayleigh image law.  Type-restricted or eligibility-restricted
refreshment is outside its conclusion unless it gives the two exact uniform
conditional partitions required by Lemmas 2.1--2.2.

Under that explicit lemma, applying the one-step theorem conditionally at
each level and union-bounding all tests is valid.  The resulting statement
is the spread top-to-chain lift already scoped by the coloured Boolean
flow theorem, not a complete universal OR word and not an unconditional
`B(k)+O(1)` result.

## 9. Final status

The audited theorem closes the one-interface probabilistic matching row,
including the complete old-plus-dummy colour sum, under mutually
independent uniform refreshes.  It does not construct those refreshes in a
persistent physical chronology.  The precise remaining theorem is
physical, serial, and typed: construct the two-shore uniform refresh kernel
while preserving and regenerating every protected role constraint.
