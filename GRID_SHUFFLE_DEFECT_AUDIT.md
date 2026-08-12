# Defect audit of the coordinate-cut grid shuffle

## 1. Outcome

The coordinate-cut construction has the correct **bulk propagation
coefficient** for `CONTRACTIVE_DEFECT_LIFT.md`: inside its product sector,
one old missing flag has at most two endpoint-decorated descendants.

It does not yet satisfy the contractive-lift hypothesis.

* One product path is produced for every old wreath, so the construction
  supplies only `Cat_m` of the `Cat_(m+1)` wreaths required in the new
  factor.  The missing number is

  \[
   \operatorname {Cat}_{m+1}-\operatorname {Cat}_m
      ={3m\over m+2}\operatorname {Cat}_m.           \tag{1.1}
  \]

  No common exact completion of this partial sector is currently proved.
* At depth `q`, a raw horizontal/vertical cut has `Theta(q)` windows meeting
  its seam.  Thus the formulas currently prove only an additive

  \[
                       O(H^2\operatorname {Cat}_m)    \tag{1.2}
  \]

  defect over depths `q<=H`, not the
  `O(H Cat_m)` term required in (3.1) of
  `CONTRACTIVE_DEFECT_LIFT.md`.

Therefore the present construction is a useful reduction, not yet an
asymptotically contractive lift.  The exact remaining lemma must do two jobs
at once:

1. complete the other asymptotic three quarters of the new factor without
   importing a positive-density vertical defect; and
2. resolve the `q` seam-crossing windows at depth `q` into only `O(1)`
   unmatched transversals per old path.

If those two statements are proved, the column-sum coefficient is `a=2<4`
and the contraction theorem applies.

## 2. Complementary paths and grid shuffles

Let `X,Y` be disjoint sets of sizes `2m,2s`.  A complementary path on `X`
is

\[
 P=(x_0,x_1,\ldots,x_m),\qquad x_m=X\setminus x_0, \tag{2.1}
\]

where consecutive terms are Johnson-adjacent.  Put

\[
 y_i=x_i\cup x_{i+1},\quad
 L_i=x_i\cap x_{i+1},\quad
 U_i=X\setminus(y_{i-1}\cup y_i),                  \tag{2.2}
\]

with `1<=i<m` in the last definition, and

\[
 E_0=X\setminus y_0,\qquad E_1=X\setminus y_{m-1}. \tag{2.3}
\]

Use analogous notation

\[
 Q=(u_0,\ldots,u_s),\quad v_j,\Lambda_j,V_j,F_0,F_1 \tag{2.4}
\]

on `Y`.

Every monotone lattice path `sigma` from `(0,0)` to `(m,s)` gives a
complementary path on `X union Y` by replacing a visited cell `(i,j)` with

\[
                            x_i\cup u_j.              \tag{2.5}
\]

With one additional distinguished coordinate `z`, (2.5) gives a wreath.
The following table is obtained by taking intersections of adjacent vertices
and complements of one or two adjacent edge unions.

| local event in `sigma` | middle object | first-lower object |
|---|---|---|
| visited cell `(i,j)` | `x_i union u_j` | -- |
| horizontal edge `(i,j)` | `z union (X-y_i) union (Y-u_j)` | `L_i union u_j` |
| vertical edge `(i,j)` | `z union (X-x_i) union (Y-v_j)` | `x_i union Lambda_j` |
| consecutive `HH` at `(i,j)` | -- | `z union U_i union (Y-u_j)` |
| consecutive `VV` at `(i,j)` | -- | `z union (X-x_i) union V_j` |
| either corner at cell `(i,j)` | -- | `z union (X-y_i) union (Y-v_j)` |

At the two ends, the first-lower endpoint flag is the complement of the
first or last edge union.  Thus a first horizontal edge contributes
`E_0 union (Y-u_0)`, a first vertical edge contributes
`(X-x_0) union F_0`, and the terminal formulas are dual.

These identities are exact for every shuffle.  In particular, the two
corner orientations `HV` and `VH` have the same first-lower value; only the
visited middle cells differ.

