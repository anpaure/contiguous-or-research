# A width-plus-surface word for three central four-box layers

## 1. Outcome

Let

\[
 P_m=[0,m]^4,
 \qquad L_j=\{x\in P_m:|x|=j\},
 \qquad M_m=|L_{2m}|.
\]

The lexicographic selected-cover graph from
`CENTRAL_EULER_UPPER_UNIVERSALITY.md` has a second use: its edge
intersections form an explicit one-step factor.

### Theorem 1 (three-layer factor)

For every `m>=2`, there is a nonzero word of length

\[
                         M_m+O(m^2)                 \tag{1.1}
\]

whose contiguous coordinatewise maxima contain every point of

\[
                         L_{2m-2}\cup L_{2m-1}\cup L_{2m}. \tag{1.2}
\]

All witnesses supplied by the main construction have lengths one, two, or
three.  Only `O(m^2)` literal repairs are appended.

The result is independent of the still-open all-upper lexicographic
excursion lemma.  It is a proved lower-factor bridge for one additional
central layer.

## 2. Lexicographic selected-cover graph

Use `L_(2m-1)` as a vertex set.  For every `z in L_(2m)`, let `p<q` be its
first two positive coordinates and put in the edge

\[
 e_z=\{z-e_p,z-e_q\}.                               \tag{2.1}
\]

Its endpoint maximum is `z`.  Its endpoint minimum is

\[
                         b_z=z-e_p-e_q\in L_{2m-2}. \tag{2.2}
\]

At an endpoint `v` of `e_z`, define the half-edge label

\[
 \lambda_v(e_z)=i\quad\Longleftrightarrow\quad b_z=v-e_i. \tag{2.3}
\]

Thus the label is the coordinate present in `v` but absent from the edge
minimum.

## 3. Local factorable transitions

At every vertex, pair two incident half-edges whenever their labels in
(2.3) are different.  Since the selected-cover graph has degree at most
three, choose at most one such pair and leave every other half-edge
unpaired.  At a degree-two vertex with equal labels, leave both unpaired.

These transitions partition the graph edges into open trails and cycles.
Cut every cycle once.  There are only `O(m^2)` resulting trail pieces.

Indeed, outside

\[
 B=\{v:v_1\in\{0,m\}\text{ or }v_2\in\{0,m\}\},  \tag{3.1}
\]

we have `0<v_1,v_2<m`.  The two incident edges are obtained from
`v+e_1` and `v+e_2`, and their labels are respectively `2` and `1`.
They are therefore paired.  All unpaired half-edges lie at the
`O(m^2)` vertices of `B`.  A transition cycle meeting `B` is charged to a
chosen transition there, while a cycle avoiding `B` is a whole component
of the degree-two graph `G-B`; there are at most `(m+1)^2` such components.
This proves the surface-order trail bound.

## 4. The intersection word

Let one trail piece be

\[
 v_0,e_1,v_1,e_2,\ldots,e_h,v_h.                  \tag{4.1}
\]

Write down the word

\[
                         b_{e_1},b_{e_2},\ldots,b_{e_h}. \tag{4.2}
\]

Concatenate (4.2) over all trail pieces.  Exactly one entry is written for
every middle edge, so the un-repaired word has length exactly `M_m`.

At an internal trail vertex `v_j`, the two paired half-edge labels are
different.  Consequently

\[
 b_{e_j}=v_j-e_a,\qquad b_{e_{j+1}}=v_j-e_b,
 \qquad a\ne b,
\]

and hence

\[
                         b_{e_j}\vee b_{e_{j+1}}=v_j. \tag{4.3}
\]

Thus every vertex used by a paired transition is recovered by an adjacent
maximum.

For an edge `e_j` which is not the first or last edge of its trail, both
endpoint transitions are paired, so (4.3) at its two endpoints gives

