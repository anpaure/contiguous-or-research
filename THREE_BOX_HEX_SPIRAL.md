# The concentric-hexagon shadow walk for a cubic three-chain box

## 1. Outcome

Let

\[
        H_a=\{(x,y,z)\in\mathbb Z^3:x+y+z=0,
                    \ |x|,|y|,|z|\le a\}.
\]

This is the middle layer of the box `[0,2a]^3`, translated by
`(-a,-a,-a)`.  Its size is

\[
                    M_a=3a^2+3a+1.
\]

There is an explicit walk `S_a` in `H_a`, of length exactly

\[
                         |S_a|=M_a+a,                 \tag{1.1}
\]

with the following surprisingly strong property.

> **Hex-spiral shadow theorem.**  Every point of `[-a,a]^3` whose
> coordinate sum is nonpositive is the coordinatewise minimum of a
> contiguous interval of `S_a`.  Every point whose coordinate sum is
> nonnegative is the coordinatewise maximum of a contiguous interval of
> `S_a`.

Thus one middle-layer walk, with only `a` repeated vertices, has **all-depth
lower intersection shadows and all-depth upper union shadows**.  In
particular, all rank-`(3a-1)` and rank-`(3a+1)` points are obtained from
adjacent pairs.

This does not yet prove the three-box OR lemma.  Coordinatewise maxima are
already interval ORs of the middle points, but coordinatewise minima are
not.  The remaining local problem is now a factor-labeling/pinning theorem
for this explicit spiral (necessarily with variable central witness
lengths); it is no longer a shadow-completeness problem.

## 2. The walk

For `s>=1`, let

\[
 R_s=\{(x,y,z)\in H_a:\max(|x|,|y|,|z|)=s\}.
\]

This is a hexagonal cycle of `6s` vertices.  Start it at

\[
                         c_s=(s,-s,0)
\]

and use, in order, `s` steps in each of the six directions

\[
\begin{split}
 &(0,1,-1),\quad(-1,1,0),\quad(-1,0,1),\\
 &(0,-1,1),\quad(1,-1,0),\quad(1,0,-1).
\end{split}                                                   \tag{2.1}
\]

Write the starting vertex again after the `6s` steps.  Define `S_a` by

\[
 S_a=(0,0,0)\ \Vert\ R_1\ \Vert\ R_2\ \Vert\cdots\Vert\ R_a, \tag{2.2}
\]

where every `R_s` in (2.2) is written as the closed walk just described.
The last point of `R_s` is `c_s`, and the first point of `R_(s+1)` is
`c_(s+1)`; these are adjacent.  Hence `S_a` is one walk.

It contains every member of `H_a` once and repeats exactly the `a` ring
starts.  Since

\[
 1+\sum_{s=1}^a6s=M_a,
\]

(1.1) follows.

For later reference, the six directed sides of `R_s` have the following
parametrizations, with `0<=t<=s`:

\[
\begin{array}{c|c}
0&(s,-s+t,-t)\\
1&(s-t,t,-s)\\
2&(-t,s,-s+t)\\
3&(-s,s-t,t)\\
4&(-s+t,-t,s)\\
5&(t,-s,s-t).
\end{array}                                                    \tag{2.3}
\]

Consecutive rows share their displayed corner endpoint.

## 3. The ring-arc lemma

The elementary geometric input is the following.

### Lemma 1

Let `v=(x,y,z)` satisfy `x+y+z<=0` and
`max(|x|,|y|,|z|)=s`.

Except possibly in the case

\[
             y=-s,\qquad z<0,\qquad -s<x<s,\quad -s<z<s,       \tag{3.1}
\]

`v` is the coordinatewise minimum of a non-wrapping interval of the
linearized closed ring `R_s` in (2.3).

Dually, if `x+y+z>=0`, the coordinatewise maximum is obtained inside
`R_s`, except possibly in the case

\[
             x=s,\qquad z>0,\qquad -s<y<s,\quad -s<z<s.         \tag{3.2}
\]

### Proof

This is a six-side calculation.  Here are the representative cases; the
remaining ones are obtained by cyclically permuting the coordinates in
(2.3).

If one coordinate of a lower target is `+s`, say `x=s`, then necessarily
`y,z<=0`.  On side 0 take the segment on which

\[
               y\leq \hbox{(the second coordinate)}\leq -s-z.
\]

The condition that this interval is nonempty is precisely
`s+y+z<=0`, and its coordinatewise minimum is `(s,y,z)`.

Now suppose the first coordinate is `-s`, and write the target as
`(-s,b,c)`, where `b+c<=s`.  If `c<0`, start on side 2 at

\[
                         (-s-c,s,c);
\]

if `c>=0`, start on side 3 at

\[
                         (-s,s-c,c).
\]

If `b<0`, end on side 4 at

