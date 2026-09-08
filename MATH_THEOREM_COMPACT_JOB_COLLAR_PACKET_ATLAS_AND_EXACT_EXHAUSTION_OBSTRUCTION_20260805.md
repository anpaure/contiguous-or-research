# Compact job collars have finite interior packet atlases, but global assembly is exact exhaustion

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional local atlas and exact global obstruction.  Every
strictly support-feasible point of a compact job bank has a neighborhood
with an explicit finite-arity interior-spread packet.  Hence a compact job
support has a finite packet cover.  However, when the complete job and
socket banks have equal work, any assembled socket demand dominated by the
physical socket measure must equal it.  A compactness/partition-of-unity
argument therefore cannot finish with a strict unused socket margin; it
still has to solve the exact aggregate marginal equation.

## 1. Interior simplex packets

Let physical socket values lie in `(q,B)`, where `0<=q<B`.  Fix a job
value `x_0` and an integer `n>=2` satisfying the strict support row

\[
                         nq<x_0<nB.              \tag{1.1}
\]

Choose numbers

\[
 q<y_1^0,\ldots,y_n^0<B,
 \qquad \sum_{i=1}^n y_i^0=x_0.                 \tag{1.2}
\]

This is possible by (1.1), for example with all `y_i^0=x_0/n`.

### Theorem 1.1 (local interior-spread packet)

There are an open job interval `U` containing `x_0`, compact socket
intervals `I_1,...,I_n subset (q,B)`, and a measurable packet kernel

\[
 Q_x(dy_1\cdots dy_n),\qquad x\in U,             \tag{1.3}
\]

such that

\[
 Q_x\{y_1+\cdots+y_n=x\}=1                     \tag{1.4}
\]

and every one-role marginal of `Q_x` is absolutely continuous on its
corresponding `I_i`, with a density bounded uniformly in `x in U`.

Consequently, if `f` is bounded on `U` and `E subset U` is measurable,
the aggregate socket density created by all jobs
`f(x)1_E(x)dx` is bounded by

\[
                         C\int_E f(x)dx          \tag{1.5}
\]

on the fixed compact set `I_1 union ... union I_n`, for a constant `C`
depending only on the packet chart.

### Proof

Choose `eta>0` so small that every point within `2n eta` of every
`y_i^0` remains in `(q,B)`.  For `i<n`, choose independent

\[
                         V_i\sim U[-\eta,\eta]
\]

and put

\[
 Y_i=y_i^0+V_i\quad(i<n),
 \qquad
 Y_n=x-\sum_{i<n}Y_i.                            \tag{1.6}
\]

For `|x-x_0|<eta`, all `Y_i` lie in fixed compact subintervals of
`(q,B)`, and their sum is `x` identically.  The first `n-1` marginals are
uniform.  The last marginal is a translate of the convolution of
`n-1` bounded uniform densities, hence has a bounded density uniformly in
`x`.  This proves (1.3)--(1.4).

Integrating the bounded role densities against `f(x)1_E(x)dx` proves
(1.5). `square`

### Corollary 1.2 (finite collar atlas)

Let `X subset (0,infinity)` be compact and suppose that every `x in X`
obeys (1.1) for at least one `n<=R`.  Then finitely many charts of
Theorem 1.1 cover `X`.

### Proof

The theorem gives an open chart at every point.  Compactness gives a finite
subcover. `square`

This closes local packet existence for the compact gapped Rayleigh core at
every strict support-feasible job value.  It is stronger than an
equal-split chart: the roles vary on a full `(n-1)`-dimensional box.

## 2. Exact exhaustion

Let `mu` and `nu` be positive job and socket measures with equal work,

\[
             \int x\,d\mu(x)=\int y\,d\nu(y)<\infty,          \tag{2.1}
\]

and suppose `nu` is supported in `[q,B]` with `q>0`.  Let a packet kernel
use every job of `mu` and let `rho` be its aggregate socket marginal.

### Theorem 2.1 (domination is equality)

If every packet is exact and

\[
                         \rho\le\nu,             \tag{2.2}
\]

