# Multilayer extensions and barriers for the four-box line word

## 1. Summary

Put

\[
 P_m=[0,m]^4,\qquad R=2m-1,
\]

and let

\[
 M_m=\#\{x\in P_m:|x|=2m\}
     ={2\over3}m^3+2m^2+{7\over3}m+1.
\]

The direct coordinate-\(\{1,2\}\) line word has exact length

\[
 N_0=M_m+(m+1)^2-1=M_m+m^2+2m.                 \tag{1.1}
\]

Its letters are all rank-\(R\) points, grouped into their complete
coordinate-\(\{1,2\}\) lines, followed by the missing rank-\(2m\)
points literally.  The note `FOUR_BOX_DIRECT_LINE_WORD.md` proves that it
covers the rank-\(R\) and rank-\(2m\) layers and classifies all of its
within-line upper witnesses.

This note gives three further conclusions.

1. **Positive shallow extension.**  For every \(q\le m\), one can append
   three-box slice words and cover every target of ranks
   \(R,R+1,\ldots,R+q\) in length
   \[
      N_0+2q(m+1)(2m+1).                            \tag{1.2}
   \]
   Hence every upper band of depth \(q=o(m)\) has a
   \(M_m+o(m^3)\) construction.  This improves the literal-exception
   range \(q=o(\sqrt m)\) to the full sublinear range.

2. **Orientation-independent hard bulk.**  Even if all six coordinate-pair
   orientations are available for free, the targets which are not maxima
   of an interval in any rank-\(R\) coordinate-pair line number
   \[
                  {1\over12}m^4+O(m^3).             \tag{1.3}
   \]
   Thus changing line orientations cannot by itself solve the upper half.
   If witnesses are restricted to one line or two consecutive intact lines,
   a positive proportion of all \(\Theta(m^2)\) seams must be genuinely
   mixed-orientation seams.  In fact the literal fixed-pair word, including
   its appended middle exceptions, still misses
   \((1/72)m^4-O(m^3)\) upper targets.

3. **Uniform-factor obstruction.**  Every seam between two nontrivial
   intact lines in the same coordinate pair creates an internal coordinate
   atom run of length at most two.  Consequently the direct fixed-pair line
   word is not \(D^d\)-factorable for any \(d\ge2\).  On the other hand,
   interval counting shows that a uniform factor capable of carrying the
   whole lower half would require
   \[
                          d\ge(3/4-o(1))m.           \tag{1.4}
   \]
   A successful use of the line word therefore has to be a genuinely
   variable-band construction, with pervasive direction changes or
   nonlocal portal transport.  A fixed erosion and a bounded number of
   switches cannot be the missing bridge.

The results do not yet give a full word for \(P_m\), but they sharply
separate what the line word already accomplishes from the two mechanisms a
full construction must add.

## 2. A sublinear-depth upper band

For a target \(y\in P_m\) of rank

\[
                         |y|=R+s,\qquad s\ge0,       \tag{2.1}
\]

the exact within-line criterion for the coordinate pair \(\{1,2\}\) is

\[
                         y_1\ge s,\qquad y_2\ge s.  \tag{2.2}
\]

We use the standard three-chain hook construction in each missing
coordinate slice.  A nonzero universal word for \([0,m]^3\) has length at
most

\[
                         (m+1)(2m+1)-1.              \tag{2.3}
\]

If a fixed positive coordinate is attached to every letter, the local zero
point also becomes a required nonzero target.  Adding it costs one position.
Thus every fixed-coordinate slice has a word of length at most

\[
                         G_m=(m+1)(2m+1)             \tag{2.4}
\]

covering all of that slice.  For the zero slice the last position is not
needed, but the uniform upper bound (2.4) is convenient.

### Theorem 2.1 (sublinear upper-band extension)

For every integer \(0\le q\le m\), there is a word of length at most

\[
                  M_m+m^2+2m+2q(m+1)(2m+1)          \tag{2.5}
\]

which covers every target of ranks \(R,R+1,\ldots,R+q\).

### Proof

Start with the direct line word.  For every \(a=0,\ldots,q-1\), append a
copy of a three-box word in the slice \(x_1=a\), and another copy in the
slice \(x_2=a\).

Let \(y\) have rank \(R+s\), where \(0\le s\le q\).  If both
\(y_1,y_2\ge s\), (2.2) gives a witness in the line word.  Otherwise one of
\(y_1,y_2\) is strictly below \(s\), and hence belongs to
\(\{0,\ldots,q-1\}\).  The corresponding fixed-coordinate slice word
covers \(y\).  There are \(2q\) appended words, each of length at most
\(G_m\), proving (2.5).  \(\square\)

