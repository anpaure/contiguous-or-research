# A Catalan-compressed Johnson lift from saturating cycles

This note proves the purely central part of the formerly conjectural
even-to-odd inverse construction in `DIMENSION_MAPS_HANDOFF.md`.  It does not
yet control the lower shadows or factor-label pins, but it shows that the
required Catalan compression is always available and is not a search problem.

Throughout, put

\[
 M=\binom{2m}{m},\qquad N=\binom{2m}{m+1},\qquad
 M-N=\operatorname {Cat}_m.
\]

For a Johnson path `P=(P_0,...,P_(M-1))` through the rank-`m` layer, color
the edge `P_iP_(i+1)` by its union.  A color run is a maximal interval of
edges with the same rank-`m+1` union.

## 1. Saturating cycles give a rainbow upper-layer order

Corollary 2 of Gregor--Mička--Mütze's
[solution of the central-levels problem](https://tmuetze.de/papers/gmlc2.pdf)
gives a simple saturating cycle in
the incidence graph between ranks `m` and `m+1` of `B_(2m)` which visits every
rank-`m+1` vertex.  Write it as

\[
 U_0,Q_0,U_1,Q_1,\ldots,U_{N-1},Q_{N-1},U_0,
\tag{1.1}
\]

where the `U_i` are all rank-`m+1` sets and the `Q_i` are distinct rank-`m`
sets.  Necessarily

\[
 Q_i=U_i\cap U_{i+1}
\tag{1.2}
\]

with cyclic subscripts.  Consequently `U_0,...,U_(N-1)` is a Hamilton cycle
in `J(2m,m+1)` whose adjacent-intersection colors are all distinct.

## 2. Exact Catalan-compressed path

### Theorem 1

For every `m>=2` there are Hamilton paths

\[
 R=(R_0,\ldots,R_{N-1})\quad\hbox{in }J(2m,m+1)
\]

and

\[
 P=(P_0,\ldots,P_{M-1})\quad\hbox{in }J(2m,m)
\]

with the following properties.

1. The adjacent intersections of `R` are distinct.
2. Every rank-`m+1` set occurs as an adjacent-union color of `P`.
3. For each color `R_i`, all edges of `P` having union `R_i` form one
   nonempty contiguous run.
4. Compressing equal consecutive union colors of `P` gives exactly `R`.
5. The initial vertex may be chosen with `P_0 subset R_0`.

In particular, the `M-1` edge colors of `P` compress by the exact Catalan
saving

\[
 M-N=\operatorname {Cat}_m.
\tag{2.1}
\]

### Proof

Start from the saturating cycle (1.1).  There are `M-N=Cat_m>0` rank-`m`
sets not among the `Q_i`; call this family `L`.  Choose `P_* in L` and choose
an upper set `U_j` containing it.  Cut (1.1) at either one of the two cycle
segments incident with `U_j`, say at

\[
 U_{j-1},Q_{j-1},U_j.
\]

The resulting linear upper order starts at `U_j` and ends at `U_(j-1)`;
call it `R`.  Its used boundary facets are all `Q_i` except `Q_(j-1)`.  Its
pool of unused middle vertices is therefore

\[
 L'=L\cup\{Q_{j-1}\},
\qquad |L'|=\operatorname {Cat}_m+1.
\tag{2.2}

Assign `P_*` to the first upper vertex `U_j` and assign the removed boundary
facet `Q_(j-1)` to the last upper vertex `U_(j-1)`.  Assign every other
member `X of L'` to any upper set `U` containing `X`.  No capacity theorem is
needed: the assigned objects at `U` are distinct unused facets of `U`, so
there can automatically be no more than the available facets.

For each upper set `U` in the linear order `R`, make a block consisting of
its incoming boundary facet, then all unused facets assigned to it in any
order, then its outgoing boundary facet.  At the first and last blocks only
one boundary facet exists; their prescribed assignments ensure that those
blocks still contain at least two vertices.  In every interior block the two
boundary facets are distinct because all `Q_i` are distinct.

Concatenate the blocks, identifying the outgoing boundary facet of one block
with the identical incoming boundary facet of the next.  Any two successive
facets inside a block are distinct `m`-subsets of the same `(m+1)`-set `U`,
so they are Johnson-adjacent and their union is `U`.  The concatenation uses
every used `Q_i` once and every member of `L'` once, hence every one of the
`M` middle sets exactly once.  It is therefore the required Hamilton path
`P`.  Its first vertex is `P_* subset U_j=R_0`.  Every `U` supplies exactly
one nonempty color run, and the run order is `R`.  This proves all claims.

## 3. Width-exact odd central lift

Let `z` be a new coordinate.  Orient the paths from Theorem 1 so that
`P_0 subset R_0`.  Then

\[
 T=\operatorname {rev}(R)\ \Vert\
   (\{z\}\cup P_0,\ldots,\{z\}\cup P_{M-1})
\tag{3.1}
\]

is a Hamilton path through the complete rank-`m+1` layer of `B_(2m+1)`.
Indeed, the first block lists all sets not containing `z`, the second lists
all sets containing `z`, and the seam is a Johnson edge because

\[
 R_0\cap(\{z\}\cup P_0)=P_0.
\tag{3.2}
\]

Thus the formerly conjectural *central enumeration and Catalan compression*
in the even-to-odd lift are unconditional in every dimension.

## 4. What this does not prove

The theorem is deliberately limited.

* It does not make the adjacent intersections of `P` cover rank `m-1`.
* It does not impose long coordinate runs or factor-label pinnability.
* The first block `R` needs its own longer upper shadows if (3.1) is to be
  universal above the middle.
* A two-sided version would require the intersection colors of `P` to admit
  an analogous contiguous-run compression simultaneously.  That is a much
  stronger object and is still open.

The gain is nevertheless structural: the exact Catalan saving and the seam
conditions require only a saturating cycle plus the elementary facet-block
lift above.  Future work should not search for this part again; it should
concentrate on making the lift two-sided and pin-compatible.
