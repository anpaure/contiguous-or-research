# Independent audit: Rayleigh interval flow, dual closedness, and renewal obstruction

**Date:** 2026-08-05  
**Method:** pure mathematical replay; no computation, search, or solver  
**Audited theorem:**
`MATH_THEOREM_RAYLEIGH_INTERVAL_FLOW_DUAL_CLOSEDNESS_AND_RENEWAL_OBSTRUCTION_20260804.md`  
**Audited theorem SHA-256:**
`3a11524d92ac95b939f8357f8b00f37eb97bb9f4927b85bdfa2628613139074d`  
**Verdict:** **GO after correction.**  The interval-flow equivalence,
narrow closedness, covering-price separation, first-piece law, product-flow
no-go, and diagonal crossing are valid.  One original equivalence involving
lower semicontinuity was false pointwise and has been removed.  The theorem
still does not construct the adaptive Rayleigh flow or prove any discrete,
named, literal, or upper-host gate.

## 1. Basic measure ledger

Put

\[
 A={\sqrt\pi\over2},\qquad p=e^{-A^2},
\]

and

\[
 j(x)=2(A+x)e^{-(A+x)^2},\qquad
 s(y)=2(A-y)e^{-(A-y)^2}.
\]

Direct substitutions give

\[
 \int_0^\infty j(x)\,dx=p,
 \qquad
 \int_0^A s(y)\,dy=1-p.
\]

Integration by parts gives the common workload

\[
 \int_0^\infty xj(x)\,dx
 =\int_A^\infty e^{-u^2}\,du
 =A-\int_0^A e^{-u^2}\,du
 =\int_0^A ys(y)\,dy,
\]

where the middle equality uses
`A=int_0^infinity exp(-u^2)du`.  Thus all later zero-trimming
arguments use an exact equality, not an asymptotic normalization.

## 2. Interval flow is exactly finite coagulation

### 2.1 Forward direction

For one finite configuration with `sum_i y_i=x`, order its pieces and put
them consecutively on `[0,x)`.  The resulting interval occupation is
exactly `1_{[0,x)}`.  Averaging over the job marginal therefore gives

\[
 g(t)=\mu((t,\infty))=e^{-(A+t)^2}.
\]

Each occurrence of a socket becomes exactly one interval, so the complete
length occurrence measure is preserved.  This direction is exact.

### 2.2 Distributional divergence

For an interval measure `eta`, let `sigma_0,sigma_1` be its start and end
marginals.  Testing against a compactly supported `C^1` function gives

\[
 \int f\,d(\sigma_1-\sigma_0)
 =\int_0^\infty f'(t)g(t)\,dt
 =\int f(x)j(x)\,dx-pf(0).
\]

Hence

\[
 \sigma_1-\sigma_0=\mu-p\delta_0.
\]

Because a positive-length interval cannot end at zero,
`sigma_1({0})=0`, and therefore `sigma_0({0})=p`.  With
`tau=sigma_0-p delta_0`, this is precisely

\[
 \sigma_0=p\delta_0+\tau,
 \qquad
 \sigma_1=\mu+\tau.
\]

No boundary sign has been reversed.

### 2.3 Path decomposition and residual elimination

At each positive endpoint `x`, disintegrate the incoming edge measure and
split it in proportions

\[
 {d\tau\over d(\mu+\tau)}(x),
 \qquad
 {d\mu\over d(\mu+\tau)}(x).
\]

Pair the first portion with the outgoing kernel based on `tau`; terminate
the second.  Ionescu--Tulcea iteration from `p delta_0` gives a path
measure and a generated edge submeasure.  Any unused edge measure has no
source.  Its unmatched incoming part is nonnegative, while total start
and end masses of an edge measure are equal.  Hence that unmatched part
has total mass zero, and the unused measure has equal start and end
marginals.

For such a residual `zeta`, its occupation density `h_zeta` has zero
distributional derivative.  It is therefore constant almost everywhere.
But

\[
 \int_0^\infty h_\zeta(t)\,dt
 =\int y\,d\zeta<\infty,
\]

