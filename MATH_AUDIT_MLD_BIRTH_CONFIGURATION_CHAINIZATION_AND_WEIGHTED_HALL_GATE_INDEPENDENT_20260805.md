# Independent audit: MLD birth configurations and weighted Hall sum

**Date:** 2026-08-05  
**Audited theorem:**
`MATH_THEOREM_MLD_BIRTH_CONFIGURATION_CHAINIZATION_AND_WEIGHTED_HALL_GATE_20260805.md`  
**Method:** independent proof replay; no computation, search, or solver  
**Verdict:** **GO**.  The generalized-Hölder step gives the requested
multi-rank Bernstein bound without independence and without a
`sqrt(D)` loss.  The theorem remains conditional on fractional
configuration feasibility, positive socket reserve, and physical exposure
of the exceptional bank, exactly as stated.

## 1. Chain-cover and birth-refinement quantifiers

Independent perfect matchings of the augmented interfaces concatenate to
an uncoloured target-once path cover: every nonempty Boolean target occurs
at one rank and on one path.  All paths born at rank `b` end at the common
cutoff `t`, so they have the same length `t-b+1`.  Hence their complete
fragmentation menu depends only on information known at birth, not on
later realised path geometry.

Uniform fixed-count assignment of configurations inside a newborn cohort
is therefore an allowed MLD refinement.  Transport through each later
independent uniform interface preserves the complete `(b,p)` label.  The
cohort-stable MLD theorem applies inductively.  The merge at rank one is
legitimate because both the nonempty continuation of the empty-set path
and rank-one newborn paths have the same residual nonempty length; MLD is
closed under merging labels.

Cutting the already disjoint paths cannot duplicate or omit an ordinary
target.  A marked top family `Q_(s,v)` is determined solely by the carried
configuration label and is thus a union of MLD cells at rank `s`.  Its
fixed size makes

\[
 p_{s,v}={|Q_{s,v}|\over\binom ks}
\]

the exact one-point marginal.

## 2. One-rank Laplace input

For fixed `T in binom([k],v)`, MLD gives

\[
 E e^{\tau X_s}
 \le(1-p_{s,v}+p_{s,v}e^\tau)^{\binom vs}
 \le\exp\{\mu_s(e^\tau-1)\},                    \tag{2.1}
\]

where

\[
 X_s=|Q_{s,v}\cap\tbinom Ts|,
 \qquad
 \mu_s=p_{s,v}\binom vs.
\]

This verifies hypothesis (5.5) of the audited theorem.  No joint
independence of the variables `(X_s)` is asserted or needed.

## 3. Generalized-Hölder replay

Let `a_s>0`, `A=sum_s a_s`, and `gamma_s=a_s/A`.  Then

\[
\begin{aligned}
 E e^{\lambda\sum_sa_sX_s}
 &\le\prod_s
      (E e^{\lambda A X_s})^{\gamma_s}\\
 &\le\exp\left{(e^{\lambda A}-1)
                  \sum_s\gamma_s\mu_s\right}\\
 &=\exp\left\{{\mu\over A}(e^{\lambda A}-1)\right\},
\end{aligned}                                    \tag{3.1}
\]

because

\[
 \sum_s\gamma_s\mu_s
 ={1\over A}\sum_sa_s\mu_s={\mu\over A}.
\]

After centering, this is exactly

\[
 E e^{\lambda(Z-\mu)}
 \le\exp\left\{{\mu\over A}
       (e^{\lambda A}-1-\lambda A)\right\}.     \tag{3.2}
\]

The standard Bennett-to-Bernstein estimate yields

\[
 P(Z-\mu\ge g)
 \le e^{-g^2/[2(A\mu+Ag/3)]}.
\]

Thus the dependence across ranks has been paid only through
`A=sum_s a_s`; there is no Cauchy--Schwarz or union-bound factor in the
number of ranks.

## 4. Flag mean and geometric weight sum

For

\[
 a_s={1\over\binom{k-s}{v-s}},
\]

