# Central Euler spines and the upper half of the four-box

## 1. Outcome

Put

\[
 P_m=[0,m]^4,\qquad
 V_m=\{v\in P_m:|v|=2m-1\},\qquad
 Z_m=\{z\in P_m:|z|=2m\}.
\]

The direct two-layer construction can be strengthened at the graph level.
For every `z` in `Z_m`, join the two lower covers obtained by subtracting
from the **first two positive coordinates of `z`**.  Call the resulting
edge-coloured graph `G_m`, with the edge below `z` coloured by `z`.

The main theorem proved here is:

> For every upper target `y in P_m`, `|y|>=2m`, the subgraph of `G_m`
> consisting of the colours `z<=y` has a connected component whose
> coordinatewise maximum is exactly `y`.

Thus the elementary lexicographic edge selection is already simultaneously
correct for **every** upper target.  The remaining obstruction is only the
linear ordering of those edges.  More precisely, one must choose the local
Euler transitions at `O(m^2)` degree-three vertices so that every one of the
above facet-spanning components leaves a facet-spanning consecutive
excursion.

This isolates a single simultaneous-transition lemma which would give a
word of length

\[
                 |Z_m|+O(m^2)
\]

covering the lower central layer, the middle layer, and the entire upper
half of the box.  The lemma is not proved here.  Component connectivity by
itself must not be confused with consecutiveness in one Euler word.

The second theorem proves that an intact natural-line architecture covering
both the lower central layer and the upper half cannot supply that missing
ordering: it costs an additional `Omega(m^3)`.  Hence
the successful ordering must splice or split the natural lines, most
naturally by recursively organizing their facet endpoints.

## 2. The selected-cover graph

If the positive coordinates of `z in Z_m` begin at positions `p<q`, put

\[
 e_z=\{z-e_p,z-e_q\}.                              \tag{2.1}
\]

There are always at least two positive coordinates, since one coordinate is
at most `m` whereas `|z|=2m`.  Equation (2.1) therefore gives one genuine
edge for every middle point.  Its endpoint maximum is

\[
                    (z-e_p)\vee(z-e_q)=z.          \tag{2.2}
\]

Consequently any trail decomposition of `G_m`, written as vertex words,
covers all of `Z_m` by adjacent pairs.

For `y in P_m`, define

\[
 G_m[y]=\bigl(V_m\cap[0,y],\{e_z:z\in Z_m, z\le y\}\bigr). \tag{2.3}
\]

The equality in (2.3) is exact: both endpoints of `e_z` lie below `y` if
and only if their maximum `z` lies below `y`.

For a coordinate `i`, let

\[
 F_i(y)=\{v\in V_m:v\le y,\ v_i=y_i\}.             \tag{2.4}
\]

A set of allowed vertices has maximum `y` precisely when it meets all four
families in (2.4).

## 3. Deficit coordinates

Write

\[
                 D=|y|-2m.
\]

Every allowed lower vertex has the unique form

\[
                 v=y-\delta,\qquad
 |\delta|=D+1,\quad 0\le\delta\le y.                \tag{3.1}
\]

Every allowed middle colour has the form