\[
                         (-s-b,b,s);
\]

if `b>=0`, end on side 3 at

\[
                         (-s,b,s-b).
\]

The start precedes the end exactly because `b+c<=s`.  Inspection of the
three intervening sides shows that their minimum is `(-s,b,c)`.  The same
argument, shifted two sides, handles `z=-s`.

If `y=-s` and `z>=0`, sides 4--5 work.  When `x<0`, start on side 4 at
`(x,-s-x,s)`; when `x>=0`, start on side 5 at `(x,-s,s-x)`.  End on side 5
at `(s-z,-s,z)`.  Again `x+z<=s` is exactly the ordering condition.
This leaves only (3.1).

Replacing minima by maxima in the same table gives the dual statement.
The only interval that crosses the chosen cut of the ring is precisely
(3.2).  This proves the lemma.  \(\square\)

## 4. Complete lower shadows

### Theorem 2

Every `v in [-a,a]^3` with `x+y+z<=0` is the coordinatewise minimum of a
contiguous interval of `S_a`.

### Proof

Induct on `a`.  The assertion is trivial for `a=0`.  A target of infinity
norm at most `a-1` has a witness in the initial copy of `S_(a-1)`.

It remains to treat a target of norm `a`.  Lemma 1 gives an interval in
`R_a` unless the target has the exceptional form

\[
                         v=(b,-a,c),\qquad c<0,                  \tag{4.1}
\]

with `-a<b<a` and `-a<c<0` (the cases with another coordinate equal to
`+a` or `-a` were already handled by a ring side).

Put `s=a-1`.  There is a suffix of the final ring `R_s`, ending at
`c_s=(s,-s,0)`, whose minimum is

\[
                         (b,-s,0).                              \tag{4.2}

\]

Indeed, for `b<0` start on side 4 at `(b,-s-b,s)`, and for `b>=0` start on
side 5 at `(b,-s,s-b)`.  The remainder of sides 4--5 has minimum (4.2).

The prefix of `R_a` from `c_a=(a,-a,0)` through the side-0 point

\[
                         (a,-a-c,c)                             \tag{4.3}

\]

has minimum `(a,-a,c)`.  The suffix (4.2), the radial edge
`c_s c_a`, and the prefix (4.3) form one contiguous interval of `S_a`.
Their coordinatewise minimum is `(b,-a,c)`, as required.  \(\square\)

## 5. Complete upper shadows

### Theorem 3

Every `v in [-a,a]^3` with `x+y+z>=0` is the coordinatewise maximum of a
contiguous interval of `S_a`.

### Proof

The induction is the same.  Lemma 1 leaves only

\[
                         v=(a,b,c),\qquad c>0,                   \tag{5.1}

\]

with `-a<b<a` and `0<c<a`.

Put `s=a-1`.  Start a suffix of `R_s` on side 5 at

\[
                         (s-c,-s,c).

\]

Its maximum through the endpoint `c_s` is `(s,-s,c)`.  In `R_a`, use the
prefix from `c_a` until the first point whose second coordinate is `b`:
this lies on side 0 if `b<=0` and on side 1 if `b>=0`.  That prefix has
maximum `(a,b,0)`.  Joining the old-ring suffix, radial edge, and new-ring
prefix gives maximum `(a,b,c)`.  \(\square\)

Combining Theorems 2 and 3 proves the hex-spiral shadow theorem.

## 6. The exact depth-one ledger

The ordinary (nonradial) cycle edges in all rings number

\[
                         \sum_{s=1}^a6s=M_a-1.                  \tag{6.1}

\]

The layers immediately below and above `H_a` also have `M_a-1` points.
The calculation in Lemma 1 specializes at rank difference one to a single
ring edge.  Therefore

* the minima of the `M_a-1` ring edges are all distinct and are exactly the
  layer of sum `-1`;
* the maxima of those edges are all distinct and are exactly the layer of
  sum `+1`.

So the ring edges form a perfect two-sided edge-color set, but topologically
they are the disjoint cycles `R_1,...,R_a`.  The `a` radial seams in `S_a`
connect these cycles and the center into one walk.  This explains the exact
`+a` term in (1.1): it is a perimeter-order topological repair, not a
shadow-cardinality loss.

## 7. What this does and does not prove

If the translated triples are interpreted as chain-prefix masks, join is
coordinatewise maximum.  Hence the word consisting of the spiral vertices
already represents every target on or above the middle rank by contiguous
ORs.

The lower theorem is an intersection statement.  Turning those interval
minima into interval unions requires choosing sparse occurrences of the
three chains' increments.  This is precisely a coordinatewise interval-
stabbing problem.  The obvious fixed-delay factorization cannot do it: the
rank-slack delay in `[0,2a]^3` is

\[
                         (4/3+o(1))a>a,                          \tag{7.1}

\]

