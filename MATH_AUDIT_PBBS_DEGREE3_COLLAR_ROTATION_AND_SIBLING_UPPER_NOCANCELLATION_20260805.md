# Audit of PBBS degree-three collar separation and sibling upper noncancellation

**Date:** 2026-08-05  
**Audited theorem:**
`MATH_THEOREM_PBBS_DEGREE3_COLLAR_ROTATION_AND_SIBLING_UPPER_NOCANCELLATION_20260805.md`  
**Status:** PASS within the theorem's stated aligned-lift scope

## 1. Collar arithmetic

For one packet the conservative collar is

\[
 [s-1,s+d+2].
\]

For forced consecutive anchors `t,t+1`, the union is

\[
 [t-1,t+d+3].
\]

The two intervals meet exactly when

\[
 t-d-3\le s\le t+d+4.
\]

The inclusive count is

\[
 (t+d+4)-(t-d-3)+1=2d+8.
\]

Thus the constant in Theorem 2.1 is correct.  The theorem uses a
conservative q2 halo; shrinking it is unnecessary.

## 2. Rotation injectivity

If a nonzero rotation fixes a rank-`m` owner on `2m+1` coordinates, that
owner is a union of orbits of a proper divisor of `2m+1`.  Its cardinality
would be divisible by that orbit length, impossible because
`gcd(m,2m+1)=1`.  If a rotation maps an unoriented edge to itself while
swapping endpoints, its action on that two-element endpoint set has order
two, impossible for an element of the odd-order rotation group.  Therefore
all `2m+1` rotated anchor edges are distinct.

An injective orbit map hits a forbidden edge set `B` at most `|B|` times.
This proves both the one-shore bound and the union bound in Corollary 2.2.

## 3. Interaction with the sibling overlap theorem

The pre-existing exact sibling theorem proves:

1. the forced pair's two shared-owner screens are disjoint;
2. the common body has rank `r-4`; and
3. `r-4>=d-1` is exactly the partitionability condition.

The new theorem does not redo or weaken that overlap.  It separates only
the optional third incidence.  Disjoint conservative collars make its
history and q2 halo independent, while the forced pair keeps its allowed
directed head-to-tail overlap.

## 4. Upper noncancellation

The private-prefix casualty has rank

\[
 |K|+4=(r-2)+4=r+2.
\]

A sibling pair shares only one component, so a role on either other shore
of the first packet is untouched by the second packet.  A private label
occurring only in that role prevents any signed occurrence from the second
displayed family from cancelling the first casualty.  This proves failure
of a context-free compound identity.  The theorem correctly leaves open an
alternative occurrence elsewhere in a completed global word.

## 5. Scope checks

The theorem does **not** infer:

- that arbitrary nonaligned antecedents inherit the same interval count;
- that all packet-tree rotations can be selected independently;
- that upper targets are globally missing;
- that a clipped upper reservoir is simultaneously plantable; or
- that typed common-cap routes transport.

These exclusions match the current research boundary.  Audit verdict:
PASS.