### Corollary 2.2

If \(q=q(m)=o(m)\), then all ranks from \(2m-1\) through
\(2m-1+q\) are covered in length

\[
                          M_m+o(m^3).                \tag{2.6}
\]

The construction is deliberately simple.  It shows that boundary slices
are sufficient throughout every sublinear upper band.  It also locates the
real difficulty at linear depth, where independent three-box slices cost
\(\Theta(m^3)\).

## 3. Which targets can any pair line cover?

Fix a coordinate pair \(\{i,j\}\).  A complete rank-\(R\) line in this
direction fixes the other two coordinates and transfers one unit at a time
between coordinates \(i\) and \(j\).

### Lemma 3.1 (orientation-free pair criterion)

Let \(y\in P_m\) have rank \(R+s\), \(s\ge0\).  It is the maximum of a
contiguous segment in some rank-\(R\) coordinate-\(\{i,j\}\) line if and
only if

\[
                              y_i,y_j\ge s.           \tag{3.1}
\]

### Proof

If (3.1) holds, the two endpoints

\[
                           y-se_i,\qquad y-se_j       \tag{3.2}
\]

have rank \(R\), lie on the same coordinate-\(\{i,j\}\) line, and the
maximum of the line segment between them is \(y\).

Conversely, a segment of span \(s\) in such a line raises both endpoint
coordinates by \(s\) when their coordinatewise maximum is taken.  Its
maximum therefore has both varying coordinates at least \(s\).  \(\square\)

It follows that a target is unavailable in **every** one of the six
directions precisely when at most one of its four coordinates is at least
its excess \(s\).

Define the hard upper family