### Proposition 1 (one grid sector is a partial factor)

Let `mathcal P` be an exact complementary path factor on `X`, fix one path
`Q` on `Y`, and assign an arbitrary monotone shuffle `sigma_P` to every
`P in mathcal P`.  If no two assigned grid paths use the same cell or the
same directed grid edge after projecting to their `X` and `Y` labels, then
the resulting wreaths form a partial middle factor.

For the one-vertical-block shuffles (3.1), this noncollision condition is
automatic for arbitrary cut positions `a(P)`.

### Proof

The middle objects are the first two columns of the table above.  Equality
of two no-`z` targets forces equality of both their `X` and `Y` parts.  Old
path vertices are globally distinct, and within `Q` the vertices `u_j` are
distinct.  Equality of two `z`-containing targets similarly forces equality
of the corresponding old vertex or edge colour and of the cap vertex or
edge colour.  The old `x` vertices and `y` edge colours are each globally
distinct in an exact complementary factor.  Different local event types
have different `X`- or `Y`-ranks and therefore cannot collide.

In (3.1), the height-zero and height-`s` horizontal pieces partition the
old `x_i` and `y_i` occurrences, while every internal height uses only the
single cut state `x_a(P)`.  Cut states belonging to distinct old paths are
distinct because the old paths partition their vertices.  Hence the
projected cell and edge condition holds.  QED.

This proposition gives exactly `Cat_m` new wreaths.  It does not give a full
next factor, which needs `Cat_(m+1)` wreaths.

## 3. The one-vertical-block transportation equations

Take

\[
                   \sigma_a=H^aV^sH^{m-a},
                   \qquad0<a<m.                     \tag{3.1}
\]

For a signed family of old paths, write `Delta` for positive minus negative
multisets.  Assume the old families are exact path factors, so the total
`x_i` and total `y_i` multisets agree.

Equality of the new middle support inside this product sector requires

\[
\begin{aligned}
 \Delta\sum_P\sum_{i=0}^{a(P)}e_{x_i(P)}&=0,\\
 \Delta\sum_P e_{x_{a(P)}(P)}&=0,\\
 \Delta\sum_P\sum_{i=0}^{a(P)-1}e_{y_i(P)}&=0.       \tag{3.2}
\end{aligned}
\]

The complementary suffix equations then follow from exactness and the
middle equation in (3.2).  The three lines respectively control the height
zero cells, all internal vertical cells, and the height zero horizontal
edges.

For first-lower targets not containing `z`, define

\[
 F_a(P)=E_1(P)+\sum_{i<a}L_i(P).                     \tag{3.3}
\]

The `Y=u_0` section has signed measure `Delta sum_P F_a(P)`, while the
`Y=u_s=Y-u_0` section has the complementary measure

\[
 \Delta\sum_P\left(E_0(P)+\sum_{i\ge a}L_i(P)\right). \tag{3.4}
\]

Since equality of the old first-lower row gives

\[
 \Delta\sum_P\left(E_0+E_1+\sum_iL_i\right)=0,       \tag{3.5}
\]

one of (3.3)--(3.4) vanishes exactly when the other does.

The remaining first-lower equations are read directly from the last three
rows of the table in Section 2.  They involve prefix and suffix sums of the
`U_i`, the cut state `x_a`, and the two corner flags

