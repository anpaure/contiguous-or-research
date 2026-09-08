# Self-audit: cohort-stable Boolean multinomial Laplace induction

**Date:** 2026-08-05  
**Audited theorem:**
`MATH_THEOREM_BOOLEAN_COHORT_STABLE_MULTINOMIAL_LAPLACE_INDUCTION_20260805.md`  
**Method:** independent algebraic replay and quantifier audit; no search or
solver  
**Verdict:** **GO** for unconditioned independent uniform Boolean
interfaces and position-independent fixed transition counts.  The theorem
does not license geometry-adaptive role refinements or protected matching
conditioning.

## 1. MLD normalization and means

For `B=empty`, both sides of MLD are one.  For a union `J` of labels,
specializing all labels in `J` to `theta` and all other labels to zero
gives

\[
 E e^{\theta X}\le(1-p+pe^\theta)^{|B|}.
\]

Taking right and left derivatives at `theta=0` (the inequality holds on
both sides of zero and is equality at zero) gives

\[
 EX=p|B|.
\]

Thus the benchmark called exact in the theorem really is the expectation,
not merely an upper comparison.

## 2. Refinement closure

Conditional on a cohort `C_i`, the colours seen on the fixed set
`B cap C_i` are a sample without replacement from the multiset containing
`n_(ij)` copies of `e^(theta_j)`.  Maclaurin gives

\[
 E e^{\sum_j\theta_j|C_(ij)\cap B|}
 \le\left(\sum_j{n_(ij)\over m_i}e^{\theta_j}
       \right)^{|B\cap C_i|}.
\]

The quantity in parentheses is strictly positive, so its logarithm is a
legal real MLD parameter.  Multiplying over conditionally independent
cohorts and invoking input MLD gives exactly

\[
 \left(\sum_j{\sum_i n_(ij)\over m}e^{\theta_j}
 \right)^{|B|}.
\]

Zero transition cells cause no problem.  A zero-size whole row should be
deleted before writing `n_(ij)/m_i`; this harmless convention is implicit.

The proof requires the matrix of counts not to be selected from realised
cohort positions.  The theorem was corrected to state this explicitly.

## 3. Strong-Rayleigh all-real transform

For fixed `B`, the Strong-Rayleigh old-image probability generating
polynomial specialized to one variable is real rooted with nonpositive
zeros and nonnegative coefficients.  After padding with zero Bernoulli
parameters if necessary it factors as

\[
 E z^Y=\prod_{j=1}^{|B|}(1-\rho_j+\rho_jz).
\]

Uniform old-image marginals give `sum rho_j=lambda|B|`.  For every real
`tau`, `a=e^tau-1` lies in `(-1,infinity)`, and

\[
 x\mapsto\log(1+ax)
\]

is concave on `[0,1]`.  Jensen therefore proves

\[
 E e^{\tau Y}\le(1-\lambda+\lambda e^\tau)^{|B|}
\]

for both signs of `tau`.  The negative-parameter case needed by a newborn
weight larger than all persistent weights is therefore valid.

## 4. Boolean transport identity

Conditional on the matching,

\[
 P_B=M^{-1}(I\cap B),\qquad |P_B|=Y,
\]

and the newborn count is exactly `|B|-Y`.  Input MLD on the deterministic
set `P_B` gives a factor `a^Y`, where

\[
 a=\sum_i p_i e^{\theta_i}.
\]

Multiplication by the newborn weight and use of the all-real transform
gives

\[
 e^{\theta_0|B|}
 (\delta+\lambda a e^{-\theta_0})^{|B|}
 =\left(\delta e^{\theta_0}
       +\sum_i\lambda p_i e^{\theta_i}\right)^{|B|}.
\]

The new proportions sum to

\[
 \delta+\lambda\sum_i p_i=1,
\]

and agree with the literal deterministic cohort sizes.  This is exact;
there is no discarded covariance or accumulated error.

Independence of the input partition from the current matching is essential
when conditioning on `M`.  Sampling each new interface independently in
the serial construction supplies it.  An arbitrary protected conditioning
does not.

## 5. Serial induction and cohort count

The initial one-class partition is MLD with equality.  Refinement closure
and Boolean transport closure alternate, so ordinary induction proves MLD
at every rank.  Neither proof contains the number of labels except inside
a convex combination whose coefficients sum to one.  Hence retaining
`O(sqrt(r))` newborn cohorts, or even more state-history labels, incurs no
loss in the Chernoff exponent.

For `0<epsilon<=1`, binomial Bernstein gives a two-sided failure bound at
most

\[
 2e^{-\epsilon^2\mu/3}.
\]

The theorem's condition

\[
 \epsilon^2\mu\ge4(Cr+\log2+\omega(1))
\]

therefore beats a family of `e^(Cr)` tests, including the subexponential
number of ranks.  The former coefficient two was corrected to four.

## 6. Post-colouring scope

A uniform whole-role refinement inside a cohort whose members have one
common eligibility menu is exactly Theorem 2.2.  A partition into classes
defined by the already realised path geometry is not generally uniform
and need not be MLD.  Consequently the note correctly leaves
geometry-dependent eligibility, protected sockets, named occurrences, and
exact target-once Rado matching outside the conclusion.

The theorem's exact counterexample is correct: if a class is defined to be
the test set `B` itself, then its count in `B` is deterministically `|B|`,
while an independent class of the same global density has a strictly
smaller positive-`theta` Laplace transform.  Thus arbitrary
geometry-adaptive refinement cannot be silently inserted into the serial
induction.

## 7. Dependency binding

The old-image input is
`MATH_THEOREM_BOOLEAN_MATCHING_IMAGE_STRONG_RAYLEIGH_AND_COLORED_ASSIGNMENT_GATE_20260805.md`.
The transition input is
`MATH_THEOREM_UNIFORM_PARTITION_TRANSITION_REFRESH_AND_BIRTH_GATE_20260805.md`.
Only their unconditional full-interface scopes are used.
