# Promoted hook parents are marked double-zero subdivisions

**Date:** 2026-08-05  
**Method:** exact hook vacancy coordinates and cyclic deletion; no search  
**Status:** unconditional.  The promoted shore `1D0` is obtained by
inserting two consecutive zero vacancy slots at the chosen root cut.  This
gives an exact inverse classification and distinct physical parent ports.
It also proves that constant component degree is impossible in a global
hook packing.  The remaining combinatorial gate is a sibling matching (or
an equivalent dynamic rail construction) in each chip-necklace graph.

## 1. Rooted hook coordinates

For the hook action `(h,1^b)`, put `q=2h-1`.  Write its rooted vacancy
coordinates as

\[
 x=(\ell_0,\ldots,\ell_{h-2},t,
                  r_{h-2},\ldots,r_0),\qquad |x|=b.
\tag{1.1}
\]

The corresponding rooted Dyck word is

\[
\begin{aligned}
 D_h(x)={}&(10)^{\ell_0}1(10)^{\ell_1}1\cdots
 (10)^{\ell_{h-2}}1(10)^{t+1}0\\
 &\qquad (10)^{r_{h-2}}0\cdots0(10)^{r_0}.
\end{aligned}
\tag{1.2}
\]

Cyclic rotation of the `q` entries changes only the root cut.  Thus the
physical hook tori are the necklaces `[x]`.

## 2. Exact promoted-parent map

Let `D=D_h(y)` have action `(h,1^(b-1))`.  Comparing (1.2) at heights `h`
and `h+1` gives the literal identity

\[
                         1D_h(y)0=D_{h+1}(0,y,0).
\tag{2.1}
\]

The first and last entries on the right are adjacent after cyclic closure.
Consequently, if the root cut of `D` lies between cyclic vacancy positions
`j` and `j+1`, define

\[
 \iota_j(y)=\text{the length-}(q+2)\text{ cyclic vector obtained by
 inserting }0,0\text{ at that cut}.
\tag{2.2}
\]

Then the three action-angle components of the leaf-plucking C6 are exactly

