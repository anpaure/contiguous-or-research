# Self-audit: Rayleigh uniform-layer packet transport and equal-split gate

**Date:** 2026-08-05  
**Method:** line-by-line mathematical replay; no computation, search, or
solver  
**Audited theorem:**
`MATH_THEOREM_RAYLEIGH_UNIFORM_LAYER_PACKET_TRANSPORT_AND_EQUAL_SPLIT_GATE_20260805.md`  
**Verdict:** **GO.**  The layer barycenter, uniform-packet criterion,
measurable integration, scaled socket density, and eventual Gaussian-tail
domination are exact.  The theorem is only sufficient outside its
explicitly defined layer-packet ansatz and does not claim the full
all-band inequality (4.4).

## 1. Layer measure

For each level `t`, the connected components of `{f>t}` are disjoint
intervals.  Weighting `U_I` by `|I|dt` cancels its normalizing denominator.
Tonelli therefore gives

\[
 \int U_I(B)d\Lambda_f
 =\int_0^\infty |B\cap\{f>t\}|dt
 =\int_Bf.
\]

The mass and midpoint identities follow by testing against one and `x`.
For the analytic Rayleigh densities, all relevant superlevel components
are bounded; endpoint and critical levels form a null set.  No degenerate
uniform law carries positive layer mass.

## 2. Uniform packet row

Reflecting `U_[a,b]` gives `U_[-b,-a]`, with the same support length and
negative midpoint.  The sum of means of
`(U_(S_1),...,U_(S_N),-U_J)` is zero exactly when socket midpoints sum to
the job midpoint.  For uniform marginals, the Wang--Wang length inequality
is necessary and sufficient, and is precisely

\[
 \ell(J)+\sum_i\ell(S_i)
 \ge2\max\{\ell(J),\ell(S_i)\}.
\]

For each arity, the coupling correspondence is nonempty and compact; fixed
marginal and fixed-sum conditions are closed under weak convergence.  Its
parameter graph is Borel, so measurable selection and integration are
legitimate.  The theorem correctly claims a converse only inside the
canonical layer-packet construction, not among all coagulations.

## 3. Equal splitting

For `x in ((n-1)c,nc)`,

\[
 0<{x\over n+1}<{n\over n+1}c<c.
\]

The pushforward density under `y=x/(n+1)` is
`(n+1)j((n+1)y)`; multiplying by the `n+1` occurrences gives the square
factor in (3.4).  Work is preserved exactly.

On interval layers, the `n+1` scaled socket midpoints sum to the job
midpoint.  Their total width equals the job width, so after including the
job width the length sum is twice the largest width.  Uniform joint
mixability sits exactly on its polygon boundary.  The deterministic equal
split is an even simpler direct realization.

## 4. Active-index algebra and scope

Writing `m=n+1` and `y=c-delta`, the scaled-band conditions are

\[
 (m-2)c<my<(m-1)c.
\]

They rearrange to

\[
 c/delta<m<2c/delta,
\]

so (4.3) is correct.  For any compact subinterval below `c`, only finitely
many integers occur; near `c`, the Gaussian factors give absolute local
summability.

If (4.4) holds, `rho_hi` is literally a submeasure of `nu_res`.  Removing
the high jobs and their constructed sockets preserves positivity and equal
work.  Nothing in this argument solves the low bank or proves (4.4), and
the theorem says neither.

For the eventual theorem, an active index `m` satisfies
`L<m<2L`, where `L=c/(c-y)`.  Therefore

\[
 my>(m-2)c.
\]

Since `m>=4` and `2c>A`, monotonicity of `j` gives the first inequality in
(4.15), while `m-2>=m/2` gives its Gaussian bound.  The resulting series is
`O(L^3 exp(-c^2L^2/8))`.

On the physical side, `sigma/(c-y)` extends continuously and positively to
`c`.  Formula (4.9) verifies the endpoint derivative; `theta>17/20` makes
`A^2-c^2<1/2`.  Positivity away from `c` follows from the unique crossing.
Thus `sigma>=q_0(c-y)=q_0c/L` on the terminal half interval.  Exponential
decay beats `1/L`, proving eventual pointwise domination.  This is a true
all-tail theorem, but it intentionally leaves a finite compact job bank.
The scope is therefore proof-safe.