because the lower half has `4a^3+O(a^2)` points while the middle layer has
`3a^2+O(a)` points; the quadratic short-interval correction is only
`O(a^2)`.  On the other hand, each of the three extreme middle-layer
coordinate supports has only `a+1` vertices.  The fixed-window run
criterion would force each such
short support to touch a row boundary, and three pairwise disjoint supports
cannot all touch only two boundaries.

Thus the right sharpened local target is:

> **Spiral pinning problem.**  Use the explicit `M_a+a` spiral order and a
> variable-band family of central witnesses to assign all lower targets to
> intervals, then prove the coordinatewise pin-survival conditions with
> only `O(a)` additional positions.

The upper and lower shadow geometry is now completely explicit.  The
remaining obstruction is simultaneous pin survival, not the existence of
the required shadows.

## 8. Independent finite sanity check

As a check on the indexing and on the two exceptional seam cases, the walk
was independently generated for every `1<=a<=10`.  For each generated word,
all contiguous intervals were enumerated, both their componentwise minima
and maxima were recorded, and these sets were compared with every point of
`[-a,a]^3`.  There were zero missing nonpositive-sum points and zero missing
nonnegative-sum points in every case.  This computation is only a sanity
check; Theorems 2 and 3 are the all-`a` proof.

## 9. A factorable variable band on the closed spiral

The closed spiral also clears the central factorability gate.  This is the
reason for retaining the repeated initial vertex of every ring.

Index the occurrences of `S_a` as

\[
                         T_1,\ldots,T_L,
             \qquad L=M_a+a,
\]

and let `d_i` be the radius of the ring containing `T_i` (with `d_1=0` at
the center).  Prescribe the central witness intervals

\[
                         I_i=[i,i+d_i].                          \tag{9.1}

\]

They live in `L+a=M_a+2a` physical positions.

### Lemma 4 (variable-window run criterion)

Let `d_1<=...<=d_L`, and prescribe sets `T_i` on intervals
`I_i=[i,i+d_i]`.  Fix one ground-set coordinate and write `eps_i=1` when
that coordinate belongs to `T_i`.  If every internal 1-run `[u,v]` obeys

\[
                       v-u+1\geq1+\max_{u\leq i\leq v}d_i,       \tag{9.2}

\]

then this coordinate can be placed in the physical word so that its union
on `I_i` is exactly `eps_i`, for every `i`.

### Proof

Every zero interval forbids all its positions.  For an internal 1-run
`[u,v]`, let

\[
 C=\max\{j+d_j:j<u,\ \epsilon_j=0\}.
\]

Zeros following the run begin only at `v+1`.  Hence the legal positions
between the neighboring zero blocks include

\[
                         [C+1,v].                               \tag{9.3}

\]

This interval is nonempty: monotonicity gives `C<=u-1+d_u`, while (9.2)
gives `v>=u+d_u`.  Moreover every positive interval `I_i`, `u<=i<=v`,
meets (9.3), since

\[
                  i\leq v,\qquad i+d_i\geq u+d_u\geq C+1.
\]

Put the coordinate at a hitting set of these legal pieces, independently
for every 1-run.  Boundary runs use the same argument with the missing
neighbor omitted.  \(\square\)

### Lemma 5 (spiral run bound)

For every coordinate direction and every threshold, the incidence word of
that threshold along `S_a` satisfies (9.2) with `d_i` equal to ring radius.

### Proof

On `R_s`, a coordinate superlevel set is a cyclic arc.  From the six side
parametrizations (2.3), every nonempty internal piece of that arc has at
least `s+1` vertices.  If the chosen cut splits the arc, its boundary pieces
either touch an endpoint of the full word or join through a radial seam to
the corresponding piece in the next ring.  In the latter case the joined
run has at least `s+1`, where `s` is its largest ring radius.  Concretely,
for the first coordinate the cut vertex has value `s`, for the second it
has value `-s`, and for the third it has value `0`; these three cases in
(2.3) give respectively a joined boundary arc, an internal arc, and one of
those two alternatives according to the sign of the threshold.  Thus every
internal run obeys (9.2).  \(\square\)

### Corollary 6 (central factor and automatic upper half)

There exists a word

\[
                        A_1,\ldots,A_{M_a+2a}                   \tag{9.4}

\]

such that

\[
                        \bigvee_{p\in I_i}A_p=T_i               \tag{9.5}

\]

for every spiral occurrence.  Every middle- or upper-rank point of the
three-chain cube is consequently an OR of a contiguous interval of `A`.

### Proof

Apply Lemmas 4--5 independently to all `6a` chain increments.  This proves
(9.5).  For a consecutive spiral interval `[u,v]`, the physical intervals
`I_u,...,I_v` have no gaps and, because their right endpoints are
nondecreasing, their union is exactly

\[
                          [u,v+d_v].
\]

