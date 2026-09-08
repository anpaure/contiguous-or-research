# Compact gapped Rayleigh core: exact finite-arity layer polytope

**Date:** 2026-08-05  
**Method:** pure mathematics; no search or solver  
**Status:** unconditional exact formulation and a homothetic Monge face.
The compact gapped Rayleigh core has an exact finite-arity transport
polytope on its canonical uniform interval layers.  Its complete dual is a
single interval-configuration price inequality.  Proportional
(`homothetic`) role packets form an especially simple Monge subface which
strictly contains equal splitting.  Feasibility of the Rayleigh marginals
in that subface, or in the full polytope, is not proved here.

## 1. Compact gapped input

Let

\[
 \mu(dx)=f(x)dx,
 \qquad
 \nu(dy)=g(y)dy
\]

be finite continuous measures of equal first moment, with

\[
 \operatorname {supp}\mu\subseteq[\delta,M],
 \qquad
 \operatorname {supp}\nu\subseteq[q,b],           \tag{1.1}
\]

where `delta,q>0`.  The compact-gapped reduction for the Rayleigh pair
has exactly this form.  Every exact configuration has arity at most

\[
 R=\lfloor M/q\rfloor.                             \tag{1.2}
\]

Let `Lambda_f,Lambda_g` be the canonical uniform-interval layer measures.
Thus `Lambda_f` is a finite measure on compact intervals `J subset
[delta,M]`, `Lambda_g` is one on compact intervals `S subset [q,b]`, and
their barycenters are `f(x)dx,g(y)dy`.

For an interval `I=[a_I,b_I]`, write

\[
 m(I)={a_I+b_I\over2},\qquad \ell(I)=b_I-a_I.
\]

## 2. The finite-arity packet relation

For `1<=n<=R`, let `P_n` be the compact set of tuples

\[
 (J;S_1,\ldots,S_n)
\]

such that

\[
 m(J)=\sum_{i=1}^n m(S_i)                         \tag{2.1}
\]

and

\[
 \ell(J)+\sum_{i=1}^n\ell(S_i)
 \ge2\max\{\ell(J),\ell(S_1),\ldots,\ell(S_n)\}. \tag{2.2}
\]

These are exactly the uniform joint-mixability rows: a tuple lies in
`P_n` iff interval-uniform random variables with those marginals can be
coupled so that

\[
 X=Y_1+\cdots+Y_n
\]

almost surely.

### Theorem 2.1 (exact layer transport polytope)

The canonical uniform-layer ansatz coagulates `(mu,nu)` iff there are
finite nonnegative measures `Pi_n` on `P_n`, `1<=n<=R`, satisfying

\[
 \boxed{
 \sum_{n=1}^R(\operatorname {pr}_J)_\#\Pi_n
 =\Lambda_f}                                      \tag{2.3}
\]

and

\[
 \boxed{
 \sum_{n=1}^R\sum_{i=1}^n
 (\operatorname {pr}_{S_i})_\#\Pi_n
 =\Lambda_g.}                                     \tag{2.4}
\]

Equivalently, one may replace equality in (2.4) by domination `<=`.
Indeed packetwise center conservation and (2.3) make the first moment of
the used socket-layer marginal equal to the job first moment, which is
also the first moment of `Lambda_g`.  Since every unused socket interval
has center at least `q>0`, a nonzero unused positive layer measure would
have positive first moment.  Hence domination forces equality.

### Proof

If the measures exist, select a joint mix on every packet and integrate
the resulting kernels against `Pi_n`.  Equations (2.3)--(2.4) and the
uniform-layer barycenter identities give exactly the desired job and
aggregate socket marginals.

Conversely, a construction inside the canonical layer-packet ansatz has a
well-defined distribution of its job interval, arity, and socket
intervals.  Those distributions are the measures `Pi_n` and satisfy
(2.3)--(2.4). `square`

This is a finite-**arity** compact polytope, not a finite-dimensional one.

## 3. Exact price/Hall dual

For a continuous socket-layer price `theta`, define the cheapest packet
price of a job layer by

\[
 \Psi_\theta(J)=
 \min_{\substack{1\le n\le R\\
                  (J;S_1,\ldots,S_n)\in P_n}}
 \sum_{i=1}^n\theta(S_i),                          \tag{3.1}
\]

with value `+infinity` if no packet exists.

### Theorem 3.1 (complete compact dual)

The layer polytope (2.3)--(2.4) is feasible iff

\[
 \boxed{
 \int\Psi_\theta(J)\,d\Lambda_f(J)
 \le
 \int\theta(S)\,d\Lambda_g(S)}                   \tag{3.2}
\]

for every continuous nonnegative socket-layer price `theta`.

### Proof

Necessity follows by applying (3.1) packetwise and integrating.

For sufficiency, use the equivalent domination form of (2.4).  The
disjoint union of the compact packet spaces `P_n` is compact.  Packet
measures whose job marginal is the fixed measure `Lambda_f` have fixed
total mass and form a compact convex set.  Their aggregate socket
marginals therefore form a compact convex set `C`.  The order interval

\[
 D=\{H:0\le H\le\Lambda_g\}
\]

is compact and convex as well.  Infeasibility says `C cap D` is empty.
Strong separation gives a continuous `theta` such that

\[
 \inf_{H\in C}\int\theta\,dH
 >\sup_{H\in D}\int\theta\,dH
 =\int\theta_+\,d\Lambda_g.                       \tag{3.3}
\]

