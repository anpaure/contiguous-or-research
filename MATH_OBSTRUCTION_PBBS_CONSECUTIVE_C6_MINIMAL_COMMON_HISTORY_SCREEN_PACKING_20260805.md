# Consecutive PBBS C6s cannot all use the minimal two-set common-history lift

**Date:** 2026-08-05  
**Method:** exact sliding-window overlap count; no computation or search  
**Status:** unconditional obstruction to simultaneously planting the minimal
common-history decoration along a long consecutive sibling rail.  It does
not obstruct isolated or sufficiently separated decorated packets, nor a
different nonminimal/compound source realization.

## 1. Sliding source windows

Let

\[
                         A=(\ldots,A_j,A_{j+1},\ldots)
\]

be a source word whose depth-`d` owner row is

\[
                         T_j=\bigcup_{s=0}^{d}A_{j+s}.       \tag{1.1}
\]

The owner transition `T_j T_(j+1)` has left screen `A_j`, ordered history

\[
                         (A_{j+1},\ldots,A_{j+d}),           \tag{1.2}
\]

and right screen `A_(j+d+1)`.

For the minimal clean-C6 common-history lift, every screen is literally one
of

\[
 \{c,a_i\}\quad\hbox{or}\quad\{a_{i-1},a_i\},              \tag{1.3}
\]

and hence has cardinality two.  The history letters form a nonempty ordered
partition of the clean-C6 core `K`, so

\[
 \left|\bigcup_{s=1}^{d}A_{j+s}\right|=|K|=r-2.             \tag{1.4}
\]

## 2. Exact overlap obstruction

### Theorem 2.1 (length-`d+1` obstruction)

Suppose each of the `d+1` consecutive owner transitions

\[
 T_jT_{j+1},T_{j+1}T_{j+2},\ldots,T_{j+d}T_{j+d+1}         \tag{2.1}
\]

is the distinguished edge of a minimal two-set common-history clean-C6
decoration.  Then necessarily

\[
                         r-2\le2d.                           \tag{2.2}
\]

If the first packet uses the stipulated disjoint history partition and all
history letters are screens of later packets, equality holds:

\[
                         r-2=2d.                             \tag{2.3}
\]

#### Proof

For `s=1,...,d`, the source letter `A_(j+s)` is the left screen of the
`s`-th later transition in (2.1).  By (1.3),

\[
                         |A_{j+s}|=2.
\]

But these same `d` letters are precisely the complete history (1.2) of the
first decorated edge.  Therefore

\[
 r-2
 =\left|\bigcup_{s=1}^{d}A_{j+s}\right|
 \le\sum_{s=1}^{d}|A_{j+s}|=2d,
\]

proving (2.2).  Under the minimal theorem's disjoint-partition hypothesis,
the union size is the sum, proving (2.3).  \(\square\)

### Corollary 2.2 (asymptotic incompatibility)

Whenever

\[
                         r-2>2d,                            \tag{2.4}
\]

no source antecedent can simultaneously realize the minimal decoration on
`d+1` consecutive owner edges.  In the OR-word regime
`d=Theta(sqrt r)`, (2.4) holds for all sufficiently large `r`.

Thus a cool-lex/PBBS sibling chain containing a run of at least `d+1`
consecutive common-child edges cannot be made all-depth transparent by
independently stamping the minimal isolated-C6 packet on every edge.

## 3. What the obstruction does and does not say

The contradiction uses both defining features of the current lift:

1. each distinguished screen is a two-set; and
2. the `d` history letters must jointly carry an `(r-2)`-set core.

It does not rule out:

1. selecting only a `d`-separated subfamily of decorated edges;
2. grouping a long sibling run into one compound source macro;
3. a nonminimal screen carrying redundant core coordinates;
4. an overlapping common history rather than a disjoint partition; or
5. protecting the deeper rows by an exterior witness reservoir without
   realizing every C6 as an independent source fragment.

Items 3--4 are not automatic escapes.  Enlarging a screen changes the
short-cell deck and must be coordinated with the next sliding owner window;
the old proof of exact strict-lower transport cannot simply be cited without
a new literal common-history identity.

## 4. Revised PBBS interface

The all-lower-depth theorem remains exact for every **actually planted**
decorated C6 and for serial compositions in which each intermediate packet
exists literally.  The present theorem shows that global physical planting
is a substantive additional row for the long sibling contour.

The next viable objects are therefore:

1. a compound sibling-rail macro whose complete source deck telescopes as a
   whole; or
2. a sparse decorated connector skeleton, with the undecorated q1/q2 C6s
   discharged by a separately protected deeper-row reservoir.

No q3 defect is inferred for either alternative; only the naive overlapping
minimal decoration is excluded.