then

\[
                         \boxed{\rho=\nu}.       \tag{2.3}
\]

### Proof

Packetwise exactness and use of the complete job marginal give

\[
 \int y\,d\rho(y)=\int x\,d\mu(x)=\int y\,d\nu(y).
\tag{2.4}
\]

Thus the positive measure `nu-rho` has zero first moment.  Since its
support is contained in `[q,B]` and `q>0`,

\[
 0=\int y\,d(\nu-\rho)(y)
   \ge q(\nu-\rho)([q,B]).                       \tag{2.5}
\]

Therefore `nu-rho=0`. `square`

The same conclusion holds without a positive lower support whenever the
socket measures have no atom at zero: a positive unused measure supported
on `(0,B]` has positive first moment.

## 3. Why a naive finite-cover proof stops

Take a finite collar atlas from Corollary 1.2 and a partition of unity on
the job support.  Applying the corresponding local packet kernel in each
chart produces an explicit aggregate socket density `rho`.  The local
estimate (1.5) makes every individual sufficiently short collar cheap in
`L^infinity`.

But if all jobs are used, Theorem 2.1 says that the desired global row is
not

\[
                         \rho<\nu
\]

with a strict interior margin.  It is the exact equation

\[
                         \boxed{\rho=\nu}.       \tag{3.1}
\]

As the collars are refined, their number grows while their individual
demands shrink; the total work never shrinks.  Compactness alone therefore
does not turn local `O(epsilon)` demand into global slack.

In particular, scalar count/work balance and the already-proved Lorenz
inequalities cannot select the collar weights automatically.  They are
necessary projections of (3.1), while finite configuration examples show
that such projections do not imply whole-packet feasibility.

## 4. A proof-safe finite-flow sufficient condition

The collar atlas does yield a genuine finite-flow theorem after one extra
input.  Partition the physical socket measure into finitely many typed
banks

\[
                         \nu=\nu_1+\cdots+\nu_s. \tag{4.1}
\]

Suppose every chart is supplied with finitely many packet modes and that:

1. the aggregate density produced in socket bank `a` by one unit of mode
   `j` is a fixed density `r_(a,j)`;
2. the job density is partitioned among those modes by nonnegative scalar
   weights; and
3. the finite mode weights solve the **literal bank equations**

   \[
      \sum_j w_j r_{a,j}=d\nu_a/dy
      \quad\text{a.e. on every bank }a.          \tag{4.2}
   \]

Then the packet mixture is an exact coagulation.  If instead the modes
have variable densities inside the charts, (4.2) is an
infinite-dimensional transport equation, not an ordinary finite flow.

Thus a true finite reduction requires a finite invariant socket-role
decomposition for which the packet modes have fixed bank marginals.  The
current Rayleigh compact reduction supplies no such invariant
decomposition.  Its exact remaining aggregate obstruction is (3.1), or
equivalently the compact configuration-price inequalities.

## 5. Consequence for the Rayleigh programme

The local threshold packet and Theorem 1.1 show that neither the
transformed origin nor any strictly feasible compact job value lacks legal
finite packets.  The obstruction is global:

\[
 \boxed{
 \text{select the local packet charts so that their aggregate socket
 marginal exhausts the Rayleigh socket density exactly.}
 }
\tag{5.1}
\]

This identifies why a bare compactness/partition-of-unity argument cannot
close the compact `2/3` gate.  A successful continuation needs either a
Rayleigh-specific exact role decomposition, or the complete price
inequality; local positive density is already enough for every packet
chart.

## 6. Dependencies

1. `MATH_THEOREM_RAYLEIGH_COMPACT_GAPPED_FINITE_ARITY_CORE_20260805.md`;
2. `MATH_THEOREM_COMPACT_GAPPED_UNIFORM_LAYER_FINITE_ARITY_POLYTOPE_20260805.md`;
3. `MATH_THEOREM_RAYLEIGH_FRAGMENTATION_CONVEX_ORDER_AND_CONFIGURATION_CUT_20260804.md`.
