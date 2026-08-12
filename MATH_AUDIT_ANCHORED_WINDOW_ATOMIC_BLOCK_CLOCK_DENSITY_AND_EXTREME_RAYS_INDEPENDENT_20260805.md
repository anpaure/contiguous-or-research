# Independent-style audit: anchored atomic blocks and dense superadditive clocks

**Date:** 2026-08-05  
**Audited file:**
`MATH_THEOREM_ANCHORED_WINDOW_ATOMIC_BLOCK_CLOCK_DENSITY_AND_EXTREME_RAYS_20260805.md`  
**Method:** pure mathematics; no computation, search, or solver  
**Verdict:** **GO**, with the universal Rayleigh sign explicitly left open.

## 1. Closed-interval equivalence

Starting from

\[
 \rho((x,x+t])\le\rho([0,t]),
\]

the substitution `x=u-epsilon`, `t=v-u+epsilon` gives

\[
 \rho([u,v])\le\rho([0,v-u+\epsilon]).
\]

Continuity from above is legitimate because the measures are locally
finite.  Conversely, applying the closed-interval inequality to
`[x+epsilon,x+t]` and then using continuity from below recovers the open
left endpoint.  Thus no atom is lost at either boundary.

For an ordered locally discrete support, every interval cuts out one
consecutive block.  Its intrinsic span is no larger than the ambient
interval length, so the block inequalities are both necessary and
sufficient.  In the unit-weight case, a block of `m+1` atoms is dominated
by the initial `m+1` atoms exactly when

\[
 x_m\le x_{p+m}-x_p.
\]

This is precisely superadditivity.

## 2. Ceiling quantization

The key inequality is exact:

\[
 \lceil Nf(x+y)\rceil
 \le\lceil Nf(x)+Nf(y)\rceil
 \le\lceil Nf(x)\rceil+\lceil Nf(y)\rceil.
\]

Thus ceiling quantization, unlike a generic shifted floor, preserves
subadditivity.  Integer jumps split into unit atoms.  The inverse jump
locations obey

\[
 a_{i+j}\ge a_i+a_j
\]

by applying subadditivity before taking the two suprema.  Initial jumps
produce repeated zero positions; bounded prices produce an eventual
cemetery position at infinity.  Both conventions agree with the stated
scope.

The uniform estimate

\[
 0\le {\lceil Nf\rceil\over N}-f<{1\over N}
\]

proves convergence of cumulative functions and hence vague convergence of
the Stieltjes measures.  More importantly, because the two Rayleigh
measures have finite total variation, it gives the direct pairing bound

\[
 \left|\int K\,d(\rho_N-\rho)\right|
 \le {\|\mu-\nu\|_{TV}\over N}.
\]

Therefore no unproved uniform-integrability step is hidden in the passage
from discrete clocks to the continuum cone.

## 3. Extreme-ray argument

In a positive decomposition of a unit counting measure, both summands are
supported on the original atom set.  If the first summand has weights
`c_n`, singleton interval domination gives `c_n<=c_0`.  Applying the same
inequality to the complementary weights gives `1-c_n<=1-c_0`, hence
`c_n=c_0` for all `n`.  This is a complete extreme-ray proof.

Arithmetic clocks are therefore extreme, but the proof applies to every
strict superadditive clock.  The example `x_n=hn^2` is valid since

\[
 (m+n)^2\ge m^2+n^2.
\]

The theorem carefully states only that arithmetic grids do not exhaust
the extreme-ray tests; it does not make an unnecessary closed-conic-hull
claim.

## 4. Rayleigh comparisons

If `x_1>=zeta`, then `x_n>=nx_1` and every compared argument is on the
increasing branch of `K`; hence the arithmetic clock with step `x_1` is a
termwise lower bound.  The cited all-ceiling theorem supplies its strict
positive sum.

For the parity clock

\[
 b_{2q}=2qA,
 \qquad
 b_{2q+1}=2qA+15A/16,
\]

even-plus-any parity gives equality in superadditivity, and odd-plus-odd
has slack `A/8`.  Its even terms coincide with the step-`A` arithmetic
clock.  Every odd term is strictly smaller in `K`: the first comparison is
inside the proved increasing interval `[15A/16,A]`, and all later ones are
on the increasing Gaussian tail.  The strict comparison of the two sums is
therefore exact and absolutely convergent.

## 5. Scope boundary

The theorem proves

\[
 \text{anchored-window positivity}
 \quad\Longleftrightarrow\quad
 \sum_jK(a_j)\ge0
 \text{ for every superadditive clock}.
\]

It does **not** prove the right-hand statement.  That statement is exactly
the all-grid Bellman gate already isolated in the source record.  In
particular, the theorem does not claim:

* that arithmetic combs generate all anchored measures;
* that every extreme ray is arithmetic;
* that all superadditive clock sums are positive;
* a continuum coagulation;
* a discrete carrier or an `O(1)` OR-word theorem.

The theorem is proof-safe within these boundaries.
