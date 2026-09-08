# Complementary seam rectangles: a near-once linear-depth portal core

## 1. Outcome

Put

\[
 P_m=[0,m]^4,\qquad R=2m-1,\qquad
 L_R=\{x\in P_m:|x|=R\}.
\]

The raw rectangle calculation in `LEX_FACTOR_ITERATION.md` can be turned
into a genuine, ordered, near-once construction at a positive linear
depth.  The result below is deliberately scoped to the targets which are
missed by **both** complementary complete-line systems.  This is the hard
boundary family which actually needs mixed seams.

### Theorem 1 (linear-depth complementary portal core)

Let

\[
             1\le q\le \left\lfloor {m\over3}\right\rfloor .          \tag{1.1}
\]

There is an explicit word (W_{m,q}), all of whose letters belong to
(L_R), with the following properties.

1. Every point of (L_R) occurs at least once and at most twice.
2. The exact length is
   \[
       |W_{m,q}|=|L_R|+4q(q-1).                       \tag{1.2}
   \]
   Thus only (O(m^2)=o(|L_R|)) occurrences are repeated, even when
   (q=\lfloor\alpha m\rfloor) for fixed (0<\alpha<1/3).
3. For every (1\le s\le q), every (y\in L_{R+s}) satisfying
   \[
       \min(y_1,y_2)<s,\qquad \min(y_3,y_4)<s          \tag{1.3}
   \]
   is the maximum of a contiguous interval of (W_{m,q}).
4. The selected witness for such a (y) has exactly (s+1) letters.  It
   is a suffix of one coordinate-({1,2}) segment followed by a prefix
   of one coordinate-({3,4}) segment.
5. The nontrivial portal part of the word alternates
   ({1,2})- and ({3,4})-segments.  Every window internal to one
   segment retains the exact line sliding equation: a window of (ell)
   consecutive rank-(R) letters has maximum rank (R+ell-1).

Since

\[
 |L_{2m-1}|=M_m-(m+1),\qquad
 M_m={2m^3+6m^2+7m+3\over3},                       \tag{1.4}
\]

the construction has length (M_m+O(m^2)).  In particular, the seam
rectangles themselves do **not** encounter a counting or physical-order
barrier at linear depth.

The theorem is not yet a word for the whole upper band.  Targets for which
one of the two inequalities in (1.3) fails have a complete-line witness,
but extracting the portal arms can cut that witness.  Sections 7--9 isolate
the exact remaining compatibility problem.

## 2. Complete-line criterion

For a target (y\in L_{R+s}), a coordinate-({1,2}) rank-(R) line
contains a witnessing interval if and only if

\[
                         y_1,y_2\ge s.                \tag{2.1}
\]

Indeed, the endpoints are (y-se_1) and (y-se_2).  The same argument
for the complementary direction gives the criterion

\[
                         y_3,y_4\ge s.                \tag{2.2}
\]

Hence (1.3) is exactly the family missed by both complete-line systems.
It is not an artificially enlarged exception set.

Under (1.1), every pair of coordinates of a target in (1.3) has exactly
one coordinate below (s).  If, for example, both (y_1,y_2<s), then
one of (y_3,y_4) is also below (s), and

\[
 |y|\le (2s-2)+(m+s-1)=m+3s-3<2m-1+s,
\]

a contradiction.  Thus, after independently swapping coordinates 1 and 2
and coordinates 3 and 4, every hard target has a unique form

\[
                     y=(m-A,a,m-B,b),                \tag{2.3}
\]

where

\[
 0\le a,b\le s-1,qquad A,B\ge0.                     \tag{2.4}
\]

The rank equation is

\[
                 A+B=a+b-s+1.                        \tag{2.5}
\]

Put (delta=A+B).  Equation (2.5) and (2.4) imply

\[
       0\le\delta\le s-1,qquad
       A,B\le\delta\le a,b.                         \tag{2.6}
\]

The last pair of inequalities is the fact which makes a near-disjoint
portal packing possible.

