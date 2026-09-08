# A width-plus-surface word for the upper three central four-box layers

## 1. Result

Let

\[
 P_m=[0,m]^4,\qquad L_j=\{x\in P_m:|x|=j\},\qquad
 M_m=|L_{2m}|.
\]

Use the lexicographic selected-cover graph `G_m`: its vertices are
`L_(2m-1)`, and the edge below `z in L_(2m)` joins the lower covers obtained
by subtracting from the first two positive coordinates of `z`.

### Theorem 1 (upper three-layer arm word)

For every `m>=2`, there is a nonzero word of length

\[
                         M_m+O(m^2)                 \tag{1.1}
\]

whose contiguous coordinatewise maxima contain every point of

\[
                         L_{2m-1}\cup L_{2m}\cup L_{2m+1}. \tag{1.2}
\]

The construction is explicit.  It concatenates every maximal forced
degree-two arm of `G_m` in an arbitrary order and orientation, then appends
only `O(m^2)` exceptional rank-`(2m+1)` targets literally.

This theorem does not use the false within-trail all-upper excursion lemma.
It shows that the first upper derivative layer is automatic away from the
surface kernel.

## 2. Canonical two-edge witness for every upper neighbour

Take `y in L_(2m+1)`, and let `i<j` be its first two positive coordinates.
Put

\[
              z_i=y-e_i,\qquad z_j=y-e_j,
              \qquad v=y-e_i-e_j.                 \tag{2.1}
\]

Both `z_i,z_j` lie in `L_(2m)`, while `v` lies in `L_(2m-1)`.

### Lemma 2 (canonical junction)

The selected edges below `z_i` and `z_j` both have endpoint `v`.  Hence

\[
                         z_i\vee z_j=y.             \tag{2.2}
\]

### Proof

In `z_i`, coordinate `j` is one of the first two positive coordinates:
if `y_i>1`, the first two remain `i,j`; if `y_i=1`, coordinate `i`
vanishes and `j` becomes first positive.  Therefore subtracting `e_j`
from `z_i` is one of its two selected lower covers, and that cover is `v`.

Symmetrically, coordinate `i` is one of the first two positive coordinates
of `z_j`.  If `y_j=1`, a third positive coordinate exists because two box
coordinates contain at most `2m<2m+1` units; coordinate `i` remains the
first positive one.  Thus `z_j-e_i=v` is selected as well.

Finally the two colours omit different coordinates from `y`, so their
coordinatewise maximum is `y`.  \(\square\)

Thus every first-upper target already has a length-two path in its induced
selected graph.  No connected-component or reverse-greedy argument is
needed at this depth.

## 3. Forced arms and automatic witnesses

Let

\[
                         K_m=\{v\in L_{2m-1}:\deg_{G_m}(v)\ne2\}. \tag{3.1}
\]

The exact directed-degree count gives

\[
                         |K_m|=2m^2+2.              \tag{3.2}
\]

Cut `G_m` at every vertex of `K_m`; cut the unique all-degree-two component
once.  The resulting maximal arms partition all middle edges and number

\[
                         2m^2+m+4.                  \tag{3.3}
\]

Write every arm as either of its two vertex sequences and concatenate the
arm words arbitrarily.  The length before repairs is exactly

\[
                         M_m+2m^2+m+4.              \tag{3.4}
\]

Every lower-central vertex occurs as a singleton, and every middle colour
is the maximum of the adjacent endpoints of its edge.

Now let `y` have canonical junction `v` from (2.1).  If `v notin K_m` and
`v` is not the one artificial cycle-cut vertex, its two incident edges are
exactly the edges below `z_i,z_j` and are consecutive in one forced arm.
Writing the local arm segment as

\[
                          a,\ v,\ b,
\]

we obtain

\[
 a\vee v=z_i,\qquad v\vee b=z_j,
 \qquad a\vee v\vee b=y.                           \tag{3.5}
\]

So `y` is a literal length-three window, independently of every choice of
arm order and orientation.

## 4. Surface repair bound

A kernel vertex can be the canonical junction for at most
`C(4,2)=6` targets: once the two decremented coordinates are specified,
equation (2.1) recovers `y` uniquely.  The artificial cycle cut spoils at
most another six canonical junctions.  Therefore the number of targets not
certified by (3.5) is at most

\[
                         6|K_m|+6=12m^2+18.         \tag{4.1}
\]

Append all of these exceptional targets literally.  This proves

\[
 |W|\le M_m+2m^2+m+4+12m^2+18
      =M_m+14m^2+m+22.                             \tag{4.2}
\]

The constant is deliberately crude.  The exact exceptional family is much
smaller; only the surface order matters here.

Appending literal targets cannot destroy any existing interval witness.
All entries are nonzero, so (4.2) proves Theorem 1.

## 5. Fixed-dimensional form

The proof works verbatim in `[0,m]^t` for fixed `t>=3` and rank `r>m`.
For `y in L_(r+1)`, decrement its first two positive coordinates to obtain
two rank-`r` colours sharing a selected rank-`(r-1)` cover.  Away from the
four boundary slices

\[
                 x_1\in\{0,m\}\quad\text{or}\quad
                 x_2\in\{0,m\},                    \tag{5.1}
\]

the selected graph is a forced degree-two `{1,2}` line.  The boundary,
the number of transverse lines, and the number of canonical junctions on
the boundary are all `O_t(m^(t-2))`.

Consequently the three consecutive ranks `r-1,r,r+1` have a word of length

\[
                         |L_r^{(t)}|+O_t(m^{t-2}).   \tag{5.2}
\]

For `t=4`, this is exactly width plus surface order.

## 6. Relation to the lower three-layer factor

`LEX_THREE_LAYER_FACTOR.md` constructs a different word of length
`M_m+O(m^2)` covering

\[
                         L_{2m-2},L_{2m-1},L_{2m}.
\]

The present theorem covers

\[
                         L_{2m-1},L_{2m},L_{2m+1}.
\]

Thus both one-step directions are now individually solved at
width-plus-surface cost using the same selected-cover graph:

* edge minima factor one layer downward;
* canonical two-edge junctions extend one layer upward.

The remaining general problem is not either first derivative.  It is to
iterate the two mechanisms through a linear number of ranks while retaining
one width-scale spine.  Any successful recursive factor should preserve
the canonical junction (2.1) and the distinct-label minimum transition at
the same time.

## 7. Exact scope

Proved:

* a direct `M_m+O(m^2)` word for the upper three central layers;
* an explicit length bound `M_m+14m^2+m+22`;
* a canonical two-edge witness for every first-upper target;
* a fixed-dimensional `|L_r|+O_t(m^(t-2))` extension.

Not proved:

* simultaneous use of the upper and lower three-layer words without paying
  two copies of `M_m`;
* coverage of ranks at distance two or more from the spine;
* the surface-defect virtual-seam lemma for the full upper half.
