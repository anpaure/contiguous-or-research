# Audit of the concentric-hexagon shadow walk

## 1. Verdict

The geometric shadow theorem in `THREE_BOX_HEX_SPIRAL.md` is correct:

* the sequence has exactly `M_a+a` positions;
* the stated lower and upper exceptional ring arcs are the exact exceptions
  caused by the linear cut;
* both induction seams realize the claimed coordinatewise extrema; and
* the ordinary ring edges biject with the two adjacent ranks.

The theorem is a genuine all-depth two-sided **shadow** construction.  The
subsequently added Section 9 is also correct: the variable intervals
`I_i=[i,i+d_i]` admit a factor of length `M_a+2a`, including across every
repeated ring start, and every upper spiral arc lifts to one contiguous factor
interval.  Thus the occurrence-schedule, central-factor, and upper-lifting
gaps are cleared.

What remains is the lower half.  One must jointly assign lower targets to
physical intervals and choose the coordinate hitting sets so those intervals
have the exact prescribed ORs.  Calling this whole joint problem
“simultaneous sparse pinning” is defensible, but ordinary pin survival for an
already fixed assignment is only its final substep; no lower Hall/assignment
theorem is yet supplied.

Equation (7.1) in the original draft is arithmetically wrong.  For the even
cube `[0,2a]^3`, the middle-rank interval-slack delay is

\[
                         \tau={4a\over3}+O(1),
\]

not `(sqrt(17)-3+o(1))a`.  The fixed-row no-go remains valid, since
`tau>=a+1`.

## 2. Sequence and length ledger

The six directions in (2.1), starting at `c_s=(s,-s,0)`, give precisely the
six parametrized sides in (2.3).  After `6s` steps the walk returns to `c_s`.
Thus the written closed ring contains `6s+1` sequence positions but only
`6s` distinct vertices.

The concatenation contains the center once, every noncentral point of `H_a`
once, and the start `c_s` of every ring one additional time.  Therefore

\[
 |S_a|=1+\sum_{s=1}^a(6s+1)
      =(1+3a(a+1))+a=M_a+a.
\]

The seam from `c_s` to `c_(s+1)` is a Johnson edge with difference
`(1,-1,0)`; the center-to-`c_1` seam has the same form.  Hence the
concatenation is indeed one lattice walk.  There are exactly `a` radial seams:
one from the center to `R_1` and `a-1` between successive rings.

## 3. Ring-arc exceptions

### 3.1 Lower arcs

Every norm-`s` target has a coordinate equal to `+s` or `-s`.

If a lower target has a coordinate `+s`, the other two coordinates are
nonpositive.  On the side where that coordinate is fixed at `+s`, the two
remaining coordinates vary oppositely.  The segment between their prescribed
values is nonempty exactly when the target sum is nonpositive.  These arcs lie
on sides 0, 2, or 4 and do not cross the cut.

For a target `(-s,b,c)`, the starts and ends listed in the proof lie, in
linear order, on sides 2--4.  When both endpoints are on side 3, their order is
equivalent to `b+c<=s`; in all cross-side cases it is automatic.  The minima
on the intervening sides are exactly `(-s,b,c)`.  The analogous `z=-s` arcs
lie on sides 0--2.

For `y=-s`, the arcs with `z>=0` lie on sides 4--5.  If instead `z<0` and the
target is not a corner already covered by another extreme-coordinate case,
the required arc runs from side 5 through `c_s` to side 0.  It crosses the
chosen linear cut.  This is exactly

\[
 y=-s,\qquad z<0,\qquad -s<x<s,\quad -s<z<s.
\]

There are no further lower exceptions.

### 3.2 Upper arcs and the cut-preserving duality

The upper claim should not be justified merely by saying “replace minima by
maxima,” because negation alone moves the cut.  The exact involution is

\[
                     \Phi(x,y,z)=(-y,-x,-z).
\]

It fixes `c_s`, maps the written ring to itself with its order reversed, and
interchanges coordinatewise minima with maxima.  Applying `Phi` to the lower
exception gives

\[
 x=s,\qquad z>0,\qquad -s<y<s,\quad -s<z<s,
\]