For reference, the number of hard targets at exact depth (s) is

\[
                         4\binom{s+2}{3},             \tag{2.7}
\]

and through depth (q) it is

\[
                         4\binom{q+3}{4}.             \tag{2.8}
\]

Thus the theorem covers a genuine (Theta(q^4)) family with a
near-Hamilton rank-(R) word.

## 3. One swapped-baseline portal

Fix (A,B\ge0) with

\[
                         A+B\le q-1.                  \tag{3.1}
\]

Define a coordinate-({1,2}) arm

\[
 X_u=(m-A-u,\ B+u,\ m-B-1,\ A),
 \qquad 0\le u\le q-1-B,                              \tag{3.2}
\]

and a coordinate-({3,4}) arm

\[
 Y_v=(m-A-1,\ B,\ m-B-v,\ A+v),
 \qquad 0\le v\le q-1-A.                              \tag{3.3}
\]

Every displayed coordinate lies in ([0,m]) under (1.1), and

\[
                         |X_u|=|Y_v|=2m-1.             \tag{3.4}
\]

Use the physical block

\[
 X_{q-1-B},X_{q-2-B},\ldots,X_0,
 Y_0,Y_1,\ldots,Y_{q-1-A}.                             \tag{3.5}
\]

For every legal (u,v), the interval from (X_u) through (Y_v) has
maximum

\[
              (m-A,\ B+u,\ m-B,\ A+v).               \tag{3.6}
\]

This is an exact physical suffix--prefix rectangle, not a capacity count.
The first arm is traversed toward (X_0); the second is traversed away
from (Y_0).  Their seam edge has maximum

\[
                    X_0\vee Y_0=(m-A,B,m-B,A)          \tag{3.7}
\]

of rank (R+1).

The choice of baseline ((B,A)), rather than ((A+B,0)), is the key.
It spreads different portal arms through the three-dimensional base layer
instead of nesting all of them on the same few lines.

## 4. Coverage of the hard family

Take (y) in the normal form (2.3) and put

\[
                         u=a-B,\qquad v=b-A.           \tag{4.1}
\]

By (2.6), these are nonnegative.  Also

\[
 u\le q-1-B,\qquad v\le q-1-A,                        \tag{4.2}
\]

and

\[
                         u+v=s-1.                     \tag{4.3}
\]

Substitution in (3.6) gives exactly (y).  The physical witness contains

\[
                         (u+1)+(v+1)=s+1              \tag{4.4}
\]

letters.  Applying the two independent coordinate swaps gives the other
three orientations in (2.3), proving the coverage claim in Theorem 1.

Notice that (4.4) is the same length as an intact line witness.  The seam
does not pay a longer-window penalty.

## 5. Near-disjointness of all portal arms

First fix one of the four coordinate orientations.

Two (X)-letters are equal only when all of (A,B,u) agree: coordinates
4 and 3 recover (A) and (B), and then coordinate 2 recovers (u).
Similarly, all (Y)-letters are distinct.

If

\[
                         X_u(A,B)=Y_v(A',B'),           \tag{5.1}
\]

then comparison of the four coordinates gives

\[
 A'=A+u-1,\qquad B'=B+u,\qquad u+v=1.                 \tag{5.2}
\]

Thus the only overlaps are

\[
 (u,v)=(0,1)\quad\hbox{or}\quad(1,0).                 \tag{5.3}
\]

There are exactly

\[
 {q(q-1)\over2}+{q(q-1)\over2}=q(q-1)                \tag{5.4}
\]

such repeated points in one orientation.  No point occurs more than once
as an (X)-letter or more than once as a (Y)-letter, so its total
multiplicity is at most two.

The four coordinate orientations are disjoint.  Indeed, in each coordinate
pair every portal letter has its designated low coordinate at most (q-1),
whereas its designated high coordinate is at least

\[
                         m-2q+2>q-1.                  \tag{5.5}
\]

Hence the location of the high coordinate in each pair is recoverable from
the point itself.

