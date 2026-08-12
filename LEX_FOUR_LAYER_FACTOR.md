# One lexicographic factor word covers four central layers

## 1. Main theorem

Let

\[
 P_m=[0,m]^4,\qquad L_j=\{x\in P_m:|x|=j\},\qquad
 M_m=|L_{2m}|.
\]

For every middle point `z in L_(2m)`, select the edge between the lower
covers obtained by subtracting from the first two positive coordinates of
`z`, and put

\[
                         b_z=z-e_p-e_q\in L_{2m-2}. \tag{1.1}
\]

Use the distinct-half-edge-label transition trails from
`LEX_THREE_LAYER_FACTOR.md`, and write the sequence of `b_z` values along
each trail.

### Theorem 1 (four-layer lexicographic factor)

For every `m>=2`, one can append `O(m^2)` literal repairs to this single
`M_m`-entry edge-minimum word so that its contiguous coordinatewise maxima
cover

\[
              L_{2m-2}\cup L_{2m-1}\cup L_{2m}\cup L_{2m+1}. \tag{1.2}
\]

Consequently these four consecutive layers have a nonzero word of length

\[
                         M_m+O(m^2).                 \tag{1.3}
\]

The lower three layers are the earlier factor theorem.  The new point is
that the very same word covers the first upper layer with only surface-order
repairs.

## 2. Canonical pair above every middle point

Fix `y in L_(2m+1)`, and let `i<j` be its first two positive coordinates.
Define

\[
 z_i=y-e_i,\qquad z_j=y-e_j,
 \qquad v=y-e_i-e_j.                               \tag{2.1}
\]

The selected edges of both `z_i` and `z_j` meet at `v`.  Indeed, coordinate
`j` is one of the first two positive coordinates of `z_i`, and coordinate
`i` is one of the first two positive coordinates of `z_j`, including when
one of `y_i,y_j` equals one.  Hence

\[
                         z_i\vee z_j=y.              \tag{2.2}
\]

The two half-edge labels at `v` are especially important, but there is one
small boundary case.  Let `k>j` be the next positive coordinate of `y`;
such a coordinate exists because `|y|=2m+1` while two coordinates hold at
most `2m`.  The labels of the two canonical half-edges are

\[
 \lambda_v(e_{z_i})=
   \begin{cases}i,&y_i\ge2,\\ k,&y_i=1,\end{cases}
 \qquad
 \lambda_v(e_{z_j})=
   \begin{cases}j,&y_j\ge2,\\ k,&y_j=1.\end{cases}       \tag{2.3}
\]

Indeed `b_{z_i}=v-e_{\lambda_v(e_{z_i})}` and similarly for `z_j`.
The two labels are distinct unless

\[
                         y_i=y_j=1.                 \tag{2.4}
\]

Because `i,j` are the first two positive positions, (2.4) is possible in
four dimensions only for

\[
                    (1,1,m-1,m),\qquad(1,1,m,m-1). \tag{2.5}
\]

Append these at most two targets literally.  Every other canonical pair is
an admissible distinct-label factor transition.

## 3. Four consecutive minima recover the upper target

Suppose the chosen transition at `v` pairs the canonical edges.  In their
trail order, write them as `e_k,e_(k+1)`.  Suppose in addition that neither
is a first or last edge of its trail.  Then the surrounding edge-minimum
word contains

\[
 b_{e_{k-1}},\ b_{e_k},\ b_{e_{k+1}},\ b_{e_{k+2}}. \tag{3.1}
\]

The established triple-factor identity gives

\[
\begin{aligned}
 b_{e_{k-1}}\vee b_{e_k}\vee b_{e_{k+1}}&=z_i,\\
 b_{e_k}\vee b_{e_{k+1}}\vee b_{e_{k+2}}&=z_j.
\end{aligned}                                      \tag{3.2}
\]

Taking the maximum of all four entries and using (2.2),

\[
 b_{e_{k-1}}\vee b_{e_k}\vee b_{e_{k+1}}\vee b_{e_{k+2}}
                         =y.                        \tag{3.3}
\]

Thus every nonexceptional first-upper target is a literal length-four
window of the same factor word.

## 4. Exact failure charging

