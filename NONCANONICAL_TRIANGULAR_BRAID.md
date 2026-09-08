# Noncanonical triangular braids: a linear repetition obstruction and the portal normal form

## 1. Outcome

Let

\[
 \mathcal T_R=\{P_0=(0,0)\}\cup
 \{E_{s,y}=(s,y):1\le s\le R,\ 0\le y<s\},
\]

where `P_s=E_(s,0)`.  For

\[
                  0\le u<r\le R,\qquad 0\le x<r,
\]

the target `Z_(u,r,x)` is represented by a contiguous word interval exactly
when the interval has bounding box

\[
                         [u,r]\times[0,x].             \tag{1.1}
\]

This note studies words over `T_R` without requiring the canonical provider
pair `P_u,E_(r,x)`.

The desired all-`R` word using every cell once plus `O(R)` repetitions has
not yet been constructed.  Two new rigorous conclusions are obtained.

1.  Linear repetition is genuinely necessary.  If a universal word contains
    every cell of `T_R` and has `q` occurrences beyond the
    `|T_R|=1+R(R+1)/2` compulsory occurrences, then

    \[
       \boxed{
       q\ge
       \left\lceil{\lfloor R/2\rfloor-2\over2}\right\rceil
       ={R\over4}-O(1).
       }                                                \tag{1.2}
    \]

    For `R>=3`, the independent exact-once obstruction also gives `q>=1`.
    Thus an `O(R)`-repeat construction, if it exists, has the best possible
    order of additive overhead.

2.  Every nonzero-height target must cross a physical peak/nonpeak boundary,
    called a **portal**.  At one fixed portal, all interval bounding boxes are
    coordinatewise joins of two nested chains, one grown to the left and one
    grown to the right.  Hence the unrestricted problem is exactly a problem
    of embedding `O(R)` two-chain grids into one near-Hamilton word.  This is
    the noncanonical mechanism absent from the earlier arm--peak chain-cover
    argument.

An explicit three-provider gadget shows that the abstract target family can
indeed be covered by `R` such grids.  Its literal concatenation is not
spanning--for example, it omits `E_(4,2)` when `R=4`--so it is a structural
grid certificate, not a repetition upper bound.  The remaining difficulty is
simultaneously spanning the triangle and sharing occurrences while realizing
all those grids in one physical word.

The heuristic words of lengths 8, 13, and 20 for `R=3,4,5` were also
independently checked.  They use respectively 1, 2, and 4 repetitions, and
fit the portal description.  They do not by themselves establish an all-`R`
pattern.

There is a numerically striking, but presently unproved, stronger pattern.
The successful excesses for `R=3,4,5` are `1,2,4`, equal to

\[
                         \left\lfloor{(R-1)^2\over4}\right\rfloor. \tag{1.3}
\]

Section 5 identifies (1.3) as the exact cardinality of a natural strict-
interior equal-rank antichain.  No injection from that antichain to repeated
occurrences is currently known, so (1.3) must not be quoted as a lower bound.

## 2. A linear lower bound on repetitions

Call a cell a **peak** when its second coordinate is zero, and a **nonpeak**
otherwise.  Thus the peaks are precisely

\[
                         P_0,P_1,\ldots,P_R.            \tag{2.1}
\]

Let a universal word over `T_R` contain every triangular cell at least once.
Write

\[
 n=|\mathcal T_R|+q,
 \qquad
 P=\hbox{number of peak occurrences}.                 \tag{2.2}
\]

Since only the `q` excess occurrences can be additional peaks,

\[
                         P\le R+1+q.                   \tag{2.3}
\]

Let `a` be the number of adjacent physical position-pairs containing two
peaks, and let `b` be the number containing one peak and one nonpeak.

### Lemma 1 (the zero-height layer consumes `R` peak--peak edges)

\[
                              a\ge R.                  \tag{2.4}
\]

#### Proof

For each `i=0,...,R-1`, consider the target

\[
                         [i,i+1]\times\{0\}.           \tag{2.5}
\]

Every cell in a witnessing interval has second coordinate zero, so the
witness is a word over `P_i,P_(i+1)` and contains both labels.  Somewhere
inside it there is an adjacent transition between these two distinct peak
labels.  Different `i` require different physical transitions, proving
(2.4).  QED.

### Lemma 2 (the first positive layer consumes many portals)

\[
                         b\ge\left\lceil{R-1\over2}\right\rceil.
                                                               \tag{2.6}
\]

#### Proof

For each `i=1,...,R-1`, consider

\[
                         [i,i+1]\times[0,1].            \tag{2.7}
\]

Its witness contains a peak, because its minimum second coordinate is zero,
and a nonpeak of height one, because its maximum second coordinate is one.
Moving inside the witness from one type to the other crosses a physical
peak/nonpeak adjacency.

