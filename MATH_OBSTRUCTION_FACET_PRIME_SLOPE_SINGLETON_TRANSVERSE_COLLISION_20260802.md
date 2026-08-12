# Prime-slope frames can intersect in exactly one named resource

Date: 2026-08-02  
Status: unconditional obstruction to an overlap-multiplicity shortcut. It
does not refute the prime-slope frame-packing conjecture.

## 0. Outcome

Let `q` be sufficiently large and put

\[
 c=r-q+1.
\]

There are two legal prime-slope frames with the same `c`-core whose complete
owner/target resource decks intersect in exactly one resource, a target of
rank `c+4`.

Consequently, a collision between two prime-slope frames need not bring
`Omega(q)` (or even two) coincident resources. Any global frame-packing
argument must handle genuinely transverse singleton collisions; it cannot
recover the missing factor `q` merely by dividing the resource-incidence
union bound by a forced overlap multiplicity.

## 1. Choosing two frames with enough private room

Use Bertrand's theorem with `n=floor(q/4)`. For all sufficiently large
`q`, it gives a prime

\[
             q/4-1<p<q/2.
\]

Put

\[
       s=q-p,\qquad m=(p-1)/2.
\]

Then `p>3`, `s>=6`, and the hypotheses of the prime-slope frame theorem
hold. Fix one `c`-set `C`. A frame uses, outside `C`,

\[
       P=p+ms\le q+q^2/8
\]

coordinate names. In the canonical middle-level range,

\[
 k-c=(k-r)+q-1,
 \qquad q^2/r\longrightarrow\pi/4.
\]

Hence

\[
 k-c-(2P-4)
 \ge (k-r)-q-1-q^2/4+4>0
\]

for all sufficiently large `q`. We may therefore choose two frame supports
whose coordinates outside `C` meet in exactly one prescribed four-set

\[
                         J=\{1,2,3,4\}.
\]

In each frame put `J` inside the private set of one distinguished slope
module. All field coordinates, all other private coordinates, and all
private coordinates of the nondistinguished slope modules are disjoint
between the two frames.

## 2. The two orders have only the whole four-set in common

Place the elements of `J` consecutively in one occupied gap of the
distinguished arithmetic-progression cycle. Use the two linear orders

\[
                  1,2,3,4
       \qquad\hbox{and}\qquad
                  2,4,1,3.                              \tag{2.1}
\]

Their two-element interval sets are respectively

\[
 \{12,23,34\},\qquad \{24,14,13\},                     \tag{2.2}
\]

and their three-element interval sets are respectively

\[
 \{123,234\},\qquad \{124,134\}.                       \tag{2.3}
\]

The families in (2.2) are disjoint, as are those in (2.3). The whole set
`J` is an interval in both orders. Because the block is bounded on both
sides by coordinates outside `J`, a proper cyclic interval contained in
`J` is exactly a proper linear interval displayed in (2.2)--(2.3).

Choose `w` and `h` outside `J` and put them in two nonadjacent gaps of the
field cycle, as required by the prime-slope construction. The remaining
private tags may be inserted arbitrarily. Thus both completed objects are
legal prime-slope frames.

## 3. Exact intersection of the resource decks

Every high target of one module has the form

\[
                         C\cup A,                       \tag{3.1}
\]

where `A` is a cyclic interval in that module's tag order. If a target
from the first frame equals one from the second, removing their common core
`C` shows that the two tag intervals are equal. The two complete outside
supports meet only in `J`. Therefore the common interval must be contained
in `J`.

Equations (2.2)--(2.3) exclude every proper interval of size at least two;
the only remaining high target is

\[
                         C\cup J,                       \tag{3.2}
\]

at rank `c+4`. It occurs once in each distinguished module. Intervals
strictly larger than `J` contain a tag outside `J`, and those tags belong to
disjoint frame supports, so they cannot agree. Nondistinguished modules
contain no coordinate of `J` and cannot contribute another equality.

An owner has the form `C union (V-{v})`. Since `q-4>=2`, every owner of a
distinguished module retains a tag outside `J`; owners of nondistinguished
modules use only their frame's disjoint outside support. Hence no owner is
common to the two frames.

Finally, the rank-`c` and rank-`(c+1)` targets are

\[
                 (C-\{\beta\})+\{w\},
             \qquad C+\{h\}.
\]

Choose `w,h` from the disjoint outside supports (and use any legal
`beta in C`). These two low targets are distinct across the frames.
The prime-slope theorem already gives simplicity inside each frame.
Therefore

\[
 \boxed{
  \operatorname{Deck}({\cal F}_1)\cap
  \operatorname{Deck}({\cal F}_2)=\{C\cup J\}.
 }
\]

## 4. Scope

The construction refutes only the proposed *forced collision clustering*
shortcut. It does not show that a large frame packing is absent. A
positive proof may still split conflicts into clustered and transverse
classes, but its transverse class must include the literal singleton
configuration above and must be controlled by an interval-spread,
switching, absorption, or correlated-residual theorem rather than by
overlap multiplicity alone.

The local frame construction used here is
`MATH_THEOREM_FACET_PRIME_SLOPE_FRAME_Q_AMPLIFIER_20260802.md`.