Replacing `theta` by `theta_+` can only increase the left infimum, so the
strict separation remains and the price may be taken nonnegative.  For a
nonnegative continuous price, minimization over packet measures with fixed
job marginal separates job layer by job layer; compactness and measurable
selection give

\[
 \inf_{H\in C}\int\theta\,dH
 =\int\Psi_\theta\,d\Lambda_f.                    \tag{3.4}
\]

Equations (3.3)--(3.4) violate (3.2), a contradiction. `square`

Indicator approximations give ordinary Hall-type consequences, but they
are not complete by themselves: a hypergraph configuration polytope
requires general prices, just as in the discrete configuration LP.

## 4. A homothetic Monge packet

For `lambda>0`, let

\[
 D_\lambda([a,b])=[\lambda a,\lambda b].
\]

### Lemma 4.1 (proportional interval packet)

Let `lambda_1,...,lambda_n>0` and

\[
 \sum_{i=1}^n\lambda_i=1.
\]

Assume additionally that every dilated socket interval lies in the
physical socket layer space:

\[
 D_{\lambda_i}J\subseteq[q,b]
 \qquad(1\le i\le n).                              \tag{4.1a}
\]

Then

\[
 \boxed{
 (J;D_{\lambda_1}J,\ldots,D_{\lambda_n}J)\in P_n.} \tag{4.1}
\]

Moreover the joint mix is deterministic: if `X` is uniform on `J`, put

\[
 Y_i=\lambda_iX.
\]

### Proof

The centers add because

\[
 \sum_i m(D_{\lambda_i}J)
 =\left(\sum_i\lambda_i\right)m(J)=m(J).
\]

The lengths satisfy

\[
 \sum_i\ell(D_{\lambda_i}J)=\ell(J).
\]

Hence the left side of (2.2) is `2 ell(J)`, while no individual length
exceeds `ell(J)`.  This proves (4.1), and the displayed deterministic
coupling proves the final assertion. `square`

### Corollary 4.2 (homothetic Monge sufficient condition)

Suppose `Lambda_f` can be decomposed into measures on job layers carrying
finite probability kernels on simplices

\[
 \Delta_n^\circ={(\lambda_1,\ldots,\lambda_n):
 \lambda_i>0,\ \sum_i\lambda_i=1},
 \qquad1\le n\le R,
\]

such that the aggregate dilation identity

\[
 \boxed{
 \Lambda_g
 =\int\sum_i\delta_{D_{\lambda_i}J}
       \,d\mathsf P_J(\lambda)\,d\Lambda_f(J)}    \tag{4.2}
\]

holds.  Then `(mu,nu)` has an exact finite coagulation.

This face strictly contains equal splitting, which is the special choice
`lambda_i=1/n`.

There is a parallel, direct literal Monge condition which does not require
the canonical layer identity (4.2): there is a kernel assigning to every
job value `x` a finite mass partition
`lambda_1+...+lambda_n=1` such that

\[
 \boxed{
 \int\varphi(y)g(y)dy
 =\int f(x)
   \mathbb E_x\!\left[\sum_i\varphi(\lambda_i x)\right]dx}   \tag{4.3}
\]

for every continuous test function `varphi`.  Equation (4.3) is the exact
differing-role dilation equation.  For fixed equal arity `n` it reduces to
the familiar density term `n^2f(ny)`.

Condition (4.2) implies such a literal construction by the interval
couplings in Lemma 4.1.  Conversely, a literal `x`-dependent kernel
satisfying (4.3) gives a Monge coagulation directly but need not induce
the canonical layer identity (4.2).  No converse between the two faces is
claimed.

## 5. Support simplex and the exact remaining Monge gate

For the compact gapped core, every proportional part must obey

\[
 q\le\lambda_i x\le b.
\]

Thus the allowed simplex at job value `x` is

\[
 \boxed{
 \mathcal D(x)=
 \bigcup_{1\le n\le R}
 \left\{\lambda\in\Delta_n^\circ:
 {q\over x}\le\lambda_i\le {b\over x}
 \right\}.}                                      \tag{5.1}
\]

It is nonempty exactly when some integer `n<=R` satisfies

\[
 nq\le x\le nb.                                   \tag{5.2}
\]

Every actual configuration necessarily satisfies the same scalar support
row, so (5.2) loses no information at that level.

The strongest simple Monge target is now:

> construct a measurable kernel on `\mathcal D(x)` satisfying the exact
> dilation marginal (4.3).

This is broader than the dead bounded equal-split ansatz and does not
require the whole socket density to be monotone.  It remains a genuine
partition-valued transport problem: ordinary northwest-corner transport
of work mass is insufficient because the outgoing proportions belonging
to one job must sum to one in the same configuration.

## 6. Exact scope

The theorem closes the functional-analytic formulation of the compact
gapped uniform-layer gate and identifies a concrete Monge face.  It does
not prove (3.2) for the Rayleigh layer measures or solve (4.2)--(4.3).
The surviving scalar/transport statement is the partition-valued dilation
identity (4.3), with the compact simplex restriction (5.1).

## 7. Frozen dependencies

1. `MATH_THEOREM_RAYLEIGH_UNIFORM_LAYER_PACKET_TRANSPORT_AND_EQUAL_SPLIT_GATE_20260805.md`.
2. `MATH_THEOREM_RAYLEIGH_COMPACT_GAPPED_FINITE_ARITY_CORE_20260805.md`,
   SHA at use
   `c34da2922b19d851c07ee7fb266442dc05b4e8f6a25cabfb4dab73b220ec6aeb`.
