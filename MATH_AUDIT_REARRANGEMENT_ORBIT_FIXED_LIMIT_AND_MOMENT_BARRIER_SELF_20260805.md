# Self-audit: rearrangement fixed-limit dichotomy and moment barrier

**Date:** 2026-08-05  
**Audited source:**
`MATH_THEOREM_REARRANGEMENT_ORBIT_FIXED_LIMIT_DICHOTOMY_AND_MOMENT_BARRIER_20260805.md`  
**Source SHA-256:**
`3db3e17d8d3c409bd42bd321b62aba7e12053bfe68b483dce832ecc9a0f308af`  
**Verdict:** **GO.**  The theorem proves conditional `L1` decay, not the
Rayleigh moment barrier and not box-norm decay.

## 1. Mass and overlap ledger

From `H_(n+1)=p_n-C_n` and `int C_n=int q_n=int p_n=A_n`, one has

\[
 p_{n+1}=(p_n-C_n)_+\le p_n,
 \qquad
 A_n-A_{n+1}=\int\min(p_n,C_n).
\]

Thus `A_n` converges, `p_n` converges in `L1`, and the overlap tends to
zero.  No compactness claim is used in this step.

## 2. Profile-moment inequality

For every negative superlevel component `(a,a+ell)` and `alpha>=0`,

\[
 \int_0^\ell t^\alpha dt
 \le\int_a^{a+\ell}t^\alpha dt.
\]

Layer cake proves `M_alpha(C_n)<=M_alpha(q_n)`.  Since
`q_n=(C_(n-1)-p_(n-1))_+<=C_(n-1)`, all nonnegative profile moments are
nonincreasing after the first profile.  This checks both the direction
and the index in Lemma 4.1.

## 3. Weak-limit structure

A uniform second moment gives tightness of the measures `C_n(t)dt` and
uniform integrability of their first moments.  On `[epsilon,R]`,
monotonicity and the mass bound imply

\[
 C_n(t)\le A_0/\epsilon.
\]

Therefore no singular mass can develop away from zero.  A subsequential
limit has exactly the form

\[
 \alpha\delta_0+c(t)dt
\]

with `c` nonincreasing.  Vanishing overlap makes `c` disjoint from the
`L1` limit of `p_n`.  This is sufficient; convergence of `C_n` in `L1`
is not assumed in the envelope-free theorem.

## 4. Strict barycentre check

If surviving mass is positive and `c` has finite support endpoint `tau`,
the positive `L1` mass is supported in `[tau,infinity)`, while the
continuous negative mass lies strictly before `tau` and any singular
negative mass lies at zero.  Equal total masses therefore give a strict
positive signed first moment.  If `c` has unbounded support, it is
positive almost everywhere and disjointness would force the positive
mass to vanish.  If `c=0`, all negative limit mass is at zero and the
strict inequality is again immediate.

Uniform second moments justify passage of first moments to the weak
limit.  Hence an all-iterate nonpositive signed-moment barrier contradicts
every nonzero surviving limit and forces `A_n->0`.

## 5. Scope

The argument supplies no proof that the Rayleigh orbit obeys

\[
 \sup_n\int tK_n(t)dt\le0.
\]

It also does not turn `L1` convergence into the unit-block box norm;
that still needs a local regularity/tail upgrade.  No all-price or OR-word
claim is made.

