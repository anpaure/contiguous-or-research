# The cool-lex adjacent-root contour has an infinite deficiency-two obstruction

**Date:** 2026-08-05  
**Method:** orbit types and parity; no search  
**Status:** unconditional obstruction to the canonical contour matching
route.  It does **not** obstruct a matching in the full adjacent-transfer
necklace graph.

## 1. Setup

Let

\[
 q=2h-1\geq 5
\]

be odd, and let \(G_{q,4}\) be the graph of cyclic weak compositions of
mass four in \(q\) slots, with an edge for moving one unit between cyclically
adjacent slots.

At the top fixed-content necklace call, the root is the concentrated
necklace and the three nontrivial child blocks will be denoted
\(B_1,B_2,B_3\).  In the standard binary encoding, \(B_i\) is the call with
fixed suffix \(01^i\).  Equivalently, it consists of those composition
necklaces whose lexicographically least rotation ends in the part \(i\).

The adjacent-root contour has block order

\[
             R-B_3-B_2-B_1,                         \tag{1.1}
\]

where \(R\) is the singleton concentrated root.

## 2. Exact child cardinalities

Put \(m=h-2\), so that \(q-3=2m\), and define

\[
 T(m)=\#\{(a,b,c)\in\mathbb Z_{\geq0}^3:
                   a+b+c=2m,\ a\geq b,\ a\geq c\}. \tag{2.1}
\]

### Theorem 2.1

The three top-child sizes are

\[
\begin{aligned}
 |B_3|&=h-1,\\
 |B_2|&=h-1+T(m),\\
 |B_1|&=h-1+\binom{q-1}{2}-T(m)+{1\over q}\binom q4.
                                                        \tag{2.2}
\end{aligned}
\]

Moreover, writing \(m=3u,3u+1,3u+2\), respectively,

\[
 T(m)=
 \begin{cases}
  6u^2+4u+1,&m=3u,\\
  6u^2+8u+3,&m=3u+1,\\
  6(u+1)^2,&m=3u+2.
 \end{cases}                                           \tag{2.3}
\]

#### Proof

Classify a mass-four necklace by its multiset of positive parts.

* For type \(3+1\), the two zero gaps have total \(q-2=2h-3\),
  which is odd.  The least rotation starts in the longer gap.  Exactly
  \(h-1\) orientations end in the part 3 and exactly \(h-1\) end in the
  part 1.
* For type \(2+2\), exchanging the two equal occupied sites identifies
  the two gap orientations.  There are \((q-1)/2=h-1\) necklaces, and
  every least rotation ends in 2.
* For type \(2+1+1\), anchor the unique part 2 and let \(a,b,c\) be the
  zero-gap lengths after the 2 and after the two successive 1s.  Then
  \(a+b+c=q-3=2m\).  The least rotation ends in 2 exactly when
  \(a\geq b,c\).  This includes ties: if \(a=b\geq c\), the rotation
  after the \(a\)-gap wins at the next zero run; if \(a=c\geq b\), it
  wins already because its next positive part is 1 rather than 2; and
  the all-equal case follows from the same comparison.  Thus exactly
  \(T(m)\) of these necklaces lie in \(B_2\), and the remaining
  \(\binom{q-1}{2}-T(m)\) lie in \(B_1\).
* Type \(1+1+1+1\) always lies in \(B_1\).  Since \(q\) is odd,
  \(\gcd(q,4)=1\), so all such four-subset orbits have size \(q\) and
  their number is \(q^{-1}\binom q4\).

This proves (2.2).

For (2.3), sum first over the largest coordinate \(a\).  For
\(\lceil2m/3\rceil\leq a<m\), the number of possible \(b\)'s is
\(3a-2m+1\); for \(m\leq a\leq2m\), it is \(2m-a+1\).  Hence

\[
 T(m)=
 \sum_{a=\lceil2m/3\rceil}^{m-1}(3a-2m+1)
 +\sum_{a=m}^{2m}(2m-a+1),                            \tag{2.4}
\]

and the three elementary evaluations in (2.3) follow. \(\square\)

## 3. Infinite contour obstruction

### Theorem 3.1

If

\[
                    h\equiv3\text{ or }11\pmod {12}, \tag{3.1}
\]

equivalently

\[
                    q\equiv5\text{ or }21\pmod {24}, \tag{3.2}
\]

then

\[
                 |B_1|\equiv0,\qquad
                 |B_2|\equiv1,\qquad
                 |B_3|\equiv0\pmod2.                \tag{3.3}
\]

Consequently the canonical recursive contour graph on (1.1) has no
perfect matching.  Its matching deficiency is at least two.  In
particular, the proposed universal bound

\[
                         \mu_{\rm contour}\leq1       \tag{3.4}
\]

is false for infinitely many odd \(q\).

#### Proof

Under (3.1), \(h\) is odd, so \(h-1\) and
\(\binom{q-1}{2}=(h-1)(2h-3)\) are even.  Also
\(m=h-2\) is congruent to 1 or 0 modulo 3, so (2.3) says that \(T(m)\)
is odd.  Finally

\[
 {1\over q}\binom q4
 ={(h-1)(h-2)(2h-3)\over6}                           \tag{3.5}
\]

is odd exactly when \(h\equiv3\pmod4\), which holds in both residue
classes in (3.1).  Substitution in (2.2) gives (3.3).

The total number of vertices in (1.1) is even: the singleton root and
the odd block \(B_2\) contribute the two odd summands.  Suppose a perfect
matching of the contour existed.  The singleton root would have to use
its only contour edge, to the distinguished root of \(B_3\).  But
\(|B_3|\) is even, so deleting that distinguished root leaves an odd
number of vertices inside \(B_3\); no matching internal to \(B_3\) can
saturate them.  The same distinguished root cannot use both contour
edges.  This contradiction proves that no perfect matching exists.
Since the total order is even, every matching deficiency is even, hence
at least two. \(\square\)

## 4. The obstruction is only to the contour

For \((q,b)=(5,4)\), the formulas give

\[
                    (|B_1|,|B_2|,|B_3|)=(6,5,2).     \tag{4.1}
\]

Nevertheless the full adjacent-transfer graph has a perfect matching.
Using lexicographically least representatives, one is

\[
\begin{array}{rcl}
(0,0,0,0,4)&--&(0,0,0,3,1),\\
(0,0,1,0,3)&--&(0,0,0,1,3),\\
(0,0,3,0,1)&--&(0,1,0,1,2),\\
(0,0,0,2,2)&--&(0,0,2,1,1),\\
(0,0,2,0,2)&--&(0,1,1,0,2),\\
(0,1,0,2,1)&--&(0,1,1,1,1),\\
(0,0,1,1,2)&--&(0,0,1,2,1).
\end{array}                                           \tag{4.2}
\]

Each row differs by one cyclic adjacent unit transfer after a possible
rotation.  Thus (4.2) also pinpoints the missing resource: cross-block
adjacent edges, not a different matching state inside the same contour.

## 5. Consequence

The first-inversion/cool-lex contour remains a useful subcubic spanning
tree and its two-state matching recurrence remains exact.  What fails is
the hoped-for scalar bound on that particular spanning subgraph.

The full hook matching theorem is still open.  Any proof must use at
least one of:

1. noncontour adjacent-transfer edges joining recursive blocks;
2. a different recursively regenerated contour; or
3. bounded parity sockets exported between hook chip levels.

No obstruction to a near-perfect matching of the full graph
\(G_{q,b}\) is claimed here.