Therefore

\[
 \bigvee_{i=u}^vT_i
   =\bigvee_{p=u}^{v+d_v}A_p.                                   \tag{9.6}
\]

Theorem 3 says that the left side of (9.6) ranges over every point on or
above the middle layer.  \(\square\)

This is stronger than a shadow-row certificate: it is an explicit proof
that the closed spiral has a valid `width+O(a)` central factor, and every
such factor automatically covers the entire upper half.  What is still
missing is a choice of the coordinate hitting sets in Lemma 4 whose shorter
OR intervals cover the lower half.  The coordinatewise maximal factor does
not have that property, nor do the naive leftmost/rightmost minimum hitting
sets; the remaining problem is genuinely simultaneous sparse pinning.

## 10. A barrier no-go for alternating singleton/pair bands

One tempting modification is to use singleton central witnesses on three
alternating sides of every ring and adjacent-pair witnesses on the other
three sides.  The offsets then move only six times per ring, for total
padding `O(a)`.  This cannot work, for a simple cardinality reason.

### Lemma 7 (middle-entry barriers)

If a physical entry is itself a middle-rank target, no interval representing
a below-middle target can contain that position.  If the barrier positions
split the remaining word into gaps of lengths `g_1,...,g_t`, the total
number of distinct below-middle targets that can be represented is at most

\[
                         \sum_j {g_j+1\choose2}.                 \tag{10.1}
\]

### Proof

OR is monotone.  An interval containing a middle-rank entry has rank at
least the middle rank.  Every lower witness is therefore wholly contained
in one barrier-free gap, which has only `binom(g_j+1,2)` intervals.  \(\square\)

In the alternating-side proposal, each radius-`s` ring has three
barrier-free pair-state runs, each of length `s+O(1)`.  Even allowing
`O(a)` additional boundary positions, (10.1) is at most

\[
  3\sum_{s=1}^a {s+O(1)\choose2}+O(a^2)
       =(1/2+o(1))a^3.                                         \tag{10.2}
\]

But the number of nonempty points strictly below the middle layer is

\[
 { (2a+1)^3-M_a\over2}-1
       =4a^3+{9\over2}a^2+{3\over2}a-1.                        \tag{10.3}
\]

Thus that band misses the necessary interval capacity by a factor tending
to eight.  More generally, a useful width-plus-perimeter band cannot place
middle-rank singleton barriers at positive density unless its nonbarrier
gaps are much longer than the ring sides.  The successful variable band
must keep only `O(a)` such barriers, or avoid them altogether.

## 11. Exact cardinality no-go for the radius band

The factorable band (9.1) itself cannot be completed to a universal word.
This failure is independent of how cleverly the legal pins are selected.

### Theorem 8 (radius-band capacity deficit)

For the closed spiral intervals `I_i=[i,i+d_i]`, the number of physical
intervals which contain no complete central witness is exactly

\[
                         2a(a+1)^2.                             \tag{11.1}

\]

This is smaller than the number of nonempty below-middle targets,

\[
        4a^3+{9\over2}a^2+{3\over2}a-1,                        \tag{11.2}

\]

for every `a>=1`.  Consequently no factor satisfying (9.5), maximal or
sparse, can be universal.

### Proof

An interval whose left endpoint is the start `i` of a central occurrence
cannot reach `i+d_i`, since it would then contain `I_i` and have OR rank at
least the middle rank.  Because the delays are nondecreasing, `I_i` is the
first-ending central witness whose left endpoint is at least `i`.  Thus a
lower candidate starting at `i` has exactly `d_i` possible positive
lengths.  The center has `d_1=0`.  After the last central occurrence there
are `a` unconstrained tail positions, contributing `binom(a+1,2)` more
intervals.  Hence the exact count is

\[
 \sum_{s=1}^a s(6s+1)+{a+1\choose2}
   =2a(a+1)^2,
\]

which proves (11.1).  Formula (11.2) is half of the noncentral volume of
the rank-symmetric cube, with the empty point removed.  Their difference is

\[
              2a^3+{1\over2}a^2-{1\over2}a-1>0
\]

for `a>=1` (it equals one at `a=1`).  \(\square\)

This identifies the quantitative correction.  A viable monotone band must
have average central-witness delay about `4a/3`, whereas the ring-radius
band has average delay asymptotic to only `2a/3`.  At the same time a fixed
delay above `a` is impossible because of the three short extreme-coordinate
supports.  The live geometric problem is therefore very specific:

> distribute extra left/right offset growth among the six ring sectors so
> that the **average** witness length reaches `4a/3+O(1)`, every short
> coordinate run is absorbed at a band transition, and only `O(a)` total
> offset is used.

The spiral solves the complete-shadow part; Theorem 8 shows exactly why its
first factorable band has only half of the lower interval capacity required.