which is precisely (3.2).  This proves both completeness and the exact
location of the upper cut exception.

A finite independent sanity check enumerating every linear ring interval for
`1<=s<=20` found exactly these two exceptional families and no others.  This
check is not needed for the proof above.

## 4. Induction seams

### 4.1 Lower seam

For an exceptional outer target

\[
                         v=(b,-a,c),\qquad c<0,
\]

integrality and strict interiority give

\[
 -s\leq b\leq s,qquad -s\leq c\leq-1,qquad s=a-1.
\]

The stated suffix of `R_s` has minimum `(b,-s,0)`:

* for `b<0`, side 4 starts at `(b,-s-b,s)` and the remainder of sides
  4--5 lowers the second and third coordinates to `-s` and `0`;
* for `b>=0`, the side-5 suffix starts at `(b,-s,s-b)` and ends at
  `c_s=(s,-s,0)`.

The prefix of `R_a` through `(a,-a-c,c)` has minimum `(a,-a,c)`.  These two
pieces are consecutive in `S_a`, separated only by the radial edge
`c_s c_a`.  Their combined minimum is `(b,-a,c)`.  For `a=1` the exceptional
integer family is empty, so no nonexistent `R_0` arc is used.

### 4.2 Upper seam

For

\[
                         v=(a,b,c),\qquad c>0,
\]

one has `-s<=b<=s` and `1<=c<=s`.  The side-5 suffix of `R_s` beginning at
`(s-c,-s,c)` has maximum `(s,-s,c)`.  The prefix of `R_a` ending at the first
point with second coordinate `b` has maximum `(a,b,0)`.  Their union across
the radial seam has maximum `(a,b,c)`.  Again the exceptional family is empty
when `a=1`.

The induction therefore proves the all-depth lower and upper shadow theorem.

## 5. Depth-one ledger

The ordinary ring edges number

\[
                         \sum_{s=1}^a6s=M_a-1.
\]

For a point `w` of sum `-1` and norm `s`, exactly two of its three upper
covers `w+e_i` remain on `R_s`; the third either leaves the norm-`s` shell or
leaves the box.  Those two covers are adjacent on `R_s`, and their
coordinatewise minimum is `w`.  This gives a direct bijection

\[
 \{\text{ordinary ring edges}\}
       \longleftrightarrow
 \{w\in[-a,a]^3:\ x+y+z=-1\}.
\]

The upper statement follows either identically from lower covers or via
`Phi`.  Hence the edge minima and maxima are respectively all distinct and
are exactly the sum `-1` and sum `+1` layers.  Since the adjacent layer size is
`M_a-1`, the depth-one ledger in Section 6 is exact.

The repeated starts add one position per ring solely to close the cycles and
make the radial concatenation.  This explains the `+a` sequence length, but
does not itself construct an OR factor.

## 6. Correct delay arithmetic

For `[0,2a]^3`,

\[
 M_a=3a^2+3a+1
\]

and the number of nonzero points strictly below the middle rank is

\[
 L_a=4a^3+{9\over2}a^2+{3\over2}a-1.
\]

The rank-slack delay is the least integer `t` satisfying

\[
                         L_a\leq tM_a+{t+1\choose2}.
\]

Since `t=Theta(a)`, the quadratic term is only `O(a^2)`, whereas `tM_a` and
`L_a` are `Theta(a^3)`.  Therefore

\[
                         t={4a\over3}+O(1).
\]

Substituting `t=a` leaves deficit

\[
 L_a-\left(aM_a+{a+1\choose2}\right)=a^3+a^2-1>0,
\]

so `t>=a+1`.  The three extreme coordinate supports each contain only `a+1`
middle vertices and are pairwise disjoint.  Thus the two-boundary run
obstruction still rules out every fixed-window middle-row factor.

## 7. Audit of the variable band in Section 9

Write `L=M_a+a` and give every occurrence in ring `s` the delay `d_i=s`, with
delay zero at the initial center.  The delay sequence is nondecreasing,
including at both copies of every ring start and across every radial seam.
Consequently

\[
 r_i=i+d_i
\]