so the constant is zero.  Positive edge lengths then force `zeta=0`.
Thus the generated paths exhaust `eta`.

The edge mass is `nu(0,A)=1-p`, while source-path mass is `p`.  Therefore
the mean edge count is `(1-p)/p<infinity`; infinite paths have zero path
measure.  Every remaining path is a finite configuration whose endpoint
has marginal `mu` and whose edge-length occurrence measure is `nu`.
This verifies the converse without assuming a finite path decomposition in
advance.

## 3. Closedness of the relaxed configuration set

Let `F` be the upward set of available socket measures `b` for which jobs
with marginal `mu` can be covered by finitely many sockets with aggregate
used marginal `lambda<=b`.  The corrected proof uses ordinary narrow
convergence on finite measures on `(0,A)`.

Suppose `b_n -> b` narrowly and choose witnesses `rho_n`.  Since the
constant function one is a narrow test,

\[
 \sup_n b_n(0,A)<\infty,
 \qquad
 \int N\,d\rho_n=\lambda_n(0,A)\le b_n(0,A).
\]

Hence `rho_n(N>R)=O(1/R)`.  On `N<=R`, the fixed job marginal is tight and
the piece coordinates lie in the compactification `[0,A]`; this gives
tightness of the configuration measures.  Narrow convergence of `b_n`
also gives uniform tightness inside `(0,A)`, and domination
`lambda_n<=b_n` prevents positive aggregate piece mass from accumulating at
either endpoint.

For `f>=0` in `C_c((0,A))`, the map

\[
 (x;y_1,\ldots,y_N)\longmapsto\sum_i f(y_i)
\]

is nonnegative lower semicontinuous on the disjoint-union
compactification.  Portmanteau gives

\[
 \int\sum_i f(y_i)\,d\rho
 \le\liminf_n\int\sum_i f(y_i)\,d\rho_n
 \le\int f\,db.
\]

Thus the positive-piece marginal of the limit is at most `b`.  The cover
condition is closed, the job marginal remains `mu`, and zero pieces may be
deleted.  A configuration left with no positive piece would have `x=0`,
which has zero `mu`-mass.  Therefore `F` is closed.  On bounded-mass sets
the narrow topology is metrizable, so the sequential proof gives the
topological closedness used by separation.

## 4. Hahn--Banach separation and pointwise minimization

The set `F` is convex, closed, and upward.  If `nu` were outside it, strong
separation in the weak measure topology would provide a bounded continuous
socket price `a`.  Upward closure forces `a>=0`: otherwise adding an
arbitrary positive atom at a point where `a<0` would violate the separating
orientation.

For fixed job size `x`, the least price of a finite cover is

\[
 a^\star(x)=\inf\left\{\sum_i a(y_i):0<y_i<A,
                                  \ \sum_i y_i\ge x\right\}.
\]

The identity

\[
 \inf_{b\in F}\int a\,db=\int a^\star(x)\,d\mu(x)
\]

is valid.  To audit the only possible integrability gap, restrict pieces
first to `[1/M,A-1/M]`.  Removing redundant pieces leaves at most
`O_M(1+x)` pieces, and this is integrable because `mu` has finite first
moment.  Compact measurable selection gives a near-minimizing kernel.
These restricted infima decrease to `a^star`; a cover by repetitions of
one fixed socket length supplies an integrable `O(1+x)` dominator.  Thus
dominated convergence proves the identity.

The strict separator would therefore violate the stated covering-price
inequality.  Conversely, the inequality is necessary configuration by
configuration.  This proves the price iff theorem.

At the critical workload, any relaxed witness satisfies

\[
 0\le
 \int(\sum_i y_i-x)\,d\rho
 +\int y\,d(\nu-\lambda)=0.
\]

Both positive terms vanish.  Hence every job is covered exactly and the
positive measure `nu-lambda` has zero integral against the strictly
positive function `y`; consequently `lambda=nu`.

## 5. Required correction: covering closures are not pointwise lsc

The original draft additionally claimed an equivalence with
lower-semicontinuous literal covering closures.  That statement is false
as written.  If `a(y)=1` on `(0,A)`, then