the exact flag identity is

\[
 \binom ks\binom{k-s}{v-s}
 =\binom kv\binom vs.
\]

Therefore

\[
 a_s\mu_s
 ={1\over\binom{k-s}{v-s}}
  {|Q_{s,v}|\over\binom ks}\binom vs
 ={|Q_{s,v}|\over\binom kv},                    \tag{4.1}
\]

and summing proves

\[
 \mu={m_v\over\binom kv}.
\]

Successive weights obey

\[
 {a_{s-1}\over a_s}
 ={v-s+1\over k-s+1}.                            \tag{4.2}
\]

When `s<=t<v<=ceil(k/2)`, the right side is at most `2/3`
(the smallest boundary case is equality).  Since the largest allowed
weight is

\[
 a_t={1\over d_v},
 \qquad d_v=\binom{k-t}{v-t},
\]

the geometric series gives

\[
 A\le {3\over d_v}.                              \tag{4.3}
\]

This is the exact no-`sqrt(D)` mechanism.

## 5. Constant in the Hall tail

Put `C=binom(k,v)`, `m=m_v`, `Delta=H_v-m`, so

\[
 \mu={m\over C},\qquad g={\Delta\over C}.
\]

Using `A<=3/d_v` and `m+Delta/3<=H_v`,

\[
 2(A\mu+Ag/3)
 \le {6H_v\over d_vC}.
\]

Hence the direct replay actually gives exponent at least

\[
 {\Delta^2d_v\over6CH_v}.
\]

The theorem's weaker denominator eight is safe.  There are at most
`2^k` owner sets, times only polynomially many ranks, so condition (5.12)
with a sufficiently large absolute constant makes the union bound pass.

The pointwise load threshold is exactly the hypothesis of the existing
fractional-matching collar theorem; bipartite integrality then supplies all
ordinary collar starts simultaneously.

## 6. Configuration rounding scope

In a basic solution of the job-specific configuration LP, the number of
positive variables exceeds the number of job equalities by at most the
number `D` of socket-tail constraints.  Every job with more than one
positive configuration accounts for at least one such excess.  Hence at
most `D` jobs are fractional.  Dropping them cannot increase any socket
usage.  Since jobs of one birth length are interchangeable, the retained
integer configuration counts can be assigned by the uniform cohort
refinement used above.

This proves exact ordinary target-once fragmentation and leaves at most
`D` exceptional whole paths.  It does not itself expose the physical
maximum-capacity socket bank needed for those paths.

## 7. Scope exclusions

The audited result closes:

* persistent/newborn colour concentration;
* target-once naming of ordinary lower chains;
* the complete weighted multi-rank pointwise Hall sum;
* cross-rank dependence, without a `sqrt(D)` reserve loss.

It does not prove:

* the all-price fractional configuration inequalities;
* a positive reserve `Delta_v` in every required collar rank;
* occurrence-faithful exposure of the exceptional socket bank;
* central carrier chronology, residence, or arbitrary-width upper
  coverage.

## 8. Dependency binding

At audit time:

* `MATH_THEOREM_BOOLEAN_COHORT_STABLE_MULTINOMIAL_LAPLACE_INDUCTION_20260805.md`
  had SHA-256
  `3e35ec57354bdfc694defc2f30fee0af7f3aadcb2485ae2cdf8629044e94912f`;
* `MATH_THEOREM_FRAGMENTATION_FERRERS_SEMIGROUP_BASIC_ROUNDING_AND_ABSORBER_20260805.md`
  had SHA-256
  `0fcb8221ddb3efaef06e7e88337119cdcc86a8307669491c06ccf2559258bdc9`;
* `MATH_THEOREM_SPREAD_TOP_NAMING_POINTWISE_CODEGREE_AND_RANDOM_PARTITION_20260805.md`
  had SHA-256
  `c8bc0aced4916641217e47bc27cbd7edc207d7706fa4284e2ab9b3864a24e7a6`.
