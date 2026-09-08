# Rayleigh residual threshold jobs admit an interior-spread two-piece packet

**Date:** 2026-08-05  
**Method:** pure mathematics; no computation, search, or solver  
**Status:** unconditional local construction.  A complete sufficiently
short band of jobs immediately above the first residual threshold can be
split into two sockets drawn from fixed compact subintervals of the physical
residual socket support.  The induced socket densities tend uniformly to
zero with the width of the job band.  Thus the small-origin obstruction to a
second equal-level subtraction is policy-specific: a non-equal-level packet
uses no sockets near the transformed origin.  This theorem does not
coagulate the remaining compact job bank.

## 1. A general interior-spread lemma

Let `B>0`.  Let

\[
 \mu(dx)=f(x)\mathbf 1_{[B,B+\varepsilon]}(x)\,dx
\]

be a finite job band, where `f` is bounded on a fixed right neighborhood of
`B`.  Let

\[
 \nu(dy)=g(y)\mathbf 1_{(0,B)}(y)\,dy,
\]

where `g` is continuous and strictly positive on `(0,B)`.

Fix once and for all

\[
 I=\left[{B\over4},{B\over3}\right],
 \qquad |I|={B\over12}.
\tag{1.1}
\]

For `0<\varepsilon<B/12`, put

\[
 J_\varepsilon
 =\left[{2B\over3},{3B\over4}+\varepsilon\right]
 \Subset(0,B).
\tag{1.2}
\]

### Theorem 1.1 (interior-spread two-piece packet)

There is `\varepsilon_0>0` such that, for every
`0<\varepsilon<=\varepsilon_0`, the complete job band `mu` has a literal
two-piece coagulation whose aggregate socket marginal is a submeasure of
`nu`.  Every first piece lies in `I`, every second piece lies in
`J_epsilon`, and hence every used socket stays a fixed positive distance
from zero.

### Proof

Conditioned on a job value `x`, choose `Y` uniformly on `I` and put

\[
                         Z=x-Y.                 \tag{1.3}
\]

Then `Y+Z=x` identically.  If `x in [B,B+epsilon]` and `Y in I`, then

\[
 {2B\over3}\le Z\le {3B\over4}+\varepsilon,
\]

so `Z in J_epsilon`.

Let `m_epsilon=mu([B,B+epsilon])`.  The first-piece occurrence density is

\[
 r_1(y)={m_\varepsilon\over |I|}\mathbf1_I(y).
\tag{1.4}
\]

The second-piece occurrence density is

\[
 r_2(z)={1\over |I|}
 \int_{[B,B+\varepsilon]\cap(z+I)} f(x)\,dx .
\tag{1.5}
\]

If `F` bounds `f` on `[B,B+B/12]`, then

\[
 0\le r_1\le {F\varepsilon\over |I|}\mathbf1_I,
 \qquad
 0\le r_2\le {F\varepsilon\over |I|}
              \mathbf1_{J_{B/12}}.              \tag{1.6}
\]

The fixed compact set

\[
 I\cup J_{B/12}
 \subseteq [B/4,5B/6]
\]

has a strictly positive socket-density floor

\[
 g_*:=\min_{[B/4,5B/6]}g>0.                     \tag{1.7}
\]

Choose

\[
 \varepsilon_0
 =\min\left\{{B\over12},{g_*|I|\over2F}\right\},
\tag{1.8}
\]

with the evident harmless convention if the job band is zero.  The two
support intervals in (1.1)--(1.2) are disjoint.  Therefore (1.6)--(1.8)
give

\[
                         r_1+r_2\le g.           \tag{1.9}
\]

Integrating the conditional packet (1.3) over `mu` proves the result.
`square`

## 2. Application to the first Rayleigh residual

After the first equal-level subtraction and cancellation, the residual
pair is

\[
 \mu_2(dx)=f_2(x)\mathbf1_{(b,\infty)}(x)\,dx,
 \qquad
 \nu_2(dy)=g_2(y)\mathbf1_{(0,b)}(y)\,dy,
\tag{2.1}
\]

where `f_2=u'` is continuous at and to the right of `b`, while

\[
                         g_2(y)>0\qquad(0<y<b).
\tag{2.2}
\]

Apply Theorem 1.1 with `B=b`, `f=f_2`, and `g=g_2`.

### Corollary 2.1

For some `epsilon_0>0`, every residual job in the complete band
`[b,b+epsilon]`, `0<epsilon<=epsilon_0`, can be removed by an explicit
two-piece kernel using a submeasure of the residual socket bank.  All used
sockets lie in

\[
 [b/4,b/3]\cup[2b/3,3b/4+\varepsilon]
 \subset(0,b).                                  \tag{2.3}
\]

After subtraction, the unused job and socket measures remain positive and
have equal first moments.

### Proof

Only the final sentence remains.  Every packet conserves work exactly, so
subtracting its job and socket marginals preserves equality of the two
remaining first moments. `square`

## 3. Exact relation to the second equal-level no-go

The repeated equal-level policy creates a new remainder density with a
positive limit at zero, while its unused socket cumulative mass at zero is
only `o(t)`.  That proves that the **repeated equal-level remainder** cannot
be coagulated.

Corollary 2.1 proves a complementary positive statement.  A whole
positive-density job band adjacent to `b` can instead be handled without
creating any remainder at all and without using any socket in
`(0,b/4)`.  Hence no intrinsic local shortage at the transformed origin is
forced by the Rayleigh marginals.  The shortage is caused by matching a
near-`b` job to a near-`b` first socket.

This does not solve the compact remainder: the theorem spends only
`O(epsilon)` interior socket mass and says nothing about simultaneously
packing all job bands or exhausting the remaining socket marginal.  Its
proof-safe consequence is narrower:

\[
 \boxed{
 \text{the final compact construction may quarantine a full threshold
 job collar while keeping a neighborhood of zero untouched.}
 }
\tag{3.1}
\]

## 4. Dependencies

1. `MATH_THEOREM_RAYLEIGH_ONE_SHOT_NORMALIZATION_GAUSSIAN_TAIL_AND_COMPACT_REMAINDER_20260805.md`;
2. `MATH_THEOREM_RAYLEIGH_EQUAL_LEVEL_ONE_WELL_REGENERATION_20260805.md`;
3. `MATH_THEOREM_RAYLEIGH_REPEATED_EQUAL_LEVEL_SECOND_STAGE_PREFIX_HALL_NOGO_20260805.md`.
