# Independent audit of `LEX_THREE_LAYER_FACTOR.md`

## Verdict

The three-layer theorem is correct.  For every `m>=2`, the construction
really gives a nonzero word of length

\[
       |L_{2m}|+O(m^2)
\]

whose contiguous coordinatewise maxima contain all of
`L_(2m-2)`, `L_(2m-1)`, and `L_(2m)`.  The adjacent- and triple-window
factor equations are exact, the number of missing bottom-layer values is
exactly `m(m-1)`, and the remaining two repair families have surface order.

The fixed-dimensional extension is also valid, with the understood scope
`m>=2`, fixed `t>=3`, and an admissible rank `r>m` (empty layers outside the
box being harmless).  Its proof is genuinely uniform in `r`: fixing one
boundary coordinate or all transverse coordinates leaves only
`O_t(m^(t-2))` choices.

There are two minor presentation points, neither of which changes a theorem.

1. The degree-three claim imported from
   `CENTRAL_EULER_UPPER_UNIVERSALITY.md` should be read with the corrected
   incidence proof in that document's audit.  The original source's
   incidence list omitted increments in zero coordinates between the first
   two positive coordinates, although its degree bound was still correct.
2. The finite checker verifies the construction for tested values; it does
   not by itself prove either asymptotic `O(m^2)` statement or the
   fixed-dimensional extension.  Those conclusions come from the boundary
   and trail-count arguments below.

I found no false combinatorial assertion and no missing repair class.

An independent checker, `scratch/audit_lex_three_layer_factor.py`, tests the
same mechanism without reusing the four-dimensional source implementation.
It verifies 106 instances with `3<=t<=6`, `2<=m<=4`, and every
`m<r<=tm` in the selected ranges, including both extreme and central ranks.

## 1. Selected edges, minima, and half-edge labels

Let `z` have rank `2m`, and let `p<q` be its first two positive
coordinates.  Since no coordinate exceeds `m`, a rank-`2m` point has at
least two positive coordinates.  The selected edge has endpoints

\[
 u=z-e_p,\qquad v=z-e_q.
\]

They are distinct rank-`(2m-1)` points and satisfy

\[
 u\vee v=z.                                      \tag{1}
\]

Their coordinatewise minimum is

\[
 b_z=u\wedge v=z-e_p-e_q.                        \tag{2}
\]

At `u`, equation (2) reads `b_z=u-e_q`, so the half-edge label is `q`;
at `v` it reads `b_z=v-e_p`, so the label is `p`.  Thus definition (2.3)
in the source is unambiguous and always subtracts a positive coordinate.

At a lower vertex `v`, let `p<q` be its first two positive coordinates.
Every incident selected edge is obtained from some legal increment
`z=v+e_i`.  The exact degree formula is

\[
 \deg(v)=\#\{i\le q:v_i<m\}.                     \tag{3}
\]

For `q<=3`, this is at most three.  For `q=4`, the only two positive
coordinates sum to `2m-1`; one of them is `m`, so again at most three of the
four increments are legal.  This supplies the corrected proof of the
degree bound used in Section 3.

The half-edge labels at `v` have an equally simple form.  Every incident
label is `p`, except that the edge from `v+e_p`, when legal, has label `q`.
Indeed:

* an increment before `p` selects `(i,p)` and labels the half-edge at `v`
  by `p`;
* the increment at `p` selects `(p,q)` and labels it by `q`;
* an increment strictly between `p` and `q`, or at `q`, labels it by `p`.

It follows that a distinct-label transition exists exactly when
`deg(v)>=2` and `v_p<m`, as claimed in Section 6.

## 2. Surface-order trail decomposition

Put

\[
 B=\{v:v_1\in\{0,m\}\text{ or }v_2\in\{0,m\}\}.
\]

If `v` is outside `B`, its first two positive coordinates are `1,2`, both
increments are legal, and (3) shows that these are its only incident edges.
Their half-edge labels are respectively `2` and `1`, so the prescribed
transition pairs them.  Therefore every unpaired half-edge belongs to a
vertex in `B`.

The layer slice obtained after fixing one coordinate to `0` or `m` has at
most `(m+1)^2` points: choose two of the three remaining coordinates and
the rank equation fixes the last.  Hence

\[
                         |B|=O(m^2).              \tag{4}
\]

The selected transitions partition the edges into open transition trails
and transition cycles.  The number of open trails is at most half the
number of unpaired half-edges, hence `O(m^2)` by (3)--(4).

A transition cycle meeting `B` can be charged injectively to one paired
transition at a boundary vertex on that cycle.  A transition cycle avoiding
`B` uses all two incident edges at every vertex it meets.  It is therefore
an entire component of `G-B`.  After `(v_3,v_4)` is fixed, the rank equation
fixes `v_1+v_2`, and the remaining internal points form one line segment.
Thus `G-B` has at most `(m+1)^2` components.  Cutting every transition cycle
once consequently leaves

\[
                         T=O(m^2)                 \tag{5}
\]

trail pieces.  This argument includes cycles created by the transition
choice inside a graph component that is not globally Eulerian.

## 3. Factor equations

Consider one trail

\[
 v_0,e_1,v_1,e_2,\ldots,e_h,v_h
\]

and write `b_j=b_(e_j)`.  At an internal trail vertex `v_j`, the two
paired labels are distinct, say `a!=b`, so

\[
 b_j=v_j-e_a,\qquad b_{j+1}=v_j-e_b.
\]

Taking the coordinatewise maximum restores the two separately omitted
coordinates:

\[
                         b_j\vee b_{j+1}=v_j.      \tag{6}
\]

For `1<j<h`, applying (6) at both endpoints of `e_j` gives