Let `T` be the number of open trail pieces after cutting transition cycles.
The earlier boundary argument proves

\[
                              T=O(m^2).              \tag{4.1}
\]

Let `D` be the set of middle edges which are first or last in a trail.
Then

\[
                              |D|\le2T.              \tag{4.2}
\]

A target `y` outside the two-element family (2.5) can fail the proof of
(3.3) for only two reasons.

### A. Its canonical pair is not chosen at `v`

Because the labels in (2.3) differ, a degree-two vertex is forced to pair
them.  Failure is possible only at a degree-three vertex, where the
construction chooses one of the two distinct-label pairs.  The number of
degree-three vertices is exactly

\[
                            m(m+1)+2.                \tag{4.3}
\]

For a fixed `v`, at most six upper targets have `v` as canonical junction:
choosing the two decremented coordinates determines `y` uniquely.  Hence
class A contains at most

\[
                         6\bigl(m(m+1)+2\bigr)       \tag{4.4}
\]

targets.

### B. A canonical edge lies in `D`

For a fixed middle colour `z`, an upper neighbour has form `z+e_h` in one
of at most four legal coordinates.  Therefore `z` is a canonical edge for
at most four targets.  Charging a failed target to either boundary edge of
its canonical pair gives at most

\[
                              4|D|\le8T              \tag{4.5}
\]

targets in class B.

Combining (2.5) and (4.4)--(4.5), the number of rank-`(2m+1)` literal
repairs is at most

\[
              2+6\bigl(m(m+1)+2\bigr)+8T=O(m^2).  \tag{4.6}
\]

The lower theorem already uses only `O(m^2)` repairs for ranks
`2m-2,2m-1,2m`.  Appending the additional family (4.6) proves Theorem 1.

This charge is robust: it does not assume an optimal transition choice,
trail orientation, or ordering of the trail pieces.

## 5. Fixed-dimensional extension

Let `t>=3` be fixed, work in `[0,m]^t`, and take any rank `r>m`.
Select the first-two-positive lower-cover edge below every point of rank
`r`, use distinct-label transition trails, and write their rank-`(r-2)`
edge minima.

The earlier proof gives ranks `r-2,r-1,r`.  For `y` of rank `r+1`, its
first two positive coordinates again produce a canonical pair.  Equal
half-edge labels require both of those coordinates to equal one; this
exceptional family has `O_t(m^(t-3))` members and may be appended
literally.  Away from it and the four slices

\[
 x_1\in\{0,m\}\quad\text{or}\quad x_2\in\{0,m\},   \tag{5.1}
\]

the graph is a forced degree-two line.  The number of boundary vertices,
unpaired half-edges, transverse line components, and trail cuts is
`O_t(m^(t-2))`.  Each exceptional vertex or boundary edge has only
`O_t(1)` canonical upper targets.

Therefore the same word covers four consecutive ranks

\[
                         r-2,r-1,r,r+1              \tag{5.2}
\]

with length

\[
                         |L_r^{(t)}|+O_t(m^{t-2}).   \tag{5.3}
\]

## 6. Consequence and next target

Both first derivatives are no longer separate constructions.  One
edge-minimum word simultaneously realizes

\[
 L_{r-2}\xrightarrow{\text{adjacent pairs}}
 L_{r-1}\xrightarrow{\text{triple windows}}
 L_r\xrightarrow{\text{four-windows}}
 L_{r+1},                                           \tag{6.1}
\]

up to one surface-size repair set.

The next genuinely new layer is `r+2`.  Reaching it requires stitching
two or more canonical central transitions, or proving a bounded-defect
ordering of the transition trails.  The failure of the old rotation-system
excursion lemma begins only there from the perspective of this four-layer
factor: it does not obstruct either adjacent derivative.

## 7. Status

Proved:

* one word of length `M_m+O(m^2)` covers four central layers in the
  four-box;
* every new upper failure is charged with bounded multiplicity to a
  degree-three transition or trail-boundary edge;
* the result extends to fixed dimension with one-lower-power error.

Not proved:

* rank `2m+2` or deeper upper coverage by the same word;
* iteration through a linear number of layers;
* a full-box `M_m+o(m^3)` construction.