\[
 \mathcal H_m=
 \{y\in P_m: s=|y|-R\ge0,\ 
                  \#\{i:y_i\ge s\}\le1\}.          \tag{3.3}
\]

### Theorem 3.2 (hard-bulk constant)

\[
                         |\mathcal H_m|
                            ={1\over12}m^4+O(m^3).   \tag{3.4}
\]

### Proof

Put \(u_i=m-y_i\) and \(U=\sum_i u_i\).  Since

\[
                         s=2m+1-U,                   \tag{3.5}
\]

the inequality \(y_i\ge s\) is equivalent to

\[
                         U-u_i\ge m+1.               \tag{3.6}
\]

Sort the deficits as

\[
                         u_1\le u_2\le u_3\le u_4.
\]

At most one of the four triple sums \(U-u_i\) is at least \(m+1\) if and
only if the second largest is at most \(m\), namely

\[
                         u_1+u_3+u_4\le m.           \tag{3.7}
\]

Condition (3.7) already implies \(s\ge0\).  After scaling by \(m\), ties
and boundary lattice points contribute only \(O(m^3)\).  The leading volume
is 24 times the ordered-region volume

\[
\begin{aligned}
 &\int_0^{1/3}\int_{u_1}^{(1-u_1)/2}
       \int_{u_3}^{1-u_1-u_3}\int_{u_1}^{u_3}
             du_2\,du_4\,du_3\,du_1\\
 &\qquad=
 \int_0^{1/3}\int_{u_1}^{(1-u_1)/2}
       (u_3-u_1)(1-u_1-2u_3)\,du_3\,du_1
 ={1\over288}.
\end{aligned}                                       \tag{3.8}
\]

Multiplication by \(4!=24\) gives \(1/12\).  Standard lattice-point
approximation for this fixed rational polytope proves (3.4).  \(\square\)

Thus even the union of all six ideal line systems misses a positive-volume
family.  Orientation selection can redistribute the easy \(5/12\) of the
upper box, but it cannot touch the last \(1/12\) without witnesses crossing
line boundaries.

## 3.5 Complementary-pair fibre tilings do not gain volume

There is a second obstruction to the most natural varying-orientation rule.
Suppose the rank-\(R\) layer is partitioned into complete lines using only
the complementary directions \(\{1,2\}\) and \(\{3,4\}\).

Fix

\[
                              q=x_3+x_4.             \tag{3.9}
\]

The corresponding slice of the rank-\(R\) layer is the Cartesian grid

\[
 A_q\times B_q,
\]

where \(A_q\) is the set of pairs \((x_1,x_2)\) of sum \(R-q\), and
\(B_q\) is the set of pairs \((x_3,x_4)\) of sum \(q\).  A complete
\(\{1,2\}\)-line is a whole row of this grid, and a complete
\(\{3,4\}\)-line is a whole column.

### Lemma 3.3 (slice rigidity)

In a disjoint partition of \(A_q\times B_q\) into complete rows and complete
columns, every selected line has the same orientation.

### Proof

Every complete row meets every complete column.  Hence a disjoint partition
cannot contain one of each.  If it contains rows, coverage forces all rows;
if it contains columns, coverage forces all columns.  \(\square\)

Write \(a_q=|A_q|\) and \(b_q=|B_q|\).  Directly,

\[
 (a_q,b_q)=
 \begin{cases}
   (q+2,q+1),&0\le q\le m-1,\\
   (2m-q,2m-q+1),&m\le q\le2m-1.
 \end{cases}                                        \tag{3.10}
\]

If the slice is tiled by rows, the number of within-line physical intervals
is

\[
                         b_q{a_q(a_q+1)\over2};
\]

if it is tiled by columns, it is

\[
                         a_q{b_q(b_q+1)\over2}.      \tag{3.11}
\]

### Theorem 3.4 (no leading gain from complementary directions)

Every complete-line tiling using only the two complementary directions has
at most

\[
          \sum_{q=0}^{2m-1}
            {a_qb_q(\max(a_q,b_q)+1)\over2}
          ={m(m+1)(m+2)(m+3)\over4}                \tag{3.12}
\]

within-line intervals.  In particular, this is

\[
                              {1\over4}m^4+O(m^3).   \tag{3.13}
\]

### Proof

Lemma 3.3 and (3.11) give the summand in (3.12).  The two halves of (3.10)
are symmetric, so the sum is

\[
 2\sum_{t=0}^{m-1}{(t+1)(t+2)(t+3)\over2}
 =\sum_{n=1}^{m}n(n+1)(n+2)
 ={m(m+1)(m+2)(m+3)\over4}.                       \tag{3.14}
\]

\(\square\)

The upper half of \(P_m\), beginning at rank \(R\), contains
\((1/2)m^4+O(m^3)\) targets.  Thus even the best complementary-pair fibre
tiling must represent at least

\[
                              {1\over4}m^4-O(m^3)    \tag{3.15}
\]

of them by cross-block intervals **if this complete-line tiling is used as
the entire upper-witness spine**.  Unrelated auxiliary or literal entries
are outside this scoped count.  Choosing the longer orientation in every
slice maximizes raw interval capacity, but changes only lower-order terms;
it does not turn the line partition itself into an all-upper construction.

## 4. A seam-local portal lower bound

The hard family also shows that a small exceptional collection of local
splices cannot repair an intact-line word.

Consider a word partitioned into intact rank-\(R\) coordinate-pair line
blocks, each of length at most \(m+1\).  Call a witness **seam-local** if it
lies in one block or in the union of two consecutive blocks.

An internal line interval never represents a member of \(\mathcal H_m\), by
Lemma 3.1.  One seam between blocks of lengths \(a,b\le m+1\) has at most
\(ab\le(m+1)^2\) crossing physical intervals.

There is a useful sharper estimate when the two lines use the same
coordinate pair.  A suffix maximum of an oriented pair line has one varying
coordinate fixed at its line height \(h\), while the other coordinate varies
monotonically.  A prefix maximum has the same form.  If their fixed-high
coordinates agree, their join fixes that coordinate and varies only the
other.  If the fixed-high coordinates differ, the larger of the two heights
fixes one of the coordinates and again only the other can vary.  Hence a
same-pair seam supplies at most \(m+1\) different crossing maxima.

### Theorem 4.1 (pervasive mixed-seam requirement)

Suppose an intact-line word has \(B=O(m^2)\) blocks and \(p\) seams whose
two blocks use different coordinate pairs.  If every member of
\(\mathcal H_m\) is required to have a seam-local witness, then

\[
                |\mathcal H_m|
                   \le p(m+1)^2+(B-1-p)(m+1),       \tag{4.1}
\]

and consequently

\[
                              p\ge(1/12-o(1))m^2.    \tag{4.2}
\]

### Proof

Charge each hard target to one seam crossed by its chosen witness.  The
general and same-pair bounds above give (4.1).  Substitute (3.4) and
\(B=O(m^2)\); the same-pair term is only \(O(m^3)\).  Division by
\((m+1)^2\) proves (4.2).  \(\square\)

In particular, the original fixed-\(\{1,2\}\) line ordering cannot cover
the hard family using only internal and adjacent-block intervals: all its
seams together contribute only \(O(m^3)\) hard candidates.  It must use
long intervals containing at least one entire intermediate line block.

The theorem is deliberately scoped to seam-local witnesses.  Long-range
intervals are the remaining portal escape.  Its message is that a bounded
or subquadratic number of local mixed-direction repairs is not enough;
mixed directions must occur on the full surface scale, or complete blocks
must be used as nonlocal portals.

For the literal direct word, even that long-range escape is unavailable on
a positive-volume subfamily.  Let \(\mathcal J_m^{12}\) consist of the hard
targets for which exactly one coordinate is at least \(s\), that coordinate
is 1 or 2, and it is strictly larger than \(s\).  The strictness deletes
only \(O(m^3)\) boundary points.

To count this family, first note that the subfamily with **no** coordinate
at least \(s\) has limiting volume \(1/18\).  In the ordered deficit
coordinates of Theorem 3.2 its volume is

\[
 24\int_0^{1/3}\int_{u_2}^{(1-u_2)/2}
       \int_{u_3}^{1-u_2-u_3}\int_0^{u_2}
       du_1\,du_4\,du_3\,du_2
 ={1\over18}.                                      \tag{4.3}
\]

The volume with exactly one qualifying coordinate is therefore
\(1/12-1/18=1/36\).  Symmetry assigns one quarter to each possible unique
coordinate, and hence

\[
                   |\mathcal J_m^{12}|
                       ={1\over72}m^4+O(m^3).        \tag{4.4}
\]

### Theorem 4.2 (the appended literal tail is not a master portal)

Take all complete coordinate-\(\{1,2\}\) rank-\(R\) lines, in any order
and either orientation, and then append the missing rank-\(2m\) points
literally, as in the direct construction.  This full word leaves

\[
                         {1\over72}m^4-O(m^3)        \tag{4.5}
\]

upper targets uncovered.

### Proof

Let \(y\in\mathcal J_m^{12}\), and suppose without loss of generality that
\(y_1>s\), while \(y_2,y_3,y_4<s\).  A complete
coordinate-\(\{1,2\}\) line with transverse coordinates \(c\le y_3\),
\(d\le y_4\) has varying-coordinate sum

\[
 K=R-c-d\ge R-y_3-y_4=y_1+y_2-s>y_2.              \tag{4.6}
\]

Its full maximum in each varying coordinate is \(\min(m,K)>y_2\).
Therefore no complete coordinate-\(\{1,2\}\) line is contained in \(y\).

An interval ending inside the line portion cannot lie in one block, by
Lemma 3.1, and cannot span three blocks, because it would contain one
complete intermediate line.  It must cross exactly one seam.  All
same-pair seams together give only \(O(m^3)\) possible values.

It remains to count intervals ending in the appended literal tail.  For one
fixed right endpoint, the maxima obtained by moving the left endpoint form
a coordinatewise chain.  Every strict change raises the sum of the four
coordinates, so the chain has at most \(4m+1\) distinct values.  The literal
tail has

\[
                         m^2+3m+1=O(m^2)            \tag{4.7}
\]

positions.  Hence all intervals ending in the tail contribute only
\(O(m^3)\) distinct maxima.  Combining this with (4.4) proves (4.5).
\(\square\)

Thus the literal middle exceptions are useful for completing the middle
layer but cannot serve as a global upper portal block.  Pervasive mixed
directions or a fundamentally different interleaving is necessary even
before the lower factor is considered.

## 5. Why the direct line spine has no uniform factor

Represent the coordinate value \(x_i\) by its nested atoms
\((i,1),\ldots,(i,x_i)\).  Coordinatewise maximum is then ordinary set
union.  For a word \(A\), write

\[
          (D^dA)_j=A_j\vee A_{j+1}\vee\cdots\vee A_{j+d}. \tag{5.1}
\]

A necessary condition for \(T=D^dA\) is:

> every internal positive run of every coordinate atom in \(T\) has length
> at least \(d+1\).

Indeed, one occurrence of the atom in \(A\) makes it positive in a block of
\(d+1\) consecutive derivative windows; overlapping such blocks can only
make the run longer.  Only runs truncated by the two global boundaries may
be shorter.

### Lemma 5.1 (two-step seam run)

Join two nontrivial complete rank-\(R\) lines using the same coordinate pair,
in arbitrary orientations and with arbitrary line heights.  At their seam
there is an internal run of some varying-coordinate atom of length at most
two.

### Proof

Write the endpoints of a nontrivial line in its two varying coordinates as

\[
                         (\ell,h),\qquad(h,\ell),
                         \qquad \ell<h.             \tag{5.2}
\]

In the forward orientation, the atom at level \(h\) in the first coordinate
occurs only at the final point; in the reverse orientation the analogous
statement holds for the second coordinate.

If the two lines have the same orientation, either the outgoing peak atom
of the first line disappears immediately, or the incoming peak atom of the
second was absent immediately before it.  The only way both failures could
be avoided would force

\[
                         \ell_2\ge h_1>\ell_1\ge h_2
                         >\ell_2,
\]

contrary to \(\ell_i<h_i\).

If the orientations are opposite, compare their peak heights.  Unequal
heights give a singleton run at the larger peak.  Equal heights give the
same peak atom at exactly the final point of the first line and the first
point of the second, and nowhere at the adjacent interior points.  Its run
has length two.  In every case the run is internal because both lines are
nontrivial.  \(\square\)

The direct fixed-pair construction has \((m+1)^2-1\) line blocks and only
two one-point lines.  For \(m\ge2\), its line portion therefore contains an
internal seam between two nontrivial lines, regardless of their order and
orientations.

### Corollary 5.2

For \(m\ge2\), the intact fixed-pair line word cannot equal \(D^dA\) for
any \(d\ge2\).

This is already incompatible with the delay demanded by lower-mask
counting.  Let \(L_m\) be the number of nonzero targets of ranks below
\(R=2m-1\).  Symmetry and

\[
              |(P_m)_{2m-1}|=M_m-(m+1)
\]

give

\[
 L_m={ (m+1)^4-3M_m\over2}+m
       ={1\over2}m^4+O(m^3).                       \tag{5.3}
\]

Suppose a near-width word \(A\) of length \(N_0+d\) covers every lower
target and also has \(D^dA=T\), where \(T\) is the line spine.  Every interval of \(A\) of
length at least \(d+1\) contains a derivative window and hence has rank at
least \(R\).  All \(L_m\) lower targets must therefore use intervals of
length at most \(d\).  Their number is

\[
             dN_0+{d(d+1)\over2}.                  \tag{5.4}
\]

Since \(N_0=(2/3+o(1))m^3\), equations (5.3)--(5.4) imply

\[
                             d\ge(3/4-o(1))m.        \tag{5.5}
\]

Corollary 5.2 rules out precisely this uniform-delay route.

## 6. The surviving all-layer target

The calculations leave a narrower and more structural target.

* Fixed-direction line intervals already handle every sublinear upper band
  at subcubic excess.
* Pair direction changes alone still leave the hard polytope of volume
  \(1/12\).
* Seam-local repair requires \(\Theta(m^2)\) mixed-direction seams.
* A uniform factor of the fixed-pair line row is impossible, whereas lower
  capacity requires delay about \(3m/4\).

Thus the plausible positive object is not “the old line word plus a few
portals.”  It is a **surface-scale complementary-pair braid**:

1. tile or split the rank-\(R\) layer into \(\Theta(m^2)\) line segments
   whose coordinate-pair directions change at a positive proportion of
   seams;
2. use long intervals through selected complete short lines to cover the
   hard family (3.3), rather than asking adjacent seam grids to do so;
3. assign nonconstant central witness widths so that a varying coordinate
   in one line becomes a transverse, persistent coordinate in the next;
4. translate the interval minima of those same line segments into the lower
   factor band.

Complementary pairs such as \(\{1,2\}\) and \(\{3,4\}\) are singled out by
the factor obstruction: both outgoing varying coordinates can become fixed
transverse coordinates across the next block, allowing their atom runs to
persist for \(\Theta(m)\) positions.  Whether one can order a full
surface-scale collection of such blocks while simultaneously realizing the
hard upper portals and the lower pin constraints is the exact open bridge.

## 7. Ledger

Proved here:

* the upper-band bound (2.5), giving width plus little-oh of \(m^3\) for
  every \(q=o(m)\);
* the exact line-orientation criterion (3.1);
* the hard residual asymptotic \(|\mathcal H_m|=m^4/12+O(m^3)\);
* the exact \(m^4/4+O(m^3)\) within-line capacity ceiling for every
  complementary-pair fibre tiling;
* the seam-local mixed-direction lower bound (4.2);
* the direct-word upper deficit (4.5), showing that the literal tail cannot
  be a master portal;
* the length-two atom-run obstruction at every same-pair line seam; and
* the incompatible uniform-delay requirements \(d\le1\) and
  \(d\ge(3/4-o(1))m\).

Not proved:

* a nonlocal portal ordering covering \(\mathcal H_m\);
* a complementary-pair tiling with the required long atom runs;
* a variable-band factor translating all lower targets; or
* the full estimate \(g_4(m,m,m,m)=M_m+o(m^3)\).
