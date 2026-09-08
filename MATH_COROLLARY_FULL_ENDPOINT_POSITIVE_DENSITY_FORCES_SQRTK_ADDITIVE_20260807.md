# Positive-density full endpoints force square-root additive overhead

**Date:** 2026-08-07  
**Method:** arbitrary-gap suffix overlap, the endpoint-interval lemma, and
greedy clustering  
**Status:** unconditional quantitative obstruction.  It strengthens the
fixed-additive full-endpoint no-go: any construction which uses a positive
density of full top-deep endpoints must have additive overhead
\(\Omega(d)=\Omega(\sqrt{k})\).  In particular no reset, toggle, puncture,
or bounded endpoint state can make the two-full-rail packet paradigm prove
\(B(k)+O(1)\).

## 1. Setup

Use the odd top-deep parameters

\[
 n=2m+1,\qquad s=m-2d,\qquad t=m-d,
 \qquad W={n\choose m}.
\]

Let a universal word have length

\[
                         N=W+d+C                         \tag{1.1}
\]

with \(C\ge0\).  An endpoint \(i\) is **full** when

\[
 \left|A_{i-j+1}\cup\cdots\cup A_i\right|=s+j-1
 \qquad(1\le j\le d).                                  \tag{1.2}
\]

Write \(E\) for the set of full endpoints.

## 2. The fixed-\(C\) density estimate

The arbitrary-gap overlap theorem in
`MATH_THEOREM_FIXED_ADDITIVE_FULL_ENDPOINT_DENSITY_NOGO_20260807.md`
proves, whenever \(0\le C\le d-2\), that

\[
 |E|\le (C+1)\left(1+\left\lfloor{N-1\over d}\right\rfloor\right).
                                                               \tag{2.1}
\]

For completeness, the only ingredients are the following.  If two full
endpoints are separated by \(g<d\), their two depth-\(d\) windows share a
full depth-\((d-g)\) suffix.  Consequently their complete span has rank at
most

\[
                         m-d+g-1.                         \tag{2.2}
\]

If \(C+1\le g\le d-1\), that span contains a length-\((d+C+1)\)
interval, but (2.2) bounds even the whole span by \(m-2\).  The
architecture-free endpoint-interval lemma requires every such interval to
have rank at least \(m\), a contradiction.  Thus two full endpoints are
either at distance at most \(C\), or at distance at least \(d\).  Greedy
clusters of diameter \(C\) have at most \(C+1\) integer positions and
their anchors are \(d\)-separated, giving (2.1).

## 3. Quantitative minimum additive cost

### Theorem 3.1

Fix \(\eta>0\).  Suppose that along an infinite sequence of dimensions a
universal word contains at least

\[
                         |E|\ge\eta W                     \tag{3.1}
\]

full endpoints.  Then

\[
                         \boxed{C=\Omega_\eta(d)}.        \tag{3.2}
\]

More precisely, either \(C\ge d-1\), or

\[
 C+1\ge {\eta Wd\over W+2d+C-1}
       =(\eta-o(1))d.                                    \tag{3.3}
\]

#### Proof

If \(C\ge d-1\), (3.2) is immediate.  Otherwise \(C\le d-2\), so
(2.1) applies.  Since

\[
 1+\left\lfloor{N-1\over d}\right\rfloor
 \le {N+d-1\over d}
 ={W+2d+C-1\over d},                                    \tag{3.4}
\]

equations (2.1) and (3.1) give the first inequality in (3.3).  In this
case \(C<d\), while \(d/W\to0\); hence its right side is
\((\eta-o(1))d\).  This proves (3.2). \(\square\)

At the optimal deadline,

\[
                         d=\Theta(\sqrt{k}),              \tag{3.5}
\]

so (3.2) is a square-root additive lower bound on this architecture.

## 4. Consequence for two-full-rail reset packets

A literal two-full-rail event has at least one distinguished full terminal
endpoint, and different physical events have different terminal positions.
Therefore a bank of \(H\) such events satisfies

\[
                         H\le |E|.                        \tag{4.1}
\]

If the theta reset ledger asks for

\[
                         H=(\theta+o(1))W,
 \qquad \theta>0,                                       \tag{4.2}
\]

Theorem 3.1 forces

\[
                         \boxed{C=\Omega(\theta d)}.      \tag{4.3}
\]

This conclusion is independent of how the packet records history.  It
therefore rules out all of the following as routes to fixed additive
overhead while preserving the two complete rails:

* bounded or \(O(d)\)-coordinate tag memories;
* zero-current tag swaps;
* alternating-polarity or toggle memories;
* punctured coordinates which leave the two endpoints full in the sense
  of (1.2);
* bounded extra endpoint states; and
* guarded adjacent-pair resets, even if the guard bank is perfectly
  recycled.

Those devices can evade tag-signature monotonicity, but they cannot evade
the architecture-free rank deficit in (2.2).

## 5. Exact surviving interfaces

The theorem does **not** rule out a construction in which the theta events
use any of the following:

1. partial endpoint chains rather than all depths \(1,\ldots,d\);
2. a distribution of depths or bottom ranks, so no positive-density class
   has the full profile (1.2);
3. nonflat middle ownership in which the relevant lower obligations are
   delivered by intervals not organized as full suffix endpoints; or
4. a global compiler rerouting which saves resets without creating one
   physical full endpoint per saving.

Thus the weakest viable replacement is not a more elaborate history state
for the old packet.  It must change the literal target interface itself.
The full two-rail chart bank remains a correct static target packing, but a
positive-density physical realization is incompatible with
\(B(k)+O(1)\).