is in fact strictly increasing, since

\[
 r_{i+1}-r_i=1+d_{i+1}-d_i\geq1.
\]

The last right endpoint is `L+a=M_a+2a`, so the physical length ledger is
correct.

### 7.1 Lemma 4

Fix a coordinate and an internal positive run `[u,v]`.  Every zero interval
before the run ends no later than

\[
 C=\max_{j<u,\epsilon_j=0}(j+d_j)
       \leq u-1+d_u.
\]

Every zero interval after the run starts at `v+1` or later.  Hence every
position in `[C+1,v]` is legal.  Condition (9.2), together with monotonicity,
gives

\[
 v\geq u+\max_{u\leq i\leq v}d_i\geq u+d_u>C.
\]

For each positive `i`,

\[
 i\leq v,qquad i+d_i\geq u+d_u\geq C+1,
\]

so `I_i` meets that legal piece.  Placing the coordinate at all positions of
the piece, or at any hitting subset, hits every positive interval and no zero
interval.  For a left boundary run, omit `C` and use the legal prefix through
`v`; for a right boundary run use the legal suffix after `C`; an all-one word
is immediate.  Thus the proof handles all earlier and later zero intervals,
not only the adjacent zero indices.

### 7.2 Lemma 5

On one ring, a nonempty coordinate superlevel is a cyclic arc.  Any part not
meeting the chosen cut has at least `s+1` positions; equality occurs at an
extreme-coordinate side.  The cut cases can be checked without handwaving:

* for `x`, the cut value is `s`; split boundary pieces join across the seam
  `c_s c_(s+1)`.  If a new threshold first appears on `R_s`, its internal
  prefix contains the entire `x=s` side and has `s+1` positions;
* for `y`, the cut value is `-s`.  A proper superlevel misses the cut and is
  one internal arc of at least `s+1` positions.  Whole-ring runs are longer;
* for `z`, the cut value is zero.  Positive thresholds give an internal arc,
  while nonpositive thresholds contain both seam endpoints and join across
  rings.

Thus every internal run has length at least one plus its largest ring radius.
The two copies of each `c_s` are essential in these boundary joins.  A direct
enumeration of all coordinates and thresholds for `a<=30` found no violation;
the coordinate argument above is the proof.

### 7.3 Corollary 6

Apply Lemma 4 independently to all `6a` increments.  This gives
`OR(I_i)=T_i` for every occurrence, including both occurrences of each `c_s`.

For consecutive indices `u<=i<=v`, successive intervals have consecutive
left endpoints and strictly increasing right endpoints.  They have no integer
gaps even at the initial delay-zero seam: `[i,i]` followed by `[i+1,...]` is
still contiguous.  Therefore

\[
 \bigcup_{i=u}^vI_i=[u,v+d_v].
\]

It follows exactly that

\[
 \bigvee_{i=u}^vT_i=\bigvee_{p=u}^{v+d_v}A_p.
\]

The upper shadow theorem therefore proves coverage of the entire middle and
upper halves in the factor word.  Section 9 really does clear the flag and
upper-lifting gates.

## 8. Exact remaining gap

For a lower target `S`, a spiral identity

\[
 S=\bigcap_{i=u}^vT_i
\]

only supplies an envelope in which `S` is legal.  It does not select a unique
physical interval `J_S`, ensure that all lower targets receive distinct
intervals, or ensure that choices for targets omitting a coordinate leave a
pin for every target containing it and for every central interval.

Thus the exact remaining theorem is:

> Choose physical witness intervals for all lower targets and choose the
> coordinate hitting sets allowed by Lemma 4 so that every assigned interval
> has exactly its target OR.

This is a combined containment/Hall/independent-transversal problem.  If the
term “spiral pinning problem” includes all three parts, it is the sole
remaining construction gate.  If “pinning” means only checking legal pins
after a matching is fixed, then a lower interval-assignment theorem remains
before it.

The defensible conclusion is now:

> The closed hex spiral solves two-sided shadow enumeration, admits a valid
> `M_a+2a` central factor, and automatically covers the upper half.  The only
> unresolved half is the joint lower matching-and-pinning problem.