\[
                 z=y-\varepsilon,\qquad
 |\varepsilon|=D,\quad 0\le\varepsilon\le y.       \tag{3.2}

If `p,q` are the first two positive coordinates of `z`, the edge below `z`
joins the two deficit vectors

\[
                 \varepsilon+e_p,qquad
                 \varepsilon+e_q.                  \tag{3.3}
\]

Thus the upper problem induced by `y` is a bounded-composition graph of
depth only `D+1`.  The target is covered by a walk in this graph exactly
when the coordinatewise minimum of its visited deficit vectors is zero.

## 4. Lexicographic component theorem

The following statement is slightly more general than the four-box case.

### Theorem 1 (reverse-greedy component)

Let `s>=2`, let `y in N^t` satisfy

\[
                 |y|\ge s,\qquad y_i\le s-1\quad(1\le i\le t). \tag{4.1}
\]

On the rank-`(s-1)` points below `y`, put one edge below every rank-`s`
point `z<=y`, joining the lower covers in the first two positive
coordinates of `z`.  Then this graph has a connected component with
coordinatewise maximum `y`.

### Proof

Put `S=s-1`.  Form the reverse-greedy rank-`S` point `x<=y`: starting with
coordinate `t` and moving left, fill each coordinate to its capacity `y_i`
until total mass `S` has been placed.  If `p` is the first positive
coordinate of `x`, then

\[
 x_i=0\ (i<p),\qquad x_i=y_i\ (i>p),\qquad x_p\le y_p. \tag{4.2}
\]

In fact we construct one simple path from `x` which visits every facet.

Coordinates `i>p` already attain their target values at `x`.  Process the
coordinates

\[
                         p,p-1,\ldots,1              \tag{4.3}
\]

in that order.  At the stage for coordinate `i`, all coordinates before
`i` are still zero.  If the current value is below `y_i`, let `q>i` be the
first positive coordinate after `i` and set

\[
 z=x+e_i,\qquad x'=x+e_i-e_q.                       \tag{4.4}
\]

All coordinates before `i` and between `i` and `q` are zero.  Hence `i,q`
are the first two positive coordinates of `z`, and (4.4) is a selected edge
below `y`.  Since `y_i<=S`, the other coordinates contain enough total mass
to repeat this until coordinate `i` equals `y_i`.  Record that facet and
continue with `i-1`.  Coordinates saturated earlier may subsequently donate
mass, but their facets have already been visited.

If `y_i=0`, every allowed point already lies on its `i`-facet.  We have
therefore found one path attaining `y_i` for every coordinate `i`.  Its
maximum is at most `y` and at least `y` coordinate by coordinate, so it is
exactly `y`.  Every move transfers a unit from a later coordinate to an
earlier one, and hence strictly decreases

\[
                         \Phi(x)=\sum_i i x_i.        \tag{4.5}
\]

The path is therefore simple and has `O_t(s)` edges.  QED.

### Corollary 2 (all upper targets pass the graph-selection gate)

For `s=2m`, every coordinate of `y in P_m` is at most `m<=2m-1`.
Theorem 1 therefore applies to every `|y|>=2m`.  In particular,

\[
 \boxed{\text{every }G_m[y]\text{ has a facet-spanning component}.} \tag{4.6}
\]

This proves that the preferred-pair rule does not miss any upper target at
the level of connected paths.  The finite checker

```
python3 scratch/check_induced_deficit_components.py 8
```

independently reconstructs all selected graphs and checks (4.6) through
`m=8`; the proof above is valid for every `m`.

## 5. Exact interval-versus-component distinction

Let a trail in `G_m` have vertex word

\[
                 W=(w_0,w_1,\ldots,w_h).
\]

For a fixed target `y`, delete conceptually every letter not below `y`.
Do **not** close the resulting gaps.  The remaining letters form maximal
consecutive `y`-runs in the original word.

### Lemma 3 (excursion criterion)

The trail word contains an interval with maximum `y` if and only if one of
its maximal `y`-runs meets every facet `F_i(y)`.

### Proof

Every interval with maximum `y` consists only of letters below `y` and
meets every facet.  The maximal `y`-run containing it has the same two
properties.  Conversely, the whole of a facet-spanning `y`-run is itself a
witness for `y`.  QED.

Every `y`-run traces a path in `G_m[y]`.  The converse is false: a connected
component of `G_m[y]` can be split into many runs by edges whose colours are
not below `y`.  The canonical components in Theorem 1 also cross one
another as `y` varies; they are not a laminar family which a single
Hierholzer recursion could automatically place into nested intervals.

This is the exact reason Corollary 2 is not yet an upper-half construction.

## 6. The remaining simultaneous-transition lemma

The graph `G_m` is unusually sparse and leaves only surface-order freedom.

### Lemma 4 (surface transition complexity)

The maximum degree of `G_m` is three.  All vertices whose degree differs
from two, all isolated lower points, and the number of connected components
are `O(m^2)`.

### Proof

For `m=1`, the four lower vertices form `K_4`, so the degree assertion is
immediate.  Assume `m>=2`, and let `p<q` be the first two positive
coordinates of `v in V_m`.  Every
incident middle edge is obtained from a unique point `z=v+e_i`.  The added
coordinate `i` is one of the first two positive coordinates of `z` exactly
in the following cases:

* `i<p`;
* `i=p`, provided `v_p<m`;
* `p<i<q`; or
* `i=q`, provided `v_q<m`.

For `i>q`, the first two positive coordinates remain `p,q`, so the new
coordinate is not selected.  Consequently

\[
 \deg(v)=q-2+\mathbf1_{v_p<m}+\mathbf1_{v_q<m}.      \tag{6.1}
\]

If `q<=3`, this is at most three.  If `q=4`, then `p,4` are the only
positive coordinates of `v`.  Their sum is `2m-1`, so their values are
`m,m-1` in some order.  Exactly one of the last two indicators in (6.1) is
one, and the degree is again three.

Away from

\[
 B=\{v:v_1\in\{0,m\}\text{ or }v_2\in\{0,m\}\},   \tag{6.2}
\]

the graph consists of the degree-two coordinate-`{1,2}` line paths with
fixed `(v_3,v_4)`.  There are at most `(m+1)^2` such paths, while
`|B|=O(m^2)`.  Adding the boundary vertices proves all the stated surface
bounds.  QED.

At every degree-two vertex the Euler transition is forced.  At every
degree-three vertex one chooses which two incident edges pass through and
which half-edge is a trail end.  Degree-one vertices are trail ends.  A
chosen transition system can also create transition cycles inside
components which are not globally even; cut each such cycle once.  A cycle
meeting a degree-three vertex is charged to that vertex's unique paired
transition, while a cycle containing only degree-two vertices is a whole
degree-two component.  Thus the number of open trails plus cuts is at most

\[
 o(G_m)/2+\#\{v:\deg(v)=3\}+c(G_m)=O(m^2).
\]

Hence every choice of these `O(m^2)` local transitions produces an edge
partition into `O(m^2)` trails and therefore a word of length
`|Z_m|+O(m^2)` after the isolated lower vertices are appended.

There is also a canonical acyclic orientation.  Orient every selected edge
in the direction which moves its unit from the later positive coordinate to
the earlier one.  The potential `Phi` in (4.5) strictly decreases.  The
facet-spanning paths constructed in Theorem 1 are directed paths in this
DAG.  Away from the same `O(m^2)` boundary set, every vertex has one incoming
and one outgoing edge.  Thus the unresolved packing concerns only a
surface-size family of directed convergences and divergences.

The entire upper-half problem for this spine is now the following one
statement.

### Former lexicographic excursion lemma (false)

The first proposed packing lemma asked for a choice of the degree-three
transitions such that, for every `y in P_m` with `|y|>=2m`, one restricted
component *inside a single transition trail* meets all four facets
`F_i(y)`.  This is false for every `m>=2`.

There is an explicit four-target obstruction supported at three degree-three
vertices.  In the notation of `LEX_EXCURSION_OBSTRUCTION.md`, one target
forces the transition `(sv)_b`; this forces `(vw)_c`; the two remaining
targets then force both `(xu)_a` and `(ur)_a`, which cannot simultaneously
be the unique paired transition at the degree-three vertex `a`.  The four
clauses are minimally inconsistent.

This does **not** refute a word of length

\[
                    |Z_m|+O(m^2).                   \tag{6.3}
\]

After the `O(m^2)` transition trails are cut, oriented, and concatenated, a
witness crossing a trail seam can realize a second, virtual transition at a
branch vertex.  Indeed the obstruction proves only that at least one of its
four targets must use such a seam.  The corrected open statement is
therefore seam-aware:

> Choose the transitions, cuts, orientations, and linear order of the
> resulting `O(m^2)` pieces so that every upper target has a facet-spanning
> below-target run either inside one piece or across a chosen piece boundary.

Equivalently, a successful proof must budget both physical transition pairs
and the virtual pairs supplied by concatenation.  Pure connectivity and a
pure rotation system on the original graph are each insufficient.  See
`LEX_EXCURSION_OBSTRUCTION.md` and
`scratch/check_lex_excursion_obstruction.py`.

## 7. Intact line blocks have a cubic obstruction

The local component theorem uses boundary edges to join the natural
coordinate lines.  If those lines are instead kept as indivisible blocks,
the lower central layer together with the upper half cannot be covered at
lower-order cost.

For a transverse pair `p=(c,d)` put

\[
 R=2m-1-c-d.
\]

When `0<=R<=m-1`, the natural lower-layer line is

\[
 B_p=((0,R,c,d),(1,R-1,c,d),\ldots,(R,0,c,d)),      \tag{7.1}
\]

in either orientation.

Call a word an **intact line-block word** if it is a concatenation, with
arbitrary multiplicities and orientations, of the complete natural lines
partitioning `V_m`, and has no other letters.  To cover all of `V_m` by
singletons, every natural line must occur at least once.

### Theorem 5 (cubic intact-line penalty)

If an intact line-block word covers every target of rank at least `2m-1`,
then

\[
             |W|\ge |Z_m|+\left({11\over192}+o(1)\right)m^3. \tag{7.2}
\]

In particular it cannot have length `|Z_m|+o(m^3)`.

### Proof

Take

\[
 {m\over4}\le R\le {m\over2},\qquad
 c+d=2m-1-R,qquad c,d\le m-2,                      \tag{7.3}
\]

with integer rounding understood.  There are `R-2` choices of `(c,d)` in
(7.3).  For every

\[
                         R<a\le m                   \tag{7.4}
\]

consider

\[
                         y=(a,0,c,d).                \tag{7.5}

Its rank is `2m-1+(a-R)>=2m`, so it is a required upper target.

Every letter in a witness for (7.5) must have second coordinate zero.  A
nontrivial complete block (7.1) has exactly one such letter, its endpoint

\[
                         (R,0,c,d).                  \tag{7.6}

Because the block is intact, an all-zero-in-coordinate-two interval can
contain endpoints from at most two adjacent nontrivial block occurrences.
The only singleton blocks with second coordinate zero have transverse
labels `(m,m-1)` and `(m-1,m)`.  Neither lies below `(c,d)` in (7.3), so
neither can occur in a witness for (7.5).

A single endpoint has rank `2m-1` and cannot represent (7.5).  Hence each
target in (7.3)--(7.5) requires a seam between two adjacent block
occurrences.  One fixed seam has one fixed coordinatewise maximum and can
serve at most one of these targets.

Their number is

\[
 \sum_{R=\lceil m/4\rceil}^{\lfloor m/2\rfloor}
       (R-2)(m-R)
   =\left({11\over192}+o(1)\right)m^3.              \tag{7.7}
\]

There are only `O(m^2)` distinct natural blocks.  Thus (7.7) forces that
many block occurrences beyond the first copies, up to `O(m^2)`.  Every
additional occurrence has positive length.  Since the first copies contain
all `|V_m|` lower points and

\[
                         |V_m|=|Z_m|-(m+1),          \tag{7.8}

(7.2) follows.  QED.

The scope is exact.  The theorem does not obstruct splitting the line
blocks and collecting their coordinate-facet endpoints into shared
lower-dimensional words.  Indeed, Theorem 1 shows that this is precisely
what the lexicographic boundary edges accomplish at the connected-graph
level.

## 8. Big-picture interpretation

The direct line word covered the upper cone

\[
 y_1,y_2\ge |y|-2m+1.
\]

The deficit proof explains the rest.  Fixed `{1,2}` edges leave the deficit
coordinates `3,4` frozen, so only one deficit line can be used.  Whenever
that line is truncated, the lexicographic boundary rule changes the active
coordinate pair and connects it to the next deficit face.  Reverse-greedy
mass transfer proves that these recursive boundary connections always
reach all four facets.

Therefore the general four-box upper problem is no longer an edge-selection
problem.  It is a simultaneous **rotation-system problem on a graph whose
branching complexity is only surface order**.

There are now two plausible next attacks:

1. **Recursive facet rotation.**  Contract every forced degree-two line.
   Prove by induction on the coordinate order that the resulting
   `O(m^2)`-size kernel admits transitions whose restricted excursions
   contain the reverse-greedy arms from Theorem 1.

2. **Bounded-copy relaxation.**  Allow `O(m^2)` repeated boundary edges or
   vertices, still preserving (6.2), and use the copies to realize all
   locally needed turns at degree-three vertices.  The proof must show that
   one copy per boundary branch suffices globally; duplicating complete
   degree-two arms would return to the cubic obstruction of Theorem 5.

Either route would settle the entire upper half of the four-box at
width-plus-surface cost.  The separate lower-factor/pinning problem would
then remain for a full max-word construction, but the former upper-shadow
obstruction would be gone.