\[
 b_{e_{j-1}}\vee b_{e_j}\vee b_{e_{j+1}}
   =v_{j-1}\vee v_j
   =z_j.                                             \tag{4.4}
\]

Thus every nonboundary middle edge colour is recovered by a triple maximum.

There are only `O(m^2)` trail endpoints and cuts.  Append literally every
rank-`2m-1` vertex not supplied by (4.3), and every rank-`2m` colour not
supplied by (4.4).  This costs `O(m^2)` positions.

## 5. Exact lower-colour deficit

The singleton values in (4.2) have a particularly simple image.

### Lemma 2

\[
 \{b_z:z\in L_{2m}\}
   =\{x\in L_{2m-2}:x_1<m,\ x_2<m\}.               \tag{5.1}
\]

Consequently exactly

\[
                         m(m-1)                    \tag{5.2}
\]

rank-`2m-2` points are missing.

### Proof

If `z_1>0`, coordinate 1 is one of the first two positive coordinates
unless both earlier positions existed, which is impossible; whenever
`z_1=m`, it is therefore decreased in (2.2).  If `z_1=0`, it stays zero.
Thus `(b_z)_1<m`; the same first-two-positive argument gives
`(b_z)_2<m`.

Conversely, let `x in L_(2m-2)` have `x_1,x_2<m`.  Then

\[
                         z=x+e_1+e_2              \tag{5.3}
\]

lies in the box and has coordinates 1 and 2 as its first two positive
coordinates.  Equation (2.2) gives `b_z=x`.

The missing points have `x_1=m` or `x_2=m`.  These two families are
disjoint at rank `2m-2`.  In either family the remaining three coordinates
sum to `m-2`, so the upper bounds are inactive and the count is

\[
 2\binom m2=m(m-1).
\]

This proves the lemma.  \(\square\)

Append these `m(m-1)` missing points literally.  Together with the
surface-order repairs in Section 4, equations (4.3)--(5.2) prove Theorem 1.

## 6. Useful exact local characterization

For completeness, almost every lower-central vertex is automatically
factorable.  Let `p<q` be the first two positive coordinates of a vertex
`v`.  All incident half-edge labels equal `p`, except that the edge obtained
from `v+e_p`, when legal, has label `q`.  Hence `v` has a good transition
if and only if it has at least two incident edges and `v_p<m`.

The vertices without a good transition number exactly

\[
                         m^2+m+1.                  \tag{6.1}
\]

Indeed, the degree-one vertices number `m(m-1)`.  Among vertices of degree
at least two, those with their first positive coordinate equal to `m`
number `2m+1`.  The sum is (6.1).  Cycle cuts may create a further
`O(m^2)` endpoint set, so the theorem uses the robust asymptotic repair
bound rather than depending on a particular choice of cuts.

## 7. Fixed-dimensional extension

The same argument works in `[0,m]^t` for every fixed `t>=3` at any rank
`r>m`.  Select the first two positive lower covers of every rank-`r` point.
Outside the four boundary slices `x_1 in {0,m}` or `x_2 in {0,m}`, every
rank-`r-1` vertex has the two factorable labels `1,2`.  The boundary and the
number of transverse line components are `O_t(m^(t-2))`.  The edge minima
cover every rank-`r-2` point with first two coordinates below `m`; the
missing boundary again has size `O_t(m^(t-2))`.

Therefore the three consecutive layers `r-2,r-1,r` admit a word of length

\[
                         |L_r^{(t)}|+O_t(m^{t-2}).  \tag{7.1}
\]

This is a genuine width-plus-one-lower-power construction, but it still
does not cover a linear number of layers.  The next target is to iterate
the intersection-factor mechanism without paying a new width-scale spine
at every depth.

## 8. Verification target

The accompanying checker should verify, for a range of `m`, the selected
edge minima, distinct-label transitions, trail decomposition, equations
(4.3)--(4.4), the exact deficit (5.2), and exhaustive coverage of all three
layers after repairs.
