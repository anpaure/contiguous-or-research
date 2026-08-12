# Uniform packet endpoint criterion and the compact Rayleigh layer gate

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional exact reformulation.  The polygon-width condition
for one job interval and finitely many socket intervals is equivalent to two
transparent endpoint inequalities.  Combined with canonical layer-cake
decomposition, this turns the final compact Rayleigh coagulation into a
finite-arity transport of interval endpoints.  The endpoint transport is
not solved here.

## 1. Endpoint form of uniform joint mixability

Let the job interval be

\[
                         J=[A,B]
\]

and let the socket intervals be

\[
                         S_i=[a_i,b_i],\qquad 1\le i\le n.
\]

All intervals are nondegenerate and lie on the nonnegative line.  Put

\[
 m(I)={\inf I+\sup I\over2},\qquad
 \ell(I)=\sup I-\inf I.
\]

The uniform joint-mixability theorem says that uniform random variables on
these intervals can be coupled so that

\[
                         X=Y_1+\cdots+Y_n
\tag{1.1}
\]

exactly when their centers agree and no interval width exceeds the sum of
all the other widths.

### Theorem 1.1 (endpoint packet criterion)

The uniform packet `(J;S_1,...,S_n)` is jointly mixable if and only if

\[
                         A+B=\sum_{i=1}^n(a_i+b_i),
\tag{1.2}
\]

\[
                         \sum_{i=1}^n a_i\le A,
\tag{1.3}
\]

and, for every `i`,

\[
                         a_i+\sum_{j\ne i}b_j\ge A.
\tag{1.4}
\]

#### Proof

Equation (1.2) is exactly equality of centers.  The job-width inequality is

\[
                         B-A\le\sum_i(b_i-a_i).
\]

Using (1.2), its right side minus its left side is

\[
 \sum_i(b_i-a_i)-(B-A)=2\left(A-\sum_i a_i\right),
\]

so it is equivalent to (1.3).

For socket `i`, the polygon inequality is

\[
 b_i-a_i\le (B-A)+\sum_{j\ne i}(b_j-a_j).
\]

Using (1.2), the right side minus the left side is

\[
 2\left(a_i+\sum_{j\ne i}b_j-A\right),
\]

so it is equivalent to (1.4).  These are all the polygon inequalities.
`square`

### Corollary 1.2 (anchored job layers)

If every job layer has the form `J=[c,B]`, the packet conditions are

\[
 c+B=\sum_i(a_i+b_i),\qquad
 sum_i a_i\le c,qquad
 a_i+\sum_{j\ne i}b_j\ge c\quad(i\in[n]).
\tag{1.5}
\]

Thus the apparent width correlation is only an endpoint packing rule: the
total lower-endpoint load cannot exceed the job's lower endpoint, and
after deleting any one socket interval the remaining upper endpoints,
together with that socket's lower endpoint, must still reach the job's
lower endpoint.

## 2. Exact layer transport

For a continuous density `f`, let `Lambda_f` be its canonical layer measure:
at height `t`, every connected component `I` of `{f>t}` contributes mass
`|I|dt` at the uniform law `U_I`.  Its barycenter is exactly `f(x)dx`.

### Theorem 2.1 (endpoint-layer transport)

Let `mu=f(x)dx` be a finite job measure and `nu=g(y)dy` a finite socket
measure with equal work.  They possess a coagulation within the canonical
uniform-layer ansatz if and only if there is a measure `Pi` on finite
packets

\[
                         (J;S_1,\ldots,S_n)
\]

such that

1. the job marginal of `Pi` is `Lambda_f`;
2. the aggregate socket marginal is `Lambda_g`; and
3. almost every packet satisfies (1.2)--(1.4).

#### Proof

The canonical layer theorem gives the two marginals.  Theorem 1.1 is
equivalent to packetwise uniform joint mixability.  Integrating measurable
packetwise joint mixes gives a coagulation.  Conversely, a construction
inside this ansatz records exactly such a packet measure.  `square`

This is an equivalence only inside the canonical layer ansatz, not with all
possible coagulations.

## 3. The final compact Rayleigh gate

The one-shot Rayleigh reductions produce a pair with

\[
 \operatorname {supp}\mu\subseteq[L_-,L_+],\qquad
 \operatorname {supp}\nu\subseteq[q,b],qquad q>0,
\tag{3.1}
\]

equal work, and a uniform finite arity bound `R`.  Its exact canonical-layer
gate is therefore a **compact finite-arity endpoint transport**:

* every job component is one interval `[A,B]` in a compact subset of
  `[L_-,L_+]^2`;
* every socket component is one interval `[a,b']` in a compact subset of
  `[q,b]^2`;
* packet arity is in `{1,...,R}`; and
* legality is exactly the linear system (1.2)--(1.4).

No vanishing endpoint, unbounded job size, infinite arity, or nonlinear
width condition remains.  Hence a proof may now use finite-dimensional
transport tools on each arity face.  What is still missing is a packet
measure with the exact prescribed layer marginals; compactness and the
scalar count/work rows alone do not produce it.

## 4. Dependencies

1. `MATH_THEOREM_RAYLEIGH_UNIFORM_LAYER_PACKET_TRANSPORT_AND_EQUAL_SPLIT_GATE_20260805.md`;
2. `MATH_THEOREM_RAYLEIGH_COMPACT_GAPPED_FINITE_ARITY_CORE_20260805.md`.
