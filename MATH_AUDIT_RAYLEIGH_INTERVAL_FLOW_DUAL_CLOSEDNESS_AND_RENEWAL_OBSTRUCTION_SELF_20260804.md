# Self-audit: Rayleigh interval flow, dual closedness, and renewal obstruction

**Date:** 2026-08-04  
**Audited file:**
`MATH_THEOREM_RAYLEIGH_INTERVAL_FLOW_DUAL_CLOSEDNESS_AND_RENEWAL_OBSTRUCTION_20260804.md`  
**Method:** independent line-by-line mathematical replay; no computation,
search, or solver  
**Verdict:** **GO**, with the adaptive Rayleigh interval kernel explicitly
left open.

## 1. Interval/configuration equivalence

For one configuration, the consecutive intervals of its ordered pieces
partition `[0,x)`.  Aggregating therefore gives occupation density
`mu((t,infinity))=exp(-(A+t)^2)` and preserves the complete socket-length
marginal.

Conversely, testing an interval measure against `f'` gives

\[
 \sigma_1-\sigma_0=\mu-p\delta_0.
\]

Because positive-length intervals cannot end at zero, the start atom at
zero has mass exactly `p`; the remaining start and end marginals are the
same measure `tau`.  Pairing those two copies of `tau` gives an acyclic
flow.  A finite residual circulation would have constant occupation
density and finite occupation integral, hence zero occupation and zero
edge mass.  Thus the path decomposition exhausts the interval measure.
Its total edge mass is `1-p`, so the edge count of a source path has finite
mean `(1-p)/p`; paths are finite almost surely.  The reverse implication is
therefore exact, not merely a relaxation.

## 2. Closedness and price sufficiency

The physically correct relaxed configuration condition is
`sum_i y_i >= x`, with aggregate used-capacity marginal `lambda<=b`.
For a convergent bounded family of available marginals, expected piece
count is bounded.  Configurations of bounded piece count are tight after
compactifying the piece interval by zero.  Zero pieces may be deleted.

The only possible marginal-loss issue is a vanishing mass of
large-piece-count configurations.  It cannot lose positive-size socket
mass: for every `epsilon>0`, a configuration has at most `x/epsilon`
pieces of size at least `epsilon`, and the fixed job first moment controls
that quantity after truncation.  Hence the positive-piece marginal of the
limit remains below the limiting available marginal.  This verifies the
closedness used by separation.

The feasible available-marginal set is convex and upward closed, so a
separator has nonnegative socket price.  Minimization separates over jobs
and is exactly the covering closure `a^star`.  Finally

\[
 \int(\sum_i y_i-x)\,d\rho+
 \int y\,d(\nu-\lambda)=0
\]

forces both zero trimming and full use.  Thus the price inequalities are
an actual iff theorem.  This closes only the former analytic closedness
caveat; it does not prove any missing price inequality.

## 3. Boundary law

Every job of size at most `t` has first piece at most `t`, proving
`kappa(0,t]>=mu(0,t]`.  Therefore

\[
 (\nu-\kappa)(0,t]
 \le 2p(e^{-t^2}\cosh(2At)-1)
 =p(\pi-2)t^2+O(t^4).
\]

The right side is positive on the full physical interval: its underlying
two-Gaussian sum increases and then decreases, while its value at `A` is
still larger than its value at zero.  The direction of every inequality
is correct.

## 4. Renewal no-go

For a product interval measure, the common length law is forced to be
`k=nu/(1-p)`.  Flow balance gives

\[
 \tau=pk+\tau*k-\mu.
\]

The internal start measure has no atom at zero, so the convolution density
vanishes at the right endpoint zero.  The forced density there is

\[
 2Ap{2p-1\over1-p}<0,
\]

because `p=e^{-pi/4}<1/2`.  This is a literal contradiction to positivity.
It rules out only start-independent/iid lengths, not adaptive Markov or
history-dependent lengths.

## 5. Diagonal crossing and scope

The density crossing equation reduces exactly to

\[
 \operatorname{arctanh}\theta={\pi\over2}\theta,
\]

which has one positive solution because
`atanh(theta)/theta` increases from one to infinity.  Removing the common
density as explicitly declared one-piece configurations leaves sockets
strictly below the crossing and jobs strictly above it, with equal work.

The theorem deliberately uses this only as a sufficient construction
face.  It does not claim that an arbitrary already-existing kernel can be
cancelled onto that face.  It also does not claim the all-grid Bellman
inequality, discrete integer absorption, named Boolean containment,
literal serialization, or the upper/residence host.