Fix such an adjacency.  Its two cells have the form `P_j` and `E_(s,1)`.
If it lies in a witness for (2.7), then

\[
                         j,s\in\{i,i+1\}.               \tag{2.8}
\]

When `j!=s`, this determines `i` uniquely.  When `j=s`, there are at most the
two choices `i=s-1,s`.  Thus one physical portal can serve at most two of the
`R-1` targets (2.7).  This proves (2.6).  QED.

### Theorem 3 (linear excess theorem)

Every universal spanning word over `T_R` satisfies (1.2).

#### Proof

Count incidences between peak occurrences and adjacent word edges.  If `e`
of the two endpoints of the whole word are occupied by peaks, then

\[
                         2P-e=2a+b.                    \tag{2.9}
\]

Consequently, by Lemma 1 and (2.3),

\[
                         b\le2P-2a
                           \le2(R+1+q)-2R=2q+2.        \tag{2.10}
\]

Combining (2.6) and (2.10) gives

\[
 q\ge
 \left\lceil{lceil(R-1)/2\rceil-2\over2}\right\rceil
 =\left\lceil{\lfloor R/2\rfloor-2\over2}\right\rceil.
                                                               \tag{2.11}
\]

QED.

This theorem is unrestricted with respect to witnesses: the minimum and
maximum `s` coordinates and the maximum `y` coordinate may be supplied by
three different cells.  Its only scope restriction is that the physical word
uses the triangular alphabet and contains every triangular cell.  Entries
outside `T_R` require a separate argument.

## 3. Portal normal form

Let a physical portal be an adjacent pair of positions `p,p+1` with one peak
and one nonpeak.  For definiteness suppose the peak is at `p` and the
nonpeak at `p+1`; the other orientation is identical.

For `l<=p`, let `L_l` be the bounding box of positions `[l,p]`.  As `l`
moves left, the four extrema of `L_l` only expand.  Thus

\[
                         L_p\subseteq L_{p-1}\subseteq\cdots
                                                               \tag{3.1}
\]

is a chain of rectangles.  Similarly the boxes `R_j` of `[p+1,j]` form a
nested chain as `j` moves right.  The bounding box of the interval `[l,j]`
is exactly

\[
                            L_l\vee R_j,                \tag{3.2}
\]

where the join takes the minimum of lower endpoints and the maximum of upper
endpoints in each coordinate.

### Proposition 4 (two-chain-grid reduction)

Every target with `x>0` can be assigned to a physical portal in one of its
witnesses.  For each fixed portal, all targets assigned there lie in the
join grid

\[
                         \{L_l\vee R_j:l\le p<j\}.      \tag{3.3}
\]

Conversely, every member of (3.3) whose extrema have the form (1.1) is
represented by the corresponding contiguous interval.

#### Proof

A positive-height witness contains both a peak and a nonpeak, hence crosses
a portal; choose one.  Formula (3.2) is the elementary rule for the bounding
box of a union of two adjacent intervals.  The converse follows by taking
that interval.  QED.

If the excess is `q=O(R)`, (2.10) shows that there are only `O(R)` physical
portals.  Therefore a near-once construction is equivalent to packing the
whole three-parameter target family into `O(R)` grids of two nested chains.
This explains how noncanonical witnesses evade the old theorem saying that
one *oriented side* of one `P_u` occurrence is only one chain: a portal uses
both sides simultaneously, and their independent endpoints form a grid.

## 4. An explicit three-provider grid for each `u`

The portal-grid mechanism is not merely a counting abstraction.  For every
fixed lower endpoint `u`, one grid covers all targets with that `u` and
positive height.

For `0<=u<R`, define the left chain

\[
 L_u=(E_{R,1},E_{R-1,1},\ldots,
      E_{\max(u+1,2),1},P_u).                          \tag{4.1}
\]

For `2<=t<=R-1`, put

\[
 Q_{u,t}=E_{\max(u,t+1),t},                            \tag{4.2}
\]

and define

\[
                         G_u=L_u\Vert
                         (Q_{u,2},Q_{u,3},\ldots,Q_{u,R-1}).
                                                               \tag{4.3}
\]

Empty ranges are omitted.  Every point in (4.2) is a legal triangular cell:
its first coordinate is strictly larger than its second.

### Proposition 5 (three-provider factorization)

For fixed `u`, every target `[u,r]x[0,x]` with `u<r<=R` and
`1<=x<r` is the bounding box of a contiguous interval of `G_u`.

#### Proof

If `x=1`, start at `E_(r,1)` in the descending left chain and stop at `P_u`.

If `x>=2`, start at `E_(r,1)`, continue through `P_u`, and stop at `Q_(u,x)`.
The terms following `P_u` have heights `2,3,...,x`, so the height extrema are
zero and `x`.  Their first coordinates are