The total number of portal occurrences is

\[
\begin{aligned}
 P_q
  &=4\sum_{\delta=0}^{q-1}(\delta+1)(2q-\delta)\\
  &=\boxed{{4q(q+1)(2q+1)\over3}}.                    \tag{5.6}
\end{aligned}
\]

The number of distinct portal points is

\[
                         P_q-4q(q-1).                 \tag{5.7}
\]

Concatenate the blocks (3.5) in any fixed order, for all (A,B) and all
four orientations.  Then append every base-layer point not already used,
once.  Equation (5.7) gives the exact total length (1.2).  The appended
points may be regarded as alternating singleton segments, so they do not
change the nontrivial segment statement.

This completes the proof of Theorem 1.

## 6. Exact sliding equations

The portal construction preserves more than the target values used in the
proof.  Along an (X)-arm, for (u_0\le u_1), the maximum of the
corresponding contiguous line interval is

\[
 (m-A-u_0,\ B+u_1,\ m-B-1,\ A),                     \tag{6.1}
\]

and its rank is (R+(u_1-u_0)).  The analogous formula along a (Y)-arm
is

\[
 (m-A-1,\ B,\ m-B-v_0,\ A+v_1).                    \tag{6.2}
\]

Thus every internal sliding window has precisely the expected erosion/join
rank.  Across the distinguished seam, equation (3.6) is the full Cartesian
product of the two arm parameters.  No separator, literal upper target, or
non-rank-(R) letter is hidden in the construction.

## 7. Why this does not yet cover the whole band

Theorem 1 settles the portal geometry for the family which cannot be served
by either complementary line direction.  It does not prove that all the
other line witnesses survive after the arms are extracted and moved.

A useful exact way to see the remaining issue is to put

\[
 a=\min(y_1,y_2),\qquad b=\min(y_3,y_4).             \tag{7.1}
\]

Consider the natural min-comparison refinement of the base layer: use
coordinate-{1,2} segments where the second-pair minimum is no larger than
the first-pair minimum, and use coordinate-{3,4} segments where the
first-pair minimum is no larger than the second-pair minimum.  Points on
the equality surface may be retained in both systems.  That surface has
only O(m^2) points, so this duplication is compatible with a near-once
word and removes an irrelevant tie convention.

The complete ({1,2})-witness for (y) stays entirely on its preferred
side whenever

\[
                         b\le a-s,                    \tag{7.2}
\]

and the complementary witness stays on its preferred side whenever

\[
                         a\le b-s.                    \tag{7.3}
\]

Therefore only the tie strip

\[
                         |a-b|<s                      \tag{7.4}
\]

needs a mixed-seam replacement in this partition.  This is much larger
than (1.3), but it still has an exact one-rectangle description.

Write a target in one chosen high/low orientation as

\[
                         y=(m-A,a,m-B,b)              \tag{7.5}
\]

and again put

\[
                         \delta=A+B=a+b-s+1.          \tag{7.6}
\]

Condition (7.4) implies

\[
 a,b\ge\left\lceil{\delta\over2}\right\rceil.        \tag{7.7}
\]

Indeed, if (a\le b), then (b-a<s=a+b-\delta+1)
gives (delta\le2a), and the other case is symmetric.

Set

\[
 c=\left\lfloor{\delta\over2}\right\rfloor,
 \qquad d=\left\lceil{\delta\over2}\right\rceil.     \tag{7.8}
\]

The seam with central endpoints