\[
 \boxed{
   [y+e_j],\qquad [y+e_{j+1}],\qquad [\iota_j(y)].
 }
\tag{2.3}

The first two have action `(h,1^b)` and the third has action
`(h+1,1^(b-1))`.

## 3. The marked-port inverse is exact

A **marked promoted port** is a pair `(z,00_*)`, where `z` is a cyclic
length-`q+2` vacancy vector of mass `b-1` and `00_*` is one distinguished
adjacent pair of zero slots.

### Theorem 3.1

The map

\[
 (y,j)\longmapsto(\iota_j(y),00_*)
\tag{3.1}
\]

is a bijection, modulo simultaneous cyclic rotation, from rooted
leaf-plucking data to marked promoted ports.

#### Proof

Insertion produces the distinguished adjacent zero pair.  Conversely,
delete the marked pair and contract the resulting gap.  This recovers the
cyclic vector `y` and the cut between its positions `j,j+1`.  The two
operations are inverse and commute with cyclic rotation.  `square`

Thus the unmarked preimages of a fixed parent necklace `[z]` are exactly
the cyclic occurrences of `00` in `z`, modulo its rotational stabilizer.
There are at most `q+2` of them.  More importantly, two distinct simple
angle edges in (2.3) never demand the same marked promoted port.

At the literal PBBS level, the mark is the root-side pair of new empty
peak-insertion gaps in `1D0`; hence it names the promoted old-edge
occurrence, not merely its action torus.  This is the capacity coordinate
which is lost if one remembers only the parent component.

## 4. The exact connector hypergraph

Let

\[
 {\cal N}_{q,b}=\{x\in\mathbb Z_{\ge0}^q:|x|=b\}/C_q.
\]

The hook connector hypergraph has one edge

\[
 E(y,j)=\{[y+e_j],[y+e_{j+1}],[\iota_j(y)]\}
\tag{4.1}

for every rooted mass-`b-1` necklace and cyclic cut.  Deleting its promoted
vertex leaves exactly the adjacent-chip-transfer graph `G_(q,b)`.

If `M_b` is a matching in `G_(q,b)`, then the hyperedges over `M_b` are
child-disjoint.  Any two of them intersect in at most their promoted parent
component; even when that component agrees, Theorem 3.1 gives distinct
marked physical ports.  Therefore, once all used promoted parents already
belong to a connected spine, the hyperedges over `M_b` form a component-
level loose hyperstar forest and add two fresh child tori per edge.

This reduces simultaneous hook absorption to an exact combinatorial row:
choose sibling matchings at all levels, with only a bounded number of
unmatched child tori, and then separate the finitely local literal halos of
their distinct marked ports.

## 5. Constant parent-component degree is impossible

The preceding statement must be formulated in marked-port, not component-
degree, language.

### Proposition 5.1

At chip level `b=2`, any sibling-pair absorption of all but `O(1)` hook
tori uses the unique level-one parent component `Omega(h)` times.

#### Proof

Here `q=2h-1`.  A two-chip necklace is determined by the shorter cyclic
distance between its chips, with distance zero allowing both chips in one
slot.  Hence there are exactly

\[
                         h
\tag{5.1}
\]

level-two tori.  At level one there is only one necklace.  Every connector
absorbs at most two level-two tori and its promoted shore is that unique
level-one component.  Covering `h-O(1)` children therefore requires at
least `(h-O(1))/2` incidences with the same parent component.  `square`

Since `h=Theta(m)`, no global theorem with parent-component degree bounded
independently of `m` can be true.  The marked ports of Theorem 3.1 are the
correct replacement: the unique parent cycle supplies linearly many
different rooted `00` ports.

## 6. The complete two-chip row

Denote the two-chip tori by

\[
                         C_0,C_1,\ldots,C_{h-1},
\tag{6.1}

where `C_0` has both chips in one slot and `C_d` has two singleton chips at
shorter cyclic distance `d`.

### Proposition 6.1

The simple adjacent-transfer graph at level two is exactly the path

\[
                         C_0-C_1-\cdots-C_{h-1}.
\tag{6.2}

Each path edge uses a different marked `00` port of the unique level-one
parent.

#### Proof

Moving one chip by one vacancy step changes the shorter distance by one.
At distance zero this creates distance one; at the antipodal endpoint
`h-1` on the odd cycle, every nonloop move returns to `h-2`.  These are all
simple adjacencies, proving (6.2).  Distinct path edges are distinct rooted
data `(y,j)`, so Theorem 3.1 gives distinct marked parent ports.  `square`

If `C_0` is the named level-two spine component, alternating edges in
(6.2) cover every nonnamed level-two torus when `h` is odd and all but one
when `h` is even.  The latter residual is forced for any loose hyperstar
rooted simultaneously at the already-present parent and `C_0`: each new
hyperedge adds two fresh vertices, while `h-1` is odd.

Thus the first nontrivial angle row already has an optimal physically
port-distinct loose packing with defect at most one.

## 7. Exact remaining gate

The all-angle incidence theorem plus Theorem 3.1 remove parent-port
collision as an abstract obstruction.  What is not yet proved is the
uniform matching statement

\[
 \nu\bigl(G_{2h-1,b}-\{\text{named root and prescribed parity socket}\}
       \bigr)=\frac{|V|-O(1)}2
\tag{7.1}

simultaneously over all `b`, together with a bounded-overlap placement of
the companion q2 halos along repeated parent cycles.

Connectivity of `G_(q,b)` alone does not imply (7.1).  Nor can a constant
component-degree hypothesis replace it, by Proposition 5.1.  A proof must
use either an adjacent-transfer necklace matching/Gray structure or the
one-or-two-rail dynamic topology to route the unmatched parity sockets
between levels.

No q3, residence, arbitrary-upper, or common-cap conclusion is included.