\[
 a^\star(x)=\min\{N:N A>x\}.
\]

In particular, `a^star` jumps upward at `x=mA`; it is not lower
semicontinuous there.  This is caused by the strict physical constraint
`y<A`.

The erroneous sentence has been removed from the theorem.  Since both
Rayleigh measures are atomless, one may replace a monotone closure by its
left-limit representative inside the integrals without changing their
values, but that representative is not the literal pointwise covering
cost at a jump.  The corrected iff theorem quantifies over bounded
continuous socket prices and uses their literal closures, with no lsc
claim.

This correction does not weaken the separation theorem or any later
conclusion.

## 6. First-piece law

Every positive piece in a job of size `x` is at most `x`.  Therefore every
job with `x<=t` has first piece at most `t`, and

\[
 \kappa(0,t]\ge\mu(0,t].
\]

As `kappa<=nu`, direct integration gives

\[
 (\nu-\kappa)(0,t]
 \le e^{-(A-t)^2}+e^{-(A+t)^2}-2p
 =2p\bigl(e^{-t^2}\cosh(2At)-1\bigr).
\]

Since `A^2=pi/4`, the expansion is

\[
 p(\pi-2)t^2+O(t^4).
\]

For positivity on `(0,A]`, the derivative has the sign of
`A tanh(2At)-t`.  Its derivative decreases strictly from a positive value,
so it has one positive zero; the Gaussian sum first rises and then falls.
Its endpoint value is `1+e^{-pi}>2p`, since `p<1/2`.  Thus it never returns
to its value at zero.  The sign statement in the theorem is correct.

## 7. Product-flow renewal no-go

Normalize the length factor `k` in `eta=alpha tensor k` to be a
probability.  The length marginal then forces

\[
 k={\nu\over1-p}.
\]

Writing `alpha=p delta_0+tau`, convolution of the start law with `k` and
the exact divergence identity give

\[
 \tau=pk+\tau*k-\mu.
\]

The density of `k` is bounded near zero.  Since `tau({0})=0`,
`(tau*k)(x)->0` as `x downarrow0`.  Hence the forced right density of
`tau` at zero is

\[
 2Ap\left({p\over1-p}-1\right)
 =2Ap{2p-1\over1-p}<0,
\]

because `p=e^{-pi/4}<1/2`.  Continuity makes the density negative on a
right neighborhood, contradicting positivity.

There is also a direct consistency check: the first-piece marginal of a
product flow is `pk=p nu/(1-p)`, whose density at zero is strictly smaller
than the job density, contradicting the first-piece law for small `t`.
The no-go applies only to start-independent product flows.

## 8. Diagonal crossing and residual face

The equality `j(c)=s(c)` is equivalent to

\[
 {A+c\over A-c}=e^{4Ac}.
\]

With `c=A theta`, this becomes

\[
 {\operatorname{arctanh}\theta\over\theta}={\pi\over2}.
\]

The left side increases strictly from one to infinity, so there is exactly
one positive solution.  The endpoint signs give `s>j` below it and `j>s`
above it.

Removing `min(j,s)` as explicit one-piece configurations subtracts the
same measure from both marginals.  It preserves workload equality and
count difference, and leaves sockets supported below `c` and jobs above
`c`.  This is only a sufficient construction face; the theorem correctly
does not assert that an arbitrary kernel can be rearranged into it.

## 9. Exact scope

The audited theorem proves:

1. finite coagulations are exactly interval flows with the stated length
   marginal and occupation profile;
2. the relaxed available-measure set is narrowly closed;
3. all bounded-continuous covering-price inequalities are necessary and
   sufficient for the anonymous continuum coagulation;
4. every successful flow satisfies the quadratic short-internal-socket
   aperture;
5. no start-independent product flow works;
6. the unique-density-crossing cancellation is a valid sufficient face.

It does **not** prove any covering-price inequality, construct the adaptive
interval kernel, round a continuum flow to one copy of each discrete job or
socket, provide named Boolean containment, serialize literal runs, or
construct the upper/residence carrier.  In particular it does not prove
`nu(k)=B(k)+O(1)`.

