# Product-coset closure of the Apéry variance gate

**Date:** 2026-08-05  
**Method:** pure mathematics; exact variance decomposition; no computation,
search, or solver  
**Status:** unconditional closure theorem.  The finite Apéry variance gate
is stable under independent sums.  Hence every exact CRT-product or
quotient-plus-subgroup product defect assembled from already-positive
factors is positive.  A surviving composite-period obstruction must use
genuine correlation between the quotient coset and its internal defect.

## 1. Abstract product closure

Let `X_1,...,X_m` be independent nonnegative random variables.  Put

\[
 \mu_i=\mathbb EX_i.
\]

Assume each satisfies the Apéry variance inequality

\[
 \operatorname {Var}(X_i)
 \le {\mu_i(\mu_i+1)\over3}.
\tag{1.1}
\]

### Theorem 1.1

The sum

\[
 X=X_1+\cdots+X_m
\]

satisfies

\[
 \boxed{
 \operatorname {Var}(X)
 \le {\mathbb EX(\mathbb EX+1)\over3}.}
\tag{1.2}
\]

#### Proof

Independence and (1.1) give

\[
\begin{aligned}
 3\operatorname {Var}(X)
 &=3\sum_i\operatorname {Var}(X_i)\\
 &\le\sum_i(\mu_i^2+\mu_i)\\
 &\le\left(\sum_i\mu_i\right)^2+\sum_i\mu_i,
\end{aligned}
\]

because all omitted cross terms `2mu_i mu_j` are nonnegative.  This is
(1.2). \(\square\)

The closure is strict whenever at least two factors have positive mean,
even if every factor individually attains equality.

## 2. Exact coset-product consequence

Suppose a cyclic defect profile, under a uniform residue, has an exact
decomposition in law

\[
 \boxed{e(R)=e_Q(Q)+e_H(H),}
\tag{2.1}
\]

where `Q` and `H` are independent uniform quotient and subgroup
coordinates.  If both component defect laws satisfy the variance gate,
then so does the complete defect law.  The general Apéry phase-moment
theorem therefore gives strict formal Rayleigh positivity whenever the
fundamental endpoint period is at most `zeta`.

This covers in particular:

1. direct CRT products of already-closed cyclic metrics;
2. exact quotient-ramp plus subgroup-ramp clocks;
3. iterated mechanical/coset products whose defect law is an independent
   sum of the component laws.

For example, a cheap subgroup producing repeated translated ramps has
defect law

\[
 U_{q-1}+cU_{h-1},
\]

up to deterministic scale, with independent discrete uniforms.  Each
ramp attains or lies below the variance gate, and Theorem 1.1 gives the
combined bound with positive cross-term room.

## 3. Exact surviving composite obstruction

Kneser's theorem reduced the unclosed formal clocks to composite periods
with a nontrivial stabilizer in a critical sublevel sumset.  Theorem 1.1
shows that the stabilizer alone is not an obstruction.  If its internal
metric is the same in every quotient coset and adds independently to the
quotient metric, the clock is already positive.

Thus a surviving profile must have a **correlated coset residual**:

\[
 e(q,h)=m(q)+y_q(h),
\]

where the law of `y_q` depends on `q` in a way that creates positive
between-coset covariance large enough to defeat the independent-sum
bound.  The next finite theorem can therefore be stated as a correlation
control or a coset symmetrization lemma, rather than a generic Kneser
induction.

This corollary does not prove that every cyclic metric admits (2.1), and it
does not address finite shoulders.

## 4. Dependencies

1. `MATH_THEOREM_RAYLEIGH_GENERAL_APERY_PHASE_MOMENTS_AND_VARIANCE_GATE_20260805.md`;
2. `MATH_THEOREM_RAYLEIGH_PRIME_PERIOD_APERY_VARIANCE_AND_FORMAL_POSITIVITY_20260805.md`.