\[
 \begin{aligned}
 b_{j-1}\vee b_j\vee b_{j+1}
   &=(b_{j-1}\vee b_j)\vee(b_j\vee b_{j+1})\\
   &=v_{j-1}\vee v_j\\
   &=z_j,                                         \tag{7}
 \end{aligned}
\]

where `z_j` is the color of `e_j`; the last equality is (1).  These are
literal adjacent and triple windows in the word of edge minima.  No
cross-trail adjacency is used.

Every vertex missed by (6) is either associated with an unpaired/cut
transition or lies in the surface set, so there are `O(m^2)` such vertices.
Every edge color missed by (7) is a first or last trail edge, so there are
at most `2T=O(m^2)` such colors.  Appending these missing values literally
does not disturb any existing witness and covers each repair by a singleton.

## 4. Exact bottom-layer image and deficit

For every selected edge minimum, the first coordinate is below `m`: if
`z_1>0`, coordinate 1 is selected and decreased, and if `z_1=0` it remains
zero.  The same holds for coordinate 2, because at most coordinate 1 can
precede it.  Therefore

\[
 \{b_z:z\in L_{2m}\}
 \subseteq\{x\in L_{2m-2}:x_1<m,\ x_2<m\}.       \tag{8}
\]

Conversely, for any point on the right of (8),

\[
                         z=x+e_1+e_2
\]

lies in the box, has rank `2m`, and has `1,2` as its first two positive
coordinates.  Its selected minimum is exactly `x`, proving equality in
(8).

The missing bottom points have `x_1=m` or `x_2=m`.  The two cases are
disjoint because the total rank is `2m-2`.  In either case the other three
coordinates have sum `m-2`; their upper bounds are inactive, so there are
`C(m,2)` points.  Hence the deficit is exactly

\[
                         2\binom m2=m(m-1).        \tag{9}
\]

These values are also appended literally.  Since `m>=2`, all constructed
and repaired entries have positive rank, so the resulting word is nonzero.
Equations (5)--(9) prove the stated length and coverage.

## 5. Audit of the exact local count

The compressed proof of equation (6.1) in the source is correct.  Here is
the full count.

A degree-one vertex must have its first two positive coordinates in
positions `1,2`, with exactly one of these two coordinates equal to `m`.
If `v_1=m`, then `v_2>=1` and

\[
 (v_2-1)+v_3+v_4=m-2,
\]

giving `C(m,2)` possibilities; the case `v_2=m` is symmetric.  Thus there
are `m(m-1)` degree-one vertices.

Now require `v_p=m` and degree at least two.  If `p=1`, this forces
`v_2=0`, and `v_3+v_4=m-1`, giving `m` vertices.  If `p=2`, then `v_1=0`
and again there are `m` choices for `(v_3,v_4)`.  If `p=3`, there is the
single vertex `(0,0,m,m-1)`.  The total is `2m+1`.  The two classes are
disjoint and exhaust the vertices without a distinct-label transition, so

\[
                         m(m-1)+(2m+1)=m^2+m+1.
\]

Cycle cuts can make additional endpoints, which is why the theorem
correctly uses an asymptotic repair count rather than this number as its
complete repair total.

## 6. Fixed-dimensional extension

Let `t>=3` be fixed, work in `[0,m]^t`, and let `r>m`.  Every rank-`r`
point has at least two positive coordinates, so the selected edge is always
defined.  Use rank-`(r-1)` vertices and the identical different-label
transition rule.

Outside

\[
 B_t=\{v:v_1\in\{0,m\}\text{ or }v_2\in\{0,m\}\},
\]

the first two coordinates are positive and nonfull.  Exactly the increments
in coordinates 1 and 2 are incident, and their half-edge labels differ.
Thus all unpaired transitions occur in `B_t`.

After one boundary coordinate is fixed, choosing `t-2` of the remaining
coordinates determines the last one from the rank equation.  Hence

\[
                         |B_t|=O_t(m^{t-2})        \tag{10}
\]

uniformly in `r`.  After the transverse tuple `(v_3,...,v_t)` is fixed,
the nonboundary graph is one `(v_1,v_2)` line segment.  There are at most
`(m+1)^(t-2)` such tuples.  The trail and cycle argument from Section 2
therefore gives `O_t(m^(t-2))` pieces and hence the same number of
rank-`(r-1)` and rank-`r` repairs.

The edge-minimum image is exactly

\[
 \{x\in L_{r-2}^{(t)}:x_1<m,\ x_2<m\},           \tag{11}
\]

by the same `x -> x+e_1+e_2` inverse.  Its complement lies in the two
boundary slices `x_1=m` or `x_2=m`, each of size `O_t(m^(t-2))` by the
same choose-all-but-one argument.  Appending that complement proves

\[
 |L_r^{(t)}|+O_t(m^{t-2})
\]

for the three layers `r-2,r-1,r`.  This is a theorem, not an extrapolation
from the four-dimensional checker.

## 7. What the checkers do and do not establish

The source checker correctly:

* constructs one selected edge for every middle point;
* pairs only distinct half-edge labels;
* partitions every edge into exactly one trail, cutting residual cycles;
* verifies (6) and (7) on the resulting trail words;
* verifies the exact bottom deficit `m(m-1)`;
* appends all three repair families and exhaustively checks every desired
  target using windows of length at most three.

It passes through the stated tested range.  Its observed exact counts for
its particular deterministic pairing are stronger than the theorem needs,
but those patterns are checker evidence unless separately proved.

The independent checker added with this audit generalizes the construction
to arbitrary fixed dimension and rank.  It verifies the exact minimum image,
all local factor equations, the nonboundary line structure, and exhaustive
defect counts in 106 small instances.  It likewise serves as regression
evidence; the all-`m` and fixed-`t` conclusions rest on the proofs above.

