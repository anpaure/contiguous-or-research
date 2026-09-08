# Anchored uniform packets reduce exactly to endpoint composition

**Date:** 2026-08-05  
**Method:** pure mathematics; Wang--Wang uniform joint mixability; no search
or solver  
**Status:** unconditional exact reduction.  A lower-anchored uniform job
layer and upper-anchored uniform socket layers are jointly mixable exactly
when their free endpoints satisfy one ordinary composition equation.  For
monotone job/socket densities, the complete anchored layer-packet problem
therefore reduces to a bounded one-dimensional endpoint coagulation.  The
first Rayleigh residual socket density is not monotone, so a positive bank
of internal socket layers remains outside this anchored reduction.

## 1. One packet

Fix `B>0`.  For `B<=z<=nB` and `0<=a_i<=B`, let

\[
 J_z=[B,z],\qquad S_{a_i}=[a_i,B],\qquad1\le i\le n,
\]

where `n>=2`.

### Theorem 1.1 (anchored packet criterion)

There are uniform random variables

\[
 X\sim U_{J_z},\qquad Y_i\sim U_{S_{a_i}}
\]

on one probability space satisfying

\[
 X=Y_1+\cdots+Y_n\quad\text{almost surely}       \tag{1.1}
\]

if and only if

\[
 \boxed{a_1+\cdots+a_n=z-(n-1)B.}                \tag{1.2}
\]

### Proof

Necessity follows by taking expectations:

\[
 {B+z\over2}=\sum_{i=1}^n{a_i+B\over2}.
\]

Conversely, (1.2) is the midpoint equality for the tuple
`(Y_1,...,Y_n,-X)`.  Its interval widths are

\[
 z-B,\qquad B-a_1,\ldots,B-a_n.
\]

Using (1.2), their total is

\[
 (z-B)+\sum_i(B-a_i)=2(n-1)B.                    \tag{1.3}
\]

Every individual width is at most `(n-1)B`: the job width obeys this
because `z<=nB`, while each socket width is at most `B` and `n>=2`.
Therefore the longest width is at most half of (1.3).  This is exactly the
uniform joint-mixability polygon inequality.  Wang--Wang's uniform theorem
now gives (1.1). `square`

No extra support inequality survives: once (1.2), `z<=nB`, and
`0<=a_i<=B` hold, all of them are automatic.

## 2. Measure-level endpoint reduction

Let a decreasing density `f` be supported on `[B,infinity)` and an
increasing density `g` on `[0,B]`.  Their canonical superlevel
decompositions are supported respectively on anchored intervals

\[
 [B,z]\quad\text{and}\quad[a,B].                 \tag{2.1}
\]

Write their layer measures as `Lambda_f(dz)` and `Lambda_g(da)`.

Choose an arity `n>=2` for every job layer, subject to `z<=nB`, and define
its endpoint demand

\[
 q=z-(n-1)B\in[0,B].                              \tag{2.2}
\]

### Theorem 2.1 (endpoint-composition lift)

Suppose there is a measure on finite endpoint configurations

\[
 (q;a_1,\ldots,a_n),\qquad q=\sum_i a_i,          \tag{2.3}
\]

whose job marginal, after the inverse map `z=(n-1)B+q`, is `Lambda_f`,
and whose aggregate endpoint marginal is `Lambda_g`.  Then
`f(x)dx` coagulates exactly into `g(y)dy`.

Conversely, within the canonical anchored uniform-layer ansatz, every
coagulation induces exactly such an endpoint-configuration measure.

### Proof

For each endpoint configuration, Theorem 1.1 gives a measurable uniform
joint mix of its anchored intervals.  Integrating those packet laws and
using the layer barycenter theorem gives the original job and socket
marginals.  The sum identity holds packetwise.  Conversely, record the
free endpoints of every anchored uniform packet. `square`

Thus the outer continuous joint-mixability problem has disappeared: the
only remaining object is an ordinary bounded composition of endpoint
sizes in `[0,B]`.

## 3. Scalar endpoint rows are automatic

Let `J=Lambda_f(1)` and `S=Lambda_g(1)`.  Suppose the arity assignment has

\[
 \int n\,d\Lambda_f=S.                            \tag{3.1}
\]

The original equal-work identity, expressed through layer midpoints, is

\[
 \int(B+z)\,d\Lambda_f
 =\int(a+B)\,d\Lambda_g.                          \tag{3.2}
\]

Since (3.1) gives

\[
 B\int(n-1)\,d\Lambda_f=B(S-J),
\]

subtracting this from (3.2) yields

\[
 \int\bigl(z-(n-1)B\bigr)\,d\Lambda_f
 =\int a\,d\Lambda_g.                            \tag{3.3}
\]

Hence the endpoint measures automatically have equal total size whenever
the outer count and work rows hold.  What remains is their configuration-
price/Hall system, not another moment identity.

## 4. Rayleigh scope

The first transformed Rayleigh job density `f_2=u'` is strictly decreasing
on `(b,infinity)`, so all of its canonical layers have the job form
`[b,z]`.  The socket density `g_2=-K'-u'`, however, satisfies

\[
 g_2'(b-)<0.
\]

Therefore it is not increasing.  Its canonical superlevel decomposition
has a positive-measure family of components whose right endpoint is
strictly below `b`; otherwise a barycenter of intervals `[a,b]` would be
nondecreasing.  These internal layers are the exact part not covered by
Theorem 2.1.

Consequently, the full Rayleigh layer route now separates into:

1. an anchored endpoint-composition bank, solved internally by Theorem 1.1
   once its endpoint configurations are found; and
2. a genuinely nonanchored cap bank requiring either mixed interval
   packets or a prior monotone-role decomposition.

The theorem does not solve the second bank.

## 5. Primary reference

The packet sufficiency uses the uniform-distribution case of the joint
mixability theorem of Bin Wang and Ruodu Wang, *Mathematics of Operations
Research* **41** (2016), 808--826, Theorem 3.2 and its uniform special
case: <https://www.math.uwaterloo.ca/~wang/papers/2015Wang-Wang-MOR.pdf>.

## 6. Frozen dependencies

1. `MATH_THEOREM_RAYLEIGH_UNIFORM_LAYER_PACKET_TRANSPORT_AND_EQUAL_SPLIT_GATE_20260805.md`,
   SHA at use
   `38cd384bfc1f92a3108204d5e5fb87507d991881cc2c911b583a099825e12784`.
2. `MATH_THEOREM_RAYLEIGH_FIRST_RESIDUAL_JOB_DENSITY_DECREASE_20260805.md`,
   SHA at use
   `a93f28d2364a84f4c4a5d3a1581c11c22419db3059ac8ea8fbbebf8684db5afa`.
3. `MATH_THEOREM_RAYLEIGH_FIRST_RESIDUAL_SOCKET_ENDPOINT_DECREASE_NOGO_20260805.md`,
   SHA at use
   `78e017354f77b21e6ba0c53301027e25cec3ffd020872727cbe9aab8802469c7`.
