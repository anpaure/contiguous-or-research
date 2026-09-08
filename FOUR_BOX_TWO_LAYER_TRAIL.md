# A near-width word for two central layers of the four-box

## Status

This note proves a positive fixed-dimensional construction.  It does **not**
yet cover the whole box, but it covers the two layers immediately below and
at the middle of `[0,m]^4` in one word of length equal to the middle-layer
size plus only `O(m^2)` terms.

This is important because it evades the intact-middle-row and portal-grid
barriers: the lower layer itself is used as the alphabet, and the middle
layer is produced by adjacent coordinatewise maxima.

## Statement

For `s >= 0`, write

```
L_s(m) = {x in {0,...,m}^4 : x_1+x_2+x_3+x_4=s}
```

and let

```
M_m = |L_{2m}(m)|.
```

### Theorem 1 (two-layer trail)

For every `m >= 1` there is a word

```
W=(w_1,...,w_N),        w_i in L_{2m-1}(m),
```

such that

1. every point of `L_{2m-1}(m)` occurs as a singleton entry of `W`;
2. every point of `L_{2m}(m)` is the coordinatewise maximum of two
   consecutive entries of `W`; and
3. `N=M_m+O(m^2)`.

One explicit bound supplied by the proof is

```
N <= M_m + (27m^2+19m+2)/2.
```

The half-integral displayed expression is only a convenient real upper
bound; of course `N` is an integer.

## Construction of the edge-coloured graph

Make the lower layer `L_{2m-1}(m)` the vertex set of a graph `G`.

For each `z in L_{2m}(m)`, choose two distinct positive coordinates of `z`.
If `z_1,z_2>0`, choose coordinates `1,2`.  Otherwise choose any two positive
coordinates, for example the lexicographically first two.  Such a pair
always exists: a vector supported on one coordinate has sum at most `m`,
whereas `z` has sum `2m`.

If the chosen coordinates are `i,j`, insert the edge

```
(z-e_i)(z-e_j)
```

and colour it by `z`.  Both endpoints lie in `L_{2m-1}(m)`, and

```
max(z-e_i,z-e_j)=z                                      (1)
```

coordinatewise.  There is exactly one edge for every middle-layer point, so

```
|E(G)|=M_m.                                             (2)
```

## Boundary localization

Put

```
B={v in L_{2m-1}(m): v_1 in {0,m} or v_2 in {0,m}}.
```

Every vertex outside `B` has degree exactly two in `G`.

Indeed, if `0<v_1,v_2<m`, the middle points `v+e_1` and `v+e_2` both use
the preferred pair `{1,2}`, so they contribute two incident edges.  A point
`v+e_i` with `i=3,4` also has positive first two coordinates, but its chosen
edge has endpoints obtained by subtracting `e_1` and `e_2`, and hence is not
incident with `v`.  Finally, an exceptional middle point with `z_1=0` or
`z_2=0` has all endpoints on the corresponding boundary hyperplane, so it
cannot create another edge at `v`.

After deleting `B`, fix `(v_3,v_4)`.  The remaining possible pairs
`(v_1,v_2)` form a consecutive integer interval on the line

```
v_1+v_2=2m-1-v_3-v_4,
```

and the preferred `{1,2}` edges join consecutive pairs.  Thus `G-B` is a
union of at most one path for each `(v_3,v_4)`.  In particular,

```
components(G-B) <= (m+1)^2.                             (3)
```

Adding the boundary vertices back can increase the number of components by
at most `|B|`, while every odd-degree or isolated vertex of `G` lies in `B`.
Therefore

```
c(G) <= (m+1)^2+|B|,
o(G) <= |B|,
i(G) <= |B|,                                            (4)
```

where `c,o,i` denote the numbers of components, odd-degree vertices, and
isolated vertices.

A crude boundary count is enough.  On `v_1=0`, ignoring the upper bounds
gives at most `C(2m+1,2)` solutions.  On `v_1=m`, the remaining sum is
`m-1`, giving exactly `C(m+1,2)` unrestricted solutions; the same estimates
hold for coordinate 2.  Hence

```
|B| <= 2[C(2m+1,2)+C(m+1,2)] = 5m^2+3m.                (5)
```

## Euler-trail linearization

Every nontrivial connected component with `o_C` odd vertices has an edge
partition into

```
max(1,o_C/2)
```

trails.  This follows by pairing odd vertices with auxiliary edges, taking
an Euler circuit, and deleting the auxiliary edges.  Consequently all edges
of `G` can be partitioned into at most

```
c(G)+o(G)/2
```

trails.  Write down the vertex sequence of every trail, concatenate these
sequences in arbitrary order, and finally append every isolated vertex.

Every graph edge appears as one adjacent pair inside its trail.  Equation
(1) therefore covers every point of `L_{2m}`.  Every nonisolated lower point
appears in a trail vertex sequence, and the isolated lower points were
appended, so every point of `L_{2m-1}` appears literally.

If there are `q` trails, their vertex sequences have total length
`|E(G)|+q`.  Equations (2)--(5) give

```
N <= M_m + (m+1)^2 + (3/2)|B|
             + |B|
  <= M_m + (m+1)^2 + (5/2)(5m^2+3m)
   = M_m + (27m^2+19m+2)/2.
```

This proves Theorem 1.

## Fixed-dimensional generalization

The same proof works in every fixed dimension `t>=3`.  Let

```
L_s^{(t)}(m)={x in {0,...,m}^t : sum x_i=s}.
```

For any rank `r>m`, put one edge below every `z in L_r^{(t)}(m)`, using the
preferred coordinate pair `{1,2}` whenever possible.  The exceptional lower
vertices lie on `x_1 in {0,m}` or `x_2 in {0,m}`, a union of four
`(t-2)`-dimensional slices containing `O_t(m^{t-2})` points.  Away from those
slices every vertex has degree two, and after fixing coordinates `3,...,t`
one obtains a path.  Hence there is a word of points in
`L_{r-1}^{(t)}(m)` of length

```
|L_r^{(t)}(m)|+O_t(m^{t-2})
```

covering `L_{r-1}^{(t)}(m)` as singletons and `L_r^{(t)}(m)` as adjacent
maxima.

At the central rank this error is one full power of `m` below the width.

## What this does and does not solve

The theorem gives a genuine `width + lower-order` factor bridge for the two
central layers.  It shows that the earlier cubic losses were artifacts of
preserving intact middle blocks or assigning one rigid portal to each
endpoint.

It does not yet produce a universal word for all of `[0,m]^4`.  The next
mathematical problem is to label or refine the trail vertices so that their
shorter-window maxima cover the entire lower half and their longer-window
maxima cover the upper half, while retaining only `o(m^3)` additional
positions.  Equivalently, the two-layer trail should become the central
spine of a variable-band factor, not be concatenated with one construction
per rank.