\[
                         \max(u,t+1)\le r
                         \quad(2\le t\le x<r).          \tag{4.4}
\]

The descending left chain starts at first coordinate `r` and thereafter
stays between `u` and `r`; `P_u` supplies the minimum `u` and height zero.
Thus the four extrema are exactly `u,r,0,x`.  QED.

Concatenating `G_0,...,G_(R-1)` and then a literal peak spine covers the
entire triangular target family.  Its length is

\[
                         {3R^2+R\over2}.                \tag{4.5}
\]

Formula (4.5) is for `R>=2`; at `R=1` the redundant empty positive-target
gadget should be omitted and the two-point peak spine used.  The concatenated
word need not contain every triangular cell, so it is not an upper bound on
the spanning repetition parameter.  Its significance is structural: it
proves that exactly `R` abstract two-chain grids suffice, with genuinely
noncanonical three-provider witnesses.  The open packing problem is to
superpose these grids while also inserting every omitted triangular cell,
without destroying the grid witnesses or recopying the shared column-one and
diagonal chains.

## 5. The small noncanonical certificates

### 5.1 The strict-interior antichain behind the observed numbers

The depth of a target is

\[
                              d=r-u+x.                 \tag{5.1}
\]

Restrict to depth `d=R-1` and to targets strictly away from both vertical
boundaries:

\[
                         1\le u<r\le R-1.              \tag{5.2}
\]

Put `a=r-u`, so `x=R-1-a`.  For fixed `a`, the admissible values of `r`
number

\[
                         \min(a,R-1-a).                \tag{5.3}
\]

Therefore this equal-depth antichain has cardinality

\[
 \sum_{a=1}^{R-2}\min(a,R-1-a)
   =\left\lfloor{(R-1)^2\over4}\right\rfloor.         \tag{5.4}
\]

In an exact-once word, the forced monotone peak block makes *every* strict-
interior positive target impossible, which explains why this family is a
natural candidate obstruction once repetitions are allowed.  However, one
repeated occurrence can alter several portal grids and can serve several
members of (5.4).  The ordinary endpoint-chain argument only says that the
members of (5.4) need distinct right endpoints; it does not say that those
endpoints must be excess occurrences.  Consequently

\[
 q\stackrel{?}{\ge}\left\lfloor{(R-1)^2\over4}\right\rfloor
                                                               \tag{5.5}
\]

is a concrete conjecture suggested by `R=3,4,5`, not a theorem.

### 5.2 Certificates

For `R=3`, the following length-8 word has one repetition and covers all 14
targets:

```text
(1,0) (2,1) (0,0) (1,0) (2,0) (3,0) (3,1) (3,2)
```

The following word contains every cell of `T_4` and two repetitions:

```text
(4,3) (4,2) (4,1) (3,1) (4,0) (3,0) (2,0)
(1,0) (0,0) (1,0) (2,1) (3,0) (3,2)
```

All 30 targets are present as contiguous bounding boxes.

The following word contains every cell of `T_5` and four repetitions:

```text
(5,4) (4,3) (4,2) (4,0) (3,1) (2,1) (1,0) (3,2)
(3,0) (2,1) (0,0) (1,0) (2,0) (3,0) (4,0) (5,0)
(4,1) (5,2) (5,3) (5,1)
```

All 55 targets are present.  In both words the zero-height targets are
handled by a complete peak spine, while positive-height witnesses use the
few portals on either side of that spine.  These are exhaustive finite
certificates, not evidence of a proved recurrence.

## 6. Exact surviving mathematical target

The canonical peak theorem forced quadratic peak multiplicity because it
assigned every target `(u,r,x)` to the exact pair `P_u,E_(r,x)` and to one
oriented side.  Proposition 4 identifies the escape precisely:

> Construct one word with `O(R)` peak/nonpeak portals such that the joins of
> the two nested bounding-box chains at those portals cover all
> `[u,r]x[0,x]`, while every triangular cell occurs only once plus `O(R)`
> total repeats.

Theorem 3 shows that the requested `O(R)` portal/repetition scale cannot be
improved in order.  Proposition 5 shows that `R` chain grids are
combinatorially enough.  What remains is a simultaneous-superstring theorem
for those grids: column-one chains and diagonal top providers must be shared
across portals without contaminating the rectangles already represented.

This is a substantially narrower problem than searching arbitrary words,
and it is genuinely noncanonical.  A successful solution would give a
fixed-`c` triangular word of length

\[
                         |\mathcal T_R|+O(R),           \tag{6.1}
\]

which is the surface-order repair needed by the four-box constant-one
program.  The present note neither proves nor disproves (6.1).