\[
 (m-A,c,m-B-1,d),\qquad(m-A-1,c,m-B,d)               \tag{7.9}

and the corresponding two line arms covers (y) with parameters

\[
                         u=a-c,\qquad v=b-d.           \tag{7.10}
\]

They are nonnegative and satisfy (u+v=s-1).  Thus the min-comparison
partition reduces the entire missing family to a **balanced seam
catalogue**, one seam label for each pair ((A,B)), not one seam for each
target.

There is a further encouraging incidence fact.  In one fixed coordinate
orientation, the ({1,2})-line used by (7.9) is labelled by

\[
                         (m-B-1,d).                   \tag{7.11}

For fixed (B,d), the value (delta) is only (2d) or (2d-1), so
at most two seam labels request that line.  Similarly, a fixed
({3,4})-line is requested by at most two labels.  The oriented
line-demand graph of the balanced catalogue therefore has maximum degree
two and is a union of paths and cycles.

This is the most concrete route to completing the construction: realize
those demand paths as one physical alternating braid, while assigning the
two possible requests on a line to opposite usable ends.

## 8. The baseline-order problem which remains

The maximum-degree-two statement above uses the canonical choice

\[
 (c,d)=(\lfloor\delta/2\rfloor,\lceil\delta/2\rceil).
\]

It is not automatically preserved when the odd baselines are changed.  For
even `(delta=2r)`, the balanced baseline is forced to be `((r,r))`.  For
odd `(delta=2r+1)`, either balanced choice is locally possible:

\[
                         (r,r+1)\quad\hbox{or}\quad(r+1,r).             \tag{8.1}

However, an arbitrary collection of the odd reversals in (8.1) can raise a
physical line's demand degree from two to three.  Conversely, at the
boundary of the demanded catalogue an odd seam need not share a requested
line with any demanded even seam.  Thus neither a universal degree-two
graph for all choices nor a universal odd/even collision is available.

For the canonical choice, the demand graph is still a union of paths and
cycles.  Some adjacent even/odd requests point into the same part of their
shared line and can overlap in `Theta(q)` points, but the number and global
distribution of those collisions have not been proved to be
`Theta(qm^2)`.  That scale is motivation, not a lower bound.

The missing lemma is therefore not a rectangle-counting statement.  It is
the following ordered parity problem.

> **Balanced line-demand braid.**  Choose baselines (or retain the canonical
> ones) so that the resulting bounded-degree line-demand graph can be cut
> and oriented, and place its requested arms so that every physical base
> point is used once apart from `o(m^3)` seam corners, while the preferred
> intact-line intervals (7.2)--(7.3) remain contiguous.

Theorem 1 proves this lemma on the smaller doubly-missed family by the
swapped baseline ((B,A)).  Extending it to the balanced tie catalogue is
the exact remaining all-band step.

## 9. Audit and status

The following points were checked explicitly in the proof and by
`scratch/verify_complementary_seam_rectangles.py`.

* Every portal letter has rank exactly (2m-1) and lies in the box.
* Formula (3.6) is the maximum of the stated **contiguous physical
  interval**, with the displayed word order.
* Every target in (1.3) has exactly one high/low orientation under (1.1),
  and equations (4.1)--(4.3) place it in a legal portal rectangle.
* The hard witness length is exactly (s+1), not merely (O(q)).
* Same-type portal letters never collide.  Cross-type collisions are
  exactly (5.2)--(5.3), giving exactly (4q(q-1)) repeated occurrences.
* The four orientation classes are disjoint because of the quantitative
  gap (5.5).
* The theorem remains a statement about the upper band over the
  rank-(2m-1) spine.  It does not provide the lower variable factor or
  coordinate pinning required for a full four-box universal word.
* Appending unused base points proves base-layer coverage and the exact
  near-once length.  It does **not** prove that every easy complete-line
  witness remains contiguous.  No such claim is made.
* The bound (q\le m/3) is used both to make the high/low orientation
  unique for hard targets and to separate the four physical portal
  regions.  The local formula (3.6) exists more broadly, but the proved
  near-disjoint packing does not.

Thus this note gives a genuine positive linear-depth portal theorem and
removes the raw-capacity ambiguity from Section 7 of
`LEX_FACTOR_ITERATION.md`.  For the canonical balanced catalogue the
unsolved part is a degree-two physical line-demand braid; allowing odd
baseline reversals gives a closely related bounded-degree choice problem.
In either form it is far more structured than an unorganized
four-dimensional rectangle cover.