\[
                   X\setminus y_{a-1},qquad
                   X\setminus y_a.                   \tag{3.6}

Thus ordinary concatenation is not the only possible product: moving the
vertical block through `P` genuinely mixes `L` with the endpoint flags.

## 4. Fixed-coordinate cuts isolate Catalan interfaces

Fix `c in X` and orient every complementary path so that

\[
                         c\in x_0.                    \tag{4.1}

Every coordinate changes membership exactly once along a complementary
path, because there are `m` Johnson edges, hence `2m` coordinate toggles,
and the endpoint is the complement.  Let edge `a(P)` be the unique edge on
which `c` leaves.

Then

\[
\begin{array}{c|c}
\text{objects containing }c&\text{indices}\\ \hline
x_i&i\le a,\\
y_i&i\le a,\\
L_i&i<a,\\
E_1&\text{yes},\\
E_0&\text{no}.
\end{array}                                          \tag{4.2}
\]

Choose the vertical block **before** the flip, at `x_a`.  The first line of
(3.2) is now the entire rank-`m` section containing `c`, and (3.3) is the
entire old `z`-free first-lower section containing `c`.  These bulk equations
therefore hold for any two exact old factors with equal old first-lower
shadow.  The failures in (3.2) are reduced to the two interface families

\[
       \{x_{a(P)}(P):P\},\qquad
       \{y_{a(P)}(P):P\}.                            \tag{4.3}
\]

There is one member of each family per old path, hence `Cat_m` of each.
The `z`-containing first-lower row leaves only a bounded list of analogous
corner/interface families per path, obtained from (3.6) and the two `U`
flags adjacent to the flip.

If instead the vertical block is placed **after** the flip at `x_(a+1)`,
all upper-edge sections in (3.2) are exact.  The interface families become
the cut vertex, the flip lower color `L_a`, the one missing adjacent `U`
flag, and the two corner complements.  Again their number is bounded per
path at depth one.

This is the useful structural reduction: at every fixed depth, the bulk is
organized by the coordinate section and all failure is localized near the
unique `c`-flip.

## 5. Exact propagation coefficient and seam count

Away from the vertical block, every old interval flag appears in at most two
new sections: once decorated by the initial cap state `u_0` and once by its
complement `u_s`.  Therefore the column sum for **nonseam inherited holes**
is

\[
                              a_{\rm bulk}=2.          \tag{5.1}
\]

This is the desired strict inequality `2<4`.

At depth `q`, however, a window of `q` transitions meets a fixed join in up
to `q` starting positions.  The word (3.1) has two joins.  Consequently the
unresolved raw seam table has

\[
               O(q\operatorname {Cat}_m)             \tag{5.2}
\]

marked occurrences at depth `q`, and summing through depth `H` gives

\[
               O(H^2\operatorname {Cat}_m).          \tag{5.3}

This estimate is an upper bound and may contain cancellations, but no
all-depth theorem reducing it to `O(Cat_m)` per depth is currently proved.

Finally, (5.1) audits only the `Cat_m`-wreath product sector.  Let
`E_aux(m,H)` denote the number of central-band targets left uncovered after
completing the remaining wreaths.  The strongest recurrence justified by
the present formulas has the schematic form

\[
 E_{m+1,H}
   \le 2E_{m,H}
       +O(H^2\operatorname {Cat}_m)
       +E_{\rm aux}(m,H).                            \tag{5.4}

Neither

\[
 E_{\rm aux}(m,H)=O(H\operatorname {Cat}_m)          \tag{5.5}

nor even the required common exact middle completion has yet been proved.

For the tail depth `H^2/m -> infinity`, the normalized seam term in (5.4)
is `O(H^2/m)`, which is not `o(1)`.  Thus (5.4) does not imply asymptotic
optimality.

## 6. The exact successor lemma

The grid programme now has a quantitative, falsifiable target.

> **Contractive grid completion lemma.**  Complete the coordinate-cut
> product sector to an exact factor so that (i) every old missing flag has at
> most two descendants, (ii) the auxiliary sectors leave only
> `O(Cat_m)` holes at each controlled depth, and (iii) the `q` raw windows
> meeting each cut are routed through the vertical grid into only `O(1)`
> unmatched interface transversals per old path.

The first clause is already true off the seam.  The second and third clauses
are the remaining mathematics.  Together they give

\[
 E_{m+1,H}\le2E_{m,H}+O(H\operatorname {Cat}_m),     \tag{6.1}

which is (3.1) of `CONTRACTIVE_DEFECT_LIFT.md` with `a=2<4` and proves
asymptotic optimality.

Without clauses (ii)--(iii), the coordinate cut is only a Catalan-interface
localization theorem, not a completed lift.

## 7. Repair-word compression removes the apparent `H^2` loss

The count in (5.3) is an obstruction only for literal listing of missing
masks.  It is **not** an obstruction for the repair cost
`R_(m,H)` from Section 7 of `CONTRACTIVE_DEFECT_LIFT.md`.

Write the omitted-label word of `P` as

\[
 (a_0,b_0,a_1,b_1,\ldots,a_{m-1},b_{m-1},z),        \tag{7.1}
\]

where edge `i` exchanges `b_i` for `a_i`.  Write the corresponding pair
word of `Q` as

\[
                   (c_0,d_0,\ldots,c_{s-1},d_{s-1}). \tag{7.2}
\]

The product path with shuffle `sigma` has omitted word obtained by
interleaving the pairs `(a_i,b_i)` and `(c_j,d_j)` in the order prescribed
by `sigma`, followed by `z`.  This follows directly from the path-to-wreath
normal form: a horizontal move performs the old `P` exchange and a vertical
move performs the `Q` exchange.

For the vertical-block shuffle (3.1), (7.1)--(7.2) become

\[
 (A_{<a},\ C,\ A_{\ge a},\ z),                      \tag{7.3}
\]

where each letter denotes a block of exchange pairs.  In ordinary cyclic
interval order, starting at `z`, this is

\[
 z,\ B_{<a},D,B_{\ge a},\ A_{<a},C,A_{\ge a},       \tag{7.4}
\]

up to reversal.  Hence the selected product order differs from either
endpoint concatenation (`C` before all `A`, or after all `A`) by at most two
block moves, and therefore by only a constant number of cuts.

### Proposition 5 (sector repair bound)

Fix the cap path `Q` and arbitrary cut positions `a(P)`.  Suppose only the
two endpoint-decorated descendant families of the old central-band targets
are required, together with every target lost when the endpoint
concatenations are changed to (7.3).  They have a repair word of length

\[
             2R_{m,H}(F_m)+O(H\operatorname {Cat}_m). \tag{7.5}
\]

The implied constant is absolute for a one-step cap and remains bounded for
a fixed cap size.

### Proof

Use two tagged copies of an optimal old repair word, one for each cap
endpoint state.  Lemma 4 of `CONTRACTIVE_DEFECT_LIFT.md` gives the first
term in (7.5).

For every old path `P`, compare the selected word (7.4) with the two endpoint
concatenations.  Every cyclic interval which changes under a block move
crosses one of its cut positions.  Form the standard erosion word of each
endpoint order by listing its cyclic intervals of the smallest controlled
rank.  A target anywhere in the controlled band is an OR of at most
`2H+2` consecutive erosion entries.  Lemma 3 of
`CONTRACTIVE_DEFECT_LIFT.md`, applied at the constant number of block-move
cuts in (7.4), therefore supplies a halo of `O(H)` entries which preserves
all changed targets for this `P`.  Summing over the `Cat_m` old paths proves
(7.5).  QED.

Thus the raw `Theta(H^2 Cat_m)` target count compresses to the desired
`O(H Cat_m)` **repair length**.  Within this one product sector, both
quantitative requirements of a contractive lift are now proved:

\[
                      a_{\rm sector}=2,
       \qquad R_{\rm seam}=O(H\operatorname {Cat}_m). \tag{7.6}

What remains unproved is not the seam halo.  It is the completion of the
other

\[
          \operatorname {Cat}_{m+1}-\operatorname {Cat}_m
          ={3m\over m+2}\operatorname {Cat}_m        \tag{7.7}
\]

wreaths while retaining a total inherited coefficient below four.

## 8. Catalan-convolution completion target

The exact count (7.7) points to the first-return decomposition

\[
 \mathcal D_{m+1}
   =\mathop{\dot\bigcup}_{i=0}^{m}
      \{,1u0v:u\in\mathcal D_i,
                 v\in\mathcal D_{m-i}\,\}.          \tag{8.1}
\]

Its sector sizes are

\[
                  \operatorname {Cat}_i
                  \operatorname {Cat}_{m-i},         \tag{8.2}
\]

and sum to `Cat_(m+1)`.  The two endpoint sectors `i=0,m` each have size
`Cat_m`; these are the two natural descendants in which an old defect should
appear.  The internal sectors account for the remaining asymptotic half of
the next factor using factors of smaller dimensions.

This yields the precise completion programme:

1. realize (8.1) as complementary-path grid products;
2. put the current factor `F_m` only in the two endpoint sectors, giving the
   already proved inherited coefficient `2`;
3. fill the internal sectors recursively from the previously constructed
   smaller factors; and
4. prove that changed endpoint-pair transversals can be matched across the
   sector seams without increasing the repair cost beyond
   `O(H Cat_m)`.

The fourth item is essential.  A Cartesian product path has middle support
depending on its endpoint pair, and arbitrary exact path factors need not
have the same endpoint-pair family.  Thus (8.1) is the correct count and
recursive geometry, but it is not yet a factor-substitution theorem.

If this endpoint-seam matching is proved, (7.5) shows that the propagation
coefficient of the two large descendants is exactly

\[
                              a=2<4,                 \tag{8.3}
\]

and `CONTRACTIVE_DEFECT_LIFT.md` gives asymptotic optimality.

## 9. Rank-rectangle conservation and the minimum braid

There is an additional counting constraint on any attempt to use two
endpoint descendants.  Add a coordinate pair `p,q` to the old even core
`X`, and classify a new rank-`m+1` core state by

\[
                     t=|S\cap\{p,q\}|\in\{0,1,2\}. \tag{9.1}
\]

The three rectangle sizes are

\[
 N_0=N_2=m\operatorname {Cat}_m,qquad
 N_1=2(m+1)\operatorname {Cat}_m.                   \tag{9.2}
\]

Every complementary path in the new core has `m+2` vertices.  Its type word
has adjacent differences at most one, and its terminal type is `2-t_0`.
In particular, **every** complementary path contains at least one type-one
vertex.

### Theorem 6 (rank-rectangle conservation)

Suppose a full next factor is divided into `B` designated endpoint paths and

\[
                 D=\operatorname {Cat}_{m+1}-B      \tag{9.3}
\]

remaining paths.  Let `e` be the number of type-zero or type-two vertices
used by the `B` endpoint paths.  Then

\[
 e\ge
 B(m+2)+D-N_1
 =B(m+1)+\operatorname {Cat}_{m+1}
        -2(m+1)\operatorname {Cat}_m.               \tag{9.4}

Equality holds exactly when every remaining path contains one type-one
vertex.

### Proof

The endpoint paths use `B(m+2)-e` type-one vertices.  The remaining paths
therefore have

\[
 N_1-B(m+2)+e                                      \tag{9.5}
\]

type-one vertices available.  Since every one of the `D` complementary
paths needs at least one, (9.5) is at least `D`, proving (9.4).  Equality is
equivalent to one type-one vertex on each remaining path.  QED.

For the proposed two endpoint sectors, `B=2 Cat_m`, so (9.4) becomes

\[
                         \boxed{e\ge\operatorname {Cat}_{m+1}}. \tag{9.6}

\]

This is strictly stronger than the naive excess count `2 Cat_m`.  In
particular, replacing only one type-one state in each endpoint path by an
upper or lower diamond consumes the entire type-one rectangle and leaves no
connector for the remaining

\[
 D=\operatorname {Cat}_{m+1}-2\operatorname {Cat}_m
   ={2(m-1)\over m+2}\operatorname {Cat}_m          \tag{9.7}

paths.  Those paths cannot be formed from only types zero and two, because
the two rectangles have no Johnson edges between them.

The obstruction is visible in the most natural local lift.  For an old
complementary path

\[
 P=(x_0,y_0,x_1,\ldots,y_{m-1},x_m),
 \qquad L_a=x_a\cap x_{a+1},                         \tag{9.8}
\]

choose one edge `a` and form the two new lower-level paths

\[
\begin{aligned}
 P_a^+={}&(x_0p,\ldots,x_ap,\,y_a,\,x_{a+1}q,\ldots,x_mq),\\
 P_a^-={}&(x_mp,\ldots,x_{a+1}p,\,L_apq,\,x_aq,\ldots,x_0q).
                                                               \tag{9.9}
\end{aligned}
\]

Here juxtaposition denotes disjoint union.  Both are complementary Johnson
paths.  Together they use every tagged type-one state `x_i p,x_i q` exactly
once and replace only two of their `2(m+2)` lower vertices by outer states,
namely `y_a` of type zero and `L_a p q` of type two.  Their upper vertices
are all tagged old `y_i` states, except for the local cap diamond whose two
outer vertices are `x_a p q` and `x_(a+1) p q`.

Across an old path factor these pairs are vertex-disjoint whenever the
chosen `L_a` are distinct; the `y_a` and all tagged old vertices are already
distinct.  Thus a rainbow choice of old lower-edge colours really does give
a clean two-descendant packing.  But it has

\[
                         e=2\operatorname {Cat}_m,               \tag{9.10}
\]

which violates (9.6).  Equivalently, it consumes the entire type-one
rectangle, leaving none of the mandatory connectors for the internal
Catalan sectors.  This proves that the failure is not a poor choice of
seams: the locally perfect diamond lift has the globally wrong rank budget.

At equality in (9.6), every remaining path has the type word

\[
                 0^r\,1\,2^{m+1-r}
       \quad\text{or its reverse}                   \tag{9.11}

for some `1<=r<=m`; it is a single rank-transfer bridge.  The average number
of non-type-one states on an endpoint path is

\[
 {\operatorname {Cat}_{m+1}\over2\operatorname {Cat}_m}
       ={2m+1\over m+2}=2-{3\over m+2}.              \tag{9.12}


Thus a minimal aggregate schedule may take

\[
 4\operatorname {Cat}_m-\operatorname {Cat}_{m+1}
   ={6\over m+2}\operatorname {Cat}_m               \tag{9.13}

endpoint paths with one excursion state and all other endpoint paths with
two.  The excursions must be balanced between types zero and two together
with the choices of `r` in (9.11), so that both totals equal
`m Cat_m`.

The set-theoretic content of (9.11) is equally explicit.  A one-connector
remaining path consists of

1. a Johnson path through rank-`m+1` subsets of `X`;
2. one flag

   \[
                         L\subset S\subset U,
   \qquad |L|=m-1, |S|=m, |U|=m+1,                \tag{9.14}
   \]

   realized as `U -> S union {p} -> L union {p,q}`; and
3. a Johnson path through rank-`m-1` subsets of `X` ending at the complement
   of the first endpoint.

Consequently the minimum feasible Catalan braid is no longer vague:

> choose `D` disjoint connector flags (9.14), decompose the residual upper
> and lower rank rectangles into complementary endpoint paths, and give the
> `2 Cat_m` endpoint descendants a total of exactly `Cat_(m+1)` short
> excursions, balanced between the two outer rectangles.

Theorem 6 is a necessary aggregate condition.  Constructing the disjoint
flags and the two residual path decompositions is the remaining global
schedule theorem.  It cannot be replaced by independent one-diamond gadgets
on the old paths.

## 10. Outer rectangles and the exact residual prism

There is a second decomposition which uses all outer lower states first and
leaves a sharply defined type-one prism.  It does not by itself give a path
factor, because its upper-edge colours have a controlled defect.

For an old path `P`, put `bar(y)=X minus y` and define the two lower-state
sequences

\[
\begin{aligned}
 O_0(P)&=(x_0p,\,y_0,\ldots,y_{m-1},\,x_mq),\\
 O_2(P)&=(x_0q,\,\bar y_{m-1}pq,\ldots,\bar y_0pq,\,x_mp).
                                                               \tag{10.1}
\end{aligned}
\]

### Proposition 7 (lower-state rectangle decomposition)

The sequences in (10.1) are complementary Johnson paths and are pairwise
disjoint at their lower vertices.  Over an old complementary-path factor,
they use

1. every type-zero lower state exactly once;
2. every type-two lower state exactly once; and
3. precisely the four tagged endpoint states
   `x_0 p,x_0 q,x_m p,x_m q` of every old path.

The unused lower states are exactly

\[
 \mathcal R\times\{p,q\},\qquad
 \mathcal R=\binom Xm\setminus
   \{x_0(P),x_m(P):P\in\mathcal F_m\}.             \tag{10.2}
\]

They form a complement-closed family of size

\[
 2(m-1)\operatorname {Cat}_m
   =(m+2)D,\qquad
 D=\operatorname {Cat}_{m+1}-2\operatorname {Cat}_m.
                                                               \tag{10.3}
\]

### Proof

Consecutive `y_i,y_(i+1)` intersect in `x_(i+1)`, and the same assertion
after complementation proves adjacency in `O_2`.  The endpoint containments
`bar(y_(m-1)) subset x_0` and `bar(y_0) subset x_m` prove the two boundary
adjacencies.  The first and last states in each sequence are complements in
`X union {p,q}`.

The old `y_i` partition rank `m+1` of `X`; their complements partition rank
`m-1`.  The endpoint sets of the old paths are distinct and closed under
complementation.  This proves disjointness, (10.2), and the count (10.3).
QED.

The induced graph on (10.2) has an especially simple description.  Its
edges are

\[
\begin{array}{ll}
 (S,t)(S',t),& S,S'\text{ Johnson-adjacent},\quad t\in\{p,q\},\\
 (S,p)(S,q),& S\in\mathcal R.
\end{array}                                                   \tag{10.4}
\]

Thus it is a two-sheeted Johnson prism.  Horizontal edges have type-one
upper colour `(S union S') union {t}`; vertical edges have type-two colour
`S union {p,q}`.  Complementation exchanges the sheets:

\[
                    (S,p)^c=(X\setminus S,q).       \tag{10.5}
\]

Consequently a completion which retains the lower ownership in Proposition
7 requires exactly `D` complementary paths of `m+2` vertices in this prism.
Every such path uses an odd, hence positive, number of vertical edges.

### Proposition 8 (upper-colour defect ledger)

The upper vertices of all `O_2(P)` are precisely

\[
                    (X\setminus x_i)\cup\{p,q\},    \tag{10.6}
\]

over all old lower vertices `x_i`; hence they enumerate every type-two
upper state exactly once.  The two boundary upper vertices of `O_0(P)` are
`y_0 p` and `y_(m-1) q`, all distinct.  Its internal upper vertices are

\[
                         y_i\cup y_{i+1},           \tag{10.7}
\]

and there are `(m-1) Cat_m` such occurrences.  The number of type-zero
upper targets is only

\[
 \binom{2m}{m+2}
   ={m(m-1)\over m+2}\operatorname {Cat}_m,
                                                               \tag{10.8}
\]

so the occurrence excess is exactly

\[
 (m-1)\operatorname {Cat}_m-\binom{2m}{m+2}=D.     \tag{10.9}
\]

The multiset (10.7) need not cover the type-zero layer, so its number of
repeated occurrences can be larger than `D` by exactly its number of holes.
This is why Proposition 7 is a lower-state decomposition, not yet a new
middle-level factor.

Indeed, the first and last unions along `O_2(P)` are `x_0 p q` and
`x_m p q`; every internal one is
`bar(y_i intersection y_(i-1)) p q=bar(x_i) p q`.  Along `O_0(P)`, the
two boundary unions and all internal unions are exactly those displayed
above.  Counting (10.7) and applying the Catalan ratio gives
(10.8)--(10.9).

If the residual `D` prism paths use the minimum one vertical edge each,
their upper-colour consumption is

\[
                    D\text{ type-two colours}
       \quad+\quad mD\text{ type-one colours}.      \tag{10.10}
\]

Since the whole type-one upper rectangle has `2m Cat_m` states, the outer
paths must then use

\[
 2m\operatorname {Cat}_m-mD
   =2\operatorname {Cat}_m+2D                     \tag{10.11}
\]

type-one colours.  Relative to (10.1), the exact minimum aggregate
rerouting ledger is therefore

\[
 \boxed{\ -D\text{ type-zero occurrences},\quad
          +2D\text{ type-one occurrences},\quad
          -D\text{ type-two occurrences}.\ }       \tag{10.12}
\]

This balance is exact: the redundant type-zero mass in (10.9) equals the
vertical mass required by the residual prism.  But (10.12) cannot be
implemented by merely relabelling upper edges.  Edge type is determined by
the types of its lower endpoints, so the completion must perform genuine
path splices through type-one connector states.

### The Catalan compression count

Before recombination, (10.2) comes with `2 Cat_m` tagged inherited segments

\[
                  (x_1t,x_2t,\ldots,x_{m-1}t),
                    \qquad t\in\{p,q\}.             \tag{10.13}
\]

Each has `m-1` vertices.  They must be recombined into `D` paths of `m+2`
vertices.  The number of components which must disappear is

\[
 h=2\operatorname {Cat}_m-D
   ={6\over m+2}\operatorname {Cat}_m,              \tag{10.14}
\]

and the exact mass identity is

\[
                         h(m-1)=3D.                 \tag{10.15}
\]

Thus, in a donor-segment implementation, the `h` eliminated segments carry
exactly three extra vertices for each of the `D` surviving paths.  Donor
segments may need many cuts individually, but (10.15) permits only
`O(Cat_m)` cuts in total.  That is sufficient for the desired
`O(H Cat_m)` halo bound; uniform bounded complexity path by path is stronger
than necessary.

The positive all-dimensional target is now concrete: construct a
colour-injective complementary-path factor of the prism (10.4), using one
vertical edge per path, while simultaneously realizing the outer ledger
(10.12) and covering every colour in (10.7)--(10.8).  A construction using
`O(Cat_m)` total splices would supply the missing Catalan seam absorber.

## 11. Canonical rank-transfer squares

The matching between redundant type-zero edges and prism rungs is actually
forced.  Index the internal old lower vertices by

\[
                \mathcal R=\{x_i(P):1\le i\le m-1\}.             \tag{11.1}
\]

For `x=x_i(P)`, define

\[
                         g(x)=y_{i-1}\cup y_i.                    \tag{11.2}
\]

The `O_0(P)` edge `y_(i-1)y_i` has type-zero colour `g(x)`, while the
vertical prism edge `x p--x q` has type-two colour `x p q`.  These four
lower states span the exact transfer square

\[
 y_{i-1}-y_i-x_iq-x_ip-y_{i-1}.                  \tag{11.3}
\]

Switching its opposite edges replaces one type-zero and one type-two colour
by the two type-one colours

\[
 y_{i-1}p,\ y_iq
 \quad\text{or}\quad
 y_{i-1}q,\ y_ip.                                  \tag{11.4}
\]

Thus every possible minimum rank transfer is indexed by one internal old
vertex; no bipartite matching between edges and rungs remains.

### Corollary 9 (fixed-outer type-zero criterion)

With the outer paths (10.1) fixed, their type-zero colours can be made
bijective by `D` switches of the form (11.3) if and only if

\[
                    g:\mathcal R\longrightarrow\binom X{m+2}
                                                               \tag{11.5}
\]

is surjective.  When it is, choose one retained representative in every
fibre of `g`; the complementary set `S` of internal vertices has size `D`,
and `S` is exactly the required set of transferred prism rungs.

### Proof

The multiset of type-zero colours is precisely the image multiset of `g`.
It has `|R|=(m-1) Cat_m` occurrences, while its target set has
`binom(2m,m+2)=|R|-D` elements.  Deleting `D` occurrences leaves every
target exactly once precisely when every target occurred initially.  In the
surjective case, retaining one point of each fibre and deleting every other
point does this, and the deleted points index the canonical squares (11.3).
QED.

After this reduction, the coupled positive theorem has only two parts:

1. find a complementary path factor of the punctured prism whose unique
   vertical edges are the prescribed set `S`; and
2. orient the squares (11.4) and choose the horizontal prism edges so that
   every tagged old upper state `y p,y q` occurs exactly once, while the
   endpoint connectivity returns to the complement matching.

The first is a prescribed-rung path-factor problem; the second is a
two-colour strand-routing problem.  They are coupled, but the old
type-zero/type-two matching ambiguity has disappeared completely.
